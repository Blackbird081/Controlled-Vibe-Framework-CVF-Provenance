# CVF Agent Work Order GFS-PY T4 Orchestrator Shell Reduction For Codex

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-26

docType: work_order

Batch ID: GFS-PY-T4-ORCHESTRATOR-SHELL-REDUCTION

dispatchBaseHead: b04db9f4

executionBaseHead: b04db9f4

closureBaseHead: b04db9f4

Commit mode: `WORKER_MAY_COMMIT_AFTER_REVIEWER_CLOSURE`

## Dispatch Prompt Envelope

Role: Codex single-agent multi-role dispatcher, worker, reviewer/closer, then
session-sync steward in a separate commit if continuity surfaces change.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_GFS_PY_T4_ORCHESTRATOR_SHELL_REDUCTION_FOR_CODEX_2026-06-26.md`

Current-time notes: T3 already closed; T4 is now operator-selected and limited
to orchestrator-shell reduction plus roadmap closure.

Do-not-misread notes: do not change any failure message, validation threshold,
dispatch-quality policy, runtime/provider behavior, resolver behavior, or
public-sync state.

## Purpose

Execute GFS-PY T4 by reducing the dispatch-quality checker monolith to an
orchestrator shell while preserving the public entrypoint and behavior.

## Scope / Methodology

Allowed scope: the GFS-PY roadmap, this GC-018/work order/completion review,
the dispatch-quality checker, three implementation modules, and the Python size
registry.

Forbidden scope: validation semantics change, failure-message changes,
runtime/provider code, public-sync, generated aggregates, resolver mutation,
adapter behavior, package work, or session-sync in the material commit.

## Authority Chain

| Authority | Path | Disposition |
|---|---|---|
| Operator instruction | current chat request to continue after GFS-PY T3 | ACCEPT |
| GFS-PY roadmap | `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | ACCEPT |
| GC-018 baseline | `docs/baselines/CVF_GC018_GFS_PY_T4_ORCHESTRATOR_SHELL_REDUCTION_2026-06-26.md` | ACCEPT |
| T3 completion | `docs/reviews/CVF_GFS_PY_T3_SOURCE_VERIFICATION_TOKEN_COLLISION_SPLIT_COMPLETION_2026-06-26.md` | ACCEPT |

## Agent Roles

| Role | Owner | Boundary |
|---|---|---|
| Dispatcher | Codex | source-verified T4 packet |
| Worker | Codex | behavior-preserving shell reduction |
| Reviewer/closer | Codex | tests, gates, material commit |
| Session-sync steward | Codex | separate commit only if needed |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex executes dispatcher, worker, reviewer/closer, and separate session-sync steward roles |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=b04db9f4`; `executionBaseHead=b04db9f4`; `closureBaseHead=b04db9f4`; session-sync base is material commit |
| changedSetScope(phase) | material paths only for code/docs/registry; session-sync paths only after material commit |
| traceScope(phase, actor) | completion review records material trace |
| commitOwner(phase) | Codex owns material commit and separate session-sync commit |
| crossBatchIsolation | do not mix runtime/provider/public/generated/session changes into material commit |
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
| T4 is the orchestrator-shell reduction | `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | Tranches | `T4 - Leave check_work_order_dispatch_quality.py as an orchestrator shell` | GFS-PY roadmap | EXISTS | ACCEPT |
| T3 predecessor is closed | `docs/reviews/CVF_GFS_PY_T3_SOURCE_VERIFICATION_TOKEN_COLLISION_SPLIT_COMPLETION_2026-06-26.md` | Status | `CLOSED_PASS_BOUNDED` | T3 completion review | EXISTS | ACCEPT |
| Main checker declares split implementation modules | `governance/compat/check_work_order_dispatch_quality.py` | line 221 | `IMPLEMENTATION_MODULES` | dispatch-quality checker shell | EXISTS | ACCEPT |
| Main checker loads implementation modules | `governance/compat/check_work_order_dispatch_quality.py` | line 229 | `_load_implementation_modules` | dispatch-quality checker shell | EXISTS | ACCEPT |
| Main checker remains the CLI entrypoint | `governance/compat/check_work_order_dispatch_quality.py` | line 283 | `main` | dispatch-quality checker shell | EXISTS | ACCEPT |
| Core module owns common validator logic | `governance/compat/check_work_order_dispatch_quality_core.py` | line 106 | `_validate_mandatory_remediation_escalation` | dispatch-quality core module | EXISTS | ACCEPT |
| Artifact module owns size-plan classification helper | `governance/compat/check_work_order_dispatch_quality_artifacts.py` | line 598 | `_classify_size_guard_path` | dispatch-quality artifact module | EXISTS | ACCEPT |
| Range module owns work-order validation | `governance/compat/check_work_order_dispatch_quality_range.py` | line 8 | `_validate_work_order` | dispatch-quality range module | EXISTS | ACCEPT |
| Range module owns changed-range classifier | `governance/compat/check_work_order_dispatch_quality_range.py` | line 520 | `_classify` | dispatch-quality range module | EXISTS | ACCEPT |
| Python size registry carries no monolith exception after T4 | `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | exception entries | `exceptions` | Python size registry | VALUE_SET | ACCEPT |

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
| Reduce monolith to orchestrator shell | split remaining implementation into modules | `IMPLEMENTATION_MODULES` | py_compile and tests | PASS |
| Preserve behavior | run existing dispatch-quality tests | existing test suite | pytest | PASS |
| Ratchet monolith exception to shell line count | set `approvedMaxLines=313` | Python size registry | size guard | PASS |
| Close roadmap | add closure package to roadmap | roadmap state | pre-closure gate | PASS |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: GFS-PY T4 may modify the dispatch-quality
checker, add three split implementation modules, ratchet the monolith Python
size exception to 313, and close the GFS-PY roadmap. It must not weaken any checker or
change validation behavior.

Protected paths:

- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/check_work_order_dispatch_quality_core.py`
- `governance/compat/check_work_order_dispatch_quality_artifacts.py`
- `governance/compat/check_work_order_dispatch_quality_range.py`
- `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`

Operator authorization: current operator request to continue after GFS-PY T3.

Rollback boundary: revert this material commit only; do not revert prior GFS-PY
closures.

## Execution Plan

| Step | Action | Evidence |
|---|---|---|
| T0 | source-verify T4 and predecessor closure | GC-018/work order |
| T1 | split remaining implementation functions | three implementation modules and shell loader |
| T2 | ratchet monolith exception to 313 | Python size registry |
| T3 | run compile, suites, and Python size guard | command output |
| T4 | update roadmap, completion review, and commit material | material commit |

## Pre-Flight Checks

| Check | Disposition |
|---|---|
| Startup read order | COMPLETE |
| T3 predecessor evidence | ACCEPT |
| T4 source verification | ACCEPT |
| ADIF disclosure | COMPLETE |
| Guard orientation and gotchas | READ |

## Write Ownership

| Path | Ownership |
|---|---|
| `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | roadmap closure update |
| `docs/baselines/CVF_GC018_GFS_PY_T4_ORCHESTRATOR_SHELL_REDUCTION_2026-06-26.md` | GFS-PY T4 baseline |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_GFS_PY_T4_ORCHESTRATOR_SHELL_REDUCTION_FOR_CODEX_2026-06-26.md` | GFS-PY T4 work order |
| `docs/reviews/CVF_GFS_PY_T4_ORCHESTRATOR_SHELL_REDUCTION_COMPLETION_2026-06-26.md` | GFS-PY T4 completion review |
| `governance/compat/check_work_order_dispatch_quality.py` | orchestrator shell |
| `governance/compat/check_work_order_dispatch_quality_core.py` | split implementation module |
| `governance/compat/check_work_order_dispatch_quality_artifacts.py` | split implementation module |
| `governance/compat/check_work_order_dispatch_quality_range.py` | split implementation module |
| `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | ratchet monolith exception to 313 |

## Operator Checkpoint

Operator selected GFS-PY T4 by saying to continue. No additional checkpoint is
required unless a gate demands behavior change, runtime/provider work,
public-sync, or destructive action.

## Required Artifact Manifest

| Artifact | Required disposition |
|---|---|
| `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | UPDATE |
| `docs/baselines/CVF_GC018_GFS_PY_T4_ORCHESTRATOR_SHELL_REDUCTION_2026-06-26.md` | CREATE |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_GFS_PY_T4_ORCHESTRATOR_SHELL_REDUCTION_FOR_CODEX_2026-06-26.md` | CREATE |
| `docs/reviews/CVF_GFS_PY_T4_ORCHESTRATOR_SHELL_REDUCTION_COMPLETION_2026-06-26.md` | CREATE |
| `governance/compat/check_work_order_dispatch_quality.py` | UPDATE |
| `governance/compat/check_work_order_dispatch_quality_core.py` | CREATE |
| `governance/compat/check_work_order_dispatch_quality_artifacts.py` | CREATE |
| `governance/compat/check_work_order_dispatch_quality_range.py` | CREATE |
| `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | UPDATE |

## Work-Order Fulfillment Manifest

| Artifact | Owner | Disposition |
|---|---|---|
| `governance/compat/check_work_order_dispatch_quality.py` | Codex | shrink to orchestrator shell |
| `governance/compat/check_work_order_dispatch_quality_core.py` | Codex | split implementation module |
| `governance/compat/check_work_order_dispatch_quality_artifacts.py` | Codex | split implementation module |
| `governance/compat/check_work_order_dispatch_quality_range.py` | Codex | split implementation module |
| `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | Codex | ratchet monolith exception to 313 |
| `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | Codex | close roadmap |
| `docs/reviews/CVF_GFS_PY_T4_ORCHESTRATOR_SHELL_REDUCTION_COMPLETION_2026-06-26.md` | Codex | completion review |

## Worker Autonomy / No-Question Rule

Allowed-scope gate failures are repaired and rerun without asking the operator.
Escalate only for scope expansion, validation semantics change, live/provider
proof, public-sync, forbidden paths, or destructive action.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | dispatch-quality checker shell, split modules, existing tests, Python size registry |
| Runtime behavior claimed | N/A_WITH_REASON: local checker refactor only |
| Helper/checker implementation claimed | behavior-preserving shell reduction, tested |
| Provider/live proof claimed | N/A_WITH_REASON |
| Provider registry surfaces | N/A_WITH_REASON: no provider-registry or live-governance claim |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS |

## Evidence Requirements

| Command | Required result |
|---|---|
| `python -m py_compile governance/compat/check_work_order_dispatch_quality.py governance/compat/check_work_order_dispatch_quality_core.py governance/compat/check_work_order_dispatch_quality_artifacts.py governance/compat/check_work_order_dispatch_quality_range.py` | PASS |
| `python -m pytest governance/compat/test_check_work_order_dispatch_quality.py governance/compat/test_check_work_order_dispatch_quality_tables.py governance/compat/test_check_work_order_dispatch_quality_lifecycle.py governance/compat/test_check_work_order_dispatch_quality_source.py -q` | PASS |
| `python governance/compat/check_python_automation_size.py --enforce` | COMPLIANT |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base b04db9f4 --head HEAD` | PASS |
| `python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base b04db9f4 --head HEAD --enforce` | PASS |

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Main checker reduced to shell | line count 313 and loader symbols |
| Behavior preserved | dispatch-quality suites pass |
| Split modules under hard threshold | Python size guard COMPLIANT |
| Monolith exception ratcheted to 313 | registry update |
| Roadmap closed | roadmap status and closure package |

## Review Gate

Reviewer/closer must confirm all tests and gates pass, no behavior messages are
changed intentionally, and material/session-sync remain split.

## Closure Checklist

| Item | Disposition |
|---|---|
| GC-018 filed | COMPLETE |
| Work order filed | COMPLETE |
| Split modules added | COMPLETE |
| Registry exception ratcheted to 313 | COMPLETE |
| Roadmap closed | COMPLETE |
| Tests/gates run | REQUIRED before commit |
| Session-sync split | REQUIRED after material commit if mode changes |

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` if all gates pass and the material commit lands.
Return `BLOCKED_WITH_REASON` if the split changes behavior.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: internal governance checker refactor; no public-sync authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | GFS-PY T4 work order |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no Delta receipt is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT - local checker refactor and tests |
| invocationBoundary | local governed source/docs edit |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | behavior-preserving orchestrator-shell reduction |
| forbiddenExpansion | no validation behavior change, provider/live proof, public-sync, session-sync in material commit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | GFS-PY T4 work order, 2026-06-26 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | source reads, mechanical rewrite, apply_patch, pytest, Python size guard, governance gates |
| Target paths | GFS-PY T4 material manifest |
| Allowed scope source | operator request to continue after GFS-PY T3 |
| Before status evidence | HEAD `b04db9f4`; clean worktree |
| After status evidence | material commit pending |
| Diff evidence | `git diff --name-status` |
| Approval boundary | GFS-PY T4 only |
| Claim boundary | local checker refactor only |
| Agent type | single-agent multi-role |
| Invocation ID | `gfs-py-t4-work-order-2026-06-26` |
| Expected manifest | roadmap, baseline, work order, completion review, checker shell, three modules, Python size registry |
| Actual changed set | pending material commit manifest |
| Manifest delta | MATCH_PENDING_COMMIT |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GFS_PY_T4_ORCHESTRATOR_SHELL_REDUCTION_COMPLETION_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_GOVERNED_PYTHON_FILE_SIZE_COVERAGE_ROADMAP_2026-06-25.md` | `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | monolith exception ratcheted to 313 | PASS |
| Registry Markdown | N/A with reason | no companion markdown registry | BLOCKED with reason |
| External evidence digest | N/A | no external digest | N/A with reason |
| System loop interlock | this work order | GFS-PY T0-T4 closed | PASS |
| Session continuity | active session state/front door/handoff | update separately after material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| py_compile | PASS | PASS |
| Combined dispatch-quality tests | 150/150 | PASS |
| Main checker line count | 313 | PASS |
| Python size guard | COMPLIANT | PASS |
| Public export evidence | N/A with reason: no public-sync authorized | N/A_WITH_REASON |

## Claim Boundary

This work order closes only GFS-PY T4 and the GFS-PY roadmap. It does not
authorize runtime/provider/live proof, public-sync, generated aggregates,
package work, adapter behavior, resolver mutation, or session-sync in the
material commit.
