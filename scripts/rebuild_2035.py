"""Rebuild only the nested 2035 scenario presentation in existing Radar JSON.

Use after installing the scenario-machine files when you want the page to appear
immediately, without waiting for a full scanner run:

    python scripts/rebuild_2035.py

Future completed scans will rebuild the same block automatically through
high_order_inference.py.
"""
from __future__ import annotations

import json
from pathlib import Path

try:
    from scripts.scenarios_2035 import build_scenarios_2035
except ModuleNotFoundError:  # running from scripts/
    from scenarios_2035 import build_scenarios_2035  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
TARGETS = (ROOT / "radar.json", ROOT / "radar_active.json")


def rebuild(path: Path) -> bool:
    if not path.exists():
        return False
    data = json.loads(path.read_text(encoding="utf-8"))
    hi = data.get("high_order_inference")
    if not isinstance(hi, dict):
        hi = {}
        data["high_order_inference"] = hi
    publications = hi.get("publications") if isinstance(hi.get("publications"), dict) else {}
    candidates = hi.get("candidates") if isinstance(hi.get("candidates"), list) else []
    evaluated_at = str(hi.get("evaluated_at") or data.get("run_completed_at") or data.get("last_updated") or "")
    hi["scenarios_2035"] = build_scenarios_2035(publications, candidates, evaluated_at)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    counts = hi["scenarios_2035"].get("counts", {})
    print(f"rebuilt {path.name}: {counts}")
    return True


if __name__ == "__main__":
    changed = sum(1 for path in TARGETS if rebuild(path))
    if not changed:
        raise SystemExit("No radar.json or radar_active.json found.")
