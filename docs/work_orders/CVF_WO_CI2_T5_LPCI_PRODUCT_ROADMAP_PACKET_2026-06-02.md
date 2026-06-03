# CVF Work Order - CI2-T5 LPCI Product Roadmap Packet

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-06-02

dispatchBaseHead: `02a201bf`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: NOT_EXECUTED_YET

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Draft the governed LPCI product packet after CI2 enforcement and pilot
readiness exist. This tranche prepares LPCI for implementation planning but
does not implement the chatbot.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| CI2 GC-018 | `docs/baselines/CVF_GC018_CI2_CORPUS_INTELLIGENCE_ENFORCEMENT_PRODUCT_READINESS_2026-06-02.md` | ACCEPT |
| CI2 roadmap | `docs/roadmaps/CVF_CI2_CORPUS_INTELLIGENCE_ENFORCEMENT_PRODUCT_READINESS_ROADMAP_2026-06-02.md` | ACCEPT |
| CI2-T4 pilot pack | `docs/corpus-intelligence/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK.json` at commit `02a201bf` | ACCEPT |
| CI1-T7 | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | dispatch after T4 closure | no implementation |
| Worker | draft GC-018, roadmap, future T1 work order | no product code |
| Reviewer | verify blocked scope and dependencies | reject runtime/API/UI changes |

## Dependency Gate

CI2-T5 may begin only after CI2-T4 closes with a product-readiness pilot pack.
This prerequisite is satisfied by commit `02a201bf`.

## Roadmap-To-Work-Order Trace Matrix

| CI2 roadmap requirement | CI2-T5 instruction |
| --- | --- |
| Convert corpus readiness into product roadmap | create LPCI GC-018 + MVP roadmap |
| Preserve blocked runtime boundary | no UI/API/vector/provider implementation |
| Use pilot pack as input | cite CI2-T4 output and gaps |

## Source Verification Block

| Claimed item | Evidence type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| LPCI may be proposed only as separate governed product roadmap | EXISTS | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | lines 62 and 213 | `LPCI product roadmap proposal` | Downstream Routing | ACCEPT |
| LPCI runtime remains blocked until separate roadmap | EXISTS | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | lines 191-201 | `Blocked Scope` | CI1-T7 intake bridge | ACCEPT |
| LPCI must inherit CI1 claim boundaries | EXISTS | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | lines 106-143 | `Claim Boundary Inheritance` | CI1-T7 intake bridge | ACCEPT |
| Existing use-case roadmap is product target context | EXISTS | `docs/roadmaps/CVF_LPCI_LEGAL_POLICY_CORPUS_INTELLIGENCE_CHATBOT_USE_CASE_ROADMAP_2026-06-01.md` | title and purpose sections | `LPCI` | use-case roadmap | ACCEPT |
| CI2-T4 pilot pack exists and is the required input | EXISTS | `docs/corpus-intelligence/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK.json` | root packet metadata | `packId` | CI2-T4 product readiness pilot corpus pack | ACCEPT |
| CI2-T4 closure exists | EXISTS | `docs/reviews/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK_COMPLETION_2026-06-02.md` | title and verdict sections | `CLOSED_PASS_BOUNDED` | CI2-T4 completion review | ACCEPT |

## Write Ownership

| Path | Action | Owner |
| --- | --- | --- |
| `docs/baselines/CVF_GC018_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_2026-06-02.md` | CREATE | Worker |
| `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md` | CREATE | Worker |
| `docs/work_orders/CVF_WO_LPCI1_T1_PRODUCT_INTAKE_AND_ARCHITECTURE_2026-06-02.md` | CREATE | Worker |
| `docs/reviews/CVF_CI2_T5_LPCI_PRODUCT_ROADMAP_PACKET_COMPLETION_2026-06-02.md` | CREATE | Worker |

## Allowed Scope

- create `docs/baselines/CVF_GC018_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_2026-06-02.md`;
- create `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md`;
- create `docs/work_orders/CVF_WO_LPCI1_T1_PRODUCT_INTAKE_AND_ARCHITECTURE_2026-06-02.md` as a future dispatch packet only;
- create `docs/reviews/CVF_CI2_T5_LPCI_PRODUCT_ROADMAP_PACKET_COMPLETION_2026-06-02.md`;
- update no runtime/product code.

Forbidden scope:

- frontend implementation in `CVF-Workspace/PolicyLocal` or this repo;
- API routes, vector DB, embeddings, provider calls, browser testing, live proof;
- public-sync;
- claiming legal advice quality or production readiness.

## Required First Reads

1. CI2-T4 pilot pack and completion review.
2. `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md`
3. `docs/roadmaps/CVF_LPCI_LEGAL_POLICY_CORPUS_INTELLIGENCE_CHATBOT_USE_CASE_ROADMAP_2026-06-01.md`
4. CI2-T3 enforced index schema.

## Pre-Flight Checks

| Check | Command | Requirement |
| --- | --- | --- |
| T4 pilot pack exists | `Test-Path docs/corpus-intelligence/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK.json` | true |
| T4 pilot pack valid | `python -m json.tool docs/corpus-intelligence/CVF_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK.json` | exit 0 |

## Execution Plan

1. Read T4 pilot, CI1-T7, and LPCI use-case roadmap.
2. Draft LPCI1 GC-018 baseline.
3. Draft LPCI1 MVP roadmap.
4. Draft future LPCI1-T1 intake/architecture work order.
5. Create completion review and run gates.

## Execution Instructions

1. Author LPCI1 GC-018 with explicit product boundary, corpus prerequisites,
   no-runtime-until-T1 gate, and legal/policy answer safety boundary.
2. Author LPCI1 MVP roadmap with tranches for intake/architecture, corpus
   ingestion, retrieval/query, UI, governance proof, and product review.
3. Create only the first future work order (`LPCI1-T1`) as a dispatch packet for
   product intake and architecture. It must not implement code.
4. Cite CI2-T4 pilot pack and list inherited gaps that LPCI must handle.
5. Create completion review and run gates.

## Acceptance Criteria

| Criterion | Requirement |
| --- | --- |
| LPCI GC-018 exists | baseline created with blocked runtime boundary |
| LPCI roadmap exists | product MVP tranches listed with dependencies |
| Future T1 work order exists | architecture/intake only, no implementation |
| CI2 evidence inherited | T4 pack, T3 schema, T2 checkers, T1 standard cited |
| No product code | no frontend/API/vector/provider files modified |

## Evidence Requirements

- LPCI artifacts cite CI1-T7 and CI2-T4.
- Runtime blocked scope is explicit.
- Future LPCI1-T1 work order is architecture/intake only.

## Review Gate

Reviewer must verify CI2-T5 creates planning artifacts only and does not start
product implementation.

## Closure Checklist

| Item | Required final state |
| --- | --- |
| LPCI1 GC-018 | authored |
| LPCI1 roadmap | authored |
| Future T1 work order | authored |
| Product code | untouched |

## Return Conditions

Return to orchestrator after roadmap packet and gates complete or if T4 closure
is missing.

## Operator Checkpoint

No additional operator checkpoint is required for roadmap drafting. Operator
authorization is required before any later implementation tranche begins.

## Required Gates

```powershell
python governance/compat/check_markdown_structural_completeness.py --base <baseHead> --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base <baseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <baseHead> --head HEAD
git diff --check
git status --short
```

## Worker Autonomy / No-Question Rule

Worker must draft the LPCI product packet from existing CI1/CI2 evidence and
must not ask whether to implement UI/runtime. Worker must stop for any request
to write product code, consume live keys/quota, or public-sync.

## Claim Boundary

CI2-T5 creates a product-roadmap packet only. It does not implement LPCI,
perform legal retrieval, answer legal questions, run live proof, or claim
production/public readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
