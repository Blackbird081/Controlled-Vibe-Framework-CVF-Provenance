# CVF Agent Work Order - EARC-T3B External Absorption Table Checker

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-18

docType: work_order

Batch ID: EARC-T3B

Owner: Codex

Worker: Codex

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `40f630a0`

executionBaseHead: `40f630a0`

closureBaseHead: `40f630a0`

rawMemoryReleased: false

## Dispatch Prompt Envelope

Role: Codex implementer/reviewer/closer

Canonical packet: `docs/baselines/CVF_GC018_EARC_T3B_EXTERNAL_ABSORPTION_TABLE_CHECKER_2026-06-18.md`

Commit mode: WORKER_MAY_COMMIT

executionBaseHead: `40f630a0`

Current-time notes: 2026-06-18; EARC-T3A is closed and EARC-T3B is the next unheld EARC foundation tranche.

Do-not-misread notes: do not open public-sync, MCP implementation, provider/live calls, workspace runtime mutation, raw package import, retroactive historical cleanup, or readiness claims.

Required first actions: implement the range-aware checker, focused tests, hook/autorun wiring, front-door workflow updates, registry coverage, completion packet, roadmap closure, gates, commit, and session-sync.

Return contract: commit accepted material, run closure gates, sync active session state, and report residual parked EARC-T2/EARC-T4 boundaries.

## Purpose

Convert the EARC-T3 Required Absorption Table from a reusable artifact rule into
a machine-enforced guard for changed external-return absorption reviews.

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one-agent-many-roles: Codex holds dispatcher, implementer, reviewer, closer, and session-sync roles across distinct phases |
| phase | DISPATCH_AUTHORING; EXECUTION; CLOSURE; SESSION_SYNC |
| baseHeadFor(phase) | `dispatchBaseHead=40f630a0`; `executionBaseHead=40f630a0`; `closureBaseHead=40f630a0` |
| changedSetScope(phase) | material EARC-T3B checker hardening changed set only; later session-sync changed set remains separate |
| traceScope(phase, actor) | one Codex Agent Operation Trace Block covers this material batch; session-sync trace is separate if state changes |
| commitOwner(phase) | Codex owns material commit; Codex owns separate session-sync commit after material closure |
| crossBatchIsolation | EARC-T2 public-sync and EARC-T4 MCP/runtime remain parked |
| nextMoveSurfaces | material batch records EARC-T3B closure; separate session sync updates state/front-door/handoff next move |
| Closer designation | Codex is the designated closer for this single-agent/multi-role batch |

## Scope / Target / Owner Boundary

Target: external-agent absorption table checker, tests, hook/autorun wiring, EARC
reference front doors, EARC roadmap, and registry coverage.

Owner boundary: Codex owns this bounded checker hardening tranche. It may update
only EARC-T3B material plus session continuity after material commit.

## Authority Chain

| Level | Artifact | Status |
|---|---|---|
| Operator instruction | Continue the defined EARC roadmap and make the Required Absorption Table guard mandatory | ACCEPTED |
| Active session next move | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | EARC-T3B_READY |
| EARC-T3A predecessor | `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_WORKSPACE_LAYER_2026-06-18.md` | PREDECESSOR_SATISFIED |
| GC-018 baseline | `docs/baselines/CVF_GC018_EARC_T3B_EXTERNAL_ABSORPTION_TABLE_CHECKER_2026-06-18.md` | CLOSURE_SATISFIED |

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher | Codex | Author bounded EARC-T3B packet |
| Implementer | Codex | Add checker, tests, and gate wiring |
| Reviewer / closer | Codex | Run gates, close evidence, and commit material |
| Session-sync steward | Codex | Update continuity after material closure |
| Operator | Human operator | Later authorize EARC-T2 public-sync or EARC-T4 MCP/runtime |

## Agent Workspace Design Control Block

| Field | Disposition |
|---|---|
| Workspace purpose | N/A with reason: this tranche hardens external-agent review absorption, not a dedicated agent workspace build. |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| Front door | `docs/reference/external_agent_review/README.md`; `docs/reference/agent_workspace/README.md` remains unchanged except as referenced context. |
| Design standard | `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md` read boundary only; no workspace implementation. |
| Storage class | stable external-agent review reference files plus dated execution evidence. |
| Handoff fields | AHB contract block above owns handoff semantics for this single-agent/multi-role batch. |
| State ownership | No workspace state file changed in this material batch. |
| Guard owner | `governance/compat/check_external_agent_absorption_table.py`; existing workspace guards are not modified. |
| Build boundary | runtime source: no; provider proof: no; public-sync: no; workspace runtime: no; registry edits: yes, GC-051 source entry and generated aggregate only. |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Required Absorption Table columns are canonical for external-agent output consumption. | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | `## Required Absorption Table` | `External item ID`; `External claim summary`; `Source basis`; `CVF verification surface`; `CVF disposition`; `Owner artifact`; `Next action`; `Claim boundary` | external-agent finding absorption workflow | ACCEPT |
| EARC-T3A made the checker candidate ready. | `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_WORKSPACE_LAYER_2026-06-18.md` | `## Checker Readiness Decision` | `CHECKER_READY_FOR_FRESH_GC018` | EARC-T3A absorption pilot review | ACCEPT |
| EARC-T3B is the next unheld checker tranche. | `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md` | `## Tranche Plan` | `EARC-T3B` | EARC roadmap | ACCEPT |
| Autorun phase gates must include governed workflow checks. | `AGENTS.md` | Mandatory Agent Autorun Workflow Control | `run_agent_autorun_workflow_gate.py` | repository agent instructions | ACCEPT |
| Local reviewer/pre-commit/pre-push hook chain is mandatory for governed artifacts. | `AGENTS.md` | Mandatory Agent Autorun Workflow Control | `run_local_governance_hook_chain.py` | repository agent instructions | ACCEPT |

## Required First Reads

| Artifact | Reason |
|---|---|
| `CVF_SESSION_MEMORY.md` | Active front door and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Machine-readable next move |
| `docs/reference/external_agent_review/README.md` | Stable external-agent review front door |
| `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | Required Absorption Table authority |
| `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Handoff contract central core |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Stable foundation folder | `docs/reference/external_agent_review/` remains the canonical external-agent review front door |
| New durable guard path | `governance/compat/check_external_agent_absorption_table.py` |
| New durable test path | `governance/compat/test_check_external_agent_absorption_table.py` |
| Index update | `docs/reference/external_agent_review/README.md` now points to the guard |
| Registry source | `docs/corpus-intelligence/registry/entries/earc-t3b-external-absorption-table-checker.json` |
| Generated aggregate | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` generated from source entries |
| Dated execution evidence | GC-018, work order, and completion stay in normal dated folders |
| Archive policy | No archive movement in this batch |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add and wire a range-aware external-agent
absorption table checker so a repeated cross-agent documentation-only rule
becomes machine enforced.

Protected paths:

- `governance/compat/check_external_agent_absorption_table.py`
- `governance/compat/test_check_external_agent_absorption_table.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`

Operator authorization: user directed Codex to continue the defined roadmap and
make foundational guards mandatory for future agents.

Rollback boundary: revert only the four protected checker/control paths above
and the EARC-T3B dated artifacts/reference updates if this tranche must be
backed out; do not alter parked EARC-T2/EARC-T4 boundaries.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work order action | Disposition |
|---|---|---|
| EARC-T3B adds a range-aware checker for Required Absorption Table. | Add `governance/compat/check_external_agent_absorption_table.py`. | DONE |
| Checker must apply to changed external-return absorption reviews. | Changed-path logic covers committed range, staged changes, and untracked review/audit files. | DONE |
| Avoid keyword false positives on completion prose. | Applicability excludes completion/worker-return paths unless explicit required marker is present. | DONE |
| Make the guard visible to future agents. | Update external-agent review front door and workflow Machine Check section. | DONE |
| Make the guard mandatory. | Wire into autorun common commands and reviewer-fast/pre-commit/pre-push hook chains. | DONE |

## Implementation Requirements

- Add the checker with `--base`, `--head`, and `--enforce` support.
- Require exact Required Absorption Table columns for applicable artifacts.
- Add focused tests for success, missing section, missing column, explicit marker,
  and completion false-positive avoidance.
- Update `docs/reference/external_agent_review/README.md`.
- Update `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`.
- Update the EARC roadmap and corpus registry coverage.

## Pre-Flight Checks

| Check | Required result |
|---|---|
| `git status --short` before work | clean worktree at `40f630a0` |
| `pytest -q governance/compat/test_check_external_agent_absorption_table.py` | PASS |
| `python governance/compat/check_external_agent_absorption_table.py --base 40f630a0 --head HEAD --enforce` | PASS |
| `git diff --check` | PASS |

## Write Ownership

Codex owns only the EARC-T3B changed set listed in the Agent Operation Trace
Block. Session-sync files are not part of the material commit and must be
committed separately after material closure.

## Execution Plan

1. Implement checker and tests.
2. Wire checker into autorun and local hook chains.
3. Update external-agent review front door and workflow.
4. Update roadmap, registry source, generated registry aggregate, and completion
   evidence.
5. Run focused tests and governance gates.
6. Commit material, then perform separate session-sync if next-move surfaces
   change.

## Evidence Requirements

| Evidence | Required disposition |
|---|---|
| Focused checker tests | PASS |
| Checker direct run over `40f630a0..HEAD` | PASS |
| Registry aggregate check | PASS |
| Worker-return fast gate | PASS |
| Commit steward implementation preflight | PASS |
| Pre-commit hook | PASS |

## Review Gate

Codex must review actual changed files, not rely on a worker claim. Any gate
failure within this work order's allowed scope must be repaired before closure.

## Closure Checklist

- [x] Checker implemented.
- [x] Focused tests added.
- [x] Autorun and local hook chain wired.
- [x] External-agent review front door updated.
- [x] EARC roadmap closed for T3B.
- [x] Registry source entry and aggregate updated.
- [x] Public-sync remains parked.
- [x] MCP/runtime remains parked.

## Return-To-Orchestrator Conditions

Return `CLOSED_PASS_BOUNDED` only after material commit and session-sync pass.
Return `BLOCKED` if public-sync, MCP/runtime, provider/live proof, or raw package
import becomes necessary.

## Operator Checkpoint

No operator checkpoint is open for EARC-T3B. EARC-T2 and EARC-T4 remain parked
until explicit authorization.

## Acceptance Criteria

- Focused tests pass.
- Range checker passes on the EARC-T3B changed set.
- `run_worker_return_fast_gate.py` passes.
- Commit steward implementation preflight passes.
- Pre-commit hook passes.
- Material commit and session-sync commit are separated.
- EARC-T2 and EARC-T4 remain parked unless explicitly authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-18 EARC-T3B external absorption table checker |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, pytest, apply_patch |
| Target paths | EARC-T3B GC-018; work order; checker; checker tests; hook chain; autorun gate; external-agent review front door; absorption workflow; EARC roadmap; registry source and aggregate; completion review |
| Allowed scope source | `docs/baselines/CVF_GC018_EARC_T3B_EXTERNAL_ABSORPTION_TABLE_CHECKER_2026-06-18.md` |
| Before status evidence | base `40f630a0`; clean worktree |
| After status evidence | EARC-T3B material closure pending commit |
| Diff evidence | `git diff --name-status 40f630a0..HEAD` |
| Approval boundary | bounded checker hardening only |
| Claim boundary | no public-sync, MCP implementation, provider/live call, workspace runtime mutation, raw package import, retroactive historical cleanup, readiness claim |
| Agent type | Codex implementer/reviewer/closer |
| Invocation ID | `earc-t3b-external-absorption-table-checker-2026-06-18` |
| Expected manifest | `docs/baselines/CVF_GC018_EARC_T3B_EXTERNAL_ABSORPTION_TABLE_CHECKER_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_EARC_T3B_EXTERNAL_ABSORPTION_TABLE_CHECKER_FOR_CODEX_2026-06-18.md`; `governance/compat/check_external_agent_absorption_table.py`; `governance/compat/test_check_external_agent_absorption_table.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `docs/reference/external_agent_review/README.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`; `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md`; `docs/corpus-intelligence/registry/entries/earc-t3b-external-absorption-table-checker.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/reviews/CVF_EARC_T3B_ABSORPTION_TABLE_CHECKER_COMPLETION_2026-06-18.md` |
| Actual changed set | `docs/baselines/CVF_GC018_EARC_T3B_EXTERNAL_ABSORPTION_TABLE_CHECKER_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_EARC_T3B_EXTERNAL_ABSORPTION_TABLE_CHECKER_FOR_CODEX_2026-06-18.md`; `governance/compat/check_external_agent_absorption_table.py`; `governance/compat/test_check_external_agent_absorption_table.py`; `governance/compat/run_local_governance_hook_chain.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `docs/reference/external_agent_review/README.md`; `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md`; `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md`; `docs/corpus-intelligence/registry/entries/earc-t3b-external-absorption-table-checker.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/reviews/CVF_EARC_T3B_ABSORPTION_TABLE_CHECKER_COMPLETION_2026-06-18.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_EARC_T3B_ABSORPTION_TABLE_CHECKER_COMPLETION_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 | `docs/baselines/CVF_GC018_EARC_T3B_EXTERNAL_ABSORPTION_TABLE_CHECKER_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md` | `ROADMAP_T1_T3_T3A_T3B_CLOSED_T2_T4_PARKED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated from source entries | PASS |
| Registry Markdown | BLOCKED with reason: no separate markdown registry is required for this reference family | no path changed | BLOCKED with reason |
| External evidence digest | `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_WORKSPACE_LAYER_2026-06-18.md` | sha256 `15E62063CD0EC1111FB524D3DF20FE49E62A41A981B84D8AB1F314C61DC4770B` | PASS |
| System loop interlock | BLOCKED with reason: no runtime interlock implementation changed | no path changed | BLOCKED with reason |
| Session continuity | separate session-sync follows material commit | active session surfaces update after material commit | N/A with reason |
| Runtime proof | BLOCKED with reason: runtime/provider/MCP proof is out of scope | no runtime proof required | BLOCKED with reason |
| Public export disposition | `DEFERRED_PRIVATE_ONLY` | private provenance checker hardening | PASS |

## Claim Boundary

This work order closes only EARC-T3B checker hardening. It does not publish,
public-sync, implement MCP, run live providers, mutate runtime behavior, or
claim readiness.
