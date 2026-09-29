# CVF GC-018 Baseline - MSEA R28 T18 MinerU Actual Durable Memory Write Adapter Implementation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-07-04

docType: baseline

Batch ID: MSEA-R28-T18-MINERU-ACTUAL-DURABLE-MEMORY-WRITE-ADAPTER-IMPLEMENTATION

rawMemoryReleased: false

dispatchBaseHead: 7374b059

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: delegated worker role

## Decision Baseline / Proposed Tranche

| Field | Value |
| --- | --- |
| Proposed tranche | MSEA-R28-T18 MinerU Actual Durable Memory Write Adapter Implementation |
| Baseline decision | DISPATCH_READY for a no-commit source/test implementation tranche |
| Selected path | implement a deterministic Extraction Foundation durable-memory write adapter candidate that validates T16 write-input candidates against T17 policy, actor, provenance, privacy, and R27 prerequisites |
| Rejected path | durable-store invocation, actual memory/RAG write, vectorization, retrieval, MinerU runtime execution, private/generated content read, Candidate Group A import, provider/live proof, public-sync, checker/hook/session/handoff edit by worker, or production workflow-chain claim |
| Dependency release basis | accepted T17 closure at material commit `5166a624`, plus session-sync routing at `7374b059` |

## Purpose

Authorize a bounded T18 implementation tranche that adds a source-backed
durable-memory write adapter candidate in the Extraction Foundation receipt
writer surface. T18 may implement deterministic source/test code that prepares
and validates a metadata-only adapter payload, but it must not invoke the
Learning Plane durable store, write memory/RAG, read private/generated content,
or claim durable persistence.

## Scope / Target / Owner Boundary

Allowed scope:

- update `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py`;
- update `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py`;
- create `docs/reviews/CVF_MSEA_R28_T18_MINERU_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_WORKER_RETURN_2026-07-04.md`;
- implement deterministic metadata-only adapter candidate structures and tests
  that preserve T16 summary-only invariants and T17 policy/actor/provenance
  gates.

Forbidden scope:

- no edits to Learning Plane TypeScript source, durable store source, runtime
  memory hierarchy source, checker/hook/session/handoff/AGENTS.md/public-sync
  paths by worker;
- no durable memory-store invocation, actual memory/RAG write, vectorization,
  retrieval, provider/live proof, MinerU runtime execution, private/generated
  content read, Candidate Group A import, dependency install, standalone app,
  legal/use-case deep dive, extraction-accuracy claim, document-truth claim,
  legal-quality claim, current-law correctness claim, production workflow-chain
  claim, worker stage, worker commit, or push.

Risk ceiling: local deterministic Python adapter candidate implementation and
focused unit tests only.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R28-T17 material closure | `docs/reviews/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md` and material commit `5166a624` | ACCEPT |
| R28-T17 selected T18 route | `docs/reference/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md` lines 56-60 select `T18_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_CANDIDATE` while keeping `MEMORY_WRITE_NOT_AUTHORIZED_BY_T17_DECISION_ONLY` | ACCEPT |
| Current session routing | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` at session-sync commit `7374b059` routes next move to T18 work-order authoring only | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `7374b059` before authoring | ACCEPT |

## Roadmap-to-Work-Order Trace Matrix

| Source requirement | T18 baseline handling |
| --- | --- |
| T16 produced a summary-only durable write-input candidate and kept actual memory write unauthorized | T18 may consume that candidate shape but must keep durable-store invocation and memory write held |
| T17 selected T18 adapter implementation as the future route | T18 implements the adapter candidate in the Extraction Foundation source/test lane |
| Durable store requires allow policy, actor authorization, sufficient provenance, and no raw payload | T18 adapter must fail closed unless those requirements are represented in the local adapter candidate |
| Runtime memory hierarchy defines durable actor lanes | T18 adapter must validate the supplied actor role against source-verified durable tier actor sets |
| R27 requires receipt, quality, source pointer, downstream-use status, and claim boundary before memory write | T18 adapter must encode these prerequisites as metadata-only gates, not as a persistence action |
| R24-T4 forbids private/generated output transfer | T18 adapter must not read, quote, copy, import, or emit private/generated output content |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T18 --title "MinerU Actual Durable Memory Write Adapter Implementation" --date 2026-07-04 --base 7374b059 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile, adapted to bounded source/test adapter implementation |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled T18 dependency release, source verification, allowed source/test scope, durable-store no-invocation boundary, worker manifest, handoff route, and adapter-only claim boundary |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, handoff-boundary, ADIF-disclosure, public-export, autorun workflow, commit-steward, and governed-file-size checker source surfaces were read before authoring |
| docOnlyNewFields | `MineruDurableMemoryWriteAdapterCandidate`; `build_mineru_durable_memory_write_adapter_candidate`; `mineru_durable_memory_write_adapter_candidate_payload`; `DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_CANDIDATE_READY`; `DURABLE_STORE_INVOCATION_NOT_AUTHORIZED_BY_T18` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router/memory persistence behavior claim. |

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
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_agent_commit_steward_preflight.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dispatch Prompt Envelope; Required First Reads; Preflight Checks; Execution Plan; Evidence Requirements; Acceptance Criteria; Review Gate; Closure Checklist; Source Verification Block; New Doc-Only Fields; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; Resolver query; Returned defects: NONE_RETURNED; Public Export Disposition; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers this baseline only; worker-created source/test changes and worker return require their own checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T17 selected T18 adapter implementation while keeping memory write unauthorized by T17. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_MATRIX_2026-07-04.md` | lines 56-60 | `T18_ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_CANDIDATE`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T17_DECISION_ONLY` | T17 decision matrix | ACCEPT |
| T17 worker return states T18 is a candidate route and no write action is released by T17. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md` | lines 57, 66-71, and 89-91 | `t18ReadinessStatus`; `memoryWriteDisposition`; `nextRecommendation` | T17 worker return | ACCEPT |
| T16 source exposes the durable write-input candidate, builder, and payload renderer that T18 may consume. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 167, 635, and 711 | `MineruDurableMemoryWriteInputCandidate`; `build_mineru_durable_memory_write_input_candidate`; `mineru_durable_memory_write_input_candidate_payload` | MinerU metadata receipt writer | ACCEPT |
| T16 mapper keeps memory write unauthorized and source output content unread. | VALUE_SET | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 27, 167-179 | `MEMORY_WRITE_NOT_AUTHORIZED_BY_T16`; `memory_write_disposition`; `output_content_read`; `memory_write_authorized` | MinerU metadata receipt writer | ACCEPT |
| Existing tests cover deterministic durable write-input candidate payload and unsafe-input failure cases. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 602-629, 640-654, and 747-753 | `test_durable_memory_write_input_candidate_is_deterministic_and_metadata_only`; `test_durable_memory_write_input_candidate_changes_with_scope_or_actor`; `test_durable_memory_write_input_candidate_fails_closed_for_unsafe_inputs` | MinerU metadata receipt writer tests | ACCEPT |
| Durable memory store write input names the policy, actor, and provenance fields the adapter must prepare. | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 52-63 | `DurableMemoryWriteInput`; `policyDecision`; `actorAuthorized`; `provenanceScore` | Learning Plane durable memory store | ACCEPT |
| Durable memory store denies writes without actor authorization and allow policy. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 195-206 | `write`; `durable_memory_policy_denied`; `actorAuthorized`; `policyDecision` | Learning Plane durable memory store | ACCEPT |
| Durable memory store rejects raw payload-like fields and low provenance before persistence. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 98, 137-143, and 249-263 | `MIN_PROVENANCE_SCORE`; `hasRawPayload`; `raw_memory_payload_rejected`; `low_provenance_score` | Learning Plane durable memory store | ACCEPT |
| Durable memory receipt remains summary-only with no raw release or reinjection. | VALUE_SET | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 46-48 and 173-175 | `summaryOnly`; `canReinject`; `rawMemoryReleased` | Learning Plane durable memory store | ACCEPT |
| Runtime memory hierarchy defines actor-role values and durable actor authorization lanes. | EXISTS | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/runtime-memory-hierarchy.ts` | lines 12-19 values `OPERATOR`, `GOVERNOR`, `HUMAN`, `BUILDER`, `AI_AGENT`, `REVIEWER`, `SERVICE_AGENT`, `OBSERVER`, `ANALYST`, `unknown`; lines 171-204 durable lanes; lines 273-274 actor membership branch | `RuntimeMemoryActorRole`; `allowedActors`; `durablePersistenceAllowed` | Runtime memory hierarchy | ACCEPT |
| R27 scan-to-memory route requires receipt, quality, source pointer, downstream-use status, and claim boundary before future memory write. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 71-87 | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED` | R27 decision ledger | ACCEPT |
| R24-T4 private-output policy keeps private/generated output content out of successor routing. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 54-64 and 212 | `privateOutputDisposition`; `PRIVATE_GENERATED_OUTPUT`; policy claim boundary | R24-T4 policy reference | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Source status |
| --- | --- | --- |
| `MineruDurableMemoryWriteAdapterCandidate` | proposed Python dataclass name for T18 worker implementation | DOC_ONLY_NEW |
| `build_mineru_durable_memory_write_adapter_candidate` | proposed Python builder name for T18 worker implementation | DOC_ONLY_NEW |
| `mineru_durable_memory_write_adapter_candidate_payload` | proposed deterministic payload renderer name for T18 worker implementation | DOC_ONLY_NEW |
| `DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION_CANDIDATE_READY` | proposed adapter-ready disposition token for T18 worker implementation | DOC_ONLY_NEW |
| `DURABLE_STORE_INVOCATION_NOT_AUTHORIZED_BY_T18` | proposed hold token confirming no durable-store invocation in T18 | DOC_ONLY_NEW |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED
priorVerificationArtifact: `docs/reviews/CVF_MSEA_R28_T17_MINERU_DURABLE_MEMORY_WRITE_AUTHORITY_DECISION_WORKER_RETURN_2026-07-04.md`
priorVerificationAnchor: `5166a624`
freshRecomputeRequired: true
recomputeReason: T18 authorizes source/test implementation, so T16 writer, durable-store, runtime hierarchy, R27, and R24-T4 evidence must be checked against current HEAD.
unicodePathHandling: use literal paths and UTF-8-safe command output; do not normalize or rewrite filenames.
extractedTextAuthority: N/A with reason
extractedTextAuthorityReason: no extracted text, private/generated output text, or document body is source authority for T18.

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
| --- | --- | --- |
| Dispatch base | `git rev-parse --short HEAD` returned `7374b059` before authoring | ACCEPT |
| Worktree state | `git status --short` was empty before T18 authoring | ACCEPT |
| Existing T18 artifact collision | planned baseline, work-order, and worker-return paths were absent before authoring | ACCEPT |
| Existing T18 token search | `rg -n --glob "*.md" --glob "*.json" "MSEA_R28_T18|MSEA-R28-T18|ACTUAL_DURABLE_MEMORY_WRITE_ADAPTER_IMPLEMENTATION" docs/baselines docs/work_orders docs/reviews docs/reference CVF_SESSION` returned only current next-move/T17 route references before authoring | ACCEPT |
| Runtime execution | No MinerU/provider/live/runtime/memory-store command is authorized by this baseline | NOT_APPLICABLE_WITH_REASON |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Path existence for T18 dispatch artifacts | `Test-Path` returned `False` for planned baseline, work order, and worker return before authoring | ACCEPT |
| T18 token search | narrowed governed-artifact/state `rg` returned only next-move and T17-route mentions before authoring | ACCEPT |
| Collision decision | Existing T17-selected route token is intentionally reused as release evidence; fresh T18 artifact paths are created by this dispatch | ACCEPT |

## Acceptance Criteria

| ID | Criterion | Evidence required |
| --- | --- | --- |
| AC1 | Worker changes only the allowed Extraction Foundation Python source, focused test file, and T18 worker return | git status and worker return |
| AC2 | Adapter candidate builder fails closed unless policyDecision is allow, actorAuthorized is true, provenanceScore meets the source-verified threshold, actor role is allowed for the selected durable tier, and R27 prerequisites are present | source diff and focused tests |
| AC3 | Adapter payload remains deterministic and metadata-only, preserving summaryOnly true, canReinject false, rawMemoryReleased false, output_content_read false, and no raw/private output fields | source diff and tests |
| AC4 | T18 does not invoke durable memory store, write memory/RAG, vectorize, retrieve, run MinerU, edit Learning Plane/checker/hook/session/public paths, or claim persistence | worker return and git status |
| AC5 | Focused pytest, worker-return fast gate, pre-implementation autorun, reviewer steward, and material pre-commit hook pass before closure | command evidence |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | MSEA source-mirror learning -> R27 plane route -> R28 receipt/checker/helper chain -> T16 adapter mapping -> T17 authority decision -> T18 adapter implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this GC-018 baseline and paired work order |
| Disposition | ADAPT accepted T17 authority decision into bounded source/test adapter implementation |
| Claim boundary | no MinerU runtime execution, private output content read, memory/RAG write, public-sync, provider/live proof, checker/hook/session edit by worker, or product-app claim |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T18 GC-018 dispatch baseline for durable-memory write adapter candidate implementation |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, memory-store invocation, memory/RAG write, provider, or public behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime or memory-store receipt is created or consumed. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime, memory, provider, public, external, or private-content action is executed or observed. |
| invocationBoundary | source/test adapter candidate dispatch and governance gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized or claimed. |
| claimLanguage | baseline dispatch evidence only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router/memory persistence behavior without fresh source-verified authorization. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T18 dispatch material is private provenance governance material only.
No public-sync export, public repository commit, or public catalog claim is
included.

## Claim Boundary

This GC-018 baseline authorizes only a bounded source/test work order for a
metadata-only MinerU durable-memory write adapter candidate and worker return.
It does not authorize actual memory/RAG write, durable-store invocation,
vectorization, retrieval, Learning Plane source edits, checker/hook edits,
session/handoff edits by worker, MinerU runtime execution, private/generated
content read, Candidate Group A import, provider/live proof, public-sync,
standalone app work, legal/use-case deep dive, extraction accuracy, document
truth, legal quality, current-law correctness, workflow-chain production
readiness, session-sync by worker, worker stage, worker commit, or push.
