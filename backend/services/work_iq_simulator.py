"""Compatibility wrapper for the local Work IQ service."""

from backend.services.work_iq_service import get_work_iq_status

__all__ = ["get_work_iq_status"]
