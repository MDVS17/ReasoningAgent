# Syntrix Final Submission Checklist

Use this checklist before submitting Syntrix — Copilot Agent Architect to the hackathon.

## Repository

- [ ] Main branch is pushed.
- [ ] GitHub repo is public.
- [ ] README is updated for **Syntrix — Copilot Agent Architect**.
- [ ] `docs/judging_rubric_mapping.md` is updated.
- [ ] `docs/demo_script.md` is current.
- [ ] `docs/hackathon_submission_copy.md` is ready for paste-in submission fields.
- [ ] Hackathon page fields are complete.
- [ ] Demo video is uploaded.

## Local App

- [ ] Dependencies install from `requirements.txt`.
- [ ] FastAPI app runs with `uvicorn backend.main:app --reload --port 8000`.
- [ ] Frontend loads at `http://localhost:8000`.
- [ ] API docs load at `http://localhost:8000/docs`.
- [ ] Streamlit backup remains available with `streamlit run app.py`.

## API Checks

- [ ] `GET /api/health` works.
- [ ] `POST /api/analyze` works.
- [ ] `GET /api/iq/status` works.
- [ ] `GET /api/profiles` works.
- [ ] `GET /api/interactions` works.
- [ ] `POST /api/blueprint` works.
- [ ] `GET /api/evaluation/summary` works.

## Product Demo Checks

- [ ] Hero shows **Syntrix — Copilot Agent Architect**.
- [ ] Microsoft 365 Signals selector works.
- [ ] Pattern Intelligence charts render.
- [ ] Agent Factory / Master Agent cards render.
- [ ] Reasoning trace appears.
- [ ] Copilot Agent Blueprint appears.
- [ ] Blueprint includes ROI, Confidence Score, Impact Score, and Deployment Readiness.
- [ ] Governance gates appear.
- [ ] Evidence cards do not overflow.
- [ ] Continuous Improvement Loop appears.

## Microsoft IQ Checks

- [ ] Foundry IQ proof screenshot exists at `docs/assets/foundry-iq-live-proof.png`.
- [ ] Foundry IQ is described as live verified in Azure Foundry.
- [ ] Fabric IQ is described as a semantic ontology layer.
- [ ] Work IQ is described as Microsoft 365-style synthetic work-context signals.
- [ ] Microsoft 365 / Graph integrations are described as simulated for the MVP.
- [ ] No live Copilot Studio runtime integration is claimed.

## Safety Checks

- [ ] No `.env` committed.
- [ ] No `.codex/` committed.
- [ ] No secrets.
- [ ] No API keys.
- [ ] No connection strings.
- [ ] No real tenant data.
- [ ] No real emails.
- [ ] No real customers.
- [ ] No real employees.
- [ ] No confidential information.
- [ ] No paid API requirement for the local demo.

## Final Commands

```bash
python -m compileall backend agents app.py
```

Optional local smoke checks:

```bash
curl http://localhost:8000/api/health
curl http://localhost:8000/api/iq/status
curl -X POST http://localhost:8000/api/analyze ^
  -H "Content-Type: application/json" ^
  -d "{\"profile\":\"Project Manager\"}"
```

## Submission Story Check

- [ ] Opening problem is clear: Copilot is powerful, but organizations do not know which Copilot agents they need.
- [ ] Product thesis is clear: Copilot helps people work faster; Syntrix helps organizations discover which Copilot agents should exist next.
- [ ] Demo shows Agent Factory reasoning, not just static charts.
- [ ] Demo shows a review-ready Copilot Agent Blueprint.
- [ ] Demo mentions Foundry IQ live verification accurately.
- [ ] Closing line is crisp.
