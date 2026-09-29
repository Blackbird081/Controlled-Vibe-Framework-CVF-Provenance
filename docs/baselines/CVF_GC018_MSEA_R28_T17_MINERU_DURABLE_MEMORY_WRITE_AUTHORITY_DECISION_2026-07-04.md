# CVF GC-018 Baseline - MSEA R28 T17 MinerU Durable Memory Write Authority Decision

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-07-04

docType: baseline

Batch ID: MSEA-R28-T17-MINERU-DURABLE-MEMORY-WRITE-AUTHORITY-DECISION

rawMemoryReleased: false

dispatchBaseHead: f0800b95

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: delegated worker role

## Decision Baseline / Proposed Tranche

| Field | Value |
| --- | --- |
| Proposed tranche | MSEA-R28-T17 MinerU Durable Memory Write Authority Decision |
| Baseline decision | DISPATCH_READY for a no-commit docs-only authority decision tranche |
| Selected path | author a source-verified decision matrix for whether and how a later T18 packet may implement actual durable-memory write behavior |
| Rejected path | actual memory/RAG write, durable-store invocation, vectorization, retrieval, source/test/checker/hook edits, runtime execution, private/generated content read, provider/live proof, public-sync, or production workflow-chain claim |
| Dependency release basis | accepted T16 closure at material commit `0bf81a68`, plus session-sync routing at `f0800b95` |

## Purpose

Authorize a bounded T17 docs-only decision tranche that evaluates the accepted
T16 durable-memory write-input candidate mapping against the Learning Plane
durable store write gate, actor authorization source, R27 scan-to-memory route,
and R24-T4 private-output policy. T17 may select or reject a future T18 actual
write implementation route, but it must not implement, call, simulate, or claim
any memory write.

## Scope / Target / Owner Boundary

Allowed scope:

- create `docs/reference/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md`;
- create `docs/reviews/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md`;
- source-verify the T16 mapper, durable store write gate, runtime memory actor
  gate, R27 route ledger, R24-T4 private-output policy, and current session
  next-move release;
- choose exactly one decision disposition for a future T18 route.

Forbidden scope:

- no source/test/checker/hook/session/handoff/AGENTS.md edits by worker;
- no durable memory-store invocation, memory/RAG write, vectorization,
  retrieval, provider/live proof, MinerU runtime execution, private/generated
  content read, Candidate Group A import, public-sync, Web/MCP/model-router
  work, dependency install, standalone app, legal/use-case deep dive,
  extraction-accuracy claim, document-truth claim, legal-quality claim,
  current-law correctness claim, production workflow-chain claim, worker stage,
  worker commit, or push.

Risk ceiling: docs-only authority decision and matrix authoring.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R28-T16 material closure | `docs/reviews/CVF_MSEA_R28_T16_MINERU_MEMORY_STORE_ADAPTER_MAPPING_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md` and material commit `0bf81a68` | ACCEPT |
| R28-T16 selected next route | `CVF_SESSION/state/entries/mseaR28T16MineruMemoryStoreAdapterMappingImplementationClosure20260704.json` records `AUTHOR_MSEA_R28_T17_GC018_AND_SOURCE_VERIFIED_WORK_ORDER_FOR_ACTUAL_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION` | ACCEPT |
| Current session routing | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` at session-sync commit `f0800b95` routes next move to T17 work-order authoring only | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `f0800b95` before authoring | ACCEPT |

## Roadmap-to-Work-Order Trace Matrix

| Source requirement | T17 work-order handling |
| --- | --- |
| T16 structurally maps MinerU memory-record candidate to durable write-input candidate shape | T17 evaluates whether the remaining write authority gates can be released for a future T18 packet |
| T16 keeps actual memory/RAG write unauthorized | T17 is docs-only and cannot call the durable store |
| Durable store denies writes unless policy and actor authorization are satisfied | T17 matrix must source-verify and decide the policyDecision, actorAuthorized, and provenanceScore supply strategy for a future packet |
| R27 requires receipt, quality, source pointer, downstream-use status, and claim boundary before future memory write | T17 matrix must prove whether the T1-T16 chain satisfies those prerequisites without reading private/generated content |
| R24-T4 private-output policy forbids generated output content import | T17 matrix must preserve metadata-only routing and reject raw/private content transfer |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T17 --title "MinerU Durable Memory Write Authority Decision" --date 2026-07-04 --base f0800b95 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile, adapted to docs-only authority decision tranche |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled T17 dependency release, source verification, docs-only scope, no-memory-write boundary, worker manifest, handoff route, and actual-write hold |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, dispatch-envelope, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX`; `T18_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_CANDIDATE`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T17_DECISION_ONLY` |
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
| claimBoundary | This read-ahead covers this baseline only; worker-created return and companion matrix require their own source and checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T16 closure accepted mapper-only behavior and released T17 authoring while keeping memory write unauthorized. | VALUE_SET | `CVF_SESSION/state/entries/mseaR28T16MineruMemoryStoreAdapterMappingImplementationClosure20260704.json` | lines 19-22 | `MEMORY_WRITE_NOT_AUTHORIZED_BY_T16_MAPPING_ONLY`; `AUTHOR_MSEA_R28_T17_GC018_AND_SOURCE_VERIFIED_WORK_ORDER_FOR_ACTUAL_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION` | active session state source entry | ACCEPT |
| T16 source exposes durable write-input candidate dataclass, builder, and payload renderer. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 167, 635, and 711 | `MineruDurableMemoryWriteInputCandidate`; `build_mineru_durable_memory_write_input_candidate`; `mineru_durable_memory_write_input_candidate_payload` | MinerU metadata receipt writer | ACCEPT |
| T16 mapper keeps memory write unauthorized and output content unread. | VALUE_SET | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 27, 167-179, and 663-669 | `MEMORY_WRITE_NOT_AUTHORIZED_BY_T16`; `output_content_read`; `memory_write_authorized` | MinerU metadata receipt writer | ACCEPT |
| Durable memory store write input names the policy, actor, and provenance fields a future write packet must decide. | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 52-63 | `DurableMemoryWriteInput`; `policyDecision`; `actorAuthorized`; `provenanceScore` | Learning Plane durable memory store | ACCEPT |
| Durable memory store denies writes without actor authorization and allow policy. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 195-206 | `write`; `durable_memory_policy_denied`; `actorAuthorized`; `policyDecision` | Learning Plane durable memory store | ACCEPT |
| Durable memory store rejects raw payload-like fields and low provenance before persistence. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 98, 137-143, and 249-263 | `MIN_PROVENANCE_SCORE`; `hasRawPayload`; `raw_memory_payload_rejected`; `low_provenance_score` | Learning Plane durable memory store | ACCEPT |
| Durable memory receipt remains summary-only with no raw release or reinjection. | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 46-48 and 173-175 | `summaryOnly`; `canReinject`; `rawMemoryReleased` | Learning Plane durable memory store | ACCEPT |
| Runtime memory hierarchy defines actor-role values and durable actor authorization lanes. | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 10-18 values `OPERATOR`, `GOVERNOR`, `HUMAN`, `BUILDER`, `AI_AGENT`, `REVIEWER`, `SERVICE_AGENT`, `OBSERVER`, `ANALYST`, `unknown`; lines 173-204 durable lanes; lines 273-276 actor-denial branch | `RuntimeMemoryActorRole`; `allowedActors`; `m1_durable_cross_session`; `actor_not_allowed_for_memory_tier` | Runtime memory hierarchy | ACCEPT |
| R27 scan-to-memory route requires receipt, quality, source pointer, downstream-use status, and claim boundary before future memory write. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 71-87 | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED` | R27 decision ledger | ACCEPT |
| R24-T4 private-output policy keeps private/generated output content out of successor routing. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 54-64 and 212 | `privateOutputDisposition`; `PRIVATE_GENERATED_OUTPUT`; policy claim boundary | R24-T4 policy reference | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Source status |
| --- | --- | --- |
| `DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX` | proposed T17 companion matrix disposition family | DOC_ONLY_NEW |
| `T18_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_CANDIDATE` | proposed future route token if source evidence supports T18 authoring | DOC_ONLY_NEW |
| `MEMORY_WRITE_NOT_AUTHORIZED_BY_T17_DECISION_ONLY` | proposed T17 hold token confirming no actual write in T17 | DOC_ONLY_NEW |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED
priorVerificationArtifact: `docs/reviews/CVF_MSEA_R28_T16_MINERU_MEMORY_STORE_ADAPTER_MAPPING_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`
priorVerificationAnchor: `0bf81a68`
freshRecomputeRequired: true
recomputeReason: T17 evaluates actual write authority prerequisites, so durable-store and runtime actor gates must be source-verified against current HEAD.
unicodePathHandling: use literal paths and UTF-8-safe command output; do not normalize or rewrite filenames.
extractedTextAuthority: N/A with reason
extractedTextAuthorityReason: no extracted text, private/generated output text, or document body is source authority for T17.

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
| --- | --- | --- |
| Dispatch base | `git rev-parse --short HEAD` returned `f0800b95` before authoring | ACCEPT |
| Worktree state | `git status --short` was empty before T17 authoring | ACCEPT |
| Existing T17 artifact collision | planned baseline, work-order, matrix, and worker-return paths were absent before authoring | ACCEPT |
| Existing Extraction Foundation mapper | `rg` found only T16 mapper and tests under Extraction Foundation; no actual durable-store invocation is authorized by this baseline | ACCEPT |
| Runtime execution | No MinerU/provider/live/runtime/memory-store command is authorized by this baseline | NOT_APPLICABLE_WITH_REASON |

## Acceptance Criteria

| ID | Criterion | Evidence required |
| --- | --- | --- |
| AC1 | Worker creates only the T17 companion decision matrix and T17 worker return | git status and worker return |
| AC2 | Matrix source-verifies policyDecision, actorAuthorized, provenanceScore, raw-payload rejection, summary-only receipt, and actor-role gates before selecting a future route | matrix Source Verification Block |
| AC3 | Matrix chooses exactly one decision disposition: future T18 authoring ready, hold pending missing authority, or blocked with reason | matrix Decision Summary |
| AC4 | T17 does not invoke durable memory store, write memory/RAG, vectorize, retrieve, run MinerU, or edit source/test/checker/hook/session/public paths | worker return and git status |
| AC5 | Worker-return fast gate, pre-implementation autorun, reviewer steward, and material pre-commit hook pass before closure | command evidence |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | MSEA source-mirror learning -> R27 plane route -> R28 receipt/checker/helper chain -> T16 adapter mapping -> T17 write authority decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline and paired work order |
| Disposition | ADAPT accepted T16 mapping closure into a bounded docs-only authority decision dispatch |
| Claim boundary | no MinerU runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, checker/hook/session edit, or product-app claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T17 GC-018 dispatch baseline for durable-memory write authority decision |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, memory-store write, RAG, provider, or public behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime or memory-store receipt is created or consumed. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime, memory, provider, public, external, or private-content action is executed or observed. |
| invocationBoundary | docs-only authority decision dispatch and governance gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized or claimed. |
| claimLanguage | baseline dispatch evidence only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router/memory behavior without fresh source-verified authorization. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T17 dispatch material is private provenance governance material only.
No public-sync export, public repository commit, or public catalog claim is
included.

## Claim Boundary

This GC-018 baseline authorizes only a bounded docs-only work order for a
durable-memory write authority decision matrix and worker return. It does not
authorize actual memory/RAG write, durable-store invocation, vectorization,
retrieval, checker/hook edits, source/test edits by worker, MinerU runtime
execution, private/generated content read, Candidate Group A import,
provider/live proof, public-sync, standalone app work, legal/use-case deep
dive, extraction accuracy, document truth, legal quality, current-law
correctness, workflow-chain production readiness, session-sync by worker,
worker stage, worker commit, or push.
