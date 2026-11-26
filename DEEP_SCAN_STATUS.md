# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **3414** (Main **1488** + Historical **1926**)
- Automatic queue still needing V2 verification: **11** (Main **7** + Historical **4**)
- Currently assigned to workers: **8** (Main **5** + Historical **3**)
- Bounded access-recovery retries still eligible: **11**
- Dropped after three failed recovery passes (archived): **204**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **3**

## Worker lanes

### Worker A
- Current package: `worker-a-20261126T103925Z-4ba35afb15ec`
- Assigned unresolved records: **8**
  1. `link:https://doi.org/10.1016/j.enpol.2026.115733` — Strategic autonomy and the energy transition: Rethinking Europe's geopolitical alignment — recovery attempt 3/3
  2. `link:https://doi.org/10.1596/45879` — Closing the Energy Efficiency Gap: Unlocking Private-Sector Investment in Poland and Romania — recovery attempt 3/3
  3. `link:https://www.bruegel.org/sites/default/files/2026-11/WP%2031%202026.pdf` — Financing Europe’s satellite infrastructure — recovery attempt 3/3
  4. `link:https://news.google.com/rss/articles/CBMitgFBVV95cUxNT3ZFdlhYd2h1RFFxTHFXTnp2T3dnbDFSU19ib1hMVFVRaEVfXzBTT1RudWFSbFN0ZDdnMTAycjFqQmhrVkplN1MzMVcyaXdhNTREeURXZFVhdmpfNWM3dUFRTmxlZnkybXZIdkdIdjBxRGtoSGl1Ujl3MUdfSXBPbG5uZmlTOUwzWHRRNUhIYWpaMEM5QUhsdWhSM3dTZW5PU2dibFlJNV90bDVXclRUY1lra0dqdw?oc=5` — Germany Eyes EU Sanctions to Bar Russia From Hockey Championship — recovery attempt 3/3
  5. `link:https://www.bruegel.org/first-glance/moving-closer-eu-uk-economic-and-security-relationship` — Moving closer: the EU-UK economic and security relationship — recovery attempt 3/3
  6. `historical:id:0533a12327b52abd` — Financing Europe’s satellite infrastructure — recovery attempt 3/3
  7. `historical:id:9992a36ef024056b` — Macroeconomic policy and governance — recovery attempt 3/3
  8. `historical:id:d8ef449c89b45ea0` — Global economy and trade policy — recovery attempt 3/3

### Worker B
- Current package: `worker-b-20261126T094455Z-b9e9dbd3f47a`
- Assigned unresolved records: **0**

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
