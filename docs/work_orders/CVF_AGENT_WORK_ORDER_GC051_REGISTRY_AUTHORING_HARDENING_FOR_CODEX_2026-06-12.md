# CVF Agent Work Order - GC-051 Registry Authoring Hardening

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-12

Assigned agent: Codex

executionBaseHead: `ec555c25`

closureBaseHead: `ec555c25`

## Purpose

Execute the bounded GC-051 registry authoring hardening authorized by the
operator.

## Authority Chain

GC-018:

`docs/baselines/CVF_GC018_GC051_REGISTRY_AUTHORING_HARDENING_2026-06-12.md`

Operator instruction: strengthen the CVF foundation before moving to the
Policy_Local use case.

## Objective

Convert GC-051 registry authoring from monolithic manual JSON editing to
per-entry source authoring plus generated aggregate validation.

## Agent Roles

Codex acts as orchestrator, implementer, reviewer, and closer for this small
control-plane tranche. Role separation is artifact-based: GC-018 baseline,
work order, tests, checker output, and completion review are kept distinct.

## Allowed Scope

- `docs/corpus-intelligence/registry/**`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`
- `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`
- `governance/toolkit/05_OPERATION/CVF_GC051_CORPUS_SCAN_REGISTRY_GUARD.md`
- `governance/compat/generate_corpus_scan_registry.py`
- `governance/compat/check_corpus_scan_registry.py`
- `governance/compat/test_generate_corpus_scan_registry.py`
- `AGENTS.md`
- this work order, matching GC-018 baseline, and completion review

## Forbidden Scope

- Do not change registry entry semantics or reclassify corpus status.
- Do not mutate Policy_Local, EC activation, retrieval, OCR, provider/API,
  corpus ingestion, public-sync, readiness claims, memory reinjection,
  high-risk promotion, or autonomous mutation.

## Required First Reads

- `AGENTS.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V18_2026-06-12.md`
- `docs/reference/CVF_CORPUS_SCAN_REGISTRY_STANDARD_2026-06-02.md`
- `governance/toolkit/05_OPERATION/CVF_GC051_CORPUS_SCAN_REGISTRY_GUARD.md`

## Pre-Flight Checks

- Confirm worktree status before edits.
- Confirm current active handoff and next allowed move.
- Run focused generator/checker tests before closure.

## Write Ownership

Write ownership is limited to the paths listed in Allowed Scope. No external
Policy_Local folder, public-sync clone, runtime provider path, or EC activation
surface is owned by this work order.

## Execution Plan

1. Add generator support for bootstrap, generate, and check modes.
2. Bootstrap current aggregate into per-entry source files.
3. Add checker drift validation.
4. Add focused unit tests.
5. Update GC-051 documentation and startup rule.
6. Run reviewer-fast and closure gates.

## Evidence Requirements

- `python governance/compat/generate_corpus_scan_registry.py --check`
- `python governance/compat/check_corpus_scan_registry.py --enforce`
- `python -m unittest governance.compat.test_generate_corpus_scan_registry`
- `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Aggregate registry is current machine front door | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | top-level object | `corpora` | GC-051 registry schema | ACCEPT |
| Checker validates registry entries | `governance/compat/check_corpus_scan_registry.py` | `_validate_entry`, `main` | `_validate_entry` | GC-051 machine guard | ACCEPT |
| Hook chains already run GC-051 checker | `governance/compat/run_local_governance_hook_chain.py` | reviewer-fast/pre-commit command list | `governance/compat/check_corpus_scan_registry.py` | local governance hook chain | ACCEPT |
| Autorun gate already runs GC-051 checker | `governance/compat/run_agent_autorun_workflow_gate.py` | `_common_commands` | `governance/compat/check_corpus_scan_registry.py` | autorun workflow gate | ACCEPT |

## Acceptance Criteria

- Per-entry source files exist for every current `corpora[]` registry entry.
- A generator can bootstrap/generate/check the aggregate.
- `check_corpus_scan_registry.py --enforce` fails if the aggregate drifts from
  source entries.
- Focused unit tests cover filename safety, ordering, source-only field
  stripping, and drift detection.
- GC-051 standard, guard, companion doc, and AGENTS startup rule tell future
  agents to edit entry sources and run the generator instead of hand-editing
  aggregate JSON.

## Verification Evidence

- `python governance/compat/generate_corpus_scan_registry.py --check` PASS.
- `python governance/compat/check_corpus_scan_registry.py --enforce` PASS.
- `python -m unittest governance.compat.test_generate_corpus_scan_registry`
  PASS 4/4.

## Review Gate

Reviewer-fast must pass before closure. Any allowed-scope reviewer-fast failure
must be fixed in this batch.

## Closure Checklist

- [x] Per-entry source files bootstrapped.
- [x] Generator added.
- [x] Checker drift validation added.
- [x] Focused unit tests added.
- [x] Documentation updated.
- [x] Claim boundary preserved.

## Return-To-Orchestrator Conditions

Return to operator only if remediation would require Policy_Local mutation,
public-sync, provider/API use, EC activation, deletion of registry entries, or
semantic reclassification of existing entries.

## Operator Checkpoint

Operator checkpoint satisfied by direct instruction to strengthen the CVF
foundation before moving into the Policy_Local use case.

## Closure Result

Status: `CLOSED_PASS_BOUNDED`.

Completion:

`docs/reviews/CVF_GC051_REGISTRY_AUTHORING_HARDENING_COMPLETION_2026-06-12.md`

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | Status: CLOSED_PASS_BOUNDED | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GC051_REGISTRY_AUTHORING_HARDENING_COMPLETION_2026-06-12.md` | Status: CLOSED_PASS_BOUNDED | PASS |
| Roadmap state | N/A | Direct operator-authorized small control-plane batch; no separate roadmap opened | N/A with reason |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | aggregate drift checker PASS | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | authoring instructions updated | PASS |
| External evidence digest | N/A | no external corpus/provider evidence used | N/A with reason |
| System loop interlock | N/A | no new loop connection claimed | N/A with reason |
| Session continuity | active front door/handoff | sync after material commit if mode changes | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private provenance control-plane hardening. No public-facing
catalog, README, or public-sync update is authorized in this batch.

## Claim Boundary

This work order proves GC-051 registry authoring hardening only. It does not
prove semantic correctness of every registry entry, full scan coverage,
Policy_Local readiness, public readiness, production readiness, OCR/provider
behavior, or autonomous mutation.
