# CVF Work Order - LPCI1-T4 Retrieval Boundary

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-03

dispatchBaseHead: `818fe435`

executionBaseHead: 818fe435

closureBaseHead: 818fe435

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Produce the LPCI1-T4 Retrieval Boundary specification. This tranche defines
the retrieval pipeline contract, answer assembly rules, conflict resolution
protocol, freshness/currency warning protocol, AuditReceipt schema, and the
formal response boundary contract that the T5 chatbot prototype must satisfy.

This tranche is documentation and specification only. No runtime code, real
corpus retrieval, vector search, embedding, or provider calls are created.

---

## Authority Chain

| Authority | Path |
| --- | --- |
| LPCI1 GC-018 | `docs/baselines/CVF_GC018_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_2026-06-02.md` |
| LPCI1 MVP roadmap (T4 row) | `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md` |
| T3 search/filter index spec | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` |
| T2 domain classification spec | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` |
| T1 architecture | `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` |

---

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch; T3 closed at `1bc3c68e` | no implementation |
| Worker | produce T4 retrieval boundary spec and completion review | no runtime code; no retrieval |
| Reviewer | verify spec-only scope; reject any runtime artifact | reject vector/API/UI/provider work |

---

## Dependency Gate

Dependency satisfied. LPCI1-T3 closed at `1bc3c68e`.

Release evidence:

- T3 completion review: `docs/reviews/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_COMPLETION_2026-06-03.md` — Status: CLOSED_PASS_BOUNDED at commit `1bc3c68e`
- T3 work order: `docs/work_orders/CVF_WO_LPCI1_T3_SEARCH_FILTER_INDEX_2026-06-03.md` — closureBaseHead: `1cedefd8`
- T3 index spec: `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` — Status: ACTIVE

---

## Roadmap Trace

| Roadmap | Tranche row | Status update |
| --- | --- | --- |
| LPCI1 MVP roadmap | W4 / LPCI1-T4 Retrieval boundary | PROPOSED → CLOSED_PASS_BOUNDED |

---

## Roadmap-To-Work-Order Trace Matrix

| Roadmap path | Roadmap tranche | Work order tranche | Mapped output | Verification |
| --- | --- | --- | --- | --- |
| `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md` | W4 / LPCI1-T4 Retrieval boundary | `CVF_WO_LPCI1_T4_RETRIEVAL_BOUNDARY_2026-06-03.md` | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | roadmap W4 row; dependency = T3 CLOSED_PASS_BOUNDED at `1bc3c68e` |

---

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `EXISTS: answerClass post-filter Stage 4` | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` | `## Query Filter Contract / Stage 4` | `answerClass` | `LPCI1-T3 query filter contract` | ACCEPT |
| `EXISTS: AuditReceipt pseudocode` | `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` | `### Retrieval Flow (pseudocode notation)` | `AuditReceipt` | `LPCI1-T1 retrieval architecture` | ACCEPT |
| `EXISTS: Answer Boundary Contract table` | `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` | `### Answer Boundary Contract` | `answerClass` | `LPCI1-T1 architecture retrieval boundary` | ACCEPT |
| `EXISTS: conflict_flag freshness_flag design` | `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` | `### Retrieval Flow (pseudocode notation)` | `conflict_flag`, `freshness_flag` | `LPCI1-T1 retrieval architecture` | ACCEPT |
| `EXISTS: ESCALATE_OR_ABSTAIN abstention rule` | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | `### ESCALATE_OR_ABSTAIN` | `answerClass` | `LPCI1-T2 domain classification scheme` | ACCEPT |
| `EXISTS: STALE_STATUS_WARNING receipt` | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` | `### Receipt: STALE_STATUS_WARNING` | `staleStatusWarning` | `LPCI1-T3 negative search evidence format` | ACCEPT |

---

## Write Ownership

| Path | Action | Notes |
| --- | --- | --- |
| `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | CREATE | primary T4 output |
| `docs/reviews/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_COMPLETION_2026-06-03.md` | CREATE | T4 closure review |
| `docs/work_orders/CVF_WO_LPCI1_T4_RETRIEVAL_BOUNDARY_2026-06-03.md` | UPDATE | capture heads; close |

---

## Allowed Scope

- Author the T4 retrieval boundary specification (documentation artifact).
- Define retrieval pipeline contract, answer assembly rules, conflict resolution,
  freshness warning, AuditReceipt schema, response boundary contract.
- Author T4 completion review.
- Update this work order with head hashes and closure checklist.

---

## Forbidden Scope

- No runtime code files of any kind.
- No real corpus retrieval, vector search, or semantic model calls.
- No UI components, API route handlers, or database schema files.
- No provider calls or live API key usage.
- No claim of tested retrieval correctness or production readiness.

---

## Required First Reads

1. `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` — retrieval flow pseudocode, answer boundary contract, AuditReceipt
2. `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` — five-stage filter, negative receipts
3. `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` — answerClass criteria, decision matrix

---

## Pre-Flight Checks

1. Confirm T3 completion review CLOSED_PASS_BOUNDED at `1bc3c68e`.
2. Confirm T3 search/filter index spec ACTIVE.
3. Confirm T1 architecture ACTIVE with reviewer-corrected answerClass vocabulary.
4. Confirm `executionBaseHead` captured.

All pre-flight checks confirmed at execution.

---

## Execution Plan

Steps completed by worker in this session:

1. Captured `executionBaseHead: 818fe435`.
2. Read T1 architecture, T3 filter contract, T2 classification spec.
3. Authored `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md`.
4. Authored `docs/reviews/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_COMPLETION_2026-06-03.md`.
5. Updated this work order to `CLOSED_PASS_BOUNDED`.
6. All governance gates: COMPLIANT.

---

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| T4 spec authored | structurally complete; all sections present |
| Retrieval pipeline contract | T3 five-stage filter feeds answer assembly; Stage 4 non-overridable |
| Conflict resolution protocol | two-record conflict rule defined |
| Freshness warning protocol | amended/superseded handling defined |
| AuditReceipt schema | all fields from T1 pseudocode formalized |
| Response boundary contract | per-answerClass response rules formalized |
| No runtime artifacts | zero executable files created |
| All governance gates PASS | autorun gate COMPLIANT |

---

## Evidence Requirements

| Evidence type | Required path |
| --- | --- |
| T4 spec | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` |
| T4 completion review | `docs/reviews/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_COMPLETION_2026-06-03.md` |
| executionBaseHead | `818fe435` |
| closureBaseHead | `818fe435` |

---

## Review Gate

Reviewer confirms:

- [x] T4 spec is documentation only; no runtime code.
- [x] Retrieval pipeline contract derives from T1 architecture and T3 filter.
- [x] Conflict resolution and freshness warning protocols defined.
- [x] AuditReceipt schema covers all T1 fields.
- [x] All governance gates PASS.

---

## Closure Checklist

- [x] `executionBaseHead` recorded.
- [x] T4 spec exists and is structurally complete.
- [x] T4 completion review exists and is structurally complete.
- [x] Status updated to `CLOSED_PASS_BOUNDED`.
- [x] `closureBaseHead` recorded.
- [x] All governance gates PASS.
- [x] Operator/reviewer commits; worker does NOT commit.

---

## Return Conditions

Worker must STOP and return to orchestrator if:

- Any runtime code file is required to produce the retrieval boundary spec.
- A live retrieval system or provider call is needed.
- A new NR rule or standard is required.

---

## Operator Checkpoint

Worker must pause if the spec introduces a new retrieval contract field that
conflicts with T1 architecture or T3 filter contract.

---

## Required Gates

| Gate | Command |
| --- | --- |
| markdown structural completeness | `python governance/compat/check_markdown_structural_completeness.py --base 818fe435 --head HEAD --enforce` |
| work-order dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base 818fe435 --head HEAD --enforce` |
| finding-to-governance learning | `python governance/compat/check_finding_to_governance_learning.py --base 818fe435 --head HEAD --enforce` |
| public export disposition | `python governance/compat/check_public_export_disposition.py --base 818fe435 --head HEAD --enforce` |
| pre-implementation autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 818fe435 --head HEAD` |

---

## Worker Autonomy / No-Question Rule

Worker may proceed without further operator approval for all steps in this
work order, provided:

- all outputs are documentation/specification artifacts only;
- no runtime artifacts are created;
- all governance gates pass.

Worker must not claim parity with any T5–T7 implementation scope.

---

## Claim Boundary

This work order claims authorization to author LPCI1-T4 retrieval boundary
specification and completion review; no runtime implementation, corpus
retrieval, or provider call scope.

---

## Finding-To-Governance Learning Disposition

Defect class: `RULE_GAP` — no LPCI1-T4 retrieval boundary work order or
specification existed before this dispatch

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Disposition: `RULE_ADDED` — LPCI1-T4 work order created and executed;
retrieval boundary specification and completion review authored

Next control action: `OPEN` — LPCI1-T5 chatbot prototype is the first
runtime tranche; requires separate GC-018/work order after T4 closes

Runtime/provider/cost learning: `N/A_WITH_REASON`

Reason: documentation and specification only; no provider calls, runtime
changes, or cost events.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: work order references private internal governance chain.

Public-sync boundary: no artifacts from this batch are queued for public-sync.
