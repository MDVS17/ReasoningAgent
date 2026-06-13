from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
from dotenv import load_dotenv

from agents import generate_blueprint, load_interactions, load_profiles, review_blueprint, score_opportunities


BASE_DIR = Path(__file__).resolve().parent


def render_metric_card(label: str, value: str, caption: str) -> None:
    st.metric(label=label, value=value, help=caption)


def blueprint_to_markdown(blueprint) -> str:
    sections = [
        ("Agent name", blueprint.agent_name),
        ("Purpose", blueprint.purpose),
        ("Target user", blueprint.target_user),
        ("Triggering work patterns", blueprint.triggering_work_patterns),
        ("Instructions", blueprint.instructions),
        ("Required knowledge sources", blueprint.required_knowledge_sources),
        ("Suggested tools/actions", blueprint.suggested_tools_actions),
        ("Guardrails", blueprint.guardrails),
        ("Human approval points", blueprint.human_approval_points),
        ("Evaluation tests", blueprint.evaluation_tests),
        ("Continuous improvement recommendation", blueprint.continuous_improvement_recommendation),
    ]
    lines = ["# Syntrix Agent Blueprint", ""]
    for title, value in sections:
        lines.append(f"## {title}")
        if isinstance(value, list):
            lines.extend([f"- {item}" for item in value])
        else:
            lines.append(str(value))
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    load_dotenv()
    st.set_page_config(page_title="Syntrix", page_icon="S", layout="wide")

    interactions = load_interactions()
    profiles = load_profiles()
    week_comparison = pd.read_csv(BASE_DIR / "synthetic_data" / "week_comparison.csv")

    profile_options = ["All roles"] + profiles["profile"].tolist()
    with st.sidebar:
        st.title("Syntrix")
        selected_profile = st.selectbox("Profile", profile_options)
        st.caption("Synthetic data only. No company data, no real employees, no real customers.")
        st.divider()
        st.subheader("Demo roles")
        for profile in profiles["profile"]:
            st.write(f"- {profile}")

    filtered = interactions if selected_profile == "All roles" else interactions[interactions["profile"] == selected_profile]
    opportunities = score_opportunities(interactions, selected_profile)
    top_opportunity = opportunities[0] if opportunities else None

    st.title("Syntrix")
    st.subheader("From scattered Copilot usage to personalized AI agents.")
    st.write(
        "Syntrix analyzes synthetic Copilot-style work interactions, discovers repeated workflows, "
        "scores agent opportunities, generates safe personalized agent blueprints, and recommends "
        "improvements over time."
    )

    st.info(
        "Problem: companies are buying Copilot, but most users do not know how to convert their daily "
        "work patterns into useful AI agents. Syntrix does not ask users to design agents. It discovers "
        "the agents they already need."
    )

    metric_cols = st.columns(4)
    with metric_cols[0]:
        render_metric_card("Synthetic interactions", str(len(filtered)), "Filtered Copilot-style logs")
    with metric_cols[1]:
        render_metric_card("Roles analyzed", str(filtered["profile"].nunique()), "Synthetic user profiles")
    with metric_cols[2]:
        render_metric_card("Repeated workflows", str(filtered["workflow"].nunique()), "Candidate agent patterns")
    with metric_cols[3]:
        score = f"{top_opportunity.opportunity_score:.1f}" if top_opportunity else "N/A"
        render_metric_card("Top Syntrix Opportunity Score", score, "Transparent heuristic score")

    st.divider()
    st.header("Synthetic Copilot-Style Interaction Logs")
    st.dataframe(
        filtered[
            [
                "date",
                "week",
                "profile",
                "workflow",
                "prompt_type",
                "synthetic_prompt_summary",
                "estimated_time_saved_minutes",
            ]
        ],
        width="stretch",
        hide_index=True,
    )

    chart_cols = st.columns(2)
    task_counts = filtered.groupby(["profile", "workflow"], as_index=False).size()
    with chart_cols[0]:
        st.subheader("Task Frequency")
        fig = px.bar(
            task_counts,
            x="workflow",
            y="size",
            color="profile",
            labels={"size": "Interactions", "workflow": "Workflow"},
        )
        fig.update_layout(xaxis_tickangle=-30, legend_title_text="Profile")
        st.plotly_chart(fig, width="stretch")

    opportunity_df = pd.DataFrame([item.model_dump(by_alias=True) for item in opportunities])
    with chart_cols[1]:
        st.subheader("Agent Opportunity Scoring")
        if not opportunity_df.empty:
            fig = px.bar(
                opportunity_df,
                x="workflow",
                y="syntrix_opportunity_score",
                color="profile",
                labels={"syntrix_opportunity_score": "Syntrix Opportunity Score", "workflow": "Workflow"},
            )
            fig.update_layout(xaxis_tickangle=-30, legend_title_text="Profile", yaxis_range=[0, 100])
            st.plotly_chart(fig, width="stretch")
        else:
            st.warning("No opportunities found for this filter.")

    st.divider()
    st.header("Syntrix Reasoning Engine")
    st.markdown(
        """
```mermaid
flowchart LR
    A[Synthetic Copilot logs] --> B[Pattern Discovery Agent]
    B --> C[Opportunity Scoring Agent]
    C --> D[Blueprint Generation Agent]
    D --> E[Safety Review Agent]
    E --> F[Syntrix Agent Blueprint]
    F --> G[Syntrix Continuous Improvement Loop]
```
"""
    )
    st.write(
        "The reasoning flow separates pattern detection, scoring, blueprint generation, governance, "
        "and improvement so each recommendation is explainable."
    )

    st.header("Recommended Agent Opportunities")
    for opportunity in opportunities[:5]:
        with st.expander(f"{opportunity.workflow} — {opportunity.profile}", expanded=opportunity == top_opportunity):
            st.write(opportunity.rationale)
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Score", f"{opportunity.opportunity_score:.1f}")
            c2.metric("Tasks", str(opportunity.task_count))
            c3.metric("Avg minutes saved", f"{opportunity.avg_time_saved_minutes:.0f}")
            c4.metric("Risk", f"{opportunity.avg_risk:.1f}/5")

    if top_opportunity:
        blueprint = generate_blueprint(top_opportunity)
        safety_review = review_blueprint(blueprint)

        st.divider()
        st.header("Generated Syntrix Agent Blueprint")
        st.markdown(blueprint_to_markdown(blueprint))

        st.header("Safety and Governance Review")
        safety_cols = st.columns(3)
        safety_cols[0].metric("Decision", safety_review.decision)
        safety_cols[1].metric("Risk level", safety_review.risk_level)
        safety_cols[2].metric("Controls", str(len(safety_review.required_controls)))
        st.write(safety_review.reviewer_notes)
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("Checks passed")
            for check in safety_review.checks_passed:
                st.write(f"- {check}")
        with c2:
            st.subheader("Required controls")
            for control in safety_review.required_controls:
                st.write(f"- {control}")

    st.divider()
    st.header("Syntrix Continuous Improvement Loop")
    improvement_df = week_comparison if selected_profile == "All roles" else week_comparison[week_comparison["profile"] == selected_profile]
    improvement_long = improvement_df.melt(
        id_vars=["profile", "workflow"],
        value_vars=["week_1_avg_score", "week_3_avg_score"],
        var_name="period",
        value_name="average_score",
    )
    improvement_long["period"] = improvement_long["period"].map(
        {"week_1_avg_score": "Week 1", "week_3_avg_score": "Week 3"}
    )
    fig = px.line(
        improvement_long,
        x="period",
        y="average_score",
        color="workflow",
        markers=True,
        labels={"average_score": "Average Syntrix Opportunity Score", "period": "Period"},
    )
    fig.update_layout(yaxis_range=[0, 100], legend_title_text="Workflow")
    st.plotly_chart(fig, width="stretch")
    st.caption(
        "Placeholder: future versions can compare accepted recommendations, user edits, escalations, "
        "and failed evaluation tests between Week 1 and Week 3."
    )


if __name__ == "__main__":
    main()
