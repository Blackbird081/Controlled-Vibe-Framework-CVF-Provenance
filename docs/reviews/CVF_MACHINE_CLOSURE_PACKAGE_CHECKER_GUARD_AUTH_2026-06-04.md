# CVF Machine Closure Package Checker Guard Authorization

Memory class: POINTER_RECORD

Status: APPROVED_GUARD_MAINTENANCE

Date: 2026-06-04

## Purpose

Authorize a bounded guard-maintenance batch that converts the Machine Closure
Package closure rule from reusable prose into a machine checker wired into
autorun and local hook chains.

## Scope

This authorization covers only Machine Closure Package enforcement and related
template/standard wording.

## Target / Source

Target: closed-equivalent governed artifacts that feed downstream CVF loops.

Sources:

- `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`
- `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
- `governance/compat/check_machine_closure_package.py`
- `governance/compat/test_check_machine_closure_package.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `AGENT_HANDOFF_V15_2026-05-29.md`

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add
`governance/compat/check_machine_closure_package.py`, add
`governance/compat/test_check_machine_closure_package.py`, wire the checker
into `governance/compat/run_agent_autorun_workflow_gate.py` and
`governance/compat/run_local_governance_hook_chain.py`, update the work-order
template and closure-quality standard to cite the checker, and perform a
dedicated active-handoff HEAD sync after the guard-maintenance commit.

Protected paths: `governance/compat/check_machine_closure_package.py`,
`governance/compat/test_check_machine_closure_package.py`,
`governance/compat/run_agent_autorun_workflow_gate.py`,
`governance/compat/run_local_governance_hook_chain.py`, and
`AGENT_HANDOFF_V15_2026-05-29.md`.

Operator authorization: operator requested Machine Closure Package become a
checker immediately before pausing LPCI/CVF hardening work.

Rollback boundary: revert this authorization, the new checker/test, autorun
and hook-chain wiring, template/standard edits, and the dedicated handoff-sync
commit as one batch if the checker blocks a valid closed-equivalent artifact
that has equivalent machine-readable closure evidence.

## Evidence Trace Block

| Evidence | Source |
| --- | --- |
| Operator finding | current session request: "Machine Closure Package thành checker riêng" |
| Repeated defect pattern | worker closure prose did not reliably update work order, completion/review, roadmap, registry, loop interlock, and session surfaces |
| Guard target | changed closed-equivalent active governed artifacts only; archive history remains grandfathered |

## Findings / Position

Finding: Machine Closure Package was upgraded into a standard, but without a
machine gate future agents could still close work through prose and leave
downstream loops without registry or digest inputs.

Position: closed-equivalent active artifacts must include a Machine Closure
Package table, must not put external/local paths in Source Verification, and
must not mark GC-051 registry rows `N/A with reason` for corpus/search or
classification closures.

## Risk / Corrective Action

Risk: a too-broad checker could break historical closure artifacts. Corrective
action: the checker evaluates only changed active governed markdown artifacts
with closed-equivalent status and excludes archive paths.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
| --- | --- | --- | --- | --- |
| Machine Closure Package standard could be ignored by future closed-equivalent artifacts | MACHINE_GATE_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_ADDED | Add `check_machine_closure_package.py`, tests, autorun wiring, and local hook wiring |
| Runtime/provider/cost behavior is not changed by this guard-maintenance batch | RUNTIME_SIGNAL_GAP | GOVERNANCE_CONTROL_PLANE | N/A_WITH_REASON | No runtime, provider, cost, token, or latency behavior is modified; no runtime-learning route is needed |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This authorization covers structural closure-package enforcement only. It does
not prove semantic correctness, product readiness, public export, legal advice
quality, runtime integration, or live governance behavior.
