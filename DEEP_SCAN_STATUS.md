# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **1003** (Main **527** + Historical **476**)
- Automatic queue still needing V2 verification: **728** (Main **165** + Historical **563**)
- Currently assigned to workers: **78** (Main **6** + Historical **72**)
- Bounded access-recovery retries still eligible: **220**
- Terminally dropped after failed scans: **1**
- Automatic queue pending and not yet assigned: **650**

## Worker lanes

### Worker A
- Current package: `worker-a-3c304429875d`
- Assigned unresolved records: **36**
  1. `historical:id:7006a14c63116431` — A Conversation with Kyriakos Pierrakakis : Competitiveness, Investment and Resilience: Europe’s Economic Future in a Fragmented World - Institut Jacques Delors
  2. `historical:id:4a0cea8a5f3dab21` — Revisiting energy security in turbulent times - Egmont Institute
  3. `historical:id:a976e9a09aec9a79` — Gulliver Unchained? Europe’s Changing Relations with Oil and Gas Producers - Egmont Institute
  4. `historical:id:ae831ab770fead22` — EU Dependence on Russian gas: There is no short-term alternative - Egmont Institute
  5. `historical:id:622afe532fddcd84` — When stars align: Leveraging European defence budgets to drive a dual-use tech boom
  6. `historical:id:a6ede7b145800daa` — Reimagining European energy security: Towards a whole-of-system approach
  7. `historical:id:2911c35b8b8ffc22` — Playing games with energy security?
  8. `historical:id:249ca8b8cd62520e` — The US pause on LNG terminals will not put Europe at risk
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-a0e68cb2055f`
- Assigned unresolved records: **36**
  1. `historical:id:15a4aaa21e800f8b` — Fasten your seatbelts: How to manage China’s economic coercion
  2. `historical:id:d0da4842f39bdbb5` — Arm for the storm: Germany’s new security strategy – European Council on Foreign Relations
  3. `historical:id:8f33f16ed878a657` — Maritime container terminal infrastructure, network corporatization, and global terminal operators: Implications for international business policy
  4. `historical:id:73037cd02fa30791` — Saudi Arabia’s once marginal relationship with China has grown into a comprehensive strategic partnership
  5. `historical:id:09c656f173cb5cb4` — Green energy depends on critical minerals. Who controls the supply chains?
  6. `historical:id:eca6a3a49c50254c` — A Transatlantic Energy and Climate Pact Is Now More Necessary Than Ever
  7. `historical:id:dc1dfdcc7b9544ff` — The WMD Non-proliferation Clause in EU Trade Agreements
  8. `historical:id:a4030651b6a84432` — Bond villains: The European Central Bank’s new strategy – European Council on Foreign Relations
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

## Terminally dropped after failed scans

These records no longer consume automatic Deep Scan slots and are excluded from active reasoning after three failed attempts. Re-open one only by explicitly resetting its work-state entry after materially new evidence becomes available.

- `link:https://doi.org/10.1093/ser/mwag003` — **Green monetary transitions? Central banking and climate finance in Europe and China** — attempts: 3/3 — Socio-Economic Review — 2026-07-09 — Identity was verified, but substantive evidence remained inaccessible or too thin after the required recovery search. — https://doi.org/10.1093/ser/mwag003
