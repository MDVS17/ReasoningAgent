"""Pydantic request and response schemas for the Syntrix API."""

from typing import Any, Literal

from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    profile: str = "All roles"


class BlueprintRequest(BaseModel):
    profile: str = "All roles"
    workflow: str | None = None


class HealthResponse(BaseModel):
    status: Literal["ok"]
    product: str
    mode: str


class ApiEnvelope(BaseModel):
    data: Any


class IQStatus(BaseModel):
    foundry_iq: dict[str, Any]
    fabric_iq: dict[str, Any]
    work_iq: dict[str, Any]


class EvaluationSummary(BaseModel):
    total_tests: int
    passing_tests: int
    safety_status: str
    rubric: list[dict[str, Any]]
