# CVF GC-018 - MSEA-R5 MinerU Deep Document Layer Scan Absorption

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-02

Batch ID: MSEA-R5

dispatchBaseHead: ca07147e

External knowledge intake routing: REQUIRED

External absorption core: REQUIRED

## Purpose

Authorize a bounded no-commit worker lane to absorb the deeper document-layer
and extraction-layer value left only partially reviewed by MSEA-R4.

MSEA-R5 exists because MSEA-R4 reconciled the full MinerU source mirror but
declared a PARTIAL blind-spot verdict for `docs/` and most non-CLI `mineru/`
internals. The operator confirmed MinerU is high-value for detailed document
and layer-scan use cases, so the next worker must read the high-value source
surfaces in depth while preserving the MSEA runtime and package boundary.

## Decision / Baseline / Proposed Tranche

Decision: dispatch MSEA-R5 as a source-mirror-backed deep absorption worker
tranche for document-layer scan value.

Baseline: MinerU remains advisory external source material pinned in the private
source mirror. CVF-owned conclusions must be recorded in governed review and
reference artifacts, not imported from upstream source.

Proposed tranche: a no-commit worker produces the MSEA-R5 worker return and
owner-surface delta named in the planned fulfillment manifest.

## Scope / Target / Owner Boundary

Target source:

`https://github.com/opendatalab/MinerU.git`

Pinned commit:

`3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`

Local mirror:

`.private_reference/source_mirrors/opendatalab__MinerU/`

MSEA-R5 target subset:

- `docs/` with text documentation read in depth and binary/assets counted with
  explicit disposition.
- `mineru/backend`, `mineru/data`, `mineru/model`, `mineru/resources`, and
  `mineru/utils`.
- Docker deployment files, for content verification and parking only.
- Existing CLI rows from MSEA-R4 may be used as interface context, but MSEA-R5
  must not replay the MSEA-R4 CLI enumeration as its main output.

Allowed write scope:

- `docs/baselines/CVF_GC018_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_2026-07-02.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_2026-07-02.md`
- worker output named by the work order under governed review and reference
  folders only

Forbidden scope:

- no MinerU install, model download, OCR/VLM/hybrid execution, parser run,
  API/router/Gradio/WebUI/server startup, Docker run, REST/API call, remote or
  OpenAI-compatible server routing, RAG index write, benchmark, provider/live
  proof, public-sync, package activation, checker implementation, model-router
  work, action authority, automatic invocation, or production-readiness claim;
- no changes inside the cloned source mirror payload;
- no use of legacy local source copies as source authority;
- no `EXTENSIONS/`, runtime source, hook-chain, CI, `scripts/`, or
  `governance/compat/` implementation changes in MSEA-R5 dispatch;
- no session-state or active-handoff edits by the worker.

Risk ceiling: R0 documentation/reference and private source-mirror control
plane only.

## Authority Chain

| Authority | Path or source | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-07-02 to create a deeper MinerU absorption work order after R4 | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V32_2026-07-02.md` | ACCEPT |
| Guard orientation | `docs/reference/guard_orientation/README.md` | ACCEPT |
| Literal-format gotchas | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | ACCEPT |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | ACCEPT |
| External absorption front door | `docs/reference/external_agent_review/README.md` | ACCEPT |
| External absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | ACCEPT |
| External absorption core standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | ACCEPT |
| Source mirror index | `.private_reference/source_mirrors/INDEX.md` | ACCEPT |
| MSEA-R4 accepted worker return | `docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md` | ACCEPT |
| MSEA-R4 owner-surface delta | `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` | ACCEPT |
| Prior MSEA-T0 roadmap | `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | ACCEPT |
| Prior MSEA-T2 advisory | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ACCEPT |
| Prior MSEA-T3 closeout | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | ACCEPT |

## Dependency Release Evidence

| Dependency | Evidence | Release disposition |
|---|---|---|
| MSEA-R4 closure | material commit `a6ddd8ba` accepted R4 worker output; session wording repair and handoff marker then advanced to `ca07147e` | SATISFIED |
| MSEA-R4 blind-spot finding | R4 worker return recorded PARTIAL coverage for `docs/` and most non-CLI `mineru/` internals | SATISFIED |
| Operator value checkpoint | operator stated MinerU has high application value for detailed document and layer scan use cases | SATISFIED |
| Fresh dispatch authority | this GC-018 and paired work order source-verify the R5 target subset before worker execution | SATISFIED |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Active handoff is V32 for this resumed session | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `activeHandoff` | `AGENT_HANDOFF_V32_2026-07-02.md` | active session state registry | VALUE_SET | ACCEPT |
| Current next move authorizes MSEA-R5 deep absorption dispatch authoring | `AGENT_HANDOFF_V32_2026-07-02.md` | Next allowed move | `MSEA-R5` | active handoff | VALUE_SET | ACCEPT |
| MSEA-R4 accepted the fresh source mirror but left deep blind spots | `docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md` | Findings and Blind-Spot verdict | `PARTIAL` | MSEA-R4 worker return | VALUE_SET | ACCEPT |
| MSEA-R4 owner delta preserves next-route deep documentation and model absorption | `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` | Route notes | `MSEA-R5` | MSEA-R4 owner surface delta | VALUE_SET | ACCEPT |
| MinerU mirror is pinned to upstream commit | `.private_reference/source_mirrors/INDEX.md` | Mirror Ledger row | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` | source mirror index | VALUE_SET | ACCEPT |
| MinerU mirror contains 425 tracked files at dispatch | `.private_reference/source_mirrors/INDEX.md` | Mirror Ledger row | `Tracked file count` | source mirror index | VALUE_SET | ACCEPT |
| MinerU package metadata declares document conversion into Markdown and JSON | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | line 10 | `description` | pyproject metadata | VALUE_SET | ACCEPT |
| MinerU declares VLM, pipeline, and Gradio optional dependency groups | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | lines 74-111 | `vlm`; `pipeline`; `gradio` | pyproject optional dependencies | VALUE_SET | ACCEPT |
| MinerU declares CLI, server, model-download, API, and router entry points | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | lines 129-135 | `mineru`; `mineru-vllm-server`; `mineru-models-download`; `mineru-api`; `mineru-router` | pyproject scripts | VALUE_SET | ACCEPT |
| MinerU README describes layout, formulas, tables, reading order, and RAG relevance | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | lines 49-68; lines 174-183 | `Markdown`; `JSON`; `RAG`; `layout`; `reading order` | upstream README | VALUE_SET | ACCEPT |
| MinerU output docs describe layout, span, middle JSON, content list, table, chart, and equation outputs | `.private_reference/source_mirrors/opendatalab__MinerU/docs/en/reference/output_files.md` | lines 17-31; 129-186; 298-308; 376-426; 671-734 | `layout.pdf`; `span.pdf`; `content_list`; `middle.json` | upstream output-file reference | VALUE_SET | ACCEPT |
| Backend option declarations name public backend choices | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/cli/backend_options.py` | lines 22-43 | `PUBLIC_BACKEND_CHOICES`; `BACKEND_SCHEMA_EXTRA` | MinerU CLI backend option schema | VALUE_SET | ACCEPT |
| VLM backend content builder includes Markdown conversion function | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/backend/vlm/vlm_middle_json_mkcontent.py` | line 359 | `mk_blocks_to_markdown` | MinerU VLM backend content builder | EXISTS | ACCEPT |
| Office backend content builder includes Markdown conversion function | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/backend/office/mkcontent/output_builders.py` | line 350 | `mk_blocks_to_markdown` | MinerU office backend content builder | EXISTS | ACCEPT |
| Data IO surfaces include file, HTTP, and S3 readers or writers | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/data/io/http.py`; `.private_reference/source_mirrors/opendatalab__MinerU/mineru/data/io/s3.py`; `.private_reference/source_mirrors/opendatalab__MinerU/mineru/data/data_reader_writer/filebase.py` | HTTP lines 10-29; S3 lines 52-120; filebase lines 7-48 | `HttpReader`; `S3Reader`; `FileBasedDataReader` | MinerU data IO layer | EXISTS | ACCEPT |
| Model and utility layers include layout labels, OCR, formula processing, table merge, visual regrouping, and title leveling | `.private_reference/source_mirrors/opendatalab__MinerU/mineru/model/layout/pp_doclayoutv2.py`; `.private_reference/source_mirrors/opendatalab__MinerU/mineru/model/ocr/pytorch_paddle.py`; `.private_reference/source_mirrors/opendatalab__MinerU/mineru/model/mfr/pp_formulanet_plus_m/predict_formula.py`; `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/table_merge.py`; `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/visual_magic_model_utils.py`; `.private_reference/source_mirrors/opendatalab__MinerU/mineru/utils/title_level_postprocess.py` | selected source symbols | `pp_doclayoutv2`; `pytorch_paddle`; `predict_formula`; `table_merge`; `visual_magic_model_utils`; `title_level_postprocess` | MinerU model and utility layers | EXISTS | ACCEPT |
| Docker files expose deployment/service candidates that remain parked | `.private_reference/source_mirrors/opendatalab__MinerU/docker/compose.yaml`; `.private_reference/source_mirrors/opendatalab__MinerU/docker/global/Dockerfile`; `.private_reference/source_mirrors/opendatalab__MinerU/docker/china/Dockerfile` | compose service blocks; Dockerfile install/model-download lines | `mineru-openai-server`; `mineru-api`; `mineru-router`; `mineru-gradio`; `mineru-models-download` | Docker deployment recipes | VALUE_SET | ACCEPT |
| MSEA-T2 is the current CVF document-extraction claim-boundary and RAG handoff advisory | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | Status; Central Rule; Document Extraction Rule | `ACTIVE_REFERENCE` | MSEA-T2 advisory | VALUE_SET | ACCEPT |
| MSEA-T3 parked checker implementation until repeated misses or new schema pressure exists | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | Claim Boundary; Machine Closure Package | `MSEA-T3` | MSEA-T3 closeout | VALUE_SET | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Disclosure note: dispatcher invoked `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json`; the resolver returned `totalCandidates=0`.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `External knowledge intake routing: REQUIRED`; `External absorption core: REQUIRED`; `## Source Verification Block`; `## External Knowledge Intake Routing`; `## External Absorption Core`; `## Corpus Completeness And Report Integrity`; `## External Absorption Value Conversion Matrix`; `## Overlap And Novelty Classification`; `## Source Mirror Migration Control`; `## Scaffold Provenance Block`; `## ADIF Defect Registry Disclosure`; `## Dispatch Prompt Envelope`; `## Agent Handoff Contract Control Block`; `## Reviewer Closure Conversion`; `contractProfile: WORKER_RETURN_FULL_GATE_V1`; `requiredGate:`; `run_worker_return_fast_gate.py`; `individualCheckerSubstitution: FORBIDDEN`; `workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED`; `CLAIM_REJECTED_NO_RECEIPT`; `CLAIM_REJECTED_NO_ACTION`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirmation/evidence run for MSEA-R5 dispatch after checker read-ahead, not initial source discovery |
| claimBoundary | checker read-ahead proves authoring diligence only; worker completion and runtime/provider/public/package/checker behavior remain unproved and unauthorized |

## Negative Search And Collision Discipline

| Check | Command | Result | Disposition |
|---|---|---|---|
| Baseline path did not exist before authoring | `Test-Path docs\baselines\CVF_GC018_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_2026-07-02.md` | `False` | ACCEPT |
| Work order path did not exist before authoring | `Test-Path docs\work_orders\CVF_AGENT_WORK_ORDER_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_2026-07-02.md` | `False` | ACCEPT |
| Planned worker-return path did not exist before authoring | checked by dispatch author before authoring | `False` | ACCEPT |
| Planned owner-surface delta path did not exist before authoring | checked by dispatch author before authoring | `False` | ACCEPT |
| Batch token collision search | `rg -n "MSEA-R5|MSEA_R5|MinerU Deep Document Layer Scan Absorption|MINERU_DEEP_DOCUMENT_LAYER_SCAN" docs CVF_SESSION AGENT_HANDOFF_V32_2026-07-02.md` | only active continuity and R4 future-route mentions before authoring | ACCEPT |

## Current Runtime Freshness Verification

| Claim checked | Verification command | Observed result | Disposition |
|---|---|---|---|
| Fresh upstream source mirror exists | `Test-Path '.private_reference/source_mirrors/opendatalab__MinerU/.git'` | `True` | ACCEPT |
| Source mirror remote points to upstream MinerU | `git -C .private_reference/source_mirrors/opendatalab__MinerU remote get-url origin` | `https://github.com/opendatalab/MinerU.git` | ACCEPT |
| Source mirror HEAD is pinned for dispatch | `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` | ACCEPT |
| R5 target subset size is known before worker execution | source-tree grouping and R4 worker ledger | `docs=146`; `mineru non-CLI internals=215`; `docker=12`; target total=373 | ACCEPT |
| CVF did not install or execute MinerU for this dispatch | dispatch command log | only read/enumeration/scaffold/checker commands used | ACCEPT |

Freshness boundary: these checks support only source-mirror and negative runtime
claim boundaries for MSEA-R5 dispatch. They do not authorize execution or prove
parsing quality, OCR correctness, document truth, RAG suitability, or production
readiness.

## Evidence / Verification

Dispatch verification is bounded to source mirror existence, source mirror index
evidence, source verification, negative path search, checker read-ahead,
external absorption blocks, and pre-dispatch governance gates. Deep absorption
completion evidence is assigned to the worker return and must not be claimed by
this dispatch baseline.

## External Absorption Core

| Field | Value |
|---|---|
| Standard | docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md |
| Input root or repository | `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; local mirror `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Enumeration command | `Get-ChildItem -LiteralPath ".private_reference/source_mirrors/opendatalab__MinerU" -Recurse -File -Force` excluding `.git` |
| Manifest artifact or inline manifest | inline `## Dispatch Source Mirror Manifest` table in this file; worker must create R5 target manifest in planned worker return |
| Processing ledger artifact or inline ledger | `docs/reviews/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_WORKER_RETURN_2026-07-02.md` target ledger section |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE, SKIPPED_WITH_REASON |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `docs/reference/CVF_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_OWNER_SURFACE_DELTA_2026-07-02.md` |
| Unresolved items | 373 targeted file rows at dispatch; worker must reduce to 0 or return `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| Completion claim boundary | dispatch and source-mirror intake only; no runtime, provider/live, public, production, OCR/VLM/hybrid execution, model download, API/router/Gradio, Docker, RAG write, checker, package activation, model-router, or action-authority claim |

## Corpus Completeness And Report Integrity

- Corpus task class: upstream external repository deep absorption dispatch.
- Corpus root: `.private_reference/source_mirrors/opendatalab__MinerU/`.
- Snapshot time: 2026-07-02 local session.
- Enumeration command: `Get-ChildItem -LiteralPath ".private_reference/source_mirrors/opendatalab__MinerU" -Recurse -File -Force` excluding `.git`.
- Manifest artifact or inline manifest: dispatch preflight count and hash recorded here; R5 target manifest required in worker return.
- Manifest hash: `sha256:3a0ad960e1d8fc663c5f099c27f8416a0b2d8147718e9788ee298dd653da6a81`.
- Processing ledger artifact or inline ledger: planned worker return.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: full manifest=425; target subset=373; ledger_terminal=0 at dispatch; exclusions=0; unresolved=373.
- Unresolved files: 373 targeted file rows at dispatch.
- Declared exclusions: none at dispatch.
- Unreadable or unsupported files: none known at dispatch.
- Aggregation check: dispatch proves source mirror availability and target subset definition, not absorption completion.
- Drift check: worker must recompute count, commit, hash, and target subset before processing.
- Output traceability: worker maps accepted value to CVF owner surfaces or returns blocked source gaps.
- Adversarial verification: prior MSEA-T0/T2/T3 and MSEA-R4 conclusions must be challenged against the targeted deep source surfaces.
- Corpus verdict: PARTIAL

## Dispatch Source Mirror Manifest

| Manifest item | Evidence |
|---|---|
| Upstream repository | `https://github.com/opendatalab/MinerU.git` |
| Pinned commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Local mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Tracked file count | 425 |
| R5 target subset count | 373 |
| Manifest hash | `sha256:3a0ad960e1d8fc663c5f099c27f8416a0b2d8147718e9788ee298dd653da6a81` |
| R5 target manifest | REQUIRED in planned worker return |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external repo or copied folder -> pinned source mirror -> external absorption core -> R5 target manifest and deep processing ledger -> value conversion matrix -> CVF owner-surface delta -> future package/runtime/checker work order only if separately authorized |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | `docs/baselines/CVF_GC018_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_2026-07-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_2026-07-02.md` |
| Disposition | DISPATCH deep source-mirror absorption review |
| Claim boundary | dispatch only; no runtime, package activation, checker wiring, provider/live proof, public-sync, MCP server, API/router/Gradio, Docker, model download, OCR/VLM/hybrid execution, RAG write, benchmark, or production-readiness claim |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| `docs/` usage and reference documentation | Upstream documentation may refine document-output, backend-choice, setup-boundary, and receipt vocabulary. | DOCTRINE_ADAPTED | planned MSEA-R5 owner-surface delta and existing MSEA-T2 advisory | Worker reads text docs deeply and records reusable doctrine only. | Documentation/reference only |
| Output-file reference for layout, spans, middle JSON, content list, tables, formulas, charts, and equations | Existing CVF extraction doctrine can become more precise about layer receipts and downstream handoff requirements. | DOCTRINE_ADAPTED | MSEA-T2 enrichment notes | Worker maps source-backed output concepts to CVF-owned receipt language. | No parser or output quality claim |
| Backend pipeline, VLM, hybrid, and office conversion builders | Runtime-looking code clarifies candidate layer boundaries for future extraction adapters. | RUNTIME_CANDIDATE | future runtime tranche only after fresh authorization | Worker parks evidence and concrete reopen conditions. | No install, execution, backend routing, or source import |
| Data IO, S3, HTTP, and file reader/writer surfaces | Source-backed storage and remote-input concepts may inform privacy and receipt boundaries. | RUNTIME_CANDIDATE | planned MSEA-R5 owner-surface delta | Worker records candidate controls and risk notes only. | No connector, credential, remote IO, or adapter implementation |
| Layout, OCR, formula, table, title, and visual regrouping code | Source-backed quality layers may inform future checker candidates when CVF sees repeated real misses. | CHECKER_CANDIDATE | future checker roadmap only after fresh source-verified work order | Worker records candidate guard ideas with triggers. | No checker implementation or hook wiring |
| Docker recipes and service compose files | Deployment surfaces are useful for boundary mapping but not current implementation. | PACKAGE_CANDIDATE | future package/deployment tranche only after fresh authorization | Worker verifies content and parks candidate-only evidence. | No Docker run, package mutation, service startup, or model download |
| Binary assets, examples, and non-text resources | Some files may be needed for corpus completeness but add no CVF doctrine. | NO_PACKAGE_OR_RUNTIME_VALUE | worker ledger | Worker counts and dispositions them with reasons. | No runtime or package behavior |
| Direct upstream implementation source | Source can inform CVF-native doctrine but must not be imported. | REJECT_DIRECT_IMPORT | CVF-native rewrite lanes only | Worker rejects direct copy or wiring. | No direct source import |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Multi-format document extraction into Markdown/JSON and layer receipts | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ENRICH_EXISTING | source-backed output files can sharpen receipt and layer-handoff terms | worker enriches owner delta only |
| Deep backend/data/model/utils evidence | `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md`; `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`; `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md`; `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` | NEW_FINDING | R4 did not fully absorb these internals at file-content depth | worker records new findings or no-new-value rows with source anchors |
| Runtime parser, OCR, VLM, hybrid, API, router, Docker, Gradio, model-download, remote-server surfaces | `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md`; `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | ENRICH_EXISTING | more concrete runtime-candidate evidence may exist, but implementation remains parked | worker parks with concrete reopen conditions |
| Direct upstream implementation source | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | REJECT_DIRECT_IMPORT | external source is not CVF authority or implementation | worker rejects direct import |
| Files that only restate already-owned MSEA doctrine | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`; `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` | NO_NEW_VALUE | no meaningful delta after worker comparison | worker closes row with reason |
| Any high-value source item without an existing CVF owner | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | worker must name source-backed gap rather than silently dropping value | worker records blocker or proposed future owner route |

## Source Mirror Migration Control

| Field | Disposition |
|---|---|
| Legacy source path | Legacy external repo clone and legacy adapter folder are not source authority for MSEA-R5; this dispatch uses the fresh source mirror instead. |
| Source mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Mirror index row | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Pinned upstream commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Migration disposition | SOURCE_MIRROR_AUTHORITY_RETAINED_FOR_THIS_TRANCHE |
| Legacy cleanup disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: older local copies may be read only for historical comparison and must not override current upstream facts |
| Claim boundary | source-mirror authority control only; no source import, package install, runtime execution, provider/live proof, public-sync, checker implementation, or production-readiness claim |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | planned MSEA-R5 worker return and owner-surface delta | internal CVF agents may read documentation/reference output only; no action authority | this baseline and work order | N/A with reason: no internal runtime adapter is implemented | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP adapter owner, not this dispatch | external agent use requires separate source-verified adapter/runtime authorization | upstream MinerU advertises CLI/API/MCP-adjacent surfaces, but CVF has not implemented them | deferred adapter owner; no ingress, auth, mutation, raw-data, receipt, or public boundary is implemented here | DEFERRED_WITH_REASON |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R5 --title "MinerU Deep Document Layer Scan Absorption" --date 2026-07-02 --base ca07147e --commit-mode WORKER_MUST_NOT_COMMIT --dependency "MSEA-R4 closed bounded at a6ddd8ba with PARTIAL blind-spot verdict; operator confirms MinerU high-value detailed document/layer scan use case" --include-worker-return-skeleton --stdout` |
| generatedProfile | packet-kind=generic-worker-dispatch; commit-mode=WORKER_MUST_NOT_COMMIT; worker-return skeleton requested |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced scaffold fields with MinerU R5 target subset, MSEA-R4 release evidence, source verification, external absorption blocks, migration control, and worker boundary text |
| checkerReadAheadConfirmation | read guard orientation, literal-format gotchas, work-order template, external absorption standards, scaffold provenance standard, and applicable checker source paths before writing |
| docOnlyNewFields | planned MSEA-R5 worker return path; planned MSEA-R5 owner-surface delta path; R5 target subset count; deep ledger obligation |
| claimBoundary | scaffold provenance supports dispatch authoring only; no worker completion, runtime/provider/live/public/package/Web/MCP/model-router/action-authority, checker, or production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MSEA-R5 dispatch is private provenance source-mirror absorption work.
No public-sync artifact is created or authorized by this baseline.

## Claim Boundary

This GC-018 baseline authorizes MSEA-R5 dispatch only. It does not authorize or
claim MinerU runtime integration, parser execution, OCR execution, VLM/hybrid
backend routing, remote backend processing, model download, API/router/Gradio
service, Docker deployment, RAG indexing, document truth verification, parser
accuracy, table/formula correctness, public-sync export, checker enforcement,
package activation, certification, generated aggregate mutation, production
readiness, hosted readiness, model-router behavior, action authority, or
universal document intelligence.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-R5 dispatch baseline and work-order authorization |
| claimDisposition | CLAIM_REJECTED: no Delta runtime execution-control claim is made |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action is executed or observed |
| invocationBoundary | local authoring, source-mirror enumeration, and governance checker invocation only |
| interceptionBoundary | no runtime interception, parser execution, provider invocation, or action-control behavior |
| claimLanguage | source-mirror dispatch and documentation/reference authorization only |
| forbiddenExpansion | no runtime/provider/live/public/package/Web/MCP/model-router/action-authority, automatic invocation, checker implementation, source import, or production-readiness claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | local workspace |
| Session or invocation | MSEA-R5 dispatch authoring, 2026-07-02 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, git, apply_patch, governance checkers |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_2026-07-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R5_MINERU_DEEP_DOCUMENT_LAYER_SCAN_ABSORPTION_2026-07-02.md` |
| Allowed scope source | operator request to create a deeper MinerU absorption work order after MSEA-R4 |
| Before status evidence | clean worktree confirmed before dispatch authoring; planned MSEA-R5 paths returned `False` in negative search |
| After status evidence | dispatch baseline and work order created with source verification and pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatcher authoring only; worker execution remains no-commit |
| Claim boundary | no runtime/provider/public/source-import/Web/MCP/model-router/checker/package/action-authority claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r5-mineru-deep-document-layer-scan-dispatch-2026-07-02` |
| Expected manifest | baseline and work order paths named above |
| Actual changed set | baseline and work order paths named above |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch artifact creation |
