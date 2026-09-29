# CVF GC-018 Baseline - GC010 SCR-R2-T1J-R2 Approval Resume Atomic Claim Durable Owner Decision

Memory class: governed-dispatch-baseline

Status: READY_FOR_DISPATCH

Batch ID: GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION

Dispatch base head: `ab3d1075c00446dafbd7af4d6737e012a88d41e4`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer/closer: orchestrator/reviewer

## Purpose

Resolve the one bounded decision left by accepted T1J-R1: which durable owner
must provide atomic single-claim and recovery semantics for approval resume
while `/api/execute` retains its existing single guard and provider-admission
pipeline. This is decision-only and opens no implementation automatically.

## Accepted Input

T1J-R1 material `35226ccf785a1092e6d3009c98e5865e5174a4f9`
selected `PARTIAL_READY_REQUIRES_RESUME_INTERFACE_OR_DURABLE_OWNER_DECISION`.
It proved a mounted approval UI and missing resume caller, rejected a second
route, and established that the current approval status-read and later delete
are not an atomic exactly-once claim.

## Required Comparison

1. Extend the existing approval store and `/api/execute` with an atomic claim,
   recovery, and terminal-state contract.
2. Compose `buildPendingAgentExecutionRuntime` narrowly inside the existing
   `/api/execute` path while preserving the route's sole guard/provider owners.
3. Use a minimal consume-before-work operation without a durable execution
   lifecycle, including its loss and ambiguity behavior.
4. Retain formal T1 parked because no safe bounded owner can be selected.

For each candidate name exact creation, claim, begin, provider-attempt,
terminal, retry/recovery, audit, storage-path, cleanup and failure owners;
duplicate state; crash windows; concurrency guarantee; smallest future
manifest; and proof that no second guard/provider pipeline is introduced.

## Allowed Terminals

- `EXISTING_APPROVAL_STORE_ATOMIC_LIFECYCLE_OWNER_READY_FOR_T1K_DECISION`
- `PENDING_RUNTIME_NARROW_IN_ROUTE_LIFECYCLE_OWNER_READY_FOR_T1K_DECISION`
- `MINIMAL_ATOMIC_CONSUME_OWNER_READY_FOR_T1K_DECISION`
- `PARTIAL_READY_REQUIRES_FAILURE_RECOVERY_INTERFACE_DECISION`
- `NO_SAFE_DURABLE_OWNER_RETAIN_FORMAL_T1_PARKED`
- `BLOCKED_SOURCE_CONTRADICTION`

`successorTrancheOpened: NO`

## Required Worker Outputs

1. `docs/assessments/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_2026-08-31.md`
2. `docs/reviews/CVF_GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION_WORKER_RETURN_2026-08-31.md`

No other output is allowed.

## Decision / Baseline

The worker must select one durable owner from current source evidence or park.
An owner is not ready merely because it has atomic CAS: it must also define
what happens when execution fails before provider admission, becomes ambiguous
after provider invocation, or must be retried without replaying effects.

## Evidence / Verification

Dispatch evidence is the accepted T1J-R1 assessment, the named current source,
clean base HEAD `ab3d1075c00446dafbd7af4d6737e012a88d41e4`, negative path/token search,
ADIF NONE_RETURNED result and the pre-dispatch governance bundle.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Approval store exposes independent Map-style get/set/delete and file persistence, not CAS | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts` | `ApprovalStore`; `persist`; overrides | `get`; `set`; `delete` | approval store | ACCEPT |
| Execute route validates approval early and audits/deletes it later before provider admission | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | approval block; `APPROVAL_CONSUMED`; provider-attempt block | `approvedRequestRecord`; `getApprovalStore().delete`; `admitAndInvokeProvider` | `POST` | ACCEPT |
| Pending core owns CAS claim, begin, terminal and recovery transitions | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | store interface; claim/begin/terminal functions | `compareAndSwap`; `claimPendingExecution`; `beginPendingExecution`; `applyTerminalTransition` | pending core | ACCEPT |
| SQLite adapter supplies single-node IMMEDIATE-transaction CAS | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.ts` | `compareAndSwap` | conditional update and `runCas.immediate()` | SQLite store | ACCEPT |
| Composition owner exposes create/get/claim/begin/terminal/reconciliation and requires caller-supplied dbPath | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-composition.ts` | runtime interface and builder | `PendingAgentExecutionComposedRuntime`; `buildPendingAgentExecutionRuntime` | pending composition | ACCEPT |
| T1J-R1 leaves durable claim ownership unresolved | accepted review | `docs/assessments/CVF_GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION_2026-08-31.md` | Independent Reviewer Correction; Decision | selected partial-ready terminal | T1J-R1 | ACCEPT |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | orchestrator/reviewer and delegated decision worker | documentation-only comparison; no source or runtime mutation | this baseline and paired work order | N/A with reason: local governed decision artifacts only | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | operator-mediated worker return | worker output is non-authoritative until local review; zero provider/live authority | exact two-file return manifest | file-return boundary only; no CLI/MCP runtime adapter is created | `DEFERRED_WITH_REASON` |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`decision assessment`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | dispatch status, source dispositions, convergence fields, exact terminal tokens, dual-agent rows, trace labels and no-commit terms |
| gateRunPurpose | Confirm dispatch shape after source-led authoring. |
| claimBoundary | Structural compliance cannot select the durable owner. |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GC010_SCR_R2_T1J_R2_APPROVAL_RESUME_ATOMIC_CLAIM_DURABLE_OWNER_DECISION --title "GC010 SCR R2 T1J R2 Approval Resume Atomic Claim Durable Owner Decision" --date 2026-08-31 --base ab3d1075c00446dafbd7af4d6737e012a88d41e4 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added accepted T1J-R1 evidence, four-candidate comparison, terminal set, source rows and exact two-output manifest. |
| checkerReadAheadConfirmation | Applicable checker sources inspected before authoring. |
| docOnlyNewFields | Durable lifecycle owner comparison and crash-window decision criteria. |
| claimBoundary | Dispatch provenance only; no runtime behavior is changed. |

## Claim Boundary

This baseline authorizes one source-backed documentation decision. It does not
authorize code, tests, route wiring, store migration, provider/live calls,
package export, public sync, deployment, production, T1K or T2.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision dispatch; no public artifact is changed.
