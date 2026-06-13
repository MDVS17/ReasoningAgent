"""Blueprint generation routes."""

from fastapi import APIRouter

from backend.models.schemas import BlueprintRequest
from backend.services.syntrix_pipeline import create_blueprint

router = APIRouter()


@router.post("/api/blueprint")
def blueprint(request: BlueprintRequest) -> dict:
    return {"data": create_blueprint(request.profile, request.workflow)}
