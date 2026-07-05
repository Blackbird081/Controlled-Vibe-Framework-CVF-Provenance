# CVF GC-018 Baseline - MSEA R28 T13 MinerU Memory Write Authority Decision

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-07-04

docType: baseline

Batch ID: MSEA-R28-T13-MINERU-MEMORY-WRITE-AUTHORITY-DECISION

rawMemoryReleased: false

dispatchBaseHead: 4cd04307

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: delegated worker role

## Purpose

Authorize a bounded MSEA-R28-T13 decision tranche that converts the accepted
T12 memory-owner admission readout into a source-verified memory-write
authority decision matrix. T13 may decide whether the next tranche can build a
deterministic memory-record candidate from metadata-only fields. T13 must not
write memory/RAG, create a store adapter, read private/generated content, run
MinerU, or claim production workflow readiness.

## Decision Baseline / Proposed Tranche

| Field | Value |
| --- | --- |
| Proposed tranche | MSEA-R28-T13 MinerU Memory Write Authority Decision |
| Baseline decision | DISPATCH_READY for a no-commit docs-only worker decision tranche |
| Selected path | source-verified decision matrix over T12 readout evidence |
| Rejected path | direct memory/RAG write, runtime execution, private/generated content read, provider/live proof, public-sync, checker/hook edit, source/test implementation, or production workflow-chain claim |
| Dependency release basis | accepted T12 readout implementation at material commit `91cc1422`, plus session-sync routing at `4cd04307` |

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reference/CVF_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md`;
- create `docs/reviews/CVF_MSEA_R28_T13_MINERU_MEMORY_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md`;
- decide one bounded route token for the next tranche;
- source-verify the decision against T12 readout evidence, current session
  next-move authority, and the current receipt writer symbols;
- keep memory/RAG write unauthorized in T13 itself.

Forbidden scope:

- no source, test, checker, hook, session-state, active handoff, AGENTS.md,
  runtime adapter, Web, MCP, model-router, package lifecycle, public-sync,
  standalone app, memory store, RAG store, or provider/live implementation;
- no MinerU command, model/cache mutation, parser/OCR/VLM/API/router/Gradio/
  Docker/WSL execution, local service startup, runtime smoke, or provider/live
  proof;
- no private source document body read and no generated output content read,
  quotation, copy, import, stage, or commit;
- no Candidate Group A import, committed runtime receipt instance, extraction
  accuracy claim, document truth claim, legal advice quality claim,
  current-law correctness claim, production workflow-chain claim, worker stage,
  worker commit, or push.

Risk ceiling: R0/R1 documentation-only decision work; no runtime/provider/private-data/public action.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R28-T12 material closure | `docs/reviews/CVF_MSEA_R28_T12_MINERU_MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md` and material commit `91cc1422` | ACCEPT |
| R28-T12 closure state entry | `CVF_SESSION/state/entries/mseaR28T12MineruMemoryOwnerAdmissionReadoutImplementationClosure20260704.json` records `MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTED` and `FUTURE_MEMORY_WRITE_WORK_ORDER_REQUIRED` | ACCEPT |
| Current session routing | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` at session-sync commit `4cd04307` routes next move to fresh memory-write authority work-order authoring if selected | ACCEPT |
| Operator lane selection | operator requested T13-T16 sequence; T13 is the authority decision start point | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `4cd04307` before authoring | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T13 --title "MinerU Memory Write Authority Decision" --date 2026-07-04 --base 4cd04307 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | docs-only WORKER_MUST_NOT_COMMIT decision tranche |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled T13 source verification, dependency release, docs-only matrix scope, no-memory-write boundary, worker manifest, and handoff route |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, dispatch-envelope, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `MEMORY_WRITE_AUTHORITY_DECISION`; `MEMORY_RECORD_CANDIDATE_BUILDER_READY`; `MEMORY_WRITE_STILL_NOT_AUTHORIZED_BY_T13`; `FUTURE_MEMORY_RECORD_CANDIDATE_WORK_ORDER_REQUIRED` |
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
| claimBoundary | This read-ahead covers this baseline only; worker-created matrix and return require their own source and checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Current session routing allows a fresh memory-write authority work order if selected, while memory/RAG write remains held. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` field | `nextAllowedMove` | active session bootstrap read model | ACCEPT |
| T12 closure recorded accepted admission readout implementation and future memory-write work-order requirement. | VALUE_SET | `CVF_SESSION/state/entries/mseaR28T12MineruMemoryOwnerAdmissionReadoutImplementationClosure20260704.json` | lines 20-25 | `selectedImplementationDisposition`; `futureAuthorityRequired` | active session state entry | ACCEPT |
| T12 worker return states future memory write still requires a separate fresh authority packet. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_T12_MINERU_MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md` | lines 68-73 and 87-90 | `FUTURE_MEMORY_WRITE_WORK_ORDER_REQUIRED` | T12 worker return | ACCEPT |
| Receipt writer owns the accepted T12 readout dataclass and payload renderer. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 120 and 462 | `MineruMemoryOwnerAdmissionReadout`; `mineru_memory_owner_admission_readout_payload` | MinerU metadata receipt writer | ACCEPT |
| Receipt writer keeps T12 memory write unauthorized through a stable token. | VALUE_SET | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 23 and 133 | `MEMORY_WRITE_NOT_AUTHORIZED_BY_T12`; `memory_write_disposition` | MinerU metadata receipt writer | ACCEPT |
| Receipt writer exposes `future_authority_required` on the T12 readout. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 135 and 472 | `future_authority_required`; `futureAuthorityRequired` | MinerU metadata receipt writer | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime/source status |
| --- | --- | --- |
| `MEMORY_WRITE_AUTHORITY_DECISION` | T13 decision-matrix classification field | DOC_ONLY_NEW |
| `MEMORY_RECORD_CANDIDATE_BUILDER_READY` | selected route if T13 releases T14 metadata-only candidate-builder work | DOC_ONLY_NEW |
| `MEMORY_WRITE_STILL_NOT_AUTHORIZED_BY_T13` | explicit T13 hold on actual memory/RAG write | DOC_ONLY_NEW |
| `FUTURE_MEMORY_RECORD_CANDIDATE_WORK_ORDER_REQUIRED` | future authority requirement for T14 if T13 selects the candidate-builder route | DOC_ONLY_NEW |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED
priorVerificationArtifact: `docs/reviews/CVF_MSEA_R28_T12_MINERU_MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`
priorVerificationAnchor: `91cc1422`
freshRecomputeRequired: true
recomputeReason: T13 creates a new decision matrix, so source facts and dependency release evidence must be recomputed against current HEAD.
unicodePathHandling: use literal paths and UTF-8-safe command output; do not normalize or rewrite filenames.
extractedTextAuthority: N/A with reason - no extracted text, private/generated output text, or document body is source authority for T13.

| Field | Value |
| --- | --- |
| verificationMode | RECOMPUTE_REQUIRED |
| priorVerificationArtifact | `docs/reviews/CVF_MSEA_R28_T12_MINERU_MEMORY_OWNER_ADMISSION_READOUT_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md` |
| priorVerificationAnchor | `91cc1422` |
| freshRecomputeRequired | true |
| recomputeReason | T13 creates a new decision matrix, so source facts and dependency release evidence must be recomputed against current HEAD |
| unicodePathHandling | use literal paths and UTF-8-safe command output; do not normalize or rewrite filenames |
| extractedTextAuthority | N/A with reason - no extracted text, private/generated output text, or document body is source authority for T13 |

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
| --- | --- | --- |
| Dispatch base | `git rev-parse --short HEAD` returned `4cd04307` before authoring | ACCEPT |
| Worktree state | `git status --short --untracked-files=all` was empty before dispatch authoring | ACCEPT |
| Existing T13 artifact collision | `Test-Path` returned false for planned baseline, work order, matrix, and worker-return paths | ACCEPT |
| Runtime execution | No MinerU/provider/live/runtime command is authorized by this baseline | NOT_APPLICABLE_WITH_REASON |

## Acceptance Criteria

| ID | Criterion | Evidence required |
| --- | --- | --- |
| AC1 | Worker creates the T13 memory-write authority decision matrix and worker return only | matrix, worker return, and git status |
| AC2 | Matrix selects exactly one route token and preserves no actual memory/RAG write in T13 | matrix findings and worker return |
| AC3 | Matrix distinguishes T14 metadata-only memory-record candidate builder scope from T16 actual memory/RAG write scope | matrix decision rows |
| AC4 | Worker leaves changes uncommitted under WORKER_MUST_NOT_COMMIT | worker return and HEAD evidence |
| AC5 | Worker-return fast gate, pre-implementation autorun, reviewer steward, and material pre-commit hook pass before closure | command evidence |

## Claim Boundary

This GC-018 baseline authorizes only a docs-only T13 authority decision matrix
and worker return. It does not authorize source/test implementation,
checker/hook edits, MinerU runtime execution, private/generated content read,
Candidate Group A import, memory/RAG write, provider/live proof, public-sync,
standalone app work, legal/use-case deep dive, extraction accuracy, document
truth, legal quality, current-law correctness, workflow-chain production
readiness, session-sync by worker, worker stage, worker commit, or push.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | MSEA source-mirror learning -> R27 plane route -> R28 receipt/checker/helper chain -> R28-T13 memory-write authority decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline and paired work order |
| Disposition | ADAPT: convert accepted T12 admission readout evidence into a bounded decision matrix for future memory-record candidate work |
| Claim boundary | no MinerU runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, checker/hook/session edit, or product-app claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T13 GC-018 dispatch baseline for memory-write authority decision |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, memory-store, RAG, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime, memory, provider, public, or external action is executed or observed. |
| invocationBoundary | local document authoring and governance gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized or claimed. |
| claimLanguage | baseline dispatch evidence only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router/memory behavior without fresh source-verified authorization. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T13 dispatch material is private provenance governance material only.
No public-sync export, public repository commit, or public catalog claim is
included.
