# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **557** (Main **479** + Historical **78**)
- Automatic queue still needing V2 verification: **1068** (Main **155** + Historical **913**)
- Currently assigned to workers: **78** (Main **8** + Historical **70**)
- Bounded access-recovery retries still eligible: **179**
- Terminally dropped after failed scans: **0**
- Automatic queue pending and not yet assigned: **990**

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
- Current package: `worker-b-e4f5ce344574`
- Assigned unresolved records: **36**
  1. `historical:id:2433c92388ae268b` — Mining for Europe's future: Critical raw materials, public attitudes and risks in enlargement partners
  2. `historical:id:0e3b1813e6c28103` — Centimanes v. Titans: right-wing populist governments’ treatment of foreign multinationals in East Central Europe
  3. `historical:id:9a02512190d6359b` — Out of Many, Many: Variation in East Central Europe Financial Governance Despite the EU's Single Market
  4. `historical:id:e7b6ff5842d21c18` — Transatlantic Approaches to Outbound Investment Screening
  5. `historical:id:2ecd9537efd7b69d` — The digital euro - anchoring Europe's strategic autonomy in a digital future | Bank for International Settlements
  6. `historical:id:83f1f6fff8bda2c1` — The European Union’s Economic Security Strategy Update
  7. `historical:id:f342875f1a3c6fd4` — Supply Chain Secondary Sanctions: How China Weaponised Lithuania's Trade Links - CELIS Institute - Investment Screening | National Security | Competitiveness
  8. `historical:id:b774f5d0aa10d3e3` — Nostalgia is a Broken Compass for Industrial Policy
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
