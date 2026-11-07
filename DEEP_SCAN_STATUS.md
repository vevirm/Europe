# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **2921** (Main **1228** + Historical **1693**)
- Automatic queue still needing V2 verification: **69** (Main **33** + Historical **36**)
- Currently assigned to workers: **55** (Main **22** + Historical **33**)
- Bounded access-recovery retries still eligible: **13**
- Dropped after three failed recovery passes (archived): **185**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **14**

## Worker lanes

### Worker A
- Current package: `worker-a-20261107T111458Z-d011181d0b1a`
- Assigned unresolved records: **36**
  1. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=4f73242d-da2f-11f1-8501-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — WORKING PARTY ON COMPETITIVENESS AND GROWTH (Internal Market) - Publications Office of the EU
  2. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=dd4e8f89-d9bf-11f1-8501-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a Regulation of the European Parliament and of the Council on the European Union Agency for Cybersecurity (ENISA), the European cybersecurity certification framework, and ICT supply chain security and repealing Regulation (EU) 2019/881 (The Cybersecurity Act 2): Title IV: Security of ICT Supply Chains: Discussion paper - Publications Office of the EU
  3. `link:https://egmontinstitute.be/india-eu-strategic-partnership-still-a-long-way-to-go/` — India-EU Strategic Partnership, Still A Long Way To Go - Egmont Institute
  4. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=c764aab8-d9bf-11f1-8501-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a Regulation of European Parliament and of the Council on the European Union Agency for Cybersecurity (ENISA), the European cybersecurity certification framework, and ICT supply chain security and repealing Regulation (EU) 2019/881 (The Cybersecurity Act 2) - Presidency second compromise text Title IV (Security of ICT Supply Chains) - Publications Office of the EU
  5. `link:https://doi.org/10.1080/08911916.2026.2743824` — Beyond the European Chips Act: Mobilizing Public Banks to Solve Europe’s Semiconductor Supply Chain Paradox
  6. `link:https://doi.org/10.1787/58c3689d-en` — SME Policy Index for Western Balkans and Türkiye 2026 – Economy Profile for Serbia
  7. `link:https://doi.org/10.1016/j.tranpol.2026.104526` — Spatial spillover effects in European dry bulk ports
  8. `link:https://doi.org/10.1016/j.jmarsys.2026.104332` — Biological status and coastal resource management of Anadara tuberculosa in the Eastern Tropical Pacific
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-20261107T111515Z-8d31efbfd461`
- Assigned unresolved records: **19**
  1. `historical:id:df2bb6abfa96ee9d` — Europe’s economic security agenda needs far better techno-industrial intelligence
  2. `historical:id:fbce8a99bb2b2a58` — European Union: Current Trends in FDI Screening and Guidance for Investors – Global Competition Review - CELIS Institute
  3. `historical:id:852f535ffa5f4979` — Institut Jacques Delors - Climate, defence, sovereignty, competitiveness, purchasing power... Europeans in the middle of the road
  4. `historical:id:622b33b802c2719c` — Shields Up: How China, Europe, Japan and the United States Shape the World through Economic Security - Institut Jacques Delors
  5. `historical:id:672ded529bade43c` — Deciphering the EU-US Trade & Technology Council
  6. `historical:id:fb7a7f8c98b16455` — Bring Europe rapidly back on track for growth with an ambitious and effective long-term competitiveness strategy
  7. `historical:id:4703fe6176ca6a24` — Institut Jacques Delors - Building the strategic autonomy of Europe while global decoupling trends accelerate
  8. `historical:id:200a25e881c352f2` — Inflation, Sanctions and Debt Distress: the Economic Face of the Russo-Ukrainian War
  - … plus 11 more in the package manifest

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
