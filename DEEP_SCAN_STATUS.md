# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **707** (Main **481** + Historical **226**)
- Automatic queue still needing V2 verification: **942** (Main **177** + Historical **765**)
- Currently assigned to workers: **78** (Main **30** + Historical **48**)
- Bounded access-recovery retries still eligible: **206**
- Terminally dropped after failed scans: **0**
- Automatic queue pending and not yet assigned: **864**

## Worker lanes

### Worker A
- Current package: `worker-a-7fb25109b0f5`
- Assigned unresolved records: **36**
  1. `link:https://dfrlab.org/2026/08/17/sovereignty-without-borders-decoding-the-transatlantic-digital-relationship-at-a-time-of-change/` — Sovereignty without borders: Decoding the transatlantic digital relationship at a time of change
  2. `link:https://ecfr.eu/wp-content/uploads/2026/09/Little-Venice-little-Sparta-The-UAEs-statecraft-meets-the-war-on-Iran-v2.pdf` — Little Venice, little Sparta: The UAE’s statecraft meets the war on Iran – European Council on Foreign Relations
  3. `link:https://doi.org/10.1177/01956574261473489` — Can Domestic Carbon Markets Buffer the Impact of EU Border Taxes? A Stochastic Frontier Analysis of Decarbonization Costs in India’s Energy-Intensive Industries
  4. `link:https://doi.org/10.4324/9781003669654-6` — Introducing Hydrogen to the European Energy Market
  5. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=35040186-bc4b-11f1-81de-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a Regulation of the European Parliament and of the Council on the European Union Agency for Cybersecurity (ENISA), the European cybersecurity certification framework, and ICT supply chain security and repealing Regulation (EU) 2019/881 (The Cybersecurity Act 2) - Explanatory note on Title IV (Security of ICT Supply Chains) - Publications Office of the EU
  6. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=21553fa5-bc4b-11f1-81de-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Proposal for a Regulation of the European Parliament and of the Council on the European Union Agency for Cybersecurity (ENISA), the European cybersecurity certification framework, and ICT supply chain security and repealing Regulation (EU) 2019/881 (The Cybersecurity Act 2) - Presidency first compromise text Title IV (Security of ICT Supply Chains) - Publications Office of the EU
  7. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=b26447fa-bc09-11f1-81de-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — Commission Proposal for a Regulation of the European Parliament and of the Council establishing diversification instrument to address critical strategic dependencies that expose the Union to economic security risks - Publications Office of the EU
  8. `link:https://doi.org/10.1016/j.rspp.2026.100336` — Divergent futures and structural change: Regional economic scenarios and resilience for trade shocks
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
