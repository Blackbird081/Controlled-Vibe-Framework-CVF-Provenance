# CVF GC-018 - MEMCON-T5 Cross-Agent Memory Consistency Contract

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-13

Owner: Codex

Assigned worker: Claude

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `76f001a6`

sourceAuthority:
`docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md`

rawMemoryReleased=false

workOrder:
`docs/work_orders/CVF_AGENT_WORK_ORDER_MEMCON_T5_CROSS_AGENT_MEMORY_CONSISTENCY_CONTRACT_FOR_CLAUDE_2026-06-13.md`

parentRoadmap:
`docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md`

## Purpose

Authorize MEMCON-T5 as a bounded documentation-and-fixture tranche for a
cross-agent memory consistency contract. The worker may define a Markdown-first
contract and sample packet that prevent Codex, Claude, Gemini, or another
worker from writing separate authoritative memories without shared ledger
references and source-backed reconciliation.

This tranche does not authorize runtime memory storage, route wiring, retrieval
behavior changes, provider/API proof, OCR, Policy_Local mutation, public-sync,
generated JSON aggregate hand-editing, memory reinjection, high-risk
promotion, or autonomous mutation.

## Scope / Target / Owner Boundary

Target: MEMCON-T5 contract and bounded sample packet only.

Owner boundary: Codex owns dispatch, review, commit, and session state. Claude
owns worker implementation artifacts under `WORKER_MUST_NOT_COMMIT` and must
return them uncommitted for Codex review.

## Decision / Baseline / Proposed Tranche

Decision: close MEMCON-T5 as `CLOSED_PASS_BOUNDED` after Claude returned
uncommitted worker artifacts and Codex completed review.

Baseline:

- MEMCON-T1a is `CLOSED_PASS_BOUNDED` and defines the workflow chain standard.
- MEMCON-T1b is `CLOSED_PASS_BOUNDED` and defines the schema appendix.
- MEMCON-T2 is `CLOSED_PASS_BOUNDED` and adds the MEMCON artifact quality
  checker.
- MEMCON-T3 is `CLOSED_PASS_BOUNDED` and adds the Markdown-first operator
  packet contract plus sample fixture.
- MEMCON-T4 is `CLOSED_PASS_BOUNDED` and adds the local retrieval-pack
  boundary helper plus focused tests.

Authorized tranche:

- add a cross-agent memory consistency contract under `docs/reference/`;
- add a bounded sample consistency packet under `docs/reviews/`;
- require shared ledger references, source artifact references, conflict
  detection, resolution owner, operator-confirmation boundary, and claim
  boundary;
- return uncommitted artifacts to Codex for review and commit.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| MEMCON-T1a standard | `docs/reference/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_STANDARD_2026-06-12.md`; material commit `84a46b62` | ACCEPT |
| MEMCON-T1b schema appendix | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md`; material commit `f94d2fbd` | ACCEPT |
| MEMCON-T2 checker | `governance/compat/check_memory_consolidation_artifact_quality.py`; material commit `f83aa7d8` | ACCEPT |
| MEMCON-T3 operator packet closure | `docs/reviews/CVF_MEMCON_T3_CONSOLIDATED_MEMORY_LEDGER_OPERATOR_PACKET_COMPLETION_2026-06-13.md`; material commit `2800e83c`; session sync `a6902ef2` | ACCEPT |
| MEMCON-T4 retrieval boundary closure | `docs/reviews/CVF_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_COMPLETION_2026-06-13.md`; material commit `f771bff8`; session sync `76f001a6` | ACCEPT |
| Fresh MEMCON-T5 authorization | this GC-018 baseline and the paired Claude work order | ACCEPT |

## Knowledge Absorption Blind-Spot Control Block

| Control item | Evidence | Disposition |
| --- | --- | --- |
| Prior absorption evidence resolved | MEMCON-T1a through T4 closures are named in dependency evidence | COMPLETE |
| Detailed source files read | roadmap, T1a standard, T1b schema appendix, T3 contract, T4 completion | COMPLETE |
| Current owner surfaces checked | schema appendix field tables and T5 roadmap section distinguish existing fields from new doc-only fields | COMPLETE |
| Accept/defer/reject dispositions recorded | Source Verification Block and New Doc-Only Fields Authorized tables below | COMPLETE |
| Adversarial role review planned | worker must include dissent/review ledger in contract and sample packet | COMPLETE |
| Blind-spot delta | no runtime storage, route wiring, provider proof, public-sync, or autonomous mutation is authorized | COMPLETE |

Verdict: `COMPLETE_WITH_DECLARED_BOUNDARIES`.

## Rescan Intelligence Hardening

- Original source artifact: MEMCON workflow chain roadmap and T1a through T4
  MEMCON closure artifacts, not a legacy private corpus folder.
- Predecessor intake artifact:
  `docs/reviews/CVF_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_COMPLETION_2026-06-13.md`
- Delta ledger status: DISPATCH_DECLARED_LIMITS - T5 is released only after T4
  closure and only for cross-agent memory consistency contract work.
- Routing matrix status: DISPATCH_DECLARED_LIMITS - runtime storage,
  retrieval behavior, provider proof, public-sync, Policy_Local, memory
  reinjection, and autonomous mutation remain out of scope.
- Semantic sampling status: DISPATCH_DECLARED_LIMITS - worker must include a
  bounded sample packet covering aligned, conflicting, unresolved,
  duplicate/noise, and operator-confirmation rows.
- Rescan intelligence verdict: COMPLETE_WITH_DECLARED_LIMITS

### Original-Intake Delta Ledger

| sampleId | Delta category | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| MEMCON-T5-GC018-D1 | UNCHANGED_FROM_INTAKE | T4 completion next move | T5 requires fresh GC-018 and source-verified work order | GC-018 and work order created | Did dispatch skip T4 release evidence? | PASS |
| MEMCON-T5-GC018-D2 | CHANGED_DISPOSITION | roadmap MEMCON-T5 row | T5 was ready for fresh authorization | status moves to DISPATCHED | Did dispatch claim closure before worker return? | PASS |
| MEMCON-T5-GC018-D3 | NEW_FINDING | T5 field list | doc-only fields need explicit boundary | new doc-only field table added | Are new fields falsely claimed as runtime symbols? | PASS |
| MEMCON-T5-GC018-D4 | REMOVED_OR_REJECTED | claim boundary | runtime/storage/public work excluded | forbidden scope retained | Does dispatch authorize runtime memory mutation? | PASS |

### Follow-Up Routing Matrix

| Route lane | Target | Disposition | Evidence | Next action |
| --- | --- | --- | --- | --- |
| DO_NOW | T5 contract and sample packet | ACCEPT | roadmap MEMCON-T5 detail | Claude implements allowed artifacts |
| SEPARATE_RUNTIME_TRANCHE | runtime memory storage or route wiring | DEFER | GC-018 claim boundary | future authorization only |
| STRATEGIC_OPERATOR_DECISION | Policy_Local PL-S1 and EC/T12 | DEFER | active session parked checkpoint | operator checkpoint later |
| OUT_OF_SCOPE | public-sync and public catalog claim | REJECT | Public Export Disposition | no public action |
| RESOLVED_BY_DESIGN | worker commits | REJECT | `WORKER_MUST_NOT_COMMIT` | Codex reviews and commits |

### Semantic Sampling / Adversarial Review

| sampleId | source section | source claim | disposition checked | adversarial challenge | verdict |
| --- | --- | --- | --- | --- | --- |
| MEMCON-T5-GC018-S1 | schema appendix | `agentSource` already exists | source verification cites field table | Could T5 invent a duplicate agent field? | PASS |
| MEMCON-T5-GC018-S2 | roadmap detail | `agentRole` is required by T5 | doc-only table separates from runtime | Could doc-only field be mistaken for RBAC? | PASS |
| MEMCON-T5-GC018-S3 | T3 contract | no runtime/storage overclaim | claim boundary repeats exclusion | Could sample packet imply durable storage? | PASS |
| MEMCON-T5-GC018-S4 | T4 completion | next move is fresh T5 dispatch | dependency release table cites T4 | Could dispatch rely on chat memory only? | PASS |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| MEMCON-T5 is the next cross-agent consistency tranche after MEMCON-T4 closure | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | lines 378-379, 579-594 | `MEMCON-T5` | MEMCON roadmap | ACCEPT |
| T5 must prevent separate authoritative memories without shared ledger and source-backed reconciliation | `docs/roadmaps/CVF_MEMORY_CONSOLIDATION_WORKFLOW_CHAIN_ROADMAP_2026-06-12.md` | lines 581-594 | `MEMCON-T5 Detail` | MEMCON roadmap | ACCEPT |
| `agentSource` already exists for cross-agent accountability | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | lines 79-93 | `agentSource` | `MemorySignal` field table | ACCEPT |
| source authority is required for candidates and records | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | lines 98-131, 192 | `sourceAuthority` | `MemoryCandidate`, `ConsolidatedMemoryRecord` | ACCEPT |
| conflict records require operator decision handling | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | lines 115, 143, 195 | `conflictSetIds`, `operatorDecision` | MEMCON schema appendix | ACCEPT |
| operator review gating exists before durable promotion | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | lines 119, 168-186 | `operatorReviewRequired`, `OperatorMemoryReviewPacket` | MEMCON schema appendix | ACCEPT |
| claim boundary and public export disposition are existing operator-packet fields | `docs/reference/CVF_MEMORY_CONSOLIDATION_SCHEMA_APPENDIX_2026-06-13.md` | lines 185-186 | `claimBoundary`, `publicExportDisposition` | `OperatorMemoryReviewPacket` | ACCEPT |
| T3 contract parks cross-agent consistency as the MEMCON-T5 lane and forbids runtime/storage overclaim | `docs/reference/CVF_MEMORY_CONSOLIDATION_LEDGER_OPERATOR_PACKET_CONTRACT_2026-06-13.md` | lines 32, 47-58, 219-228 | `MEMCON-T5 lane`, `rawMemoryReleased` | MEMCON-T3 operator packet contract | ACCEPT |
| T4 closure releases MEMCON-T5 only through fresh GC-018 and source-verified work order | `docs/reviews/CVF_MEMCON_T4_RETRIEVAL_PACK_BOUNDARY_CONFORMANCE_COMPLETION_2026-06-13.md` | lines 202-214 | `Next Allowed Move` | MEMCON-T4 completion | ACCEPT |

## New Doc-Only Fields Authorized

These fields are new MEMCON-T5 documentation-contract fields. They are not
claimed as current runtime/source symbols.

| New doc-only field | Roadmap source | Target contract path | Boundary |
| --- | --- | --- | --- |
| `agentRole` | roadmap lines 581-591 | `docs/reference/CVF_MEMORY_CONSOLIDATION_CROSS_AGENT_CONSISTENCY_CONTRACT_2026-06-13.md` | doc-only role label, not runtime RBAC |
| `sourceArtifact` | roadmap lines 581-591 | same | source path/hash/reference, not hidden memory |
| `conflictsWithAgentMemory` | roadmap lines 581-591 | same | explicit conflict pointer, not automatic mutation |
| `resolutionOwner` | roadmap lines 581-591 | same | responsible reviewer/operator, not autonomous resolution |
| `operatorConfirmed` | roadmap lines 581-591 | same | visible confirmation flag, not implied approval |

## Authorized Artifact Set

Claude may create or update only:

- `docs/reference/CVF_MEMORY_CONSOLIDATION_CROSS_AGENT_CONSISTENCY_CONTRACT_2026-06-13.md`;
- `docs/reviews/CVF_MEMCON_T5_CROSS_AGENT_MEMORY_CONSISTENCY_SAMPLE_PACKET_2026-06-13.md`;
- `docs/reviews/CVF_MEMCON_T5_CROSS_AGENT_MEMORY_CONSISTENCY_WORKER_RETURN_2026-06-13.md`;
- the paired work order only if adding worker-return evidence is necessary;
- the parent roadmap row only to mark worker-return status, not final closure.

## Evidence / Verification

Required dispatch verification:

- MEMCON artifact quality checker passes on the dispatch package.
- work-order dispatch quality checker passes on the dispatch package.
- pre-dispatch autorun gate passes on the dispatch package.
- reviewer-fast and pre-commit gates pass before Codex commits.

Required worker verification is defined in the paired work order.

## Claim Boundary

This GC-018 authorizes bounded MEMCON-T5 contract and fixture work only. It
does not claim runtime memory storage, cross-agent memory consistency is
implemented, semantic correctness is proven, retrieval behavior changed,
Policy_Local is ready, public catalog export exists, provider/API proof exists,
OCR is available, memory reinjection is authorized, high-risk promotion is
authorized, or autonomous mutation is authorized.

rawMemoryReleased=false

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

This is a private provenance dispatch baseline. No public-sync artifact or
public catalog claim is authorized by this tranche.
