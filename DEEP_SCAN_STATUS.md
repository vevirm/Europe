# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what now needs hands-on verification.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` counts as one genuine recovery pass. After **3** unsuccessful passes, the work leaves the automatic queue and enters **Hands-on verification needed**.

- Authoritative V2 verified: **173** (Main **173** + Historical **0**)
- Automatic queue still needing V2 verification: **1018** (Main **347** + Historical **671**)
- Currently assigned to workers: **74** (Main **74** + Historical **0**)
- Bounded access-recovery retries still eligible: **0**
- Hands-on verification needed: **0**
- Automatic queue pending and not yet assigned: **944**

## Worker lanes

### Worker A
- Current package: `worker-a-20260926T055115Z-acd70f673165`
- Assigned unresolved records: **36**
  1. `link:https://doi.org/10.17645/pag.11403` — Geoeconomic Exposure and EU Industrial Policy: Export Dependence Amid US–China Techno‐Nationalist Rivalry
  2. `link:https://doi.org/10.1111/jcms.70140` — China and Limits to the European Union's Geoeconomic Turn
  3. `link:https://doi.org/10.1080/09662839.2026.2709844` — Reconceptualising security of supply in European defence politics
  4. `link:https://doi.org/10.1080/01402382.2026.2662873` — The EU as a global actor in the geoeconomic age: power and weakness in and through trade
  5. `link:https://doi.org/10.2478/ie-2026-0034` — Strategic Approach to Mitigating Europe’s Critical Dependencies: Aligning Economic Security Instruments with the Criticality of Supply Chains
  6. `link:https://doi.org/10.1080/14747731.2026.2658892` — The EU global gateway and energy infrastructure: navigating varieties of economic statecraft
  7. `link:https://doi.org/10.1080/07036337.2026.2652993` — Continuity in times of geoeconomic change: the European Union’s strategic trade relations with the Global South
  8. `link:https://doi.org/10.1007/s13347-026-01186-2` — For Good or Ill? A Conceptual Analysis of the Notion of Dual-use Technology
  - … plus 28 more in the package manifest

### Worker B
- Current package: `worker-b-20260926T055127Z-871d462bffbb`
- Assigned unresolved records: **38**
  1. `link:https://doi.org/10.1186/s43093-026-00993-5` — Climate-related financial risk and business resilience under the green transition: evidence from Central and Eastern European EU Economies
  2. `link:https://doi.org/10.1177/2336825x261473745` — European security, cooperation, and the challenge of strategic autonomy
  3. `link:https://doi.org/10.1186/s40008-026-00374-9` — Have non-EU countries become more involved in the UK’s value-added trade? An input–output analysis following the EU referendum
  4. `link:https://doi.org/10.1093/migration/mnag042` — From stratification to coercion: EU externalization and Turkey’s differentiated return regime
  5. `link:https://doi.org/10.1093/ser/mwag003` — Green monetary transitions? Central banking and climate finance in Europe and China
  6. `link:https://doi.org/10.1016/j.enpol.2026.115615` — Coherent, credible and comprehensive or diffuse and ineffective? The energy poverty policy mix in Norway during geopolitical changes
  7. `link:https://globaltradealert.org/reports/World-Import-Spending-Accelerates/` — World Import Spending Accelerates: What the China Shock 2.0 Narrative Misses - Global Trade Alert
  8. `link:https://doi.org/10.1016/j.telpol.2026.103222` — Enabling the EU's digital Sovereignty: A Europe-level quantum internet as the key infrastructure for a European digital polity
  - … plus 30 more in the package manifest

### Worker SINGLE
- Current package: `20260925T114333Z-23119bacb823`
- Assigned unresolved records: **30**
  1. `link:https://doi.org/10.17645/pag.11403` — Geoeconomic Exposure and EU Industrial Policy: Export Dependence Amid US–China Techno‐Nationalist Rivalry
  2. `link:https://doi.org/10.1111/jcms.70140` — China and Limits to the European Union's Geoeconomic Turn
  3. `link:https://doi.org/10.1080/09662839.2026.2709844` — Reconceptualising security of supply in European defence politics
  4. `link:https://doi.org/10.1080/01402382.2026.2662873` — The EU as a global actor in the geoeconomic age: power and weakness in and through trade
  5. `link:https://doi.org/10.2478/ie-2026-0034` — Strategic Approach to Mitigating Europe’s Critical Dependencies: Aligning Economic Security Instruments with the Criticality of Supply Chains
  6. `link:https://doi.org/10.1080/14747731.2026.2658892` — The EU global gateway and energy infrastructure: navigating varieties of economic statecraft
  7. `link:https://doi.org/10.1080/07036337.2026.2652993` — Continuity in times of geoeconomic change: the European Union’s strategic trade relations with the Global South
  8. `link:https://doi.org/10.1007/s13347-026-01186-2` — For Good or Ill? A Conceptual Analysis of the Notion of Dual-use Technology
  - … plus 22 more in the package manifest
