# CVF Work Order - LPCI1-T3 Search and Filter Index

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-03

dispatchBaseHead: `1cedefd8`

executionBaseHead: 1cedefd8

closureBaseHead: 1cedefd8

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Produce the LPCI1-T3 Search and Filter Index specification. This tranche
defines the faceted index schema, query filter contract, and negative search
evidence format for LPCI1. These outputs feed the T4 retrieval boundary and T5
chatbot prototype.

This tranche is documentation and specification only. No runtime code, real
corpus indexing, vector store, embedding pipeline, or provider calls are
created.

---

## Authority Chain

| Authority | Path |
| --- | --- |
| LPCI1 GC-018 | `docs/baselines/CVF_GC018_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_2026-06-02.md` |
| LPCI1 MVP roadmap (T3 row) | `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md` |
| T2 domain classification spec | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` |
| T1 architecture | `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` |
| T1 corpus intake spec | `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md` |
| CI2-T3 enforced index model | `docs/corpus-intelligence/CVF_CI2_ENFORCED_CROSS_CORPUS_INDEX_MODEL.json` |

---

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch; T2 closed at `2bef0c56` | no implementation |
| Worker | produce T3 search/filter index spec and completion review | no runtime code; no corpus indexing |
| Reviewer | verify spec-only scope; reject any runtime artifact | reject UI/API/vector/index/provider work |

---

## Dependency Gate

Dependency satisfied. LPCI1-T2 closed at `2bef0c56`.

Release evidence:

- T2 completion review: `docs/reviews/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_COMPLETION_2026-06-03.md` — Status: CLOSED_PASS_BOUNDED at commit `2bef0c56`
- T2 work order: `docs/work_orders/CVF_WO_LPCI1_T2_DOMAIN_CLASSIFICATION_2026-06-03.md` — closureBaseHead: `89d5940f`
- T2 domain classification spec: `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` — Status: ACTIVE

---

## Roadmap Trace

| Roadmap | Tranche row | Status update |
| --- | --- | --- |
| LPCI1 MVP roadmap | W3 / LPCI1-T3 Search and filter index | PROPOSED → IN_PROGRESS upon execution |

---

## Roadmap-To-Work-Order Trace Matrix

| Roadmap path | Roadmap tranche | Work order tranche | Mapped output | Verification |
| --- | --- | --- | --- | --- |
| `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md` | W3 / LPCI1-T3 Search and filter index | `CVF_WO_LPCI1_T3_SEARCH_FILTER_INDEX_2026-06-03.md` | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` | roadmap W3 row; dependency = T2 CLOSED_PASS_BOUNDED at `2bef0c56` |

---

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `EXISTS: answerClass four canonical values` | `docs/corpus-intelligence/CVF_CI2_ENFORCED_CROSS_CORPUS_INDEX_MODEL.json` | `enforcedFields[answerClass].description` | `answerClass` | `CI2 enforced cross-corpus index model` | ACCEPT |
| `EXISTS: dispositionAlias NR-11 rules` | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | `## dispositionAlias Rules (NR-11)` | `dispositionAlias` | `LPCI1-T2 domain classification scheme` | ACCEPT |
| `EXISTS: documentType enum` | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | `## documentType Enum` | `documentType` | `LPCI1-T2 domain classification scheme` | ACCEPT |
| `EXISTS: jurisdiction taxonomy` | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | `## Jurisdiction Taxonomy` | `jurisdiction` | `LPCI1-T2 domain classification scheme` | ACCEPT |
| `EXISTS: sensitivityLevel enum` | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | `## Sensitivity Classification (NR-06)` | `sensitivityLevel` | `LPCI1-T2 domain classification scheme` | ACCEPT |
| `VALUE_SET: knowledgeRegion legal/policy value` | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | `### knowledgeRegion for Legal/Policy Domain` | `knowledgeRegion` | `LPCI1-T2 domain classification scheme` | ACCEPT |
| `EXISTS: Retrieval answer boundary contract` | `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` | `### Answer Boundary Contract` | `answerClass` | `LPCI1-T1 architecture retrieval boundary` | ACCEPT |

---

## Write Ownership

| Path | Action | Notes |
| --- | --- | --- |
| `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` | CREATE | primary T3 output; faceted index schema, query filter contract, negative search evidence format |
| `docs/reviews/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_COMPLETION_2026-06-03.md` | CREATE | T3 closure review |
| `docs/work_orders/CVF_WO_LPCI1_T3_SEARCH_FILTER_INDEX_2026-06-03.md` | UPDATE | capture executionBaseHead and closureBaseHead |

---

## Allowed Scope

- Author the search and filter index specification (documentation artifact).
- Define the faceted index schema: index fields, facet definitions, sort fields.
- Define the query filter contract: filter parameters, filter application rules,
  sensitivity pre-filter, answerClass post-filter.
- Define the negative search evidence format: no-results receipt, filtered-out
  receipt, abstention/escalation audit receipt.
- Author the T3 completion review.
- Update this work order with captured head hashes and checked closure checklist.

---

## Forbidden Scope

- No runtime code files of any kind.
- No real corpus indexing, scanning, or GC-051 registration.
- No vector store, embedding, or semantic index implementation.
- No UI components, API route handlers, or database schema files.
- No provider calls or live API key usage.
- No claim of tested index correctness or production readiness.

---

## Required First Reads

1. `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` — full classification scheme, answerClass criteria, decision matrix
2. `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` — retrieval and answer boundary design, API/UI surface sketch
3. `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md` — inherited gaps, NR-04/NR-05 adoption

---

## Pre-Flight Checks

1. Confirm T2 completion review CLOSED_PASS_BOUNDED.
2. Confirm T2 domain classification spec ACTIVE.
3. Capture `executionBaseHead` via `git rev-parse --short HEAD`.

---

## Execution Plan

### Step 1 — Capture executionBaseHead

```
git rev-parse --short HEAD → record in this work order
```

### Step 2 — Author T3 search and filter index spec

Create `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md`
covering all sections required by the reference structural checker:

- `## Purpose`
- `## Source`
- `## Faceted Index Schema` — index fields, facet definitions, sort fields
- `## Query Filter Contract` — filter parameters and application rules
- `## Negative Search Evidence Format` — no-results, filtered-out, abstention receipts
- `## Requirements`
- `## Enforcement`
- `## Verification`
- `## Non-Goals`
- `## Claim Boundary`
- `## Related`

### Step 3 — Author T3 completion review

Create `docs/reviews/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_COMPLETION_2026-06-03.md`.

### Step 4 — Update this work order

Set `executionBaseHead`, `closureBaseHead`, `Status: CLOSED_PASS_BOUNDED`,
check all closure checklist items.

### Step 5 — Run governance gates

```
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Must exit 0 / COMPLIANT before signaling done.

---

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| T3 spec authored | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` exists and is structurally complete |
| Faceted index schema present | all T2 classification fields mapped to index fields with facet definitions |
| Query filter contract present | filter parameters, sensitivity pre-filter, answerClass post-filter defined |
| Negative search evidence format present | all three receipt types defined |
| No runtime artifacts | zero executable files created |
| All governance gates PASS | autorun pre-implementation gate COMPLIANT |

---

## Evidence Requirements

| Evidence type | Required path |
| --- | --- |
| T3 spec | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` |
| T3 completion review | `docs/reviews/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_COMPLETION_2026-06-03.md` |
| executionBaseHead | captured in this work order |
| closureBaseHead | captured in this work order |

---

## Review Gate

Reviewer confirms:

- [x] T3 spec is documentation only; no runtime code.
- [x] Faceted index schema covers all T2 classification fields.
- [x] Query filter contract consistent with T2 answerClass / dispositionAlias rules.
- [x] Negative search evidence format covers all abstention cases from T2 decision matrix.
- [x] All governance gates PASS.

---

## Closure Checklist

- [x] `executionBaseHead` recorded.
- [x] T3 spec exists and is structurally complete.
- [x] T3 completion review exists and is structurally complete.
- [x] Status updated to `CLOSED_PASS_BOUNDED`.
- [x] `closureBaseHead` recorded.
- [x] All governance gates PASS.
- [x] Operator/reviewer commits; worker does NOT commit.

---

## Return Conditions

Worker must STOP and return to orchestrator if:

- Any runtime code file is required to produce the index spec.
- A real legal corpus must be indexed to define the schema.
- A live vector store or embedding model is required.
- Any live provider call is needed.

---

## Operator Checkpoint

Worker must pause for operator review before final commit if:

- The index spec introduces a new field or facet that conflicts with the CI2-T3
  enforced model or T2 classification scheme.
- A new NR rule or standard is required.

---

## Required Gates

| Gate | Command |
| --- | --- |
| markdown structural completeness | `python governance/compat/check_markdown_structural_completeness.py --base <executionBaseHead> --head HEAD --enforce` |
| work-order dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base <executionBaseHead> --head HEAD --enforce` |
| finding-to-governance learning | `python governance/compat/check_finding_to_governance_learning.py --base <executionBaseHead> --head HEAD --enforce` |
| public export disposition | `python governance/compat/check_public_export_disposition.py --base <executionBaseHead> --head HEAD --enforce` |
| pre-implementation autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` |

---

## Worker Autonomy / No-Question Rule

Worker may proceed without further operator approval for all steps in this
work order, provided:

- all outputs are documentation/specification artifacts only;
- no runtime artifacts are created;
- all governance gates pass.

Worker must not claim parity with any T4–T7 implementation scope.

---

## Claim Boundary

This work order claims:

- authorization to author LPCI1-T3 search and filter index specification and
  completion review;
- no runtime implementation, corpus indexing, or provider call scope.

This work order does NOT claim:

- runtime index correctness or tested search behavior;
- legal answer accuracy or production readiness;
- any T4–T7 scope.

---

## Finding-To-Governance Learning Disposition

Defect class: `RULE_GAP` — no LPCI1-T3 search/filter index work order or
specification existed before this dispatch

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Disposition: `RULE_ADDED` — LPCI1-T3 work order created; authorizes T3
search and filter index specification authoring

Next control action: `OPEN` — execute per Execution Plan above

Runtime/provider/cost learning: `N/A_WITH_REASON`

Reason: work order dispatch document; no provider calls, runtime behavior
changes, or cost events.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: work order references private internal governance chain.

Public-sync boundary: no artifacts from this batch are queued for public-sync.
