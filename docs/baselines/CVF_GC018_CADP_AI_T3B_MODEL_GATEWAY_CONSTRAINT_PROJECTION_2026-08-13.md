# CVF GC-018 Baseline - CADP-AI-T3B Model Gateway Constraint Projection

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-13

Batch ID: CADP-AI-T3B

Dispatch base head: `52a5833c5`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: implementation worker

## Purpose

Open the bounded Model Gateway integration tranche after T3A acceptance. Add a
pure local constraint projection that combines non-authoritative T3A eligibility
metadata with repository-owned provider capability metadata without resolving a
credential, calling a provider, recording quota use, or authorizing execution.

## Authorization

The operator directed `continue` from the T3A closed checkpoint on 2026-08-13.
This releases T3B dispatch and implementation only. T4-T7, provider/live,
CLI/MCP, public sync, deployment, production, trusted-evidence, and
cross-runtime claims remain parked.

## Scope

The worker may add one strict Model Gateway constraint-projection contract and
tests and export it through the package root. It may consume only the accepted
T3A projection, a repository-authenticated owner handle, and provider-neutral
constraint fields. Every output must be immutable and retain literal false
flags for execution, live execution, provider calls, and credential resolution.

## Non-Goals

No credential resolution, environment-secret read, provider adapter, execution
bridge, network/process call, quota mutation, provider-specific request body,
receipt/trusted-evidence claim, new registry authority, live proof, public sync,
deployment, or production-readiness claim.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; Source Verification Block; Required Artifact Manifest; Dual Agent Surface Matrix; Public Export Disposition; Agent Operation Trace Block |
| gateRunPurpose | confirmation evidence after source inspection and packet authoring |
| claimBoundary | checker conformance does not prove semantic isolation, absence of authority widening, or T3B acceptance |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T3A is accepted only as a non-executing eligibility projection | current authority | `docs/reviews/CVF_CADP_AI_T3A_EXECUTION_PLANE_VERIFIED_CAPABILITY_CONSUMER_COMPLETION_2026-08-13.md` | Disposition and Claim Boundary | `ACCEPT_CLOSED_PASS_BOUNDED`; material commit `f1dc9a6f7a0fc7824d6ba82cce3db47bbdfd91ac` | T3A independent review | ACCEPT |
| provider capability negotiation is pure local metadata logic | runtime source | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-negotiation.ts` | exported function and result | `negotiateProviderCapability` | Model Gateway | ACCEPT |
| capability metadata is repository-owned | runtime source | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | registry export | `PROVIDER_CAPABILITY_REGISTRY` | Model Gateway | ACCEPT |
| provider methods have a closed contract | runtime source | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-method-contract.ts` | method type | `ProviderMethodName` | Model Gateway | ACCEPT |
| adapter admission explicitly cannot authorize live execution | runtime source | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-adapter-admission.ts` | admission record with literal false value | `liveExecutionAuthorized` | Model Gateway | ACCEPT |
| credentials can be resolved by the credential boundary | forbidden runtime source | `EXTENSIONS/CVF_MODEL_GATEWAY/src/credential-boundary.ts` | resolution methods | `resolveSecretForRuntime`; `resolveMetadata` | credential boundary | REJECT |
| quota use can be mutated | forbidden runtime source | `EXTENSIONS/CVF_MODEL_GATEWAY/src/quota-ledger.ts` | mutation method | `recordUse` | quota ledger | REJECT |
| execution bridge can call an adapter | forbidden runtime source | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-execution-bridge.ts` | execution method | `execute` | execution bridge | REJECT |

## Trust And Ordering Decision

T3A output is plain frozen metadata and is not an authenticated receipt; copied
or reconstructed bytes are therefore not proof of provenance. T3B must use the
opaque owner handle only to confirm the grant identity to which the projection
refers, must never promote the projection into execution authority, and must
perform all strict input and identity checks before repository-owned capability
negotiation. Even a satisfied result remains non-authoritative.

## Acceptance Criteria

- strict plain, exact-shape, non-Proxy inputs fail closed;
- the owner handle is authentic and its grant identity matches the T3A projection;
- only an `ELIGIBLE`, reconciled T3A projection with `executionAuthorized: false` is considered;
- provider/model/method support comes only from the repository registry;
- caller constraints can narrow but never widen registry capabilities;
- copied or reconstructed T3A projection bytes gain no execution authority;
- raw-secret-shaped fields and provider-specific payloads are rejected;
- no credential, quota mutation, adapter, execution bridge, network, or process path is reachable;
- every result is deeply immutable and all four authorization flags are literal false;
- package-root export is proven and independently reviewed.

## Decision / Baseline

`DISPATCH_READY` for a hermetic T3B no-commit worker. The baseline authorizes a
metadata projection only; every provider/live or executing path remains parked.

## Evidence / Verification

Evidence requires Model Gateway typecheck, focused adversarial tests, the full
package suite, root-export proof, focused T3A/owner-binding regression,
system-chain freshness, file-size/diff checks, worker-return gates, and a fresh
independent full-diff review with reviewer-authored negative probes.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | T3B work order | `Status: DISPATCH_READY`; worker must not commit | N/A with reason: dispatch, not closure |
| Completion or reviewer artifact | future T3B completion review | reviewer-owned after worker return | N/A with reason: not yet authored |
| Roadmap state | CADP roadmap | T3B dispatched; later tranches parked | PASS |
| Registry JSON | no registry change authorized | N/A | BLOCKED with reason: dispatch does not authorize registry mutation |
| Registry Markdown | no registry change authorized | N/A | BLOCKED with reason: dispatch does not authorize registry mutation |
| External evidence digest | T3A completion committed at `f1dc9a6f7` | SHA-256 `d8c4cab34ca0d9cb4144122025b70db489b939b01adc38c6944ee0aa61e14171` | PASS |
| System loop interlock | no loop registry change authorized | N/A | N/A with reason |
| Session continuity | active handoff and state sources | worker execution is next | PASS |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| T3A predecessor material exists | commit `f1dc9a6f7a0fc7824d6ba82cce3db47bbdfd91ac` contains accepted material | PASS |
| T3A completion digest matches | committed/worktree SHA-256 `d8c4cab34ca0d9cb4144122025b70db489b939b01adc38c6944ee0aa61e14171` | PASS |
| T3B remains non-executing | all result authorization flags are required literal false | PASS |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | current Model Gateway registry, negotiation, method, admission, credential, quota and execution-bridge sources; accepted T3A contract |
| Runtime behavior claimed | BOUNDED: future worker may add only a hermetic provider-neutral constraint projection |
| Provider/live proof claimed | N/A_WITH_REASON: forbidden in T3B |
| Public-sync claimed | N/A_WITH_REASON: forbidden in T3B |
| Freshness disposition | PASS - targeted current-source reads separate pure metadata seams from secret, mutation and execution owners |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| existing CADP Model Gateway projection | source/path search found none | NEW_PATH |
| pure negotiation and registry pattern | current Model Gateway source | ENRICH_EXISTING_PACKAGE |
| credential/quota/execution overlap | explicit current owners found | FORBIDDEN_IMPORT_OR_CALL |
| proposed baseline/work-order/worker paths | repository collision search before authoring | NEW_PATHS |
| system-chain entry | no current Model Gateway root fingerprint entry found | CONDITIONAL_NO_CHANGE_WITH_REASON |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CADP-AI-T3B --title "Model Gateway Constraint Projection" --date 2026-08-13 --base 52a5833c5 --commit-mode WORKER_MUST_NOT_COMMIT --stdout --include-worker-return-skeleton` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source verification, unauthenticated-projection boundary, forbidden owners, exact manifest and independent probes |
| checkerReadAheadConfirmation | applicable checker sources inspected before governed authoring |
| docOnlyNewFields | T3B constraint semantics and explicit non-authoritative projection disposition |
| claimBoundary | scaffold provenance only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defect count: 0.

Returned defects: NONE_RETURNED

Dispatch impact: independent negative probes remain mandatory; an empty result
is not correctness evidence.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Model Gateway tranche; no public-sync action is authorized.

## Claim Boundary

This baseline dispatches only a local, provider-neutral, non-authoritative
constraint projection. It makes no provider compatibility, credential, quota,
live, execution, trusted-evidence, CLI/MCP, public, deployment, production, or
cross-runtime claim.
