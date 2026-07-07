# CVF MSEA-T0 MinerU Structured Extraction External Absorption Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-28

Batch ID: MSEA-T0

External knowledge intake routing: REQUIRED

## Purpose

Audit the current upstream `opendatalab/MinerU` repository and the
operator-provided `CVF MinerU Structured Extraction Adapter/` folder, move the
folder out of the repository root into legacy reference storage, and select the
next governed CVF tranche.

Decision:
`CLOSE_MSEA_ABSORPTION_LANE_NO_CHECKER_NOW`

Recommended next:
`SELECT_NEXT_EXTERNAL_ABSORPTION_LANE_OR_OPEN_FRESH_MSEA_RUNTIME_GC018_IF_REOPEN_CONDITIONS_ARE_MET`

## Target / Source

Reviewed sources:

- upstream repository clone:
  `opendatalab/MinerU` at commit `3e60291`
- operator-provided external folder retained after audit under:
  `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/`
- current CVF Extraction Foundation owner surfaces under:
  `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/`
- current external-intake chain map:
  `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`

Roadmap base head: `47c1720c`.

## Scope / Methodology

1. Read CVF startup, active state, active handoff, guard orientation, literal
   format guidance, and the external knowledge intake chain map.
2. Clone the current upstream MinerU repository and inspect README, output-file
   documentation, backend option source, API request source, and package
   metadata.
3. Read the operator-provided MinerU adapter folder beyond filenames, including
   scope/claim boundary, baseline audit, capability audit, absorption map,
   gateway spec, smart router policy, adapter contract, extraction receipt,
   quality gate, RAG handoff, privacy/local-first policy, reference drafts, and
   checker prototype.
4. Compare MinerU and the external adapter package against current CVF
   Extraction Foundation route, envelope, OCR-adapter, quality, chunking, and
   storage-boundary surfaces.
5. Select a documentation and reconciliation-only next tranche that maps the
   high-value subset into CVF-owned owner surfaces before any implementation,
   checker, or runtime adapter work.

No runtime source, generated aggregate, checker, provider call, public-sync,
adapter implementation, package activation, certification, MinerU install,
model download, API server, router, VLM backend, remote backend, OCR service,
RAG index write, extraction run, benchmark, document-truth claim, parsing
accuracy claim, or production-readiness claim is authorized by MSEA-T0.

## Authorization / Decision

Operator authorization: continue the existing external-absorption rule for
`opendatalab/MinerU` and the operator-provided
`CVF MinerU Structured Extraction Adapter/` folder.

Roadmap decision:
`CLOSE_MSEA_ABSORPTION_LANE_NO_CHECKER_NOW`

This closes the bounded MSEA documentation/reference absorption lane after
MSEA-T1/T2/T3. It does not authorize implementation.

## Non-Goals

- No direct import of MinerU runtime, CLI, FastAPI app, router, Gradio app,
  SDK, Docker stack, model downloader, VLM backend, hybrid backend, or
  http-client backend.
- No direct import of the external adapter package into
  `EXTENSIONS/CVF_MODEL_GATEWAY` or `EXTENSIONS/CVF_EXTRACTION_FOUNDATION`.
- No direct promotion of copied reference drafts as canonical CVF standards.
- No direct promotion of the copied checker prototype.
- No model download, model lifecycle decision, GPU routing, remote provider
  processing, or OpenAI-compatible server routing.
- No RAG index mutation, corpus registry mutation, memory write, public-sync,
  hosted-readiness, production-readiness, parsing accuracy, OCR correctness,
  table/formula correctness, or document-truth claim.

## Design Control Gate

| Control | Required disposition |
|---|---|
| Existing CVF owner surface | MSEA-T1 must map all accepted concepts to `CVF_EXTRACTION_FOUNDATION` before promotion |
| External-source handling | MinerU upstream and the copied adapter folder stay source inputs only |
| Runtime boundary | MinerU install, API, router, model download, VLM/hybrid, OCR execution, and remote backend routes remain parked |
| Claim boundary | parsed text is artifact evidence, not truth; quality gate can approve use, not certify domain correctness |
| RAG boundary | extraction output cannot enter RAG/context/memory without a receipt and quality disposition |
| Checker boundary | copied checker is a candidate only after CVF-owned vocabulary and owner surfaces exist |

## Work Plan

| Step | Output | Status |
|---|---|---|
| MSEA-T0.1 | inspect upstream MinerU repository at fixed commit | COMPLETE |
| MSEA-T0.2 | inspect local external adapter folder beyond filenames | COMPLETE |
| MSEA-T0.3 | compare against current CVF Extraction Foundation owner surfaces | COMPLETE |
| MSEA-T0.4 | reject direct runtime/package/checker import for this tranche | COMPLETE |
| MSEA-T0.5 | select MSEA-T1 source-verified reconciliation as next move | COMPLETE |
| MSEA-T0.6 | move external folder from root to legacy reference storage | COMPLETE |

## Acceptance Criteria

| Criterion | Evidence | Status |
|---|---|---|
| Upstream MinerU reviewed at fixed commit | External Artifact Hash Manifest | PASS |
| Local folder reviewed beyond filenames | External Artifact Hash Manifest and Absorption Classification | PASS |
| Existing CVF extraction owner surfaces considered | Source Verification Block | PASS |
| Direct runtime/package/checker import rejected | Non-Goals and Claim Boundary | PASS |
| Runtime/provider/RAG/document-truth work not authorized | Non-Goals and Current Runtime Freshness Verification | PASS |
| Next tranche selected | Proposed Roadmap | PASS |
| Root folder hygiene restored | retained external source path under `.private_reference/legacy/` | PASS |

## Verification / Evidence

| Evidence item | Result |
|---|---|
| `git rev-parse --short HEAD` before material edit | `47c1720c` |
| upstream MinerU clone commit | `3e60291` |
| local external folder status before move | untracked root external source folder |
| retained external source path | `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/` |
| external hash capture | recorded in External Artifact Hash Manifest |
| expected changed set | this roadmap only |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | `CVF_EXTRACTION_FOUNDATION` route, envelope, OCR adapter boundary, quality report, chunking, storage boundary, plus MinerU backend/API/output docs |
| Runtime behavior claimed | N/A_WITH_REASON: this roadmap performs documentation and intake routing only |
| Live/provider proof claimed | N/A_WITH_REASON: no live governance behavior is claimed |
| Extraction run claimed | N/A_WITH_REASON: no MinerU or OCR parser execution is performed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized or performed |
| Freshness disposition | PASS - current source evidence supports bounded documentation/intake routing only |

## External Artifact Hash Manifest

| Artifact | Source class | Commit or local source | SHA256 |
|---|---|---|---|
| `.private_reference/external_repos/MinerU/README.md` | upstream MinerU | `opendatalab/MinerU@3e60291` | `C11F9029605C9FD5D9866B5BDB933E102C8CF7FC7016D06351D877AAE066CB52` |
| `.private_reference/external_repos/MinerU/docs/en/reference/output_files.md` | upstream MinerU | `opendatalab/MinerU@3e60291` | `0D3BF05492967E100415DB12BD73FF82F70F9C7B4829BC99AD6EB8C1A0433A6C` |
| `.private_reference/external_repos/MinerU/mineru/cli/backend_options.py` | upstream MinerU | `opendatalab/MinerU@3e60291` | `1FEBAA707E07DD4EA2910C4FC1EA9840D59DB38B813D10785E83D5B88E3EA917` |
| `.private_reference/external_repos/MinerU/mineru/cli/api_request.py` | upstream MinerU | `opendatalab/MinerU@3e60291` | `AE58960FE0D938F1F206242FD4825F1702420BB1EA3176A39FEB357839E0841B` |
| `.private_reference/external_repos/MinerU/pyproject.toml` | upstream MinerU | `opendatalab/MinerU@3e60291` | `0C436A658E27275B3D11CF1BE17D8943BA796CBD8959621BAEA2A33A53B763DA` |
| `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/docs/absorptions/mineru-governed-document-ingestion/00_SCOPE_AND_CLAIM_BOUNDARY.md` | operator-provided folder | local external folder | `788ABF1851F512EADC16ED5FE5A821CB403A1A8011F3C9D5B0F1A3ADDA79A2AB` |
| `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/docs/absorptions/mineru-governed-document-ingestion/04_GOVERNED_DOCUMENT_INGESTION_GATEWAY_SPEC.md` | operator-provided folder | local external folder | `423A502EE5FE26D7D7CCC8DDAB4427C2858C36E8721D5CFA8108000FFD235365` |
| `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/docs/absorptions/mineru-governed-document-ingestion/07_DOCUMENT_EXTRACTION_RECEIPT_CONTRACT.md` | operator-provided folder | local external folder | `3BF81FD51368F5264BB06A94825AF2706E132A3F770BA78BE87E7ABA161B161E` |
| `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/docs/absorptions/mineru-governed-document-ingestion/08_EXTRACTION_QUALITY_GATE.md` | operator-provided folder | local external folder | `F5AC51BE5E4B4AB055E03D86AF0622499A9924A39605BA12CCB9C9D237B8580F` |
| `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/docs/absorptions/mineru-governed-document-ingestion/09_RAG_INDEXING_HANDOFF_CONTRACT.md` | operator-provided folder | local external folder | `E9AB259ADFDD25DD98EE3D8FA5FC52F600FAC5AE3F229FEFABB4993906352343` |
| `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/governance/compat/check_document_extraction_claim_boundary.py` | operator-provided folder | local external folder | `277D5330125FA3CF43B7945A0E98AAE952E5761F2FB801299F126D3501CE6341` |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| MinerU presents itself as a parser for PDF, image, DOCX, PPTX, and XLSX into Markdown/JSON | `.private_reference/external_repos/MinerU/README.md` | line 164 | Project Introduction | MinerU README | EXISTS | ACCEPT |
| MinerU documents human-readable order, layout/span visualization, and local orchestration surfaces | `.private_reference/external_repos/MinerU/README.md` | lines 174, 182, 183 | Key Features | MinerU README | EXISTS | ACCEPT |
| MinerU exposes pipeline, VLM, hybrid, and http-client backend labels | `.private_reference/external_repos/MinerU/mineru/cli/backend_options.py` | lines 3-22 | PUBLIC_BACKEND_CHOICES | MinerU backend options | EXISTS | ACCEPT |
| MinerU API request form can request Markdown, middle JSON, model output, content list, images, and client-side output generation | `.private_reference/external_repos/MinerU/mineru/cli/api_request.py` | lines 31-50, 162-251 | ParseRequestOptions | MinerU API request options | EXISTS | ACCEPT |
| MinerU output docs define layout and span files plus model, middle, and content-list JSON artifacts | `.private_reference/external_repos/MinerU/docs/en/reference/output_files.md` | lines 15-119, 292-402 | output files documentation | MinerU output artifact docs | EXISTS | ACCEPT |
| MinerU package metadata declares custom license reference and console/API/router scripts | `.private_reference/external_repos/MinerU/pyproject.toml` | lines 8-12, 129-136 | project metadata and scripts | MinerU package metadata | EXISTS | ACCEPT |
| Current CVF already has deterministic document-intelligence route decisions and authorization gates | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | lines 25, 35, 51, 139 | decide_document_intelligence_route | CVF Extraction Foundation DIR | EXISTS | ACCEPT |
| Current CVF already has a document-intelligence control envelope and handoff gate | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py` | lines 33, 44, 69, 124 | build_document_intelligence_control_envelope | CVF Extraction Foundation DICE | EXISTS | ACCEPT |
| Current CVF already has OCR adapter boundary, extraction quality report, chunking, and storage boundary surfaces | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | lines 43, 101, 117, 152, 187, 235, 370, 424 | ExtractionQualityReport; ExtractionStorageBoundary | CVF Extraction Foundation pipeline | EXISTS | ACCEPT |
| Current CVF Tier 1 extractor supports `.docx` and `.pdf` only and blocks other formats | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1_extractor.py` | lines 137, 147, 149, 152 | extract_tier1 | CVF Tier 1 extractor | EXISTS | ACCEPT |
| External adapter folder states parser output is not truth and requires CVF gates before downstream use | `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/docs/absorptions/mineru-governed-document-ingestion/00_SCOPE_AND_CLAIM_BOUNDARY.md` | Trust Rule; Required CVF Gates | parsed text is not truth | external adapter claim boundary | LITERAL_INVARIANT | ACCEPT |
| External adapter folder defines extraction receipt and quality-disposition rule before trusted context use | `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/docs/absorptions/mineru-governed-document-ingestion/01_CVF_DOCUMENT_INGESTION_BASELINE_AUDIT.md` | line 113 | Baseline Enforcement Rule | external adapter baseline audit | LITERAL_INVARIANT | ACCEPT |
| External adapter folder defines route, artifact, quality, downstream, and forbidden gateway behaviors | `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/docs/absorptions/mineru-governed-document-ingestion/04_GOVERNED_DOCUMENT_INGESTION_GATEWAY_SPEC.md` | Route Requirements; Artifact Requirements; Quality Dispositions; Downstream Decisions; Forbidden Behavior | Governed Document Ingestion Gateway | external adapter gateway spec | EXISTS | ACCEPT |
| External adapter folder defines extraction receipt fields and default forbidden downstream uses | `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/docs/absorptions/mineru-governed-document-ingestion/07_DOCUMENT_EXTRACTION_RECEIPT_CONTRACT.md` | Required Receipt Fields; Downstream Use Rules; Review Promotion | cvf.document_extraction_receipt | external adapter receipt contract | EXISTS | ACCEPT |
| External adapter folder defines quality dimensions and mandatory human-review cases | `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/docs/absorptions/mineru-governed-document-ingestion/08_EXTRACTION_QUALITY_GATE.md` | Quality Dimensions; Mandatory Human Review | Extraction Quality Gate | external adapter quality gate | EXISTS | ACCEPT |
| External adapter folder defines RAG handoff, chunking, citation, stale-index, and forbidden-handoff controls | `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/docs/absorptions/mineru-governed-document-ingestion/09_RAG_INDEXING_HANDOFF_CONTRACT.md` | Handoff Rule; Chunking Rules; Citation Rules; Reindexing Rule; Forbidden Handoff | cvf.rag_indexing_handoff | external adapter RAG handoff | EXISTS | ACCEPT |
| External-intake chain treats external repo or copied folder as advisory until promoted through CVF owner surfaces | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | Central Core; Input Type Router | External repo or copied folder | external knowledge chain map | LITERAL_INVARIANT | ACCEPT |

## Findings / Position

| Finding | Evidence | Disposition |
|---|---|---|
| MinerU is high-signal for CVF document extraction because it emits Markdown/JSON plus visual/debug artifacts | upstream README and output docs | ADAPT |
| The external adapter folder correctly frames the key trust rule: parsed text is artifact evidence, not truth | external scope/claim boundary and baseline audit | ABSORB_AS_MSEA_T1_SOURCE |
| Current CVF already owns a deterministic extraction route/envelope/quality/chunking foundation | `CVF_EXTRACTION_FOUNDATION` source | MAP_TO_EXISTING_OWNER_SURFACES |
| External gateway, receipt, quality, and RAG handoff contracts are useful but overlap current CVF extraction surfaces | external docs 04, 07, 08, 09 plus current extraction source | RECONCILE_BEFORE_PROMOTION |
| External adapter contract is mislocated under Model Gateway for current CVF ownership | copied `EXTENSIONS/CVF_MODEL_GATEWAY/adapters/mineru` plus current extraction foundation | ADAPT_TO_EXTRACTION_FOUNDATION_NOT_MODEL_GATEWAY |
| MinerU's remote/http-client and model-download paths create privacy, cost, and dependency risk | upstream backend/API/package metadata plus privacy policy draft | PARK_RUNTIME_AND_REMOTE_ROUTES |
| Prototype claim-boundary checker is useful but not ready for direct guard import | copied checker plus non-CVF-owned vocabulary | DEFER_WITH_REOPEN_CONDITION |
| Best next move is a source-verified reconciliation before any reference, checker, or adapter implementation | combined audit | MSEA_T1_READY |

Decision:
`CLOSE_MSEA_ABSORPTION_LANE_NO_CHECKER_NOW`

## Absorption Classification

| External item | Source | CVF disposition | Reason / next condition |
|---|---|---|---|
| MinerU multi-format parsing capability | upstream README and package metadata | ADAPT_AS_ENGINE_CAPABILITY_INPUT | Useful, but no direct dependency or parser execution authorized |
| Markdown, middle JSON, content-list JSON, model JSON, layout PDF, span PDF | upstream output docs | ADAPT_AS_ARTIFACT_MANIFEST_CANDIDATE | Strong fit for extraction receipt and quality report |
| Pipeline/VLM/hybrid/http-client backend taxonomy | upstream backend source and API request source | ADAPT_TO_CVF_ROUTE_POLICY | Must map to current DIR/DICE gates and privacy controls |
| Governed Document Ingestion Gateway concept | external docs 03 and 04 | ADAPT_TO_EXTRACTION_FOUNDATION_OWNER_SURFACE | Good product surface, but CVF source owner is Extraction Foundation |
| Extraction receipt contract | external doc 07 | ADAPT_AS_RECEIPT_CANDIDATE | Needs reconciliation with CVF receipt/gate naming and generated-state boundaries |
| Extraction quality gate | external doc 08 | ADAPT_TO_EXISTING_EXTRACTION_QUALITY_REPORT | Useful for reading order, table/formula, provenance, and human-review vocabulary |
| RAG handoff contract | external doc 09 | ADAPT_TO_CONTEXT_RAG_HANDOFF_BOUNDARY | Must not write directly to index or memory without separate authorization |
| Privacy/local-first policy | external doc 10 | ADAPT_TO_ROUTE_POLICY_AND_SECURITY_BOUNDARY | Strong fit for remote backend, sensitive docs, retention, and model-download controls |
| External reference drafts | copied docs/reference | REWRITE_AS_CVF_OWNED_REFERENCE_LATER | Useful only after source-verified reconciliation |
| Copied checker prototype | copied governance/compat checker | DEFER_WITH_REOPEN_CONDITION | Reopen only after MSEA-T1/T2 define CVF-owned unsafe vocabulary and owner surface |
| MinerU CLI/API/router/Gradio/Docker/model downloader | upstream repo | PARKED_RUNTIME | Requires fresh GC-018, dependency/license review, model lifecycle plan, sample corpus, and reproducible proof |
| Model Gateway adapter placement | copied adapter folder | REJECT_AS_OWNER_SURFACE | Current owner should be Extraction Foundation unless later source verification proves gateway ownership |
| Public/production/support claims | upstream badges, docs, release notes | BLOCK_UNTIL_CVF_PROOF | External claims are not CVF evidence |

## Proposed Roadmap

| Tranche | Status | Objective | Boundary |
|---|---|---|---|
| MSEA-T0 | CLOSED_PASS_BOUNDED | audit upstream MinerU and copied adapter folder, move folder to legacy storage, and select next move | documentation-only |
| MSEA-T1 | CLOSED_PASS_BOUNDED | author GC-018 and source-verified reconciliation matrix mapping MinerU/external-adapter concepts to CVF Extraction Foundation, corpus, RAG, and receipt owner surfaces | no runtime/checker/import |
| MSEA-T2 | CLOSED_PASS_BOUNDED | promote the highest-value subset into one CVF-owned document extraction claim-boundary, receipt, quality, and RAG-handoff advisory reference | reference only |
| MSEA-T3 | CLOSED_PASS_BOUNDED | decide whether one static checker candidate is worth implementing | no checker now; reopen only on concrete conditions |
| MSEA-RUNTIME | PARKED | MinerU install, model download, CLI/API/router invocation, sample corpus run, OCR/VLM/hybrid execution, receipt samples, quality reports, RAG handoff tests | fresh governed authorization, source verification, dependency/license review, security/privacy plan, sample corpus, and reproducible proof |

## Risk / Corrective Action

| Risk | Corrective action | Status |
|---|---|---|
| External parser becomes a CVF trust root | MSEA-T1 must map parser output to CVF receipt and quality owner surfaces first | PASS |
| Direct adapter import bypasses existing Extraction Foundation | Reject direct import and map to current route/envelope/quality source | PASS |
| Remote backend leaks sensitive documents | Keep remote/http-client routes parked behind privacy and route-policy approval | PASS |
| Model downloads happen silently | Keep model lifecycle as separate governed action | PASS |
| RAG consumes unreviewed extraction output | Carry receipt plus quality-disposition rule into MSEA-T1/T2 | PASS |
| Upstream benchmark or product claims become CVF claims | Treat upstream claims as advisory only until CVF sample-corpus proof exists | PASS |
| Checker import happens before vocabulary is CVF-owned | Defer checker behind MSEA-T1/T2 and reopen condition | PASS |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | External repo or copied folder -> Root/folder lifecycle classification plus absorption map when retained -> CVF-owned reconciliation roadmap -> fresh GC-018/work order only if implementation is separately authorized |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` |
| Disposition | CLOSED selected MinerU and external-adapter concepts through MSEA-T1 reconciliation, MSEA-T2 reference, and MSEA-T3 no-checker-now closeout |
| Claim boundary | external repo and copied folder are source input only; MSEA creates no runtime, package, public, provider, OCR, adapter, RAG index, document-truth, production, or checker support |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-T0 external absorption roadmap only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no Delta receipt evidence is created or consumed |
| actionEvidence | N/A with reason: no runtime action is executed or observed |
| invocationBoundary | no wrapper, proxy, mandatory invocation, direct IDE/shell/git/filesystem interception, arbitrary command execution, or EDIT/COMMIT execution |
| interceptionBoundary | no direct interception claim |
| claimLanguage | roadmap and external-intake selection only |
| forbiddenExpansion | no runtime, OCR/provider/live, MinerU install, model download, VLM/hybrid route, remote backend, API/router/Gradio service, RAG index write, public-sync, package activation, certification, checker implementation, generated aggregate, extraction accuracy, document-truth, or production-readiness claim |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | this roadmap | may use as next-lane selection and source-boundary record | Source Verification Block and Absorption Classification | N/A with reason: documentation-only roadmap | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future adapter, CLI, MCP, or public-safe readout | no external CLI, MCP, plugin, public API, parser adapter, or RAG behavior is created | Claim Boundary | separate GC-018/source-verified work order required | `DEFERRED_WITH_REASON` |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Escalation state | Next control action |
|---|---|---|---|---|
| Document parsing output can be mistaken for source truth | CLAIM_BOUNDARY_RISK | EXTRACTION_FOUNDATION | ROADMAP_READY | MSEA-T1 reconciliation before promotion |
| RAG handoff can bypass extraction receipt and quality disposition | GOVERNANCE_CONTROL_GAP | CONTEXT_RAG_HANDOFF | ROADMAP_READY | map receipt/quality handoff to CVF owner surfaces |
| Remote VLM/hybrid routes can bypass local-first privacy controls | SCOPE_EXPANSION_RISK | EXTRACTION_ROUTE_POLICY | CLOSED_WITH_BOUNDARY | keep remote routes parked until separately authorized |
| Prototype checker exists but vocabulary is not CVF-owned yet | SOURCE_BEHAVIOR_MISMATCH | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | define owner vocabulary before checker import |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance external absorption roadmap. Public-safe export or
public MinerU/document-extraction claims require a separate public-sync
decision and claim-boundary review.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | local workspace |
| Session or invocation | `msea-t0-mineru-structured-extraction-external-absorption-2026-06-28` |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, git clone, rg, Get-Content, Get-FileHash, Move-Item, apply_patch, governance gates |
| Target paths | MSEA-T1 baseline, MSEA-T2 reference, MSEA-T3 closeout, MSEA-T0 roadmap update |
| Allowed scope source | operator instruction to finish the roadmap |
| Before status evidence | baseHead `8790a502`; worktree clean before material patch |
| After status evidence | MSEA-T1/T2/T3 artifacts authored and MSEA-T0 closure updated |
| Diff evidence | `git diff --name-status 8790a502 --` |
| Approval boundary | external absorption documentation/reference/closeout only |
| Claim boundary | no runtime, OCR/provider/live, MinerU install, model download, VLM/hybrid route, remote backend, API/router/Gradio service, RAG index write, public-sync, checker, generated aggregate, adapter implementation, package activation, certification, extraction accuracy, document-truth, or production/hosted readiness |
| Agent type | single-agent reviewer/closer |
| Invocation ID | `msea-t0-mineru-structured-extraction-absorption-2026-06-28` |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_T1_SOURCE_VERIFIED_DOCUMENT_EXTRACTION_RECONCILIATION_2026-06-28.md`; `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`; `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md`; `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_T1_SOURCE_VERIFIED_DOCUMENT_EXTRACTION_RECONCILIATION_2026-06-28.md`; `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`; `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md`; `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | operator-provided external folder moved from root to `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/` |

## Claim Boundary

MSEA-T0 is an external-knowledge absorption roadmap only. It does not claim CVF
has implemented MinerU runtime integration, OCR execution, VLM/hybrid backend
routing, remote parser processing, model download, API/router/Gradio service,
RAG indexing, document QA, document truth verification, parser accuracy,
table/formula correctness, public-sync export, checker enforcement, package
activation, certification, generated aggregate mutation, or production/hosted
readiness.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason: direct single-agent roadmap/reference/closeout tranche | N/A with reason | N/A with reason |
| Roadmap state | this roadmap | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_MSEA_T1_SOURCE_VERIFIED_DOCUMENT_EXTRACTION_RECONCILIATION_2026-06-28.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Reference artifact | `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md` | `Status: ACTIVE_REFERENCE` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Checker implementation | N/A with reason: MSEA-T3 decides no checker now | no checker path changed | N/A with reason |
| Checker tests | N/A with reason: no checker implementation | no test path changed | N/A with reason |
| Registry JSON | BLOCKED with reason: no registry JSON mutation is authorized | no registry path changed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown mutation is authorized | no registry path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: MSEA-T0 hash manifest and MSEA-T1 source verification record external source evidence | MSEA-T0 and MSEA-T1 | N/A with reason |
| System loop interlock | N/A with reason: local documentation closeout only | Claim Boundary | N/A with reason |
| Public sync | N/A with reason: no public-sync is authorized | no public paths changed | N/A with reason |
| Runtime/live proof | N/A with reason: no runtime/parser/provider governance behavior is claimed | no live run required | N/A with reason |
| Session continuity | active session/front-door sync planned after material commit | separate session-sync commit required | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| lane decision | `CLOSE_MSEA_ABSORPTION_LANE_NO_CHECKER_NOW` | PASS |
| absorbed surfaces | MSEA-T1 and MSEA-T2 present | PASS |
| remaining candidates | concrete reopen conditions recorded in MSEA-T3 | PASS |
| public export | `DEFERRED_PRIVATE_ONLY` | PASS |
| runtime/live proof | N/A with reason: no runtime/parser/provider governance behavior is asserted | N/A with reason |
