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

DEPARTMENT_BY_PROFILE = {
    "Marketing Manager": "Marketing",
    "Project Manager": "Program Delivery",
    "HR Business Partner": "People Operations",
}


def _microsoft_365_signals(workflow: str) -> list[str]:
    workflow_lower = workflow.lower()
    base_signals = [
        "Outlook: repeated follow-up emails and unresolved approval chains",
        "Teams: recurring decision threads, project updates, and blocked-task discussions",
        "Calendar: recurring preparation patterns and follow-up loops",
        "SharePoint/OneDrive: repeated document access, policy references, and reporting packs",
        "Planner: recurring tasks, overdue work, and handoff patterns",
    ]
    if "campaign" in workflow_lower or "content" in workflow_lower:
        return [
            "Outlook: recurring launch follow-ups and stakeholder approval requests",
            "Teams: campaign decision threads and blocker discussions",
            "Calendar: recurring launch readiness meetings and preparation loops",
            "SharePoint/OneDrive: repeated access to campaign briefs and content packs",
            "Planner: launch tasks, owners, handoffs, and overdue campaign work",
        ]
    if "risk" in workflow_lower or "status" in workflow_lower or "dependency" in workflow_lower:
        return [
            "Outlook: repeated executive status requests and approval follow-ups",
            "Teams: dependency threads, blocked-task discussions, and delivery decisions",
            "Calendar: recurring status meetings with preparation and follow-up loops",
            "SharePoint/OneDrive: project reporting packs and risk logs",
            "Planner: overdue tasks, dependency owners, and handoff patterns",
        ]
    if "policy" in workflow_lower or "guidance" in workflow_lower or "onboarding" in workflow_lower:
        return [
            "Outlook: repeated manager guidance requests and approval-sensitive follow-ups",
            "Teams: policy clarification threads and employee-support discussions",
            "Calendar: recurring advisory meetings and onboarding check-ins",
            "SharePoint/OneDrive: repeated policy references and onboarding documents",
            "Planner: onboarding tasks, manager handoffs, and overdue people actions",
        ]
    return base_signals


def generate_blueprint(opportunity: AgentOpportunity) -> AgentBlueprint:
    """Create a deterministic, presentation-ready agent blueprint."""

    agent_name = AGENT_NAME_BY_WORKFLOW.get(opportunity.workflow, f"{opportunity.workflow.title()} Agent")
    department = DEPARTMENT_BY_PROFILE.get(opportunity.profile, "Cross-functional Operations")
    annual_occurrences = max(opportunity.task_count * 52, 1)
    estimated_hours_saved = round((annual_occurrences * opportunity.avg_time_saved_minutes) / 60, 1)
    estimated_annual_roi = f"${estimated_hours_saved * 75:,.0f}"
    confidence_score = round(
        min(96, 58 + (opportunity.avg_repetition * 5) + (opportunity.task_count * 3) - opportunity.avg_risk),
        1,
    )
    impact_score = opportunity.opportunity_score
    deployment_readiness = (
        "Ready for Copilot Studio review after governance owner approval"
        if opportunity.avg_risk <= 3
        else "Needs governance review before Copilot Studio review"
    )
    signals = _microsoft_365_signals(opportunity.workflow)
    instructions = [
        "Summarize the user's goal and infer the next best workflow step.",
        "Draft structured outputs in the user's role-specific language.",
        "Ask for clarification when confidence is low or policy-sensitive context is missing.",
        "Keep a traceable reasoning summary with assumptions, inputs, and recommended next actions.",
    ]
    knowledge_sources = [
        "Foundry IQ knowledge pack: agent design principles",
        "Foundry IQ knowledge pack: enterprise AI governance",
        "Foundry IQ knowledge pack: safe agent deployment checklist",
        "Synthetic Copilot interaction history",
        "Role playbook and workflow checklist",
        "Approved template library",
    ]
    actions = [
        "Draft document or message for human review",
        "Create task checklist",
        "Summarize meeting, campaign, project, or policy context",
        "Prepare next-action and owner recommendations",
    ]

    return AgentBlueprint(
        agent_name=agent_name,
        department=department,
        business_problem=(
            f"{opportunity.profile}s repeatedly spend time turning scattered Microsoft 365-style "
            f"signals into a reliable {opportunity.workflow.lower()} output."
        ),
        detected_work_pattern=(
            f"{opportunity.task_count} repeated synthetic interactions show recurring "
            f"{opportunity.workflow.lower()} work with high repetition and business value."
        ),
        microsoft_365_signals_used=signals,
        suggested_knowledge_sources=knowledge_sources,
        suggested_actions=actions,
        system_instructions=instructions,
        purpose=(
            f"Help a {opportunity.profile} complete the recurring workflow "
            f"'{opportunity.workflow}' with less manual coordination and a review-ready Copilot Agent Blueprint."
        ),
        target_user=opportunity.profile,
        triggering_work_patterns=[
            f"User repeatedly asks Copilot for help with {opportunity.workflow.lower()}.",
            "Similar prompts appear across planning, drafting, summarizing, and follow-up tasks.",
            "The work pattern has measurable time savings and medium-to-high business value.",
        ],
        instructions=instructions,
        required_knowledge_sources=knowledge_sources,
        suggested_tools_actions=actions,
        guardrails=[
            "Use synthetic demo data only; never ingest real company content in this local demo.",
            "Do not send messages, update systems, or make commitments without human approval.",
            "Flag sensitive HR, legal, financial, or customer-impacting content for review.",
            "Show source assumptions and confidence signals before recommending automation.",
        ],
        estimated_hours_saved=estimated_hours_saved,
        estimated_annual_roi=estimated_annual_roi,
        confidence_score=confidence_score,
        impact_score=impact_score,
        deployment_readiness=deployment_readiness,
        copilot_studio_review_notes=(
            "Graph-ready signal model and Copilot Studio review-ready blueprint only; "
            "no live Microsoft Graph or Copilot Studio runtime integration is claimed."
        ),
        foundry_iq_grounding=[
            "Live-verified Foundry IQ knowledge base with synthetic governance documents",
            "Synthetic blueprint quality standards",
            "Synthetic safe agent deployment checklist",
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
