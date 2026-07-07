# CVF GC-018 FPC-PRG-T1 Parked Reopen Condition Source Inventory

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: gc018_baseline

Date: 2026-06-28

Owner: Codex

rawMemoryReleased: false

## Purpose

Create the source-verified inventory that FPC-PRG-T2 can consume before any
parked reopen checker is implemented.

## Scope / Target / Owner Boundary

Allowed material scope:

- add the parked reopen condition source inventory JSON;
- file this GC-018 baseline and the matching completion review;
- source-verify lane IDs, condition text, owning artifacts, evidence fields,
  and forbidden-until-gate-passes lists.

Forbidden material scope:

- no checker implementation;
- no gate or hook wiring;
- no downstream implementation lane selection;
- no public-sync or push from the provenance workspace;
- no runtime/MCP/CLI/IDE bridge implementation;
- no provider/live proof;
- no adapter, resolver, package, certification, or generated session mutation;
- no MPI-T6 runtime work.

## Decision / Baseline / Proposed Tranche

Decision: `CREATE_PARKED_REOPEN_CONDITION_SOURCE_INVENTORY`.

Baseline: PRG-T0 closed with checker implementation deferred until T1 inventory
exists. DSD-T1 records lane-specific reopen-condition text, and T7 records the
matching downstream lane IDs, required conditions, and forbidden-until-gate
lists.

Proposed next tranche: `FPC-PRG-T2 Parked Reopen Gate Checker`.

## Source Authority

| Source | Path | Role |
|---|---|---|
| PRG-T0 roadmap | `docs/roadmaps/CVF_FPC_PRG_T0_PARKED_REOPEN_GATE_SYSTEMIZATION_ROADMAP_2026-06-28.md` | upstream sequence authority |
| Active front door | `CVF_SESSION_MEMORY.md` | current next move and parked checkpoint |
| Active handoff | `AGENT_HANDOFF_V25_2026-06-28.md` | current lane conditions and forbidden scope |
| DSD-T1 baseline | `docs/baselines/CVF_GC018_FPC_DSD_T1_FOUNDATION_DOWNSTREAM_POST_PUBLIC_EXPORT_LANE_SELECTION_DECISION_2026-06-28.md` | lane-specific reopen-condition text |
| T7 ledger | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` | lane IDs, required conditions, and forbidden lists |
| Value-parked standard | `docs/reference/CVF_VALUE_PARKED_LANE_REOPEN_DISCIPLINE_STANDARD_2026-06-25.md` | rule against re-proposal before checking recorded condition |

Provider-specific memory, browser state, local API keys, and chat-only facts are
not CVF source authority for this tranche.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| PRG-T1 must create inventory before checker work | `docs/roadmaps/CVF_FPC_PRG_T0_PARKED_REOPEN_GATE_SYSTEMIZATION_ROADMAP_2026-06-28.md` | `Roadmap Sequence` | `FPC-PRG-T1` | PRG-T0 roadmap | VALUE_SET | ACCEPT |
| next allowed move is PRG-T1 inventory only | `CVF_SESSION_MEMORY.md` | `Next Allowed Move` | `FPC-PRG-T1 Parked Reopen Condition Source Inventory` | active session front door | VALUE_SET | ACCEPT |
| active handoff forbids checker implementation until after inventory | `AGENT_HANDOFF_V25_2026-06-28.md` | `Next Allowed Move` | `Checker implementation is deferred to T2` | active handoff | VALUE_SET | ACCEPT |
| DSD-T1 owns lane-specific reopen-condition text | `docs/baselines/CVF_GC018_FPC_DSD_T1_FOUNDATION_DOWNSTREAM_POST_PUBLIC_EXPORT_LANE_SELECTION_DECISION_2026-06-28.md` | `Reopen Conditions` | `Reopen Conditions` | DSD-T1 baseline | VALUE_SET | ACCEPT |
| T7 ledger owns downstream lane IDs and gate lists | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` | `downstreamReopenGates` | `downstreamReopenGates` | T7 ledger schema | EXISTS | ACCEPT |
| value-parked standard blocks re-proposal before checking recorded condition | `docs/reference/CVF_VALUE_PARKED_LANE_REOPEN_DISCIPLINE_STANDARD_2026-06-25.md` | `Required Action Before Re-Proposing` | `Required Action Before Re-Proposing` | value-parked lane reopen discipline standard | LITERAL_INVARIANT | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0006

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | active front door, active handoff, PRG-T0 roadmap, DSD-T1 baseline, T7 ledger, value-parked standard |
| Runtime behavior claimed | N/A_WITH_REASON: no runtime, route, CLI/MCP, adapter, provider, public, or MPI-T6 behavior is changed |
| Live/provider proof claimed | N/A_WITH_REASON: no live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized or performed |
| Freshness disposition | PASS - current source evidence supports inventory only |

## Inventory Output

| Output | Path | Status |
|---|---|---|
| parked reopen condition source inventory | `docs/reference/CVF_FPC_PRG_T1_PARKED_REOPEN_CONDITION_SOURCE_INVENTORY_2026-06-28.json` | ACTIVE_REFERENCE |

## Lane Inventory Matrix

| Lane | Condition owner | Gate-list owner | Evidence fields disposition | Status |
|---|---|---|---|---|
| `MPI-T6-runtime` | DSD-T1 baseline and MPI-T6 decision packet | T7 ledger | inventoried in JSON | PARKED |
| `runtime-provider-live` | DSD-T1 baseline and live-run diagnostic standard | T7 ledger | inventoried in JSON | PARKED |
| `use-case-adapter-public` | DSD-T1 baseline and UAP-T2 completion | T7 ledger | inventoried in JSON | PARKED |

## Acceptance Criteria

| ID | Criterion | Disposition |
|---|---|---|
| AC1 | inventory contains all three parked lane IDs from T7 | PASS |
| AC2 | each lane records condition text from DSD-T1 | PASS |
| AC3 | each lane records owning artifacts and evidence fields | PASS |
| AC4 | each lane records required conditions and forbidden lists from T7 | PASS |
| AC5 | no checker or hook wiring is implemented in T1 | PASS |
| AC6 | next tranche is T2 checker implementation only after inventory exists | PASS |

## Evidence / Verification

| Evidence item | Command or artifact | Required result |
|---|---|---|
| inventory JSON parse | `python -m json.tool docs/reference/CVF_FPC_PRG_T1_PARKED_REOPEN_CONDITION_SOURCE_INVENTORY_2026-06-28.json` | PASS |
| T7 checker | `python governance/compat/check_fpc_system_chain_acceptance_ledger.py --enforce` | PASS |
| ADIF resolver import | inline resolver call for taskClass, role, lifecyclePhase | ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0006 |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | `docs/roadmaps/CVF_FPC_PRG_T0_PARKED_REOPEN_GATE_SYSTEMIZATION_ROADMAP_2026-06-28.md` | T1 sequence row | PASS |
| Work order status | N/A with reason: direct single-agent inventory tranche | N/A with reason | N/A with reason |
| Completion or reviewer artifact | `docs/reviews/CVF_FPC_PRG_T1_PARKED_REOPEN_CONDITION_SOURCE_INVENTORY_COMPLETION_2026-06-28.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Inventory JSON | `docs/reference/CVF_FPC_PRG_T1_PARKED_REOPEN_CONDITION_SOURCE_INVENTORY_2026-06-28.json` | JSON parse PASS | PASS |
| Registry JSON | BLOCKED with reason: no registry JSON mutation is authorized | no registry path changed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown mutation is authorized | no registry path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence digest is consumed | no external source promoted | N/A with reason |
| System loop interlock | `governance/compat/check_fpc_system_chain_acceptance_ledger.py` | T7 checker remains PASS | PASS |
| Checker implementation | BLOCKED with reason: checker implementation is T2 after T1 inventory | no checker path changed | BLOCKED with reason |
| Public sync | N/A with reason: no public-sync is authorized | no public paths changed | N/A with reason |
| Runtime/live proof | N/A with reason: no runtime/provider governance behavior is claimed | no live run required | N/A with reason |
| Session continuity | N/A with reason: T5 owns session/front-door sync after T2-T4 complete | no generated session state change | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance source inventory for internal parked-lane governance.
No public artifact is authorized by T1.

## Claim Boundary

FPC-PRG-T1 creates only a source inventory for parked reopen conditions. It does
not authorize or claim checker enforcement, hook wiring, runtime execution,
provider behavior, live proof, public-sync, adapter behavior, package activation,
certification, generated-state mutation, push, or MPI-T6 runtime work.
