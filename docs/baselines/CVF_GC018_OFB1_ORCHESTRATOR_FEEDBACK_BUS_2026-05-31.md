# CVF GC-018 Fast Lane — OFB-1 Orchestrator Feedback Bus

Memory class: BASELINE_RECORD

Status: AUTHORIZED

Date: 2026-05-31

Parent: LHW18 T1 Failure Simulation gap-map + CBP-1 context budget advisory

---

## Purpose

Authorize OFB-1: aggregate all subagent feedback signals (worker timeout,
reviewer rejection count, context budget, human intervention flag) into a
single structured `orchestratorFeedback` field in `/api/execute` ALLOW response
and a new `cvf_get_feedback_summary` MCP tool. Closes the "feedback captured
but not surfaced" gap identified in the Orchestrator monitoring audit (2026-05-31).

## Scope / Target / Owner Boundary

Target: `cvf.orchestratorFeedbackBus.ofb1.v1`
Owner: `cvf-web/src/lib/orchestrator-feedback-bus.ts` (new) + `/api/execute` (additive field) + `CVF_ECO_v2.5_MCP_SERVER` (new tool).
Boundary: additive advisory only; no execution blocking; no routing decisions made by CVF; `runtimeExecutionAuthorized=false`. route.ts is AT hard limit 1000 — must inline or shorten elsewhere.

## Source / Predecessor Evidence

- Audit: `pipeline-chain-orchestrator.ts` — `PipelineChainState` has `workerRetryCount`, `reviewerRetryCount`, `humanInterventionRequired`, `receipts[]`
- EL-2: `worker-timeout-handler.ts` — `WorkerTimeoutReadout.triggered`, `retryCount`, `escalateToOrchestrator`
- EL-3: `reviewer-deadlock-handler.ts` — `ReviewerDeadlockReadout.rejectionCount`, `triggered`, `decomposedWorkOrders`
- CBP-1: `context-budget-readout.ts` — `withinBudget`, `budgetTokens`
- Gap: all signals advisory only; no aggregated view; Orchestrator cannot subscribe

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED as Fast Lane R1 (additive advisory aggregation; no behavior change).

Proposed deliverables:
1. `cvf-web/src/lib/orchestrator-feedback-bus.ts` — `buildOrchestratorFeedbackSummary(workerTimeout, reviewerDeadlock, contextBudget)` returns structured `OrchestratorFeedbackSummary` with all signals aggregated
2. `route.ts` — inline `orchestratorFeedback` field on ALLOW path. Route.ts is at 1000 lines — must compress existing inline to stay at limit.
3. `cvf_get_feedback_summary` MCP tool in `CVF_ECO_v2.5_MCP_SERVER/src/index.ts` — Orchestrator can poll feedback summary by receiptId
4. Unit tests: `route.orchestrator-feedback-bus.test.ts` (≥6 tests)

## Evidence / Verification

- `OrchestratorFeedbackSummary` has: `workerTimeoutSignal`, `reviewerRejectionSignal`, `contextBudgetSignal`, `humanInterventionRequired`, `overallSignal`, `recommendedAction`
- `overallSignal`: `"NOMINAL" | "CAUTION" | "ESCALATE"`
- `recommendedAction`: structured string Orchestrator can read to decide next step
- route.ts stays at ≤ 1000 lines
- MCP server stays at ≤ 1000 lines (currently 868)
- Unit tests PASS, TypeScript PASS, live proof PASS

## Claim Boundary

`runtimeExecutionAuthorized=false` — OFB-1 aggregates and surfaces signals only.
CVF does NOT make routing decisions. The Orchestrator (AI agent) reads the feedback
and decides whether to re-decompose, escalate, or change model. No new receipt envelope.

## Fast Lane Risk Assessment

Risk class: R1. Same additive pattern as EL-2/EL-3/CBP-1.
Fast Lane authorized: YES.
