# CVF GC-018 Baseline - LPCI1 Web UC-01 Context-To-LLM Provider Binding Build

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: LPCI1-WEB-UC01-B2

Date: 2026-08-09

dispatchBaseHead: `542fb041d`

Commit mode: WORKER_MUST_NOT_COMMIT

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `Source Verification Block`; `ADIF Defect Registry Disclosure`; `Agent Operation Trace Block`; `Machine Closure Package` |
| gateRunPurpose | confirmation and evidence after checker-shape review, not first discovery |
| claimBoundary | read-ahead confirms packet-shape expectations only; it does not prove implementation or closure |

## Purpose

Authorize one bounded BUILD-only tranche that consumes the independently
accepted UC-01 provider-binding DESIGN. The worker must replace route-local
provider fetch ownership with a thin LPCI composition over the existing Model
Gateway, harden trim-empty credential handling at the credential owner, and
prove the result with deterministic network-free tests.

Provider/live proof, secret inspection, public-sync, deployment, persistence,
vector/RAG, corpus mutation, readiness, and release claims remain forbidden.

## Target / Source

Target: the current LPCI query route, its new thin provider-binding seam, the
existing Model Gateway bridge/credential/adapter owners, package import seam,
safe example configuration, and focused deterministic tests.

Source authority: accepted D1 audit and completion, current runtime source at
`542fb041d`, canonical package manifests, and this GC-018 packet.

## Scope / Methodology

The worker performs one source-freshness pass, implements only the exact
manifest below, runs Model Gateway and cvf-web focused/static/non-live checks,
files one worker return, and leaves everything uncommitted and unstaged.

The route may invoke the binding only after the existing S1 clearance and
projection boundary has produced an eligible answer candidate. All other S1
outcomes retain zero bridge, adapter, and network calls.

## Authority And Scope

Verbatim operator authority: `tiep tuc`.

Normalized authority token:
`AUTHORIZE_LPCI1_WEB_UC01_PROVIDER_BINDING_BUILD_ONLY`.

The operator continued the current next allowed move after D1 bounded
acceptance. This authorizes local source, package, example-config, and
deterministic test mutation only. It does not authorize reading ignored local
environment files, using real credentials, provider calls, live tests, browser
proof, public export, push, or deployment.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id LPCI1-WEB-UC01-B2 --title "LPCI1 Web UC-01 Context-To-LLM Provider Binding Build" --date 2026-08-09 --base 542fb041d --commit-mode WORKER_MUST_NOT_COMMIT --dependency "UC-01 D1 closure 2e770480c" --include-worker-return-skeleton --stdout` |
| generatedProfile | web route plus Model Gateway package integration; deterministic network-free tests |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact source verification, fifteen-path manifest, D1 SP-01-SP-12, AHB/AOT, no-secret/no-live boundary |
| checkerReadAheadConfirmation | dispatch, structural, authority, AOT, scaffold, handoff, and worker-return contracts reviewed |
| docOnlyNewFields | isolated in New Doc-Only Fields until implementation |
| claimBoundary | scaffold provenance only |

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition | Status |
|---|---|---|---|---|
| UC-01 D1 DESIGN | `docs/audits/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_2026-08-09.md` | `2e770480c` | `INDEPENDENTLY_ACCEPTED_BOUNDED` | PASS |
| UC-01 D1 completion | `docs/reviews/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_COMPLETION_2026-08-09.md` | `2e770480c` | `CLOSED_PASS_BOUNDED`; fresh BUILD-only packet is next | PASS |
| current continuity | repository HEAD | `542fb041d` | clean and synchronized with `origin/main` | PASS |
| operator continuation | current instruction | N/A with reason: recorded verbatim above | BUILD-only release | PASS |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| D1 is accepted bounded and releases only fresh BUILD packet authoring | VALUE_SET | `docs/reviews/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_COMPLETION_2026-08-09.md` | Findings / Position; Next Allowed Move | `CLOSED_PASS_BOUNDED` | D1 completion | ACCEPT |
| route currently owns direct provider fetch and implicit endpoint/model defaults | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | lines 286-309 | `POST` | LPCI query route | ACCEPT |
| route builds the accepted S1 projection before provider execution | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts` | provider-entry branch before lines 286-309 | `buildModelEvidenceProjection` | LPCI query route | ACCEPT |
| credential metadata and runtime secret resolution are separate | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | lines 3-38 | `CredentialBoundary` | credential boundary | ACCEPT |
| whitespace-only values are currently treated as available | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | lines 18-38 | `resolveSecret` | credential boundary | ACCEPT |
| bridge accepts injected routing, credential, health, quota, receipt, references, and adapters | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | lines 43-78 | `ProviderExecutionBridgeOptions` | bridge constructor | ACCEPT |
| bridge returns response, error, and mandatory receipt | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | lines 53-57 | `ProviderExecutionBridgeResult` | bridge result | ACCEPT |
| exact provider/model/capability selection is represented by the routing request | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | `RoutingRequest`; `decide` | `RoutingRequest` | routing policy engine | ACCEPT |
| current capability registry contains `openai/gpt-4o` with `complete` | VALUE_SET | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | OpenAI registry entry | `PROVIDER_CAPABILITY_REGISTRY` | provider capability registry | ACCEPT |
| public exports include the bridge | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` | bridge export block | `ProviderExecutionBridge` | package public surface | ACCEPT |
| a thin OpenAI-compatible adapter function exists only in the live-proof harness | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | lines 104-151 | `createOpenAiCompatibleExecuteAdapter` | P4B live-proof harness | ACCEPT |
| live-proof harness is not a production binding owner | LITERAL_INVARIANT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | file header | `P4B_B_LIVE_PROOF_HARNESS_VERSION` | live-proof-only harness | ACCEPT |
| cvf-web has no Model Gateway package dependency | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependencies | `dependencies` | npm package manifest | ACCEPT |
| safe example environment file exists and currently exposes provider-key examples | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.example` | AI Provider API Keys section | `OPENAI_API_KEY` | example configuration | ACCEPT |
| package-owned tests exclude `.live.test.ts` but not `.live.test.tsx` | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | scripts | `scripts` | npm scripts | ACCEPT |

The nonexistent paths `src/capability-registry.ts` and
`src/provider-adapter.ts` are rejected. Current owners are
`provider-capability-registry.ts`, `provider-method-gate.ts`, and the adapter
contract inside `provider-execution-bridge.ts`.

## New Doc-Only Fields

| Proposed item | Kind | Intended owner | Disposition before implementation |
|---|---|---|---|
| `LPCI1-WEB-UC01-B2` | batch token | this dispatch | DOC_ONLY_NEW |
| `openai-compatible-execute-adapter.ts` | reusable Model Gateway adapter owner extracted from live harness | Model Gateway | DOC_ONLY_NEW |
| `createCredentialBoundOpenAiCompatibleExecuteAdapter` | secret-contained adapter factory | Model Gateway credential/adapter seam | DOC_ONLY_NEW |
| `provider-binding.ts` | thin LPCI composition seam | cvf-web LPCI domain | DOC_ONLY_NEW |
| `LpciModelGatewayBinding` | injected binding contract | cvf-web LPCI domain | DOC_ONLY_NEW |
| `resolveLpciProviderBindingConfig` | atomic config parser | cvf-web LPCI domain | DOC_ONLY_NEW |
| `LPCI_PROVIDER_BINDING_INVALID` | server-internal diagnostic class | cvf-web LPCI domain | DOC_ONLY_NEW |

## Selected Build Boundary

1. Harden `CredentialBoundary` so missing and trim-empty values are unavailable;
   preserve the original non-empty secret bytes for runtime use.
2. Extract the existing OpenAI-compatible adapter implementation from the
   live-proof-only harness into a neutral Model Gateway module. Add a
   credential-bound factory so LPCI receives an adapter without receiving the
   raw secret.
3. Keep the live harness behavior intact by importing the extracted adapter.
4. Export the reusable adapter/factory through the existing Model Gateway
   public surface.
5. Add the file dependency from cvf-web to Model Gateway and update the lockfile
   only through the package manager.
6. Implement the thin LPCI binding with atomic config validation, exact current
   capability admission, singleton provider allowlist, requested model,
   `requiredCapabilities=['complete']`, secret-safe metadata preflight, bridge
   execution, and response/receipt identity validation.
7. Replace only the route-local provider branch after S1 clearance. Preserve
   existing outcome messages and LPCI audit correlation.
8. Document all three LPCI variables together in `.env.example` without a
   secret value.

## Allowed Scope

Worker writable paths are exactly:

1. `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts`
2. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/credential-boundary.test.ts`
3. `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts`
4. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/openai-compatible-execute-adapter.test.ts`
5. `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts`
6. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/p4b-b-dry-run-gate.test.ts`
7. `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
8. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`
9. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json`
10. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.example`
11. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.ts`
12. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/provider-binding.test.ts`
13. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts`
14. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.test.ts`
15. `docs/reviews/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_BUILD_WORKER_RETURN_2026-08-09.md`

## Forbidden Scope

- ignored local environment files, raw secret output, real keys, provider/live
  calls, live tests, browser proof, release bundles, and network access;
- new provider registry, routing engine, receipt owner, retry/fallback engine,
  public route, UI/dashboard, storage, vector/RAG, corpus, grant, session,
  governance checker, roadmap, completion review, public-sync, deployment, push,
  staging, or worker commit;
- direct route-local provider fetch after BUILD;
- importing the live-proof harness into production LPCI code;
- copying the adapter instead of extracting one neutral owner;
- every path not listed in Allowed Scope.

## Deterministic Proof Contract

The worker must cover D1 SP-01 through SP-12 with injected fake fetch/bridge
owners and zero network. The proof must additionally show:

- missing and whitespace-only credential metadata are unavailable;
- runtime secret bytes are not trimmed or exposed for a non-empty credential;
- route source contains no provider `fetch` call and imports the binding;
- package dependency resolves through the declared file seam;
- no secret, endpoint, provider diagnostic, Gateway receipt, or alternate
  provider identity appears in client output;
- all non-provider S1 outcomes retain zero bridge/adapter/fetch calls.

## Evidence / Verification

Dispatch evidence consists of direct repository source reads, exact current
HEAD/status, ADIF resolver output, paired-packet name-status, checker results,
and pre-dispatch autorun. Implementation and test outcomes remain pending the
worker and independent reviewer phases.

## Acceptance Criteria

- [ ] Exact fifteen-path manifest only.
- [ ] Model Gateway credential trim-empty hardening and focused regression pass.
- [ ] Neutral adapter is extracted; live harness imports it and retains tests.
- [ ] Raw credential resolution remains inside the Model Gateway owner.
- [ ] cvf-web declares the Model Gateway dependency and lockfile matches.
- [ ] LPCI binding enforces the atomic three-variable contract and exact pair.
- [ ] Route-local provider fetch/default ownership is removed after S1 clearance.
- [ ] Existing LPCI messages, response allowlists, audit equality, and S1 outcomes remain intact.
- [ ] D1 SP-01 through SP-12 pass without network.
- [ ] Model Gateway focused tests/check and cvf-web focused tests/check/lint pass.
- [ ] GC-023, worker-return fast gate, diff hygiene, exact manifest, and staged-empty checks pass.
- [ ] No live/provider/secret/public/deployment action occurs.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class implementation --role dispatcher --lifecycle-phase pre-dispatch --json`

Returned defects: NONE_RETURNED

Worker pre-implementation query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-implementation`

Worker resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-implementation --json`

Worker returned defects (0): NONE

## Decision / Disposition

Decision: dispatch one no-commit implementation worker after pre-dispatch PASS.

Disposition: `DISPATCH_READY`.

## Machine Closure Package

N/A with reason: this is a dispatch-ready baseline, not a closure artifact.
The reviewer must create the machine closure package only after accepted
implementation evidence and a non-empty committed material range exist.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance BUILD dispatch and evidence only. No public artifact
or public-sync action is authorized.

## Epistemic Process Block

### Expected Result / Prediction

Prediction: the accepted thin composition is implementable by extracting the
existing live-harness adapter into a neutral Model Gateway owner, hardening the
credential boundary, and keeping LPCI limited to public exports and metadata.

### Evidence Comparison Requirement

The worker compares implementation evidence with this prediction and records
any missing owner, incompatible package seam, or contract contradiction.

### Contradiction Or Gap Disposition

Any need for raw secret handling in LPCI, a second routing/registry owner,
arbitrary endpoint fetch, or scope expansion is `BLOCKED_RETURN_TO_REVIEWER`.

### Claim Update Requirement

The worker classifies the prediction as confirmed, narrowed, or invalidated.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | primary reviewer/dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | `lpci1-web-uc01-b2-dispatch-2026-08-09` |
| Working directory | repository root |
| Command or tool surface | governed source reads, ADIF resolver, apply_patch, dispatch gates, Git |
| Target paths | paired GC-018 baseline and work order |
| Allowed scope source | operator continuation and D1 next allowed move |
| Before status evidence | clean synchronized HEAD `542fb041d` |
| After status evidence | pending pre-dispatch and dispatch commit |
| Diff evidence | exact paired-packet name-status and gate receipts |
| Approval boundary | BUILD-only deterministic local implementation dispatch |
| Claim boundary | no implementation result, provider/live, public, deployment, or readiness claim |
| Agent type | dispatcher/reviewer |
| Invocation ID | `lpci1-web-uc01-b2-dispatch-2026-08-09` |
| Expected manifest | this baseline and matching work order |
| Actual changed set | pending paired dispatch packet |
| Manifest delta | pending dispatch gate |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This baseline authorizes bounded local BUILD and deterministic network-free
proof only. It does not prove the implementation, authorize provider/live
execution, expose credentials, export public artifacts, or claim production
readiness.
