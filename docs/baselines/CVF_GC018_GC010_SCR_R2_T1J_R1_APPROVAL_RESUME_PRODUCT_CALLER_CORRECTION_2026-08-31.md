# CVF GC-018 Baseline - GC010 SCR-R2-T1J-R1 Approval Resume Product Caller Correction

Memory class: governed-dispatch-baseline

Status: READY_FOR_DISPATCH

Batch ID: GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION

Dispatch base head: `072dffc3338fd2ed9a6fb98673953a5b807cd7b1`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer/closer: orchestrator/reviewer

## Purpose

Correct T1J's missed product-surface evidence. Determine whether the existing
approval UI plus approval-bound `/api/execute` path supplies a concrete caller
for a safe-resume composition, whether it instead proves that AER would remain
duplicative, or whether one exact interface/owner decision remains.

## New Independent Critical Evidence

- `ApprovalInbox` is mounted at user and admin approval pages and PATCHes
  `/api/approvals/[id]`.
- `/api/execute` creates bound approval records on `NEEDS_APPROVAL` and accepts
  an approved, actor-bound, request-hash-bound `approvalId` on a later request.
- `ProcessingScreen` submits and displays approvals but its execution request
  does not currently send the stored approval ID for resume.
- The pending-agent-execution core already models approval-bound durable claim,
  begin, terminal and stale-input rejection.

## Required Comparison

1. Existing `/api/execute` approval-ID resubmission with the smallest UI resume
   affordance and no AER/pending-runtime composition.
2. Isolated approval-resume route using `buildPendingAgentExecutionRuntime` and
   `PendingAgentExecutionSqliteStore`, invoked from the existing approval UI.
3. Approval-decision route-triggered execution, including why coupling admin
   decision and provider execution is safe or unsafe.
4. Retain parked.

For each, identify the exact product caller, request owner, approval binding,
guard owner, provider/admission owner, durable owner, response/failure owner,
duplicate-boundary risk, value beyond the current route and smallest future
manifest.

## Allowed Terminals

- `APPROVAL_RESUME_CALLER_READY_FOR_T1K_IMPLEMENTATION_DECISION`
- `PARTIAL_READY_REQUIRES_RESUME_INTERFACE_OR_DURABLE_OWNER_DECISION`
- `EXISTING_EXECUTE_RESUME_MAKES_AER_CONSUMER_DUPLICATIVE_RETAIN_PARKED`
- `NO_SOURCE_BACKED_CALLER_RETAIN_FORMAL_T1_PARKED`
- `BLOCKED_SOURCE_CONTRADICTION`

`successorTrancheOpened: NO`

## Required Worker Outputs

1. `docs/assessments/CVF_GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION_2026-08-31.md`
2. `docs/reviews/CVF_GC010_SCR_R2_T1J_R1_APPROVAL_RESUME_PRODUCT_CALLER_CORRECTION_WORKER_RETURN_2026-08-31.md`

No other output is allowed.

## Decision / Baseline

T1J is reopened only for the missed approval-surface evidence. The prior
terminal remains effective unless this bounded rework proves a different
allowed terminal. No implementation successor opens automatically.

## Evidence / Verification

Dispatch evidence is the named current source, exact clean base HEAD, ADIF
NONE_RETURNED result, pre-dispatch governance bundle and two-file manifest.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Approval inbox is a registered UI surface | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ApprovalInbox.tsx` | request loading and `handleAction` | `/api/approvals`; `/api/approvals/[id]` | `ApprovalInboxContent` | ACCEPT |
| User/admin pages mount the inbox | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/approvals/page.tsx` | page body | `ApprovalInbox` | approvals page | ACCEPT |
| Execute route accepts bound approval resume input | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | approval validation block | `approvalId` | `POST` | ACCEPT |
| Approval decision route persists decision only | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/[id]/route.ts` | `PATCH` | `updatedRecord`; `APPROVAL_DECIDED` | approval route | ACCEPT |
| Processing UI retains approval ID but does not send it in its execute body | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ProcessingScreen.tsx` | `executeReal`; `approvalRequestId` | `/api/execute` request | `ProcessingScreen` | ACCEPT |
| Pending core binds approval and durable lifecycle | runtime source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | approval validation and claim lifecycle | `ApprovalRecordLookup` | pending execution core | ACCEPT |
| T1J parked because it reported no product UI/caller | accepted assessment | `docs/assessments/CVF_GC010_SCR_R2_T1J_REGISTERED_PRODUCTION_INVOCATION_OWNER_AND_INVOKED_PATH_COMPOSITION_DECISION_2026-08-31.md` | questions 3 and 12 | prior terminal | T1J | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`decision assessment`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | dispatch status, Source Verification rows, rework control fields, terminal tokens, trace labels and no-commit evidence |
| gateRunPurpose | Confirmation after source-led authoring, not discovery of required shape. |
| claimBoundary | Structural readiness does not decide product value or topology. |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GC010_SCR_R2_T1J_R1_APPROVAL_SURFACE_PRODUCT_CALLER_CORRECTION --title "GC010 SCR R2 T1J R1 Approval Surface Product Caller Correction" --date 2026-08-31 --base 072dffc3338fd2ed9a6fb98673953a5b807cd7b1 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 1 --root-cause-cluster-id T1J_MISSED_APPROVAL_PRODUCT_SURFACE --prior-finding-set-digest 88173edc1fa61883cd1961cce2fdac6a69293944061398af0cf16ba09e89589b --cumulative-external-invocation-count 1 --external-invocation-ceiling 2 --new-independent-critical-evidence "ApprovalInbox and approval-bound execute path" --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit rework profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added corrected source evidence, four-way comparison, terminal set and two-output manifest. |
| checkerReadAheadConfirmation | Applicable dispatch and worker-return checker sources inspected. |
| docOnlyNewFields | New Independent Critical Evidence; Required Comparison; Allowed Terminals. |
| claimBoundary | Provenance only; no runtime behavior is changed. |

## Claim Boundary

Decision-only correction. No source/test/roadmap/session edit, implementation,
route/package/provider/audit wiring, provider/live call, public sync, deployment
or production claim is authorized.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance rework decision packet.
