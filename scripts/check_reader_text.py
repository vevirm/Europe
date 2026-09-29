#!/usr/bin/env python3
"""Validate the optional Deep Scan / reader_text.json sidecar only."""
import collections
import difflib
import json
import re
import sys
from pathlib import Path

SIDE = Path("reader_text.json")
MAX_REPEATS = 3
NEAR = 0.86
CAP = {"reader_title": 18, "reader_what": 20, "reader_why": 20}
MORE_CAP = 135
JARGON = [
    "bibliographic coupling", "citation burst", "change-point detection",
    "semantic shift", "dynamic topic model", "graph anomaly detection",
    "technology intelligence", "chokepoint", "admissibility-relevant", "selective conditionality",
    "the radar's hypothesis", "the radar's synthesis", "concrete action",
]


def clean(v):
    return re.sub(r"\s+", " ", str(v or "")).strip()

def validate_reader_text_entry(entry, why_count_before=0):
    """Validate one proposed reader-text entry without rescanning the whole sidecar."""
    fails = []
    if not isinstance(entry, dict):
        return ["entry is not an object"]

    if not clean(entry.get("source_hash")):
        fails.append("entry missing source_hash")

    for field, cap in CAP.items():
        value = clean(entry.get(field))
        if value and len(value.split()) > cap:
            fails.append(f"{field} over {cap} words: {value[:60]}")
        if value.endswith(("...", "…")):
            fails.append(f"{field} ends in ellipsis: {value[:60]}")
        for term in JARGON:
            if value and re.search(rf"\b{re.escape(term)}\b", value, re.I):
                fails.append(f"{field} uses '{term}': {value[:60]}")

    more = clean(entry.get("reader_more"))
    if more and len(more.split()) > MORE_CAP:
        fails.append(f"reader_more over {MORE_CAP} words")

    deep = entry.get("deep_analysis")
    if entry.get("profile", "").startswith("deep-reader"):
        if not isinstance(deep, dict):
            fails.append("deep-reader entry missing deep_analysis object")
        elif clean(deep.get("confidence")) not in {"high", "medium", "low"}:
            fails.append("deep_analysis confidence must be high/medium/low")
        if deep and not deep.get("why_supported", False) and clean(entry.get("reader_why")):
            fails.append("reader_why present although deep_analysis.why_supported is false")

    why = clean(entry.get("reader_why"))
    if why and why_count_before + 1 > MAX_REPEATS:
        fails.append(f"WHY repeats {why_count_before + 1} times: {why[:70]}")

    return fails



def validate_reader_text_doc(doc):
    """Return (failures, warnings, stats) using the exact CLI validation rules.

    Importers call this before committing an individual Deep Scan result so a bad
    reader-text field cannot abort the whole workflow after valid records were
    already marked complete.
    """
    records = doc.get("records", {}) if isinstance(doc, dict) else {}
    if not isinstance(records, dict):
        return ["sidecar records is not an object"], [], {"entries": 0, "whys": 0, "distinct_whys": 0}
    entries = [v for v in records.values() if isinstance(v, dict)]
    fails, warns = [], []
    whys = [clean(v.get("reader_why")) for v in entries if clean(v.get("reader_why"))]
    for text, n in collections.Counter(whys).items():
        if n > MAX_REPEATS:
            fails.append(f"WHY repeats {n} times: {text[:70]}")
    seen = []
    for w in whys:
        for prev in seen:
            if difflib.SequenceMatcher(None, w.lower(), prev.lower()).ratio() > NEAR:
                warns.append(f"WHY near duplicate: {w[:60]}")
                break
        seen.append(w)
    for v in entries:
        if not clean(v.get("source_hash")):
            fails.append("entry missing source_hash")
        for field, cap in CAP.items():
            text = clean(v.get(field))
            if text and len(text.split()) > cap:
                fails.append(f"{field} over {cap} words: {text[:60]}")
            if text.endswith(("...", "…")):
                fails.append(f"{field} ends in ellipsis: {text[:60]}")
            for term in JARGON:
                if text and re.search(rf"\b{re.escape(term)}\b", text, re.I):
                    fails.append(f"{field} uses '{term}': {text[:60]}")
        more = clean(v.get("reader_more"))
        if more and len(more.split()) > MORE_CAP:
            fails.append(f"reader_more over {MORE_CAP} words")
        deep = v.get("deep_analysis")
        if v.get("profile", "").startswith("deep-reader"):
            if not isinstance(deep, dict):
                fails.append("deep-reader entry missing deep_analysis object")
            elif clean(deep.get("confidence")) not in {"high", "medium", "low"}:
                fails.append("deep_analysis confidence must be high/medium/low")
            if deep and not deep.get("why_supported", False) and clean(v.get("reader_why")):
                fails.append("reader_why present although deep_analysis.why_supported is false")
    return fails, warns, {"entries": len(entries), "whys": len(whys), "distinct_whys": len(set(whys))}


def main():
    if not SIDE.exists():
        print("reader_text.json absent: Deep Scan layer is safely disabled")
        return
    doc = json.loads(SIDE.read_text(encoding="utf-8"))
    fails, warns, stats = validate_reader_text_doc(doc)
    print(f"reader entries {stats['entries']} | WHY {stats['whys']} | distinct WHY {stats['distinct_whys']}")
    for x in warns[:30]:
        print("warn:", x)
    for x in fails:
        print("FAIL:", x)
    print(f"{len(fails)} failures, {len(warns)} warnings")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
