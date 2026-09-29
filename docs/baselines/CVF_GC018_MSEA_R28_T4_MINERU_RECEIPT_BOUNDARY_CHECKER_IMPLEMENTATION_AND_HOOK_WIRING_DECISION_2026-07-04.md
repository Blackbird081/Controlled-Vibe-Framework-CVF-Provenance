# CVF GC-018 Baseline - MSEA-R28-T4 MinerU Receipt Boundary Checker Implementation And Hook Wiring Decision

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-07-04

docType: baseline

Batch ID: MSEA-R28-T4-RECEIPT-BOUNDARY-CHECKER-IMPLEMENTATION-DECISION

rawMemoryReleased: false

dispatchBaseHead: 55961ef2

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: reviewer/closer

Worker target: worker role, not a specific provider name

## Purpose

Authorize one bounded governance-checker implementation tranche for the MinerU
receipt-boundary checker and hook-wiring decision. The worker may create a new
deterministic checker and focused tests, then wire it into the existing autorun
and local hook catalog surfaces if implementation passes focused evidence.

This baseline does not authorize MinerU runtime execution, private or generated
content reads, memory/RAG writes, provider/live proof, public-sync, standalone
PDF app work, legal/use-case deep dive, extraction accuracy, document truth,
legal quality, current-law correctness, workflow-chain production readiness,
worker stage, worker commit, or push.

## Scope / Target / Owner Boundary

Allowed worker target: a local governance checker for committed MinerU metadata
receipt artifacts, focused tests, allowed hook/autorun catalog wiring, any
required GC-051 registry source entry for newly changed review/source evidence,
and a no-commit worker return.

Allowed worker output paths:

- `governance/compat/check_mineru_receipt_boundary.py`
- `governance/compat/test_check_mineru_receipt_boundary.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `docs/reviews/CVF_MSEA_R28_T4_MINERU_RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION_WORKER_RETURN_2026-07-04.md`
- `docs/corpus-intelligence/registry/entries/msea-r28-t4-mineru-receipt-boundary-checker-source.json` only if the worker-created review or changed source evidence makes GC-051 coverage necessary
- `docs/corpus-intelligence/registry/entries/msea-r28-t4-mineru-receipt-boundary-checker-tests.json` only if the worker-created review or changed test evidence makes GC-051 coverage necessary
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` only when generated from source entries by the existing registry generator

Forbidden paths and actions: no edits to R28-T1 writer source/tests, R28-T3
accepted worker return or companion matrix, R24/R26/R27 references, session
state, active handoff, root startup files, AGENTS.md, public-sync clone, product
runtime, Web/UI, MCP/CLI adapter, memory/RAG owner, Candidate Group A source or
generated output, private source documents, or generated MinerU output content.

## Baseline Decision

| Field | Value |
| --- | --- |
| selectedRoute | `RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION` |
| releaseBasis | R28-T3 material commit `4d64e33f` accepted the checker-candidate design and routed next move to R28-T4 packet authoring. |
| implementationBoundary | one deterministic checker module, focused tests, bounded autorun/local hook catalog wiring, registry coverage only if required, and worker return |
| memoryRouteDisposition | `MEMORY_ROUTE_HELD_PENDING_ACTUAL_CHECKER_AND_QUALITY` remains held; this tranche may prove a checker, but does not add quality/source-pointer fields or memory writes. |
| runtimeDisposition | no MinerU runtime execution, no private/generated content read, no extraction accuracy or document-truth claim |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R28-T4 --title "MinerU Receipt Boundary Checker Implementation And Hook Wiring Decision" --date 2026-07-04 --base 55961ef2 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile, with protected governance path trigger active |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled R28-T4 purpose, source verification, protected-path authorization, dual-agent matrix, work-order fulfillment manifest, no-commit handoff controls, and R28 held-lane boundaries |
| checkerReadAheadConfirmation | dispatch-quality, handoff-boundary, lifecycle-hygiene, checker-read-ahead, operation-trace, delta-boundary, ADIF-disclosure, public-export, corpus-scan-registry, autorun catalog, and hook catalog source surfaces were read before authoring |
| docOnlyNewFields | `RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION`; `CHECKER_IMPLEMENTATION_AUTHORIZED_PENDING_WORKER_RETURN_REVIEW`; `MEMORY_ROUTE_STILL_HELD_AFTER_CHECKER_IMPLEMENTATION` |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF-specific extra instruction is required beyond active guard orientation, literal-format gotchas, scaffold output, source verification, protected-path authorization, and worker-output checker read-ahead. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_corpus_scan_registry.py`; `governance/compat/check_core_guard_self_protection.py` |
| literalTokensReviewed | Status: DISPATCH_READY; WORKER_MUST_NOT_COMMIT; Source Verification Block; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Work-Order Fulfillment Manifest; Worker Return Packet Shape Contract; Core Guard Self-Protection Authorization; applicableCheckersRead; literalTokensReviewed; gateRunPurpose; claimBoundary; Resolver query; Returned defects: NONE_RETURNED; Public Export Disposition; Delta Execution Claim Boundary Control Block; protected paths; source-not-found disposition spelling |
| gateRunPurpose | Confirmation evidence after checker read-ahead; gates confirm dispatch shape and do not define implementation scope. |
| claimBoundary | This read-ahead covers the R28-T4 dispatch packet only; worker-created checker, tests, catalog edits, registry entries, and worker return require their own source and checker read-ahead before editing. |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Active session state releases R28-T4 packet authoring after accepted R28-T3 checker-candidate design closure. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `nextAllowedMove` field | `MSEA-R28-T4`; `4d64e33f` | active session bootstrap read model | ACCEPT |
| R28-T3 closure accepted design evidence and routed the next recommended move to R28-T4 checker implementation and hook wiring decision. | VALUE_SET | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | lines 7200-7221 | `selectedDesignDisposition`; `checkerImplementationDisposition`; `nextRecommendedMove` | active session state entry `mseaR28T3MineruReceiptBoundaryCheckerCandidateDesignClosure20260704` | ACCEPT |
| R28-T3 worker return selected design-only disposition and held implementation and memory-route release pending later work. | VALUE_SET | `docs/reviews/CVF_MSEA_R28_T3_MINERU_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_WORKER_RETURN_2026-07-04.md` | lines 105-109 | `CHECKER_IMPLEMENTATION_HELD_PENDING_ACCEPTED_DESIGN`; `MEMORY_ROUTE_HELD_PENDING_ACTUAL_CHECKER_AND_QUALITY` | R28-T3 worker return | ACCEPT |
| R28-T3 companion matrix maps candidate check families and failure dispositions for a future checker. | VALUE_SET | `docs/reference/CVF_MSEA_R28_T3_MINERU_RECEIPT_BOUNDARY_CHECKER_CANDIDATE_DESIGN_MATRIX_2026-07-04.md` | lines 58-77 | `Checker Candidate Design Matrix` | R28-T3 companion design matrix | ACCEPT |
| R26 records checker candidate status and check families without authorizing implementation in R26. | VALUE_SET | `docs/reference/CVF_MSEA_R26_T1_MINERU_RECEIPT_SCHEMA_WRITER_CONTRACT_AND_CHECKER_CANDIDATE_DESIGN_2026-07-04.md` | lines 100-111 | `checkerCandidateStatus`; `CHECKER_CANDIDATE`; `NOT_AUTHORIZED_BY_R26` | R26 receipt contract | ACCEPT |
| R24-T4 defines private receipt envelope fields and private output classes the checker must protect. | VALUE_SET | `docs/reference/CVF_MSEA_R24_T4_MINERU_WORKFLOW_CHAIN_RECEIPT_POLICY_AND_PRIVATE_OUTPUT_HANDLING_POLICY_2026-07-04.md` | lines 39-66 | `outputContentRead`; `downstreamRelease`; `PRIVATE_INPUT_ONLY`; `PRIVATE_RUNTIME_COPY`; `PRIVATE_GENERATED_OUTPUT`; `RECEIPT_METADATA_ALLOWED` | R24-T4 private-output policy | ACCEPT |
| R27 keeps memory-safe candidate and memory write routes held pending receipt, quality, source pointer, allowed downstream use, claim boundary, and a fresh memory owner work order. | VALUE_SET | `docs/reference/CVF_MSEA_R27_MINERU_DOCUMENT_INTELLIGENCE_PLANE_INTEGRATION_DECISION_LEDGER_2026-07-04.md` | lines 77-87 | `QUALITY_DISPOSITION_READY`; `MEMORY_SAFE_CANDIDATE_READY`; `MEMORY_WRITE_AUTHORIZED`; `NOT_AUTHORIZED_BY_R27` | R27 decision ledger | ACCEPT |
| R28-T1 writer source exposes held downstream release, required receipt object, output-content-read rejection, filename allowlist, payload renderer, and JSON renderer. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` | lines 18, 26, 48, 66, 93-104, 112, 135-137, 159, 178 | `DOWNSTREAM_RELEASE_HELD`; `ALLOWED_OUTPUT_FILE_NAMES`; `OUTPUT_CONTENT_READ_FORBIDDEN`; `MineruMetadataReceipt`; `_validate_output_file_name`; `build_mineru_metadata_receipt`; `mineru_metadata_receipt_payload`; `render_mineru_metadata_receipt_json` | Extraction Foundation metadata receipt writer | ACCEPT |
| R28-T1 writer tests prove stable payload, held downstream release, false output-content-read behavior, and output-content-read rejection. | EXISTS | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/tests/test_mineru_metadata_receipt_writer.py` | lines 42, 59, 62-64, 98, 112, 133 | `test_receipt_payload_contains_required_r24_r26_metadata_fields`; `test_json_rendering_is_stable_and_metadata_only`; `test_downstream_lanes_remain_held_for_future_packets`; `OUTPUT_CONTENT_READ_FORBIDDEN` | Extraction Foundation metadata receipt writer tests | ACCEPT |
| Autorun common command catalog is the source-visible surface for adding a range-aware checker to agent autorun gates. | EXISTS | `governance/compat/agent_autorun_command_catalog.py` | lines 41-56 and 84-90, 132-134, 360-362 | `_range_command`; `_common_commands`; `check_work_order_dispatch_quality.py`; `check_agent_handoff_boundary.py`; `check_corpus_scan_registry.py` | agent autorun command catalog | ACCEPT |
| Local hook chains route pre-commit and pre-push checks through catalog source files. | EXISTS | `governance/compat/local_governance_hook_catalog.py` | lines 7-22 | `PRE_COMMIT_CHECKS`; `PRE_PUSH_CHECKS`; `HOOK_CHAINS` | local governance hook catalog | ACCEPT |
| Pre-commit hook catalog is the source-visible surface for adding a checker command to pre-commit. | EXISTS | `governance/compat/local_governance_hook_catalog_pre_commit.py` | lines 6, 64, 96, 208, 251, 331 | `PRE_COMMIT_CHECKS`; `check_work_order_dispatch_quality.py`; `check_agent_handoff_boundary.py`; `check_corpus_scan_registry.py`; `changed corpus registry coverage`; `dispatch scaffold provenance` | pre-commit hook catalog | ACCEPT |
| Pre-push hook catalog is the source-visible surface for adding a checker command to pre-push. | EXISTS | `governance/compat/local_governance_hook_catalog_pre_push.py` | lines 6, 37, 65, 405 | `PRE_PUSH_CHECKS`; `check_work_order_dispatch_quality.py`; `check_agent_handoff_boundary.py`; `dispatch scaffold provenance` | pre-push hook catalog | ACCEPT |
| GC-051 corpus scan registry checker scans changed review files for real extension path mentions and requires registry coverage when applicable. | RUNTIME_BEHAVIOR | `governance/compat/check_corpus_scan_registry.py` | lines 111-129, 213-235 | `_get_changed_corpus_scan_files`; `_extract_corpus_paths_from_text`; `_check_audit_coverage` | GC-051 corpus scan registry checker | ACCEPT |

## New Doc-Only Fields

| Field or token | Purpose | Source fact type | Worker rule |
| --- | --- | --- | --- |
| `RECEIPT_BOUNDARY_CHECKER_IMPLEMENTATION_AND_HOOK_WIRING_DECISION` | selected R28-T4 route token | DOC_ONLY_NEW | use for this dispatch only |
| `CHECKER_IMPLEMENTATION_AUTHORIZED_PENDING_WORKER_RETURN_REVIEW` | bounded implementation authorization token | DOC_ONLY_NEW | checker implementation remains unaccepted until reviewer closure |
| `MEMORY_ROUTE_STILL_HELD_AFTER_CHECKER_IMPLEMENTATION` | memory-route hold token for T4 | DOC_ONLY_NEW | preserve R27/R28 memory hold even if checker implementation passes |

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
| --- | --- | --- |
| Existing checker path check | `Test-Path governance/compat/check_mineru_receipt_boundary.py` returned `False` before authoring. | PASS |
| Existing focused test path check | `Test-Path governance/compat/test_check_mineru_receipt_boundary.py` returned `False` before authoring. | PASS |
| Existing receipt writer owner check | `rg -n "DOWNSTREAM_RELEASE_HELD|ALLOWED_OUTPUT_FILE_NAMES|OUTPUT_CONTENT_READ_FORBIDDEN|class MineruMetadataReceipt|def _validate_output_file_name|def build_mineru_metadata_receipt|def mineru_metadata_receipt_payload|def render_mineru_metadata_receipt_json" EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/mineru_metadata_receipt_writer.py` confirmed the current writer owner surface. | PASS |
| Existing hook/catalog owner check | `rg -n "PRE_COMMIT_CHECKS|PRE_PUSH_CHECKS|_common_commands|_range_command" governance/compat/agent_autorun_command_catalog.py governance/compat/local_governance_hook_catalog.py governance/compat/local_governance_hook_catalog_pre_commit.py governance/compat/local_governance_hook_catalog_pre_push.py` confirmed catalog owner surfaces. | PASS |
| Freshness disposition | No current R28-T4 checker implementation or focused checker test exists; current owner surfaces are R28-T1 writer source/tests, R28-T3 design matrix, and existing autorun/local hook catalogs. | PASS |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| Planned artifact paths absent before authoring | `Test-Path` returned `False` for the planned R28-T4 GC-018, work order, checker source, checker test, and worker return paths. | PASS |
| Token search for R28-T4 lane before authoring | `rg -n --fixed-strings "MSEA-R28-T4" docs CVF_SESSION governance EXTENSIONS` returned only current session next-move references and archived V35 next-move text before this packet was created. | PASS |
| Collision decision | No existing R28-T4 dispatch, checker implementation, focused test, or worker return exists; this baseline may create the first dispatch packet. | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Predecessor requirement | Source evidence | R28-T4 handling |
| --- | --- | --- |
| R28-T3 accepted checker-candidate design | R28-T3 material commit `4d64e33f`; worker return and companion matrix | allow one checker implementation and hook-wiring decision tranche |
| R28-T1 writer source evidence | writer source/tests and GC-051 registry entries | use as fixture/invariant source only; do not edit writer |
| R26 checker-candidate criteria | R26 reference lines 100-111 | implement deterministic checks only for candidate families named there and refined by R28-T3 |
| R24-T4 private-output policy | R24-T4 policy lines 39-66 | enforce metadata/no-content-read boundary for receipt fields |
| R27 scan-to-memory route matrix | R27 decision ledger lines 77-87 | keep memory route held; no memory write or RAG release |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | local governance checker and autorun/hook catalog surfaces | internal worker may create deterministic checker and catalog rows under WORKER_MUST_NOT_COMMIT; reviewer must accept before closure | this GC-018, paired work order, source verification, focused tests, worker return | internal-only local Python checker; no external adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no CLI/MCP or external adapter owner in R28-T4 | external ingress, authentication, approval, receipt, raw-data, mutation, and public boundaries remain out of scope | no source-verified external adapter authority in R28-T4 | adapter deferred; no CLI/MCP surface implemented or claimed | DEFERRED_WITH_REASON |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Corpus scan or extraction intake |
| Chain map route | corpus/source evidence -> CVF-owned references and runtime source verification -> fresh GC-018/work order -> autorun pre-dispatch gates |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired R28-T4 GC-018 and work order |
| Disposition | ADAPT prior R28/R26/R24/R27 evidence into a bounded checker implementation dispatch; no external source becomes authority by itself |
| Claim boundary | routing evidence only; no external repository absorption, private/generated content read, runtime/provider/live proof, public-sync, app, or production claim |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: create one MinerU receipt-boundary checker,
focused tests, and bounded autorun/local hook catalog wiring for that checker
only.

Protected paths:

- `governance/compat/check_mineru_receipt_boundary.py`
- `governance/compat/test_check_mineru_receipt_boundary.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `docs/corpus-intelligence/registry/entries/msea-r28-t4-mineru-receipt-boundary-checker-source.json` only if GC-051 coverage is required
- `docs/corpus-intelligence/registry/entries/msea-r28-t4-mineru-receipt-boundary-checker-tests.json` only if GC-051 coverage is required
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` only when regenerated from source entries

Operator authorization: operator instructed authoring a fresh R28-T4
source-verified work order for receipt-boundary checker implementation and hook
wiring decision after R28-T3 closure.

Rollback boundary: revert only R28-T4 checker, focused test, catalog wiring,
registry source/aggregate, and worker-return artifacts if rejected; do not
modify or revert R28-T1, R28-T3, R24, R26, R27, active session, active handoff,
or public-sync artifacts.

Not authorized: no session-state edit by worker, AGENTS.md edit, active handoff
edit, MinerU runtime execution, private/generated content read, memory/RAG
write, provider/live proof, public-sync, external adapter, standalone app,
legal/use-case deep dive, extraction accuracy, document truth, current-law
correctness, workflow-chain production readiness, worker stage, worker commit,
or push.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R28-T4 dispatch baseline for local deterministic checker implementation |
| claimDisposition | CLAIM_REJECTED: no runtime-enforcement, direct-interception, mandatory-wrapper, universal governed-coding, or provider behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: predecessor metadata receipt writer evidence is cited, but this baseline creates no runtime receipt. |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: this baseline runs no MinerU, provider, memory, or external action. |
| invocationBoundary | local file reads, source verification, scaffold generation, and governance dispatch gates only |
| interceptionBoundary | No direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized. |
| claimLanguage | dispatch authoring for a local checker tranche only |
| forbiddenExpansion | Do not expand into runtime/provider/live/public/package/Web/MCP/model-router behavior or memory write without fresh source-verified authorization. |

## Evidence / Verification

| Evidence item | Required result | Current dispatch evidence |
| --- | --- | --- |
| Source verification | ACCEPT rows cite CVF-governed surfaces or current runtime source | Source Verification Block in this baseline and paired work order |
| Prior design release | R28-T3 accepted checker-candidate design and held memory route | R28-T3 worker return, companion matrix, active session state, and material commit `4d64e33f` |
| Dispatch gates | pre-dispatch autorun must pass before worker implementation begins | pending gate evidence in dispatcher final report |
| Worker implementation evidence | focused tests, hook/catalog diff, worker return, and no-commit proof | required by paired work order; not produced by this baseline |
| Claim exclusions | no runtime/provider/live/public/private-content/app/legal/deep-quality claim | Claim Boundary and Public Export Disposition in this baseline |

## Claim Boundary

This baseline authorizes dispatch of a no-commit worker to implement and test a
local deterministic receipt-boundary checker and bounded hook/autorun catalog
wiring. It does not accept the checker as closed, release memory/RAG, run MinerU,
read private/generated content, make public or provider claims, build an app, or
claim extraction accuracy, document truth, legal quality, current-law
correctness, workflow-chain production readiness, worker commit, or push.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R28-T4 is private provenance governance-checker dispatch work and does
not change the public-sync repository or public catalog.
