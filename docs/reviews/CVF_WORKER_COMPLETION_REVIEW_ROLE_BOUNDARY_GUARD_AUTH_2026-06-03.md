# CVF Worker Completion Review Role Boundary Guard Authorization

Memory class: POINTER_RECORD

Status: APPROVED_GUARD_MAINTENANCE

Date: 2026-06-03

## Purpose

Authorize a bounded dispatch-quality guard update that prevents delegated
`WORKER_MUST_NOT_COMMIT` workers from owning reviewer completion reviews.

## Scope

This authorization covers a documentation and machine-check hardening batch for
the worker/reviewer boundary in CVF work orders.

## Target / Source

Target: dispatch-quality validation for `WORKER_MUST_NOT_COMMIT` work orders.

Sources:

- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`
- `docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md`
- `AGENT_HANDOFF_V15_2026-05-29.md`

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: update
`governance/compat/check_work_order_dispatch_quality.py`,
`governance/compat/test_check_work_order_dispatch_quality.py`,
`docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`,
`docs/reference/CVF_TRANCHE_COMMIT_CHOREOGRAPHY_STANDARD_2026-06-03.md`, and
`docs/reference/CVF_WORKER_AUTONOMY_DISPATCH_PROMPT_STANDARD_2026-06-01.md`,
plus a dedicated active-handoff HEAD sync after the guard-maintenance commit.

Protected paths: `governance/compat/check_work_order_dispatch_quality.py`,
`governance/compat/test_check_work_order_dispatch_quality.py`,
`AGENT_HANDOFF_V15_2026-05-29.md`, and active governance reference docs named
above.

Operator authorization: operator identified that Claude acting as worker must
not author completion review unless the agent role changes to orchestrator or
reviewer.

Rollback boundary: revert this authorization, the checker/test edits, the
three reference-doc boundary edits, and the dedicated active-handoff sync as
one batch if the rule blocks a valid explicit role-change work order.

## Evidence Trace Block

| Evidence | Source |
| --- | --- |
| Operator finding | current session request: worker should not own completion review while acting as worker |
| Existing weak pattern | prior CI work orders assigned completion review to Worker under no-commit mode |
| Targeted remediation | dispatch-quality gate blocks only ready/dispatch packets with `WORKER_MUST_NOT_COMMIT` and worker-owned completion review |

## Findings / Position

Finding: a worker operating under `WORKER_MUST_NOT_COMMIT` should not author or
own the completion review, because that collapses worker output, reviewer
disposition, and committed-range closure evidence into one role.

Position: worker output may include a handoff, evaluation packet, report, or
pending artifact list. The completion review is reviewer / committer owned
unless the work order explicitly changes role and commit mode before dispatch.

## Risk / Corrective Action

Risk: without this boundary, future orchestrators can accidentally assign
reviewer closure work to a worker and then treat pending worker evidence as a
closed-equivalent review.

Corrective action: add a dispatch-quality machine check, focused unit tests,
and reference/template wording so the rule is visible to both humans and
agents.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| Work orders allowed worker-owned completion review despite `WORKER_MUST_NOT_COMMIT` | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | Dispatch-quality gate now blocks worker-owned completion reviews unless role/commit mode changes before dispatch |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This authorization allows a narrow dispatch-quality guard and template
hardening. It does not change product execution behavior, authorize public sync, or
invalidate already-closed historical completion reviews.
