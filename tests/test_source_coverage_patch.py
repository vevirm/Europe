"""Small offline regression checks for source-coverage repair; no network requests."""
import datetime as dt
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts import scan_radar as s
from scripts.audit_source_coverage import coverage_report


class SourceCoverageRepair(unittest.TestCase):
    def test_official_sources_and_feeds_configured(self):
        sources = {x['domain']: x for x in s.CONFIG['institution_sources']}
        self.assertIn('cordis.europa.eu', sources)
        self.assertIn('epo.org', sources)
        self.assertTrue(sources['consilium.europa.eu'].get('feeds'))
        self.assertTrue(sources['epo.org'].get('feeds'))
        self.assertFalse(s.CONFIG.get('force_backfill_on_source_expansion', False))
        self.assertFalse(s.STRAND_B_ENABLED)

    def test_valid_feed_yields_only_own_domain_pages(self):
        feed = b'''<?xml version="1.0"?><rss version="2.0"><channel><title>EPO</title>
            <item><title>Study</title><link>https://www.epo.org/en/news-events/news/a-study</link></item>
            <item><title>Malicious</title><link>https://not-epo.example.com/page</link></item>
            </channel></rss>'''
        src = {'domain': 'epo.org', 'name': 'EPO', 'tier': 1, 'feeds': ['https://www.epo.org/en/news-events/news/feed']}
        transport = {}
        with patch.object(s, 'get', return_value=SimpleNamespace(content=feed)):
            with patch.object(s, '_known_institution_url_should_skip', return_value=False):
                jobs = s._institution_feed_jobs(src, dt.date(2026, 1, 1), transport=transport)
        self.assertEqual(len(jobs), 1)
        self.assertEqual(transport['feed_successful'], 1)
        self.assertEqual(jobs[0][0], 'https://www.epo.org/en/news-events/news/a-study')

    def test_html_block_page_not_counted_as_successful_feed(self):
        src = {'domain': 'epo.org', 'name': 'EPO', 'tier': 1, 'feeds': ['https://www.epo.org/en/news-events/news/feed']}
        transport = {}
        with patch.object(s, 'get', return_value=SimpleNamespace(content=b'<html><body>Blocked</body></html>')):
            jobs = s._institution_feed_jobs(src, dt.date(2026, 1, 1), transport=transport)
        self.assertEqual(jobs, [])
        self.assertEqual(transport['feed_successful'], 0)

    def test_healthy_feed_does_not_cause_false_sitemap_failure(self):
        src = {'domain': 'epo.org', 'name': 'EPO', 'tier': 1, 'feeds': ['https://www.epo.org/en/news-events/news/feed']}
        job = ('https://www.epo.org/en/a-study','EPO',1,'fingerprint')
        def fake_feed(_src, _date, _deadline, _reconsider, transport):
            transport['feed_successful'] = 1
            return [job]
        with patch.object(s, '_source_adapter_domain_jobs', return_value=[]), \
             patch.object(s, '_institution_feed_jobs', side_effect=fake_feed), \
             patch.object(s, 'discover_sitemaps', return_value=[]):
            jobs, warning = s._discover_domain(src, dt.date(2026, 1, 1))
        self.assertEqual(jobs, [job])
        self.assertIsNone(warning)

    def test_working_adapter_not_reported_as_failed_sitemap(self):
        src = {'domain': 'oecd.org', 'name': 'OECD', 'tier': 1}
        job = ('https://www.oecd.org/en/publications/reports/test.html', 'OECD', 1, 'fp')
        with patch.object(s, '_source_adapter_domain_jobs', return_value=[job]), \
             patch.object(s, '_institution_feed_jobs', return_value=[]), \
             patch.object(s, 'discover_sitemaps', return_value=[]):
            jobs, warning = s._discover_domain(src, dt.date(2026, 1, 1))
        self.assertEqual(jobs, [job])
        self.assertIsNone(warning)

    def test_publisher_abstract_reuses_existing_doi_request(self):
        html = '<html><section id="abstract">Abstract ' + ('A meaningful European industrial policy result. ' * 18) + '</section></html>'
        response = SimpleNamespace(status_code=200, text=html, headers={'content-type':'text/html'})
        with patch.object(s, 'deadline_reached', return_value=False), patch.object(s.SESSION, 'get', return_value=response) as request:
            abstract = s.doi_landing_abstract('10.1234/example', 4)
        self.assertGreater(len(abstract.split()), 40)
        self.assertEqual(request.call_count, 1)

    def test_audit_read_only_and_rotation_reported(self):
        report = coverage_report({'institution_sources':[{'domain':'epo.org'}]},
            {'last_updated':'now','scan_state':{'institution_cursor':3,'completed_cycles':{'institutions':2}},
             'scan_diagnostics':{'source_transport_attempts':{'epo.org':{'status':'ok','jobs_found':1}}}})
        self.assertIn('Institution full cycles: 2', report)
        self.assertIn('epo.org: ok', report)

if __name__ == '__main__':
    unittest.main()
