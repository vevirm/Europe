# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **2773** (Main **1151** + Historical **1622**)
- Automatic queue still needing V2 verification: **51** (Main **33** + Historical **18**)
- Currently assigned to workers: **51** (Main **33** + Historical **18**)
- Bounded access-recovery retries still eligible: **0**
- Dropped after three failed recovery passes (archived): **185**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **0**

## Worker lanes

### Worker A
- Current package: `worker-a-20261101T092722Z-b5e10cee9735`
- Assigned unresolved records: **36**
  1. `link:https://doi.org/10.1016/j.apenergy.2026.129040` — A systematic review of cross-sectoral life cycle assessments of carbon capture, utilization, and storage systems
  2. `link:https://www.atlanticcouncil.org/issue/technology-innovation/` — Technology & Innovation
  3. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=ab289355-d3aa-11f1-9458-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a Regulation of the European Parliament and of the Council on the European Union Agency for Cybersecurity (ENISA), the European cybersecurity certification framework, and ICT supply chain security and repealing Regulation (EU)2019/881 (The Cybersecurity Act 2) – Title II (ENISA) - Presentation by the Presidency - Publications Office of the EU
  4. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=edc102a9-d3b0-11f1-9458-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a Regulation of the European Parliament and of the Council on the European Union Agency for Cybersecurity (ENISA), the European cybersecurity certification framework, and ICT supply chain security and repealing Regulation (EU) 2019/881 (The Cybersecurity Act 2) – Title II (Fees), Articles 47 - Presentation by the Commission - Publications Office of the EU
  5. `link:https://doi.org/10.1017/err.2026.10171` — Governing the Unmeasured Load: Hyperscale Data Centres, Systemic Risk and the Assessment–Management Gap in EU Law
  6. `link:https://data.consilium.europa.eu/doc/document/ST-15118-2026-INIT/en/pdf` — Please note that the numbering of the Commission proposal remains unchanged until the end of negotiations.
  7. `link:https://cordis.europa.eu/search?q=contenttype='project' AND /project/relations/associations/relatedMasterCall/call/identifier='HORIZON-CL2-2025-01'&p=1&num=10&srt=Relevance:decreasing` — The European Union's Quest for a Relational Open Strategic Autonomy | QUEST | Project | Fact Sheet | HORIZON | CORDIS | European Commission
  8. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=716bcf01-d3e8-11f1-9458-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — WORKING PARTY ON COMPETITIVENESS AND GROWTH (Industry) (morning only) - Publications Office of the EU
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-20261101T092736Z-c510784a458c`
- Assigned unresolved records: **15**
  1. `historical:id:49d10cd2bd833c73` — Offensive strategy: The EU’s economic security – European Council on Foreign Relations
  2. `historical:id:c80a9af0a8393065` — Chinese Multinationals and Europe’s Geoeconomic Turn: The De‐Globalization of the Chinese ICT and Automotive Industry?
  3. `historical:id:4e9262a70ca2129c` — A maker, not a taker: Why Europe needs an economic security mechanism – European Council on Foreign Relations
  4. `historical:id:2bc644e26ffbd1e4` — Onwards and outwards: Why the EU needs to move from strategic autonomy to strategic interdependence – European Council on Foreign Relations
  5. `historical:id:a27d1d9b839e53bc` — Lessons from EU Space Programmes for Collective Defence
  6. `historical:id:7c60bc71a5c5be0c` — Russia’s Demise as an Energy Superpower
  7. `historical:id:5927691e8594f1fc` — Europe’s Security at Stake
  8. `historical:id:a3655168f4bb7453` — Europe’s new economic statecraft: A strong Anti-Coercion Instrument – European Council on Foreign Relations
  - … plus 7 more in the package manifest

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
