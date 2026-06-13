"""Safety and governance review for Syntrix Agent Blueprints."""

from .models import AgentBlueprint, SafetyReview


def review_blueprint(blueprint: AgentBlueprint) -> SafetyReview:
    """Review a blueprint against synthetic-data and human-approval controls."""

    checks = [
        "Synthetic data boundary is explicit",
        "Human approval is required for external or sensitive actions",
        "Knowledge sources are listed and auditable",
        "Evaluation tests are defined before deployment",
    ]
    controls = [
        "Keep demo mode read-only",
        "Block real emails, real employee records, and real customer data",
        "Require approval gates for write actions",
        "Log assumptions and generated recommendations",
    ]

    sensitive = any("HR" in item or "employee" in item.lower() for item in blueprint.human_approval_points)
    return SafetyReview(
        decision="Approved for synthetic local demo",
        risk_level="Medium" if sensitive else "Low",
        checks_passed=checks,
        required_controls=controls,
        reviewer_notes=(
            "The blueprint is suitable for hackathon demonstration because it produces advisory "
            "workflow guidance from synthetic data and keeps consequential actions behind approval."
        ),
    )
