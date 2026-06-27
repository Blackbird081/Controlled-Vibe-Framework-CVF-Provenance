# CVF GC-018 FPC-PRG-T2 Parked Reopen Gate Checker

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018_baseline

Date: 2026-06-28

Owner: Codex

rawMemoryReleased: false

## Purpose

Implement the focused parked reopen inventory checker after PRG-T1 created a
source inventory.

## Scope / Target / Owner Boundary

Allowed material scope:

- add `governance/compat/check_fpc_parked_reopen_inventory.py`;
- add focused unit coverage for the checker;
- file this GC-018 baseline and matching completion review.

Forbidden material scope:

- no autorun, reviewer-fast, pre-commit, or pre-push wiring yet;
- no downstream implementation lane selection;
- no public-sync or push from the provenance workspace;
- no runtime/MCP/CLI/IDE bridge implementation;
- no provider/live proof;
- no adapter, resolver, package, certification, or generated session mutation;
- no MPI-T6 runtime work.

## Decision / Baseline / Proposed Tranche

Decision: `IMPLEMENT_PARKED_REOPEN_INVENTORY_CHECKER`.

Baseline: PRG-T1 inventory exists at
`docs/reference/CVF_FPC_PRG_T1_PARKED_REOPEN_CONDITION_SOURCE_INVENTORY_2026-06-28.json`
and is ready for machine validation against DSD-T1 and T7.

Proposed next tranche: `FPC-PRG-T3 Parked Reopen Gate Wiring Decision`.

## Source Authority

| Source | Path | Role |
|---|---|---|
| PRG-T0 roadmap | `docs/roadmaps/CVF_FPC_PRG_T0_PARKED_REOPEN_GATE_SYSTEMIZATION_ROADMAP_2026-06-28.md` | T2 checker sequence authority |
| PRG-T1 inventory | `docs/reference/CVF_FPC_PRG_T1_PARKED_REOPEN_CONDITION_SOURCE_INVENTORY_2026-06-28.json` | checker input |
| DSD-T1 baseline | `docs/baselines/CVF_GC018_FPC_DSD_T1_FOUNDATION_DOWNSTREAM_POST_PUBLIC_EXPORT_LANE_SELECTION_DECISION_2026-06-28.md` | reopen condition text owner |
| T7 ledger | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` | lane IDs, required conditions, and forbidden lists |
| Existing FPC checker | `governance/compat/check_fpc_system_chain_acceptance_ledger.py` | checker pattern |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| T2 is the checker tranche after T1 inventory | `docs/roadmaps/CVF_FPC_PRG_T0_PARKED_REOPEN_GATE_SYSTEMIZATION_ROADMAP_2026-06-28.md` | `Roadmap Sequence` | `FPC-PRG-T2` | PRG-T0 roadmap | VALUE_SET | ACCEPT |
| PRG-T1 inventory exists | `docs/reference/CVF_FPC_PRG_T1_PARKED_REOPEN_CONDITION_SOURCE_INVENTORY_2026-06-28.json` | top-level JSON | `inventoryId` | PRG-T1 inventory schema | EXISTS | ACCEPT |
| DSD-T1 owns reopen condition table | `docs/baselines/CVF_GC018_FPC_DSD_T1_FOUNDATION_DOWNSTREAM_POST_PUBLIC_EXPORT_LANE_SELECTION_DECISION_2026-06-28.md` | `Reopen Conditions` | `Reopen Conditions` | DSD-T1 baseline | VALUE_SET | ACCEPT |
| T7 ledger owns downstream gate lists | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` | `downstreamReopenGates` | `downstreamReopenGates` | T7 ledger schema | EXISTS | ACCEPT |
| existing FPC checker uses `validate_ledger` pattern | `governance/compat/check_fpc_system_chain_acceptance_ledger.py` | function | `validate_ledger` | FPC checker | RUNTIME_BEHAVIOR | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0006

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add a focused checker and unit tests for
PRG-T2, and correct any PRG-T1 inventory source-path drift the checker exposes,
without hook wiring or runtime/public implementation.

Protected paths:

- `governance/compat/check_fpc_parked_reopen_inventory.py`
- `governance/compat/test_check_fpc_parked_reopen_inventory.py`

Operator authorization: approved T1-T5 continuation after PRG-T0 selected the
parked reopen gate systemization roadmap.

Rollback boundary: if T2 is rejected, revert only the checker, tests, T2
baseline, T2 completion review, and the PRG-T1 inventory path correction in
this T2 range. Do not revert PRG-T1 inventory commit `ca60e1fd`, PRG-T0
material commit `8d4ed2f4`, or earlier FPC closures.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | PRG-T1 inventory, T7 ledger, DSD-T1 baseline, existing FPC checker pattern |
| Runtime behavior claimed | N/A_WITH_REASON: checker validates local governed artifacts only |
| Live/provider proof claimed | N/A_WITH_REASON: no live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized or performed |
| Freshness disposition | PASS - current source evidence supports checker implementation only |

## Acceptance Criteria

| ID | Criterion | Disposition |
|---|---|---|
| AC1 | checker validates PRG-T1 inventory parses as JSON | PASS |
| AC2 | checker requires the three parked lane IDs | PASS |
| AC3 | checker compares condition text to DSD-T1 | PASS |
| AC4 | checker compares required and forbidden lists to T7 | PASS |
| AC5 | checker rejects missing owning artifacts or empty evidence fields | PASS |
| AC6 | no gate wiring is added in T2 | PASS |
| AC7 | checker-exposed PRG-T1 source-path drift is corrected to the existing archive path | PASS |

## Evidence / Verification

| Evidence item | Command or artifact | Required result |
|---|---|---|
| focused unit tests | `python -m unittest governance.compat.test_check_fpc_parked_reopen_inventory` | PASS |
| checker on current repo | `python governance/compat/check_fpc_parked_reopen_inventory.py --enforce` | PASS |
| governance gates | pre-implementation autorun and commit steward over T2 range | PASS before commit |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_FPC_PRG_T0_PARKED_REOPEN_GATE_SYSTEMIZATION_ROADMAP_2026-06-28.md` | T2 sequence row | PASS |
| Work order status | N/A with reason: direct single-agent checker tranche | N/A with reason | N/A with reason |
| Completion or reviewer artifact | `docs/reviews/CVF_FPC_PRG_T2_PARKED_REOPEN_GATE_CHECKER_COMPLETION_2026-06-28.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Checker implementation | `governance/compat/check_fpc_parked_reopen_inventory.py` | checker command PASS | PASS |
| Checker tests | `governance/compat/test_check_fpc_parked_reopen_inventory.py` | focused unittest PASS | PASS |
| Registry JSON | BLOCKED with reason: no registry JSON mutation is authorized | no registry path changed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown mutation is authorized | no registry path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence digest is consumed | no external source promoted | N/A with reason |
| System loop interlock | `governance/compat/check_fpc_system_chain_acceptance_ledger.py` | T7 checker remains PASS | PASS |
| Gate wiring | BLOCKED with reason: wiring is T3 | no hook/catalog path changed | BLOCKED with reason |
| Public sync | N/A with reason: no public-sync is authorized | no public paths changed | N/A with reason |
| Runtime/live proof | N/A with reason: no runtime/provider governance behavior is claimed | no live run required | N/A with reason |
| Session continuity | N/A with reason: T5 owns final session/front-door sync after T2-T4 complete | no generated session state change | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance checker for internal parked-lane evidence.
No public artifact is authorized by T2.

## Claim Boundary

FPC-PRG-T2 implements a local artifact checker only. It does not authorize or
claim hook wiring, live governance proof, runtime execution, provider behavior,
route behavior, MCP/CLI/IDE bridge behavior, public-sync, package activation,
certification, adapter implementation, MPI-T6 runtime value, production
readiness, public readiness, or universal governed control.
