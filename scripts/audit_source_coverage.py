#!/usr/bin/env python3
"""Read-only source/rotation health summary of the last committed radar.json.

Use after a completed ordinary Radar scan, not on a run stopped in regression tests.
No network access; no scanner state or corpus modifications.
"""
from __future__ import annotations
import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def coverage_report(config: dict, radar: dict) -> str:
    configured = [s for s in config.get('institution_sources', []) if isinstance(s, dict)]
    diag = radar.get('scan_diagnostics') or {}
    attempts = diag.get('source_transport_attempts') or {}
    health = diag.get('source_transport_health') or {}
    state = radar.get('scan_state') or {}
    tried = Counter(str((r or {}).get('status', 'unknown')) for r in attempts.values() if isinstance(r, dict))
    lines = [
        'SOURCE COVERAGE — last saved Radar scan',
        'Scan completed: ' + str(radar.get('run_completed_at') or radar.get('last_updated') or 'unknown'),
        f'Institutional domains configured: {len(configured)}',
        f'Domains/routes attempted: {len(attempts)} (includes any independent API routes)',
        'Transport attempts: ' + ', '.join(f'{key}={tried[key]}' for key in sorted(tried)) if tried else 'Transport attempts: none recorded',
        f'Institution rotation cursor: {state.get("institution_cursor", "not reported")}',
        f'Institution full cycles: {(state.get("completed_cycles") or {}).get("institutions", "not reported")}',
        '',
        'Configured domains with unhealthy or missing most-recent transport:',
    ]
    issues = []
    for src in configured:
        domain = str(src.get('domain', '')).lower().removeprefix('www.')
        record = attempts.get(domain) or health.get(domain) or {}
        status = str(record.get('status') or record.get('last_status') or 'not yet attempted')
        if status not in ('ok', 'ok_empty'):
            issues.append(f'  {domain}: {status} — {record.get("note") or record.get("last_note") or "no diagnostic"}')
    lines.extend(issues or ['  none (for domains with recorded attempts)'])
    lines.extend(['', 'New/repair-target route checklist:'])
    for domain in ('consilium.europa.eu', 'oecd.org', 'chathamhouse.org', 'cordis.europa.eu', 'epo.org'):
        src = next((s for s in configured if s.get('domain') == domain), None)
        if not src:
            lines.append(f'  {domain}: not configured')
        else:
            record = attempts.get(domain) or health.get(domain) or {}
            status = record.get('status') or record.get('last_status') or 'awaiting first scan'
            lines.append(f'  {domain}: {status}')
    lines.extend(['', 'Low new-item yield can be genuine saturation. This report tests reachability, not relevance or admissions.'])
    return '\n'.join(lines)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--radar', type=Path, default=ROOT/'radar.json')
    ap.add_argument('--config', type=Path, default=ROOT/'radar_config.json')
    args = ap.parse_args()
    print(coverage_report(json.loads(args.config.read_text(encoding='utf-8')),
                          json.loads(args.radar.read_text(encoding='utf-8'))))


if __name__ == '__main__':
    main()
