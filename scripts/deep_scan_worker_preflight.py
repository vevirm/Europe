#!/usr/bin/env python3
"""Stand-alone, zero-dependency, fail-closed preflight bundled as CHECK_RESULTS.py.

Checks the worker result against its own manifest and supplied claims vocabulary.
Intended to catch common importer rejection causes *before* the result reaches inbox.
This does not verify that citations or substantive conclusions are true; that
remains the researcher's responsibility and the importer is authoritative.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
STEPS = {"supplied_url", "doi", "exact_title", "title_author_year", "official_publisher_or_repository", "broader_identity_search"}
SUCCESS = {"success", "found", "matched", "recovered", "resolved"}
UNFINISHED = {"not_verified", "pending", "unattempted", "skipped"}
DEPTHS = {"full_text_primary", "full_text_repository_copy", "official_full_document", "full_text_or_substantive_primary", "substantive_primary_after_recovery"}
CORRECT_FIELDS = {"title", "authors", "source", "date", "type", "eu_relevance", "text_mode", "source_text_mode", "event_status"}
UNSET_FIELDS = CORRECT_FIELDS | {"source_tier"}
JARGON = {"bibliographic coupling", "citation burst", "change-point detection", "semantic shift", "dynamic topic model", "graph anomaly detection", "technology intelligence", "chokepoint", "admissibility-relevant", "selective conditionality", "the radar's hypothesis", "the radar's synthesis", "concrete action"}
# Generic text is a sign of an unresearched placeholder, not source-grounded Deep Scan.
FILLER = ("the source describes ", "the matching source examines ", "potentially relevant to european economic-security", "provides evidence relevant to european strategic economic policy")


def clean(s):
    return re.sub(r"\s+", " ", str(s or "")).strip()


def norm(s):
    return clean(s).lower().replace("-", "_").replace(" ", "_")


def date_precision(s):
    s = clean(s)
    try:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", s):
            dt.date.fromisoformat(s)
            return "day"
        if re.fullmatch(r"\d{4}-\d{2}", s):
            dt.date.fromisoformat(s + "-01")
            return "month"
        if re.fullmatch(r"\d{4}", s) and 1 <= int(s) <= 9999:
            return "year"
    except ValueError:
        pass
    return None


def problems_for(row, job, vocab):
    problems = []
    if not isinstance(row, dict):
        return ["result must be a JSON object"]
    required = job.get("required_output", {})
    for field in ("record_key", "source_hash", "identity_hash"):
        if row.get(field) != required.get(field):
            problems.append(f"{field} does not match assigned job")
    v = row.get("verification") if isinstance(row.get("verification"), dict) else {}
    a = row.get("admission") if isinstance(row.get("admission"), dict) else {}
    deep = row.get("deep_analysis") if isinstance(row.get("deep_analysis"), dict) else {}
    dup = row.get("duplicate") if isinstance(row.get("duplicate"), dict) else {}
    corr = row.get("metadata_correction") if isinstance(row.get("metadata_correction"), dict) else {}
    decision = clean(a.get("decision")).lower()
    target = clean(a.get("target_strand")).upper()
    depth = clean(v.get("evidence_depth"))
    if decision not in {"keep", "review", "drop", "defer", "drop_unverifiable"}:
        problems.append("invalid admission.decision")
    if decision in {"keep", "review"} and target not in ({"A"} if job.get("corpus_scope") == "historical" else {"A", "C"}):
        problems.append("keep/review must target A or C (historical: A only)")
    if not re.fullmatch(r"[A-Z0-9_\-]{3,80}", clean(a.get("reason_code")).upper()):
        problems.append("invalid admission.reason_code")
    if len(clean(a.get("reason"))) < 12:
        problems.append("admission.reason requires a specific explanation")
    if len(clean(v.get("verification_note"))) < 12:
        problems.append("verification.verification_note too short")
    attempts_list = v.get("retrieval_attempts") if isinstance(v.get("retrieval_attempts"), list) else []
    attempts = {norm(item.get("step")): item for item in attempts_list if isinstance(item, dict) and clean(item.get("step"))}
    if "supplied_url" not in attempts:
        problems.append("missing supplied_url retrieval audit")
    access = job.get("automatic_scanner") if isinstance(job.get("automatic_scanner"), dict) else {}
    source_access = access.get("source_access") if isinstance(access.get("source_access"), dict) else {}
    scanner_route = bool(access.get("source_validation_url") or source_access.get("validation_url") or access.get("ep_document_pdf") or access.get("celex") or source_access.get("celex") or source_access.get("document_pdf"))
    steps = STEPS | ({"scanner_validation_route"} if scanner_route else set())
    used_sources = [s for s in (v.get("recovered_sources") or []) if isinstance(s, dict) and s.get("evidence_used") is True and clean(s.get("url")).startswith(("https://", "http://")) and clean(s.get("kind")) not in {"snippet", "search_result", "search_snippet"}]
    if decision in {"defer", "drop_unverifiable"} or depth == "substantive_primary_after_recovery":
        missing = steps - attempts.keys()
        if missing:
            problems.append(f"incomplete recovery ladder: {', '.join(sorted(missing))}")
        unfinished = sorted(s for s in steps & attempts.keys() if norm(attempts[s].get("outcome")) in UNFINISHED)
        if unfinished:
            problems.append(f"unfinished research (does NOT count as a genuine scan): {', '.join(unfinished)}")
        thin = sorted(s for s in steps & attempts.keys() if len(clean(attempts[s].get("note"))) < 12)
        if thin:
            problems.append(f"missing specific retrieval notes: {', '.join(thin)}")
        distinct_notes = {clean(attempts[s].get("note")).lower() for s in steps & attempts.keys()}
        if len(distinct_notes) < 4:
            problems.append("recovery notes are generic/repetitive; document real searches")
    if decision in {"keep", "review", "drop"}:
        if v.get("identity_verified") is not True or depth not in DEPTHS or not used_sources:
            problems.append("keep/review/drop requires verified identity, authoritative evidence_depth, and a substantive matching recovered source")
        supplied = attempts.get("supplied_url", {})
        if norm(supplied.get("outcome")) not in SUCCESS:
            if not any(norm(attempts.get(s, {}).get("outcome")) in SUCCESS for s in (steps - {"supplied_url"})):
                problems.append("supplied URL failed but no later successful recovery step is recorded")
    elif decision == "defer":
        if v.get("identity_verified") is not True or depth != "identity_only_after_recovery" or clean(a.get("reason_code")) != "EVIDENCE_ACCESS_LIMITED":
            problems.append("defer requires verified identity, identity_only_after_recovery and EVIDENCE_ACCESS_LIMITED")
        if corr.get("fields") or corr.get("unset"):
            problems.append("defer cannot have metadata corrections")
        if any(clean(row.get(k)) for k in ("reader_title", "reader_what", "reader_why", "reader_more")):
            problems.append("defer cannot have reader summaries")
        if any(clean(deep.get(k)) for k in ("work_kind", "research_question", "main_finding", "method_or_basis", "qualification", "radar_relevance")):
            problems.append("defer cannot have substantive deep_analysis")
    elif decision == "drop_unverifiable":
        if v.get("identity_verified") is not False or used_sources:
            problems.append("drop_unverifiable must have identity_verified=false and no substantive source")
        if any(norm(attempts.get(s, {}).get("outcome")) in SUCCESS for s in steps):
            problems.append("drop_unverifiable cannot claim successful source recovery")

    status = clean(dup.get("status")) or "unique"
    if status not in {"unique", "duplicate", "review"}:
        problems.append("invalid duplicate.status")
    if status == "duplicate":
        possible = {x.get("record_key") for x in job.get("possible_duplicates", []) if isinstance(x, dict)}
        if decision != "drop" or dup.get("duplicate_of") not in possible:
            problems.append("duplicate must be DROP and identify a supplied canonical record_key")
    elif clean(dup.get("duplicate_of")):
        problems.append("duplicate_of must be blank unless duplicate.status=duplicate")
    fields = corr.get("fields") if isinstance(corr.get("fields"), dict) else {}
    unset = corr.get("unset") if isinstance(corr.get("unset"), list) else []
    if set(fields) - CORRECT_FIELDS:
        problems.append("unsupported metadata_correction.fields: " + str(sorted(set(fields) - CORRECT_FIELDS)))
    if set(unset) - UNSET_FIELDS:
        problems.append("unsupported metadata_correction.unset: " + str(sorted(set(unset) - UNSET_FIELDS)))
    if (fields or unset) and (len(clean(corr.get("reason"))) < 12 or not used_sources):
        problems.append("metadata correction needs specific reason and substantive source")

    reader_caps = {"reader_title": 18, "reader_what": 20, "reader_why": 20, "reader_more": 135}
    for field, cap in reader_caps.items():
        val = clean(row.get(field))
        if val and len(val.split()) > cap:
            problems.append(f"{field} > {cap} words")
        if val.endswith(("...", "…")):
            problems.append(f"{field} ends with ellipsis")
        if field != "reader_more" and any(re.search(r"\b"+re.escape(t)+r"\b", val, flags=re.I) for t in JARGON):
            problems.append(f"{field} uses prohibited jargon")
        if decision in {"keep", "review"} and any(filler in val.lower() for filler in FILLER):
            problems.append(f"{field} appears to be a generic research placeholder")
    if clean(row.get("reader_why")) and deep.get("why_supported") is not True:
        problems.append("reader_why is present despite deep_analysis.why_supported=false")
    if clean(deep.get("confidence")) not in {"high", "medium", "low"}:
        problems.append("deep_analysis.confidence must be high/medium/low")
    if decision in {"keep", "review"}:
        for field in ("main_finding", "method_or_basis", "radar_relevance"):
            if len(clean(deep.get(field))) < 12:
                problems.append(f"deep_analysis.{field} lacks substantive source-based analysis")
        for field in ("main_finding", "radar_relevance"):
            if any(filler in clean(deep.get(field)).lower() for filler in FILLER):
                problems.append(f"deep_analysis.{field} appears to be a placeholder")

    claims = row.get("claims")
    if decision in {"keep", "review"}:
        if not isinstance(claims, list) or not 1 <= len(claims) <= 3:
            problems.append("keep/review requires 1–3 valid claims")
        else:
            for i, c in enumerate(claims):
                prefix = f"claims[{i}]"
                if not isinstance(c, dict):
                    problems.append(prefix + " must be a JSON object"); continue
                for field, voc in (("object", "objects"), ("mechanism", "mechanisms"), ("direction", "directions"), ("status", "statuses"), ("kind", "kinds"), ("confidence", "confidence")):
                    if clean(c.get(field)) not in vocab[voc]:
                        problems.append(f"{prefix}.{field} is not in claims_vocabulary.json: {c.get(field)!r}")
                secondary = c.get("secondary_objects")
                if not isinstance(secondary, list) or len(secondary) > 3 or any(s not in vocab["objects"] for s in secondary):
                    problems.append(f"{prefix}.secondary_objects invalid")
                actor = c.get("actor") if isinstance(c.get("actor"), dict) else {}
                if len(clean(actor.get("name"))) < 2 or clean(actor.get("class")) not in vocab["actor_classes"]:
                    problems.append(f"{prefix}.actor invalid")
                scope = c.get("scope") if isinstance(c.get("scope"), dict) else {}
                countries = scope.get("countries")
                level = clean(scope.get("level"))
                if level not in vocab["scopes"] or not isinstance(countries, list) or any(not clean(cc) for cc in countries) or (level in {"member_state", "associated_country"} and not countries):
                    problems.append(f"{prefix}.scope invalid")
                prec = date_precision(c.get("status_date"))
                declared = clean(c.get("status_date_precision"))
                if prec is None or (prec in {"month", "year"} and declared != prec) or (prec == "day" and declared not in {"", "day"}):
                    problems.append(f"{prefix}.status_date invalid (or missing status_date_precision)")
                if c.get("deadline") not in (None, "") and date_precision(c.get("deadline")) != "day":
                    problems.append(f"{prefix}.deadline requires YYYY-MM-DD")
                if len(clean(c.get("text"))) < 8:
                    problems.append(f"{prefix}.text missing substantive claim")
                if any(filler in clean(c.get("text")).lower() for filler in FILLER):
                    problems.append(f"{prefix}.text is an unverified generic placeholder")
                if not isinstance(c.get("qualification"), str):
                    problems.append(f"{prefix}.qualification must be text")
                if i == 0 and clean(c.get("qualification")) != clean(deep.get("qualification")):
                    problems.append("claims[0].qualification must exactly match deep_analysis.qualification")
                for owned in ("merit", "origin", "era", "provisional", "claim_id", "record_key"):
                    if owned in c:
                        problems.append(f"{prefix}.{owned} is importer-owned; omit")
    elif claims != []:
        problems.append(f"{decision} must have claims: []")
    return problems


def check_document(doc, jobs, manifest, vocab):
    errors = []
    if not isinstance(doc, dict):
        return ["result file must be a JSON object"]
    if doc.get("format") != "radar-deep-scan-results-v2" or doc.get("claims_format") != "radar-claims-v1" or doc.get("package_id") != manifest.get("package_id"):
        errors.append("format, claims_format or package_id mismatch")
    rows = doc.get("results")
    if not isinstance(rows, list) or not 1 <= len(rows) <= len(jobs):
        return errors + [f"results must be a nonempty consecutive prefix of at most {len(jobs)} jobs"]
    for i, row in enumerate(rows):
        for issue in problems_for(row, jobs[i], vocab):
            errors.append(f"result {i+1}/{len(rows)}: {issue}")
    # Prevent repository-wide repeated WHY errors when a worker repeats boilerplate.
    whys = [clean(r.get("reader_why")) for r in rows if isinstance(r, dict) and clean(r.get("reader_why"))]
    if len(whys) - len(set(whys)) >= 3:
        errors.append("reader_why is repeated too often within this submission")
    return errors


def load_context(root=ROOT):
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    jobs = []
    for batch in manifest["batches"]:
        jobs.extend(json.loads((root / batch["file"]).read_text(encoding="utf-8"))["jobs"])
    vocab = json.loads((root / "claims_vocabulary.json").read_text(encoding="utf-8"))
    if vocab.get("profile") != "radar-claims-vocabulary-v1":
        raise ValueError("unsupported vocabulary profile")
    return manifest, jobs, vocab


def main():
    parser = argparse.ArgumentParser(description="Strict preflight: refuses invalid Deep Scan worker outputs before upload")
    parser.add_argument("result_file", type=pathlib.Path)
    args = parser.parse_args()
    try:
        manifest, jobs, vocab = load_context()
        doc = json.loads(args.result_file.read_text(encoding="utf-8"))
        errors = check_document(doc, jobs, manifest, vocab)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        errors = [f"cannot check result: {exc}"]
    if errors:
        print(f"FAIL — NOT INBOX-READY: {len(errors)} problem(s)")
        for e in errors[:100]:
            print(" -", e)
        sys.exit(1)
    print(f"PASS — INBOX PREFLIGHT: {len(doc['results'])}/{len(jobs)} results; no detected structural/importer-rule errors")
    print("Note: source truth and GitHub work-state are only confirmed by authoritative importer.")


if __name__ == "__main__":
    main()
