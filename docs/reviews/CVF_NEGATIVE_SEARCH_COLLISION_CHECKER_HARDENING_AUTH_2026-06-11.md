# CVF Negative Search Collision Checker Hardening Authorization

Memory class: REVIEW_AUTHORIZATION

Status: AUTHORIZED_GUARD_MAINTENANCE

## Purpose

Authorize a bounded governance/control-plane checker hardening batch for
negative-search and same-token collision discipline.

This responds to the EC-T1 review finding where a worker-visible claim treated
`documentStatus` as absent even though the same token already existed in a
different DSCP test-fixture context.

## Target / Source

Target:

- dispatch-quality checker enforcement for negative-search claims;
- work-order template marker;
- closure-quality standard marker;
- focused checker tests.

Source:

- operator instruction on 2026-06-11 to continue tightening checker
  enforcement without overclaiming CVF foundation guarantees;
- EC-T1 review finding that `documentStatus` had a same-token occurrence in a
  different DSCP test-fixture context.

## Findings / Position

Position: proceed with bounded checker hardening.

Findings:

- Reusable control-plane finding: bare absence claims can hide same-token
  collisions when a worker or orchestrator searches too narrowly.
- Correct control response: enforce evidence structure and collision
  disposition, not semantic correctness.

## Risk / Corrective Action

Risk: a broad checker could overclaim or overblock legitimate absence claims.

Corrective action:

- require evidence/collision structure only when an artifact uses the
  absence-claim tokens;
- keep semantic correctness outside the checker claim boundary;
- cover the failure and pass paths with focused tests.

## Negative Search And Collision Discipline

- Search roots: `EXTENSIONS/`, `docs/`, `governance/`, and current changed
  artifact text.
- Search command: `rg "documentStatus|NOT FOUND|BLOCKED_SOURCE_NOT_FOUND" EXTENSIONS docs governance`.
- Coverage: source, tests, docs, JSON, and external evidence applicability are
  represented in the checker requirements; this artifact uses the terms only
  to authorize the checker.
- Same-token collision results: `documentStatus` occurs as a
  non-authoritative DSCP test-fixture token with different meaning from EC-02
  lifecycle support.
- Disposition: the occurrence is a collision/isolation constraint, not proof
  of EC-02 lifecycle runtime support and not a bare absence claim.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add a bounded dispatch-quality machine
check that requires negative-search evidence for `NOT FOUND` and
`BLOCKED_SOURCE_NOT_FOUND` claims, and detects same-token repo collisions that
are not recorded as collision or non-authoritative occurrences.

Protected paths:

- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`

Operator authorization: 2026-06-11 operator instructed Codex to continue
tightening checker enforcement after confirming CVF must avoid overclaim while
promoting repeated findings into reusable controls.

Rollback boundary: revert only this authorization artifact, the
negative-search/collision checker changes, focused tests, and the matching
template/standard marker updates if the guard proves too broad. Do not revert
LPCI2 EX/EC artifacts, DSCP artifacts, public-sync README commits, session
state, handoff history, or unrelated governance maintenance.

## Scope Boundary

Allowed:

- update the dispatch-quality checker;
- update focused dispatch-quality checker tests;
- add the exact rule marker to the work-order template;
- add the exact rule marker to the closure-quality standard;
- run focused tests and reviewer-fast gates.

Forbidden:

- runtime/source behavior changes outside governance checker code;
- provider/API-key use;
- public-sync changes;
- corpus ingestion or extraction behavior changes;
- EC-T2 dispatch or implementation;
- production, public-readiness, legal-quality, or current-law claims.

## Finding-To-Governance Learning Disposition

| Field | Value |
| --- | --- |
| defectClass | MACHINE_GATE_GAP |
| learningLane | GOVERNANCE_CONTROL_PLANE |
| disposition | MACHINE_CHECK_ADDED |
| runtime/provider/cost lane | N/A_WITH_REASON - this is control-plane checker hardening only |
| next control action | Keep the guard bounded to evidence/collision discipline; do not claim semantic correctness or legal/current-law quality. |

## Claim Boundary

This artifact authorizes and records a control-plane checker hardening batch
only. It does not prove semantic correctness, runtime behavior, provider
behavior, public readiness, production readiness, legal advice quality, or
current-law freshness.
