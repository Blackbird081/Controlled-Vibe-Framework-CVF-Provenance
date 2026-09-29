# CVF FPC-PRG-T0 Parked Reopen Gate Systemization Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-28

Owner: Codex

rawMemoryReleased: false

## Authorization / Decision

The operator approved the proposal to systemize the parked-lane reopen
discipline before any downstream implementation lane is reopened.

Decision: `SYSTEMIZE_PARKED_REOPEN_GATE_BEFORE_DOWNSTREAM_IMPLEMENTATION`.

This roadmap records the next foundation-maintenance lane after DSD-T1. It
does not reopen runtime-provider-live, use-case-adapter-public,
public-sync expansion, adapter implementation, package activation, or
MPI-T6-runtime work.

## Purpose

Turn the current parked/deferred discipline into a source-verified roadmap so a
future checker tranche can reject speculative reopen attempts. The useful
movement now is not implementation; it is making the reopen-condition evidence
machine-addressable before implementation can be proposed again.

## Non-Goals

This roadmap does not:

- implement a checker;
- wire a checker into pre-dispatch, reviewer-fast, or pre-push gates;
- edit runtime, route, provider, CLI/MCP, IDE bridge, adapter, package, or
  public-sync behavior;
- run provider/live proof or consume API keys;
- reopen MPI-T6 runtime work;
- mutate generated active-session state in the material commit.

## Scope / Target / Owner Boundary

Allowed material scope:

- file this FPC-PRG-T0 roadmap;
- file the matching GC-018 baseline and completion review;
- update the FPC guidance with the PRG-T0 systemization direction;
- source-verify current reopen-condition owners;
- define the T1 through T5 roadmap sequence for a future checker lane.

Forbidden material scope:

- no downstream implementation lane selection;
- no public-sync or push from the provenance workspace;
- no runtime/MCP/CLI/IDE bridge implementation;
- no provider/live proof;
- no Policy_Local or Document Translator implementation;
- no Model Gateway or Sandbox Runtime expansion;
- no MPI-T6 runtime work;
- no adapter, resolver, package, certification, registry, checker, or generated
  workspace state mutation.

## Source Authority

| Source | Path | Role |
|---|---|---|
| Active front door | `CVF_SESSION_MEMORY.md` | current HOLD boundary and next allowed move |
| Active handoff | `AGENT_HANDOFF_V25_2026-06-28.md` | current handoff reopen conditions and parked checkpoint |
| DSD-T1 baseline | `docs/baselines/CVF_GC018_FPC_DSD_T1_FOUNDATION_DOWNSTREAM_POST_PUBLIC_EXPORT_LANE_SELECTION_DECISION_2026-06-28.md` | downstream hold decision and lane reopen conditions |
| DSD-T1 completion | `docs/reviews/CVF_FPC_DSD_T1_FOUNDATION_DOWNSTREAM_POST_PUBLIC_EXPORT_LANE_SELECTION_DECISION_COMPLETION_2026-06-28.md` | reviewer acceptance of HOLD decision |
| T7 ledger | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` | current downstream reopen gates |
| T7 checker | `governance/compat/check_fpc_system_chain_acceptance_ledger.py` | existing machine coverage for gate shape and PARKED status |
| Value-parked standard | `docs/reference/CVF_VALUE_PARKED_LANE_REOPEN_DISCIPLINE_STANDARD_2026-06-25.md` | rule that a value-parked lane must not be re-proposed without checking recorded condition |

Provider-specific memory, browser state, local API keys, and chat-only facts are
not CVF source authority for this roadmap.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| current next move permits foundation maintenance only when source evidence supports it | `CVF_SESSION_MEMORY.md` | line 102 | `Next Allowed Move` | active session front door | VALUE_SET | ACCEPT |
| active handoff records concrete downstream reopen conditions | `AGENT_HANDOFF_V25_2026-06-28.md` | lines 88-104 | `Next Allowed Move` | active handoff | VALUE_SET | ACCEPT |
| value-parked standard blocks re-proposal before checking recorded condition | `docs/reference/CVF_VALUE_PARKED_LANE_REOPEN_DISCIPLINE_STANDARD_2026-06-25.md` | `Required Action Before Re-Proposing` | `Required Action Before Re-Proposing` | value-parked lane reopen discipline standard | LITERAL_INVARIANT | ACCEPT |
| T7 ledger owns downstream reopen gate records | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` | line 88 | `downstreamReopenGates` | T7 acceptance ledger schema | EXISTS | ACCEPT |
| T7 ledger keeps downstream lanes parked | `docs/reference/CVF_FPC_SCG_T7_FOUNDATION_SYSTEM_CHAIN_ACCEPTANCE_LEDGER_2026-06-27.json` | lines 91, 107, 124 | `gateStatus` | T7 acceptance ledger schema | VALUE_SET | ACCEPT |
| T7 checker already validates required gate fields and PARKED status | `governance/compat/check_fpc_system_chain_acceptance_ledger.py` | lines 48-52 and 249-250 | `REQUIRED_GATE_FIELDS`; `gateStatus` | T7 checker | RUNTIME_BEHAVIOR | ACCEPT |
| DSD-T1 baseline records `HOLD_DOWNSTREAM_IMPLEMENTATION` | `docs/baselines/CVF_GC018_FPC_DSD_T1_FOUNDATION_DOWNSTREAM_POST_PUBLIC_EXPORT_LANE_SELECTION_DECISION_2026-06-28.md` | lines 19 and 49 | `HOLD_DOWNSTREAM_IMPLEMENTATION` | DSD-T1 baseline | VALUE_SET | ACCEPT |
| DSD-T1 baseline records lane-specific reopen conditions | `docs/baselines/CVF_GC018_FPC_DSD_T1_FOUNDATION_DOWNSTREAM_POST_PUBLIC_EXPORT_LANE_SELECTION_DECISION_2026-06-28.md` | lines 122-128 | `Reopen Conditions` | DSD-T1 baseline | VALUE_SET | ACCEPT |
| DSD-T1 completion accepts the HOLD decision | `docs/reviews/CVF_FPC_DSD_T1_FOUNDATION_DOWNSTREAM_POST_PUBLIC_EXPORT_LANE_SELECTION_DECISION_COMPLETION_2026-06-28.md` | lines 46-48 | `Review Decision` | DSD-T1 completion review | VALUE_SET | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0006

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | active front door, active handoff, DSD-T1 baseline, DSD-T1 completion, T7 ledger, T7 checker, value-parked standard |
| Runtime behavior claimed | N/A_WITH_REASON: this roadmap changes no runtime, route, CLI/MCP, adapter, provider, public, or MPI-T6 behavior |
| Live/provider proof claimed | N/A_WITH_REASON: no live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized or performed |
| Freshness disposition | PASS - current source evidence supports a foundation-maintenance roadmap, not downstream implementation |

## Roadmap Sequence

| Tranche | Purpose | Output | Boundary |
|---|---|---|---|
| FPC-PRG-T0 | roadmap and baseline decision | this roadmap, GC-018, completion, guidance update | no checker implementation |
| FPC-PRG-T1 | reopen-condition source inventory | JSON or markdown inventory of condition owners and lane IDs | no enforcement change |
| FPC-PRG-T2 | parked reopen gate checker | focused checker plus tests for missing or invalid reopen evidence | no runtime/provider/live behavior |
| FPC-PRG-T3 | gate wiring decision | autorun or reviewer-fast integration if source-verified | no broad hook expansion |
| FPC-PRG-T4 | fixture coverage | valid reopen, missing evidence, wrong lane, and stale condition fixtures | no downstream lane reopen |
| FPC-PRG-T5 | session/front-door sync | nextAllowedMove records checker availability and reopen workflow | no implementation lane selection |

## Work Plan

| Step | Output | Stop condition |
|---|---|---|
| Verify current HOLD boundary | source verification against active state, handoff, DSD-T1, and T7 | any downstream implementation condition is already satisfied |
| Define systemization sequence | PRG-T0 through PRG-T5 roadmap rows | sequence skips source inventory before checker work |
| Record next tranche | T1 inventory recommendation | recommendation opens checker implementation or runtime work |
| Update guidance | FPC guidance records PRG-T0 direction | guidance authorizes public-sync or downstream implementation |

## Recommended Next Tranche

Recommended next work order:

`FPC-PRG-T1 Parked Reopen Condition Source Inventory`

T1 should source-verify the exact lane IDs, condition text, owning artifacts,
and evidence fields that T2 will later consume. T1 must not implement the
checker or wire any gate.

## Design Control Gate

| Design control | Handling | Verdict |
|---|---|---|
| Source authority | CVF-governed surfaces only | PASS |
| Downstream restraint | all downstream implementation lanes remain held | PASS |
| Checker boundary | checker is deferred to T2 after T1 inventory | PASS |
| Public/provenance boundary | no public-sync in T0 | PASS |
| Live proof boundary | no runtime/provider claim in T0 | PASS |
| Acceptance criteria | AC1 through AC6 below | PASS |

## Verification / Evidence

| Evidence item | Command or artifact | Required result |
|---|---|---|
| T7 checker | `python governance/compat/check_fpc_system_chain_acceptance_ledger.py --enforce` | PASS |
| ADIF resolver | inline resolver call for taskClass, role, lifecyclePhase | ADIF-0001, ADIF-0002, ADIF-0007, ADIF-0006 |
| Structural/gate checks | governance gates over base `c6248014` and `HEAD` | PASS before commit |

## Acceptance Criteria

| ID | Criterion | Disposition |
|---|---|---|
| AC1 | PRG-T0 records a foundation-maintenance roadmap, not downstream implementation | PASS |
| AC2 | reopen-condition owners are source-verified | PASS |
| AC3 | T1 through T5 sequence separates inventory, checker, wiring, fixtures, and sync | PASS |
| AC4 | public-sync, runtime/provider/live, adapter, package, and MPI-T6 remain out of scope | PASS |
| AC5 | next recommended tranche is T1 inventory, not checker or implementation | PASS |
| AC6 | T7 checker remains PASS on current HEAD | PASS |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order disposition | Status |
|---|---|---|
| Define parked reopen gate systemization lane | N/A with reason: T0 is a decision roadmap and has no implementation work order | PASS |
| Preserve downstream HOLD boundary | N/A with reason: no implementation work is assigned | PASS |
| Prepare next actionable tranche | T1 work order will be fresh-authored after T0 closure | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_FPC_PRG_T0_PARKED_REOPEN_GATE_SYSTEMIZATION_ROADMAP_2026-06-28.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | N/A with reason: T0 is decision-only and assigns no worker | N/A with reason | N/A with reason |
| Completion or reviewer artifact | `docs/reviews/CVF_FPC_PRG_T0_PARKED_REOPEN_GATE_SYSTEMIZATION_ROADMAP_COMPLETION_2026-06-28.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Guidance update | `docs/reference/CVF_FOUNDATION_PLANE_SYSTEM_CHAIN_GAP_PRIORITY_GUIDANCE_2026-06-27.md` | PRG-T0 direction recorded | PASS |
| Registry JSON | BLOCKED with reason: no registry JSON mutation is authorized | no registry path changed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown mutation is authorized | no registry path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: no external evidence digest is consumed | no external source promoted | N/A with reason |
| System loop interlock | `governance/compat/check_fpc_system_chain_acceptance_ledger.py` | T7 checker remains PASS | PASS |
| Checker implementation | BLOCKED with reason: checker implementation is T2 after T1 inventory | no checker path changed | BLOCKED with reason |
| Public sync | N/A with reason: no public-sync is authorized | no public paths changed | N/A with reason |
| Runtime/live proof | N/A with reason: no runtime/provider governance behavior is claimed | no live run required | N/A with reason |
| Session continuity | active session sync | pending separate session-sync after material commit | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance foundation-maintenance roadmap. The public-sync
boundary remains closed for this tranche; it cites internal tranche IDs, active
state, and parked-lane boundaries.

## Claim Boundary

This roadmap records PRG-T0 as a bounded foundation-maintenance decision. It
does not authorize or claim public-sync, runtime execution, live/provider
proof, adapter behavior, certification, package activation, generated-state
mutation, push, or MPI-T6 runtime work.
