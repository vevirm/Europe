# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **624** (Main **481** + Historical **143**)
- Automatic queue still needing V2 verification: **1001** (Main **153** + Historical **848**)
- Currently assigned to workers: **78** (Main **6** + Historical **72**)
- Bounded access-recovery retries still eligible: **181**
- Terminally dropped after failed scans: **0**
- Automatic queue pending and not yet assigned: **923**

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
- Current package: `worker-b-cf8b3f0e0b5f`
- Assigned unresolved records: **36**
  1. `historical:id:f342875f1a3c6fd4` — Supply Chain Secondary Sanctions: How China Weaponised Lithuania's Trade Links - CELIS Institute - Investment Screening | National Security | Competitiveness
  2. `historical:id:40a6b5f31d319cbf` — Comparing Complements: The Concept of Foreign Subsidy Under The EU Foreign Subsidies Regulation In Light of EU State Aid Law and WTO Subsidy Law
  3. `historical:id:d5a511bb499c8787` — Policy Coherence in the Time of Economic Insecurity: Balancing the Sustainable Trade and Development Playbook of the New European Commission
  4. `historical:id:298747664b0b7e07` — Human Rights and Environmental Due Diligence Regulations for Deforestation‐Free Value Chains? Exploring the Implementation of the EU Regulation on Deforestation‐Free Products in the Cocoa and Coffee Sectors of Peru
  5. `historical:id:a59129e23f173be6` — Less food waste could bring lower EU food prices and decrease greenhouse gas emissions
  6. `historical:id:49366cd6741e9019` — Detecting Cybersecurity Threats in Digital Energy Systems Using Deep learning for Imbalanced Datasets
  7. `historical:id:0d88769ecda78716` — Dependent development under geopolitical reconfiguration: the Orbán regime in Hungary
  8. `historical:id:03d67ae8db1449d4` — Conference Report: BDI/CELIS German Chapter – Investment Screening Conference - CELIS Institute - Investment Screening | National Security | Competitiveness
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
