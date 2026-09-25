# ADIF-0059 - Terminal Status Contradicts Closeability Recheck

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0059
title: Terminal status contradicts closeability recheck
defectCategory: PROCESS_AND_GATE_ORDER
defectClass: MACHINE_GATE_GAP
defectRole: ROOT_CAUSE
severity: HIGH
lifecycleState: ACTIVE
taskClasses: Worker execution (WORKER_MUST_NOT_COMMIT); Reviewer-return review
roles: worker; reviewer; closer
lifecyclePhases: pre-closure
surfaceSelectors: changed self-declared worker returns and completion reviews under docs/reviews/
detectionSignals: Status COMPLETE_PENDING_REVIEW coexists with UNCLOSEABLE_PACKET_CONTRADICTION or a named outside-authority blocker; UNCLOSEABLE_PACKET_CONTRADICTION lacks Status BLOCKED_WITH_REASON
enforcementLevel: MACHINE_CHECKED
checkerBindings: governance/compat/check_gate_to_role_closeability.py
promotionState: MACHINE_CHECK_ADDED
supersedes: NONE
lastVerifiedCommit: 8788efa79
roadmapSeedId: NONE
```

## Purpose

Prevent a return from presenting a completion-ready top-level status while its
machine-readable closeability recheck says that the packet cannot lawfully
close. This keeps unattended CLI/MCP or worker flows fail-closed at the first
returned-evidence boundary.

## Scope / Applies To

Applies prospectively to changed self-declared worker returns and completion
reviews evaluated by the gate-to-role closeability checker. It does not decide
whether an implementation finding is technically correct, expand a path
manifest, authorize redispatch, or intercept execution outside configured CVF
gates.

## Bad Example

A worker return declares `Status: COMPLETE_PENDING_REVIEW` while its
`Return-Time Closeability Recheck` declares
`UNCLOSEABLE_PACKET_CONTRADICTION`, names an outside-authority blocker, and
routes repair to the operator. The old checker validates each closeability
field locally and lets the contradictory document pass.

## Good Example

A return with a named packet contradiction declares
`Status: BLOCKED_WITH_REASON`, forbids worker redispatch, and selects one
controlled repair route. A completion-pending return declares `CLOSEABLE` and
`outsideAuthorityBlockers: NONE`.

## Canonical Sources

- `docs/reference/CVF_GATE_TO_ROLE_CLOSEABILITY_MACHINE_STANDARD.md`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/review_cost_control/CVF_REVIEW_COST_AND_DIMINISHING_RETURN_CONTROL_STANDARD.md`
- `docs/reference/guard_orientation/README.md`

## Remediation

Cross-check top-level `Status` against the return-time disposition and blocker
fields. Reject `COMPLETE_PENDING_REVIEW` unless the packet is `CLOSEABLE` with
no outside-authority blocker. Reject an uncloseable packet unless its top-level
status is `BLOCKED_WITH_REASON`. Preserve the existing controlled repair-route
and no-redispatch checks.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| Independent status and closeability validation allowed a semantically impossible worker return to pass | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_ADDED` | cross-check status, disposition and blockers in the existing closeability checker | Handled by the focused regression and checker amendment |

Runtime/provider/cost learning lane: `N/A_WITH_REASON` - the defect and guard
are entirely local repository governance behavior; no provider call,
credential, quota, runtime activation, or cost evidence is involved.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add the exact status-to-closeability
cross-field invariant exposed by the AKOE-P2 return; preserve every other
closeability rule and catalog binding.

Protected paths:

- `governance/compat/check_gate_to_role_closeability.py`
- `governance/compat/test_check_gate_to_role_closeability.py`

Operator authorization: explicit operator confirmation on 2026-09-25 authorizing AKOE-P2-R1
runtime correction and machine-gate hardening after the contradictory P2
worker return was reported.

Rollback boundary: revert only the ADIF-0059 status/recheck cross-field rule,
its focused tests, and this bounded standard clarification; preserve the
existing ADIF-0057 closeability graph and all unrelated governance behavior.

## Machine Enforcement

`governance/compat/check_gate_to_role_closeability.py` emits
`uncloseable_status_mismatch` when an uncloseable packet is not top-level
blocked and `complete_status_not_closeable` when a completion-pending return
has either an uncloseable disposition or a named blocker. Focused positive and
negative tests bind both directions.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer and governance guard maintainer |
| Provider or surface | private CVF workspace |
| Session or invocation | AKOE-P2 return adjudication and P2-R1 preparation, 2026-09-25 |
| Working directory | repository root |
| Command or tool surface | governed source reads, `apply_patch`, focused pytest, worker-return and repository gates |
| Target paths | this entry; closeability standard; closeability checker and focused test; corrected AKOE-P2 worker return |
| Allowed scope source | operator authorization to tighten the machine gate and open AKOE-P2-R1 |
| Before status evidence | AKOE-P2 return combined `COMPLETE_PENDING_REVIEW` with `UNCLOSEABLE_PACKET_CONTRADICTION` and passed the existing fast/reviewer gates |
| After status evidence | the contradictory pair fails the existing configured closeability gate; the truthful blocked pair passes |
| Diff evidence | focused checker regression plus exact changed-set and governed-gate evidence before material commit |
| Approval boundary | bounded local governance guard correction and P2 evidence adjudication only |
| Claim boundary | configured repository artifact validation only; no universal tool interception or runtime repair claim |
| Agent type | orchestrator/reviewer |
| Invocation ID | `adif-0059-akoe-p2-status-closeability-20260925` |
| Expected manifest | this entry; closeability standard; checker; focused test; corrected P2 worker return and preserved worker evidence tests |
| Actual changed set | verified before material commit |
| Manifest delta | pending final verification |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance learning. No public-sync action or public
catalog claim is authorized.

## Epistemic Process Block

### Expected Result / Prediction

Cross-field validation should reject the exact contradictory P2 return while
accepting a truthful blocked return with a named blocker and controlled route.

### Evidence Comparison

Focused fixtures exercise both the formerly accepted contradiction and the
corrected blocked form against the same checker entry point.

### Contradiction Or Gap Disposition

The earlier checker correctly validated individual recheck fields but did not
compare them with top-level status. The new rule closes only that missing join.

### Claim Update

Status/recheck consistency is now machine-checked at configured repository
gate entry points; out-of-band messages remain outside the claim.

## Claim Boundary

This entry records and guards one cross-field worker-return contradiction. It
does not validate implementation correctness, authorize scope expansion or
redispatch, repair the durable run store, or authorize provider/live/public/
deployment/production action.
