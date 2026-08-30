# CVF GC-018 GC010 SCR-R2-T0B Pending Agent Execution Safe Resume Contract Decision

Memory class: governed-baseline

docType: baseline

Status: DISPATCHED_DECISION_ONLY

Batch ID: GC010-SCR-R2-T0B

Date: 2026-08-30

dispatchBaseHead: `276fc4344`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize one documentation-only decision that freezes the smallest safe
contract for a durable pending Agent Execution record, fail-closed persistence,
atomic claim, and internal resume authority. This tranche continues the same
GC010 system chain closed direction from T0A and does not implement it.

## Authority Chain

- Operator authorized full orchestrator/reviewer handling and instructed
  continuation of the system-chain roadmap without lane drift.
- T0A completion:
  `docs/reviews/CVF_GC010_SCR_R2_T0A_AGENT_EXECUTION_API_CROSS_OWNER_CONTRACT_DECISION_COMPLETION_2026-08-30.md`.
- T0A assessment:
  `docs/assessments/CVF_GC010_SCR_R2_T0A_AGENT_EXECUTION_API_CROSS_OWNER_CONTRACT_DECISION_2026-08-30.md`.
- Active handoff: `AGENT_HANDOFF_V59_2026-08-11.md`.
- Paired work order:
  `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R2_T0B_PENDING_AGENT_EXECUTION_SAFE_RESUME_CONTRACT_DECISION_2026-08-30.md`.

## Scope / Target / Owner Boundary

Target exactly one versioned contract decision covering:

- the pending-agent-execution record and canonical digest;
- explicit persistence failure semantics;
- lifecycle states and legal transitions;
- one atomic claim/consume primitive with concurrency semantics;
- approval decision versus execution authority separation;
- an unforgeable internal resume grant and validation sequence;
- stale policy/guard/binding behavior;
- the exact future file/test manifest, without creating it.

Worker writes only the companion assessment and worker return. Runtime,
package, route, store, test, checker, workflow, continuity, provider/live,
public-sync, deployment, and production mutations are forbidden.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Current Web approval record lacks a complete pending AER execution and atomic claim | runtime/schema | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts` | `ApprovalRequestRecord`; `persist()` | approval store | cvf-web approval owner | ACCEPT |
| Current approval persistence catches write failures | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts` | `FileBackedApprovalStore.persist` | persistence behavior | cvf-web approval owner | ACCEPT |
| Existing actor/hash binding is reusable but not a complete AER authority digest | runtime/schema | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.ts` | `buildApprovalActorBinding`; `computeApprovalRequestHash` | approval binding | cvf-web | ACCEPT |
| AER public execution accepts a caller-provided guard result | runtime | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | `execute(intent, guardResult)` | `execute` | Guard Contract | ACCEPT |
| Existing approval PATCH is decision mutation, not execution authority | runtime | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/[id]/route.ts` | `PATCH` | approval decision handler | cvf-web | ACCEPT |

## Mandatory Invariants

1. Approval PATCH remains decision-only and starts zero provider calls.
2. Approval status alone is never sufficient execution authority.
3. No external caller may supply or synthesize `ALLOW` for resume.
4. A pending record is immutable except through named atomic transitions.
5. Persistence or claim uncertainty fails closed before provider admission.
6. At most one resume claimant may receive an executable internal grant.
7. Actor, request digest, full AER binding, approval expiry/status, and
   guard/policy fingerprint are revalidated before claim succeeds.
8. Drift produces a stale terminal/non-executable disposition, never implicit
   approval.
9. The contract must compose with exactly one future
   `admitAndInvokeProvider` admission per actual provider call.
10. T0B creates no runtime readiness or successor authority.

## Required Contract Decisions

The worker must answer all of these with exact fields/enums/operations:

1. What is the schema name and `schemaVersion`?
2. Which normalized intent, actor, session, cwd, environment, file-scope,
   build-authority, guard decision, fingerprint, approval, attempt and audit
   fields are mandatory?
3. What exact bytes/normalization form the canonical record digest?
4. Which fields are immutable and which transition metadata may change?
5. What are all lifecycle states and legal transitions?
6. What persisted evidence proves create success before returning pending?
7. How do write, fsync/replace, parse, corruption and restart failures fail
   closed?
8. What is the atomic claim operation, precondition and success receipt?
9. How do concurrent resume requests yield at most one winner?
10. How are abandoned/expired claims reconciled without duplicate execution?
11. What validates approval actor, status, expiry and request hash?
12. What validates complete AER binding and guard/policy fingerprint?
13. What exact stale disposition applies on drift?
14. What makes the internal resume grant non-caller-constructible?
15. Which component may consume that grant and how is single use enforced?
16. How are approvalId, pendingExecutionId, claimId, requestId, attempt index,
    audit event and response correlated?
17. Which negative cases must future focused tests prove?
18. Is the contract ready for a later T1 packet, requires another decision, or
    must remain parked?

## Terminal Tokens

Select exactly one:

- `SAFE_RESUME_CONTRACT_READY_FOR_T1_CONSIDERATION`
- `PARTIAL_CONTRACT_REQUIRES_FURTHER_DECISION`
- `NO_SAFE_RESUME_CONTRACT_RETAIN_PARKED`
- `BLOCKED_SOURCE_CONTRADICTION`

The first token permits reviewer consideration of a later T1 packet only. It
does not open T1 automatically.

## Acceptance Criteria

- Three designs are compared: extend approval record; dedicated pending store
  plus separate grant; retain parked.
- All 18 questions are answered with one coherent contract.
- Schema, state machine, CAS/claim semantics, failure behavior, grant boundary,
  identity/fingerprint checks and negative tests are exact.
- Exactly one terminal token is selected and alternatives are defeated.
- Zero runtime edits, provider calls, external calls, staging or worker commit.

## Decision / Baseline / Proposed Tranche

Baseline position: T0A is accepted only as architecture direction. T0B must
either freeze an exact safe-resume contract or retain the chain parked. The
proposed tranche is documentation-only, opens no T1, and has no runtime effect.

## Evidence / Verification

Required evidence is the fresh source inventory, three-design comparison,
18/18 answers, one terminal token, exact command receipts, clean two-output
manifest, zero-call declaration, and worker-return fast-gate result.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GC010-SCR-R2-T0B --title "Pending Agent Execution Safe Resume Contract Decision" --date 2026-08-30 --base 276fc4344 --commit-mode WORKER_MUST_NOT_COMMIT --dependency "accepted T0A architecture direction; no implementation" --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 2 --stdout` |
| generatedProfile | generic worker dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | filled exact schema, state, claim, grant, output and terminal decision controls |
| checkerReadAheadConfirmation | dispatch, structural, worker-return, trace, delta and public-disposition checkers read |
| docOnlyNewFields | pending record; state machine; atomic claim; safe resume grant |
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
| Dispatch impact | normal decision-only controls remain binding |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch envelope fields; source table columns; worker-return headings; operation trace fields; claim-boundary fields; public disposition |
| gateRunPurpose | confirmation evidence after direct checker inspection, not first discovery |
| claimBoundary | artifact shape only; semantic acceptance remains reviewer-owned |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private decision-only system-chain authority; no public artifact or
release claim is authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | paired work order | `Status: DISPATCHED_DECISION_ONLY` | PENDING_WORKER_RETURN |
| Completion or reviewer artifact | worker return addendum or completion | reviewer-owned | PENDING_REVIEW |
| Roadmap state | prior roadmap and T0A closure | no historical rewrite | PASS |
| Registry JSON | active session state | session-sync steward only | N/A with reason: dispatch precedes continuity sync |
| Registry Markdown | front door/handoff | steward-owned | N/A with reason: separate continuity commit |
| External evidence digest | N/A with reason: zero external calls | none | N/A with reason |
| System loop interlock | successor flag NO | packet literals | PASS |
| Session continuity | separate post-material commit | steward-owned | PENDING |

## Claim Boundary

This baseline authorizes a contract decision only. It does not implement a
store, route, claim primitive, resume grant, AER export, provider adapter or
test, and it makes no live, public, deployment or production claim.
