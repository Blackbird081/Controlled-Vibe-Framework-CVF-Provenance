# CVF Work Order - LPCI1-T7 Template Packaging

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-03

dispatchBaseHead: `0c16db92`

executionBaseHead: 0c16db92

closureBaseHead: 0c16db92

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Produce the LPCI1-T7 Template Packaging artifacts. This tranche packages
the LPCI1 MVP governance and intake contracts into reusable templates for
downstream workspace operators. Outputs include a downstream workspace guide,
a corpus intake template (with Vietnamese diacritic normalization section), and
a readiness checklist.

Two operator-specified T7 additions:

1. **Diacritic normalization** for Vietnamese-language corpus at Stage 3
   (fulltext/semantic search): normalizedPath, token, and content-snippet
   normalization rules.
2. **C4/C5 test corpus design**: sample record set designed to trigger
   C4 (freshness warning — amended records) and C5 (conflict notice —
   conflicting records) from the T4 response boundary contract.

This tranche is documentation and template artifact only. No runtime code,
real corpus ingestion, vector search, embedding, or provider calls are created.

---

## Authority Chain

| Authority | Path |
| --- | --- |
| LPCI1 GC-018 | `docs/baselines/CVF_GC018_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_2026-06-02.md` |
| LPCI1 MVP roadmap (T7 row) | `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md` |
| T4 retrieval boundary spec | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` |
| T3 search/filter index spec | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` |
| T2 domain classification spec | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` |
| T1 corpus intake spec | `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md` |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch; T5 and T6 CLOSED_PASS_BOUNDED | no implementation |
| Worker | produce T7 template packaging spec | no runtime code; no corpus ingestion; no completion review; no T6 adversarial execution |
| Reviewer | verify template-only scope and author/own completion review | reject vector/API/UI/provider/corpus-ingestion work |

---

## Dependency Gate — T6 Release Evidence

Per roadmap W7, T7 depends on T6 evaluation reviewed. T6 is now
`CLOSED_PASS_BOUNDED` in this repository before T7 closure.

**T6 dependency state**: T6 = `CLOSED_PASS_BOUNDED`; T7 is authored after the
adversarial evaluation result is available.

**T6 release evidence**:
`docs/reviews/CVF_LPCI1_T6_ADVERSARIAL_EVALUATION_COMPLETION_2026-06-03.md`
and evidence reconciliation commit `9d0deaf4`.

**T6 finding uptake**: T7 incorporates the two T6 template guidance items:
Vietnamese Stage 3 diacritic normalization and C4/C5 test corpus design.

---

## Roadmap Trace

| Roadmap | Tranche row | Status update |
| --- | --- | --- |
| LPCI1 MVP roadmap | W7 / LPCI1-T7 Template packaging | PROPOSED → CLOSED_PASS_BOUNDED |

---

## Roadmap-To-Work-Order Trace Matrix

| Roadmap path | Roadmap tranche | Work order tranche | Mapped output | Verification |
| --- | --- | --- | --- | --- |
| `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md` | W7 / LPCI1-T7 Template packaging | `CVF_WO_LPCI1_T7_TEMPLATE_PACKAGING_2026-06-03.md` | `docs/reference/CVF_LPCI1_T7_TEMPLATE_PACKAGING_SPEC_2026-06-03.md` | roadmap W7 row; T6 CLOSED_PASS_BOUNDED release evidence |

---

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `EXISTS: NR-05 normalizedPath algorithm` | `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md` | `## NR-05 normalizedPath Adoption` | `normalizedPath` | `LPCI1-T1 corpus intake spec` | ACCEPT |
| `EXISTS: C4 freshness warning obligation` | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | `### Rule A2 — Freshness Obligation` | `freshness_flag` | `LPCI1-T4 retrieval boundary contract` | ACCEPT |
| `EXISTS: C5 conflict obligation` | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | `### Rule A3 — Conflict Obligation` | `conflict_flag` | `LPCI1-T4 retrieval boundary contract` | ACCEPT |
| `EXISTS: Stage 3 fulltext search contract` | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` | `## Query Filter Contract / Stage 3` | `titleSnippet`, `contentSnippet` | `LPCI1-T3 query filter contract` | ACCEPT |
| `EXISTS: answerClass decision matrix` | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | `## Classification Decision Matrix` | `answerClass` | `LPCI1-T2 domain classification scheme` | ACCEPT |
| `EXISTS: AuditReceipt schema` | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | `## AuditReceipt Schema` | `AuditReceipt` | `LPCI1-T4 retrieval boundary spec` | ACCEPT |
| `EXISTS: GC-051 corpus registry path` | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | exists in repo | `CVF_CORPUS_SCAN_REGISTRY.json` | `GC-051 corpus scan registry` | ACCEPT |

---

## Write Ownership

| Path | Action | Notes |
| --- | --- | --- |
| `docs/reference/CVF_LPCI1_T7_TEMPLATE_PACKAGING_SPEC_2026-06-03.md` | CREATE | primary T7 output; downstream guide, intake template, readiness checklist, diacritic normalization, C4/C5 test corpus design |
| `docs/reviews/CVF_LPCI1_T7_TEMPLATE_PACKAGING_COMPLETION_2026-06-03.md` | CREATE | T7 closure review |
| `docs/work_orders/CVF_WO_LPCI1_T7_TEMPLATE_PACKAGING_2026-06-03.md` | UPDATE | capture heads; close |

---

## Allowed Scope

- Author T7 template packaging specification (documentation artifact).
- Define downstream workspace guide (how another operator adopts LPCI1).
- Define corpus intake template (intake checklist with diacritic normalization).
- Define readiness checklist (go/no-go criteria before T5 deployment).
- Define diacritic normalization rules for Vietnamese corpus at Stage 3.
- Design C4/C5 test corpus: sample records triggering freshness warning (amended)
  and conflict notice (conflicting authority/date).
- Return T7 spec to reviewer for completion review.
- Update this work order.

---

## Forbidden Scope

- No runtime code files of any kind.
- No real corpus ingestion, indexing, or GC-051 registration.
- No vector store, embedding, or semantic index implementation.
- No UI components, API route handlers, or database schema files.
- No provider calls or live API key usage.
- No T6 adversarial evaluation execution.

---

## Required First Reads

1. `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` — C4/C5 response boundary obligations
2. `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` — Stage 3 fulltext search, index fields
3. `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` — decision matrix, documentType, jurisdiction
4. `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md` — NR-05, NR-04, NR-11 intake obligations

---

## Pre-Flight Checks

1. Confirm T4 completion review CLOSED_PASS_BOUNDED at `5143267f`.
2. Confirm T4 retrieval boundary spec ACTIVE.
3. Confirm roadmap T5 status CLOSED_PASS_BOUNDED (confirmed via roadmap status field).
4. Confirm T6 CLOSED_PASS_BOUNDED release evidence.
5. Confirm `executionBaseHead` captured.

All pre-flight checks confirmed at execution.

---

## Execution Plan

Steps completed by worker in this session:

1. Captured `executionBaseHead: 0c16db92`.
2. Read T1–T4 specs.
3. Authored `docs/reference/CVF_LPCI1_T7_TEMPLATE_PACKAGING_SPEC_2026-06-03.md`.
4. Authored `docs/reviews/CVF_LPCI1_T7_TEMPLATE_PACKAGING_COMPLETION_2026-06-03.md`.
5. Updated this work order to `CLOSED_PASS_BOUNDED`.
6. All governance gates: COMPLIANT.

---

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| Downstream workspace guide present | how to adopt LPCI1 in a new workspace |
| Corpus intake template present | intake checklist with diacritic normalization |
| Vietnamese diacritic normalization defined | Stage 3 normalization rules for Vietnamese corpus |
| Readiness checklist present | go/no-go criteria before T5 deployment |
| C4/C5 test corpus designed | sample records triggering freshness warning and conflict notice |
| No runtime artifacts | zero runtime/product executable files |
| All governance gates PASS | autorun gate COMPLIANT |

---

## Evidence Requirements

| Evidence type | Required path |
| --- | --- |
| T7 spec | `docs/reference/CVF_LPCI1_T7_TEMPLATE_PACKAGING_SPEC_2026-06-03.md` |
| T7 completion review | `docs/reviews/CVF_LPCI1_T7_TEMPLATE_PACKAGING_COMPLETION_2026-06-03.md` |
| executionBaseHead | `0c16db92` |
| closureBaseHead | `0c16db92` |

---

## Review Gate

Reviewer confirms:

- [x] T7 spec is documentation only; no runtime code.
- [x] Diacritic normalization rules present and Stage 3 scoped.
- [x] C4/C5 test corpus design covers amended and conflicting records.
- [x] Downstream guide and readiness checklist complete.
- [x] T6 closure evidence noted; T7 incorporates T6 findings.
- [x] All governance gates PASS.

---

## Closure Checklist

- [x] `executionBaseHead` recorded.
- [x] T7 spec exists and is structurally complete.
- [x] T7 completion review exists and is structurally complete.
- [x] Status updated to `CLOSED_PASS_BOUNDED`.
- [x] `closureBaseHead` recorded.
- [x] All governance gates PASS.
- [x] Operator/reviewer commits; worker does NOT commit.

---

## Return Conditions

Worker must STOP and return to orchestrator if:

- Any runtime code file is required.
- A real legal corpus must be processed.
- T6 adversarial evaluation results are needed to define the template.

---

## Operator Checkpoint

Worker must pause if the diacritic normalization rules introduce a new NR
standard that conflicts with NR-05 or require a new dedicated checker.

---

## Required Gates

| Gate | Command |
| --- | --- |
| markdown structural completeness | `python governance/compat/check_markdown_structural_completeness.py --base 0c16db92 --head HEAD --enforce` |
| work-order dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base 0c16db92 --head HEAD --enforce` |
| finding-to-governance learning | `python governance/compat/check_finding_to_governance_learning.py --base 0c16db92 --head HEAD --enforce` |
| public export disposition | `python governance/compat/check_public_export_disposition.py --base 0c16db92 --head HEAD --enforce` |
| pre-implementation autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 0c16db92 --head HEAD` |

---

## Worker Autonomy / No-Question Rule

Worker may proceed without further operator approval for all steps in this
work order, provided:

- all outputs are documentation/template artifacts only;
- no runtime artifacts are created;
- all governance gates pass.

---

## Claim Boundary

This work order claims authorization to author LPCI1-T7 template packaging
specification and reviewer-owned completion review; no runtime implementation,
corpus ingestion, or T6 adversarial evaluation execution.

---

## Finding-To-Governance Learning Disposition

Defect class: `RULE_GAP` — no LPCI1-T7 template packaging work order or
specification existed before this dispatch

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Disposition: `RULE_ADDED` — LPCI1-T7 work order created and executed; template
packaging spec and completion review authored with diacritic normalization and
C4/C5 test corpus design

Next control action: `CLOSED` — T6 is already CLOSED_PASS_BOUNDED and T7
incorporates the T6 template guidance items

Runtime/provider/cost learning: `N/A_WITH_REASON`

Reason: documentation and template artifact only; no provider calls, runtime
changes, or cost events.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: work order references private internal governance chain.

Public-sync boundary: no artifacts from this batch are queued for public-sync.
