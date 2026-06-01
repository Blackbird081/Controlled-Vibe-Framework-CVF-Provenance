# CVF Work Order - MKG7-T2 Memory Readout-Eligibility Lifecycle

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

docType: work_order

Date: 2026-06-01

## Purpose

Add a deterministic readout-eligibility lifecycle policy, orthogonal to the
existing tier-state machine, covering six eligibility states:
`READOUT_ALLOWED`, `READOUT_DENIED`, `STALE_NEEDS_REFRESH`, `REVOKED`,
`NO_AUTHORITY_SOURCE`, `OUT_OF_SCOPE_FOR_ACTOR`. Output is a new LPF policy
file with focused unit tests. The existing `memory-lifecycle-policy.ts` must
not be modified.

Success: new policy file exists, all 6 states covered by tests, `rawMemoryReleased=false`
and `canReinject=false` asserted on the readout surface, LPF TypeScript check
PASS, file-size guard PASS, both files left pending and uncommitted.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-01 dispatch MKG7 T2–T7 for worker execution | ACCEPT |
| MKG7-T2 GC-018 | `docs/baselines/CVF_GC018_MKG7_T2_MEMORY_READOUT_ELIGIBILITY_LIFECYCLE_2026-06-01.md` | ACCEPT |
| MKG7 roadmap | `docs/roadmaps/CVF_MKG7_MEMORY_PLANE_OPERATIONALIZATION_ROADMAP_2026-06-01.md` | ACCEPT |
| T1 contract | `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md` | ACCEPT |
| Worker autonomy standard | `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch and review pending output | no silent scope expansion |
| Worker | implement policy file + tests | no route changes, no tier-machine edits, no commit |
| Reviewer | verify 6 states covered, invariants asserted, existing tier machine unmodified | reject if tier machine edited |

## Scope

Allowed scope:

- create `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-readout-eligibility-policy.ts`;
- create `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-readout-eligibility-policy.test.ts`;
- optionally add export to `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime.ts` if within file-size limit;
- create `docs/reviews/CVF_MKG7_T2_MEMORY_READOUT_ELIGIBILITY_LIFECYCLE_COMPLETION_2026-06-01.md`;
- run listed gates and fix allowed-scope defects.

Forbidden scope:

- any edit to `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts`;
- any edit to `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts`;
- route changes of any kind;
- provider calls, live proof, prompt injection, persistence mutation;
- public-sync, push, or commit.

Risk ceiling: R1 — new policy helper only.

## Required First Reads

- `docs/baselines/CVF_GC018_MKG7_T2_MEMORY_READOUT_ELIGIBILITY_LIFECYCLE_2026-06-01.md`
- `docs/reference/CVF_MEMORY_PLANE_OPERATIONAL_CONTRACT_2026-06-01.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` — understand existing tier states; must not be modified

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/check_work_order_dispatch_quality.py --base 5e55714d --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 5e55714d --head HEAD
```

Expected: both gates PASS. If a gate fails inside Allowed scope, repair and
rerun. Do not ask the operator.

## 6A. Source-Fidelity Pass

### Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Existing tier states (must not be replicated) | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` | lines 4–11 | `MemoryLifecycleState` | tier lifecycle policy | ACCEPT |
| `evaluateLifecycleTransition` (must not be modified) | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` | line 49 | `evaluateLifecycleTransition` | tier policy | ACCEPT |
| `rawMemoryReleased=false` invariant on readout surface | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 202–203 | `rawMemoryReleased` | readout route | ACCEPT |
| `canReinject=false` on readout surface | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | lines 202–203 | `canReinject` | readout route | ACCEPT |

New doc-only fields:

| New doc-only field | Purpose | Not sourced from runtime? | Runtime claim blocked? | Validation expectation |
| --- | --- | --- | --- | --- |
| `MemoryReadoutEligibilityState` | readout-eligibility state enum | Yes | Yes | unit tests only |
| `evaluateReadoutEligibility` | deterministic eligibility function | Yes | Yes | unit tests only |

## 6B. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Add deterministic readout-eligibility decisions | Execution Plan step 2 | `memory-readout-eligibility-policy.ts` | LPF `npm run check` + focused tests | DISPATCHED |
| Distinct from tier-state machine | Scope / Forbidden | existing file untouched | `git diff --name-status` | DISPATCHED |
| `rawMemoryReleased=false` preserved | Source Verification Block | policy function output | focused test assertion | DISPATCHED |
| `canReinject=false` preserved | Source Verification Block | policy function output | focused test assertion | DISPATCHED |
| Focused tests covering all states | Execution Plan step 3 | test file | test run result | DISPATCHED |

## 6C. Worker Autonomy / No-Question Rule

Proceed autonomously with reading named files, creating owned source/test files,
running gates, and fixing allowed-scope defects. Ask only for scope expansion,
forbidden-path edits, live proof, secrets, push/publish, commit, or destructive
actions.

## 6D. Pending Artifact Evidence Finality

Do not commit. Record actual `git status --short` (pending lines). Do not cite
a committed-only or empty range as proof for pending files.

## 6G. Work-Order Fulfillment Manifest

### Required Artifact Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-readout-eligibility-policy.ts` | Yes | new eligibility policy |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-readout-eligibility-policy.test.ts` | Yes | focused tests |
| `docs/reviews/CVF_MKG7_T2_MEMORY_READOUT_ELIGIBILITY_LIFECYCLE_COMPLETION_2026-06-01.md` | Yes | pending completion review |

### Forbidden Path Manifest

| Path | Reason |
| --- | --- |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-lifecycle-policy.ts` | existing tier machine must not be modified |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts` | must not expand root barrel |

### Required Proof Manifest

| Proof | Path | Required literal | Required at handoff |
| --- | --- | --- | --- |
| All 6 eligibility states tested | test file | `READOUT_ALLOWED` | Yes |
| `rawMemoryReleased=false` asserted | test file | `rawMemoryReleased` | Yes |
| `canReinject=false` asserted | test file | `canReinject` | Yes |

## 7. Write Ownership

Owned files: `memory-readout-eligibility-policy.ts`, test file, optionally `memory-runtime.ts` export, completion review.
Forbidden: `memory-lifecycle-policy.ts`, `index.ts`, any route file.
Write mode: create-only for new files; additive export-only for `memory-runtime.ts`.

## 8. Execution Plan

1. Capture `baseHead` and actual git status. Run pre-flight gates.
2. Create `memory-readout-eligibility-policy.ts` with:
   - `MemoryReadoutEligibilityState` type covering all 6 states;
   - `MemoryReadoutEligibilityInput` interface (actor role, scope, lifecycle state, age, staleness flag, revocation flag);
   - `evaluateReadoutEligibility(input)` returning state + reason + `rawMemoryReleased:false` + `canReinject:false`;
   - deterministic branches for each state.
3. Create focused tests: one test per eligibility state, plus invariant assertions.
4. Run `npm run check` from LPF directory. Run `python governance/compat/check_governed_file_size.py --enforce`.
5. Create pending completion review with gate results, changed files, Public Export Disposition, Finding-To-Governance Learning Disposition, Claim Boundary.
6. Leave all files pending and uncommitted.

## Evidence Requirements

- `npm run check` from `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/` — PASS;
- `python governance/compat/check_governed_file_size.py --enforce` — PASS;
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 5e55714d --head HEAD` — PASS;
- actual `git status --short`;
- `git diff --name-status` confirming no edits to forbidden paths.

## 10. Acceptance Criteria

- [ ] `memory-readout-eligibility-policy.ts` exists with all 6 states
- [ ] Tests cover all 6 states and assert `rawMemoryReleased=false` + `canReinject=false`
- [ ] `memory-lifecycle-policy.ts` is unmodified (verify with `git diff`)
- [ ] LPF `npm run check` PASS
- [ ] File-size guard PASS
- [ ] Both new files left pending and uncommitted

Fail conditions:

- [ ] Any edit to `memory-lifecycle-policy.ts` or `index.ts`
- [ ] Missing eligibility state in implementation or tests
- [ ] Worker commits or asks whether to fix an allowed-scope gate failure

## 11. Review Gate

Pre-implementation autorun gate must pass before edits. Closure (by
orchestrator) requires reviewer no-blocking objection.

## 12. Closure Checklist

N/A: worker must not close or commit T2. Return pending files for orchestrator.

## 13. Return-To-Orchestrator Conditions

Return if: pre-flight fails outside Allowed scope; a required source symbol
cannot be verified; scope conflict found; forbidden path edit required.

## Operator Checkpoint

Operator requested all MKG7 T2–T7 work orders dispatched for worker execution.
T2 is dispatch-ready; documentation + new policy file only.

## Worker Dispatch Prompt

```text
You are assigned MKG7-T2 Memory Readout-Eligibility Lifecycle.

Primary work order:
docs/work_orders/CVF_WO_MKG7_T2_MEMORY_READOUT_ELIGIBILITY_LIFECYCLE_2026-06-01.md

Read the complete work order before coding. Implement only its Allowed scope.

Critical rules:
- create a NEW file memory-readout-eligibility-policy.ts with 6 eligibility
  states: READOUT_ALLOWED, READOUT_DENIED, STALE_NEEDS_REFRESH, REVOKED,
  NO_AUTHORITY_SOURCE, OUT_OF_SCOPE_FOR_ACTOR;
- do NOT modify memory-lifecycle-policy.ts — the tier machine is read-only;
- policy output must set rawMemoryReleased:false and canReinject:false;
- run LPF npm run check and file-size guard.

Worker Autonomy Rule: repair allowed-scope gate failures and rerun without asking.
Pending Artifact Rule: do not commit; record actual git status.
Stop and ask only for scope expansion, forbidden-path edits, live proof, secrets,
push/publish, commit, or destructive actions.
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

T2 authorizes a new readout-eligibility policy helper and tests only. No route
changes, provider calls, prompt injection, persistence mutation, tier-machine
modification, public-sync, or push.
