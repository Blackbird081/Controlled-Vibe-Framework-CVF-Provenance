# CVF GC-018 - MSEA-R6 MinerU Application Route Decision And Adapter Readiness Selection

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-02

Batch ID: MSEA-R6

dispatchBaseHead: 088fdcb4

External knowledge intake routing: REQUIRED

External absorption core: REQUIRED

## Purpose

Authorize a bounded no-commit worker lane that converts MSEA-R4 and MSEA-R5
MinerU absorption evidence into a source-backed application-route decision.
This tranche chooses the next MinerU lane or holds all implementation lanes;
it does not implement an adapter, run MinerU, call a provider, use credentials,
write a RAG index, build a checker, or claim production readiness.

## Decision / Baseline / Proposed Tranche

Decision: dispatch MSEA-R6 as a documentation/reference decision worker.

Baseline: MSEA-R5 accepted source-mirror-backed deep absorption at material
commit `1bac8163` and session-sync commit `088fdcb4`. It reconciled the full
MinerU mirror 425/425 and the R5 target subset 373/373, then parked candidate
evidence for receipt-schema adoption, RagFlow/RAG integration, an
OpenAI-compatible title-correction surface, S3 credential storage, table/layout
quality layers, Docker deployment, and checker candidates.

Proposed tranche: a no-commit worker produces the route decision worker return
and a compact route decision matrix. The worker must select one routing outcome
from the allowed outcome vocabulary or return a source-backed blocker.

## Scope / Target / Owner Boundary

Allowed write scope:

- `docs/reviews/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_WORKER_RETURN_2026-07-02.md`
- `docs/reference/CVF_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_MATRIX_2026-07-02.md`

Allowed source inputs:

- CVF startup/session surfaces and active handoff.
- MSEA-T0, MSEA-T2, MSEA-T3, MSEA-R4, and MSEA-R5 governed artifacts.
- `.private_reference/source_mirrors/INDEX.md`.
- The pinned MinerU source mirror only for source verification of route
  candidates already identified by MSEA-R5.
- `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md`
  for existing MSEA checker-candidate reopen conditions.

Forbidden scope:

- no MinerU install, parser execution, OCR/VLM/hybrid/backend/API/router/Gradio
  execution, Docker run, model download, provider/live proof, OpenAI-compatible
  endpoint call, S3 connection, credential storage, RAG index write, benchmark,
  source import, checker implementation, package activation, public-sync,
  Web/UI work, MCP/CLI adapter implementation, model-router work, action
  authority, automatic invocation, or production-readiness claim;
- no edits to source mirror payload, `.private_reference/legacy/`, `EXTENSIONS/`,
  runtime source, scripts, hooks, CI, `governance/compat/`, active session
  state, or active handoff by the worker;
- no direct import or copy of upstream MinerU source into CVF implementation.

Risk ceiling: R0 documentation/reference and decision-only routing.

## Authority Chain

| Authority | Path or source | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-07-02 to issue the next MinerU work order after MSEA-R5 acceptance | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V32_2026-07-02.md` | ACCEPT |
| MSEA-R5 accepted worker return | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | ACCEPT |
| MSEA-R5 owner-surface delta | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | ACCEPT |
| MSEA-R4 accepted worker return | `docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md` | ACCEPT |
| MSEA-T2 advisory | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ACCEPT |
| MSEA-T3 closeout | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | ACCEPT |
| Source mirror index | `.private_reference/source_mirrors/INDEX.md` | ACCEPT |
| External absorption conditional reopen index | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | ACCEPT |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| MSEA-R5 closure | Material commit `1bac8163` accepted the worker return and owner-surface delta; session-sync commit `088fdcb4` changed next move to operator route selection | Fresh route decision may dispatch after R5 acceptance and session-sync alignment | SATISFIED |
| Operator route selection | User requested the next work order after R5 and previously named detailed document/layer scan as high-value | A decision-only tranche may translate existing evidence into next-route selection | SATISFIED |
| Runtime boundary | R5 kept all implementation candidates `DEFER_DEMAND_GATED` or candidate-only | MSEA-R6 may decide a route but must not execute or claim runtime behavior | SATISFIED |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Current mode is pending next MinerU route decision | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `currentMode` | `msea_r5_accepted_pending_next_mineru_route_decision` | active session bootstrap | VALUE_SET | ACCEPT |
| MSEA-R5 accepted full mirror and target subset reconciliation | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | Full Mirror Manifest and R5 Target Subset Manifest | `425/425`; `373/373` | MSEA-R5 worker return | VALUE_SET | ACCEPT |
| MSEA-R5 selected decision routing rather than implementation | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | Selected Routing Outcome and Follow-Up Routing Matrix | `STRATEGIC_OPERATOR_DECISION` | MSEA-R5 worker return | VALUE_SET | ACCEPT |
| MSEA-R5 owner delta parks receipt schema adoption behind fresh GC-018 | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | Conditional Reopen Candidates | `Document-extraction receipt schema adoption into a CVF-native receipt contract` | MSEA-R5 owner-surface delta | VALUE_SET | ACCEPT |
| MSEA-R5 owner delta parks OpenAI-compatible provider-call surface behind live/provider proof boundary | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | Conditional Reopen Candidates | `llm_aided.py` | MSEA-R5 owner-surface delta | VALUE_SET | ACCEPT |
| MSEA-R5 owner delta parks S3 credential surface behind credential-handling boundary | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | Conditional Reopen Candidates | `s3.py` | MSEA-R5 owner-surface delta | VALUE_SET | ACCEPT |
| MinerU source mirror is pinned and preferred for current upstream facts | `.private_reference/source_mirrors/INDEX.md` | Mirror Ledger row `opendatalab__MinerU` | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` | source mirror index | VALUE_SET | ACCEPT |
| MinerU output files document layer, model, middle, and content-list receipts | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` | lines 17, 35, 62, 109, 292, 396, 730-742 | `layout.pdf`; `span.pdf`; `model.json`; `middle.json`; `content_list.json`; `content_list_v2.json` | upstream output-file reference | VALUE_SET | ACCEPT |
| RagFlow guide names MinerU as a built-in PDF parser and local deployment integration | `.private_reference/source_mirrors/opendatalab__MinerU/docs/zh/usage/plugin/RagFlow.md` | lines 1-68 | `RagFlow`; `MINERU_EXECUTABLE` | upstream RagFlow plugin guide | VALUE_SET | ACCEPT |
| MinerU utility layer instantiates OpenAI-compatible client from caller-supplied config | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/llm_aided.py` | lines 6; 164-166 | `OpenAI`; `api_key`; `base_url` | MinerU LLM-aided title utility | EXISTS | ACCEPT |
| MinerU S3 reader requires access key, secret key, endpoint URL, and on-demand boto3 import | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/data/io/s3.py` | lines 6-15; 18-45; 90-113 | `S3Reader`; `ak`; `sk`; `endpoint_url`; `boto3` | MinerU S3 IO layer | EXISTS | ACCEPT |
| Existing MSEA checker candidates are parked behind concrete reopen conditions | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | rows `MSEA-document-truth-overclaim-checker`, `MSEA-runtime-readiness-overclaim-checker`, `MSEA-rag-handoff-checker` | `PARKED_UNTIL_CONDITION` | external absorption conditional reopen index | VALUE_SET | ACCEPT |

## Evidence / Verification

This baseline is supported by the source verification table, current-runtime
freshness table, negative-search table, external absorption core block, corpus
completeness block, source mirror migration control, and pre-dispatch gate
evidence. It authorizes only route-decision dispatch and does not verify any
MinerU runtime behavior.

## Current Runtime Freshness Verification

| Claim checked | Verification command | Observed result | Disposition |
|---|---|---|---|
| No current CVF-owned MinerU runtime adapter implementation is visible outside governed MSEA/reference evidence | `rg -n "MinerU|mineru" EXTENSIONS governance scripts docs/reference docs/roadmaps docs/reviews docs/work_orders docs/baselines -g "!*MSEA*"` | returned only external absorption conditional-reopen index rows for MSEA checker candidates | ACCEPT |
| Provider registry surfaces are accounted for as out of scope | `Test-Path EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`; `rg -n "PROVIDER_CAPABILITY_REGISTRY" EXTENSIONS/CVF_MODEL_GATEWAY/src -g "*.ts"` | provider registry exists; `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` declares `PROVIDER_CAPABILITY_REGISTRY`; MSEA-R6 makes no provider registry absence, provider-routing, hardcoded-provider, or live-governance claim | ACCEPT |
| MSEA-R6 planned baseline path did not exist before authoring | `Test-Path docs\baselines\CVF_GC018_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_2026-07-02.md` | `False` before authoring | ACCEPT |
| MSEA-R6 planned work order path did not exist before authoring | `Test-Path docs\work_orders\CVF_AGENT_WORK_ORDER_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_2026-07-02.md` | `False` before authoring | ACCEPT |

Freshness boundary: this verification supports only decision-route dispatch.
It does not prove MinerU execution, parser behavior, provider behavior, S3
connectivity, RAG ingestion, adapter readiness, accuracy, document truth, or
production readiness.

## Negative Search And Collision Discipline

| Check | Command | Result | Disposition |
|---|---|---|---|
| Batch collision search | `rg -n "MSEA-R6|MSEA_R6|MinerU Application Route Decision|MINERU_APPLICATION_ROUTE_DECISION|MinerU Route Decision" docs CVF_SESSION AGENT_HANDOFF_V32_2026-07-02.md` | only R5 future-route mentions before authoring | ACCEPT |
| Planned output path absence | checked with `Test-Path` before authoring for both planned worker output files | both absent before authoring | ACCEPT |
| Existing runtime adapter search | `rg -n "MinerU|mineru" EXTENSIONS governance scripts docs/reference docs/roadmaps docs/reviews docs/work_orders docs/baselines -g "!*MSEA*"` | no implementation surface outside governed reference/conditional-reopen evidence | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Disclosure note: dispatcher invoked `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json`; the resolver returned `totalCandidates=0`.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `External knowledge intake routing: REQUIRED`; `External absorption core: REQUIRED`; `## Source Verification Block`; `## Current Runtime Freshness Verification`; `## Negative Search And Collision Discipline`; `## ADIF Defect Registry Disclosure`; `## Checker Source Read-Ahead Block`; `## External Knowledge Intake Routing`; `## External Absorption Core`; `## Corpus Completeness And Report Integrity`; `## External Absorption Value Conversion Matrix`; `## Overlap And Novelty Classification`; `WORKER_RETURN_FULL_GATE_V1`; `individualCheckerSubstitution: FORBIDDEN`; `workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED`; `SINGLE_AGENT_MULTI_ROLE`; `DEFERRED_PRIVATE_ONLY`; `CLAIM_REJECTED_NO_RECEIPT`; `CLAIM_REJECTED_NO_ACTION` |
| gateRunPurpose | confirmation/evidence run for MSEA-R6 dispatch after checker read-ahead, not first discovery |
| claimBoundary | checker read-ahead proves dispatch authoring diligence only; worker completion and any runtime/provider/public/package/checker behavior remain unproved and unauthorized |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external repo or copied folder -> pinned source mirror and accepted MSEA evidence -> route decision matrix -> future GC-018/work order only if a route is selected |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | this GC-018 baseline and paired MSEA-R6 work order |
| Disposition | DISPATCH decision-only source-backed route selection |
| Claim boundary | dispatch only; no MinerU execution, provider/live proof, credential use, source import, public-sync, package activation, checker implementation, Web/MCP/model-router/action-authority, or production-readiness claim |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md |
| Input root or repository | `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; local mirror `.private_reference/source_mirrors/opendatalab__MinerU/`; accepted MSEA-R5 evidence at `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` |
| Enumeration command | R5 verified full mirror 425/425 and target subset 373/373; MSEA-R6 worker must spot-check route-specific source anchors rather than replay the full corpus |
| Manifest artifact or inline manifest | inline table: `## Route Candidate Manifest` table in this file and planned route decision matrix |
| Processing ledger artifact or inline ledger | inline table: planned worker return route-evaluation ledger |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | inline table: planned MSEA-R6 route decision matrix |
| Unresolved items | route selection pending worker evaluation |
| Completion claim boundary | decision-only route selection; no runtime/provider/public/package/checker expansion |

## Route Candidate Manifest

| Candidate route | Source-backed input | Minimum worker decision |
|---|---|---|
| `OPEN_RECEIPT_SCHEMA_CONTRACT_DRAFT` | `output_files.md` schema and MSEA-T2/MSEA-R5 owner surfaces | select only if schema-contract drafting is the highest value next documentation lane |
| `OPEN_LOCAL_PARSER_ADAPTER_VALUE_PROBE` | CLI/API/backend evidence from MSEA-R4/R5 | select only if bounded runtime proof should be proposed for a later fresh work order |
| `OPEN_RAG_HANDOFF_ROUTE_PROBE` | RagFlow integration and MSEA-T2 RAG-handoff doctrine | select only if RAG handoff becomes the next source-backed product route |
| `OPEN_PROVIDER_ASSISTED_TITLE_CORRECTION_PROBE` | `llm_aided.py` OpenAI-compatible title-correction surface | select only if provider/live-proof boundary is explicitly required later |
| `OPEN_STORAGE_CREDENTIAL_BOUNDARY_PROBE` | `s3.py` S3 reader credential surface | select only if remote-storage credential handling is the next route |
| `OPEN_CHECKER_CANDIDATE_VALUE_PROBE` | MSEA-T3 and conditional reopen index checker rows | select only if existing reopen conditions are met or a current source-backed checker gap is found |
| `HOLD_ALL_IMPLEMENTATION_LANES` | no source-backed route outranks hold | select if evidence supports value parking without immediate next implementation |

## Corpus Completeness And Report Integrity

- Corpus task class: external repository route-decision dispatch from accepted MSEA evidence.
- Corpus root: `.private_reference/source_mirrors/opendatalab__MinerU/` plus accepted MSEA-R4/R5 governed artifacts.
- Snapshot time: 2026-07-02 local session.
- Enumeration command: `rg --files --hidden --no-ignore .private_reference/source_mirrors/opendatalab__MinerU`; R5 accepted the source-mirror manifest evidence, so MSEA-R6 uses route-specific source-anchor spot checks and no full-corpus replay.
- Manifest artifact or inline manifest: inline `## Route Candidate Manifest`.
- Manifest hash: inherited from MSEA-R5 worker return evidence; worker may recompute if using source mirror facts beyond listed anchors.
- Processing ledger artifact or inline ledger: planned MSEA-R6 worker return route-evaluation ledger.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=7 route candidates; ledger_terminal=0 at dispatch before worker execution; exclusions=R5 full-corpus replay; unresolved=0.
- Unresolved files: 0
- Declared exclusions: no full 425-file replay and no 373-file replay; R5 already owns that manifest evidence.
- Unreadable or unsupported files: none known at dispatch.
- Aggregation check: all route candidates map to existing MSEA source evidence or source mirror anchors.
- Drift check: worker must verify source mirror commit still matches the index if it reads source files directly.
- Output traceability: selected route must cite the worker return and route decision matrix.
- Adversarial verification: worker must compare route selection against R5 limits and MSEA-T3 parked checker conditions.
- Corpus verdict: PARTIAL

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Blind-spot control applicability | REQUIRED because this dispatch references source-mirror and legacy-reference boundaries. |
| Prior coverage basis | MSEA-R5 accepted 425/425 full mirror and 373/373 target subset evidence with declared PARTIAL limits. |
| MSEA-R6 coverage boundary | route-decision spot checks only; no full-corpus replay and no silent `NO_NEW_VALUE` conclusion. |
| Declared blind spot | worker must carry forward R5 model/utils and Docker hardware-variant limitations if relevant to route selection. |
| Required worker action | evaluate every route candidate and record selected outcome or blocker with source-backed evidence. |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| `output_files.md` and MSEA-T2/MSEA-R5 receipt evidence | Concrete output receipt vocabulary for layout, spans, model, middle, content list, tables, formulas, and V2 content list | DOCTRINE_ADAPTED | planned MSEA-R6 route decision matrix and existing MSEA-T2 advisory | Worker may select a receipt-schema contract draft as a later documentation lane | No schema implementation or parser claim |
| RagFlow and other plugin integration evidence | Shipped integration evidence and RAG handoff route pressure | PACKAGE_CANDIDATE | planned route decision matrix and MSEA-T2 RAG-handoff owner surface | Worker may recommend a later RAG handoff value probe | No plugin wiring, RAG write, or adapter execution |
| `llm_aided.py` title-correction provider surface | OpenAI-compatible client with caller-supplied `api_key` and `base_url` | RUNTIME_CANDIDATE | planned route decision matrix and MSEA-R5 owner delta | Worker may park or recommend later provider/live-proof probe | No provider call or credential use |
| `s3.py` S3 reader storage surface | Credential-requiring remote IO with `ak`, `sk`, and `endpoint_url` | RUNTIME_CANDIDATE | planned route decision matrix and MSEA-R5 owner delta | Worker may park or recommend later credential-boundary probe | No S3 connection or credential storage |
| MSEA-T3 and conditional reopen index checker rows | Document-truth, runtime-readiness, and RAG-handoff checker candidates | CHECKER_CANDIDATE | conditional reopen index and planned route decision matrix | Worker may hold unless concrete reopen conditions are met | No checker implementation or hook wiring |
| Direct upstream implementation source | Source informs CVF-native decisions but is not CVF implementation | REJECT_DIRECT_IMPORT | planned route decision matrix | Worker rejects direct copy/import | No source import or direct wiring |
| Full-corpus replay after R5 | R5 already reconciled the full mirror and target subset | NO_PACKAGE_OR_RUNTIME_VALUE | MSEA-R5 accepted worker return | Worker must not spend the tranche recreating the R5 ledger unless drift is detected | No runtime or package behavior |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Receipt schema route | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`; `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | ENRICH_EXISTING | R5 makes the downstream receipt-contract route concrete but not implemented | evaluate as route option |
| RAG handoff route | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ENRICH_EXISTING | RagFlow evidence is stronger than the earlier generic RAG claim | evaluate as route option |
| Provider-assisted title route | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | NEW_FINDING | distinct provider-call surface inside utility layer | park or recommend later live-proof probe |
| S3 storage route | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` | NEW_FINDING | distinct credential-handling surface | park or recommend later credential-boundary probe |
| Checker route | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CONDITIONAL_REOPEN_INDEX.md` | CONFIRMED_EXISTING | existing parked checker rows remain the owner unless reopen conditions are met | evaluate conditions, do not duplicate rows |
| Direct source import | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | REJECT_DIRECT_IMPORT | upstream source remains external advisory input only | reject direct import |
| Full R5 replay | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` | NO_NEW_VALUE | replaying the same manifest adds no route-decision value unless drift is detected | avoid replay |

## Source Mirror Migration Control

| Field | Disposition |
|---|---|
| Legacy source path | Legacy adapter folder remains secondary historical material and is not source authority for MSEA-R6. |
| Source mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Mirror index row | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Pinned upstream commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Migration disposition | SOURCE_MIRROR_AUTHORITY_RETAINED_FOR_THIS_TRANCHE |
| Legacy cleanup disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: historical comparison only; source facts must prefer the pinned mirror or governed MSEA artifacts |
| Claim boundary | source-mirror authority control only; no source import, install, runtime execution, provider/live proof, public-sync, checker implementation, or production-readiness claim |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | MSEA-R6 worker return and route decision matrix | internal CVF agents may read decision evidence only | this baseline and paired work order | no internal runtime adapter is implemented | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter owner, not this dispatch | external-agent access requires separate source-verified adapter authorization | MinerU has CLI/API evidence from prior MSEA artifacts, but no CVF adapter is authorized here | no ingress, auth, mutation, raw-data, receipt, or public boundary is implemented | DEFERRED_WITH_REASON |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R6 --title "MinerU Application Route Decision And Adapter Readiness Selection" --date 2026-07-02 --base 088fdcb4 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MSEA-R5 accepted at 1bac8163; operator selected next MinerU route decision after high-value document/layer scan absorption" --include-worker-return-skeleton --stdout` |
| generatedProfile | packet-kind=generic-worker-dispatch; commit-mode=WORKER_MUST_NOT_COMMIT; worker-return skeleton requested |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced scaffold fields with MSEA-R6 route decision scope, source verification, external absorption blocks, source mirror migration control, dual-agent matrix, and no-commit worker boundary |
| checkerReadAheadConfirmation | read guard orientation, literal-format gotchas, work-order template, external absorption standards, source mirror index, MSEA-R5 artifacts, and applicable checker source paths before writing |
| docOnlyNewFields | route candidate manifest; selected routing outcome vocabulary; route decision matrix path |
| claimBoundary | scaffold provenance supports dispatch authoring only; no worker completion, runtime/provider/live/public/package/Web/MCP/model-router/action-authority, checker, or production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MSEA-R6 dispatch is private provenance route-decision work derived from
private source-mirror absorption evidence. No public-sync artifact is created
or authorized by this baseline.

## Claim Boundary

This GC-018 baseline authorizes MSEA-R6 dispatch only. It does not authorize or
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
| claimScope | MSEA-R6 dispatch baseline and route-decision work-order authorization |
| claimDisposition | CLAIM_REJECTED: no Delta runtime execution-control claim is made |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | local authoring, source verification, and governance checker invocation only |
| interceptionBoundary | no runtime interception, parser execution, provider invocation, S3 access, or action-control behavior |
| claimLanguage | source-backed decision-route dispatch only |
| forbiddenExpansion | no runtime/provider/live/public/package/Web/MCP/model-router/action-authority, automatic invocation, checker implementation, source import, credential handling, or production-readiness claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local workspace |
| Session or invocation | MSEA-R6 dispatch authoring, 2026-07-02 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, git, apply_patch, governance checkers |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_2026-07-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R6_MINERU_APPLICATION_ROUTE_DECISION_AND_ADAPTER_READINESS_SELECTION_2026-07-02.md` |
| Allowed scope source | operator request to issue the next MinerU work order after MSEA-R5 acceptance |
| Before status evidence | clean worktree at `088fdcb4`; planned MSEA-R6 paths absent before authoring |
| After status evidence | dispatch baseline and work order created with source verification and pending pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatcher authoring only; worker execution remains no-commit |
| Claim boundary | no runtime/provider/public/source-import/Web/MCP/model-router/checker/package/action-authority claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r6-mineru-application-route-decision-dispatch-2026-07-02` |
| Expected manifest | baseline and work order paths named above |
| Actual changed set | baseline and work order paths named above |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch artifact creation |
