"""Regression tests for bounded, labelled cross-object opportunity discovery."""
from __future__ import annotations

import unittest

from scripts.claims_schema import load_vocabulary
from scripts.claim_reasoning_shadow import adjacent_conversion_candidates
from scripts.claim_reasoning_live import _presentation_ready, _reader_copy, _select_stage7


def node(claim_id: str, source: str, obj: str, kind: str, text: str,
         status: str = "delivered") -> dict:
    return {
        "claim_id": claim_id, "_record_id": claim_id, "_source": source,
        "object": obj, "secondary_objects": [], "_primary": True, "era": "current",
        "kind": kind, "text": text, "status": status, "status_date": "2026-10-10",
        "merit": 82,
    }


class OpportunityBridgeTests(unittest.TestCase):
    def setUp(self):
        self.vocab = load_vocabulary()
        self.need = node("need-1", "Research Institute", "defence.production_capacity", "diagnosis",
            "European defence production capacity is restricted by weak industrial capacity and delays.")
        self.action = node("measure-1", "European Commission", "defence.drone_capability", "action",
            "The EU launched a drone industrial cooperation programme to expand production capacity.", "operating")

    def test_separate_sources_create_testable_hypothesis_without_live_connection(self):
        candidates = adjacent_conversion_candidates([self.need, self.action], self.vocab)
        self.assertEqual(1, len(candidates))
        c = candidates[0]
        self.assertEqual("opportunity", c["product"])
        self.assertTrue(c["hypothesis_bridge"])
        self.assertFalse(c["connection_evidenced"])
        self.assertEqual([], c["missing_roles"])
        self.assertEqual(2, len(c["claim_ids"]))
        title, summary = _reader_copy("adjacent_conversion", "opportunity", c, {})
        self.assertIn("Could", title)
        self.assertIn("These sources do not establish a direct connection", summary)
        self.assertIn("Potential obstacle or research question", summary)
        self.assertIn("industrial cooperation", summary)

    def test_same_source_or_same_record_is_not_independent(self):
        self.assertFalse(adjacent_conversion_candidates([self.need, dict(self.action, _source="Research Institute")], self.vocab))
        self.assertFalse(adjacent_conversion_candidates([self.need, dict(self.action, _record_id="need-1")], self.vocab))

    def test_no_cross_namespace_or_unrelated_object(self):
        cross = dict(self.action, object="trade.market_access")
        self.assertFalse(adjacent_conversion_candidates([self.need, cross], self.vocab))

    def test_no_topic_tag_only_or_announced_intent_pass(self):
        unrelated = dict(self.action, text="The EU launched a programme to strengthen generic industrial capacity.")
        self.assertFalse(adjacent_conversion_candidates([self.need, unrelated], self.vocab))
        proposed = dict(self.action, status="proposed")
        self.assertFalse(adjacent_conversion_candidates([self.need, proposed], self.vocab))

    def test_shared_single_anchor_does_not_erase_distinct_argument(self):
        anchor = {"identity": "source-A", "source": "Commission", "source_statement":
                  "The Commission launched a drone programme to improve capabilities."}
        need = {"identity": "source-B", "source": "Institute", "source_statement":
                "European defence production capacity remains constrained."}
        baseline = {"id": "a", "claim_native": True, "product": "opportunity",
                    "grammar_id": "corroborated_claim", "status": "watch", "wow": 2,
                    "topic_key": "corroborated_claim|opportunity|defence.drone_capability",
                    "object": "defence.drone_capability", "score": 80,
                    "primary_sources": 1, "primary_records": 1,
                    "direction_grounded_sources": 1, "direction_grounded_records": 1,
                    "evidence_semantic_alignment": True, "support": [anchor],
                    "reader_title": "EU drone programme begins"}
        bridge = {"id": "b", "claim_native": True, "product": "opportunity",
                  "grammar_id": "adjacent_conversion", "status": "watch", "wow": 3,
                  "topic_key": "adjacent_conversion|defence.production_capacity|defence.drone_capability",
                  "endpoint_objects": ["defence.production_capacity", "defence.drone_capability"],
                  "hypothesis_bridge": True, "score": 82, "primary_sources": 2,
                  "primary_records": 2, "support": [anchor, need],
                  "reader_title": "Could the drone programme reduce the production shortfall?"}
        publications, meta = _select_stage7([baseline, bridge], {})
        self.assertEqual({"a", "b"}, set(publications["opportunity"]))
        self.assertEqual(0, meta["opportunity"]["folded"])

    def test_reader_gate_separates_evidence_and_hypothesis(self):
        c = {"product": "opportunity", "grammar_id": "adjacent_conversion",
             "hypothesis_bridge": True, "maturity_score": 64,
             "primary_sources": 2, "primary_records": 2,
             "support": [{"source_statement": "European defence industrial production faces capacity constraints."},
                         {"source_statement": "The EU launched a drone programme to improve capacity."}],
             "role_strength_floor_passes": True}
        self.assertTrue(_presentation_ready(c)[0])
        self.assertFalse(_presentation_ready(dict(c, hypothesis_bridge=False))[0])
        self.assertFalse(_presentation_ready(dict(c, primary_sources=1))[0])
        self.assertFalse(_presentation_ready(dict(c, support=c["support"][:1]))[0])
        self.assertFalse(_presentation_ready({"product": "opportunity", "grammar_id": "latent_channel",
            "level": 5, "missing_roles": ["live_connection"], "maturity_score": 99,
            "primary_sources": 4, "primary_records": 4})[0])


if __name__ == "__main__":
    unittest.main()
