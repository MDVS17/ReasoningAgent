"""Lightweight QA checks for Syntrix Reasoning Engine v1."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from agents import load_interactions  # noqa: E402
from backend.services.syntrix_pipeline import analyze  # noqa: E402


def run_reasoning_engine_qa(profile: str = "All roles") -> dict[str, Any]:
    interactions = load_interactions()
    result = analyze(profile)

    checks = {
        "synthetic_data_loads": len(interactions) > 0,
        "reasoning_pipeline_runs": bool(result.get("master_agent_summary")) and bool(result.get("reasoning_trace")),
        "at_least_3_opportunities_scored": len(result.get("opportunity_scores", [])) >= 3,
        "blueprint_generated": bool(result.get("recommended_blueprint", {}).get("agent_name")),
        "governance_gates_present": len(result.get("governance_gates", [])) >= 5,
        "learning_loop_recommendation_present": bool(result.get("learning_loop_recommendation", {}).get("recommendation")),
    }

    return {
        "profile": profile,
        "passed": all(checks.values()),
        "checks": checks,
        "top_recommendation": result.get("master_agent_summary", {}).get("top_recommendation"),
        "opportunities_scored": len(result.get("opportunity_scores", [])),
    }


if __name__ == "__main__":
    report = run_reasoning_engine_qa()
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["passed"] else 1)
