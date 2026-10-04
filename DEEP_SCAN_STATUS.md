# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **1484** (Main **682** + Historical **802**)
- Automatic queue still needing V2 verification: **422** (Main **133** + Historical **289**)
- Currently assigned to workers: **86** (Main **86** + Historical **0**)
- Bounded access-recovery retries still eligible: **208**
- Terminally dropped after failed scans: **1**
- Automatic queue pending and not yet assigned: **336**

## Worker lanes

### Worker A
- Current package: `worker-a-ecb01ee41905`
- Assigned unresolved records: **40**
  1. `link:https://doi.org/10.24425/gsm.2026.6006` — Strategic autonomy in practice: Ukraine’s critical raw materials, growth accounting and shift-share evidence, 2010–2023
  2. `link:https://doi.org/10.1016/j.erss.2026.104857` — From industrialization to industrial decarbonization: Divergent steel decarbonization pathways in South Korea and Germany
  3. `link:https://doi.org/10.1080/13563467.2026.2737132` — The geoeconomics of wholesale central bank digital currencies: great power rivalry
  4. `link:https://doi.org/10.24425/gsm.2026.6007` — Potential of critical raw materials of Slovakia
  5. `link:https://doi.org/10.1016/j.erss.2026.105005` — How energy dependence becomes domestically acceptable in European countries: Legitimation of Russian energy use during the Russia–Ukraine war
  6. `link:https://doi.org/10.1111/aepr.70032` — Comment on “Supply Chain Diversification and Industrial Policies to Strengthen Economic Security”
  7. `link:https://doi.org/10.1002/bse.71515` — Rewiring the Circular Economy Through AI‐Informed Pathways: Structural and Distributional Drivers of Environmental Outcomes in the European Union
  8. `link:https://doi.org/10.1002/ese3.70639` — Use of Hydrogen Energy Storage to Stabilize Solar Power Output With an Energy Efficiency Analysis for European Union Member Countries
  - … plus 32 more in the package manifest

### Worker B
- Current package: `worker-b-bd0c29ee0c20`
- Assigned unresolved records: **40**
  1. `link:https://doi.org/10.54648/eerr2026019` — Cybersecurity at the Borders: The EU’s Differentiated Approaches to Cyber Capacity Building in Its Neighbours — recovery attempt 2/3
  2. `link:https://doi.org/10.1177/20322844261446530` — Directive 2024/1226: A new EU response to sanctions breaches and circumvention — recovery attempt 2/3
  3. `link:https://doi.org/10.1016/j.econlet.2026.113217` — GVC participation and inflation in the European Union — recovery attempt 2/3
  4. `link:https://doi.org/10.30965/18763332-20262010` — Rethinking External Finance for Economic Growth in the Western Balkans: A Comparison with Central Eastern Europe — recovery attempt 2/3
  5. `link:https://doi.org/10.1163/15691497-20263012` — Global Gateway. The EU’s Competition in Latin America and the Caribbean — recovery attempt 2/3
  6. `link:https://doi.org/10.1002/sd.71203` — Advancing SDG 13 and Net‐Zero Emissions in Europe: The Role of Green Technology Innovation, Renewable Energy, Environmental Taxation and Trade Openness — recovery attempt 2/3
  7. `link:https://fiia.fi/en/publication/the-geopolitical-commission` — The Geopolitical Commission - FIIA - Finnish Institute of International Affairs — recovery attempt 2/3
  8. `link:https://doi.org/10.1002/sd.71514` — Revolutionizing Climate Action: Achieving SDG 13 Through the Lens of the Rule of Law, Green Technology Innovation, Renewable Energy, and Trade Openness — recovery attempt 2/3
  - … plus 32 more in the package manifest

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
