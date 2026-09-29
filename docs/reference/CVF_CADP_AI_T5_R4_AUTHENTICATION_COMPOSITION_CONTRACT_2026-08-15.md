# CVF CADP-AI-T5-R4 Authentication Composition Contract

Memory class: FULL_RECORD

docType: reference

Status: ACCEPTED_BY_REVIEWER_WITH_REPAIRS

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CADP_AI_T5_R4_AUTHENTICATION_COMPOSITION_CONTRACT_HARDENING_2026-08-15.md`

executionBaseHead: `7ff5f4b25152c29ba336812c0ebe2f0d2ed0c644`

Batch ID: CADP-AI-T5-R4

## Purpose

Convert the T5-R3 bounded owner selection
(`SELECT_ROUTE_GOVERNANCE_PROOF_OWNER_BOUNDED`) into a precise, source-grounded
design contract that a later bounded implementation packet can follow without
re-deriving policy from scratch. This contract designs; it implements nothing.

## Scope / Applies To

Applies to a possible future CADP ingress route that would reuse
`authorizeRouteGovernanceProof` (`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts`)
as its authentication-composition owner. Does not apply to CADP authorization,
risk-tier decisions, receipt persistence, transport registration (MCP/CLI/HTTP),
or any currently-registered non-CADP route in `ROUTE_GOVERNANCE_PROOF_REGISTRY`.
Does not implement, edit, or execute any source, test, route, or configuration
file.

## Target / Source

| Source file | Symbol(s) |
|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | `authorizeRouteGovernanceProof`; `buildProof`; `ROUTE_GOVERNANCE_PROOF_REGISTRY`; `RouteGovernanceProof`; `RouteGovernanceAuthorization` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | `verifyServiceTokenRequest`; `computeServiceRequestSignature`; `constantTimeEqual`; `deriveServiceTokenIdentity` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | `verifySessionCookie`; `SessionCookie`; `resolveBaseSessionFromRequest`; `resolveBaseSessionAmbient` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | `authSecret`; `nextAuthConfig` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.test.ts` | `authorizeRouteGovernanceProof` test suite |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.test.ts` | `verifyServiceTokenRequest` test suite |
| `docs/reviews/CVF_CADP_AI_T5_R3_EXTERNAL_AUTHENTICATION_OWNER_ADOPTION_READINESS_DECISION_COMPLETION_2026-08-15.md` | `SELECT_ROUTE_GOVERNANCE_PROOF_OWNER_BOUNDED`; Reviewer Correction Ledger |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owner | Disposition |
|---|---|---|---|---|---|---|
| registry-driven token/session composition exists | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 25-61, 118-208 | `ROUTE_GOVERNANCE_PROOF_REGISTRY`; `authorizeRouteGovernanceProof` | route governance proof | ACCEPT |
| valid service token short-circuits before any session check | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 132-158 | `authorizeRouteGovernanceProof` | route governance proof | ACCEPT |
| invalid or absent presented token falls through to session evaluation | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 160-179 | `authorizeRouteGovernanceProof` | route governance proof | ACCEPT |
| deny branch sets `actorId: null`; no service-identity hash is disclosed on deny | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 181-208 | `buildProof` | route governance proof | ACCEPT |
| proof timestamp uses ambient wall clock with no injectable parameter | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | line 114 | `buildProof` | proof generator | ACCEPT |
| service-token verifier already accepts an injectable `now` parameter | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | lines 37-43 | `verifyServiceTokenRequest` | service-token authentication | ACCEPT |
| test-environment shortcut returns true on token match alone, before signature/timestamp checks | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | lines 47-53 | `verifyServiceTokenRequest` | service-token authentication | ACCEPT |
| session verifier supplies impersonated identity at top level and real-actor identity nested under `impersonation` | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | lines 19-30, 118-156 | `SessionCookie`; `verifySessionCookie` | middleware authentication | ACCEPT |
| Auth.js has literal mock-string fallback secret/OAuth defaults and an env-keyed legacy-admin credential fallback | RISK_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | lines 30-40, 66-79 | `authSecret`; `nextAuthConfig` | Auth.js configuration | ACCEPT |
| current focused tests cover valid-token, valid-session-with-no-token, deny, and registry-membership cases only | TEST_COVERAGE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.test.ts` | lines 39-101 | `authorizeRouteGovernanceProof` test suite | route proof tests | ACCEPT |
| current focused tests cover production-mode valid and bad-signature cases only; the test-environment shortcut path itself is not directly asserted | TEST_COVERAGE | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.test.ts` | lines 27-52 | `verifyServiceTokenRequest` test suite | service-token tests | ACCEPT |
| T5-R3 selected bounded composition ownership only, with reviewer corrections on body/disclosure/production-bypass claims | GOVERNED_DECISION | `docs/reviews/CVF_CADP_AI_T5_R3_EXTERNAL_AUTHENTICATION_OWNER_ADOPTION_READINESS_DECISION_COMPLETION_2026-08-15.md` | Findings / Position; Reviewer Correction Ledger | `SELECT_ROUTE_GOVERNANCE_PROOF_OWNER_BOUNDED` | T5-R3 completion authority | ACCEPT |

## Findings / Position

### Required Contract Questions

**1. What exact function owns authentication composition, and which
responsibilities remain outside it?**

`authorizeRouteGovernanceProof` (`route-governance-proof.ts:118-208`) owns
authentication composition: it decides, for one request, whether a presented
service token or an authenticated session grants access, and it returns a
bounded `RouteGovernanceAuthorization` (`allowed`, `proof`, `session`,
optional `response`). See the Responsibility Separation Matrix below for the
exact list of responsibilities it does **not** own.

### Responsibility Separation Matrix

| Responsibility | In scope of `authorizeRouteGovernanceProof`? | Actual owner |
|---|---|---|
| service-token signature/timestamp verification | Delegated | `verifyServiceTokenRequest` (`service-token-auth.ts:37-67`) |
| session/impersonation resolution | Delegated | `verifySessionCookie` (`middleware-auth.ts:118-156`) |
| ALLOW/DENY decision and proof shape | Owned | `authorizeRouteGovernanceProof`/`buildProof` |
| CADP role/scope/risk authorization | Not owned; does not exist yet | future CADP authorization layer (unselected) |
| durable receipt persistence | Not owned; helper returns an in-memory object only | future receipt owner (unselected; see Decision Proof And Durable Receipt Boundary) |
| deterministic/injected proof time | Not owned; uses `new Date()` directly | future wrapper must inject a clock (see Deterministic Time Contract) |
| production-safe environment configuration | Not owned; test/mock defaults live in the composed primitives | future environment-invariant owner (see Environment Fail-Closed Invariants) |
| CADP route registration (MCP/CLI/HTTP) | Not owned; no CADP entry exists in `ROUTE_GOVERNANCE_PROOF_REGISTRY` today | future transport/registration packet (explicitly out of scope of T5-R4) |

**2. What is the complete credential precedence state machine?**

| Presented service token | Session present/valid | Outcome | Source evidence |
|---|---|---|---|
| absent | absent/invalid | DENY, `authMode: 'unauthorized'`, `actorId: null` | `route-governance-proof.ts:181-208` |
| absent | valid | ALLOW, `authMode: 'session'`, `actorId: session.userId` | `route-governance-proof.ts:160-179` |
| presented, valid | not evaluated (short-circuit) | ALLOW, `authMode: 'service_token'`, `actorId: deriveServiceTokenIdentity(token)`; session branch never runs | `route-governance-proof.ts:132-158` |
| presented, invalid | absent/invalid | DENY, `authMode: 'unauthorized'`, `actorId: null` | `route-governance-proof.ts:160-179`, `181-208` |
| presented, invalid | valid | ALLOW, `authMode: 'session'`, `actorId: session.userId` (falls through to session) | `route-governance-proof.ts:160-179` |

This state machine is exhaustive over the two boolean-ish inputs (service
token valid/invalid/absent, session valid/absent) as currently implemented.

**3. Does invalid presented service token plus valid session fail closed, or
is fallback allowed only through an explicit policy input?**

Current behavior (row 5 above) **allows fallback unconditionally**: there is
no policy input in `authorizeRouteGovernanceProof` today that can make an
invalid-token-plus-valid-session request fail closed. This contract requires
a future CADP wrapper to enforce an explicit policy rather than inherit the
current unconditional fallback silently. The operator checkpoint on
2026-08-15 selected Option A as the mandatory CADP policy:

- **Selected - Option A (`CADP_FAIL_CLOSED_ON_INVALID_TOKEN`)**: a future CADP wrapper
  rejects the request outright when a service token is presented and fails
  verification, regardless of session validity, on the reasoning that a
  service-identity caller presenting a bad credential should not silently
  degrade to a human session identity.
- Rejected for this contract - Option B (`CADP_ALLOW_SESSION_FALLBACK`): a future CADP wrapper explicitly
  accepts the current helper behavior (row 5) as intended, on the reasoning
  that the human caller's own valid session should not be penalized by an
  unrelated bad service-token header.

The later implementation packet must cite this state machine and implement
`CADP_FAIL_CLOSED_ON_INVALID_TOKEN` as an explicit named policy constant. It
must not reopen Option B without a new operator checkpoint and a contract
revision.

**4. What body representation is signed, captured, parsed, logged, and
excluded?**

The exact **body text** supplied by the caller to `request.text()` is what is
signed: `computeServiceRequestSignature` (`service-token-auth.ts:27-35`)
computes an HMAC over `` `${timestamp}.${body}` ``, where `body` is that same
string. `authorizeRouteGovernanceProof` receives `bodyText` as a parameter
(`route-governance-proof.ts:120`) and does not itself call `request.text()`;
the caller is responsible for capturing it before any parsing occurs. This
contract makes **no transport-byte claim** - "body text" here means the
string value returned by the Fetch API's `Request.text()`, not a claim about
exact wire bytes, encoding, or transport-layer framing, which
`authorizeRouteGovernanceProof` and `verifyServiceTokenRequest` do not
inspect. Neither symbol logs the body; `RouteGovernanceProof` does not
include a body or body-hash field (`route-governance-proof.ts:64-80`).
`JSON.parse` must run only after both the signature check and the body-text
capture, matching the ordering the work order's Finding 3 already confirmed
in the two existing readout routes.

**5. What actor and real-actor identities exist for service, session,
impersonation, and deny cases?**

### Principal And Impersonation Provenance

| Case | `actorId` on the proof | Real-actor field | Source evidence |
|---|---|---|---|
| service token (valid) | `deriveServiceTokenIdentity(token)` = `` `service:${sha256(token).slice(0,16)}` `` | none (service tokens have no separate "real actor" concept) | `route-governance-proof.ts:154`; `service-token-auth.ts:23-25` |
| session (no impersonation) | `session.userId` | none; `realUserId`/`realRole`/`impersonation` are all absent on the returned `SessionCookie` | `route-governance-proof.ts:176`; `middleware-auth.ts:85-93` |
| session (impersonated) | `session.userId` = the **impersonated** user's id | `session.realUserId`, `session.realRole`, and `session.impersonation.realActorId` all carry the real actor's identity | `middleware-auth.ts:118-156` |
| unauthorized/deny | `null` | none | `route-governance-proof.ts:191` |

`authorizeRouteGovernanceProof` itself only reads `session.userId` for
`actorId` (`route-governance-proof.ts:176`); it does not itself read or
surface `session.impersonation`. A future CADP wrapper that needs
audit-grade real-actor provenance for an impersonated request must read
`session.impersonation.realActorId` directly from the `session` field already
returned on `RouteGovernanceAuthorization` (`route-governance-proof.ts:85`),
not assume `actorId` alone captures it.

**6. What information may appear in a public deny response versus internal
proof?**

### Public Deny Response Redaction

The 401 JSON response (`route-governance-proof.ts:198-208`) echoes the full
`proof` object back to the caller. On deny, that proof contains:
`actorId: null` (no identity disclosed on deny, correcting T5-R3's earlier
audit misstatement per its Reviewer Correction Ledger), `authMode:
'unauthorized'`, `decision: 'DENY'`, `serviceTokenConfigured`,
`serviceTokenPresented`, `serviceSignaturePresented` (all booleans),
`generatedAt`, and static route/risk metadata (`routeId`, `surface`,
`riskLevel`, `evidenceBasis`). No raw token, no raw signature, and no session
cookie value ever appear in the proof object at any point
(`route-governance-proof.ts:64-116`), on either the allow or deny path. The
only non-zero disclosure this contract records is the three presence/validity
booleans, which reveal to any unauthenticated caller whether a service token
is *configured* and whether *some* token/signature was presented - not
whether it was theirs. A future CADP wrapper reusing this response shape
inherits that same, already-bounded disclosure; this contract does not
require narrowing it further, but flags it for reviewer/policy sign-off
rather than treating it as self-evidently acceptable.

**7. Which later owner supplies CADP role, scope, risk, and literal-false
authority decisions?**

### CADP Authorization Separation

No current symbol in the four verified source files supplies this. `role` on
`SessionCookie` (`middleware-auth.ts:22`) is a generic `TeamRole`, not a CADP
authority field, and `riskLevel` on `RouteGovernanceProof`
(`route-governance-proof.ts:69`) is a static per-route registry value
(`route-governance-proof.ts:25-61`), not a live authorization decision. A
future, separately-selected CADP authorization layer must map the
authenticated `actorId`/`role`/`session` context onto the CADP contract
family's literal-false authority fields (the pattern already enforced by
`governance/compat/check_cadp_authority_boundary_drift.py` for
`T1_GUARD_CONTRACT`, `T3A_EXECUTION_PLANE_CONSUMER`,
`T3B_MODEL_GATEWAY_PROJECTION`, `T5R1_EXTERNAL_READOUT_FOUNDATION`, and
`T5R2_EXTERNAL_READOUT_ADAPTER` in
`governance/compat/fixtures/cadp_authority_boundary_contract.v1.json`).
Authentication (this contract's scope) answers only "who is this caller,"
never "what is this caller allowed to do in CADP terms."

**8. Is the proof proof-only, or is a durable receipt required? What
evidence would be needed to select persistence?**

### Decision Proof And Durable Receipt Boundary

`RouteGovernanceProof` is **proof-only** as currently implemented:
`buildProof` (`route-governance-proof.ts:89-116`) constructs and returns a
plain object; nothing in `route-governance-proof.ts` writes it to storage,
and the caller in `authorizeRouteGovernanceProof` returns it directly
in-memory (`route-governance-proof.ts:143-208`). This contract's default is
**proof-only**, matching the work order's Decision/Baseline row and the
T5-R3 completion's Acceptance Receipt Assertion Matrix ("decision-proof/
receipt separation: no persistence in helper: PASS"). Evidence that would be
needed before a later packet could select durable-receipt persistence
instead: (a) an explicit CADP requirement citing which of
`receiptGrantsExecution`/`receiptGrantsMutation`/`receiptGrantsActivation`
(the literal-false fields already present on
`T5R1_EXTERNAL_READOUT_FOUNDATION` in the CADP fixture) the CADP ingress
needs to satisfy; (b) a selected, source-verified persistence owner (this
contract selects none); (c) a design for how the receipt's authenticity
would be independently verifiable after the fact, since an in-memory proof
alone cannot serve as later evidence once the response is sent.

**9. How is proof time injected and propagated without global clock
stubbing?**

### Deterministic Time Contract

`buildProof` currently calls `new Date().toISOString()` directly
(`route-governance-proof.ts:114`) with no parameter, so it cannot be
deterministically tested without globally stubbing `Date`.
`verifyServiceTokenRequest` already accepts an optional `now?: number`
parameter (`service-token-auth.ts:43`) used by its own test via explicit
injection (`service-token-auth.test.ts:41`, `50`), not global stubbing. This
contract requires that any future modification propagating a clock through
`buildProof`/`authorizeRouteGovernanceProof` follow that same
already-established injectable-parameter precedent (for example an optional
`now?: () => string` or `now?: number` argument threaded through), rather
than introducing a new global-stub pattern or a different injection shape.
This contract does not itself add the parameter; it only sets the
requirement for whichever later packet does.

**10. What environment invariant prevents test shortcuts and mock/default
Auth.js settings from becoming acceptable non-test configuration?**

### Environment Fail-Closed Invariants

Two independent invariants are required, restating T5-R3's corrected
position precisely: the test-environment shortcut in
`verifyServiceTokenRequest` (`service-token-auth.ts:47-53`, gated on
`process.env.NODE_ENV === 'test'`) is **real source behavior that exists
today**, but this contract makes **no claim that it is reachable in any
running production deployment** - no evidence of a production process
running with `NODE_ENV=test` was found or is asserted here, correcting the
T5-R3 audit's overclaim per that review's Reviewer Correction Ledger. The
invariant required before implementation is: (a) a future packet must add an
explicit, source-verifiable assertion (test or startup check) that no
CADP-reachable process can execute with `NODE_ENV=test`, rather than relying
on operational convention; and (b) a future packet must add an explicit,
source-verifiable assertion that `NEXTAUTH_SECRET` and the OAuth
client id/secret env vars are non-default in any CADP-reachable deployment,
since `auth.ts:30-40` currently falls back to literal mock strings silently
when they are unset, and the `CVF_ADMIN_USER`/`CVF_ADMIN_PASS`
credentials-provider fallback (`auth.ts:66-76`) must be excluded from any
CADP-reachable configuration entirely. Both (a) and (b) are preconditions
for implementation, not implemented by this contract.

**11. What exact source and test paths form the smallest later
implementation?**

### Planned Implementation Manifest

The existing paths below are not edited by this documentation-only contract;
the paths marked `NEW` do not exist at review time. Together they are the
exact bounded manifest for a later, separately-authorized implementation
packet:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts`
   and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.test.ts`
   - narrow or remove the `NODE_ENV === 'test'` shortcut so it cannot fire
   outside an actual test-runner process (Environment Fail-Closed
   Invariants, item a).
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` and
   `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.test.ts` (`NEW`) - fail closed
   when `NEXTAUTH_SECRET` or required OAuth env vars are unset in any
   non-test/non-development environment, and exclude the
   `CVF_ADMIN_USER`/`CVF_ADMIN_PASS` fallback from CADP-reachable
   configuration (Environment Fail-Closed Invariants, item b).
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts`
   and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.test.ts`
   - thread an injectable clock parameter through `buildProof`/
   `authorizeRouteGovernanceProof` (Deterministic Time Contract).
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/cadp-authentication-policy.ts`
   (`NEW`) and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/cadp-authentication-policy.test.ts`
   (`NEW`) - define and test `CADP_FAIL_CLOSED_ON_INVALID_TOKEN`, then invoke
   the existing composition helper only when the selected policy permits it.
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/cadp-authorization.ts`
   (`NEW`) and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/cadp-authorization.test.ts`
   (`NEW`) - map authenticated identity/role to CADP literal-false authority
   fields while remaining separate from authentication composition.

A registry row and CADP route are deliberately excluded from this smallest
implementation manifest. They require a later registration packet that names
the actual product route and its exact route/test paths after items 1-5 pass.

### Focused Test Matrix

| Test case | Currently exists? | Required before a later CADP registry row |
|---|---|---|
| valid service token allows, session never evaluated | Yes (`route-governance-proof.test.ts:39-60`) | Already satisfied |
| valid session allows when no token presented | Yes (`route-governance-proof.test.ts:62-78`) | Already satisfied |
| deny sets `actorId: null` and 401 | Yes (`route-governance-proof.test.ts:80-89`) | Already satisfied |
| registry membership | Yes (`route-governance-proof.test.ts:91-100`) | Already satisfied |
| production-mode valid/bad-signature token verification | Yes (`service-token-auth.test.ts:27-52`) | Already satisfied |
| **invalid presented token + valid session is denied under `CADP_FAIL_CLOSED_ON_INVALID_TOKEN`** | **No** | Required |
| **test-shortcut path is unreachable outside `NODE_ENV=test`** | **No** | Required (Environment Fail-Closed Invariants, item a) |
| **injected proof time produces deterministic `generatedAt`** | **No** | Required (Deterministic Time Contract) |
| **`NEXTAUTH_SECRET`/OAuth env-var absence fails closed outside test/dev** | **No** | Required (Environment Fail-Closed Invariants, item b) |
| **impersonated session preserves `realActorId` through to a CADP-facing identity read** | **No** | Required (Principal And Impersonation Provenance) |

### Rollback And Reopen Conditions

Rollback unit: items 1-5 of the Planned Implementation Manifest, with edits
to existing files reverted and `NEW` files removed together if a later
implementation is rejected. This contract itself changes none of those
paths, so it has no runtime rollback action.
Reopen conditions: (a) this contract should be revisited if the test-mode
shortcut or Auth.js mock defaults are independently hardened for unrelated
reasons before a CADP implementation packet is opened, since that would
change the Environment Fail-Closed Invariants evidence; (b) if a materially
different authentication primitive is added to CVF Web before an
implementation packet is opened; (c) if an operator later proposes replacing
the selected Option A policy, which requires reopening this contract before
implementation proceeds.

**12. What focused negative cases must pass before a CADP registry row is
added?**

The five bolded "Required" rows in the Focused Test Matrix above must all
pass, in addition to the five already-passing rows continuing to pass
unmodified, before a CADP registry row may be added by a later registration
packet.

**13. What rollback unit and reopen triggers control the later
implementation?**

Answered under Rollback And Reopen Conditions above.

**14. Which single readiness token is supported?**

`READY_FOR_BOUNDED_IMPLEMENTATION`

This token authorizes only a reviewer recommendation that a separate,
source-verified implementation packet (covering Planned Implementation
Manifest items 1-5 in order) may be opened with the operator-selected
`CADP_FAIL_CLOSED_ON_INVALID_TOKEN` policy. It does not itself
release, schedule, or pre-authorize that implementation.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | this reference contract | design specification only; no runtime authority | source citations above | no runtime adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | possible future CADP ingress through `authorizeRouteGovernanceProof` | authentication-composition design only; no invocation, no registration, no authorization | no current CADP route or adapter exists | fresh source-verified implementation packet required | `DEFERRED_WITH_REASON` |

## Risk / Corrective Action

Risk: a later implementation packet could silently inherit the current
unconditional session-fallback behavior. Corrective action: the 2026-08-15
operator checkpoint selected `CADP_FAIL_CLOSED_ON_INVALID_TOKEN`, and this
contract requires that named policy to deny an invalid presented service
token regardless of session validity.
A second risk is conflating the "test shortcut exists in source" fact with a
"production bypass is reachable" claim, which the T5-R3 reviewer already
corrected once; this contract repeats the corrected, narrower framing
throughout Environment Fail-Closed Invariants to avoid reintroducing that
overclaim.

## Disposition

`READY_FOR_BOUNDED_IMPLEMENTATION`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_cadp_authority_boundary_drift.py` |
| literalTokensReviewed | `reference` docType section groups (`Purpose`, `Scope`/`Applies To`/`Target`, `Claim Boundary`); CADP fixture surface IDs and literal-false field names |
| gateRunPurpose | confirmation of the reference-artifact structural shape, read ahead of drafting |
| claimBoundary | read-ahead evidence for this contract file only; does not cover the worker-return file's separate checker family |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | documentation-contract worker |
| Provider or surface | local private provenance repository |
| Session or invocation | CADP-AI-T5-R4 worker execution, 2026-08-15 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg` symbol searches, direct file writes, governance gates |
| Target paths | exactly the two worker-owned paths named in the paired work order |
| Allowed scope source | paired GC-018 baseline and work order `## Write Ownership` / `## Scope` sections |
| Before status evidence | HEAD `7ff5f4b25152c29ba336812c0ebe2f0d2ed0c644`; clean worktree; empty staging |
| After status evidence | HEAD unchanged; staging empty; two untracked worker-owned paths |
| Diff evidence | `git status --short --untracked-files=all`; `git diff --name-status` |
| Approval boundary | worker execution only, per `WORKER_MUST_NOT_COMMIT`; material commit and closure remain reviewer/closer-owned |
| Claim boundary | design contract only; no production, runtime, auth, provider/live, or public claim |
| Agent type | worker |
| Invocation ID | `cadp-ai-t5-r4-worker-execution-2026-08-15` |
| Expected manifest | `docs/reference/CVF_CADP_AI_T5_R4_AUTHENTICATION_COMPOSITION_CONTRACT_2026-08-15.md`; `docs/reviews/CVF_CADP_AI_T5_R4_AUTHENTICATION_COMPOSITION_CONTRACT_HARDENING_WORKER_RETURN_2026-08-15.md` |
| Actual changed set | `docs/reference/CVF_CADP_AI_T5_R4_AUTHENTICATION_COMPOSITION_CONTRACT_2026-08-15.md`; `docs/reviews/CVF_CADP_AI_T5_R4_AUTHENTICATION_COMPOSITION_CONTRACT_HARDENING_WORKER_RETURN_2026-08-15.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this batch |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | documentation-only CADP-AI-T5-R4 authentication composition contract |
| claimDisposition | CLAIM_REJECTED: no runtime control or authentication behavior is created by this contract |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no source, test, route, or authentication action occurs |
| invocationBoundary | local read-only source inspection and documentation authoring only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, CLI, MCP, Web runtime, or adapter interception claim |
| claimLanguage | design contract pending independent reviewer acceptance |
| forbiddenExpansion | no source/test/route/authentication/runtime/live/public/deployment behavior; no CADP registry, wrapper, authorization layer, or receipt store is created |

## Epistemic Process Block

- Epistemic Process Applicability: BOUNDED_GOVERNANCE_IMPLEMENTATION
- Expected Result / Prediction: `authorizeRouteGovernanceProof` was predicted, per the work order's own Decision/Baseline row, to remain the bounded composition owner while requiring an explicit credential-precedence policy, injected proof time, and fail-closed environment invariants before implementation.
- Evidence Comparison: compared that prediction against the exact composition order in `authorizeRouteGovernanceProof` (`route-governance-proof.ts:132-179`), the ambient-clock call in `buildProof` (`route-governance-proof.ts:114`), the already-injectable `now` parameter precedent in `verifyServiceTokenRequest` (`service-token-auth.ts:37-43`), and the mock/default Auth.js facts (`auth.ts:30-79`); all four confirm the prediction.
- Contradiction Or Gap Disposition: no source contradiction found. The policy gap was resolved by the 2026-08-15 operator checkpoint selecting `CADP_FAIL_CLOSED_ON_INVALID_TOKEN`; current runtime fallback remains an implementation gap, not accepted target behavior.
- Claim Update: CONFIRMED - `READY_FOR_BOUNDED_IMPLEMENTATION` is selected with Option A fixed as policy and with Planned Implementation Manifest items 1-5 required before any later registration packet may add a CADP registry row.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - this contract makes no
  complete-corpus claim; it evaluates exactly the source and test files named
  in the work order's Source Verification Block and Required First Reads.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance design contract; no public artifact or sync action
is authorized.

## Claim Boundary

This reference contract is a documentation-only authentication-composition
design specification. It implements no code, registers no route, executes no
authentication, TypeScript, HTTP, CLI, MCP, provider, or network call, and
reads no secret or credential value. Selecting
`READY_FOR_BOUNDED_IMPLEMENTATION` authorizes only a future reviewer
recommendation for a separately-authorized, source-verified implementation
packet using the selected `CADP_FAIL_CLOSED_ON_INVALID_TOKEN` policy; it
grants no runtime, production, public, or deployment
readiness, and does not itself open, schedule, or authorize that
implementation packet.
