# Syntrix Submission Checklist

## Repository

- [ ] Public repository is accessible to judges.
- [ ] README is complete and current.
- [ ] Foundry IQ proof screenshot is included at `docs/assets/foundry-iq-live-proof.png`.
- [ ] `docs/foundry_iq_setup.md` documents the live Foundry IQ verification without secrets.
- [ ] `.codex/` is ignored and not submitted.
- [ ] No private Codex memory or prompts are exposed.
- [ ] No unnecessary generated files are included.

## Local Run

- [ ] Dependencies install from `requirements.txt`.
- [ ] FastAPI app runs with `uvicorn backend.main:app --reload --port 8000`.
- [ ] Product demo loads at `http://localhost:8000`.
- [ ] API docs load at `http://localhost:8000/docs`.
- [ ] Streamlit backup remains available with `streamlit run app.py`.

## Required Endpoints

- [ ] `GET /api/health` works.
- [ ] `GET /api/profiles` works.
- [ ] `GET /api/interactions` works.
- [ ] `POST /api/analyze` works.
- [ ] `POST /api/blueprint` works.
- [ ] `GET /api/iq/status` works.
- [ ] `GET /api/iq/evidence` works.
- [ ] `POST /api/iq/retrieve` works.
- [ ] `GET /api/evaluation/summary` works.

## Safety

- [ ] Synthetic data only.
- [ ] No real emails.
- [ ] No real customers.
- [ ] No real employees.
- [ ] No confidential information.
- [ ] No secrets or paid API keys.
- [ ] No paid APIs required.
- [ ] Human approval gates are visible.
- [ ] Foundry IQ is described as live verified in Azure Foundry.
- [ ] Fabric IQ is described as a local semantic ontology layer.
- [ ] Work IQ is described as synthetic work-context signals.
- [ ] No Azure credentials are included in the public repo.

## Demo Readiness

- [ ] Demo script is rehearsed.
- [ ] Demo video is recorded or ready.
- [ ] Opening problem is clear.
- [ ] Product thesis is stated.
- [ ] Reasoning trace is shown.
- [ ] Generated blueprint is shown.
- [ ] Microsoft IQ evidence/citations are shown.
- [ ] Foundry IQ live verification is mentioned accurately.
- [ ] Learning loop is shown.
- [ ] Closing line is crisp.
