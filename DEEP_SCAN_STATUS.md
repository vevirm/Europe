# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **3370** (Main **1468** + Historical **1902**)
- Automatic queue still needing V2 verification: **38** (Main **10** + Historical **28**)
- Currently assigned to workers: **2** (Main **1** + Historical **1**)
- Bounded access-recovery retries still eligible: **16**
- Dropped after three failed recovery passes (archived): **204**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **36**

## Worker lanes

### Worker A
- Current package: `worker-a-20261125T120016Z-88d37e55ab59`
- Assigned unresolved records: **1**
  1. `historical:id:9f4d7ac5ea0babd5` — FDI screening mechanism will lead to “bedlam”, EU lawyers say – Global Competition Review - CELIS Institute — recovery attempt 2/3

### Worker B
- Current package: `worker-b-20261125T115449Z-8ef714219d30`
- Assigned unresolved records: **1**
  1. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=b20bca19-e82f-11f1-b745-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Presidency Flash for the Working Party on Competitiveness and Growth (Internal Market) on 24-25 November 2026 - Publications Office of the EU — recovery attempt 2/3

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
