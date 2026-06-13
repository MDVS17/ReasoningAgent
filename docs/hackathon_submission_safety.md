# Hackathon Submission Safety

## Submitted Product Files

The submitted Syntrix product should include the files that are required to explain, run, and evaluate the local demo:

- `README.md`, `LICENSE`, `requirements.txt`, `.env.example`, and `AGENTS.md`
- `app.py` as the Streamlit backup demo
- `backend/` for the FastAPI API
- `frontend/` for the cinematic product UI
- `agents/` for local reasoning modules
- `synthetic_data/` for synthetic Copilot-style demo data
- `diagrams/`, `evals/`, `outputs/`, `knowledge/`, and `docs/` for public documentation, sample artifacts, evaluation material, and architecture context

## Developer-Only Files

Developer-only files should stay outside the submitted product unless the hackathon rules explicitly ask for them:

- `.codex/` for Codex-only prompts, project memory, planning notes, and local workflows
- `.agents/` for local Codex or developer workflow helpers
- `.venv/`, caches, logs, local secrets, generated runtime state, and editor-specific files

Public documentation belongs in `docs/`. Codex-only prompts, project memory, and internal workflows belong in `.codex/`.

## Why Codex Files Should Stay Private

Codex prompt, memory, and workflow files can contain development process notes, reasoning traces, prompt experiments, or local automation preferences. These are useful while building, but they are not part of the product experience and can distract reviewers from the submitted demo.

They should not be submitted unless the hackathon explicitly requires them, because the product should be judged on the working application, public documentation, synthetic datasets, architecture, evaluation approach, and safety story.

## Data and API Boundary

Syntrix uses synthetic data only. The repository should not include real emails, real customers, real employees, confidential documents, production exports, or private company data.

No secrets or paid APIs are required for the local hackathon demo. `.env.example` may document future configuration names, but real credentials must not be committed.
