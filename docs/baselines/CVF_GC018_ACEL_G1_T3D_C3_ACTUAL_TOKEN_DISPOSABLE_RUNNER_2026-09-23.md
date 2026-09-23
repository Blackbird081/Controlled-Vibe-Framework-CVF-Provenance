# CVF GC-018 Baseline - ACEL G1 T3D-C3 Actual-Token Disposable Runner

Memory class: governed-dispatch-baseline

docType: baseline

Status: APPROVED_FOR_EXECUTION

Batch ID: ACEL-G1-T3D-C3-ACTUAL-TOKEN-DISPOSABLE-RUNNER

Dispatch base head: `3ad4903dec375121b0af1a3c6774078ca199b8cf`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Local orchestrator/reviewer

Reviewer owner: Local reviewer distinct from the implementation phase; same-thread role switch is disclosed and is not independent actor review

Worker target: shared-workspace INTERNAL_AGENT Local implementation role

## Purpose

Authorize one bounded implementation tranche for the missing Group 4
disposable actual-token runner. The tranche may build and test the runner only
under the current Local token. It must not launch Party B/C, request a password,
create the real Group 4 source, open T3E or claim actual-token success.

## Source / Predecessor Evidence

| Source | Accepted evidence |
|---|---|
| `docs/audits/CVF_ACEL_G1_T3D_C1_R2_POST_CLOSURE_ACTUAL_TOKEN_EXECUTION_READINESS_AUDIT_2026-09-23.md` | material commit `a765880e4`; exact runner gap and seven-gate operator checkpoint |
| `docs/audits/CVF_ACEL_G1_T3D_C0_R1_GROUP4_OPERATIONAL_BOUNDARY_AMENDMENT_2026-09-23.md` | controlling actual-token matrix and fail-closed fallback |
| `docs/audits/CVF_ACEL_G1_T3D_GROUP4_DISPOSABLE_ROOT_PROOF_PACKET_2026-09-23.md` | containment, ledger, identity and stop-condition boundary |
| `docs/reviews/CVF_ACEL_G1_T3D_C1_R2_RESERVATION_COMPATIBLE_TOOLING_LOCAL_REVIEW_2026-09-23.md` | accepted hermetic transaction primitives; actual principal proof excluded |

## Decision / Baseline

Select one three-script runner architecture:

1. Local coordinator creates and verifies the disposable root, exact parent and
   reservations, authorization records, evidence manifest and command packet.
2. Principal probe accepts one frozen role/action envelope, verifies its exact
   token and containment, invokes only the bounded transaction/negative probe,
   and appends no trusted final verdict.
3. Local finalizer verifies complete pre/post evidence and emits only
   `PASS_ACTUAL_TOKEN_PROOF` or `INCONCLUSIVE_OR_FAILED`.

The implementation may reuse accepted writer functions but may not silently
change their canonical real-source entrypoints. Any needed writer change is a
new authority decision.

## Evidence / Verification

Required evidence is current-token hermetic proof of containment, schema and
command generation; exact identity mismatch rejection; real-source rejection;
complete matrix planning; semantic security tuple capture; fail-closed missing
or altered evidence; deterministic peer protocol; and no credential storage.

The worker return remains `PENDING_REVIEWER_EXECUTION`. Static and hermetic
success are not Windows actual-token proof.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T3D-C3-ACTUAL-TOKEN-DISPOSABLE-RUNNER --title "ACEL G1 T3D-C3 Actual-Token Disposable Runner" --date 2026-09-23 --base 3ad4903dec375121b0af1a3c6774078ca199b8cf --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --no-evidence-readiness-applicable --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with the accepted Group 4 contract, exact manifests and single-agent role boundary |
| checkerReadAheadConfirmation | work-order template, high-risk transaction standard and applicable checker sources read before authoring |
| docOnlyNewFields | none |
| claimBoundary | dispatch baseline only; no principal execution or source authority |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`PURE_LOCAL_IMPLEMENTATION`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "PURE_LOCAL_IMPLEMENTATION" --role dispatcher --lifecycle-phase pre-dispatch`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | baseline/review structural headings, source-verification dispositions, high-risk applicability and nine-key JSON shape, trace labels, private export token |
| gateRunPurpose | confirm the completed dispatch packet rather than discover its contract |
| claimBoundary | static dispatch admission only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: machine-specific Windows principal and ACL tooling remains private; no
public-sync action is authorized.

## Claim Boundary

This baseline authorizes source/test authoring under the current token only. It
does not authorize Party B/C execution, passwords, account changes, real source
creation, T3E, provider/live calls, public sync, deployment or production use.
