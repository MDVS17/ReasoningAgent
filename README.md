# Syntrix — Copilot Agent Architect

**Tagline:** From scattered Copilot usage to personalized AI agents.

Syntrix is an **AI Agent Factory for Microsoft 365** that discovers work patterns and generates review-ready **Copilot Agent Blueprints**.

**Core thesis:** Do not ask users to design agents. Let AI discover the agents they already need.

## Problem Statement

Companies are buying Copilot, but most teams still do not know which Copilot Agents they should build first. Their Microsoft 365 work is scattered across meetings, messages, drafts, summaries, status updates, and follow-ups. The agent architecture opportunity is hidden in repeated work patterns, not in any single prompt.

## Solution Overview

Syntrix continuously discovers enterprise work patterns and designs the next generation of Microsoft 365 Copilot Agents. It analyzes simulated Microsoft 365 collaboration signals, applies Pattern Intelligence, scores business impact, generates governed Copilot Agent Blueprints, grounds outputs in approved synthetic knowledge, and prepares artifacts for Copilot Studio review.

The primary flow is:

```text
Microsoft 365 Signals
-> Pattern Intelligence
-> Agent Factory
-> Copilot Agent Blueprint
-> Ready for Copilot Studio Review
```

Syntrix includes two demo surfaces:

- Cinematic FastAPI + vanilla frontend demo at `http://localhost:8000`.
- Streamlit backup demo in `app.py`.

## Why Syntrix Matters

Most agent-building workflows start by asking users to configure an agent. Syntrix starts from the work itself. It helps an enterprise move from scattered Copilot usage to an Agent Factory by identifying where repeated work exists, what the business impact and ROI could be, and which review gates must exist before a Copilot Agent Blueprint is ready for Copilot Studio review.

## Architecture Overview

```mermaid
flowchart LR
    A[Microsoft 365-style synthetic signals] --> B[Pattern Intelligence]
    B --> C[Syntrix Agent Factory]
    C --> D[Master Agent]
    D --> E[Signal Discovery Agent]
    D --> F[Pattern Scoring Agent]
    D --> G[Blueprint Architect Agent]
    D --> H[Safety Governance Agent]
    D --> I[Learning Loop Agent]
    E --> J[Enterprise work patterns]
    F --> K[Impact Score / ROI / Confidence Score]
    G --> L[Copilot Agent Blueprint]
    H --> M[Copilot Studio Review Gates]
    I --> N[Deployment readiness update]
    O[Syntrix IQ Layer] --> G
    O --> H
```

Key layers:

- `backend/`: FastAPI app, routes, services, IQ layer, and pipeline orchestration.
- `frontend/`: cinematic vanilla HTML/CSS/JS product demo.
- `agents/`: deterministic product-facing reasoning modules.
- `knowledge/`: Foundry IQ knowledge pack, Fabric-style ontology, and Work IQ-style synthetic signals.
- `synthetic_data/`: synthetic Copilot-style interaction logs and week comparison data.
- `evals/`: lightweight QA scripts, checklist, rubric, and test cases.
- `docs/`: demo script, architecture notes, setup notes, storyboard, and submission checklist.

## Multi-Agent System

Syntrix uses six product-facing agents:

- **Master Agent:** orchestrates the Microsoft 365 signal-to-blueprint factory loop.
- **Signal Discovery Agent:** detects repeated patterns from Microsoft 365-style synthetic signals.
- **Pattern Scoring Agent:** ranks patterns using Impact Score, ROI, and Confidence Score signals.
- **Blueprint Architect Agent:** generates a review-ready Copilot Agent Blueprint.
- **Safety Governance Agent:** applies deployment readiness gates, traceability, and sensitive-content controls.
- **Learning Loop Agent:** prepares controlled blueprint updates from Week 1 vs Week 3 signals.

## Syntrix Reasoning Engine

`POST /api/analyze` returns one complete reasoning response with:

- `master_agent_summary`
- `reasoning_trace`
- `opportunity_scores`
- `recommended_blueprint`
- `copilot_agent_blueprint`
- `governance_gates`
- `learning_loop_recommendation`
- `iq_evidence`

The engine is deterministic, local, and explainable. It does not call Microsoft Graph, Copilot Studio, paid APIs, hidden model calls, or live enterprise systems to run.

The generated `copilot_agent_blueprint` is a review-ready Microsoft 365 Copilot Agent Blueprint with department, business problem, detected work pattern, Microsoft 365 Signals Used, suggested knowledge sources, suggested actions, system instructions, guardrails, estimated hours saved, estimated annual ROI, Confidence Score, Impact Score, deployment readiness, Copilot Studio review notes, Foundry IQ grounding, evaluation tests, human approval points, and continuous improvement recommendation.

## Microsoft IQ Integration

Syntrix uses a three-part Microsoft IQ story:

- **Foundry IQ:** live verified in Azure Foundry with synthetic governance documents.
- **Fabric IQ:** represented through a local semantic ontology layer.
- **Work IQ:** represented through Microsoft 365-style synthetic work-context signals.

### Live Foundry IQ Verification

Syntrix has a real Microsoft Foundry knowledge base that was created and tested in Azure Foundry using the synthetic Syntrix knowledge pack. The Foundry agent successfully answered from the uploaded synthetic governance documents.

Non-secret verification details:

| Item | Value |
| --- | --- |
| Foundry project | `syntrix-project` |
| Foundry IQ / Azure AI Search resource | `syntrix-project-srch` |
| Knowledge base | `kb-syntrix-agent-knowledge` |
| Knowledge source | `syntrix-governance-docs` |
| Resource group | `rg-mdvs2-1164` |
| Region | `Canada East` |
| Pricing tier | `Basic` |
| Data used | Synthetic markdown documents only |
| Proof screenshot | `docs/assets/foundry-iq-live-proof.png` |

No Azure credentials, API keys, connection strings, tenant secrets, or private environment files are included in the public repo.

### Foundry IQ-ready Knowledge Pack

`knowledge/foundry_iq_pack/` contains approved synthetic markdown sources used for grounding blueprint and governance recommendations:

- Agent design principles
- Enterprise AI governance
- Copilot adoption patterns
- Safe agent deployment checklist
- Blueprint quality standards
- Agent readiness rubric

### Fabric IQ Semantic Ontology

`knowledge/fabric_ontology/syntrix_ontology.json` models:

- `UserProfile`
- `WorkSignal`
- `WorkPattern`
- `AgentOpportunity`
- `AgentBlueprint`
- `GovernanceGate`
- `EvaluationCase`
- `LearningLoopUpdate`

This is a local semantic ontology layer. It does not claim live Fabric IQ integration.

### Work IQ Synthetic Work Signals

`knowledge/work_iq_signals/work_context_signals.json` models synthetic work context:

- Frequent apps
- Meeting load
- Collaboration patterns
- Recurring tasks
- Output preferences
- Stakeholder context
- Approval sensitivity

This is a local Microsoft 365-style synthetic work-context signal layer. It does not use real Microsoft Graph, Copilot Studio, Microsoft 365 tenant data, email, customer, employee, or company data.

## Safety and Governance

Syntrix is a governed Copilot Agent Blueprint generation system, not an autonomous write agent.

- Human approval before external communication.
- Human approval before system changes.
- Source traceability required.
- Sensitive HR, legal, financial, employee-impacting, and customer-impacting content flagged.
- No autonomous write actions without approval.
- Learning loop recommends controlled blueprint updates; it does not silently retrain a model.

## Synthetic Data Policy

This repository uses synthetic data only.

- No real emails.
- No real customers.
- No real employees.
- No confidential documents.
- No production exports.
- No secrets or paid API keys.
- No Azure credentials required for the local demo.

Synthetic data lives in `synthetic_data/` and `knowledge/`.

## How To Run Locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Run the primary cinematic demo:

```bash
uvicorn backend.main:app --reload --port 8000
```

Open:

- Product demo: `http://localhost:8000`
- API docs: `http://localhost:8000/docs`

Run the Streamlit backup:

```bash
streamlit run app.py
```

## API Endpoints

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/` | GET | Serves the cinematic frontend |
| `/docs` | GET | FastAPI Swagger docs |
| `/api/health` | GET | Health check |
| `/api/profiles` | GET | Synthetic workspace profile list |
| `/api/interactions` | GET | Synthetic interaction records |
| `/api/analyze` | POST | Full Syntrix Agent Factory reasoning response |
| `/api/blueprint` | POST | Standalone Copilot Agent Blueprint generation |
| `/api/iq/status` | GET | IQ Layer status with Foundry live-verification metadata |
| `/api/iq/evidence` | GET | Grounded evidence and citations |
| `/api/iq/retrieve` | POST | Query local IQ evidence |
| `/api/evaluation/summary` | GET | Evaluation summary |

Example:

```bash
curl -X POST http://localhost:8000/api/analyze ^
  -H "Content-Type: application/json" ^
  -d "{\"profile\":\"Project Manager\"}"
```

## Demo Flow

1. Open `http://localhost:8000`.
2. Start with the thesis: "Do not ask users to design agents. Let AI discover the agents they already need."
3. Use the Microsoft 365 Signals selector.
4. Show task frequency and Impact Score.
5. Walk through the Syntrix Agent Factory and reasoning trace.
6. Show the generated Copilot Agent Blueprint.
7. Point to Copilot Studio Review Gates.
8. Show Microsoft IQ-ready architecture, Foundry live verification, and cited synthetic evidence.
9. Close with the Syntrix Learning Loop: controlled recommendations, not silent retraining.

## Evaluation and QA

Run:

```bash
python -m compileall backend agents evals
python evals/qa_reasoning_engine.py
python evals/qa_iq_layer.py
```

These verify that:

- Synthetic data loads.
- Reasoning pipeline runs.
- At least three opportunities are scored.
- A Copilot Agent Blueprint is generated.
- Governance gates are present.
- Learning loop recommendation is present.
- IQ knowledge pack, ontology, signals, evidence, and citations load.

Additional public evaluation materials:

- `evals/scoring_rubric.md`
- `evals/test_cases.md`
- `evals/qa_checklist.md`
- `docs/final_qa.md`

## Hackathon Judging Rubric Alignment

- **Accuracy & relevance:** Copilot Agent Blueprints are tied to repeated synthetic work patterns and transparent impact scores.
- **Reasoning & multi-step thinking:** Master Agent coordinates specialist agents and returns a reasoning trace.
- **Creativity & originality:** Syntrix reframes agent creation as Agent Factory blueprint generation from Microsoft 365-style signals, not manual configuration.
- **User experience & presentation:** cinematic frontend tells a complete product story with Microsoft 365 Signals, Pattern Intelligence, Copilot Agent Blueprints, governance, IQ evidence, Foundry verification, and deployment readiness.
- **Reliability & safety:** local deterministic pipeline, synthetic data policy, no secrets, no required paid APIs, human approval gates.
- **Community vote:** clear thesis, strong enterprise relevance, and a polished story judges can understand quickly.

## Key Public Docs

- `docs/demo_script.md`
- `docs/video_storyboard.md`
- `docs/submission_checklist.md`
- `docs/final_qa.md`
- `docs/judging_rubric_mapping.md`
- `docs/architecture_overview.md`
- `docs/foundry_iq_setup.md`
- `docs/hackathon_submission_safety.md`

## Project Structure

```text
ReasoningAgent/
|-- app.py
|-- backend/
|-- frontend/
|-- agents/
|-- synthetic_data/
|-- knowledge/
|   |-- foundry_iq_pack/
|   |-- fabric_ontology/
|   `-- work_iq_signals/
|-- diagrams/
|-- docs/
|-- evals/
|-- outputs/
|-- requirements.txt
`-- README.md
```

## Internal Product Labels

- Syntrix Reasoning Engine
- Syntrix Impact Score
- Syntrix Copilot Agent Blueprint
- Syntrix Continuous Improvement Loop
