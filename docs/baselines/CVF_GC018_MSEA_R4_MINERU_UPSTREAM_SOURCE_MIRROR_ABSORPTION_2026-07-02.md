# CVF GC-018 - MSEA-R4 MinerU Upstream Source Mirror Absorption

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-02

Batch ID: MSEA-R4

dispatchBaseHead: 4d6cd237

External knowledge intake routing: REQUIRED

External absorption core: REQUIRED

## Purpose

Authorize a bounded no-commit worker lane to absorb the freshly pinned
`opendatalab/MinerU` upstream source mirror into CVF-owned MSEA owner-surface
evidence.

MSEA-R4 exists because the operator explicitly requested a fresh clone into
`.private_reference/source_mirrors/` rather than relying on older local source
copies. This baseline authorizes dispatch only: the worker may read the pinned
upstream mirror, produce a worker-return review and owner-surface delta, and
classify doctrine/package/runtime/checker value without installing or running
MinerU.

## Decision / Baseline / Proposed Tranche

Decision: dispatch MSEA-R4 as a source-mirror-backed external absorption
worker tranche.

Baseline: MinerU is advisory external source material pinned in a private
source mirror. CVF-owned conclusions must be recorded in governed review and
reference artifacts, not imported from upstream source.

Proposed tranche: no-commit worker produces the MSEA-R4 worker return and
owner-surface delta named in the planned fulfillment manifest.

## Scope / Target / Owner Boundary

Target source:

`https://github.com/opendatalab/MinerU.git`

Pinned commit:

`3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`

Local mirror:

`.private_reference/source_mirrors/opendatalab__MinerU/`

Allowed write scope:

- `docs/baselines/CVF_GC018_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md`
- planned worker output under `docs/reviews/` and `docs/reference/` named by
  the work order only

Forbidden scope:

- no MinerU install, model download, OCR/VLM/hybrid execution, parser run,
  API/router/Gradio/WebUI/server startup, Docker run, REST/API call, remote or
  OpenAI-compatible server routing, RAG index write, benchmark, provider/live
  proof, public-sync, package activation, checker implementation, model-router
  work, action authority, automatic invocation, or production-readiness claim;
- no changes inside the cloned source mirror payload;
- no use of legacy local source copies as source authority;
- no `EXTENSIONS/`, runtime source, hook-chain, CI, `scripts/`, or
  `governance/compat/` implementation changes in MSEA-R4 dispatch;
- no session-state or active-handoff edits by the worker.

Risk ceiling: R0 documentation/reference and private source-mirror control
plane only.

## Authority Chain

| Authority | Path or source | Disposition |
|---|---|---|
| Operator instruction | chat request on 2026-07-02 to clone MinerU fresh into source mirrors and create the work order | ACCEPT |
| Active session front door | `CVF_SESSION_MEMORY.md` | ACCEPT |
| Bootstrap read model | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | ACCEPT |
| Active state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Active handoff | `AGENT_HANDOFF_V31_2026-07-02.md` | ACCEPT |
| Guard orientation | `docs/reference/guard_orientation/README.md` | ACCEPT |
| Literal-format gotchas | `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | ACCEPT |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | ACCEPT |
| External absorption front door | `docs/reference/external_agent_review/README.md` | ACCEPT |
| External absorption chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | ACCEPT |
| External absorption core standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | ACCEPT |
| Source mirror index | `.private_reference/source_mirrors/INDEX.md` | ACCEPT |
| Prior MSEA-T0 roadmap | `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | ACCEPT |
| Prior MSEA-T1 baseline | `docs/baselines/CVF_GC018_MSEA_T1_SOURCE_VERIFIED_DOCUMENT_EXTRACTION_RECONCILIATION_2026-06-28.md` | ACCEPT |
| Prior MSEA-T2 advisory | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ACCEPT |
| Prior MSEA-T3 closeout | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | ACCEPT |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Active handoff is V31 for this resumed session | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | `activeHandoff` | `AGENT_HANDOFF_V31_2026-07-02.md` | active session state registry | VALUE_SET | ACCEPT |
| MSEA-R4 uses the fresh source mirror rather than older source copies | `.private_reference/source_mirrors/INDEX.md` | Mirror Ledger row | `opendatalab__MinerU` | source mirror index | VALUE_SET | ACCEPT |
| MinerU mirror is pinned to upstream commit | `.private_reference/source_mirrors/INDEX.md` | Mirror Ledger row | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` | source mirror index | VALUE_SET | ACCEPT |
| MinerU mirror contains 425 tracked files at dispatch | `.private_reference/source_mirrors/INDEX.md` | Mirror Ledger row | `Tracked file count` | source mirror index | VALUE_SET | ACCEPT |
| External repo intake must route through manifest, ledger, owner map, and value conversion | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | Central Core; Required Artifact Block; Required Value Conversion Matrix | `External Absorption Core` | external absorption core standard | VALUE_SET | ACCEPT |
| High-value upstream repo absorption should use a source mirror when available | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | Source Mirror Discipline | `.private_reference/source_mirrors/` | external absorption core standard | LITERAL_INVARIANT | ACCEPT |
| MinerU package identity is visible in upstream package metadata | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | line 6; line 10 | `name`; `description` | pyproject metadata | VALUE_SET | ACCEPT |
| MinerU declares VLM, pipeline, and Gradio extras | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | lines 74-111 | `vlm`; `pipeline`; `gradio` | pyproject optional dependencies | VALUE_SET | ACCEPT |
| MinerU declares CLI/API/router/model-download/server entry points | `.private_reference/source_mirrors/opendatalab__MinerU/pyproject.toml` | lines 129-136 | `mineru`; `mineru-api`; `mineru-router`; `mineru-models-download` | pyproject scripts | VALUE_SET | ACCEPT |
| MinerU README describes document conversion into Markdown and JSON | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | lines 49-51; lines 164-181 | `Markdown`; `JSON` | upstream README | VALUE_SET | ACCEPT |
| MinerU README describes MCP, RAG framework, CLI, REST API, Docker, and Gradio surfaces | `.private_reference/source_mirrors/opendatalab__MinerU/README.md` | lines 65-68; lines 316-339 | `MCP Server`; `CLI`; `REST API`; `Docker`; `Gradio`; `mineru-router` | upstream README | VALUE_SET | ACCEPT |
| MSEA-T0 closed bounded and forbade runtime, checker, package, provider, public, model download, API/router, VLM/OCR, RAG, and production claims | `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | Status; Non-Goals; Current Runtime Freshness Verification | `CLOSED_PASS_BOUNDED` | MSEA-T0 roadmap | VALUE_SET | ACCEPT |
| MSEA-T2 is the current document-extraction claim-boundary and RAG handoff advisory | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | Status; External Knowledge Intake Routing | `ACTIVE_REFERENCE` | MSEA-T2 advisory | VALUE_SET | ACCEPT |
| MSEA-T3 closed the prior static-checker lane without building a checker | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | Status; Claim Boundary; Machine Closure Package | `CLOSED_PASS_BOUNDED` | MSEA-T3 closeout | VALUE_SET | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`docs/baselines;docs/work_orders`, riskCeiling=`HIGH`, maxResults=`20`

Returned defects: NONE_RETURNED

Disclosure note: dispatcher invoked `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch`; the resolver returned `totalCandidates=0`.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_source_mirror_migration.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `External knowledge intake routing: REQUIRED`; `External absorption core: REQUIRED`; `## Source Verification Block`; `## External Knowledge Intake Routing`; `## External Absorption Core`; `## Corpus Completeness And Report Integrity`; `## External Absorption Value Conversion Matrix`; `## Overlap And Novelty Classification`; `## Source Mirror Migration Control`; `## Scaffold Provenance Block`; `## ADIF Defect Registry Disclosure`; `DEFERRED_PRIVATE_ONLY`; `WORKER_MUST_NOT_COMMIT` |
| gateRunPurpose | confirmation/evidence run for MSEA-R4 baseline and work-order dispatch after checker read-ahead, not first discovery |
| claimBoundary | checker read-ahead proves authoring diligence only; it does not prove worker completion, runtime/provider behavior, public-sync, package activation, checker implementation, model-router behavior, or production readiness |

## Negative Search And Collision Discipline

| Check | Command | Result | Disposition |
|---|---|---|---|
| Baseline path did not exist before authoring | `Test-Path docs\baselines\CVF_GC018_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md` | `False` | ACCEPT |
| Work order path did not exist before authoring | `Test-Path docs\work_orders\CVF_AGENT_WORK_ORDER_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md` | `False` | ACCEPT |
| Planned worker-return path did not exist before authoring | `Test-Path docs\reviews\CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md` | `False` | ACCEPT |
| Planned owner-surface delta path did not exist before authoring | `Test-Path docs\reference\CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` | `False` | ACCEPT |
| Batch token collision search | `rg -n "MSEA-R4|MSEA_R4|MinerU Upstream Source Mirror Absorption|MINERU_UPSTREAM" docs CVF_SESSION AGENT_HANDOFF_V31_2026-07-02.md` | no matches before authoring | ACCEPT |

## Current Runtime Freshness Verification

| Claim checked | Verification command | Observed result | Disposition |
|---|---|---|---|
| Fresh upstream source mirror exists | `Test-Path '.private_reference/source_mirrors/opendatalab__MinerU/.git'` | `True` | ACCEPT |
| Source mirror remote points to upstream MinerU | `git -C .private_reference/source_mirrors/opendatalab__MinerU remote get-url origin` | `https://github.com/opendatalab/MinerU.git` | ACCEPT |
| Source mirror HEAD is pinned for dispatch | `git -C .private_reference/source_mirrors/opendatalab__MinerU rev-parse HEAD` | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` | ACCEPT |
| CVF did not install or execute MinerU for this dispatch | dispatch command log | only read/enumeration/scaffold/checker commands used | ACCEPT |
| Prior MSEA runtime/checker lanes remain bounded/closed | prior MSEA-T0/T2/T3 artifacts | documentation/reference only; no runtime or checker authorization | ACCEPT |

Freshness boundary: these checks support only source-mirror and negative
runtime claim boundaries for MSEA-R4 dispatch. They do not authorize execution
or prove parsing quality, OCR correctness, document truth, RAG suitability, or
production readiness.

## Evidence / Verification

Dispatch verification is bounded to source mirror existence, source mirror index
evidence, source verification, negative path search, checker read-ahead,
external absorption blocks, and pre-dispatch governance gates. Absorption
completion evidence is assigned to the worker return and must not be claimed by
this dispatch baseline.

## External Absorption Core

| Field | Value |
|---|---|
| Standard | docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md |
| Input root or repository | `https://github.com/opendatalab/MinerU.git` at `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491`; local mirror `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Enumeration command | `Get-ChildItem -LiteralPath ".private_reference/source_mirrors/opendatalab__MinerU" -Recurse -File -Force` excluding `.git` |
| Manifest artifact or inline manifest | inline `## Dispatch Source Mirror Manifest` table in this file; worker must create full manifest in planned worker return |
| Processing ledger artifact or inline ledger | planned worker return under `docs/reviews/CVF_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_WORKER_RETURN_2026-07-02.md` |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | planned `docs/reference/CVF_MSEA_R4_MINERU_UPSTREAM_OWNER_SURFACE_DELTA_2026-07-02.md` |
| Unresolved items | 425 unresolved at dispatch; worker must reduce to 0 or return `COMPLETE_WITH_LIMITATIONS_PENDING_REVIEW` or `BLOCKED_WITH_REASON` |
| Completion claim boundary | dispatch and source-mirror intake only; no runtime, provider/live, public, production, OCR/VLM/hybrid execution, model download, API/router/Gradio, Docker, RAG write, checker, package activation, model-router, or action-authority claim |

## Corpus Completeness And Report Integrity

- Corpus task class: upstream external repository absorption dispatch.
- Corpus root: `.private_reference/source_mirrors/opendatalab__MinerU/`.
- Snapshot time: 2026-07-02 local session.
- Enumeration command: `Get-ChildItem -LiteralPath ".private_reference/source_mirrors/opendatalab__MinerU" -Recurse -File -Force` excluding `.git`.
- Manifest artifact or inline manifest: dispatch preflight count and hash recorded here; full manifest required in worker return.
- Manifest hash: `sha256:3a0ad960e1d8fc663c5f099c27f8416a0b2d8147718e9788ee298dd653da6a81`.
- Processing ledger artifact or inline ledger: planned worker return.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=425; ledger_terminal=0 at dispatch; exclusions=0; unresolved=425.
- Unresolved files: 425 at dispatch.
- Declared exclusions: none at dispatch.
- Unreadable or unsupported files: none known at dispatch.
- Aggregation check: dispatch proves source mirror availability, not absorption completion.
- Drift check: worker must recompute count, commit, and manifest hash before processing.
- Output traceability: worker maps accepted value to CVF owner surfaces or returns blocked source gaps.
- Adversarial verification: prior MSEA-T0/T1/T2/T3 conclusions must be challenged against the current 425-file upstream mirror.
- Corpus verdict: PARTIAL

## Dispatch Source Mirror Manifest

| Manifest item | Evidence |
|---|---|
| Upstream repository | `https://github.com/opendatalab/MinerU.git` |
| Pinned commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Local mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Tracked file count | 425 |
| Manifest hash | `sha256:3a0ad960e1d8fc663c5f099c27f8416a0b2d8147718e9788ee298dd653da6a81` |
| Full file-level manifest | REQUIRED in planned worker return |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | external repo or copied folder -> pinned source mirror -> external absorption core -> full manifest and processing ledger -> value conversion matrix -> CVF owner-surface delta -> future package/runtime/checker work order only if separately authorized |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_source_mirror_migration.py` |
| Owner surface | `docs/baselines/CVF_GC018_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md` |
| Disposition | DISPATCH upstream source-mirror absorption review |
| Claim boundary | dispatch only; no runtime, package activation, checker wiring, provider/live proof, public-sync, MCP server, API/router/Gradio, Docker, model download, OCR/VLM/hybrid execution, RAG write, benchmark, or production-readiness claim |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| Upstream source mirror control plane | Current MinerU source authority is pinned for future absorption. | DOCTRINE_ADAPTED | `.private_reference/source_mirrors/INDEX.md` | Use upstream mirror as source authority for MSEA-R4 facts. | No runtime or package behavior |
| README and pyproject document-conversion claims | MinerU describes multi-format document parsing into Markdown/JSON for downstream retrieval and extraction. | DOCTRINE_ADAPTED | planned MSEA-R4 owner-surface delta and existing MSEA-T2 advisory | Worker maps deltas to CVF extraction-foundation language. | Documentation/reference only |
| CLI/API/router/Gradio/Docker/server/model-download/VLM/OCR/hybrid surfaces | Upstream exposes executable surfaces, but CVF has not authorized execution. | RUNTIME_CANDIDATE | planned worker return and MSEA conditional reopen notes | Worker may classify value and reopen conditions only. | No install, execution, model download, API/router/Gradio, Docker, VLM/OCR/hybrid, or provider/live proof |
| MCP, RAG framework, SDK, and no-code integration claims | Upstream integration surfaces may become package or adapter candidates after separate authorization. | PACKAGE_CANDIDATE | planned worker return | Worker records candidate evidence only. | No package root, registry mutation, adapter, MCP/CLI integration, or activation |
| Claimed quality, OCR, parsing, table/formula, long-document, and concurrency behavior | Future guards may be valuable only if CVF identifies repeated real misses or authorized receipt gaps. | CHECKER_CANDIDATE | planned worker return and future reopen conditions | Worker may record candidate guard ideas with concrete triggers. | No checker implementation or hook wiring |
| Upstream source files, tests, workflows, and deployment recipes | Direct import remains unsafe and non-authoritative. | REJECT_DIRECT_IMPORT | CVF-native rewrite lanes only | Worker rejects direct copy/wiring and records reasons. | No direct source import |
| Duplicate, asset-only, marketing-only, or non-CVF-value files after full read | Some files may add no CVF-native doctrine/package/runtime/checker delta. | NO_PACKAGE_OR_RUNTIME_VALUE | worker ledger | Worker records explicit no-new-value reason. | No runtime or package behavior |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Multi-format document extraction into Markdown/JSON | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ENRICH_EXISTING | upstream mirror may refine receipt, output, and handoff language | worker enriches owner delta only |
| Runtime parser, OCR, VLM, hybrid, API, router, Docker, Gradio, model-download, remote-server surfaces | `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md`; `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | ENRICH_EXISTING | current upstream has more concrete runtime-candidate evidence than prior bounded closeout | worker parks with concrete reopen conditions |
| MCP/RAG/framework integration claims | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | ENRICH_EXISTING | integration claims may sharpen package/adapter candidate taxonomy | worker records candidate-only evidence |
| Direct upstream implementation source | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | REJECT_DIRECT_IMPORT | external source is not CVF authority or implementation | worker rejects direct import |
| Files that only restate already-owned MSEA doctrine | `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md`; `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`; `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | NO_NEW_VALUE | no meaningful delta after worker comparison | worker closes row with reason |
| Any high-value source item without an existing CVF owner | OWNER_SURFACE_NOT_FOUND | OWNER_SURFACE_NOT_FOUND | worker must name source-backed gap rather than silently dropping value | worker records blocker or proposed future owner route |

## Source Mirror Migration Control

| Field | Disposition |
|---|---|
| Legacy source path | Legacy external repo clone and legacy adapter folder are not source authority for MSEA-R4; this dispatch uses the fresh source mirror instead. |
| Source mirror path | `.private_reference/source_mirrors/opendatalab__MinerU/` |
| Mirror index row | `.private_reference/source_mirrors/INDEX.md` row `opendatalab__MinerU` |
| Pinned upstream commit | `3e60291846cb7c3bf8fe7f4f16238f4fc6cce491` |
| Migration disposition | MIGRATED_TO_SOURCE_MIRROR_AUTHORITY_FOR_THIS_TRANCHE |
| Legacy cleanup disposition | LEGACY_REFERENCE_ONLY_WITH_REASON: older local copies may be read only if needed for historical comparison and must not override current upstream facts |
| Claim boundary | source-mirror authority control only; no source import, package install, runtime execution, provider/live proof, public-sync, checker implementation, or production-readiness claim |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | planned MSEA-R4 worker return and owner-surface delta | internal CVF agents may read documentation/reference output only; no action authority | this baseline and work order | N/A with reason: no internal runtime adapter is implemented | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | future CLI/MCP adapter owner, not this dispatch | external agent use requires separate source-verified adapter/runtime authorization | upstream MinerU advertises MCP and CLI/API surfaces, but CVF has not implemented them | deferred adapter owner; no ingress, auth, mutation, raw-data, receipt, or public boundary is implemented here | DEFERRED_WITH_REASON |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION --title "MSEA-R4 MinerU Upstream Source Mirror Absorption" --date 2026-07-02 --base 4d6cd237 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | packet-kind=source-intake; commit-mode=WORKER_MUST_NOT_COMMIT; worker-return skeleton requested |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced scaffold placeholders with MinerU source-mirror facts, MSEA predecessor surfaces, source verification, external absorption blocks, migration control, and worker boundary text |
| checkerReadAheadConfirmation | read guard orientation, literal-format gotchas, work-order template, external absorption standards, scaffold provenance standard, and applicable checker source paths before writing |
| docOnlyNewFields | planned worker return path; planned owner-surface delta path; MSEA-R4 manifest hash; source-mirror migration disposition |
| claimBoundary | scaffold provenance supports dispatch authoring only; no worker completion, runtime/provider/live/public/package/Web/MCP/model-router/action-authority, checker, or production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MSEA-R4 dispatch is private provenance source-mirror absorption work.
No public-sync artifact is created or authorized by this baseline.

## Claim Boundary

This GC-018 baseline authorizes MSEA-R4 dispatch only. It does not authorize or
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
| claimScope | MSEA-R4 dispatch baseline and work-order authorization |
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
| Session or invocation | MSEA-R4 dispatch authoring, 2026-07-02 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, git, apply_patch, governance checkers |
| Target paths | `docs/baselines/CVF_GC018_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R4_MINERU_UPSTREAM_SOURCE_MIRROR_ABSORPTION_2026-07-02.md` |
| Allowed scope source | operator request to create the MinerU work order after fresh source mirror clone |
| Before status evidence | planned MSEA-R4 paths returned `False` in negative search |
| After status evidence | dispatch baseline and work order created with source verification and pre-dispatch gates |
| Diff evidence | `git diff --name-status` before material commit |
| Approval boundary | dispatcher authoring only; worker execution remains no-commit |
| Claim boundary | no runtime/provider/public/source-import/Web/MCP/model-router/checker/package/action-authority claim |
| Agent type | dispatcher |
| Invocation ID | `msea-r4-mineru-upstream-source-mirror-dispatch-2026-07-02` |
| Expected manifest | baseline and work order paths named above |
| Actual changed set | baseline and work order paths named above |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch artifact creation |
