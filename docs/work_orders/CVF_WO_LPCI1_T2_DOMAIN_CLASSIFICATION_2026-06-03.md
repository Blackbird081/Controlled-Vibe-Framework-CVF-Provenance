# CVF Work Order - LPCI1-T2 Domain Classification

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-03

dispatchBaseHead: `2402aea0`

executionBaseHead: 89d5940f

closureBaseHead: 89d5940f

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Produce the LPCI1-T2 Domain Classification specification. This tranche defines
the legal/policy classification scheme aligned with GC-050, NR-11 alias
enforcement, and the canonical `answerClass` vocabulary introduced in T1
architecture review.

This tranche is documentation and specification only. No runtime code, vector
index, embedding pipeline, real corpus ingestion, or provider calls are
created.

---

## Authority Chain

| Authority | Path |
| --- | --- |
| LPCI1 GC-018 | `docs/baselines/CVF_GC018_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_2026-06-02.md` |
| LPCI1-T1 GC-018 supplement | `docs/baselines/CVF_GC018_LPCI1_T1_SUPPLEMENT_2026-06-02.md` |
| LPCI1 MVP roadmap (T2 row) | `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md` |
| T1 architecture | `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` |
| T1 corpus intake spec | `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md` |
| GC-050 classification standard | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` |
| NR-11 standard | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` |

---

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch; T1 closure artifact committed at `62976163` | no implementation |
| Worker | produce T2 classification spec and completion review | no runtime code; no real corpus ingestion |
| Reviewer | verify classification-only scope; reject any runtime artifact | reject UI/API/vector/provider work |

---

## Dependency Gate

Dependency satisfied. LPCI1-T1 closure artifact committed at `62976163`.

Release evidence:

- T1 completion review: `docs/reviews/CVF_LPCI1_T1_PRODUCT_INTAKE_AND_ARCHITECTURE_COMPLETION_2026-06-02.md` — Status: CLOSED_PASS_BOUNDED at commit `62976163`
- T1 work order: `docs/work_orders/CVF_WO_LPCI1_T1_PRODUCT_INTAKE_AND_ARCHITECTURE_2026-06-02.md` — closureBaseHead: `a155f505`
- T1 architecture: `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` — Status: ACTIVE (answerClass vocabulary canonicalized to GC-050 by reviewer)
- LPCI1 GC-018: `docs/baselines/CVF_GC018_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_2026-06-02.md` — Status: ACTIVE

---

## Roadmap Trace

| Roadmap | Tranche row | Status update |
| --- | --- | --- |
| LPCI1 MVP roadmap | W2 / LPCI1-T2 Domain classification | PROPOSED → IN_PROGRESS upon execution |

---

## Roadmap-To-Work-Order Trace Matrix

| Roadmap path | Roadmap tranche | Work order tranche | Mapped output | Verification |
| --- | --- | --- | --- | --- |
| `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md` | W2 / LPCI1-T2 Domain classification | `CVF_WO_LPCI1_T2_DOMAIN_CLASSIFICATION_2026-06-03.md` | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | roadmap W2 row; dependency = T1 CLOSED_PASS_BOUNDED at `62976163` |

---

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `answerClass` GC-050 canonical vocabulary | `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` | Answer Boundary Contract table (reviewer-corrected) | `answerClass` | LPCI1-T1 Architecture Answer Boundary Contract | ACCEPT |
| `rawDisposition` / `dispositionAlias` NR-11 | `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md` | NR-11 dispositionAlias Adoption section | `rawDisposition`; `dispositionAlias` | LPCI1-T1 Corpus Intake Spec NR-11 adoption | ACCEPT |
| GC-050 classification standard | `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` | Corpus Intelligence Classification standard | `DIRECT_CITED_ANSWER`; `SUMMARY_WITH_SOURCE`; `PROCEDURAL_GUIDANCE`; `ESCALATE_OR_ABSTAIN` | CVF Corpus Intelligence Classification Standard | ACCEPT |
| `legalPolicy` domain extension fields | `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` | Intake Record Schema table | `jurisdiction`; `authorityLevel`; `issuingBody`; `effectiveDate`; `status`; `documentType` | LPCI1-T1 Architecture Intake Record Schema | ACCEPT |
| Inherited gap G3 (legalPolicy absent in CI2-T4) | `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md` | Inherited Gaps G3 row | `legalPolicy` domain fields | LPCI1-T1 Corpus Intake Spec inherited gaps | ACCEPT |
| GC-051 registry file | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | file exists | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | GC-051 registry front door | ACCEPT |

---

## Write Ownership

| Path | Action | Notes |
| --- | --- | --- |
| `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | CREATE | primary T2 output; classification scheme, GC-050 alignment, answerClass table |
| `docs/reviews/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_COMPLETION_2026-06-03.md` | CREATE | T2 closure review |
| `docs/work_orders/CVF_WO_LPCI1_T2_DOMAIN_CLASSIFICATION_2026-06-03.md` | UPDATE | capture executionBaseHead and closureBaseHead |

---

## Allowed Scope

- Author the domain classification specification (documentation artifact).
- Define legal/policy `answerClass` enum values using GC-050 canonical
  vocabulary (`DIRECT_CITED_ANSWER`, `SUMMARY_WITH_SOURCE`,
  `PROCEDURAL_GUIDANCE`, `ESCALATE_OR_ABSTAIN`).
- Define `dispositionAlias` enforcement rules per NR-11 for the legal/policy
  domain.
- Define jurisdiction taxonomy (country, state, company, org scope levels).
- Define sensitivity classification rules per NR-06 for legal/policy documents.
- Define `ownerSurface` and `knowledgeRegion` canonical mapping for legal/policy.
- Describe classification criteria for each `documentType` enum value.
- Author the T2 completion review.
- Update this work order with captured head hashes.

---

## Forbidden Scope

- No runtime code files (Python, TypeScript, JavaScript, etc.).
- No database schema implementation files.
- No vector store, embedding, or semantic index files.
- No real legal corpus files; no GC-051 new corpus scan.
- No UI components or API route handlers.
- No provider calls or live API key usage.
- No modification of GC-051 scan registry with a real corpus (placeholder
  entries for T2 planning are allowed as documentation, not registry mutation).
- No claim of production readiness.

---

## Required First Reads

Before authoring, worker must read:

1. `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` — Answer Boundary Contract table (canonicalized vocabulary)
2. `docs/reference/CVF_LPCI1_T1_CORPUS_INTAKE_SPEC_2026-06-02.md` — Inherited gaps G1–G3, NR-04/NR-05/NR-11 adoption
3. `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` — GC-050 classification standard
4. `docs/baselines/CVF_GC018_LPCI1_T1_SUPPLEMENT_2026-06-02.md` — NR-11 dispositionAlias policy

---

## Pre-Flight Checks

1. Confirm T1 completion review exists and is CLOSED_PASS_BOUNDED.
2. Confirm `docs/reference/CVF_LPCI1_T1_ARCHITECTURE_2026-06-02.md` exists with reviewer-corrected `answerClass` vocabulary.
3. Confirm `docs/reference/CVF_CORPUS_INTELLIGENCE_CLASSIFICATION_STANDARD_2026-06-01.md` exists.
4. Capture `executionBaseHead` via `git rev-parse --short HEAD`.

---

## Execution Plan

### Step 1 — Capture executionBaseHead

```
git rev-parse --short HEAD → record in this work order as executionBaseHead
```

### Step 2 — Read required sources

Read files listed in Required First Reads.

### Step 3 — Author T2 domain classification spec

Create `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md`
covering all sections required by the reference structural checker:

- `## Purpose`
- `## Source`
- `## answerClass Enum` — GC-050 canonical values with classification criteria
- `## documentType Enum` — legal/policy document types
- `## jurisdictionTaxonomy` — jurisdiction level hierarchy
- `## sensitivityClassification` — NR-06 rules for legal/policy
- `## ownerSurface Mapping` — canonical enum for legal/policy domain
- `## knowledgeRegion Mapping` — knowledge region values for legal/policy
- `## dispositionAlias Rules` — NR-11 enforcement for legal/policy
- `## Requirements`
- `## Enforcement`
- `## Verification`
- `## Non-Goals`
- `## Claim Boundary`
- `## Related`

### Step 4 — Author T2 completion review

Create `docs/reviews/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_COMPLETION_2026-06-03.md`.

### Step 5 — Update this work order

Set `executionBaseHead`, `closureBaseHead`, and `Status: CLOSED_PASS_BOUNDED`.

### Step 6 — Run governance gates

```
python governance/compat/check_markdown_structural_completeness.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_public_export_disposition.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

All must exit 0 / COMPLIANT before worker signals done.

---

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| T2 classification spec authored | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` exists and is structurally complete |
| GC-050 alignment present | all four `answerClass` values defined with GC-050 criteria |
| NR-11 dispositionAlias rules present | `dispositionAlias: ACCEPT_DEFERRED` rule for DEFER/ACCEPT_SUMMARY_ONLY explicitly stated |
| No runtime artifacts | zero executable files created |
| All governance gates PASS | autorun pre-implementation gate COMPLIANT |

---

## Evidence Requirements

| Evidence type | Required path |
| --- | --- |
| T2 classification spec | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` |
| T2 completion review | `docs/reviews/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_COMPLETION_2026-06-03.md` |
| executionBaseHead | captured in this work order |
| closureBaseHead | captured in this work order |
| Gate results | recorded in T2 completion review |

---

## Review Gate

Reviewer confirms:

- [x] T2 classification spec is documentation only; no runtime code.
- [x] GC-050 canonical answerClass values used throughout.
- [x] NR-11 dispositionAlias rules present and consistent with NR-11 standard.
- [x] No real corpus ingestion attempted.
- [x] All governance gates PASS.

---

## Closure Checklist

- [x] `executionBaseHead` recorded.
- [x] T2 classification spec exists and is structurally complete.
- [x] T2 completion review exists and is structurally complete.
- [x] Status updated to `CLOSED_PASS_BOUNDED`.
- [x] `closureBaseHead` recorded.
- [x] All governance gates PASS.
- [x] Operator/reviewer commits; worker does NOT commit.

---

## Return Conditions

Worker must STOP and return to orchestrator if:

- Any runtime code file is required to produce the classification spec.
- A real legal corpus must be scanned to define the classification categories.
- A GC-051 registry entry mutation is required beyond documentation.
- Any live provider call is needed.

---

## Operator Checkpoint

Worker must pause for operator review before final commit if:

- The classification spec introduces new `answerClass` values beyond the four
  GC-050 canonical values in T1 architecture.
- A new NR rule or standard is required that does not exist in the repo.

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

Worker must not claim parity with any T3–T7 implementation scope.

---

## Claim Boundary

This work order claims:

- authorization to author LPCI1-T2 domain classification specification and
  completion review;
- no runtime implementation, corpus ingestion, or provider call scope.

This work order does NOT claim:

- runtime classification correctness;
- legal answer accuracy or production readiness;
- corpus ingestion readiness;
- any T3–T7 scope.

---

## Finding-To-Governance Learning Disposition

Defect class: `RULE_GAP` — no LPCI1-T2 domain classification work order or
specification existed before this dispatch

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Disposition: `RULE_ADDED` — LPCI1-T2 work order created; authorizes T2
classification specification authoring

Next control action: `OPEN` — execute per Execution Plan above

Runtime/provider/cost learning: `N/A_WITH_REASON`

Reason: work order dispatch document; no provider calls, runtime behavior
changes, or cost events.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: work order references private internal governance chain; not suitable
for public CVF repository at this stage.

Public-sync boundary: no artifacts from this batch are queued for public-sync.
