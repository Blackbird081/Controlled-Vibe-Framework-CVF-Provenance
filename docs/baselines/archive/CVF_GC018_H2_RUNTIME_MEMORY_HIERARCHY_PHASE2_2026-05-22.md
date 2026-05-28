# CVF GC-018 H2 Runtime Memory Hierarchy Phase 2

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_H2_RUNTIME_MEMORY_HIERARCHY_PHASE2

Date: 2026-05-22

## Source or Predecessor Evidence

- `.private_reference/legacy/CVF 17.05/Review CVF.md`
- `docs/reviews/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`
- `docs/roadmaps/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINT_ROADMAP_2026-05-22.md`
- `docs/reviews/CVF_G1_EXECUTION_IDENTITY_RUNTIME_GATE_COMPLETION_2026-05-22.md`
- `docs/reviews/CVF_E2_OPERATIONAL_BENCHMARK_SUITE_COMPLETION_2026-05-22.md`
- `docs/reviews/CVF_T5_RUNTIME_MEMORY_WIRING_COMPLETION_2026-05-22.md`

## Purpose / Decision / Baseline

Authorize H2, the bounded runtime memory hierarchy phase after G1 actor identity
and E2 operational benchmarking.

Decision: proceed with a runtime memory hierarchy policy/evaluator over the
existing seven-tier memory model, plus one additional runtime proof tier:
ephemeral same-execution `working` memory.

## Decision / Baseline / Proposed Tranche

Baseline:

- H1/T5 established classifier and task-memory runtime wiring.
- T5 proved only an ephemeral in-process task-memory store and audit readout.
- CDH-H preserved the audit-memory `canReinject=false` boundary.

Gap: Review CVF.md still expects a canonical memory hierarchy with injection,
retrieval, privacy, and contamination-boundary rules. Before H2, CVF had a task
slice, not a runtime map spanning working, task, skill, organizational,
long-term, audit, and receipt memory.

Proposed tranche:

- add `cvf.runtimeMemoryHierarchy.v1`;
- define actor-aware action policy for the existing seven tiers;
- prove the `working` tier with an ephemeral in-process runtime store;
- deny memory injection and reinjection deterministically;
- preserve `canReinject=false`, no durable persistence, and no new memory tier.

## Scope / Proposed Tranche

In scope:

- memory hierarchy runtime map for the frozen seven tiers:
  `working`, `task`, `skill`, `organizational`, `long-term`, `audit`,
  and `receipt`;
- deterministic evaluator for `write`, `retrieve`, `inject`, and `reinject`;
- actor-aware access rules using existing G1-style role names only;
- privacy and contamination-boundary checks;
- an ephemeral same-execution `working` memory store as the one H2 runtime
  proof tier;
- tests for allowed, denied, restricted, contaminated, durable-persistence,
  cross-session, injection, and reinjection paths.

Out of scope:

- new memory tier names;
- durable persistence, database, file-backed store, external memory service, or
  archive memory;
- cross-session memory continuity or automatic reinjection;
- route changes, provider changes, receipt-envelope changes, policy/risk guard
  changes, public-sync, hosted readiness, Maika proof, or freeze release.

## Blocked-Work Override

Blocked-work override: `new_memory_tiers_beyond_lane_h_scope` is granted only
for the bounded H2 runtime mapping and ephemeral `working` tier proof.

The override does not permit durable memory, organizational memory runtime,
long-term memory runtime, new tier IDs, provider prompt reinjection, or
cross-session memory continuity.

## Evidence / Required Evidence / Verification

Required evidence:

- focused H2 runtime-memory tests pass;
- Learning Plane TypeScript check passes;
- Learning Plane full test suite passes;
- local governance hook chain passes before final commit.

Live provider proof:

- Not required because H2 does not assert new live governance behavior,
  provider routing, or AI-output control. It is a deterministic memory policy
  and in-process working-memory proof.

## Claim Boundary / Approval Gate

H2 closes only runtime memory hierarchy phase 2 for the current private
baseline: a canonical seven-tier policy map, deterministic action evaluator,
and ephemeral working-memory proof. It does not claim durable memory,
organizational memory, long-term memory, cross-session continuity, automatic
reinjection, or provider-side memory behavior.
