# CVF Intake Role Routing Decision Checker Hardening Authorization

Memory class: REVIEW_AUTHORIZATION

Status: AUTHORIZED_GUARD_MAINTENANCE

## Purpose

Authorize a bounded governance/control-plane checker hardening batch for
intake-to-role-routing decisions.

The goal is to let non-coder operators provide natural-language or vibe-coding
intake while requiring the orchestrator to decide whether execution should use
single-agent/multi-role, multi-agent/multi-role, or another bounded route
before worker dispatch.

## Target / Source

Target:

- dispatch-quality checker enforcement for `## Intake Role Routing Decision`;
- work-order template marker;
- closure-quality standard marker;
- new canonical intake routing standard;
- focused checker tests.

Source:

- operator instruction on 2026-06-11 that non-coder operators should not need
  to manually decide or copy/paste between agents for role topology;
- existing CVF governed lifecycle, work-order dispatch quality, single-agent
  multi-role control, worker autonomy, and closure-quality standards.

## Findings / Position

Position: proceed with bounded checker hardening.

Findings:

- Reusable control-plane finding: raw intake can be natural and incomplete,
  but dispatch requires a role topology decision before implementation.
- Correct control response: require the orchestrator to record intake summary,
  scope, risk, route mode, role separation basis, and escalation condition
  before marking a work order ready or dispatched.

## Risk / Corrective Action

Risk: a broad checker could block harmless draft/HOLD work or overclaim that
the selected role route is optimal.

Corrective action:

- enforce only on ready or dispatched work orders;
- allow pending route modes only before dispatch;
- state that the control proves routing evidence discipline only;
- keep single-agent multi-role separately bounded by the existing control
  block and no-independent-review boundary.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add a bounded dispatch-quality machine
check that requires `## Intake Role Routing Decision` before dispatch.

Protected paths:

- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`

Operator authorization: 2026-06-11 operator instructed Codex to tighten CVF so
non-coder vibe-coding intake can be routed by the orchestrator without the
operator manually deciding between multi-agent/multi-role and
single-agent/multi-role execution.

Rollback boundary: revert only this authorization artifact, the intake routing
standard, checker/test changes, and matching template/standard marker updates
if the guard proves too broad. Do not revert LPCI2 EX/EC artifacts, DSCP
artifacts, single-agent multi-role control, negative-search checker hardening,
public-sync README commits, session state, handoff history, or unrelated
governance maintenance.

## Scope Boundary

Allowed:

- update the dispatch-quality checker;
- update focused dispatch-quality checker tests;
- add the exact rule marker to the work-order template;
- add the exact rule marker to the closure-quality standard;
- add the canonical standard;
- run focused tests and governance gates.

Forbidden:

- runtime/source behavior changes outside governance checker code;
- provider/API-key use;
- public-sync changes;
- EC-T2 dispatch or implementation;
- production, public-readiness, legal-quality, current-law, provider-quality,
  or independent-review claims.

## Finding-To-Governance Learning Disposition

| Field | Value |
| --- | --- |
| defect class | PHASE_GATE_PLACEMENT_GAP |
| learningLane | GOVERNANCE_CONTROL_PLANE |
| disposition | MACHINE_CHECK_ADDED |
| runtime/provider/cost lane | N/A_WITH_REASON - this is control-plane checker hardening only |
| next control action | Require orchestrator-owned intake role routing before ready/dispatch work orders. |

## Claim Boundary

This artifact authorizes and records a control-plane checker hardening batch
only. It does not prove independent review, semantic correctness, runtime
behavior, provider behavior, public readiness, production readiness, legal
advice quality, current-law freshness, or live governance behavior.
