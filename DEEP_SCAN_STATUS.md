# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **3064** (Main **1295** + Historical **1769**)
- Automatic queue still needing V2 verification: **18** (Main **15** + Historical **3**)
- Currently assigned to workers: **18** (Main **15** + Historical **3**)
- Bounded access-recovery retries still eligible: **18**
- Dropped after three failed recovery passes (archived): **188**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **0**

## Worker lanes

### Worker A
- Current package: `worker-a-20261112T091804Z-6ad6a1b7644f`
- Assigned unresolved records: **18**
  1. `link:https://doi.org/10.1080/23745118.2026.2758769` — Governing readiness: anticipatory defence governance in EU defence policy after 2022 — recovery attempt 3/3
  2. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=dd4e8f89-d9bf-11f1-8501-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a Regulation of the European Parliament and of the Council on the European Union Agency for Cybersecurity (ENISA), the European cybersecurity certification framework, and ICT supply chain security and repealing Regulation (EU) 2019/881 (The Cybersecurity Act 2): Title IV: Security of ICT Supply Chains: Discussion paper - Publications Office of the EU — recovery attempt 2/3
  3. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=c764aab8-d9bf-11f1-8501-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a Regulation of European Parliament and of the Council on the European Union Agency for Cybersecurity (ENISA), the European cybersecurity certification framework, and ICT supply chain security and repealing Regulation (EU) 2019/881 (The Cybersecurity Act 2) - Presidency second compromise text Title IV (Security of ICT Supply Chains) - Publications Office of the EU — recovery attempt 2/3
  4. `link:https://doi.org/10.1080/08911916.2026.2743824` — Beyond the European Chips Act: Mobilizing Public Banks to Solve Europe’s Semiconductor Supply Chain Paradox — recovery attempt 2/3
  5. `link:https://doi.org/10.1163/29505720-bja00020` — From CAI to De-Risking, Seven Years to Conclude, Four Months to Freeze — recovery attempt 2/3
  6. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=bd116d80-da2f-11f1-8501-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Presidency Flash for the Working Party on Competitiveness and Growth (Internal Market - Skills Portability) on 5 November 2026 - Publications Office of the EU — recovery attempt 2/3
  7. `link:https://doi.org/10.1016/j.esr.2026.102389` — Reassessing the EU’s LNG expansion strategy: Geopolitical dependencies, energy security, and climate goals after the Russian invasion of Ukraine — recovery attempt 2/3
  8. `link:https://doi.org/10.1080/10168737.2026.2692699` — European Manufacturing Exports and Exposure to Chinese ICT Services — recovery attempt 2/3
  - … plus 10 more in the package manifest

### Worker B
- Current package: `worker-b-20261112T083933Z-0ed9895e9bb7`
- Assigned unresolved records: **0**

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
