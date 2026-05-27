# CVF Work Order — LHW3-T1 Operational Failure Trend Readout Connector

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-27

---

## Purpose

Implement LHW3-T1: a connector spec mapping W4 operational benchmark scorecard
metrics and V3 execution diagnostic classes into a failure-trend readout chain.
Closes the gap where W4 reports per-call metrics and V3 exposes diagnostic
classes, but no connector standard ties recurring failure patterns into a
trend signal with recommended operator action.

Documentation-only tranche. No source code, runtime module, route, or provider
behavior is changed.

## Authority Chain

- LHW3 roadmap: `docs/roadmaps/CVF_LHW3_WORKFLOW_CONNECTOR_WAVE3_ROADMAP_2026-05-27.md`
- Fast Lane audit: `docs/reviews/CVF_LHW3_T1_FAST_LANE_AUDIT_2026-05-27.md` → FAST_LANE_READY
- LH1 ledger (`abtop` trigger): `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- W4: `docs/reviews/CVF_W4_OPERATIONAL_BENCHMARK_SCORECARD_COMPLETION_2026-05-24.md`
- V3: `docs/reviews/CVF_V3_EXECUTION_DIAGNOSTIC_CONTRACT_COMPLETION_2026-05-24.md`
- V3 route source: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- W4 metric source: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`
- W4 scorecard source: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts`
- LHW2-T1 spec: `docs/reference/CVF_LHW2_MEMORY_EVENT_CAPTURE_WORKFLOW_RECEIPT_LOOP_CONNECTOR_SPEC_2026-05-27.md`

## Agent Roles

Implementer writes spec (S1–S5) using W4 + V3 vocabulary verbatim. Reviewer
checks W4 metric names verbatim, V3 class tokens verbatim, boundary table
honest, no runtime claim added, no `.ts` file touched, S5 Source Verification
complete with no `BLOCKED_SOURCE_NOT_FOUND` rows. Auditor confirms LH1 trigger
documented, no live dashboard or alerting runtime claimed. No self-review.

## Scope

**Allowed:**

- `docs/reference/CVF_LHW3_OPERATIONAL_FAILURE_TREND_READOUT_CONNECTOR_SPEC_2026-05-27.md`
  (new — primary deliverable)
- this work order (status update only)
- session continuity files

**Forbidden:** `EXTENSIONS/` (any file), `governance/contracts/` (any file),
`src/lib/workflows/` (any file), any `.ts`/`.tsx`/`.js`/`.py` file, receipt
envelope schema, public-sync repo. Live observability dashboard and alerting
runtime remain blocked.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reviews/CVF_W4_OPERATIONAL_BENCHMARK_SCORECARD_COMPLETION_2026-05-24.md`
   — confirm the W4 scorecard metric field names:
   `taskCompletionRate`, `policyViolationRate`, `receiptIntegrityRate`,
   `retryCount`, `humanCorrectionCount`, `crossSessionContinuityRate`,
   `longHorizonStabilityRate`, `deterministicConsistencyRate`,
   `rollbackSuccessRate`; note `hallucinationRecovery` is deferred
4. `docs/reviews/CVF_WR1_WORKFLOW_RECOVERY_STATE_PROOF_COMPLETION_2026-05-25.md`
   — understand recovery readout structure only; WR1 is not the source
   authority for V3 diagnostic class tokens
5. `docs/reviews/CVF_V3_EXECUTION_DIAGNOSTIC_CONTRACT_COMPLETION_2026-05-24.md`
   — confirm V3 completion evidence for `model_unavailable` and
   `policy_blocked`
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
   — confirm route diagnostic classes: `invalid_input`, `routing_denied`,
   `unknown_error`, `provider_empty_output`
7. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts`
   and `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/operational-benchmark-suite.test.ts`
   — confirm diagnostic readout extraction and benchmark sample classes
   `provider_timeout` and `receipt_missing`
8. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`
   — confirm metric functions and metric field names used by W4
9. `docs/reference/CVF_LHW2_MEMORY_EVENT_CAPTURE_WORKFLOW_RECEIPT_LOOP_CONNECTOR_SPEC_2026-05-27.md`
   — understand the S2/S5 table pattern for field mapping and boundary table
10. `docs/reference/CVF_LHW3_WORKFLOW_CONNECTOR_WAVE3_ROADMAP_2026-05-27.md`
   — confirm T1 deliverable shape

If any required file is missing, stop and report to Orchestrator.

## Pre-Dispatch Source Verification Block

The work-order author has verified these source anchors before dispatch.
Worker must preserve these exact source-backed names and must not introduce
draft-only diagnostic tokens.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| W4 scorecard metric fields cited in S2 | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/operational-benchmark-suite.ts` | lines 22-30, 135-143 | `taskCompletionRate`, `retryCount`, `policyViolationRate`, `humanCorrectionCount`, `receiptIntegrityRate` | `OperationalBenchmarkMetrics` / `OperationalBenchmarkScorecard` | ACCEPT |
| W4 reliability metric functions cited in S2 | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts` | lines 57, 93, 106, 114, 153 | `receiptIntegrityRate`, `taskCompletionRate`, `retryCount`, `policyViolationRate`, `humanCorrectionCount` | governance reliability metrics module | ACCEPT |
| V3 diagnostic token `policy_blocked` | `docs/reviews/CVF_V3_EXECUTION_DIAGNOSTIC_CONTRACT_COMPLETION_2026-05-24.md` | line 104 | `policy_blocked` | V3 diagnostic completion evidence | ACCEPT |
| V3 diagnostic token `model_unavailable` | `docs/reviews/CVF_V3_EXECUTION_DIAGNOSTIC_CONTRACT_COMPLETION_2026-05-24.md` | line 94 | `model_unavailable` | V3 diagnostic completion evidence | ACCEPT |
| Route diagnostic tokens | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 112, 570, 869 | `invalid_input`, `routing_denied`, `unknown_error`, `provider_empty_output` | `buildExecutionDiagnostic` route usage | ACCEPT |
| Benchmark diagnostic sample tokens | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/operational-benchmark-suite.test.ts` | lines 219, 229, 255-256 | `provider_timeout`, `receipt_missing` | operational benchmark diagnostic sample | ACCEPT |

If implementation evidence contradicts any row above, worker must stop and
return `BLOCKED_SOURCE_CONFLICT` instead of inventing replacement vocabulary.

## Deliverable — Connector Spec

File: `docs/reference/CVF_LHW3_OPERATIONAL_FAILURE_TREND_READOUT_CONNECTOR_SPEC_2026-05-27.md`

Required sections:

### S1 — Purpose and claim boundary

- State what the connector is: a normative doc mapping W4 scorecard metric
  combinations and V3 diagnostic classes into a failure-trend readout chain.
- State what it is not: not a W4/V3 runtime extension; not a live dashboard;
  not a failure alerting engine.
- Explicit statement: "W4 `cvf.operationalBenchmark.v1` is the runtime evidence
  source for scorecard metrics; V3 `cvf.executionDiagnostic.v1` is the runtime
  evidence source for diagnostic class tokens. This connector extends those
  outputs to a standard trend readout shape usable by Orchestrator and operators."

### S2 — W4 metric + V3 class to trend signal mapping

Table columns: `W4 metric field` | `V3 diagnostic class` | `Trend signal` |
`Operator action recommendation`

Minimum rows:

- High `policyViolationRate` + `policy_blocked` or `routing_denied` class → overconstraint signal → review policy / routing boundaries
- High `retryCount` + `model_unavailable` or `provider_timeout` class → instability signal → check provider health / rotate provider
- Low `taskCompletionRate` + `invalid_input` class → underspecification signal → request clarification (see T2 loop)
- High `humanCorrectionCount` + `unknown_error` or `provider_empty_output` class → drift/degraded-output signal → review prompt engineering / pack selection
- Low `receiptIntegrityRate` + `receipt_missing` class → audit gap signal → inspect receipt chain

Use W4 metric field names and V3 diagnostic class tokens verbatim. If a field
name cannot be verified from runtime source, canonical contract, or completion
evidence listed in Required First Reads,
mark it `BLOCKED_SOURCE_NOT_FOUND`, stop the work order, and return to
Orchestrator. Draft-only diagnostic class tokens are blocking defects unless a
separate governed V3 source updates the vocabulary first.

### S3 — Drift signal interpretation rules

Prose description (max 10 lines): how an operator or next-agent reads the trend
readout packet:

- What a single elevated metric means vs. multiple co-occurring metrics
- What `rollbackSuccessRate` below 1.0 combined with `invalid_from_current_state`
  WR1 class means for governance escalation
- State explicitly: "Trend signals are advisory readout only. They do not
  automatically escalate, retry, or modify workflow state."

### S4 — Runtime-enforcement boundary table

| Behavior | Current status | Future path |
| --- | --- | --- |
| W4 scorecard metric collection | Runtime (Governance CLI) | Stable |
| V3 diagnostic class classification | Runtime (cvf-web route) | Stable |
| Metric-to-trend signal mapping | Document-only | Future: trend aggregator service |
| Drift signal threshold evaluation | Document-only | Future: policy-configurable threshold contract |
| Operator action routing | Document-only | Future: governance escalation queue |
| Live failure alerting | Document-only | Future: observability dashboard |

Do not label any row "Runtime" unless a closed PASS tranche implements it.

### S5 — Source Verification Table (mandatory)

Required columns: `Claimed item` | `Source file` | `Verified line/section` |
`Verified path or symbol` | `Owning interface/function/schema` | `Disposition`

Cover every W4 metric field and V3 diagnostic class token cited in S2. Valid
dispositions are `ACCEPT`, `REJECT`, and `BLOCKED_SOURCE_NOT_FOUND`. If any
item cannot be source-verified, mark it `BLOCKED_SOURCE_NOT_FOUND`, stop, and
return to Orchestrator. No blocked, guessed, draft-only, or unstaged source
fact may remain in S2.

## Pre-Flight

- [ ] Working tree clean
- [ ] All required first reads done
- [ ] W4 metric field names confirmed from W4 metric/scorecard source
- [ ] V3 diagnostic class tokens confirmed from V3 completion evidence,
      route source, or operational benchmark source/test evidence

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be
modified.

## Execution Plan

1. Read all required first reads.
2. Confirm W4 metric names and V3 class tokens from source files and completion
   evidence named above.
3. Draft spec (S1–S5) with Source Verification Table.
4. Confirm no code file staged.
5. Reviewer perspective — record result.
6. Update session continuity (`lhw3_t1_complete`).
7. Commit: `docs(lhw3-t1): add operational failure trend readout connector spec`.
8. Write completion review; include T2 gate answer (see below).

Spec size guard: < 200 lines. Trim S3 prose if approaching 180 lines.

## Evidence Requirements

- Spec at target path with all 5 sections present
- S2 field mapping table uses W4 and V3 vocabulary verbatim (no invented names)
- S3 drift signal rules state advisory-only constraint explicitly
- S4 boundary table present; no doc-only row labeled Runtime
- S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- No `.ts`/`.tsx`/`.js`/`.py` file in `git diff --name-only`
- Session continuity updated to `lhw3_t1_complete`
- Completion review written with T2 gate answer

## Acceptance Criteria

- [ ] Spec with all 5 sections created
- [ ] S2 maps at minimum 5 W4+V3 combinations to distinct trend signals
- [ ] S3 explicitly states trend signals are advisory only
- [ ] S4 boundary table honest (no doc-only row labeled Runtime)
- [ ] S5 Source Verification Table complete with no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] No code file in diff
- [ ] Session continuity updated

## Review Gate

Before committing: Reviewer perspective completed; all W4 field names verbatim;
all V3 class tokens verbatim; S4 boundary table honest; S5 complete with no
`BLOCKED_SOURCE_NOT_FOUND` rows; no code file in diff.

## Closure Checklist

- [ ] Spec created with all 5 sections
- [ ] S2 mapping table uses W4 + V3 vocabulary verbatim
- [ ] S3 advisory-only statement explicit
- [ ] S5 Source Verification Table complete; no `BLOCKED_SOURCE_NOT_FOUND` rows
- [ ] No code file in diff
- [ ] Session continuity updated
- [ ] Completion review with T2 gate answer written

## Return-To-Orchestrator Conditions

Stop and report to Orchestrator if:

- any required first read file is missing or unreadable;
- a W4 metric field name or V3 diagnostic class token cannot be confirmed from
  runtime source, canonical contract, or completion evidence named above without
  modifying source;
- writing the connector requires adding a new W4 metric or V3 class not in the
  existing vocabularies;
- spec exceeds 200 lines before S4 is complete.

## T2 Gate Output (required in completion review)

Answer explicitly: "Was a concrete clarification re-intake gap identified during
T1 work?"

- YES → describe gap in one sentence; T2 proceeds.
- NO → "No gap found. T2 proceeds per roadmap rationale."
  (T2 proceeds regardless — this output is informational.)

## Operator Checkpoint

operator.checkpoint.waiver: Low-risk documentation-only tranche gated by
source-verified W4 and V3 field names from current source and completion evidence; no
operator checkpoint required unless a conflict with W4/V3 vocabulary is
discovered during implementation.

## Claim Boundary

LHW3-T1 produces a documentation artifact. It does not claim W4/V3/WR1 runtime
extension, live observability dashboard, failure alerting, receipt envelope
extension, provider behavior, hosted readiness, production readiness, or public
release readiness.
