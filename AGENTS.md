# AGENTS.md

## Product

Syntrix is a hackathon-quality reasoning agent demo that turns synthetic Copilot-style usage into safe personalized AI agent blueprints.

## Operating Principles

- Storytelling first.
- Synthetic data only.
- No paid APIs in the local demo.
- No real company, customer, employee, email, or confidential data.
- Multi-agent reasoning beats generic chat.
- Keep modules readable and demoable.
- Prefer deterministic outputs until real model integrations are intentionally added.

## Agent Roles

### Pattern Discovery Agent

Finds repeated workflows across synthetic Copilot-style interaction logs.

### Opportunity Scoring Agent

Calculates the **Syntrix Opportunity Score** using frequency, time saved, repetition, business value, and risk.

### Blueprint Generation Agent

Produces the **Syntrix Agent Blueprint** with purpose, triggers, tools, guardrails, approvals, tests, and improvement recommendations.

### Safety Review Agent

Checks data boundaries, approval gates, governance controls, and risk level before a blueprint is presented.

### Continuous Improvement Agent

Compares Week 1 and Week 3 usage to recommend future refinements.

## Engineering Guidance

- Use Python, Streamlit, pandas, plotly, pydantic, python-dotenv, Markdown, and Mermaid.
- Keep `agents/` modular.
- Keep synthetic datasets in `synthetic_data/`.
- Put sample generated artifacts in `outputs/`.
- Put evaluation cases and rubrics in `evals/`.
- Put architecture diagrams in `diagrams/`.
- Do not add real secrets to `.env` or source files.
