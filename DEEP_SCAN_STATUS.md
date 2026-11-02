# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **2834** (Main **1179** + Historical **1655**)
- Automatic queue still needing V2 verification: **8** (Main **7** + Historical **1**)
- Currently assigned to workers: **1** (Main **0** + Historical **1**)
- Bounded access-recovery retries still eligible: **7**
- Dropped after three failed recovery passes (archived): **185**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **7**

## Worker lanes

### Worker A
- Current package: `worker-a-20261102T152113Z-2b1cc2661e2a`
- Assigned unresolved records: **0**

### Worker B
- Current package: `worker-b-20261101T092736Z-c510784a458c`
- Assigned unresolved records: **1**
  1. `historical:id:8b6f795f74a8f736` — Trump's trade attack on China – who laughs last?

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
