# CVF MSEA-T2 Document Extraction Claim Boundary Receipt Quality And RAG Handoff Advisory

Memory class: FULL_RECORD

Status: ACTIVE_REFERENCE

docType: reference

Date: 2026-06-28

Owner: Codex

rawMemoryReleased: false

## Purpose

Promote the useful subset of upstream MinerU and the retained MinerU
structured-extraction adapter folder into a CVF-owned reference for document
extraction claim boundaries, receipt vocabulary, quality disposition, and RAG
handoff limitations.

This reference absorbs the source material as governance doctrine. It does not
import MinerU runtime, the copied adapter package, copied reference drafts,
prototype checker, model downloader, CLI/API/router service, OCR/VLM/hybrid
backend, remote backend route, RAG index writer, parser execution, or runtime
behavior.

## Scope / Applies To

Applies to future CVF roadmaps, GC-018 baselines, work orders, completion
reviews, Extraction Foundation design packets, corpus-ingestion packets, and
RAG/context packets that discuss document parsing, extraction artifacts,
extraction receipts, quality gates, storage boundaries, or downstream context
use of extracted text.

Does not apply to runtime source implementation, live/provider proof, public
sync, parser certification, generated aggregate mutation, model download,
remote backend routing, VLM/hybrid execution, OCR execution, benchmark
execution, RAG index mutation, or document truth verification.

## Source Authority

CVF authority comes from governed owner surfaces. Upstream MinerU and the
retained adapter folder are external advisory input only.

| Authority class | Source | Disposition |
|---|---|---|
| CVF roadmap authority | `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` | ACCEPT |
| CVF reconciliation authority | `docs/baselines/CVF_GC018_MSEA_T1_SOURCE_VERIFIED_DOCUMENT_EXTRACTION_RECONCILIATION_2026-06-28.md` | ACCEPT |
| Existing CVF route owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_router.py` | ACCEPT |
| Existing CVF handoff owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/document_intelligence_control_envelope.py` | ACCEPT |
| Existing CVF quality/storage owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/extraction_pipeline.py` | ACCEPT |
| Existing CVF Tier 1 owner | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/tier1_extractor.py` | ACCEPT |
| External source input | `.private_reference/external_repos/MinerU/README.md` | ADVISORY_ONLY |
| External source input | `.private_reference/external_repos/MinerU/docs/en/reference/output_files.md` | ADVISORY_ONLY |
| External source input | `.private_reference/external_repos/MinerU/mineru/cli/backend_options.py` | ADVISORY_ONLY |
| External source input | `.private_reference/external_repos/MinerU/mineru/cli/api_request.py` | ADVISORY_ONLY |
| External source input | `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/docs/absorptions/mineru-governed-document-ingestion/00_SCOPE_AND_CLAIM_BOUNDARY.md` | ADVISORY_ONLY |
| External source input | `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/docs/absorptions/mineru-governed-document-ingestion/04_GOVERNED_DOCUMENT_INGESTION_GATEWAY_SPEC.md` | ADVISORY_ONLY |
| External source input | `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/docs/absorptions/mineru-governed-document-ingestion/07_DOCUMENT_EXTRACTION_RECEIPT_CONTRACT.md` | ADVISORY_ONLY |
| External source input | `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/docs/absorptions/mineru-governed-document-ingestion/08_EXTRACTION_QUALITY_GATE.md` | ADVISORY_ONLY |
| External source input | `.private_reference/legacy/CVF_MinerU_Structured_Extraction_Adapter/docs/absorptions/mineru-governed-document-ingestion/09_RAG_INDEXING_HANDOFF_CONTRACT.md` | ADVISORY_ONLY |

## Non-Authority Inputs

The following are not CVF authority:

- upstream MinerU README badges, benchmark language, product claims, or support
  claims;
- copied adapter package source under the retained external folder;
- copied prototype checker and copied checker tests;
- copied sample receipts as schema authority;
- remote/http-client backend behavior as a privacy-approved route;
- provider-local memory or chat-only source summaries;
- parsing accuracy, OCR correctness, table/formula correctness, or document
  truth claims not backed by a future authorized proof tranche.

## Central Rule

Document extraction produces governed artifacts, not truth. CVF route policy
decides parser authority, extraction receipts record artifact lineage, quality
gates decide downstream use, and RAG handoff must preserve source limitations.

The allowed order is:

1. classify document sensitivity, file type, and requested downstream use;
2. apply the document-intelligence route decision and authorization gate;
3. select parser/backend only through an authorized route surface;
4. capture output artifacts as receipt evidence and storage-boundary records;
5. evaluate extraction quality before trusted downstream use;
6. chunk extracted material only with source pointers and quality disposition;
7. hand off to RAG/context/memory only when the receipt and quality disposition
   allow that use;
8. keep human review, validation, and truth verification separate from parser
   output.

## Owner Surface Matrix

| Document-extraction concept | External source basis | CVF owner surface | CVF adaptation | Future checker posture |
|---|---|---|---|---|
| Multi-format parsing | MinerU README | future Extraction Foundation adapter | parser capability input only | no checker now |
| Pipeline/VLM/hybrid/http-client backend choice | MinerU backend/API source | `decide_document_intelligence_route`; control envelope | route and privacy policy decide backend eligibility | checker candidate only if repeated route overclaims appear |
| Markdown and JSON outputs | MinerU output docs | future extraction receipt; `ExtractionStorageBoundary` | artifact manifest evidence only | no checker now |
| Layout/span visual debug files | MinerU output docs | future quality review artifact list | human-review support, not correctness proof | no checker now |
| Extraction receipt | retained receipt contract | future CVF extraction receipt; storage boundary | receipt vocabulary, not active schema | defer schema checker |
| Quality dimensions | retained quality gate | `ExtractionQualityReport` | quality disposition language | no checker now |
| RAG handoff | retained RAG handoff | `ExtractionChunk`; future RAG/context contract | handoff requires source pointer and quality status | checker candidate only after repeated bypass |
| Local-first and remote backend caution | retained privacy policy | route policy and future security review | remote route parked until authorized | no checker now |
| Copied Model Gateway adapter placement | retained package structure | Extraction Foundation owner surfaces | reject direct owner surface | no checker now |
| Prototype claim-boundary checker | retained checker | future static guard candidate only | candidate vocabulary, not active guard | evaluate in MSEA-T3 |

## Claim Boundary Vocabulary

Allowed bounded claims:

- MinerU can inform future parser-engine design;
- extracted Markdown/JSON can be artifact evidence;
- layout/span artifacts can support review and debugging;
- extraction receipts can record source file, parser/backend, artifact list,
  quality status, and downstream-use limits;
- extraction quality can decide whether downstream use is allowed, blocked, or
  requires review;
- RAG handoff can receive extracted chunks only with source pointers and quality
  disposition;
- current CVF owns route/envelope/quality/chunk/storage foundations that future
  parser adapters must map to.

Forbidden claims without separate authorization:

- CVF has implemented MinerU runtime integration;
- CVF has installed MinerU or downloaded MinerU models;
- CVF has run MinerU, OCR, VLM, hybrid, or remote/http-client parsing;
- extracted text is source truth or legal/domain truth;
- parser output proves document correctness;
- OCR, table, formula, or layout accuracy is certified;
- RAG may consume extracted text without receipt and quality disposition;
- copied sample receipts are canonical CVF schemas;
- copied checkers are active CVF guards;
- public or production readiness follows from this reference.

## Receipt Advisory

A future CVF-owned extraction receipt may be proposed only through fresh GC-018.
Until then, this reference is advisory vocabulary for source verification and
work-order authoring.

| Advisory field family | Current or future owner | Allowed use | Forbidden expansion |
|---|---|---|---|
| source file identity | future extraction receipt | record input path, hash, type, and source classification | claiming source truth |
| parser/backend identity | route decision and control envelope | record authorized parser/backend candidate | bypassing route policy |
| artifact manifest | `ExtractionStorageBoundary` or future receipt | record Markdown, JSON, image, layout, span, and model artifacts when produced | treating artifact existence as accuracy proof |
| quality status | `ExtractionQualityReport` | record quality disposition and review needs | claiming correctness without validation |
| downstream-use status | future receipt or handoff packet | allow, block, or require review before RAG/context use | silent context injection |
| source pointers | `ExtractionChunk` | preserve page, block, artifact, and quote pointers where available | orphan chunks |
| privacy route | route policy and future security review | require local or approved route for sensitive material | unapproved remote/http-client processing |
| human review | future work order or review packet | promote or reject extraction evidence | replacing human review with parser output |

## Quality And RAG Handoff Advisory

Future extraction handoff must preserve:

- source file identity and hash;
- parser/backend and version evidence, when authorized;
- artifact manifest and storage boundary;
- quality disposition and review requirement;
- chunk-to-source pointers;
- allowed downstream use;
- stale-index or reindex requirement;
- explicit limitation that extracted text is not source truth.

RAG/context/memory ingestion is forbidden unless the handoff includes receipt
evidence, quality disposition, and a downstream-use status that authorizes that
specific use.

## Rejected Direct Imports

| External source element | Disposition | Reason |
|---|---|---|
| MinerU runtime package | REJECT_DIRECT_IMPORT | no dependency/license/security/model lifecycle review in this lane |
| MinerU CLI/API/router/Gradio service | PARKED_RUNTIME | runtime invocation requires separate authorization |
| MinerU model downloader and local model lifecycle | PARKED_RUNTIME | model storage, provenance, and update policy are not decided |
| VLM/hybrid/http-client backend | PARKED_RUNTIME | remote/provider/privacy route needs separate security and live diagnostic plan |
| copied adapter package | REJECT_DIRECT_IMPORT | current owner is Extraction Foundation, not copied package authority |
| copied reference drafts | ADAPT_AS_LANGUAGE_ONLY | CVF-owned reference replaces copied draft authority |
| copied checker prototype | DEFER_WITH_REOPEN_CONDITION | no repeated miss justifies a new guard now |
| copied sample receipts | ADAPT_AS_LANGUAGE_ONLY | samples are not canonical schemas |
| public/production/support claims | BLOCK_UNTIL_CVF_PROOF | external claims are not CVF proof |

## Checker Candidate Ledger

| Candidate ID | Description | Value now | Decision |
|---|---|---|---|
| MSEA-CC-1 | flag claims that extracted text is truth or certified correctness | medium | evaluate in MSEA-T3 |
| MSEA-CC-2 | flag claims that MinerU runtime is installed, active, or production-ready | medium | evaluate in MSEA-T3 |
| MSEA-CC-3 | flag RAG/context use without receipt and quality disposition | medium | evaluate in MSEA-T3 |
| MSEA-CC-4 | validate a future extraction receipt schema | low now | defer until CVF owns schema fields |
| MSEA-CC-5 | enforce no remote/http-client parser route without privacy authorization | low now | defer until runtime route is proposed |

## Document Extraction Rule

Future document-extraction work must pass this order:

1. source-verify parser capability and CVF owner surface;
2. map parser/backend choice to document-intelligence route and control
   envelope;
3. define receipt and artifact manifest before downstream use;
4. map quality disposition to `ExtractionQualityReport` or an authorized
   successor;
5. preserve source pointers for chunks and RAG/context handoff;
6. reject direct runtime/package/checker import when a CVF owner already exists;
7. open fresh GC-018 before runtime, model download, OCR/VLM/hybrid execution,
   remote backend, RAG index mutation, checker, public-sync, or generated
   aggregate work.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | this reference plus existing Extraction Foundation owner surfaces | internal agents may cite the reference for planning, source verification, and review language only | MSEA-T1 source verification and this reference | N/A with reason: internal documentation/reference only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | future parser CLI/MCP adapter owner, if separately authorized | no current ingress, authentication, approval, mutation, raw-data release, public claim, parser execution, or RAG mutation | MSEA-T0/T1/T2 all defer adapter and runtime work | deferred adapter owner | `DEFERRED_WITH_REASON` |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | External repo or copied folder -> source-verified reconciliation -> CVF-owned document-extraction reference -> future GC-018 only if implementation is separately authorized |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this document-extraction reference |
| Disposition | ADAPT high-value MinerU and retained adapter doctrine to existing CVF Extraction Foundation owner surfaces |
| Claim boundary | this reference creates no runtime, package, public, provider, adapter, OCR, VLM, hybrid, remote backend, RAG index, parser execution, document-truth, production, or checker support |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MSEA-T2 document-extraction reference |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no runtime receipt is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: documentation reference and governance gate evidence only |
| invocationBoundary | local private provenance documentation only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, adapter, package, watcher, daemon, parser, RAG index, or production route interception claim |
| claimLanguage | document-extraction owner-surface mapping, claim boundary, receipt advisory, quality advisory, and RAG-handoff language only |
| forbiddenExpansion | no runtime, OCR/provider/live proof, public-sync, package activation, MinerU install, model download, API/router/Gradio service, VLM/hybrid/http-client backend, RAG index write, extraction accuracy, document truth, checker implementation, certification, generated aggregate mutation, or production/hosted readiness |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | `msea-t2-document-extraction-reference-2026-06-28` |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, source reads, apply_patch, governance gates |
| Target paths | this reference |
| Allowed scope source | active session next allowed move after MSEA-T1 |
| Before status evidence | HEAD `8790a502`; worktree clean before material patch |
| After status evidence | MSEA-T2 reference authored |
| Diff evidence | `git diff --name-status 8790a502 --` |
| Approval boundary | documentation/reference only |
| Claim boundary | no runtime, OCR/provider/live proof, public-sync, checker, generated aggregate, adapter, package activation, certification, MinerU install, model download, API/router/Gradio service, VLM/hybrid/http-client backend, RAG index write, extraction accuracy, document truth, or production/hosted readiness |
| Agent type | single-agent reviewer/closer |
| Invocation ID | `msea-t2-reference-2026-06-28` |
| Expected manifest | `docs/baselines/CVF_GC018_MSEA_T1_SOURCE_VERIFIED_DOCUMENT_EXTRACTION_RECONCILIATION_2026-06-28.md`; `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`; `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md`; `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` |
| Actual changed set | `docs/baselines/CVF_GC018_MSEA_T1_SOURCE_VERIFIED_DOCUMENT_EXTRACTION_RECONCILIATION_2026-06-28.md`; `docs/reference/CVF_MSEA_T2_DOCUMENT_EXTRACTION_CLAIM_BOUNDARY_RECEIPT_QUALITY_AND_RAG_HANDOFF_ADVISORY_2026-06-28.md`; `docs/reviews/CVF_MSEA_T3_STATIC_CHECKER_VALUE_DECISION_AND_LANE_CLOSEOUT_2026-06-28.md`; `docs/roadmaps/CVF_MSEA_T0_MINERU_STRUCTURED_EXTRACTION_EXTERNAL_ABSORPTION_ROADMAP_2026-06-28.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this tranche |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance reference. No public-sync remote, public commit,
public artifact path, or public document-extraction claim is authorized.

## Claim Boundary

This reference is a document-extraction claim-boundary, receipt-advisory,
quality-advisory, and RAG-handoff advisory surface only. It does not authorize
or claim MinerU runtime integration, parser execution, OCR execution,
VLM/hybrid backend routing, remote backend processing, model download,
API/router/Gradio service, RAG indexing, document QA, document truth
verification, parser accuracy, table/formula correctness, public-sync export,
checker enforcement, package activation, certification, generated aggregate
mutation, production readiness, hosted readiness, or universal document
intelligence.
