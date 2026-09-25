# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what now needs hands-on verification.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` counts as one genuine recovery pass. After **3** unsuccessful passes, the work leaves the automatic queue and enters **Hands-on verification needed**.

- Authoritative V2 verified: **4** (Main **4** + Historical **0**)
- Automatic queue still needing V2 verification: **966** (Main **480** + Historical **486**)
- Currently assigned to workers: **115** (Main **115** + Historical **0**)
- Bounded access-recovery retries still eligible: **1**
- Hands-on verification needed: **0**
- Automatic queue pending and not yet assigned: **851**

## Worker lanes

### Worker A
- Current package: `worker-a-20260925T123845Z-7b354dc9317b`
- Assigned unresolved records: **58**
  1. `link:https://doi.org/10.65864/bm5cpn0bpv` — Trade-related Vulnerabilities and the Controversial Boundaries of Member States’ Economic Security in the EU
  2. `link:https://doi.org/10.1080/09692290.2026.2658660` — High-road or low-road? Europe’s EV battery rollout and the tradeoffs of green industrial policy in a geoeconomic world
  3. `link:https://doi.org/10.17645/pag.11403` — Geoeconomic Exposure and EU Industrial Policy: Export Dependence Amid US–China Techno‐Nationalist Rivalry
  4. `link:https://doi.org/10.1111/jcms.70140` — China and Limits to the European Union's Geoeconomic Turn
  5. `link:https://doi.org/10.1080/17487870.2026.2689934` — Lithium, leverage, and limits: Chile’s industrial policy vis-à-vis the EU-Chile free trade agreement’s energy and raw materials chapter
  6. `link:https://doi.org/10.1080/09662839.2026.2709844` — Reconceptualising security of supply in European defence politics
  7. `link:https://doi.org/10.1111/jcms.70156` — Under the Surface: Subsea Infrastructure and Everyday Geoeconomics in the European Union
  8. `link:https://doi.org/10.1007/s44282-026-00431-5` — Energy security dynamics in Europe amid transatlantic decoupling from Russia
  - … plus 50 more in the package manifest

### Worker B
- Current package: `worker-b-20260925T123905Z-a4a0383b3860`
- Assigned unresolved records: **57**
  1. `link:https://doi.org/10.1186/s43093-026-00993-5` — Climate-related financial risk and business resilience under the green transition: evidence from Central and Eastern European EU Economies
  2. `link:https://doi.org/10.1177/2336825x261473745` — European security, cooperation, and the challenge of strategic autonomy
  3. `link:https://doi.org/10.1186/s40008-026-00374-9` — Have non-EU countries become more involved in the UK’s value-added trade? An input–output analysis following the EU referendum
  4. `link:https://doi.org/10.1093/migration/mnag042` — From stratification to coercion: EU externalization and Turkey’s differentiated return regime
  5. `link:https://doi.org/10.1093/ser/mwag003` — Green monetary transitions? Central banking and climate finance in Europe and China
  6. `link:https://doi.org/10.1016/j.enpol.2026.115615` — Coherent, credible and comprehensive or diffuse and ineffective? The energy poverty policy mix in Norway during geopolitical changes
  7. `link:https://globaltradealert.org/reports/World-Import-Spending-Accelerates/` — World Import Spending Accelerates: What the China Shock 2.0 Narrative Misses - Global Trade Alert
  8. `link:https://doi.org/10.1016/j.telpol.2026.103222` — Enabling the EU's digital Sovereignty: A Europe-level quantum internet as the key infrastructure for a European digital polity
  - … plus 49 more in the package manifest

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **60**
  1. `link:https://doi.org/10.65864/bm5cpn0bpv` — Trade-related Vulnerabilities and the Controversial Boundaries of Member States’ Economic Security in the EU
  2. `link:https://doi.org/10.1080/09692290.2026.2658660` — High-road or low-road? Europe’s EV battery rollout and the tradeoffs of green industrial policy in a geoeconomic world
  3. `link:https://doi.org/10.17645/pag.11403` — Geoeconomic Exposure and EU Industrial Policy: Export Dependence Amid US–China Techno‐Nationalist Rivalry
  4. `link:https://doi.org/10.1111/jcms.70140` — China and Limits to the European Union's Geoeconomic Turn
  5. `link:https://doi.org/10.1080/17487870.2026.2689934` — Lithium, leverage, and limits: Chile’s industrial policy vis-à-vis the EU-Chile free trade agreement’s energy and raw materials chapter
  6. `link:https://doi.org/10.1080/09662839.2026.2709844` — Reconceptualising security of supply in European defence politics
  7. `link:https://doi.org/10.1111/jcms.70156` — Under the Surface: Subsea Infrastructure and Everyday Geoeconomics in the European Union
  8. `link:https://doi.org/10.1007/s44282-026-00431-5` — Energy security dynamics in Europe amid transatlantic decoupling from Russia
  - … plus 52 more in the package manifest
