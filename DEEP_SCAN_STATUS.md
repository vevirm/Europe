# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **2999** (Main **1264** + Historical **1735**)
- Automatic queue still needing V2 verification: **83** (Main **46** + Historical **37**)
- Currently assigned to workers: **71** (Main **34** + Historical **37**)
- Bounded access-recovery retries still eligible: **12**
- Dropped after three failed recovery passes (archived): **188**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **12**

## Worker lanes

### Worker A
- Current package: `worker-a-20261112T083924Z-f892969a7165`
- Assigned unresolved records: **36**
  1. `link:https://data.consilium.europa.eu/doc/document/ST-10476-2026-ADD-23-REV-1/en/pdf` — It concerns corrections in some figures.
  2. `link:https://doi.org/10.1017/nie.2026.10107` — ECONOMIC SECURITY STRATEGY AS A COMPONENT OF THE NATIONAL SECURITY STRATEGY: OBJECTIVES, INDICATORS AND INSTRUMENTS OF IMPLEMENTATION
  3. `link:https://joint-research-centre.ec.europa.eu/scientific-activities/economic-security-trade-foreign-investment-and-global-value-chains_en` — Economic Security: Trade, Foreign Investment and Global Value Chains
  4. `link:https://doi.org/10.1016/j.fufo.2026.101250` — Seaweed Traceability of Geographic Origin and Detection of Species-Mislabeling: Trends, Methods, Challenges, and Implications for the EU Industry
  5. `link:https://celis.institute/the-devil-is-still-in-the-details-the-annual-screening-report-2026-celis-edition/#download-pdf` — The Devil Is Still in the Details – The Annual Screening Report, 2026 CELIS Edition - CELIS Institute
  6. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=1d08d46d-dc23-11f1-8501-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a Regulation on establishing a framework of measures for accelerating industrial capacity and decarbonisation in strategic sectors (Industrial Accelerator Act) -Guidance for further work - Publications Office of the EU
  7. `link:https://institutdelors.eu/en/publications/us-mid-term-elections-what-are-the-implications-for-europe/` — US mid-term elections: what are the implications for Europe? - Institut Jacques Delors
  8. `link:https://www.eib.org/files/publications/20260192-091126-eib-group-investment-survey-2026-eu-overview-en.pdf` — EIB Group Investment Survey 2026 – European Union overview
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-20261112T083933Z-0ed9895e9bb7`
- Assigned unresolved records: **35**
  1. `historical:id:2184954833889def` — EU Sanctions and Investment Arbitration: An Attempt at Moving the Goalposts through Increased Securitisation? - CELIS Institute
  2. `historical:id:b6093870aea4eea5` — A pathway to Europe's Competitiveness: the clean transition. The essential brief
  3. `historical:id:5d0af4e6f227ccec` — Reinforcing the attractiveness of Europe’s Eastern Border Regions
  4. `historical:id:ab9facfe15150f32` — Towards The End Of Russian Oil And Gas In Europe? - CELIS Institute
  5. `historical:id:64e92926b0145efe` — Strategic solar module stockpiling in the EU: A scenario-based analysis of costs and benefits beyond 2030
  6. `historical:id:ac58e8c462b015b7` — Transatlantic Insecurity: Revaluation of Economic Security Policy’s Business Impacts Amid US-European Turbulence - CELIS Institute
  7. `historical:id:d4b334b725c426e9` — The EU’s Evolving Approach to Open Strategic Autonomy: a Critical Perspective on the Competitiveness Compass for the EU and Other Recent Policy Developments - CELIS Institute
  8. `historical:id:58bb36f2d81f883b` — EU-Mercosur trade agreement: now is the time
  - … plus 27 more in the package manifest

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
