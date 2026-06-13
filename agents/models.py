"""Pydantic models for Syntrix agent reasoning artifacts."""

from typing import List

from pydantic import BaseModel, Field


class AgentOpportunity(BaseModel):
    """A scored workflow pattern that may justify a personalized agent."""

    profile: str
    workflow: str
    task_count: int
    avg_time_saved_minutes: float
    avg_risk: float
    avg_repetition: float
    avg_business_value: float
    opportunity_score: float = Field(alias="syntrix_opportunity_score")
    rationale: str


class AgentBlueprint(BaseModel):
    """A safe, personalized Syntrix Agent Blueprint."""

    agent_name: str
    purpose: str
    target_user: str
    triggering_work_patterns: List[str]
    instructions: List[str]
    required_knowledge_sources: List[str]
    suggested_tools_actions: List[str]
    guardrails: List[str]
    human_approval_points: List[str]
    evaluation_tests: List[str]
    continuous_improvement_recommendation: str


class SafetyReview(BaseModel):
    """Governance review for a generated blueprint."""

    decision: str
    risk_level: str
    checks_passed: List[str]
    required_controls: List[str]
    reviewer_notes: str
