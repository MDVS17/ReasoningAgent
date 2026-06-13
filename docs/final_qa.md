# Syntrix Final QA

Run these checks before submitting or recording the final demo.

## Compile Check

```bash
python -m compileall backend agents evals
```

Expected: Python files compile without errors.

## Start Local App

```bash
uvicorn backend.main:app --reload --port 8000
```

Expected local app URL:

```text
http://localhost:8000
```

## Health Endpoint

```bash
curl http://localhost:8000/api/health
```

Expected: `status` is `ok`.

## Analyze Endpoint

```bash
curl -X POST http://localhost:8000/api/analyze ^
  -H "Content-Type: application/json" ^
  -d "{\"profile\":\"Project Manager\"}"
```

Expected: response includes `master_agent_summary`, `reasoning_trace`, `opportunity_scores`, `recommended_blueprint`, `governance_gates`, and `learning_loop_recommendation`.

## IQ Status Endpoint

```bash
curl http://localhost:8000/api/iq/status
```

Expected: response includes:

- Foundry IQ status `live_verified`.
- Foundry project `syntrix-project`.
- Knowledge base `kb-syntrix-agent-knowledge`.
- Fabric IQ ontology metadata.
- Work IQ synthetic signal metadata.

## Docs Endpoint

```bash
curl http://localhost:8000/docs
```

Expected: Swagger docs page returns successfully.

## Scripted QA

```bash
python evals/qa_reasoning_engine.py
python evals/qa_iq_layer.py
```

Expected: both scripts report `"passed": true`.

## Safety Check

- No Azure credentials are included in the public repo.
- No `.env` file is committed.
- No real company data is used.
- Foundry IQ is described as live verified.
- Fabric IQ is described as a semantic ontology layer.
- Work IQ is described as synthetic work-context signals.
