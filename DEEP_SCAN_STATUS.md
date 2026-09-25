# Deep Scan V2 work status

This file is generated from the authoritative Deep Scan sidecar plus the persistent worker-assignment ledger.
It exists so a new chat or operator can see what has already been verified, what each worker owns, and what now needs hands-on verification.

Scheduling policy: preserve existing worker reservations; fill new slots with fresh **Main Radar first**; then use spare capacity for **Historical Radar**. Access-recovery retries are bounded and throttled so difficult works cannot consume every run.
A validated `defer` counts as one genuine recovery pass. After **3** unsuccessful passes, the work leaves the automatic queue and enters **Hands-on verification needed**.

- Authoritative V2 verified: **0** (Main **0** + Historical **0**)
- Automatic queue still needing V2 verification: **970** (Main **484** + Historical **486**)
- Currently assigned to workers: **120** (Main **120** + Historical **0**)
- Bounded access-recovery retries still eligible: **0**
- Hands-on verification needed: **0**
- Automatic queue pending and not yet assigned: **850**

## Worker lanes

### Worker A
- Current package: `worker-a-20260925T095801Z-87d10350b778`
- Assigned unresolved records: **60**
  1. `link:https://ecipe.org/publications/from-periphery-to-power/#_ftnref1` — From Periphery to Power: The Geoeconomic Case for Southeast Europe
  2. `link:https://doi.org/10.1007/s41125-026-00115-w` — EU Governance of Critical Infrastructure: Resilience and Artificial Intelligence as Policy Challenges
  3. `link:https://doi.org/10.65864/bm5cpn0bpv` — Trade-related Vulnerabilities and the Controversial Boundaries of Member States’ Economic Security in the EU
  4. `link:https://doi.org/10.1080/09692290.2026.2658660` — High-road or low-road? Europe’s EV battery rollout and the tradeoffs of green industrial policy in a geoeconomic world
  5. `link:https://doi.org/10.17645/pag.11403` — Geoeconomic Exposure and EU Industrial Policy: Export Dependence Amid US–China Techno‐Nationalist Rivalry
  6. `link:https://doi.org/10.1111/jcms.70140` — China and Limits to the European Union's Geoeconomic Turn
  7. `link:https://doi.org/10.1080/17487870.2026.2689934` — Lithium, leverage, and limits: Chile’s industrial policy vis-à-vis the EU-Chile free trade agreement’s energy and raw materials chapter
  8. `link:https://doi.org/10.1080/09662839.2026.2709844` — Reconceptualising security of supply in European defence politics
  - … plus 52 more in the package manifest

### Worker B
- Current package: `worker-b-20260925T095822Z-046eea0afde3`
- Assigned unresolved records: **60**
  1. `link:https://doi.org/10.1515/ev-2026-2001` — From Dependence to Sovereignty: Why Europe Needs a Digital Euro
  2. `link:https://doi.org/10.1111/jcms.70109` — Geopoliticization and Support for Free Trade in the European Parliament: From Rhetorical Shift to Voting Results
  3. `link:https://doi.org/10.1016/j.eist.2026.101177` — Socio-technical pathways of automotive decarbonization: evidence from patent network analysis in Germany and Japan
  4. `link:https://doi.org/10.1186/s43093-026-00993-5` — Climate-related financial risk and business resilience under the green transition: evidence from Central and Eastern European EU Economies
  5. `link:https://doi.org/10.1177/2336825x261473745` — European security, cooperation, and the challenge of strategic autonomy
  6. `link:https://doi.org/10.1186/s40008-026-00374-9` — Have non-EU countries become more involved in the UK’s value-added trade? An input–output analysis following the EU referendum
  7. `link:https://doi.org/10.1093/migration/mnag042` — From stratification to coercion: EU externalization and Turkey’s differentiated return regime
  8. `link:https://doi.org/10.1093/ser/mwag003` — Green monetary transitions? Central banking and climate finance in Europe and China
  - … plus 52 more in the package manifest
