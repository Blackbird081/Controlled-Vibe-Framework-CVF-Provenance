# CVF CADP-AI-T5-R3 External Authentication Owner Adoption Readiness Decision

Memory class: FULL_RECORD

docType: audit

Status: COMPLETE_PENDING_REVIEW

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T5_R3_EXTERNAL_AUTHENTICATION_OWNER_ADOPTION_READINESS_DECISION_2026-08-15.md`

executionBaseHead: `07c65efd69a2860b2ce903864e658552bd29d46a`

Batch ID: CADP-AI-T5-R3

## Purpose

Decide, from current CVF Web source only, whether an existing authentication
owner is reusable for a future CADP ingress, without implementing,
registering, or invoking any authentication behavior.

## Target / Source

| Source file | Symbol(s) |
|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | `authorizeRouteGovernanceProof`; `buildProof`; `ROUTE_GOVERNANCE_PROOF_REGISTRY`; `RouteGovernanceProof`; `RouteGovernanceAuthorization` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | `verifyServiceTokenRequest`; `computeServiceRequestSignature`; `constantTimeEqual`; `deriveServiceTokenIdentity` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | `verifySessionCookie`; `resolveBaseSessionFromRequest`; `resolveBaseSessionAmbient` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | `authSecret`; `nextAuthConfig` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/memory/readout/route.ts` | `POST` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/learning-plane/readout/route.ts` | `POST` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.test.ts` | test-mode/production HMAC coverage |

## Scope / Methodology

Read-only source inspection of the seven files above plus a targeted registry
and symbol search; no TypeScript execution, no route invocation, no
authentication call, and no secret access. Reproduced the exact searches
named by the work order's Verification Commands from repository root, then
answered all twelve Required Decision Questions from source citations only,
built one Candidate Comparison table, and selected exactly one owner-readiness
token.

### Reproduced Searches

```
rg -n "authorizeRouteGovernanceProof|ROUTE_GOVERNANCE_PROOF_REGISTRY" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src
```

7 matches: `route-governance-proof.ts` (definition), `route-governance-proof.test.ts`, and four registered route handlers
(`artifacts/export`, `governance/override`, `knowledge/ingest`, `lpci/intake`) plus `lpci/query`.

```
rg -n "verifyServiceTokenRequest|verifySessionCookie" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src
```

Broad reuse confirmed: both symbols are composed together directly (outside
`authorizeRouteGovernanceProof`) in at least `memory/readout/route.ts`,
`learning-plane/readout/route.ts`, and multiple other route/test files, in
addition to the five routes that go through the proof-helper composition.

```
rg -niE "CADP|cadp" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts
```

No match. `ROUTE_GOVERNANCE_PROOF_REGISTRY` (lines 25-56 of
`route-governance-proof.ts`) currently lists exactly five non-CADP route
entries; a CADP route does not yet exist in this registry.

## Findings / Position

### Required Decision Questions

**1. Which exact module/function, if any, should own authentication for a
future CADP ingress?**

The selected bounded authentication-composition owner for a future CADP
ingress is `authorizeRouteGovernanceProof`
(`route-governance-proof.ts:118-208`). This does not select it as the CADP
authorization or durable-receipt owner: those responsibilities are absent
and remain separate prerequisites. It already composes the two lower-level primitives this
audit also evaluated directly: `verifyServiceTokenRequest`
(`service-token-auth.ts:37-67`) and `verifySessionCookie`
(`middleware-auth.ts:118-156`). Direct Auth.js (`auth.ts`) ownership is
rejected for this bounded tranche because its current configuration carries
mock defaults (Finding 10).

**2. Why is each alternative accepted, rejected, or subordinate?**

See the Candidate Comparison table below. Summary: the proof-helper
composition is accepted as the *closest* bounded reuse target because it is
already registry-driven, already returns a bounded allow/deny proof object,
and is already referenced by five repository route handlers; direct composition of the two
primitives is subordinate (functionally equivalent but would duplicate the
proof-shape and registry wiring that `authorizeRouteGovernanceProof` already
provides); the two existing readout-route patterns
(`memory/readout/route.ts`, `learning-plane/readout/route.ts`) are rejected
as the ingress model because they compose the two primitives directly
*without* the registry/proof step, which would leave a CADP ingress with no
per-route registry evidence trail; direct Auth.js ownership is rejected per
Finding 10; a wholly new owner is rejected as unnecessary because the
composition primitives already exist in current route source.

**3. Must the raw request body be captured before signature verification and
JSON parsing, and what exact ordering is required?**

Yes. `memory/readout/route.ts:140-154` and
`learning-plane/readout/route.ts:79-93` both call `request.text()` to capture
`bodyText` *before* calling `verifyServiceTokenRequest({..., body: bodyText})`
and before `JSON.parse(bodyText)`. `computeServiceRequestSignature`
(`service-token-auth.ts:27-35`) computes the HMAC over
`` `${timestamp}.${body}` ``, so the exact body text supplied to signature
generation must be preserved unparsed for verification. `request.text()` is
a decoded string boundary, not proof that original transport bytes are
retained. Parsing first would let a
re-serialization change silently invalidate a valid signature or (worse) let
whitespace-insensitive parsing accept a body that does not match the signed
bytes. `authorizeRouteGovernanceProof` (`route-governance-proof.ts:118-140`)
follows the same ordering: it receives `bodyText` as a parameter and evaluates
the service token before any parsing occurs in its caller.

**4. What is the precedence when a service token is presented but invalid and
a valid session exists? Is that behavior acceptable for CADP?**

Behavior differs by candidate and the difference is CADP-relevant:

- In `authorizeRouteGovernanceProof` (`route-governance-proof.ts:132-179`),
  the check is short-circuiting: `verifyServiceTokenRequest` runs first only
  when `serviceTokenPresented` is true; on success it returns immediately
  with `authMode: 'service_token'` and **never evaluates the session**. Only
  when the service-token branch does not return (token absent, or presented
  but invalid) does it fall through to `verifySessionCookie`.
- In both readout routes (`memory/readout/route.ts:147-158`,
  `learning-plane/readout/route.ts:86-97`), `verifySessionCookie` is called
  **unconditionally**, regardless of whether `isServiceAllowed` is already
  true; the two results are combined only at the final `!session &&
  !isServiceAllowed` check. A valid session is evaluated even on a call that
  already succeeded via a valid service token.

For CADP, an invalid presented service token combined with a valid session
currently still succeeds via the session branch in every candidate (none of
the three treats "token presented but wrong" as an outright reject that
overrides a valid session). That fallback is not accepted automatically for
CADP because it can change the principal class from service to human. A
future CADP wrapper must fail closed or explicitly authorize whether a service-identity
caller presenting a bad token should be allowed to fall back to a human
session identity, because the two produce different `actorId` provenance
(Finding 5) and that has authorization consequences the proof layer does not
adjudicate.

**5. What actor identity is produced for service-token, session, impersonated,
and unauthorized requests?**

- Service-token success: `actorId` = `deriveServiceTokenIdentity(serviceToken)`
  (`route-governance-proof.ts:154`), which is
  `` `service:${sha256(token).slice(0,16)}` `` (`service-token-auth.ts:23-25`)
  - a stable, non-reversible hash-derived identity, not the raw token and not
  a human identity.
- Session success (no impersonation): `actorId` = `session.userId`
  (`route-governance-proof.ts:176`), sourced from the Auth.js JWT/session
  (`middleware-auth.ts:85-93`, `101-109`).
- Session success (impersonated): `verifySessionCookie`
  (`middleware-auth.ts:118-156`) returns a `SessionCookie` whose top-level
  `userId`/`user`/`role`/`orgId`/`teamId` are the *impersonated* user's
  values, with the real actor preserved separately in `realUserId`,
  `realRole`, and a nested `impersonation` object
  (`sessionId`, `realActorId`, `impersonatedUserId`, `startedAt`,
  `expiresAt`). `authorizeRouteGovernanceProof` uses `session.userId` as
  `actorId`, i.e. the impersonated identity, not the real actor, unless a
  caller separately reads `session.impersonation.realActorId`.
- Unauthorized: `actorId: null` (`route-governance-proof.ts:191`).

**6. Which facts are authentication only, and which later owner must supply
CADP role/scope/risk authorization?**

Authentication-only facts produced by every candidate: whether the caller
presented a valid service token or a valid session, and which identity
string resulted (Finding 5). None of the three candidates evaluate or emit
any CADP-specific role, scope, or risk-tier decision - `SessionCookie.role`
(`middleware-auth.ts:22`) and `RouteGovernanceProof.riskLevel`
(`route-governance-proof.ts:69`) are the *nearest* existing fields, but
`riskLevel` is a static per-route registry value (`route-governance-proof.ts:25-56`),
not a live authorization decision, and `role` is a generic
`TeamRole` unrelated to CADP-specific authority fields
(`executionAuthorized`, `externalReadoutAuthorized`, etc., per the CADP
contract family already governed by
`governance/compat/check_cadp_authority_boundary_drift.py`). A future CADP
ingress needs a separate authorization owner that maps the authenticated
identity/role onto CADP-specific literal-false authority fields; this audit
does not select or design that owner.

**7. Does the proof contain sensitive material? Which request/response values
must be excluded or redacted?**

`RouteGovernanceProof` (`route-governance-proof.ts:64-80`) contains
`actorId`, `authMode`, `decision`, `serviceTokenConfigured`,
`serviceTokenPresented`, `serviceSignaturePresented`, `generatedAt`, and
route/risk metadata - no raw token, no raw signature, and no session cookie
value are included; only booleans about their presence/validity and the
hash-derived `actorId` (Finding 5) appear. The 401 response
(`route-governance-proof.ts:198-208`) echoes the deny `proof`, but the
unauthorized branch sets `actorId: null` at line 191. It therefore does not
disclose the hash-derived service identity for an invalid token. The response
still exposes route/risk metadata and credential-presence booleans, which a
future CADP wrapper must explicitly classify before echoing them to an
unauthenticated caller.

**8. Is the route-governance proof a decision proof, durable receipt, neither,
or both? Cite the persistence boundary.**

It is a **decision proof only**, not a durable receipt. `buildProof`
(`route-governance-proof.ts:89-116`) constructs and returns a plain object;
nothing in `route-governance-proof.ts` writes it to storage, a log, or any
persistence layer, and `authorizeRouteGovernanceProof` returns it directly to
the caller in-memory (`route-governance-proof.ts:143-208`). Unless the
calling route handler independently persists the returned `proof` object
(out of scope of this audit's read set), the proof exists only for the
duration of the request and is not queryable evidence after the response is
sent. This distinction matters directly for CADP: the CADP contract family's
`receiptGrantsExecution`/`receiptGrantsMutation`/`receiptGrantsActivation`
literal-false fields (see `T5R1_EXTERNAL_READOUT_FOUNDATION` in
`governance/compat/fixtures/cadp_authority_boundary_contract.v1.json`) treat
receipts as a distinct, durable authority artifact; this route-governance
proof does not currently satisfy that durable-receipt bar.

**9. How does `new Date()` affect deterministic tests and future receipt
reuse?**

`buildProof` sets `generatedAt: new Date().toISOString()`
(`route-governance-proof.ts:114`), i.e. real wall-clock time with no
injectable clock parameter, so every call produces a different `generatedAt`
and the full proof object cannot be asserted for exact equality across two
calls or reproduced deterministically in a test without either stubbing
`Date` globally or asserting on all fields except `generatedAt`. This
contrasts with `verifyServiceTokenRequest`, which already accepts an optional
injectable `now` parameter (`service-token-auth.ts:43`,
`61`) used by its own test (`service-token-auth.test.ts:41`, `50`) - i.e. the
lower-level primitive already has a deterministic test seam that the
higher-level proof helper does not propagate. A future CADP wrapper wanting
a deterministic receipt/proof-time seam should accept an injectable
clock/now parameter rather than calling `new Date()` directly, following the
existing `verifyServiceTokenRequest` precedent instead of inventing a new
pattern.

**10. Do current test-mode service-token shortcuts or Auth.js mock defaults
make direct adoption unsafe without a separate hardening packet?**

They are distinct source risks and must not be conflated:

- `verifyServiceTokenRequest` (`service-token-auth.ts:47-53`) returns `true`
  as soon as the presented token constant-time-matches the configured token
  **whenever `process.env.NODE_ENV === 'test'`**, skipping signature and
  timestamp verification entirely in that branch. This is explicit test
  behavior: `service-token-auth.test.ts:28` explicitly
  `vi.stubEnv('NODE_ENV', 'production')` to exercise the HMAC-verified path
  at all, which means the shortcut branch is the *default* behavior under a
  standard Vitest run. This is not evidence of a production bypass when
  `NODE_ENV=production`; it is a configuration-sensitive seam that a future
  CADP packet must test and constrain.
- `auth.ts:30` defines `authSecret` with a hardcoded literal fallback
  (`"cvf-enterprise-secret-mock-2026"`) whenever `NEXTAUTH_SECRET` is unset;
  `auth.ts:35-40` default GitHub/Google OAuth client id/secret to literal
  `"mock-*"` strings when their env vars are unset; and the `CredentialsProvider`
  (`auth.ts:42-79`) accepts any `findMockUserByUsername` match paired with
  the password pattern `` `${username}123` ``, plus a second fallback path
  keyed only on the `CVF_ADMIN_USER`/`CVF_ADMIN_PASS` env vars
  (`auth.ts:66-76`).

The Auth.js fallbacks make direct session-path adoption unsafe for a
CADP-reachable non-development deployment until fail-closed configuration is
proved. The service-token test shortcut requires deterministic
production-mode negative coverage and an environment invariant; source alone
does not prove it can execute in production. These are preconditions for a
later implementation packet, not a claim that a production bypass occurred.

**11. Is adding one registry entry sufficient, or would a CADP-specific
wrapper, authorization layer, receipt store, and tests also be required?**

One registry entry is **not** sufficient. Per Findings 6, 8, and 10, a future
CADP adoption packet requires, at minimum: (a) the Finding-10 hardening
packet; (b) a CADP-specific authorization layer mapping the authenticated
identity/role to CADP literal-false authority fields (Finding 6), since
`RouteGovernanceProof` carries no CADP authorization semantics; (c) a
decision on whether the proof needs to become a durable receipt for CADP's
receipt-grants-execution/mutation/activation semantics, and if so a receipt
store (Finding 8); and (d) new tests covering the CADP registry row and the
authorization layer, following the deterministic-clock precedent from
Finding 9. Adding only a `ROUTE_GOVERNANCE_PROOF_REGISTRY` row without (a)-(d)
would produce a route that authenticates but does not correctly authorize or
durably evidence a CADP decision.

**12. What is the exact smallest future changed set, deterministic local
proof, rollback boundary, and reopen condition?**

Smallest future changed set (not authorized by this audit; recorded for a
later packet only):

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts`
   and its focused test - retain or narrow the test shortcut only with an
   explicit environment invariant and production-mode signature/timestamp
   negative coverage (Finding 10).
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` and focused auth
   configuration tests - fail closed
   (throw or refuse to start) when `NEXTAUTH_SECRET` or required OAuth env
   vars are unset in any non-test/non-dev environment, rather than silently
   defaulting to mock literals (Finding 10).
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts`
   and its focused test - add the CADP registry configuration, make proof time
   injectable, and specify invalid-service-token/session-fallback policy.
4. One new CADP route file composing `authorizeRouteGovernanceProof` with
   body-text capture before parsing.
5. A new CADP authorization-layer module mapping identity/role to CADP
   literal-false authority fields (Finding 6), reviewed against
   `governance/compat/check_cadp_authority_boundary_drift.py`'s existing
   surface family.
6. A durable-receipt owner and focused tests only if a separately accepted
   receipt decision requires persistence; otherwise an explicit proof-only
   boundary and negative persistence claim.

Deterministic local proof for that future packet: a focused Vitest suite
asserting production-mode HMAC failure cases, fail-closed session
configuration, invalid-token/session precedence, actor provenance, injected
proof time, authorization denial, and the selected receipt boundary. The
existing CADP drift checker is extended only if a later governed contract
surface is added.

Rollback boundary: none of items 1-6 exist yet; there is nothing to roll
back from this audit. A future packet's rollback boundary should be that
same six-item list, reverted together.

Reopen condition: this decision should be revisited if the `NODE_ENV`
shortcut or Auth.js mock defaults are hardened for unrelated reasons before a
CADP packet is opened (evidence would change), or if a materially different
authentication owner is added to CVF Web before then.

### Candidate Comparison

| Candidate | Existing owner symbol | Request-body handling | Service-token behavior | Session/impersonation behavior | Identity provenance | Authorization separation | Proof/receipt boundary | Determinism | Mock/default risk | Smallest future changed set | Accept/reject evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Route-governance proof helper | `authorizeRouteGovernanceProof` | not itself responsible; caller must capture body text first | short-circuits on valid token; skips session check on success | evaluated only if token absent/invalid; supports impersonation via `session.userId` | `service:<hash>` or `session.userId` (impersonated if active) | none produced; only auth facts | decision proof only, in-memory, `new Date()` non-deterministic | no injectable clock | inherits Finding 10 risk via composed primitives | registry config/helper test + CADP wrapper/authorization and explicit receipt decision | **ACCEPT as bounded composition base**; registry-driven and referenced by 5 route handlers |
| Direct `verifyServiceTokenRequest` + `verifySessionCookie` composition | both primitives directly | caller-responsible, proven pattern in 2 live readout routes | test-mode shortcut live (Finding 10); session evaluated unconditionally even after token success | same impersonation semantics (shared `verifySessionCookie`) | same as above | none produced | no proof object at all unless caller builds one | no injectable clock at this layer for session; token layer has `now` param | same Finding 10 risk | would duplicate registry/proof plumbing the helper already provides | REJECT as primary; SUBORDINATE reference for ordering evidence |
| Existing readout-route pattern (`memory/readout`, `learning-plane/readout`) | route-local `POST` handlers | body-text-before-parse ordering (Finding 3) | same as direct composition | same as direct composition | same as above | none produced | no registry proof step; no persisted receipt | same as direct composition | same Finding 10 risk | would need to add registry/proof step to align with other 5 routes | REJECT as CADP ingress model; useful only as body-ordering reference |
| Direct Auth.js ownership | `auth.ts` `nextAuthConfig`/`authSecret` | N/A (session issuance, not per-request verification) | N/A | issues the session `verifySessionCookie` reads | JWT/session-derived | none produced | N/A | N/A | mock secret, mock OAuth ids, mock credentials, admin-env fallback all live (Finding 10) | **REJECT for this tranche** pending hardening packet |
| New/no current owner | none | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | full new build | REJECT: existing composition primitives already cover the mechanics; a full new owner is unnecessary |

### Terminal Owner-Readiness Enum

`SELECT_ROUTE_GOVERNANCE_PROOF_OWNER_BOUNDED`

Selection authorizes only a future packet recommendation per the smallest
future changed set in Finding 12. It does not authorize implementation,
route registration, authentication execution, or CADP closure.

## Risk / Corrective Action

Risk: adopting `authorizeRouteGovernanceProof` without satisfying Finding 10
would inherit configuration-sensitive test behavior and mock authentication
defaults into a CADP-reachable surface. Corrective action: the smallest future
changed set makes production-mode negative proof and fail-closed session
configuration preconditions of any CADP registry-row addition,
not a parallel or later-optional task. A secondary risk is conflating this
route-governance proof with a durable CADP receipt (Finding 8); corrective
action is that any future CADP wrapper must explicitly decide and implement
a receipt-persistence boundary rather than assuming the proof object already
satisfies it.

## Claim Boundary

This audit is a documentation-only, source-verified readiness decision. It
implements no code, registers no route, executes no authentication,
TypeScript, HTTP, CLI, MCP, provider, or network call, and reads no secret
value (only presence/absence of environment variables was inspected via
source, never printed or resolved at runtime). Selecting
`SELECT_ROUTE_GOVERNANCE_PROOF_OWNER_BOUNDED` authorizes only a future
packet recommendation subject to independent reviewer acceptance; it grants
no runtime, production, public, or deployment readiness, and does not itself
open, authorize, or schedule the hardening packet named in Finding 10/12.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - this audit makes no
  complete-corpus claim; it evaluates exactly the seven source files named
  in the work order's Source Verification Block and Required First Reads.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision audit; no public artifact or sync action
is authorized.
