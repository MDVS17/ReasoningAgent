"""Local Work IQ-style synthetic work signal service."""

import json
from pathlib import Path
from typing import Any

from agents import load_interactions

BASE_DIR = Path(__file__).resolve().parents[2]
WORK_SIGNAL_PATH = BASE_DIR / "knowledge" / "work_iq_signals" / "work_context_signals.json"


def load_work_iq_signals() -> dict[str, Any]:
    return json.loads(WORK_SIGNAL_PATH.read_text(encoding="utf-8"))


def get_work_iq_status() -> dict[str, Any]:
    interactions = load_interactions()
    signals = load_work_iq_signals()
    return {
        "name": "Work IQ",
        "status": "local_demo_ready",
        "mode": signals.get("mode", "local_demo"),
        "description": "Work-context signals from synthetic collaboration patterns and user activity.",
        "signal_source": str(WORK_SIGNAL_PATH.relative_to(BASE_DIR)),
        "signals": [
            {"label": "Synthetic interactions", "value": int(len(interactions))},
            {"label": "Roles", "value": int(interactions["profile"].nunique())},
            {"label": "Repeated workflows", "value": int(interactions["workflow"].nunique())},
            {"label": "Context signal groups", "value": len(signals.get("signals", {}))},
        ],
    }


def get_work_iq_evidence(profile: str = "All roles") -> list[dict[str, Any]]:
    signals = load_work_iq_signals()
    payload = signals.get("signals", {})
    meeting_load = payload.get("meeting_load", {})
    output_preferences = payload.get("output_preferences", {})
    approval_sensitivity = payload.get("approval_sensitivity", {})

    selected_meeting_load = (
        "Mixed synthetic workspace load"
        if profile == "All roles"
        else meeting_load.get(profile, "Synthetic workspace activity")
    )
    selected_preferences = (
        sorted({item for values in output_preferences.values() for item in values})
        if profile == "All roles"
        else output_preferences.get(profile, [])
    )

    return [
        {
            "layer": "Work IQ",
            "source_name": "work_context_signals.json",
            "source_path": str(WORK_SIGNAL_PATH.relative_to(BASE_DIR)),
            "snippet": (
                f"{profile} context: {selected_meeting_load}. Output preferences include "
                f"{', '.join(selected_preferences[:4])}."
            ),
            "citation": "work_context_signals.json",
            "frequent_apps": payload.get("frequent_apps", []),
            "recurring_tasks": payload.get("recurring_tasks", []),
            "approval_sensitivity": approval_sensitivity,
        }
    ]
