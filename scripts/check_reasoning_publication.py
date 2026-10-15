#!/usr/bin/env python3
"""Verify that the scheduled scan publishes freshly rebuilt reasoning in both JSON files.

This is a publication integrity check, not a generator or a requirement that every
run produce new findings. Zero new findings is valid if the analytical products
were successfully recomputed.
"""
import json
import os
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = ('high_order_inference', 'shock_inference')


def load(name):
    with (ROOT / name).open(encoding='utf-8') as fh:
        data = json.load(fh)
    if not isinstance(data, dict):
        raise ValueError(f'{name}: JSON root must be an object')
    return data


def parse_time(value, label):
    if not isinstance(value, str) or not value:
        raise ValueError(f'{label}: missing timestamp')
    try:
        timestamp = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError as exc:
        raise ValueError(f'{label}: invalid timestamp {value!r}') from exc
    if timestamp.tzinfo is None:
        raise ValueError(f'{label}: timestamp has no timezone')
    return timestamp.astimezone(timezone.utc)


def verify(raw, active):
    errors = []
    for name, data in (('radar.json', raw), ('radar_active.json', active)):
        try:
            scanned = parse_time(data.get('run_completed_at') or data.get('last_updated'), f'{name} scan')
            refresh = data.get('reader_products_refresh')
            if not isinstance(refresh, dict):
                raise ValueError(f'{name}: missing reader_products_refresh')
            refreshed = parse_time(refresh.get('completed_at'), f'{name} reader refresh')
            if abs((refreshed - scanned).total_seconds()) > 1800:
                errors.append(f'{name}: reasoning refresh is more than 30 minutes from scan time')
            for key in PRODUCTS:
                state = data.get(key)
                if not isinstance(state, dict):
                    errors.append(f'{name}: missing {key}')
                    continue
                evaluated = parse_time(state.get('evaluated_at'), f'{name} {key}')
                if abs((evaluated - refreshed).total_seconds()) > 1800:
                    errors.append(f'{name}: {key} is more than 30 minutes from active rebuild')
                if refresh.get(key) is not True:
                    errors.append(f'{name}: {key} refresh not confirmed')
                collection = 'candidates' if key == 'high_order_inference' else 'dynamic_shocks'
                if not isinstance(state.get(collection), list):
                    errors.append(f'{name}: {key}.{collection} missing or not a list')
        except ValueError as exc:
            errors.append(str(exc))

    for key in PRODUCTS:
        if raw.get(key) != active.get(key):
            errors.append(f'Published analytical product differs: {key}')
    return errors


def main():
    errors = verify(load('radar.json'), load('radar_active.json'))
    if errors:
        for err in errors:
            print('ERROR:', err)
        raise SystemExit(1)
    high = load('radar_active.json')['high_order_inference']
    shock = load('radar_active.json')['shock_inference']
    print('Reasoning publication OK:', len(high['candidates']), 'reasoning candidates,',
          len(shock['dynamic_shocks']), 'shock hypotheses. Counts are not quality guarantees.')
    data = load('radar_active.json')
    stats = data.get('stats') or {}
    lines = [
        '### Published analytical refresh',
        f"- Higher-order candidates: {len(high['candidates'])} (new this scan: {stats.get('high_order_candidates_new_this_run', 'unknown')}; updated: {stats.get('high_order_candidates_updated_this_run', 'unknown')})",
        f"- Shock hypotheses: {len(shock['dynamic_shocks'])} (new this scan: {stats.get('inferred_shocks_new_this_run', 'unknown')}; updated: {stats.get('inferred_shocks_updated_this_run', 'unknown')})",
        '- Both radar JSON publications matched at validation time.',
        '- Zero newly identified findings can be valid; it does not mean the scan was skipped.',
    ]
    summary = os.environ.get('GITHUB_STEP_SUMMARY')
    if summary:
        with open(summary, 'a', encoding='utf-8') as f:
            f.write('\n'.join(lines) + '\n')
    else:
        print('\n'.join(lines))


if __name__ == '__main__':
    main()
