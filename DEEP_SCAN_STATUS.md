# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **336** (Main **336** + Historical **0**)
- Automatic queue still needing V2 verification: **1156** (Main **232** + Historical **924**)
- Currently assigned to workers: **78** (Main **78** + Historical **0**)
- Bounded access-recovery retries still eligible: **54**
- Terminally dropped after failed scans: **0**
- Automatic queue pending and not yet assigned: **1078**

## Worker lanes

### Worker A
- Current package: `worker-a-6fd90428172e`
- Assigned unresolved records: **36**
  1. `link:https://doi.org/10.1177/10245294261450371` — Disciplining venture capital? The remaking of innovation financing in the EU
  2. `link:https://doi.org/10.1177/10245294261443734` — What drives the Spanish deindustrialization? A subsystem approach
  3. `link:https://doi.org/10.1080/23745118.2026.2655143` — Competing visions: the impact of Franco-German narrative divergence on EU strategy
  4. `link:https://doi.org/10.1186/s43093-026-00945-z` — The effect of institutions on foreign direct investment: What matters most?
  5. `link:https://doi.org/10.1007/s11367-026-02643-y` — Evaluating social sustainability in European photovoltaic module supply chains through social life cycle assessment
  6. `link:https://op.europa.eu/o/opportal-service/download-handler?identifier=7d0241d4-b3d2-11f1-81de-01aa75ed71a1&format=pdf&language=en&productionSystem=cellar&part=` — R&I needs to reduce dependencies on critical raw materials through advanced materials in passenger vehicles - Publications Office of the EU
  7. `link:https://doi.org/10.1093/ia/iiag046` — The EU's Indo-Pacific strategic narratives: reception and perception gaps in Japan
  8. `link:https://doi.org/10.1007/s13132-026-03447-z` — Moral Economics: Human Capital, Gender Education and Foreign Direct Investment. Updated Empirical Results
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-4a5d0616dd2f`
- Assigned unresolved records: **36**
  1. `link:https://doi.org/10.1007/s11625-026-01872-2` — Leveraging change: a soft systems approach to transforming the EU food system
  2. `link:https://doi.org/10.1007/s11115-026-01001-8` — Failed Procurements as a Measure of Public Procurement Performance
  3. `link:https://doi.org/10.1016/j.future.2026.108672` — AI4EOSC: A federated cloud platform for Artificial Intelligence in scientific research
  4. `link:https://doi.org/10.1186/s41120-026-00188-w` — Real-time release testing: a review of global regulatory frameworks and application by the industry
  5. `link:https://doi.org/10.1016/j.ocecoaman.2026.108239` — Between giving and taking: unpacking EU sectoral support in African Sustainable Fisheries Partnership Agreements
  6. `link:https://news.google.com/rss/articles/CBMinwFBVV95cUxOd3Y2RWUwcjVhQjNwdC1hZ1JFT1ZuT1J5T29PR01OTXNldC1sOFdEeHJINTQzY043c3ZHUkNxNm9fV3hyb0lldFFBNzhUV0hqSnZlTUpwMGdqaTBIRFlmSDB0RVN0Njk3dndhblVnLUlVRWtrWDJwdVQzNGJJWW1NWHA0aHRKb2Y1aDZjM1B3ZmlvdEtvNmxhVWEtZ0hNaTQ?oc=5` — EU launches diplomatic offensive to stop Trump’s diesel export ban
  7. `link:https://borderlex.net/2026/09/23/eu-india-series-wine-and-spirits-tariff-cuts-come-with-limits/` — EU-India series: Wine and spirits tariff cuts come with limits - Borderlex - European trade policy
  8. `link:https://news.google.com/rss/articles/CBMisAFBVV95cUxNMnhFeHB1dlJzNUFaZkYzM0d3cFNyaDI3bFo3VjJFYW5wc0dhandneXlLVkstbVhfd0REaXJrUmx2TF9tRTd0QzdoTExocDNHSFhwVTlVRkZ6RzhKMU4yckMwNzEzS0xtalhQQl9vSkpBdjRxbUFVczFVc1NEQVJQM3R0NEdaQThjX0owTkdxbUcxb3JuM1c3XzNCVGN4dXV4OTNBeEQ3bURQWGxnRmdaVw?oc=5` — EU renews Russia sanctions, drops Russian billionaires Usmanov and Fridman
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
