"""Synthetic Microsoft Fabric IQ ontology signals."""


def get_fabric_iq_status() -> dict:
    return {
        "name": "Fabric IQ",
        "status": "simulated",
        "description": "Represents how Syntrix could map workflows, roles, and business entities into governed enterprise semantics.",
        "ontology_entities": [
            "SyntheticUserProfile",
            "WorkflowPattern",
            "AgentOpportunity",
            "GovernanceControl",
            "EvaluationResult",
        ],
        "signals": [
            {"label": "Semantic consistency", "score": 87},
            {"label": "Lineage clarity", "score": 90},
            {"label": "Synthetic data boundary", "score": 100},
        ],
        "demo_note": "No real Fabric tenant or enterprise data is used.",
    }
