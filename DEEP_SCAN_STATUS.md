# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **3217** (Main **1385** + Historical **1832**)
- Automatic queue still needing V2 verification: **28** (Main **19** + Historical **9**)
- Currently assigned to workers: **2** (Main **1** + Historical **1**)
- Bounded access-recovery retries still eligible: **23**
- Dropped after three failed recovery passes (archived): **189**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **26**

## Worker lanes

### Worker A
- Current package: `worker-a-20261119T124211Z-472cf5fb1605`
- Assigned unresolved records: **2**
  1. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=dd4e8f89-d9bf-11f1-8501-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a Regulation of the European Parliament and of the Council on the European Union Agency for Cybersecurity (ENISA), the European cybersecurity certification framework, and ICT supply chain security and repealing Regulation (EU) 2019/881 (The Cybersecurity Act 2): Title IV: Security of ICT Supply Chains: Discussion paper - Publications Office of the EU — recovery attempt 3/3
  2. `historical:id:b717036206691a04` — International finance and the geopolitics of market infrastructures — recovery attempt 2/3

### Worker B
- Current package: `worker-b-20261119T111044Z-e17d78dfa9d6`
- Assigned unresolved records: **0**

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
