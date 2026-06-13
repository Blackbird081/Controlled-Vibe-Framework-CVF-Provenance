# CVF GC-018 - MEMCON-T4 Retrieval-Pack Boundary Conformance

Memory class: FULL_RECORD

Status: DISPATCHED

docType: baseline

Date: 2026-06-13

Owner: Codex

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `a6902ef2`

sourceAuthority:
`docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md`

rawMemoryReleased=false

workOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_FOR_CLAUDE_2026-06-13.md`

parentRoadmap:
`docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md`

## Purpose

Authorize MEMCON-T4 as a bounded implementation tranche for retrieval-pack
boundary conformance. The worker may add a small Learning Plane helper and
focused tests that prove MEMCON consolidated-memory summaries can be prepared
for the existing retrieval owner surfaces without raw memory release.

This tranche does not authorize route wiring, durable storage, semantic memory
correctness claims, provider/API proof, OCR, Policy_Local mutation, public-sync,
production readiness, memory reinjection, high-risk promotion, or autonomous
mutation.

## Decision / Baseline / Proposed Tranche

Decision: dispatch MEMCON-T4 to Claude under `WORKER_MUST_NOT_COMMIT`.

Baseline:

- MEMCON-T1a is `CLOSED_PASS_BOUNDED` and defines the workflow chain standard.
- MEMCON-T1b is `CLOSED_PASS_BOUNDED` and defines the schema appendix.
- MEMCON-T2 is `CLOSED_PASS_BOUNDED` and adds the MEMCON artifact quality
  checker.
- MEMCON-T3 is `CLOSED_PASS_BOUNDED` and adds the Markdown-first operator
  packet contract plus sample fixture.

Authorized tranche:

- add a deterministic retrieval-pack boundary helper in
  `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/`;
- add focused conformance tests in `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/`;
- prove expired, disputed, sensitive, time-ambiguous, stale-blocked, conflict,
  source-missing, and confidence-missing inputs cannot enter the selected
  retrieval pack;
- keep `rawMemoryReleased=false` on every retrieval-facing output;
- return uncommitted artifacts to Codex for review and commit.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| MEMCON-T1a standard | `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md`; material commit `84a46b62` | ACCEPT |
| MEMCON-T1b schema appendix | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md`; material commit `f94d2fbd` | ACCEPT |
| MEMCON-T2 checker | `governance/compat/check_memory_consolidation_artifact_quality.py`; material commit `f83aa7d8` | ACCEPT |
| MEMCON-T3 operator packet closure | `docs/reviews/CVF_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_COMPLETION_2026-06-13.md`; material commit `2800e83c`; session sync `a6902ef2` | ACCEPT |
| Fresh T4 authorization | this GC-018 baseline and the paired Claude work order | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| T4 goal is retrieval-pack boundary | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | lines 544-560 | `MEMCON-T4` | MEMCON roadmap | ACCEPT |
| T4 must connect consolidated memory to existing retrieval policy and runtime workflow surfaces without claiming raw memory release | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | lines 548-550 | `memory-retrieval-policy.ts`, `memory-runtime-workflow-chain.ts` | MEMCON roadmap | ACCEPT |
| T4 conformance excludes expired, disputed, sensitive, time-ambiguous, stale-blocked memory and includes source path plus confidence in selected context | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | lines 552-560 | `Required conformance` | MEMCON roadmap | ACCEPT |
| Retrieval policy exposes MemoryRetrievalCandidate lifecycle state and raw release invariant | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | lines 17-49 | `MemoryRetrievalCandidate`, `rawMemoryReleased` | memory retrieval policy | ACCEPT |
| Retrieval policy blocks expired and disputed lifecycle states | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | lines 52, 147-148, 232-233 | `BLOCKED_STATES` | memory retrieval policy | ACCEPT |
| Runtime workflow chain exposes packaged, denied, and deferred statuses while preserving raw release false | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-runtime-workflow-chain.ts` | lines 26-60, 95-215 | `runMemoryRuntimeWorkflowChain`, `rawMemoryReleased` | memory runtime workflow chain | ACCEPT |
| Controlled memory gateway preserves raw release false and blocks unauthorized reinjection | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | lines 35-50, 76-88, 120-121 | `rawMemoryReleased`, `memory_reinjection_not_authorized` | controlled memory gateway | ACCEPT |
| MemoryRetrievalPackInput fields include selected/excluded record IDs, summary-only, raw release false, and retrieval consumer | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | lines 149-166 | `MemoryRetrievalPackInput` | MEMCON T1b schema appendix | ACCEPT |
| ConsolidatedMemoryRecord retrieval fields include retrievalBoundary, retrievalEligibility, and raw release false | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | lines 121-147 | `ConsolidatedMemoryRecord` | MEMCON T1b schema appendix | ACCEPT |
| Source authority and relative-date blocking rules apply to retrieval-facing shapes | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | lines 188-198 | `Promotion And Blocking Rules` | MEMCON T1b schema appendix | ACCEPT |
| T3 retrieval preview section requires rawMemoryReleased=false and no raw memory release implication | `docs/reference/CVF_MEMORY_CONSOLIDATION_LEDGER_OPERATOR_PACKET_CONTRACT_2026-06-13.md` | lines 166-181 | `rawMemoryReleased` | MEMCON-T3 operator packet contract | ACCEPT |
| MEMCON checker enforces retrieval-facing raw release boundary on changed MEMCON artifacts | `governance/compat/check_memory_consolidation_artifact_quality.py` | lines 102-108, 355-368 | `RETRIEVAL_BOUNDARY_MARKER`, `_check_retrieval_boundary` | MEMCON artifact quality checker | ACCEPT |

## New Implementation Symbols Authorized

These symbols are new T4 implementation targets, not pre-existing source
claims:

| New symbol | Target file | Purpose | Boundary |
| --- | --- | --- | --- |
| `MEMCON_RETRIEVAL_PACK_BOUNDARY_VERSION` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-consolidation-retrieval-pack-boundary.ts` | version constant for the T4 helper | new T4 source |
| `MemconConsolidatedMemoryRecordInput` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-consolidation-retrieval-pack-boundary.ts` | narrow input shape for consolidated-memory summaries | does not replace doc-only schema appendix |
| `buildMemconRetrievalPackBoundary` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-consolidation-retrieval-pack-boundary.ts` | deterministic pack-selection helper | no route wiring or provider call |

## Evidence / Verification

Required dispatch verification:

- MEMCON artifact quality checker passes on the dispatch package.
- work-order dispatch quality checker passes on the dispatch package.
- pre-dispatch autorun gate passes on the dispatch package.
- reviewer-fast and pre-commit gates pass before Codex commits.

Required worker verification is defined in the paired work order.

## Authorized Artifact Set

Claude may create or update only the files named in the paired work order:

- a Learning Plane helper for MEMCON retrieval-pack boundary conformance;
- focused tests for the helper;
- a worker-return packet.

No route wiring, session state, public-sync, provider/API, OCR, Policy_Local,
generated JSON aggregate, or external workspace mutation is authorized for the
worker.

## Claim Boundary

This GC-018 authorizes bounded T4 helper and conformance-test implementation
only. It does not claim runtime retrieval behavior is changed, semantic memory
correctness is proven, durable memory storage exists, vector retrieval exists,
operator UI exists, Policy_Local is ready, public catalog export exists,
provider/API proof exists, OCR is available, memory reinjection is authorized,
high-risk promotion is authorized, or autonomous mutation is authorized.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

This is a private provenance dispatch baseline. No public-sync artifact or
public catalog claim is authorized by this tranche.
