# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **3305** (Main **1432** + Historical **1873**)
- Automatic queue still needing V2 verification: **11** (Main **6** + Historical **5**)
- Currently assigned to workers: **7** (Main **3** + Historical **4**)
- Bounded access-recovery retries still eligible: **11**
- Dropped after three failed recovery passes (archived): **204**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **4**

## Worker lanes

### Worker A
- Current package: `worker-a-20261123T072800Z-c35a7db7a44f`
- Assigned unresolved records: **7**
  1. `link:https://doi.org/10.1016/j.enpol.2026.115733` — Strategic autonomy and the energy transition: Rethinking Europe's geopolitical alignment — recovery attempt 2/3
  2. `link:https://doi.org/10.1080/09692290.2026.2762334` — Strategic regulatory engagement in multipolar value chains: contesting the EU Deforestation regulation in the Global South — recovery attempt 2/3
  3. `link:https://doi.org/10.1596/45879` — Closing the Energy Efficiency Gap: Unlocking Private-Sector Investment in Poland and Romania — recovery attempt 2/3
  4. `historical:id:0533a12327b52abd` — Financing Europe’s satellite infrastructure — recovery attempt 2/3
  5. `historical:id:9992a36ef024056b` — Macroeconomic policy and governance — recovery attempt 2/3
  6. `historical:id:d8ef449c89b45ea0` — Global economy and trade policy — recovery attempt 2/3
  7. `historical:id:e894b0783402fd6c` — Foreign Direct Investment Regimes Laws and Regulations Report 2025 Germany – ICLG.com - CELIS Institute — recovery attempt 2/3

### Worker B
- Current package: `worker-b-20261123T060949Z-6a4deb5cb704`
- Assigned unresolved records: **0**

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
