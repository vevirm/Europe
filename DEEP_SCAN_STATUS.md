# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **3151** (Main **1349** + Historical **1802**)
- Automatic queue still needing V2 verification: **95** (Main **56** + Historical **39**)
- Currently assigned to workers: **72** (Main **41** + Historical **31**)
- Bounded access-recovery retries still eligible: **20**
- Dropped after three failed recovery passes (archived): **188**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **23**

## Worker lanes

### Worker A
- Current package: `worker-a-20261119T111032Z-f58a62f556dc`
- Assigned unresolved records: **36**
  1. `link:https://data.consilium.europa.eu/doc/document/WK-14980-2026-INIT/en/pdf` — Handling and further distribution are under the sole responsibility of community members.
  2. `link:https://doi.org/10.1007/s10645-026-09478-w` — Impact of the US–China tariff war on the eurozone under Trump 2.0: an agent-based modelling approach
  3. `link:https://doi.org/10.1111/imig.70251` — Ideology and Utopia in the Governance of Migration: The Case of the 2024 Pact on Migration and Asylum and the Common European System for Returns
  4. `link:https://doi.org/10.1111/jcms.70191` — Assessing Norms Convergence and Divergence in EU–Latin American Trade Relations: The Cases of EU–Mexico and EU–Mercosur Negotiations
  5. `link:https://doi.org/10.1111/1477-8947.70105` — Due Diligence in Agribusiness, Natural Resource Governance, and Trade: Rethinking Voluntary Standards Under Sustainability Regulations
  6. `link:https://doi.org/10.1016/j.eist.2026.101220` — The security-sustainability nexus in innovation policy: Synergies, tensions and governance in a new era
  7. `link:https://www.cer.eu/sites/default/files/EV_CBAM_16.11.26.pdf` — Where extending the EU’s carbon border adjustment mechanism does – and does not – make sense
  8. `link:https://rhg.com/wp-content/uploads/2026/11/CIM_Global-Clean-Tech-Manufacturing-in-Q3-2026-1.pdf` — Clean Investment Monitor: Q3 2026 Update on Global Clean Technology Manufacturing
  - … plus 28 more in the package manifest

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
