"""Health and profile routes."""

from fastapi import APIRouter

from backend.models.schemas import HealthResponse
from backend.services.syntrix_pipeline import get_profiles

router = APIRouter()


@router.get("/api/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", product="Syntrix", mode="synthetic-local-demo")


@router.get("/api/profiles")
def profiles() -> dict:
    return {"data": get_profiles()}
