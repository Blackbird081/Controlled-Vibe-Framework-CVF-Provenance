# CVF Single-Agent Multi-Role Control Checker Hardening Authorization

Memory class: REVIEW_AUTHORIZATION

Status: AUTHORIZED_GUARD_MAINTENANCE

## Purpose

Authorize a bounded governance/control-plane checker hardening batch for
single-agent multi-role execution.

The goal is to let small, bounded, control-plane tranches proceed without
constant operator copy/paste between agents while preventing a single agent
from presenting self-review as independent multi-agent review.

## Target / Source

Target:

- dispatch-quality checker enforcement for single-agent multi-role control;
- role-assignment matrix pointer;
- work-order template marker;
- closure-quality standard marker;
- focused checker tests.

Source:

- operator instruction on 2026-06-11 to tighten CVF because one agent may need
  to execute multiple roles when the operator lacks time for manual
  cross-agent transfer;
- existing CVF role-assignment matrix, work-order template, reviewer closure
  conversion, worker pending-return, and finding-to-governance controls.

## Findings / Position

Position: proceed with bounded checker hardening.

Findings:

- Reusable control-plane finding: single-agent multi-role execution is useful
  for small work, but without an explicit control block it can blur worker,
  reviewer, and committer duties.
- Correct control response: require role-separation evidence and self-review
  boundary before dispatch when same actor owns implementation plus
  review/closure roles.

## Risk / Corrective Action

Risk: a broad checker could block harmless role references or overclaim that
single-agent review is independent review.

Corrective action:

- trigger only on explicit single-agent multi-role language or role tables
  where the same actor owns implementation plus review/closure roles;
- require evidence basis, self-review boundary, escalation conditions, and
  gate sequence;
- state that independent review is not claimed.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add a bounded dispatch-quality machine
check that requires `## Single-Agent Multi-Role Control Block` before dispatch
when one agent owns implementation plus review/closure roles.

Protected paths:

- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`

Operator authorization: 2026-06-11 operator instructed Codex to tighten CVF so
single-agent multi-role execution can be used safely for small, bounded,
control-plane work when manual multi-agent transfer is not practical.

Rollback boundary: revert only this authorization artifact, the
single-agent/multi-role checker changes, focused tests, and matching
template/standard/role-matrix marker updates if the guard proves too broad. Do
not revert LPCI2 EX/EC artifacts, DSCP artifacts, negative-search checker
hardening, public-sync README commits, session state, handoff history, or
unrelated governance maintenance.

## Scope Boundary

Allowed:

- update the dispatch-quality checker;
- update focused dispatch-quality checker tests;
- add the exact rule marker to the work-order template;
- add the exact rule marker to the closure-quality standard;
- add a role-matrix pointer to the control standard;
- run focused tests and reviewer-fast gates.

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
| defectClass | MACHINE_GATE_GAP |
| learningLane | GOVERNANCE_CONTROL_PLANE |
| disposition | MACHINE_CHECK_ADDED |
| runtime/provider/cost lane | N/A_WITH_REASON - this is control-plane checker hardening only |
| next control action | Keep single-agent multi-role allowed only with evidence/gate separation and explicit no-independent-review boundary. |

## Claim Boundary

This artifact authorizes and records a control-plane checker hardening batch
only. It does not prove independent review, semantic correctness, runtime
behavior, provider behavior, public readiness, production readiness, legal
advice quality, current-law freshness, or live governance behavior.
