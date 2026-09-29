# CVF GC-018 Baseline - LPCI1 Web UC-01 Full Route Live Proof

Memory class: governed-dispatch-baseline

Status: CLOSED_PASS_BOUNDED_FULL_ROUTE_LIVE_PROOF_ACCEPTED

Batch ID: LPCI1-WEB-UC01-ROUTE-LIVE

Dispatch base head: `77c60d6cf`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: primary reviewer/dispatcher

Worker target: delegated worker

## Authorization / Decision

The operator supplied the exact token
`AUTHORIZE_LPCI1_WEB_UC01_FULL_ROUTE_LIVE_PROOF_ONLY` on 2026-08-09. This
releases one bounded invocation of the current `/api/lpci/query` POST handler
with the synthetic public corpus and current OpenAI binding. It does not
authorize retry, source implementation, a server/deployment, release or
production readiness, public sync, or any other roadmap lane.

## Purpose

Obtain fresh secret-safe evidence that the existing route can authorize a
signed local service request, admit/retrieve public synthetic evidence, invoke
the current provider binding exactly once, emit an answer, and correlate its
audit receipt. Missing prerequisites or any failure is a classified bounded
result with no retry.

## Baseline Decision

Proceed with one no-commit evidence-only worker. The worker may create only
the two review outputs named by the paired work order. It may enter the
provider fetch boundary at most once after all local gates and credential
presence controls pass.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| B2 binding accepted | material commit `5c86f6d77`; B2 completion review | ACCEPT |
| binding-only live proof accepted | material commit `1c808fd39`; `docs/reviews/CVF_LPCI1_WEB_UC01_PROVIDER_LIVE_PROOF_COMPLETION_2026-08-09.md` | ACCEPT_BOUNDED |
| closure continuity synchronized | clean dispatch base `77c60d6cf`; active handoff V56 | ACCEPT |
| full-route live checkpoint | exact operator token recorded above | ACCEPT_BOUNDED_ONE_ATTEMPT |
| live diagnostic rule | `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldTool | `governance/compat/build_dispatch_packet_scaffold.py` |
| packetKind | `runtime-provider-live` |
| scaffoldBase | `77c60d6cf` |
| scaffoldDisposition | used as starting profile and completed against current LPCI route/auth/source |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id LPCI1-WEB-UC01-ROUTE-LIVE --title "LPCI1 Web UC-01 Full Route Live Proof" --date 2026-08-09 --base 77c60d6cf --commit-mode WORKER_MUST_NOT_COMMIT --dependency "provider-binding live closure 1c808fd39" --stdout --include-worker-return-skeleton` |
| generatedProfile | runtime-provider-live plus signed-route evidence-only no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact route/auth/corpus source verification, one-fetch limit, secret controls, two-path manifest, diagnostics, and reviewer conversion |
| checkerReadAheadConfirmation | applicable dispatch, handoff, live, worker-return, corpus, and file-size guards reviewed |
| docOnlyNewFields | `LPCI1_WEB_UC01_FULL_ROUTE_LIVE_PROOF_PASS`; `LPCI1_WEB_UC01_FULL_ROUTE_LIVE_PROOF_BLOCKED` |
| claimBoundary | scaffold provenance is not execution or live-result evidence |

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `DISPATCHED`; `WORKER_MUST_NOT_COMMIT`; `NONE_RETURNED`; `DEFERRED_PRIVATE_ONLY`; `Checker Source Read-Ahead Block` |
| gateRunPurpose | confirmation and evidence after checker-shape review, not first discovery |
| claimBoundary | read-ahead is not route execution or reviewer acceptance evidence |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`LPCI web UC-01 full route live proof`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "LPCI web UC-01 full route live proof" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | standard live diagnostics, signed-route correlation, one-fetch, secret, and no-commit controls apply |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| binding-only proof prerequisite | EXISTS | `docs/reviews/CVF_LPCI1_WEB_UC01_PROVIDER_LIVE_PROOF_COMPLETION_2026-08-09.md` | status and findings | `LPCI1_WEB_UC01_PROVIDER_LIVE_PROOF_PASS` | prior reviewer closure | ACCEPT |
| route entrypoint | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | exported handler | `POST` | LPCI query route | ACCEPT |
| route governance owner | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | registry and authorization function | `authorizeRouteGovernanceProof` | route governance proof | ACCEPT |
| signed service-token contract | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | compute and verify functions | `computeServiceRequestSignature`; `verifyServiceTokenRequest` | service-token auth | ACCEPT |
| route risk/config | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | query registry row | `/api/lpci/query` | route governance registry | ACCEPT |
| registered synthetic corpus | EXISTS | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | matching corpus entry | `GOVERNANCE_PILOT_NO_LEGAL_CORPUS` | GC-051 registry | ACCEPT |
| route-loadable public fixture | EXISTS | `docs/corpus-intelligence/GOVERNANCE_PILOT_NO_LEGAL_CORPUS-index.json` | four-row index | `sensitivityLevel` | LPCI synthetic index | ACCEPT |
| runnable bounded query seam | RUNTIME_BEHAVIOR | `docs/corpus-intelligence/GOVERNANCE_PILOT_NO_LEGAL_CORPUS-index.json` | matching public snippets | `nghi phep nam` | LPCI retrieval pipeline | ACCEPT |
| provider call occurs after clearance/projection | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | post-retrieval provider branch | `executeLpciProviderBinding` | LPCI query route | ACCEPT |
| exact provider pair/key | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts` | constants and credential reference | `LPCI_LLM_API_KEY`; `OPENAI_MODEL_ID` | LPCI provider binding | ACCEPT |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | current source plus one fresh signed route/provider attempt maximum |
| verifiedBase | `77c60d6cf` |
| staleEvidenceRule | binding-only receipt and synthetic tests cannot substitute for this full-route attempt |

## Runtime Expansion Control Block

| Field | Value |
|---|---|
| expansionClass | evidence-only direct invocation of existing route handler |
| existingOwnerReuse | route governance, retrieval/projection/audit, LPCI provider binding, Model Gateway |
| sideEffectCeiling | one route invocation and one provider fetch entry maximum |
| retryCeiling | zero retries |
| server/deploy | forbidden; no daemon or hosted route |
| forbiddenOwners | runtime source, tests, packages, config, session state, public sync, deployment, production |

## Live Credential And Auth Control Block

| Field | Value |
|---|---|
| provider credential | `LPCI_LLM_API_KEY` only, process-local load from ignored cvf-web environment file |
| provider pair | `openai/gpt-4o`; canonical endpoint only |
| route auth | invocation-local random `CVF_SERVICE_TOKEN`, used as configured/presented token and HMAC key in memory only |
| signature | current timestamp plus exact request body through `computeServiceRequestSignature` |
| missing provider credential | diagnostic `missing_api_key`; zero route/provider calls; no retry |
| persistence rule | never print, echo, hash, copy, commit, or persist raw credentials, service token, signature, headers, request body, provider body, or answer |
| alias rule | do not map any other provider key into `LPCI_LLM_API_KEY` |

## Allowed Scope

Worker may create exactly the sanitized evidence JSON and worker return named
in the paired work order. Read-only current-source inspection and one temporary
process-local route invocation are allowed. Worker must not stage or commit.

## Forbidden Scope

All other files; source/config/package/test edits; more than one route
invocation or provider fetch; retry; raw request/response persistence; secret
output; browser/UI; server daemon; broad release bundle; deployment;
production; public sync; session mutation; stage; commit; push.

## Evidence / Verification

Evidence must record route/provider call counts, retry count, HTTP/outcome,
route governance decision/auth mode/risk class, public-only authorization,
evidence outcome, audit correlation, matched-source count, latency, and answer
length/digest only. Failure requires the full secret-safe diagnostic object.

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| authorization | exact full-route-proof-only token | exact token | PASS |
| route/provider attempts | one / one maximum | 1 / 1 | PASS |
| retries | zero | 0 | PASS |
| route/provider HTTP | successful bounded result | 200 / 200 | PASS |
| result | public evidence answer emitted | `ANSWER_EMITTED`; `PUBLIC_ONLY` | PASS |
| route proof | signed allowed R2 service-token request | `ALLOW`; `service_token`; `R2` | PASS |
| audit correlation | all required correlations true | all true; matched source count 1 | PASS |
| persistence boundary | sanitized metadata only | length/digest only; no secret/body/query/answer | PASS |
| worker commit | forbidden | HEAD unchanged; staging empty | PASS |

## Closure Checklist

- [x] Exact operator authority and accepted prerequisites verified.
- [x] Pre-implementation passed before credential load and network action.
- [x] Exactly one route and provider attempt with zero retries verified.
- [x] Receipt and worker return independently reviewed.
- [x] Secret and raw-content persistence boundaries verified.
- [x] Focused tests and reviewer gates passed.
- [x] Broader release, deployment, public, and continuation lanes remain parked.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired work order | `CLOSED_PASS_BOUNDED_FULL_ROUTE_LIVE_PROOF_ACCEPTED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LPCI1_WEB_UC01_FULL_ROUTE_LIVE_PROOF_COMPLETION_2026-08-09.md` | reviewer token and bounded disposition | PASS |
| Worker return | named worker return | `COMPLETE_PENDING_REVIEW`; accepted by completion | PASS |
| Evidence JSON | named receipt | route 1; provider 1; retry 0; HTTP 200 | PASS |
| Roadmap state | LPCI1 roadmap | `LPCI1_WEB_UC01_FULL_ROUTE_LIVE_PROOF_ACCEPTED_BOUNDED_NO_RELEASE_OR_CONTINUATION` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | existing corpus owner; no registry mutation | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | existing lookup guidance; no registry mutation | PASS |
| External evidence digest | sanitized JSON receipt | sha256 `0298701A1332BDC2C5A88702F92425F8FB97DEF18B9F70F9CD5E99B5358E3634` | PASS |
| System loop interlock | binding proof -> full-route proof -> stop | broader lanes parked | PASS |
| Session continuity | protected session state and handoff | separate sync after material commit | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private provenance live evidence and public sync is not
authorized by the operator token.

## Claim Boundary

This baseline authorizes one fresh local full-route attempt only. Success
would prove one signed synthetic-public route request at one timestamp. It
would not certify release quality, hosted behavior, ongoing availability,
output quality, production, deployment, public availability, arbitrary
providers/corpora, or any other LPCI use case.
