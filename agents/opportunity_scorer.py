"""Syntrix Reasoning Engine opportunity scoring."""

import pandas as pd

from .models import AgentOpportunity


def _normalize(series: pd.Series) -> pd.Series:
    if series.max() == series.min():
        return pd.Series([0.5] * len(series), index=series.index)
    return (series - series.min()) / (series.max() - series.min())


def score_opportunities(interactions: pd.DataFrame, profile: str | None = None) -> list[AgentOpportunity]:
    """Score repeated workflows using transparent, demo-friendly heuristics."""

    df = interactions.copy()
    if profile and profile != "All roles":
        df = df[df["profile"] == profile]

    grouped = (
        df.groupby(["profile", "workflow"], as_index=False)
        .agg(
            task_count=("interaction_id", "count"),
            avg_time_saved_minutes=("estimated_time_saved_minutes", "mean"),
            avg_risk=("risk_score", "mean"),
            avg_repetition=("repetition_score", "mean"),
            avg_business_value=("business_value_score", "mean"),
        )
        .sort_values(["task_count", "avg_business_value"], ascending=False)
    )

    if grouped.empty:
        return []

    grouped["frequency_norm"] = _normalize(grouped["task_count"])
    grouped["time_norm"] = _normalize(grouped["avg_time_saved_minutes"])
    grouped["risk_penalty"] = grouped["avg_risk"] / 5
    grouped["syntrix_opportunity_score"] = (
        100
        * (
            0.30 * grouped["frequency_norm"]
            + 0.25 * grouped["time_norm"]
            + 0.20 * (grouped["avg_repetition"] / 5)
            + 0.20 * (grouped["avg_business_value"] / 5)
            - 0.05 * grouped["risk_penalty"]
        )
    ).round(1)

    opportunities: list[AgentOpportunity] = []
    for row in grouped.sort_values("syntrix_opportunity_score", ascending=False).to_dict("records"):
        row["rationale"] = (
            f"Detected {row['task_count']} repeated interactions with strong repetition "
            f"and about {row['avg_time_saved_minutes']:.0f} minutes saved per occurrence."
        )
        opportunities.append(AgentOpportunity(**row))

    return opportunities
