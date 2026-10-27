# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **2722** (Main **1121** + Historical **1601**)
- Automatic queue still needing V2 verification: **13** (Main **11** + Historical **2**)
- Currently assigned to workers: **7** (Main **6** + Historical **1**)
- Bounded access-recovery retries still eligible: **8**
- Dropped after three failed recovery passes (archived): **174**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **6**

## Worker lanes

### Worker A
- Current package: `worker-a-20261027T175213Z-5a9685515802`
- Assigned unresolved records: **0**

### Worker B
- Current package: `worker-b-20261027T175216Z-d9afc5af0e51`
- Assigned unresolved records: **7**
  1. `link:https://doi.org/10.1515/ordo-2026-2012` — Towards a rule-bound EU transformation policy: Can Ordnungspolitik and industrial strategy be reconciled?
  2. `link:https://doi.org/10.1093/eurpub/ckag169.087` — G.2. Round Table: From call to action to delivery: scaling climate–health solutions across Europe
  3. `link:https://doi.org/10.1093/eurpub/ckag169.430` — P.7. Round Table: Building the foundation: Data governance and harmonisation for CVD and diabetes in Europe
  4. `link:https://doi.org/10.1177/16118944261490056` — An Offshore Financial Centre Inside Europe: Luxembourg, Taxation and European Economic Community (1960s–1970s)
  5. `link:https://doi.org/10.1093/eurpub/ckag169.883` — Governance, not technology: low-hanging fruits for AI readiness in Europe, a latent class analysis
  6. `link:https://doi.org/10.1016/j.ecolecon.2026.109266` — Europe at the crossroads: trading strategic autonomy for resilience under degrowth — recovery attempt 2/3
  7. `historical:id:e1abd351d9984dbd` — Christoph Herrmann and Mareike Hoffmann, Investment in the European Union: Competences, Structures, Responsibility and Policy - CELIS Institute - Investment Screening | National Security | Competitiveness — recovery attempt 3/3

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
