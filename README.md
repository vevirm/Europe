# EU Economic Security Radar

Scanner, reasoning and reader pages for one question: how Europe can protect itself from the
weaponisation of interdependence while keeping the open economy that trade and investment rely on,
and deepening ties with like-minded partners. Built from the R&I × Geopolitics Radar (v25.1) with
the topic moved into data files and Strand B (methods) switched off.

## What runs

| Workflow | Trigger | Does |
|---|---|---|
| `radar-scan.yml` | every 4 h | smoke tests → `scan_radar.py` → `rebuild_active_radar.py` → Excel |
| `historical-scan.yml` | every 4 h, offset 2 h | older evidence (before the main window) |
| `deep-scan-prepare-workers.yml` | manual | packages ≤12 records for an external LLM to verify |
| `deep-scan-import.yml` | push to `deep_scan_inbox/` | validates LLM results, rebuilds the active corpus |
| `reader-language.yml` | manual | packages reader-facing wording that reads heavily, for an external LLM to rewrite |
| `reader-language-import.yml` | push to `reader_language_inbox/` | validates the rewrites and saves them to `reader_language/approved.json` |

Created by the first runs: `radar.json`, `radar_active.json`, `historical/historical.json`,
`reader_text.json`, `admission_state.json`, `record_corrections.json`, `deep_scan_work_state.json`,
`DEEP_SCAN_STATUS.md`, `stuff/source_merit_ranking.xlsx`.

Secrets: `OPENALEX_API_KEY` (strongly recommended), `CROSSREF_MAILTO` (your email).

## Better wording (Reader Language)

Optional and never blocks publishing. Run **Reader Language** in Actions, download the package,
give it to an LLM, upload the returned `reader_language_results.json` to `reader_language_inbox/`.
Approved rewrites are overlaid on the pages by `reader_language.js`, each tied to a fingerprint of
the exact original sentence, so a rewrite stops applying if the underlying text changes. Evidence,
sources, scores and Deep Scan decisions are never touched. Details: `READER_LANGUAGE_SETUP.md`.

## Where the topic lives

| File | Holds |
|---|---|
| `topic_lexicon.json` | the term lists the scanner's admission gates use (domain, geoeconomic, EU scope, themes) |
| `radar_config.json` | queries, sources, journals, news feeds, frontier-cell queries; `strand_b_enabled: false` |
| `radar_phrase_rules.json` | curated phrases for admission and news retrieval |
| `historical/config.json` | historical topics and sources |
| `claims_vocabulary.json` | objects and clusters the Deep Scan LLM may use for claims |
| `scripts/shock_inference.py` | what can be hit (assets) and how (pressures) |
| `scripts/high_order_inference.py`, `scripts/scenarios_2035.py` | reasoning topics and the four 2035 worlds |
| `frontier/frontier.js` | the matrix: rows (technology; energy, materials & infrastructure; industry, trade & investment; tools, coercion & partners) × columns (more secure & stronger / more secure, less open / open gains, still reliant / exposed & weaker) |
| `shocks/scenarios.js`, `trends/trends.js`, `read/issues.js`, `briefing/insights.js`, `glossary/glossary.js` | hand-written shocks, trend pairs, reader maps, topics and glossary |
| `scripts/prepare_deep_scan_package.py` | verification criteria given to the LLM |

To reuse for yet another topic, change these files; the corpus/admission/Deep Scan plumbing is topic-neutral.

## Before going live

- Add verified primary documents (e.g. JOIN(2025) 977, JOIN(2023) 20) to
  `must_not_miss_primary_evidence_urls` in `radar_config.json`.
- The home-page password gate is inherited unchanged (same password as the R&I radar);
  change `PASSWORD_HASH` in `index.html` if you want a different one.
- Some internal variable names still say `RI_*` or `research_*`; they are labels only.

## Compact curated build — 2026-09-25

This repository is packaged as a compact deployment while preserving the reader-facing Radar pages and the main scanner/deep-scan scripts.

- Raw scanner archive remains in `radar.json` for audit/scanner continuity.
- `admission_state.json` limits the reader-facing active corpus to 82 retained records (55 Strand A rows and 27 Strand C rows after shared-link expansion).
- `reader_text.json` contains 73 manually curated Deep Scan V2 authoritative identities. The compact promotion uses the substantive source text, publisher abstract/metadata, or dated weak-signal evidence already recovered by the scanner; qualifications are retained where only abstract/news evidence is available.
- Scenario frame: **guarded / strategically restricted integration ↔ open global integration** crossed with **constrained European capacity ↔ expanding European capacity**.
- The 2035 section contains four main worlds and four variants per world (16 variants; 20 cards including the four parent worlds). These are scenarios, not forecasts.
- Items excluded by the compact admission layer remain in the raw scanner archive so a later scan or re-curation can promote them again.
