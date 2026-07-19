# CVF Agent Work Order - CVF Web UX T1P Audit Refinement

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: CVF-WEB-UX-T1P

Dispatch base head: `32ec223ad`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: generic worker

Reviewer/closer: independent reviewer/closer

Worker return path: `docs/reviews/CVF_WEB_UX_T1P_WORKER_RETURN_2026-07-19.md`

## Dispatch Prompt Envelope

Role: refine and source-verify the T1P hosted packaging and freshness audit.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_UX_T1P_AUDIT_REFINEMENT_2026-07-19.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: require the operator-provided committed packet-repair/session-sync HEAD before any edit.

Current-time notes: packet source base is `0a46eafa0`; worker execution begins only from the later committed packet-repair/session-sync HEAD supplied by the dispatcher.

Do-not-misread notes: Do not create a new audit from scratch. Modify the existing `docs/reviews/CVF_WEB_UX_T1P_HOSTED_PACKAGING_AND_FRESHNESS_AUDIT_2026-07-19.md`.

Required first actions: read the existing audit document, the previous T1 work order, and the CVF governance rules.

Return contract: leave all changes uncommitted and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

To officially refine and source-verify the existing T1P Hosted Packaging and Freshness Audit without starting from scratch. 
The refinement must correctly classify each hypothesis as `CONFIRMED`, `REJECTED`, or `INSUFFICIENT_EVIDENCE`.
It must explicitly NOT propose deployment as an action belonging to T1P.

## Authority Chain

Operator instruction -> T1 UX Roadmap -> T1 completion -> T1P Audit Refinement.

## Agent Roles

- Worker: refines the audit document and produces the worker return.
- Reviewer: recomputes source, verifies structure, and owns closure.

## Required First Reads

1. `docs/reviews/CVF_WEB_UX_T1P_HOSTED_PACKAGING_AND_FRESHNESS_AUDIT_2026-07-19.md`.

## Pre-Flight Checks

- confirm the worktree is clean, capture `executionBaseHead`, and require it to
  equal the operator-provided final session-sync HEAD before any edit.
- confirm target files are present.

## Write Ownership

Worker owns the refinement of the audit file and the generation of the worker return.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-UX-T1P --title "CVF Web UX T1P Hosted Packaging And Freshness Audit Refinement" --date 2026-07-19 --base 0a46eafa0 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Adapted for audit refinement |
| checkerReadAheadConfirmation | `governance/compat/check_markdown_structural_completeness.py` |
| docOnlyNewFields | None |
| claimBoundary | Dispatch authoring provenance only. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope checker failures directly. Worker should return to orchestrator only for a source contradiction, forbidden-scope need, or missing authority that makes completion impossible.

## Implementation Requirements

1. Modify `docs/reviews/CVF_WEB_UX_T1P_HOSTED_PACKAGING_AND_FRESHNESS_AUDIT_2026-07-19.md` in place. Do not start from scratch.
2. In the Hypothesis-Verdict Matrix, classify each hypothesis strictly as `CONFIRMED`, `REJECTED`, or `INSUFFICIENT_EVIDENCE`.
3. In the Backlog and Tranche Map, or Risk / Corrective Action, explicitly ensure that **deployment is NOT proposed as an action belonging to T1P**. T1P is strictly a read-only audit.
4. Produce `docs/reviews/CVF_WEB_UX_T1P_WORKER_RETURN_2026-07-19.md` detailing the changes.

## Execution Plan

1. Open the existing T1P audit document.
2. Update the Verdict column for all hypotheses to match the constrained vocabulary.
3. Review and adjust any language suggesting deployment is part of T1P.
4. Draft the worker return documenting these compliance adjustments.

## Allowed Scope

- `docs/reviews/CVF_WEB_UX_T1P_HOSTED_PACKAGING_AND_FRESHNESS_AUDIT_2026-07-19.md`
- `docs/reviews/CVF_WEB_UX_T1P_WORKER_RETURN_2026-07-19.md`

## Forbidden Scope

All other files. Specifically, no code changes and no deployment/mutation actions are allowed.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`audit-refinement`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "audit-refinement" --role dispatcher --lifecycle-phase pre-dispatch` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | standard constraints apply |

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake source | Operator instruction |
| Scope classification | Audit refinement |
| Intake role | Worker |
| Reviewer role | Independent reviewer |
| Routing decision | `WORKER_MUST_NOT_COMMIT` |
| Public route | `DEFERRED_PRIVATE_ONLY` |
| canonical route mode | `SINGLE_AGENT_SINGLE_ROLE` |
| selected role route | Worker to reviewer |
| escalation condition | BLOCKED_WITH_REASON |
| risk sensitivity | LOW (read-only audit refinement) |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | standard dispatch headings |
| gateRunPurpose | state confirmation |
| claimBoundary | bound to structure |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Next.js config | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/next.config.ts` | Entire file | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/next.config.ts` | N/A | ACCEPT |
| Netlify config | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/netlify.toml` | Entire file | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/netlify.toml` | N/A | ACCEPT |
| Package json | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | Entire file | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | N/A | ACCEPT |
| Read model | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts` | Entire file | `cvf-workspace-read-model.ts` | N/A | ACCEPT |
| Evidence T0 | EXISTS | `docs/reviews/evidence/CVF_WEB_UX_T0_R3_LOCALHOST_2026-07-19` | Directory | `docs/reviews/evidence/CVF_WEB_UX_T0_R3_LOCALHOST_2026-07-19` | N/A | ACCEPT |
| Evidence T1 | EXISTS | `docs/reviews/evidence/CVF_WEB_UX_T1_R1_LOCALHOST_2026-07-19` | Directory | `docs/reviews/evidence/CVF_WEB_UX_T1_R1_LOCALHOST_2026-07-19` | N/A | ACCEPT |

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | Source paths checked above |
| Runtime behavior claimed | None |
| Provider/live proof claimed | N/A_WITH_REASON |
| Public-sync claimed | N/A_WITH_REASON |
| Freshness disposition | PASS |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | review-packet |
| Storage decision | N/A |
| Existing aggregate impact | none |
| Generated state impact | none |
| Durable governance boundary | N/A with reason: no governance foundation or index is created |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | generic worker to independent reviewer |
| phase | refinement |
| baseHeadFor(phase) | dispatchBaseHead=32ec223ad; executionBaseHead=OPERATOR_PROVIDED_FINAL_SESSION_SYNC_HEAD; closureBaseHead=REVIEWER_TO_SET |
| changedSetScope(phase) | exactly the two Allowed Scope paths |
| traceScope(phase, actor) | worker trace |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT |
| crossBatchIsolation | all deployment and public lanes parked |
| nextMoveSurfaces | reviewer approval required |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_WEB_UX_T1P_COMPLETION_2026-07-19.md` |
| reviewerOwnedClosurePaths | The allowed scope paths |
| closureOwner | independent reviewer |
| workerCommitPermission | FORBIDDEN |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| Audit file | Refine classification and deployment constraints |
| Worker return | Document exactly what was changed |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_WEB_UX_T1P_WORKER_RETURN_2026-07-19.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
$executionBaseHead = git rev-parse --short HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $executionBaseHead --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

## Web/UI Claim Boundary

| Field | Value |
|---|---|
| DESIGN.md read | REQUIRED |
| UI claim boundary | no production-readiness, hosted, or live-data claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local workspace |
| Session or invocation | CVF-WEB-UX-T1P Work Order Authoring |
| Working directory | repository root |
| Command or tool surface | file generation |
| Target paths | `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_WEB_UX_T1P_AUDIT_REFINEMENT_2026-07-19.md` |
| Allowed scope source | user instruction |
| Before status evidence | clean worktree at HEAD 0a46eafa0 |
| After status evidence | Work order created |
| Diff evidence | `git diff --name-status` |
| Approval boundary | T1P |
| Claim boundary | dispatch only |
| Agent type | dispatcher |
| Invocation ID | `cvf-web-ux-t1p-dispatch-2026-07-19` |
| Expected manifest | the work order |
| Actual changed set | the work order |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | documentation refinement |
| claimDisposition | CLAIM_REJECTED |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | ACTION_EVIDENCE_PRESENT |
| invocationBoundary | no provider calls |
| interceptionBoundary | no wrapper |
| claimLanguage | documentation |
| forbiddenExpansion | no expansion into deployment or other systems |

## Acceptance Criteria

- [ ] Existing audit is edited in-place
- [ ] Hypotheses correctly classified (CONFIRMED/REJECTED/INSUFFICIENT_EVIDENCE)
- [ ] No deployment proposed as part of T1P
- [ ] Only two files output (audit and worker return)

## Evidence Requirements

- Exact verification of the updated Verdict column strings
- Git status showing only the two Allowed Scope files modified
- Absence of deployment terminology in the Tranche Map for T1P

## Review Gate

Reviewer must verify the edited audit file matches the expected vocabulary and constraints, and check that no source code files or deployment configuration have been modified.

## Closure Checklist

- [ ] Audit correctly verified
- [ ] Rules strictly adhered to

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` when done.

## Operator Checkpoint

T1P dispatch is authorized for audit refinement only. Production deployment remains parked until explicit unparking.

## Claim Boundary

Authorizes the refinement of the T1P audit document. Hosted mutation, deploy, public-sync, and provider/live remain parked. No code changes allowed.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: Internal review stage.
