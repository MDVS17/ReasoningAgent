# Fabric Ontology

Synthetic semantic layer for Syntrix.

## Entities

- SyntheticUserProfile
- CopilotStyleInteraction
- WorkflowPattern
- AgentOpportunity
- SyntrixOpportunityScore
- SyntrixAgentBlueprint
- GovernanceControl
- EvaluationResult

## Relationships

- A SyntheticUserProfile produces CopilotStyleInteractions.
- CopilotStyleInteractions cluster into WorkflowPatterns.
- WorkflowPatterns produce AgentOpportunities.
- AgentOpportunities generate SyntrixAgentBlueprints.
- SyntrixAgentBlueprints require GovernanceControls and EvaluationResults.

## Boundary

No Microsoft Fabric workspace, tenant, lakehouse, or real semantic model is used in this local demo.
