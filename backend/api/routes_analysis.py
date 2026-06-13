"""Analysis routes for the Syntrix Reasoning Engine."""

from fastapi import APIRouter, Query

from backend.models.schemas import AnalyzeRequest
from backend.services.evaluation_service import get_evaluation_summary
from backend.services.syntrix_pipeline import analyze, get_interactions

router = APIRouter()


@router.get("/api/interactions")
def interactions(profile: str = Query(default="All roles")) -> dict:
    return {"data": get_interactions(profile)}


@router.post("/api/analyze")
def analyze_profile(request: AnalyzeRequest) -> dict:
    return {"data": analyze(request.profile)}


@router.get("/api/evaluation/summary")
def evaluation_summary() -> dict:
    return {"data": get_evaluation_summary()}
