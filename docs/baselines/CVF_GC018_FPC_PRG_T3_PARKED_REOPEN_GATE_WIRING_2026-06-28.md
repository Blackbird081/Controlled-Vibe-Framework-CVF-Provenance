# CVF GC-018 FPC-PRG-T3 Parked Reopen Gate Wiring - 2026-06-28

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

## Purpose

Wire the existing PRG-T2 parked reopen inventory checker into local governance
catalogs so future agents cannot bypass recorded reopen-condition validation.

## Decision / Baseline / Proposed Tranche

Decision: `WIRE_EXISTING_PARKED_REOPEN_CHECKER_INTO_LOCAL_GATES`.

Baseline: FPC-PRG-T2 added
`governance/compat/check_fpc_parked_reopen_inventory.py` and focused tests at
material commit `ec7e4057`.

Proposed tranche: FPC-PRG-T3 wires the existing checker into local autorun and
hook catalogs. It does not change the checker contract or reopen any parked
runtime/provider/public/MPI lane.

## Source Authority

| Source | Role |
|---|---|
| `docs/roadmaps/CVF_FPC_PRG_T0_PARKED_REOPEN_GATE_SYSTEMIZATION_ROADMAP_2026-06-28.md` | T3 sequence authority |
| `docs/baselines/CVF_GC018_FPC_PRG_T2_PARKED_REOPEN_GATE_CHECKER_2026-06-28.md` | checker existence and T3 deferral authority |
| `governance/compat/agent_autorun_command_catalog.py` | autorun catalog |
| `governance/compat/local_governance_hook_catalog_pre_commit.py` | pre-commit hook catalog |
| `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | reviewer-fast hook catalog |
| `governance/compat/local_governance_hook_catalog_pre_push.py` | pre-push hook catalog |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Evidence kind | Disposition |
|---|---|---|---|---|---|---|
| T3 is gate wiring after T2 checker | `docs/roadmaps/CVF_FPC_PRG_T0_PARKED_REOPEN_GATE_SYSTEMIZATION_ROADMAP_2026-06-28.md` | `Roadmap Sequence` | `FPC-PRG-T3` | PRG-T0 roadmap | VALUE_SET | ACCEPT |
| T2 checker exists | `governance/compat/check_fpc_parked_reopen_inventory.py` | `def main()` | `main` | Python checker CLI | EXISTS | ACCEPT |
| autorun catalog supports range commands | `governance/compat/agent_autorun_command_catalog.py` | `_range_command` entries | `_range_command` | autorun catalog | EXISTS | ACCEPT |
| local pre-commit catalog exists | `governance/compat/local_governance_hook_catalog_pre_commit.py` | `PRE_COMMIT_CHECKS` | `PRE_COMMIT_CHECKS` | local hook catalog | EXISTS | ACCEPT |
| reviewer-fast catalog exists | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | command tuple list | `FPC system-chain acceptance ledger` | local hook catalog | EXISTS | ACCEPT |
| pre-push catalog exists | `governance/compat/local_governance_hook_catalog_pre_push.py` | command tuple list | `FPC system-chain acceptance ledger` | local hook catalog | EXISTS | ACCEPT |

## ADIF Defect Registry Disclosure

Query line:
`resolve_defect_packet(task_class='Work-order authoring / dispatch', role='dispatcher', lifecycle_phase='pre-dispatch')`

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0006

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: wire the existing PRG-T2 checker into
existing local governance catalogs only.

Protected paths:

- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`

Operator authorization: approved T1-T5 continuation after PRG-T0 selected the
parked reopen gate systemization roadmap.

Rollback boundary: if T3 is rejected, revert only the four catalog edits, this
baseline, and the T3 completion review. Do not revert PRG-T2 material commit
`ec7e4057` or session-sync commit `c22ef0f0`.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | autorun catalog, local hook catalogs, PRG-T2 checker |
| Runtime behavior claimed | N/A_WITH_REASON: T3 wires local governance commands only |
| Live/provider proof claimed | N/A_WITH_REASON: no live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized or performed |
| Freshness disposition | PASS - current source evidence supports gate wiring only |

## Acceptance Criteria

| ID | Criterion | Disposition |
|---|---|---|
| AC1 | autorun pre-implementation includes `FPC parked reopen inventory` | PASS |
| AC2 | pre-commit catalog includes `FPC parked reopen inventory` | PASS |
| AC3 | reviewer-fast catalog includes `FPC parked reopen inventory` | PASS |
| AC4 | pre-push catalog includes `FPC parked reopen inventory` | PASS |
| AC5 | no runtime/provider/live/public/MPI lane implementation is added | PASS |

## Evidence / Verification

| Evidence item | Command or artifact | Required result |
|---|---|---|
| checker still passes | `python governance/compat/check_fpc_parked_reopen_inventory.py --enforce` | PASS |
| autorun includes new gate | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base c22ef0f0 --head HEAD --serial` | PASS |
| steward preflight | `python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base c22ef0f0 --head HEAD --enforce` | PASS before commit |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | PRG-T0 roadmap | T3 sequence row | PASS |
| Work order status | N/A with reason: direct single-agent wiring tranche | N/A with reason | N/A with reason |
| Completion or reviewer artifact | `docs/reviews/CVF_FPC_PRG_T3_PARKED_REOPEN_GATE_WIRING_COMPLETION_2026-06-28.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Gate wiring | four catalog files | checker command present | PASS |
| Registry JSON | BLOCKED with reason: no registry JSON mutation is authorized | no registry path changed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown mutation is authorized | no registry path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence digest is consumed | no external source promoted | N/A with reason |
| System loop interlock | `governance/compat/check_fpc_system_chain_acceptance_ledger.py` | T7 checker remains PASS | PASS |
| Runtime/live proof | N/A with reason: no runtime/provider behavior is claimed | no live run required | N/A with reason |
| Public sync | N/A with reason: no public-sync is authorized | no public paths changed | N/A with reason |
| Session continuity | N/A with reason: T5 owns final session/front-door sync after T3-T4 | no generated session state change | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T3 is private provenance governance wiring only. No public-facing
artifact or public-sync mutation is authorized.

## Claim Boundary

FPC-PRG-T3 proves only local gate wiring for the parked reopen inventory
checker. It does not approve reopening or implementing any parked lane.
