# CVF GC-018 Baseline - CADP-AI-T3A Execution Plane Verified Capability Consumer

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-13

Batch ID: CADP-AI-T3A

Dispatch base head: `a2b8c555a`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: implementation worker

## Purpose

Open the first downstream-consumer tranche after T2A bounded closure. Add one
Execution Plane pre-execution adapter that consumes the repository-authenticated
CADP owner handle and existing admission, assignment, distribution, evidence,
and observation contracts without creating a second authority source.

## Authorization

The operator directed `next` following CADP-AI-T2A acceptance on 2026-08-13. This
releases T3A only. T3B Model Gateway integration, provider/live execution,
CLI/MCP, public sync, deployment, production, and cross-runtime claims remain
parked.

## Scope

The worker may add one fail-closed Execution Plane consumer contract and tests,
export it from the package root, refresh the system-chain fingerprint required
by that export, and add a narrow ignore rule for the T2A SQLite runtime-state
files. The adapter may return only an immutable eligibility projection with
`executionAuthorized: false`; it may not invoke an action or provider.

## Non-Goals

No new grant format, owner mint, caller evidence index, raw-secret resolver,
provider adapter, Model Gateway change, live proof, external CLI/MCP adapter,
receipt schema, deployment, public sync, or production-readiness claim.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_system_chain_map_freshness.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `Required Artifact Manifest`; Source Verification Block; Dual Agent Surface Matrix; Public Export Disposition; Agent Operation Trace Block |
| gateRunPurpose | confirmation evidence after source inspection and packet authoring |
| claimBoundary | checker conformance does not prove absence of authority widening or independently accept the adapter |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T2A is independently accepted only for hermetic repository-owned scope | current authority | `docs/reviews/CVF_CADP_AI_T2A_REPOSITORY_OWNER_BINDING_CONTINUATION_COMPLETION_2026-08-13.md` | Reviewer verdict and Claim Boundary | reviewer verdict | T2A independent review | ACCEPT |
| owner authentication is opaque and module-owned | runtime source | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts` | owner handle and reconciliation exports | `isBoundCapabilityOwner` | capability owner binding | ACCEPT |
| observation reconciliation consumes durable replay state | runtime source | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts` | reconciliation implementation | `reconcileGrantWithObservation` | capability owner binding | ACCEPT |
| CADP validators expose non-executing admission, assignment, distribution and evidence decisions | runtime source | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-admission-distribution-profile.contract.ts` | public record types and validators | `validateCapabilityAdmission` | CADP contract | ACCEPT |
| Execution Plane already consumes Guard Contract through repository-relative imports | runtime source | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/execution.bridge.consumer.contract.ts` | imports and receipt wrapping | `ExecutionBridgeConsumerContract` | Execution Plane | ACCEPT |
| provider credential resolution belongs outside T3A | runtime source | `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts` | adapter options and runtime resolution | `credentialReference` | Model Gateway | REJECT |

## Trust And Ordering Decision

The adapter receives an already bound opaque handle and never accepts a grant
object or repository path. It must validate the complete non-side-effecting
record chain before calling durable observation reconciliation. This ordering
prevents malformed or unauthorized requests from consuming invocation or retry
budget. A successful output means only eligible for a later execution handoff;
it never means execution occurred or is authorized by the adapter itself.

## Acceptance Criteria

- forged, copied, serialized, proxied, revoked, or absent handles fail closed;
- invalid admission, assignment, distribution, evidence, or cross-record IDs
  fail before durable invocation consumption;
- exact committed grant observation reconciliation is required last;
- only assigned and admitted action IDs can become eligible;
- raw secret material is neither accepted nor returned;
- returned data is immutable and always carries `executionAuthorized: false`;
- package-root export is proven by a dedicated test;
- T2A SQLite DB/WAL/SHM files are narrowly ignored without ignoring all logs;
- independent review authors new negative probes before acceptance.

## Decision / Baseline

`DISPATCH_READY` for a hermetic T3A no-commit worker. T3B and every live or
provider-facing surface remain outside this baseline.

## Evidence / Verification

Evidence requires Execution Plane typecheck, focused adapter tests, full
Execution Plane tests, package-root proof, Guard Contract focused regression,
system-chain freshness, diff/file-size checks, worker-return fast gate, and an
independent full-diff review.

## Machine Closure Package

N/A with reason: this is a dispatch baseline, not a closure artifact; the
reviewer-owned completion packet carries final closure evidence.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| existing CADP Execution Plane adapter | source search found no CADP capability consumer | NEW_PATH |
| existing consumer pattern | Execution Plane consumer contracts and root barrel exist | ENRICH_EXISTING_PACKAGE |
| Model Gateway overlap | provider credential resolution exists there | DEFER_T3B_NO_EDIT |
| T2A work-order manifest debt | pinned work-order bytes cannot change without invalidating its committed grant | HISTORICAL_IMMUTABLE_DEBT; fresh T3A packet includes the manifest |
| runtime logs residue | `.gitignore` lacks a capability-owner SQLite pattern | NARROW_HYGIENE_COMPANION |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CADP-AI-T3A --title "Execution Plane Verified Capability Consumer Adapter" --date 2026-08-13 --base a2b8c555a --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source verification, split-tranche boundary, ordering invariant, exact scope and acceptance evidence |
| checkerReadAheadConfirmation | applicable checker sources inspected before governed authoring |
| docOnlyNewFields | T3A/T3B split and historical immutable-debt disposition |
| claimBoundary | scaffold provenance only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`implementation`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defect count: 0.

Returned defects: NONE_RETURNED

Dispatch impact: independent negative probes remain mandatory; an empty result
is not correctness evidence.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance internal-consumer tranche; no public-sync action is
authorized.

## Claim Boundary

This baseline authorizes only a hermetic, non-executing Execution Plane
eligibility adapter and narrow runtime-state ignore rule. It makes no provider,
live, T3B, CLI/MCP, public, deployment, production, or cross-runtime claim.
