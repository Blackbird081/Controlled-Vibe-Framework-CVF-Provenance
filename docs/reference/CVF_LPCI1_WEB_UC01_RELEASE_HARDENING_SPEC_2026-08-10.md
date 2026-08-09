# CVF LPCI1 Web UC-01 Release Hardening Specification

Memory class: governed-reference

Status: SPEC_ACCEPTED_BOUNDED_WITH_R1_CORRECTIONS

Date: 2026-08-10

docType: spec

Batch ID: LPCI1-WEB-UC01-RELEASE-HARDENING-DESIGN-SPEC

## Purpose

Define the normative, finite acceptance contract for a future UC-01 release
hardening BUILD. This specification is documentation only and is not runtime or
release evidence.

## Scope / Applies To

This specification applies to the authenticated `POST /api/lpci/query`
composition, its existing route-governance proof, LPCI provider binding and
Model Gateway path, rate-limit backend, control-plane event store, system-health
projection, and future release operations. It does not apply to other query,
execute, provider, or public routes.

## Owner And Source Lineage

| Concern | Current owner | Future composition interface | Status |
|---|---|---|---|
| request authorization | `authorizeRouteGovernanceProof` and middleware-auth | `releaseRolePolicy` | DOC_ONLY_NEW interface over CURRENT_SOURCE owner |
| model execution | `executeLpciProviderBinding` and Model Gateway bridge | existing binding plus `providerAttemptTimeout` | timeout is DOC_ONLY_NEW |
| query/provider quota | `getRateLimiter`, `RateLimitStore`, Redis backend status | `queryQuotaPolicy` | DOC_ONLY_NEW interface over CURRENT_SOURCE owner |
| response receipt | `buildAuditReceipt` | unchanged response receipt | CURRENT_SOURCE |
| durable evidence | `appendAuditEvent`, `EventListAdapter`, SIEM forwarder | `durableAuditProjection` plus atomic append/probe/expiry on the same adapter owner | DOC_ONLY_NEW projector and owner extension |
| readiness | `getSystemHealth` | `releaseHealthContract` | DOC_ONLY_NEW UC-01 projection |
| configuration | current LPCI config resolver and credential boundary | `hostedConfigLifecycle` | DOC_ONLY_NEW hosted lifecycle |
| promotion/recovery | platform build carriers and operator process | `promotionRollbackContract` | DOC_ONLY_NEW operations contract |

No future BUILD may introduce a parallel generic authorization, provider,
limiter, audit, storage, or health owner. Narrow UC-01 composition modules MUST
delegate to the owners above.

## Contract Requirements

### R1 - Ordered fail-closed composition

The query route MUST preserve the order: route proof -> role/service policy ->
parse/validate -> distributed query quota -> corpus/retrieval -> release health
and atomic config -> provider-attempt quota -> one provider attempt -> response
receipt -> synchronous durable audit -> response.

Every failed stage MUST prevent all later functional stages. The terminal audit
stage remains mandatory for authorization, role-policy, and parse denial and
receives only server-generated invocation metadata for those early paths.
Pre-binding negative outcomes MUST NOT consume provider-attempt quota or enter
the bridge. Audit persistence MUST precede delivery of every terminal response.

### R2 - Role and service identity admission

| Auth mode | Presented identity | Admission | Required identity key | Failure |
|---|---|---|---|---|
| session | canonical owner/admin/developer/reviewer/viewer | ALLOW | hash of verified effective session actor plus role class | N/A |
| session | missing or noncanonical role | DENY | none | 403 `ROLE_NOT_ALLOWED` |
| service token | signature valid and derived actor hash is allowlisted for `lpci-query` | ALLOW | hash of registered service identity | N/A |
| service token | valid global token but actor not purpose-allowlisted | DENY | none | 403 `SERVICE_IDENTITY_NOT_ALLOWED` |
| either | invalid/absent proof | DENY | none | existing 401 authorization response |

`releaseRolePolicy` is DOC_ONLY_NEW. It MUST normalize only against the current
`TeamRole` vocabulary. Client body, query string, or headers MUST NOT assign a
role or service purpose. Impersonation MUST use the effective role; durable
evidence MUST NOT expose real or impersonated actor IDs.

### R3 - Atomic configuration lifecycle

| State | Three-key condition | Provider lane | Health state |
|---|---|---|---|
| `ABSENT` | no hosted bundle version | BLOCK | `STATIC_BLOCKED_CONFIG` |
| `PARTIAL` | one or two names available, or versions differ | BLOCK | `STATIC_BLOCKED_CONFIG` |
| `INVALID` | blank/trim-empty key metadata, noncanonical model/endpoint, or invalid bundle metadata | BLOCK | `STATIC_BLOCKED_CONFIG` |
| `ROTATION_PENDING` | candidate exists but is not atomically promoted | BLOCK candidate; retain accepted active version | active version determines readiness |
| `READY` | one immutable version has all three valid names | ALLOW after remaining checks | continue evaluation |

`hostedConfigLifecycle` is DOC_ONLY_NEW. Hosted release MUST explicitly set
`LPCI_LLM_API_KEY`, `LPCI_LLM_MODEL=openai/gpt-4o`, and
`LPCI_LLM_ENDPOINT=https://api.openai.com/v1/chat/completions` as one versioned
bundle. The source-level optional endpoint default MAY remain for local
compatibility but MUST NOT satisfy hosted readiness.

The API key MUST be read only by the existing credential boundary/adapter. All
other checks MUST use metadata availability and MUST treat trim-empty as
unavailable. Raw secret, secret length, prefix/suffix, fingerprint, secret-store
identifier, secret version, and secret-derived rotation metadata MUST NOT enter
logs, receipts, UI, or tests.

Rotation MUST create, validate, and promote a complete new bundle atomically.
On failure it MUST retain or restore the complete prior version. A mixed-version
bundle and single-variable rollback are forbidden.

Promotion receipts MAY include an opaque non-secret config bundle version,
schema version, and digest. The digest MUST cover only schema plus non-secret
model/endpoint configuration and MUST exclude the key, credential metadata,
secret version, and secret-store identity. These fields exist only for
artifact/config correlation and MUST NOT be usable as a secret fingerprint.

### R4 - Distributed query and provider-attempt quota

`queryQuotaPolicy` is DOC_ONLY_NEW and MUST reuse the existing limiter stores
and backend-status contract. Hosted mode MUST require
`configurationStatus=ACTIVE_REDIS_REST` and `distributed=true`. Memory mode is
allowed only in deterministic local tests and MUST report non-release status.

| Stage | Key | Consume condition | Denial behavior |
|---|---|---|---|
| query admission | `lpci:query:<identityKind>:<identityHash>` | once after valid request parsing | 429 with bounded retry-after; no retrieval/provider |
| provider attempt | query key plus `openai/gpt-4o` | once immediately before bridge entry | 429 with bounded retry-after; bridge count zero |

Thresholds MUST be positive finite integers supplied by release-owned server
configuration. Missing, invalid, unsupported, non-distributed hosted backend,
ambiguous identity, or store error MUST fail closed. IP address MUST NOT replace
authenticated identity. Provider-attempt consumption MUST NOT consume the query
counter a second time.

### R5 - Durable minimized audit and server telemetry

`durableAuditProjection` is DOC_ONLY_NEW. It MUST call the existing
`appendAuditEvent` owner with event type `LPCI_QUERY_TERMINAL` and MUST await the
durable append before returning a response. The current `EventListAdapter`
remains the sole storage interface. Its future BUILD extension MUST provide an
atomic distributed append, a static capability descriptor, and per-record
30-day expiry. File and SQLite remain local-only; the current Redis stub MUST
produce a static blocked-capability state until that same adapter owner is
implemented and tested. External store liveness remains outside static health.

Allowed durable fields:

| Field | Rule |
|---|---|
| schemaVersion | fixed version literal |
| invocationId/auditId/traceId | server-generated identifiers; later two may be absent on early denial |
| timestamp/routeId | server-generated time and fixed route |
| authMode/roleClass | normalized class only |
| actorRef | one-way hash of verified identity, never raw identity |
| outcome/httpStatus | finite route outcome and status |
| corpusRef | one-way hash of corpus ID |
| responseBoundaryClass | existing bounded enum when available |
| providerId/modelId | only when an attempt was selected; exact configured pair |
| queryQuota/providerQuota | allow/deny plus safe retry-after bucket |
| providerAttemptCount | `0` or `1` only |
| timeoutFlag/diagnosticCode | safe finite fields |
| latencyBucket | coarse bucket, not raw timeline |

Prohibited durable, log, metric, and UI fields: raw query, system prompt, answer,
matched paths, provider payload/body, request/response body, headers, cookies,
tokens, API keys, credential or secret metadata, stack traces, raw actor ID, and
raw corpus ID.

The control-plane evidence owner MUST enforce 30-day retention and audit/security
administrator access for this event class. Aggregated server telemetry MAY emit
counts and coarse latency buckets by route, outcome, diagnostic code, and exact
provider/model pair. Telemetry MUST NOT substitute for the durable append. An
append failure MUST yield 503 `AUDIT_UNAVAILABLE`, MUST NOT deliver a pending
answer, and MUST NOT retry the provider. SIEM forwarding failure MAY be
separately counted after a successful append.

### R6 - Provider timeout and retry

`providerAttemptTimeout` is DOC_ONLY_NEW and MUST equal 30,000 ms. Current
`ProviderExecutionAdapterInput` and `OpenAiCompatibleFetch` init have no signal.
The future BUILD MUST extend the existing bridge execute option with
`signal?: AbortSignal`, forward the same signal into
`ProviderExecutionAdapterInput`, and include it in the OpenAI-compatible fetch
init. LPCI MUST create one controller, schedule one abort, pass the signal
through the bridge, and clear the timer on settlement. A `Promise.race` without
actual request cancellation MUST fail acceptance. The request MUST have at most
one bridge entry, at most one adapter/network entry, zero automatic retries,
zero hedges, zero provider fallback, and zero model fallback.

| Failure | HTTP | Public message | Durable diagnostic |
|---|---:|---|---|
| deadline exceeded | 504 | The answer provider is temporarily unavailable. | `PROVIDER_TIMEOUT` |
| bridge/adapter error | 502 | The answer provider is temporarily unavailable. | `PROVIDER_ERROR` |
| wrong provider/model response or receipt | 502 | The answer provider is temporarily unavailable. | `EXACT_PAIR_MISMATCH` |
| configuration unavailable | 503 | No answer provider is configured. | `NO_PROVIDER_CONFIGURED` |

No safe public message may contain provider body, endpoint detail, credential
state, stack trace, or internal policy reason.

### R7 - Side-effect-free release health

`releaseHealthContract` is DOC_ONLY_NEW. Evaluation MUST read only static
policy/version metadata, safe config metadata, limiter backend configuration
and implementation capability, audit-adapter configuration and implementation
capability, route-composition version, and Model Gateway registry/capability
metadata. It MUST NOT claim Redis liveness, evidence-store writability, or
provider liveness. It MUST NOT parse a user query, consume a quota counter,
append an event, resolve raw credentials, invoke the bridge/adapter, or perform
any network call.

| Priority | Failed dependency | State | Safe operator action |
|---:|---|---|---|
| 1 | auth policy metadata missing/stale | `STATIC_BLOCKED_AUTH_POLICY` | restore accepted policy version |
| 2 | atomic config metadata not ready | `STATIC_BLOCKED_CONFIG` | restore/promote one complete bundle |
| 3 | distributed limiter config/implementation capability absent | `STATIC_BLOCKED_LIMITER_CAPABILITY` | restore accepted distributed adapter configuration/code |
| 4 | durable audit config/implementation capability absent | `STATIC_BLOCKED_AUDIT_CAPABILITY` | restore accepted evidence adapter configuration/code |
| 5 | route composition version mismatch | `STATIC_BLOCKED_ROUTE_COMPOSITION` | deploy accepted route artifact under fresh authority |
| 6 | exact Model Gateway registry capability absent | `STATIC_BLOCKED_PROVIDER_CAPABILITY` | restore accepted registry/binding artifact |
| 7 | none | `STATIC_READY` | static prerequisites only; external liveness remains unproven |

The first failing static dependency wins. Health MUST return no secret presence
detail, identity material, quota key, endpoint, or provider request data.
Redis/store/provider liveness and store writability require a separately
authorized hosted smoke or operational-monitoring signal and MUST NOT be
inferred from `STATIC_READY`.

### R8 - Promotion, smoke, rollback, recovery, and migration

Promotion MUST proceed development -> preview -> staging -> production. Each
boundary MUST bind an immutable artifact digest, opaque non-secret config bundle
version, policy/composition schema versions, deterministic test receipt, and
side-effect-free `STATIC_READY` receipt. Production promotion MUST NOT inherit
authority from a lower environment.

Deterministic smoke MUST use injected stores, clock, identities, adapter, abort,
and event sink. It MUST make no provider or external call. A hosted smoke needs
fresh hosted authority. A provider/live smoke needs fresh live authority after
BUILD acceptance and MUST preserve the separately dispatched call/retry budget.

Rollback MUST trigger on any of: non-ready dependency, authorization bypass,
distributed quota bypass/unavailability, durable append failure, exact-pair
mismatch, provider timeout/error threshold breach, or smoke mismatch. Release
operator owns the decision; platform operations restores the last accepted
artifact and complete configuration bundle; application owner verifies health,
audit, and deterministic smoke. Rollback MUST NOT disable authorization, quota,
audit, timeout, exact-pair, or health controls.

Recovery MUST record a secret-safe cause, repair one governed owner, rerun all
deterministic cases, obtain fresh promotion authority, and generate a new smoke
receipt. Existing response-local audit receipts remain historical evidence and
MUST NOT be backfilled. New durable schema versions MUST remain readable for the
30-day retention window. No current database or provider/model migration is
authorized.

## UI Information Boundary

A future UI MAY show only: `Ready`, `Temporarily unavailable`, `Rate limited`,
`Authorization required`, or `Configuration required`, plus a concise recovery
action and trace ID. It MUST use text/icon in addition to color, accessible
labels, keyboard-readable details, and plain non-coder language per `DESIGN.md`.
It MUST NOT show actor references, role matrices, quota keys/threshold internals,
raw diagnostics, provider bodies, endpoint/config values, or secret state.

## Verification

### Deterministic acceptance matrix

| Case | Setup | Required assertions |
|---|---|---|
| DS-01 | five canonical session roles | each admitted; one stable identity key; no bypass |
| DS-02 | unknown role, absent role, unregistered service actor | deny before parse/retrieval/quota/provider |
| DS-03 | valid allowlisted signed service identity | admit and key by registered identity, not IP |
| DS-04 | each atomic config state | only `READY` reaches provider-attempt quota |
| DS-05 | trim-empty key metadata | blocked; credential metadata check allowed; bridge/adapter count zero |
| DS-06 | hosted memory or invalid Redis backend | blocked; no fallback to memory |
| DS-07 | query limit exhausted | one 429, bounded retry-after, zero retrieval/provider |
| DS-08 | provider limit exhausted | query admitted, provider denied, bridge count zero |
| DS-09 | corpus/grounding/phase-1/abstained outcomes | provider counter and bridge both zero |
| DS-10 | every terminal outcome including auth/role/parse denial | exactly one allowed-field event; early denial carries no request payload |
| DS-11 | durable append rejects | 503, pending answer withheld, provider not retried |
| DS-12 | timeout | same signal reaches bridge input and fetch init; one abort/bridge/fetch, zero retry/fallback, safe 504; Promise race alone fails |
| DS-13 | mismatched response/receipt pair | fail closed, safe 502, minimized evidence |
| DS-14 | static health for every dependency state | exact static priority, zero side effects, and no external liveness/writability claim |
| DS-15 | prohibited-field sentinel set | sentinel absent from event, logs, metrics, response, and UI projection |
| DS-16 | rotation failure | no mixed bundle; prior complete version remains active |
| DS-17 | rollback simulation | accepted artifact/config restored; all controls remain enabled |
| DS-18 | migration compatibility | historical response receipt readable; no backfill write |
| DS-19 | lifecycle authority | no downstream phase starts without its fresh packet |

### Future BUILD path manifest

The future BUILD packet MUST either own exactly the twenty-four paths listed in the
paired design's Future BUILD Manifest or return to the dispatcher with direct
source evidence for a corrected exact manifest. This specification does not
authorize those changes.

### Observable release evidence

Deterministic test PASS proves only source behavior. A release-readiness claim
would additionally require independent BUILD acceptance, a fresh hosted/live/
deploy authority, immutable artifact/config receipts, authorized smoke, health,
quota, audit, and rollback evidence. A public claim additionally requires a
separate public export packet.

## Failure Conditions

The future BUILD MUST fail review if any owner is duplicated; any future field
is claimed current; any role/service identity is implicitly trusted; hosted
memory quota is accepted; provider or audit work is retried automatically; raw
sensitive content is emitted or persisted; health has side effects; rollback
disables controls; the exact provider/model pair can change; or authority is
inherited across lifecycle transitions.

## Lifecycle And Authority Boundary

The only valid chain is:

`independent DESIGN/SPEC acceptance -> fresh BUILD authority -> deterministic tests and independent BUILD acceptance -> fresh hosted/live/deploy authority`

Authority MUST NOT inherit across any arrow. DESIGN/SPEC acceptance MUST NOT
authorize file changes. BUILD authority MUST NOT authorize credentials, hosted
execution, live calls, deployment, rollback execution, public sync, or
production. Deterministic test PASS MUST NOT authorize hosted/live/deploy
action. Hosted/live/deploy evidence MUST NOT authorize public export.

## Related Artifacts

- `docs/audits/CVF_LPCI1_WEB_UC01_RELEASE_HARDENING_DESIGN_2026-08-10.md`
- `docs/baselines/CVF_GC018_LPCI1_WEB_UC01_RELEASE_HARDENING_DESIGN_SPEC_2026-08-10.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_UC01_RELEASE_HARDENING_DESIGN_SPEC_2026-08-10.md`
- `docs/reviews/CVF_LPCI1_WEB_UC01_RELEASE_READINESS_DISCOVERY_COMPLETION_2026-08-10.md`

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this repository-specific release contract has no public projection or
public-sync authority.

## Claim Boundary

This is a pending normative specification. It neither changes source nor proves
release readiness. BUILD, tests, configuration, UI, session state, credentials,
provider/network/live action, hosted execution, deployment, rollback execution,
public sync, production, staging, commit, push, and downstream authority remain
forbidden until separately authorized.
