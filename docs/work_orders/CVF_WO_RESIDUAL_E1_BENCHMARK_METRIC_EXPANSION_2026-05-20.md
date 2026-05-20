# Work Order — Residual E1: Operational Benchmark Metric Expansion

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Worker role: Codex (Implementer)

Orchestrator: Claude

Date dispatched: 2026-05-20

Predecessor:

- `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md` (Candidate E1, REBUTTAL_ACCEPTED)
- `docs/reviews/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_CODEX_REBUTTAL_2026-05-19.md` (Codex verdict: NON_BLOCKING_AFTER_ASSESSMENT_FIX)
- `docs/reviews/CVF_LANE_E_BENCHMARK_REORIENTATION_COMPLETION_2026-05-19.md` (W3 closed)

Assessment correction already applied: Problem E is now scored PARTIAL overall
in `docs/reviews/CVF_17_05_REVIEW_CVF_RESIDUAL_PAIN_POINTS_ASSESSMENT_2026-05-19.md`.

---

## Purpose

Extend the offline governance benchmark from 9 to 12 metrics by adding the
three computable residual metrics (human correction rate, long-horizon
stability rate, rollback success rate) plus the required upstream audit-event
schema additions.

Hallucination recovery is explicitly REJECTED in this work order — it requires
LLM-judged event classification, which is out of scope for the offline
benchmark.

---

## Scope / Target / Owner Boundary

In scope:

- Two new audit-event types: `operator_correction`, `rollback` (with
  `success: boolean` field).
- Three new metric functions in
  `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`:
  `humanCorrectionRate`, `longHorizonStabilityRate`, `rollbackSuccessRate`.
- Extension of `GovernanceReliabilityReport` from 9 fields to 12.
- Extension of benchmark table and JSON output formatters to include the
  three new metrics.
- Test coverage for all three new metrics.
- Closure review recording hallucination recovery as REJECTED.

Out of scope:

- Hallucination recovery metric (LLM-judged, rejected).
- Live benchmark mode (remains offline only).
- Any new CLI commands or subcommands beyond those already in W3.
- Provider API calls of any kind.
- Changes to any file outside `CVF_ECO_v2.2_GOVERNANCE_CLI/`.

Constraint: upstream event-type additions must be merged BEFORE the metric
functions that consume them. Do not ship metric code that references undefined
event types.

---

## Deliverables

### Step E1.1 — GC-018 Baseline

File: `docs/baselines/CVF_GC018_E1_BENCHMARK_METRIC_EXPANSION_2026-05-20.md`

Required sections: `## Status`, `## Source or Predecessor Evidence`,
`## Purpose / Decision / Baseline`, `## Scope or Proposed Tranche`,
`## Evidence / Required Evidence / Verification`, `## Claim Boundary`.

The baseline must:

- Reference W3 closure and Codex rebuttal NON_BLOCKING verdict.
- List the three new metrics and their data dependencies explicitly.
- Name `hallucination_recovery` as explicitly rejected and state the reason
  (LLM-judged classification out of scope for offline benchmark).
- State that the benchmark remains offline only.

### Step E1.2 — Audit-Event Schema Extension

Target file: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`
(or the upstream type file if the event schema is defined there).

Add two new event types:

```typescript
// operator_correction event — emitted when a human operator corrects an
// AI-generated output. Required fields:
//   executionId: string
//   correctedAt: string (ISO 8601)
//   correctionSource: "operator" | "reviewer"

// rollback event — emitted when an execution is rolled back.
// Required fields:
//   executionId: string
//   rolledBackAt: string (ISO 8601)
//   success: boolean
```

Both types must be part of the typed audit-event discriminated union (or
equivalent typed registry). Do not add them as string literals.

### Step E1.3 — New Metric Functions

Add to `governance-reliability-metrics.ts`:

```typescript
// humanCorrectionRate(events: AuditEvent[]): number
//   — ratio of executions that received an operator_correction event to
//     total executions in the input window.
//   — Denominator: distinct executionId count.
//   — Returns 0 when no executions present.

// longHorizonStabilityRate(events: AuditEvent[], windowDays: number): number
//   — ratio of executions whose last audit event falls within windowDays of
//     the first event for the same executionId, with no policy_violation or
//     rollback(success=false) event in between.
//   — Data already exists in the JSONL audit log; no new upstream field needed.
//   — Returns 1.0 when no executions present (vacuously stable).

// rollbackSuccessRate(events: AuditEvent[]): number
//   — ratio of rollback events with success=true to total rollback events.
//   — Returns null (not 0) when no rollback events are present, to avoid
//     misleading a 0% rate when rollbacks never occurred.
```

### Step E1.4 — Report and Formatter Extension

Extend `GovernanceReliabilityReport`:

```typescript
humanCorrectionRate: number;
longHorizonStabilityRate: number;
rollbackSuccessRate: number | null;
```

Extend both formatters:

- Table formatter: add three new rows with the same column alignment as the
  existing nine metrics.
- JSON formatter: include all three new fields in output.

### Step E1.5 — Test Coverage

File decision: check current line count of
`tests/governance-reliability-metrics.test.ts` before adding tests.

- If adding ~12 tests stays within the `test_code` governed threshold
  (800 lines advisory, 1000 lines hard): add to the existing file.
- If adding would exceed the threshold: create
  `tests/governance-reliability-metrics.expansion.test.ts` as a dedicated
  file.

Minimum tests per metric:

- `humanCorrectionRate`: 3 tests — no events, events with corrections,
  events without corrections.
- `longHorizonStabilityRate`: 3 tests — no events, stable window,
  unstable window (rollback or violation in window).
- `rollbackSuccessRate`: 3 tests — no rollback events (returns null), all
  successful, mixed.

All tests must use fixture JSONL data, no live API calls.

### Step E1.6 — Closure Review

File: `docs/reviews/CVF_E1_BENCHMARK_METRIC_EXPANSION_CLOSURE_REVIEW_2026-05-20.md`

Required structure: Purpose, Target, Scope/Methodology, Findings,
Decision/Disposition, Claim Boundary.

The closure review must confirm:

- Schema extension shipped before metric functions.
- Three new metric functions present and tested.
- `GovernanceReliabilityReport` extended to 12 fields.
- Both formatters updated.
- Hallucination recovery recorded as explicitly rejected with reason.
- Benchmark remains offline only.
- `npm test` PASS in `CVF_ECO_v2.2_GOVERNANCE_CLI`.
- `npm run check` PASS (TypeScript type-check).
- Problem E status confirmed as PARTIAL-then-CLOSED after this tranche.

---

## Acceptance Criteria

All of the following must be true before this work order is CLOSED:

- [ ] GC-018 baseline exists and is AUTHORIZED.
- [ ] Two new audit-event types defined in the typed schema.
- [ ] Three new metric functions implemented and exported.
- [ ] `GovernanceReliabilityReport` has 12 fields.
- [ ] Table and JSON formatters include all 12 metrics.
- [ ] Minimum 9 new tests added (3 per metric), all PASS.
- [ ] `npm test` PASS in `CVF_ECO_v2.2_GOVERNANCE_CLI`.
- [ ] `npm run check` PASS.
- [ ] Pre-commit and pre-push hooks PASS.
- [ ] Closure review filed confirming hallucination recovery rejected.

---

## Forbidden Actions

- Do NOT implement hallucination recovery (LLM-judged, rejected).
- Do NOT promote the benchmark to live mode.
- Do NOT add new CLI commands in this tranche.
- Do NOT make provider API calls.
- Do NOT change files outside `CVF_ECO_v2.2_GOVERNANCE_CLI/`.
- Do NOT ship metric functions before the upstream event types are defined.

---

## Authority Chain

- Authorized by: Codex rebuttal (E1: NON_BLOCKING_AFTER_ASSESSMENT_FIX); assessment correction applied 2026-05-20
- Roadmap: `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md` (REBUTTAL_ACCEPTED)
- Predecessor: `docs/reviews/CVF_LANE_E_BENCHMARK_REORIENTATION_COMPLETION_2026-05-19.md` (W3 CLOSED)
- Orchestrator: Claude; Worker: Codex; Operator approval required for GC-018

---

## Agent Roles

- Worker (Codex): all implementation steps, GC-018, tests, closure review
- Orchestrator (Claude): reviews closure review after filing

---

## Required First Reads

1. `docs/roadmaps/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_2026-05-19.md` — E1 scope
2. `docs/reviews/CVF_REVIEW_CVF_RESIDUAL_CLOSURE_ROADMAP_CODEX_REBUTTAL_2026-05-19.md` — E1 verdict + downstream guards
3. `docs/reviews/CVF_LANE_E_BENCHMARK_REORIENTATION_COMPLETION_2026-05-19.md` — W3 baseline (existing 9 metrics)
4. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts` — current implementation

---

## Pre-Flight Checks

- [ ] Confirm W3 closure review remains CLOSED
- [ ] Read current `governance-reliability-metrics.ts` to confirm 9 existing metric functions
- [ ] Check current test file line count before deciding whether to extend or create new file
- [ ] Confirm `npm test` baseline PASS in `CVF_ECO_v2.2_GOVERNANCE_CLI`

---

## Write Ownership

May create or modify only files under `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/`, plus:

- `docs/baselines/CVF_GC018_E1_BENCHMARK_METRIC_EXPANSION_2026-05-20.md` (new)
- `docs/reviews/CVF_E1_BENCHMARK_METRIC_EXPANSION_CLOSURE_REVIEW_2026-05-20.md` (new)

No other files may be created or modified.

---

## Execution Plan

1. File GC-018 baseline (Step E1.1) — must be AUTHORIZED before schema work
2. Add audit-event schema extension (Step E1.2) — before metrics
3. Add three metric functions (Step E1.3) — after schema
4. Extend report and formatters (Step E1.4)
5. Add test coverage (Step E1.5)
6. File closure review (Step E1.6)

---

## Evidence Requirements

- GC-018 baseline AUTHORIZED with explicit rejection of hallucination recovery
- `governance-reliability-metrics.ts` exports 12 metric functions (was 9)
- `GovernanceReliabilityReport` has 12 fields
- Both table and JSON formatters updated
- Test file(s) with minimum 9 new tests, all PASS
- `npm test` PASS, `npm run check` PASS

---

## Review Gate

Stop and return to Orchestrator if:

- Schema extension requires modifying files outside the CLI extension
- Hallucination recovery cannot be cleanly rejected without scope inflation

---

## Closure Checklist

- [ ] GC-018 AUTHORIZED
- [ ] 2 new event types in schema (`operator_correction`, `rollback`)
- [ ] 3 new metric functions implemented and exported
- [ ] `GovernanceReliabilityReport` has 12 fields
- [ ] Both formatters updated
- [ ] Minimum 9 new tests PASS
- [ ] `npm test` PASS, `npm run check` PASS
- [ ] Hallucination recovery explicitly REJECTED in closure review
- [ ] Pre-commit and pre-push hooks PASS

---

## Return-To-Orchestrator Conditions

Return if: metric implementation requires changes outside the CLI extension; hook failure outside this scope.

---

## Claim Boundary

This work order covers schema extension + 3 metrics + formatter extension +
tests + closure review only. It does not extend to CLI command changes (C1),
provider method contracts (D1), role catalog (G1), or memory tier gates (H1).
The offline benchmark boundary is preserved.
