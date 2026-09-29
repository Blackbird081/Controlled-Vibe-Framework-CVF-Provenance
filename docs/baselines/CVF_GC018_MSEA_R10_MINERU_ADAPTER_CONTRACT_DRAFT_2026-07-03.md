# CVF GC-018 Baseline - MSEA-R10 MinerU Adapter Contract Draft

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-07-03

Batch ID: MSEA-R10

Dispatch base head: 7c19b587

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator-authorized dispatcher

Reviewer owner: reviewer/closer role for worker return handoff

Worker target: delegated worker role, provider-neutral

## Purpose

Authorize a bounded documentation/reference worker tranche to draft a CVF-owned
MinerU adapter contract that connects the accepted MSEA-R7 receipt vocabulary
and MSEA-R9 application route blueprint to future CVF application routes. This
baseline does not authorize adapter implementation, schema implementation,
receipt-writer code, MinerU runtime, provider/live proof, package activation,
checker implementation, public-sync, or production-readiness claims.

## Baseline Decision

MSEA-R10 is ready for dispatch because MSEA-R9 closed with accepted route
`OPEN_ADAPTER_CONTRACT_DRAFT_ONLY` and source-backed prerequisites for a
documentation/reference-only adapter contract draft. The worker must create
only the planned worker return and companion reference draft, leave them
uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Verification Evidence

| Evidence | Command or source | Result |
|---|---|---|
| Clean starting worktree | `git status --short` before dispatch authoring | clean |
| Source mirror commit | `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Source mirror file count | `git -C .private_reference/source_mirrors/opendatalab__MinerU ls-files` | `425` files |
| ADIF dispatcher query | `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --json` | `NONE_RETURNED` |
| Scaffold readout | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R10 --title "MinerU Adapter Contract Draft" --date 2026-07-03 --base 7c19b587 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MSEA-R9 accepted at material commit 2a58322b; route OPEN_ADAPTER_CONTRACT_DRAFT_ONLY selected for documentation/reference-only adapter contract draft" --include-worker-return-skeleton --stdout` | scaffold profile reviewed |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MSEA-R9 route selection | `docs/reviews/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md`, `## Reviewer Decision`, accepts `OPEN_ADAPTER_CONTRACT_DRAFT_ONLY` | fresh source-verified MSEA-R10 work order may be authored for docs/reference-only adapter contract draft | SATISFIED |
| MSEA-R7 receipt contract draft | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`, `## Receipt Artifact Family Map`, `## Field Family Map`, `## Backend Variant Boundary` | R10 may adapt this vocabulary into a higher-level adapter contract, not implement it | SATISFIED |
| Source mirror authority | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU`, commit `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`, count `425` | worker must recompute commit and file count before citing current source facts | SATISFIED |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R9 selected docs-only adapter contract draft route | VALUE_SET | `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md` | lines 103-114, `## Selected Routing Outcome` | `OPEN_ADAPTER_CONTRACT_DRAFT_ONLY` | MSEA-R9 reference route decision | ACCEPT |
| R9 reviewer accepted route and preserved non-implementation boundary | VALUE_SET | `docs/reviews/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md` | lines 470-480, `## Reviewer Decision` | `ACCEPT_FOR_MATERIAL_COMMIT` | MSEA-R9 reviewer decision | ACCEPT |
| Receipt artifact families are already CVF-owned vocabulary | VALUE_SET | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | lines 63-76, `## Receipt Artifact Family Map` | `layout.pdf`; `span.pdf`; `model.json`; `middle.json`; `content_list.json`; `content_list_v2.json` | MSEA-R7 receipt contract draft | ACCEPT |
| Receipt field families and backend variant boundary exist | EXISTS | `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | lines 79-116, `## Field Family Map`; `## Backend Variant Boundary`; `## Downstream Use Boundary` | `Field Family Map`; `Backend Variant Boundary`; `Downstream Use Boundary` | MSEA-R7 receipt contract draft | ACCEPT |
| R6 selected receipt-schema contract path before R7 | VALUE_SET | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | lines 38-52 and 88-108 | `OPEN_RECEIPT_SCHEMA_CONTRACT_DRAFT` | MSEA-R6 route matrix | ACCEPT |
| T2 owns receipt/quality/RAG advisory boundary | EXISTS | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | `## Receipt Advisory`; `## Claim Boundary` | `Receipt Advisory` | MSEA-T2 advisory | ACCEPT |
| R4/R5/R8 preserve runtime, provider, S3, Docker, RAG, and package candidates as held | VALUE_SET | `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | lines 217-229 and 282-315 | `RUNTIME_CANDIDATE`; `PACKAGE_CANDIDATE`; `REJECT_DIRECT_IMPORT` | MSEA-R8 residual ledger | ACCEPT |
| Source mirror is current authority input for MinerU facts | VALUE_SET | `.private_reference/source_mirrors/INDEX.md` | row `opendatalab__MinerU` | `.private_reference/source_mirrors/opendatalab__MinerU/` | source mirror index | ACCEPT |
| Worker output checker-shape lesson remains required read-ahead | EXISTS | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0023.md` | field block and remediation sections | `ADIF-0023` | ADIF entry | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime status |
|---|---|---|
| adapterContractSection | Names the sections the worker should draft in the R10 reference | DOC_ONLY_NEW |
| receiptFamilyMapping | Maps MSEA-R7 receipt artifact families into CVF adapter contract prose | DOC_ONLY_NEW |
| applicationRouteBinding | Connects MSEA-R9 blueprint layers to the adapter contract draft | DOC_ONLY_NEW |
| nonRuntimeHoldCondition | Preserves held runtime/provider/S3/RAG/Docker/checker lanes | DOC_ONLY_NEW |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Planned R10 baseline path | `Test-Path docs/baselines/CVF_GC018_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` returned `False` before authoring | ACCEPT |
| Planned R10 work-order path | `Test-Path docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` returned `False` before authoring | ACCEPT |
| Planned worker return path | `Test-Path docs/reviews/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_WORKER_RETURN_2026-07-03.md` returned `False` before authoring | ACCEPT |
| Planned reference path | `Test-Path docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` returned `False` before authoring | ACCEPT |
| R10 token search | `rg -n "MSEA-R10|MinerU Adapter Contract Draft|CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT" docs CVF_SESSION AGENT_HANDOFF_V32_2026-07-02.md` found only current next-move references before this dispatch | ACCEPT |

## Current Runtime Freshness Verification

| Check | Evidence | Disposition |
|---|---|---|
| Source mirror commit | `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` returned `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` | ACCEPT |
| Source mirror file count | `git -C .private_reference/source_mirrors/opendatalab__MinerU ls-files` returned `425` files | ACCEPT |
| Runtime remains forbidden | Active next-move state forbids MinerU install/runtime, model download, parser/OCR/VLM/hybrid/API/router/Gradio/Docker execution, provider/live call, credentials/S3, RAG write, source import, package activation, checker implementation, public-sync, Web/MCP/model-router/action-authority, benchmark, document-truth, extraction-accuracy, schema implementation, adapter implementation, and production claims | ACCEPT |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | MinerU source mirror plus accepted MSEA owner surfaces -> CVF adapter contract draft reference -> future implementation only by fresh authorization |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | MSEA-R10 worker return and companion reference draft |
| Disposition | ADAPT: convert accepted receipt and route vocabulary into a CVF-owned adapter contract draft |
| Claim boundary | documentation/reference-only draft; no runtime, provider/live, S3, RAG, Docker, package, checker, source import, schema implementation, adapter implementation, public-sync, or production claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; local mirror `.private_reference/source_mirrors/opendatalab__MinerU/`; accepted MSEA-T2/R4/R5/R6/R7/R8/R9 evidence |
| Enumeration command | worker must run `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` and `git -C .private_reference/source_mirrors/opendatalab__MinerU ls-files` before citing mirror facts |
| Manifest artifact or inline manifest | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Processing ledger artifact or inline ledger | `docs/reviews/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_WORKER_RETURN_2026-07-03.md` and `docs/reference/CVF_MSEA_R10_MINERU_ADAPTER_CONTRACT_DRAFT_2026-07-03.md` |
| Ledger terminal statuses | READ, SOURCE_VERIFIED, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, SKIPPED_WITH_REASON, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | MSEA-T2/R4/R5/R6/R7/R8/R9 owner surfaces |
| Unresolved items | none expected; worker must block on missing MSEA owner surface or source mirror drift |
| Completion claim boundary | draft contract only; no runtime/provider/public/package/checker/source-import/schema/adapter expansion |

## Corpus Completeness And Report Integrity

- Corpus task class: source-backed adapter contract drafting from accepted MinerU absorption evidence.
- Corpus root: `.private_reference/source_mirrors/opendatalab__MinerU/` plus accepted MSEA governed artifacts.
- Snapshot time: 2026-07-03 dispatch authoring session.
- Enumeration command: `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU -g '!**/.git/**'` returned `425` files; `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` returned `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`.
- Manifest artifact or inline manifest: `.private_reference/source_mirrors/INDEX.md` plus MSEA-R8 residual closure ledger.
- Manifest hash: source mirror commit `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`.
- Processing ledger artifact or inline ledger: planned worker return and R10 reference draft.
- Allowed terminal statuses: READ, SOURCE_VERIFIED, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, SKIPPED_WITH_REASON, BLOCKED_UNREADABLE, BLOCKED_WITH_REASON.
- ledger_terminal=READ for accepted MSEA owner surfaces; ledger_terminal=SOURCE_VERIFIED for source mirror commit/count; ledger_terminal=ADAPTED for R10 contract drafting; ledger_terminal=DEFERRED for held runtime/provider/RAG/S3/Docker/checker routes; ledger_terminal=REJECTED for direct upstream import; ledger_terminal=NO_NEW_VALUE for already-owned evidence.
- Reconciliation: manifest=425 source-mirror files; ledger_terminal=READ/SOURCE_VERIFIED/ADAPTED/DEFERRED/REJECTED/NO_NEW_VALUE/SKIPPED_WITH_REASON/BLOCKED_UNREADABLE for cited artifacts; exclusions=0 expected; unresolved=0 expected.
- Unresolved files: 0 expected for dispatch authoring; worker must block if an owner surface is missing or mirror drift appears.
- Declared exclusions: no new source files are excluded by dispatch; worker must not claim a new full-file corpus pass.
- Unreadable or unsupported files: none known at dispatch time; binary/content limits remain owned by MSEA-R8.
- Aggregation check: PASS: R10 uses accepted MSEA owner surfaces and source mirror index rather than directly importing upstream source.
- Drift check: PASS at dispatch: mirror commit/count match `.private_reference/source_mirrors/INDEX.md`.
- Output traceability: planned worker return and reference must trace contract sections to MSEA owner surfaces or source mirror facts.
- Adversarial verification: contract draft must distinguish docs-only contract vocabulary from runtime readiness, schema implementation, adapter implementation, document truth, extraction accuracy, and production readiness.
- Corpus verdict: PARTIAL

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| MSEA-R7 receipt artifact and field vocabulary | source-backed receipt families and field-family prose | DOCTRINE_ADAPTED | MSEA-R10 adapter contract draft | map receipt vocabulary into adapter contract sections | no schema implementation or receipt writer |
| MSEA-R9 blueprint/readiness route | accepted docs-only adapter contract route | DOCTRINE_ADAPTED | MSEA-R10 adapter contract draft | draft route-binding and non-claim sections | no adapter implementation |
| R4/R5/R8 runtime/provider/S3/Docker/RAG evidence | held candidate surfaces and concrete reopen conditions | RUNTIME_CANDIDATE | MSEA-R10 hold-condition section | preserve holds, do not execute | no install, model download, parser run, provider call, S3, Docker, RAG write, or package activation |
| R4/R8 Docker and deployment evidence | held deployment recipes and package-lane preconditions | PACKAGE_CANDIDATE | MSEA-R10 hold-condition section | preserve package/deployment hold conditions only | no Docker build/run or package activation |
| MSEA-T3/R6 checker candidate evidence | possible overclaim guard remains condition-gated | CHECKER_CANDIDATE | MSEA-R10 non-claim and future-checker note only | preserve no-checker-now unless repeated misses appear | no checker implementation or hook wiring |
| Direct MinerU upstream code | source mirror remains advisory input only | REJECT_DIRECT_IMPORT | MSEA source mirror control | reject direct copy/import; adapt CVF-native doctrine only | no direct import |
| Already-owned evidence | prior MSEA artifacts already own route and receipt facts | NO_PACKAGE_OR_RUNTIME_VALUE | prior MSEA owner surfaces | cite owner surfaces rather than duplicate full scans | no runtime or package behavior |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Receipt artifact and field vocabulary | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`; `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` | ENRICH_EXISTING | R10 turns vocabulary into adapter-contract obligations and non-claims | adapt into R10 reference |
| Application route readiness | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md`; `docs/reference/CVF_MSEA_R9_MINERU_CVF_APPLICATION_BLUEPRINT_AND_ADAPTER_CONTRACT_READINESS_2026-07-02.md` | ENRICH_EXISTING | R10 binds route readiness to adapter contract sections | adapt into R10 reference |
| Runtime/provider/S3/Docker/RAG candidates | `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md`; `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md`; `docs/reference/CVF_MSEA_R8_MINERU_RESIDUAL_FULL_REPOSITORY_ABSORPTION_CLOSURE_LEDGER_2026-07-02.md` | CONFIRMED_EXISTING | R10 preserves hold conditions rather than reopening execution | defer |
| Direct upstream implementation | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`; `.private_reference/source_mirrors/INDEX.md` | REJECT_DIRECT_IMPORT | no direct code import remains allowed | reject import |
| Checker route | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md`; `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md`; `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0023.md` | CONFIRMED_EXISTING | output-shape read-ahead required; no new checker implementation authorized | require worker read-ahead only |

## Source Mirror Migration Control

| Field | Disposition |
|---|---|
| Legacy source path | Legacy MinerU adapter folder remains secondary historical material only |
| Source mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Mirror index row | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Pinned upstream commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Migration disposition | MIGRATED_TO_SOURCE_MIRROR |
| Legacy cleanup disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: historical comparison only; source facts must prefer pinned mirror or governed MSEA artifacts |
| Claim boundary | source-mirror authority control only; no runtime, install, package activation, provider/live proof, public-sync, checker implementation, source import, schema implementation, adapter implementation, or production-readiness claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | ADIF-0023 is still listed as a Required First Read for worker-output shape because the active next move requires output-artifact checker read-ahead even though the dispatcher query returns no defects |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `## Source Verification Block`; `## Negative Search And Collision Discipline`; `## External Knowledge Intake Routing`; `## External Absorption Core`; `## Corpus Completeness And Report Integrity`; `## External Absorption Value Conversion Matrix`; `## Overlap And Novelty Classification`; `## Source Mirror Migration Control`; `## ADIF Defect Registry Disclosure`; `## Checker Source Read-Ahead Block`; `WORKER_RETURN_FULL_GATE_V1`; `requiredGate:`; `individualCheckerSubstitution: FORBIDDEN`; `workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED`; `SINGLE_AGENT_MULTI_ROLE`; `DEFERRED_PRIVATE_ONLY`; `CLAIM_REJECTED_NO_RECEIPT`; `CLAIM_REJECTED_NO_ACTION`; `PARTIAL`; `CHECKER_CANDIDATE`; `REMOVED_OR_REJECTED`; `RESOLVED_BY_DESIGN`; `ledger_terminal=` |
| gateRunPurpose | Confirmation evidence for dispatch readiness, not first discovery |
| claimBoundary | Read-ahead for MSEA-R10 dispatch artifacts only; worker must still read checker source by each output artifact before authoring |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch. No public-sync export is authorized.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R10 baseline for documentation/reference-only MinerU adapter contract draft |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, direct-interception, mandatory-wrapper, provider, parser, adapter, schema, receipt-writer, or production behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | local governed document authoring and future worker document synthesis only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | baseline authorizes pending worker documentation/reference artifacts only |
| forbiddenExpansion | no MinerU runtime, install, model download, parser/OCR/VLM/hybrid/API/router/Gradio/Docker execution, provider/live call, credentials/S3, RAG write, source import, package activation, checker implementation, public-sync, Web/MCP/model-router/action-authority, automatic invocation, benchmark, document-truth, extraction-accuracy, schema implementation, receipt-writer code, adapter implementation, or production-readiness claim |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R10 --title "MinerU Adapter Contract Draft" --date 2026-07-03 --base 7c19b587 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MSEA-R9 accepted at material commit 2a58322b; route OPEN_ADAPTER_CONTRACT_DRAFT_ONLY selected for documentation/reference-only adapter contract draft" --include-worker-return-skeleton --stdout` |
| generatedProfile | packet-kind=generic-worker-dispatch; commit-mode=WORKER_MUST_NOT_COMMIT; worker-return skeleton requested |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced scaffold placeholders with MSEA-R10 source verification, dependency release evidence, external absorption blocks, and no-runtime claim boundary |
| checkerReadAheadConfirmation | read guard orientation, literal-format gotchas, R9 dispatch pattern, applicable MSEA owner surfaces, source mirror anchors, and applicable checker source paths before writing |
| docOnlyNewFields | adapterContractSection; receiptFamilyMapping; applicationRouteBinding; nonRuntimeHoldCondition |
| claimBoundary | scaffold provenance supports dispatch authoring only; no worker completion, runtime/provider/live/public/package/Web/MCP/model-router/action-authority, checker, schema, adapter implementation, or production claim |

## Claim Boundary

This baseline authorizes only MSEA-R10 dispatch packet creation for a delegated
`WORKER_MUST_NOT_COMMIT` documentation/reference tranche. It does not authorize
worker commits, source import, runtime execution, provider/live proof,
credential use, public-sync, package activation, checker implementation,
schema implementation, receipt-writer code, adapter implementation,
Web/MCP/model-router work, action authority, automatic invocation, benchmark,
document-truth, extraction-accuracy, or production-readiness claims.
