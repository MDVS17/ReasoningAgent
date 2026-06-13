# Syntrix QA Checklist

## Local App Checks

- [ ] `uvicorn backend.main:app --reload --port 8000` starts successfully.
- [ ] `http://localhost:8000` loads the cinematic demo.
- [ ] `http://localhost:8000/docs` loads Swagger docs.
- [ ] `GET /api/health` returns `status: ok`.

## Reasoning Engine Checks

- [ ] `python evals/qa_reasoning_engine.py` passes.
- [ ] Synthetic data loads.
- [ ] Reasoning pipeline runs.
- [ ] At least three opportunities are scored.
- [ ] Recommended blueprint is generated.
- [ ] Governance gates are present.
- [ ] Learning loop recommendation is present.

## IQ Layer Checks

- [ ] `python evals/qa_iq_layer.py` passes.
- [ ] Foundry IQ-ready knowledge pack loads.
- [ ] Fabric IQ-style ontology loads.
- [ ] Work IQ-style signals load.
- [ ] IQ evidence includes citations.
- [ ] `/api/analyze` includes IQ alignment on the recommended blueprint.

## Safety Checks

- [ ] No real data is present.
- [ ] No secrets are present.
- [ ] No paid APIs are required.
- [ ] Human approval gates remain visible.
- [ ] Synthetic data policy is documented.
