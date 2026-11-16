# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **3151** (Main **1349** + Historical **1802**)
- Automatic queue still needing V2 verification: **20** (Main **17** + Historical **3**)
- Currently assigned to workers: **2** (Main **2** + Historical **0**)
- Bounded access-recovery retries still eligible: **20**
- Dropped after three failed recovery passes (archived): **188**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **18**

## Worker lanes

### Worker A
- Current package: `worker-a-20261116T073451Z-6b6ee5452681`
- Assigned unresolved records: **2**
  1. `link:https://doi.org/10.1080/14683849.2026.2752280` — From customs-union asymmetry to bounded co-management? Strategic autonomy and the CETA-plus free trade agreement alternative in EU–Türkiye trade governance — recovery attempt 2/3
  2. `link:https://data.consilium.europa.eu/doc/document/ST-13545-2026-INIT/en/pdf` — Changes in comparison to the Commission proposal, document ST 10094/26 + ADD1, are marked in bold for additions and in strikethrough for deletions. — recovery attempt 2/3

### Worker B
- Current package: `worker-b-20261116T070207Z-162cd0dae8a9`
- Assigned unresolved records: **0**

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
