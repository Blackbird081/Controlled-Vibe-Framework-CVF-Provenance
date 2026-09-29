# CVF GC-018 Baseline - EAFR-R10 External Store Authority And Shared Adapter Destination Policy Implementation

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: EAFR-R10-EXTERNAL-STORE-AUTHORITY-AND-SHARED-ADAPTER-DESTINATION-POLICY-IMPLEMENTATION

Dispatch base head: `45684c86e804b2e5a5ac8ed581c57336bc93e5c8`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through the committed EAFR roadmap and accepted R9 decision

Reviewer owner: current independent orchestrator/reviewer

Worker target: bounded TypeScript implementation worker

providerExecutionAuthority: FORBIDDEN

## Purpose

Implement the two exact R9 decisions without widening them: add the sibling
external-store grant contract and evaluator in the control-plane foundation,
and make one gateway-owned destination classifier govern both the injected
gateway adapter boundary and the existing Web test guard.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R10 --title "External Store Authority And Shared Adapter Destination Policy Implementation" --date 2026-08-26 --base 45684c86e --commit-mode WORKER_MUST_NOT_COMMIT --dependency "EAFR-R9 accepted bounded at 7767c728f" --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact R9 interfaces, ten-file implementation manifest, pre-fetch adapter denial contract, focused verification matrix, and explicit live-store wiring exclusion |
| checkerReadAheadConfirmation | applicable dispatch, trace, delta, ADIF, forbidden-filesystem and worker-return checker sources read |
| docOnlyNewFields | External Store Authority Contract; Shared Destination Policy Contract; Adapter Enforcement Contract |
| claimBoundary | dispatch authoring only; no implementation, provider, network, external-store, release, or public claim |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| EAFR-R9 accepted decision | `docs/reviews/CVF_EAFR_R9_EXTERNAL_STORE_GRANT_AND_ADAPTER_DESTINATION_POLICY_OWNER_WORKER_RETURN_2026-08-26.md`; material commit `7767c728f` | RELEASED |
| R9 exact grant design | sibling types and evaluator in `delegation.contract.ts`, using `store` and `allowedStores` | ACCEPT |
| R9 exact policy owner | `EXTENSIONS/CVF_MODEL_GATEWAY/src/adapter-destination-policy.ts` with `AdapterDestinationDecision` and `classifyAdapterDestination` | ACCEPT |
| R9 continuity closure | session commits `0eae3067a` and `45684c86e` | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime-source-implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class runtime-source-implementation --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | ordinary CVF controls apply |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_forbidden_filesystem_state.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Source Verification Block; Current Runtime Freshness Verification; Evidence Reuse scalars; Forbidden Path Manifest; Pre-Implementation Forbidden Filesystem State; Agent Operation Trace; Delta Execution Claim Boundary; Public Export Disposition |
| gateRunPurpose | author checker-shaped evidence before dispatch rather than discover requirements by trial |
| claimBoundary | structural compliance does not prove the future implementation |

## Current Runtime Freshness Verification

Verified at dispatch base `45684c86e804b2e5a5ac8ed581c57336bc93e5c8`:

- `delegation.contract.ts` contains only provider-scoped authority types and
  evaluator; its tests and coordination barrel are the established extension
  points;
- `openai-compatible-execute-adapter.ts` invokes its injected `fetchImpl`
  without classifying the configured endpoint;
- the only current destination classifier is duplicated nowhere but lives in
  `cvf-web/src/test/provider-execution-guard.ts`, so it is not gateway-owned;
- cvf-web already depends on `cvf-model-gateway`; the gateway needs no new
  dependency to own and use a local policy module;
- gateway has no runtime/local workspace dependencies and retains four
  tooling-only devDependencies; package manifests need no change;
- both intended new gateway paths are absent.

No live or provider behavior is needed to prove this tranche. The external-
store grant is a contract/evaluator only; deliberate store execution remains
unwired and denied.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R9 accepts a sibling external-store grant design | DECISION_AUTHORITY | `docs/reviews/CVF_EAFR_R9_EXTERNAL_STORE_GRANT_AND_ADAPTER_DESTINATION_POLICY_OWNER_WORKER_RETURN_2026-08-26.md` | Decision A; Reviewer Decision | ExternalStoreExecutionGrant | R9 accepted worker return | ACCEPT |
| R9 names the exact gateway policy interface | DECISION_AUTHORITY | `docs/reviews/CVF_EAFR_R9_EXTERNAL_STORE_GRANT_AND_ADAPTER_DESTINATION_POLICY_OWNER_WORKER_RETURN_2026-08-26.md` | Decision B; Reviewer Decision | adapter-destination-policy.ts | R9 accepted worker return | ACCEPT |
| provider evaluator establishes ordered fail-closed precedent | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` | provider authority types and evaluator | evaluateProviderExecutionAuthority | delegation contract | ACCEPT |
| foundation test and barrel are existing extension points | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/delegation.contract.test.ts`; `src/control.plane.coordination.barrel.ts` | file scope | delegation tests and exports | control-plane foundation | ACCEPT |
| adapter reaches injected fetch before any policy check | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts` | execute body | createOpenAiCompatibleExecuteAdapter | model gateway | ACCEPT |
| adapter residual test currently proves arbitrary endpoint reachability | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/openai-compatible-execute-adapter.test.ts` | injected-fetch tests | adapter test suite | model gateway tests | ACCEPT |
| current classifier and provider-host data are Web-test-local | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts` | classifier helpers | classifyDestination | cvf-web test guard | ACCEPT |
| Web can consume gateway export without a new edge | PACKAGE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependencies | cvf-model-gateway | cvf-web manifest | ACCEPT |

## External Store Authority Contract

Add to `delegation.contract.ts` exactly the accepted sibling design:

- `ExternalStoreExecutionAuthority = "FORBIDDEN" | "ORCHESTRATOR_GRANT_REQUIRED"`;
- `ExternalStoreExecutionGrant` with authority, nullable grantId, nullable
  ORCHESTRATOR authorizer, subjectAgentId, delegationId, allowedStores,
  maxCalls and nullable expiresAt;
- `ExternalStoreExecutionRequest` with workerAgentId, delegationId, grantId,
  store, consumedCalls and nowIso;
- `evaluateExternalStoreExecutionAuthority` returning `{ allowed; reason }`
  and applying the provider evaluator's same ordered fail-closed checks with
  `store`/`allowedStores` substituted.

Export the types/function from the existing coordination barrel. Do not add
an `externalStoreExecution` field to `DelegationContract`, wire a runtime
consumer, inspect credentials, or issue a grant.

## Shared Destination Policy Contract

Create the exact R9-owned module and export:

`AdapterDestinationDecision = { kind: "permit-non-provider" } | { kind:
"provider"; provider: string } | { kind: "deny"; reason: string }`

`classifyAdapterDestination(input: string | URL): AdapterDestinationDecision`

Move/canonicalize the current Web classifier semantics into this one module:
relative URLs, loopback and current non-egress protocols remain permitted;
known provider endpoints return their provider identity; malformed,
unrecognized, or external-store destinations deny. Provider endpoint data
must continue to derive from gateway-owned constants, including the Alibaba
ledger constants. Re-export through gateway `src/index.ts`.

The Web guard must consume this function rather than retain a second provider
hostname/protocol permit list. A thin `Request`-to-URL compatibility wrapper
is permitted; duplicate classification data or logic is not.

## Adapter Enforcement Contract

Before invoking any injected `fetchImpl`, the adapter must classify its
configured endpoint and:

1. reject `deny` without calling fetch;
2. reject a `provider` result whose identity differs from configured
   `providerId`, without calling fetch;
3. permit matching provider endpoints and `permit-non-provider` destinations
   already allowed by the shared policy.

This closes the arbitrary injected-endpoint bypass. It does not authorize an
external store, general internet host, provider call, or live test.

## Exact Implementation Manifest

Create exactly:

1. `EXTENSIONS/CVF_MODEL_GATEWAY/src/adapter-destination-policy.ts`
2. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/adapter-destination-policy.test.ts`
3. `docs/reviews/CVF_EAFR_R10_EXTERNAL_STORE_AUTHORITY_AND_SHARED_ADAPTER_DESTINATION_POLICY_IMPLEMENTATION_WORKER_RETURN_2026-08-26.md`

Modify exactly:

1. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts`
2. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/delegation.contract.test.ts`
3. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.coordination.barrel.ts`
4. `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts`
5. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/openai-compatible-execute-adapter.test.ts`
6. `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
7. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts`
8. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.test.ts`

No delete, rename, package manifest, lockfile, config, environment, roadmap,
session, checker, registry, runtime store consumer, public clone, or deployment
path is authorized.

## Baseline Decision / Proposed Tranche

Dispatch one bounded no-commit implementation tranche with exactly the three
creates and eight modifications above. The worker implements the already
accepted interfaces, proves them with local fake-based focused tests and
typechecks, authors the worker return, and yields to an independent reviewer.
Any need for live-store wiring, a dependency/config edit, or a wider decision
type returns blocked for separate authority.

## Verification And Acceptance

Acceptance requires focused tests for all ordered grant denials and success;
all three destination classes; malformed/unrecognized denial; adapter
fail-before-fetch on deny and provider mismatch; matching-provider and
non-provider compatibility; Web guard regression; package typechecks; exact
manifest; empty staging; worker HEAD unchanged; zero provider calls; zero
external-store calls; and the required worker-return fast gate.

Package commands are specified in the work order. Full repository tests,
builds, release gates, and live commands are not selected because this
bounded implementation makes no release-quality or live-governance claim.

## Boundaries And Non-Goals

No runtime use of `ExternalStoreExecutionGrant`; no Upstash or other store
request; no credential access; no package/dependency edit; no change to
provider registry identity semantics; no general URL allowlist; no RFR,
BuildAuthority, public sync, push, deployment, or production-readiness claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance implementation dispatch with no public-sync authority.

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | R10 GC-018 implementation baseline only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: accepted R9 decision, pinned source inspection and absent-target checks |
| actionEvidence | ACTION_EVIDENCE_PRESENT: this baseline defines the bounded future worker manifest only |
| invocationBoundary | local documentation authoring and read-only source verification |
| interceptionBoundary | no universal runtime, CLI, MCP, provider, network, or external-store interception claim |
| forbiddenExpansion | any path or effect outside the exact eleven-path worker manifest |
| claimLanguage | the committed paired packet authorizes local fake-based implementation proof only |

## Claim Boundary

This baseline authorizes only the exact implementation and evidence manifest
above after the paired packet is committed. It does not itself implement or
prove either control and grants no provider, network, external-store, release,
deployment, public, or push authority.
