# Syntrix Architecture Overview

## FastAPI Backend

`backend/main.py` creates the FastAPI app, serves the cinematic frontend at `/`, mounts static files from `frontend/`, and exposes Swagger docs at `/docs`.

Core route modules:

- `backend/api/routes_health.py`
- `backend/api/routes_analysis.py`
- `backend/api/routes_blueprint.py`
- `backend/api/routes_iq.py`

## Cinematic Frontend

`frontend/index.html`, `frontend/styles.css`, and `frontend/app.js` implement the local product demo. The frontend calls the FastAPI endpoints, renders charts with vanilla JavaScript/CSS, shows the multi-agent cards, displays the reasoning trace, and presents the generated blueprint and IQ evidence panel.

## Master Agent

The Master Agent lives in the product-facing reasoning flow, implemented through `agents/reasoning_engine.py`. It orchestrates the specialist agents and returns a single JSON-ready result for `/api/analyze`.

## Specialist Agents

- **Signal Discovery Agent:** groups synthetic work interactions into repeated workflow clusters.
- **Pattern Scoring Agent:** calculates Syntrix Opportunity Scores.
- **Blueprint Architect Agent:** creates a structured Syntrix Agent Blueprint.
- **Safety Governance Agent:** attaches governance gates and approval controls.
- **Learning Loop Agent:** compares Week 1 and Week 3 signals and recommends controlled blueprint updates.

## Reasoning Trace

The reasoning trace is returned from `POST /api/analyze`. It explains each agent step, input, decision, output, and handoff. This makes Syntrix inspectable and demoable as a reasoning-agent system.

## IQ Services

The Syntrix IQ Layer is implemented locally:

- `backend/services/foundry_iq_service.py`
- `backend/services/fabric_iq_service.py`
- `backend/services/work_iq_service.py`
- `backend/services/iq_layer_service.py`

These services load local synthetic knowledge files, return status, provide evidence snippets, and attach citations to blueprint recommendations.

## Knowledge Pack

`knowledge/foundry_iq_pack/` contains synthetic markdown sources used as approved grounding documents for blueprint and governance reasoning.

## Ontology

`knowledge/fabric_ontology/syntrix_ontology.json` defines the semantic model for users, signals, patterns, opportunities, blueprints, governance gates, evaluation cases, and learning updates.

## Work Signals

`knowledge/work_iq_signals/work_context_signals.json` defines synthetic collaboration context, recurring tasks, output preferences, stakeholder context, and approval sensitivity.

## API Docs

Run the FastAPI app and open `http://localhost:8000/docs` to inspect and test the endpoints.
