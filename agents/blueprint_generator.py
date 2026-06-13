"""Generate safe Syntrix Agent Blueprints from scored opportunities."""

from .models import AgentBlueprint, AgentOpportunity


AGENT_NAME_BY_WORKFLOW = {
    "Campaign launch brief": "Campaign Launch Brief Agent",
    "Weekly performance narrative": "Performance Narrative Agent",
    "Content repurposing plan": "Content Repurposing Agent",
    "Executive status update": "Executive Status Agent",
    "Risk and dependency tracker": "Risk & Dependency Tracker Agent",
    "Meeting action follow-up": "Meeting Action Follow-up Agent",
    "Manager guidance draft": "Manager Guidance Agent",
    "Onboarding checklist": "Onboarding Checklist Agent",
    "Policy Q&A response": "Policy Guidance Agent",
}


def generate_blueprint(opportunity: AgentOpportunity) -> AgentBlueprint:
    """Create a deterministic, presentation-ready agent blueprint."""

    agent_name = AGENT_NAME_BY_WORKFLOW.get(opportunity.workflow, f"{opportunity.workflow.title()} Agent")

    return AgentBlueprint(
        agent_name=agent_name,
        purpose=(
            f"Help a {opportunity.profile} complete the recurring workflow "
            f"'{opportunity.workflow}' with less manual coordination and better follow-through."
        ),
        target_user=opportunity.profile,
        triggering_work_patterns=[
            f"User repeatedly asks Copilot for help with {opportunity.workflow.lower()}.",
            "Similar prompts appear across planning, drafting, summarizing, and follow-up tasks.",
            "The work pattern has measurable time savings and medium-to-high business value.",
        ],
        instructions=[
            "Summarize the user's goal and infer the next best workflow step.",
            "Draft structured outputs in the user's role-specific language.",
            "Ask for clarification when confidence is low or policy-sensitive context is missing.",
            "Keep a traceable reasoning summary with assumptions, inputs, and recommended next actions.",
        ],
        required_knowledge_sources=[
            "Synthetic Copilot interaction history",
            "Role playbook and workflow checklist",
            "Approved template library",
            "Policy and governance guidance",
        ],
        suggested_tools_actions=[
            "Draft document or message",
            "Create task checklist",
            "Summarize meeting or campaign context",
            "Recommend next action and owner",
        ],
        guardrails=[
            "Use synthetic demo data only; never ingest real company content in this local demo.",
            "Do not send messages, update systems, or make commitments without human approval.",
            "Flag sensitive HR, legal, financial, or customer-impacting content for review.",
            "Show source assumptions and confidence signals before recommending automation.",
        ],
        human_approval_points=[
            "Before external communication is sent",
            "Before employee-impacting or customer-impacting recommendations are applied",
            "Before connecting to enterprise systems or write-capable tools",
        ],
        evaluation_tests=[
            "Blueprint includes role, trigger, tools, guardrails, and approval points.",
            "Generated output avoids real names, real customers, and confidential data.",
            "Recommendations map back to at least one repeated synthetic workflow pattern.",
            "Risky actions are routed to human approval instead of autonomous execution.",
        ],
        continuous_improvement_recommendation=(
            "Compare Week 1 and Week 3 usage to refine triggers, remove low-value steps, "
            "and add new tests for repeated failure or escalation patterns."
        ),
    )
