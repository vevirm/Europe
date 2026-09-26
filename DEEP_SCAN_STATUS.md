# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what now needs hands-on verification.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` counts as one genuine recovery pass. After **3** unsuccessful passes, the work leaves the automatic queue and enters **Hands-on verification needed**.

- Authoritative V2 verified: **184** (Main **184** + Historical **0**)
- Automatic queue still needing V2 verification: **1042** (Main **336** + Historical **706**)
- Currently assigned to workers: **72** (Main **72** + Historical **0**)
- Bounded access-recovery retries still eligible: **0**
- Hands-on verification needed: **0**
- Automatic queue pending and not yet assigned: **970**

## Worker lanes

### Worker A
- Current package: `worker-a-20260926T095353Z-3dbd0c7a2da0`
- Assigned unresolved records: **36**
  1. `link:https://doi.org/10.1177/2336825x261466891` — Ukraine and the transformation of French strategic imaginaries: The discursive reconfiguration of European strategic autonomy under the presidency of Emmanuel Macron (2017-2026)
  2. `link:https://doi.org/10.1007/s13563-026-00701-3` — The Circular vs. Extraction Dilemma: Impacts of EU Critical Raw Materials Strategy on Poverty and Income Inequality – Evidence from Nickel in Finland, Greece, Poland, and Spain
  3. `link:https://doi.org/10.1093/jeea/jvag051` — Exorbitant Privilege of the Periodic Table? Geoeconomics, Endogenous Centrality and Strategic Minerals for the Green Transition
  4. `link:https://doi.org/10.1080/13501763.2026.2734066` — More than a broker: the commission in trilogues for geoeconomic instruments
  5. `link:https://doi.org/10.1093/hrlr/ngag015` — Finding a bridge between Erga Omnes obligations and WTO agreements: the case of human rights-based export controls on cyber-surveillance items
  6. `link:https://eur-lex.europa.eu/eli/reg/2021/821/oj/eng` — 2026 Update of the EU Control List of Dual-Use Items
  7. `link:https://doi.org/10.1057/s41599-026-08972-5` — The impact of Trump 2.0 tariff policy on international trade: evidence from Chinese firms
  8. `link:https://doi.org/10.1007/s43615-026-00944-w` — Resource Efficiency and Economic Resilience: Panel Evidence from the European Union
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-20260926T095403Z-77ea1109a623`
- Assigned unresolved records: **36**
  1. `link:https://doi.org/10.1186/s40008-026-00374-9` — Have non-EU countries become more involved in the UK’s value-added trade? An input–output analysis following the EU referendum
  2. `link:https://doi.org/10.1093/migration/mnag042` — From stratification to coercion: EU externalization and Turkey’s differentiated return regime
  3. `link:https://doi.org/10.1093/ser/mwag003` — Green monetary transitions? Central banking and climate finance in Europe and China
  4. `link:https://doi.org/10.1016/j.enpol.2026.115615` — Coherent, credible and comprehensive or diffuse and ineffective? The energy poverty policy mix in Norway during geopolitical changes
  5. `link:https://globaltradealert.org/reports/World-Import-Spending-Accelerates/` — World Import Spending Accelerates: What the China Shock 2.0 Narrative Misses - Global Trade Alert
  6. `link:https://doi.org/10.1016/j.telpol.2026.103222` — Enabling the EU's digital Sovereignty: A Europe-level quantum internet as the key infrastructure for a European digital polity
  7. `link:https://doi.org/10.17645/pag.12525` — The Politics of Procurement: Green Industrial Policy Through Non‐Price Criteria in European Offshore Wind Auctions
  8. `link:https://doi.org/10.1177/10242589261444001` — How can trade unions act strategically in response to decarbonisation? Union strategic capacity and automotive transition policies in Germany, Spain and the UK
  - … plus 28 more in the package manifest

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **19**
  1. `link:https://doi.org/10.1177/2336825x261466891` — Ukraine and the transformation of French strategic imaginaries: The discursive reconfiguration of European strategic autonomy under the presidency of Emmanuel Macron (2017-2026)
  2. `link:https://doi.org/10.1007/s13563-026-00701-3` — The Circular vs. Extraction Dilemma: Impacts of EU Critical Raw Materials Strategy on Poverty and Income Inequality – Evidence from Nickel in Finland, Greece, Poland, and Spain
  3. `link:https://doi.org/10.1093/jeea/jvag051` — Exorbitant Privilege of the Periodic Table? Geoeconomics, Endogenous Centrality and Strategic Minerals for the Green Transition
  4. `link:https://doi.org/10.1080/13501763.2026.2734066` — More than a broker: the commission in trilogues for geoeconomic instruments
  5. `link:https://doi.org/10.1093/hrlr/ngag015` — Finding a bridge between Erga Omnes obligations and WTO agreements: the case of human rights-based export controls on cyber-surveillance items
  6. `link:https://eur-lex.europa.eu/eli/reg/2021/821/oj/eng` — 2026 Update of the EU Control List of Dual-Use Items
  7. `link:https://doi.org/10.1057/s41599-026-08972-5` — The impact of Trump 2.0 tariff policy on international trade: evidence from Chinese firms
  8. `link:https://doi.org/10.1007/s43615-026-00944-w` — Resource Efficiency and Economic Resilience: Panel Evidence from the European Union
  - … plus 11 more in the package manifest
