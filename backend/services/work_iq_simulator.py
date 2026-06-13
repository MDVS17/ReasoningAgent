"""Synthetic Work IQ signals derived from local demo data."""

from agents import load_interactions


def get_work_iq_status() -> dict:
    interactions = load_interactions()
    return {
        "name": "Work IQ",
        "status": "simulated",
        "description": "Synthesizes work-pattern signals from Copilot-style demo interactions.",
        "signals": [
            {"label": "Synthetic interactions", "value": int(len(interactions))},
            {"label": "Roles", "value": int(interactions["profile"].nunique())},
            {"label": "Repeated workflows", "value": int(interactions["workflow"].nunique())},
        ],
        "demo_note": "Signals are generated from synthetic CSV files in this repository.",
    }
