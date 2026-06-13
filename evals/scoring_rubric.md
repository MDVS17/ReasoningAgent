# Syntrix Evaluation and Scoring Rubric

## Opportunity Score Rubric

The Syntrix Opportunity Score is a transparent local heuristic for hackathon demonstration.

| Dimension | Weight | Description |
| --- | ---: | --- |
| Frequency | 30% | How often the workflow appears in synthetic Copilot-style logs |
| Time saved | 25% | Estimated minutes saved per repeated workflow |
| Repetition | 20% | How templatable or pattern-like the workflow is |
| Business value | 20% | Value to leadership, delivery, people operations, or go-to-market outcomes |
| Risk penalty | -5% | Reduces score when workflow requires stronger governance |

## Blueprint Quality Rubric

| Criterion | Pass condition |
| --- | --- |
| Purpose | Explains what the agent helps the target user accomplish |
| Triggering work patterns | Tied to repeated synthetic interactions |
| Instructions | Clear, role-specific, and action-oriented |
| Knowledge sources | Lists approved synthetic or generic sources |
| Suggested tools/actions | Describes useful actions without connecting to live systems |
| Guardrails | Blocks real data and consequential autonomous actions |
| Human approval points | Requires review before sensitive or external actions |
| Evaluation tests | Defines checks before deployment |
| Continuous improvement | Recommends refinement from usage over time |

## Safety Rubric

- Must use synthetic data only.
- Must not contain real employees, customers, emails, or confidential information.
- Must keep write actions behind human approval.
- Must expose assumptions and limits.
- Must be demoable without paid APIs or live enterprise connectors.
