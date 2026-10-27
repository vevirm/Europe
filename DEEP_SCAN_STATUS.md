# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It shows what is verified, what each worker owns, and what is still eligible. Exhausted failures are closed, not work-by-hand.

Scheduling policy: preserve active worker reservations; fill new slots with Main Radar first, then Historical Radar. Do not fill packages artificially at saturation.
A validated unsuccessful recovery is one pass; packaging alone is not a pass. After **3** failed passes, close the work as **dropped**, keeping an audit. No work-by-hand loop.

- Authoritative V2 verified: **2705** (Main **1107** + Historical **1598**)
- Automatic queue still needing V2 verification: **33** (Main **25** + Historical **8**)
- Currently assigned to workers: **26** (Main **19** + Historical **7**)
- Bounded access-recovery retries still eligible: **11**
- Dropped after three failed recovery passes (archived): **171**
- Legacy work-by-hand requiring reconciliation: **0**
- Automatic queue pending and not yet assigned: **7**

## Worker lanes

### Worker A
- Current package: `worker-a-20261027T170445Z-e30dc563a099`
- Assigned unresolved records: **20**
  1. `link:https://www.cer.eu/sites/default/files/IB_Evidence_HofC_foreign_affair_committee_Russia_Oct26.pdf` — Evidence to the House of Commons Foreign Affairs Committee's Inquiry on Russia
  2. `link:https://www.businesseurope.eu/wp-content/uploads/2026/10/2026-10-27-Priorities-for-European-startups-and-scaleups.pdf` — Priorities for European startups and scaleups - a BusinessEurope position paper
  3. `link:https://institutdelors.eu/en/publications/made-in-europe-yet-another-missed-opportunity-in-the-mediterranean/` — ‘Made in Europe’: yet another missed opportunity in the Mediterranean - Institut Jacques Delors
  4. `link:https://merics.org/en/video/merics-media-briefing-xi-jinping-visits-usa` — MERICS Media Briefing: Xi Jinping visits the USA
  5. `link:https://data.consilium.europa.eu/doc/document/ST-13708-2026-INIT/en/pdf` — The aim is to establish harmonised conditions for disbursing public money with the purpose of strengthening the Union’s industrial capacity and thus reducing economic dependencies.
  6. `link:https://data.consilium.europa.eu/doc/document/ST-12886-2026-INIT/en/pdf` — EU competition rules have been part of the bedrock of the internal market from the outset.
  7. `link:https://link.epo.org/web/publications/studies/en-europes-technology-transfer-landscape.pdf` — From public research to market success: Europe’s tech transfer challenge
  8. `link:https://data.consilium.europa.eu/doc/document/ST-12236-2026-REV-1/en/pdf` — Changes in comparison to the first Presidency compromise texts included in documents ST 10817/26, 11237/26 and 11423/26 are marked in bold for additions and in strikethrough for deletions.
  - … plus 12 more in the package manifest

### Worker B
- Current package: `worker-b-20261026T115433Z-adc5978a6022`
- Assigned unresolved records: **6**
  1. `link:https://doi.org/10.1080/13563467.2026.2751107` — Globalised but divided: European corporations and the EU’s geoeconomic turn against China — recovery attempt 2/3
  2. `link:https://doi.org/10.1080/13563467.2026.2751104` — Chinese and Russian nuclear energy companies in Europe’s geoeconomic turn: giving way to the Americans? — recovery attempt 2/3
  3. `link:https://doi.org/10.1002/sd.71344` — Green Energy Transition and Sustainable Development Outcomes in Europe: Evidence of Threshold and Moderating Effects — recovery attempt 2/3
  4. `link:https://doi.org/10.1177/2336825x261466887` — EU policy towards the sahel in the “post-West” era — recovery attempt 2/3
  5. `link:https://doi.org/10.1080/23322969.2026.2751120` — Emerging research security approaches: organisational arrangements at three European universities — recovery attempt 2/3
  6. `historical:id:dfdf69eee6d7a0f4` — Supranational security states for national security problems: governing by rules & capacities in tech-driven security spaces — recovery attempt 2/3

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **0**

## Closure policy

Three unsuccessful recorded recovery attempts -> `dropped_after_3_failures` and
`admission_state.json: drop_unverifiable`; no further Deep Scan or manual-work queue.
The full attempt notes remain in `deep_scan_work_state.json`; see `DEEP_SCAN_DROPPED.json` for the compact index.
Records with fewer than three documented completed attempts are not auto-dropped.
