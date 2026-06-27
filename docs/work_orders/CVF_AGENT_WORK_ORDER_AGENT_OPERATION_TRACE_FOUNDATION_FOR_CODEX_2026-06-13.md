# CVF Agent Work Order - Agent Operation Trace Foundation For Codex

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-13

Owner / Orchestrator: Codex

Implementer: Codex

Reviewer / closer: Codex, with machine gates

Commit mode: WORKER_MAY_COMMIT

executionBaseHead: `f789498d`

rawMemoryReleased=false

## Purpose

Implement a bounded CVF control-plane trace foundation so future agent/provider
work leaves repo-local evidence without CVF pretending to build or own
`codex_cowork`, `claude_cowork`, OS audit, or provider platform capability.

## Authority Chain

Operator instruction in the current session authorizes Codex to proceed after
the AOT-T1 trace-foundation recommendation. FPC-T3-C07 supplies the governed
design boundary for repo-local implementation.

## Agent Roles

| Role | Actor | Boundary |
| --- | --- | --- |
| Orchestrator | Codex | source-verify and keep scope bounded |
| Implementer | Codex | update standard, template, checker, tests, and hook wiring only |
| Reviewer / closer | Codex plus machine gates | verify trace evidence, closure rows, and clean worktree |

## Required First Reads

| File | Reason |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | active front door |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | machine-readable state |
| `AGENT_HANDOFF_V18_2026-06-12.md` | active handoff |
| `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | C07 boundary |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | template owner surface |

## Scope / Target / Owner Boundary

Allowed files:

- `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`;
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`;
- `governance/compat/check_agent_operation_trace.py`;
- `governance/compat/test_check_agent_operation_trace.py`;
- `governance/compat/run_local_governance_hook_chain.py`;
- `governance/compat/run_agent_autorun_workflow_gate.py`;
- this work order;
- paired GC-018 and completion review.

Forbidden files/actions:

- external app repositories;
- `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`;
- runtime provider/OCR/source behavior outside governance checkers;
- `CVF_SESSION/**` until a later dedicated session sync;
- public-sync;
- OS audit, Sysmon, EDR, file watcher services, destructive broker, or agent
  computer-control permission changes.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| FPC-T3-C07 is design-only and repo-local checker needs separate work order | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | `FPC-T3-C07 Design Boundary` | `check_workspace_integrity.py` boundary | FPC-T3 C07 plan | ACCEPT |
| C07 OS attribution requires separate operator decision | `docs/reference/CVF_FPC_T3_FOUNDATION_CHECKER_TEMPLATE_COVERAGE_PLAN_2026-06-13.md` | `separate OPERATOR DECISION` | `Windows Security Audit`, `Sysmon`, `file watcher service` | FPC-T3 C07 plan | ACCEPT |
| Work-order template is the canonical execution packet surface | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | `## Purpose` | `CVF Agent Work Order` | work-order template | ACCEPT |
| Reviewer-fast/pre-commit hook chain is centrally wired | `governance/compat/run_local_governance_hook_chain.py` | `REVIEWER_FAST_CHECKS`, `HOOK_CHAINS` | `reviewer-fast`, `pre-commit`, `pre-push` | hook chain runner | ACCEPT |
| Autorun common gates are centrally wired | `governance/compat/run_agent_autorun_workflow_gate.py` | `_common_commands` | phase gate command bundle | autorun workflow wrapper | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Source requirement | Work-order action | Status |
| --- | --- | --- |
| FPC-T3-C07 repo-local implementation requires separate Codex work order | this work order supplies that authorization | PASS |
| C07 must not claim OS/user attribution | standard and checker claim boundary exclude OS-level attribution | PASS |
| Agent/provider work should leave evidence useful now | template and checker require Agent Operation Trace Block on changed execution artifacts | PASS |
| Protected-folder disappearance must be visible | checker flags protected delete/rename without disposition | PASS |

## Pre-Flight Checks

| Check | Evidence | Status |
| --- | --- | --- |
| Active session state | `python governance/compat/check_active_session_state.py --enforce` | PASS |
| Worktree before edits | `git status --short` | clean |
| Execution base | `git rev-parse --short HEAD` | `f789498d` |

## Write Ownership

Codex may write only the allowed files listed in this work order. Any
session-state update must be a later dedicated session-sync batch.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one new repo-local agent operation
trace checker, focused tests, hook-chain wiring, autorun wiring, the canonical
trace standard, and the work-order-template trace block. This scope does not
authorize unrelated guard semantics, session-state mutation, runtime behavior,
external repository work, public-sync, or OS/endpoint audit configuration.

Protected paths:

- `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `governance/compat/check_agent_operation_trace.py`
- `governance/compat/test_check_agent_operation_trace.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `docs/baselines/CVF_GC018_AGENT_OPERATION_TRACE_FOUNDATION_2026-06-13.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_AGENT_OPERATION_TRACE_FOUNDATION_FOR_CODEX_2026-06-13.md`
- `docs/reviews/CVF_AGENT_OPERATION_TRACE_FOUNDATION_COMPLETION_2026-06-13.md`

Operator authorization: after Codex recommended the agent-operation trace
foundation as the highest-value CVF core response to co_work platform growth,
the operator confirmed the framing and instructed Codex to proceed.

Rollback boundary: revert only this AOT-T1 trace-foundation batch if the
checker, template block, hook wiring, standard, or closure packet is incorrect.
Do not revert FPC-T3 material closure commit `c1fd85d3`, session sync commit
`f789498d`, or unrelated history.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex |
| Provider or surface | Codex CLI |
| Session or invocation | current session; execution base `f789498d` |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | `apply_patch`, PowerShell, Python unittest, governance hook chain |
| Target paths | allowed files listed in this work order |
| Allowed scope source | operator instruction plus FPC-T3-C07 closure boundary |
| Before status evidence | `git status --short` clean before material edits |
| After status evidence | completion review verification and final status |
| Diff evidence | `git diff --name-status`, committed-range pre-closure |
| Approval boundary | operator approved proceeding with CVF trace supervision, not co_work development |
| Claim boundary | repo-local trace/integrity evidence only; no OS/user attribution |
| Deletion or rename disposition | N/A with reason: no protected deletion or rename authorized |

## Execution Plan

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Add canonical trace standard | new reference file |
| 2 | Add checker and focused tests | `check_agent_operation_trace.py`; unittest |
| 3 | Wire checker into local and autorun gates | hook chain and autorun wrapper diff |
| 4 | Update work-order template | new trace block and checklist item |
| 5 | Close with governance evidence | completion review, reviewer-fast, pre-commit, pre-closure |

## Review Gate

Closure requires focused tests, direct AOT checker pass, reviewer-fast,
pre-commit, committed-range pre-closure after commit, and clean final worktree.

## Evidence Requirements

Required evidence:

- `python -m unittest governance.compat.test_check_agent_operation_trace`;
- `python governance/compat/check_agent_operation_trace.py --base f789498d --head HEAD --enforce`;
- `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`;
- `python governance/compat/run_local_governance_hook_chain.py --hook pre-commit`;
- committed-range `pre-closure` after commit.

## Acceptance Criteria

| Criterion | Status |
| --- | --- |
| Standard states CVF supervises agent/provider traces and does not develop co_work | PASS |
| Template requires Agent Operation Trace Block | PASS |
| Checker catches missing trace block on changed work orders/reviews | PASS |
| Checker catches protected delete/rename without disposition | PASS |
| Tests cover core positive and negative cases | PASS |
| Hook chain and autorun wrapper call the checker | PASS |
| OS attribution remains out of scope | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AGENT_OPERATION_TRACE_FOUNDATION_COMPLETION_2026-06-13.md` | completion review exists | PASS |
| Roadmap state | N/A with reason | AOT-T1 is a C07 implementation follow-up authorized by GC-018, not a parent-roadmap status closure | N/A with reason |
| Registry JSON | BLOCKED with reason | no GC-051 source/test/runtime registry surface is authorized | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason | no corpus registry Markdown owner surface is authorized | BLOCKED with reason |
| External evidence digest | N/A with reason | no external source, provider, OCR, OS audit, or endpoint artifact used | N/A with reason |
| Session continuity | N/A with reason | session sync is a dedicated follow-up only if current mode changes after material closure | N/A with reason |
| System loop interlock | N/A with reason | no interlock registry mutation authorized | N/A with reason |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |

## Closure Checklist

| Item | Status |
| --- | --- |
| Acceptance criteria satisfied | PASS |
| Focused tests run | PASS |
| Agent Operation Trace Block present | PASS |
| Changed-file scope recorded | PASS |
| Core Guard Self-Protection Authorization included | PASS |
| No public-sync authorized | PASS |
| No OS/endpoint attribution claim made | PASS |

## Return-To-Orchestrator Conditions

Return to operator only if a required gate fails outside allowed scope, a
protected deletion/rename appears without authorization, or OS/endpoint audit
becomes necessary.

## Operator Checkpoint

No operator checkpoint remains inside AOT-T1. OS-level attribution, Sysmon,
EDR, file watcher services, destructive broker, and agent computer-control
changes remain separate operator decisions.

## Claim Boundary

This work order authorizes only repo-local governance-control hardening. It
does not implement co_work, OS audit, endpoint telemetry, provider platform
features, runtime behavior, public-sync, or readiness claims.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance-control hardening. Public-sync is not
authorized.

rawMemoryReleased=false
