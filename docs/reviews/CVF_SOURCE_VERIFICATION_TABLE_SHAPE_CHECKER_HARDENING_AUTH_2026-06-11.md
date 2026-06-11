# CVF Source Verification Table Shape Checker Hardening Authorization

Memory class: REVIEW_AUTHORIZATION

Status: AUTHORIZED_GUARD_MAINTENANCE

## Purpose

Authorize a bounded governance/control-plane checker hardening batch for work
order Source Verification table shape discipline.

This responds to an EC-T3 dispatch review finding where a source-verification
table could be named correctly but use abbreviated columns, leaving the
dispatch-quality checker without the canonical six-column row contract needed
for source facts.

## Target / Source

Target:

- dispatch-quality checker enforcement for noncanonical Source Verification
  table shapes;
- focused checker regression test;
- canonical Source Verification table-shape standard;
- work-order template cleanup for the reviewer-owned closure anchor token.

Source:

- operator instruction on 2026-06-11 to continue tightening CVF foundation
  controls before the next tranche;
- EC-T3 dispatch packet finding that abbreviated source verification tables
  should be rejected before worker implementation;
- existing mandatory work-order source verification and closure-quality
  standards.

## Findings / Position

Position: proceed with bounded checker hardening.

Findings:

- Reusable control-plane finding: a work order can include a section named
  `Source Verification Block` while its table schema is too weak for the
  existing Source Verification row validators to parse.
- Template finding: the work-order template still used `NOT_EXECUTED_YET` as a
  pending closure anchor token while closure packaging treats that token as
  forbidden closed-equivalent residue.

## Risk / Corrective Action

Risk: a broad checker could block non-source auxiliary tables inside the Source
Verification section.

Corrective action:

- trigger only on ready/dispatched work orders;
- flag only tables whose headers look like source verification evidence;
- leave auxiliary tables such as New Doc-Only Fields outside the shape failure
  unless they are presented as verified source facts;
- state that the checker proves table-shape discipline only, not semantic
  source correctness.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add a bounded dispatch-quality machine
check that rejects noncanonical Source Verification table shapes before worker
dispatch, and add the matching focused regression test.

Protected paths:

- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`

Operator authorization: 2026-06-11 operator instructed Codex to keep promoting
foundation-related findings into CVF controls while Claude continues EC-T3
implementation under a separate worker boundary.

Rollback boundary: revert only this authorization artifact, the
Source Verification table-shape checker change, the focused regression test,
and the matching work-order template cleanup if the guard proves too broad. Do
not revert LPCI2 EX/EC artifacts, DSCP artifacts, public-sync README commits,
session state, active handoff history, worker EC-T3 files, or unrelated
governance maintenance.

## Scope Boundary

Allowed:

- update the dispatch-quality checker;
- update focused dispatch-quality checker tests;
- add the canonical Source Verification table-shape standard;
- update the work-order template wording for canonical Source Verification
  table columns and reviewer-owned closure anchor placeholder;
- run focused tests and reviewer-fast gates.

Forbidden:

- runtime/source behavior changes outside governance checker code;
- provider/API-key use;
- public-sync changes;
- EC-T3 worker implementation or review closure;
- production, public-readiness, legal-quality, current-law, provider-quality,
  runtime-governance, or independent-review claims.

## Finding-To-Governance Learning Disposition

| Field | Value |
| --- | --- |
| defectClass | MACHINE_GATE_GAP |
| learningLane | GOVERNANCE_CONTROL_PLANE |
| disposition | MACHINE_CHECK_ADDED |
| runtime/provider/cost lane | N/A_WITH_REASON - this is control-plane checker hardening only |
| next control action | Dispatch-quality rejects source-verification-like tables that omit the canonical six Source Verification columns. |

## Evidence

| Evidence | Result |
| --- | --- |
| Focused dispatch-quality regression test | `python -m pytest governance/compat/test_check_work_order_dispatch_quality.py` PASS |
| Dispatch-quality gate | `python governance/compat/check_work_order_dispatch_quality.py --base 9ceeec7c --head HEAD --enforce` PASS |
| Guard target | `governance/compat/check_work_order_dispatch_quality.py` |
| Regression target | `governance/compat/test_check_work_order_dispatch_quality.py` |

## Claim Boundary

This artifact authorizes and records a control-plane checker/template hardening
batch only. It does not prove semantic source correctness, runtime behavior,
provider behavior, public readiness, production readiness, legal advice
quality, current-law freshness, or live governance behavior.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance guard-hardening authorization; not public-synced.
