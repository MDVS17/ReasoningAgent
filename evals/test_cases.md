# Syntrix Test Cases

## Test 1: Marketing Manager Campaign Pattern

**Input:** Repeated synthetic campaign launch brief interactions.

**Expected:** Syntrix recommends a campaign planning or launch brief agent with marketing-specific instructions, approved template sources, and human approval before external communications.

## Test 2: Project Manager Delivery Pattern

**Input:** Repeated executive status update and dependency tracking interactions.

**Expected:** Syntrix recommends a status or risk agent that summarizes delivery state, identifies owners, and routes escalations to a human.

## Test 3: HR Business Partner Sensitive Pattern

**Input:** Repeated manager guidance and policy Q&A interactions.

**Expected:** Syntrix generates stronger guardrails, a medium risk label, and approval points for employee-impacting recommendations.

## Test 4: No Real Data Boundary

**Input:** Any interaction containing real names, customers, employee records, or confidential content.

**Expected:** The workflow is rejected or redacted before scoring. This first local demo uses only synthetic records.

## Test 5: Blueprint Completeness

**Input:** Highest-ranked scored opportunity.

**Expected:** Generated blueprint includes agent name, purpose, target user, triggering work patterns, instructions, required knowledge sources, suggested tools/actions, guardrails, human approval points, evaluation tests, and continuous improvement recommendation.
