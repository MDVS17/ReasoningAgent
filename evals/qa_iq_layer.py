"""Lightweight QA checks for Syntrix IQ Layer v1."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from backend.services.iq_layer_service import get_iq_evidence, get_iq_layer_status, retrieve_iq_evidence  # noqa: E402
from backend.services.syntrix_pipeline import analyze  # noqa: E402


def run_iq_layer_qa() -> dict[str, Any]:
    status = get_iq_layer_status()
    evidence = get_iq_evidence(profile="Project Manager", workflow="Risk and dependency tracker")
    retrieval = retrieve_iq_evidence("governance approval blueprint", profile="Project Manager")
    analysis = analyze("Project Manager")
    blueprint = analysis.get("recommended_blueprint", {})

    checks = {
        "foundry_pack_loaded": status["foundry_iq"]["document_count"] >= 5,
        "fabric_ontology_loaded": status["fabric_iq"]["entity_count"] >= 8,
        "work_iq_signals_loaded": status["work_iq"]["signals"][-1]["value"] >= 7,
        "evidence_has_citations": len(evidence["citations"]) >= 3,
        "retrieve_returns_snippets": len(retrieval["evidence"]) >= 3,
        "analyze_blueprint_has_iq_alignment": bool(blueprint.get("iq_alignment")),
        "analyze_blueprint_has_citations": len(blueprint.get("citations", [])) >= 3,
    }

    return {
        "passed": all(checks.values()),
        "checks": checks,
        "citations": evidence["citations"],
        "blueprint": blueprint.get("agent_name"),
    }


if __name__ == "__main__":
    report = run_iq_layer_qa()
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["passed"] else 1)
