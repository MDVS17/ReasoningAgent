# Live Foundry IQ Verification Setup

This document records the non-secret Microsoft Foundry IQ verification completed for Syntrix.

## Scope

Syntrix was verified with a real Microsoft Foundry knowledge base using synthetic markdown documents from the Syntrix knowledge pack. No real company data, emails, customers, employees, credentials, secrets, or confidential files were uploaded.

This verification applies to Foundry IQ only. Fabric IQ and Work IQ are represented in this repository as local architecture layers using a semantic ontology and synthetic work-context signals.

## Azure Resources

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

## Setup Steps Completed

1. Created or opened the Microsoft Foundry project `syntrix-project`.
2. Created the Foundry IQ / Azure AI Search resource `syntrix-project-srch`.
3. Created the knowledge base `kb-syntrix-agent-knowledge`.
4. Added the knowledge source `syntrix-governance-docs`.
5. Uploaded synthetic markdown documents from `knowledge/foundry_iq_pack/`.
6. Tested the Foundry agent against the knowledge base.
7. Captured the proof screenshot at `docs/assets/foundry-iq-live-proof.png`.

## Test Question

```text
What governance gates should a generated agent blueprint include?
```

## Success Criteria

The Foundry agent should answer from the knowledge base using the synthetic governance documents and mention controls such as:

- Human approval before external communication.
- Human approval before system changes.
- Source traceability.
- Sensitive content flagging.
- No autonomous write actions without approval.

## Troubleshooting Notes

- If Azure AI Search creation fails, register the `Microsoft.Search` provider in the Azure subscription.
- If capacity is blocked in the selected region, choose another supported region.
- If retrieval returns `403`, assign the appropriate `Search Index Data Reader` or `Search Index Data Contributor` role.
- Ensure networking allows access for the demo environment.
- Confirm only synthetic markdown files are uploaded.

## Credential Boundary

The public repository does not include Azure credentials, API keys, connection strings, or tenant secrets. `.env.example` documents placeholder names only.
