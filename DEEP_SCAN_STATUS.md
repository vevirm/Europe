# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what has been terminally dropped after repeated failed scans.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` or rejected current-package scan return counts as a failed attempt. After **3** failed attempts, the record is terminally dropped from automatic scanning and active reasoning.

- Authoritative V2 verified: **303** (Main **303** + Historical **0**)
- Automatic queue still needing V2 verification: **1189** (Main **265** + Historical **924**)
- Currently assigned to workers: **82** (Main **82** + Historical **0**)
- Bounded access-recovery retries still eligible: **47**
- Terminally dropped after failed scans: **0**
- Automatic queue pending and not yet assigned: **1107**

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
- Current package: `worker-b-cae9f2e76bc3`
- Assigned unresolved records: **40**
  1. `link:https://www.businesseurope.eu/publications/security-and-defence-policy-needs-to-be-integrated-into-europes-competitiveness-strategy/` — Security and defence policy needs to be integrated into Europe’s competitiveness strategy
  2. `link:https://arxiv.org/abs/2607.21048` — Accelerating fossil gas independence in Europe
  3. `link:https://doi.org/10.1057/s41254-026-00441-9` — From public diplomacy to branding: the European Union’s external communication through the global gateway
  4. `link:https://www.cer.eu/sites/default/files/KP_EPF_africa_1.5.26.pdf` — The EU is trying to speak the language of power in Africa, but what is it saying?
  5. `link:https://doi.org/10.1016/j.ijhydene.2026.154457` — The role of green hydrogen imports under demand and supply uncertainties in Europe
  6. `link:https://www.cer.eu/sites/default/files/EC_JS_energy_shock_14.4.26_updated.pdf` — Energy shock 2.0: Lessons from 2022 for the Hormuz crisis
  7. `link:https://www.cer.eu/sites/default/files/ST_transatlantic_divorce_7.4.26.pdf` — One year liberation day: The delusion of transatlantic economic divorce
  8. `link:https://www.cer.eu/sites/default/files/AS_WTO_reform_2.4.26_final.pdf` — WTO reform after Yaoundé: What next for the multilateral trade order?
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
