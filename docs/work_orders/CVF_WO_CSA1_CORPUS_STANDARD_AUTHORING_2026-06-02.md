# CVF Work Order - CSA1 Corpus Standard Authoring (NR-05 / NR-11)

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-02

dispatchBaseHead: `8e7d1770`

executionBaseHead: `8e7d1770`

closureBaseHead: TBD — set by the committing session after gate PASS.

## Purpose

Author the two written governance standards that CI1-T6 marked
`STANDARD_REQUIRED_FIRST`: the NR-05 CVF Corpus Path Normalization Algorithm
and the NR-11 canonical disposition merge rule. These standards are the
precondition that unblocks the deferred NR-05/NR-11 checker spec stubs and are
inherited obligations for any future LPCI ingest/query/classification work.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-02 selection: NR-05/NR-11 standard authoring as next tranche | ACCEPT |
| CSA1 GC-018 | `docs/baselines/CVF_GC018_CSA1_CORPUS_STANDARD_AUTHORING_2026-06-02.md` | ACCEPT |
| CI1-T6 decision | `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` | ACCEPT |
| CI1-T7 intake bridge | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | ACCEPT |
| T4 model | `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch CSA1 after CI1 chain closure | no runtime/checker work |
| Worker | author NR-05 standard + NR-11 merge rule + completion review | doc-only; no checker code |
| Reviewer | verify standards contract, checker-readiness notes, claim boundary | reject runtime/checker scope bleed |

## Scope

Allowed scope:

- read `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md`;
- read `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md`;
- read `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`;
- read `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md`;
- read `docs/reference/CVF_CORPUS_INTELLIGENCE_READINESS_PACKET_TEMPLATE_2026-06-02.md`;
- create `docs/reference/CVF_CORPUS_PATH_NORMALIZATION_ALGORITHM_STANDARD_2026-06-02.md`;
- add a bounded NR-11 disposition merge rule section to
  `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md`;
- create `docs/baselines/CVF_GC018_CSA1_CORPUS_STANDARD_AUTHORING_2026-06-02.md` (done);
- create `docs/work_orders/CVF_WO_CSA1_CORPUS_STANDARD_AUTHORING_2026-06-02.md` (this file);
- create `docs/reviews/CVF_CSA1_CORPUS_STANDARD_AUTHORING_COMPLETION_2026-06-02.md`;
- repair allowed-scope Markdown defects;
- dedicated session-sync continuity updates after dispatch and closure, limited to
  `CVF_SESSION_MEMORY.md`,
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`,
  `AGENT_HANDOFF_V15_2026-05-29.md`,
  `docs/reviews/CVF_CSA1_DISPATCH_SESSION_SYNC_AUTHORIZATION_2026-06-02.md`, and
  `docs/reviews/CVF_CSA1_CLOSURE_SESSION_SYNC_AUTHORIZATION_2026-06-02.md`.

Forbidden scope:

- implementing any Python checker, TypeScript guard, or test file;
- editing `governance/compat/`, `governance/toolkit/`, hook chains, guard docs;
- implementing any LPCI component, runtime, provider call, or live proof;
- enumerating or scanning any new legacy root or sibling folder;
- modifying the T4 model JSON (NR-05/NR-11 vocabulary already present);
- public-sync.

Risk ceiling: R1 documentation-only standards authoring.

## Write Ownership

| Path | Action | Owner |
| --- | --- | --- |
| `docs/baselines/CVF_GC018_CSA1_CORPUS_STANDARD_AUTHORING_2026-06-02.md` | CREATE | Worker |
| `docs/work_orders/CVF_WO_CSA1_CORPUS_STANDARD_AUTHORING_2026-06-02.md` | CREATE | Worker |
| `docs/reference/CVF_CORPUS_PATH_NORMALIZATION_ALGORITHM_STANDARD_2026-06-02.md` | CREATE | Worker |
| `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | UPDATE (add NR-11 merge rule section only) | Worker |
| `docs/reviews/CVF_CSA1_CORPUS_STANDARD_AUTHORING_COMPLETION_2026-06-02.md` | CREATE | Worker |

All other paths are read-only for this work order.

## Required First Reads

1. `docs/baselines/CVF_GC018_CSA1_CORPUS_STANDARD_AUTHORING_2026-06-02.md`
2. `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md`
3. `docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json`

## Pre-Flight Checks

| Check | Command | Requirement |
| --- | --- | --- |
| T6 decision present | `Test-Path docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` | true |
| Classification standard present | `Test-Path docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | true |
| T4 model valid | `python -m json.tool docs/corpus-intelligence/CVF_CROSS_CORPUS_INDEX_MODEL.json` | exit 0 |

## Execution Plan

1. Read CSA1 GC-018 baseline and the CI1-T6 NR-05/NR-11 decision rows.
2. Author `docs/reference/CVF_CORPUS_PATH_NORMALIZATION_ALGORITHM_STANDARD_2026-06-02.md` per the NR-05 standards contract.
3. Add a bounded NR-11 disposition merge rule section to the existing classification standard per the NR-11 standards contract.
4. Cite the matching CI1-T6 checker spec stub as the deferred follow-on in both standards.
5. Author the completion review.
6. Run the pre-closure gate suite; record results.

## Evidence Requirements

Evidence Trace Block:

- NR-05 standard must specify the canonical form (forward-slash, lowercase, no trailing separator, relative to corpus root) cited from CI1-T6 NR-05 decision row;
- NR-11 merge rule must define `ACCEPT_DEFERRED` canonical value with `rawDisposition` preservation cited from CI1-T6 NR-11 decision row;
- both standards must reference the matching CI1-T6 checker spec stub.

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| NR-05 standard created | canonical form + application + edge cases + checker-readiness note |
| NR-11 merge rule added | `ACCEPT_DEFERRED` + `rawDisposition` preservation |
| Checker stubs referenced | both standards cite matching CI1-T6 stub |
| No checker code | `governance/compat/` not modified |
| No runtime artifacts | no TS/py/test files |
| Claim boundary | no checker-enforcement/runtime/LPCI/public claim |

## Review Gate

Reviewer must verify before final closure:

1. NR-05 canonical algorithm is unambiguous and matches the CI1-T6 decision.
2. NR-11 merge rule defines `ACCEPT_DEFERRED` and `rawDisposition`.
3. Both standards reference their deferred checker stub.
4. No checker, runtime, or LPCI artifact was created.
5. Claim boundary present in each standard.

## Closure Checklist

- [x] NR-05 path normalization standard created
- [x] NR-11 disposition merge rule section added
- [x] Both standards cite CI1-T6 checker stubs
- [x] Completion review created
- [x] Pre-closure gates PASS over committed range

## Return-To-Orchestrator Conditions

Return to orchestrator when:

- both standards are authored to the standards contract;
- both reference their deferred checker stub;
- completion review contains gate results and F2G disposition.

Stop and escalate to operator when:

- a request to implement checker code is received;
- the NR-05 algorithm or NR-11 merge value cannot be specified without
  information only the operator holds.

## Operator Checkpoint

operator.checkpoint.waiver: CSA1 is a bounded R1 documentation-only
standards-authoring tranche selected by the operator on 2026-06-02. No
additional operator checkpoint is required before authoring. Operator
intervention is required only for checker-code implementation requests,
forbidden-scope access, or scope expansion.

## Worker Autonomy / No-Question Rule

Worker must not escalate to the operator for:

- choosing exact wording of the NR-05 canonical algorithm when the CI1-T6
  decision row already fixes the form (forward-slash, lowercase, no trailing
  separator, relative to corpus root);
- choosing the NR-11 canonical merge value when CI1-T6 already fixes it as
  `ACCEPT_DEFERRED` with `rawDisposition` preservation;
- repairing allowed-scope Markdown or structural defects to pass gates.

Worker must escalate to the operator for:

- any request to implement checker code in this tranche;
- any request to modify forbidden-scope files;
- any case where the standard cannot be specified without information only the
  operator holds.

## Commit Mode

Commit mode: WORKER_MAY_COMMIT

The dispatching session may author the two standards and commit them as a
single governed batch (R1 documentation-only, no protected/checker/runtime
scope), then perform a dedicated session-sync commit. closureBaseHead is set
after the committed-range pre-closure gate PASS.

## Claim Boundary

This work order authorizes documentation-only standards authoring only. It
does not authorize checker implementation, runtime control changes, LPCI
implementation, provider calls, live proof, or public-sync. The NR-05/NR-11
checker spec stubs remain deferred to a separate checker-implementation
roadmap.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
