# CVF Work Order - CI1-T7 LPCI Intake Bridge

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-02

dispatchBaseHead: `137ed506`

executionBaseHead: `137ed506`

## Purpose

Synthesize the CI1 corpus-intelligence chain (T2–T6) into a typed LPCI intake
bridge specification that defines what LPCI-T1 must consume, what governance
gates it must satisfy, and what scope remains blocked pending separate
implementation tranches.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-02 sequential CI1 continuation — open CI1-T7 | ACCEPT |
| CI1-T7 GC-018 | `docs/baselines/CVF_GC018_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | ACCEPT |
| CI1 roadmap | `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | ACCEPT |
| CI1-T6 decision | `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` | ACCEPT |
| CI1-T6 completion | `docs/reviews/CVF_CI1_T6_CHECKER_DECISION_COMPLETION_2026-06-02.md` | ACCEPT |
| T4 model | `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json` | ACCEPT |
| T5 results | `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json` | ACCEPT |
| GC-052 registry | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch T7 after T6 closure | no worker implementation |
| Worker | author intake bridge spec, work order, GC-052 route, completion review | doc-only synthesis; no LPCI code; WORKER_MUST_NOT_COMMIT |
| Reviewer | verify intake contract completeness, blocked scope explicit, claim boundary | reject if LPCI implementation scope bleeds in |

## Scope

Allowed scope:

- read `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md`;
- read `docs/reviews/CVF_CI1_T6_CHECKER_DECISION_COMPLETION_2026-06-02.md`;
- read `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`;
- read `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json`;
- read `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md`;
- create `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md`;
- create `docs/baselines/CVF_GC018_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md`;
- create `docs/work_orders/CVF_WO_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` (this file);
- update `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`
  (add `checker-decision-to-lpci-intake` route only);
- create `docs/reviews/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_COMPLETION_2026-06-02.md`;
- update `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md`
  CI1-T7 row and final status only;
- repair allowed-scope Markdown, JSON, interlock, and dispatch-quality defects;
- reviewer/orchestrator session continuity updates after reviewer closure
  (`CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, and
  `AGENT_HANDOFF_V15_2026-05-29.md`) to unlock LPCI roadmap proposal.

Forbidden scope:

- implementing any LPCI chatbot, runtime route, API endpoint, UI component,
  embedding pipeline, or vector database;
- implementing any Python checker, TypeScript guard, or test file;
- editing `governance/compat/`, `governance/toolkit/`, hook chains, guard docs,
  session front doors, active handoff, or state registry (worker only);
- enumerating or scanning any new legacy root or sibling folder;
- calling any provider or performing live proof;
- public-sync, commit, or push.

Risk ceiling: R1 private read-only design synthesis and documentation output.

## Write Ownership

| Path | Action | Owner |
| --- | --- | --- |
| `docs/baselines/CVF_GC018_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | CREATE | Worker |
| `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | CREATE | Worker |
| `docs/work_orders/CVF_WO_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | CREATE | Worker |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | UPDATE (append route only) | Worker |
| `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | UPDATE (T7 row + final status only) | Worker |
| `docs/reviews/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_COMPLETION_2026-06-02.md` | CREATE | Worker |

All other paths are read-only for this work order.

## Required First Reads

1. `docs/baselines/CVF_GC018_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md`
2. `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md`
3. `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`

## Pre-Flight Checks

| Check | Command | Requirement |
| --- | --- | --- |
| T6 decision artifact present | `Test-Path docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` | true |
| T4 model valid | `python -m json.tool docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json` | exit 0 |
| T5 results valid | `python -m json.tool docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json` | exit 0 |
| GC-052 registry valid | `python -m json.tool docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | exit 0 |

## Execution Plan

1. Read CI1-T7 GC-018 baseline.
2. Read `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` — extract decision table, checker stubs, gap acknowledgments, and T7_READY verdict.
3. Read `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json` — extract commonFacets, normalizationRules, claimBoundary.
4. Read `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json` — extract overallVerdict and claimBoundary.
5. Author `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` with: corpus input contract, claim boundary inheritance, gap acknowledgment, governance gate requirements, blocked scope, downstream routing, CI1 chain closure statement.
6. Add GC-052 route `checker-decision-to-lpci-intake`.
7. Update CI1 roadmap T7 row to CLOSED_PASS_BOUNDED and final chain status.
8. Author completion review.
9. Run pre-closure gate suite. Record results.

## Evidence Requirements

Evidence Trace Block:

- corpus input contract must cite T4/T5/T6 artifact paths as named inputs;
- blocked scope must explicitly name LPCI chatbot, runtime route, API endpoint,
  UI, embedding pipeline, and vector database as blocked;
- CI1 chain closure statement must list T1–T7 with CLOSED_PASS_BOUNDED status.

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| Corpus input contract | T4 model, T5 results, T6 decisions named as typed inputs |
| Claim boundary inherited | T4/T5/T6 boundaries explicitly carried into LPCI scope |
| Gap acknowledgment | NR-04/NR-05/NR-11 named with LPCI impact statement |
| Blocked scope explicit | LPCI implementation listed as blocked |
| GC-052 route present | `checker-decision-to-lpci-intake` in registry |
| No runtime artifacts | `governance/compat/` and `EXTENSIONS/` not modified |
| CI1 chain closure stated | T1–T7 all CLOSED_PASS_BOUNDED |
| Claim boundary present | no production, chatbot, or public claim |

## Review Gate

Reviewer must verify before committing:

1. Corpus input contract names T4/T5/T6 as typed inputs.
2. Blocked scope explicitly lists LPCI implementation as blocked.
3. CI1-T7 gate from T6 (`T7_READY`) is acknowledged.
4. No LPCI code, route, or runtime artifact was created.
5. GC-052 route `checker-decision-to-lpci-intake` is present.
6. All modified JSON files are well-formed.

## Closure Checklist

- [x] GC-018 baseline created
- [x] Work order created
- [x] Intake bridge spec created with corpus input contract
- [x] Gap acknowledgment present (NR-04/NR-05/NR-11)
- [x] Blocked scope explicit
- [x] GC-052 route added
- [x] CI1 roadmap T7 row updated
- [x] Completion review created
- [x] All modified JSON valid
- [x] Pre-closure content gates PASS (committed-range run: reviewer responsibility per GC-053)

## Return-To-Orchestrator Conditions

Return to orchestrator when:

- all six artifacts are created/updated as listed in Write Ownership;
- CI1 chain closure statement lists T1–T7 as CLOSED_PASS_BOUNDED;
- blocked scope is explicit and unambiguous;
- completion review contains gate results and F2G disposition.

Stop and escalate to operator when:

- a request to implement LPCI chatbot, route, or runtime code is received;
- any T6 decision is contradicted or ambiguous in the bridge spec.

## Operator Checkpoint

operator.checkpoint.waiver: CI1-T7 is a documentation-only design synthesis
tranche. No operator checkpoint is required before the worker produces the
intake bridge artifacts. Operator intervention is required only if: (a) worker
receives a request to implement LPCI code, (b) worker needs to access
forbidden-scope paths, or (c) the bridge spec cannot be authored without
information only the operator holds.

## Claim Boundary

This work order authorizes documentation-only CI1-T7 design synthesis only.
It does not authorize LPCI chatbot implementation, runtime route authoring,
provider integration, embedding pipeline, vector database, UI components,
live proof, public-sync, commit, or push. LPCI implementation requires a
separate governed roadmap with its own GC-018 after CI1-T7 closes.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
