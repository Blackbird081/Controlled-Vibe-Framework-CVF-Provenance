# CVF LPCI1 Web Context-To-LLM Use Case Intake Roadmap

Memory class: FULL_RECORD

Status: LPCI1_WEB_UC01_RELEASE_READINESS_GAPS_PARKED_PENDING_FRESH_DESIGN_SPEC_AUTHORITY

docType: roadmap

Date: 2026-08-09

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_roadmap_closure_freshness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_corpus_scan_registry.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | roadmap heading groups (`## Authorization`/`## Decision`, `## Purpose`/`## Why`, `## Scope`, `## Non-Goals`, `## Design Control Gate`/`## Dispatch Boundary`, `## Work Plan`, `## Acceptance Criteria`, `## Verification`/`## Evidence`); `Status:` line; `PROPOSED_OPERATOR_REVIEW_REQUIRED`; `DEFERRED_PRIVATE_ONLY`; `Verified path or symbol` (real symbol, not filename); ADIF disclosure exact-query requirement |
| gateRunPurpose | confirm structural and dispatch-quality shape after source-backed authoring; not first discovery of checker requirements |
| claimBoundary | documentation-only intake/roadmap planning; no DESIGN/SPEC/BUILD/provider/live claim |

## Authorization / Decision

Operator authority received on 2026-08-09 as the literal first line of the
operator's chat instruction that opened this intake session:

`AUTHORIZE_FRESH_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_INTAKE_ROADMAP_DOCUMENTATION_ONLY`

Evidence of invocation: this exact token is the operator's own conversational
instruction text for this session, not a prior committed governed artifact.
No prior GC-018, work order, or handoff contains this token; a repository
search confirms it is absent from every committed path (it exists only inside
this roadmap and its paired worker return, both authored in response to it).
This roadmap does not inherit authority from the current-owner defect intake
roadmap (`docs/roadmaps/CVF_LPCI_CURRENT_OWNER_GROUNDING_AND_CLEARANCE_DEFECT_INTAKE_ROADMAP_2026-08-08.md`)
or any other prior LPCI1-Web artifact; it treats those artifacts as source
evidence only, per the Current Source Verification table below.

This authority opens only this fresh documentation-only intake/roadmap for
concrete use cases where context already processed, filtered, bounded, and
audited by LPCI1 Web is passed to an LLM through a provider API to answer a
user. It does not inherit or imply DESIGN, SPEC, BUILD, provider/model
selection, provider invocation, live proof, persistence, vector/RAG, runtime
mutation, test execution, non-public grants, public-sync, deployment, or
readiness authority.

Decision: `LPCI1_WEB_CONTEXT_TO_LLM_INTAKE_ACCEPTED_BOUNDED_HOLD_BEFORE_DESIGN`.
Independent reviewer closure accepts the source-backed
candidate use cases, an owner/consumer/dependency map, a value/risk ranking, and
one recommended next-tranche candidate. It selects UC-01 only as the candidate
for a possible future DESIGN tranche; it does not authorize that tranche or
open any later lifecycle phase.

## Purpose

Identify, without designing a solution, which concrete consumer use cases can
send LPCI1-Web-governed, filtered, bounded, and audited context to an LLM
through a provider API to answer a user, and classify each candidate's
readiness so a future operator can select at most one for a fresh DESIGN
authorization.

## Non-Goals

This intake does not select a solution, design an interface, lock a SPEC,
implement or execute runtime/test code, call a provider, use an API key, add
persistence, vector/embedding/RAG/graph storage, create an entitlement/grant
store, open non-public/restricted/confidential/classified access, or claim
public-sync/deployment/readiness. It records candidates and one recommended
next tranche only.

## Scope / Target / Owner Boundary

Scope: documentation-only current-source verification and use-case candidate
intake for context-to-LLM consumers of the existing LPCI1-Web query surface.

Target: `POST /api/lpci/query`, its current helpers under
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/`, and the current
LPCI dashboard consumer page cited by full path in the Current Source
Verification table below.

Owner: the existing LPCI1-T5 cvf-web route/library/UI/test family, unchanged
since the closures below. Owner boundary: this is not a generic governed-
retrieval, Control Plane, Memory, KGR, vector, or provider lane. No cross-owner
design is justified by this intake.

## Current Runtime Freshness Verification

Verification date and base: 2026-08-09; starting HEAD
`95340497fe4ca835ee85d44f311f651632b9c606`. All rows in the Current Source
Verification table below were read directly from current source at this base,
not inherited from a prior snapshot. The provider-registry finding was added
after the dispatch-quality gate identified `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
as a surface this intake had not yet checked; it was then read in full and is
now included as source fact `PCR-01` below.

## Current Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Source fact type | Disposition |
|---|---|---|---|---|---|
| provider fetch call exists in current route | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 289-320 | `fetch` | RUNTIME_BEHAVIOR | ACCEPT |
| provider API key env var name appears in current route, read directly with no config-schema owner | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | line 263 | `LPCI_LLM_API_KEY` | RUNTIME_BEHAVIOR | ACCEPT |
| provider endpoint/model env var names with hardcoded defaults | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 286-287 | `LPCI_LLM_ENDPOINT` | RUNTIME_BEHAVIOR | ACCEPT |
| `LPCI_LLM_*` vars absent from documented env contract | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.example` | full file (75 lines) | `OPENAI_API_KEY` | NEGATIVE_SEARCH | ACCEPT |
| `.env.local` present and gitignored; contents not read (secret) | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.gitignore` | line 34 | `.env*` | EXISTS | ACCEPT |
| route auth/governance-proof owner and its registry entry for this route | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | lines 50-55 | `ROUTE_GOVERNANCE_PROOF_REGISTRY` | EXISTS | ACCEPT |
| registry contains 160 total corpus entries; it is not one-entry | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | `corpora` array | `corpora` | EXISTS | ACCEPT |
| registry entries carry no row-level `sensitivityLevel` field; sensitivity cannot be inferred from registry membership alone | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | `corpora` array, all 160 entries | `corpora` | NEGATIVE_SEARCH | ACCEPT |
| exactly one query-loadable LPCI index file exists on disk | `docs/corpus-intelligence/GOVERNANCE_PILOT_NO_LEGAL_CORPUS-index.json` | full file (4 array entries) | `GOVERNANCE_PILOT_NO_LEGAL_CORPUS-index.json` | EXISTS | ACCEPT |
| that index's 4 rows are all `sensitivityLevel: public` | `docs/corpus-intelligence/GOVERNANCE_PILOT_NO_LEGAL_CORPUS-index.json` | full file | `sensitivityLevel` | EXISTS | ACCEPT |
| no other `<corpusId>-index.json` file exists under the corpus-intelligence directory | `docs/corpus-intelligence/` | directory listing | `-index.json` | NEGATIVE_SEARCH | ACCEPT |
| dashboard is the only current non-test caller of the route | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.tsx` | lines 33-37 | `handleQuery` | `page.tsx` dashboard consumer | RUNTIME_BEHAVIOR | ACCEPT |
| accepted S1 conformance contract for this route | `docs/reference/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_2026-08-08.md` | Core Contract; Model Evidence Projection sections | `modelEvidenceProjection` | LITERAL_INVARIANT | ACCEPT |
| B1/BR1 bounded closure evidence | `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD_COMPLETION_2026-08-09.md` | Verification Evidence table | `CLOSED_PASS_BOUNDED` | RUNTIME_BEHAVIOR | ACCEPT |
| current owner intake defect roadmap and its recorded next-move deferral of this exact topic | `docs/roadmaps/CVF_LPCI_CURRENT_OWNER_GROUNDING_AND_CLEARANCE_DEFECT_INTAKE_ROADMAP_2026-08-08.md` | `## Next Allowed Move` | `Next Allowed Move` | LITERAL_INVARIANT | ACCEPT |
| stale prior product-vision roadmap remains `PROPOSED`, not current authority | `docs/roadmaps/CVF_LPCI_LEGAL_POLICY_CORPUS_INTELLIGENCE_CHATBOT_USE_CASE_ROADMAP_2026-06-01.md` | line 5 | `Status` | EXISTS | ACCEPT |
| closed MVP roadmap is a different, already-closed lifecycle | `docs/roadmaps/CVF_LPCI1_LEGAL_POLICY_CORPUS_INTELLIGENCE_PRODUCT_MVP_ROADMAP_2026-06-02.md` | line 5 | `Status` | EXISTS | ACCEPT |
| active handoff and session-state next-move gate this exact intake topic | `AGENT_HANDOFF_V55_2026-08-05.md` | Startup Acknowledgment | `Startup Acknowledgment` | LITERAL_INVARIANT | ACCEPT |
| `PCR-01`: existing CVF Model Gateway provider-capability registry exists but has no LPCI provider entry, and its provider IDs (`alibaba`, `deepseek`, `openai`) do not match `LPCI_LLM_*` naming | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | lines 49-126 | `PROVIDER_CAPABILITY_REGISTRY` | NEGATIVE_SEARCH | ACCEPT |
| Model Gateway owner-ref pattern for retry/cost/risk exists and could be a future provider-lane owner target | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | lines 49-68 | `PROVIDER_CAPABILITY_OWNER_REFS` | EXISTS | ACCEPT |

## Existing Vs Proposed Symbols

Existing runtime symbols cited above: `fetch`, `LPCI_LLM_API_KEY`,
`LPCI_LLM_ENDPOINT`, `LPCI_LLM_MODEL`,
`buildAnswerBoundaryPrompt`, `buildModelEvidenceProjection`,
`ROUTE_GOVERNANCE_PROOF_REGISTRY`, `authorizeRouteGovernanceProof`,
`isCorpusRegistered`, `LpciQueryResponse`, `AuditReceipt`,
`PROVIDER_CAPABILITY_REGISTRY`, `PROVIDER_CAPABILITY_OWNER_REFS`.

The following are DOC_ONLY_NEW candidate names for a future DESIGN and MUST NOT
be claimed as current runtime fields: `contextToLlmUseCaseOwner`,
`useCaseConsumerRegistry`, `entitlementGrantOwner`,
`nonPublicCorpusAuthorizationRecord`, `provideConfigOwner`. None of these exist
in current source; they appear only as candidate names in this roadmap.

## Provider Execution/Configuration Owner Finding

The current route (`route.ts` lines 263, 286-287, 289-320) already contains a
real `fetch` call to an LLM provider, gated only by presence of
`LPCI_LLM_API_KEY`. This is a source-present branch, not a
configured/live/production-ready branch: `.env.example` (the documented env
contract) does not list `LPCI_LLM_API_KEY`, `LPCI_LLM_ENDPOINT`, or
`LPCI_LLM_MODEL` at all, unlike the documented `OPENAI_API_KEY`,
`ANTHROPIC_API_KEY`, `GOOGLE_AI_API_KEY`, `ALIBABA_API_KEY`, and
`DEEPSEEK_API_KEY` provider family.

An existing CVF Model Gateway provider-lane pattern does exist for generic
provider execution semantics:
`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` defines
`PROVIDER_CAPABILITY_REGISTRY` for providers `alibaba`, `deepseek`, and
`openai`, each with `PROVIDER_CAPABILITY_OWNER_REFS` naming existing
`retry`/`cost`/`risk` owner surfaces (`fallback-policy.ts`, `quota-ledger.ts`,
`gateway-policy.ts`). No canonical CVF source was found that mandates every
provider-calling route integrate with this Model Gateway registry, so this
finding does not claim the LPCI route "bypasses a mandatory gateway" or is
"ungoverned" in a general sense. The narrower, source-verified fact is: none of
the Model Gateway registry's entries reference LPCI, and no `LPCI_LLM_*`-named
provider exists in that registry. This means the current LPCI direct-`fetch`
branch is not source-verified as integrated with the existing Model
Gateway/config owner - only the LPCI-specific config/integration of
`LPCI_LLM_API_KEY`, `LPCI_LLM_ENDPOINT`, and `LPCI_LLM_MODEL` lacks a
verified owner/binding; generic provider execution semantics (retry/cost/risk)
already have an existing Model Gateway owner that a future tranche should
reuse or compose, not duplicate. A local `.env.local` file exists and is
gitignored; per this intake's forbidden-scope rule, its contents were not
read and its presence is not evidence of a live, configured, or
production-ready provider path. Distinguishing source-present from
configured/live/production-ready is exactly the operator's question 4: the
LPCI-specific binding of these three env vars currently belongs to no
documented CVF provider-lane owner, even though a documented provider-lane
pattern exists in CVF for other providers.

## Use-Case Candidate Matrix

This intake identifies five concrete use-case candidates (`UC-01`, `UC-02`,
`UC-03`, `UC-05`, `UC-06`) plus one cross-cutting provider-integration
dependency lane (`UC-04`, recorded separately below the use-case table so it
does not compete in the value/risk ranking as an independent use case; every
use case that reaches `ANSWER_EMITTED` shares the same unresolved dependency).

| ID | Named consumer | User question shape | Context source | Governance/filter stages already applied | Output destination | Existing owner | Provider requirement | Security/privacy risk | Deterministic proof seam | Live-proof requirement | Dependency | Reopen condition | Disposition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `UC-01` | LPCI dashboard operator/pilot user (existing `/lpci` page) | runnable synthetic query `nghi phep nam` (Vietnamese, "annual leave"): the current `applySearch` matcher in `filter-pipeline.ts` lowercases the whole query string and does a substring match against each record's `titleSnippet`/`contentSnippet`; `nghi phep nam` is verified present (case-insensitive substring) in 2 of the 4 fixture rows' `titleSnippet`/`contentSnippet` fields, so this exact string is runnable against the current matcher today - a schema/governance demonstration query against the synthetic fixture, not a legal-correctness, current-law, legal-advice, or production-corpus proof | the one route-loadable index file `GOVERNANCE_PILOT_NO_LEGAL_CORPUS-index.json` (synthetic, public-only, 4 fixture rows; not a real legal/policy/decree corpus) | S1 public-only admission, filter pipeline, retrieval boundary, `modelEvidenceProjection`, safe serialization, audit receipt | existing `/lpci` dashboard response panel | existing LPCI1-T5 cvf-web owner; no new owner needed | yes; the shared `UC-04` provider-integration dependency below applies | LOW: fixture data is synthetic/public-only and explicitly not legal advice; B1 fail-closes non-public | B1's 99 focused/7-file test suite plus P1-P8/F1-F16 synthetic matrix | yes, before any real user-facing answer claim; zero calls proven so far | none beyond existing B1/BR1 closure and the `UC-04` dependency | already eligible for DESIGN-only authorization now; see `## Recommended Next Tranche` for the single-chain lifecycle | `READY_FOR_FRESH_DESIGN_AUTHORITY` |
| `UC-02` | future organization/internal-policy user needing a real (non-synthetic) corpus | "What does our internal SOP/company policy say about Y?" | unspecified - no current corpus is claimed as the future UC-02 corpus. The PolicyLocal production corpus registry entry (`policylocal-production-corpus-dropzone`, `DEEP_CLASSIFIED`, LPCI2-owned) remains counterexample-only: it has no matching LPCI1 `<corpusId>-index.json` and represents different LPCI2-owned laws/documents | none yet for LPCI1; S1/B1 apply only once a route-compatible index is admitted for a selected future corpus | future org-internal consumer, undetermined | accepted discovery found only the dashboard-to-synthetic-pilot caller; no named real UC-02 consumer | yes; the accepted UC-04 binding applies only once UC-02 is reachable | MEDIUM: real organizational content; current source exposes none through UC-02 | same B1 seam once a route-compatible index is available | yes | all simultaneously: named real non-test consumer; matching route-compatible public index; direct consumer-to-corpus-to-route selection/binding | accepted discovery found A/B/C all NOT_MET; reopen only when all three become direct current-source facts | `PARKED_REOPEN_CONDITION_NOT_MET` |
| `UC-03` | any consumer needing non-public (restricted/confidential/classified) corpus answers | "What does this confidential/internal-only document say?" | any corpus with non-public `sensitivityLevel` rows | S1 explicitly fails these closed at Stage 1; B1 proves fail-close (P4/P5/F2/F11) | none; route returns `FILTERED_OUT` or admits nothing | no entitlement/grant owner exists anywhere in current source | yes, plus an unresolved entitlement owner | HIGH if ever built without a grant owner; currently zero exposure because fail-closed | existing fail-closed tests already prove the negative case | yes, but blocked on entitlement owner first | a source-verified non-public entitlement/grant-store owner, not present today | reopen only when a governed entitlement/grant owner is source-verified to exist | `PARKED_MISSING_ENTITLEMENT_OWNER` |
| `UC-05` | a hypothetical second LPCI-like corpus-to-LLM consumer outside cvf-web (e.g. a CLI or MCP tool) | any query shape routed through a non-cvf-web caller | any admitted corpus | none observed; no such caller exists in current source | undetermined | no source-verified non-test, non-dashboard caller of `/api/lpci/query` exists | undetermined | undetermined; no current evidence to assess | none; no caller to test | undetermined | a source-verified new caller with a registered production trigger | reopen only when a real non-test, non-dashboard caller is source-verified to exist and call this route | `NO_CURRENT_VALUE_WITH_REOPEN_CONDITION` |
| `UC-06` | duplicate/second cvf-web LPCI query owner (a parallel route doing the same job) | any | any | N/A | N/A | the existing single route already owns this responsibility | N/A | N/A | N/A | N/A | N/A | `N/A - permanently rejected duplicate owner` | `REJECT_DUPLICATE_OWNER` |

## Cross-Cutting Provider-Integration Dependency Lane

`UC-04` is not an independent use case: its "named consumer" would be "any
consumer whose use case reaches `ANSWER_EMITTED`," which is not a concrete
consumer. It is retained under its own ID only so downstream sections (Value
And Risk Ranking, Reopen Conditions, Design Control Gate) can trace it, and it
does not compete for value/risk rank against `UC-01`, `UC-02`, `UC-03`,
`UC-05`, or `UC-06`.

| ID | Nature | Applies to | Current owner | Requirement | Risk | Dependency | Reopen condition | Disposition |
|---|---|---|---|---|---|---|---|---|
| `UC-04` | cross-cutting provider-integration dependency, not a standalone use case | every use case that would reach `ANSWER_EMITTED` (currently only `UC-01`) | LPCI1-T5 route owns the call site; the LPCI-specific integration/binding of `LPCI_LLM_API_KEY`/`LPCI_LLM_ENDPOINT`/`LPCI_LLM_MODEL` to a documented CVF provider-lane owner is not source-verified | resolving this dependency before any live provider call | MEDIUM: an unresolved LPCI-specific provider-config binding is a governance gap even before any live call; this is not a claim that generic provider execution itself is unowned | a fresh decision that reuses or composes the existing CVF Model Gateway provider-capability owner (`PROVIDER_CAPABILITY_REGISTRY`/`PROVIDER_CAPABILITY_OWNER_REFS`) for LPCI's three env vars; a new parallel generic provider owner is not an available option | reopen only when both: (a) the LPCI-specific binding of `LPCI_LLM_API_KEY`/`LPCI_LLM_ENDPOINT`/`LPCI_LLM_MODEL` to the existing Model Gateway owner is source-verified in runtime code; and (b) a documented config contract for that binding exists (e.g. a `.env.example` entry or equivalent config-schema documentation naming the Model Gateway integration). Naming the variables in `.env.example` alone, without a source-verified Model Gateway integration, is insufficient. | `PARKED_PROVIDER_OR_LIVE_AUTHORITY` |

Negative-search note: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src` was
searched for `/api/lpci/query` callers; only the route's own tests and the
`/lpci` dashboard page matched (see Current Source Verification table). No
other route, CLI, MCP tool, or script calls this endpoint in current source.

## Owner/Consumer/Dependency Map

| Layer | Owner | Evidence |
|---|---|---|
| Route/response contract | existing LPCI1-T5 cvf-web route owner | `route.ts`; accepted S1 spec |
| Filter/retrieval/audit helpers | existing LPCI1-T5 cvf-web library owner | `filter-pipeline.ts`; `audit-receipt.ts`; `query-conformance.ts` |
| Auth/route-governance-proof | existing route-governance-proof owner (shared across `/api/lpci/query`, `/api/lpci/intake`, and other registered routes) | `route-governance-proof.ts` lines 25-56 |
| Corpus registration | GC-051 corpus scan registry owner | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |
| Only current consumer | LPCI dashboard page (`/lpci`) | `page.tsx` lines 33-37 |
| LPCI-specific provider integration/binding | unresolved; `LPCI_LLM_API_KEY`/`LPCI_LLM_ENDPOINT`/`LPCI_LLM_MODEL` are not source-verified as bound to any documented CVF provider-lane owner | Cross-Cutting Provider-Integration Dependency Lane (`UC-04`) above |
| Generic provider execution semantics (retry/cost/risk) | existing CVF Model Gateway owner (`PROVIDER_CAPABILITY_OWNER_REFS`); not LPCI-specific | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` lines 49-68 |
| Non-public entitlement | unresolved; does not exist | UC-03 row above; also recorded in the current-owner defect intake roadmap |

## Value And Risk Ranking

Five use-case candidates are ranked; `UC-04` is a cross-cutting dependency, not
a use case, and does not appear in this ranking (see the Cross-Cutting
Provider-Integration Dependency Lane table above for its own disposition).

| Candidate | Value if built | Risk if built now | Rank |
|---|---|---|---|
| `UC-01` | LOW-MEDIUM: proves the existing pilot path end-to-end for internal demonstration; no real user value yet because the fixture is synthetic | LOW | 1 (highest readiness) |
| `UC-02` | MEDIUM-HIGH: real organizational value once a real corpus is both registered and route-compatible with a named consumer | LOW-MEDIUM: S1 fail-close already covers non-public rows | 2 |
| `UC-03` | potentially HIGH long-term value | HIGH without an entitlement owner; correctly parked | 3 (blocked) |
| `UC-05` | unknown; no evidence of demand | unknown | 4 (no evidence) |
| `UC-06` | none; duplicate | N/A | rejected |

## Provider/API-Key Boundary

No provider call, API key, or live invocation is used or authorized by this
roadmap. The finding above is a read-only source observation: the current
route already contains provider-call code gated on `LPCI_LLM_API_KEY`, but that
variable has no documented owner in `.env.example`, and its LPCI-specific
integration with any existing CVF provider-lane owner (such as the Model
Gateway provider-capability pattern) is not source-verified. Its presence in a
local untracked `.env.local` file is not evidence of a configured, live, or
production-ready path. Any future use of a real key requires a separate fresh
GC-018 naming the exact provider-lane owner or verifying integration with an
existing one; future work should reuse or compose that existing Model Gateway
owner rather than create a parallel provider-lane owner.

## Public/Non-Public Data Boundary

Three distinct facts must not be collapsed into one another:

1. **Registry membership**: `CVF_CORPUS_SCAN_REGISTRY.json` lists 160 total
   corpus entries across many unrelated CVF domains. The registry schema does
   not carry a row-level `sensitivityLevel` field, so registry membership
   alone says nothing about whether a corpus's underlying rows are public or
   non-public.
2. **Route-compatible index availability**: `route.ts`'s `loadCorpusIndexText`
   only loads a file at the literal path
   `docs/corpus-intelligence/<corpusId>-index.json`. Exactly one such file
   exists on disk today: `GOVERNANCE_PILOT_NO_LEGAL_CORPUS-index.json`. No
   other registry entry, including the PolicyLocal production corpus entry
   cited as a counterexample under `UC-02` (registry membership does not
   equal route-compatible index availability), currently has a matching
   `<corpusId>-index.json` file that this route could load.
3. **Sensitivity**: the one route-loadable index's 4 rows are all
   `sensitivityLevel: public`, verified directly from that file's contents.

`UC-03` (non-public data) is parked and MUST NOT be treated as reachable until
a source-verified entitlement/grant owner exists, independent of whether a
future route-loadable index ever contains non-public rows.

## Deterministic And Live Proof Separation

Deterministic proof today is exactly the B1/BR1 evidence already accepted:
LPCI focused suite (7 files, 99 tests), execute repair suite (3 files, 5
tests), full non-live regression (304 files, 3397 passed, 2 skipped), with
proven zero/one mocked-fetch call counts. No live provider call has been made
against this route by any governed artifact reviewed in this intake. Any
future live proof requires its own fresh GC-018, a resolved provider-lane
owner, and explicit operator release; it is not implied by this roadmap.

## Recommended Next Tranche

At most one candidate is recommended: `UC-01`, using the existing LPCI1-T5
owner and the one currently route-loadable synthetic index
(`GOVERNANCE_PILOT_NO_LEGAL_CORPUS-index.json`), demonstrated runnable today
with the query `nghi phep nam`. It requires no new consumer, no new
entitlement owner, and no corpus registration work.

`UC-01` follows exactly one lifecycle chain, with no alternate branch. Steps 1
and 2 were completed by the later operator-authorized D1 packet and independent
review; this roadmap did not itself grant them:

1. **Fresh DESIGN-only authority** may open a DESIGN tranche for `UC-01`.
   That DESIGN must include the `UC-04` decision: reuse or compose the existing
   Model Gateway owner for the LPCI-specific binding and define its documented
   config contract. This intake grants no DESIGN authority itself.
2. **The complete DESIGN, including the `UC-04` binding decision, must be
   independently accepted.** DESIGN completion or acceptance cannot be
   inferred from this intake and cannot be bypassed by provider readiness.
3. **Only after step 2** may a separate, fresh operator authority open a
   source-verified BUILD tranche. BUILD must implement the accepted UC-04
   composition/config contract, including Model Gateway-owned trim-empty
   credential hardening, with deterministic network-free proof.
4. **Only after accepted BUILD evidence** may another separate fresh authority
   grant provider/live-proof scope. DESIGN or BUILD authority never grants a
   provider call or live proof.

Current continuation: the complete UC-01 DESIGN, bounded B2 BUILD, one
provider-binding proof, and one signed synthetic-public full-route proof are
independently accepted. The last proof recorded one route invocation, one
provider call, zero retries, HTTP 200, `ANSWER_EMITTED`, `PUBLIC_ONLY`, and
required audit correlations. No retry, release, hosted, deployment,
production, public, or later-roadmap authority follows.

The separately authorized UC-02 reopen discovery is independently accepted as
`UC02_REOPEN_CONDITION_NOT_MET`. Current source has no named real UC-02
consumer, no real UC-02 route-compatible public index, and no corresponding
consumer-to-corpus-to-route binding. UC-02 remains parked; discovery creates no
DESIGN, BUILD, mutation, or live authority.

The separately authorized UC-01 release-readiness discovery is independently
accepted as `UC01_RELEASE_READINESS_GAPS_REQUIRE_REMEDIATION`. Route
authorization is PRESENT; auth/RBAC, secret/config, and health/failure are
PARTIAL; rate limits/quotas, durable audit/observability, and deploy/rollback
are GAP; public export is NOT_APPLICABLE and `DEFERRED_PRIVATE_ONLY`. The lane
is parked pending fresh authority for
`UC01_RELEASE_HARDENING_DESIGN_SPEC_ONLY`; discovery grants no remediation,
BUILD, hosted action, deployment, production, or public authority.

## Explicit Parked Lanes

- `UC-02`: `PARKED_REOPEN_CONDITION_NOT_MET` - accepted discovery found A/B/C
  all NOT_MET: no named real consumer, no matching real public index, and no
  direct consumer-to-corpus-to-route binding. PolicyLocal remains an LPCI2
  registry counterexample only.
- `UC-03`: `PARKED_MISSING_ENTITLEMENT_OWNER` - no non-public grant/entitlement
  owner exists in current source.
- `UC-04`: `RUNTIME_BINDING_AND_BOUNDED_FULL_ROUTE_PROOF_ACCEPTED` - the accepted B2 BUILD
  composes LPCI with the existing Model Gateway, documents the atomic
  three-variable contract, and proves fail-closed behavior network-free. Live
  invocation and one separately authorized full-route proof are accepted. Any
  additional call or broader proof requires another fresh operator grant.
- `UC-05`: `NO_CURRENT_VALUE_WITH_REOPEN_CONDITION` - no non-test, non-dashboard
  caller exists.
- `UC-06`: `REJECT_DUPLICATE_OWNER` - the existing route already owns this
  responsibility.
- `UC-01 release readiness`: `GAPS_REQUIRE_REMEDIATION` - direct operational
  gaps remain in route rate limiting, durable minimized audit/telemetry, role
  policy, timeout/health coverage, and deploy/rollback controls. Only a fresh
  documentation-only design/spec packet may continue this lane.
- DESIGN and BUILD were opened by later operator GC-018 packets and are
  independently accepted; this roadmap did not itself grant them. SPEC,
  provider/live, persistence, vector/RAG, non-public grants, public-sync,
  deployment, and readiness remain parked for every candidate in this roadmap
  regardless of rank.

## Reopen Conditions

| Lane | Concrete reopen condition |
|---|---|
| `UC-02` | NOT_MET at accepted 2026-08-10 discovery. Reopen only when simultaneously: (a) a named, source-verified real organization/internal-policy non-test consumer; (b) a matching route-compatible `<corpusId>-index.json` whose admitted rows are public; and (c) direct source proving that consumer selects that corpus and calls `/api/lpci/query`. Registry membership, the synthetic pilot, or any single/paired condition is insufficient. |
| `UC-03` | a governed entitlement/grant-store owner is source-verified to exist and is named with a file path and symbol |
| `UC-04` | both simultaneously: (a) the LPCI-specific binding of `LPCI_LLM_API_KEY`, `LPCI_LLM_ENDPOINT`, and `LPCI_LLM_MODEL` to the existing Model Gateway owner is source-verified in runtime code (reuse/compose, not a new parallel owner); and (b) a documented config contract for that binding exists. `.env.example` naming alone, without source-verified Model Gateway integration, is insufficient. Live-proof authority additionally requires a fresh separate operator grant. |
| `UC-05` | a real non-test, non-dashboard caller of `/api/lpci/query` is source-verified to exist |
| `UC-01` (DESIGN-only eligibility) | SATISFIED: later D1 authority produced an independently accepted complete DESIGN including UC-04 |
| `UC-01` (BUILD eligibility) | SATISFIED: B2 implemented and independently accepted the source-verified Model Gateway/cvf-web binding with deterministic network-free proof |
| `UC-01` (provider-binding live-proof eligibility) | SATISFIED_AND_CONSUMED: exact operator token released one binding attempt; reviewer accepted its sanitized receipt. |
| `UC-01` (full-route live-proof eligibility) | SATISFIED_AND_CONSUMED: exact full-route token released one signed synthetic-public attempt; reviewer accepted route 1/provider 1/retry 0 and the sanitized correlated receipt. No retry, release, production, deployment, public, or later-lane authority follows. |
| `UC-01` (release-hardening eligibility) | DISCOVERY_SATISFIED_AND_CONSUMED: accepted discovery identified operational gaps. Reopen only with fresh authority for documentation-only design/spec defining source-verified ownership and acceptance contracts before BUILD. |

## Acceptance Case Planning For A Future Tranche (Not Executed)

This is planning only; no provider is called and no test is executed by this
roadmap.

| Case | Shape | Provider invocation count expected |
|---|---|---|
| positive public-evidence case | a valid public admitted record with eligible evidence; expect `ANSWER_EMITTED` | exactly one |
| no-evidence fail-closed case | admitted record missing/blank/oversized `contentSnippet`; expect `GROUNDING_EVIDENCE_UNAVAILABLE` | exactly zero |
| non-public denial case | all matched rows non-public; expect `PHASE1_NEGATIVE` `FILTERED_OUT` | exactly zero |
| prompt-injection boundary case | evidence field containing role labels, delimiters, or instruction-like text; expect one parseable JSON evidence object with no second prompt section | exactly one (if otherwise eligible) or zero (if this pushes the record over an existing bound) |
| no-provider-configured case | `LPCI_LLM_API_KEY` absent; expect `NO_PROVIDER_CONFIGURED` | exactly zero |
| provider-error minimization case | provider call throws or returns non-OK; expect `PROVIDER_ERROR` with the fixed safe message only | exactly one attempted, zero successful |

These cases restate the already-accepted S1 P1-P8/F1-F16 synthetic matrix and
add no new runtime requirement; they are recorded here only to bound what a
future DESIGN/SPEC tranche must still cover for a context-to-LLM use case.

## Design Control Gate

Gate status: `DESIGN_ACCEPTED_BOUNDED_NO_BUILD_OR_LIVE_RELEASED`.

| Gate question | Current answer | Effect |
|---|---|---|
| Is a concrete use case identified with a named consumer, source, and governance stages? | Yes, `UC-01` | eligible for a future fresh DESIGN authorization |
| Is a provider-lane owner selected for `LPCI_LLM_API_KEY`/`LPCI_LLM_ENDPOINT`/`LPCI_LLM_MODEL`? | Yes at DESIGN level: thin composition over existing Model Gateway | runtime binding/config evidence remains a BUILD prerequisite |
| Is a non-public entitlement owner selected? | No | `UC-03` remains parked; not required for `UC-01` |
| Is DESIGN authorized by this roadmap? | No; later operator authority opened and independent review accepted D1 | no authority inheritance to later phases |
| Is BUILD, provider, or live-proof authorized by this roadmap? | No authority originates here; later packets separately authorized and completed B2 BUILD, one provider-binding proof, and one full-route proof | no retry, release, deployment, production, public, or roadmap continuation follows |

## Dispatch Boundary

The later D1 DESIGN and B2 BUILD were independently accepted. Separate exact
operator tokens then opened one provider-binding proof and one signed
synthetic-public full-route proof. The latter produced route HTTP 200,
provider HTTP 200, `ANSWER_EMITTED`, `PUBLIC_ONLY`, one route invocation, one
provider call, zero retries, and all required audit correlations; the reviewer
accepted only sanitized metadata. No retry, release/hosted proof, additional
provider call, implementation, persistence, vector/RAG, non-public grant,
public-sync, deployment, production readiness, or later roadmap continuation
is authorized.

## Work Plan

| Step | Documentation-only action | Output | Stop condition |
|---|---|---|---|
| `CTL-T0.1` | source-verify current LPCI1-Web route, helpers, dashboard, auth registry, corpus registry, and env contract | Current Source Verification table | stop before selecting a use case |
| `CTL-T0.2` | enumerate and classify concrete context-to-LLM use-case candidates | Use-Case Candidate Matrix | stop before designing any interface |
| `CTL-T0.3` | rank candidates by value/risk and recommend at most one next tranche | Value And Risk Ranking; Recommended Next Tranche | stop before DESIGN |
| `CTL-T0.4` | record parked lanes and concrete reopen conditions | Explicit Parked Lanes; Reopen Conditions | stop before implementation |

## Acceptance Criteria

| ID | Criterion | Required disposition |
|---|---|---|
| `AC-01` | operator authority is recorded as documentation-only intake/roadmap | `PASS_REQUIRED` |
| `AC-02` | current source is verified against the operator's nine intake questions | `PASS_REQUIRED` |
| `AC-03` | provider/API-key ownership is distinguished from source-presence | `PASS_REQUIRED` |
| `AC-04` | every candidate carries a disposition from the operator's required enum | `PASS_REQUIRED` |
| `AC-05` | at most one candidate is recommended for next tranche | `PASS_REQUIRED` |
| `AC-06` | public/non-public boundary is stated using current registry evidence only | `PASS_REQUIRED` |
| `AC-07` | no DESIGN, SPEC, BUILD, provider, live, persistence, vector/RAG, non-public grant, public-sync, or deployment authority is claimed or released | `PASS_REQUIRED` |

## Negative Search And Collision Discipline

- Search roots: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src` (LPCI files),
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.example`,
  `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`,
  `docs/roadmaps/`, `docs/reviews/`, `docs/reference/` LPCI-named files.
- Search commands: `Grep` for `lpci` (case-insensitive) across cvf-web `src`;
  `Grep` for `LPCI_LLM_API_KEY`/`LPCI_LLM_ENDPOINT`/`LPCI_LLM_MODEL` across
  cvf-web `src`; `Grep` for `/api/lpci/query` across cvf-web `src`; direct read
  of `.env.example`; `git check-ignore -v` on `.env.local`/`.env.netlify`
  (contents not read); direct read of the corpus registry JSON.
- Coverage: current LPCI1-Web source, tests, accepted S1 spec, B1/BR1
  completions, current-owner defect intake roadmap, prior LPCI product
  roadmaps, and the corpus registry. Generated dependency trees and Git
  internals were excluded.
- Same-token collision results: `lpci` and `provider` occur across many
  unrelated CVF surfaces (LPCI2 PolicyLocal, general provider docs); those
  occurrences are non-authoritative for this route unless confirmed in the
  exact cited files above.
- Disposition: no other caller, provider owner, or entitlement owner was found
  within the stated search roots; absence claims are bounded to those roots and
  exact symbols.

## Machine Closure Package

N/A with reason: this roadmap's top status is
`LPCI1_WEB_UC01_RELEASE_READINESS_GAPS_PARKED_PENDING_FRESH_DESIGN_SPEC_AUTHORITY`,
an accepted bounded continuation state rather than a closed-equivalent token.
Intake closure remains recorded in the R3 completion; D1 and B2 acceptance are
recorded in their separate completion reviews.

## ADIF Defect Registry Disclosure

Resolver query executed: `python governance/compat/run_adif_defect_resolver.py --role worker --max-results 50 --json`

Total candidates returned: 38 (not truncated). Every returned `defectId`:

`ADIF-0001`, `ADIF-0002`, `ADIF-0008`, `ADIF-0012`, `ADIF-0014`, `ADIF-0015`,
`ADIF-0019`, `ADIF-0020`, `ADIF-0021`, `ADIF-0027`, `ADIF-0028`, `ADIF-0029`,
`ADIF-0030`, `ADIF-0033`, `ADIF-0034`, `ADIF-0035`, `ADIF-0037`, `ADIF-0038`,
`ADIF-0040`, `ADIF-0041`, `ADIF-0042`, `ADIF-0044`, `ADIF-0045`, `ADIF-0047`,
`ADIF-0048`, `ADIF-0050`, `ADIF-0007`, `ADIF-0010`, `ADIF-0011`, `ADIF-0022`,
`ADIF-0023`, `ADIF-0024`, `ADIF-0031`, `ADIF-0032`, `ADIF-0036`, `ADIF-0039`,
`ADIF-0043`, `ADIF-0049`.

Most directly applicable to this documentation-only intake: `ADIF-0008`
(reusable lesson must not remain only in provider memory - honored by writing
findings into this governed roadmap, not session memory); `ADIF-0002`
(provider-local interaction accepted as authority - honored by treating the
`.env.local` file's mere presence as non-authoritative for provider readiness);
`ADIF-0014` (scope-triggered absorption control evaded by completeness
silence - not directly triggered here because no external-repository
absorption occurs, recorded for completeness).

## Verification/Evidence

The original intake authoring executed no runtime, test, or provider command.
The later B2 closure independently ran 70 deterministic focused tests,
TypeScript checks, scoped lint, and local governance gates; those receipts are
recorded in the B2 completion review. Provider/network/live execution count
remains zero.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author / documentation-only intake worker |
| Provider or surface | local private provenance repository |
| Session or invocation | `lpci1-web-context-to-llm-use-case-intake-2026-08-09` |
| Working directory | repository root |
| Command or tool surface | `Read`, `Grep`, `Bash` (`git rev-parse`, `git status --short`, `git check-ignore -v`, one Python JSON read, `run_adif_defect_resolver.py`) |
| Target paths | this roadmap; the paired worker return |
| Allowed scope source | `AUTHORIZE_FRESH_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_INTAKE_ROADMAP_DOCUMENTATION_ONLY` |
| Before status evidence | HEAD `95340497fe4ca835ee85d44f311f651632b9c606`; `git status --short` clean |
| After status evidence | two new untracked documentation paths; no other path changed |
| Diff evidence | `git status --short` after authoring, recorded in the paired worker return |
| Approval boundary | documentation-only intake/roadmap authoring |
| Claim boundary | no runtime/test/provider/live/network/persistence/vector-RAG/non-public-grant/public-sync/deployment/commit action |
| Agent type | dispatch author / no-commit documentation worker |
| Invocation ID | `lpci1-web-context-to-llm-use-case-intake-2026-08-09` |
| Expected manifest | this roadmap; the paired worker return |
| Actual changed set | this roadmap; the paired worker return |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | documentation-only context-to-LLM use-case intake and candidate ranking |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | `CLAIM_REJECTED_NO_RECEIPT`: file reads and grep/JSON inspection are not a CVF live receipt |
| actionEvidence | `ACTION_EVIDENCE_PRESENT`: exact source citations and search commands are recorded above |
| invocationBoundary | repository-local reads and searches only |
| interceptionBoundary | no provider or live interception claim |
| claimLanguage | candidate intake and ranking only; no runtime, provider, or readiness claim |
| forbiddenExpansion | no DESIGN, SPEC, BUILD, provider/live, persistence, vector/RAG, non-public grant, public-sync, deployment, or readiness claim |

## Related Artifacts

The LPCI dashboard consumer page is source-verified at the full contiguous
repository path
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.tsx`.
The bounded R3 checker repair accepts this balanced parenthesized Next.js route
segment while continuing to reject malformed unbalanced path citations.

- `docs/reference/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_SPEC_2026-08-08.md`
- `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD_COMPLETION_2026-08-09.md`
- `docs/reviews/CVF_LPCI1_WEB_BUILD_EXTERNAL_BASELINE_REPAIR_COMPLETION_2026-08-09.md`
- `docs/roadmaps/CVF_LPCI_CURRENT_OWNER_GROUNDING_AND_CLEARANCE_DEFECT_INTAKE_ROADMAP_2026-08-08.md`

## External Knowledge Intake Routing

Chain map reference: `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`.

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` reviewed; no route applies because no external repository, copied folder, or third-party source is absorbed by this documentation-only roadmap or its R1/R2 repairs |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_TRIGGERED: this roadmap absorbs no external repository, copied folder, or third-party source |
| Matching local-view guard | N/A with reason: no absorption guard applies because no external repository, copied folder, or third-party source is absorbed by this documentation-only roadmap |
| Owner surface | existing CVF-governed LPCI1-Web source and prior CVF-governed artifacts inside this repository |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | no external-repository or third-party absorption occurs in this documentation-only roadmap |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance intake with internal source citations; no
public-safe export packet or public-sync authority exists for this roadmap.

## Claim Boundary

This roadmap began as a documentation-only context-to-LLM use-case intake and
now records later independently accepted D1 DESIGN and B2 BUILD evidence.
Those later packets implemented a bounded local provider-binding seam and
deterministic tests; they did not call a provider, read a real credential,
open non-public access, public-sync, deploy, or establish readiness. Any live
proof still requires fresh explicit operator authority and a new governed
packet.
