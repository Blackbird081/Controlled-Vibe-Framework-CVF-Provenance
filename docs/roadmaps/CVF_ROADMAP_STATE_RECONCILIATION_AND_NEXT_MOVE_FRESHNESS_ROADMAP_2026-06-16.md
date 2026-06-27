# CVF Roadmap State Reconciliation And Next-Move Freshness Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-16

rawMemoryReleased: false

Roadmap class: governance-foundation-roadmap-state-freshness

## Purpose

Prevent agents from dispatching duplicate or stale work from an older roadmap
row when newer closure artifacts already prove that the tranche or downstream
tranches have closed.

This roadmap was opened after a live orchestration defect was found: the CI2
roadmap still advertises CI2-T3 as executable, while CI2-T3, CI2-T4, and CI2-T5
completion reviews already exist with closed bounded status. The right response
is not to reopen CI2-T3. The right response is to reconcile the roadmap state
and promote the defect into a reusable dispatch freshness guard.

## Authorization / Decision

Decision: RSF-T1 is closed bounded at material commit `1c3724d0`; RSF-T2 is
implemented and closed bounded in the reviewer material batch. RSF-T3 is closed
bounded after Claude verified that the stale Model Gateway C-02 P2 next-move
contradiction existed at dispatch-selection time and was pointer-remediated
before worker execution.

No runtime, live-provider, credential, public-sync, Model Gateway, LPCI product,
or broad legacy absorption work is authorized by this roadmap.

## Scope

In scope:

- CI2 roadmap state reconciliation using existing completion artifacts;
- next-move freshness evidence before creating any new CI2/LPCI follow-up
  dispatch;
- a bounded standard/checker design note for stale-roadmap redispatch;
- a first Claude work order for the documentation reconciliation tranche.

Out of scope:

- Model Gateway implementation;
- LPCI runtime or product implementation;
- broad legacy rescan;
- provider calls, live proof, credentials, or public-sync;
- changing current runtime behavior;
- claiming that all roadmap stale states are solved.

## Non-Goals

- Do not reopen CI2-T3, CI2-T4, or CI2-T5 as implementation work.
- Do not use this roadmap to select LPCI product work.
- Do not scan legacy material.
- Do not change runtime code or tests.
- Do not claim all roadmap stale states are solved by RSF-T2.

## Source-Backed Trigger Evidence

| Evidence item | Source | Current fact | Disposition |
|---|---|---|---|
| CI2 roadmap status | `docs/roadmaps/CVF_CI2_CORPUS_INTELLIGENCE_ENFORCEMENT_PRODUCT_READINESS_ROADMAP_2026-06-02.md` line 5 | top status still says T3 is executable | STALE_STATE_FOUND |
| CI2-T3 row | same roadmap line 79 | CI2-T3 row still says executable | STALE_STATE_FOUND |
| CI2-T4 row | same roadmap line 80 | CI2-T4 row still says blocked on T3 | STALE_STATE_FOUND |
| CI2-T5 row | same roadmap line 81 | CI2-T5 row still says blocked on T4 | STALE_STATE_FOUND |
| CI2-T3 completion | `docs/reviews/CVF_CI2_T3_ENFORCED_CROSS_CORPUS_INDEX_MODEL_COMPLETION_2026-06-02.md` line 5 | closed bounded status exists | CLOSURE_EXISTS |
| CI2-T4 completion | `docs/reviews/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK_COMPLETION_2026-06-02.md` line 5 | closed bounded status exists | CLOSURE_EXISTS |
| CI2-T5 completion | `docs/reviews/CVF_CI2_T5_LPCI_PRODUCT_ROADMAP_PACKET_COMPLETION_2026-06-02.md` line 5 | closed bounded status exists | CLOSURE_EXISTS |
| Closure-quality standard | `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md` line 291 | roadmap state must record tranche final state and next dependency state | RULE_EXISTS |
| Dependency-release standard | `docs/reference/CVF_WORK_ORDER_DEPENDENCY_RELEASE_EVIDENCE_STANDARD_2026-06-03.md` lines 51-62 | ready/dispatch needs refreshed prerequisite evidence and base anchors | RULE_EXISTS |

## Design Rule

Before a new roadmap-derived work order is dispatched, the orchestrator must
check whether the target roadmap/tranche already has a newer completion review,
closed work order, or downstream closure artifact. If closure exists, the next
move is reconciliation or dependency-release refresh, not duplicate dispatch.

## Design Control Gate

| Control | Decision |
|---|---|
| Foundation value | High: stale roadmap state can cause duplicate work and wrong next moves across planes |
| Scope size | Small: one stale roadmap reconciliation plus learning review |
| Runtime risk | None authorized |
| Latency posture | RSF-T2 must be narrow and dispatch-time; no broad repository scan |
| Legacy posture | Not applicable; no legacy content is read or absorbed |
| Claim boundary | One stale CI2 roadmap defect reconciled, not all roadmap freshness solved |

## Tranche Plan

| Tranche | Status | Purpose | Owner |
|---|---|---|---|
| RSF-T1 | CLOSED_PASS_BOUNDED | Reconcile CI2 roadmap state against T3/T4/T5 closure evidence and author a stale-roadmap learning review | Claude worker, Codex reviewer |
| RSF-T2 | CLOSED_PASS_BOUNDED | Add or extend a machine guard that blocks ready packets when source evidence shows the target tranche is already closed | Claude worker, Codex reviewer |
| RSF-T3 | CLOSED_PASS_BOUNDED | Apply the guard to one non-CI2 roadmap sample and document operator-facing next-move behavior | Claude worker, Codex reviewer |

## Work Plan

1. RSF-T1 reconciles the stale CI2 roadmap rows. DONE at `1c3724d0`.
2. RSF-T1 writes a source-backed learning review. DONE at `1c3724d0`.
3. Codex reviews and commits RSF-T1 if accepted. DONE at `1c3724d0`.
4. RSF-T2 designs and implements the narrow machine guard. DONE in reviewer
   material batch.

## RSF-T1 Acceptance Criteria

| ID | Criterion |
|---|---|
| T1-AC1 | CI2 roadmap top status is updated from stale T3-ready language to an evidence-backed closed/reconciled status. |
| T1-AC2 | CI2 tranche rows for T3, T4, and T5 cite their completion reviews and no longer imply dispatch/hold work remains. |
| T1-AC3 | A completion or audit review records the stale roadmap defect, the exact source evidence, and the corrected next-move boundary. |
| T1-AC4 | The review includes Finding-To-Governance Learning Disposition and recommends RSF-T2 as machine-check candidate, not worker blame. |
| T1-AC5 | No runtime, provider, credential, public-sync, or broad legacy scan work is performed. |

## Acceptance Criteria

The roadmap is successful when RSF-T1 produces a clean no-commit worker return,
Codex verifies the actual diff, and the CI2 roadmap no longer contradicts the
existing T3/T4/T5 closure artifacts.

## Verification / Evidence

Required evidence:

- source rows from the CI2 roadmap and CI2-T3/T4/T5 completion reviews;
- `git diff --name-status`;
- worker-return fast gate;
- reviewer closure gates on the committed range;
- explicit `N/A with reason` for runtime, provider, public-sync, and legacy
  absorption.

## RSF-T2 Guard Candidate

RSF-T2 should inspect and, if feasible, extend dispatch-time checks so that a
ready/dispatch work order derived from a roadmap cannot proceed when the
target roadmap/tranche has a newer closed completion artifact. The exact
implementation should be source-verified after RSF-T1, but likely candidates
include:

- `governance/compat/check_work_order_dispatch_quality.py`;
- `governance/compat/run_agent_autorun_workflow_gate.py`;
- a narrow new checker invoked by dispatch-quality and pre-dispatch gates.

RSF-T2 must avoid a slow broad repository scan. It should use explicit roadmap
and work-order references first, then a bounded filename search for matching
tranche identifiers.

## RSF-T2 Acceptance Criteria

| ID | Criterion |
|---|---|
| T2-AC1 | Dispatch-quality blocks a ready/dispatch work order when it references a roadmap/tranche whose matching completion artifact already reports `CLOSED_PASS_BOUNDED`. |
| T2-AC2 | The guard uses explicit work-order/roadmap references and bounded filename matching; it does not scan all repository text. |
| T2-AC3 | Focused tests include one negative stale-redispatch fixture and one non-stale control fixture. |
| T2-AC4 | Existing dispatch-quality tests continue to pass. |
| T2-AC5 | No runtime, provider, credential, public-sync, broad legacy scan, or product implementation is performed. |

## RSF-T2 Closure Note

RSF-T2 added a bounded stale-roadmap redispatch validation to
`governance/compat/check_work_order_dispatch_quality.py` and focused tests in
`governance/compat/test_check_work_order_dispatch_quality.py`. Codex accepted
the worker return after one reviewer repair: explicit completion-path matching
now reads only the work order's own `completionReviewPath` field, so prior
completion artifacts cited in an Authority Chain do not false-positive as the
current tranche closure.

Verification:

- `python -m pytest governance/compat/test_check_work_order_dispatch_quality.py`
  PASS 84/84.
- `python governance/compat/check_work_order_dispatch_quality.py --base 12d805d1 --head HEAD --enforce`
  PASS.
- `python governance/compat/run_worker_return_fast_gate.py` PASS.
- `python governance/compat/check_agent_operation_trace.py --base 12d805d1 --head HEAD --enforce`
  PASS.
- `git diff --check` PASS.

## RSF-T3 Dispatch Note

RSF-T3 was selected after a Codex source audit of CCLV-T2 actual work and
current continuity. The non-CI2 sample is the Model Gateway C-02 P2 next-move
surface: C-02 P2 work order and state entry already report
`CLOSED_PASS_BOUNDED`, while current front-door/handoff continuity still points
to C-02 P2. The worker must verify this sample from source files and document
operator-facing next-move behavior without redispatching C-02 P2 or touching
runtime/provider/public/session state.

Dispatch artifacts:

- `docs/reviews/CVF_CCLV_T2_CLAUDE_ACTUAL_WORK_AUDIT_AND_RSF_T3_SELECTION_2026-06-16.md`
- `docs/baselines/CVF_GC018_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_2026-06-16.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_FOR_CLAUDE_2026-06-16.md`

## RSF-T3 Closure Note

RSF-T3 is `CLOSED_PASS_BOUNDED`. Claude's worker return confirmed C-02 P2 is
`CLOSED_PASS_BOUNDED` from the work order and state entry, confirmed the stale
next-move contradiction existed at CCLV-T2 audit/dispatch-selection time, and
verified that current front-door, handoff, and `nextAllowedMove` surfaces now
route to RSF-T3 and explicitly block C-02 P2 redispatch. Codex accepts the
worker return with reviewer repairs to close the roadmap tranche.

Verification:

- `python governance/compat/run_worker_return_fast_gate.py` PASS.
- `python governance/compat/check_active_session_state.py --enforce` PASS.
- `python governance/compat/check_session_mode_consistency.py --enforce` PASS.
- committed-range pre-closure gate is reviewer-owned for this material batch.

Next control candidate: a fresh, separately authorized next-move freshness
checker that reads `nextAllowedMove.json` and blocks stale references to closed
targets. This roadmap does not implement that checker.

## Non-Regression Boundary

This roadmap does not make old roadmaps canonical again. It creates a bounded
way to prove whether an old roadmap row is still actionable before an agent
dispatches from it.

## Claim / Final / Verification Boundary

This roadmap authorizes reconciliation and guard design only. It does not claim
all stale roadmap states are repaired, and it does not claim a machine guard
until RSF-T2 closes with source-backed implementation evidence.

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `ORCHESTRATOR_PACKET_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `MACHINE_CHECK_ADDED` |
| Next control action | RSF-T3 closed; fresh authorization may open a bounded next-move freshness checker for closed-target references |
| Worker blame | `N/A_WITH_REASON`: stale roadmap state is a control-plane freshness gap; the worker should not infer closure from chat history |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_FOR_CLAUDE_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_COMPLETION_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | this file | `Status: CLOSED_PASS_BOUNDED`; RSF-T3 row `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason | no corpus registry JSON mutation authorized; RSF-T3 is not a corpus registry tranche | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no corpus registry Markdown mutation authorized; RSF-T3 is not a corpus registry tranche | BLOCKED with reason |
| External evidence digest | N/A with reason | no external source, provider, OCR, or live-proof artifact | N/A with reason |
| System loop interlock | N/A with reason | no system loop interlock registry mutation authorized | N/A with reason |
| Session continuity | N/A with reason | material closure excludes session-sync; session update is reviewer-owned after commit if needed | N/A with reason |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance roadmap. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Expected changed set | `docs/roadmaps/CVF_ROADMAP_STATE_RECONCILIATION_AND_NEXT_MOVE_FRESHNESS_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_FOR_CLAUDE_2026-06-16.md`; `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_WORKER_RETURN_2026-06-16.md`; `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_COMPLETION_2026-06-16.md` |
| Actual changed set | `docs/roadmaps/CVF_ROADMAP_STATE_RECONCILIATION_AND_NEXT_MOVE_FRESHNESS_ROADMAP_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_FOR_CLAUDE_2026-06-16.md`; `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_WORKER_RETURN_2026-06-16.md`; `docs/reviews/CVF_ROADMAP_STATE_RECONCILIATION_T3_NON_CI2_NEXT_MOVE_SAMPLE_COMPLETION_2026-06-16.md` |
| Trace boundary | RSF-T3 material closure only |
