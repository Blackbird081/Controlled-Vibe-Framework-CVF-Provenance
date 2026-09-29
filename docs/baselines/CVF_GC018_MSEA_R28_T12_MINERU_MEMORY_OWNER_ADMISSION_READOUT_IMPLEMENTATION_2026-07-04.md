# CVF GC-018 Baseline - MSEA R28 T12 MinerU Memory Owner Admission Readout Implementation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-07-04

docType: baseline

Batch ID: MSEA-R28-T12-MINERU-MEMORY-OWNER-ADMISSION-READOUT-IMPLEMENTATION

rawMemoryReleased: false

dispatchBaseHead: 89c356a4

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: delegated worker role

## Purpose

Authorize a bounded MSEA-R28-T12 implementation tranche that adds a
deterministic metadata-only memory-owner admission readout helper over the
existing MinerU memory-safe candidate contract. The readout may verify the T11
admission criteria from metadata fields, but it must not write memory/RAG,
read private/generated content, run MinerU, or claim production workflow
readiness.

## Decision Baseline / Proposed Tranche

| Field | Value |
| --- | --- |
| Proposed tranche | MSEA-R28-T12 MinerU Memory Owner Admission Readout Implementation |
| Baseline decision | DISPATCH_READY for a no-commit worker implementation tranche |
| Selected path | deterministic metadata-only admission readout helper and focused tests |
| Rejected path | direct memory/RAG write, runtime execution, private/generated content read, provider/live proof, public-sync, checker/hook edit, or production workflow-chain claim |
| Dependency release basis | accepted T11 matrix and worker return at material commit `dec53037`, plus session-sync routing at `89c356a4` |

## Scope / Target / Owner Boundary

Allowed scope:

- modify `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`;
- modify `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`;
- create `docs/reviews/CVF_MSEA_R28_T12_MINERU_MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`;
- implement a deterministic metadata-only admission readout dataclass, builder,
  and payload renderer from `MineruMemorySafeCandidateContract`;
- keep `memoryWriteAuthorized` false and preserve the T11/T27 requirement that
  a separate future memory-write work order is required before any memory/RAG
  write.

Forbidden scope:

- no MinerU command, model/cache mutation, parser/OCR/VLM/API/router/Gradio/
  Docker/WSL execution, local service startup, runtime smoke, or provider/live
  proof;
- no private source document body read and no generated output content read,
  quotation, copy, import, stage, or commit;
- no Candidate Group A import, committed runtime receipt instance, memory-layer
  write, RAG write, adapter implementation, S3, Web, MCP, model-router,
  package lifecycle, action-authority, public-sync, standalone PDF app,
  legal/use-case deep dive, extraction-accuracy claim, document-truth claim,
  legal advice quality claim, current-law correctness claim, production
  workflow-chain claim, checker edit, hook wiring, session-sync by worker,
  worker stage, worker commit, or push.

Risk ceiling: R1 deterministic local source/test implementation; no
runtime/provider/private-data/public action.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R28-T11 material closure | `docs/reviews/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_WORKER_RETURN_2026-07-04.md` and material commit `dec53037` | ACCEPT |
| R28-T11 companion design matrix | `docs/reference/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_MATRIX_2026-07-04.md` at accepted closure commit `dec53037` | ACCEPT |
| R28-T11 session-sync routing | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` at session-sync commit `89c356a4` routes next move to T12 work-order authoring if selected | ACCEPT |
| Operator lane selection | operator requested multi-role completion of MSEA-R28-T12 in this session | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `89c356a4` before authoring | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T12 --title "MinerU Memory Owner Admission Readout Implementation" --date 2026-07-04 --base 89c356a4 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled T12 source verification, dependency release, bounded source/test implementation scope, no-memory-write boundary, worker manifest, and handoff route |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, dispatch-envelope, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `MEMORY_OWNER_ADMISSION_READOUT`; `MEMORY_OWNER_ADMISSION_READY_FOR_REVIEW`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T12_DISPATCH`; `FUTURE_MEMORY_WRITE_WORK_ORDER_REQUIRED` |
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
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Preflight Checks; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Source Verification Block; New Implementation Symbols; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; External Knowledge Intake Routing; Foundation Storage Layout Block; Current Runtime Freshness Verification; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; Resolver query; Returned defects: NONE_RETURNED; Delta Execution Claim Boundary Control Block; Public Export Disposition; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers this baseline only; worker-created return requires its own source and checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Active session routing releases T12 work-order authoring only after T11 closure and keeps memory/RAG write unauthorized. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` field | `nextAllowedMove` | active session bootstrap read model | ACCEPT |
| T11 matrix defines admission criteria for receipt, quality, source pointer, downstream-use status, claim boundary, private-output boundary, memory-write authority, and candidate readiness. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_MATRIX_2026-07-04.md` | lines 40-47 | `Admission Design Matrix` | MSEA-R28-T11 admission design matrix | ACCEPT |
| T11 selected design-only disposition and requires future memory-owner implementation authority. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_MATRIX_2026-07-04.md` | lines 53-56 | `MEMORY_OWNER_ADMISSION_DESIGN_ONLY`; `FUTURE_MEMORY_OWNER_IMPLEMENTATION_WORK_ORDER_REQUIRED` | MSEA-R28-T11 selected disposition | ACCEPT |
| R27 requires memory-safe candidates to carry receipt, quality, source pointer, downstream-use status, and claim boundary before memory admission. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 74 and 86-87 | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED` | MSEA-R27 decision ledger | ACCEPT |
| Receipt writer owns the memory-safe candidate contract dataclass and existing payload renderer. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 98 and 358 | `MineruMemorySafeCandidateContract`; `mineru_memory_safe_candidate_contract_payload` | MinerU metadata receipt writer | ACCEPT |
| Receipt writer validates bounded identifiers, source pointers, held downstream release, and memory-safe candidate contracts. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 119-155 and 295-352 | `_validate_safe_id`; `_validate_quality_source_pointer`; `build_mineru_memory_safe_candidate_contract` | MinerU metadata receipt writer validation | ACCEPT |
| Current focused tests cover deterministic memory-safe candidate contracts and unsafe receipt rejection. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 255-333 | `test_memory_safe_candidate_contract_is_deterministic_and_metadata_only`; `test_memory_safe_candidate_contract_fails_closed_for_unsafe_receipts` | MinerU metadata receipt writer tests | ACCEPT |

## New Implementation Symbols

| Symbol | Type | Purpose | Source status |
| --- | --- | --- | --- |
| `MEMORY_OWNER_ADMISSION_READOUT_VERSION` | constant | stable readout version for T12 metadata-only admission payloads | NEW_IMPLEMENTATION_SYMBOL |
| `MEMORY_WRITE_NOT_AUTHORIZED_BY_T12` | constant | stable T12 memory-write hold token | NEW_IMPLEMENTATION_SYMBOL |
| `MineruMemoryOwnerAdmissionReadout` | dataclass | metadata-only admission readout derived from a memory-safe candidate contract | NEW_IMPLEMENTATION_SYMBOL |
| `build_mineru_memory_owner_admission_readout` | helper function | verify T11 admission criteria from existing candidate contract metadata | NEW_IMPLEMENTATION_SYMBOL |
| `mineru_memory_owner_admission_readout_payload` | helper function | render stable camelCase readout payload without content-bearing fields | NEW_IMPLEMENTATION_SYMBOL |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED
priorVerificationArtifact: `docs/reference/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_MATRIX_2026-07-04.md`
priorVerificationAnchor: `dec53037`
freshRecomputeRequired: true
recomputeReason: T12 changes source/test behavior, so source facts and focused tests must be recomputed against current HEAD.
unicodePathHandling: use literal paths and UTF-8-safe command output; do not normalize or rewrite filenames.
extractedTextAuthority: N/A with reason - no extracted text, private/generated output text, or document body is source authority for T12.

| Field | Value |
| --- | --- |
| verificationMode | RECOMPUTE_REQUIRED |
| priorVerificationArtifact | `docs/reference/CVF_MSEA_R28_T11_MINERU_MEMORY_OWNER_ADMISSION_DESIGN_MATRIX_2026-07-04.md` |
| priorVerificationAnchor | `dec53037` |
| freshRecomputeRequired | true |
| recomputeReason | T12 changes source/test behavior, so source facts and focused tests must be recomputed against current HEAD |
| unicodePathHandling | use literal paths and UTF-8-safe command output; do not normalize or rewrite filenames |
| extractedTextAuthority | N/A with reason - no extracted text, private/generated output text, or document body is source authority for T12 |

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
| --- | --- | --- |
| Dispatch base | `git rev-parse --short HEAD` returned `89c356a4` before authoring | ACCEPT |
| Worktree state | `git status --short --untracked-files=all` was empty before dispatch authoring | ACCEPT |
| Existing T12 artifact collision | `Test-Path` returned false for planned baseline, work order, and worker-return paths | ACCEPT |
| Runtime execution | No MinerU/provider/live/runtime command is authorized by this baseline | NOT_APPLICABLE_WITH_REASON |

## Acceptance Criteria

| ID | Criterion | Evidence required |
| --- | --- | --- |
| AC1 | Worker adds deterministic memory-owner admission readout helper and payload renderer in the allowed receipt writer source only | source diff and focused tests |
| AC2 | Readout verifies metadata-only T11 gates: candidate id, receipt id, input digest, quality report ref, source pointer, downstream-use status, claim boundary, output-content-read false, and memory-write authorization false | focused tests |
| AC3 | Readout payload omits content-bearing fields such as extracted text, OCR text, document body, memory record body, vector content, and output file names | focused tests |
| AC4 | Worker creates the named worker return and leaves changes uncommitted | worker return, git status, and HEAD evidence |
| AC5 | Focused pytest, worker-return fast gate, pre-implementation autorun, reviewer steward, and material pre-commit hook pass before closure | command evidence |

## Claim Boundary

This GC-018 baseline authorizes only a deterministic local metadata-only
admission readout implementation, focused tests, and worker return. It does
not authorize MinerU runtime execution, private/generated content read,
Candidate Group A import, memory/RAG write, provider/live proof, public-sync,
standalone app work, legal/use-case deep dive, extraction accuracy, document
truth, legal quality, current-law correctness, workflow-chain production
readiness, checker/hook edit, session-sync by worker, worker stage, worker
commit, or push.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | MSEA source-mirror learning -> R27 plane route -> R28 receipt/checker/helper chain -> R28-T12 memory-owner admission readout implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline and paired work order |
| Disposition | ADAPT: convert accepted T11 admission design evidence into a bounded metadata-only admission readout helper |
| Claim boundary | no MinerU runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, checker/hook/session edit, or product-app claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T12 GC-018 dispatch baseline for deterministic metadata-only admission readout implementation |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, memory-store, RAG, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime, memory, provider, public, or external action is executed or observed. |
| invocationBoundary | local document authoring and governance gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized or claimed. |
| claimLanguage | baseline dispatch evidence only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router/memory behavior without fresh source-verified authorization. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T12 dispatch material is private provenance governance material only.
No public-sync export, public repository commit, or public catalog claim is
included.
