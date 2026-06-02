# CVF GC-018 - CI1-T6 Checker Decision

Memory class: FULL_RECORD

Status: AUTHORIZED_FOR_IMPLEMENTATION

docType: baseline

Date: 2026-06-02

baseHead: `0808aa8d`

dispatchBaseHead: `0808aa8d`

## Purpose

Authorize CI1-T6 to evaluate the six normalization gaps identified in the
CI1-T5 sampling results and decide, for each gap, whether the gap requires a
structural machine checker, a written standard/vocabulary rule, documentation
only, or no action.

CI1-T6 is a decision artifact, not an implementation tranche. Its output is a
structured decision table that unblocks CI1-T7 (LPCI Intake Bridge). It does
not implement any checker code, runtime indexing, LPCI UI/API, provider calls,
or public-sync.

## Source

- CI1 roadmap:
  `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md`
- T5 machine-readable results:
  `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json`
- T5 completion review:
  `docs/reviews/CVF_CI1_T5_CLASSIFICATION_SAMPLING_PROTOCOL_COMPLETION_2026-06-02.md`
- T4 cross-corpus index model:
  `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`
- CI1-T5 GC-018:
  `docs/baselines/CVF_GC018_CI1_T5_CLASSIFICATION_SAMPLING_PROTOCOL_2026-06-02.md`
- GC-052 registry:
  `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`

## Decision

Proceed with a bounded documentation-only decision tranche that creates:

- `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` — the primary
  decision artifact with per-gap ruling table
- `docs/work_orders/CVF_WO_CI1_T6_CHECKER_DECISION_2026-06-02.md` — the
  scoped work order
- GC-052 route `classification-sampling-to-checker-decision`
- a bounded completion review

No checker code is written in this tranche. Decisions that require a
structural checker produce a spec-stub only within the decision artifact;
checker implementation requires a separate governed roadmap.

## Scope / Target / Owner Boundary

Worker may:

- read the committed T5 results JSON and T5 completion review;
- read the T4 model for cross-reference;
- consult the CI1 roadmap for T6 row status;
- create the four allowed output artifacts listed above;
- add the GC-052 route `classification-sampling-to-checker-decision`;
- update the CI1-T6 roadmap row status only;
- repair allowed-scope documentation and interlock defects.

Worker must not:

- implement any Python checker, TypeScript guard, or test file;
- edit `governance/compat/` or `governance/toolkit/` files unless this
  baseline is explicitly extended by operator instruction;
- modify `governance/compat/check_corpus_intelligence_classification.py`
  or any other checker without a separate guard-maintenance authorization;
- enumerate or scan any new legacy root, sibling folder, or runtime source;
- implement LPCI UI/API, provider calls, live proof, public-sync, commit, or
  push;
- claim universal semantic correctness, legal correctness, production
  readiness, hosted readiness, or public readiness.

Risk ceiling: R1 read-only evaluation and private documentation output.

## Decision Contract

The decision artifact must include a decision table with the following columns
for each of the six T5 gaps:

| Column | Requirement |
| --- | --- |
| gapId | NR-04, NR-05, NR-11, NR-03-vocab, NR-06, NR-07 |
| sourceFromT5 | verbatim gap description from T5 results JSON |
| problem | one-sentence restatement of the governance risk |
| decision | one of the allowed decision values (see below) |
| checkerAction | CHECKER_SPEC_STUB / STANDARD_FIRST / VOCABULARY_EXTENSION / DOCUMENTATION_ENTRY / NONE |
| standardAction | text or NONE |
| downstreamImpact | which downstream component is affected |
| blocksCI1T7 | YES / NO |
| rationale | one-sentence justification |

Allowed decision values:

| Value | Meaning |
| --- | --- |
| STRUCTURAL_CHECK_REQUIRED | gap must be enforced by machine; spec-stub required |
| STANDARD_REQUIRED_FIRST | written standard/algorithm must precede any checker |
| VOCABULARY_EXTENSION_REQUIRED | vocabulary extension required; checker optional after |
| DOCUMENTATION_ONLY | documentation guidance is sufficient; no machine check |
| ACCEPT_NO_ACTION | gap already handled; no new artifact required |
| BLOCKED | cannot decide without additional evidence; must state what is needed |

## CI1-T7 Gate

CI1-T6 must return one of:

- **T7_READY** — all six gaps decided with no BLOCKED verdict; CI1-T7 may
  proceed as LPCI Intake Bridge after the CI1-T6 artifacts are committed.
- **T7_HOLD** — one or more gaps have BLOCKED verdict; CI1-T7 remains locked
  until the block is resolved.

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| Decision table completeness | All six T5 gaps must have a row |
| Allowed decisions only | No undefined decision values in table |
| blocksCI1T7 populated | YES/NO for each row |
| GC-052 route added | `classification-sampling-to-checker-decision` present |
| No checker code written | governance/compat not modified in this tranche |
| No runtime artifacts | no TS, py, or test files created |
| CI1-T7 gate stated | T7_READY or T7_HOLD with rationale |
| Claim boundary present | no production, runtime, LPCI, or public claim |

## Source Verification Table

| Token | Verified path or symbol |
| --- | --- |
| `CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json` | `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json` |
| `normalizationGaps` | `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json` §normalizationGaps |
| `t6Inputs` | `docs/corpus-intelligence/CVF_CI1_T5_CLASSIFICATION_SAMPLING_RESULTS.json` §t6Inputs |
| `CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` |
| `CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` | `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` |

## Evidence

The following evidence is required before the reviewer may commit CI1-T6 artifacts:

| Evidence | Requirement |
| --- | --- |
| Decision table completeness | All 6 T5 gaps present in decision artifact with allowed decision values |
| No BLOCKED verdict | All gaps decided; T7_READY verdict stated |
| GC-052 route present | `classification-sampling-to-checker-decision` in registry |
| JSON validity | `python -m json.tool` exits 0 for all modified JSON artifacts |
| No checker code written | `governance/compat/` not modified in this tranche |
| Pre-closure gates PASS | All 5 autorun gates PASS over committed range |

## Commit Mode

WORKER_MUST_NOT_COMMIT

Worker records all artifacts as uncommitted outputs. Reviewer/orchestrator
performs commit after reviewing the decision table, gate results, and GC-052
route validity.

closureBaseHead: TBD — set by reviewer after gate PASS.

## Claim Boundary

This baseline authorizes CI1-T6 documentation-only decision evaluation only.
It does not authorize checker code implementation, runtime source modification,
LPCI UI/API implementation, provider calls, live proof, public-sync, commit,
or push. The NR-03-vocab vocabulary extension to `CVF_CROSS_CORPUS_INDEX_MODEL.json`
is the only data file write authorized under this baseline; `governance/compat/`
and `governance/toolkit/` files are forbidden. T7_READY verdict unlocks
CI1-T7 dispatch only after reviewer commit and session front-door update.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY — CI1-T6 decision artifacts are private governance
records. No public-sync at this stage.
