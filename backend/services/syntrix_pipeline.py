"""Application service that runs the Syntrix reasoning pipeline."""

from pathlib import Path
from typing import Any

import pandas as pd

from agents import (
    generate_blueprint,
    load_interactions,
    load_profiles,
    review_blueprint,
    run_reasoning_engine,
    score_opportunities,
)

BASE_DIR = Path(__file__).resolve().parents[2]


def _records(df: pd.DataFrame) -> list[dict[str, Any]]:
    clean = df.copy()
    for column in clean.columns:
        if pd.api.types.is_datetime64_any_dtype(clean[column]):
            clean[column] = clean[column].dt.strftime("%Y-%m-%d")
    return clean.to_dict("records")


def get_profiles() -> list[dict[str, Any]]:
    return _records(load_profiles())


def get_interactions(profile: str = "All roles") -> list[dict[str, Any]]:
    interactions = load_interactions()
    if profile != "All roles":
        interactions = interactions[interactions["profile"] == profile]
    return _records(interactions)


def analyze(profile: str = "All roles") -> dict[str, Any]:
    interactions = load_interactions()
    filtered = interactions if profile == "All roles" else interactions[interactions["profile"] == profile]
    week_comparison = pd.read_csv(BASE_DIR / "synthetic_data" / "week_comparison.csv")
    if profile != "All roles":
        week_comparison = week_comparison[week_comparison["profile"] == profile]
    engine_result = run_reasoning_engine(interactions, week_comparison, profile)

    task_frequency = (
        filtered.groupby(["profile", "workflow"], as_index=False)
        .size()
        .rename(columns={"size": "count"})
        .sort_values("count", ascending=False)
    )

    opportunity_records = engine_result["opportunity_scores"]
    top = opportunity_records[0] if opportunity_records else None

    return {
        "selected_profile": profile,
        "summary": {
            "interaction_count": int(len(filtered)),
            "role_count": int(filtered["profile"].nunique()),
            "workflow_count": int(filtered["workflow"].nunique()),
            "top_opportunity_score": top["syntrix_opportunity_score"] if top else None,
        },
        "interactions": _records(filtered),
        "task_frequency": _records(task_frequency),
        "opportunities": opportunity_records,
        "opportunity_scores": opportunity_records,
        "week_comparison": _records(week_comparison),
        "reasoning_flow": [
            "Master Agent",
            "Signal Discovery Agent",
            "Pattern Discovery Agent",
            "Pattern Scoring Agent",
            "Blueprint Architect Agent",
            "Safety Governance Agent",
            "Learning Loop Agent",
        ],
        **engine_result,
    }


def create_blueprint(profile: str = "All roles", workflow: str | None = None) -> dict[str, Any]:
    interactions = load_interactions()
    opportunities = score_opportunities(interactions, profile)
    if workflow:
        matching = [item for item in opportunities if item.workflow == workflow]
        selected = matching[0] if matching else opportunities[0]
    else:
        selected = opportunities[0]

    blueprint = generate_blueprint(selected)
    safety_review = review_blueprint(blueprint)
    return {
        "opportunity": selected.model_dump(by_alias=True),
        "blueprint": blueprint.model_dump(),
        "safety_review": safety_review.model_dump(),
    }
