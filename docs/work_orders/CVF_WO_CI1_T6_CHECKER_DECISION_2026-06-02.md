# CVF Work Order - CI1-T6 Checker Decision

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

docType: work_order

Date: 2026-06-02

dispatchBaseHead: `0808aa8d`

executionBaseHead: `0808aa8d`

## Purpose

Evaluate the six normalization gaps from CI1-T5 and return a structured
per-gap decision that determines whether each gap requires a structural machine
checker, a written standard/vocabulary rule, documentation only, or no action.
Output clears the CI1-T7 gate or holds it pending further work.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-02 sequential CI1 continuation | ACCEPT |
| CI1-T6 GC-018 | `docs/baselines/CVF_GC018_CI1_T6_CHECKER_DECISION_2026-06-02.md` | ACCEPT |
| CI1 roadmap | `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | ACCEPT |
| T5 completion | `docs/reviews/CVF_CI1_T5_CLASSIFICATION_SAMPLING_PROTOCOL_COMPLETION_2026-06-02.md` | ACCEPT |
| T5 results JSON | `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json` | ACCEPT |
| GC-052 registry | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch T6 after T5 closure and reviewer commit | no worker implementation |
| Worker | produce decision artifact, work order, GC-052 route, completion review | read-only evaluation; no checker code; WORKER_MUST_NOT_COMMIT |
| Reviewer | verify decision table completeness, allowed values, CI1-T7 gate | reject missing rows or BLOCKED without evidence |

## Scope

Allowed scope:

- read `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json`;
- read `docs/reviews/CVF_CI1_T5_CLASSIFICATION_SAMPLING_PROTOCOL_COMPLETION_2026-06-02.md`;
- read `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`;
- read `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md`;
- create `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md`;
- create `docs/baselines/CVF_GC018_CI1_T6_CHECKER_DECISION_2026-06-02.md`;
- create `docs/work_orders/CVF_WO_CI1_T6_CHECKER_DECISION_2026-06-02.md` (this file);
- update `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`
  (add `classification-sampling-to-checker-decision` route only);
- create `docs/reviews/CVF_CI1_T6_CHECKER_DECISION_COMPLETION_2026-06-02.md`;
- update `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md`
  CI1-T6 row status only;
- repair allowed-scope Markdown, JSON, interlock, and dispatch-quality defects.

Forbidden scope:

- implementing any Python checker, TypeScript guard, or test file;
- editing `governance/compat/`, `governance/toolkit/`, hook chains, guard docs,
  session front doors, active handoff, or state registry;
- enumerating or scanning any new legacy root or sibling folder;
- modifying runtime source, LPCI UI/API, provider calls, live proof,
  public-sync, commit, or push;
- claiming universal semantic coverage, legal correctness, production
  readiness, hosted readiness, or public readiness.

Risk ceiling: R1 private read-only evaluation and documentation output.

## Write Ownership

| Path | Action | Owner |
| --- | --- | --- |
| `docs/baselines/CVF_GC018_CI1_T6_CHECKER_DECISION_2026-06-02.md` | CREATE | Worker |
| `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` | CREATE | Worker |
| `docs/work_orders/CVF_WO_CI1_T6_CHECKER_DECISION_2026-06-02.md` | CREATE | Worker |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | UPDATE (append route only) | Worker |
| `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json` | UPDATE (NR-03 vocabulary only) | Worker |
| `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | UPDATE (T6/T7 rows + C1.17-C1.19 only) | Worker |
| `docs/reviews/CVF_CI1_T6_CHECKER_DECISION_COMPLETION_2026-06-02.md` | CREATE | Worker |

All other paths are read-only for this work order.

## Required First Reads

1. `docs/baselines/CVF_GC018_CI1_T6_CHECKER_DECISION_2026-06-02.md`
2. `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json`
3. `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md`

## Pre-Flight Checks

| Check | Command | Requirement |
| --- | --- | --- |
| T5 JSON valid | `python -m json.tool docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json` | exit 0 |
| T4 model readable | `python -m json.tool docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json` | exit 0 |
| GC-052 registry valid | `python -m json.tool docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | exit 0 |
| T5 completion review present | `Test-Path docs/reviews/CVF_CI1_T5_CLASSIFICATION_SAMPLING_PROTOCOL_COMPLETION_2026-06-02.md` | true |

## Execution Plan

1. Read CI1-T6 GC-018 baseline.
2. Read `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json` — extract `normalizationGaps` array and `t6Inputs` block.
3. For each of the six gaps, apply three-axis evaluation (enforceability, precondition completeness, risk if unresolved) and assign a decision from the allowed values.
4. Author `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` with per-gap decision table, checker spec stubs (NR-04/NR-05/NR-11), and CI1-T7 gate verdict.
5. Apply the NR-03-vocab vocabulary extension to `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json` (add `CONTROL_PLANE_ADAPTERS` to `normalizationRules[2].valueVocabulary`).
6. Add GC-052 route `classification-sampling-to-checker-decision` to `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`.
7. Update CI1 roadmap T6/T7 rows and add work-plan steps C1.17–C1.19.
8. Author completion review.
9. Run pre-closure gate suite. Record results in completion review.

## Evidence Requirements

Evidence Trace Block (per decision claim):

- each gapId in decision table must cite its source in
  `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json`
  §normalizationGaps or §t6Inputs as `sourceFromT5`;
- NR-03-vocab vocabulary extension must cite T3 classification ledger row C4
  as source;
- CI1-T7 gate verdict must cite the absence of BLOCKED verdicts as evidence.

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| Decision table rows | All 6 T5 gaps have a decision row |
| Allowed decision values | Only values from the GC-018 allowed list |
| blocksCI1T7 populated | YES/NO for every row |
| GC-052 route present | `classification-sampling-to-checker-decision` in registry |
| No checker code written | governance/compat not modified |
| CI1-T7 gate explicit | T7_READY or T7_HOLD stated with rationale |
| Claim boundary present | per GC-018 decision contract |

## Review Gate

Reviewer must verify before committing:

1. Decision table contains exactly six rows — one per T5 normalization gap.
2. All decision values are from the allowed list in the GC-018 baseline.
3. No BLOCKED verdict remains unresolved.
4. CI1-T7 gate verdict is T7_READY or T7_HOLD with explicit rationale.
5. `governance/compat/` directory was not modified.
6. GC-052 route `classification-sampling-to-checker-decision` is present in
   the registry.
7. All modified JSON files are well-formed.

## Closure Checklist

- [x] GC-018 baseline created
- [x] Work order created
- [x] Decision artifact created with per-gap table
- [x] Checker spec stubs recorded (NR-04, NR-05, NR-11)
- [x] NR-03-vocab vocabulary extension applied to T4 model
- [x] GC-052 route added
- [x] CI1 roadmap T6/T7 rows updated
- [x] Completion review created
- [x] All modified JSON valid
- [x] Worker sub-gates PASS; reviewer committed-range pre-closure remains pending per WORKER_MUST_NOT_COMMIT

## Return-To-Orchestrator Conditions

Return to orchestrator when:

- all seven artifacts are created/updated as listed in Write Ownership;
- all JSON artifacts are well-formed;
- CI1-T7 gate verdict is explicit (T7_READY or T7_HOLD);
- completion review contains gate results and finding-to-governance learning
  disposition for all six gaps.

Stop and escalate to operator when:

- a gap cannot be decided with the allowed decision values;
- any T5 evidence is contradictory or missing;
- a request to implement checker code is received.

## Operator Checkpoint

operator.checkpoint.waiver: CI1-T6 is a documentation-only decision tranche.
No operator checkpoint is required before the worker produces the decision
artifacts. Operator intervention is required only if: (a) worker receives a
request to implement checker code, (b) worker needs to access forbidden-scope
paths, or (c) a gap yields a BLOCKED verdict requiring additional evidence that
only the operator can provide.

## Pre-Closure Gates

| Gate | Command | Requirement |
| --- | --- | --- |
| JSON validation | `python -m json.tool docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json` | exit 0 |
| Work order dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base 0808aa8d --head HEAD --enforce` | PASS |
| Markdown structural completeness | `python governance/compat/check_markdown_structural_completeness.py --base 0808aa8d --head HEAD --enforce` | PASS |
| Finding-to-governance learning | `python governance/compat/check_finding_to_governance_learning.py --base 0808aa8d --head HEAD --enforce` | PASS |
| Public export disposition | `python governance/compat/check_public_export_disposition.py --base 0808aa8d --head HEAD --enforce` | PASS |
| Autorun pre-closure | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 0808aa8d --head HEAD` | PASS |

## Commit Mode

WORKER_MUST_NOT_COMMIT

Reviewer/orchestrator performs commit after reviewing all artifacts and gate
results. closureBaseHead is set by the reviewer.

## Worker Autonomy / No-Question Rule

Worker must not escalate to the operator for:

- choosing among the six allowed decision values when T5 evidence is clear;
- deciding whether a gap is DOCUMENTATION_ONLY vs VOCABULARY_EXTENSION_REQUIRED
  when both T5 t6Category and T5 notes support one option;
- choosing T7_READY vs T7_HOLD when no BLOCKED verdict remains.

Worker must escalate to the operator for:

- any request to implement checker code in this tranche;
- any request to modify forbidden-scope files;
- any gap where T5 evidence is genuinely ambiguous and two allowed decisions
  remain equally supported after reading the T5 JSON.

## Claim Boundary

This work order authorizes documentation-only CI1-T6 decision evaluation only.
It does not authorize checker code implementation, runtime source modification,
LPCI UI/API implementation, provider calls, live proof, public-sync, commit,
or push. The NR-03-vocab vocabulary extension to the T4 model JSON is the only
data file write authorized; all governance/compat and governance/toolkit files
are forbidden. T7_READY verdict unlocks CI1-T7 dispatch after reviewer commit
and session front-door update; it does not authorize LPCI implementation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
