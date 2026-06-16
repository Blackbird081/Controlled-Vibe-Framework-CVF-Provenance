# CVF Agent Work Order - Roadmap State Reconciliation T2 Stale Roadmap Redispatch Guard For Claude

Memory class: FULL_RECORD

Status: DISPATCHED_TO_WORKER

docType: work_order

Date: 2026-06-16

Owner / Orchestrator: Codex

Implementer: Claude

Reviewer / closer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: e31ac133

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: NOT_EXECUTED_YET

riskCeiling: R1_GOVERNANCE_CHECKER_ONLY

rawMemoryReleased: false

completionReviewPath:
`docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T2_STALE_ROADMAP_REDISPATCH_GUARD_COMPLETION_2026-06-16.md`

workerReturnPath:
`docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T2_STALE_ROADMAP_REDISPATCH_GUARD_WORKER_RETURN_2026-06-16.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T2_STALE_ROADMAP_REDISPATCH_GUARD_COMPLETION_2026-06-16.md`

## Purpose

Implement the RSF-T2 stale-roadmap redispatch guard. The guard should prevent a
ready/dispatch work order from passing dispatch-quality when it references a
roadmap/tranche that already has a matching closed completion artifact.

This is a governance foundation improvement. It is not runtime/product work.

## 1. Mission

Extend `governance/compat/check_work_order_dispatch_quality.py` with a narrow
dispatch-time validation and add focused tests in
`governance/compat/test_check_work_order_dispatch_quality.py`.

The validation must use explicit roadmap/work-order references and bounded
filename matching under `docs/reviews/`. Do not perform a broad full-text
repository scan.

## 2. Authority Chain

- Operator: asked Codex to continue after RSF-T1 closure on 2026-06-16.
- Roadmap:
  `docs/roadmaps/CVF_ROADMAP_STATE_RECONCILIATION_AND_NEXT_MOVE_FRESHNESS_ROADMAP_2026-06-16.md`.
- GC-018:
  `docs/baselines/CVF_GC018_ROADMAP_STATE_RECONCILIATION_T2_STALE_ROADMAP_REDISPATCH_GUARD_2026-06-16.md`.
- RSF-T1 completion:
  `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T1_CI2_COMPLETION_2026-06-16.md`.
- Active state registry: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`.

## 3. Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Orchestrator | Codex | source audit, dispatch, reviewer closure |
| Worker | Claude | checker/test implementation, no commit |
| Reviewer / closer | Codex | inspect diff, run gates, commit |
| Operator | Human | scope expansion, runtime, live/provider, public-sync |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake summary | RSF-T1 proved stale roadmap state can survive after a closed review exists and mislead next work selection |
| Scope classification | R1 governance checker only |
| Risk sensitivity | Governance guard source/test only; no runtime/provider/secret/public-sync |
| Selected route mode | MULTI_AGENT_MULTI_ROLE |
| Selected role route | Codex orchestrates/reviews/commits; Claude implements no-commit worker return |
| routeMode | MULTI_AGENT_MULTI_ROLE |
| Role separation basis | Codex authored source-verified packet; Claude implements checker and tests; Codex reviews and commits |
| Escalation condition | Stop for runtime changes, broad full-text scan, broad legacy scan, provider/live work, public-sync, or claim expansion |

## 4. Required First Reads

| File | Required use |
|---|---|
| `CVF_SESSION_MEMORY.md` | startup front door only |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | active handoff and current mode |
| `AGENT_HANDOFF_V19_2026-06-15.md` | current continuity only |
| `docs/roadmaps/CVF_ROADMAP_STATE_RECONCILIATION_AND_NEXT_MOVE_FRESHNESS_ROADMAP_2026-06-16.md` | governing roadmap |
| `docs/baselines/CVF_GC018_ROADMAP_STATE_RECONCILIATION_T2_STALE_ROADMAP_REDISPATCH_GUARD_2026-06-16.md` | authorized scope |
| `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T1_CI2_COMPLETION_2026-06-16.md` | dependency release evidence |
| `governance/compat/check_work_order_dispatch_quality.py` | implementation target |
| `governance/compat/test_check_work_order_dispatch_quality.py` | focused tests |

## 5. Allowed Scope

Claude may modify or create only:

| Path | Action |
|---|---|
| `governance/compat/check_work_order_dispatch_quality.py` | add bounded stale-roadmap redispatch validation |
| `governance/compat/test_check_work_order_dispatch_quality.py` | add focused tests for fail/pass behavior |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ROADMAP_STATE_RECONCILIATION_T2_STALE_ROADMAP_REDISPATCH_GUARD_FOR_CLAUDE_2026-06-16.md` | update worker-return status/evidence only |
| `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T2_STALE_ROADMAP_REDISPATCH_GUARD_WORKER_RETURN_2026-06-16.md` | create worker-return packet |

Codex may later create the reviewer-owned completion review and commit if the
worker return is accepted.

## 6. Forbidden Scope And Stop Conditions

Stop before:

- touching runtime/product source outside the checker/test pair above;
- touching Model Gateway, LPCI product, provider adapters, UI, or public-sync;
- reading credentials, `.env` files, or running live/provider/network calls;
- scanning `.private_reference/legacy/`;
- implementing a broad full-text repository scan;
- claiming all stale roadmap states are solved;
- changing session state or active handoff as worker;
- committing.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| RSF-T1 completion closed | `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T1_CI2_COMPLETION_2026-06-16.md` | line 5 | `Status` | RSF-T1 completion review | ACCEPT |
| RSF-T1 authorizes RSF-T2 corrective action | `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T1_CI2_COMPLETION_2026-06-16.md` | lines 84-85 | `RSF-T2` | RSF-T1 corrective action | ACCEPT |
| Roadmap authorizes RSF-T2 | `docs/roadmaps/CVF_ROADMAP_STATE_RECONCILIATION_AND_NEXT_MOVE_FRESHNESS_ROADMAP_2026-06-16.md` | line 101 | `RSF-T2` | RSF roadmap tranche table | ACCEPT |
| Work-order dispatch validation owner exists | `governance/compat/check_work_order_dispatch_quality.py` | lines 2162-2228 | `_validate_work_order` | dispatch-quality checker | ACCEPT |
| Roadmap-derived detection exists | `governance/compat/check_work_order_dispatch_quality.py` | lines 734-735 | `_is_roadmap_derived` | dispatch-quality checker | ACCEPT |
| Dependency-release evidence is required before dispatch | `docs/reference/CVF_WORK_ORDER_DEPENDENCY_RELEASE_EVIDENCE_STANDARD_2026-06-03.md` | lines 51-62 | `Required evidence` | dependency-release standard | ACCEPT |
| Machine closure package roadmap-state row exists | `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` | lines 287-292 | `Roadmap state` | closure-quality standard | ACCEPT |
| Dispatch-quality focused tests exist | `governance/compat/test_check_work_order_dispatch_quality.py` | lines 2369-2415 | `test_closed_work_order_with_open_rows_and_unchecked_boxes_fails`; `test_closed_roadmap_with_hold_residue_fails` | dispatch-quality test suite | ACCEPT |

## Source-Fidelity Pass

Existing source facts were recomputed from the current workspace at
`dispatchBaseHead: e31ac133`.

No provider-specific memory file is source authority. Do not cite `CLAUDE.md`,
Codex memory, IDE summaries, or chat text as canonical evidence.

## Current Runtime Freshness Verification

This work order claims no runtime behavior, provider call, credential use,
public-sync, legacy absorption, or product-readiness result. It changes only a
governance checker and its tests.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: RSF-T2 implements a governance checker derived from
RSF-T1 governed closure evidence. It does not absorb, reopen, or scan legacy
material and does not modify a legacy-adjacent capability surface.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: Worker must recompute current dispatch-quality source and
tests before implementation.

unicodePathHandling: literal paths only; no Unicode-path corpus evidence is
used.

extractedTextAuthority: SOURCE_AUTHORITY

Text encoding: all authored prose and source comments must use ASCII only.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order section | Output artifact | Verification | Status |
|---|---|---|---|---|
| Implement dispatch freshness guard | Sections 5 and 7 | `check_work_order_dispatch_quality.py` | focused tests and dispatch-quality gate | PASS |
| Avoid broad repository scan | Sections 1, 6, and 7 | implementation diff | reviewer source inspection | PASS |
| Add stale and non-stale tests | Sections 7 and Acceptance Criteria | `test_check_work_order_dispatch_quality.py` | focused pytest | PASS |
| Keep runtime/provider/public/legacy out of scope | Sections 6 and Claim Boundary | changed-file set | `git diff --name-status` | PASS |
| Preserve reviewer-owned closure | Reviewer Closure Conversion | completion review by Codex only | reviewer gate | PASS |

## Worker Autonomy / No-Question Rule

Claude may repair gate failures inside Allowed Scope without asking the
operator. Stop only for forbidden scope, claim expansion, runtime/provider/live
work, public-sync, credential use, broad legacy scan, broad full-text scan, or
changes outside Allowed Scope.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: this work order authorizes a narrow change
to dispatch-quality governance checker source and its focused tests.

Authorized paths:

- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`

The implementation must preserve existing checker behavior except for adding
the stale-roadmap redispatch failure mode and its control fixture.

## Reviewer Closure Conversion

Because `Commit mode: WORKER_MUST_NOT_COMMIT`, Claude returns uncommitted
artifacts only. Codex owns the final completion review, committed-range gates,
material commit, and any session-sync decision.

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T2_STALE_ROADMAP_REDISPATCH_GUARD_COMPLETION_2026-06-16.md`

Claude must not set a closed status, must not commit, and must not author
session-continuity files.

## Write Ownership

| Surface | Owner |
|---|---|
| Dispatch-quality checker implementation | Claude worker |
| Focused tests | Claude worker |
| Worker-return packet | Claude worker |
| Final completion review | Codex reviewer |
| Commit and session sync | Codex reviewer |

## 7. Implementation Instructions

1. Capture `executionBaseHead` with `git rev-parse --short HEAD`.
2. Read the required first reads.
3. Inspect current dispatch-quality helpers before editing.
4. Implement a bounded stale-roadmap redispatch validation.
5. The validation should trigger only for ready/dispatch work orders that are
   roadmap-derived and can be associated with a target tranche or work item.
6. Look for matching completion artifacts under `docs/reviews/` by bounded
   filename or explicit path references. A matching artifact must have
   `Status: CLOSED_PASS_BOUNDED` before the guard blocks dispatch.
7. Do not perform broad full-text scans across the repository.
8. Add tests:
   - stale roadmap-derived dispatch with matching closed completion fails;
   - non-stale roadmap-derived dispatch passes;
   - existing dispatch-quality behavior remains intact.
9. Update this work order to `COMPLETE_PENDING_REVIEW` only after the worker
   return gates pass.
10. Author the worker-return packet named in `workerReturnPath`.

## Required Proof Manifest Atomic Literal Discipline

Work-Order Fulfillment Manifest:

| Required output | Literal path | Owner | Disposition |
|---|---|---|---|
| Checker implementation | `governance/compat/check_work_order_dispatch_quality.py` | Claude worker | ASSIGNED |
| Focused tests | `governance/compat/test_check_work_order_dispatch_quality.py` | Claude worker | ASSIGNED |
| Worker return | `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T2_STALE_ROADMAP_REDISPATCH_GUARD_WORKER_RETURN_2026-06-16.md` | Claude worker | ASSIGNED |
| Completion review | `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T2_STALE_ROADMAP_REDISPATCH_GUARD_COMPLETION_2026-06-16.md` | Codex reviewer | REVIEWER_OWNED |

Required proof commands:

- `python -m pytest governance/compat/test_check_work_order_dispatch_quality.py`
- `python governance/compat/check_work_order_dispatch_quality.py --base e31ac133 --head HEAD --enforce`
- `python governance/compat/run_worker_return_fast_gate.py`
- `git diff --check`

Required changed paths are exactly the Allowed Scope paths plus the worker
return packet. If implementation requires any other path, stop and return to
Codex with `BLOCKED_SCOPE_EXPANSION_REQUIRED`.

## Execution Plan

| Step | Action | Owner |
|---|---|---|
| 1 | Capture execution base and read required files | Claude |
| 2 | Patch checker with bounded validation | Claude |
| 3 | Add focused tests | Claude |
| 4 | Run focused tests and worker-return gates | Claude |
| 5 | Return uncommitted artifacts | Claude |
| 6 | Review, author completion, and commit if accepted | Codex |

## Evidence Requirements

Required worker evidence:

- `git diff --name-status`;
- focused pytest output for
  `governance/compat/test_check_work_order_dispatch_quality.py`;
- dispatch-quality gate output for the changed range;
- worker-return fast gate output;
- `git diff --check`;
- explicit reviewer-readable note proving the implementation uses bounded
  path/filename matching and not a broad full-text repository scan.

## Acceptance Criteria

| ID | Criterion |
|---|---|
| T2-AC1 | Matching closed completion artifact blocks stale roadmap-derived ready/dispatch work order. |
| T2-AC2 | Non-stale roadmap-derived dispatch still passes. |
| T2-AC3 | No broad full-text repository scan is introduced. |
| T2-AC4 | Focused dispatch-quality tests pass. |
| T2-AC5 | Worker-return fast gate and diff hygiene pass. |

## Review Gate

Codex must inspect the real diff, verify the bounded scan shape, run focused
tests and pre-closure gates, and author the reviewer-owned completion review
before any commit.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when all Allowed Scope edits are on disk,
uncommitted, and gates have passed. Return `BLOCKED` only if the guard requires
Forbidden Scope or a broader repository scan.

## Operator Checkpoint

No checkpoint is required for actions inside Allowed Scope. Return to operator
only for runtime changes, provider/live work, public-sync, broad legacy scan,
broad repository scan, or widening the claim boundary.

## Pre-Flight Checks

| Check | Command | Expected |
|---|---|---|
| Active session state | `python governance/compat/check_active_session_state.py --enforce` | PASS |
| Mode consistency | `python governance/compat/check_session_mode_consistency.py --enforce` | PASS |
| Pre-implementation gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base e31ac133 --head HEAD` | PASS |

## Completion Gates

| Gate | Command | Expected |
|---|---|---|
| Focused tests | `python -m pytest governance/compat/test_check_work_order_dispatch_quality.py` | PASS |
| Dispatch-quality gate | `python governance/compat/check_work_order_dispatch_quality.py --base e31ac133 --head HEAD --enforce` | PASS |
| Worker return fast gate | `python governance/compat/run_worker_return_fast_gate.py` | PASS |
| Diff hygiene | `git diff --check` | PASS |
| Worker return | no command | `COMPLETE_PENDING_REVIEW`, no commit |

## Closure Checklist

| Item | Required state |
|---|---|
| Work order | `COMPLETE_PENDING_REVIEW` after Claude return |
| Checker implementation | bounded stale-roadmap redispatch validation implemented |
| Focused tests | stale negative and non-stale control tests present |
| Worker-return packet | present and source-backed |
| Completion review | reviewer-owned, created by Codex |
| Commit | Codex only |

## Claim Boundary

Allowed claim after successful worker return:

CVF dispatch-quality now has a bounded stale-roadmap redispatch guard for the
implemented pattern.

Forbidden claims:

- all stale roadmap states are solved;
- runtime behavior changed;
- provider routing or live governance behavior changed;
- public readiness, production readiness, or provider readiness;
- legacy content was absorbed;
- LPCI or Model Gateway work continues.

## Dispatch Prompt Envelope

Worker prompt:

```text
You are Claude acting as WORKER for CVF RSF-T2 Stale Roadmap Redispatch Guard.
Read the work order, GC-018, roadmap, and RSF-T1 completion named in the
authority chain. Capture executionBaseHead first. Your scope is a bounded
governance checker/test implementation only: extend dispatch-quality so a
roadmap-derived ready/dispatch packet is blocked when a matching closed
completion artifact already exists, add focused tests, run the listed gates,
and return COMPLETE_PENDING_REVIEW without committing. Do not touch runtime,
provider, credentials, public-sync, broad legacy scan, broad repository scan,
Model Gateway, or LPCI product files.
```

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `ORCHESTRATOR_PACKET_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `MACHINE_CHECK_ADDED_BY_WORKER_IF_SUCCESSFUL` |
| Next control action | Add stale-roadmap redispatch validation to dispatch-quality |
| Worker blame | `N/A_WITH_REASON`: RSF-T1 established this as a control-plane freshness gap |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex orchestrator/author |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 RSF-T2 dispatch packet |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | source reads, apply_patch, governance gates |
| Target paths | RSF roadmap, RSF-T2 GC-018, RSF-T2 work order |
| Allowed scope source | operator continuation request and RSF-T1 closure |
| Before status evidence | RSF-T1 closed at `1c3724d0`; session sync `e31ac133` |
| After status evidence | RSF-T2 work order dispatched to Claude worker |
| Diff evidence | dispatch batch from `e31ac133..HEAD` |
| Approval boundary | dispatch packet authoring only; worker implementation not in this commit |
| Claim boundary | no runtime/provider/public/live/legacy broad scan claim |
| Agent type | Codex orchestrator; Claude worker target |
| Invocation ID | `rsf-t2-stale-roadmap-redispatch-guard-work-order-2026-06-16` |
| Expected manifest | `docs/roadmaps/CVF_ROADMAP_STATE_RECONCILIATION_AND_NEXT_MOVE_FRESHNESS_ROADMAP_2026-06-16.md`; `docs/baselines/CVF_GC018_ROADMAP_STATE_RECONCILIATION_T2_STALE_ROADMAP_REDISPATCH_GUARD_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ROADMAP_STATE_RECONCILIATION_T2_STALE_ROADMAP_REDISPATCH_GUARD_FOR_CLAUDE_2026-06-16.md` |
| Actual changed set | `docs/roadmaps/CVF_ROADMAP_STATE_RECONCILIATION_AND_NEXT_MOVE_FRESHNESS_ROADMAP_2026-06-16.md`; `docs/baselines/CVF_GC018_ROADMAP_STATE_RECONCILIATION_T2_STALE_ROADMAP_REDISPATCH_GUARD_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ROADMAP_STATE_RECONCILIATION_T2_STALE_ROADMAP_REDISPATCH_GUARD_FOR_CLAUDE_2026-06-16.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
| Trace boundary | Dispatch packet authoring only; worker execution will update this work order and create the worker-return packet |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance work order. No public-sync batch is
authorized.
