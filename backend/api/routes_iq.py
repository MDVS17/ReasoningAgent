"""Microsoft IQ-ready local demo routes."""

from fastapi import APIRouter, Query

from backend.models.schemas import IQRetrieveRequest
from backend.services.iq_layer_service import get_iq_evidence, get_iq_layer_status, retrieve_iq_evidence

router = APIRouter()


@router.get("/api/iq/status")
def iq_status() -> dict:
    return {"data": get_iq_layer_status()}


@router.get("/api/iq/evidence")
def iq_evidence(
    profile: str = Query(default="All roles"),
    workflow: str | None = Query(default=None),
) -> dict:
    return {"data": get_iq_evidence(profile=profile, workflow=workflow)}


@router.post("/api/iq/retrieve")
def iq_retrieve(request: IQRetrieveRequest) -> dict:
    return {
        "data": retrieve_iq_evidence(
            query=request.query,
            profile=request.profile,
            workflow=request.workflow,
        )
    }
