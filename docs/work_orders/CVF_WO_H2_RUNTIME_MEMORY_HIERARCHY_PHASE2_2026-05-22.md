# CVF Work Order H2 Runtime Memory Hierarchy Phase 2

Memory class: FULL_RECORD

Status: CLOSED_H2_RUNTIME_MEMORY_HIERARCHY_PHASE2

Date: 2026-05-22

## Purpose

Implement the H2 runtime memory hierarchy phase 2 authorized by GC-018.

## Authority Chain

- Original source oracle: `.private_reference/legacy/CVF 17.05/Review CVF.md`
- Post-B/C assessment:
  `docs/reviews/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`
- Roadmap:
  `docs/roadmaps/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINT_ROADMAP_2026-05-22.md`
- G1 completion:
  `docs/reviews/CVF_G1_EXECUTION_IDENTITY_RUNTIME_GATE_COMPLETION_2026-05-22.md`
- E2 completion:
  `docs/reviews/CVF_E2_OPERATIONAL_BENCHMARK_SUITE_COMPLETION_2026-05-22.md`
- GC-018:
  `docs/baselines/CVF_GC018_H2_RUNTIME_MEMORY_HIERARCHY_PHASE2_2026-05-22.md`

## Agent Roles

- Orchestrator: Codex
- Implementer: Codex
- Reviewer: Codex, via tests and completion review
- Auditor: Codex, via completion packet and governance hooks

## Scope / Allowed Scope / Forbidden Scope

Allowed:

- add a Learning Plane runtime memory hierarchy module;
- map the existing seven memory tiers without adding tier IDs;
- add actor-aware deterministic action evaluation;
- add an ephemeral same-execution working-memory proof store;
- add tests and completion documentation.

Forbidden:

- durable persistence, database, external memory service, file-backed store, or
  archive memory;
- cross-session continuity or automatic reinjection;
- provider prompt memory injection;
- new role taxonomy, policy/risk guard semantics, route behavior, or receipt
  envelope field;
- public-sync, hosted readiness, Maika proof, or freeze release.

## Required First Reads

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-tier-classifier.contract.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/task-memory/task-memory-store.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled.memory.gateway.contract.ts`
- `docs/reviews/CVF_T5_RUNTIME_MEMORY_WIRING_COMPLETION_2026-05-22.md`

## Pre-Flight Checks

- Confirm no new memory tier is introduced.
- Confirm H2 proof tier is `working`, not durable or organizational memory.
- Confirm `canReinject=false` remains invariant.
- Confirm injection and reinjection actions fail deterministically.

## Write Ownership

Primary write scope:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/`
- completion documentation and session state

## Execution Plan / Execution Rules

1. Add runtime memory hierarchy contract.
2. Add tier rules for working, task, skill, organizational, long-term, audit,
   and receipt memory.
3. Add deterministic action evaluator.
4. Add ephemeral working-memory runtime proof store.
5. Add focused tests for allow/deny/privacy/contamination/reinjection
   boundaries.
6. Verify Learning Plane targeted tests, full tests, and TypeScript check.
7. File completion review and commit H2.

## Acceptance Criteria

- Tier access is actor-aware.
- No durable persistence is introduced.
- No cross-session reinjection is introduced.
- Rejected memory actions produce deterministic reasons.
- `canReinject=false` is preserved.
- The seven-tier model remains unchanged.

## Evidence Requirements

- Targeted H2 tests pass.
- Full Learning Plane tests pass.
- Learning Plane TypeScript check passes.
- Local governance hook chain passes before commit.

## Review Gate

Completion review must state whether H2 is closed, partial, or failed, and
must include exact tests run.

## Closure Checklist / Completion Requirements

- [x] Runtime memory hierarchy map added.
- [x] Actor-aware action evaluator added.
- [x] Ephemeral working-memory proof added.
- [x] Injection and reinjection denial tested.
- [x] Durable and cross-session denials tested.
- [x] Completion review filed.
- [x] Commit created for H2 phase.

Completion review:

`docs/reviews/CVF_H2_RUNTIME_MEMORY_HIERARCHY_PHASE2_COMPLETION_2026-05-22.md`

## Operator Checkpoint

operator.checkpoint.waiver: Operator authorized Codex to proceed through the
six remaining phases in priority order and to use API keys when needed. H2 does
not need live API key usage because it makes no new live provider claim.

## Return-To-Orchestrator Conditions

Return to the operator if H2 requires durable persistence, cross-session
memory, provider prompt reinjection, route changes, receipt-envelope changes,
new role taxonomy, public-sync, hosted readiness, Maika proof, or freeze
release.

## Claim Boundary

This work order closes only H2 runtime memory hierarchy phase 2 for the current
private baseline.
