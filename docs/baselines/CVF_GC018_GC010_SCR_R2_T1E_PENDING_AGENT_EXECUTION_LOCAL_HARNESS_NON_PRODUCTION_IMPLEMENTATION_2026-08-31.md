# CVF GC-018 GC010 SCR-R2-T1E Pending Agent Execution Local Harness Non-Production Implementation

Memory class: governed-baseline

docType: baseline

Status: DISPATCHED_IMPLEMENTATION_BOUNDED

Batch ID: GC010-SCR-R2-T1E

Date: 2026-08-31

dispatchBaseHead: `ab6a4ef9f`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize the exact two-path non-production implementation selected by T1D:
one synchronous cvf-web local harness that becomes the first non-test consumer
of the accepted T1C composition, and one focused test. No package/barrel export,
registration, route or external effect is authorized.

## Authority Chain

- Operator instructed continuation of the same GC010 system chain and allowed
  an internal sub-agent worker under orchestrator/reviewer control.
- Accepted T1C durable single-node material: `82c64a6f5`.
- Accepted T1D decision material: `0e4aacdc6`.
- T1D terminal:
  `NON_PRODUCTION_CONSUMER_EXPORT_BOUNDARY_READY_FOR_T1E_CONSIDERATION`.
- T1D assessment and independent reviewer addendum:
  `docs/assessments/CVF_GC010_SCR_R2_T1D_PENDING_AGENT_EXECUTION_NON_PRODUCTION_CONSUMER_PACKAGE_EXPORT_BOUNDARY_DECISION_2026-08-31.md`.
- Paired work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R2_T1E_PENDING_AGENT_EXECUTION_LOCAL_HARNESS_NON_PRODUCTION_IMPLEMENTATION_2026-08-31.md`.

Historical GC010-SCR-R1 production work remains parked and is not authority
for this local harness.

## Source / Predecessor Evidence

Accepted T1C source at `82c64a6f5` supplies the unchanged composition, core
types and specialized SQLite store. Accepted T1D material `0e4aacdc6` supplies
the controlling exact-two-path selection and reviewer correction requiring a
static client/import boundary assertion. Direct committed source, not provider
memory or historical production-roadmap prose, controls implementation.

## Scope / Target / Owner Boundary

The internal worker owns exactly two new implementation files and one worker
return. The harness owns local construction, one ordered lifecycle and cleanup;
accepted T1C retains lifecycle, grant, CAS, digest, approval/policy and storage
semantics. Reviewer owns acceptance, bounded repair and commits. All existing
files and external-effect owners remain read-only.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| T1C composition | accepted at `82c64a6f5`; builder owns store wrappers and close | harness may call exported wrappers only | ACCEPT |
| T1D owner decision | accepted at `0e4aacdc6` with exact two-path manifest | implement without widening paths or imports | ACCEPT |
| Existing SQLite dependency | already present in private cvf-web package | no package or lockfile mutation | ACCEPT |
| Route/provider/audit/production | explicitly parked | no import, registration or call | ACCEPT_PARKED |

## Exact Implementation Manifest

The worker may create exactly these implementation paths:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/pending-agent-execution-local-harness.ts`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/pending-agent-execution-local-harness.test.ts`

The full worker changed set is those two paths plus the named worker return.
No existing file may be edited.

## Required Harness Contract

Export exactly:

- `runPendingAgentExecutionLocalHarness`;
- `PendingAgentExecutionLocalHarnessInput`;
- `PendingAgentExecutionLocalHarnessOutcome`.

The harness is synchronous. It constructs exactly one runtime per invocation
with `buildPendingAgentExecutionRuntime(input.dbPath)`, passes the explicit
caller-owned path unchanged, and drives exactly:

`create -> claim -> begin -> terminal`.

It stops on the first failure, never returns or fabricates a grant, never
retries or recovers, and always closes a constructed runtime in `finally`.
The outcome records the truthful stopped stage, reason and record. Only a
successful terminal transition returns `ok: true`.

## Import Boundary

Harness value import: only `buildPendingAgentExecutionRuntime` from
`../pending-agent-execution-composition`.

Harness type-only imports: only accepted pending-execution types from
`../pending-agent-execution`. It must not import the SQLite store directly.

No route, React/client, Next UI, provider/admission, audit, MAO/execution-plane,
configuration/environment, fetch, process environment or package/barrel owner
may be imported or called. Directory placement alone is not proof; the focused
test must statically enforce the import/client boundary.

## Required Focused Proof

- Real happy path with versions `0/1/2/3` and statuses
  `CREATED/CLAIMED/EXECUTING/SUCCEEDED`.
- Actor, request, claim, attempt and terminal identities/reason preserved.
- Reopen the same SQLite file after harness close and verify durable terminal
  state, then close the read handle.
- Relative database path fails closed without implicit resolution.
- Approval-not-found and policy-fingerprint drift stop at claim and never
  produce executing or terminal state.
- Temporary directory is deletable immediately after return on Windows.
- Static source proof permits only the two selected internal module specifiers
  and rejects client, route, provider, audit, MAO, config/env and network use.
- Run focused T1E plus T1A/T1C regression suites and TypeScript no-emit.

## Acceptance Criteria

- Exactly two implementation paths plus one worker return; no other mutation.
- The harness is the first non-test caller of the T1C builder.
- One construction and one ordered lifecycle per invocation.
- No later stage occurs after an earlier failure.
- Authentic grant is consumed only by begin and never escapes the harness.
- Terminal expected version comes from begin; claim ID comes from the authentic
  grant; caller supplies attempt and terminal data.
- Constructed runtime closes even on denial/failure.
- All focused proof and governance gates pass with zero external calls.
- No package export, trigger, route or production claim.

## Decision / Baseline / Proposed Tranche

T1E is a bounded implementation prerequisite only. Successful worker return
still requires independent review and does not open route/provider/audit or
production integration automatically.

successorTrancheOpened: NO

## Evidence / Verification

Required evidence includes initial and final HEAD/status, exact three-path
worker manifest, source/import scans, focused Vitest receipts, TypeScript
receipt, worker-return fast gate, actual quality checker, zero provider/external
calls and no commit.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GC010-SCR-R2-T1E --title "Pending Agent Execution Local Harness Non-Production Implementation" --date 2026-08-31 --base ab6a4ef9f --commit-mode WORKER_MUST_NOT_COMMIT --dependency "accepted T1D consumer boundary material 0e4aacdc6; exact two-path local harness implementation" --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --include-worker-return-skeleton --stdout` |
| generatedProfile | generic internal-worker implementation dispatch plus no-commit return profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact two-path implementation, three-path worker manifest, lifecycle, imports, tests, gates and parked boundaries |
| checkerReadAheadConfirmation | dispatch, lifecycle, read-ahead, review-cost, worker-return, trace, delta, public, handoff, external-intake and storage checkers read |
| implementationFields | localHarnessContract; firstFailureStop; staticClientBoundary; exactTwoPathManifest |
| docOnlyNewFields | implementationFields; internalWorkerChangedSet; staticClientBoundary |
| claimBoundary | authoring provenance only; no harness exists from this baseline |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | normal bounded implementation controls remain binding |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_foundation_storage_layout.py` |
| literalTokensReviewed | dispatch envelope, source dispositions, internal-agent route, no-commit return, trace/delta labels, handoff rows, public/external/storage boundaries |
| gateRunPurpose | confirmation/evidence after source and checker inspection; not first discovery |
| claimBoundary | artifact conformance only; worker/reviewer own implementation correctness |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private non-production implementation dispatch; public export is forbidden.

## Claim Boundary

This baseline authorizes exactly two future local implementation files and one
worker return. It does not implement or invoke the harness, export a package,
register a trigger, wire route/provider/audit, prove distributed safety,
synchronize public artifacts, deploy, open production or authorize an
automatic successor.
