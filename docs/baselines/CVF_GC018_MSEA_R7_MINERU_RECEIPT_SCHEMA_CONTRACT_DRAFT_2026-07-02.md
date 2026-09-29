# CVF GC-018 - MSEA-R7 MinerU Receipt Schema Contract Draft

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-02

Batch ID: MSEA-R7

dispatchBaseHead: ce48461e

External knowledge intake routing: REQUIRED

External absorption core: REQUIRED

## Purpose

Authorize a bounded no-commit documentation/reference worker lane that drafts
a CVF-native MinerU receipt schema contract from accepted MSEA-T2/R5/R6 owner
surfaces and the pinned MinerU `output_files.md` evidence. This tranche creates
contract language only; it does not implement a schema, run MinerU, import
source, call a provider, write a RAG index, implement a checker, or claim
production readiness.

## Decision / Baseline / Proposed Tranche

Decision: dispatch MSEA-R7 as a documentation/reference contract-draft worker.

Baseline: MSEA-R6 closed at material commit `2d0b05c4`, selected
`OPEN_RECEIPT_SCHEMA_CONTRACT_DRAFT`, and routed the next move to this fresh
GC-018/work-order authoring lane.

Proposed tranche: a no-commit worker produces a worker return and a CVF-owned
receipt schema contract draft reference. The draft must map upstream receipt
artifacts and field families into CVF language while preserving claim
boundaries and future implementation blockers.

## Scope / Target / Owner Boundary

Allowed worker write scope:

- `docs/reviews/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_WORKER_RETURN_2026-07-02.md`
- `docs/reference/CVF_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`

Allowed source inputs:

- CVF startup/session surfaces and active handoff.
- This GC-018 baseline and paired MSEA-R7 work order.
- MSEA-T2 receipt advisory, MSEA-R5 worker return and owner delta, MSEA-R6
  worker return and route decision matrix.
- The pinned MinerU source mirror only for `docs/en/reference/output_files.md`
  and source-mirror HEAD verification.

Forbidden scope:

- no MinerU install, parser execution, OCR/VLM/hybrid/backend/API/router/Gradio
  execution, Docker run, model download, provider/live proof,
  OpenAI-compatible endpoint call, S3 connection, credential storage, RAG index
  write, benchmark, source import, checker implementation, package activation,
  public-sync, Web/UI work, MCP/CLI adapter implementation, model-router work,
  action authority, automatic invocation, or production-readiness claim;
- no edits to source mirror payload, legacy external folders, runtime source,
  scripts, hooks, CI, governance checker source, active session state, or active
  handoff by the worker;
- no direct copy of upstream MinerU schemas as CVF implementation.

Risk ceiling: R0 documentation/reference contract draft only.

## Authority Chain

| Authority | Path or source | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-07-02 to continue with the next work order after MSEA-R6 | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V32_2026-07-02.md` | ACCEPT |
| MSEA-R6 route decision matrix | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | ACCEPT |
| MSEA-R6 worker return | `docs/reviews/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md` | ACCEPT |
| MSEA-R5 worker return | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | ACCEPT |
| MSEA-R5 owner-surface delta | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | ACCEPT |
| MSEA-T2 receipt advisory | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ACCEPT |
| Source mirror index | `.private_reference/source_mirrors/INDEX.md` | ACCEPT |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MSEA-R6 closure | Material commit `2d0b05c4` accepted the route decision and selected `OPEN_RECEIPT_SCHEMA_CONTRACT_DRAFT` | Fresh GC-018/work order may dispatch a documentation-only receipt contract draft | SATISFIED |
| MSEA-R5 receipt evidence | MSEA-R5 recorded `output_files.md` as concrete receipt schema evidence that enriches MSEA-T2 | R7 may draft contract language from accepted evidence without runtime execution | SATISFIED |
| Runtime boundary | MSEA-R6 explicitly forbids runtime/provider/S3/RAG/checker/package work | R7 remains R0 documentation/reference only | SATISFIED |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Current mode authorizes MSEA-R7 receipt schema contract work-order authoring | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `currentMode` | `msea_r6_accepted_pending_msea_r7_receipt_schema_contract_work_order_authoring` | active session bootstrap | VALUE_SET | ACCEPT |
| MSEA-R6 selected the receipt schema contract route | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | Selected Routing Outcome | `OPEN_RECEIPT_SCHEMA_CONTRACT_DRAFT` | MSEA-R6 route decision matrix | VALUE_SET | ACCEPT |
| MSEA-R6 limits the selected route to future documentation/reference work | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | Next Action Boundary | `OPEN_RECEIPT_SCHEMA_CONTRACT_DRAFT` | MSEA-R6 route decision matrix | VALUE_SET | ACCEPT |
| MSEA-T2 owns receipt vocabulary and defers schema validation until CVF owns schema fields | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | Owner Surface Matrix and checker candidate rows | `MSEA-CC-4` | MSEA-T2 reference | VALUE_SET | ACCEPT |
| MSEA-R5 identified `output_files.md` as concrete receipt schema evidence | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | Findings / Position and Targeted Deep Ledger | `output_files.md` | MSEA-R5 worker return | VALUE_SET | ACCEPT |
| MSEA-R5 owner delta allows CVF-native receipt contract drafting through fresh GC-018 | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | Conditional Reopen Candidates | `Document-extraction receipt schema adoption into a CVF-native receipt contract` | MSEA-R5 owner delta | VALUE_SET | ACCEPT |
| MinerU source mirror is pinned and preferred for current upstream facts | `.private_reference/source_mirrors/INDEX.md` | line 35 | `opendatalab__MinerU`; `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` | source mirror index | VALUE_SET | ACCEPT |
| MinerU documents output artifacts for layout, spans, model, middle, content list, and content list v2 | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` | lines 17, 35, 62, 109, 292, 396, 730-742 | `layout.pdf`; `span.pdf`; `model.json`; `middle.json`; `content_list.json`; `content_list_v2.json` | upstream output-file reference | VALUE_SET | ACCEPT |
| MinerU documents block types, table content, formulas, and structured V2 content fields | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` | lines 129-186, 292-329, 402-426, 474-548 | `type`; `tables`; `interline_equations`; `content`; `math_content` | upstream output-file reference | VALUE_SET | ACCEPT |

## Evidence / Verification

This baseline is supported by the source verification table, current-runtime
freshness table, negative-search table, external absorption blocks, source
mirror migration control, and pre-dispatch gate evidence. It authorizes only
contract-draft dispatch.

## Current Runtime Freshness Verification

| Claim checked | Verification command | Observed result | Disposition |
|---|---|---|---|
| MSEA-R7 planned baseline path was absent before authoring | `Test-Path -LiteralPath 'docs/baselines/CVF_GC018_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md'` | `False` before authoring | ACCEPT |
| MSEA-R7 planned work order path was absent before authoring | `Test-Path -LiteralPath 'docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md'` | `False` before authoring | ACCEPT |
| MSEA-R7 planned worker output paths were absent before authoring | `Test-Path` checks for the planned worker return and reference contract draft | `False`; `False` before authoring | ACCEPT |
| Source mirror HEAD must remain pinned for worker source reads | `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` | worker must confirm `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` before drafting | ACCEPT |

Freshness boundary: no runtime execution, parser behavior, provider behavior,
S3 connectivity, RAG ingestion, adapter readiness, extraction accuracy,
document truth, or production readiness is verified.

## Negative Search And Collision Discipline

| Check | Command | Result | Disposition |
|---|---|---|---|
| Batch collision search | `rg -n "MSEA-R7|MSEA_R7|MinerU Receipt Schema Contract|MINERU_RECEIPT_SCHEMA_CONTRACT" docs CVF_SESSION AGENT_HANDOFF_V32_2026-07-02.md` | pre-authoring path checks were absent; post-authoring search may show this dispatch baseline and work order plus existing session next-move mentions only | ACCEPT |
| Existing worker output path absence | `Test-Path` checks for planned worker return and reference contract draft | both absent before authoring | ACCEPT |
| Existing implementation search | `rg -n "MinerU|mineru" EXTENSIONS governance scripts docs/reference docs/roadmaps docs/reviews docs/work_orders docs/baselines -g "!*MSEA*"` | no CVF-owned MinerU runtime implementation surface is authorized by this dispatch | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Disclosure note: dispatcher invoked `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json`; the resolver returned `totalCandidates=0`.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_rescan_intelligence_hardening.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `External knowledge intake routing: REQUIRED`; `External absorption core: REQUIRED`; `## Source Verification Block`; `## Current Runtime Freshness Verification`; `## Negative Search And Collision Discipline`; `## ADIF Defect Registry Disclosure`; `## Checker Source Read-Ahead Block`; `## External Knowledge Intake Routing`; `## External Absorption Core`; `## Corpus Completeness And Report Integrity`; `## External Absorption Value Conversion Matrix`; `## Overlap And Novelty Classification`; `## Source Mirror Migration Control`; `WORKER_RETURN_FULL_GATE_V1`; `individualCheckerSubstitution: FORBIDDEN`; `workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED`; `SINGLE_AGENT_MULTI_ROLE`; `DEFERRED_PRIVATE_ONLY`; `CLAIM_REJECTED_NO_RECEIPT`; `CLAIM_REJECTED_NO_ACTION`; `PARTIAL` |
| gateRunPurpose | confirmation/evidence run for MSEA-R7 dispatch after checker read-ahead, not first discovery |
| claimBoundary | checker read-ahead proves dispatch authoring diligence only; worker completion and any runtime/provider/public/package/checker behavior remain unproved and unauthorized |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external repo or copied folder -> pinned source mirror and accepted MSEA evidence -> CVF-native receipt schema contract draft reference -> future implementation only by fresh authorization |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | this GC-018 baseline and paired MSEA-R7 work order |
| Disposition | DISPATCH documentation-only contract drafting from accepted external source evidence |
| Claim boundary | dispatch only; no MinerU execution, provider/live proof, credential use, source import, public-sync, package activation, checker implementation, Web/MCP/model-router/action-authority, or production-readiness claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md |
| Input root or repository | `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; local mirror `.private_reference/source_mirrors/opendatalab__MinerU/`; accepted MSEA-T2/R5/R6 evidence |
| Enumeration command | `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU`; MSEA-R7 uses route-specific receipt-schema source anchors and no full-corpus replay |
| Manifest artifact or inline manifest | inline table: `## Receipt Schema Contract Draft Manifest` |
| Processing ledger artifact or inline ledger | inline table: `## Receipt Schema Contract Draft Manifest` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`; `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md`; `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` |
| Unresolved items | contract draft pending worker execution |
| Completion claim boundary | documentation-only contract draft; no runtime/provider/public/package/checker expansion |

## Receipt Schema Contract Draft Manifest

| Contract area | Source-backed input | Required worker output |
|---|---|---|
| Artifact inventory | `layout.pdf`, `span.pdf`, `model.json`, `middle.json`, `content_list.json`, `content_list_v2.json` | CVF receipt artifact family table with claim boundary |
| Coordinate and layout metadata | bounding boxes, page/layer hierarchy, visual debug outputs | field-family notes without accuracy claims |
| Content block taxonomy | text, image, table, equation, chart, code, list, title, footnote, seal subtype | CVF block-type vocabulary mapped to upstream evidence |
| Backend variants | pipeline and VLM output variants plus legacy content list and V2 common content list | variant-disposition section that prevents universal schema claims |
| Downstream readiness | MSEA-T2 receipt/quality/RAG handoff advisory | downstream-use status and forbidden RAG mutation boundary |
| Future validation | MSEA-CC-4 checker candidate | deferred checker-readiness notes only, no checker implementation |

## Corpus Completeness And Report Integrity

- Corpus task class: external repository documentation/reference contract-draft dispatch from accepted MSEA evidence.
- Corpus root: `.private_reference/source_mirrors/opendatalab__MinerU/` plus accepted MSEA-T2/R5/R6 governed artifacts.
- Snapshot time: 2026-07-02 local session.
- Enumeration command: `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU`; MSEA-R7 uses receipt-schema source anchors and no full-corpus replay.
- Manifest artifact or inline manifest: inline `## Receipt Schema Contract Draft Manifest`.
- Manifest hash: inherited from MSEA-R5 full-mirror evidence unless worker detects source mirror drift.
- Processing ledger artifact or inline ledger: planned MSEA-R7 worker return and receipt schema contract draft reference.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=6 contract areas; ledger_terminal=0 at dispatch before worker execution; exclusions=full-corpus replay; unresolved=0.
- Unresolved files: 0
- Declared exclusions: no full 425-file replay and no 373-file replay; R5 already owns that manifest evidence.
- Unreadable or unsupported files: none known at dispatch.
- Aggregation check: all contract areas map to existing MSEA source evidence or source mirror anchors.
- Drift check: worker must verify source mirror commit still matches the index if it reads source files directly.
- Output traceability: contract draft must cite worker return and source verification anchors.
- Adversarial verification: worker must distinguish artifact existence, schema vocabulary, extraction quality, document truth, and runtime readiness.
- Corpus verdict: PARTIAL

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| `output_files.md` receipt artifact list | concrete output artifact families and field vocabulary | DOCTRINE_ADAPTED | planned MSEA-R7 receipt schema contract draft | worker adapts language into CVF-owned contract draft | no parser/schema implementation |
| MSEA-T2 receipt advisory | receipt and quality boundary owner surface | DOCTRINE_ADAPTED | planned MSEA-R7 contract draft | worker enriches existing owner language | no RAG mutation or truth claim |
| RagFlow/RAG integration evidence | downstream package pressure remains relevant but not selected for R7 | PACKAGE_CANDIDATE | MSEA-R6 route decision matrix and MSEA-T2 RAG handoff advisory | worker records deferred boundary only if needed | no plugin wiring, RAG write, or adapter execution |
| Provider and S3 candidates | title-correction and credential surfaces are not part of receipt contract drafting | RUNTIME_CANDIDATE | MSEA-R5 owner delta and MSEA-R6 route matrix | worker preserves forbidden expansion boundary | no provider call, S3 access, or credential use |
| MSEA-CC-4 future schema checker | future validation concept only after CVF owns schema fields | CHECKER_CANDIDATE | MSEA-T2 advisory and planned MSEA-R7 draft | worker may include checker-readiness note | no checker implementation or hook wiring |
| Direct upstream schema/source import | upstream documentation informs CVF language but is not CVF implementation | REJECT_DIRECT_IMPORT | planned MSEA-R7 draft | worker must adapt and cite, not copy as runtime contract | no source import or direct wiring |
| Full-corpus replay after R5/R6 | previous tranches already reconciled source mirror and selected route | NO_PACKAGE_OR_RUNTIME_VALUE | MSEA-R5/R6 accepted artifacts | worker must avoid replay unless drift is detected | no runtime or package behavior |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Receipt contract draft | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ENRICH_EXISTING | concrete schema fields become CVF draft language | create draft reference |
| R5 schema evidence | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | CONFIRMED_EXISTING | R5 already identified the receipt schema adoption candidate | use as dependency-release evidence |
| R6 route decision | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | CONFIRMED_EXISTING | R6 selected this route explicitly | use as dispatch authority |
| Runtime/provider/S3/RAG routes | `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md` | NO_NEW_VALUE | not part of R7 selected documentation route | preserve deferred boundaries |
| Future schema checker | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ENRICH_EXISTING | MSEA-CC-4 can be sharpened after draft exists | record checker-readiness note only |
| Direct upstream source import | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | REJECT_DIRECT_IMPORT | upstream source remains advisory input only | reject direct import |
| Unknown new owner surface | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | OWNER_SURFACE_NOT_FOUND | not expected; worker must return blocker if a necessary owner surface is missing | do not invent owner silently |

## Source Mirror Migration Control

| Field | Disposition |
|---|---|
| Legacy source path | Legacy MinerU adapter folder remains secondary historical material and is not source authority for MSEA-R7. |
| Source mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Mirror index row | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Pinned upstream commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Migration disposition | SOURCE_MIRROR_AUTHORITY_RETAINED_FOR_THIS_TRANCHE |
| Legacy cleanup disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: historical comparison only; source facts must prefer the pinned mirror or governed MSEA artifacts |
| Claim boundary | source-mirror authority control only; no source import, install, runtime execution, provider/live proof, public-sync, checker implementation, or production-readiness claim |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | MSEA-R7 worker return and receipt schema contract draft reference | internal CVF agents may read contract-draft evidence only | this baseline and paired work order | no internal runtime adapter is implemented | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter owner, not this dispatch | external-agent access requires separate source-verified adapter authorization | MinerU has upstream CLI/API evidence from prior MSEA artifacts, but no CVF adapter is authorized here | no ingress, auth, mutation, raw-data, receipt, or public boundary is implemented | DEFERRED_WITH_REASON |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R7 --title "MinerU Receipt Schema Contract Draft" --date 2026-07-02 --base 42cb5e46 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MSEA-R6 accepted at 2d0b05c4; selected OPEN_RECEIPT_SCHEMA_CONTRACT_DRAFT as documentation-only next route" --include-worker-return-skeleton --stdout` |
| generatedProfile | packet-kind=generic-worker-dispatch; commit-mode=WORKER_MUST_NOT_COMMIT; worker-return skeleton requested |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced scaffold fields with MSEA-R7 receipt-contract scope, source verification, external absorption blocks, source mirror migration control, dual-agent matrix, and no-commit worker boundary |
| checkerReadAheadConfirmation | read guard orientation, literal-format gotchas, compact worker-return standard, MSEA-R6 artifacts, MSEA-T2/R5 owner surfaces, source mirror anchors, and applicable checker source paths before writing |
| docOnlyNewFields | receipt schema contract draft path; contract area manifest; artifact family map requirement |
| claimBoundary | scaffold provenance supports dispatch authoring only; no worker completion, runtime/provider/live/public/package/Web/MCP/model-router/action-authority, checker, or production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MSEA-R7 dispatch is private provenance receipt-contract drafting work
derived from private source-mirror absorption evidence. No public-sync artifact
is created or authorized by this baseline.

## Claim Boundary

This GC-018 baseline authorizes MSEA-R7 dispatch only. It does not authorize or
claim MinerU runtime integration, parser execution, OCR execution, VLM/hybrid
backend routing, remote backend processing, model download, API/router/Gradio
service, Docker deployment, RAG indexing, provider/live proof, S3 access,
credential handling, document truth verification, parser accuracy,
table/formula correctness, public-sync export, checker enforcement, package
activation, certification, generated aggregate mutation, production readiness,
hosted readiness, model-router behavior, action authority, or universal
document intelligence.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R7 dispatch baseline and receipt schema contract-draft work-order authorization |
| claimDisposition | CLAIM_REJECTED: no Delta runtime execution-control claim is made |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | local authoring, source verification, and governance checker invocation only |
| interceptionBoundary | no runtime interception, parser execution, provider invocation, S3 access, RAG write, or action-control behavior |
| claimLanguage | source-backed documentation/reference contract-draft dispatch only |
| forbiddenExpansion | no runtime/provider/live/public/package/Web/MCP/model-router/action-authority, automatic invocation, checker implementation, source import, credential handling, or production-readiness claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local workspace |
| Session or invocation | MSEA-R7 dispatch authoring, 2026-07-02 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, git, apply_patch, governance checkers |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R7_MINERU_RECEIPT_SCHEMA_CONTRACT_DRAFT_2026-07-02.md` |
| Allowed scope source | operator request to create the next work order after MSEA-R6 selected `OPEN_RECEIPT_SCHEMA_CONTRACT_DRAFT` |
| Before status evidence | clean worktree at `ce48461e`; planned MSEA-R7 paths absent before authoring |
| After status evidence | dispatch baseline and work order created with source verification and pending pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatcher authoring only; worker execution remains no-commit |
| Claim boundary | no runtime/provider/public/source-import/Web/MCP/model-router/checker/package/action-authority claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r7-mineru-receipt-schema-contract-dispatch-2026-07-02` |
| Expected manifest | baseline and work order paths named above |
| Actual changed set | baseline and work order paths named above |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch artifact creation |
