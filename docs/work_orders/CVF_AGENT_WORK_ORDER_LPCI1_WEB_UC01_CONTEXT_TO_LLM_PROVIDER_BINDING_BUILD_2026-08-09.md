# CVF Agent Work Order - LPCI1 Web UC-01 Context-To-LLM Provider Binding Build

Memory class: governed-agent-work-order

Status: DISPATCH_READY

Batch ID: LPCI1-WEB-UC01-B2

Date: 2026-08-09

dispatchBaseHead: `542fb041d`

executionBaseHead: capture the clean committed HEAD immediately before worker edits

closureBaseHead: N/A with reason: pending independent reviewer conversion

Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Role: implementation worker. The primary agent is independent reviewer/closer.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_BUILD_2026-08-09.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

Base: executionBaseHead must equal the clean committed HEAD captured with
`git rev-parse --short HEAD` immediately before worker edits.

Current-time notes: no live key, provider call, network, ignored local
environment read, public-sync, push, or deployment is authorized.

Do-not-misread notes: the P4B live-proof harness is source material for an
adapter extraction, not a production import target; the worker must extract one
neutral owner and keep raw credential resolution inside Model Gateway.

Required first actions: read the paired baseline, accepted D1 audit/completion,
guard orientation, literal-format gotchas, and all Source Packet owners; capture
clean status/HEAD; run ADIF resolver and pre-implementation.

Return contract: `COMPLETE_PENDING_REVIEW`, `BLOCKED_SOURCE_MISMATCH`, or
`BLOCKED_SCOPE_EXPANSION_REQUIRED`, with executionBaseHead, exact changed paths,
test/gate receipts, staged-empty evidence, and unchanged HEAD.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py` |
| literalTokensReviewed | `Dispatch Prompt Envelope`; `Worker Autonomy / No-Question Rule`; `Work-Order Fulfillment Manifest`; `nextMoveSurfaces`; `WORKER_MUST_NOT_COMMIT`; `COMPLETE_PENDING_REVIEW` |
| gateRunPurpose | confirmation and evidence after checker-shape review, not first discovery |
| claimBoundary | read-ahead confirms work-order shape only; no implementation, live, provider, or closure claim |

## Purpose

Dispatch one bounded no-commit worker to implement the accepted UC-01 BUILD
with deterministic network-free evidence and return it for independent review.

## 0. Surface Fidelity Gate

The worker must refresh every decision-driving source cited in the paired
baseline at `executionBaseHead` before editing. If a named owner, export,
package seam, accepted D1 invariant, or exact writable path has drifted, stop
with `BLOCKED_SOURCE_MISMATCH` or a source-backed contradiction. Do not infer a
replacement from chat or provider memory.

## 1. Authority Chain

1. Operator continuation: `tiep tuc`.
2. Accepted D1 audit:
   `docs/audits/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_2026-08-09.md`.
3. Accepted D1 completion:
   `docs/reviews/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_COMPLETION_2026-08-09.md`.
4. Paired baseline:
   `docs/baselines/CVF_GC018_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_BUILD_2026-08-09.md`.
5. This work order.

Authority token:
`AUTHORIZE_LPCI1_WEB_UC01_PROVIDER_BINDING_BUILD_ONLY`.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id LPCI1-WEB-UC01-B2 --title "LPCI1 Web UC-01 Context-To-LLM Provider Binding Build" --date 2026-08-09 --base 542fb041d --commit-mode WORKER_MUST_NOT_COMMIT --dependency "UC-01 D1 closure 2e770480c" --include-worker-return-skeleton --stdout` |
| generatedProfile | web route plus Model Gateway package integration; deterministic network-free tests |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source verification, exact manifest, D1 SP ledger, no-secret/no-live controls, handoff and return contracts |
| checkerReadAheadConfirmation | required dispatch checkers reviewed before gate execution |
| docOnlyNewFields | isolated in paired baseline and work order |
| claimBoundary | scaffold provenance only |

## 2. Transfer Objective

Implement the accepted UC-01 provider binding as one bounded, network-free
BUILD. Harden credential whitespace handling at Model Gateway, extract the
existing OpenAI-compatible adapter from the live-only harness into a neutral
owner, add a credential-contained adapter factory, declare the cvf-web package
seam, implement the thin LPCI binding, and replace the route-local provider
branch only after existing S1 clearance.

Return all owned changes unstaged and uncommitted for independent review.

## 3. Source Packet

Required full reads before editing:

- paired GC-018 baseline and accepted D1 audit/completion;
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts`;
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts`;
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts`;
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`;
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-gate.ts`;
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts`;
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`;
- relevant current Model Gateway focused tests;
- current cvf-web route, route test, package manifests, and `.env.example`.

Never read ignored local environment files or print environment values.

## Required First Reads

The `## 3. Source Packet` list is mandatory and must be completed before any
material edit. Provider-local memory and chat are not source authority.

## Pre-Flight Checks

Before editing: confirm clean worktree and captured executionBaseHead; run the
worker ADIF query; run pre-implementation on the captured base; confirm all
fifteen writable paths and all forbidden boundaries.

## 4. Role Assignment

| Role | Actor | Responsibility |
|---|---|---|
| dispatcher/reviewer | primary agent | source verification, packet, independent semantic review, closure, commit |
| implementation worker | delegated subagent | exact BUILD manifest, deterministic tests, worker return; no commit |
| closer | primary reviewer | reviewer closure conversion and committed-range gates |
| session-sync steward | primary reviewer | separate continuity update after accepted material commit |

## Agent Roles

The authoritative role allocation is the `## 4. Role Assignment` table above.
The worker implements and returns; the primary agent reviews, closes, commits,
and synchronizes continuity.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | operator continuation of the accepted D1 next move |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| risk sensitivity | bounded source/package/route implementation; no live or secret access |
| selected role route | `MULTI_AGENT_MULTI_ROLE` |
| Worker role | exact implementation/test manifest and worker return only |
| Reviewer role | independent semantic review, closure conversion, commit, and session sync |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Checkpoint disposition | BUILD-only checkpoint satisfied; provider/live remains parked |
| escalation condition | source contradiction, scope expansion, raw secret access outside Model Gateway, live/provider/network, public-sync, deployment, destructive action, or claim-boundary change |

## Worker Autonomy / No-Question Rule

The worker must repair and rerun every failure inside Allowed Scope without
asking the operator. Stop and return a governed blocker only for source
absence, scope expansion, forbidden paths/actions, live/provider/network,
secret access outside the authorized Model Gateway owner, public-sync,
deployment, destructive action, or claim-boundary change.

## Execution Plan

Execute the sequential source-freshness, credential hardening, adapter
extraction, package binding, LPCI composition, route integration, deterministic
proof, and worker-return steps in `## 5. Execution Instructions`. No step is
parallel-safe with another agent editing the same worktree.

## 5. Execution Instructions

1. Capture `executionBaseHead`, confirm clean worktree, run the worker ADIF
   resolver query, and run pre-implementation before any material edit.
2. Harden `CredentialBoundary.resolveSecret` to ignore missing and trim-empty
   candidates while returning the original non-empty bytes. Add focused tests
   for missing, empty, whitespace, alias fallback, metadata shielding, and
   preserved runtime bytes.
3. Extract `createOpenAiCompatibleExecuteAdapter` from the live-proof-only
   harness into the new neutral Model Gateway module. The harness must import
   it; duplicated implementations are forbidden.
4. Add `createCredentialBoundOpenAiCompatibleExecuteAdapter` or an equivalently
   narrow public factory owned by Model Gateway. It accepts a
   `CredentialBoundary`, `CredentialReference`, exact provider/model/endpoint,
   and injected fetch; it resolves the secret internally and returns no raw
   value. Missing credential fails before adapter/network execution.
5. Keep endpoint acceptance fail-closed. For this tranche the only production
   pair required for successful composition is current `openai/gpt-4o` with
   canonical endpoint `https://api.openai.com/v1/chat/completions`. Optional
   `LPCI_LLM_ENDPOINT` must normalize to that exact HTTPS endpoint. Other
   registered pairs without an admitted production adapter fail safely before
   network; do not invent provider endpoints.
6. Export the neutral adapter/factory through `CVF_MODEL_GATEWAY/src/index.ts`.
7. Add `cvf-model-gateway` as a file dependency in cvf-web and update only the
   matching package lock with npm. Do not install unrelated packages.
8. Implement `provider-binding.ts` as the thin LPCI seam. It must parse
   `providerId/modelId` with exactly one slash, require non-empty tokens, use
   current capability admission for `complete`, preflight only secret-safe
   metadata, build singleton `allowedProviderIds`, exact `requestedModelId`,
   and exactly `requiredCapabilities=['complete']`, then call one injected or
   composed `ProviderExecutionBridge`.
9. Validate bridge result before returning text: no error, non-empty text,
   response and receipt trace equal request trace, and response/receipt
   provider/model equal the configured pair. The Gateway receipt remains
   server-internal.
10. Replace the existing route-local provider fetch/default branch with the
    binding after S1 clearance. Keep existing `NO_PROVIDER_CONFIGURED` and
    `PROVIDER_ERROR` messages, response allowlists, LPCI audit construction,
    `auditId` equality, and every non-provider S1 outcome.
11. Add the three-variable atomic contract to `.env.example`. Use no secret
    sample. `LPCI_LLM_MODEL=openai/gpt-4o` is the safe syntax example;
    `LPCI_LLM_ENDPOINT` is optional and must describe exact canonical matching.
12. Implement D1 SP-01 through SP-12 plus source assertions for route-local
    fetch absence and package import presence. All provider seams must be fakes
    or injected fetch doubles; network count is zero.
13. Create the worker return from the required scaffold, complete every required
    section, rerun the exact final commands after the last edit, and leave the
    staged set empty.

Any in-scope failure is repaired and rerun. Scope expansion, real provider or
secret access, live proof, arbitrary endpoint support, new registry/routing
owner, or raw credential handling outside Model Gateway returns to reviewer.

## 6. Role Output Schema

Worker output status must be `COMPLETE_PENDING_REVIEW`,
`BLOCKED_SOURCE_MISMATCH`, or `BLOCKED_SCOPE_EXPANSION_REQUIRED`.

The worker return must include these headings:

- `Checker Source Read-Ahead Block`
- `Purpose`
- `Target / Source`
- `Scope / Methodology`
- `Authority And Role Boundary`
- `Source Inventory`
- `Findings / Position`
- `Risk / Corrective Action`
- `Decision / Disposition`
- `Implementation Manifest`
- `Test And Gate Evidence`
- `Synthetic Proof Ledger`
- `External Knowledge Intake Routing`
- `Epistemic Process Block`
- `Worker Self-Audit`
- `Agent Operation Trace Block`
- `Public Export Disposition`
- `Claim Boundary`

Source Inventory action cells must contain only `READ`, `FULL_READ`,
`PARTIAL_READ`, or `SOURCE_VERIFIED`.

## 7. Dissent And Review Ledger

The worker records every source contradiction, rejected alternative, gate
repair, and manifest delta. No dissent is silently resolved by widening scope.
Reviewer acceptance is not claimed by the worker.

## 8. Integration Decision

Integration is pending independent reviewer review. The worker must not stage,
commit, push, update session state, close the work order, change roadmap status,
or claim BUILD acceptance.

## Source Verification Block

The full source-verification table in the paired baseline is incorporated by
reference and is binding. Key accepted current symbols are:

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| bridge composition contract | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | interfaces and constructor | `ProviderExecutionBridgeOptions` | `ProviderExecutionBridge` | ACCEPT |
| secret-safe metadata preflight | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | class methods | `resolveMetadata` | `CredentialBoundary` | ACCEPT |
| runtime secret stays at credential owner | EXISTS | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | class methods | `resolveSecretForRuntime` | `CredentialBoundary` | ACCEPT |
| exact pair routing controls | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` | `decide` | `allowedProviderIds`; `requestedModelId`; `requiredCapabilities` | `RoutingPolicyEngine` | ACCEPT |
| current `complete` capability admission | VALUE_SET | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | OpenAI model row | `openai/gpt-4o` | `PROVIDER_CAPABILITY_REGISTRY` | ACCEPT |
| reusable adapter is not yet neutral production owner | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` | header and adapter function | `createOpenAiCompatibleExecuteAdapter` | live-proof harness | ACCEPT |
| thin LPCI binding path | DOC_ONLY_NEW | `docs/audits/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_DESIGN_2026-08-09.md` | BUILD Manifest | `src/lib/lpci/provider-binding.ts` | proposed LPCI seam | ACCEPT |
| neutral adapter/factory path | DOC_ONLY_NEW | `docs/baselines/CVF_GC018_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_BUILD_2026-08-09.md` | Selected Build Boundary | `src/openai-compatible-execute-adapter.ts` | proposed Model Gateway seam | ACCEPT |

## New Doc-Only Fields

The DOC_ONLY_NEW table in the paired baseline is binding. The worker must map
the final concrete identifiers in its return; it must not cite them as
pre-existing source facts.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap/D1 control | Work-order handling | Required evidence | Status before execution |
|---|---|---|---|
| UC-01 DESIGN accepted before BUILD | dependency table and accepted D1 source | accepted audit/completion | PASS |
| UC-04 atomic binding/config | three-variable parser, package seam, binding, example config | source plus SP-01-SP-05 | PASS |
| no duplicate generic owner | extract existing adapter and reuse current Gateway owners | source diff and imports | PASS |
| fail closed before provider | metadata/config/capability/endpoint preflight | SP-02-SP-07 | PASS |
| exact pair and no fallback | singleton allowlist plus post-result identity checks | SP-01, SP-11, SP-12 | PASS |
| preserve S1 clearance | binding only after eligible projection | SP-10 and route regressions | PASS |
| deterministic BUILD evidence | injected fakes and zero network | all SP cases and command receipts | PASS |
| provider/live later | explicit forbidden scope | zero live/provider call evidence | PASS |

## Allowed Scope

Writable manifest is exactly the fifteen paths enumerated in the paired
baseline. No substitution, additional test file, helper, config, generated
artifact, or documentation path is allowed without reviewer authority.

## Write Ownership

The worker owns only the exact fifteen writable paths in the paired baseline.
The reviewer alone owns completion, roadmap/work-order finality, commits, and
session/front-door/handoff synchronization.

## Forbidden Scope

The paired baseline Forbidden Scope is incorporated verbatim. In particular:
do not read `.env.local` or `.env.netlify`; do not inspect process environment
values; do not execute a real fetch; do not run live tests or release bundles;
do not touch provider settings UI, roadmap, session state, governance files,
public-sync, or Git history.

## Required Proof Manifest

| Proof | Command/owner | Required result |
|---|---|---|
| credential hardening | Model Gateway credential test | missing/empty/whitespace unavailable; alias fallback and original bytes preserved |
| adapter extraction | new adapter test plus live-harness dry-run test | one neutral implementation; injected fetch only; no raw secret output |
| Model Gateway static/focused | package `test` targets and `npm run check` | PASS |
| binding SP-01-SP-12 | new provider-binding test | all twelve cases PASS; zero real network |
| route preservation | LPCI route test | existing S1/outcome/audit tests plus new binding mapping PASS |
| route ownership | source assertion | no provider `fetch` in route; binding import exists |
| package seam | manifests and install/check | `cvf-model-gateway` file dependency resolves; lockfile aligned |
| cvf-web static | `npm run check` and scoped lint | PASS |
| maintainability | GC-023 | zero violations |
| worker handoff | worker-return fast gate, exact status and Git evidence | PASS; staged set empty |

## Work-Order Fulfillment Manifest

| Artifact or surface | Owner | Required disposition |
|---|---|---|
| fifteen-path worker manifest | implementation worker | implemented, tested, unstaged, and uncommitted |
| D1 SP-01 through SP-12 ledger | implementation worker | every case mapped to deterministic proof |
| worker return | implementation worker | `COMPLETE_PENDING_REVIEW` or governed blocker |
| completion review | primary reviewer | created only after independent review |
| roadmap/work-order closure state | primary reviewer | updated only after accepted material evidence |
| session/front door/handoff | session-sync steward | separate continuity commit only |

## Required Artifact Manifest

| Artifact | Path or owner | Required status |
|---|---|---|
| Model Gateway credential, adapter, export, harness, and tests | exact paths 1 through 7 in the paired baseline writable manifest | implemented and deterministic tests pass |
| cvf-web package seam and example config | exact paths 8 through 10 in the paired baseline writable manifest | aligned and static check passes |
| LPCI binding, route, and tests | exact paths 11 through 14 in the paired baseline writable manifest | implemented and focused tests pass |
| worker return | `docs/reviews/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_BUILD_WORKER_RETURN_2026-08-09.md` | complete pending review or governed blocker |
| reviewer dispatch repair | three reviewer-owned paths recorded under Verification Commands | committed before worker final-gate resume |

## Verification Commands

Reviewer-owned dispatch repair, 2026-08-09:

- The originally dispatched worker-return pytest target omitted the canonical
  `_gate` suffix. The corrected source-verified target is used in command 8.
- The required new adapter test exposed a GC-051 coverage prerequisite. The
  primary reviewer owns the separate registry source entry and regenerated
  aggregate; these governance paths are not added to the worker's fifteen-path
  implementation manifest.
- Repair paths:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_BUILD_2026-08-09.md`,
  `docs/corpus-intelligence/registry/entries/lpci1-web-uc01-b2-provider-binding-adapter-tests.json`,
  and `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`.
- The worker may resume final verification only after this repair is committed
  and the dispatcher reruns the applicable pre-dispatch gate.

Run from repository root unless a command explicitly changes working directory:

1. `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD`
2. `npm test -- --run tests/credential-boundary.test.ts tests/openai-compatible-execute-adapter.test.ts tests/p4b-b-dry-run-gate.test.ts` from `EXTENSIONS/CVF_MODEL_GATEWAY`
3. `npm run check` from `EXTENSIONS/CVF_MODEL_GATEWAY`
4. `npm run test:run -- src/lib/lpci/provider-binding.test.ts src/app/api/lpci/query/route.test.ts --exclude "src/**/*.live.test.tsx"` from cvf-web
5. `npm run check` from cvf-web
6. `npx eslint src/lib/lpci/provider-binding.ts src/lib/lpci/provider-binding.test.ts src/app/api/lpci/query/route.ts src/app/api/lpci/query/route.test.ts` from cvf-web
7. `python governance/compat/check_governed_file_size.py --enforce`
8. `python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_worker_return_quality_gate.py`
9. `git diff --check`
10. `git status --short --untracked-files=all`
11. `git diff --cached --name-only`

The worker may run narrower diagnostic commands before the final sequence. It
must rerun the exact final sequence after the last material edit. Test commands
must not load ignored local environment files; if the repository test setup
would load them, explicitly isolate/unset that loader or return a blocker
without reading their contents.

## Evidence Requirements

The worker return must record every final command exactly as run, working
directory, result, executionBaseHead, HEAD unchanged, exact name-status/status,
SP-01-SP-12 mapping, zero-network evidence, no-secret-read boundary, and empty
staging. Unqualified PASS prose is not evidence.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Scaffold command:

`python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_BUILD_WORKER_RETURN_2026-08-09.md --title "LPCI1 Web UC-01 Context-To-LLM Provider Binding Build Worker Return"`

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class implementation --role dispatcher --lifecycle-phase pre-dispatch --json`

Returned defects: NONE_RETURNED

Worker pre-implementation query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-implementation`

Worker resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class implementation --role worker --lifecycle-phase pre-implementation --json`

Worker returned defects (0): NONE

## Agent Handoff Contract Control Block

Contract source archive-qualified checker exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher/reviewer -> one no-commit implementation worker -> independent reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=`542fb041d`; executionBaseHead=captured immediately before edits; closureBaseHead=reviewer capture |
| changedSetScope(phase) | dispatch=paired packet; execution=exact fifteen paths; closure=accepted worker material plus reviewer-owned packet/status paths; session sync=canonical continuity only |
| traceScope(phase, actor) | each actor records commands, exact manifest, status, and manifest delta for its phase |
| commitOwner(phase) | dispatcher commits dispatch; worker must not commit; reviewer commits accepted material; steward separately commits continuity |
| crossBatchIsolation | worker starts from a clean worktree; no unrelated worktree, side-channel, previous tranche, or public-sync changes may enter this batch |
| nextMoveSurfaces | worker does not mutate roadmap/session/handoff; reviewer updates them only in the session-sync phase following an accepted material commit |

Canonical route token: `MULTI_AGENT_MULTI_ROLE`.

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_LPCI1_WEB_UC01_CONTEXT_TO_LLM_PROVIDER_BINDING_BUILD_COMPLETION_2026-08-09.md`

reviewerOwnedClosurePaths:

- the completion review above;
- this work order status/checklist;
- `docs/roadmaps/CVF_LPCI1_WEB_CONTEXT_TO_LLM_USE_CASE_ROADMAP_2026-08-09.md`;
- canonical session/front-door/handoff paths only in a separate sync commit.

The reviewer must independently inspect the source, tests, manifest, no-secret
boundary, and D1 SP ledger before acceptance.

## Design Control Carry-Forward

| Design control | D1 source | Work-order handling | Verdict |
|---|---|---|---|
| scope boundary | Selected ownership boundary | thin composition only | PASS |
| non-goals | Claim Boundary | no live/provider/public/readiness | PASS |
| lane split | Future BUILD Manifest | BUILD-only exact manifest | PASS |
| credential prerequisite | Configuration Contract | Model Gateway hardening first | PASS |
| exact pair | Request mapping | singleton allowlist, requested model, complete capability | PASS |
| result correlation | Result and correlation mapping | response/receipt trace and identity validation | PASS |
| acceptance | Synthetic Proof Contract | SP-01-SP-12 | PASS |
| dispatch readiness | Independent Reviewer Acceptance | fresh BUILD packet authorized now | PASS |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | bounded local UC-01 provider-binding BUILD and deterministic tests |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: worker creates test evidence, not a live execution receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source diffs, deterministic test output, worker return, and Git manifest |
| invocationBoundary | local governed source/test editing and network-free commands |
| interceptionBoundary | no IDE, shell, Git, filesystem, provider, or network interception claim |
| claimLanguage | implementation tested locally with injected fakes only |
| forbiddenExpansion | provider/live proof, secret inspection, public export, deployment, production readiness, or universal runtime control |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the existing bridge plus extracted adapter owner
is sufficient for thin composition without raw credential handling in LPCI.

Evidence Comparison Requirement: compare actual package, adapter, credential,
route, and test evidence against the prediction.

Contradiction Handling Requirement: record any missing owner or design
contradiction and return without widening scope.

Claim Update Requirement: classify the prediction as confirmed, narrowed, or
invalidated.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | primary reviewer/dispatcher; delegated no-commit worker at execution |
| Provider or surface | local private provenance repository |
| Session or invocation | `lpci1-web-uc01-b2-dispatch-2026-08-09` |
| Working directory | repository root |
| Command or tool surface | source verification, ADIF, apply_patch, gates, Git; worker local implementation/test tools |
| Target paths | paired dispatch packet now; exact fifteen-path worker manifest after dispatch |
| Allowed scope source | operator continuation, D1 accepted next move, paired baseline |
| Before status evidence | clean worktree; `git status --short` empty at synchronized HEAD `542fb041d` |
| After status evidence | pending dispatch commit and worker execution |
| Diff evidence | exact phase-local name-status/status evidence |
| Approval boundary | BUILD-only, deterministic, network-free |
| Claim boundary | repo-local trace only; no live/provider/public/readiness claim |
| Agent type | multi-agent dispatcher/worker/reviewer chain |
| Invocation ID | `lpci1-web-uc01-b2-dispatch-2026-08-09` |
| Expected manifest | exact phase-local manifest stated above |
| Actual changed set | pending phase execution |
| Manifest delta | pending phase execution |
| Deletion or rename disposition | N/A with reason: no deletion or rename authorized |

## Acceptance Criteria

- [ ] Worker runs ADIF and pre-implementation before edits.
- [ ] Exact fifteen-path manifest only; no staged or committed worker changes.
- [ ] Credential trim-empty hardening preserves non-empty runtime bytes.
- [ ] Adapter implementation has one neutral owner and live harness imports it.
- [ ] Raw credential is resolved only inside Model Gateway.
- [ ] Package dependency and lockfile are aligned.
- [ ] Atomic config, exact pair, endpoint, capability, routing, and correlation rules are implemented.
- [ ] Existing S1 response/audit/outcome contract is preserved.
- [ ] SP-01 through SP-12 and route ownership assertions pass network-free.
- [ ] Required focused/static/lint/file-size/worker-return/diff/staged-empty commands pass.
- [ ] Worker return includes full evidence and no reviewer acceptance claim.
- [ ] No live/provider/secret/public/deployment/readiness action occurs.

Fail conditions:

- [ ] source owner/export/package seam is missing or incompatible;
- [ ] implementation needs a path outside exact scope;
- [ ] LPCI must read a raw secret or arbitrary endpoint;
- [ ] any real network/provider/live or ignored local environment access occurs;
- [ ] any required final command fails after allowed-scope repair;
- [ ] exact manifest or staged-empty boundary is violated.

Closure is blocked while any fail condition is present.

## Review Gate

Implementation may begin only after paired dispatch commit and pre-dispatch
PASS. Worker material edits may begin only after pre-implementation PASS on the
captured execution base.

Worker handoff is never closure. Reviewer acceptance requires semantic review,
reviewer-return steward PASS, material commit, non-empty committed-range
pre-closure PASS, separate session synchronization, and clean worktree.

## Operator Checkpoint

The operator checkpoint releases BUILD-only execution. Provider/live, real
credentials, arbitrary endpoints, public-sync, deployment, and production
readiness remain parked behind later explicit authority.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only with all final evidence. Return
`BLOCKED_SOURCE_MISMATCH` or `BLOCKED_SCOPE_EXPANSION_REQUIRED` for a genuine
source/scope blocker. Do not continue into reviewer closure, provider/live, or
session synchronization.

## Closure Checklist

- [ ] All acceptance criteria resolved
- [ ] D1 SP-01-SP-12 mapped to passing tests
- [ ] Exact changed manifest verified
- [ ] Secret-safe and zero-network boundaries independently reviewed
- [ ] Worker-return fast gate passed
- [ ] Reviewer-return commit steward passed
- [ ] Reviewer completion packet filed
- [ ] Work order and roadmap statuses updated without open residue
- [ ] Material commit hook passed
- [ ] Material-only pre-closure range passed
- [ ] Session state/handoff synchronized separately
- [ ] Final active-session gate passed
- [ ] Worktree and staged set clean

## External Knowledge Intake Routing

Canonical chain map:
`docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`.

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current local runtime source verification for BUILD only; provider/live/readiness proof remains blocked |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py` and provider-memory boundary |
| Owner surface | paired GC-018 baseline and this work order |
| Disposition | `BLOCKED_UNTIL_CVF_PROOF` for provider/live/readiness; bounded local BUILD remains authorized |
| Claim boundary | current repository source controls; no external absorption claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation and evidence. A later public action
requires separate authority and the sibling public-sync clone.

## Claim Boundary

This work order authorizes only the exact local BUILD and deterministic proof
described above. It does not authorize or prove live provider behavior,
credential validity, public export, deployment, or production readiness.
