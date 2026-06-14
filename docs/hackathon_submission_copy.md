# Hackathon Submission Copy

## Project Name

Syntrix — Copilot Agent Architect

## Tagline

An AI Agent Factory for Microsoft 365.

## Keywords

Microsoft 365, Copilot, AI agents, Agent Factory, Azure AI Foundry, Foundry IQ, Microsoft Graph, Copilot Studio, enterprise AI, agent blueprints, governance, ROI

## Description

Syntrix is an AI Agent Factory for Microsoft 365 that discovers enterprise work patterns and generates review-ready Copilot Agent Blueprints. Instead of asking users to manually design agents, Syntrix analyzes Microsoft 365-style collaboration signals and identifies where repeated work, approvals, follow-ups, reporting routines, and knowledge gaps create high-value automation opportunities.

The demo uses simulated signals inspired by Outlook, Teams, SharePoint, OneDrive, Calendar, and Planner patterns. Syntrix applies Pattern Intelligence, scores opportunities by Business Impact, ROI, Confidence Score, Impact Score, and Deployment Readiness, then generates a complete Copilot Agent Blueprint. Each blueprint includes the business problem, detected work pattern, Microsoft 365 Signals Used, suggested knowledge sources, suggested actions, system instructions, guardrails, evaluation tests, human approval points, Foundry IQ grounding, and continuous improvement guidance.

Syntrix is designed for Microsoft 365 architecture while staying safe for a public hackathon submission. Foundry IQ was live verified in Azure Foundry with a synthetic governance knowledge base. Fabric IQ is represented through a semantic ontology layer, and Work IQ is represented through Microsoft 365-style synthetic work-context signals. The local MVP does not include credentials, real tenant data, live Microsoft Graph access, or Copilot Studio runtime deployment.

## Personal Story

I built Syntrix after seeing the gap between having access to Copilot and knowing how to use it strategically. People can use AI for one-off tasks, but the real organizational value is hidden in repeated workflows, approval loops, status updates, reporting routines, follow-ups, and knowledge gaps.

Syntrix was created to surface those patterns automatically. The idea is simple: do not ask every user to become an agent designer. Let an AI Agent Factory study the work signals, identify where a Copilot agent would create value, and generate a review-ready blueprint that a human can evaluate before deployment.

## Microsoft IQ Explanation

Syntrix uses a Microsoft IQ-ready architecture with a clear MVP boundary.

- **Foundry IQ:** live verified in Azure Foundry using a synthetic governance knowledge base. The repo includes non-secret setup notes and a proof screenshot at `docs/assets/foundry-iq-live-proof.png`.
- **Fabric IQ:** represented through a local semantic ontology layer that models users, work signals, work patterns, agent opportunities, Copilot Agent Blueprints, governance gates, evaluation cases, and learning loop updates.
- **Work IQ:** represented through Microsoft 365-style work-context signals using synthetic data inspired by collaboration patterns, recurring tasks, output preferences, stakeholder context, and approval sensitivity.
- **Microsoft 365 / Graph:** integrations are simulated for the MVP through a Graph-ready signal model. No live Microsoft Graph tenant data is used.
- **Copilot Studio:** Syntrix produces Copilot Studio Review-ready blueprints, but it does not claim live Copilot Studio runtime deployment.

No credentials, API keys, connection strings, secrets, real emails, real customers, real employees, confidential documents, or real tenant data are included in the public repository.

## Short Pitch

Copilot helps people work faster. Syntrix helps organizations discover which Copilot agents should exist next.

Syntrix turns Microsoft 365-style work signals into Pattern Intelligence, Pattern Intelligence into an Agent Factory, and the Agent Factory into governed Copilot Agent Blueprints ready for human review.

## Closing Line

Syntrix turns scattered Microsoft 365 work patterns into governed Copilot agents: discovered by Pattern Intelligence, designed by an Agent Factory, grounded by Foundry IQ, and ready for Copilot Studio Review.
