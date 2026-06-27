# CVF EARC-T3B Absorption Table Checker Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-18

docType: review

## Purpose

Close EARC-T3B after implementing the range-aware Required Absorption Table
guard for changed external-return absorption reviews.

## Scope / Target / Owner Boundary

Target: checker implementation, tests, hook/autorun wiring, EARC reference
front doors, EARC roadmap, and corpus registry coverage.

Owner boundary: Codex owned the implementation, review, material commit, and
session-sync. Public-sync and MCP/runtime remain held.

## Findings / Position

Position: EARC-T3B successfully promotes the Required Absorption Table from a
documentation-only external-agent absorption rule into a mandatory range-aware
machine guard.

## Risk / Corrective Action

Risk: a broad keyword checker could falsely fail completion prose or unrelated
external-agent references.

Corrective action: checker applicability is path/marker constrained and the
focused tests include a completion-prose false-positive canary.

## Source Authority

| Source | Role |
|---|---|
| `docs/baselines/CVF_GC018_EARC_T3B_EXTERNAL_ABSORPTION_TABLE_CHECKER_2026-06-18.md` | Authorized scope and boundaries |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_EARC_T3B_EXTERNAL_ABSORPTION_TABLE_CHECKER_FOR_CODEX_2026-06-18.md` | Work order trace and acceptance criteria |
| `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | Required table and machine guard authority |
| `docs/reference/external_agent_review/README.md` | Stable front door |
| `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md` | Tranche plan and parked boundaries |

## Delivered Changes

| Artifact | Change |
|---|---|
| `governance/compat/check_external_agent_absorption_table.py` | Added range-aware checker for applicable changed review/audit files. |
| `governance/compat/test_check_external_agent_absorption_table.py` | Added focused canary tests. |
| `governance/compat/run_agent_autorun_workflow_gate.py` | Added checker to common autorun gates. |
| `governance/compat/run_local_governance_hook_chain.py` | Added checker to reviewer-fast, pre-commit, and pre-push lanes. |
| `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | Promoted Machine-Check Candidate to active Machine Check. |
| `docs/reference/external_agent_review/README.md` | Indexed checker path in the external-agent review front door. |
| `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md` | Closed EARC-T3B and removed stale next-candidate text. |
| `docs/corpus-intelligence/registry/entries/earc-t3b-external-absorption-table-checker.json` | Added registry source coverage for the checker tranche. |

## Validation

| Command | Result |
|---|---|
| `pytest -q governance/compat/test_check_external_agent_absorption_table.py` | PASS: 5 focused tests passed |
| `python governance/compat/check_external_agent_absorption_table.py --base 40f630a0 --head HEAD --enforce` | PASS |
| `python governance/compat/generate_corpus_scan_registry.py --check` | PASS |
| `git diff --check` | PASS |
| `python governance/compat/run_worker_return_fast_gate.py` | PASS |
| `python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base 40f630a0 --head HEAD --enforce` | PASS |
| Pre-commit hook | pending material commit |

## Closure Diff Gate

| Requirement | Evidence | Disposition |
|---|---|---|
| Add range-aware checker. | `governance/compat/check_external_agent_absorption_table.py` | PASS |
| Avoid completion-prose false positives. | `test_completion_review_phrase_does_not_trigger` | PASS |
| Require exact table columns. | `REQUIRED_COLUMNS` plus missing-column test | PASS |
| Wire into mandatory gates. | Autorun and hook-chain updates | PASS |
| Keep public-sync and MCP/runtime held. | Roadmap closure note and claim boundary | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_EARC_T3B_EXTERNAL_ABSORPTION_TABLE_CHECKER_FOR_CODEX_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 | `docs/baselines/CVF_GC018_EARC_T3B_EXTERNAL_ABSORPTION_TABLE_CHECKER_2026-06-18.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md` | `ROADMAP_T1_T3_T3A_T3B_CLOSED_T2_T4_PARKED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | generated from source entries | PASS |
| Registry Markdown | BLOCKED with reason: no separate markdown registry is required for this reference family | no path changed | BLOCKED with reason |
| External evidence digest | `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_WORKSPACE_LAYER_2026-06-18.md` | sha256 `15E62063CD0EC1111FB524D3DF20FE49E62A41A981B84D8AB1F314C61DC4770B` | PASS |
| System loop interlock | BLOCKED with reason: no runtime interlock implementation changed | no path changed | BLOCKED with reason |
| Session continuity | separate session-sync follows material commit | active session surfaces update after material commit | N/A with reason |
| Runtime proof | BLOCKED with reason: runtime/provider/MCP proof is out of scope | no runtime proof required | BLOCKED with reason |
| Public export disposition | `DEFERRED_PRIVATE_ONLY` | private provenance checker hardening | PASS |

## Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening. Public-facing updates require
separate public-sync authorization.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-18 EARC-T3B external absorption table checker |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, pytest, apply_patch |
| Target paths | EARC-T3B GC-018; work order; checker; checker tests; hook chain; autorun gate; external-agent review front door; absorption workflow; EARC roadmap; GC-051 registry entry and aggregate; completion review |
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

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Finding | External-agent returns can be acted on without the Required Absorption Table if the rule remains documentation-only. |
| Defect class | `RULE_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `MACHINE_CHECK_ADDED` |
| Governance action | Promoted the EARC-T3 table rule to active checker and stable front-door guidance. |
| Machine-check action | `governance/compat/check_external_agent_absorption_table.py` now runs in autorun and hook chains. |
| Next action | Keep EARC-T2 and EARC-T4 parked until explicit authorization. |
| Runtime/provider/cost learning lane | `N/A_WITH_REASON`: no runtime/provider/cost behavior changed. |

## Epistemic Process Block

### Expected Result / Prediction

The first real absorption pilot should provide enough stable shape to automate
table enforcement without broad keyword false positives.

### Evidence Comparison

The checker can target path and explicit-marker semantics instead of free-form
prose, and the canary tests cover the main false-positive class.

### Contradiction Or Gap Disposition

No contradiction found. Future expansion may broaden applicability only after a
new real packet demonstrates another stable marker.

### Claim Update

EARC external-agent absorption now has both a stable artifact rule and a
mandatory machine guard.

## Claim Boundary

This completion closes checker hardening only. It does not publish, public-sync,
implement MCP, run live providers, mutate runtime behavior, import raw external
packages, reopen history, or claim readiness.
