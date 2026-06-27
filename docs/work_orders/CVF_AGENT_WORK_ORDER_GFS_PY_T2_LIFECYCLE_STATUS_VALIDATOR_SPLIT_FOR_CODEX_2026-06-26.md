# CVF Agent Work Order GFS-PY T2 Lifecycle Status Validator Split For Codex

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: work_order

Batch ID: GFS-PY-T2-LIFECYCLE-STATUS-SPLIT

dispatchBaseHead: 006491be

executionBaseHead: 006491be

closureBaseHead: 006491be

Commit mode: `WORKER_MAY_COMMIT_AFTER_REVIEWER_CLOSURE`

## Dispatch Prompt Envelope

Role: Codex single-agent multi-role dispatcher, worker, reviewer/closer, then
session-sync steward in a separate commit if continuity surfaces change.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_GFS_PY_T2_LIFECYCLE_STATUS_VALIDATOR_SPLIT_FOR_CODEX_2026-06-26.md`

Current-time notes: T1 already closed; T2 is now operator-selected and limited
to lifecycle/status validator extraction.

Do-not-misread notes: do not move source-verification or token-collision
validators, do not begin T4 orchestrator-shell reduction, and do not change any
failure message or validation threshold.

## Purpose

Execute GFS-PY T2 by extracting lifecycle/status helpers into a dedicated module
while preserving dispatch-quality behavior and shrinking the monolith.

## Scope / Methodology

Allowed scope: the GFS-PY roadmap, this GC-018/work order/completion review,
the dispatch-quality checker, one lifecycle helper module, one focused test
module, and the Python size registry cap.

Forbidden scope: source-verification/token-collision validator split, T4 shell
reduction, new validator behavior, failure-message changes, runtime/provider
code, public-sync, generated aggregates, resolver mutation, adapter behavior,
package work, or session-sync in the material commit.

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | current chat request to proceed to GFS-PY T2 | ACCEPT |
| GFS-PY roadmap | `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | ACCEPT |
| GC-018 baseline | `docs/baselines/CVF_GC018_GFS_PY_T2_LIFECYCLE_STATUS_VALIDATOR_SPLIT_2026-06-26.md` | ACCEPT |
| T1 completion | `docs/reviews/CVF_GFS_PY_T1_DISPATCH_QUALITY_HELPER_SPLIT_COMPLETION_2026-06-25.md` | ACCEPT |

## Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Dispatcher | Codex | source-verified T2 packet |
| Worker | Codex | behavior-preserving extraction |
| Reviewer/closer | Codex | tests, gates, material commit |
| Session-sync steward | Codex | separate commit only if needed |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex executes dispatcher, worker, reviewer/closer, and separate session-sync steward roles |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=006491be`; `executionBaseHead=006491be`; `closureBaseHead=006491be`; session-sync base is material commit |
| changedSetScope(phase) | material paths only for code/docs/registry; session-sync paths only after material commit |
| traceScope(phase, actor) | completion review records material trace |
| commitOwner(phase) | Codex owns material commit and separate session-sync commit |
| crossBatchIsolation | do not mix T3/T4, runtime/provider/public/generated/session changes into material commit |
| nextMoveSurfaces | update after material commit if mode or next allowed move changes |
| Closer designation | Codex reviewer/closer |

## Required First Reads

| Source | Action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V23_2026-06-26.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | SOURCE_VERIFIED |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| T2 is the lifecycle/status split | `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | Tranches | `T2 - Split work-order lifecycle / status validators` | GFS-PY roadmap | EXISTS | ACCEPT |
| Status extraction is imported by the checker | `governance/compat/check_work_order_dispatch_quality.py` | import block | `_extract_status` | dispatch-quality checker | EXISTS | ACCEPT |
| Lifecycle module owns closed-status finality | `governance/compat/check_work_order_dispatch_quality_lifecycle.py` | function definition | `_validate_closed_artifact_finality` | lifecycle/status helper module | EXISTS | ACCEPT |
| Lifecycle module owns dependency release validation | `governance/compat/check_work_order_dispatch_quality_lifecycle.py` | function definition | `_validate_ready_dependency_release` | lifecycle/status helper module | EXISTS | ACCEPT |
| Focused lifecycle tests cover extracted behavior | `governance/compat/test_check_work_order_dispatch_quality_lifecycle.py` | test module | `test_ready_dependency_release_commit_path_mismatch_fails` | lifecycle/status helper tests | EXISTS | ACCEPT |
| Python size registry carries the monolith cap | `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | exception entry | `approvedMaxLines` | Python size registry | VALUE_SET | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects:

- ADIF-0001 - exact paths only.
- ADIF-0002 - no provider-local authority.
- ADIF-0007 - no gate-trigger prose as evidence.
- ADIF-0006 - symbol cells use bare symbols.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order action | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Extract lifecycle/status validators | move named helpers to lifecycle module | `check_work_order_dispatch_quality_lifecycle.py` | focused tests | PASS |
| Preserve behavior | run existing dispatch-quality tests | existing test suite | pytest | PASS |
| Lower monolith cap | set `approvedMaxLines=2720` | Python size registry | size guard | PASS |
| Keep T3/T4 separate | leave T3 work-order-ready, T4 held | roadmap state | completion review | PASS |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: GFS-PY T2 may modify the dispatch-quality
checker, add lifecycle helper/test modules, and lower the Python size registry
cap. It must not weaken any checker or change validation behavior.

Protected paths:

- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/check_work_order_dispatch_quality_lifecycle.py`
- `governance/compat/test_check_work_order_dispatch_quality_lifecycle.py`
- `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`

Operator authorization: current operator request to move to GFS-PY T2.

Rollback boundary: revert this material commit only; do not revert prior GFS-PY
closures.

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| T0 | source-verify T2 and predecessor closure | GC-018/work order |
| T1 | extract lifecycle/status helpers | new module and monolith imports |
| T2 | add focused tests | lifecycle test module |
| T3 | run suites and Python size guard | command output |
| T4 | update roadmap, completion review, and commit material | material commit |

## Pre-Flight Checks

| Check | Disposition |
|---|---|
| Startup read order | COMPLETE |
| T1 predecessor evidence | ACCEPT |
| T2 source verification | ACCEPT |
| ADIF disclosure | COMPLETE |
| Guard orientation and gotchas | READ |

## Write Ownership

| Path | Ownership |
|---|---|
| `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | material roadmap update |
| `docs/baselines/CVF_GC018_GFS_PY_T2_LIFECYCLE_STATUS_VALIDATOR_SPLIT_2026-06-26.md` | GFS-PY T2 baseline |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_GFS_PY_T2_LIFECYCLE_STATUS_VALIDATOR_SPLIT_FOR_CODEX_2026-06-26.md` | GFS-PY T2 work order |
| `docs/reviews/CVF_GFS_PY_T2_LIFECYCLE_STATUS_VALIDATOR_SPLIT_COMPLETION_2026-06-26.md` | GFS-PY T2 completion review |
| `governance/compat/check_work_order_dispatch_quality.py` | lifecycle/status extraction call sites |
| `governance/compat/check_work_order_dispatch_quality_lifecycle.py` | extracted lifecycle/status helpers |
| `governance/compat/test_check_work_order_dispatch_quality_lifecycle.py` | focused lifecycle/status tests |
| `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | monolith cap ratchet |

## Operator Checkpoint

Operator selected GFS-PY T2. No additional checkpoint is required unless a
gate demands behavior change, T3/T4 execution, runtime/provider work,
public-sync, or destructive action.

## Required Artifact Manifest

| Artifact | Required disposition |
|---|---|
| `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | UPDATE |
| `docs/baselines/CVF_GC018_GFS_PY_T2_LIFECYCLE_STATUS_VALIDATOR_SPLIT_2026-06-26.md` | CREATE |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_GFS_PY_T2_LIFECYCLE_STATUS_VALIDATOR_SPLIT_FOR_CODEX_2026-06-26.md` | CREATE |
| `docs/reviews/CVF_GFS_PY_T2_LIFECYCLE_STATUS_VALIDATOR_SPLIT_COMPLETION_2026-06-26.md` | CREATE |
| `governance/compat/check_work_order_dispatch_quality.py` | UPDATE |
| `governance/compat/check_work_order_dispatch_quality_lifecycle.py` | CREATE |
| `governance/compat/test_check_work_order_dispatch_quality_lifecycle.py` | CREATE |
| `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | UPDATE |

## Work-Order Fulfillment Manifest

| Artifact | Owner | Disposition |
|---|---|---|
| `governance/compat/check_work_order_dispatch_quality.py` | Codex | shrink and import lifecycle helpers |
| `governance/compat/check_work_order_dispatch_quality_lifecycle.py` | Codex | new extracted helper module |
| `governance/compat/test_check_work_order_dispatch_quality_lifecycle.py` | Codex | new focused tests |
| `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | Codex | lower monolith cap |
| `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | Codex | update T2/T3 state |
| `docs/reviews/CVF_GFS_PY_T2_LIFECYCLE_STATUS_VALIDATOR_SPLIT_COMPLETION_2026-06-26.md` | Codex | completion review |

## Worker Autonomy / No-Question Rule

Allowed-scope gate failures are repaired and rerun without asking the operator.
Escalate only for scope expansion, validation semantics change, live/provider
proof, public-sync, forbidden paths, destructive action, or T3/T4 execution.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; tests named above |
| Runtime behavior claimed | N/A_WITH_REASON: local checker refactor only |
| Helper/checker implementation claimed | behavior-preserving extraction, tested |
| Provider/live proof claimed | N/A_WITH_REASON |
| Provider registry surfaces | N/A_WITH_REASON: no provider-registry or live-governance claim |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS |

## Evidence Requirements

| Command | Required result |
|---|---|
| `python -m pytest governance/compat/test_check_work_order_dispatch_quality_lifecycle.py -q` | PASS |
| `python -m pytest governance/compat/test_check_work_order_dispatch_quality.py governance/compat/test_check_work_order_dispatch_quality_tables.py governance/compat/test_check_work_order_dispatch_quality_lifecycle.py -q` | PASS |
| `python governance/compat/check_python_automation_size.py --enforce` | COMPLIANT |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 006491be --head HEAD` | PASS |
| `python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base 006491be --head HEAD --enforce` | PASS |

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Lifecycle/status helpers extracted | new helper module and monolith imports |
| Behavior unchanged | dispatch-quality suites pass |
| Monolith shrinks | line count 2720 |
| Registry cap lowered | `approvedMaxLines=2720` |
| T3/T4 not executed | roadmap state and claim boundary |

## Review Gate

Reviewer/closer must confirm all tests and gates pass, no behavior messages are
changed intentionally, and material/session-sync remain split.

## Closure Checklist

| Item | Disposition |
|---|---|
| GC-018 filed | COMPLETE |
| Work order filed | COMPLETE |
| Lifecycle module added | COMPLETE |
| Focused tests added | COMPLETE |
| Registry cap lowered | COMPLETE |
| Tests/gates run | REQUIRED before commit |
| Session-sync split | REQUIRED after material commit if mode changes |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` if all gates pass and the material commit lands.
Return `BLOCKED_WITH_REASON` if extraction changes behavior or T3/T4 scope is
required.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: internal governance checker refactor; no public-sync authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | GFS-PY T2 work order |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no Delta receipt is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT - local checker refactor and tests |
| invocationBoundary | local governed source/docs edit |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | behavior-preserving lifecycle/status helper split |
| forbiddenExpansion | no T3/T4, validation behavior change, provider/live proof, public-sync, session-sync in material commit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | GFS-PY T2 work order, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | source reads, apply_patch, pytest, Python size guard, governance gates |
| Target paths | GFS-PY T2 material manifest |
| Allowed scope source | operator request to move to GFS-PY T2 |
| Before status evidence | HEAD `006491be`; clean worktree |
| After status evidence | material commit pending |
| Diff evidence | `git diff --name-status` |
| Approval boundary | GFS-PY T2 only |
| Claim boundary | local checker refactor only |
| Agent type | single-agent multi-role |
| Invocation ID | `gfs-py-t2-work-order-2026-06-26` |
| Expected manifest | roadmap, baseline, work order, completion review, checker, lifecycle module/test, Python size registry |
| Actual changed set | pending material commit manifest |
| Manifest delta | MATCH_PENDING_COMMIT |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GFS_PY_T2_LIFECYCLE_STATUS_VALIDATOR_SPLIT_COMPLETION_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | `T2_PASS_BOUNDED_T3_WORK_ORDER_READY` | PASS |
| Registry JSON | `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | `approvedMaxLines=2720` | PASS |
| Registry Markdown | N/A with reason | no companion markdown registry | BLOCKED with reason |
| External evidence digest | N/A | no external digest | N/A with reason |
| System loop interlock | this work order | T3 remains fresh-work-order only | PASS |
| Session continuity | active session state/front door/handoff | update separately after material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Focused lifecycle tests | 11/11 | PASS |
| Combined dispatch-quality tests | 144/144 | PASS |
| Monolith line count | 2720 | PASS |
| Python size guard | COMPLIANT | PASS |
| Public export evidence | N/A with reason: no public-sync authorized | N/A_WITH_REASON |

## Claim Boundary

This work order closes only GFS-PY T2. It does not authorize T3/T4 execution,
runtime/provider/live proof, public-sync, generated aggregates, package work,
adapter behavior, resolver mutation, or session-sync in the material commit.
