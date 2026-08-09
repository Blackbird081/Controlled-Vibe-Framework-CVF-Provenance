# CVF GC-018 Baseline - LPCI1 Web UC-01 Provider Live Proof

Memory class: governed-dispatch-baseline

Status: DISPATCHED

Batch ID: LPCI1-WEB-UC01-LIVE

Dispatch base head: `102fcc890`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Operator

Reviewer owner: primary reviewer/dispatcher

Worker target: delegated worker

## Authorization / Decision

The operator supplied the exact token
`AUTHORIZE_LPCI1_WEB_UC01_PROVIDER_LIVE_PROOF_ONLY` on 2026-08-09. This
releases one bounded proof attempt through the already-built UC-01 LPCI Model
Gateway provider binding. It does not authorize source implementation,
deployment, production readiness, public sync, or any other roadmap lane.

## Purpose

Obtain fresh, secret-safe evidence for the accepted B2 provider binding using
at most one real OpenAI provider request. A missing compatible credential is a
valid classified blocked result and must consume zero network calls.

## Baseline Decision

Proceed with one no-commit, evidence-only worker. The worker may create only
the two review outputs named by the paired work order and may attempt at most
one provider request after all local gates and credential-presence controls
pass.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| B2 implementation accepted | material commit `5c86f6d77`; `docs/reviews/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_BUILD_COMPLETION_2026-08-09.md` | ACCEPT |
| B2 continuity synchronized | clean dispatch base `102fcc890`; active handoff `AGENT_HANDOFF_V56_2026-08-09.md` | ACCEPT |
| provider/live checkpoint | exact operator token recorded above | ACCEPT_BOUNDED_ONE_ATTEMPT |
| live diagnostic rule | `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldTool | `governance/compat/build_dispatch_packet_scaffold.py` |
| packetKind | `runtime-provider-live` |
| scaffoldBase | `102fcc890` |
| scaffoldDisposition | used as starting profile and completed against current LPCI source |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id LPCI1-WEB-UC01-LIVE --title "LPCI1 Web UC-01 Provider Live Proof" --date 2026-08-09 --base 102fcc890 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "B2 accepted at 5c86f6d77" --stdout --include-worker-return-skeleton` |
| generatedProfile | runtime-provider-live plus evidence-only no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact LPCI source verification, one-attempt limit, secret controls, two-path manifest, diagnostics, and reviewer conversion |
| checkerReadAheadConfirmation | applicable dispatch, handoff, live, worker-return, and file-size guards reviewed |
| docOnlyNewFields | `LPCI1_WEB_UC01_PROVIDER_LIVE_PROOF_PASS`; `LPCI1_WEB_UC01_PROVIDER_LIVE_PROOF_BLOCKED` |
| claimBoundary | scaffold provenance is not execution or live-result evidence |

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `DISPATCHED`; `WORKER_MUST_NOT_COMMIT`; `NONE_RETURNED`; `DEFERRED_PRIVATE_ONLY`; `Checker Source Read-Ahead Block` |
| gateRunPurpose | confirm checker-safe dispatch shape before worker execution |
| claimBoundary | read-ahead is not live execution or reviewer acceptance evidence |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`LPCI web UC-01 provider live proof`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "LPCI web UC-01 provider live proof" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | standard live diagnostic, one-attempt, secret, and no-commit controls apply |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| B2 accepted bounded implementation | EXISTS | `docs/reviews/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_BUILD_COMPLETION_2026-08-09.md` | top status and Findings | `LPCI1_WEB_UC01_PROVIDER_BINDING_BUILD_ACCEPT` | B2 completion review | ACCEPT |
| live authority remained separately gated | EXISTS | `docs/roadmaps/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_ROADMAP_2026-08-09.md` | UC-04 reopen rule | `PARKED_PROVIDER_OR_LIVE_AUTHORITY` | LPCI1 roadmap | ACCEPT |
| exact supported pair | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts` | constants and config resolver | `OPENAI_PROVIDER_ID`; `OPENAI_MODEL_ID` | LPCI provider binding | ACCEPT |
| exact endpoint | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts` | constants and `resolveEndpoint` | `OPENAI_ENDPOINT` | LPCI provider binding | ACCEPT |
| credential key contract | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts` | credential reference | `LPCI_LLM_API_KEY` | `CredentialBoundary` integration | ACCEPT |
| provider execution owner | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts` | `executeLpciProviderBinding` and `buildBridge` | `executeLpciProviderBinding` | LPCI thin composition over Model Gateway | ACCEPT |
| route invokes binding only after eligible evidence | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | provider invocation after projection and abstention exits | `executeLpciProviderBinding` | LPCI query route | ACCEPT |
| adapter makes OpenAI-compatible POST | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts` | `createOpenAiCompatibleExecuteAdapter` | `fetchImpl` | Model Gateway adapter | ACCEPT |
| operator-key continuity location | EXISTS | `AGENTS.md` | Mandatory Live Governance Proof, operator-key continuity note | ignored local environment file | operator environment boundary | ACCEPT |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES |
| runtimeMutationAuthorized | NO |
| freshnessVerificationMode | current source plus one fresh provider attempt maximum |
| verifiedBase | `102fcc890` |
| staleEvidenceRule | B2 synthetic tests and older provider receipts cannot substitute for this fresh attempt |

## Runtime Expansion Control Block

| Field | Value |
|---|---|
| expansionClass | evidence-only live proof over existing binding |
| existingOwnerReuse | `executeLpciProviderBinding` and Model Gateway bridge/adapter |
| sideEffectCeiling | one provider request maximum; zero if compatible credential absent |
| retryCeiling | zero retries |
| forbiddenOwners | runtime source, tests, packages, config, session state, public sync, deployment, production |

## Live Credential Control Block

| Field | Value |
|---|---|
| required process variable | `LPCI_LLM_API_KEY` |
| required model | `openai/gpt-4o` |
| required endpoint | `https://api.openai.com/v1/chat/completions` |
| load boundary | ignored local environment file into the live command process only |
| missing credential result | diagnostic class `missing_api_key`; zero network calls; no retry |
| persistence rule | never print, echo, hash, copy, commit, or persist the raw value or authorization header |
| alias rule | do not map DashScope, Alibaba, DeepSeek, or generic OpenAI variables into `LPCI_LLM_API_KEY` |

## Allowed Scope

Worker may create exactly the sanitized evidence JSON and worker return named
in the paired work order. Read-only current-source inspection and one temporary
process-local invocation are allowed. Worker must not stage or commit.

## Forbidden Scope

All other files; source/config/package edits; more than one provider request;
retry; raw response persistence; secret reads through output-producing
commands; browser/UI; server daemon; release or broad governance bundle;
deployment; production; public sync; session mutation; stage; commit; push.

## Evidence / Verification

Evidence must record call count, retry count, provider/model/endpoint class,
latency, bounded result, a safe response digest only after excluding secrets,
and the mandatory diagnostic object on missing/failing/empty results. The raw
provider body and generated answer must not be persisted.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private provenance live evidence and public sync is not
authorized by the operator token.

## Claim Boundary

This baseline authorizes one fresh UC-01 provider-binding attempt only. A
successful result proves only that this local binding completed one request at
this time. A blocked result proves only its classified cause. Neither result
certifies the full route, release readiness, production, deployment, public
availability, arbitrary models/providers, or any other LPCI use case.
