# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **2773** (Main **1151** + Historical **1622**)
- Automatic queue still needing V2 verification: **0** (Main **0** + Historical **0**)
- Currently assigned to workers: **0** (Main **0** + Historical **0**)
- Bounded access-recovery retries still eligible: **0**
- Dropped after three failed recovery passes (archived): **185**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **0**

## Worker lanes

### Worker A
- Current package: `worker-a-20261029T142048Z-ba895bb237cc`
- Assigned unresolved records: **0**

### Worker B
- Current package: `worker-b-20261029T141553Z-a6f415f8e42e`
- Assigned unresolved records: **0**

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
