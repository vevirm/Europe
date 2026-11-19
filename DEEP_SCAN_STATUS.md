# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **3184** (Main **1382** + Historical **1802**)
- Automatic queue still needing V2 verification: **62** (Main **23** + Historical **39**)
- Currently assigned to workers: **62** (Main **23** + Historical **39**)
- Bounded access-recovery retries still eligible: **23**
- Dropped after three failed recovery passes (archived): **188**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **0**

## Worker lanes

### Worker A
- Current package: `worker-a-20261119T123830Z-2bf2591b436e`
- Assigned unresolved records: **26**
  1. `historical:id:8f4a482461ab316a` — States, firms, and security: How private actors implement sanctions, lessons learned from the Netherlands
  2. `historical:id:568c10f15cb9cfc2` — The EU-Japan free trade agreement in evolving global trade politics
  3. `historical:id:d973a6232f08ea25` — Lithuania, Latvia and Estonia: Euro-Atlantic consolidation
  4. `historical:id:729a734abf1d8ced` — EU-Japan EPA a “Stumbling Block or a Stepping Stone” toward Multilateralism for Food and Beverages
  5. `historical:id:6662f2a2c5ad46e2` — EU Sanctions against Russia: A Punishment, a Signal of Displeasure or a Wild-Goose Chase
  6. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=c764aab8-d9bf-11f1-8501-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a Regulation of European Parliament and of the Council on the European Union Agency for Cybersecurity (ENISA), the European cybersecurity certification framework, and ICT supply chain security and repealing Regulation (EU) 2019/881 (The Cybersecurity Act 2) - Presidency second compromise text Title IV (Security of ICT Supply Chains) - Publications Office of the EU — recovery attempt 2/3
  7. `link:https://doi.org/10.1080/08911916.2026.2743824` — Beyond the European Chips Act: Mobilizing Public Banks to Solve Europe’s Semiconductor Supply Chain Paradox — recovery attempt 2/3
  8. `link:https://doi.org/10.1163/29505720-bja00020` — From CAI to De-Risking, Seven Years to Conclude, Four Months to Freeze — recovery attempt 2/3
  - … plus 18 more in the package manifest

### Worker B
- Current package: `worker-b-20261119T111044Z-e17d78dfa9d6`
- Assigned unresolved records: **36**
  1. `link:https://www.ispionline.it/en/publication/the-gulf-model-under-strain-re-equipping-states-to-manage-economic-and-security-disruptions-250748` — The Gulf Model Under Strain: Re-equipping States to Manage Economic and Security Disruptions | ISPI
  2. `link:https://data.consilium.europa.eu/doc/document/ST-13817-2026-INIT/en/pdf` — On 16 July 2025, the Commission transmitted its proposal for a Regulation on establishing the European Competitiveness Fund (ECF)1 to the European Parliament and to the Council.
  3. `link:https://doi.org/10.1787/b7b3852e-en` — The Economic Case for Pandemic Preparedness and Response: Beyond Lockdowns
  4. `historical:id:011a11a6a0c16391` — Europe’s strained social model
  5. `historical:id:70ba4db2287d4abd` — How geopolitics, geoeconomics, and new organizational models are changing the world of business
  6. `historical:id:0ea8860c247e6178` — Sovereign Rails, Dependent Stacks: Payment Infrastructure, Artificial Intelligence and Financial Sovereignty after 2022
  7. `historical:id:93263dec296e197e` — Where and when it pays: the economic value of solar and wind power placement in Europe
  8. `historical:id:8347e7a72bb1efc0` — The European Competitiveness Fund: a new logic for the EU budget?
  - … plus 28 more in the package manifest

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
