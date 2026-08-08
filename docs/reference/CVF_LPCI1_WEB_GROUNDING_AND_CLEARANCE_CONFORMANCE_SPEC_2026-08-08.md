# CVF LPCI1 Web Grounding And Clearance Conformance Specification

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

docType: reference

Date: 2026-08-08

Specification ID: LPCI1-WEB-S1

executionBaseHead: `88a3e6b2a`

## Purpose

Define the narrow LPCI1-Web query contract that permits evidence-grounded
answers from validated public index records while failing closed for every
non-public, malformed, ungrounded, mixed-escalation, or over-bound outcome.
This specification reconciles two existing LPCI1 contract conflicts without
implementing or proving runtime behavior.

## Scope / Applies To

This specification applies only to `POST /api/lpci/query`, its current LPCI1
filter/retrieval/audit helpers, and the current LPCI dashboard consumer. It does
not apply to LPCI2, generic retrieval, other Web routes, corpus intake,
persistence, vector or embedding search, RAG, provider selection, or public
surfaces.

The existing LPCI1-Web family remains the sole product owner. This document
creates no grant owner, entitlement store, durable audit store, or cross-owner
interface.

## Authority And Narrow Precedence

The authority chain is the committed LPCI1-WEB-S1 GC-018 baseline and work
order, the accepted bounded D1 design, and current LPCI T2, T3, and T4
contracts. Normative words `MUST`, `MUST NOT`, `SHOULD`, and `MAY` have their
ordinary requirements meaning.

This specification supplements T2, T3, and T4 and supersedes only the following
LPCI1-Web query statements:

1. T3's `contentSnippet` display-hint-only rule is narrowed: a snippet MAY be
   model evidence only when it passes every validation, public-admission,
   answer-boundary, serialization, and size rule in this specification. It is
   still not the full document, an adjudicated quotation, or proof of legal
   correctness.
2. T4's statement that the full `RetrievalReceipt` is passed to the LLM is
   replaced for this route by the derived allowlisted `modelEvidenceProjection`.
   The canonical internal receipt remains available to retrieval and audit
   logic and MUST NOT be sent to the provider or returned by the no-provider
   branch.
3. T4 C7's phrase "every query" means every authenticated, syntactically valid
   LPCI query request that reaches corpus evaluation. Authentication denial and
   invalid request bodies occur before LPCI audit construction.
4. T4 C9 preserves the canonical Phase 1 negative core fields at the response
   top level: `receiptType`, `query`, and optional `reason`. The route adds only
   its discriminant, audit, proof, and response-local correlation fields.
   Phase 2 remains uninvoked; no `phase1Receipt` nesting is permitted.

All other T2/T3/T4 answer class, freshness, conflict, no-legal-advice,
classification, and AuditReceipt obligations remain in force.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| answer classes | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 3-7 | `AnswerClass` | LPCI types | VALUE_SET | ACCEPT |
| record statuses | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 9-16 | `RecordStatus` | LPCI types | VALUE_SET | ACCEPT |
| snippet and sensitivity fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 33-50 | `contentSnippet`; `sensitivityLevel` | `LpciIndexRecord` | EXISTS | ACCEPT |
| client clearance field | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 52-58 | `sensitivityClearance` | `FilterParams` | EXISTS | ACCEPT |
| phase-one receipt values | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 31 and 65-69 | `Phase1ReceiptType` | LPCI types | VALUE_SET | ACCEPT |
| canonical audit fields | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | lines 94-109 | `AuditReceipt` | LPCI types | EXISTS | ACCEPT |
| unchecked JSON cast | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 17-25 | `loadCorpusIndex` | LPCI query route | RUNTIME_BEHAVIOR | ACCEPT |
| current classified-only filter | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.ts` | lines 14-28 and 109-120 | `applySensitivityFilter` | LPCI filter pipeline | RUNTIME_BEHAVIOR | ACCEPT |
| current mixed-answer precedence | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/retrieval.ts` | lines 15-31 and 93-122 | `mostRestrictiveAnswerClass` | LPCI retrieval pipeline | RUNTIME_BEHAVIOR | ACCEPT |
| current prompt and provider boundary | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 40-90 and 219-268 | `buildAnswerBoundaryPrompt` | LPCI query route | RUNTIME_BEHAVIOR | ACCEPT |
| current no-provider full receipt | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 189-216 | `retrievalReceipt` | LPCI query route | RUNTIME_BEHAVIOR | ACCEPT |
| audit copies supplied filters | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/audit-receipt.ts` | lines 32-74 | `buildAuditReceipt` | LPCI audit builder | RUNTIME_BEHAVIOR | ACCEPT |
| UI response consumer | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.tsx` | lines 17-26 and 127-207 | `QueryResult` | LPCI dashboard | RUNTIME_BEHAVIOR | ACCEPT |
| canonical sensitivity levels | `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md` | Sensitivity Classification (NR-06) | `sensitivityLevel` | LPCI T2 contract | VALUE_SET | ACCEPT |
| 512-character display hint | `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md` | Searchable Fields, lines 78-86 | `contentSnippet` | LPCI T3 contract | LITERAL_INVARIANT | ACCEPT |
| full-receipt context and audit schema | `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md` | RetrievalReceipt and AuditReceipt schemas | `RetrievalReceipt`; `AuditReceipt` | LPCI T4 contract | LITERAL_INVARIANT | ACCEPT |

## Existing Symbols And New Doc-Only Vocabulary

Existing runtime symbols are `AnswerClass`, `RecordStatus`,
`LpciIndexRecord`, `FilterParams`, `Phase1ReceiptType`, `RetrievalReceipt`,
`AuditReceipt`, `buildAnswerBoundaryPrompt`, `runFilterPipeline`,
`runRetrievalPipeline`, `buildAuditReceipt`, `RouteGovernanceProof`, and the UI
`QueryResult` interface.

The following are DOC_ONLY_NEW contract names and MUST NOT be claimed as current
runtime fields or types: `modelEvidenceProjection`, `evidenceEligibilityRule`,
`authorizationContext`, `authorizationDecision`, `grantEvidence`,
`noProviderProjection`, `auditCorrelation`, `syntheticProofMatrix`,
`GROUNDING_EVIDENCE_UNAVAILABLE`, `effectiveServerFilters`,
`routeResponseUnion`, `projectionLimits`, `outcome`, `evidenceOutcome`, the
top-level response copy `auditId`, and the response uses of
`authorizationDecision` and `corpusId`.

## Core Contract

The route MUST authenticate and validate before corpus work. It MUST perform
exact public-only sensitivity admission before search. It MUST preserve the
most-restrictive answer class before evidence assembly. It MUST call a provider
only when one to four final records all have valid, bounded evidence and the
complete serialized projection fits the aggregate byte limit.

No client value, authenticated role, service token, impersonated identity, or
generic team/scope MAY grant non-public LPCI access under this specification.

## Request Validation Requirements

| Input | Normative validation | Failure outcome |
|---|---|---|
| request body | MUST be a JSON object | `INVALID_REQUEST` |
| all accepted request string values | MUST contain only Unicode scalar values; any unpaired UTF-16 surrogate is forbidden before trimming, normalization, or serialization | `INVALID_REQUEST` |
| `query` | MUST be a scalar-valid string, trim to nonempty, and be at most 4096 UTF-8 bytes | `INVALID_REQUEST` |
| `corpusId` | MUST match `[A-Za-z0-9._-]+`, be nonempty, and be at most 128 ASCII bytes | `INVALID_REQUEST` |
| `filters` | MUST be absent or an object; unknown keys MUST be rejected | `INVALID_REQUEST` |
| `filters.status` | MUST be an array of unique exact `RecordStatus` values with at most seven entries | `INVALID_REQUEST` |
| string facet | `jurisdiction`, `documentType`, and `authorityLevel` MUST each be a nonblank string of at most 256 UTF-8 bytes | `INVALID_REQUEST` |
| `sensitivityClearance` | MAY be accepted for backward-compatible parsing but MUST be ignored for authority and normalized to `false` in effective filters | never elevates access |

Every UTF-8 byte limit in this request table is computed only after Unicode
scalar validation succeeds. This includes `query` and every request filter
string that can enter the shared exact serializer through response hashing or
`AuditReceipt.applied_filters`.

Authentication denial occurs before this table. `AUTHORIZATION_DENIED` and
`INVALID_REQUEST` MUST include `routeGovernanceProof` and MUST NOT create an
`AuditReceipt`, because no valid LPCI query execution exists.

## Index Runtime Validation Requirements

The current JSON cast is not validation. Index admission MUST be ordered so
that malformed non-public record details cannot influence, fail, or leak into
an otherwise valid public result.

First, the registered corpus index MUST load and parse as JSON whose root is an
array and whose every entry is a JSON object. A registered-index read/load
failure, invalid JSON, non-array root, or non-object array entry MUST return
`GROUNDING_EVIDENCE_UNAVAILABLE` with HTTP 200, the fixed safe message defined
below, a canonical `AuditReceipt`, empty `matched_paths`,
`sensitivity_pre_filter_applied:false`, and zero provider calls. The response
and audit MUST NOT expose a path, parser message, exception, or malformed
value.

Second, the route MUST inspect only `sensitivityLevel` across the object rows.
Missing sensitivity canonicalizes to `unknown`. A present value MUST already be
one of the exact lowercase strings `public`, `restricted`, `confidential`,
`classified`, or `unknown`; trimming, case folding, and type coercion are
forbidden. Any wrong type or noncanonical value fails the whole query closed as
`GROUNDING_EVIDENCE_UNAVAILABLE`, with empty `matched_paths`,
`sensitivity_pre_filter_applied:false`, and zero provider calls. No other field
of any row may be inspected for filtering, ranking, projection, audit paths, or
client output before this sensitivity-only pass succeeds.

Third, Stage 1 MUST admit exactly the rows whose canonical sensitivity is
`public`. All other rows are immediately excluded. Only the admitted public
rows are then validated for the remaining fields below before use:

| Field | Normative validation |
|---|---|
| `normalizedPath` | string; nonblank; relative forward-slash path; no empty, `.` or `..` segment; no control or NUL character; at most 1024 UTF-8 bytes |
| `status` | exact `RecordStatus` member: `effective`, `draft`, `amended`, `superseded`, `repealed`, `obsolete`, or `unknown` |
| `answerClass` | exact `AnswerClass` member |
| `effectiveDate` | required for model evidence; exact valid Gregorian `YYYY-MM-DD` date |
| `contentSnippet` | when present, string; model evidence form is outer-trimmed, nonblank, and at most 512 Unicode code points |
| `authorityLevel` | when present, nonblank string of at most 128 UTF-8 bytes because it drives ranking/conflict behavior |

An invalid admitted-public `normalizedPath`, status, answer class, date,
snippet type, or projection-driving authority value MUST fail the whole valid
query closed as `GROUNDING_EVIDENCE_UNAVAILABLE`. It MUST NOT be silently
coerced, truncated, dropped while other records answer, or allowed to reach a
provider. A missing or canonical non-public sensitivity is not malformed; it
is denied at Stage 1, and malformed fields other than sensitivity on that
excluded row MUST NOT influence the outcome or appear in audit/client output.

## Public-Only Authorization And Effective Filters

`authorizationDecision` is fixed to `PUBLIC_ONLY`. Stage 1 MUST admit only
records whose validated sensitivity is exactly `public`. Missing, `unknown`,
`restricted`, `confidential`, and `classified` records MUST be excluded before
fulltext search and MUST NOT contribute paths, snippets, freshness, conflicts,
audit matches, or provider context.

`effectiveServerFilters` MUST be a new server-computed `FilterParams` value
containing only validated status/jurisdiction/documentType/authorityLevel
filters and `sensitivityClearance: false`. The original client object MUST NOT
be copied into `AuditReceipt.applied_filters`. The route MUST construct and
normalize this value immediately after valid request parsing, before corpus
registration, index load, sensitivity processing, or any audited early return.
Every audited branch MUST use this same server-sanitized value as
`AuditReceipt.applied_filters`; its later application remains at the canonical
filter stage. Because mandatory Stage 1 ran,
`AuditReceipt.sensitivity_pre_filter_applied` MUST be `true` only after the
sensitivity-only pass and exact Stage 1 admission complete. It is `false` for
index load/container failures and invalid sensitivity shape/value; it is
`true` for every other valid, registered query outcome.

`authorizationContext` MAY contain current server-derived identity and exact
corpus identity for response-local correlation, but it MUST NOT be provider
evidence or entitlement. `grantEvidence` remains absent and parked.

## Ordered Eligibility And Fail-Close Protocol

The later runtime MUST use this order:

1. authenticate and emit route proof;
2. parse and validate request;
3. construct and normalize `effectiveServerFilters` without applying it;
4. verify corpus registration;
5. load and parse the registered index container;
6. validate and canonicalize only sensitivity shape/value across object rows;
7. apply exact public-only Stage 1 and immediately exclude every other row;
8. if no public row remains, return canonical `FILTERED_OUT`;
9. validate all remaining fields only on admitted public rows;
10. apply `effectiveServerFilters` through the canonical status, search,
    answer-class, and facet stages;
11. compute most-restrictive answer class across all final matched records;
12. if any final record is `ESCALATE_OR_ABSTAIN`, abstain with zero provider calls;
13. validate evidence eligibility for every final record;
14. enforce record-count and serialized-byte limits;
15. construct one deterministic projection and only then evaluate provider availability;
16. invoke the provider at most once or return the appropriate zero-call outcome;
17. construct canonical audit and the discriminated client envelope.

All-escalate results remain the Phase 1 `ESCALATED` receipt. Mixed direct plus
escalate results MUST return `ABSTAINED`; no filtering or projection step may
remove the restrictive record and downgrade the aggregate answer class.

After Stage 1, if no public records remain, the route returns the canonical
Phase 1 `FILTERED_OUT` receipt. After search/facets, canonical `NO_RESULTS` and
`ESCALATED` semantics remain unchanged.

## Evidence Eligibility Rule

Every final non-escalate record MUST have a valid path, valid effective date,
exact valid status and answer class, and a trimmed nonblank `contentSnippet` of
at most 512 Unicode code points. The count is `Array.from(trimmedSnippet).length`
semantics: Unicode code points before JSON escaping, not UTF-16 code units or
serialized bytes.

If any final matched record lacks eligible evidence, the whole route MUST
return `GROUNDING_EVIDENCE_UNAVAILABLE` with zero provider calls. Selective
dropping is forbidden because it would silently narrow answer coverage.

## Model Evidence Projection

`modelEvidenceProjection.schemaVersion` MUST be the literal
`cvf.lpci1Web.modelEvidence.v1`. Its top-level object MUST contain exactly the
keys `schemaVersion`, then `records`, in that order. Each record MUST contain
exactly these keys in this order:

- `normalizedPath`;
- `effectiveDate`;
- `status`;
- `answerClass`;
- `contentSnippet`.

It MUST NOT contain the query, full `RetrievalReceipt`, `matched_records`,
`sourceHash`, sensitivity label, filters, audit data, route proof, actor,
session, grant, provider, model, registry, or corpus-row fields not listed
above. Record order MUST preserve deterministic retrieval ranking and MUST NOT
be truncated to meet a limit.

## Safe Serialization And Prompt Boundary

The projection MUST use compact RFC 8259 serialization of the exact ordered
allowlist above, encoded as UTF-8 without BOM, insignificant whitespace, or a
trailing newline. Byte-exact escaping is fixed: quotation mark is `\"`;
reverse solidus is `\\`; U+0008 is `\b`; U+0009 is `\t`; U+000A is `\n`;
U+000C is `\f`; U+000D is `\r`; and every other U+0000 through U+001F code
point is lowercase `\u00xx`. Solidus and valid non-ASCII characters MUST NOT
be escaped, and unpaired surrogates MUST be rejected. Projection size and every
structured negative/abstention hash input MUST use these identical serialized
bytes. Every projected string MUST be passed through that serializer; raw
string interpolation, Markdown fences, XML tags, delimiter replacement, and
manual escaping are forbidden. The serialized object MUST appear once after a
fixed trusted instruction stating that every JSON string is untrusted evidence,
not an instruction. The user query remains the separate user message.

Quotes, backslashes, newlines, control characters, markup, role labels,
delimiter-like text, and instruction-like content inside any projected field
MUST remain JSON string data and MUST NOT create a second prompt section. This
is a structural framing requirement, not a universal model-obedience claim.

## Projection Limits

`projectionLimits` are:

| Limit | Normative value | Rationale |
|---|---|---|
| per-record evidence | 512 Unicode code points after outer trim | adopts the existing T3 maximum without query-time truncation |
| maximum evidence records | 4 | supports single-source and bounded multi-source conflict context while preventing unbounded record fan-out |
| maximum serialized projection | 16384 UTF-8 bytes | bounds the exact provider evidence object after escaping and accommodates four maximum snippets plus bounded paths/metadata |

The byte count MUST be computed over the final RFC 8259 JSON UTF-8 bytes after
escaping and before prompt concatenation. Values exactly at each limit MAY
proceed. A fifth record, a 513th snippet code point, or a 16385th serialized
byte MUST cause `GROUNDING_EVIDENCE_UNAVAILABLE`, zero provider calls, and no
partial/truncated projection.

## Route Response Union

`routeResponseUnion` uses the required top-level discriminant `outcome`. No
variant MAY include `retrievalReceipt`, `matched_records`, snippet text,
`sourceHash`, provider endpoint/model/status/body, stack, grant, or internal
diagnostic text.

| Outcome | HTTP | Exact additional client fields | Audit boundary |
|---|---:|---|---|
| `AUTHORIZATION_DENIED` | 401 | fixed safe `message`; `routeGovernanceProof` | no `AuditReceipt` |
| `INVALID_REQUEST` | 400 | fixed safe `message`; `routeGovernanceProof` | no `AuditReceipt` |
| `CORPUS_NOT_REGISTERED` | 403 | fixed safe `message`; `query`; `corpusId`; `auditId`; `authorizationDecision`; `evidenceOutcome`; `auditReceipt`; `routeGovernanceProof` | post-validation negative audit |
| `PHASE1_NEGATIVE` | 200 | top-level `receiptType`; `query`; optional `reason`; `corpusId`; `auditId`; `authorizationDecision`; `evidenceOutcome`; `auditReceipt`; `routeGovernanceProof` | `phase1_receipt_type` required |
| `ABSTAINED` | 200 | fixed bounded `response`; `query`; `corpusId`; `answerClass`; `auditId`; `authorizationDecision`; `evidenceOutcome`; `auditReceipt`; `routeGovernanceProof` | `ABSTAINED` audit |
| `GROUNDING_EVIDENCE_UNAVAILABLE` | 200 | fixed safe `message`; `query`; `corpusId`; `auditId`; `authorizationDecision`; `evidenceOutcome`; `auditReceipt`; `routeGovernanceProof` | route-level negative; no phase-one type |
| `NO_PROVIDER_CONFIGURED` | 200 | fixed safe `message`; `query`; `corpusId`; `auditId`; `authorizationDecision`; `evidenceOutcome`; `auditReceipt`; `routeGovernanceProof` | route-level negative; no phase-one type |
| `PROVIDER_ERROR` | 502 | fixed safe `message`; `query`; `corpusId`; `auditId`; `authorizationDecision`; `evidenceOutcome`; `auditReceipt`; `routeGovernanceProof` | route-level negative; no phase-one type |
| `ANSWER_EMITTED` | 200 | `response`; `query`; `corpusId`; `answerClass`; `matchedSources`; `freshnessFlag`; `conflictFlag`; `auditId`; `authorizationDecision`; `evidenceOutcome`; `auditReceipt`; `routeGovernanceProof` | `ANSWER_EMITTED` audit |

For `PHASE1_NEGATIVE`, top-level `receiptType` MUST be the exact canonical
`Phase1ReceiptType`, top-level `query` and optional `reason` MUST retain the
canonical Phase 1 values, and `auditReceipt.phase1_receipt_type` MUST equal
top-level `receiptType`. A consumer that reads those three canonical top-level
fields requires no compatibility translation.

The fixed provider-error client message MUST be exactly:

`The answer provider is temporarily unavailable.`

The other fixed safe messages MUST be exactly:

- `CORPUS_NOT_REGISTERED`: `The requested corpus is not available for LPCI query.`
- `GROUNDING_EVIDENCE_UNAVAILABLE`: `Grounding evidence is unavailable for this query.`
- `NO_PROVIDER_CONFIGURED`: `No answer provider is configured.`

Raw provider status, body, endpoint, model, exception, stack, latency, and
diagnostic detail MUST remain server-internal and secret-safe. This SPEC does
not select persistence for such diagnostics.

## No-Provider Projection

`noProviderProjection` is the `NO_PROVIDER_CONFIGURED` variant above. It MUST
contain no full retrieval receipt or evidence. The UI MUST derive its matched
source count from `auditReceipt.matched_paths.length`; `matchedSources` is not
required on this variant. Provider-call count is zero.

## AuditReceipt And Response-Local Correlation

The canonical `AuditReceipt` type and mandatory fields remain unchanged. The
route MUST retain `model_response_hash`, `applied_filters`, and
`sensitivity_pre_filter_applied`. It MUST use `effectiveServerFilters`, never
the raw client filters.

For `ANSWER_EMITTED`, `model_response_hash` is SHA-256 of the exact emitted
response text. Every audited negative or abstention uses the compact RFC 8259
UTF-8 serializer defined above and hashes exactly the following ordered object,
with no additional key:

| Outcome | Exact ordered hash-input keys |
|---|---|
| `CORPUS_NOT_REGISTERED` | `outcome`, `query`, `corpusId`, `authorizationDecision`, `evidenceOutcome`, `message` |
| `PHASE1_NEGATIVE` | `outcome`, `receiptType`, `query`, optional `reason`, `corpusId`, `authorizationDecision`, `evidenceOutcome` |
| `ABSTAINED` | `outcome`, `response`, `query`, `corpusId`, `answerClass`, `authorizationDecision`, `evidenceOutcome` |
| `GROUNDING_EVIDENCE_UNAVAILABLE` | `outcome`, `query`, `corpusId`, `authorizationDecision`, `evidenceOutcome`, `message` |
| `NO_PROVIDER_CONFIGURED` | `outcome`, `query`, `corpusId`, `authorizationDecision`, `evidenceOutcome`, `message` |
| `PROVIDER_ERROR` | `outcome`, `query`, `corpusId`, `authorizationDecision`, `evidenceOutcome`, `message` |

The optional `reason` key is omitted, not serialized as null, when absent.
`auditId`, `auditReceipt`, and `routeGovernanceProof` are never hash inputs.
Only `PHASE1_NEGATIVE` sets `phase1_receipt_type`.

For every audited variant, the response-local correlation invariant is exact:
top-level `auditId === auditReceipt.auditId`;
`routeGovernanceProof.actorId` and `routeGovernanceProof.authMode` are the
authenticated values for the same request; top-level `corpusId` is the exact
validated request corpus ID; and `authorizationDecision` is exactly
`PUBLIC_ONLY`. `evidenceOutcome` MUST map as follows:

| Route outcome | Exact `evidenceOutcome` | Exact `AuditReceipt.response_boundary_class` |
|---|---|---|
| `CORPUS_NOT_REGISTERED` | `NOT_EVALUATED` | `NEGATIVE_RECEIPT` |
| Phase 1 `NO_RESULTS` | `NO_MATCHES` | `NEGATIVE_RECEIPT` |
| Phase 1 `FILTERED_OUT` | `FILTERED_PUBLIC_ONLY` | `NEGATIVE_RECEIPT` |
| Phase 1 `ESCALATED` | `ABSTAINED` | `NEGATIVE_RECEIPT` |
| `ABSTAINED` | `ABSTAINED` | `ABSTAINED` |
| `GROUNDING_EVIDENCE_UNAVAILABLE` | `UNAVAILABLE` | `NEGATIVE_RECEIPT` |
| `NO_PROVIDER_CONFIGURED` | `ELIGIBLE_NOT_SENT` | `NEGATIVE_RECEIPT` |
| `PROVIDER_ERROR` | `PROVIDER_FAILED` | `NEGATIVE_RECEIPT` |
| `ANSWER_EMITTED` | `ANSWER_EMITTED` | `ANSWER_EMITTED` |

Matched-path correlation is also exact. Every failure before search produces
`auditReceipt.matched_paths: []`. This includes corpus-not-registered,
container failures, invalid sensitivity, no-public Phase 1 `FILTERED_OUT`, and
validation failure in any admitted public row. Phase 1 `NO_RESULTS` and
`ESCALATED` also use an empty list. Abstention uses exactly the final public
search/facet match paths. A grounding failure after search/facet matching uses
exactly those final public match paths. No-provider, provider-error, and answer
variants use exactly the projection record paths in projection order.
`ANSWER_EMITTED.matchedSources` MUST equal `auditReceipt.matched_paths`.

This response-local invariant introduces no new durable object. The audit
schema does not acquire actor, corpus, grant, provider, or model fields, and no
stored authorization correlation is claimed.

## Rejection Criteria

A later BUILD packet MUST be rejected if it:

- treats TypeScript casting as runtime validation;
- sends a full receipt or non-allowlisted field to the provider/client;
- trusts client clearance, a role, service token, or impersonation as a grant;
- admits missing, unknown, restricted, confidential, or classified evidence;
- drops an escalate record or ineligible final match to produce an answer;
- truncates records/snippets or exceeds any selected bound;
- manually interpolates any evidence field;
- exposes raw provider diagnostics;
- omits canonical audit fields or copies raw client filters;
- claims durable audit correlation, non-public authorization, provider quality,
  live behavior, persistence, vector/RAG, or readiness.

## Threat Matrix

| Threat | Required outcome |
|---|---|
| forged client clearance true | same public-only decision/effective filters as false |
| missing/unknown/non-public sensitivity only | `FILTERED_OUT`; zero provider calls |
| mixed public and non-public | only public records reach search, receipt, audit matches, and projection |
| malformed sensitivity shape/value | `GROUNDING_EVIDENCE_UNAVAILABLE`; empty audit paths; pre-filter flag false; zero calls |
| malformed admitted-public enum/type/date/path/class | `GROUNDING_EVIDENCE_UNAVAILABLE`; zero calls |
| malformed nonsensitivity field on an excluded non-public row | cannot influence outcome or appear in audit/client output |
| registered-index load/JSON/container failure | minimized `GROUNDING_EVIDENCE_UNAVAILABLE`; empty audit paths; zero calls; no diagnostic detail |
| blank or oversized evidence | `GROUNDING_EVIDENCE_UNAVAILABLE`; zero calls |
| injection in any projected field | one valid JSON evidence object; data cannot create a second section |
| fifth record or aggregate overflow | `GROUNDING_EVIDENCE_UNAVAILABLE`; zero calls; no truncation |
| mixed direct and escalate | `ABSTAINED`; zero calls |
| service identity without grant | public-only |
| impersonated session | public-only; route proof remains identity evidence only |
| cross-corpus grant assertion | ignored; public-only |
| no provider | minimized `NO_PROVIDER_CONFIGURED`; zero calls |
| provider failure | fixed safe message; one attempted call maximum; no raw diagnostics |
| auth denial | 401 route proof only; no LPCI audit |
| invalid request JSON/body | 400 route proof only; no LPCI audit |
| unpaired surrogate in query or any accepted request string | 400 `INVALID_REQUEST`; route proof only; no LPCI audit/provider call |
| response shape confusion | exactly one `outcome` variant and its allowlist |

## Synthetic Acceptance Cases

`syntheticProofMatrix` defines later tests only. No test is executed by S1.

| ID | Fixture | Required assertions |
|---|---|---|
| P1 | one valid public effective direct record, 1-code-point snippet | one provider call; literal schema version; exact ordered top-level and five-field record allowlists; `ANSWER_EMITTED`; complete correlation invariant |
| P2 | four valid public records, each 512 code points, serialized projection exactly 16384 bytes or less | one call; deterministic compact RFC 8259 UTF-8 golden bytes; no BOM, whitespace, trailing newline, or unlisted field |
| P3 | valid public record with no provider | zero calls; no retrieval receipt; UI count equals audit matched paths |
| P4 | clearance false then true with identical request | byte-equivalent authorization outcome and `sensitivityClearance:false` effective filters |
| P5 | mixed public and canonical non-public records, with malformed nonsensitivity fields on a non-public row | public-only projection/audit paths; malformed excluded fields do not change outcome and no protected path, text, or diagnostic appears |
| P6 | each canonical Phase 1 negative receipt | `receiptType`, `query`, and optional `reason` remain top-level and byte-compatible for a consumer reading those core fields; additive outcome/audit/proof/correlation only; no `phase1Receipt` |
| P7 | each audited response variant | exact audit ID, actor/auth mode, corpus, public-only decision, outcome mapping, and matched-path equalities hold |
| P8 | each audited negative with escaping-sensitive strings | SHA-256 input equals the exact ordered compact JSON bytes specified above; omitted Phase 1 reason is absent, not null |
| F1 | missing, blank, or 513-code-point snippet in a final match | grounding unavailable; zero calls; no selective answer |
| F2 | invalid sensitivity type/value in any row | HTTP 200 grounding unavailable; empty audit paths; pre-filter flag false; zero calls; no other field from that row is inspected or exposed |
| F3 | all records missing/unknown/restricted/confidential/classified | Phase 1 filtered out; zero calls |
| F4 | one direct plus one escalate final match | abstained; zero calls; most-restrictive class retained |
| F5 | path/date/status/class/snippet contains quote, newline, backslash, markup, delimiter, role label, or instruction text | parseable single JSON object; no second structural prompt block |
| F6 | five eligible records | grounding unavailable; zero calls; no first-four truncation |
| F7 | final serialized projection is 16385 UTF-8 bytes | grounding unavailable; zero calls |
| F8 | provider returns status/body/stack-like text | 502 fixed safe message only; audit hash matches safe payload |
| F9 | authentication denial | 401; route proof; no audit/provider call |
| F10 | invalid JSON or missing required request field after auth | 400; route proof; no audit/provider call |
| F11 | service token, impersonation, or cross-corpus grant-shaped input | public-only; no non-public admission |
| F12 | each response branch | exact outcome allowlist; forbidden fields absent |
| F13 | registered index read/load failure, invalid JSON, non-array root, or non-object array entry | HTTP 200 grounding unavailable with exact fixed message/allowlist, canonical audit, empty paths, pre-filter flag false, zero calls, and no parser/path/value diagnostic |
| F14 | admitted public row with invalid status, answer class, date, path, snippet type, or authority shape | HTTP 200 grounding unavailable; `auditReceipt.matched_paths: []`; zero calls; no selective answer or pre-search path disclosure |
| F15 | projection contains solidus, non-ASCII text, control characters, or an unpaired surrogate | solidus/non-ASCII follow the exact serialization policy; controls are JSON escaped; unpaired surrogate fails grounding closed with zero calls |
| F16 | query or any request filter string contains a leading, embedded, or trailing unpaired surrogate | 400 `INVALID_REQUEST` before trim/UTF-8 count; route proof; no LPCI audit/provider call |

## Later-Build Candidate Manifest

The following are candidates only. A fresh operator checkpoint, GC-018,
source-verified work order, current base, and deterministic test authorization
are required before any edit or execution.

| Candidate path | Candidate responsibility | Current authority |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | validated sensitivity/projection/response types | FORBIDDEN |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.ts` | public-only Stage 1 and effective filters | FORBIDDEN |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/retrieval.ts` | fail-close ordering and bounded final set | FORBIDDEN |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/audit-receipt.ts` | canonical audit/hash inputs | FORBIDDEN |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | validation, projection, envelopes, minimization, safe provider error | FORBIDDEN |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.tsx` | discriminated consumer and audit-path count | FORBIDDEN |
| existing same-family LPCI tests | synthetic cases P1-P5 and F1-F12 | FORBIDDEN |

No persistence, vector store, embedding/RAG service, provider adapter, grant
database, new entitlement owner, production corpus, or cross-owner route is a
candidate in this specification.

## Requirements Summary

Implementations conform only when every MUST/MUST NOT rule, response variant,
limit, audit obligation, and synthetic case in this document is satisfied.
Partial projection, permissive fallback, or undocumented response variants are
non-conformant.

## Enforcement / Verification

S1 verification is documentation-only: current source reads, canonical
contract comparison, worker-return governance gates, Git status/diff evidence,
and independent reviewer inspection. Runtime validation, route/unit/E2E tests,
provider calls, live proof, benchmarks, and deployment verification are N/A
with reason: the work order forbids execution and implementation.

## Finding-To-Governance Learning Disposition

| Field | Value |
|---|---|
| Defect class | RULE_GAP |
| Learning lane | GOVERNANCE_CONTROL_PLANE |
| Disposition | RULE_EXISTS |
| Evidence | The LPCI current-owner intake roadmap and accepted D1 design already own the product conformance gap; S1 resolves its bounded specification questions. |
| Runtime/provider learning | N/A_WITH_REASON: S1 performs no runtime or provider observation. |
| Next action | independent reviewer accepts or returns this SPEC; BUILD remains a fresh operator checkpoint. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_worker_experience_retrospective.py` |
| literalTokensReviewed | reference structural headings; source-table Source fact type; evidence-heavy epistemic fields; finding disposition and next action; public disposition; ASCII and file-size boundaries |
| gateRunPurpose | validate exact documentation structure and claims after source-backed normative authoring |
| claimBoundary | LPCI1-WEB-S1 private documentation-only specification |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated LPCI1-WEB-S1 specification worker |
| Provider or surface | local private provenance repository |
| Session or invocation | `lpci1-web-s1-spec-worker-2026-08-08` |
| Working directory | repository root `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | governed source/checker reads, ADIF resolver, pre-implementation autorun, `apply_patch`, worker-return fast gate, `git diff --check`, Git status/diff evidence |
| Target paths | reference SPEC and paired worker return |
| Allowed scope source | committed LPCI1-WEB-S1 work order at `88a3e6b2a` |
| Before status evidence | HEAD `88a3e6b2a`; initial status empty |
| After status evidence | exact two untracked documentation outputs; no staged path |
| Diff evidence | `git diff --name-status` plus untracked-aware `git status --short --untracked-files=all` |
| Approval boundary | documentation-only SPEC |
| Claim boundary | no BUILD/runtime/test/provider/live/persistence/vector-RAG/corpus/public/deployment action |
| Agent type | no-commit specification worker |
| Invocation ID | `lpci1-web-s1-spec-worker-2026-08-08` |
| Expected manifest | `docs/reference/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_2026-08-08.md`; `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_WORKER_RETURN_2026-08-08.md` |
| Actual changed set | `docs/reference/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_2026-08-08.md`; `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_WORKER_RETURN_2026-08-08.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a narrow public-only companion specification can
ratify bounded snippets as route-specific evidence, replace full provider
receipt context, and remain independent of any non-public grant owner.

Evidence Comparison: current source confirms unchecked JSON casts,
client-controlled classified filtering, metadata-only prompting, full
no-provider receipts, raw-derived provider errors, canonical audit fields, and
mixed-answer precedence. T3 and T4 provide contrary display-hint and full-context
wording, resolved only through the narrow precedence section above.

Contradiction Or Gap Disposition: finite limits, exact response variants,
invalid-body audit treatment, and provider-error text are resolved normatively.
Non-public grants and durable correlation remain parked rather than invented.

Claim Update: one complete normative SPEC is pending independent review; no
runtime conformance or readiness is claimed.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private security/conformance specification with no public-safe packet
or public-sync authority.

## Claim Boundary

This document is a private documentation-only specification. It does not edit
or execute runtime/tests, prove model grounding or authorization enforcement,
authorize non-public retrieval, select a provider/model/key, create storage,
persistence, vector/RAG, grants, public artifacts, deployment, or readiness.
Any BUILD or execution requires fresh explicit operator authority and a new
governed packet.

## Related Artifacts

- `docs/baselines/CVF_GC018_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_2026-08-08.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_2026-08-08.md`
- `docs/audits/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_DESIGN_2026-08-08.md`
- `docs/reference/CVF_LPCI1_T2_DOMAIN_CLASSIFICATION_SPEC_2026-06-03.md`
- `docs/reference/CVF_LPCI1_T3_SEARCH_FILTER_INDEX_SPEC_2026-06-03.md`
- `docs/reference/CVF_LPCI1_T4_RETRIEVAL_BOUNDARY_SPEC_2026-06-03.md`
