# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **3335** (Main **1462** + Historical **1873**)
- Automatic queue still needing V2 verification: **73** (Main **16** + Historical **57**)
- Currently assigned to workers: **37** (Main **10** + Historical **27**)
- Bounded access-recovery retries still eligible: **17**
- Dropped after three failed recovery passes (archived): **204**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **36**

## Worker lanes

### Worker A
- Current package: `worker-a-20261125T115439Z-51684bd091f2`
- Assigned unresolved records: **36**
  1. `historical:id:4d3c6bfb26c04bac` — Energy security of the Slovak Republic in the context of the ongoing conflict in Ukraine
  2. `historical:id:58350f2d94b3ceb6` — Presentation of the report "The Road to a New European Automotive Strategy" - Institut Jacques Delors
  3. `historical:id:33f7cf5dcb286705` — Institut Jacques Delors - The EU support to Ukraine: from the sanction strategy to a strategic alliance?
  4. `historical:id:16fc2eedbfcd1124` — Commission proposes 2-year extension to EU Gas Storage Regulation
  5. `historical:id:afaca5d628a05c72` — A theory of economic coercion and fragmentation | Bank for International Settlements
  6. `historical:id:a555fa099057ec24` — Institut Jacques Delors - [FR] Euroquestions #55 | European foreign and defence policy put to the test by the war in Ukraine
  7. `historical:id:2998bd0bcb969fad` — GHG emissions, trade balance, and carbon leakage: Insights from modeling thirty-one European decarbonization pathways towards 2050
  8. `historical:id:599307ab190216a4` — Beyond Foreign Policy? EU Sanctions at the Intersection of Development, Trade, and CFSP
  - … plus 28 more in the package manifest

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
