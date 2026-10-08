#!/usr/bin/env python3
"""Build bounded, manually researched EU Economic Security discovery assignments.

This tool does not browse journals or contact any AI. It reads the repository's
published scanner rules and records to make a downloadable research ZIP.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import zipfile
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.llm_discovery_common import ROOT, FORMAT, PACKAGE_FORMAT, clean, doi, norm
from scripts.scan_radar import BOOTSTRAP_LOOKBACK_MONTHS, EXTENDED_TOP_QUALITY_LOOKBACK_MONTHS
from scripts.prepare_deep_scan_package import INSTRUCTIONS as DEEP_SCAN_CRITERIA

# Core international political economy/economic-security literature first, not
# the unrelated research-and-innovation venue list from the parent project.
PRIORITY_JOURNALS = [
    'Journal of European Public Policy',
    'Review of International Political Economy',
    'Journal of Common Market Studies',
    'International Organization',
    'International Affairs',
    'World Trade Review',
    'Journal of International Economic Law',
    'Economic Policy',
    'Journal of International Economics',
    'New Political Economy',
    'The World Economy',
    'Review of World Economics',
    'Business and Politics',
    'Journal of International Business Policy',
    'Energy Policy',
    'Resources Policy',
    'Global Policy',
    'Nature',
    'Science',
]
PRIORITY_INSTITUTIONS = [
    ('European Commission — Trade and Economic Security', 'https://policy.trade.ec.europa.eu/'),
    ('Joint Research Centre — Economic Security', 'https://joint-research-centre.ec.europa.eu/'),
    ('OECD — Trade and Global Value Chains', 'https://www.oecd.org/'),
    ('WTO — Trade Monitoring and Research', 'https://www.wto.org/'),
    ('European Parliament — Research Service', 'https://www.europarl.europa.eu/thinktank/'),
    ('Bruegel — European Economic Security', 'https://www.bruegel.org/'),
    ('European Central Bank', 'https://www.ecb.europa.eu/'),
    ('European Investment Bank', 'https://www.eib.org/'),
    ('International Energy Agency', 'https://www.iea.org/'),
    ('World Bank', 'https://www.worldbank.org/'),
    ('International Monetary Fund', 'https://www.imf.org/'),
    ('European Commission — Internal Market and Industry', 'https://single-market-economy.ec.europa.eu/'),
    ('Centre for European Policy Studies', 'https://www.ceps.eu/'),
    ('MERICS', 'https://merics.org/'),
    ('Kiel Institute for the World Economy', 'https://www.ifw-kiel.de/'),
]
THEMES = [
    'European import concentration, critical raw materials and supplier substitution',
    'trade weaponisation, economic coercion, sanctions and retaliation',
    'EU foreign direct investment screening, outbound investment and technology leakage',
    'export controls, dual-use goods, semiconductors and advanced technology dependencies',
    'European trade diversification and partnerships with like-minded economies',
    'EU energy security, clean-tech supply chains and strategic infrastructure',
    'industrial policy, strategic autonomy, competitiveness and resilience trade-offs',
    'empirical EU-China and EU-US geoeconomic exposure and interdependence',
]

START = '''# START HERE — Manual EU Economic Security research discovery

You are a human-initiated, browsing-capable LLM research assistant, NOT the
Radar's authoritative Deep Scan verifier. There are NO automated LLM APIs.
Investigate the bounded, prioritized assignments in `tasks.json` in order.
Strand A is the priority: actual peer-reviewed analytical studies AND substantial
institutional economic-security research and reports. Do not return generic news,
press releases, institution portals, calls, speeches or hypothetical studies.

This repository studies **European economic security**: protecting Europe from
weaponised interdependence while retaining the benefits of an open economy and
cooperating with partners. A qualifying work must offer actual source-supported
European/EU evidence on trade, investment, geoeconomic coercion, strategic
supply-chain/technology/energy dependencies, risk mitigation or related systemic
capacities. A study may be published anywhere, but an author's European address
or incidental mention of Europe is not enough. Journal prestige is not admission.
Do NOT search mainly for Horizon Europe grants, generic university performance,
research careers, open science or general R&I studies: that is a *different Radar*.

Read `admission_policy.txt` and `topic_focus.json`. Use
`existing_radar_records.json` to avoid duplicates across strands and archives.
`candidate_leads.json` contains scanner-deferred *unverified* metadata, NOT real
verified publications. `coverage_gaps.json` lists observed gaps, not proof that
any particular paper was missed.

## Deliverable — one JSON file for manual GitHub upload

Return a downloadable **UTF-8** `llm_research_results.json` using the **exact**
`results_TEMPLATE.json` schema and `package_id`; up to 24 findings; zero if no
publications pass. Work tasks in order. No Markdown fences, invented citations,
made-up publications, unverifiable dates, padded entries or fabricated abstracts.

For each candidate supply the exact article/report title, actual authors/issuer,
credible source/journal, official HTTPS publication URL, DOI if present, the
**first publication date** YYYY-MM-DD as independently verified (NOT a web
update/crawl date), study evidence, principal findings, and concrete **European
/EU economic-security relevance**. Supply **at least two different, meaningful,
verbatim passages of 10+ words each from the publisher's actual abstract/body
or official institution report**, with original evidence references and any
access/verification limitations. When the official full report is a PDF, use
`metadata_url` for its separate official dated landing page if necessary.
Distinguish directly verified material from your own tentative inferences.

GitHub's importer independently obtains first-party records and verifies source
identity, original dates, passages, substantive content and the current **same
Economic Security Strand-A gate** as the scanner. The LLM's own prose is NOT
source proof. Unsupported candidates are rejected, even if likely to be real.
The importer NEVER sends a finding back through the scanner's discovery/retrieval
search stage. Admitted records go directly into `radar.json` as **LLM-assisted
discovery — Pending Deep Scan**, which the EXISTING manual Deep Scan then verifies
with its normal KEEP/REVIEW/DROP/DROP_UNVERIFIABLE and retry rules.

Aim for up to two genuinely important works per task but at most 24 overall.
Do not let a short institutional briefing crowd out primary scientific evidence.
'''


def _configured_institutions(cfg):
    insts = []
    for row in cfg.get('institution_sources', []):
        if isinstance(row, dict) and row.get('domain') and row.get('name'):
            insts.append((clean(row['name']), 'https://' + clean(row['domain']) + '/'))
    return insts


def _raw_leads(corpus, known_dois):
    deferred = (corpus.get('scan_state') or {}).get('deferred_metadata_queue', [])
    leads = []
    for row in deferred if isinstance(deferred, list) else []:
        if not isinstance(row, dict):
            continue
        raw = row.get('raw') if isinstance(row.get('raw'), dict) else {}
        identifier = doi(raw.get('DOI') or raw.get('doi'))
        title = raw.get('title') or raw.get('display_name') or ''
        title = title[0] if isinstance(title, list) and title else title
        title = clean(title)
        if not identifier or identifier in known_dois or not title:
            continue
        if norm(title).startswith(('book review', 'editorial', 'corrigendum', 'retraction')):
            continue
        scope = norm(title)
        if not any(term in scope for term in (
            'europe', 'eu ', 'european union', 'trade', 'economic security',
            'supply chain', 'de risking', 'coercion', 'sanction', 'raw material',
            'export control', 'investment screening', 'industrial policy',
            'energy security', 'strategic autonomy', 'tariff', 'critical mineral',
        )):
            continue
        leads.append({'title_unverified': title, 'doi_unverified': identifier,
                      'provider': clean(row.get('provider')), 'scanner_state': 'deferred_metadata',
                      'reason': 'incomplete_metadata',
                      'instructions': 'Investigate actual identity, original publication date, full study evidence and EU economic-security relevance; do NOT presume admissibility.'})
        if len(leads) == 12:
            break
    return leads, len(deferred) if isinstance(deferred, list) else 0


def build(corpus, cfg, limit=18, today=None):
    today = today or dt.date.today()
    assert 5 <= limit <= 20
    counts = Counter(norm(x.get('source')) for x in corpus.get('strand_a', []) if isinstance(x, dict))
    journal_names = list(dict.fromkeys(PRIORITY_JOURNALS + cfg.get('crossref_priority_journals', []) +
                                        cfg.get('top_journal_watchlist', [])))
    journal_core = PRIORITY_JOURNALS[:11]
    journal_names = journal_core + sorted([x for x in journal_names if x not in journal_core],
                                          key=lambda x: (counts[norm(x)], x))
    inst_core = PRIORITY_INSTITUTIONS[:6]
    insts = list(dict.fromkeys(PRIORITY_INSTITUTIONS + _configured_institutions(cfg)))
    insts = inst_core + sorted([x for x in insts if x not in inst_core],
                               key=lambda x: (counts[norm(x[0])], x[0]))
    journal_count = min(11, max(3, round(limit * .61)))
    institution_count = min(6, max(2, round(limit * .33)))
    while journal_count + institution_count > limit:
        if journal_count > 3:
            journal_count -= 1
        else:
            institution_count -= 1
    tasks = []
    for i, name in enumerate(journal_names[:journal_count]):
        tasks.append({'id': f'J{i+1:02}', 'priority': 1 if i < 6 else 2,
                      'type': 'scientific_journal', 'target': name,
                      'existing_strand_a_count': counts[norm(name)],
                      'focus': THEMES[i % len(THEMES)],
                      'instructions': 'Investigate original articles, DOI/publisher abstract and date; credible geoeconomic mechanism and European evidence required.'})
    for i, (name, url) in enumerate(insts[:institution_count]):
        tasks.append({'id': f'I{i+1:02}', 'priority': 1 if i < 3 else 2,
                      'type': 'institutional_research', 'target': name,
                      'starting_url': url, 'existing_strand_a_count': counts[norm(name)],
                      'focus': THEMES[(i + 2) % len(THEMES)],
                      'instructions': 'Investigate completed, dated analytical reports and empirical evidence, not announcements, portals or news.'})
    known_dois = {doi(row.get('_doi') or row.get('doi') or row.get('link'))
                  for group in ('strand_a', 'strand_b', 'strand_c', 'ab_archive', 'signal_archive')
                  for row in corpus.get(group, []) if isinstance(row, dict)}
    leads, queue_size = _raw_leads(corpus, known_dois)
    remaining = limit - len(tasks)
    for i, lead in enumerate(leads[:remaining]):
        tasks.append({'id': f'R{i+1:02}', 'priority': 2,
                      'type': 'unresolved_scanner_lead', **lead})
    # If scanner state has no relevant deferred DOI, still reserve this bounded
    # assignment for an explicit under-covered topic; never manufacture a lead.
    if len(tasks) < limit:
        tasks.append({'id': f'R{len(tasks)-journal_count-institution_count+1:02}', 'priority': 2,
                      'type': 'targeted_coverage_gap', 'target': 'European economic security source gaps',
                      'focus': THEMES[(len(tasks)+1) % len(THEMES)],
                      'instructions': 'Search official research collections and journals not covered by other tasks. Do not infer a particular scanner failure without diagnostics.'})
    tasks = tasks[:limit]
    gaps = {
        'radar': 'EU Economic Security Radar',
        'scanner_diagnostics': {'scan_health': corpus.get('scan_health'),
                                'deferred_metadata_queue_size': queue_size,
                                'last_scan_at': (corpus.get('scan_state') or {}).get('last_completed_at'),
                                'transport_failure_warning_count': (corpus.get('scan_diagnostics') or {}).get('transport_failure_warning_count')},
        'priority': 'Substantive empirical European/EU economic-security evidence from scientific journals and trusted institutions',
        'interpretation_note': 'Sparse coverage is a search priority, not proof of missed publications or an inaccessible publisher.',
        'underrepresented_journals': [{'journal': j, 'strand_a_count': counts[norm(j)]} for j in journal_names[:25]],
        'underrepresented_institutions': [{'institution': n, 'strand_a_count': counts[norm(n)]} for n, _ in insts[:20]],
        'publication_window': {'normal_months': BOOTSTRAP_LOOKBACK_MONTHS,
                               'exceptional_tier_months': EXTENDED_TOP_QUALITY_LOOKBACK_MONTHS,
                               'as_of': today.isoformat()},
    }
    return tasks, leads, gaps


def existing_identity_index(corpus, root=ROOT):
    """Include the Main Radar plus historical/private identities for LLM dedupe.

    These are read-only inputs. No historic data or private candidate pool is
    rewritten, and this package does not treat them as verified publications.
    """
    records = []
    def append_rows(rows, collection):
        for row in rows if isinstance(rows, list) else []:
            if isinstance(row, dict):
                records.append({'strand': collection,
                                'title': clean(row.get('title') or row.get('headline')),
                                'doi': doi(row.get('_doi') or row.get('doi') or row.get('link')),
                                'link': clean(row.get('link') or row.get('url')),
                                'date': clean(row.get('date'))})
    for k in ('strand_a', 'strand_b', 'strand_c', 'frontier_evidence', 'ab_archive', 'signal_archive'):
        append_rows(corpus.get(k, []), k)
    for filename, bucket, label in (
        ('historical/historical.json', 'items', 'historical_archive'),
        ('deep_a_candidates.json', 'candidates', 'private_deep_a'),
        ('deep_a_candidate_archive.json', 'records', 'prior_deep_a_review'),
    ):
        p = root / filename
        if p.exists():
            data = json.loads(p.read_text(encoding='utf-8'))
            if isinstance(data, dict):
                append_rows(data.get(bucket, []), label)
    return records


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--corpus', type=Path, default=ROOT / 'radar.json')
    ap.add_argument('--config', type=Path, default=ROOT / 'radar_config.json')
    ap.add_argument('--output', type=Path, default=ROOT / 'llm-discovery-research-package.zip')
    ap.add_argument('--max-tasks', type=int, default=18)
    args = ap.parse_args()
    if not 5 <= args.max_tasks <= 20:
        ap.error('--max-tasks must be between 5 and 20')
    corpus = json.loads(args.corpus.read_text(encoding='utf-8'))
    cfg = json.loads(args.config.read_text(encoding='utf-8'))
    tasks, leads, gaps = build(corpus, cfg, args.max_tasks)
    now = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    package_id = 'econ-a-' + now
    template = {'format': FORMAT, 'package_id': package_id, 'findings': [{
        'title': 'REPLACE — exact publication title', 'authors': ['Actual authors or issuing institution'],
        'source': 'Actual scholarly journal or institution', 'publication_type': 'journal_article',
        'doi': '10.xxxx/real-article (or empty string for a report without DOI)',
        'official_url': 'https://official-publisher-or-institution.example/publication',
        'metadata_url': '', 'publication_date': 'YYYY-MM-DD',
        'abstract_or_evidence': 'Actual independently checkable research abstract or substantive evidence',
        'principal_findings': ['Substantive source-grounded empirical result, with caveats'],
        'eu_economic_security_relevance': 'What actual evidence shows about European dependencies, resilience, openness, coercion, exposure or security policy',
        'evidence_quotes': ['Verbatim 10+ word passage from the official original abstract or publication',
                            'Distinct second 10+ word passage from the official original abstract or publication'],
        'source_references': [{'url': 'https://real-original-evidence.example', 'supports': 'Exact identity, original date and evidence'}],
        'verification_limitations': 'Specific inaccessible or unverified elements (or none)',
        'discovery_task_id': 'J01', 'suspected_scanner_miss': 'Unverified hypothesis or empty',
    }]}
    records = existing_identity_index(corpus, args.corpus.resolve().parent)
    files = {
        'START_HERE.md': START,
        'tasks.json': json.dumps({'format': PACKAGE_FORMAT, 'package_id': package_id, 'tasks': tasks}, ensure_ascii=False, indent=2) + '\n',
        'coverage_gaps.json': json.dumps(gaps, ensure_ascii=False, indent=2) + '\n',
        'candidate_leads.json': json.dumps(leads, ensure_ascii=False, indent=2) + '\n',
        'existing_radar_records.json': json.dumps(records, ensure_ascii=False, indent=2) + '\n',
        'results_TEMPLATE.json': json.dumps(template, ensure_ascii=False, indent=2) + '\n',
        'topic_focus.json': json.dumps({
            'radar': 'EU Economic Security Radar', 'central_question': 'Protect against weaponised interdependence without surrendering open economy gains',
            'strands': {'A': 'Evidence on economic security and European capacity/dependencies',
                        'B': 'Disabled in this repository', 'C': 'Current strategic developments (outside this Strand-A research importer)'},
            'research_themes': THEMES,
            'configured_top_sources': cfg.get('crossref_priority_journals', [])[:30],
            'admission': 'Existing scripts.scan_radar.gate_scope(...).a_pass; no publication prestige shortcut',
        }, ensure_ascii=False, indent=2) + '\n',
        'admission_policy.txt': DEEP_SCAN_CRITERIA + '\n\nEconomic-security terms and sources are configured in topic_lexicon.json and radar_config.json. Importer reuses scripts.scan_radar.gate_scope(...), final_ab_candidate_worthiness(...), quality_from_crossref(...), bootstrap_floor(...) and extended_top_quality_floor(...) unchanged. Strand B is disabled here.\n',
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for name, content in files.items():
            z.writestr(name, content)
    print(f'EU Economic Security manual research package: {args.output} tasks={len(tasks)} candidates={len(leads)} existing={len(records)} id={package_id}')


if __name__ == '__main__':
    main()
