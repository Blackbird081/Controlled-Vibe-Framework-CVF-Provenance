# CVF GC-018 - CI1-T7 LPCI Intake Bridge

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_IMPLEMENTATION

docType: baseline

Date: 2026-06-02

baseHead: `137ed506`

dispatchBaseHead: `137ed506`

## Purpose

Authorize CI1-T7 to map the CI1 corpus-intelligence chain (T2/T3 scan
packets → T4 cross-corpus index model → T5 sampling results → T6 checker
decisions) into the LPCI product intake specification.

CI1-T7 produces the typed bridge document that defines what LPCI-T1 must
receive as input, what claim boundaries it must respect, and what governance
gates it must satisfy before chatbot implementation begins.

CI1-T7 is a documentation-only design tranche. It does not implement the
LPCI chatbot, any runtime route, any provider call, any UI component, or any
database. LPCI runtime/chatbot implementation remains blocked until CI1-T7
closes with a `CLOSED_PASS_BOUNDED` review.

## Source

- CI1-T6 decision artifact:
  `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md`
- CI1-T6 completion review:
  `docs/reviews/CVF_CI1_T6_CHECKER_DECISION_COMPLETION_2026-06-02.md`
- T4 cross-corpus index model:
  `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`
- T5 sampling results:
  `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json`
- CI1 roadmap:
  `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md`
- GC-052 registry:
  `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`

## Decision

Proceed with a bounded documentation-only tranche that creates:

- `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` — the primary
  intake bridge specification
- `docs/work_orders/CVF_WO_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` — scoped
  work order
- GC-052 route `checker-decision-to-lpci-intake`
- a bounded completion review

No LPCI runtime artifact is written. No chatbot code, route, database, UI, or
provider integration is created in this tranche.

## Scope / Target / Owner Boundary

Worker may:

- read the committed CI1 chain artifacts (T2–T6);
- read the GC-052 registry and CI1 roadmap;
- author the four output artifacts listed above;
- add GC-052 route `checker-decision-to-lpci-intake`;
- update the CI1-T7 roadmap row status only;
- repair allowed-scope documentation and interlock defects.

Worker must not:

- implement any LPCI chatbot, runtime route, API endpoint, UI component,
  database, or embedding pipeline;
- implement any Python checker, TypeScript guard, or test file;
- edit `governance/compat/`, `governance/toolkit/`, hook chains, guard docs,
  session front doors, active handoff, or state registry;
- enumerate or scan any new legacy root or sibling folder;
- call any provider or perform any live proof;
- public-sync, commit, or push.

Risk ceiling: R1 read-only design synthesis and private documentation output.

## Intake Bridge Contract

The bridge document must specify:

| Section | Requirement |
| --- | --- |
| Corpus input contract | Which CI1 artifacts LPCI-T1 must consume and in what form |
| Claim boundary inheritance | Which CI1 claim boundaries carry forward into LPCI |
| Gap acknowledgment | Which T6 deferred gaps (NR-04/NR-05/NR-11) LPCI-T1 must acknowledge |
| Governance gate requirements | Which CVF gates LPCI-T1 must satisfy before implementation |
| Blocked scope | What LPCI-T1 must NOT implement without additional tranches |
| Downstream routing | How LPCI-T1 connects back to CVF governance after intake |
| CI1 chain closure statement | Explicit statement that CI1-T1 through CI1-T7 are closed |

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| Corpus input contract present | T4 model, T5 results, T6 decisions as named inputs |
| Claim boundary inherited | T4/T5/T6 claim boundaries explicitly carried into LPCI scope |
| Gap acknowledgment present | NR-04/NR-05/NR-11 deferred gaps named with LPCI impact |
| Blocked scope explicit | LPCI runtime/chatbot blocked until separate governed roadmap |
| GC-052 route added | `checker-decision-to-lpci-intake` present |
| No runtime artifacts | no TS, py, or test files created |
| CI1 chain closure stated | all T1–T7 listed as CLOSED_PASS_BOUNDED |
| Claim boundary present | no production, runtime, chatbot, or public claim |

## Source Verification Table

| Token | Verified path or symbol |
| --- | --- |
| `CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` | `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` |
| `CVF_CROSS_CORPUS_INDEX_MODEL.json` | `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json` |
| `CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json` | `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json` |
| `CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` |
| `CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` |

## Evidence

The following evidence is required before the reviewer may commit CI1-T7 artifacts:

| Evidence | Requirement |
| --- | --- |
| Corpus input contract present | T4/T5/T6 artifacts named as typed inputs |
| Blocked scope explicit | LPCI runtime implementation listed as blocked |
| GC-052 route valid | `checker-decision-to-lpci-intake` in registry |
| No runtime artifacts | `governance/compat/` and `EXTENSIONS/` not modified |
| Pre-closure gates PASS | all content-checking autorun gates PASS over committed range |

## Claim Boundary

This baseline authorizes CI1-T7 documentation-only design synthesis only.
It does not authorize LPCI chatbot implementation, runtime route authoring,
provider integration, embedding pipeline, vector database, UI components,
live proof, public-sync, commit, or push. LPCI implementation requires a
separate governed roadmap with its own GC-018 baseline after CI1-T7 closes.

## Commit Mode

WORKER_MUST_NOT_COMMIT

Reviewer/orchestrator performs commit after reviewing all artifacts and gate
results. closureBaseHead is set by the reviewer.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
