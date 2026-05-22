# CVF Work Order E2 Operational Benchmark Suite

Memory class: FULL_RECORD

Status: CLOSED_E2_OPERATIONAL_BENCHMARK_SUITE

Date: 2026-05-22

## Purpose

Implement the E2 operational benchmark suite authorized by GC-018.

## Authority Chain

- Original source oracle: `.private_reference/legacy/CVF 17.05/Review CVF.md`
- Post-B/C assessment:
  `docs/reviews/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`
- Roadmap:
  `docs/roadmaps/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINT_ROADMAP_2026-05-22.md`
- D2 completion:
  `docs/reviews/CVF_D2_PROVIDER_CAPABILITY_MATRIX_COMPLETION_2026-05-22.md`
- GC-018:
  `docs/baselines/CVF_GC018_E2_OPERATIONAL_BENCHMARK_SUITE_2026-05-22.md`

## Agent Roles

- Orchestrator: Codex
- Implementer: Codex
- Reviewer: Codex, via tests and completion review
- Auditor: Codex, via completion packet and governance hooks

## Scope / Allowed Scope / Forbidden Scope

Allowed:

- add Governance CLI operational benchmark module and tests;
- extend existing governance reliability metric helpers with count metrics;
- add `cvf benchmark operational` command path;
- preserve existing `benchmark governance` and `benchmark run` behavior;
- file completion documentation.

Forbidden:

- new policy/risk guard semantics;
- live provider benchmark claim;
- output-quality benchmark or QBS rerun;
- route changes;
- receipt-envelope changes;
- public-sync or hosted-readiness work.

## Required First Reads

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/governance-reliability-metrics.test.ts`
- `docs/baselines/CVF_GOVERNANCE_RELIABILITY_BASELINE_2026-05-19.md`

## Pre-Flight Checks

- Confirm E2 is a benchmark reporting tranche, not a provider runtime tranche.
- Confirm no new live provider proof is claimed.
- Confirm hallucination recovery remains deferred without a bounded event
  contract.
- Confirm old benchmark commands remain compatible.

## Write Ownership

Primary write scope:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/`
- completion documentation and session state

## Execution Plan / Execution Rules

1. Add operational benchmark report schema.
2. Add audit JSONL and release-gate JSON ingestion.
3. Add evidence-mode breakdown.
4. Add retry and human-correction count metrics.
5. Add `cvf benchmark operational`.
6. Verify targeted and full Governance CLI tests.
7. File completion review and commit E2.

## Acceptance Criteria

- Operational report exposes all Review-CVF operational metrics.
- Live, offline, fixture, and unknown evidence modes are separated.
- Release-gate JSON-style evidence can be ingested.
- Hallucination recovery is explicitly deferred with replacement metrics.
- Existing benchmark commands remain compatible.

## Evidence Requirements

- Targeted E2 tests pass.
- Full Governance CLI tests pass.
- Governance CLI TypeScript check passes.
- Local governance hook chain passes before commit.

## Review Gate

Completion review must state whether E2 is closed, partial, or failed, and
must include exact tests run.

## Closure Checklist / Completion Requirements

- [x] Operational benchmark schema added.
- [x] Evidence ingestion added.
- [x] Evidence-mode breakdown added.
- [x] CLI command path added.
- [x] Tests updated.
- [x] Completion review filed.
- [x] Commit created for E2 phase.

Completion review:

`docs/reviews/CVF_E2_OPERATIONAL_BENCHMARK_SUITE_COMPLETION_2026-05-22.md`

## Operator Checkpoint

operator.checkpoint.waiver: Operator already authorized Codex to proceed
through the six remaining phases in priority order and to use API keys when
needed; E2 does not require live key usage because it makes no new live
provider claim.

## Return-To-Orchestrator Conditions

Return to the operator if E2 requires new policy/risk guard semantics, live
provider benchmarking, output-quality scoring, route changes, receipt-envelope
changes, public-sync, hosted readiness, Maika proof, or freeze release.

## Claim Boundary

This work order closes only E2 operational benchmark suite foundation for the
current private baseline.
