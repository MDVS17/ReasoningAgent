"""Local Fabric IQ-style semantic ontology service."""

import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parents[2]
ONTOLOGY_PATH = BASE_DIR / "knowledge" / "fabric_ontology" / "syntrix_ontology.json"


def load_fabric_ontology() -> dict[str, Any]:
    return json.loads(ONTOLOGY_PATH.read_text(encoding="utf-8"))


def get_fabric_iq_status() -> dict[str, Any]:
    ontology = load_fabric_ontology()
    entities = ontology.get("entities", {})
    relationships = ontology.get("relationships", [])
    return {
        "name": "Fabric IQ",
        "status": "local_demo_ready",
        "mode": ontology.get("mode", "local_demo"),
        "description": "Semantic ontology for users, workflows, agents, guardrails, evaluation, and learning updates.",
        "ontology_source": str(ONTOLOGY_PATH.relative_to(BASE_DIR)),
        "entity_count": len(entities),
        "relationship_count": len(relationships),
        "ontology_entities": list(entities.keys()),
        "signals": [
            {"label": "Ontology entities", "value": len(entities)},
            {"label": "Semantic relationships", "value": len(relationships)},
            {"label": "Lineage model", "value": "ready"},
        ],
    }


def get_fabric_evidence() -> list[dict[str, Any]]:
    ontology = load_fabric_ontology()
    return [
        {
            "layer": "Fabric IQ",
            "source_name": "syntrix_ontology.json",
            "source_path": str(ONTOLOGY_PATH.relative_to(BASE_DIR)),
            "snippet": (
                "Ontology maps UserProfile -> WorkSignal -> WorkPattern -> AgentOpportunity -> "
                "AgentBlueprint -> GovernanceGate, with EvaluationCase and LearningLoopUpdate support."
            ),
            "citation": "syntrix_ontology.json",
            "entities": list(ontology.get("entities", {}).keys()),
            "relationships": ontology.get("relationships", []),
        }
    ]
