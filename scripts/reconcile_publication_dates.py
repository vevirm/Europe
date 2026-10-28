#!/usr/bin/env python3
"""Non-destructive, Deep-Scan-date-driven routing between Radar and Earlier Findings.

Scanner archives and Deep Scan IDs stay unchanged. Only explicit, valid date
corrections which cross the cutoff produce a route; normal aging never does.
"""
from __future__ import annotations
import argparse
import calendar
import copy
import datetime as dt
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from scripts.active_corpus import record_key, apply_correction, apply_deep_semantics, decision_for
from scripts.deep_read_works import historical_record_key


def parse_day(value):
    # Do not promote a year-only or month-only guess across a boundary.
    try:
        return dt.date.fromisoformat(str(value)) if isinstance(value, str) and len(value) == 10 else None
    except ValueError:
        return None


def month_cutoff(today):
    month = today.month - 6
    year = today.year
    while month <= 0:
        month += 12
        year -= 1
    return dt.date(year, month, min(today.day, calendar.monthrange(year, month)[1]))


def reconcile(radar, history, corrections, admission, reader, cutoff):
    changes = corrections.get('records', {})
    states = admission.get('records', {})
    reads = reader.get('records', {})
    recent, earlier, review = [], [], []
    # No automatic reassignment on mere aging: both dates must be known and
    # cross the same current cutoff. Unknown dates go to manual audit.
    sources = [('historical', x) for x in history.get('items', []) if isinstance(x, dict)]
    sources += [(section, x) for section in ('strand_a', 'strand_b', 'strand_c') for x in radar.get(section, []) if isinstance(x, dict)]
    active_main_keys = {record_key(x) for c in ('strand_a', 'strand_b', 'strand_c') for x in radar.get(c, []) if isinstance(x, dict)}
    active_historical_links = {str(x.get('url') or x.get('link') or '').strip().lower() for x in history.get('items', []) if isinstance(x, dict)}
    for source, raw in sources:
        key = historical_record_key(raw) if source == 'historical' else record_key(raw)
        correction = changes.get(key, {})
        fields = correction.get('fields', {}) if isinstance(correction, dict) else {}
        if not isinstance(fields, dict) or 'date' not in fields:
            continue
        old, new = parse_day(raw.get('date')), parse_day(fields['date'])
        if not old or not new:
            review.append({'key': key, 'reason': 'ambiguous_date', 'old': raw.get('date'), 'corrected': fields['date']})
            continue
        old_recent, new_recent = old >= cutoff, new >= cutoff
        if old_recent == new_recent:
            continue
        # An actual crossing is not enough: it has to have been on the wrong
        # side for its collection. Don't churn source identities on aging.
        if (source == 'historical' and not new_recent) or (source != 'historical' and new_recent):
            continue
        state = decision_for(key, admission)
        if state['decision'] not in ('keep', 'review'):
            review.append({'key': key, 'reason': 'not_approved', 'decision': state['decision']})
            continue
        row = apply_deep_semantics(apply_correction(raw, correction), reads.get(key))
        row['date'] = new.isoformat()
        row['year'] = new.year
        row['reconciled_from'] = source
        row['original_record_key'] = key
        row['admission_status'] = state['decision']
        if source == 'historical':
            row['link'] = row.get('link') or row.get('url')
            target = str(state.get('target_strand') or row.get('strand') or 'A').upper()
            if target not in ('A', 'B'):
                review.append({'key': key, 'reason': 'unsupported_recent_strand', 'strand': target})
                continue
            row['strand'] = target
            # If already collected independently by Main Radar, do not show twice.
            if record_key(row) in active_main_keys:
                review.append({'key': key, 'reason': 'already_in_main'})
                continue
            recent.append(row)
        else:
            link = str(row.get('url') or row.get('link') or '').strip().lower()
            if link and link in active_historical_links:
                review.append({'key': key, 'reason': 'already_in_earlier'})
                continue
            row['url'] = row.get('url') or row.get('link')
            row['id'] = 'reconciled-' + key.encode('utf-8').hex()[:36]
            earlier.append(row)
    return {'profile': 'publication-date-reconciliation-v1', 'cutoff': cutoff.isoformat(),
            'recent_from_earlier': recent, 'earlier_from_recent': earlier,
            'recent_from_earlier_keys': [r['original_record_key'] for r in recent],
            'earlier_from_recent_keys': [r['original_record_key'] for r in earlier],
            'review': review,
            'counts': {'recent_from_earlier': len(recent), 'earlier_from_recent': len(earlier), 'review': len(review)}}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root', type=Path, default=ROOT)
    ap.add_argument('--today', type=dt.date.fromisoformat, default=dt.datetime.now(dt.timezone.utc).date())
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()
    root = args.root
    def read(path): return json.loads((root / path).read_text(encoding='utf8'))
    result = reconcile(read('radar.json'), read('historical/historical.json'), read('record_corrections.json'), read('admission_state.json'), read('reader_text.json'), month_cutoff(args.today))
    destination = args.output or root / 'publication_reconciliation.json'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf8')
    print(json.dumps(result['counts']))

if __name__ == '__main__': main()
