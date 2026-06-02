# CVF GC-018 - CI2 Corpus Intelligence Enforcement And Product Readiness

Memory class: FULL_RECORD

Status: AUTHORIZED_DISPATCH_PACKET

docType: gc018_baseline

Date: 2026-06-02

dispatchBaseHead: `65a0620f`

## Purpose

Authorize CI2 as the post-CI1 / post-CSA1 roadmap that turns Corpus
Intelligence from standards and reviewed packets into an enforceable,
product-ready intake chain.

CI2 is the required bridge before any LPCI chatbot runtime, API route,
frontend, vector store, embedding pipeline, or legal/policy answer surface is
implemented.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-02 approval to create the next optimized roadmap with five ordered work orders | ACCEPT |
| CI1 closure | `docs/roadmaps/CVF_CI1_CORPUS_INTELLIGENCE_OPERATIONALIZATION_ROADMAP_2026-06-02.md` status `ALL_TRANCHES_CLOSED_PASS_BOUNDED_LPCI_ROADMAP_READY` | ACCEPT |
| CI1-T6 checker decision | `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` | ACCEPT |
| CI1-T7 LPCI intake bridge | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | ACCEPT |
| CSA1 closure | NR-05 standard and NR-11 merge rule authored | ACCEPT |

## Source / Predecessor Evidence

| Predecessor | Evidence | CI2 dependency |
| --- | --- | --- |
| CI1-T6 | `docs/reference/CVF_CI1_T6_CHECKER_DECISION_2026-06-02.md` | defines NR-04/NR-05/NR-11 checker obligations |
| CI1-T7 | `docs/reference/CVF_CI1_T7_LPCI_INTAKE_BRIDGE_2026-06-02.md` | blocks LPCI runtime until separate roadmap |
| CSA1 | `docs/reference/CVF_CORPUS_PATH_NORMALIZATION_ALGORITHM_STANDARD_2026-06-02.md` and NR-11 rule in classification standard | satisfies two standard-first prerequisites |

## Decision / Baseline / Proposed Tranche

Decision: authorize CI2 as a five-tranche ordered roadmap. The baseline is
documentation and structural-enforcement preparation only; later workers must
execute each tranche through its own work order and closure evidence.

## Authorized Sequence

| Tranche | Work order | Goal | Dependency |
| --- | --- | --- | --- |
| CI2-T1 | `docs/work_orders/CVF_WO_CI2_T1_SOURCE_HASH_STANDARD_2026-06-02.md` | Author NR-04 per-file source hash standard and readiness-template rule | none beyond CI1/CSA1 closure |
| CI2-T2 | `docs/work_orders/CVF_WO_CI2_T2_PACKET_NORMALIZATION_CHECKERS_2026-06-02.md` | Implement structural checkers for NR-04, NR-05, NR-11 | CI2-T1 closed |
| CI2-T3 | `docs/work_orders/CVF_WO_CI2_T3_ENFORCED_CROSS_CORPUS_INDEX_MODEL_2026-06-02.md` | Produce enforced cross-corpus index schema/model v2 | CI2-T2 closed |
| CI2-T4 | `docs/work_orders/CVF_WO_CI2_T4_PRODUCT_READINESS_PILOT_CORPUS_PACK_2026-06-02.md` | Build a pilot product-readiness corpus pack using enforced fields | CI2-T3 closed |
| CI2-T5 | `docs/work_orders/CVF_WO_CI2_T5_LPCI_PRODUCT_ROADMAP_PACKET_2026-06-02.md` | Draft LPCI product GC-018 and MVP roadmap packet | CI2-T4 closed |

## Scope

Allowed:

- governance standards for per-file source hashes;
- machine checkers for source hash, normalized path, and canonical disposition;
- hook/autorun integration only when explicitly owned by CI2-T2;
- cross-corpus index schema/model documents;
- pilot product-readiness pack from existing CI1 evidence or an operator-provided
  bounded corpus;
- LPCI product roadmap and GC-018 proposal after CI2-T4 closes.

Forbidden:

- implementing LPCI runtime, chatbot UI, API routes, vector DB, embeddings, or
  provider calls;
- scanning a new corpus without GC-051 registration and work-order authority;
- public-sync;
- claiming semantic correctness, legal correctness, production readiness, hosted
  readiness, or public readiness.

Risk ceiling: R2 for CI2-T2 checker implementation; R1 for all other CI2
tranches.

## Claim Boundary

This GC-018 authorizes planning, standards, structural enforcement, index
schema, pilot-readiness packaging, and LPCI roadmap proposal only. It does not
authorize product implementation or live governance proof.

## Evidence / Verification

Required dispatch verification for this baseline:

```powershell
python governance/compat/check_markdown_structural_completeness.py --base 65a0620f --head HEAD --enforce
python governance/compat/check_work_order_dispatch_quality.py --base 65a0620f --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 65a0620f --head HEAD
```

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
