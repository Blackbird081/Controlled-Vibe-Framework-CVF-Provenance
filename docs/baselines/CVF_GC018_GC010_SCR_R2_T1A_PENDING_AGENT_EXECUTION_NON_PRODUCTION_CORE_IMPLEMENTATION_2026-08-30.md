# CVF GC-018 GC010 SCR-R2-T1A Pending Agent Execution Non-Production Core Implementation

Memory class: governed-baseline

docType: baseline

Status: DISPATCHED_IMPLEMENTATION_BOUNDED

Batch ID: GC010-SCR-R2-T1A

Date: 2026-08-30

dispatchBaseHead: `be7ce7d2b`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize one bounded non-production implementation slice for the corrected
T0B pending-execution contract. The slice creates the core schema, canonical
digest, single-process linearizable store, runtime-held single-use capability,
state transitions, and focused tests without adding a route, provider adapter,
or production consumer.

## Authority Chain

- Operator instructed continuation of the same GC010 system chain and granted
  full orchestrator/reviewer authority.
- Accepted T0B material commit: `7b9fc8b7f`.
- T0B completion:
  `docs/reviews/CVF_GC010_SCR_R2_T0B_PENDING_AGENT_EXECUTION_SAFE_RESUME_CONTRACT_DECISION_COMPLETION_2026-08-30.md`.
- Controlling corrected contract:
  `docs/assessments/CVF_GC010_SCR_R2_T0B_PENDING_AGENT_EXECUTION_SAFE_RESUME_CONTRACT_DECISION_2026-08-30.md`.
- Paired work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R2_T1A_PENDING_AGENT_EXECUTION_NON_PRODUCTION_CORE_IMPLEMENTATION_2026-08-30.md`.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| Corrected safe-resume contract | T0B completion and material `7b9fc8b7f` retain `SAFE_RESUME_CONTRACT_READY_FOR_T1_CONSIDERATION` | one bounded non-production slice only | ACCEPT |
| Exact source manifest | two absent paths verified at dispatch base | create exactly core module and focused test | ACCEPT |
| Production consumer | historical R1 T1 remains parked | no route/export/provider consumer in T1A | ACCEPT |

## Scope

Worker-owned implementation paths:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.test.ts`
- `docs/reviews/CVF_GC010_SCR_R2_T1A_PENDING_AGENT_EXECUTION_NON_PRODUCTION_CORE_IMPLEMENTATION_WORKER_RETURN_2026-08-30.md`

Everything else is read-only to the worker. This tranche is explicitly
single-process and non-production. It does not modify `/api/execute`, approval
PATCH, package exports, AER, provider-attempt admission, control-plane storage,
configuration, dependencies, workflows, continuity, or roadmap state.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| T0B corrected contract permits one non-production slice | decision authority | `docs/assessments/CVF_GC010_SCR_R2_T0B_PENDING_AGENT_EXECUTION_SAFE_RESUME_CONTRACT_DECISION_2026-08-30.md` | Independent Reviewer Contract Correction | `PendingAgentExecutionRecord`; controlling lifecycle | T0B reviewer | ACCEPT |
| Approval snapshot/hash and actor checks exist | runtime/schema | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.ts` | exported functions | `computeApprovalRequestHash`; `approvalRecordMatchesActor` | cvf-web approval binding | ACCEPT |
| Approval record exposes required linked evidence | runtime/schema | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts` | interfaces | `ApprovalRequestRecord`; `ApprovalRequestSnapshot` | cvf-web approval store | ACCEPT |
| Provider attempt owner remains outside this slice | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/provider-attempt-admission.ts` | ledger/admission exports | `ProviderAttemptLedger`; `admitProviderAttempt` | cvf-web provider admission | ACCEPT |
| No current pending-execution owner exists | negative source verification | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src` | exact token search at `be7ce7d2b` | `PendingAgentExecution`; `ResumeAuthorityGrant`; `claimPendingExecution` | proposed new core owner | ACCEPT |

## Mandatory Implementation Contract

1. Create `PendingAgentExecutionRecord` with schema version
   `cvf.pendingAgentExecution.v1`, complete immutable authority payload,
   mutable versioned transition metadata, and the controlling lifecycle.
2. Implement a local RFC8785/JCS-compatible canonicalizer for the supported
   JSON domain and lowercase SHA-256 digest. Reject undefined, non-finite
   numbers, sparse arrays, non-plain objects, cycles, unsupported values, and
   unknown environment fields before record creation.
3. Define a deterministic `GuardPolicySnapshot` containing schema version,
   ordered guard identifier/version/config-digest rows, phase, risk, role,
   channel, control mode, and policy snapshot identifier; compute its
   fingerprint from the same canonicalizer.
4. Expose a store interface with versioned `compareAndSwap`. Implement only a
   synchronous in-memory adapter whose declared boundary is one JavaScript
   process and whose CAS check plus update does not yield. It must be named and
   documented non-production and must never claim cross-process safety.
5. Implement create, claim, begin-execution, and terminal transitions. Resume
   input contains only pending ID and authenticated actor; current approval is
   injected/read separately and verified against the stored snapshot/hash.
6. `ResumeAuthorityGrant` is never serialized or publicly constructible.
   Runtime authenticity uses a module-private `WeakSet` or stronger private
   membership registry. Beginning execution deletes membership before the
   durable-in-adapter `CLAIMED -> EXECUTING` CAS; CAS failure grants zero
   provider authority.
7. Allocate and persist `attemptIndex` before `EXECUTING`. Final states are
   `SUCCEEDED`, `FAILED`, `DENIED`, or `UNKNOWN_TERMINAL`. Pre-start terminal
   states are `EXPIRED`, `STALE`, and `ABANDONED_BEFORE_START`. No terminal
   state may transition back to executable state.
8. No function in this slice may import or call a provider, AER,
   `admitProviderAttempt`, `recordProviderCallStart`, route handler, or durable
   audit store. The module supplies a future composition prerequisite only.

## Acceptance Criteria

- Exact three-path worker manifest and no dependency/package-lock change.
- Focused tests prove every immutable field changes the digest; invalid JSON
  and secret/non-allowlisted environment input fail closed.
- Two concurrent/reentrant claims in the declared single-process boundary
  yield one grant; stale versions and status drift fail CAS.
- Structurally forged and replayed grants fail at runtime.
- Crash-before-executing permits only `ABANDONED_BEFORE_START`; ambiguity after
  `EXECUTING` permits only `UNKNOWN_TERMINAL`, never replay.
- Terminal results remain distinct and all correlation identifiers are stored.
- Focused tests and cvf-web TypeScript no-emit pass with zero provider calls.

## Decision / Baseline / Proposed Tranche

T1A is a prerequisite core implementation, not the historical roadmap's
production T1 consumer. It may prove local contract behavior only. A later
tranche must independently decide durable adapter, route/composition,
provider-admission, audit, and real consumer ownership.

## Evidence / Verification

Required evidence: fresh HEAD/status, exact diff, focused Vitest result,
TypeScript no-emit result, negative import/call search, worker-return fast gate,
zero-call statement, and no-commit statement.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GC010-SCR-R2-T1A --title "Pending Agent Execution Non-Production Core Implementation" --date 2026-08-30 --base be7ce7d2b --commit-mode WORKER_MUST_NOT_COMMIT --dependency "accepted T0B contract material 7b9fc8b7f; bounded non-production core only" --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 2 --stdout` |
| generatedProfile | generic worker dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled exact two-source implementation boundary, tests, owners, gates and claims |
| checkerReadAheadConfirmation | dispatch, lifecycle, structural, trace, delta, worker-return and public-disposition checkers read |
| docOnlyNewFields | declaredAdapterBoundary; terminalTransitionDisposition |
| claimBoundary | authoring provenance only |

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
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_machine_closure_package.py` |
| literalTokensReviewed | dispatch envelope fields; source table columns; no-commit return shape; trace labels; claim boundary fields; public disposition |
| gateRunPurpose | confirmation evidence before dispatch, not runtime truth |
| claimBoundary | artifact conformance only; implementation correctness remains worker/reviewer-owned |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private non-production implementation dispatch; no public artifact or
release claim is authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | paired work order | dispatch status | PENDING_WORKER_RETURN |
| Completion or reviewer artifact | worker return then reviewer disposition | reviewer-owned | PENDING_REVIEW |
| Roadmap state | GC010 roadmap | historical T1 remains parked | PASS |
| Registry JSON | active session state | session-sync steward only | N/A with reason: dispatch precedes continuity sync |
| Registry Markdown | front door/handoff | steward-owned | N/A with reason: separate continuity commit |
| External evidence digest | N/A with reason: zero external evidence | none | N/A with reason |
| System loop interlock | successor flag NO | no automatic successor | PASS |
| Session continuity | post-material dispatch sync | steward-owned | PENDING |

## Claim Boundary

This baseline authorizes exactly one non-production in-process core module and
its focused test. It does not authorize filesystem/distributed persistence,
HTTP routes, package exports, AER construction, provider admission/invocation,
durable audit integration, public sync, deployment, or production readiness.
