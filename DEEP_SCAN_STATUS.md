# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **236** (Main **236** + Historical **0**)
- Automatic queue still needing V2 verification: **1075** (Main **318** + Historical **757**)
- Currently assigned to workers: **72** (Main **72** + Historical **0**)
- Bounded access-recovery retries still eligible: **2**
- Terminally dropped after failed scans: **0**
- Automatic queue pending and not yet assigned: **1003**

## Worker lanes

### Worker A
- Current package: `worker-a-1ae35096240e`
- Assigned unresolved records: **36**
  1. `link:https://doi.org/10.1177/2336825x261466891` — Ukraine and the transformation of French strategic imaginaries: The discursive reconfiguration of European strategic autonomy under the presidency of Emmanuel Macron (2017-2026)
  2. `link:https://doi.org/10.1093/hrlr/ngag015` — Finding a bridge between Erga Omnes obligations and WTO agreements: the case of human rights-based export controls on cyber-surveillance items
  3. `link:https://eur-lex.europa.eu/eli/reg/2021/821/oj/eng` — 2026 Update of the EU Control List of Dual-Use Items
  4. `link:https://doi.org/10.4324/9781003756637-13` — The EU-Japan Strategic Partnership Agreement (SPA)
  5. `link:https://doi.org/10.1080/09662839.2026.2700180` — Institutionalising defence production: reconceptualising the role of institutions and states in European defence industrial policy
  6. `link:https://doi.org/10.1177/17816858261489016` — European autonomy, competitiveness and security in the new space era
  7. `link:https://doi.org/10.1080/09662839.2026.2700178` — European arms production: A re-conceptualisation of the defence technological and industrial base, industrial policy and hybrid governance
  8. `link:https://doi.org/10.1186/s43093-026-00893-8` — Politics, power, and investment: geoeconomic determinants of FDI in CEE’s post-pandemic landscape
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-8e7eccd00b73`
- Assigned unresolved records: **36**
  1. `link:https://doi.org/10.17645/pag.12525` — The Politics of Procurement: Green Industrial Policy Through Non‐Price Criteria in European Offshore Wind Auctions
  2. `link:https://doi.org/10.1080/21582041.2026.2725729` — London’s stock exchange ten years after Brexit: from regulatory divergence to multi-channel geopolitics?
  3. `link:https://doi.org/10.1177/10245294261448607` — (S)tra(te)gic banking Europe’s geopolitical turn and the contradictory trajectory of TBTF banks
  4. `link:https://doi.org/10.1177/17816858261477419` — Defence readiness 2030: The industrial dimension
  5. `link:https://doi.org/10.1080/13501763.2026.2710717` — Promising security, delivering dependency: the material constraints of EU semiconductor collective securitisation
  6. `link:https://doi.org/10.1080/23745118.2026.2655142` — Exporting the European third way: strategic narratives of a value-based digital order
  7. `link:https://doi.org/10.1057/s41599-026-08829-x` — Unveiling the nexus between products and influential countries in the multi-layer trade network of global lithium battery
  8. `link:https://doi.org/10.1016/j.apenergy.2026.127884` — Multi-objective supply chain optimization of renewable energy carrier imports for Europe
  - … plus 28 more in the package manifest

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **8**
  1. `link:https://doi.org/10.1177/2336825x261466891` — Ukraine and the transformation of French strategic imaginaries: The discursive reconfiguration of European strategic autonomy under the presidency of Emmanuel Macron (2017-2026)
  2. `link:https://doi.org/10.1093/hrlr/ngag015` — Finding a bridge between Erga Omnes obligations and WTO agreements: the case of human rights-based export controls on cyber-surveillance items
  3. `link:https://eur-lex.europa.eu/eli/reg/2021/821/oj/eng` — 2026 Update of the EU Control List of Dual-Use Items
  4. `link:https://doi.org/10.4324/9781003756637-13` — The EU-Japan Strategic Partnership Agreement (SPA)
  5. `link:https://doi.org/10.1080/09662839.2026.2700180` — Institutionalising defence production: reconceptualising the role of institutions and states in European defence industrial policy
  6. `link:https://doi.org/10.1177/17816858261489016` — European autonomy, competitiveness and security in the new space era
  7. `link:https://doi.org/10.1080/09662839.2026.2700178` — European arms production: A re-conceptualisation of the defence technological and industrial base, industrial policy and hybrid governance
  8. `link:https://doi.org/10.1186/s43093-026-00893-8` — Politics, power, and investment: geoeconomic determinants of FDI in CEE’s post-pandemic landscape
