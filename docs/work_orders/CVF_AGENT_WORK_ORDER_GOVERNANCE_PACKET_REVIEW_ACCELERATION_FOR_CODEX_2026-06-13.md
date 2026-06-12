# CVF Agent Work Order - Governance Packet Review Acceleration

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-13

Assigned agent: Codex

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `0386aa35`

executionBaseHead: `0386aa35`

closureBaseHead: `0386aa35`

## Purpose

Execute a bounded control-plane hardening batch before MEMCON-T1b so CVF can
catch malformed proof-manifest requirements earlier.

## Authority Chain

GC-018:

`docs/baselines/CVF_GC018_GOVERNANCE_PACKET_REVIEW_ACCELERATION_2026-06-13.md`

Operator instruction: strengthen CVF before moving to MEMCON-T1b.

## Objective

Add a pre-dispatch machine check that rejects compound Required Proof Manifest
literal cells and documents the authoring rule for future orchestrators.

## Agent Roles

Codex acts as orchestrator, implementer, reviewer, and closer for this bounded
control-plane tranche.

## Single-Agent Multi-Role Control Block

- Role separation ledger: GC-018, work order, checker diff, tests, and
  completion review record distinct duties.
- Evidence basis: review uses git diff, source paths, focused unit tests, and
  governance gates, not memory-only claims.
- Self-review boundary: independent review is not claimed for this batch.
- Escalation conditions: stop for operator or external reviewer if scope
  expands to MEMCON-T1b, Policy_Local, public-sync, provider/API, or live proof.
- Gate sequence: focused unittest, reviewer-fast, commit hook chain, and
  pre-closure gate on a real range.

## Intake Role Routing Decision

- Intake summary: operator requested CVF foundation hardening before MEMCON-T1b.
- Scope classification: bounded governance-control-plane checker and standard
  update.
- Risk sensitivity: no public-sync, provider, live, secret, legal, production,
  or readiness claim.
- Selected role route: routeMode=SINGLE_AGENT_MULTI_ROLE.
- Role separation basis: small tranche uses artifact-separated single-agent
  roles with machine gates.
- Escalation condition: stop if changes require public-sync, live proof,
  Policy_Local, MEMCON-T1b implementation, or broad template refactor.

## Allowed Scope

Allowed scope:

- `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md`
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/test_check_work_order_dispatch_quality.py`
- `docs/baselines/CVF_GC018_GOVERNANCE_PACKET_REVIEW_ACCELERATION_2026-06-13.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_GOVERNANCE_PACKET_REVIEW_ACCELERATION_FOR_CODEX_2026-06-13.md`
- `docs/reviews/CVF_GOVERNANCE_PACKET_REVIEW_ACCELERATION_COMPLETION_2026-06-13.md`

Forbidden scope:

- MEMCON-T1b implementation or dispatch.
- Policy_Local mutation.
- EC activation, retrieval, OCR/provider/API, corpus ingestion, public-sync,
  public readiness, production readiness, memory reinjection, or autonomous
  mutation claims.
- Broad template refactor, archive cleanup, or session-front-door rotation.

## Worker Autonomy / No-Question Rule

Allowed-scope remediation is mandatory. If the focused tests or governance
gates fail inside Allowed scope, Codex must repair and rerun instead of asking
the operator whether to fix it.

## Current Runtime Freshness Verification

Runtime/source absence claims are out of scope for this work order. The changed
range is limited to the dispatch-quality checker, its focused test module, and
governance documentation. No runtime route, provider path, Policy_Local path,
EC activation path, retrieval path, OCR path, or memory reinjection path is
claimed changed or unchanged as product behavior.

## Required First Reads

- `AGENTS.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V18_2026-06-12.md`
- `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md`
- `governance/compat/check_work_order_dispatch_quality.py`

## Pre-Flight Checks

- Confirm worktree status before edits.
- Confirm current active handoff and next allowed move.
- Run focused dispatch-quality tests before closure.
- Run reviewer-fast before commit.

## Write Ownership

Write ownership is limited to the paths listed in Allowed Scope. Session
continuity updates, if required after material commit, must be a separate
session-sync batch.

## Execution Plan

1. Add atomic Required Proof Manifest literal validation to the dispatch-quality
   checker.
2. Add focused unit tests for compound and atomic proof literal rows.
3. Update authoring hardening guidance.
4. Run focused tests and governance gates.
5. Commit material closure, then update session continuity if mode changes.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Required Proof Manifest uses a Required literal column | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | Required Proof Manifest | `Required literal` | work-order template | ACCEPT |
| Dispatch checker reads Required Proof Manifest rows | `governance/compat/check_work_order_dispatch_quality.py` | `_validate_work_order_fulfillment_manifests` | `Required Proof Manifest` | dispatch-quality checker | ACCEPT |
| Authoring hardening addendum owns adjacent packet-hardening rules | `docs/reference/CVF_WORK_ORDER_AUTHORING_HARDENING_ADDENDUM_2026-06-11.md` | Near-Threshold Template Owner Discipline | `Near-Threshold Template Owner Discipline` | work-order authoring hardening addendum | ACCEPT |
| Focused dispatch-quality tests exist | `governance/compat/test_check_work_order_dispatch_quality.py` | unittest module | `WorkOrderDispatchQualityTests` | dispatch-quality tests | ACCEPT |

## Acceptance Criteria

- Compound Required Proof Manifest literal cells are rejected.
- One atomic literal per row is accepted.
- The authoring addendum explains the rule and the reason.
- Focused tests pass.
- Reviewer-fast and pre-closure gates pass for the changed range.

## Evidence Requirements

- `python -m unittest governance.compat.test_check_work_order_dispatch_quality`
- `python governance/compat/check_work_order_dispatch_quality.py --base 0386aa35 --head HEAD --enforce`
- `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`

## Verification Evidence

- `python -m unittest governance.compat.test_check_work_order_dispatch_quality`
  PASS 66/66.
- `python governance/compat/check_work_order_dispatch_quality.py --base 0386aa35 --head HEAD --enforce`
  PASS before closure artifacts were added.

## Closure Checklist

- [x] Checker hardening added.
- [x] Focused tests added.
- [x] Authoring guidance updated.
- [x] Claim boundary preserved.
- [x] No MEMCON-T1b, Policy_Local, public-sync, provider/API, or readiness
  claim added.

## Review Gate

Reviewer-fast must pass before material closure. Any allowed-scope
reviewer-fast failure must be fixed in this batch.

## Return-To-Orchestrator Conditions

Return to operator only if remediation would require MEMCON-T1b execution,
Policy_Local mutation, public-sync, provider/API proof, broad template
refactor, session-front-door rotation, or changes outside Allowed scope.

## Operator Checkpoint

Operator checkpoint satisfied by direct instruction to upgrade CVF before
MEMCON-T1b.

## Closure Result

Status: `CLOSED_PASS_BOUNDED`.

Completion:

`docs/reviews/CVF_GOVERNANCE_PACKET_REVIEW_ACCELERATION_COMPLETION_2026-06-13.md`

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | Status: CLOSED_PASS_BOUNDED | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GOVERNANCE_PACKET_REVIEW_ACCELERATION_COMPLETION_2026-06-13.md` | Status: CLOSED_PASS_BOUNDED | PASS |
| Roadmap state | N/A | Direct operator-authorized small control-plane batch; no separate roadmap opened | N/A with reason |
| Registry JSON | N/A | GC-051 registry is outside this checker-authoring batch | BLOCKED with reason |
| Registry Markdown | N/A | GC-051 registry Markdown is outside this checker-authoring batch | BLOCKED with reason |
| External evidence digest | N/A | no external evidence used | N/A with reason |
| System loop interlock | N/A | no new runtime/system loop connection claimed | N/A with reason |
| Session continuity | active handoff/session state | sync after material commit if current mode changes | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is private provenance control-plane hardening. No public-facing
catalog, README, or public-sync update is authorized in this batch.

## Claim Boundary

This work order proves only Required Proof Manifest atomic literal discipline
and dispatch-quality checker coverage. It does not prove global hook latency
reduction, MEMCON-T1b readiness, Policy_Local readiness, public readiness,
production readiness, OCR/provider behavior, or autonomous mutation.
