#!/usr/bin/env python3
"""Idempotent, audit-safe cleanup of terminal Deep Scan failures.

A failure budget is consumed only by recorded research attempts, never by ZIP issuance.
Completed work is kept; three failed recovery passes close the record as dropped, not
as a permanent manual-verification backlog. Old statuses migrate without changing the
retrieval history. Unfinished records with fewer passes retain their place in the queue.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from scripts.deep_scan_work_state import (
        ROOT, MAX_RECOVERY_ATTEMPTS, load_state, save_state, sync_verified,
        update_record_metadata, write_status_markdown,
    )
    from scripts.deep_read_works import pending, historical_pending, load_sidecar
except ModuleNotFoundError:
    from deep_scan_work_state import (  # type: ignore
        ROOT, MAX_RECOVERY_ATTEMPTS, load_state, save_state, sync_verified,
        update_record_metadata, write_status_markdown,
    )
    from deep_read_works import pending, historical_pending, load_sidecar  # type: ignore


def close_exhausted(state: dict, admission: dict, reader: dict) -> dict[str, int]:
    """Close only failed, unverified three-pass entries; never rewrite KEEP/REVIEW."""
    verified = {k for k, v in reader.get("records", {}).items()
                if isinstance(v, dict) and v.get("profile") == "deep-reader-v2-authoritative"}
    recs = state.get("records", {})
    decisions = admission.setdefault("records", {})
    migrated = admitted = orphan_assignments = prior_locks = 0
    for key, row in recs.items():
        if not isinstance(row, dict) or key in verified:
            continue
        attempt_count = int(row.get("recovery_attempts") or 0)
        if attempt_count < MAX_RECOVERY_ATTEMPTS:
            continue
        if row.get("status") not in {"needs_manual_verification", "dropped_after_3_failures", "deferred"}:
            continue  # never infer failure merely from an old counter on a live record
        if row.get("status") != "dropped_after_3_failures":
            row["closed_from_status"] = row["status"]
            row["status"] = "dropped_after_3_failures"
            migrated += 1
        row.setdefault("closed_at", row.get("manual_verification_since") or row.get("last_recovery_at") or "")
        row.setdefault("drop_reason", row.get("manual_verification_reason") or row.get("recovery_reason") or "Three recorded unsuccessful recovery attempts")
        decision = decisions.get(key)
        if not isinstance(decision, dict) or not decision.get("decision"):
            decisions[key] = {
                "decision": "drop_unverifiable", "target_strand": "",
                "reason_code": "EVIDENCE_ACCESS_FAILED_3X",
                "reason": "Dropped after three recorded unsuccessful Deep Scan recovery attempts; evidence inadequate for a defensible assessment.",
                "source": "deep_scan_queue_cleanup", "recovery_attempts": attempt_count,
                "corpus_scope": "historical" if key.startswith("historical:") else "main",
            }
            admitted += 1
        elif decision.get("decision") in {"keep", "review"}:
            raise ValueError(f"Conflicting authoritative admission on terminal recovery failure: {key}")

    # Stale previous_assigned lists are *not* live reservations. Keeping their
    # keys excluded from scheduling strands otherwise-eligible works forever.
    # Historical package membership is still preserved under state['packages'].
    active = set()
    for lane in state.get("lanes", {}).values():
        if not isinstance(lane, dict):
            continue
        original = lane.get("assigned", [])
        lane["assigned"] = [k for k in original if k in recs and recs[k].get("status") != "dropped_after_3_failures" and k not in verified]
        active.update(lane["assigned"])
        prior_locks += len(lane.get("previous_assigned", []))
        lane.pop("previous_assigned", None)
    for key, row in recs.items():
        if not isinstance(row, dict):
            continue
        if row.get("status") == "assigned" and key not in active:
            row["status"] = "pending"  # no live worker reservation
            row.pop("lane", None)
            orphan_assignments += 1
    return {"normalized_to_drop": migrated, "new_admission_drops": admitted,
            "released_stale_previous_reservations": prior_locks,
            "released_orphan_assigned_flags": orphan_assignments}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=ROOT)
    args = ap.parse_args()
    root = args.root
    state = load_state(root / "deep_scan_work_state.json")
    admission = json.loads((root / "admission_state.json").read_text(encoding="utf-8"))
    reader = load_sidecar(root / "reader_text.json")
    sync_verified(state, reader)
    old_admission = json.dumps(admission, sort_keys=True, ensure_ascii=False)
    metrics = close_exhausted(state, admission, reader)
    radar = json.loads((root / "radar.json").read_text(encoding="utf-8"))
    historical = json.loads((root / "historical" / "historical.json").read_text(encoding="utf-8"))
    items = pending(radar, reader) + historical_pending(historical, reader)
    for _, key, _, row, _ in items:
        update_record_metadata(state, key, row)
    save_state(state, root / "deep_scan_work_state.json")
    if json.dumps(admission, sort_keys=True, ensure_ascii=False) != old_admission:
        (root / "admission_state.json").write_text(json.dumps(admission, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_status_markdown(state, reader, [x[1] for x in items], root / "DEEP_SCAN_STATUS.md")
    counts = {
        "closed_3x": sum(1 for r in state["records"].values() if isinstance(r, dict) and r.get("status") == "dropped_after_3_failures"),
        "still_pending": sum(1 for _, k, _, _, _ in items if state["records"].get(k, {}).get("status") not in {"dropped_after_3_failures", "deferred", "needs_manual_verification"}),
    }
    print(json.dumps({**metrics, **counts}, indent=2))


if __name__ == "__main__":
    main()
