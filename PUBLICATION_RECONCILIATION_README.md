# Publication date correction reconciliation

## What changes

A Deep Scan **date correction crossing the current six-month boundary** changes the active publication route between Main Radar and Earlier Findings. The original scanner JSON files, source keys, and Deep Scan records are **never moved or overwritten**. Normal aging (without a date correction) does not cause a transfer.

The generated `publication_reconciliation.json` is a derived, reproducible routing view. It records both moved items and exceptions. Main Radar displays only approved (`keep`/`review`) moved items, consistent with its existing verification gate. The Earlier Findings page displays migrated Main Radar items, retaining the original record key in the routing view. The active-corpus rebuild uses the same routes for analytical inputs, so Shocks and other derived inference can be rebuilt with corrected grouping.

## Deploy

1. Deploy all files in this patch **together** to a test branch first. Do not upload the snapshot's `radar.json`, `historical/historical.json`, `admission_state.json`, or `reader_text.json` over newer live files.
2. Run `python scripts/reconcile_publication_dates.py` against the **current repository data**. Inspect `publication_reconciliation.json`, particularly `review`. Dates with incomplete precision and inactive/unapproved records do not transfer automatically.
3. Run `python -m unittest tests.test_publication_date_reconciliation tests.test_core_smoke`.
4. Run `python scripts/rebuild_active_radar.py --check-only` and inspect the report, then perform the standard live rebuild/retrace sequence when approved.
5. Publish after confirming both pages and the active rebuild; Deep Scan import now regenerates the routing file before rebuilding.

## Snapshot audit (2026-10-28)

- Eight approved historical records route to recent A/B.
- One approved Main Radar record routes to Earlier Findings.
- Fifty-six cases flagged (53 ambiguous dates; 3 not-approved). Some are partial-date corrections, not demonstrably misplaced records.

**Caution:** This patch addresses records with an *explicit Deep Scan corrected date* that crosses the cutoff. It does not attempt to detect every initial scanner date error, fix all fuzzy metadata dates, or alter the separate six-month discovery/retention policies. This snapshot is not guaranteed to match live GitHub state.
