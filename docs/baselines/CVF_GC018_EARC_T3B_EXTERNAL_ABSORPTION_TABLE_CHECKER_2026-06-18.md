# CVF GC-018 - EARC-T3B External Absorption Table Checker

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-18

docType: baseline

## Purpose

Authorize a bounded machine-check hardening tranche that converts the EARC-T3
Required Absorption Table from workflow guidance into a range-aware guard.

## Scope

In scope:

- add a focused checker for changed external-return absorption reviews;
- add focused tests for pass, missing-table, missing-column, explicit marker,
  and completion-prose false-positive cases;
- wire the checker into autorun and local hook chains;
- update the external-agent review front door and workflow local view;
- update the EARC roadmap and GC-051 corpus registry coverage.

Out of scope:

- public-sync or public repository edits;
- MCP implementation or workspace runtime behavior;
- provider/live calls;
- modifying or importing the raw copied external package;
- reopening historical reviews outside the changed range;
- production, release, public, provider, MCP, workspace, or external-facing
  readiness claims.

## Source Verification

| Claimed item | Source file | Verified section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EARC workflow requires a Required Absorption Table for artifacts that consume external-agent output. | `docs/reference/external_agent_review/CVF_EXTERNAL_AGENT_FINDING_ABSORPTION_WORKFLOW.md` | `## Required Absorption Table` | table columns | external-agent finding absorption workflow | ACCEPT |
| The first real EARC-T3A pilot proved the checker candidate is ready. | `docs/reviews/CVF_EARC_T3A_EXTERNAL_RETURN_ABSORPTION_PILOT_WORKSPACE_LAYER_2026-06-18.md` | `## Checker Readiness Decision` | `CHECKER_READY_FOR_FRESH_GC018` | EARC-T3A absorption pilot review | ACCEPT |
| EARC roadmap lists EARC-T3B as the next checker tranche. | `docs/roadmaps/CVF_EXTERNAL_AGENT_REVIEW_CONTEXT_SYSTEMIZATION_ROADMAP_2026-06-18.md` | `## Tranche Plan` | `EARC-T3B` | EARC roadmap | ACCEPT |
| Autorun phase gates are the governed place for range-aware workflow checks. | `AGENTS.md` | Mandatory Agent Autorun Workflow Control | `run_agent_autorun_workflow_gate.py` | repository agent instructions | ACCEPT |
| Local hook chain is the governed early gate surface for reviewer-fast, pre-commit, and pre-push checks. | `AGENTS.md` | Reviewer fast preflight and local hook chain requirement | `run_local_governance_hook_chain.py` | repository agent instructions | ACCEPT |

## Decision

Proceed with checker hardening. The guard should be narrow enough to avoid
keyword-triggering ordinary completion reviews, but strict for changed
external-return absorption reviews and explicit
`External absorption review: REQUIRED` packets.

## Evidence / Verification

| Evidence | Expected result |
|---|---|
| `pytest -q governance/compat/test_check_external_agent_absorption_table.py` | Focused checker tests pass |
| `python governance/compat/check_external_agent_absorption_table.py --base 40f630a0 --head HEAD --enforce` | Changed absorption-table guard passes |
| `python governance/compat/generate_corpus_scan_registry.py --generate` | Registry aggregate updates from source entries |
| `python governance/compat/generate_corpus_scan_registry.py --check` | Registry aggregate matches sources |
| `git diff --check` | Diff hygiene passes |
| `python governance/compat/run_worker_return_fast_gate.py` | Reviewer-fast checks pass |
| `python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base 40f630a0 --head HEAD --enforce` | Material commit shape is bounded |
| Pre-commit hook | Required local governance checks pass |

## Claim Boundary

This GC-018 authorizes a documentation/checker hardening tranche only. It does
not authorize public-sync, MCP implementation, provider/live calls, workspace
runtime mutation, raw external package import, retroactive historical cleanup,
or readiness claims.

## Work Order

The authorized work order is:

`docs/work_orders/CVF_AGENT_WORK_ORDER_EARC_T3B_EXTERNAL_ABSORPTION_TABLE_CHECKER_FOR_CODEX_2026-06-18.md`
