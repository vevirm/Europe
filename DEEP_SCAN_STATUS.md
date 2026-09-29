# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **588** (Main **479** + Historical **109**)
- Automatic queue still needing V2 verification: **1037** (Main **155** + Historical **882**)
- Currently assigned to workers: **78** (Main **8** + Historical **70**)
- Bounded access-recovery retries still eligible: **181**
- Terminally dropped after failed scans: **0**
- Automatic queue pending and not yet assigned: **959**

## Worker lanes

### Worker A
- Current package: `worker-a-6a3b91754c56`
- Assigned unresolved records: **36**
  1. `link:https://doi.org/10.1057/s41599-026-08607-9` — The obstacles and changes in Sino-European trade routes in the twenty-first century due to climate change and geopolitical risks
  2. `link:https://www.atlanticcouncil.org/wp-content/uploads/2026/07/beyond-the-corridor-imec-as-a-network-of-routes.pdf` — A network of corridors is the only reliable hedge against Middle East chokepoint disruptions
  3. `historical:id:b13d4236ef741b9f` — How and Why EU Institutions Promote the Digital Euro: The Politics of a Central Bank Digital Currency (CBDC)
  4. `historical:id:19f2d49289e7c3cd` — Thrown under the omnibus: How the EU’s digital deregulation fuels US coercion – European Council on Foreign Relations
  5. `historical:id:7a77d64ecea562f3` — The Supply Chain Disruption Survey: A new survey on knowledge flows in global supply chains - Kiel Institute
  6. `historical:id:fe87d58e76432253` — Belgium’s Second Annual FDI Screening Report: A Balance Between Openness and National Security - CELIS Institute - Investment Screening | National Security | Competitiveness
  7. `historical:id:3f6a6440696eb51d` — EU Data Sovereignty: An Autonomy–Interdependence Governance Gap?
  8. `historical:id:2e7d584322aa1076` — Preventing the Critical Minerals Crisis - Egmont Institute
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
