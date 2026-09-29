"""Evidence-driven 2035 scenario machine.

Structure
---------
1) One fixed 2x2 frame creates four major 2035 worlds.
   X: global economic connectedness (fragmented <-> connected)
   Y: European strategic capacity (thin <-> deep)

2) Each major world gets its own evidence-selected 2x2 sub-frame.  The machine
   chooses two axes from a fixed library of economically meaningful radars.
   The *library* is stable; the *pair selected for each world* can change as the
   Radar evidence changes.

3) Each of the four sub-scenarios gets four conditional variants.  A variant
   inserts one evidence-grounded development: shock, opportunity, trend, or
   risk/constraint.  These are branches of the same structural scenario, not
   extra axes.

The output is deterministic for the same evidence.  Scenario prose is clearly
conditional; concrete trigger material is sourced from the Radar's own
higher-order candidates and their evidence records.
"""
from __future__ import annotations

import hashlib
import re
from typing import Any, Iterable

HORIZON = 2035


def _clean(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def _slug(value: str) -> str:
    out = re.sub(r"[^a-z0-9]+", "-", _clean(value).lower()).strip("-")
    return out or "scenario"


def _stable(value: str) -> int:
    return int(hashlib.sha1(value.encode("utf-8")).hexdigest(), 16)


def _text(*parts: Any) -> str:
    return " ".join(_clean(p).lower() for p in parts if _clean(p))


def _contains(text: str, terms: Iterable[str]) -> int:
    return sum(1 for term in terms if term in text)


# ---------------------------------------------------------------------------
# Fixed major frame.  These two uncertainties are intentionally stable.  They
# describe the external economic environment and Europe's internal capacity to
# act, rather than one temporary policy topic.
# ---------------------------------------------------------------------------
MAJOR_AXES = {
    "x": {
        "id": "global_connectedness",
        "title": "Global economic connectedness",
        "low": "More fragmented / guarded",
        "high": "More connected / open",
        "low_short": "Fragmented links",
        "high_short": "Connected links",
        "question": "How open are trade, investment, technology and partner networks around Europe?",
    },
    "y": {
        "id": "strategic_capacity",
        "title": "European strategic capacity",
        "low": "Thin capacity / few buffers",
        "high": "Deep capacity / more buffers",
        "low_short": "Thin capacity",
        "high_short": "Deep capacity",
        "question": "How much industrial, financial, energy and supply capacity can Europe mobilise?",
    },
}


# DOM position is the visual 2x2 order: top-left, top-right, bottom-left,
# bottom-right.  x_side/y_side are used by the page as coordinates.
MAJOR_WORLDS = (
    {
        "id": "independent_scale",
        "legacy_id": "fortress_frontier",
        "name": "Independent Scale",
        "tagline": "Deep European capacity, but weaker global links.",
        "x_side": "low",
        "y_side": "high",
        "story": (
            "Europe reaches 2035 with stronger industrial, technology and financing capacity, "
            "while trade and investment run through a narrower, more controlled set of relationships."
        ),
        "tradeoff": "Europe gains room to act, but pays for it through narrower access, higher friction and possible retaliation.",
    },
    {
        "id": "connected_growth",
        "legacy_id": "big_commons",
        "name": "Connected Growth",
        "tagline": "Deep European capacity and strong global links.",
        "x_side": "high",
        "y_side": "high",
        "story": (
            "Europe reaches 2035 with more industrial, technology and financing capacity while remaining strongly connected "
            "to global trade, investment and research networks."
        ),
        "tradeoff": "Scale and openness reinforce each other, but external dependencies still transmit shocks quickly.",
    },
    {
        "id": "constrained_europe",
        "legacy_id": "quiet_retreat",
        "name": "Constrained Europe",
        "tagline": "Thin European capacity and weaker global links.",
        "x_side": "low",
        "y_side": "low",
        "story": (
            "Europe reaches 2035 with fewer buffers and weaker global economic links. Governments protect a smaller strategic core "
            "while investment, market access and room for manoeuvre tighten."
        ),
        "tradeoff": "Exposure is reduced in some areas, but so are scale, choice and the resources available to adapt.",
    },
    {
        "id": "open_under_pressure",
        "legacy_id": "brilliant_but_broke",
        "name": "Open Under Pressure",
        "tagline": "Thin European capacity, but strong global links.",
        "x_side": "high",
        "y_side": "low",
        "story": (
            "Europe remains strongly connected to trade, capital and partners in 2035, but carries thin domestic buffers and "
            "depends heavily on outside suppliers, finance and markets."
        ),
        "tradeoff": "Openness preserves access and choice, but weak buffers make concentrated dependencies harder to absorb.",
    },
)


# ---------------------------------------------------------------------------
# Stable sub-axis library.  The selected pair is evidence-driven.
# category prevents the machine from choosing two near-duplicate axes.
# ---------------------------------------------------------------------------
AXIS_LIBRARY = (
    {
        "id": "input_resilience",
        "category": "inputs",
        "title": "Critical-input resilience",
        "low": "Concentrated / brittle inputs",
        "high": "Diversified / buffered inputs",
        "low_short": "Input exposure",
        "high_short": "Input resilience",
        "question": "Are critical materials, components and supply routes concentrated or buffered?",
        "keywords": (
            "critical raw", "raw material", "materials", "supply chain", "supplier", "dependency", "dependencies",
            "chokepoint", "shortage", "storage", "resilience", "diversification", "lng", "gas supply", "semiconductor",
        ),
    },
    {
        "id": "technology_control",
        "category": "technology",
        "title": "Control of critical technology",
        "low": "External technology dependence",
        "high": "European technology control",
        "low_short": "Tech dependence",
        "high_short": "Tech control",
        "question": "Who controls the critical technologies, compute, infrastructure and know-how Europe depends on?",
        "keywords": (
            "technology", "digital sovereignty", "quantum", "ai ", "artificial intelligence", "compute", "chips",
            "semiconductor", "dual-use", "dual use", "research security", "export control", "cyber", "data", "telecom",
        ),
    },
    {
        "id": "capital_mobilisation",
        "category": "capital",
        "title": "Strategic capital mobilisation",
        "low": "Capital constrained",
        "high": "Investment at scale",
        "low_short": "Capital constraint",
        "high_short": "Capital at scale",
        "question": "Can Europe mobilise enough public and private capital for strategic projects?",
        "keywords": (
            "funding", "finance", "financing", "investment", "capital", "budget", "eib", "state aid", "fund",
            "acquisition", "industrial policy", "competitiveness", "scale-up", "scale up",
        ),
    },
    {
        "id": "partner_diversification",
        "category": "external",
        "title": "Partner diversification",
        "low": "Narrow / concentrated partners",
        "high": "Broad / diversified partners",
        "low_short": "Narrow partners",
        "high_short": "Diversified partners",
        "question": "Does Europe depend on a narrow partner set or maintain multiple credible economic routes?",
        "keywords": (
            "partnership", "agreement", "market access", "trade", "wto", "global gateway", "cooperation", "alliance",
            "china", "united states", " u.s.", " us ", "africa", "latin america", "india", "japan", "partner",
        ),
    },
    {
        "id": "economic_security_controls",
        "category": "controls",
        "title": "Economic-security controls",
        "low": "Light / permissive controls",
        "high": "Tight / interventionist controls",
        "low_short": "Light controls",
        "high_short": "Tight controls",
        "question": "How strongly are investment, exports, subsidies, suppliers and trade screened or restricted?",
        "keywords": (
            "sanction", "screening", "export control", "dual-use", "dual use", "trade defence", "trade defense",
            "foreign subsidies", "anti-coercion", "anti coercion", "high-risk vendor", "high risk vendor", "tariff",
            "economic security", "de-risk", "derisk", "restrict", "control list",
        ),
    },
    {
        "id": "european_coordination",
        "category": "governance",
        "title": "European coordination",
        "low": "Fragmented national action",
        "high": "Coordinated European action",
        "low_short": "Fragmented action",
        "high_short": "EU coordination",
        "question": "Do European actors pool decisions and capacity, or respond mainly through separate national choices?",
        "keywords": (
            "european union", " eu ", "commission", "member state", "single market", "joint", "common", "coordination",
            "framework", "union", "europe-level", "europe level", "shared", "collective",
        ),
    },
    {
        "id": "energy_resilience",
        "category": "energy",
        "title": "Energy-system resilience",
        "low": "Constrained / volatile energy",
        "high": "Secure / flexible energy",
        "low_short": "Energy constraint",
        "high_short": "Energy resilience",
        "question": "Can Europe's energy system absorb supply, price and infrastructure stress?",
        "keywords": (
            "energy", "gas", "lng", "electricity", "grid", "hydrogen", "storage", "power", "renewable", "oil",
            "energy security", "pipeline", "interconnector",
        ),
    },
    {
        "id": "industrial_capacity",
        "category": "industry",
        "title": "Industrial mobilisation",
        "low": "Thin production base",
        "high": "Scaled production base",
        "low_short": "Thin production",
        "high_short": "Scaled production",
        "question": "Can Europe expand strategic production fast enough when demand or security needs rise?",
        "keywords": (
            "industry", "industrial", "manufacturing", "production", "factory", "capacity", "strategic sectors",
            "defence production", "defense production", "equipment", "scale", "supply capacity", "decarbonisation",
        ),
    },
)

AXIS_BY_ID = {axis["id"]: axis for axis in AXIS_LIBRARY}

# Contextual priors do not decide the axes by themselves.  They make a relevant
# signal more useful inside a particular major world.
WORLD_AXIS_POOLS = {
    "connected_growth": {"partner_diversification", "technology_control", "capital_mobilisation", "input_resilience"},
    "independent_scale": {"economic_security_controls", "technology_control", "industrial_capacity", "european_coordination"},
    "open_under_pressure": {"input_resilience", "capital_mobilisation", "partner_diversification", "energy_resilience"},
    "constrained_europe": {"input_resilience", "energy_resilience", "capital_mobilisation", "european_coordination"},
}

WORLD_AXIS_PRIORS = {
    "connected_growth": {
        "partner_diversification": 1.40,
        "technology_control": 1.80,
        "capital_mobilisation": 1.50,
        "input_resilience": 1.10,
    },
    "independent_scale": {
        "economic_security_controls": 1.80,
        "technology_control": 1.65,
        "industrial_capacity": 1.45,
        "european_coordination": 0.75,
    },
    "open_under_pressure": {
        "input_resilience": 1.70,
        "capital_mobilisation": 1.70,
        "energy_resilience": 1.50,
        "partner_diversification": 0.90,
    },
    "constrained_europe": {
        "input_resilience": 1.70,
        "energy_resilience": 1.80,
        "capital_mobilisation": 1.50,
        "european_coordination": 0.70,
    },
}


MODE_KEYWORDS = {
    "shock": (
        "war", "conflict", "crisis", "shock", "disruption", "blockade", "outage", "attack", "breach", "emergency",
        "sanction", "tariff", "ban", "shortage", "supply cut", "retaliat", "hormuz", "weapon",
    ),
    "opportunity": (
        "investment", "agreement", "partnership", "platform", "funding", "breakthrough", "expand", "cooperation",
        "initiative", "new capacity", "gateway", "association", "innovation", "acquire", "build",
    ),
    "trend": (
        "growth", "increase", "rising", "shift", "continue", "accelerat", "diversif", "adoption", "transition",
        "framework", "sovereignty", "formal policy", "turn", "emerg", "expansion",
    ),
    "risk": (
        "risk", "dependency", "blind spot", "vulnerab", "concentration", "low storage", "shortage", "coercion",
        "pressure", "bottleneck", "constraint", "retaliat", "weak", "exposure", "failure",
    ),
}

MODE_LABELS = {
    "shock": "Shock inserted",
    "opportunity": "Opportunity inserted",
    "trend": "Trend accelerated",
    "risk": "Risk crystallises",
}


# ---------------------------------------------------------------------------
# Evidence extraction
# ---------------------------------------------------------------------------
def _candidate_title(candidate: dict[str, Any]) -> str:
    if _clean(candidate.get("product")) == "trend":
        balance = candidate.get("trend_balance") if isinstance(candidate.get("trend_balance"), dict) else {}
        left = _clean(balance.get("left_title"))
        right = _clean(balance.get("right_title"))
        if left and right:
            return f"{left} vs {right}"
    return _clean(candidate.get("reader_title") or candidate.get("title") or candidate.get("topic_label") or candidate.get("id"))


def _record_ref(record: dict[str, Any]) -> dict[str, str]:
    return {
        "title": _clean(record.get("title")),
        "source": _clean(record.get("source")),
        "date": _clean(record.get("date"))[:10],
        "link": _clean(record.get("link")),
    }


def _collect_evidence(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    for candidate in candidates:
        if not isinstance(candidate, dict):
            continue
        cid = _clean(candidate.get("id"))
        product = _clean(candidate.get("product")) or "finding"
        status = _clean(candidate.get("status")) or "unknown"
        topic = _clean(candidate.get("topic_label"))
        candidate_text = _text(
            _candidate_title(candidate),
            candidate.get("reader_summary"),
            topic,
            candidate.get("object"),
            " ".join(_clean(x) for x in (candidate.get("endpoint_objects") or []) if _clean(x)),
        )
        key = f"finding:{cid}"
        if cid and key not in seen:
            seen.add(key)
            out.append({
                "id": key,
                "candidate_id": cid,
                "product": product,
                "status": status,
                "topic": topic,
                "title": _candidate_title(candidate),
                "source": "Radar finding",
                "date": _clean(candidate.get("last_updated_at"))[:10],
                "link": "",
                "quality": float(candidate.get("score", 50) or 50),
                "candidate_text": candidate_text,
                "text": candidate_text,
            })
        for lane in ("support", "context", "against"):
            records = candidate.get(lane) if isinstance(candidate.get(lane), list) else []
            for record in records:
                if not isinstance(record, dict):
                    continue
                ref = _record_ref(record)
                if not ref["title"]:
                    continue
                identity = _clean(record.get("identity") or record.get("link") or ref["title"])
                rkey = f"record:{identity}"
                if rkey in seen:
                    continue
                seen.add(rkey)
                out.append({
                    "id": rkey,
                    "candidate_id": cid,
                    "product": product,
                    "status": status,
                    "topic": topic,
                    **ref,
                    "quality": float(record.get("quality", 50) or 50),
                    "candidate_text": candidate_text,
                    "text": _text(ref["title"], ref["source"], topic, candidate_text),
                    "lane": lane,
                })
    return out


def _publication_ids(publications: dict[str, Any]) -> set[str]:
    ids: set[str] = set()
    for value in publications.values() if isinstance(publications, dict) else []:
        if isinstance(value, list):
            ids.update(_clean(v) for v in value if _clean(v))
    return ids


def _candidate_weight(candidate: dict[str, Any], published: set[str]) -> float:
    status = _clean(candidate.get("status"))
    status_weight = {"qualified": 1.35, "watch": 1.0, "dormant": 0.65, "killed": 0.2}.get(status, 0.8)
    cid = _clean(candidate.get("id"))
    pub_weight = 1.22 if cid in published else 1.0
    try:
        score = max(0.2, min(1.4, float(candidate.get("score", 50) or 50) / 75.0))
    except (TypeError, ValueError):
        score = 0.8
    return status_weight * pub_weight * score


def _axis_scores(world_id: str, candidates: list[dict[str, Any]], publications: dict[str, Any]) -> list[dict[str, Any]]:
    published = _publication_ids(publications)
    rows: list[dict[str, Any]] = []
    priors = WORLD_AXIS_PRIORS.get(world_id, {})
    pool = WORLD_AXIS_POOLS.get(world_id)
    for axis in AXIS_LIBRARY:
        if pool and axis["id"] not in pool:
            continue
        score = 0.0
        basis: list[tuple[float, str, str]] = []
        for candidate in candidates:
            if not isinstance(candidate, dict):
                continue
            title = _candidate_title(candidate)
            ctext = _text(
                title,
                candidate.get("reader_summary"),
                candidate.get("topic_label"),
                candidate.get("object"),
                " ".join(_clean(x) for x in (candidate.get("endpoint_objects") or []) if _clean(x)),
                " ".join(_clean(r.get("title")) for r in (candidate.get("support") or []) if isinstance(r, dict)),
                " ".join(_clean(r.get("title")) for r in (candidate.get("context") or []) if isinstance(r, dict)),
            )
            hits = _contains(ctext, axis["keywords"])
            if not hits:
                continue
            contribution = min(5.0, 1.0 + hits * 0.65) * _candidate_weight(candidate, published)
            score += contribution
            basis.append((contribution, _clean(candidate.get("id")), title))
        # Tiny deterministic floor means an empty/young radar still produces a
        # complete frame, but real evidence rapidly dominates it.
        score = (score + 0.05) * float(priors.get(axis["id"], 1.0))
        basis.sort(key=lambda x: (-x[0], x[1]))
        rows.append({
            "axis": axis,
            "score": round(score, 3),
            "basis": [
                {"finding_id": cid, "title": title, "weight": round(weight, 3)}
                for weight, cid, title in basis[:4]
                if cid
            ],
        })
    rows.sort(key=lambda r: (-r["score"], _stable(world_id + r["axis"]["id"])))
    return rows


def _select_axes(world_id: str, candidates: list[dict[str, Any]], publications: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any], list[dict[str, Any]]]:
    ranked = _axis_scores(world_id, candidates, publications)
    first = ranked[0]
    second = next((r for r in ranked[1:] if r["axis"]["category"] != first["axis"]["category"]), ranked[1])
    # Put the more externally oriented axis on X when possible; this makes
    # repeated frames easier to read without changing what was selected.
    external_categories = {"external", "controls", "inputs", "energy"}
    if second["axis"]["category"] in external_categories and first["axis"]["category"] not in external_categories:
        first, second = second, first
    return first, second, ranked


# ---------------------------------------------------------------------------
# Sub-scenarios and leaf variants
# ---------------------------------------------------------------------------
def _side(axis: dict[str, Any], which: str) -> str:
    return axis["high_short"] if which == "high" else axis["low_short"]


def _sub_name(x_axis: dict[str, Any], y_axis: dict[str, Any], x_side: str, y_side: str) -> str:
    return f"{_side(y_axis, y_side)} + {_side(x_axis, x_side)}"


def _sub_story(parent: dict[str, Any], x_axis: dict[str, Any], y_axis: dict[str, Any], x_side: str, y_side: str) -> str:
    return (
        f"Inside {parent['name']}, this branch combines {_side(x_axis, x_side).lower()} with "
        f"{_side(y_axis, y_side).lower()}. The parent world's assumptions stay fixed; only these two "
        "second-order uncertainties are resolved differently."
    )


def _evidence_score(item: dict[str, Any], mode: str, axes: tuple[dict[str, Any], dict[str, Any]], parent_id: str, used: set[str]) -> tuple[float, int]:
    text = _clean(item.get("text")).lower()
    score = 0.0
    # Axis relevance matters most.
    score += 1.5 * sum(_contains(text, axis["keywords"]) for axis in axes)
    score += 2.2 * _contains(text, MODE_KEYWORDS[mode])
    product = _clean(item.get("product"))
    if product == mode:
        score += 5.0
    elif mode == "trend" and product == "continuity":
        score += 2.0
    elif mode == "risk" and product in {"risk", "continuity"}:
        score += 2.0
    status = _clean(item.get("status"))
    score += {"qualified": 1.2, "watch": 0.7, "dormant": 0.2}.get(status, 0.35)
    try:
        score += min(1.2, float(item.get("quality", 50) or 50) / 100.0)
    except (TypeError, ValueError):
        pass
    if item.get("id") in used:
        score -= 7.0
    # Prefer concrete evidence records over the abstract finding when scores tie.
    if str(item.get("id", "")).startswith("record:"):
        score += 0.4
    return score, _stable(parent_id + mode + _clean(item.get("id")))


def _pick_evidence(evidence: list[dict[str, Any]], mode: str, axes: tuple[dict[str, Any], dict[str, Any]], parent_id: str, used: set[str]) -> dict[str, Any] | None:
    if not evidence:
        return None
    ranked = sorted(evidence, key=lambda item: (-_evidence_score(item, mode, axes, parent_id, used)[0], _evidence_score(item, mode, axes, parent_id, used)[1]))
    picked = ranked[0]
    used.add(_clean(picked.get("id")))
    return picked


def _mechanism(axis: dict[str, Any], side: str) -> str:
    if side == "high":
        return f"the system leans toward {axis['high'].lower()}"
    return f"the system leans toward {axis['low'].lower()}"


def _variant_story(mode: str, seed: dict[str, Any] | None, sub: dict[str, Any], x_axis: dict[str, Any], y_axis: dict[str, Any]) -> list[str]:
    title = _clean(seed.get("title")) if seed else "a new development picked up by the Radar"
    mechanism = f"{_mechanism(x_axis, sub['x_side'])}, while {_mechanism(y_axis, sub['y_side'])}"
    if mode == "shock":
        first = f"Stress test: if the pressure visible in “{title}” becomes a larger external shock, this branch is forced to react quickly."
        second = f"Because {mechanism}, the shock tests which dependency or buffer fails first."
    elif mode == "opportunity":
        first = f"Upside branch: if the opening visible in “{title}” scales, Europe gets a chance to improve its position inside this scenario."
        second = f"Because {mechanism}, the opportunity changes who can invest, supply or cooperate without changing the parent world itself."
    elif mode == "trend":
        first = f"Acceleration branch: if the direction visible in “{title}” persists toward 2035, it becomes part of the operating environment."
        second = f"Because {mechanism}, the trend reinforces one side of this sub-scenario and makes reversal harder."
    else:
        first = f"Failure branch: if the weakness visible in “{title}” hardens, a manageable exposure becomes a structural constraint."
        second = f"Because {mechanism}, the cost appears as lost choice, slower adjustment or greater dependence."
    return [first, second]


def _variant(mode: str, seed: dict[str, Any] | None, sub: dict[str, Any], x_axis: dict[str, Any], y_axis: dict[str, Any], number: int) -> dict[str, Any]:
    title = _clean(seed.get("title")) if seed else "Radar development"
    short = title.rstrip(".?!")
    if len(short) > 82:
        short = short[:79].rstrip() + "…"
    evidence = None
    if seed:
        evidence = {
            "finding_id": _clean(seed.get("candidate_id")),
            "title": _clean(seed.get("title")),
            "source": _clean(seed.get("source")),
            "date": _clean(seed.get("date")),
            "link": _clean(seed.get("link")),
            "product": _clean(seed.get("product")),
        }
    return {
        "id": f"{sub['id']}:{mode}",
        "kind": mode,
        "label": MODE_LABELS[mode],
        "name": f"{MODE_LABELS[mode]}: {short}",
        "trigger": title,
        "story": _variant_story(mode, seed, sub, x_axis, y_axis),
        "evidence": evidence,
        "order": number,
    }


def _build_subframe(parent: dict[str, Any], candidates: list[dict[str, Any]], publications: dict[str, Any], evidence: list[dict[str, Any]], globally_used: set[str]) -> dict[str, Any]:
    x_rank, y_rank, ranking = _select_axes(parent["id"], candidates, publications)
    x_axis = dict(x_rank["axis"])
    y_axis = dict(y_rank["axis"])
    x_axis["selection_score"] = x_rank["score"]
    x_axis["basis"] = x_rank["basis"]
    y_axis["selection_score"] = y_rank["score"]
    y_axis["basis"] = y_rank["basis"]

    quadrants = (
        ("low", "high"),   # top-left
        ("high", "high"),  # top-right
        ("low", "low"),    # bottom-left
        ("high", "low"),   # bottom-right
    )
    subs: list[dict[str, Any]] = []
    for idx, (x_side, y_side) in enumerate(quadrants, start=1):
        name = _sub_name(x_axis, y_axis, x_side, y_side)
        sub = {
            "id": f"{parent['id']}:sub:{idx}",
            "name": name,
            "tagline": f"{x_axis['title']}: {_side(x_axis, x_side)} · {y_axis['title']}: {_side(y_axis, y_side)}",
            "x_side": x_side,
            "y_side": y_side,
            "story": _sub_story(parent, x_axis, y_axis, x_side, y_side),
            "order": idx,
        }
        variants = []
        for number, mode in enumerate(("shock", "opportunity", "trend", "risk"), start=1):
            seed = _pick_evidence(evidence, mode, (x_axis, y_axis), sub["id"], globally_used)
            variants.append(_variant(mode, seed, sub, x_axis, y_axis, number))
        sub["variants"] = variants
        subs.append(sub)

    return {
        "id": f"{parent['id']}:frame",
        "title": f"Inside {parent['name']}",
        "question": f"Which two uncertainties matter most inside {parent['name']} given the current Radar?",
        "x_axis": x_axis,
        "y_axis": y_axis,
        "selection": {
            "method": "Two highest evidence-relevant axes from the fixed axis library, with near-duplicate categories prevented and a world-context relevance prior.",
            "ranked_axes": [
                {"id": row["axis"]["id"], "title": row["axis"]["title"], "score": row["score"], "basis": row["basis"]}
                for row in ranking
            ],
        },
        "scenarios": subs,
    }


# ---------------------------------------------------------------------------
# Public builder
# ---------------------------------------------------------------------------
def build_scenarios_2035(publications: dict[str, Any], candidates: list[dict[str, Any]], evaluated_at: str = "") -> dict[str, Any]:
    publications = publications if isinstance(publications, dict) else {}
    candidates = [c for c in (candidates or []) if isinstance(c, dict)]
    evidence = _collect_evidence(candidates)
    scenarios: list[dict[str, Any]] = []
    for position, world_template in enumerate(MAJOR_WORLDS, start=1):
        world = dict(world_template)
        world["order"] = position
        world["coordinates"] = {
            "x": MAJOR_AXES["x"][world["x_side"]],
            "y": MAJOR_AXES["y"][world["y_side"]],
        }
        world["subframe"] = _build_subframe(world, candidates, publications, evidence, set())
        world["bullets"] = [
            {"label": "2035 picture", "text": world["story"]},
            {"label": "Trade-off", "text": world["tradeoff"]},
            {"label": "Sub-frame", "text": f"The current Radar selects {world['subframe']['x_axis']['title']} and {world['subframe']['y_axis']['title']} as the two second-order uncertainties for this world."},
        ]
        # Kept for older reader-language tooling.  The actual UI uses nested
        # subframe.scenarios[*].variants.
        world["variants"] = []
        scenarios.append(world)

    return {
        "horizon": HORIZON,
        "evaluated_at": evaluated_at,
        "model": "fixed-major-2x2__evidence-selected-sub-2x2__four-conditional-variants",
        "counts": {"major": 4, "subscenarios": 16, "leaf_variants": 64, "total_nodes": 84},
        "axes": MAJOR_AXES,
        "axis_library": [
            {k: v for k, v in axis.items() if k != "keywords"}
            for axis in AXIS_LIBRARY
        ],
        "method": {
            "major": "The first 2x2 is fixed in advance: global economic connectedness × European strategic capacity.",
            "sub": "Each major world independently selects a 2x2 from a stable library using the current Radar candidates and evidence.",
            "leaf": "Each sub-scenario keeps its structural assumptions and receives four conditional branches: shock, opportunity, trend acceleration and risk crystallisation.",
        },
        "evidence_pool_size": len(evidence),
        "scenarios": scenarios,
    }
