# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **458** (Main **458** + Historical **0**)
- Automatic queue still needing V2 verification: **1111** (Main **153** + Historical **958**)
- Currently assigned to workers: **78** (Main **27** + Historical **51**)
- Bounded access-recovery retries still eligible: **132**
- Terminally dropped after failed scans: **0**
- Automatic queue pending and not yet assigned: **1033**

## Worker lanes

### Worker A
- Current package: `worker-a-8bd82ab3b71d`
- Assigned unresolved records: **36**
  1. `link:https://doi.org/10.1016/j.marpol.2026.107297` — Balancing blue growth and the ecosystem approach: policy coherence in Sweden’s Marine Spatial Plan for the Baltic Sea
  2. `link:https://doi.org/10.1163/22119000-bja10101` — Assessing the Barriers to the EU’s Green and Low-Carbon Hydrogen Imports
  3. `link:https://doi.org/10.1111/jcms.70168` — Migration Power Europe: Diplomacy, Crises and Power Struggles at the EU Periphery
  4. `link:https://doi.org/10.1016/j.accinf.2026.100791` — A new way to analyze ESG reports: A theme based model supported by AI
  5. `link:https://www.ispionline.it/wp-content/uploads/2026/09/ISPI-POLICY-PAPER-2026-ISPI-Study-for-AHK-Italien-2.pdf` — Under Pressure: Europe, Italy and Germany in a Weaponised Global Economy | ISPI
  6. `link:https://doi.org/10.1016/j.jimonfin.2026.103682` — Tax harmonization and the innovation–FDI trade-off: A quantitative analysis
  7. `link:https://www.businesseurope.eu/wp-content/uploads/2026/09/2026-09-28-Draft-Regional-Aid-Guidelines-Amendments-Reply-to-Commission-consultation.pdf` — Guidelines on regional state aid – Proposed amendments - BusinessEurope reply to the European Commission consultation
  8. `link:https://www.ispionline.it/wp-content/uploads/2026/09/ISPI-REPORT-2026-the-new-centrality-of-the-adriatic-sea-and-napa-in-the-age-of-fragmentation-2.pdf` — The New Centrality of the Adriatic Sea and NAPA in the Age of Fragmentation | ISPI
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-4eb7623e3b6c`
- Assigned unresolved records: **36**
  1. `historical:id:64f7d996c94f7cd1` — “Economic Security” Done Badly Will Make Us Less Economically Secure
  2. `historical:id:6d00e26535bd49ca` — Let’s Get Critical: Critical Minerals Mini Deals as Evolving Models of Trade Cooperation
  3. `historical:id:910592fe83ac1500` — The digital euro - strengthening Europe's payments ecosystem | Bank for International Settlements
  4. `historical:id:2433c92388ae268b` — Mining for Europe's future: Critical raw materials, public attitudes and risks in enlargement partners
  5. `historical:id:250a74bab8cf52ee` — How EU industrial policy got its groove back: securitisation and governance shifts in the geoeconomic era
  6. `historical:id:0e3b1813e6c28103` — Centimanes v. Titans: right-wing populist governments’ treatment of foreign multinationals in East Central Europe
  7. `historical:id:56f43b36e4bd7bd7` — A pivot or a saga? How Turkish foreign policy is torn between domestic pressures and economic needs – CEPS
  8. `historical:id:2b9abbfbed136d9d` — China and the EU-US rift + Economic security + Car imports from China
  - … plus 28 more in the package manifest

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **6**
  1. `link:https://doi.org/10.1177/2336825x261466891` — Ukraine and the transformation of French strategic imaginaries: The discursive reconfiguration of European strategic autonomy under the presidency of Emmanuel Macron (2017-2026) — recovery attempt 2/3
  2. `link:https://doi.org/10.1093/hrlr/ngag015` — Finding a bridge between Erga Omnes obligations and WTO agreements: the case of human rights-based export controls on cyber-surveillance items — recovery attempt 2/3
  3. `link:https://doi.org/10.4324/9781003756637-13` — The EU-Japan Strategic Partnership Agreement (SPA) — recovery attempt 2/3
  4. `link:https://doi.org/10.1080/09662839.2026.2700180` — Institutionalising defence production: reconceptualising the role of institutions and states in European defence industrial policy — recovery attempt 2/3
  5. `link:https://doi.org/10.1177/17816858261489016` — European autonomy, competitiveness and security in the new space era — recovery attempt 2/3
  6. `link:https://doi.org/10.1080/09662839.2026.2700178` — European arms production: A re-conceptualisation of the defence technological and industrial base, industrial policy and hybrid governance — recovery attempt 2/3
