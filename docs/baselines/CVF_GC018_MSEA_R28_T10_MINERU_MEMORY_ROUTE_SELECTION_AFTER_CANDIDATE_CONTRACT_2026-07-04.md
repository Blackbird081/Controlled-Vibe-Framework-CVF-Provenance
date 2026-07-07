# CVF GC-018 Baseline - MSEA R28 T10 MinerU Memory Route Selection After Candidate Contract

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-07-04

docType: baseline

Batch ID: MSEA-R28-T10-MINERU-MEMORY-ROUTE-SELECTION-AFTER-CANDIDATE-CONTRACT

rawMemoryReleased: false

dispatchBaseHead: bd2c2d95

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: orchestrator

Reviewer owner: reviewer/closer

Worker target: delegated worker role

## Purpose

Authorize a docs-only no-commit T10 worker to create a source-verified route
selection matrix and worker return after accepted T9 memory-safe candidate
contract evidence. This baseline does not authorize memory/RAG write,
runtime execution, private/generated content read, or implementation beyond
the two worker-owned documentation artifacts.

## Decision / Baseline / Proposed Tranche

| Field | Value |
| --- | --- |
| Baseline decision | `MSEA_R28_T10_ROUTE_SELECTION_DOCS_ONLY` |
| Proposed tranche | MSEA-R28-T10 MinerU Memory Route Selection After Candidate Contract |
| Worker route | WORKER_MUST_NOT_COMMIT docs-only companion matrix plus worker return |
| Selected dispatch posture | DISPATCH_READY after T9 closure and session-sync release evidence |
| Memory write posture | `MEMORY_WRITE_STILL_NOT_AUTHORIZED_BY_T10_DISPATCH` |
| Future authority boundary | any memory-owner implementation or memory/RAG write requires a later fresh GC-018 and work order |

## Evidence / Verification

| Evidence | Result |
| --- | --- |
| R28-T9 material closure | PASS: commit `45fb7a9a` accepted T9 candidate contract helper evidence |
| R28-T9 session-sync routing | PASS: commit `bd2c2d95` routes next allowed move to T10 work-order authoring |
| ADIF resolver | PASS: no returned defects for work-order-authoring dispatcher pre-dispatch |
| Negative path search | PASS: planned T10 baseline, work order, matrix, and worker return paths were absent before authoring |
| Dispatch gate plan | REQUIRED: run dispatch-quality, pre-dispatch autorun, commit steward, and pre-commit before dispatch commit |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T10 --title "MinerU Memory Route Selection After Candidate Contract" --date 2026-07-04 --base bd2c2d95 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled dependency release evidence, source verification, no-commit docs-only output manifest, handoff control, T10 route-selection boundaries, and no-memory-write claim boundary. |
| checkerReadAheadConfirmation | dispatch-quality, source-validation, lifecycle, dispatch-envelope, handoff-boundary, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, external-intake, foundation-storage, autorun catalog, and hook catalog surfaces were read before authoring. |
| docOnlyNewFields | `MEMORY_ROUTE_SELECTION_AFTER_CANDIDATE_CONTRACT_MATRIX`; `MEMORY_SAFE_CANDIDATE_READY_FOR_MEMORY_OWNER_REVIEW`; `MEMORY_WRITE_STILL_NOT_AUTHORIZED_BY_T10`; `FUTURE_MEMORY_OWNER_WORK_ORDER_REQUIRED` |
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
| Dispatch impact | No ADIF-specific extra instruction is required beyond active guard orientation, literal-format gotchas, scaffold output, source verification, checker read-ahead, and no-commit discipline. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_work_order_dispatch_quality_lifecycle.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_foundation_storage_layout.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Dependency Release Evidence; Source Verification Block; Negative Search And Collision Discipline; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition; Delta Execution Claim Boundary Control Block; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define route decision content. |
| claimBoundary | This read-ahead covers this baseline only; worker-created matrix and return require their own checker read-ahead before writing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Active session state releases T10 work-order authoring after accepted T9 closure. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` field | `nextAllowedMove` | active session bootstrap read model | ACCEPT |
| T9 closure accepted the candidate contract helper and still withheld memory write. | VALUE_SET | `CVF_SESSION/state/entries/mseaR28T9MemorySafeCandidateContractClosure20260704.json` | lines 14-20 | `MEMORY_SAFE_CANDIDATE_CONTRACT_IMPLEMENTED`; `MEMORY_WRITE_NOT_AUTHORIZED_BY_T9_DISPATCH` | active session state entry | ACCEPT |
| T9 worker return recommends T10 only after reviewer acceptance and session-sync, and does not authorize memory write. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_WORKER_RETURN_2026-07-04.md` | lines 49-55 and 66-69 | `t10Recommendation`; `memoryWriteDisposition` | T9 worker return | ACCEPT |
| T8 decision matrix reserved T10 for route selection after accepted T9 evidence. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T8_MINERU_DOWNSTREAM_USE_AND_MEMORY_ROUTE_RELEASE_DECISION_MATRIX_2026-07-04.md` | lines 59-63 | `MEMORY_SAFE_CANDIDATE_CONTRACT_RECOMMENDED`; `t10Recommendation` | T8 decision matrix | ACCEPT |
| R27 ledger requires receipt, quality, source pointer, downstream-use status, and claim boundary before memory-safe candidates, and a fresh memory-owner work order before memory write. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 74 and 86-87 | `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED` | R27 decision ledger | ACCEPT |
| R24-T4 policy keeps private/generated output content out of governed route-selection evidence. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 17, 104, and 118 | `private-output`; `claim boundary`; `no production claim` | R24-T4 private-output policy | ACCEPT |
| Current receipt writer owns the T9 candidate contract helper and payload symbols. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 98, 295, and 358 | `MineruMemorySafeCandidateContract`; `build_mineru_memory_safe_candidate_contract`; `mineru_memory_safe_candidate_contract_payload` | receipt writer source | ACCEPT |
| Focused tests prove memory-write authorization remains false and content-bearing fields are absent from candidate payload. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 255-270 | `memoryWriteAuthorized`; `memoryWriteDisposition`; `outputFileNames` | receipt writer focused tests | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned T10 dispatch paths absent before authoring | `Test-Path` returned `False` for planned T10 baseline, work order, worker return, and matrix paths before authoring. | PASS |
| Token search for T10 before authoring | `rg -n "MSEA-R28-T10|MEMORY_ROUTE_SELECTION_AFTER_CANDIDATE_CONTRACT|Memory Route Selection After Candidate Contract" docs CVF_SESSION governance EXTENSIONS` found no existing T10 dispatch artifact before this packet was created. | PASS |
| Collision decision | Existing T8/T9 next-route references are predecessor release evidence, not an existing T10 packet. | PASS |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| R28-T9 material closure | `docs/reviews/CVF_MSEA_R28_T9_MINERU_MEMORY_SAFE_CANDIDATE_CONTRACT_WORKER_RETURN_2026-07-04.md` at material commit `45fb7a9a` accepted `MEMORY_SAFE_CANDIDATE_CONTRACT_IMPLEMENTED`. | ACCEPT |
| R28-T9 session-sync routing | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` at session-sync commit `bd2c2d95` routes next move to T10 work-order authoring. | ACCEPT |
| Current dispatch base | `git rev-parse --short HEAD` returned `bd2c2d95` before authoring. | ACCEPT |

## Claim Boundary

This baseline authorizes only T10 dispatch authoring for a docs-only
route-selection matrix and worker return. It does not authorize MinerU runtime
execution, private/generated content read, Candidate Group A import,
source/test/checker/hook edits, memory/RAG write, provider/live proof,
public-sync, standalone app work, legal/use-case deep dive, extraction
accuracy, document truth, legal quality, current-law correctness,
workflow-chain production-readiness claim, worker commit, or push.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T10 docs-only route-selection baseline |
| claimDisposition | CLAIM_REJECTED: no runtime-enforcement, direct-interception, mandatory-wrapper, universal governed-coding, memory-store, RAG, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: predecessor metadata/helper evidence is cited, but this baseline creates no runtime receipt. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: this baseline runs no MinerU, provider, memory, or external action. |
| invocationBoundary | local source verification, dispatch authoring, and governance gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | docs-only route-selection baseline and bounded dispatch evidence only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior, checker/hook/source edit, or memory write without fresh source-verified authorization. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T10 is private provenance dispatch work and does not change the
public-sync repository or public catalog.
