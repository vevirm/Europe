#!/usr/bin/env python3
"""Persistent coordination state for parallel Deep Scan V2 worker lanes.

The authoritative verification itself still lives in reader_text.json / admission_state.json.
This file coordinates work assignment so multiple browsing-capable LLMs do not receive the
same queue head.  It also bounds access-recovery retries: a work whose identity is known but
whose substantive source remains inaccessible may receive at most three genuine Deep Scan
recovery passes before it is closed as dropped (with full audit history).
"""
from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_WORK_STATE = ROOT / "deep_scan_work_state.json"
PROFILE = "radar-deep-scan-work-state-v1"
DEFAULT_LANES = ("A", "B")
DEFAULT_LANE_SIZE = 36
MAX_RECOVERY_ATTEMPTS = 3
MAX_SCAN_PACKAGE_ATTEMPTS = 3
RETRY_INTERVAL = 12  # at most one retry per 12 historical/background slots while fresh history exists
TERMINAL_MANUAL_STATUSES = {"needs_manual_verification", "dropped_after_3_failures", "deferred"}  # legacy name; all are excluded from automatic queue


def utc_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def empty_state() -> dict[str, Any]:
    return {
        "version": 1,
        "profile": PROFILE,
        "updated_at": None,
        "lanes": {
            lane: {
                "target_size": DEFAULT_LANE_SIZE,
                "assigned": [],
                "current_package_id": "",
                "package_history": [],
            }
            for lane in DEFAULT_LANES
        },
        "records": {},
        "packages": {},
    }


def load_state(path: Path = DEFAULT_WORK_STATE) -> dict[str, Any]:
    if not path.exists():
        return empty_state()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValueError(f"Unreadable Deep Scan work state {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"Invalid Deep Scan work state root: {path}")
    data.setdefault("version", 1)
    data.setdefault("profile", PROFILE)
    data.setdefault("updated_at", None)
    lanes = data.setdefault("lanes", {})
    for lane in DEFAULT_LANES:
        row = lanes.setdefault(lane, {})
        row.setdefault("target_size", DEFAULT_LANE_SIZE)
        row.setdefault("assigned", [])
        row.setdefault("current_package_id", "")
        row.setdefault("package_history", [])
    data.setdefault("records", {})
    data.setdefault("packages", {})
    _backfill_scan_package_attempts(data)
    return data


def save_state(state: dict[str, Any], path: Path = DEFAULT_WORK_STATE) -> None:
    state["version"] = 1
    state["profile"] = PROFILE
    state["updated_at"] = utc_now()
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _unique(items: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for item in items:
        if item and item not in seen:
            seen.add(item)
            out.append(item)
    return out


def _is_historical(key: str) -> bool:
    return isinstance(key, str) and key.startswith("historical:")


def _attempt_count(row: dict[str, Any] | None) -> int:
    try:
        return max(0, int((row or {}).get("recovery_attempts") or 0))
    except (TypeError, ValueError):
        return 0


def _scan_package_attempt_count(row: dict[str, Any] | None) -> int:
    try:
        return max(0, int((row or {}).get("scan_package_attempts") or 0))
    except (TypeError, ValueError):
        return 0


def _backfill_scan_package_attempts(state: dict[str, Any]) -> None:
    """Infer per-record issuance counts from historical package membership."""
    memberships: dict[str, int] = {}
    for pkg in state.get("packages", {}).values():
        if not isinstance(pkg, dict):
            continue
        keys = {k for k in (pkg.get("record_keys") or []) if isinstance(k, str) and k}
        for key in keys:
            memberships[key] = memberships.get(key, 0) + 1
    for key, rec in state.get("records", {}).items():
        if not isinstance(rec, dict):
            continue
        inferred = max(_attempt_count(rec), memberships.get(key, 0))
        if inferred > _scan_package_attempt_count(rec):
            rec["scan_package_attempts"] = inferred


def sync_verified(state: dict[str, Any], reader: dict[str, Any]) -> None:
    """Mirror authoritative V2 completion into the human/audit coordination ledger."""
    records = state.setdefault("records", {})
    table = reader.get("records", {}) if isinstance(reader, dict) else {}
    verified = {
        key for key, row in table.items()
        if isinstance(row, dict) and row.get("profile") == "deep-reader-v2-authoritative"
    }
    for key in verified:
        entry = records.setdefault(key, {})
        entry["status"] = "verified"
        entry["verified_at"] = row_time = str(table[key].get("reader_text_written_at") or "")
        if not row_time:
            entry["verified_at"] = entry.get("verified_at") or utc_now()
        entry["verified_package_id"] = str(table[key].get("deep_scan_package_id") or entry.get("verified_package_id") or "")
    for lane_row in state.get("lanes", {}).values():
        assigned = lane_row.get("assigned", []) if isinstance(lane_row, dict) else []
        lane_row["assigned"] = [k for k in assigned if k not in verified]


def assigned_keys(state: dict[str, Any]) -> set[str]:
    out: set[str] = set()
    for lane_row in state.get("lanes", {}).values():
        if not isinstance(lane_row, dict):
            continue
        out.update(k for k in lane_row.get("assigned", []) if isinstance(k, str) and k)
    return out


def manual_verification_keys(state: dict[str, Any]) -> set[str]:
    """Closed records blocked from assignment (legacy function name retained).

    Completed three-pass failures are DROPPED, never a perpetual manual-work backlog.
    Older terminal statuses are blocked until the migration normalizes them.
    """
    return {
        key for key, row in state.get("records", {}).items()
        if isinstance(row, dict) and str(row.get("status") or "") in TERMINAL_MANUAL_STATUSES
    }


def deferred_keys(state: dict[str, Any]) -> set[str]:
    """Backward-compatible alias for terminal access-limited work."""
    return manual_verification_keys(state)


def assignment_blocked_keys(state: dict[str, Any]) -> set[str]:
    """Block only records whose *validated recovery* budget is exhausted.

    Appearing in a package does not mean that a worker returned a valid result.
    Earlier versions counted ZIP issuance as a real attempt, permanently freezing
    outstanding records after three package downloads despite no verified result.
    Preserve scan_package_attempts for audit and hard-pass annotation, but never
    use that counter alone to remove unfinished research from the worker queue.
    """
    return {
        key for key, row in state.get("records", {}).items()
        if isinstance(row, dict)
        and str(row.get("status") or "") != "verified"
        and _attempt_count(row) >= MAX_RECOVERY_ATTEMPTS
    }


def recovery_retry_keys(state: dict[str, Any]) -> set[str]:
    return {
        key for key, row in state.get("records", {}).items()
        if isinstance(row, dict)
        and str(row.get("status") or "") == "recovery_retry"
        and 0 < _attempt_count(row) < MAX_RECOVERY_ATTEMPTS
    }


def update_record_metadata(state: dict[str, Any], key: str, row: dict[str, Any]) -> None:
    """Keep enough non-semantic metadata to make the hands-on list usable."""
    rec = state.setdefault("records", {}).setdefault(key, {})
    title = str(row.get("title") or row.get("headline") or "").strip()
    source = str(row.get("source") or row.get("journal") or row.get("institution") or "").strip()
    date = str(row.get("date") or row.get("year") or "").strip()
    url = str(row.get("link") or row.get("url") or row.get("doi") or "").strip()
    if title:
        rec["title"] = title
    if source:
        rec["source_name"] = source
    if date:
        rec["date"] = date
    if url:
        rec["url"] = url
    rec["corpus_scope"] = "historical" if _is_historical(key) else "main"
    strand = str(row.get("strand") or "").strip().upper()
    if bool(row.get("must_deep_scan")) or str(row.get("deep_scan_priority") or "").strip().lower() == "must":
        rec["queue_priority"] = "must_scan"
    elif bool(row.get("deep_a_private_candidate")):
        rec["queue_priority"] = "private_strand_a"
    elif strand in {"A", "BOTH"}:
        rec["queue_priority"] = "strand_a"
    elif rec.get("queue_priority") in {"must_scan", "private_strand_a", "strand_a"}:
        # Metadata can be refreshed from a corrected/reclassified copy later. Do not keep
        # a stale A-priority tag if the row itself no longer identifies as Strand A.
        rec.pop("queue_priority", None)


def prioritize_pending_keys(state: dict[str, Any], pending_keys: list[str]) -> list[str]:
    """Schedule urgent Strand-A verification first while preserving retry safeguards.

    Fresh Main Radar evidence still outranks Historical work, but within each scope the
    queue now gives Strand A explicit priority. Ordinary public Strand-A discoveries come first so the normal scanner's high-confidence
    A evidence is verified as fast as possible. Private 24-minute Deep-A candidates follow
    immediately; both A queues stay ahead of other Main Radar work.
    Difficult access-recovery retries remain throttled exactly as before and therefore
    cannot monopolize worker capacity.
    """
    terminal = manual_verification_keys(state)
    blocked = assignment_blocked_keys(state)
    records = state.get("records", {}) if isinstance(state.get("records"), dict) else {}
    ordered = _unique([k for k in pending_keys if k not in terminal and k not in blocked])

    fresh_main_must: list[str] = []
    fresh_private_a: list[str] = []
    fresh_main_a: list[str] = []
    fresh_main_other: list[str] = []
    fresh_hist_must: list[str] = []
    fresh_hist_a: list[str] = []
    fresh_hist_other: list[str] = []
    must_retries: list[str] = []
    retries: list[str] = []
    for key in ordered:
        rec = records.get(key) if isinstance(records.get(key), dict) else {}
        attempts = _attempt_count(rec)
        status = str(rec.get("status") or "")
        # Issuing a ZIP is not an evidence-recovery attempt.  Putting every
        # previously packaged Main record in the retry tail can strand the
        # entire Main queue behind Historical work without any actual scan.
        is_retry = status == "recovery_retry" or attempts > 0
        priority = str(rec.get("queue_priority") or "")
        if is_retry:
            (must_retries if priority == "must_scan" else retries).append(key)
        elif _is_historical(key):
            if priority == "must_scan":
                fresh_hist_must.append(key)
            elif priority in {"private_strand_a", "strand_a"}:
                fresh_hist_a.append(key)
            else:
                fresh_hist_other.append(key)
        elif priority == "must_scan":
            fresh_main_must.append(key)
        elif priority == "private_strand_a":
            fresh_private_a.append(key)
        elif priority == "strand_a":
            fresh_main_a.append(key)
        else:
            fresh_main_other.append(key)

    # Prefer never-issued works within each priority group, then the oldest
    # outstanding issuance.  This prevents asking an operator to rescan the
    # same package while other equally important work has never been issued.
    def oldest_unfinished_first(keys: list[str]) -> list[str]:
        return sorted(keys, key=lambda key: (
            _scan_package_attempt_count(records.get(key)) > 0,
            str((records.get(key) or {}).get("last_scan_package_at") or ""),
        ))

    # Explicit must-scan records are deterministic operator requirements and therefore lead
    # the automatic queue. Main still remains ahead of ordinary Historical work.
    out = sum((oldest_unfinished_first(group) for group in (
        fresh_main_must, must_retries, fresh_main_a, fresh_private_a, fresh_main_other
    )), [])
    fresh_hist = sum((oldest_unfinished_first(group) for group in (
        fresh_hist_must, fresh_hist_a, fresh_hist_other
    )), [])
    retries = oldest_unfinished_first(retries)
    if fresh_hist:
        retry_idx = 0
        for start in range(0, len(fresh_hist), RETRY_INTERVAL - 1):
            out.extend(fresh_hist[start:start + RETRY_INTERVAL - 1])
            if retry_idx < len(retries):
                out.append(retries[retry_idx])
                retry_idx += 1
        out.extend(retries[retry_idx:])
    else:
        out.extend(retries)
    return _unique(out)


def fill_lane(
    state: dict[str, Any],
    lane: str,
    pending_keys: list[str],
    *,
    target_size: int = DEFAULT_LANE_SIZE,
) -> list[str]:
    """Reserve a new lane, respecting live reservations and unverified backlog.

    Only records in a currently occupied lane are in flight. Old individual
    `status=assigned` flags with no lane reservation do not make records
    permanently ineligible. Issuing a ZIP never exhausts a recovery attempt.
    """
    lane = lane.upper()
    if lane not in state.setdefault("lanes", {}):
        state["lanes"][lane] = {
            "target_size": target_size,
            "assigned": [],
            "current_package_id": "",
            "package_history": [],
        }
    lane_row = state["lanes"][lane]
    lane_row["target_size"] = int(target_size)
    terminal = manual_verification_keys(state)
    prioritized = prioritize_pending_keys(state, pending_keys)
    pending_set = set(prioritized)
    # A live reservation is the key's presence in a worker lane, not an old
    # per-record 'assigned' flag. Before this fix, an earlier prepare run
    # emptied the lane but left that flag behind, making the entire backlog
    # appear unassignable forever.
    in_flight = assigned_keys(state)
    # Reserve the previous contents of the other lane for the *entire* A/B
    # preparation run. Without this, Worker B can immediately select the 36
    # jobs Worker A just replaced, creating overlapping new scan packages.
    just_replaced = {
        key
        for row in state.get("lanes", {}).values()
        if isinstance(row, dict)
        for key in row.get("previous_assigned", [])
        if isinstance(key, str)
    }
    occupied = in_flight | terminal | just_replaced
    current: list[str] = []
    for key in prioritized:
        if key not in pending_set or key in occupied:
            continue
        current.append(key)
        if len(current) >= max(1, int(target_size)):
            break
    # When the previous lane still owns work and no new tasks are available,
    # do not lose that reservation. The caller will report no NEW assignments.
    if current:
        lane_row["previous_assigned"] = list(lane_row.get("assigned", []))
        lane_row["assigned"] = current
    else:
        lane_row["assigned"] = [
            key for key in lane_row.get("assigned", [])
            if key in pending_set and key not in terminal
        ]
    for key in current:
        rec = state.setdefault("records", {}).setdefault(key, {})
        rec["status"] = "assigned"
        rec["lane"] = lane
        rec.setdefault("assigned_at", utc_now())
    return current


def register_package(state: dict[str, Any], lane: str, package_id: str, record_keys: list[str]) -> None:
    lane = lane.upper()
    now = utc_now()
    state.setdefault("packages", {})[package_id] = {
        "lane": lane,
        "created_at": now,
        "record_keys": list(record_keys),
    }
    lane_row = state.setdefault("lanes", {}).setdefault(lane, {})
    lane_row["current_package_id"] = package_id
    hist = lane_row.setdefault("package_history", [])
    if package_id not in hist:
        hist.append(package_id)
    lane_row["package_history"] = hist[-40:]
    for key in record_keys:
        rec = state.setdefault("records", {}).setdefault(key, {})
        rec["status"] = "assigned"
        rec["lane"] = lane
        rec["last_package_id"] = package_id
        rec["scan_package_attempts"] = _scan_package_attempt_count(rec) + 1
        rec["last_scan_package_at"] = now
        rec.setdefault("assigned_at", now)


def package_info(state: dict[str, Any], package_id: str) -> dict[str, Any] | None:
    row = state.get("packages", {}).get(package_id)
    return row if isinstance(row, dict) else None


def expected_remaining_for_package(
    state: dict[str, Any],
    package_id: str,
    reader: dict[str, Any],
) -> list[str] | None:
    pkg = package_info(state, package_id)
    if not pkg:
        return None
    verified = {
        key for key, row in reader.get("records", {}).items()
        if isinstance(row, dict) and row.get("profile") == "deep-reader-v2-authoritative"
    }
    terminal = manual_verification_keys(state)
    return [
        key for key in pkg.get("record_keys", [])
        if isinstance(key, str) and key not in verified and key not in terminal
    ]


def mark_verified(state: dict[str, Any], key: str, package_id: str, when: str | None = None) -> None:
    when = when or utc_now()
    rec = state.setdefault("records", {}).setdefault(key, {})
    lane = rec.get("lane")
    rec.update({
        "status": "verified",
        "verified_at": when,
        "verified_package_id": package_id,
    })
    if lane in state.get("lanes", {}):
        state["lanes"][lane]["assigned"] = [k for k in state["lanes"][lane].get("assigned", []) if k != key]


def mark_recovery_failure(
    state: dict[str, Any],
    key: str,
    package_id: str,
    *,
    reason: str,
    verification: dict[str, Any],
    when: str | None = None,
    max_attempts: int = MAX_RECOVERY_ATTEMPTS,
) -> str:
    """Record one *validated full recovery ladder* failure.

    Returns the new status.  Attempts 1-2 become ``recovery_retry``; attempt 3
    becomes ``dropped_after_3_failures`` and is never automatically assigned again.
    """
    when = when or utc_now()
    max_attempts = max(1, int(max_attempts))
    rec = state.setdefault("records", {}).setdefault(key, {})
    lane = rec.get("lane")
    # Re-importing a retained JSON is NOT a fresh research pass. One issued
    # package can charge a record at most once, even across separate imports.
    already_counted = any(
        isinstance(old, dict) and old.get("package_id") == package_id
        for old in (rec.get("recovery_history") or [])
    )
    if already_counted or _attempt_count(rec) >= max_attempts:
        return str(rec.get("status") or "recovery_retry")
    # Only a successfully validated defer consumes one of the three recovery
    # passes.  Merely shipping a record inside a ZIP must not consume a pass.
    attempts = min(max_attempts, _attempt_count(rec) + 1)
    history = rec.get("recovery_history") if isinstance(rec.get("recovery_history"), list) else []
    history = list(history)[-(max_attempts - 1):] if max_attempts > 1 else []
    history.append({
        "attempt": attempts,
        "package_id": package_id,
        "at": when,
        "reason": reason,
        "verification": verification,
    })
    terminal = attempts >= max_attempts
    rec.update({
        "status": "dropped_after_3_failures" if terminal else "recovery_retry",
        "recovery_attempts": attempts,
        "last_recovery_at": when,
        "last_recovery_package_id": package_id,
        "recovery_reason": reason,
        "verification": verification,
        "recovery_history": history,
    })
    if terminal:
        rec["closed_at"] = when
        rec["drop_reason"] = reason
    if lane in state.get("lanes", {}):
        state["lanes"][lane]["assigned"] = [k for k in state["lanes"][lane].get("assigned", []) if k != key]
    return str(rec["status"])


def mark_deferred(
    state: dict[str, Any],
    key: str,
    package_id: str,
    *,
    reason: str,
    verification: dict[str, Any],
    when: str | None = None,
) -> None:
    """Compatibility wrapper: a V2 ``defer`` now means one bounded recovery failure."""
    mark_recovery_failure(
        state, key, package_id, reason=reason, verification=verification, when=when
    )


def status_counts(state: dict[str, Any], reader: dict[str, Any], pending_keys: list[str]) -> dict[str, Any]:
    verified = {
        key for key, row in reader.get("records", {}).items()
        if isinstance(row, dict) and row.get("profile") == "deep-reader-v2-authoritative"
    }
    manual = manual_verification_keys(state)
    assigned = assigned_keys(state)
    queue = [k for k in _unique(pending_keys) if k not in manual]
    pending_main = [k for k in queue if not _is_historical(k)]
    pending_hist = [k for k in queue if _is_historical(k)]
    assigned = assigned & set(queue)
    assigned_main = {k for k in assigned if not _is_historical(k)}
    assigned_hist = {k for k in assigned if _is_historical(k)}
    retries = {k for k in queue if 0 < _attempt_count(state.get("records", {}).get(k)) < MAX_RECOVERY_ATTEMPTS}
    return {
        "verified": len(verified),
        "verified_main": len([k for k in verified if not _is_historical(k)]),
        "verified_historical": len([k for k in verified if _is_historical(k)]),
        "pending_total": len(queue),
        "pending_main": len(pending_main),
        "pending_historical": len(pending_hist),
        "assigned": len(assigned),
        "assigned_main": len(assigned_main),
        "assigned_historical": len(assigned_hist),
        "recovery_retries": len(retries),
        "manual_verification": len([k for k in manual if _attempt_count(state.get("records", {}).get(k)) < MAX_RECOVERY_ATTEMPTS]),
        "dropped_after_3_failures": len([k for k, r in state.get("records", {}).items() if isinstance(r, dict) and r.get("status") == "dropped_after_3_failures" and _attempt_count(r) >= MAX_RECOVERY_ATTEMPTS]),
        "unassigned_pending": len([k for k in queue if k not in assigned]),
    }


def _display_manual_row(key: str, row: dict[str, Any]) -> str:
    title = str(row.get("title") or "").strip() or key
    source = str(row.get("source_name") or "").strip()
    date = str(row.get("date") or "").strip()
    url = str(row.get("url") or "").strip()
    attempts = _attempt_count(row)
    attempt_text = f"{attempts}/{MAX_RECOVERY_ATTEMPTS}" if attempts else "legacy terminal"
    reason = str(row.get("manual_verification_reason") or row.get("defer_reason") or row.get("recovery_reason") or "substantive source access unresolved").strip()
    bits = [f"**{title}**", f"attempts: {attempt_text}"]
    if source:
        bits.append(source)
    if date:
        bits.append(date)
    bits.append(reason)
    if url:
        bits.append(url)
    return " — ".join(bits)


def write_dropped_audit(state: dict[str, Any], path: Path) -> None:
    """Compact, independently inspectable index; full per-route evidence remains in ledger."""
    dropped = []
    for key, rec in sorted(state.get("records", {}).items()):
        if not isinstance(rec, dict) or rec.get("status") != "dropped_after_3_failures":
            continue
        history = rec.get("recovery_history") if isinstance(rec.get("recovery_history"), list) else []
        dropped.append({
            "record_key": key,
            "title": rec.get("title", ""),
            "source": rec.get("source_name", ""),
            "url": rec.get("url", ""),
            "recovery_attempts_recorded": _attempt_count(rec),
            "recovery_history_entries_retained": len(history),
            "history_package_ids": [h.get("package_id", "") for h in history if isinstance(h, dict)],
            "closed_at": rec.get("closed_at") or rec.get("manual_verification_since") or rec.get("last_recovery_at") or "",
            "reason": rec.get("drop_reason") or rec.get("recovery_reason") or "",
        })
    audit = {
        "profile": "radar-deep-scan-dropped-index-v1",
        "rule": "After 3 recorded failed research passes, close as dropped; no hands-on queue. Package issuance alone is not a research pass.",
        "note": "The full retrieval notes and available recovery history remain in deep_scan_work_state.json. Some legacy records have fewer retained history entries than the recorded attempt counter; no missing attempts are invented.",
        "count": len(dropped),
        "records": dropped,
    }
    path.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_status_markdown(
    state: dict[str, Any],
    reader: dict[str, Any],
    pending_keys: list[str],
    path: Path,
) -> None:
    counts = status_counts(state, reader, pending_keys)
    lines = [
        "# Deep Scan V2 work status",
        "",
        "This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.",
        "It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.",
        "",
        "Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.",
        f"A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **{MAX_RECOVERY_ATTEMPTS}** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.",
        "",
        f"- Authoritative V2 verified: **{counts['verified']}** (Main **{counts['verified_main']}** + Historical **{counts['verified_historical']}**)",
        f"- Automatic queue still needing V2 verification: **{counts['pending_total']}** (Main **{counts['pending_main']}** + Historical **{counts['pending_historical']}**)",
        f"- Currently assigned to workers: **{counts['assigned']}** (Main **{counts['assigned_main']}** + Historical **{counts['assigned_historical']}**)",
        f"- Bounded access-recovery retries still eligible: **{counts['recovery_retries']}**",
        f"- Dropped after three failed recovery passes (archived): **{counts['dropped_after_3_failures']}**",
        f"- Legacy work-by-hand requiring reconciliation: **{counts['manual_verification']}**",
        f"- Automatic queue pending and not yet assigned: **{counts['unassigned_pending']}**",
        "",
        "## Worker lanes",
        "",
    ]
    for lane in sorted(state.get("lanes", {})):
        row = state["lanes"][lane]
        assigned = row.get("assigned", []) if isinstance(row, dict) else []
        lines.extend([
            f"### Worker {lane}",
            f"- Current package: `{row.get('current_package_id') or 'none'}`",
            f"- Assigned unresolved records: **{len(assigned)}**",
        ])
        if assigned:
            for i, key in enumerate(assigned[:8], 1):
                rec = state.get("records", {}).get(key, {})
                title = str(rec.get("title") or "").strip()
                suffix = f" — {title}" if title else ""
                attempts = _attempt_count(rec)
                retry = f" — recovery attempt {attempts + 1}/{MAX_RECOVERY_ATTEMPTS}" if attempts else ""
                lines.append(f"  {i}. `{key}`{suffix}{retry}")
            if len(assigned) > 8:
                lines.append(f"  - … plus {len(assigned) - 8} more in the package manifest")
        lines.append("")

    # Terminally dropped works must never be expanded into a perpetual hands-on list.
    # An audit index is generated next to the status file; all detailed evidence
    # remains unchanged in the authoritative state ledger.
    write_dropped_audit(state, path.parent / "DEEP_SCAN_DROPPED.json")
    lines.extend([
        "## Closure policy",
        "",
        "Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and",
        "`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.",
        "The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.",
        "Records with fewer than three documented completed attempts are not auto-dropped.",
        "",
    ])
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
