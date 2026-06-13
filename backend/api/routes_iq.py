"""Microsoft IQ simulation routes."""

from fastapi import APIRouter

from backend.services.fabric_iq_service import get_fabric_iq_status
from backend.services.foundry_iq_service import get_foundry_iq_status
from backend.services.work_iq_simulator import get_work_iq_status

router = APIRouter()


@router.get("/api/iq/status")
def iq_status() -> dict:
    return {
        "data": {
            "foundry_iq": get_foundry_iq_status(),
            "fabric_iq": get_fabric_iq_status(),
            "work_iq": get_work_iq_status(),
        }
    }
