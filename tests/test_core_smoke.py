"""Pre-scan gate for the slim radar template.

Replaces the 87-file version-by-version legacy suite. Checks only what must hold
for a scan to be safe: modules import, topic files parse, reasoning runs on an
empty corpus, the active-corpus rebuild works, and every page asset resolves.
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

CORE_MODULES = [
    "scan_radar", "scanner_run_guard", "high_order_inference", "shock_inference",
    "claim_reasoning_live", "claim_reasoning_shadow", "claims_schema", "scenarios_2035",
    "active_corpus", "rebuild_active_radar", "downstream_retrace", "deep_read_works",
    "deep_scan_work_state", "prepare_deep_scan_package", "import_deep_scan_results",
]

TOPIC_FILES = [
    "radar_config.json", "radar_phrase_rules.json", "claims_vocabulary.json",
    "priority_people.json", "curator_candidate_inputs.json", "radar_seed.json",
    "historical/config.json", "historical/historical_seed.json",
    "historical/curated_seed_evidence.json", "historical/manual_evidence.json",
    "reader_language/approved.json", "topic_lexicon.json",
]


class CoreSmoke(unittest.TestCase):
    def test_core_modules_import(self):
        import importlib
        for name in CORE_MODULES:
            with self.subTest(module=name):
                importlib.import_module(f"scripts.{name}")

    def test_topic_files_parse(self):
        for rel in TOPIC_FILES:
            with self.subTest(file=rel):
                self.assertIsInstance(json.loads((ROOT / rel).read_text(encoding="utf-8")), dict)

    def test_topic_lexicon_complete(self):
        import scripts.scan_radar as S
        self.assertTrue(S.THEMES and S.RI_STRONG and S.GEO_STRONG and S.EU_DIRECT)

    def test_strand_b_disabled(self):
        import scripts.scan_radar as S
        cfg = json.loads((ROOT / "radar_config.json").read_text(encoding="utf-8"))
        self.assertFalse(cfg.get("strand_b_enabled", True))
        self.assertFalse(S._b_method_evidence("Scenario method", "a new foresight method", "", "journal", 1)[0])

    def test_propaganda_sources_blocked(self):
        import scripts.scan_radar as S
        blocked = [("Global Times", "globaltimes.cn", ""), ("Sputnik Globe", "", ""),
                   ("", "", "https://pravda-fr.com/x"), ("RT DE", "rtde.tech", ""),
                   ("Strategic Culture Foundation", "", ""), ("Russia in Global Affairs", "", ""),
                   ("", "", "https://english.news.cn/x")]
        for src, dom, link in blocked:
            with self.subTest(source=src or dom or link):
                self.assertTrue(S.source_integrity_hard_block(src, dom, link)[0])
        allowed = [("Reuters", "reuters.com", ""), ("Journal of Contemporary China", "", ""),
                   ("", "", "https://www.courtsport.com/"), ("", "", "https://www.merics.org/en")]
        for src, dom, link in allowed:
            with self.subTest(source=src or dom or link):
                self.assertFalse(S.source_integrity_hard_block(src, dom, link)[0])
        self.assertFalse(S.trusted_independent_c_source("Global Times", "globaltimes.cn"))
        self.assertFalse(S.trusted_independent_c_source("Some Blog", "someblog.net"))
        self.assertTrue(S.trusted_independent_c_source("Reuters", "reuters.com"))

    def test_claims_vocabulary_loads(self):
        from scripts.claims_schema import load_vocabulary
        self.assertTrue(load_vocabulary())

    def test_reasoning_runs_on_empty_corpus(self):
        from scripts.high_order_inference import refresh_high_order_inference
        from scripts.shock_inference import refresh_shock_inference
        doc = {"strand_a": [], "strand_b": [], "strand_c": []}
        self.assertIsInstance(refresh_shock_inference(doc, {}, "2026-01-01T00:00:00Z"), dict)
        self.assertIsInstance(refresh_high_order_inference(doc, {}, "2026-01-01T00:00:00Z"), dict)

    def test_rebuild_active_on_empty_repo(self):
        with tempfile.TemporaryDirectory() as tmp:
            t = Path(tmp)
            (t / "radar.json").write_text(json.dumps({"strand_a": [], "strand_b": [], "strand_c": []}))
            for name in ("admission_state.json", "record_corrections.json", "reader_text.json"):
                (t / name).write_text("{}")
            proc = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "rebuild_active_radar.py"),
                 "--radar", str(t / "radar.json"), "--admission", str(t / "admission_state.json"),
                 "--corrections", str(t / "record_corrections.json"), "--reader", str(t / "reader_text.json"),
                 "--active-output", str(t / "radar_active.json")],
                cwd=ROOT, capture_output=True, text=True, timeout=300,
            )
            self.assertEqual(proc.returncode, 0, (proc.stdout + proc.stderr)[-3000:])
            self.assertTrue((t / "radar_active.json").is_file())

    @unittest.skipUnless(shutil.which("node"), "node not installed")
    def test_frontier_bridge_accepts_empty_corpus(self):
        proc = subprocess.run(["node", str(ROOT / "scripts" / "frontier_coverage.js")],
                              input="{}", capture_output=True, text=True, cwd=ROOT, timeout=60)
        self.assertEqual(proc.returncode, 0, proc.stderr[-2000:])
        self.assertIn("counts", json.loads(proc.stdout))

    def test_every_page_asset_resolves(self):
        ref = re.compile(r'(?:src|href)="([^"#:?]+\.(?:js|css))')
        for page in ROOT.rglob("*.html"):
            for asset in ref.findall(page.read_text(encoding="utf-8")):
                with self.subTest(page=str(page.relative_to(ROOT)), asset=asset):
                    self.assertTrue((page.parent / asset).resolve().is_file())

    def test_workflows_reference_existing_scripts(self):
        call = re.compile(r"(?:python3?|node) (scripts/[\w./-]+|historical/[\w./-]+)")
        for wf in (ROOT / ".github" / "workflows").glob("*.yml"):
            for path in call.findall(wf.read_text(encoding="utf-8")):
                with self.subTest(workflow=wf.name, script=path):
                    self.assertTrue((ROOT / path).is_file())


if __name__ == "__main__":
    unittest.main()
