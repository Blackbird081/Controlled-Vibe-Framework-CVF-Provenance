# CVF LPCI1 Web Grounding And Clearance Conformance Design

Memory class: FULL_RECORD

Status: DESIGN_ACCEPTED_BOUNDED_CONDITIONAL_ON_SPEC_RECONCILIATION

Date: 2026-08-08

Design ID: LPCI1-WEB-D1

docType: audit

## Purpose

Define one bounded, source-verified LPCI1-Web design candidate for evidence-grounded answers from eligible public records, fail-closed handling of every non-public or unowned authorization case, minimized provider and client disclosure, response-local audit correlation, and deterministic later-build proof cases. This document is DESIGN only.

## Scope / Target / Owner Boundary

ownerBoundary: the existing LPCI1-Web query route, LPCI retrieval/filter library, route-governance authentication surfaces, and LPCI dashboard response consumer are the current product boundary. LPCI2, generic retrieval, persistence, vector/RAG, corpus mutation, provider execution, live proof, and public export are excluded.

The selected design does not require an authorization owner that does not exist. It keeps current access public-only and treats richer authorization as parked work requiring a separately governed owner and contract.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | structural headings; Fast Doc literals; trace fields; epistemic fields; finding disposition vocabulary; Delta receipt/action tokens; public disposition token; file-size boundary |
| gateRunPurpose | ensure these documentation outputs expose the exact evidence and claim boundaries the reviewer and worker-return fast gate require |
| claimBoundary | LPCI1-WEB-D1 source-backed documentation design only |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| indexed content evidence exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 33-50 | `contentSnippet` | `LpciIndexRecord` | EXISTS | ACCEPT |
| indexed sensitivity label exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 33-50 | `sensitivityLevel` | `LpciIndexRecord` | EXISTS | ACCEPT |
| client clearance boolean exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 52-58 | `sensitivityClearance` | `FilterParams` | EXISTS | ACCEPT |
| retrieval receipt retains full matched rows | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 71-80 | `matched_records` | `RetrievalReceipt` | EXISTS | ACCEPT |
| audit receipt exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 94-109 | `AuditReceipt` | `AuditReceipt` | EXISTS | ACCEPT |
| retrieval populates full matched rows | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/retrieval.ts` | lines 108-122 | `runRetrievalPipeline` | LPCI retrieval pipeline | RUNTIME_BEHAVIOR | ACCEPT |
| prompt omits content evidence | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 40-90 | `buildAnswerBoundaryPrompt` | LPCI query route | RUNTIME_BEHAVIOR | ACCEPT |
| no-provider response returns full retrieval receipt | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 189-216 | `retrievalReceipt` | LPCI query route | RUNTIME_BEHAVIOR | ACCEPT |
| provider success response is already reduced | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 273-306 | `matchedSources` | LPCI query route | RUNTIME_BEHAVIOR | ACCEPT |
| filter honors client boolean only for classified rows | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.ts` | lines 14-28 and 109-120 | `applySensitivityFilter` | LPCI filter pipeline | RUNTIME_BEHAVIOR | ACCEPT |
| UI no-provider source count reads retrieval receipt | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.tsx` | lines 127-135 | `retrievalReceipt.matched_paths` | LPCI dashboard `QueryResult` consumer | RUNTIME_BEHAVIOR | ACCEPT |
| UI already consumes audit receipt and matched sources | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.tsx` | lines 17-26 and 168-207 | `auditReceipt` | LPCI dashboard `QueryResult` consumer | EXISTS | ACCEPT |
| canonical snippet is a bounded display hint | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` | Searchable Fields, lines 78-85 | `contentSnippet` | LPCI1 T3 search/filter/index contract | LITERAL_INVARIANT | ACCEPT |
| canonical sensitivity policy is public-first and non-public authorization-bound | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | Sensitivity Classification (NR-06), lines 209-233 | `sensitivityLevel` | LPCI1 T2 domain classification contract | LITERAL_INVARIANT | ACCEPT |
| canonical receipt contains full matched records and is described as LLM context | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | retrieval receipt and LLM context, lines 72-98 and 114-127 | `matched_records` | LPCI1 T4 retrieval contract | LITERAL_INVARIANT | ACCEPT |
| current grant owner or reader | current LPCI route/library/auth sources and canonical LPCI closures | negative search | `grantEvidence` | no owning runtime interface found | DOC_ONLY_NEW | BLOCKED_SOURCE_NOT_FOUND |

The final row blocks only a richer non-public authorization design. It does not block the selected public-only design.

## Existing Runtime Symbols And New Doc-Only Fields

Existing runtime symbols used as facts are `LpciIndexRecord`, `contentSnippet`, `sensitivityLevel`, `FilterParams.sensitivityClearance`, `RetrievalReceipt.matched_records`, `AuditReceipt`, `buildAnswerBoundaryPrompt`, `matchedSources`, and `routeGovernanceProof`.

The following are DOC_ONLY_NEW design vocabulary and are not claimed as runtime fields or types: `modelEvidenceProjection`, `evidenceEligibilityRule`, `authorizationContext`, `authorizationDecision`, `grantEvidence`, `noProviderProjection`, `auditCorrelation`, `syntheticProofMatrix`, `GROUNDING_EVIDENCE_UNAVAILABLE`, and any future helper or resolver name used below. A later work order must source-verify or explicitly introduce each before BUILD.

## Findings

1. The current prompt receives record path/status/date metadata but no `contentSnippet`; therefore an answer may be constrained by policy metadata without being grounded in record text.
2. Retrieval already retains bounded snippets inside `matched_records`, so the public-only value gap can be addressed without adding a persistence or vector/RAG dependency.
3. The no-provider response returns the full retrieval receipt, including matched records, although the UI needs only a match count plus existing audit data.
4. Client `sensitivityClearance` is not trustworthy authorization. Current filtering gives it classified-row effect without a server-owned grant decision.
5. No current LPCI grant store, grant reader, revocation contract, corpus-scoped entitlement resolver, or owner was found. A general non-public access design is not selectable in D1.

## Grounding Option Matrix

groundingOptionMatrix:

| Option | Supporting evidence | Contradicting evidence / risk | Disclosure posture | Disposition |
|---|---|---|---|---|
| A. Minimized eligible snippet projection | existing `contentSnippet` is bounded by the T3 contract and retained in `matched_records`; it is the smallest current-field candidate for closing the prompt content gap | T3 calls it a display hint, not approved answer evidence; it can also be blank, oversized, stale, or adversarial | send only an allowlisted public projection, never the receipt | SELECTED_DESIGN_CANDIDATE_CONDITIONAL_ON_SPEC_RECONCILIATION |
| B. Metadata-only abstention | existing prompt metadata supports source identification and bounded refusal | cannot support a substantive content claim | no content disclosure; useful fail-closed fallback | REQUIRED FALLBACK |
| C. New approved-evidence contract | could eventually formalize excerpts, provenance, transformations, and grants | no current schema, owner, storage, or reader; selecting it would invent runtime authority | potentially safe only after separate governance | PARKED; reopen when an owner and source contract are committed |

Rejection criteria for any grounding option: it permits a substantive answer without eligible text; exposes full `matched_records`; sends `sourceHash`, auth/session facts, route proof, filters, or sensitivity labels to the provider; allows non-public evidence without server-owned grant evidence; or requires an absent owner.

## Selected Model Evidence Projection

modelEvidenceProjection: DOC_ONLY_NEW name for an ephemeral provider-bound value assembled from existing record fields. For each eligible public match it contains only:

This projection is not BUILD-ready under the current T3/T4 contracts. A later
authorized SPEC must explicitly ratify whether the display-hint snippet is
eligible answer evidence and replace T4's full-receipt-as-context wording with
a minimized model-bound projection contract before any implementation.

| Existing value | Provider disposition | Reason |
|---|---|---|
| `normalizedPath` | INCLUDE | bounded source attribution already exposed as matched source |
| `effectiveDate` | INCLUDE when present | freshness context |
| `status` | INCLUDE | current record lifecycle status used by the answer boundary |
| `answerClass` | INCLUDE | bounded response class |
| `contentSnippet` | INCLUDE only after eligibility | the actual grounding text |
| `sourceHash` | EXCLUDE | audit/index metadata unnecessary for answering |
| `sensitivityLevel` | EXCLUDE from provider | eligibility is decided server-side; label disclosure is unnecessary |
| full `RetrievalReceipt` or `matched_records` | EXCLUDE | violates minimization and couples provider input to internal receipt shape |
| actor, grant, session, filters, `routeGovernanceProof` | EXCLUDE | authorization and governance metadata are not answer evidence |

Evidence is placed in a fixed, clearly delimited untrusted-evidence block. Delimiters and control characters are escaped or encoded before interpolation. The system instruction states that evidence text is data, not instructions. This is a defense boundary, not a claim that a model can be made universally immune to prompt injection.

## Evidence Eligibility Rule

evidenceEligibilityRule: DOC_ONLY_NEW rule split across two ordered boundaries.
Under the selected D1 public-only design, the canonical mandatory Stage 1
sensitivity boundary admits only records whose normalized sensitivity is
exactly `public`, before search or receipt construction. This is a proposed
conformance rule, not a claim about the current permissive runtime. After the
remaining canonical filter/search/ranking stages, a
separate model-evidence eligibility check runs before provider dispatch or
outward positive-answer construction.

A record is model-evidence eligible only when all are true: it passed the
public-only Stage 1 sensitivity admission; `contentSnippet` is present after
trimming; its source-contract length is at most 512 characters; the record
survived the later status, search, answer-class, and facet stages; and the
serialized evidence block passes deterministic delimiter/control-character
handling.

Missing, blank, over-limit, unknown-sensitivity, restricted, confidential, classified, or malformed evidence is excluded. If no eligible snippet remains, provider dispatch count is zero and the route returns a bounded negative result with `AuditReceipt`. Metadata alone must not produce a substantive answer.

## Authorization Option Matrix

authorizationOptionMatrix:

| Option | Source support | Owner / revocation readiness | Failure posture | Disposition |
|---|---|---|---|---|
| A. Dedicated LPCI resolver with injected read-only grant source | compatible with corpus-scoped, server-side decisions | no current grant source, interface, or owner | can fail closed when reader unavailable, but cannot be selected now | PARKED; safest future candidate after separate authority |
| B. GC-051-owned grants | corpus registration policy discusses authorization for restricted material | registry is not verified as a user entitlement store or revocation reader | ownership would be inferred | REJECT as current owner |
| C. Generic team/scope reuse | existing route auth can identify an actor/session | no verified mapping from generic scopes to LPCI corpus sensitivity grants | risks privilege conflation and cross-corpus access | REJECT |
| D. Current public-only fail-closed | requires no absent owner and satisfies public unrestricted rule | does not unlock non-public value | all non-public evidence excluded | SELECTED |

Rejection criteria for authorization: any client assertion becomes authority; a generic role is treated as a corpus grant; a service token gains implicit content access; grant absence/reader error/expiry/revocation is permissive; cross-corpus grants match; or confidential/classified access is inferred without explicit operator authority.

## Authorization Context, Decision, And Grant Evidence

authorizationContext: DOC_ONLY_NEW conceptual input. In this selected design it is limited to source-verified server identity facts needed to bind audit correlation; it confers no non-public access.

authorizationDecision: DOC_ONLY_NEW conceptual result fixed to `PUBLIC_ONLY` for D1. Client `sensitivityClearance`, request-body role, or request-body corpus identity cannot elevate it.

grantEvidence: DOC_ONLY_NEW and absent from current runtime. Its absence is decisive: exact-corpus, cross-corpus, expired, revoked, malformed, unreadable, service-token-only, and impersonated-session scenarios all remain non-public denied. A later general-access design may reopen only after a named server-owned reader and grant schema define subject, corpus, sensitivity ceiling, issuer, issued/expiry times, revocation state, decision ID, and failure semantics.

## Client Clearance Disposition

clientClearanceDisposition: ignore or reject `FilterParams.sensitivityClearance` as an authority-bearing input. The server computes public-only eligibility regardless of a client-supplied true value. The selected design must not preserve any path where that boolean admits classified content.

## No-Provider Projection

noProviderProjection: DOC_ONLY_NEW response policy using existing response values. When no provider is configured or evidence is ineligible, the client receives only the bounded negative `receiptType`/message/query fields already appropriate to the route, existing `AuditReceipt`, and existing `routeGovernanceProof` where required. It does not receive `retrievalReceipt`, `matched_records`, snippets, `sourceHash` or any new evidence hash, sensitivity labels, grants, or internal filter state. The existing mandatory `AuditReceipt.model_response_hash` remains inside the retained audit projection unless a later SPEC changes that contract.

The UI source count moves from the current optional `retrievalReceipt.matched_paths.length` read to `auditReceipt.matched_paths.length`, or to existing `matchedSources` when supplied. This is a later BUILD candidate, not an edit made by D1.

## Audit Correlation

auditCorrelation: DOC_ONLY_NEW design rule. Current `AuditReceipt` provides
`auditId`, `query`, `query_timestamp`, `matched_paths`, answer/flag fields,
`model_response_hash`, response boundary, filters, and sensitivity-filter
state. It does not provide a query hash, actor identity, corpus ID, grant
reference, authorization decision, provider ID, or model ID. Current
`routeGovernanceProof` separately provides response-local actor/auth evidence.

A later authorized SPEC must decide a minimized correlation contract that
binds `auditId` to server-derived actor, exact corpus, public-only authorization
decision, and evidence-path outcome without placing those facts in the provider
prompt or inventing persistence. Until then, D1 claims response-local design
correlation only, not durable authorization audit correlation. Client-visible
audit output records only paths that survived the selected public-only Stage 1
policy and must not imply that excluded records were searched or that the
answer covers the full corpus.

For a zero-provider branch, provider-call count is zero and no provider/model
identifier is invented. For a provider branch, later synthetic seams must
prove exactly one call and response-local correlation to the returned audit
receipt without exposing prompt content or secrets.

## Required Threat Matrix

| Threat / case | Required design behavior | Fail condition |
|---|---|---|
| forged client clearance `true` | ignore/reject as authority; public-only remains | any non-public record becomes eligible |
| public-only corpus | eligible bounded snippets may be projected | full rows or unnecessary metadata sent |
| session with no grant | public-only | non-public access inferred from session |
| exact-corpus grant | public-only now; parked future resolver may evaluate | D1 treats absent grant contract as real |
| cross-corpus grant | public-only and deny cross-corpus use | corpus mismatch accepted |
| confidential/classified override | denied absent explicit operator-authorized future contract | generic role or boolean grants access |
| restricted or unknown sensitivity | excluded | unknown defaults public |
| expired/revoked/malformed grant | public-only; future resolver must deny | permissive parsing or stale grant use |
| grant reader failure | public-only; future resolver must fail closed | fallback to client clearance |
| service token with no grant | public-only | service identity implies content entitlement |
| impersonated session | public-only; audit actor binding preserved | request-body identity controls access |
| mixed public and non-public matches | project only eligible public snippets | protected paths/text leak to provider or client |
| missing/blank/oversize evidence | zero provider call if none remains; bounded negative | metadata-only substantive answer |
| delimiter or prompt injection | deterministic escaping/delimiting; evidence treated as data | raw evidence can break framing |
| no-provider response | minimized negative response plus audit correlation | full retrieval receipt disclosed |

## Synthetic Proof Matrix

syntheticProofMatrix: DOC_ONLY_NEW later-build proof plan. No test or provider was run in D1.

| ID | Fixture / action | Positive assertion | Fail-closed assertion |
|---|---|---|---|
| P1 | one public record with exact bounded snippet and provider seam | provider sees exactly allowlisted path/date/status/class/snippet; one call; audit ID correlates | no hash, sensitivity, receipt, auth, filter, or route-proof field in prompt |
| P2 | provider unavailable with public match | response has bounded negative, query/receipt type, existing audit including its current `model_response_hash`, and route proof; UI count derives from audit paths | zero provider calls; no retrieval receipt, rows, snippet, `sourceHash`, or new evidence hash in response |
| P3 | client sends clearance true with public record | public record behavior equals clearance false | boolean does not alter server authorization |
| F1 | only missing, blank, or greater-than-512 snippets | bounded grounding-unavailable negative and audit correlation | zero provider calls; no metadata-only substantive answer |
| F2 | only restricted/confidential/classified/unknown records plus forged clearance | bounded filtered/no-evidence result | zero provider calls and no protected path/text in response |
| F3 | mixed public and non-public matches | only public projection reaches provider and public paths reach response audit | no protected metadata or text; audit makes no full-corpus claim |
| F4 | snippet contains delimiter and instruction-like text | serialized block remains structurally bounded and content is quoted as evidence | injected text cannot create a second instruction block in deterministic serialization |
| A1 | no session grant, service token, or impersonated request identity | public-only result | identity alone grants no non-public access |
| A2 | exact/cross-corpus/expired/revoked/malformed synthetic grant supplied before a grant owner exists | all cases remain public-only | no unowned grant shape is accepted |
| A3 | future grant reader seam returns error | public-only/deny result with safe audit classification | no client-clearance fallback |

## Later Build Candidate Manifest

laterBuildCandidateManifest: proposals only; all remain unauthorized until a fresh operator checkpoint, GC-018, work order, and source verification.

| Candidate path | Candidate change | Authority now |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | construct eligible minimized evidence projection; minimize no-provider response | FORBIDDEN in D1 |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.ts` | remove client authority effect and enforce public-only eligibility | FORBIDDEN in D1 |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.tsx` | derive no-provider count from existing audit/matched-source fields | FORBIDDEN in D1 |
| existing same-family LPCI route/filter/UI test files | deterministic P1-P3, F1-F4, A1-A3 cases with a synthetic provider seam | FORBIDDEN in D1 |

No new persistence, vector store, RAG service, provider adapter, grant database, or general auth subsystem is a later-build candidate in this design.

## Findings / Position

exitRecommendation: `DESIGN_ACCEPTED_BOUNDED_CONDITIONAL_ON_SPEC_RECONCILIATION`.

The recommended bounded design candidate is Option A plus Option B as its
mandatory zero-evidence fallback and authorization Option D. It does not close
runtime defects in D1. A later SPEC must ratify the evidence class, minimized
projection, response shape, and correlation contract before BUILD can be
considered. Option C and authorization Option A remain parked behind explicit
reopen conditions.

## Risk / Corrective Action

| Risk | Corrective action in design | Reopen / reject condition |
|---|---|---|
| snippets are display hints rather than adjudicated quotations | cap, trim, delimit, attribute, and restrict claims to text actually present | reject BUILD if exact source-contract semantics cannot be preserved |
| prompt injection in indexed text | deterministic serialization and evidence-as-data instruction; synthetic structural proof | do not claim universal model obedience |
| public-only reduces available corpus value | disclose bounded coverage in response/audit | reopen non-public access only with committed owner, schema, reader, revocation, and proof authority |
| no-provider response minimization could break UI count | consume existing audit paths or matched sources | reject if consumer cannot be migrated without new disclosure |
| audit path disclosure may itself be sensitive | audit only post-policy public paths in client response | return to reviewer if current audit contract mandates pre-policy protected paths |

## Finding-To-Governance Learning Disposition

| Field | Value |
|---|---|
| Finding class | RULE_GAP |
| Learning lane | GOVERNANCE_CONTROL_PLANE |
| Disposition | RULE_EXISTS |
| Evidence | The committed LPCI1-Web intake roadmap and LPCI1-WEB-D1 work order already govern these product conformance findings. No new repeated or non-obvious agent defect was observed. |
| Runtime/provider learning lane | N/A_WITH_REASON: this packet records a documentation design gap and performs no runtime or provider observation. |
| Next action | independent reviewer performs semantic acceptance and closure conversion; any later SPEC or BUILD requires a fresh operator checkpoint and governed packet. |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a minimized public-only snippet projection can restore bounded evidence grounding without selecting a nonexistent grant owner, while metadata-only abstention safely handles missing evidence.

Evidence Comparison: current source confirms snippets exist in matched records, the prompt omits them, the no-provider response exposes the receipt, client clearance affects filtering, and no grant owner is present. Those facts support the selected options and contradict any immediate general-access design.

Contradiction Or Gap Disposition: canonical T4 describes the full receipt as LLM context, while minimization requires a derived projection. This design records that conflict explicitly and selects the narrower provider-bound projection; a later SPEC must reconcile the contract before BUILD.

Claim Update: one bounded design is accepted only as a SPEC input; no runtime
conformance, evidence eligibility, durable audit correlation, or authorization
capability is claimed.

## Verification

Source verification used exact repository searches and bounded reads at execution base `8cf648301e0cdb17efb1692d937d5cd27bc3c262`. The mandated pre-implementation autorun gate passed before this file was created. No tests, provider calls, live calls, network actions, or runtime execution were performed.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private source/security design packet. No public-safe artifact or public-sync authority exists.

## Claim Boundary

This audit recommends documentation-only DESIGN for LPCI1-Web. It does not prove runtime behavior, implement a projection or authorization resolver, authorize non-public retrieval, create a grant owner, run tests or provider/live proof, or authorize SPEC, BUILD, persistence, vector/RAG, public-sync, push, or deployment.
