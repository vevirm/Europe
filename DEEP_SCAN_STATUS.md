# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **3230** (Main **1390** + Historical **1840**)
- Automatic queue still needing V2 verification: **58** (Main **50** + Historical **8**)
- Currently assigned to workers: **22** (Main **18** + Historical **4**)
- Bounded access-recovery retries still eligible: **18**
- Dropped after three failed recovery passes (archived): **189**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **36**

## Worker lanes

### Worker A
- Current package: `worker-a-20261121T073919Z-780934f5aa64`
- Assigned unresolved records: **22**
  1. `link:https://data.consilium.europa.eu/doc/document/WK-16104-2026-INIT/en/pdf` — Handling and further distribution are under the sole responsibility of community members.
  2. `link:https://doi.org/10.1016/j.enpol.2026.115733` — Strategic autonomy and the energy transition: Rethinking Europe's geopolitical alignment
  3. `link:https://doi.org/10.1016/j.tej.2026.107579` — Energy crisis management in small isolated energy systems
  4. `link:https://borderlex.net/2026/11/20/tuna-origin-rules-split-industry-as-eu-thailand-talks-near-finish-line/` — Tuna origin rules split industry as EU-Thailand talks near finish line - Borderlex - European trade policy
  5. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=dd4e8f89-d9bf-11f1-8501-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a Regulation of the European Parliament and of the Council on the European Union Agency for Cybersecurity (ENISA), the European cybersecurity certification framework, and ICT supply chain security and repealing Regulation (EU) 2019/881 (The Cybersecurity Act 2): Title IV: Security of ICT Supply Chains: Discussion paper - Publications Office of the EU — recovery attempt 3/3
  6. `historical:id:b717036206691a04` — International finance and the geopolitics of market infrastructures — recovery attempt 2/3
  7. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=c764aab8-d9bf-11f1-8501-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a Regulation of European Parliament and of the Council on the European Union Agency for Cybersecurity (ENISA), the European cybersecurity certification framework, and ICT supply chain security and repealing Regulation (EU) 2019/881 (The Cybersecurity Act 2) - Presidency second compromise text Title IV (Security of ICT Supply Chains) - Publications Office of the EU — recovery attempt 3/3
  8. `link:https://doi.org/10.1080/08911916.2026.2743824` — Beyond the European Chips Act: Mobilizing Public Banks to Solve Europe’s Semiconductor Supply Chain Paradox — recovery attempt 3/3
  - … plus 14 more in the package manifest

### Worker B
- Current package: `worker-b-20261121T065040Z-ec94ffae757a`
- Assigned unresolved records: **0**

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
