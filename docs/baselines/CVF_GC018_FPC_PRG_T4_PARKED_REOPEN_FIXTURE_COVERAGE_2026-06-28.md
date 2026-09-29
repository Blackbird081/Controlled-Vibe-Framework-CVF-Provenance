# CVF GC-018 FPC-PRG-T4 Parked Reopen Fixture Coverage - 2026-06-28

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

## Purpose

Expand focused unit-test coverage for the PRG-T2 parked reopen inventory
checker after PRG-T3 wired it into local governance gates.

## Decision / Baseline / Proposed Tranche

Decision: `EXPAND_PARKED_REOPEN_CHECKER_FIXTURE_COVERAGE`.

Baseline: PRG-T3 wired `governance/compat/check_fpc_parked_reopen_inventory.py`
into local governance catalogs at material commit `f74f0b7a`.

Proposed tranche: PRG-T4 adds fixture coverage for wrong lane ID, missing
evidence fields, boundary flag drift, and forbidden-list drift. It does not
change gate wiring or runtime behavior.

## Source Authority

| Source | Role |
|---|---|
| `docs/roadmaps/CVF_FPC_PRG_T0_PARKED_REOPEN_GATE_SYSTEMIZATION_ROADMAP_2026-06-28.md` | T4 sequence authority |
| `governance/compat/check_fpc_parked_reopen_inventory.py` | checker contract |
| `governance/compat/test_check_fpc_parked_reopen_inventory.py` | focused fixture suite |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Evidence kind | Disposition |
|---|---|---|---|---|---|---|
| T4 is fixture coverage after wiring | `docs/roadmaps/CVF_FPC_PRG_T0_PARKED_REOPEN_GATE_SYSTEMIZATION_ROADMAP_2026-06-28.md` | `Roadmap Sequence` | `FPC-PRG-T4` | PRG-T0 roadmap | VALUE_SET | ACCEPT |
| checker validates lane IDs | `governance/compat/check_fpc_parked_reopen_inventory.py` | `validate_inventory` | `REQUIRED_LANE_IDS` | checker validation | EXISTS | ACCEPT |
| checker validates boundary false fields | `governance/compat/check_fpc_parked_reopen_inventory.py` | `validate_inventory` | `REQUIRED_BOUNDARY_FALSE_FIELDS` | checker validation | EXISTS | ACCEPT |
| checker validates forbidden list drift | `governance/compat/check_fpc_parked_reopen_inventory.py` | `validate_inventory` | `forbiddenUntilGatePasses` | checker validation | EXISTS | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0006

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: extend the focused unit-test suite for the
existing parked reopen checker only.

Protected paths:

- `governance/compat/test_check_fpc_parked_reopen_inventory.py`

Operator authorization: approved T1-T5 continuation after PRG-T0 selected the
parked reopen gate systemization roadmap.

Rollback boundary: if T4 is rejected, revert only the test-file additions, this
baseline, and the T4 completion review. Do not revert PRG-T3 material commit
`f74f0b7a` or session-sync commit `f925103e`.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | PRG-T2 checker and focused test suite |
| Runtime behavior claimed | N/A_WITH_REASON: T4 validates local checker fixtures only |
| Live/provider proof claimed | N/A_WITH_REASON: no live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized or performed |
| Freshness disposition | PASS - current source evidence supports fixture coverage only |

## Acceptance Criteria

| ID | Criterion | Disposition |
|---|---|---|
| AC1 | wrong lane ID fixture rejects inventory | PASS |
| AC2 | empty evidence fields fixture rejects inventory | PASS |
| AC3 | boundary flag drift fixture rejects inventory | PASS |
| AC4 | forbidden-list drift fixture rejects inventory | PASS |
| AC5 | no catalog wiring or runtime/public/MPI implementation is added | PASS |

## Evidence / Verification

| Evidence item | Command or artifact | Required result |
|---|---|---|
| focused unit tests | `python -m unittest governance.compat.test_check_fpc_parked_reopen_inventory` | PASS |
| checker on current repo | `python governance/compat/check_fpc_parked_reopen_inventory.py --enforce` | PASS |
| steward preflight | `python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base f925103e --head HEAD --enforce` | PASS before commit |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | PRG-T0 roadmap | T4 sequence row | PASS |
| Work order status | N/A with reason: direct single-agent fixture tranche | N/A with reason | N/A with reason |
| Completion or reviewer artifact | `docs/reviews/CVF_FPC_PRG_T4_PARKED_REOPEN_FIXTURE_COVERAGE_COMPLETION_2026-06-28.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Fixture tests | `governance/compat/test_check_fpc_parked_reopen_inventory.py` | focused unittest PASS | PASS |
| Registry JSON | BLOCKED with reason: no registry JSON mutation is authorized | no registry path changed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown mutation is authorized | no registry path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence digest is consumed | no external source promoted | N/A with reason |
| System loop interlock | `governance/compat/check_fpc_system_chain_acceptance_ledger.py` | T7 checker remains PASS | PASS |
| Runtime/live proof | N/A with reason: no runtime/provider behavior is claimed | no live run required | N/A with reason |
| Public sync | N/A with reason: no public-sync is authorized | no public paths changed | N/A with reason |
| Session continuity | N/A with reason: T5 owns final session/front-door sync after T4 | no generated session state change | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T4 is private provenance test coverage only.

## Claim Boundary

FPC-PRG-T4 proves only local checker fixture coverage. It does not approve or
implement any parked lane.
