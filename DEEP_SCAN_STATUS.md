# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **3370** (Main **1468** + Historical **1902**)
- Automatic queue still needing V2 verification: **55** (Main **27** + Historical **28**)
- Currently assigned to workers: **53** (Main **26** + Historical **27**)
- Bounded access-recovery retries still eligible: **16**
- Dropped after three failed recovery passes (archived): **204**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **2**

## Worker lanes

### Worker A
- Current package: `worker-a-20261126T094434Z-5be00d3d1887`
- Assigned unresolved records: **36**
  1. `link:https://ecfr.eu/wp-content/uploads/2026/11/Cleaner-together-Why-energy-cooperation-is-vital-for-a-fossil-free-Europe.pdf` — Cleaner together: Why energy cooperation is vital for a fossil-free Europe – European Council on Foreign Relations
  2. `link:https://cdn.ceps.eu/2026/11/2027-17-ERCC-Offshore-solar.pdf` — Unlocking Europe’s offshore solar potential – CEPS
  3. `link:https://doi.org/10.1007/s10100-026-01046-6` — Ranking of EU member states based on sectoral adoption of artificial intelligence
  4. `link:https://doi.org/10.69473/iasr.2026.29.3.245` — European Union’s Strategic Posture in a Competitive World: Rethinking the Common Security and Defence Policy (CSDP) in the Age of Global Rivalry
  5. `link:https://doi.org/10.1080/10220461.2026.2761629` — EU role adaptation in Africa amid partner expectations: The Global Gateway in Angola, Cabo Verde and Mozambique
  6. `link:https://www.delorscentre.eu/en/policy-areas/security-foreign-policy-and-geo-economics` — Security, foreign policy, and geo-economics | Jacques Delors Centre
  7. `link:https://digital-strategy.ec.europa.eu/en/library/eu-action-plan-cybersecurity-and-artificial-intelligence` — EU Action Plan on Cybersecurity and Artificial Intelligence
  8. `link:https://rhg.com/wp-content/uploads/2026/11/Growing-Global-Demand-for-Sustainable-Aviation-Fuels.pdf` — Growing Global Demand for Sustainable Aviation Fuels
  - … plus 28 more in the package manifest

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
