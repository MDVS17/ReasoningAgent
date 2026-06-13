"""Syntrix IQ Layer v1 orchestration service."""

from typing import Any

from backend.services.fabric_iq_service import get_fabric_evidence, get_fabric_iq_status
from backend.services.foundry_iq_service import get_foundry_iq_status, retrieve_foundry_evidence
from backend.services.work_iq_service import get_work_iq_evidence, get_work_iq_status


def get_iq_layer_status() -> dict[str, Any]:
    return {
        "mode": "local_demo",
        "requires_credentials": False,
        "foundry_iq": get_foundry_iq_status(),
        "fabric_iq": get_fabric_iq_status(),
        "work_iq": get_work_iq_status(),
    }


def get_iq_evidence(profile: str = "All roles", workflow: str | None = None, query: str | None = None) -> dict[str, Any]:
    retrieval_query = query or "agent blueprint governance approval quality"
    if workflow:
        retrieval_query = f"{retrieval_query} {workflow}"

    foundry = retrieve_foundry_evidence(retrieval_query, limit=5)
    fabric = get_fabric_evidence()
    work = get_work_iq_evidence(profile)
    evidence = foundry + fabric + work
    citations = sorted({item["citation"] for item in evidence})

    return {
        "mode": "local_demo",
        "profile": profile,
        "workflow": workflow,
        "query": retrieval_query,
        "evidence": evidence,
        "citations": citations,
        "evidence_summary": (
            "Blueprint recommendation is grounded in approved synthetic knowledge sources, "
            "a Fabric IQ-style ontology, and Work IQ-style synthetic context signals."
        ),
        "iq_alignment": {
            "foundry_iq": "Grounded retrieval over approved local synthetic knowledge pack.",
            "fabric_iq": "Semantic model connects users, work signals, opportunities, blueprints, gates, tests, and learning updates.",
            "work_iq": "Synthetic work-context signals describe collaboration patterns, recurring tasks, and approval sensitivity.",
        },
    }


def retrieve_iq_evidence(query: str, profile: str = "All roles", workflow: str | None = None) -> dict[str, Any]:
    return get_iq_evidence(profile=profile, workflow=workflow, query=query)
