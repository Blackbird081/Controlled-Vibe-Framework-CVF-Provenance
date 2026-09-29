# CVF GC-018 Baseline - MSEA R28 T14 MinerU Memory Record Candidate Builder

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-07-04

docType: baseline

Batch ID: MSEA-R28-T14-MINERU-MEMORY-RECORD-CANDIDATE-BUILDER

rawMemoryReleased: false

dispatchBaseHead: ef99f417

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: delegated worker role

## Decision Baseline / Proposed Tranche

| Field | Value |
| --- | --- |
| Proposed tranche | MSEA-R28-T14 MinerU Memory Record Candidate Builder |
| Baseline decision | DISPATCH_READY for a no-commit metadata-only source/test implementation tranche |
| Selected path | deterministic local helper derived from accepted T12 admission readout fields |
| Rejected path | direct memory/RAG write, memory store adapter, runtime execution, private/generated content read, provider/live proof, public-sync, checker/hook edit, or production workflow-chain claim |
| Dependency release basis | accepted T13 authority decision at material commit `0002de2d`, plus session-sync routing at `ef99f417` |

## Purpose

Authorize a bounded T14 implementation tranche for a deterministic
metadata-only memory-record candidate builder. The worker may add a local
candidate dataclass/helper/payload and focused tests in the existing MinerU
metadata receipt writer module only. T14 must not write memory/RAG, create a
store adapter, read private/generated content, run MinerU, or claim production
workflow readiness.

## Scope / Target / Owner Boundary

Allowed scope:

- edit `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`;
- edit `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`;
- create `docs/reviews/CVF_MSEA_R28_T14_MINERU_MEMORY_RECORD_CANDIDATE_BUILDER_WORKER_RETURN_2026-07-04.md`;
- implement a deterministic metadata-only memory-record candidate builder from
  accepted T12 admission readout fields;
- preserve actual memory/RAG write as unauthorized.

Forbidden scope:

- no memory/RAG store write, store adapter, vectorization, retrieval, provider
  call, MinerU runtime execution, private/generated content read, Candidate
  Group A import, public-sync, checker/hook/session edit, Web/MCP/model-router
  work, standalone app, legal/use-case deep dive, extraction-accuracy claim,
  document-truth claim, legal-quality claim, current-law correctness claim,
  production workflow-chain claim, worker stage, worker commit, or push.

Risk ceiling: local deterministic metadata helper and focused tests only.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R28-T13 material closure | `docs/reviews/CVF_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md` and material commit `0002de2d` | ACCEPT |
| R28-T13 selected route | `docs/reference/CVF_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md` selected `MEMORY_RECORD_CANDIDATE_BUILDER_READY` | ACCEPT |
| R28-T13 closure state entry | `CVF_SESSION/state/entries/mseaR28T13MineruMemoryWriteAuthorityDecisionClosure20260704.json` records T14 work-order authoring release and T16 write hold | ACCEPT |
| Current session routing | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` at session-sync commit `ef99f417` routes next move to T14 work-order authoring | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `ef99f417` before authoring | ACCEPT |

## Roadmap-to-Work-Order Trace Matrix

| Source requirement | T14 work-order handling |
| --- | --- |
| T13 releases only future metadata-only candidate-builder work | T14 scope is source/test helper implementation only |
| T13 keeps actual memory/RAG write held | T14 forbidden scope blocks memory/RAG write and store adapter work |
| T14 requires fresh GC-018/source-verified work order before implementation | This baseline pairs with the T14 work order and must pass pre-dispatch gates before worker execution |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T14 --title "MinerU Memory Record Candidate Builder" --date 2026-07-04 --base ef99f417 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | source/test WORKER_MUST_NOT_COMMIT implementation tranche |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled T14 source verification, dependency release, helper/test scope, no-memory-write boundary, and handoff route |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, dispatch-envelope, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `MineruMemoryRecordCandidate`; `build_mineru_memory_record_candidate`; `mineru_memory_record_candidate_payload`; `MEMORY_RECORD_CANDIDATE_READY_FOR_REVIEW`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T14_CANDIDATE_ONLY` |
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
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Preflight Checks; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Source Verification Block; New Source Symbols; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; External Knowledge Intake Routing; Foundation Storage Layout Block; Current Runtime Freshness Verification; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; Resolver query; Returned defects: NONE_RETURNED; Delta Execution Claim Boundary Control Block; Public Export Disposition; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers this baseline only; worker-created return requires its own source and checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T13 selected the metadata-only memory-record candidate builder route. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md` | lines 49-53 | `selectedRoute`; `t14Disposition` | T13 decision matrix | ACCEPT |
| T13 closure keeps actual memory/RAG write held and T16 blocked pending store-write authority. | VALUE_SET | `CVF_SESSION/state/entries/mseaR28T13MineruMemoryWriteAuthorityDecisionClosure20260704.json` | `selectedRoute`; `t16Disposition` fields | `MEMORY_RECORD_CANDIDATE_BUILDER_READY`; `T16_ACTUAL_MEMORY_RAG_WRITE_HELD_PENDING_SOURCE_BACKED_STORE_WRITE_AUTHORITY` | active session state entry | ACCEPT |
| Receipt writer exposes the T12 admission readout dataclass consumed by T14. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 120-136 | `MineruMemoryOwnerAdmissionReadout` | MinerU metadata receipt writer | ACCEPT |
| Receipt writer exposes the T12 readout builder and payload renderer. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 403 and 462-482 | `build_mineru_memory_owner_admission_readout`; `mineru_memory_owner_admission_readout_payload` | MinerU metadata receipt writer | ACCEPT |
| Existing T12 readout keeps output content unread and memory write unauthorized. | VALUE_SET | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 131-135 | `output_content_read`; `memory_write_authorized`; `memory_write_disposition`; `future_authority_required` | MinerU metadata receipt writer | ACCEPT |
| Focused receipt-writer tests already cover deterministic metadata-only admission readout behavior and unsafe candidate failures. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 343-367 and 449-456 | `test_memory_owner_admission_readout_is_deterministic_and_metadata_only`; `test_memory_owner_admission_readout_fails_closed_for_unsafe_candidates` | MinerU receipt writer tests | ACCEPT |

## New Source Symbols

| Symbol | Purpose | Source status |
| --- | --- | --- |
| `MineruMemoryRecordCandidate` | metadata-only candidate record for future memory-owner/store review | DOC_ONLY_NEW |
| `build_mineru_memory_record_candidate` | deterministic builder from T12 admission readout | DOC_ONLY_NEW |
| `mineru_memory_record_candidate_payload` | stable camelCase payload renderer | DOC_ONLY_NEW |
| `MEMORY_RECORD_CANDIDATE_READY_FOR_REVIEW` | candidate disposition token | DOC_ONLY_NEW |
| `MEMORY_WRITE_NOT_AUTHORIZED_BY_T14_CANDIDATE_ONLY` | explicit T14 hold on actual memory/RAG write | DOC_ONLY_NEW |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED
priorVerificationArtifact: `docs/reference/CVF_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md`
priorVerificationAnchor: `0002de2d`
freshRecomputeRequired: true
recomputeReason: T14 modifies source/test behavior, so all consumed symbols and new symbols must be source-verified against current HEAD.
unicodePathHandling: use literal paths and UTF-8-safe command output; do not normalize or rewrite filenames.
extractedTextAuthority: N/A with reason - no extracted text, private/generated output text, or document body is source authority for T14.

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
| --- | --- | --- |
| Dispatch base | `git rev-parse --short HEAD` returned `ef99f417` before authoring | ACCEPT |
| Worktree state | `git status --short --untracked-files=all` was empty before dispatch authoring | ACCEPT |
| Existing T14 artifact collision | planned baseline, work order, and worker-return paths were absent before authoring | ACCEPT |
| Runtime execution | No MinerU/provider/live/runtime command is authorized by this baseline | NOT_APPLICABLE_WITH_REASON |

## Acceptance Criteria

| ID | Criterion | Evidence required |
| --- | --- | --- |
| AC1 | Worker changes only the receipt writer source, focused receipt writer tests, and T14 worker return | git status and worker return |
| AC2 | Candidate builder is deterministic and metadata-only | focused tests |
| AC3 | Payload omits output file names and content-bearing fields | focused tests |
| AC4 | Actual memory/RAG write remains unauthorized | source constants, payload, tests |
| AC5 | Worker-return fast gate, focused pytest, pre-implementation autorun, reviewer steward, and material pre-commit hook pass before closure | command evidence |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | MSEA source-mirror learning -> R27 plane route -> R28 receipt/checker/helper chain -> T13 decision -> T14 metadata-only candidate builder |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline and paired work order |
| Disposition | ADAPT accepted T13 evidence into a bounded metadata-only candidate-builder implementation |
| Claim boundary | no MinerU runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, checker/hook/session edit, or product-app claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T14 GC-018 dispatch baseline for metadata-only candidate-builder implementation |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, memory-store, RAG, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime, memory, provider, public, or external action is executed or observed. |
| invocationBoundary | local source/test implementation and governance gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized or claimed. |
| claimLanguage | baseline dispatch evidence only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router/memory behavior without fresh source-verified authorization. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T14 dispatch material is private provenance governance material only.
No public-sync export, public repository commit, or public catalog claim is
included.

## Claim Boundary

This GC-018 baseline authorizes only a local deterministic metadata-only
candidate-builder implementation and focused tests after the paired work order
passes dispatch gates. It does not authorize actual memory/RAG write,
checker/hook edits, MinerU runtime execution, private/generated content read,
Candidate Group A import, provider/live proof, public-sync, standalone app
work, legal/use-case deep dive, extraction accuracy, document truth, legal
quality, current-law correctness, workflow-chain production readiness,
session-sync by worker, worker stage, worker commit, or push.
