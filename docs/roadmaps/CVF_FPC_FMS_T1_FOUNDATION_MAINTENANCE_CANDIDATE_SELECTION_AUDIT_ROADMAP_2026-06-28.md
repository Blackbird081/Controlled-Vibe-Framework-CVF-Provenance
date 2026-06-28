# CVF FPC-FMS-T1 Foundation Maintenance Candidate Selection Audit Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_READY_FOR_FPC_T2_C05_GC018_AUTHORING

docType: roadmap

Date: 2026-06-28

Owner: Codex

rawMemoryReleased: false

## Authorization / Decision

User instruction approved continuing to the next foundation maintenance step
after FMS-T0 created the selection lane.

Decision: `SELECT_FPC_T2_C05_REGISTRY_ENTRY_GC018`.

Selected implementation lane: none.

Recommended next tranche:

`FPC-T2-C05 Registry Entry GC-018`

## Purpose

Execute the FMS-T1 candidate selection audit at roadmap level and choose the
next foundation maintenance dispatch candidate.

This roadmap selects a follow-on GC-018 authoring target only. It does not
implement the selected candidate, edit the system-loop registry, edit a checker,
or reopen downstream runtime/provider/public/MPI implementation lanes.

## Scope / Target / Owner Boundary

In scope:

- evaluate every FMS-T0 candidate row;
- compare each candidate condition with current source-backed evidence;
- select exactly one routing outcome from FMS-T0;
- name the follow-on GC-018 title and forbidden scope;
- preserve downstream parked-lane and no-implementation boundaries.

Out of scope:

- authoring the selected GC-018 or work order inside FMS-T1;
- editing `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json`;
- editing governance checkers, generated state, or runtime source;
- runtime/provider/live proof;
- public-sync mutation;
- Policy_Local implementation;
- Document Translator implementation;
- MPI-T6 runtime work;
- adapter, resolver, package, or certification work;
- push from the provenance workspace.

## Non-Goals

This roadmap does not:

- close FPC-T2-C05;
- create a registry entry;
- alter the system-loop interlock registry;
- prove runtime, provider, live, adapter, package, certification, public-sync, or
  MPI behavior;
- replace the later GC-018 source-verification duty.

## Source Authority

| Source | Role | Verification status |
|---|---|---|
| `CVF_SESSION_MEMORY.md` | active front-door startup and next-move boundary | SOURCE_VERIFIED |
| `AGENT_HANDOFF_V25_2026-06-28.md` | active handoff and parked-lane boundary | SOURCE_VERIFIED |
| `docs/roadmaps/CVF_FPC_FMS_T0_FOUNDATION_MAINTENANCE_SELECTION_AND_SYSTEM_CHAIN_REFRESH_ROADMAP_2026-06-28.md` | FMS-T1 candidate list and selection rules | SOURCE_VERIFIED |
| `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | foundation roadmap status, C01 result, and viable next candidates | SOURCE_VERIFIED |
| `docs/roadmaps/CVF_FPC_DLR_T1_DOWNSTREAM_REOPEN_EVIDENCE_AUDIT_AND_LANE_SELECTION_DECISION_ROADMAP_2026-06-28.md` | downstream no-implementation audit boundary | SOURCE_VERIFIED |
| `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | current interlock registry surface and checker pointer | SOURCE_VERIFIED |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Verification type | Disposition |
|---|---|---|---|---|---|---|
| Active next move requires fresh source-verified selection and parked-reopen checks before material implementation | `CVF_SESSION_MEMORY.md` | lines 32-34 and 120-124 | `Startup acknowledged` | active-session front door | VALUE_SET | ACCEPT |
| Active handoff keeps runtime/provider-live, adapter implementation, package activation, public-sync expansion, and MPI-T6 runtime parked until a recorded condition is verified | `AGENT_HANDOFF_V25_2026-06-28.md` | lines 7-9 and 135-145 | `Startup acknowledged` | active handoff | VALUE_SET | ACCEPT |
| FMS-T0 requires FMS-T1 to choose exactly one listed routing outcome | `docs/roadmaps/CVF_FPC_FMS_T0_FOUNDATION_MAINTENANCE_SELECTION_AND_SYSTEM_CHAIN_REFRESH_ROADMAP_2026-06-28.md` | lines 39-47 and 182-189 | `FPC-FMS-T1 Foundation Maintenance Candidate Selection Audit` | FMS-T0 roadmap | VALUE_SET | ACCEPT |
| FMS-T0 candidate matrix names `FPC-T2-C05 registry-entry work order` and requires source-backed gap evidence after C01 exists | `docs/roadmaps/CVF_FPC_FMS_T0_FOUNDATION_MAINTENANCE_SELECTION_AND_SYSTEM_CHAIN_REFRESH_ROADMAP_2026-06-28.md` | lines 137-146 | `FPC-T2-C05 registry-entry work order` | FMS-T0 candidate matrix | VALUE_SET | ACCEPT |
| Foundation roadmap status is `FPC_T3_C04_C01_CLOSED_PASS_BOUNDED` | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | lines 1-5 | `Status` | foundation roadmap | VALUE_SET | ACCEPT |
| C01 exists as an epistemic process packet checker and reviewer-fast now includes that gate | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | lines 512-522 | `governance/compat/check_epistemic_process_packet.py` | FPC-T3-C04+C01 closure result | VALUE_SET | ACCEPT |
| The C04/C01 closure made no registry edit and no FPC-T2-C05 entry | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | lines 524-527 | `FPC-T2-C05 entry` | FPC-T3-C04+C01 closure boundary | VALUE_SET | ACCEPT |
| Foundation roadmap lists opening an FPC-T2-C05 registry-entry work order as a viable next candidate now that C01 exists | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | lines 534-539 | `FPC-T2-C05 registry-entry work order` | foundation roadmap next candidates | VALUE_SET | ACCEPT |
| FPC-T4 remains available only after explicit operator decision | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | lines 534-539 and 625-635 | `FPC-T4` | foundation roadmap future control action | VALUE_SET | ACCEPT |
| DLR-T1 remains an audit-definition roadmap and selects no downstream implementation lane | `docs/roadmaps/CVF_FPC_DLR_T1_DOWNSTREAM_REOPEN_EVIDENCE_AUDIT_AND_LANE_SELECTION_DECISION_ROADMAP_2026-06-28.md` | lines 28-36 and 55-70 | `Selected implementation lane` | DLR-T1 roadmap boundary | VALUE_SET | ACCEPT |
| System-loop registry has current standard, checker, lastUpdated, and connection array fields | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | lines 1-6 | `connections` | system-loop interlock registry | VALUE_SET | ACCEPT |

## Current Gate Readout

| Gate | Command | Result |
|---|---|---|
| Parked reopen inventory | `python governance/compat/check_fpc_parked_reopen_inventory.py --base a62cd5f7 --head HEAD --enforce` | Required before commit |
| System-loop interlock registry | `python governance/compat/check_system_loop_interlock.py --base a62cd5f7 --head HEAD --enforce` | Required before commit |

## Candidate Selection Matrix

| Candidate | conditionMet | Source-backed evidence | Missing evidence | Risk | Value | recommendedDisposition |
|---|---|---|---|---|---|---|
| `FPC-T2-C05 registry-entry work order` | YES | Foundation roadmap states C01 exists, states no FPC-T2-C05 entry was made, and lists this work order as viable now that C01 exists. | Exact registry-entry content and owner paths must be source-verified in the later GC-018. | Medium: registry mutation must not occur from this roadmap. | High: turns the completed C01 checker into discoverable system-loop governance without reopening downstream use cases. | `SELECT_FOR_FRESH_GC018` |
| `FPC-T2 C01-C04 registry-edit work order` | PARTIAL | Foundation roadmap lists it as viable, but FMS-T1 evidence is narrower for C05 because C01 exists and the missing C05 entry is explicit. | Specific C01-C04 registry-edit requirement and mutation plan are not yet separated from the C05 entry question. | Medium: broader registry edit could overreach this selector. | Medium: useful after C05 scope is source-verified. | `HOLD_BEHIND_C05_GC018` |
| `FPC-T4` | NO | Foundation roadmap allows FPC-T4 only after explicit operator decision. | No explicit operator decision to bypass FPC-T2 candidate selection. | High: would skip the recorded interlock-decision dependency. | Unknown until FPC-T2 evidence is resolved. | `BLOCKED_UNTIL_EXPLICIT_OPERATOR_DECISION` |
| `HOLD foundation maintenance pending DLR-T1` | NO | DLR-T1 remains a downstream audit-definition roadmap, and the operator approved continuing the foundation maintenance next step. | No source-backed reason that DLR-T1 must close before this no-implementation FMS selector. | Low: holding would preserve safety but delay foundation closure. | Low for current objective because this roadmap can select a no-implementation GC-018 target. | `NOT_SELECTED` |

## Selected Routing Outcome

Selected routing outcome:

`OPEN_FPC_T2_C05_REGISTRY_ENTRY_GC018`.

Follow-on GC-018 title:

`CVF GC-018 FPC-T2-C05 System-Loop Registry Entry Decision And Work Order`.

Forbidden follow-on scope unless that later GC-018 explicitly authorizes it:

- runtime/provider/live proof;
- public-sync mutation;
- downstream use-case implementation;
- MPI-T6 runtime work;
- package activation or certification;
- broad registry rewrite beyond the source-verified C05 entry;
- generated active-session or workspace-state mutation outside session-sync;
- push from the provenance workspace.

## Design Control Gate

Accepted design:

- select C05 only as a later GC-018 authoring target;
- keep the selected next step inside foundation maintenance;
- require fresh source verification before any registry mutation;
- hold broader C01-C04 registry-edit work behind the C05 decision;
- keep FPC-T4 blocked without explicit operator decision;
- keep downstream lanes in audit/hold posture.

Rejected design:

- editing the registry directly from FMS-T1;
- treating C01 existence as automatic mutation authority;
- opening FPC-T4 without explicit operator decision;
- treating DLR-T1 as downstream implementation authorization;
- reopening Policy_Local, Document Translator, runtime/provider/live, public-sync,
  or MPI runtime work from this selector.

## Roadmap-To-Work-Order Trace Matrix

| FMS-T0 requirement | FMS-T1 response | Follow-on owner |
|---|---|---|
| Re-run parked reopen inventory gate | Required before FMS-T1 commit | FMS-T1 closer |
| Re-run system-loop interlock gate | Required before FMS-T1 commit | FMS-T1 closer |
| Source-verify front door, handoff, DLR-T1, foundation roadmap, and registry | Completed in Source Verification Block | FMS-T1 roadmap |
| Evaluate every candidate in the Candidate Selection Matrix | Completed in Candidate Selection Matrix | FMS-T1 roadmap |
| Select exactly one routing outcome | `OPEN_FPC_T2_C05_REGISTRY_ENTRY_GC018` | FMS-T1 roadmap |
| Name follow-on GC-018 title and forbidden scope | Completed in Selected Routing Outcome | Future FPC-T2-C05 GC-018 |

## Work Plan

The next tranche should author the FPC-T2-C05 GC-018 only. It should not
implement a registry entry until that GC-018 and any source-verified work order
pass their dispatch gates.

Required next steps:

1. Capture a fresh `dispatchBaseHead`.
2. Read the active front door, active state, active handoff, this roadmap, FMS-T0,
   the foundation roadmap, and the system-loop registry standard/checker.
3. Source-verify the exact registry owner path and schema fields for any
   proposed C05 entry.
4. Author the FPC-T2-C05 GC-018 with Source Verification Block, dependency
   release evidence, Roadmap-to-Work-Order Trace Matrix, Public Export
   Disposition, and Claim Boundary.
5. Keep the GC-018 in dispatch-only posture unless its gates pass.

## Acceptance Criteria

| ID | Criterion | Required result |
|---|---|---|
| AC1 | Parked reopen inventory gate runs on current FMS-T1 range | PASS before commit |
| AC2 | System-loop interlock gate runs on current FMS-T1 range | PASS before commit |
| AC3 | Every FMS-T0 candidate row is evaluated | PASS |
| AC4 | Candidate selection is source-backed by current roadmap and registry evidence | PASS |
| AC5 | Exactly one routing outcome is selected | PASS |
| AC6 | Follow-on GC-018 title and forbidden scope are named | PASS |
| AC7 | No implementation, live proof, public-sync, adapter, package, registry, checker, or generated-state mutation occurs | PASS |

## Verification / Evidence

| Evidence item | Command or artifact | Required result |
|---|---|---|
| Parked reopen inventory gate | `python governance/compat/check_fpc_parked_reopen_inventory.py --base a62cd5f7 --head HEAD --enforce` | PASS before commit |
| System-loop interlock gate | `python governance/compat/check_system_loop_interlock.py --base a62cd5f7 --head HEAD --enforce` | PASS before commit |
| Roadmap structural gate | `python governance/compat/check_markdown_structural_completeness.py --base a62cd5f7 --head HEAD --enforce` | PASS before commit |
| Dispatch-quality gate | `python governance/compat/check_work_order_dispatch_quality.py --base a62cd5f7 --head HEAD --enforce` | PASS before commit |
| Pre-implementation autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base a62cd5f7 --head HEAD --serial` | PASS before commit |
| Diff hygiene | `git diff --check` | PASS before commit |

## Fail Conditions

FMS-T1 must fail or block if:

- fewer than all FMS-T0 candidate rows are evaluated;
- more than one routing outcome is selected;
- C05 is selected without source-backed evidence that C01 exists and the C05
  entry remains undone;
- FPC-T4 is selected without explicit operator decision;
- downstream implementation, live proof, public-sync, package activation, or
  MPI-T6 runtime work is reopened;
- registry, checker, runtime, or generated-state files are edited from this
  roadmap-only tranche;
- any required gate fails and the assigned role does not repair the
  allowed-scope defect before continuing.

## Roadmap-To-Work-Order Expectations

Any FPC-T2-C05 GC-018 or work order must include:

- Source Verification Block;
- ADIF Defect Registry Disclosure if the artifact is dispatch-equivalent;
- Agent Handoff Contract Control Block if agent handoff semantics are used;
- Roadmap-to-Work-Order Trace Matrix;
- dependency release evidence from FMS-T0, this FMS-T1 selector, and the current
  foundation system roadmap;
- exact registry owner path and schema fields;
- explicit forbidden scope for runtime/provider/live proof, public-sync,
  downstream implementation, MPI runtime, package activation, certification,
  and broad registry rewrite;
- Public Export Disposition;
- Claim Boundary.

## Epistemic Process Block

Epistemic Process Applicability: EPISTEMIC_PROCESS_APPLIED.

Expected Result / Prediction: FMS-T1 should select `FPC-T2-C05` only if current
foundation evidence shows C01 exists and the C05 registry-entry step remains
undone; otherwise FMS-T1 should hold or request operator evidence.

Evidence Comparison: current source evidence shows C01 exists, reviewer-fast
includes the C01 gate, the prior closure made no FPC-T2-C05 entry, and the
foundation roadmap lists the C05 registry-entry work order as viable now that
C01 exists.

Contradiction Or Gap Disposition: the evidence does not authorize direct
registry mutation from this roadmap. The gap is routed to a later fresh GC-018
with source verification and forbidden scope.

Claim Update: FMS-T1 updates the next foundation maintenance recommendation
from open candidate selection to `OPEN_FPC_T2_C05_REGISTRY_ENTRY_GC018`.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance roadmap. It does not create a public-sync
artifact, public repository commit, catalog claim, or export-ready public
surface.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | active front door; active handoff; FMS-T0 roadmap; DLR-T1 roadmap; foundation system roadmap; system-loop interlock registry |
| Runtime behavior claimed | N/A_WITH_REASON: no runtime, route, CLI/MCP, adapter, provider, public, or MPI-T6 behavior is changed |
| Live/provider proof claimed | N/A_WITH_REASON: no live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized or performed |
| Freshness disposition | PASS: this roadmap selects a later GC-018 target only and records no implementation authorization |

## Machine Closure Package

This roadmap is not closed; it is ready for FPC-T2-C05 GC-018 authoring.

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | this file | `Status: ROADMAP_READY_FOR_FPC_T2_C05_GC018_AUTHORING` | PASS |
| Work order status | N/A with reason: this roadmap does not create a work order | no work order path created | N/A with reason |
| Completion or reviewer artifact | N/A with reason: this roadmap is a selector for later GC-018 authoring | no completion review required yet | N/A with reason |
| Registry JSON | BLOCKED with reason: no registry JSON mutation is authorized | no registry path changed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown mutation is authorized | no registry Markdown path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: no external artifact, source bundle, or live proof is consumed | no digest artifact required | N/A with reason |
| System loop interlock | `governance/compat/check_system_loop_interlock.py` | system-loop interlock gate PASS before commit | PASS |
| Runtime/live proof | N/A with reason: no runtime/provider governance behavior is claimed | no live run required | N/A with reason |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |

## Claim Boundary

This roadmap selects a later FPC-T2-C05 GC-018 authoring target only. It does
not authorize or perform registry mutation, checker mutation, runtime/provider
work, live proof, public-sync, downstream implementation, package activation,
certification, generated-state mutation, MPI-T6 runtime work, or push from the
provenance workspace.
