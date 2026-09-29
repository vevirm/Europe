# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **660** (Main **481** + Historical **179**)
- Automatic queue still needing V2 verification: **965** (Main **153** + Historical **812**)
- Currently assigned to workers: **78** (Main **6** + Historical **72**)
- Bounded access-recovery retries still eligible: **181**
- Terminally dropped after failed scans: **0**
- Automatic queue pending and not yet assigned: **887**

## Worker lanes

### Worker A
- Current package: `worker-a-263494cb1fb0`
- Assigned unresolved records: **36**
  1. `historical:id:52ee9b435418d418` — Spillovers to the EU from US tariffs imposed on third countries – model-based simulations
  2. `historical:id:57350d1b81a67917` — Selective Industrial Policy for the EU Open Strategic Autonomy: the Role of Products' Relatedness
  3. `historical:id:67d42817310851ea` — Presentation of the paper : The European pilar of NATO - Institut Jacques Delors
  4. `historical:id:eb40900c031cf2f7` — Pending legislation 2014 - Business input to the screening exercise by vice-president Timmermans
  5. `historical:id:a98f78be76f69e69` — Over-dependencies in services: A blind spot in the EU economic security strategy? - Institut Jacques Delors
  6. `historical:id:9aed1fea861ced82` — Market analysis
  7. `historical:id:7d9119823a96094f` — Institut Jacques Delors - Background Paper : Energy Trends in Europe
  8. `historical:id:e934dfafdbba1834` — Institut Jacques Delors - An external strategy for European agriculture
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-60389f6094bf`
- Assigned unresolved records: **36**
  1. `historical:id:a33a7348262884f0` — Legal Convergence Through Soft Law? The EU–US Trade and Technology Council (TTC)
  2. `historical:id:31654575c0798757` — Global Greenhouse Gas Emissions: 1990-2022 and Preliminary 2023 Estimates
  3. `historical:id:0b734410a1aff56b` — A Geoeconomic Fix? European Industrial Policy on Semiconductors Amidst Global Competition
  4. `historical:id:228414398c910b57` — Strategic Autonomy in Security and Defence as an Impracticability? How the European Union’s Rhetoric Meets Reality
  5. `historical:id:3d6dca3dd8918ca5` — Looking for Resource Sovereignty in a Fragmenting Global Order: The EU’s Response to Critical Raw Materials Challenges
  6. `historical:id:4ee82ade88d10254` — EU Trade Policy in Light of a Fragmented Liberal International Order
  7. `historical:id:37cd926025b1714d` — EU Foreign Policy and the Fragmentation of the International Order: A Framework for Analysis
  8. `historical:id:ea967d90699d9808` — Belgium - Screening of Foreign Direct Investment - Annual Report 2023-2024 (30 September 2024) - CELIS Institute - Investment Screening | National Security | Competitiveness
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
