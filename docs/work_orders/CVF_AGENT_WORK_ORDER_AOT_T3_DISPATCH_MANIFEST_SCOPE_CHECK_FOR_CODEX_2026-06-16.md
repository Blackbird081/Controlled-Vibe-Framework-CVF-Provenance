# CVF Agent Work Order - AOT-T3 Dispatch Manifest Scope Check For Codex

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-16

Owner: Codex

Worker: Codex

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `e509aa4d`

executionBaseHead: `e509aa4d`

closureBaseHead: `e509aa4d`

rawMemoryReleased: false

## Dispatch Prompt Envelope

Prompt:

Implement AOT-T3 as a standalone B12 cleanup. Keep the scope limited to the AOT
checker/test/standard and roadmap/closure artifacts. Do not open AHB-T2.

Execution mode: `WORKER_MAY_COMMIT`.

Reviewer: Codex self-review under governed gates.

## Purpose

Close the queued B12 machine-check hardening: dispatch trace manifests must
describe the dispatch changed set, and future execution paths must stay in
ownership or expected-deliverable sections.

## Authority Chain

- Operator instruction: 2026-06-16 selection of AOT-T3 as the fast cleanup.
- Active session state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Finding standard:
  `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`.
- AOT standard:
  `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`.
- Finding roadmap:
  `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md`.
- GC-018:
  `docs/baselines/CVF_GC018_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_2026-06-16.md`.
- Active handoff: `AGENT_HANDOFF_V19_2026-06-15.md`.

Authority boundary: this work order does not authorize AHB-T2, public-sync,
runtime/product behavior changes, external API usage, interlock registry edits,
or live governance proof.

## Agent Roles

- Orchestrator / dispatcher: Codex.
- Implementer: Codex.
- Reviewer / committer: Codex.
- Operator approval required for: scope expansion, AHB-T2 ratification,
  public-sync, live/provider proof, runtime/product mutation, destructive
  actions, or claim-boundary changes.

## Scope

Allowed scope:

- update the AOT checker and focused tests;
- update the AOT standard;
- update the finding-propagation and AHB roadmaps to record standalone AOT-T3
  closure;
- create this work order, GC-018, and completion review.
- allowed paths:
  `governance/compat/check_agent_operation_trace.py`;
  `governance/compat/test_check_agent_operation_trace.py`;
  `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`;
  `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md`;
  `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`;
  `docs/baselines/CVF_GC018_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_2026-06-16.md`;
  `docs/work_orders/CVF_AGENT_WORK_ORDER_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_FOR_CODEX_2026-06-16.md`;
  `docs/reviews/CVF_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_COMPLETION_2026-06-16.md`.

Forbidden scope:

- do not open or ratify AHB-T2;
- do not implement unified AHB contract enforcement;
- do not edit product runtime, provider adapters, interlock registries, public
  clone content, provider-local memory, or external app content;
- do not run live/provider proof;
- do not claim public or production readiness.

Risk ceiling: R2 bounded governance checker hardening.

## Required First Reads

- `governance/compat/check_agent_operation_trace.py`
- `governance/compat/test_check_agent_operation_trace.py`
- `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`
- `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md`
- `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md`
- `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`

## Pre-Flight Checks

Commands:

```powershell
git rev-parse --short HEAD
git status --short
python -m unittest governance.compat.test_check_agent_operation_trace
```

Expected results: base HEAD is `e509aa4d`, worktree starts clean, and focused
AOT tests pass before or after allowed-scope repair.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| AOT checker compares trace manifests | `governance/compat/check_agent_operation_trace.py` | `_check_manifest_delta` | `Expected manifest` | AOT checker | ACCEPT |
| AOT checker parses paths from trace fields | `governance/compat/check_agent_operation_trace.py` | `_parse_path_list` | `_parse_path_list` | AOT checker | ACCEPT |
| AOT tests already cover manifest match and deltas | `governance/compat/test_check_agent_operation_trace.py` | `AgentOperationTraceTests` | `MISSING_DELIVERABLE`; `UNAUTHORIZED_ADDITION` | unittest module | ACCEPT |
| B12 guidance is governed | `docs/reference/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_STANDARD_2026-06-16.md` | `## Dispatch Manifest Scope Discipline` | `B12` | finding standard | ACCEPT |
| AOT-T3 is queued as machine-check hardening | `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md` | `Cross-Lane Queued Follow-Up` | `AOT-T3` | finding roadmap | ACCEPT |

## Current Runtime Freshness Verification

Runtime freshness is `N/A with reason`: this work order changes governance
checker/test code and governed Markdown only. It does not change product
runtime, model routing, provider adapter behavior, public-sync content,
interlock registry data, or live governance behavior.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| Ship AOT-T3 after operator selection | Purpose / Scope | completion review | pre-closure gate | PASS |
| Keep B11 documentation-only | Scope / Claim Boundary | roadmap and completion | closure diff gate | PASS |
| Preserve AOT-T2 manifest behavior | Acceptance Criteria | focused tests | unittest suite | PASS |
| Do not open AHB-T2 | Forbidden scope | AHB roadmap wording | closure diff gate | PASS |

## Worker Autonomy / No-Question Rule

Codex proceeds autonomously for allowed-scope checker/test/docs repairs and gate
reruns. Escalation is reserved for scope expansion, AHB-T2 ratification,
public-sync, live/provider proof, runtime/product mutation, secrets/quota,
forbidden paths, destructive actions, or claim-boundary changes.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: patch the existing AOT checker, focused AOT
tests, and AOT standard for B12 dispatch manifest scope discipline.

Protected paths:

- governance/compat/check_agent_operation_trace.py
- governance/compat/test_check_agent_operation_trace.py
- docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md

Operator authorization: operator selected AOT-T3 on 2026-06-16 after asking
which path was faster.

Rollback boundary: revert only AOT-T3 changed files if rejected; do not revert
AHB-T1, AHB-T1A, PLCS, or FPRC closure commits.

## Write Ownership

Owned files:

- `governance/compat/check_agent_operation_trace.py`
- `governance/compat/test_check_agent_operation_trace.py`
- `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`
- `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md`
- `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`
- `docs/baselines/CVF_GC018_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_2026-06-16.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_FOR_CODEX_2026-06-16.md`
- `docs/reviews/CVF_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_COMPLETION_2026-06-16.md`

Forbidden paths:

- `EXTENSIONS/**`
- `CVF_SESSION/**` in material commit
- `CVF_SESSION_MEMORY.md` in material commit
- `AGENT_HANDOFF*.md` in material commit
- public-sync clone
- provider-local memory files

## Execution Plan

1. Add focused checker helpers for dispatch-work-order future execution paths.
2. Add AOT-T3 tests for the compliant and violating B12 cases.
3. Update AOT standard and roadmaps.
4. Create completion evidence.
5. Run focused tests and governance gates.
6. Commit material range, then perform session sync if next move changes.

## Acceptance Criteria

| Criterion | Required evidence |
|---|---|
| Future paths in `Write Ownership` remain valid | focused passing test |
| Future paths in dispatch `Expected manifest` fail | focused `DISPATCH_SCOPE_VIOLATION` test |
| AOT-T2 behavior preserved | full AOT unittest suite |
| Standard updated | AOT standard AOT-T3 section |
| Roadmaps updated | finding roadmap and AHB roadmap |
| Completion filed | AOT-T3 completion review |

Fail conditions:

| Fail condition | Return action |
|---|---|
| Checker requires every ownership path to appear in dispatch manifest | repair parser/scope rule |
| Existing manifest delta tests regress | repair before closure |
| AHB-T2 is opened | stop and revert that scope |
| Runtime/product/public-sync/provider behavior is changed | stop and split new authorization |

## Review Gate

Closure may proceed only after focused tests, AOT checker self-run, pre-closure
autorun, and closure steward preflight pass on the material range.

## Evidence Requirements

Required evidence:

- focused unittest result for `governance.compat.test_check_agent_operation_trace`;
- AOT checker self-run on `e509aa4d..HEAD`;
- `git diff --check`;
- pre-closure autorun gate on `e509aa4d..HEAD`;
- closure steward preflight on `e509aa4d..HEAD`;
- committed diff and clean worktree after material commit.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | `docs/baselines/CVF_GC018_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_FOR_CODEX_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_COMPLETION_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | finding roadmap AOT-T3 row | `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason: no registry edit authorized in this checker cleanup | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown edit authorized in this checker cleanup | N/A | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence | N/A | N/A with reason |
| System loop interlock | N/A with reason: no interlock edit | N/A | N/A with reason |
| Session continuity | N/A with reason: follows material commit if next move changes | N/A | N/A with reason |

## Operator Checkpoint

Operator checkpoint is required only if this work needs scope expansion, AHB-T2
ratification, public-sync, live/provider proof, runtime/product mutation,
secrets/quota, forbidden paths, destructive actions, or claim-boundary changes.

## Closure Checklist

| Closure item | Disposition |
|---|---|
| Acceptance criteria satisfied | PASS |
| Focused tests run | PASS |
| AOT checker self-run | PASS pending final gate record |
| `git diff --check` run | PASS |
| Pre-closure autorun gate | PASS pending final gate record |
| Closure steward preflight | PASS pending final gate record |
| AHB-T2 remains unopened | PASS |
| Public export disposition recorded | PASS |

## Return-To-Orchestrator Conditions

Return without closure if focused tests regress, the AOT checker cannot preserve
AOT-T2 behavior, structural gates require scope outside this work order, AHB-T2
ratification becomes necessary, public-sync/live/provider/runtime work becomes
necessary, or the material changed set exceeds Write Ownership.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 AOT-T3 dispatch manifest scope check |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, unittest, governance gates |
| Target paths | `governance/compat/check_agent_operation_trace.py`; `governance/compat/test_check_agent_operation_trace.py`; `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`; `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/baselines/CVF_GC018_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_FOR_CODEX_2026-06-16.md`; `docs/reviews/CVF_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_COMPLETION_2026-06-16.md` |
| Allowed scope source | operator instruction plus AOT-T3 GC-018 |
| Before status evidence | base `e509aa4d`; clean worktree |
| After status evidence | pending material commit |
| Diff evidence | `git diff --name-status e509aa4d..HEAD` |
| Approval boundary | B12 cleanup only |
| Claim boundary | no AHB-T2/runtime/public/provider behavior claim |
| Agent type | Codex |
| Invocation ID | `aot-t3-dispatch-manifest-scope-check-codex-2026-06-16` |
| Expected manifest | `governance/compat/check_agent_operation_trace.py`; `governance/compat/test_check_agent_operation_trace.py`; `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`; `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/baselines/CVF_GC018_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_FOR_CODEX_2026-06-16.md`; `docs/reviews/CVF_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_COMPLETION_2026-06-16.md` |
| Actual changed set | `governance/compat/check_agent_operation_trace.py`; `governance/compat/test_check_agent_operation_trace.py`; `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md`; `docs/roadmaps/CVF_FINDING_PROPAGATION_AND_ROOT_CAUSE_GROUPING_ROADMAP_2026-06-16.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/baselines/CVF_GC018_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_FOR_CODEX_2026-06-16.md`; `docs/reviews/CVF_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_COMPLETION_2026-06-16.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening. No public-sync batch is
authorized.

## Claim Boundary

AOT-T3 closes only the B12 dispatch manifest scope checker gap. It does not
open AHB-T2, implement unified handoff contract enforcement, mutate runtime or
provider behavior, change public content, or claim production/public readiness.
