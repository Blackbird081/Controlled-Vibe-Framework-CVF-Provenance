# CVF GC-018 Baseline - EAFR-R9 External Store Grant And Adapter Destination Policy Owner

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: EAFR-R9-EXTERNAL-STORE-GRANT-AND-ADAPTER-POLICY

Dispatch base head: `f357d8e50fce8397d613dc597af56aab5bf7c98f`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator through the committed EAFR roadmap

Reviewer owner: current independent orchestrator/reviewer

Worker target: external-store grant and adapter destination-policy worker role

providerExecutionAuthority: FORBIDDEN

## Purpose

Source-verify and dispatch a bounded, orchestrator-issued external-store
execution grant that parallels the existing provider-execution grant, and a
single shared, non-duplicated destination-policy owner the gateway adapter can
consume to close its injected-fetch bypass, without weakening the R7/R8
fail-closed egress defaults.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id EAFR-R9 --title "External Store Grant And Adapter Destination Policy Owner" --date 2026-08-26 --base f357d8e50 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source-verified grant-contract precedent, shared-package reachability finding, destination-policy owner contract, and egress-invariant preservation rule |
| checkerReadAheadConfirmation | dispatch, authority, trace, delta, epistemic and worker-return checker sources reviewed |
| docOnlyNewFields | External Store Grant Contract; Adapter Destination Policy Owner Contract; Egress Invariant Preservation Rule |
| claimBoundary | dispatch authoring only; no live, provider, network, credential, build, package-dependency or public claim |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
| --- | --- | --- |
| EAFR-R8 blocked closure | `docs/reviews/CVF_EAFR_R8_NON_LIVE_EXTERNAL_STORE_ISOLATION_AND_ADAPTER_BOUNDARY_COMPLETION_2026-08-26.md`; material commit `fe0ea5937` | RELEASED |
| R8 corrective scope statement | same review, Risk / Corrective Action naming an orchestrator-issued external-store grant and a shared, non-duplicated adapter destination-policy owner | ACCEPT |
| EAFR-R7 blocked closure | `docs/reviews/CVF_EAFR_R7_FAIL_CLOSED_PROVIDER_EGRESS_AUTHORITY_REPAIR_COMPLETION_2026-08-26.md`; material commit `74cf99354` | ACCEPT |
| EAFR roadmap authority | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md`, EAFR-R9 row and Acceptance Criteria | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`external store execution authority`, role=`worker`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "external store execution authority" --role worker --lifecycle-phase dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | none |
| Dispatch impact | ordinary CVF controls apply |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_subagent_provider_execution_authority.py`; `governance/compat/check_equivalence_claim_evidence.py` |
| literalTokensReviewed | Source Verification Block; Current Runtime Freshness Verification; exact manifest; no-commit status; trace labels; Public Export Disposition; providerExecutionAuthority declaration; equivalence disposition tokens; Negative Search And Collision Discipline; Intake Role Routing Decision; Evidence Reuse And Encoding Plan; Worker Return Packet Shape Contract required terms |
| gateRunPurpose | confirm as evidence that the source-verified dispatch already matches required shape |
| claimBoundary | structural conformance does not prove either control is implementable inside the manifest |

## Current Runtime Freshness Verification

Verified directly at HEAD `f357d8e50fce8397d613dc597af56aab5bf7c98f` on
2026-08-26, after R8 session-sync closure:

- the R7/R8 fail-closed guard (`classifyDestination` in
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts`)
  is retained unchanged; it denies any hostname that is not a recognised
  provider endpoint, a loopback host, or a non-egress protocol, before any
  network I/O;
- provider egress under a denied destination is gated by
  `evaluateProviderExecutionAuthority` and the `ProviderExecutionGrant`
  contract, both defined in
  `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` (lines
  1-91), re-exported from the `cvf-control-plane-foundation` package, and
  already imported by the guard;
- `ProviderExecutionGrant` and `ProviderExecutionRequest` are scoped to a
  single `provider: string` field with `allowedProviders: string[]`; neither
  type has a destination-class or external-store-scoped field today, so no
  existing grant instance can authorize deliberate Upstash or other
  external-store use without either a new sibling contract or a generalized
  field: this is a real design decision, not a copy-paste extension;
- `classifyDestination` itself is defined only inside the test-only file
  `cvf-web/src/test/provider-execution-guard.ts`; it is not exported from any
  shared package and is not importable outside `cvf-web`'s test tree;
- `EXTENSIONS/CVF_MODEL_GATEWAY/package.json` declares zero runtime or local
  workspace dependencies (`devDependencies` only: `@types/node`,
  `@vitest/coverage-v8`, `typescript`, `vitest`); the gateway package cannot
  import `cvf-control-plane-foundation`, `cvf-web`, or any other local package
  without a new dependency edit, which is itself an out-of-manifest,
  cross-package authority change;
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts`
  still calls a caller-supplied `fetchImpl` directly in `execute()` (lines
  53-70), with no destination check of any kind before invoking it; this is
  the unchanged R7/R8 adapter residual;
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/openai-compatible-execute-adapter.test.ts`
  is the existing focused test file for the adapter and is the only test path
  this baseline's manifest may extend;
- the R8 work order's Adapter Boundary Contract already forbids copying
  `classifyDestination`'s logic into a second permit list; R9 must therefore
  either (a) source-verify and dispatch a shared package both `cvf-web` and
  `EXTENSIONS/CVF_MODEL_GATEWAY` can depend on, or (b) return
  `BOUNDED_WITH_NAMED_RESIDUAL` again, this time naming the missing package
  edge itself as the blocking condition, not merely the missing logic.

No live, provider, network, credential, build, or package-dependency command is
authorized by this baseline. R9 changes source-verification and dispatch
authoring only; it claims no provider, deployment, release, or production
posture, and it does not itself add a package dependency, move
`classifyDestination`, or grant live external-store execution.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R9 is scoped to exactly two controls named by R8's corrective lane | ROADMAP_AUTHORITY | `docs/reviews/CVF_EAFR_R8_NON_LIVE_EXTERNAL_STORE_ISOLATION_AND_ADAPTER_BOUNDARY_COMPLETION_2026-08-26.md` | Risk / Corrective Action | EAFR-R9 | R8 completion review | ACCEPT |
| R9 must preserve R8 isolation while source-verifying the grant and shared owner | ROADMAP_AUTHORITY | `docs/roadmaps/CVF_EAFR_REMEDIATION_ROADMAP_2026-08-25.md` | Acceptance Criteria, R9 row | EAFR-R9 | EAFR roadmap | ACCEPT |
| the R7/R8 guard denies unrecognised destinations before network I/O and is unchanged | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts` | destination classifier default branch, line 118 | classifyDestination | cvf-web provider execution guard | ACCEPT |
| the orchestrator-grant contract and evaluator already exist for provider execution, scoped to `provider` only | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` | lines 5-14 (`ProviderExecutionGrant`), lines 48-55 (`ProviderExecutionRequest`), lines 57-91 (`evaluateProviderExecutionAuthority`) | ProviderExecutionGrant; ProviderExecutionRequest; evaluateProviderExecutionAuthority | cvf-control-plane-foundation delegation contract | ACCEPT |
| the guard already imports the grant contract from the shared foundation package | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts` | import block, lines 1-4 | evaluateProviderExecutionAuthority; ProviderExecutionGrant | cvf-web provider execution guard | ACCEPT |
| `classifyDestination` is defined only in a test-only file and is not exported from any shared package | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/provider-execution-guard.ts` | file scope; no barrel or package export of this symbol exists | classifyDestination | cvf-web provider execution guard | ACCEPT |
| the gateway package declares zero runtime or local workspace dependencies | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/package.json` | `dependencies`/`devDependencies` fields | cvf-model-gateway package manifest | cvf-model-gateway | ACCEPT |
| the adapter still calls a caller-injected fetch with no destination check | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/src/openai-compatible-execute-adapter.ts` | `execute()` body, lines 47-70 | createOpenAiCompatibleExecuteAdapter | OpenAI-compatible execute adapter | ACCEPT |
| the existing focused adapter test file is the only extensible test path for R9 | RUNTIME_SOURCE_FACT | `EXTENSIONS/CVF_MODEL_GATEWAY/tests/openai-compatible-execute-adapter.test.ts` | file scope | adapter focused test suite | cvf-model-gateway tests | ACCEPT |

## External Store Grant Contract

A deliberate external-store execution capability must be authorized the same
way deliberate provider execution is: by an orchestrator-issued, bounded,
expiring grant evaluated before the operation, never by a test-selection
variable or an ambient credential.

1. **Grant shape precedent.** The grant must reuse the existing
   subject/delegation/call-budget/expiry shape already proven by
   `ProviderExecutionGrant` and `evaluateProviderExecutionAuthority`. R9 must
   source-verify and decide, without implementing, whether this is achieved by
   (a) a new sibling contract type in the same owning file or package scoped to
   an external-store identifier, or (b) a generalized field on the existing
   contract; either decision must preserve `ProviderExecutionGrant`'s existing
   behavior for callers that do not use the new field.
2. **No ambient authority.** An environment variable, local `.env` file value,
   or test-selection flag must never itself constitute a grant. Only an
   explicit, orchestrator-authored grant object, evaluated by a function
   mirroring `evaluateProviderExecutionAuthority`'s checks, may permit the
   operation.
3. **Fail-closed default.** Absent a valid grant, external-store execution
   remains denied exactly as it is today; R9 must not weaken the existing
   denial to make the grant path reachable.
4. **Bounded scope.** The grant, if drafted, is a contract-and-evaluator design
   only in this tranche; wiring it into `rate-limit.ts` or
   `storage-adapter.ts` to permit a real deliberate live call is out of scope
   unless a later work order explicitly authorizes it.

## Adapter Destination Policy Owner Contract

`classifyDestination` must become reachable by both the cvf-web guard and the
gateway adapter through one shared, non-duplicated owner, not by copying its
logic into a second permit list and not by silently re-accepting the residual.

Acceptable dispositions, in preference order:

- **DESIGNATED_SHARED_PACKAGE_OWNER**: R9 source-verifies and names the exact
  shared package (existing or newly justified) both `cvf-web` and
  `EXTENSIONS/CVF_MODEL_GATEWAY` can depend on without violating either
  package's existing boundary, and states the precise interface the adapter
  would call. Adding the dependency edge and moving the function is
  implementation, deferred to the follow-on work order; R9 decides and records
  the owner only.
- **BOUNDED_WITH_NAMED_RESIDUAL**: no such shared owner can be source-verified
  inside the current package boundaries without a change this baseline does
  not authorize (for example, a new shared package, or a dependency edit to an
  existing one). The blocking condition and the exact authority required must
  be named.

`ACCEPTED_AS_IS` and silent carry-forward are forbidden dispositions. The
residual was accepted once in R7 and again in R8; R9 exists to either name its
shared owner or explain precisely why none exists yet, not to re-accept it
without new evidence.

### Provider registry accounting for this boundary

`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and
`PROVIDER_CAPABILITY_REGISTRY` remain provider-identity-keyed, as established
in R6 and preserved through R7/R8. Neither declares a hostname, so neither
can serve as, or substitute for, the destination-policy owner this baseline
requires. R9 must not resolve the boundary by keying on `providerId`.

## Egress Invariant Preservation Rule

The R7/R8 fail-closed default must survive R9 unchanged:

- an unrecognised hostname must still be denied before network I/O;
- provider endpoints must still be derived from gateway constants;
- loopback and non-egress protocols must remain the only ungranted permits;
- an external-store grant or a shared destination-policy owner must not widen
  provider egress and must not create a second permit list a future endpoint
  could hide behind.

Any drafted change that would restore silent external egress, or that would
make deliberate live external-store use permanently unreachable, is a fail
condition, not a trade-off, regardless of how many residuals it would appear
to close. `provider-execution-guard.ts`'s `classifyDestination` behavior is not
writable for behavioral change in this tranche; only its shared-owner
reachability may be decided.

## Exact Worker Manifest

This is a source-verification and dispatch-authoring tranche. The worker
manifest for the follow-on implementation work order is not yet open; R9
itself produces only:

1. This baseline (dispatcher-owned).
2. The paired work order (dispatcher-owned):
   `docs/work_orders/CVF_AGENT_WORK_ORDER_EAFR_R9_EXTERNAL_STORE_GRANT_AND_ADAPTER_DESTINATION_POLICY_OWNER_2026-08-26.md`.
3. `docs/reviews/CVF_EAFR_R9_EXTERNAL_STORE_GRANT_AND_ADAPTER_DESTINATION_POLICY_OWNER_WORKER_RETURN_2026-08-26.md`
   (worker-owned, no-commit).

No source or test file outside this documentation set may be edited under
this baseline. Any need to write a grant contract type, an evaluator function,
a shared package, a package-dependency edit, or an adapter change returns
`BLOCKED_WITH_REASON` to the orchestrator for a fresh, separately authorized
implementation work order.

## Baseline Decision / Proposed Tranche

Dispatch one bounded, no-commit source-verification and design-decision
tranche. The worker decides and records, without implementing: (a) the exact
grant-contract extension shape for external-store execution, reusing the
`ProviderExecutionGrant`/`evaluateProviderExecutionAuthority` precedent, and
(b) one Adapter Destination Policy Owner disposition, per the contract above.
Any need to edit source, tests, a package manifest, an environment file, a
checker, a roadmap, a registry, or to run a provider/build/live command,
returns blocked to the orchestrator.

## Evidence / Verification

The worker must return: the exact grant-contract design decision with its
source-verified precedent citations; the exact Adapter Destination Policy
Owner disposition with its source-verified reachability evidence; proof that
no source or test file was edited; confirmation that the R7/R8 egress
invariants are undisturbed because no runtime file changed; the negative
search proving no prior EAFR-R9 artifact existed before this dispatch; the
worker-return fast gate; unchanged HEAD; empty staging; and an explicit
zero-provider-call and zero-external-store-call statement.

## Risk / Rollback

Primary risk is drafting a grant or owner design that quietly widens egress
authority or that pre-commits to an implementation before the operator opens a
fresh, separately authorized work order for it. Secondary risk is treating
`BOUNDED_WITH_NAMED_RESIDUAL` as a failure to avoid rather than an honest
result. Rollback is the bounded pending worker diff, which in this
documentation-only tranche is limited to the worker-return file.

## Claim Boundary

This baseline authorizes only bounded source verification and dispatch
authoring for an external-store grant design and an adapter destination-policy
owner decision. It authorizes no provider, live, network, credential, build,
dependency, environment-file, checker, roadmap, registry, public-sync,
deployment, or push action, no RFR resumption, no BuildAuthority repair, and no
implementation of the grant contract, the evaluator, the shared package, or the
adapter change. Naming a design decision is not a security proof and makes no
claim about credential hygiene, past traffic, or production readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance source-verification and dispatch authoring; public
sync is separately governed and not authorized.
