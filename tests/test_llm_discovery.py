"""Offline end-to-end contract tests for the manual LLM discovery route."""
from __future__ import annotations

import copy
import datetime as dt
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import scan_radar
from scripts import deep_read_works
from scripts import import_llm_discovery as I
from scripts import prepare_llm_discovery as P
from scripts.llm_discovery_common import FORMAT, duplicate_of, host, same_title, write_json

TODAY = dt.date(2026, 10, 8)
TITLE = 'European Union strategic dependencies and economic coercion in critical minerals trade'
A = ('This empirical study measures the European Union import dependence on critical minerals used in semiconductor and battery supply chains. '
     'Using product-level trade data for EU member states and China and the United States, we estimate supplier concentration, import diversification, sanctions exposure, and strategic vulnerabilities to economic coercion. '
     'European Union strategic autonomy and economic security depend on diversified foreign suppliers, resilient transport infrastructure, and coordinated investment screening across EU member states. '
     'Panel regressions show that concentrated rare earth imports increase disruption risks and that EU partnerships with like minded countries can lower supply chain exposure without closing European markets. '
     'The paper uses customs data, tariff schedules and input output analysis to quantify strategic dependencies, export controls and vulnerability to trade restrictions. '
     'Observed effects on firms and industries indicate the costs of decoupling and the economic benefits of open trade with improved security safeguards.')
Q1 = 'This empirical study measures the European Union import dependence on critical minerals used in semiconductor and battery supply chains.'
Q2 = 'Using product-level trade data for EU member states and China and the United States, we estimate supplier concentration, import diversification, sanctions exposure, and strategic vulnerabilities to economic coercion.'
DOI = '10.9999/eu-trade.2026'



def journal_meta():
    return {
        'DOI': DOI, 'type': 'journal-article', 'container-title': ['Review of International Political Economy'],
        'publisher': 'Taylor & Francis', 'title': [TITLE],
        'author': [{'given': 'Anna', 'family': 'Example'}],
        'published-online': {'date-parts': [[2026, 9, 12]]},
        'URL': f'https://doi.org/{DOI}',
        'abstract': '<jats:p>' + A + '</jats:p>',
    }


def submission():
    return {
        'title': TITLE, 'authors': ['Anna Example'], 'source': 'Review of International Political Economy',
        'publication_type': 'journal_article', 'doi': DOI,
        'official_url': f'https://doi.org/{DOI}',
        'metadata_url': '', 'publication_date': '2026-09-12',
        'abstract_or_evidence': A, 'principal_findings': ['Source-verified comparison of EU raw-material dependencies and coercion'],
        'eu_economic_security_relevance': 'Effects on EU dependence, import concentration, supply security and European open-economy resilience',
        'evidence_quotes': [Q1, Q2], 'source_references': [{'url': f'https://doi.org/{DOI}', 'supports': 'DOI article'}],
        'verification_limitations': 'Full text not retrieved; Crossref depositor abstract was available',
        'discovery_task_id': 'J01',
    }


class MockResponse:
    status_code = 200
    headers = {'content-type': 'application/json'}

    def __init__(self, body):
        self.content = body


class MockSession:
    def get(self, url, **kwargs):
        if url.startswith(I.CROSSREF):
            return MockResponse(json.dumps({'message': journal_meta()}).encode())
        raise AssertionError('Importer should never search the web or fetch a DOI redirect: ' + url)


class ResearchDiscoveryTests(unittest.TestCase):
    def test_preparation_bounded_journals_and_institutions_and_duplicate_inventory(self):
        tasks, leads, gaps = P.build({'strand_a': [], 'scan_state': {'deferred_metadata_queue': []}},
                                     {'institution_sources': []}, 18, TODAY)
        self.assertLessEqual(len(tasks), 18)
        self.assertGreaterEqual(sum(t['type'] == 'scientific_journal' for t in tasks), 8)
        self.assertGreaterEqual(sum(t['type'] == 'institutional_research' for t in tasks), 5)
        self.assertIn('Review of International Political Economy', [t['target'] for t in tasks])
        self.assertEqual(gaps['scanner_diagnostics']['deferred_metadata_queue_size'], 0)

    def test_research_identity_inventory_includes_historical_and_private(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'historical').mkdir()
            write_json(root/'historical'/'historical.json', {'items': [
                {'title': 'Historical economic security evidence', 'doi': '10.1111/historical'}]})
            write_json(root/'deep_a_candidates.json', {'candidates': [
                {'title': 'Pending independent verification', 'doi': '10.1111/private'}]})
            write_json(root/'deep_a_candidate_archive.json', {'records': [
                {'title': 'Reviewed in the past', 'doi': '10.1111/reviewed'}]})
            rows = P.existing_identity_index({'strand_a': [{'title': TITLE, 'doi': DOI}]}, root)
            self.assertEqual(len(rows), 4)
            self.assertEqual({x['strand'] for x in rows},
                             {'strand_a', 'historical_archive', 'private_deep_a', 'prior_deep_a_review'})

    def test_economic_security_package_cannot_import_into_ri_format(self):
        from scripts.llm_discovery_common import FORMAT, PACKAGE_FORMAT
        self.assertEqual(FORMAT, 'eu-economic-security-llm-discovery-results-v1')
        self.assertEqual(PACKAGE_FORMAT, 'eu-economic-security-llm-discovery-package-v1')
        self.assertTrue(P.PRIORITY_JOURNALS[0].startswith('Journal of European Public Policy'))
        self.assertIn('economic security', P.START.lower())
        self.assertNotIn('Horizon Europe grants, generic university performance,\nresearch careers', P.START[:50])

    def test_source_alone_cannot_make_economic_security_gate_pass(self):
        p = submission()
        with patch.object(I.radar, 'gate_scope', return_value={'a_pass': False, 'aboutness_reason': 'no economic security evidence'}):
            with self.assertRaisesRegex(I.Reject, 'substantive admission failed'):
                I.verify_candidate(p, MockSession(), today=TODAY)

    def test_verified_journal_import_uses_shared_gate_and_is_deep_scan_pending(self):
        row = I.verify_candidate(submission(), MockSession(), today=TODAY)
        self.assertEqual(row['discovery_method'], 'LLM-assisted discovery — Pending Deep Scan')
        self.assertEqual(row['strand'], 'A')
        self.assertEqual(row['date'], '2026-09-12')
        self.assertEqual(row['llm_discovery']['profile'], I.PROFILE)
        self.assertTrue(row['llm_discovery']['source_supported_quotes'])
        self.assertTrue(any(k == deep_read_works.record_key(row) for _,k,_,_,_ in
                            deep_read_works.pending({'strand_a': [row], 'strand_b': [], 'strand_c': [], 'frontier_evidence': []}, {'records': {}})))

    def test_native_publisher_article_page_requires_matching_crossref_doi(self):
        p = submission()
        p['official_url'] = 'https://www.tandfonline.com/doi/full/10.9999/eu-trade.2026'
        p['source_references'] = [{'url': p['official_url'], 'supports': 'Publisher article and DOI'}]
        class NativePublisherSession(MockSession):
            def get(self, url, **kwargs):
                if url.startswith(I.CROSSREF):
                    return super().get(url, **kwargs)
                assert url == p['official_url']
                payload = (f'<html><head><meta name="citation_title" content="{TITLE}">'
                           f'<meta name="citation_doi" content="{DOI}"></head>'
                           f'<body><article><h1>{TITLE}</h1><p>{A}</p></article></body></html>')
                response = MockResponse(payload.encode())
                response.headers = {'content-type': 'text/html'}
                return response
        result = I.verify_candidate(p, NativePublisherSession(), today=TODAY)
        self.assertEqual(result['link'], p['official_url'])
        self.assertTrue(any(x.get('kind') == 'verified_publisher_page' for x in result['llm_discovery']['primary_evidence']))

    def test_doi_indexed_abstract_recovers_publisher_block_without_llm_claims(self):
        p = submission()
        work = journal_meta()
        work.pop('abstract', None)
        inverted = {}
        for pos, word in enumerate(A.split()):
            inverted.setdefault(word, []).append(pos)
        class IndexedSession:
            def get(self, url, **kwargs):
                if url.startswith(I.CROSSREF):
                    return MockResponse(json.dumps({'message': work}).encode())
                if url.startswith(I.OPENALEX):
                    return MockResponse(json.dumps({'results': [{
                        'doi': f'https://doi.org/{DOI}', 'title': TITLE,
                        'abstract_inverted_index': inverted
                    }]}).encode())
                raise AssertionError('Indexer must use exact DOI; no free-text search or publisher fetch')
        row = I.verify_candidate(p, IndexedSession(), today=TODAY)
        self.assertEqual(row['doi'], DOI)
        self.assertTrue(any(x['kind'] == 'independent_doi_matched_abstract_index'
                            for x in row['llm_discovery']['primary_evidence']))

    def test_rejects_unverifiable_date_and_fabricated_quotation(self):
        p = submission()
        p['publication_date'] = '2026-09-13'
        with self.assertRaisesRegex(I.Reject, 'date disagrees'):
            I.verify_candidate(p, MockSession(), today=TODAY)
        p = submission()
        p['evidence_quotes'][0] = 'Fabricated publication evidence that cannot be checked in any official source page and must be rejected.'
        with self.assertRaisesRegex(I.Reject, 'source passages matched'):
            I.verify_candidate(p, MockSession(), today=TODAY)

    def test_bypass_llm_unsupported_summaries_in_substantive_gate(self):
        p = submission()
        p['abstract_or_evidence'] = 'Unsupported invented achievement about trade dominance and European resilience.'
        p['principal_findings'] = ['Unsupported claim not in publisher abstract']
        p['eu_economic_security_relevance'] = 'Unsupported political claim about European trade leadership'
        row = I.verify_candidate(p, MockSession(), today=TODAY)
        self.assertNotIn('trade dominance', row['summary'])
        self.assertEqual(row['llm_discovery']['llm_claims_not_authoritative'], True)

    def test_no_relevance_even_with_verified_doi_is_rejected(self):
        p = submission()
        with patch.object(I.radar, 'gate_scope', return_value={'a_pass': False, 'aboutness_reason': 'not European economic-security evidence'}):
            with self.assertRaisesRegex(I.Reject, 'existing Strand A substantive admission failed'):
                I.verify_candidate(p, MockSession(), today=TODAY)

    def test_protected_url_and_identity_duplicate(self):
        for u in ['http://example.org/a', 'https://127.0.0.1/a', 'https://localhost/a', 'https://user:pass@oecd.org/doc']:
            self.assertFalse(host(u), u)
        known = [({'title': TITLE, '_doi': DOI, 'link': f'https://doi.org/{DOI}'}, 'strand_a')]
        self.assertEqual(duplicate_of({'title': TITLE+'!', 'doi': DOI}, known)[0], 'strand_a')

    def test_process_full_inbox_and_replay_same_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            report_dir = root / 'reports'
            f = root / 'discovery.json'
            write_json(f, {'format': FORMAT, 'package_id': 'econ-a-20261008T100000Z',
                           'findings': [submission(), submission()]})
            c = {'strand_a': [], 'strand_b': [], 'strand_c': [], 'frontier_evidence': [], 'scan_state': {}}
            r = I.process_file(f, corpus=c, pool={}, session=MockSession(), report_dir=report_dir, today=TODAY)
            self.assertEqual(r['admitted'], 1)
            self.assertEqual(r['duplicates'], 1)
            self.assertEqual(len(c['strand_a']), 1)
            self.assertEqual(I.process_file(f, corpus=c, pool={}, session=MockSession(), report_dir=report_dir)['already_processed'], True)
            self.assertEqual(len(c['strand_a']), 1)

    def test_uncommitted_report_does_not_suppress_a_valid_import_retry(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            f = root/'discovery.json'
            write_json(f, {'format': FORMAT, 'package_id': 'econ-a-20261008T100000Z',
                           'findings': [submission()]})
            corpus = {'strand_a': [], 'scan_state': {}}
            first = I.process_file(f, corpus=corpus, pool={}, session=MockSession(), report_dir=root/'reports', today=TODAY)
            self.assertEqual(first['admitted'], 1)
            # Simulate a process failure after the report but before corpus
            # write, without modifying the real project.
            corpus['strand_a'].clear()
            again = I.process_file(f, corpus=corpus, pool={}, session=MockSession(), report_dir=root/'reports', today=TODAY)
            self.assertEqual(again['admitted'], 1)
            self.assertEqual(len(corpus['strand_a']), 1)

    def test_evidence_insufficient_is_reported_not_admitted(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            f=root/'bad.json'
            bad=submission(); bad['evidence_quotes'] = ['This is a fictional passage with absolutely no actual evidentiary basis in source material at all.' ,Q2]
            write_json(f, {'format': FORMAT, 'package_id': 'econ-a-20261008T100000Z', 'findings': [bad]})
            c={'strand_a': [], 'scan_state': {}}
            r=I.process_file(f, corpus=c, pool={}, session=MockSession(), report_dir=root/'reports', today=TODAY)
            self.assertEqual((r['rejected'], len(c['strand_a'])), (1,0))

    def test_institutional_date_from_publication_metadata_and_verified_body(self):
        p=submission(); p.update(publication_type='institutional_report', doi='',
            official_url='https://publications.jrc.ec.europa.eu/repository/handle/JRC-TEST',
            source='Joint Research Centre', discovery_task_id='I01')
        p['source_references']=[{'url': p['official_url'], 'supports': 'original report'}]
        class InstitutionalSession:
            def get(self, url, **kwargs):
                self_url=p['official_url']
                assert url == self_url
                x=f'<html><head><meta name="citation_title" content="{TITLE}"><meta name="citation_publication_date" content="2026-09-12"></head><body><article><h1>{TITLE}</h1><p>{A}</p></article></body></html>'
                o=MockResponse(x.encode()); o.headers={'content-type': 'text/html'}; return o
        row=I.verify_candidate(p, InstitutionalSession(), today=TODAY)
        self.assertEqual(row['llm_discovery']['primary_evidence'][0]['kind'], 'official_institution_publication')
        p['publication_date']='2026-09-11'
        with self.assertRaisesRegex(I.Reject, 'date differs'):
            I.verify_candidate(p, InstitutionalSession(), today=TODAY)

    def test_old_article_cannot_bypass_two_tier_recency_even_with_good_abstract(self):
        p=submission(); p['publication_date']='2024-09-12'
        work=journal_meta(); work['published-online']={'date-parts': [[2024,9,12]]}
        class OldSession:
            def get(self, url, **kwargs):
                return MockResponse(json.dumps({'message': work}).encode())
        with self.assertRaisesRegex(I.Reject, 'publication-date window'):
            I.verify_candidate(p, OldSession(), today=TODAY)


if __name__ == '__main__':
    unittest.main()
