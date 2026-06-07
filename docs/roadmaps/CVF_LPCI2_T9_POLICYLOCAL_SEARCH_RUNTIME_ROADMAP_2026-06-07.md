# CVF LPCI2-T9 PolicyLocal Search Runtime Roadmap

Memory class: FULL_RECORD

Status: PROPOSED

docType: roadmap

Date: 2026-06-07

baseHead: `4ce03931`

## Purpose

Open the next PolicyLocal Corpus Intelligence roadmap after LPCI2-T8 reached a
bounded `READY` verdict for search implementation work-order authoring.

This roadmap scopes a local deterministic search runtime for the two-document
PolicyLocal pilot corpus. It turns the T8 governance scaffold into an
implementation plan for chunk generation, keyword/filter retrieval, response
boundary enforcement, and query receipt emission.

This roadmap does not dispatch implementation by itself.

## Scope / Applies To

Applies to future LPCI2-T9 work over the local PolicyLocal workspace:

- corpus records at
  `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json`;
- future generated chunk/index/query receipt files in the same local workspace;
- governing repo artifacts under `docs/reference/`, `docs/reviews/`,
  `docs/work_orders/`, and `docs/corpus-intelligence/`.

Allowed future T9 implementation scope, only after a separate work order:

- generate `policylocal-chunks.json` from existing READ_DEEP corpus records;
- build deterministic in-memory or local file-backed keyword/filter index;
- implement query boundary enforcement from the T7 contract;
- emit query receipts using the T8 receipt model;
- add deterministic tests for accepted, excluded, and escalate query paths.

Forbidden under this roadmap unless a later work order explicitly authorizes it:

- provider calls;
- chatbot answer generation;
- vector or embedding retrieval;
- legal advice quality claim;
- latest-law claim;
- hosted readiness;
- production readiness;
- public-sync;
- public readiness;
- corpus expansion beyond the current two files;
- current-law rescan after 2026-07-01.

## Authority Chain

| Authority | Evidence | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-07 request to move to a new roadmap after clean worktree | ACCEPT |
| LPCI2 roadmap | `docs/roadmaps/CVF_LPCI2_POLICYLOCAL_PRODUCTIZATION_ROADMAP_2026-06-03.md` | ACCEPT |
| T8 completion | `docs/reviews/CVF_LPCI2_T8_SEARCH_LAYER_SCAFFOLDING_COMPLETION_2026-06-04.md` | ACCEPT |
| Query receipt model | `docs/reference/CVF_LPCI_QUERY_RECEIPT_MODEL_2026-06-04.md` | ACCEPT |
| Retrieval trace design | `docs/reference/CVF_LPCI_RETRIEVAL_TRACE_DESIGN_2026-06-04.md` | ACCEPT |
| Response boundary contract | `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | ACCEPT |
| Corpus registry | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` and `.md` | ACCEPT |
| Local corpus records | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json` | ACCEPT |

## Authorization/Decision

Authorization: operator requested a new roadmap after worktree cleanup on
2026-06-07.

Decision: create a proposed LPCI2-T9 roadmap for local deterministic
PolicyLocal search runtime work-order authoring. Do not dispatch implementation
from this roadmap alone.

## Roadmap Decision

Decision: `OPEN_T9_SEARCH_RUNTIME_WORK_ORDER_CANDIDATE`

Rationale:

- T8 final readiness is `READY`.
- T8 says the next implementation work order must generate chunks, build a
  filter index, emit query receipts, and pass runtime acceptance testing.
- The current corpus records are schema `policylocal.corpusRecords.t8.v1` and
  include `topicTags`, `freshnessStatus`, boundary contract references, query
  receipt references, retrieval trace references, and structural negative
  search evidence.
- The search runtime can be local and deterministic; no provider call is needed
  to prove retrieval, boundary, and receipt mechanics.

## Non-Goals

- Do not implement T9 in this roadmap.
- Do not create search scripts, chunk files, index files, API routes, UI, or
  provider adapters in this roadmap.
- Do not build chat runtime or LLM answer generation.
- Do not add vector search or embeddings.
- Do not claim legal advice quality or current-law status.
- Do not claim hosted, production, public, or release readiness.
- Do not public-sync or push public-facing artifacts.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| T8 produced governance scaffold for future search implementation | `docs/reviews/CVF_LPCI2_T8_SEARCH_LAYER_SCAFFOLDING_COMPLETION_2026-06-04.md` | line 27 | `searchImplementationWorkOrder` | T8 completion review | ACCEPT |
| T8 final readiness verdict is READY | `docs/reviews/CVF_LPCI2_T8_SEARCH_LAYER_SCAFFOLDING_COMPLETION_2026-06-04.md` | lines 163, 253 | `finalReadinessVerdict` | T8 completion review | ACCEPT |
| T8 next control action requires chunk file, filter index, query receipts, and tests | `docs/reviews/CVF_LPCI2_T8_SEARCH_LAYER_SCAFFOLDING_COMPLETION_2026-06-04.md` | line 277 | `nextControlAction` | T8 completion review | ACCEPT |
| Query receipts must be emitted for every query | `docs/reference/CVF_LPCI_QUERY_RECEIPT_MODEL_2026-06-04.md` | line 96 | `receipt` | LPCI query receipt model | ACCEPT |
| Escalate receipts must have empty selectedCandidateIds | `docs/reference/CVF_LPCI_QUERY_RECEIPT_MODEL_2026-06-04.md` | lines 97, 105-106 | `selectedCandidateIds` | LPCI query receipt model | ACCEPT |
| T9 chunk file is designed but not yet generated | `docs/reviews/CVF_LPCI2_T8_SEARCH_LAYER_SCAFFOLDING_COMPLETION_2026-06-04.md` | lines 205, 227 | `policylocal-chunks.json` | T8 completion review | ACCEPT |
| Chunk schema version is defined | `docs/reference/CVF_LPCI_RETRIEVAL_TRACE_DESIGN_2026-06-04.md` | lines 50, 72 | `policylocal.chunk.t8.v1` | LPCI retrieval trace design | ACCEPT |
| Lookup sequence is filter-first then keyword-rank then boundary check | `docs/reference/CVF_LPCI_RETRIEVAL_TRACE_DESIGN_2026-06-04.md` | lines 108-116 | `lookupSequence` | LPCI retrieval trace design | ACCEPT |
| Initial retrieval must not require vector store | `docs/reference/CVF_LPCI_RETRIEVAL_TRACE_DESIGN_2026-06-04.md` | lines 122-124 | `vectorStore` | LPCI retrieval trace design | ACCEPT |
| Boundary contract is required before any search layer opens | `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | line 21 | `searchLayer` | LPCI boundary contract | ACCEPT |
| Not-yet-in-force answers require freshness disclosure | `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | lines 105, 120 | `freshnessStatus` | LPCI boundary contract | ACCEPT |
| Corpus records are t8 schema | `docs/reviews/CVF_LPCI2_T8_SEARCH_LAYER_SCAFFOLDING_COMPLETION_2026-06-04.md` | lines 116-121, 249 | `schemaVersion` | PolicyLocal corpus records evidence | ACCEPT |
| Corpus records include negative search evidence | `docs/reviews/CVF_LPCI2_T8_SEARCH_LAYER_SCAFFOLDING_COMPLETION_2026-06-04.md` | lines 98, 127, 248 | `negativeSearchEvidence` | PolicyLocal corpus records evidence | ACCEPT |
| Corpus records include query receipt reference | `docs/reviews/CVF_LPCI2_T8_SEARCH_LAYER_SCAFFOLDING_COMPLETION_2026-06-04.md` | lines 128, 142 | `queryReceiptModelRef` | PolicyLocal corpus records evidence | ACCEPT |
| Corpus records include retrieval trace reference | `docs/reviews/CVF_LPCI2_T8_SEARCH_LAYER_SCAFFOLDING_COMPLETION_2026-06-04.md` | lines 129, 143 | `retrievalTraceDesignRef` | PolicyLocal corpus records evidence | ACCEPT |
| Registry records T8 READY but blocks implementation without fresh work order | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | lines 83, 145, 161 | `READY_FOR_OPERATOR_AUTH` | GC-051 registry markdown | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | T9 work-order obligation | Source evidence | Status |
| --- | --- | --- | --- |
| Use T8 READY scaffold | cite T8 completion and registry rows | T8 completion lines 163, 253; registry line 161 | REQUIRED |
| Generate chunks before index | produce `policylocal-chunks.json` with schema `policylocal.chunk.t8.v1` | retrieval design lines 50-72; T8 completion lines 205, 227 | REQUIRED |
| Preserve source trace | chunk rows must preserve sourcePath, sourceHash, parentRecordHash, chunkHash, articleRef | retrieval design lines 50-72 | REQUIRED |
| Use filter-first keyword retrieval | hard filters, soft filters, keyword rank, boundary check | retrieval design lines 108-116 | REQUIRED |
| Emit query receipts | every query produces `policylocal.queryReceipt.t8.v1` receipt | receipt model lines 57, 96 | REQUIRED |
| Enforce escalate boundary | escalate answers have empty selectedCandidateIds and no legal advice | receipt model lines 97, 105-106; boundary contract EC rules | REQUIRED |
| Preserve freshness disclosure | not_yet_in_force candidates require disclosure | boundary contract lines 105, 120 | REQUIRED |
| Exclude vector retrieval | no embeddings/vector store in T9 | retrieval design lines 122-124 | REQUIRED |
| Produce runtime negative evidence | convert structural negative evidence into deterministic query receipts | T8 completion line 217 and registry line 146 | REQUIRED |

## Tranche Plan

| Tranche | Name | Objective | Exit criteria |
| --- | --- | --- | --- |
| T9A | Search Work Order And Source Map | Create source-verified work order with allowed paths, tests, and forbidden claims | work order DISPATCH_READY only after autorun gates pass |
| T9B | Chunk Generator | Generate article-boundary chunks from existing t8 corpus records | `policylocal-chunks.json`; drift check; chunk hash check; tests |
| T9C | Keyword/Filter Index | Build local deterministic index over chunk rows | exact/filter/topic/query cases pass; no vector or provider |
| T9D | Boundary And Receipt Runtime | Apply EC-01 through EC-04, freshness disclosure, and receipt emission | accepted and escalate receipts conform to T8 model |
| T9E | Deterministic Query Acceptance Evidence | Produce query receipt evidence for positive, zero-result, jurisdiction mismatch, and legal-advice escalation paths | test receipts saved or summarized; no provider output |
| T9F | Closure Review | Close only local search mechanics if tests and gates pass | CLOSED_PASS_BOUNDED or BLOCKED with reason |

## Work Plan

1. Author a T9 work order with source-verified allowed paths and no runtime
   implementation before pre-dispatch gates pass.
2. Recheck local corpus drift before generating chunks.
3. Generate chunk rows from existing t8 corpus records only.
4. Build deterministic keyword/filter retrieval over chunk rows.
5. Apply the boundary contract before selecting candidates for response.
6. Emit query receipts for every query path.
7. Validate positive, negative, and escalation cases with deterministic tests.
8. Close with explicit public, provider, legal-advice, and production-readiness
   boundaries.

## Work-Order Candidate

Recommended next work order:

`docs/work_orders/CVF_WO_LPCI2_T9_POLICYLOCAL_SEARCH_RUNTIME_2026-06-07.md`

Recommended status at authoring: `DRAFT` or `DISPATCH_READY` only after source
verification and pre-dispatch autorun pass.

Allowed future changed paths should be constrained to:

- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\scripts\`;
- `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\`;
- T9 work order, completion review, and optional reference spec under `docs/`;
- GC-051 registry only if the generated search evidence changes corpus status.

Forbidden future changed paths unless separately authorized:

- `EXTENSIONS/`;
- `.github/`;
- package files and lockfiles;
- public-sync clone;
- provider configuration;
- production deployment configuration.

## Acceptance Criteria For T9

| Criterion | Required result |
| --- | --- |
| Corpus input stable | corpus records file hash and per-record sourceHash drift checks pass |
| Chunk generation | chunks preserve sourcePath, sourceHash, parentRecordHash, chunkHash, articleRef, topicTags, answerClass, freshnessStatus |
| Index behavior | jurisdiction, topicTags, articleRef, answerClass, and freshnessStatus filters are deterministic |
| Positive query receipt | law number or effective date query returns SUMMARY_WITH_SOURCE with citation and freshness disclosure |
| Negative query receipt | out-of-corpus law query returns zero selected candidates with excluded reason |
| Escalation query receipt | legal advice or current applicability query returns ESCALATE_OR_ABSTAIN with empty selectedCandidateIds |
| Boundary enforcement | DIRECT_CITED_ANSWER remains blocked |
| Provider boundary | no provider calls, model calls, or LLM answer generation |
| Public boundary | no public-sync, hosted, production, or public readiness claim |

## Verification/Evidence

Pre-roadmap gate:

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 4ce03931 --head HEAD`: PASS.

Roadmap source evidence:

- T8 completion review records `Final readiness verdict: READY`.
- T8 completion review records the next control action: generate chunk file,
  build filter index, implement query receipt emission, and run runtime
  acceptance testing.
- Query receipt model requires every query to emit a receipt.
- Retrieval trace design defines chunk schema, filter-first keyword rank, and
  no-vector boundary.
- Response boundary contract is required before search opens.
- GC-051 registry records PolicyLocal as ready for operator-authored search
  implementation work-order authoring, while keeping implementation blocked
  until fresh authorization.

## Knowledge Absorption Blind-Spot Control Block

- Prior absorption evidence resolved: LPCI2-T4S, T4, T5, T6, T7, T8, GC-051
  registry, query receipt model, retrieval trace design, and boundary contract.
- Detailed source files read: T8 completion review, T6 completion review, LPCI2
  productization roadmap, T8 query receipt model, T8 retrieval trace design,
  T7 response boundary contract, GC-051 registry rows, and local t8 corpus
  records.
- Accepted value normalized into existing CVF owner surfaces: search is a local
  deterministic PolicyLocal/LPCI implementation candidate, not a general CVF
  chatbot or legal-advice product claim.
- Accept/defer/reject disposition: accept T9 local search work-order candidate;
  defer chat runtime, vector retrieval, corpus expansion, and public-sync;
  reject provider calls, legal advice, current-law claim, hosted readiness, and
  production readiness in T9.
- Adversarial role review: the main risk is converting a retrieval proof into a
  legal answer quality claim. T9 must prove mechanics only: chunks, filters,
  boundary decisions, and receipts.
- Blind-spot delta: exact script/interface names are not defined in this
  roadmap. The T9 work order must source-verify file paths and function names
  before implementation.
- Verdict: PARTIAL_WITH_LOW_RISK_REASON. Remaining unknowns are intentionally
  deferred to the T9 source-verified work order and do not block this roadmap.

## Corpus Completeness And Report Integrity

- Corpus task class: bounded roadmap source review, not a full fresh corpus
  rescan.
- Corpus root: bounded source set listed in Authority Chain.
- Snapshot time: 2026-06-07 at base `4ce03931`.
- Enumeration command: `rg --files --hidden --no-ignore docs D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local | rg "(LPCI2_T8|LPCI_QUERY_RECEIPT|LPCI_RETRIEVAL_TRACE|LPCI_RESPONSE_BOUNDARY|policylocal-corpus-records|CVF_CORPUS_SCAN_REGISTRY)"`
- Manifest artifact or inline manifest: Authority Chain and Source Verification Block.
- Manifest hash: N/A with reason - inline bounded source manifest only.
- Processing ledger artifact or inline ledger: Source Verification Block.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=8; ledger_terminal=8; exclusions=2; unresolved=0.
- Unresolved files: none.
- Declared exclusions: no fresh DOCX extraction; no full Policy_Local source
  tree scan; no legal/policy content reclassification.
- Unreadable or unsupported files: none encountered in the bounded source set.
- Aggregation check: source facts in the roadmap trace back to cited lines.
- Drift check: PASS for repo source set; local corpus records drift must be
  rerun by T9 before implementation.
- Output traceability: every runtime/source claim is in the Source Verification
  Block or marked as future work-order scope.
- Adversarial verification: checked T8 READY, T8 structural negative evidence
  caveat, query receipt mandatory fields, no-vector boundary, and
  ESCALATE_OR_ABSTAIN selectedCandidateIds rule.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Knowledge System Reconciliation

- Knowledge task class: roadmap from corpus-derived search readiness evidence.
- Source manifest: Authority Chain and Source Verification Block.
- Source manifest hash: N/A with reason - inline manifest.
- Enumeration safety: `rg --files --hidden --no-ignore docs D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local`
- Intake registry or ledger: GC-051 registry rows for PolicyLocal.
- Authority assets: T8 completion, T6 completion, LPCI2 roadmap, query receipt
  model, retrieval trace design, boundary contract, registry JSON/MD, and local
  t8 corpus records.
- Derived views: this T9 roadmap.
- Semantic region ledger: POLICYLOCAL_CORPUS, QUERY_RECEIPT, RETRIEVAL_TRACE,
  RESPONSE_BOUNDARY, GC051_REGISTRY, T9_ROADMAP.
- Region reconciliation: assets=8; mapped=8; deferred=0; unmapped=0.
- Orphan or unmapped assets: none
- Cross-region links: corpus records reference query receipt model, retrieval
  trace design, boundary contract, topicTags, freshnessStatus, and
  negativeSearchEvidence.
- Drift check: PASS
- Rebuildability check: PASS from cited docs and local corpus records.
- Retrieval boundary: roadmap only; no runtime retrieval is implemented here.
- Adversarial verification: checked that `READY` authorizes only fresh work-order
  authoring, not implementation or public/product readiness.
- Knowledge-map verdict: RECONCILED_VERIFIED

## Corpus Intelligence Classification

- Classification task class: LEGAL_POLICY_QA
- Source corpus evidence: `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local\data\generated\policylocal-corpus-records.json`
- Knowledge map evidence: Knowledge System Reconciliation block above.
- Classification ledger: inline table below.
- Legal/policy corpus: YES
- Domain fields: jurisdiction=VN_NATIONAL; authorityLevel=law; effectiveDate=2026-07-01; sourceAuthority=Quoc Hoi; answerBoundary=SUMMARY_WITH_SOURCE ceiling plus ESCALATE_OR_ABSTAIN for legal advice/current applicability.
- Response Boundary: DIRECT_CITED_ANSWER, SUMMARY_WITH_SOURCE, PROCEDURAL_GUIDANCE, ESCALATE_OR_ABSTAIN
- Adversarial sampling plan: T9 work order must produce deterministic query receipts for positive, zero-result, jurisdiction mismatch, legal-advice escalation, and current-applicability escalation cases.
- Classification verdict: CLASSIFIED_WITH_DECLARED_GAPS

### Corpus Intelligence Classification Ledger

| sourcePath | processingStatus | knowledgeRegion | ownerSurface | disposition | evidencePointer | answerClass | domainFields |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Policy_Local/data/generated/policylocal-corpus-records.json` | READ_DEEP | LEGAL_POLICY | LEGAL_ADVISORY | ACCEPT_SUMMARY_ONLY | schemaVersion `policylocal.corpusRecords.t8.v1`; two records; T8 READY | SUMMARY_WITH_SOURCE | jurisdiction=VN_NATIONAL; authorityLevel=law; effectiveDate=2026-07-01; sourceAuthority=Quoc Hoi |
| `docs/reference/CVF_LPCI_QUERY_RECEIPT_MODEL_2026-06-04.md` | READ_SHALLOW | REFERENCE | RETRIEVAL_INDEX | ACCEPT | schemaVersion `policylocal.queryReceipt.t8.v1` | ESCALATE_OR_ABSTAIN | answerBoundary=query receipt model only; no legal answer |
| `docs/reference/CVF_LPCI_RETRIEVAL_TRACE_DESIGN_2026-06-04.md` | READ_SHALLOW | REFERENCE | RETRIEVAL_INDEX | ACCEPT | designVersion `policylocal.retrievalTrace.t8.v1` | ESCALATE_OR_ABSTAIN | answerBoundary=retrieval trace design only; no legal answer |
| `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-04.md` | READ_SHALLOW | GOVERNANCE | PRIVATE_PROVENANCE | ACCEPT | contractVersion `policylocal.boundaryContract.t7.v1` | ESCALATE_OR_ABSTAIN | answerBoundary=boundary contract only; no legal answer |

Response-boundary classes allowed for future T9 mechanics:

- `SUMMARY_WITH_SOURCE`: allowed only with sourcePath, evidencePointer,
  effectiveDate, freshnessStatus, and freshness disclosure when required.
- `ESCALATE_OR_ABSTAIN`: required for legal advice, current applicability before
  effective date, legal interpretation, and compliance determination.
- `DIRECT_CITED_ANSWER`: blocked for the pilot corpus.
- `PROCEDURAL_GUIDANCE`: deferred until separate proof.

GC-050 boundary: this roadmap does not claim legal advice quality, latest-law
status, runtime answer truth, or production response readiness.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Handled or deferred | Next control action |
| --- | --- | --- | --- | --- | --- |
| T8 READY can be overread as implementation authorization | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | ROADMAP_ADDED | HANDLED_IN_BATCH | T9 roadmap separates roadmap, work-order authoring, and implementation |
| Structural negative search evidence is not runtime query evidence | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | MACHINE_CHECK_CANDIDATE | DEFERRED_TO_T9 | T9 work order must produce deterministic query receipts |
| Legal corpus search can be overclaimed as legal advice | CLAIM_BOUNDARY_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | HANDLED_IN_BATCH | Claim boundary preserves SUMMARY_WITH_SOURCE and ESCALATE_OR_ABSTAIN limits |

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: private provenance roadmap only; no public-facing artifact or public
repository change is authorized in this batch.

This roadmap is private provenance planning for a local PolicyLocal pilot. Any
public-facing claim requires separate public-sync authorization, public-safe
artifact selection, remote verification, and public commit evidence.

## Claim Boundary

This roadmap claims only that PolicyLocal LPCI2 has a source-backed T9 search
runtime work-order candidate after T8 readiness. It does not implement search,
chat, provider use, vector retrieval, legal advice, latest-law status, hosted
readiness, production readiness, public readiness, public-sync, memory
reinjection, autonomous mutation, or Learning Orchestrator runtime behavior.
