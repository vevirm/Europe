# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **3405** (Main **1485** + Historical **1920**)
- Automatic queue still needing V2 verification: **20** (Main **10** + Historical **10**)
- Currently assigned to workers: **20** (Main **10** + Historical **10**)
- Bounded access-recovery retries still eligible: **16**
- Dropped after three failed recovery passes (archived): **204**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **0**

## Worker lanes

### Worker A
- Current package: `worker-a-20261126T101915Z-8e1f435941d0`
- Assigned unresolved records: **3**
  1. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=b20bca19-e82f-11f1-b745-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Presidency Flash for the Working Party on Competitiveness and Growth (Internal Market) on 24-25 November 2026 - Publications Office of the EU — recovery attempt 2/3
  2. `historical:id:9f4d7ac5ea0babd5` — FDI screening mechanism will lead to “bedlam”, EU lawyers say – Global Competition Review - CELIS Institute — recovery attempt 2/3
  3. `link:https://news.google.com/rss/articles/CBMihAFBVV95cUxQbkF3U1dUMGY4ZkV6NDUtOUNQTXloME80UXFxTmg5cnd6c0ctRVhaQ25MZ1pzZHZSclZGWjN2WW1vNEZnZUlIamJMbWViZTM1WXF2VEltWFZEcVhvNVpISjhibm53Snc4NjNSZDhfb3BCMzAxcmtuZ3B2OGhndk9UbGVNYkc?oc=5` — European arms makers race to untangle supply chains from China and US — recovery attempt 2/3

### Worker B
- Current package: `worker-b-20261126T094455Z-b9e9dbd3f47a`
- Assigned unresolved records: **17**
  1. `historical:id:96158653b03a8479` — Why the EU will have an industrial policy - but not necessarily a good one
  2. `historical:id:8b019b94f9f2adac` — Irish Diplomacy in a Time of Crisis and the Evolution of a ‘European’ Diplomatic Service
  3. `historical:id:7cb90c9504537d1f` — The Transatlantic Trade and Investment Partnership - A long hard road to multilateralism?
  4. `historical:id:8de6f8561b6f52ef` — Lamfalussy was right - independence and interdependence in a monetary union | Bank for International Settlements
  5. `link:https://doi.org/10.1016/j.enpol.2026.115733` — Strategic autonomy and the energy transition: Rethinking Europe's geopolitical alignment — recovery attempt 2/3
  6. `link:https://doi.org/10.1080/09692290.2026.2762334` — Strategic regulatory engagement in multipolar value chains: contesting the EU Deforestation regulation in the Global South — recovery attempt 2/3
  7. `link:https://doi.org/10.1596/45879` — Closing the Energy Efficiency Gap: Unlocking Private-Sector Investment in Poland and Romania — recovery attempt 2/3
  8. `link:https://www.bruegel.org/sites/default/files/2026-11/WP%2031%202026.pdf` — Financing Europe’s satellite infrastructure — recovery attempt 2/3
  - … plus 9 more in the package manifest

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
