# CVF H2 Runtime Memory Hierarchy Phase 2 Completion

Memory class: FULL_RECORD

Status: CLOSED_H2_RUNTIME_MEMORY_HIERARCHY_PHASE2

Date: 2026-05-22

## Purpose

Close H2 from the post-B/C Review-CVF remaining pain-point roadmap by extending
CVF beyond the T5 task-memory slice into a canonical runtime memory hierarchy
map and one additional ephemeral runtime proof tier.

## Scope / Target / Owner Boundary

Target: `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION`.

Owner: Codex, acting as implementer, reviewer, and evidence owner under the
operator authorization to process the remaining Review-CVF pain-point phases in
priority order.

Boundary: H2 adds no route behavior, provider behavior, receipt-envelope field,
durable persistence, cross-session memory, automatic reinjection, public-sync,
hosted readiness, Maika proof, or freeze release.

## Target / Source

Target artifact:

- H2 runtime memory hierarchy phase 2.

Source artifacts:

- `.private_reference/legacy/CVF 17.05/Review CVF.md`
- `docs/reviews/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`
- `docs/roadmaps/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINT_ROADMAP_2026-05-22.md`
- `docs/baselines/CVF_GC018_H2_RUNTIME_MEMORY_HIERARCHY_PHASE2_2026-05-22.md`
- `docs/work_orders/CVF_WO_H2_RUNTIME_MEMORY_HIERARCHY_PHASE2_2026-05-22.md`

## Scope / Methodology

Methodology:

- reuse the existing seven-tier `MemoryTier` classifier;
- add a runtime map rather than a new tier vocabulary;
- make tier access actor-aware using existing G1-style role names;
- separate write/retrieve from injection/reinjection;
- deny injection and reinjection deterministically in H2;
- prove one additional runtime tier, `working`, as ephemeral in-process
  same-execution memory.

## Authority Chain

- Original source oracle: `.private_reference/legacy/CVF 17.05/Review CVF.md`
- Assessment:
  `docs/reviews/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINTS_ASSESSMENT_2026-05-22.md`
- Roadmap:
  `docs/roadmaps/CVF_REVIEW_CVF_POST_BC_REMAINING_PAIN_POINT_ROADMAP_2026-05-22.md`
- GC-018:
  `docs/baselines/CVF_GC018_H2_RUNTIME_MEMORY_HIERARCHY_PHASE2_2026-05-22.md`
- Work order:
  `docs/work_orders/CVF_WO_H2_RUNTIME_MEMORY_HIERARCHY_PHASE2_2026-05-22.md`

## Delivered

- Added `runtime-memory-hierarchy.ts`.
- Added `cvf.runtimeMemoryHierarchy.v1`.
- Added seven-tier runtime rules for `working`, `task`, `skill`,
  `organizational`, `long-term`, `audit`, and `receipt`.
- Added `evaluateRuntimeMemoryAction()` for `write`, `retrieve`, `inject`, and
  `reinject`.
- Added durable-persistence, cross-session, restricted-memory, contamination,
  actor, injection, and reinjection denial reasons.
- Added `createWorkingMemoryRuntimeStore()` as the bounded H2 proof tier.
- Exported the H2 contract from the Learning Plane package index.
- Added focused H2 tests.

## Findings / Position

Finding 1: the Review-CVF H pain point remained partially valid before H2
because T5 proved only task memory. H2 now supplies the missing canonical
runtime policy map for all frozen memory tiers.

Finding 2: H2 intentionally does not turn skill, organizational, long-term,
audit, or receipt memory into new runtime stores. Those tiers now have
deterministic rules and denial boundaries, not hidden persistence.

Finding 3: `canReinject=false` remains invariant. The evaluator rejects both
`inject` and `reinject` actions unless a future separate reinjection tranche is
explicitly authorized.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| H2 accidentally creates a new memory tier | Runtime map reuses existing seven-tier classifier |
| Working memory is mistaken for durable memory | Store is in-process only and reports `persistentStoreCreated=false` |
| Prompt reinjection slips in through "injection" wording | `inject` and `reinject` are explicit denied actions |
| Organizational or long-term memory is overclaimed | Both remain `policy_map_only` and action-denied |
| Actor identity is ignored | Evaluator requires actor role and denies unauthorized actors |

## Evidence Trace Block

Files changed:

```text
EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts
EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts
EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/runtime-memory-hierarchy.test.ts
```

Focused verification:

```text
npm run test -- tests/runtime-memory-hierarchy.test.ts
-> PASS, 1 file / 11 tests

npm run check
-> PASS

npm test
-> PASS, 50 files / 1532 tests

python governance/compat/run_local_governance_hook_chain.py
-> PASS, 43/43 checks
```

## Acceptance Criteria Result

| Criterion | Result |
| --- | --- |
| Tier access is actor-aware | PASS |
| No durable persistence introduced | PASS |
| No cross-session reinjection introduced | PASS |
| Rejected actions have deterministic reasons | PASS |
| `canReinject=false` preserved | PASS |
| Existing seven-tier model unchanged | PASS |

## Decision / Recommendation / Disposition

Disposition: `CLOSED_H2_RUNTIME_MEMORY_HIERARCHY_PHASE2`.

Recommendation: continue the post-B/C remaining pain-point roadmap with F2
noncoder outcome UX hardening next.

## Public Catalog Disposition

Public catalog update: `N/A`.

Reason: H2 is a private provenance Learning Plane runtime policy/proof tranche.
It adds no public-facing setup claim, public hosted-readiness claim, or public
memory persistence claim.

## Claim Boundary

H2 is closed for runtime memory hierarchy phase 2 only. It does not claim
durable memory, organizational memory, long-term memory, database readiness,
external memory, provider-side memory, cross-session continuity, automatic
reinjection, route behavior, public-sync, hosted readiness, Maika proof, or
freeze release.

Live provider proof was not required or run for this phase because the closed
claim is deterministic memory policy and in-process working-memory behavior,
not new live governance behavior.
