# CVF LPCI1-T1 Dependency Release Commit Evidence Guard Hardening

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: review

Date: 2026-06-03

## Purpose

Authorize a bounded dispatch-quality hardening discovered during LPCI1-T1
dependency release review: the pre-dispatch gates passed even when a ready work
order cited a prerequisite artifact at a commit that did not contain that
artifact.

## Scope

Allowed changed paths:

- `docs/work_orders/CVF_WO_LPCI1_T1_PRODUCT_INTAKE_AND_ARCHITECTURE_2026-06-02.md`
- `docs/reviews/CVF_LPCI1_T1_DEPENDENCY_RELEASE_COMMIT_EVIDENCE_GUARD_HARDENING_2026-06-03.md`
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`

Forbidden scope: runtime implementation, LPCI product code, provider/live proof,
public-sync, broad dependency-resolution redesign, archive cleanup, and
unrelated guard refactors.

## Target / Source

Target: dependency-release evidence discipline for ready/dispatch work orders.

Source evidence:

- `docs/reference/CVF_WORK_ORDER_DEPENDENCY_RELEASE_EVIDENCE_STANDARD_2026-06-03.md`;
- `docs/work_orders/CVF_WO_LPCI1_T1_PRODUCT_INTAKE_AND_ARCHITECTURE_2026-06-02.md`;
- CI2-T5 closure commit `6324fd76`;
- active dispatch-quality checker `governance/compat/check_work_order_dispatch_quality.py`.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: update `check_work_order_dispatch_quality.py`
so a ready/dispatch work order line that cites an artifact path "at commit
`hash`" must use a commit tree that actually contains that artifact path.

Protected paths:

- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`

Operator authorization: the operator has repeatedly required that findings
caused by rules/templates/guards be fixed as reusable CVF controls rather than
one-off packet repairs.

Rollback boundary: revert this guard-hardening commit to restore the prior
dependency-release behavior. LPCI1-T1 can remain held or be re-released with
manual review if the machine rule is rolled back.

## Evidence Trace Block

| Evidence | Value |
| --- | --- |
| Finding | LPCI1-T1 release evidence cited CI2-T5 closure review at `1ab83302`, but the closure artifact was introduced at `6324fd76` |
| Packet repair | LPCI1-T1 release evidence updated to cite `6324fd76`; `dispatchBaseHead` refreshed to `0dbce418` |
| Guard repair | dispatch-quality checker validates artifact-path-at-commit evidence |
| Focused regression | `test_ready_work_order_dependency_artifact_commit_must_contain_path` |
| Boundary | no runtime, provider, public-sync, product implementation, or broad guard rewrite |

## Findings / Position

Position: APPROVE bounded guard hardening and packet repair.

Findings:

- The previous dependency-release rule rejected placeholder prose but did not
  verify that a cited commit actually contained the cited prerequisite artifact.
- This is a reusable control-plane issue, not a worker-quality-only issue.
- The fix keeps the semantic boundary narrow: it verifies artifact existence at
  the cited commit, not semantic quality of the prerequisite artifact.

## Risk / Corrective Action

Risk: low. The new check applies only to explicit "artifact at commit" evidence
inside ready/dispatch artifacts. It does not require all commit hashes in prose
to be interpreted as dependency evidence.

Corrective action: if a legitimate ready work order needs to cite a commit that
does not contain the artifact, rewrite the evidence to name the actual closure
commit or explain the exception in a HOLD/BLOCKED note before dispatch.

## Final Boundary

This authorization is final for LPCI1-T1 dependency-release commit-evidence
hardening only. It does not authorize LPCI runtime implementation, legal answer
claims, public export, provider calls, or any worker commit permission change.

## Verification Boundary

Verification is local and structural: focused unit tests and governance gates.
No runtime/provider/cost proof is required or claimed.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next action |
| --- | --- | --- | --- | --- |
| Ready work order can cite an artifact at a commit that does not contain it | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | Dispatch-quality checker now validates artifact-path-at-commit evidence |
| LPCI1-T1 release evidence used stale CI2-T5 commit hash | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_ADDED | Packet evidence repaired and reusable guard added |
| Runtime/provider/cost terms appear only in forbidden-scope and verification-boundary text | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | N/A_WITH_REASON | No runtime/provider/cost behavior is evaluated in this guard-maintenance batch |

## Claim Boundary

This packet claims only bounded dependency-release evidence hardening. It does
not claim LPCI1-T1 implementation quality, product readiness, runtime behavior,
legal correctness, public readiness, or production readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance guard-maintenance record; no public-facing product
artifact is exported.
