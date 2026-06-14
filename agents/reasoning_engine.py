"""Deterministic Syntrix Master Agent reasoning pipeline."""

from typing import Any

import pandas as pd

from .blueprint_generator import generate_blueprint
from .opportunity_scorer import score_opportunities
from .safety_reviewer import review_blueprint


PRODUCT_AGENTS = [
    "Master Agent",
    "Signal Discovery Agent",
    "Pattern Scoring Agent",
    "Blueprint Architect Agent",
    "Safety Governance Agent",
    "Learning Loop Agent",
]


def _filter_profile(df: pd.DataFrame, profile: str) -> pd.DataFrame:
    if profile == "All roles":
        return df.copy()
    return df[df["profile"] == profile].copy()


def _records(df: pd.DataFrame) -> list[dict[str, Any]]:
    return df.to_dict("records")


def discover_signals(interactions: pd.DataFrame, profile: str = "All roles") -> dict[str, Any]:
    """Signal Discovery Agent: find repeated workflow clusters."""

    filtered = _filter_profile(interactions, profile)
    if filtered.empty:
        return {
            "selected_profile": profile,
            "signal_count": 0,
            "workflow_count": 0,
            "top_clusters": [],
        }

    clusters = (
        filtered.groupby(["profile", "workflow"], as_index=False)
        .agg(
            signal_count=("interaction_id", "count"),
            avg_repetition=("repetition_score", "mean"),
            avg_business_value=("business_value_score", "mean"),
            avg_risk=("risk_score", "mean"),
        )
        .sort_values(["signal_count", "avg_business_value"], ascending=False)
    )

    return {
        "selected_profile": profile,
        "signal_count": int(len(filtered)),
        "workflow_count": int(filtered["workflow"].nunique()),
        "top_clusters": _records(clusters.head(5)),
    }


def build_governance_gates(safety_review: Any) -> list[dict[str, str]]:
    """Safety Governance Agent: expose product-grade controls."""

    gates = [
        (
            "Human approval before external communication",
            "External messages remain draft-only until a human approves them.",
        ),
        (
            "Human approval before system changes",
            "No system updates, workflow changes, or write actions run autonomously.",
        ),
        (
            "Source traceability required",
            "Blueprint recommendations must map back to approved source signals.",
        ),
        (
            "Sensitive content flagged",
            "HR, legal, financial, customer-impacting, and employee-impacting content is escalated.",
        ),
        (
            "No autonomous write actions without approval",
            "The v1 local engine recommends controlled blueprint updates only.",
        ),
    ]
    return [
        {
            "gate": gate,
            "status": "required",
            "reason": reason,
            "review_risk": safety_review.risk_level,
        }
        for gate, reason in gates
    ]


def build_learning_loop_recommendation(
    week_comparison: pd.DataFrame,
    profile: str,
    selected_workflow: str,
) -> dict[str, Any]:
    """Learning Loop Agent: recommend controlled blueprint updates."""

    filtered = _filter_profile(week_comparison, profile)
    if filtered.empty:
        return {
            "current_version": "Agent v1.0",
            "recommended_version": "Agent v1.1",
            "recommendation": "Keep monitoring workspace signals until enough repeated patterns emerge.",
            "new_signal": "No week comparison signal available for this workspace view.",
            "new_capability": "No new capability recommended yet",
            "confidence_lift": 0,
            "approval_required": True,
            "evidence": [],
        }

    matching = filtered[filtered["workflow"] == selected_workflow]
    selected = matching.iloc[0] if not matching.empty else filtered.iloc[0]
    confidence_lift = int(selected["week_3_avg_score"] - selected["week_1_avg_score"])
    evidence = _records(
        filtered.assign(
            confidence_lift=filtered["week_3_avg_score"] - filtered["week_1_avg_score"],
        ).sort_values("confidence_lift", ascending=False)
    )

    return {
        "current_version": "Agent v1.0",
        "recommended_version": "Agent v1.1",
        "recommendation": (
            "Recommend a controlled blueprint update for human approval. Refine triggers, "
            "add one escalation-summary capability, and tighten evaluation checks."
        ),
        "new_signal": (
            f"{selected['workflow']} improved from Week 1 score {selected['week_1_avg_score']} "
            f"to Week 3 score {selected['week_3_avg_score']}."
        ),
        "new_capability": f"{selected['workflow']} escalation summary",
        "confidence_lift": confidence_lift,
        "approval_required": True,
        "evidence": evidence[:5],
    }


def run_reasoning_engine(
    interactions: pd.DataFrame,
    week_comparison: pd.DataFrame,
    profile: str = "All roles",
) -> dict[str, Any]:
    """Master Agent: orchestrate specialist agents into one JSON-ready result."""

    filtered = _filter_profile(interactions, profile)
    signal_discovery = discover_signals(interactions, profile)
    opportunities = score_opportunities(interactions, profile)
    opportunity_scores = [item.model_dump(by_alias=True) for item in opportunities]

    selected = opportunities[0] if opportunities else None
    blueprint = generate_blueprint(selected) if selected else None
    safety_review = review_blueprint(blueprint) if blueprint else None
    governance_gates = build_governance_gates(safety_review) if safety_review else []
    learning_loop = (
        build_learning_loop_recommendation(week_comparison, profile, selected.workflow)
        if selected
        else build_learning_loop_recommendation(week_comparison, profile, "")
    )

    top_name = blueprint.agent_name if blueprint else "No Copilot Agent Blueprint generated yet"
    top_score = opportunity_scores[0]["syntrix_opportunity_score"] if opportunity_scores else None
    master_summary = {
        "system_name": "Syntrix Reasoning Engine",
        "selected_profile": profile,
        "input_signal_count": int(len(filtered)),
        "workflows_detected": signal_discovery["workflow_count"],
        "specialist_agents_used": PRODUCT_AGENTS[1:],
        "orchestration_decision": (
            f"Generate {top_name} because repeated Microsoft 365-style signals produced the highest "
            f"Impact Score."
            if selected
            else "Continue monitoring. No repeated workflow pattern was strong enough for blueprint generation."
        ),
        "top_recommendation": top_name,
        "top_opportunity_score": top_score,
    }

    reasoning_trace = [
        {
            "step": 1,
            "agent": "Master Agent",
            "input": f"{len(filtered)} workspace signals for {profile}",
            "decision": "Route signals through discovery, scoring, blueprint, governance, and learning agents.",
            "output": "Specialist reasoning plan created",
            "handoff_to": "Signal Discovery Agent",
        },
        {
            "step": 2,
            "agent": "Signal Discovery Agent",
            "input": "Synthetic Copilot-style interaction logs",
            "decision": f"Detected {signal_discovery['workflow_count']} repeated workflow clusters.",
            "output": signal_discovery["top_clusters"],
            "handoff_to": "Pattern Scoring Agent",
        },
        {
            "step": 3,
            "agent": "Pattern Scoring Agent",
            "input": "Workflow clusters with frequency, time saved, repetition, value, and risk",
            "decision": f"Ranked {len(opportunity_scores)} patterns using Impact Score.",
            "output": opportunity_scores[:3],
            "handoff_to": "Blueprint Architect Agent",
        },
        {
            "step": 4,
            "agent": "Blueprint Architect Agent",
            "input": "Top ranked workflow opportunity",
            "decision": f"Generated {top_name}.",
            "output": blueprint.model_dump() if blueprint else None,
            "handoff_to": "Safety Governance Agent",
        },
        {
            "step": 5,
            "agent": "Safety Governance Agent",
            "input": "Generated blueprint",
            "decision": "Attach approval gates and keep write-capable actions behind human review.",
            "output": governance_gates,
            "handoff_to": "Learning Loop Agent",
        },
        {
            "step": 6,
            "agent": "Learning Loop Agent",
            "input": "Week 1 vs Week 3 signal comparison",
            "decision": "Recommend controlled blueprint updates for human approval, not silent retraining.",
            "output": learning_loop,
            "handoff_to": "Master Agent",
        },
    ]

    return {
        "master_agent_summary": master_summary,
        "reasoning_trace": reasoning_trace,
        "opportunity_scores": opportunity_scores,
        "recommended_blueprint": blueprint.model_dump() if blueprint else None,
        "copilot_agent_blueprint": blueprint.model_dump() if blueprint else None,
        "governance_gates": governance_gates,
        "learning_loop_recommendation": learning_loop,
        "safety_review": safety_review.model_dump() if safety_review else None,
    }
