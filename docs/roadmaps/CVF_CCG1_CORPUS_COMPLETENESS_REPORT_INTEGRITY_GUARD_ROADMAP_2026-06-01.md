# CVF CCG-1 Corpus Completeness And Report Integrity Guard Roadmap

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-01

## Purpose

Deliver a general machine-enforced corpus-completeness control so an agent
cannot publish a complete-sounding report from a silently incomplete project
source set.

## Scope / Target / Owner Boundary

Target contract: `cvf.corpusCompletenessReportIntegrity.ccg1.v1`.

Allowed scope:

- general corpus evidence standard and `GC-047` guard;
- compatibility checker plus focused tests;
- autorun, local hook, and documentation-CI wiring;
- agent front-door, GC-018 template, control-matrix, policy, README, KB,
  session-state, audit-accuracy, and handoff-continuity updates.

Forbidden scope:

- legacy concept absorption;
- runtime/provider/route/receipt/prompt/memory changes;
- public-sync;
- semantic-understanding proof claims.

## Authorization / Decision

Decision: CLOSED_PASS_BOUNDED.

Operator authorized implementation on 2026-06-01 after confirming that the
control must cover future folder/file-based reporting, extraction, comparison,
and execution tasks, not only CVF legacy absorption.

## Non-Goals

- Do not absorb unread Legacy content in this tranche.
- Do not create runtime file parsers for every document format.
- Do not claim that evidence-shape checks replace adversarial review.
- Do not push public-facing artifacts.

## Work Plan

| Step | Status | Output |
| --- | --- | --- |
| Stage authority packet | PASS | GC-018, roadmap, work order |
| Add standard and operational guard | PASS | reference standard + `GC-047` |
| Implement checker and focused tests | PASS | compat script + tests |
| Wire earliest applicable gates | PASS | autorun + hooks + CI + front doors |
| Repair legacy audit and continuity drift | PASS | corrected counts + current state |
| Verify and close | PASS | focused tests, governance gates, completion review |

## Acceptance Criteria

| Criterion | Required disposition |
| --- | --- |
| Corpus protocol is general, not Legacy-only | PASS |
| Manifest, ledger, reconciliation, drift, traceability, and adversarial verification are required | PASS |
| `COMPLETE_VERIFIED` is blocked when unresolved files remain | PASS |
| Checker is wired into autorun, local hooks, and CI | PASS |
| AGENTS, CLAUDE, GC-018 template, policy, matrix, README, and KB route through `GC-047` | PASS |
| Legacy audit count correction is command-backed | PASS |
| Continuity gate passes after closure sync | PASS |

## Verification / Evidence

```powershell
python -m pytest governance/compat/test_check_corpus_completeness_report_integrity.py -q
python governance/compat/check_corpus_completeness_report_integrity.py --base fe29b4d6 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base fe29b4d6 --head HEAD
```

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| Agent may report from a silently incomplete bounded corpus | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_ADDED` | Add `GC-047`, checker, and earliest gate wiring |
| Legacy-specific wording is too narrow for user project work | `RULE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `RULE_ADDED` | Generalize to folder/file-based corpus tasks |
| Runtime/provider/cost behavior | `DOCUMENTATION_GAP` | `DOCUMENTATION_ONLY_LEARNING` | `N/A_WITH_REASON` - roadmap is repository-governance-only | No runtime/provider/cost control mutation |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening only. Public-sync is outside
this roadmap.

## Claim Boundary

This roadmap delivers report-integrity evidence controls. It does not prove
semantic correctness for every source file and does not absorb Legacy content.

## Closure Decision

Decision: `CLOSED_PASS_BOUNDED`.

Completion review:

`docs/reviews/CVF_CCG1_CORPUS_COMPLETENESS_REPORT_INTEGRITY_GUARD_COMPLETION_2026-06-01.md`
