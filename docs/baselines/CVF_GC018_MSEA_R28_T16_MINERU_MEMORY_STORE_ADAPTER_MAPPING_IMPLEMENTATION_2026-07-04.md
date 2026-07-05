# CVF GC-018 Baseline - MSEA R28 T16 MinerU Memory Store Adapter Mapping Implementation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-07-04

docType: baseline

Batch ID: MSEA-R28-T16-MINERU-MEMORY-STORE-ADAPTER-MAPPING-IMPLEMENTATION

rawMemoryReleased: false

dispatchBaseHead: c9528ec8

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: delegated worker role

## Decision Baseline / Proposed Tranche

| Field | Value |
| --- | --- |
| Proposed tranche | MSEA-R28-T16 MinerU Memory Store Adapter Mapping Implementation |
| Baseline decision | DISPATCH_READY for a no-commit source/test mapping implementation tranche |
| Selected path | implement a deterministic summary-only durable-memory write-input candidate mapper from the T14 MinerU memory-record candidate |
| Rejected path | actual memory/RAG write, durable-store invocation, vectorization, retrieval, runtime execution, private/generated content read, provider/live proof, public-sync, or production workflow-chain claim |
| Dependency release basis | accepted T15 closure at material commit `50afaa0f`, plus session-sync routing at `c9528ec8` |

## Purpose

Authorize a bounded T16 implementation tranche that maps an accepted
metadata-only MinerU memory-record candidate into a summary-only durable-memory
write-input candidate payload. The worker must not call the durable memory
store, write memory/RAG, read private/generated content, or claim retrieval or
production workflow readiness.

## Scope / Target / Owner Boundary

Allowed scope:

- modify `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`;
- modify `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`;
- create `docs/reviews/CVF_MSEA_R28_T16_MINERU_MEMORY_STORE_ADAPTER_MAPPING_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`;
- add deterministic constants, dataclass, builder, and payload renderer for a
  summary-only durable-memory write-input candidate;
- add focused tests proving deterministic mapping, no raw/private/generated
  content fields, no durable-store invocation, and fail-closed policy gates.

Forbidden scope:

- no durable memory-store invocation, memory/RAG write, vectorization,
  retrieval, provider/live proof, MinerU runtime execution, private/generated
  content read, Candidate Group A import, public-sync, Web/MCP/model-router
  work, dependency install, standalone app, legal/use-case deep dive,
  extraction-accuracy claim, document-truth claim, legal-quality claim,
  current-law correctness claim, production workflow-chain claim, checker/hook/
  session/handoff/AGENTS.md edit by worker, worker stage, worker commit, or
  push.

Risk ceiling: local deterministic mapping helper/test behavior and worker
return only.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R28-T15 material closure | `docs/reviews/CVF_MSEA_R28_T15_MINERU_CANDIDATE_REVIEW_AND_STORE_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md` and material commit `50afaa0f` | ACCEPT |
| R28-T15 selected T16 route | `CVF_SESSION/state/entries/mseaR28T15MineruCandidateReviewAndStoreWriteAuthorityDecisionClosure20260704.json` records `MEMORY_STORE_WRITE_WORK_ORDER_AUTHORING_READY` and `T16_MAPPING_REQUIRED_BEFORE_ANY_WRITE` | ACCEPT |
| Current session routing | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` at session-sync commit `c9528ec8` routes next move to T16 work-order authoring | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `c9528ec8` before authoring | ACCEPT |

## Roadmap-to-Work-Order Trace Matrix

| Source requirement | T16 work-order handling |
| --- | --- |
| T15 releases T16 authoring only | T16 dispatch is fresh GC-018/work-order and keeps worker no-commit |
| T15 requires adapter mapping before any write | T16 scope is deterministic mapping helper/test, not durable-store invocation |
| T15 keeps actual memory/RAG write held | T16 forbidden scope blocks store calls, writes, vectorization, retrieval, and runtime proof |
| R24-T4 private-output policy forbids private/generated output content | T16 mapping must use only metadata fields already present in the T14 candidate |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T16 --title "MinerU Memory Store Adapter Mapping Implementation" --date 2026-07-04 --base c9528ec8 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | source/test WORKER_MUST_NOT_COMMIT mapping implementation tranche |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled T16 dependency release, source verification, allowed source/test scope, no-memory-write boundary, worker manifest, handoff route, and actual-write hold |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, dispatch-envelope, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `MEMORY_STORE_ADAPTER_MAPPING_IMPLEMENTED`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T16_MAPPING_ONLY`; `MineruDurableMemoryWriteInputCandidate`; `build_mineru_durable_memory_write_input_candidate`; `mineru_durable_memory_write_input_candidate_payload` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router/memory behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF-specific extra instruction is required beyond guard orientation, literal-format gotchas, source verification, checker read-ahead, and no-commit discipline. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_foundation_storage_layout.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Preflight Checks; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Source Verification Block; New Doc-Only Fields; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; External Knowledge Intake Routing; Foundation Storage Layout Block; Current Runtime Freshness Verification; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; Resolver query; Returned defects: NONE_RETURNED; Delta Execution Claim Boundary Control Block; Public Export Disposition; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers this baseline only; worker-created return requires its own source and checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T15 selected T16 authoring-ready route while keeping actual write unauthorized. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T15_MINERU_CANDIDATE_REVIEW_AND_STORE_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md` | Decision Summary | `MEMORY_STORE_WRITE_WORK_ORDER_AUTHORING_READY`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T15_DECISION_ONLY` | T15 decision matrix | ACCEPT |
| T14 source exposes a metadata-only memory-record candidate and payload renderer. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 143, 509, and 591-602 | `MineruMemoryRecordCandidate`; `build_mineru_memory_record_candidate`; `mineru_memory_record_candidate_payload` | MinerU metadata receipt writer | ACCEPT |
| T14 source keeps downstream release held and memory write unauthorized. | VALUE_SET | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 22, 25, 157-159, and 535 | `DOWNSTREAM_RELEASE_HELD`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T14`; `future_authority_required` | MinerU metadata receipt writer | ACCEPT |
| T14 tests cover deterministic metadata-only candidate behavior and fail-closed unsafe readouts. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 470-587 | `test_memory_record_candidate_is_deterministic_and_metadata_only`; `test_memory_record_candidate_fails_closed_for_unsafe_readouts` | MinerU receipt writer tests | ACCEPT |
| Durable memory store write input requires id, scope, actor, actor role, summary, optional policy decision, authorization, and provenance score. | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 52-63 and 195-203 | `DurableMemoryWriteInput`; `policyDecision`; `actorAuthorized`; `provenanceScore` | Learning Plane durable memory store | ACCEPT |
| Durable memory store rejects raw payload-like fields and low provenance before persistence. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 98, 137-143, and 252-263 | `MIN_PROVENANCE_SCORE`; `hasRawPayload`; `raw_memory_payload_rejected`; `low_provenance_score` | Learning Plane durable memory store | ACCEPT |
| Durable memory receipt remains summary-only with no raw release or reinjection. | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 35-49 and 160-175 | `summaryOnly`; `canReinject`; `rawMemoryReleased` | Learning Plane durable memory receipt | ACCEPT |
| Runtime memory hierarchy defines actor-role values and durable actor authorization lanes. | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 10-18 values `OPERATOR`, `GOVERNOR`, `HUMAN`, `BUILDER`, `AI_AGENT`, `REVIEWER`, `SERVICE_AGENT`, `OBSERVER`, `ANALYST`, `unknown`; lines 173-204 durable actor lanes and `m1_durable_cross_session` | `RuntimeMemoryActorRole`; `allowedActors`; `m1_durable_cross_session` | Runtime memory hierarchy | ACCEPT |
| R27 scan-to-memory route requires receipt, quality, source pointer, downstream-use status, and claim boundary before future memory write. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 71-87 | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED` | R27 decision ledger | ACCEPT |
| R24-T4 private-output policy keeps private/generated output content out of successor routing. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 43-56 and 212 | `sourceInputSlot`; `privateOutputDisposition`; policy claim boundary | R24-T4 policy reference | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Source status |
| --- | --- | --- |
| `MEMORY_STORE_ADAPTER_MAPPING_IMPLEMENTED` | proposed T16 implementation disposition token | DOC_ONLY_NEW |
| `MEMORY_WRITE_NOT_AUTHORIZED_BY_T16_MAPPING_ONLY` | proposed T16 memory-write hold token | DOC_ONLY_NEW |
| `MineruDurableMemoryWriteInputCandidate` | proposed Python dataclass for summary-only durable write input candidate | DOC_ONLY_NEW |
| `build_mineru_durable_memory_write_input_candidate` | proposed Python builder from T14 candidate to durable write input candidate | DOC_ONLY_NEW |
| `mineru_durable_memory_write_input_candidate_payload` | proposed Python payload renderer for stable camelCase output | DOC_ONLY_NEW |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED
priorVerificationArtifact: `docs/reference/CVF_MSEA_R28_T15_MINERU_CANDIDATE_REVIEW_AND_STORE_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md`
priorVerificationAnchor: `50afaa0f`
freshRecomputeRequired: true
recomputeReason: T16 authorizes source/test implementation, so consumed symbols and durable-store owner surfaces must be source-verified against current HEAD.
unicodePathHandling: use literal paths and UTF-8-safe command output; do not normalize or rewrite filenames.
extractedTextAuthority: N/A with reason
extractedTextAuthorityReason: no extracted text, private/generated output text, or document body is source authority for T16.

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
| --- | --- | --- |
| Dispatch base | `git rev-parse --short HEAD` returned `c9528ec8` before authoring | ACCEPT |
| Worktree state | `git status --short` was empty before dispatch authoring | ACCEPT |
| Existing T16 artifact collision | planned baseline and work-order paths were absent before authoring | ACCEPT |
| Runtime execution | No MinerU/provider/live/runtime/memory-store command is authorized by this baseline | NOT_APPLICABLE_WITH_REASON |

## Acceptance Criteria

| ID | Criterion | Evidence required |
| --- | --- | --- |
| AC1 | Worker changes only allowed receipt-writer source, focused receipt-writer test, and T16 worker return | git status and worker return |
| AC2 | Implementation creates a deterministic summary-only durable write-input candidate mapper | focused tests and source diff |
| AC3 | Candidate payload excludes raw OCR, extracted text, document body, private/generated output content, vector content, and durable-store write receipts | focused tests |
| AC4 | T16 does not invoke durable memory store, write memory/RAG, vectorize, retrieve, run MinerU, or edit session/checker/hook/public paths | worker return and git status |
| AC5 | Worker-return fast gate, pre-implementation autorun, reviewer steward, and material pre-commit hook pass before closure | command evidence |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | MSEA source-mirror learning -> R27 plane route -> R28 receipt/checker/helper chain -> T15 store-write authority decision -> T16 adapter mapping |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline and paired work order |
| Disposition | ADAPT accepted T15 authoring-ready route into a bounded source/test mapping implementation dispatch |
| Claim boundary | no MinerU runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, checker/hook/session edit, or product-app claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T16 GC-018 dispatch baseline for memory-store adapter mapping implementation |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, memory-store write, RAG, provider, or public behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime or memory-store receipt is created or consumed. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime, memory, provider, public, external, or private-content action is executed or observed. |
| invocationBoundary | source/test mapping implementation dispatch and governance gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized or claimed. |
| claimLanguage | baseline dispatch evidence only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router/memory behavior without fresh source-verified authorization. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T16 dispatch material is private provenance governance material only.
No public-sync export, public repository commit, or public catalog claim is
included.

## Claim Boundary

This GC-018 baseline authorizes only a bounded source/test implementation work
order for a deterministic summary-only durable-memory write-input candidate
mapper plus worker return. It does not authorize actual memory/RAG write,
durable-store invocation, vectorization, retrieval, checker/hook edits, MinerU
runtime execution, private/generated content read, Candidate Group A import,
provider/live proof, public-sync, standalone app work, legal/use-case deep
dive, extraction accuracy, document truth, legal quality, current-law
correctness, workflow-chain production readiness, session-sync by worker,
worker stage, worker commit, or push.
