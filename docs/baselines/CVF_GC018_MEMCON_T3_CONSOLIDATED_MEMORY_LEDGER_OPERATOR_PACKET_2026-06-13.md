# CVF GC-018 - MEMCON-T3 Consolidated Memory Ledger And Operator Packet

Memory class: FULL_RECORD

Status: DISPATCHED

docType: baseline

Date: 2026-06-13

Owner: Codex

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `c454921a`

sourceAuthority:
`docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md`

rawMemoryReleased=false

workOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_FOR_CLAUDE_2026-06-13.md`

parentRoadmap:
`docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md`

## Purpose

Authorize MEMCON-T3 as a documentation-first worker tranche for a consolidated
memory ledger contract and a Markdown-first operator-visible review packet.

The tranche exists so later memory retrieval packaging can consume only
source-authorized, temporally classified, conflict-aware, and operator-visible
memory summaries. It does not authorize runtime memory storage, retrieval
behavior, Policy_Local mutation, public-sync, provider/API proof, OCR, or raw
memory release.

## Decision / Baseline / Proposed Tranche

Decision: dispatch MEMCON-T3 to Claude under `WORKER_MUST_NOT_COMMIT`.

Baseline:

- MEMCON-T1a is `CLOSED_PASS_BOUNDED` and defines the workflow chain standard.
- MEMCON-T1b is `CLOSED_PASS_BOUNDED` and defines the schema appendix.
- MEMCON-T2 is `CLOSED_PASS_BOUNDED` and adds the MEMCON artifact quality
  checker.

Proposed tranche:

- create a Markdown-first ledger and operator packet contract;
- create a bounded sample operator packet with distinct category fixtures;
- create a worker-return packet with proof evidence;
- return uncommitted artifacts to Codex for review and commit.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| MEMCON-T1a standard | `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md`; material commit `84a46b62` | ACCEPT |
| MEMCON-T1b schema appendix | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md`; material commit `f94d2fbd` | ACCEPT |
| MEMCON-T2 checker | `governance/compat/check_memory_consolidation_artifact_quality.py`; material commit `f83aa7d8`; session sync `c454921a` | ACCEPT |
| Fresh T3 authorization | this GC-018 baseline and the paired Claude work order | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| T3 deliverable is the consolidated memory ledger and Markdown-first operator packet | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | `MEMCON-T3 Detail` | `MEMCON-T3` | MEMCON roadmap | ACCEPT |
| T3 expected outputs include Markdown review packet and distinct sample fixtures | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | `MEMCON-T3 Detail` | `sample fixtures` | MEMCON roadmap | ACCEPT |
| Operator review packet is Markdown-first | `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md` | `Operator-Visible Memory Review Packet` | `Operator-Visible Memory Review Packet` | MEMCON T1a standard | ACCEPT |
| Retrieval-facing output must retain raw release boundary | `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md` | `Retrieval Eligibility Rule` | `rawMemoryReleased` | MEMCON T1a standard | ACCEPT |
| OperatorMemoryReviewPacket fields are source-defined | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | `OperatorMemoryReviewPacket Field Table` | `OperatorMemoryReviewPacket` | MEMCON T1b schema appendix | ACCEPT |
| Source authority blocks promotion when empty | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | `Promotion And Blocking Rules` | `sourceAuthority` | MEMCON T1b schema appendix | ACCEPT |
| Every retrieval-facing shape carries the raw release invariant | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | `Promotion And Blocking Rules` | `rawMemoryReleased` | MEMCON T1b schema appendix | ACCEPT |
| T2 checker enforces source authority and retrieval boundary markers on changed MEMCON artifacts | `governance/compat/check_memory_consolidation_artifact_quality.py` | constants and validator rules | `SOURCE_AUTHORITY_MARKERS` | MEMCON artifact quality checker | ACCEPT |
| JSON aggregate work requires source layout and generator discipline | `docs/reference/CVF_JSON_GENERATED_AGGREGATE_DISCIPLINE_STANDARD_2026-06-12.md` | generated aggregate requirements | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | JSON generated aggregate discipline standard | ACCEPT |

## Evidence / Verification

Required dispatch verification:

- MEMCON artifact quality checker passes on the dispatch package;
- work-order dispatch quality checker passes on the dispatch package;
- pre-dispatch autorun gate passes on the dispatch package;
- reviewer-fast and pre-commit gates pass before Codex commits.

## Authorized Artifact Set

Claude may create or update only the files named in the paired work order. The
default implementation is Markdown-first:

- a reference contract for the consolidated memory ledger and operator review
  packet;
- a worker-return review packet;
- a bounded sample packet or fixture section proving active, stale,
  conflicted, pruned or rejected, and time-ambiguous memory rows are rendered
  distinctly.

JSON ledger creation is not the default route. If Claude finds the ledger must
be append-heavy or repeatedly agent-edited, Claude must return with a scoped
generator/source-layout recommendation instead of hand-editing a large JSON
aggregate.

## Claim Boundary

This GC-018 authorizes documentation and fixture design only. It does not claim
runtime memory implementation, retrieval integration, semantic memory
correctness, production readiness, public readiness, live governance behavior,
provider/API proof, OCR, Policy_Local mutation, EC activation, corpus
ingestion, T12 unlock, memory reinjection, high-risk promotion, or autonomous
mutation.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

This is a private provenance dispatch baseline. No public-sync artifact or
public catalog claim is authorized by this tranche.
