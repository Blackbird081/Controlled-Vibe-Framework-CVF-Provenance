# CVF Governance Fast Reviewer Gate And Front-Door Rotation Roadmap

Memory class: GOVERNED_ROADMAP

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-07

Owner: Codex reviewer/committer

## Purpose

Reduce reviewer/commit latency for governed worker-return batches without
weakening the full closure chain.

## Scope / Target / Owner Boundary

Target:

- local governance hook runner;
- reviewer/committer preflight workflow;
- active session front door and handoff pointer files.

Owner boundary:

- private control-plane hardening only;
- no runtime route, provider, corpus, public-sync, or product readiness work.

## Authorization / Decision

Operator authorized Codex on 2026-06-07 to proceed with the Governance Fast
Reviewer Gate / Commit Latency Reduction roadmap and to rotate or compact
`AGENT_HANDOFF_V16_2026-06-06.md` plus `CVF_SESSION_MEMORY.md`.

Decision: execute as a bounded direct Codex reviewer/committer batch.

## Scope

In scope:

- add `reviewer-fast` local hook mode;
- run latency-sensitive local hook modes in parallel by default;
- retain `--serial` debug escape hatch;
- update agent/closure standards to use the fast reviewer gate;
- rotate V16 and compact session memory.

## Non-Goals

Out of scope:

- removing any full hook-chain checker;
- weakening pre-closure or pre-push autorun gates;
- changing provider/runtime behavior;
- public-sync or public catalog export;
- DSCP-T2 implementation;
- PolicyLocal T12 authoring.

## Work Plan

1. Add `reviewer-fast` to `run_local_governance_hook_chain.py`.
2. Add focused tests for hook-chain structure and parallel defaults.
3. Document reviewer-fast placement in `AGENTS.md` and the closure standard.
4. Rotate V16 to archive and open compact V17.
5. Compact `CVF_SESSION_MEMORY.md`.
6. Run focused and autorun gates, then commit material and session-sync
   changes.

## Acceptance Criteria

- `reviewer-fast` is a valid hook-chain mode.
- `reviewer-fast`, `pre-commit`, and `pre-push` default to parallel execution.
- `--serial` remains available.
- Exactly one root active handoff exists.
- `CVF_SESSION_MEMORY.md` is back below soft threshold.
- Full pre-commit and committed-range pre-closure still pass.

## Verification / Evidence

Required verification commands:

- `python -m pytest governance/compat/test_run_local_governance_hook_chain.py -q`
- `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`
- `python governance/compat/check_active_session_state.py --enforce`
- `python governance/compat/check_governed_file_size.py --enforce`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 82b53975 --head HEAD`

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work instruction | Output artifact | Verification |
| --- | --- | --- | --- |
| Add early reviewer-return defect filter | Add `reviewer-fast` local hook mode | `governance/compat/run_local_governance_hook_chain.py` | focused unit test and reviewer-fast run |
| Reduce commit latency while preserving checks | Run latency-sensitive hook modes in parallel by default with `--serial` escape hatch | `governance/compat/run_local_governance_hook_chain.py` | focused unit test and pre-commit hook run |
| Make future agents use the gate | Document reviewer-fast phase placement | `AGENTS.md`; closure-quality standard | docs governance and dispatch-quality gates |
| Rotate soft-threshold front doors | Archive V16 and open compact V17; compact session memory | `AGENT_HANDOFF_V17_2026-06-07.md`; `CVF_SESSION_MEMORY.md`; archived V16 | active-session and governed-file-size gates |

## Closure Diff Gate

Allowed paths:

- `AGENTS.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V17_2026-06-07.md`
- `CVF_SESSION/handoffs/archive/AGENT_HANDOFF_V16_2026-06-06.md`
- `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`
- `docs/roadmaps/CVF_GOVERNANCE_FAST_REVIEWER_GATE_AND_FRONT_DOOR_ROTATION_ROADMAP_2026-06-07.md`
- `docs/reviews/CVF_GOVERNANCE_FAST_REVIEWER_GATE_AND_FRONT_DOOR_ROTATION_COMPLETION_2026-06-07.md`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/test_run_local_governance_hook_chain.py`
- `governance/compat/CVF_ROOT_FILE_EXPOSURE_REGISTRY.json`

Forbidden paths:

- public-sync repository;
- runtime provider routes;
- PolicyLocal corpus data;
- package manifests;
- API keys or secret files.

## Negative And Fail-Condition Scan

| Condition | Expected disposition |
| --- | --- |
| `reviewer-fast` missing from local hook choices | BLOCKED |
| Pre-commit no longer runs full chain | BLOCKED |
| Parallel mode has no serial escape hatch | BLOCKED |
| More than one root active handoff | BLOCKED |
| Front door points to archived handoff | BLOCKED |
| V16 remains as active root handoff | BLOCKED |
| Public/runtime/readiness claim appears | BLOCKED |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | N/A with reason | operator-authorized direct governance hardening batch | N/A with reason - no delegated work order |
| Completion or reviewer artifact | `docs/reviews/CVF_GOVERNANCE_FAST_REVIEWER_GATE_AND_FRONT_DOOR_ROTATION_COMPLETION_2026-06-07.md` | completion packet created | PASS |
| Roadmap state | `docs/roadmaps/CVF_GOVERNANCE_FAST_REVIEWER_GATE_AND_FRONT_DOOR_ROTATION_ROADMAP_2026-06-07.md` | status `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `governance/compat/CVF_ROOT_FILE_EXPOSURE_REGISTRY.json` | active root handoff exposure path changed to V17 | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V17_2026-06-07.md` | front-door pointers compacted and updated | PASS |
| External evidence digest | N/A with reason | no external artifacts or provider evidence | N/A with reason - no external evidence |
| System loop interlock | N/A with reason | no new cross-loop runtime signal | N/A with reason - control-plane latency hardening only |
| Session continuity | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V17_2026-06-07.md` | current mode and next move updated | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance control-plane hardening only. No public-sync,
public catalog, runtime behavior, or readiness claim is authorized by this
roadmap.

## Claim Boundary

This roadmap closes only local reviewer-fast preflight, parallel local hook
execution, and compact active-session rotation. It does not claim runtime
governance behavior, provider behavior, live proof, public-sync, public
readiness, hosted readiness, production readiness, PolicyLocal T12 readiness,
or DSCP-T2 implementation.
