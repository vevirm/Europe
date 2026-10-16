"""Regressions for Deep Scan handoff, bounded opportunity synthesis and output depth."""
from __future__ import annotations

import datetime as dt
import unittest

from scripts.claims_schema import load_vocabulary, validate_claim
from scripts.claim_reasoning_shadow import constraint_conversion_candidates, flatten_claims, level3_findings
from scripts.claim_reasoning_live import _presentation_ready, _reader_copy, _select_stage7


class RadarReasoningRepairs(unittest.TestCase):
    def test_quick_scan_observations_survive_as_context_not_implementation(self):
        claim = {
            "record_key": "link:https://example.org/legacy", "claim_id": "c:legacy:1",
            "object": "econsec.trade_security", "secondary_objects": [],
            "actor": {"name": "Europe / European actors", "class": "european_system"},
            "mechanism": "shapes", "direction": "mixed", "status": "observation",
            "status_date": "2026-07-29", "scope": {"level": "europe", "countries": []},
            "kind": "evidence", "merit": 78, "qualification": "Abstract-based quick review.",
            "text": "Europe faces trade-security vulnerabilities across several sectors.",
            "confidence": "medium", "origin": "deep_scan", "era": "current", "provisional": False,
        }
        vocabulary = load_vocabulary()
        self.assertEqual([], validate_claim(claim, vocabulary))
        row = {"claims": [claim], "link": "https://example.org/legacy", "source": "Example",
               "deep_read_mode": "manual_quickscan_from_scanner_evidence_v1"}
        nodes, diagnostics = flatten_claims({"strand_a": [row]}, vocabulary)
        self.assertEqual(1, len(nodes))
        self.assertEqual(1, diagnostics["quick_scan_context_claims"])
        self.assertFalse(nodes[0]["_primary"])
        self.assertEqual(0.35, nodes[0]["_context_weight"])

    @staticmethod
    def _node(cid, source, kind, text, obj="energy.grid"):
        return {"claim_id": cid, "_record_id": cid, "_source": source,
                "_primary": True, "era": "current", "object": obj, "secondary_objects": [],
                "kind": kind, "status": "announced" if kind == "action" else "delivered",
                "status_date": "2026-10-08", "merit": 82, "text": text}

    def test_opportunity_pair_is_independent_and_explicitly_conditional(self):
        gap = self._node("c:gap", "Research Institute", "diagnosis",
                         "Risk-bearing and fragmented grid finance weaken feasibility for manufacturers.")
        measure = self._node("c:action", "European Investment Bank", "action",
                             "The bank launched financing guarantees for European electricity-grid manufacturers.")
        rows = constraint_conversion_candidates([gap, measure])
        self.assertTrue(rows)
        candidate = next(c for c in rows if c["issue"] == "finance")
        self.assertEqual("opportunity", candidate["product"])
        self.assertEqual(2, len(candidate["claim_ids"]))
        self.assertEqual([], candidate["missing_roles"])
        title, summary = _reader_copy("constraint_conversion", "opportunity", candidate,
                                       {"support": [], "primary_records": 2, "primary_sources": 2})
        self.assertIn("financing", title)
        self.assertIn("Risk-bearing", summary)
        self.assertIn("guarantees", summary)
        self.assertIn("neither source establishes", summary)
        self.assertEqual([], constraint_conversion_candidates([gap, dict(measure, _source="Research Institute")]))
        self.assertEqual([], constraint_conversion_candidates([gap, dict(measure, object="trade.agreement")]))

    def test_incomplete_pathways_remain_in_stock_not_published(self):
        candidate = {"product": "opportunity", "grammar_id": "latent_channel", "level": 5,
                     "missing_roles": ["live_connection"], "maturity_score": 99,
                     "primary_sources": 4, "primary_records": 4, "primary_role_coverage": 0.8}
        self.assertFalse(_presentation_ready(candidate)[0])

    def test_china_restriction_does_not_become_eu_rule_gap(self):
        china = self._node("c:china", "China regulator", "action",
                           "China imposed dual-use export restrictions.", "export_control.dual_use_list")
        china.update({"status_date":"2026-07-27", "scope":{"level":"third_country","countries":["China"]},
                      "actor":{"name":"Chinese Ministry","class":"third_country"}})
        doctrine = self._node("c:eu", "European Commission", "action",
                              "European Commission reviewed the EU dual-use export control regulation.",
                              "export_control.dual_use_list")
        doctrine.update({"status_date":"2026-09-14", "scope":{"level":"eu","countries":[]},
                        "actor":{"name":"European Commission","class":"eu_body"}})
        findings = level3_findings([china, doctrine], dt.date(2026, 10, 16))
        self.assertFalse(any(x.get("grammar_id")=="practice_before_doctrine" for x in findings))

    def test_repeated_rulebook_phrase_removed(self):
        candidate = {"support": [
            {"source_statement": "The EU introduced customs checks."},
            {"source_statement": "The Commission published an evaluation."},
        ]}
        title, explanation = _reader_copy("practice_before_doctrine", "risk",
                                          {"object": "trade.market_access"}, candidate)
        self.assertNotIn("catches up", title + explanation)
        self.assertIn("customs checks", explanation)

    def test_page_cap_is_25_not_15(self):
        pubs, selection = _select_stage7([], {})
        self.assertEqual(5, selection["page_guarantee"]["slots_per_wow"])
        self.assertEqual(25, selection["page_guarantee"]["slots_per_wow"] * 5)
        self.assertEqual(0, sum(len(x) for x in pubs.values()))


if __name__ == "__main__":
    unittest.main()
