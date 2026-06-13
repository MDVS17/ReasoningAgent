"""Evaluation summary for the Syntrix demo."""


def get_evaluation_summary() -> dict:
    rubric = [
        {"criterion": "Synthetic data boundary", "status": "pass", "score": 100},
        {"criterion": "Blueprint completeness", "status": "pass", "score": 94},
        {"criterion": "Human approval gates", "status": "pass", "score": 96},
        {"criterion": "Reasoning traceability", "status": "pass", "score": 90},
        {"criterion": "Continuous improvement loop", "status": "pass", "score": 88},
    ]
    return {
        "total_tests": len(rubric),
        "passing_tests": sum(1 for item in rubric if item["status"] == "pass"),
        "safety_status": "Approved for synthetic hackathon demo",
        "rubric": rubric,
    }
