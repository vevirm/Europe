# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **1073** (Main **527** + Historical **546**)
- Automatic queue still needing V2 verification: **667** (Main **174** + Historical **493**)
- Currently assigned to workers: **94** (Main **22** + Historical **72**)
- Bounded access-recovery retries still eligible: **222**
- Terminally dropped after failed scans: **1**
- Automatic queue pending and not yet assigned: **573**

## Worker lanes

### Worker A
- Current package: `worker-a-2ccf933cd725`
- Assigned unresolved records: **44**
  1. `link:https://doi.org/10.1080/13563467.2026.2737133` — From Pontes to Appia, but not to an Agorá: strategic hedging and infrastructural geoeconomics in the ECB's wCBDC initiative
  2. `link:https://ecipe.org/publications/6g-wake-up-call-for-europe/#_ftnref1` — The 6G Wake-up Call for Europe: Reforms Urgently Needed to Sustain Europe’s Telecommunications Leadership
  3. `link:https://doi.org/10.1016/j.lanepe.2026.101778` — Rebalancing innovation, affordability, and access for orphan drugs in the European Union
  4. `link:https://doi.org/10.1111/agec.70148` — The Impact of the EU Common Agricultural Policy on Regional Agricultural Productivity
  5. `link:https://doi.org/10.1016/j.crsus.2026.100836` — Interannual weather variability reshapes Europe’s cost-optimal hydrogen supply strategy
  6. `link:https://doi.org/10.1177/1087724x261471186` — Post-Brexit Import Control Infrastructure: Analysing the National Border Control Post Programme and its Impact on Ports Around Great Britain
  7. `link:https://doi.org/10.1080/00396338.2026.2730899` — Canada: Off the Menu?
  8. `historical:id:5ca9ab64874aebce` — Analysis of Developments in EU Capital Flows in the Global Context (2021) – CEPS
  - … plus 36 more in the package manifest

### Worker B
- Current package: `worker-b-4f3865965194`
- Assigned unresolved records: **44**
  1. `historical:id:7b65c4b7515137ac` — Europe’s energy security and EU-US cooperation
  2. `historical:id:c9edfa6b3626faa7` — EU: Three Russian banks and one technology company added to the frozen funds list as part of sanctions package - Global Trade Alert
  3. `historical:id:e2a628c87a06054e` — EU: Additional financial sanctions on Russia, including the exclusion of 7 banks from the SWIFT paying system - Global Trade Alert
  4. `historical:id:e2eec73b1db2c549` — EU discusses energy security with Japan
  5. `historical:id:209cab6667c84237` — EU Space Strategy for Security and Defence
  6. `historical:id:15db2f653fa8bcb3` — Declaration by the High Representative on behalf of the European Union on leaks in the Nord Stream gas pipelines
  7. `historical:id:23f72ce10b2dc494` — Balancing inflation, output and fiscal sustainability: policy responses to energy shocks
  8. `historical:id:ddb09e818241b367` — Agrifood trade and EU sanctions adopted further to the invasion of Ukraine by the Russian Federation and the support of Belarus to it
  - … plus 36 more in the package manifest

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
