# CVF FPC-FMS-T0 Foundation Maintenance Selection And System-Chain Refresh Roadmap

Memory class: FULL_RECORD

Status: ROADMAP_READY_FOR_FMS_T1_SELECTION_AUDIT

docType: roadmap

Date: 2026-06-28

Owner: Codex

rawMemoryReleased: false

## Authorization / Decision

User instruction approved the proposed foundation maintenance selection roadmap
after DLR-T1 established the downstream reopen evidence-audit path.

Decision: `OPEN_FOUNDATION_MAINTENANCE_SELECTION_BEFORE_DOWNSTREAM_REOPEN`.

Selected implementation lane: none.

Recommended next tranche:

`FPC-FMS-T1 Foundation Maintenance Candidate Selection Audit`

## Purpose

Refresh the foundation maintenance decision surface after parked-reopen
discipline and downstream reopen audit planning.

The current foundation roadmap is no longer merely parked. It records
FPC-T1/T2/T3 progress, a closed FPC-T3 C04/C01 status, and viable next
foundation candidates. This roadmap creates a narrow selection lane to decide
which foundation maintenance candidate should be opened next, without
reopening downstream runtime/provider/public/MPI implementation lanes.

FMS-T1 should source-verify the current foundation roadmap, current session
next-move boundary, system-loop interlock registry, and DLR-T1 no-implementation
boundary, then return exactly one of:

- `OPEN_FPC_T2_C05_REGISTRY_ENTRY_GC018`;
- `OPEN_FPC_T2_C01_C04_REGISTRY_EDIT_GC018`;
- `HOLD_FOUNDATION_MAINTENANCE_PENDING_DLR_T1`;
- `REQUEST_OPERATOR_PRODUCT_REQUIREMENT_EVIDENCE`;
- `OPEN_FPC_T4_ONLY_AFTER_EXPLICIT_OPERATOR_DECISION`.

## Scope / Target / Owner Boundary

In scope:

- record the FMS-T0 roadmap;
- source-verify current foundation roadmap status and candidate list;
- source-verify that DLR-T1 has not selected an implementation lane;
- define a T1 selection audit for foundation maintenance candidates;
- preserve downstream parked-lane and no-implementation boundaries.

Out of scope:

- executing FMS-T1;
- authoring an FMS-T1 GC-018 or work order;
- selecting or implementing an FPC-T2/FPC-T4 candidate inside this roadmap;
- editing the system-loop interlock registry;
- runtime/provider/live proof;
- public-sync mutation;
- Policy_Local implementation;
- Document Translator implementation;
- MPI-T6 runtime work;
- adapter, resolver, package, certification, checker, registry, or generated
  state mutation;
- push from the provenance workspace.

## Non-Goals

This roadmap does not:

- reopen any downstream implementation lane;
- claim FPC-T2 C05, FPC-T2 C01-C04, or FPC-T4 is currently selected;
- run live/provider proof;
- edit public-sync content;
- create a runtime, MCP, CLI, IDE, adapter, package, certification, registry,
  checker, or generated-state change;
- treat provider-specific memory as CVF source authority.

## Source Authority

| Source | Path | Role |
|---|---|---|
| Active session front door | `CVF_SESSION_MEMORY.md` | current next allowed move and parked checkpoint |
| DLR-T1 roadmap | `docs/roadmaps/CVF_FPC_DLR_T1_DOWNSTREAM_REOPEN_EVIDENCE_AUDIT_AND_LANE_SELECTION_DECISION_ROADMAP_2026-06-28.md` | downstream audit/no-implementation boundary |
| Foundation system roadmap | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | current foundation maintenance status and candidate list |
| System-loop interlock registry | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | current interlock registry surface and checker pointer |

No provider-specific memory file, chat-only fact, API key, external app tree, or
public browser state is source authority for this roadmap.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Active next move allows only fresh source-verified roadmap or tranche selection after the parked reopen inventory gate | `CVF_SESSION_MEMORY.md` | lines 104-112 | `Next Allowed Move` | active session front door | VALUE_SET | ACCEPT |
| Active checkpoint keeps downstream runtime/provider/public/MPI lanes parked without separate authorization | `CVF_SESSION_MEMORY.md` | lines 114-124 | `Parked Checkpoint` | active session front door | VALUE_SET | ACCEPT |
| DLR-T1 does not execute the audit, select implementation, or authorize downstream implementation GC-018 | `docs/roadmaps/CVF_FPC_DLR_T1_DOWNSTREAM_REOPEN_EVIDENCE_AUDIT_AND_LANE_SELECTION_DECISION_ROADMAP_2026-06-28.md` | lines 28-36 | `Purpose` | DLR-T1 roadmap | VALUE_SET | ACCEPT |
| DLR-T1 expected outcomes include opening foundation maintenance instead of downstream implementation | `docs/roadmaps/CVF_FPC_DLR_T1_DOWNSTREAM_REOPEN_EVIDENCE_AUDIT_AND_LANE_SELECTION_DECISION_ROADMAP_2026-06-28.md` | lines 38-43 | `OPEN_FOUNDATION_MAINTENANCE_INSTEAD` | DLR-T1 roadmap | VALUE_SET | ACCEPT |
| DLR-T1 rejected design prevents selecting a lane directly from the roadmap | `docs/roadmaps/CVF_FPC_DLR_T1_DOWNSTREAM_REOPEN_EVIDENCE_AUDIT_AND_LANE_SELECTION_DECISION_ROADMAP_2026-06-28.md` | lines 155-163 | `Rejected design` | DLR-T1 roadmap | VALUE_SET | ACCEPT |
| DLR-T1 acceptance criteria forbid implementation, live proof, public-sync, adapter, package, registry, checker, or generated-state mutation | `docs/roadmaps/CVF_FPC_DLR_T1_DOWNSTREAM_REOPEN_EVIDENCE_AUDIT_AND_LANE_SELECTION_DECISION_ROADMAP_2026-06-28.md` | lines 200-207 | `Acceptance Criteria` | DLR-T1 roadmap | VALUE_SET | ACCEPT |
| Foundation roadmap current top status is FPC_T3_C04_C01_CLOSED_PASS_BOUNDED | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | lines 1-5 | `Status` | foundation roadmap | VALUE_SET | ACCEPT |
| Foundation roadmap operator direction ranks CVF foundation quality before downstream use cases | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | lines 15-31 | `Authorization / Decision` | foundation roadmap | VALUE_SET | ACCEPT |
| Foundation roadmap purpose is completing CVF as connected workflow-chain systems | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | lines 36-55 | `Purpose` | foundation roadmap | VALUE_SET | ACCEPT |
| Foundation roadmap original design selected FPC-T1/T2/T3 before use-case execution | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | lines 198-218 | `Design Control Gate` | foundation roadmap | VALUE_SET | ACCEPT |
| Foundation roadmap current closure result records C04/C01 checker/template/hook hardening and no registry/runtime/public mutation | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | lines 503-527 | `Status` | foundation roadmap | VALUE_SET | ACCEPT |
| Foundation roadmap current viable next candidates are FPC-T2-C05, FPC-T2 C01-C04 registry edit, or FPC-T4 after operator decision | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | lines 534-539 | `Next allowed move` | foundation roadmap | VALUE_SET | ACCEPT |
| Foundation roadmap captured priority drift, interlock visibility, and machine-checked versus structural-only status as future control issues | `docs/roadmaps/CVF_FOUNDATION_PLANES_WORKFLOW_CHAIN_SYSTEM_COMPLETION_ROADMAP_2026-06-13.md` | lines 625-643 | `Foundation Issues Captured` | foundation roadmap | VALUE_SET | ACCEPT |
| System-loop interlock registry has a standard pointer, checker pointer, lastUpdated value, and connection records | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | lines 1-6 | `connections` | system-loop interlock registry | VALUE_SET | ACCEPT |

## Current Gate Readout

| Gate | Command | Result |
|---|---|---|
| Parked reopen inventory | `python governance/compat/check_fpc_parked_reopen_inventory.py --base 201e198a --head HEAD --enforce` | PASS before commit |
| System-loop interlock registry | `python governance/compat/check_system_loop_interlock.py --base 201e198a --head HEAD --enforce` | PASS before commit |

The PASS results mean the current inventories and registry are internally
aligned. They do not select a foundation maintenance implementation candidate.

## Current Runtime Freshness Verification

| Field | Disposition |
|---|---|
| Runtime/source paths checked | active front door; DLR-T1 roadmap; foundation system roadmap; system-loop interlock registry |
| Runtime behavior claimed | N/A_WITH_REASON: no runtime, route, CLI/MCP, adapter, provider, public, or MPI-T6 behavior is changed |
| Live/provider proof claimed | N/A_WITH_REASON: no live governance behavior is claimed |
| Public-sync claimed | N/A_WITH_REASON: no public-sync is authorized or performed |
| Freshness disposition | PASS: this roadmap defines a foundation maintenance selection path only and records no implementation authorization |

## Candidate Selection Matrix

FMS-T1 must fill one row per candidate.

| Candidate | Current source signal | Evidence to collect | Default stance |
|---|---|---|---|
| `FPC-T2-C05 registry-entry work order` | foundation roadmap viable next candidate | whether C05 has a source-backed registry-entry gap after C01 exists, plus exact owner paths and forbidden scope | HOLD unless the gap is source-backed |
| `FPC-T2 C01-C04 registry-edit work order` | foundation roadmap viable next candidate | whether C01-C04 needs registry edit rather than checker/template-only closure, plus registry mutation authorization plan | HOLD unless mutation need is source-backed |
| `FPC-T4` | foundation roadmap viable next candidate only after explicit operator decision | exact operator decision, dependency release from T1/T2/T3, and no bypass of FPC-T2 evidence | BLOCKED without explicit operator decision |
| `HOLD foundation maintenance pending DLR-T1` | DLR-T1 still not executed | whether downstream reopen audit must close before any foundation maintenance selection | HOLD if operator wants DLR-T1 first |

## Design Control Gate

Accepted design:

- make FMS-T0 a roadmap-only selection surface;
- evaluate foundation maintenance candidates before opening GC-018;
- preserve DLR-T1 downstream audit boundary;
- keep Policy_Local, Document Translator, runtime/provider/live work, public-sync,
  and MPI-T6 runtime parked;
- require source-backed evidence before registry/checker/generated-state edits.

Rejected design:

- selecting FPC-T2-C05, FPC-T2 C01-C04, or FPC-T4 directly from this roadmap;
- treating current foundation roadmap status as automatic registry-edit
  authorization;
- treating DLR-T1 as completed or as implementation authorization;
- treating FPC-T4 as available without explicit operator decision;
- reopening downstream use-case lanes because foundation maintenance is useful.

## Work Plan

FMS-T1 should be a decision/audit tranche, not an implementation tranche.

Required steps:

1. Capture `dispatchBaseHead`.
2. Re-run `python governance/compat/check_fpc_parked_reopen_inventory.py --base <dispatchBaseHead> --head HEAD --enforce`.
3. Re-run `python governance/compat/check_system_loop_interlock.py --base <dispatchBaseHead> --head HEAD --enforce`.
4. Source-verify the active front door, active state, active handoff, DLR-T1
   roadmap, foundation system roadmap, and system-loop interlock registry.
5. Evaluate every candidate in the Candidate Selection Matrix with
   `candidateId`, `sourceSignal`, `conditionMet`, `evidence`,
   `missingEvidence`, `risk`, `value`, and `recommendedDisposition`.
6. Select exactly one final routing outcome:
   `OPEN_FPC_T2_C05_REGISTRY_ENTRY_GC018`,
   `OPEN_FPC_T2_C01_C04_REGISTRY_EDIT_GC018`,
   `HOLD_FOUNDATION_MAINTENANCE_PENDING_DLR_T1`,
   `REQUEST_OPERATOR_PRODUCT_REQUIREMENT_EVIDENCE`, or
   `OPEN_FPC_T4_ONLY_AFTER_EXPLICIT_OPERATOR_DECISION`.
7. If a candidate is selected, name the exact follow-on GC-018 title and
   forbidden scope. Do not implement the candidate inside FMS-T1.

## Acceptance Criteria

| ID | Criterion | Required result |
|---|---|---|
| AC1 | Parked reopen inventory gate runs on current FMS-T1 range | PASS |
| AC2 | System-loop interlock gate runs on current FMS-T1 range | PASS |
| AC3 | All candidate ids in the Candidate Selection Matrix are evaluated | PASS |
| AC4 | Every candidate condition is compared with current source-backed evidence | PASS |
| AC5 | Every missing-evidence claim is explicit | PASS |
| AC6 | Exactly one routing outcome is selected | PASS |
| AC7 | Any selected candidate names a later fresh GC-018 title and forbidden scope | PASS or N/A with reason if no candidate selected |
| AC8 | No implementation, live proof, public-sync, adapter, package, registry, checker, or generated-state mutation occurs | PASS |

## Verification / Evidence

| Evidence item | Command or artifact | Required result |
|---|---|---|
| Parked reopen inventory gate | `python governance/compat/check_fpc_parked_reopen_inventory.py --base 201e198a --head HEAD --enforce` | PASS before commit |
| System-loop interlock gate | `python governance/compat/check_system_loop_interlock.py --base 201e198a --head HEAD --enforce` | PASS before commit |
| Roadmap structural gate | `python governance/compat/check_markdown_structural_completeness.py --base 201e198a --head HEAD --enforce` | PASS before commit |
| Dispatch-quality gate | `python governance/compat/check_work_order_dispatch_quality.py --base 201e198a --head HEAD --enforce` | PASS before commit |
| Pre-implementation autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 201e198a --head HEAD --serial` | PASS before commit |
| Diff hygiene | `git diff --check` | PASS before commit |

## Fail Conditions

FMS-T1 must fail or block closure if:

- fewer than all Candidate Selection Matrix rows are evaluated;
- a candidate is selected only because it is useful, without source-backed
  condition evidence;
- FPC-T4 is selected without explicit operator decision;
- registry/checker/generated-state mutation is proposed without a fresh
  source-verified GC-018;
- runtime/provider/live, public-sync, Policy_Local, Document Translator, or
  MPI-T6 work is selected;
- implementation paths are edited before the selection decision closes.

## Roadmap-To-Work-Order Expectations

Any FMS-T1 GC-018 or work order must include:

- Source Verification Block;
- ADIF Defect Registry Disclosure if the artifact is dispatch-equivalent;
- Agent Handoff Contract Control Block if agent handoff semantics are used;
- Roadmap-to-Work-Order Trace Matrix;
- dependency release evidence from DLR-T1, FPC-PRG-T1 through FPC-PRG-T5, and
  the current foundation system roadmap;
- exact candidate ids from this roadmap;
- evidence rows for condition-met and missing-evidence status;
- explicit forbidden scope for implementation, live proof, public-sync, and MPI;
- Public Export Disposition;
- Claim Boundary.

## Epistemic Process Block

Epistemic Process Applicability: EPISTEMIC_PROCESS_NA_WITH_REASON: this roadmap
defines a source-backed selection plan and does not run an empirical experiment,
provider proof, runtime test, or prediction-vs-result benchmark.

Expected Result / Prediction: FMS-T1 should select `FPC-T2-C05` or
`FPC-T2 C01-C04` only if the current foundation roadmap and registry evidence
show a concrete source-backed gap; otherwise it should hold or request operator
evidence.

Evidence Comparison Requirement: FMS-T1 must compare each candidate condition
against current source-backed evidence before any selection.

Contradiction Or Gap Disposition: if evidence contradicts a candidate
selection, FMS-T1 must hold foundation maintenance, request operator evidence,
or block implementation rather than soft-opening a GC-018.

Claim Update Requirement: FMS-T1 must state whether DLR-T1's hold-first posture
changed after source verification.

## Machine Closure Package

This roadmap is not closed; it is ready for FMS-T1 selection audit.

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Roadmap state | this file | `Status: ROADMAP_READY_FOR_FMS_T1_SELECTION_AUDIT` | PASS |
| Work order status | N/A with reason: this roadmap does not create a work order | no work order path created | N/A with reason |
| Completion or reviewer artifact | N/A with reason: this roadmap is a proposal for FMS-T1 dispatch authoring | no completion review required yet | N/A with reason |
| Registry JSON | BLOCKED with reason: no registry JSON mutation is authorized | no registry path changed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown mutation is authorized | no registry path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: no external artifact, source bundle, or live proof is consumed | no digest artifact required | N/A with reason |
| System loop interlock | `governance/compat/check_system_loop_interlock.py` | system-loop interlock gate PASS before commit | PASS |
| Runtime/live proof | N/A with reason: no runtime/provider governance behavior is claimed | no live run required | N/A with reason |
| Public export | this file | `DEFERRED_PRIVATE_ONLY` | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance roadmap for foundation maintenance selection
authoring. Public-sync mutation is explicitly out of scope.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex |
| Provider or surface | local repository tools |
| Session or invocation | 2026-06-28 FPC-FMS-T0 roadmap authoring |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, source reads, apply_patch, parked reopen inventory gate, system-loop interlock gate |
| Target paths | `docs/roadmaps/CVF_FPC_FMS_T0_FOUNDATION_MAINTENANCE_SELECTION_AND_SYSTEM_CHAIN_REFRESH_ROADMAP_2026-06-28.md` |
| Allowed scope source | user instruction approving the proposed FMS-T0 roadmap |
| Before status evidence | HEAD `201e198a`; worktree clean before roadmap patch |
| After status evidence | roadmap artifact added; no implementation paths changed |
| Diff evidence | `git diff --name-status 201e198a` |
| Approval boundary | FMS-T0 roadmap only |
| Claim boundary | no downstream implementation, runtime/provider/live proof, public-sync, MPI-T6 runtime, adapter, package, certification, registry, checker, or generated-state mutation |
| Agent type | single-agent roadmap author |
| Invocation ID | `fpc-fms-t0-foundation-maintenance-selection-roadmap-2026-06-28` |
| Expected manifest | `docs/roadmaps/CVF_FPC_FMS_T0_FOUNDATION_MAINTENANCE_SELECTION_AND_SYSTEM_CHAIN_REFRESH_ROADMAP_2026-06-28.md` |
| Actual changed set | `docs/roadmaps/CVF_FPC_FMS_T0_FOUNDATION_MAINTENANCE_SELECTION_AND_SYSTEM_CHAIN_REFRESH_ROADMAP_2026-06-28.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in this roadmap batch |

## Claim Boundary

This roadmap only defines the next FMS-T1 foundation maintenance selection
decision route. It does not authorize or claim runtime behavior,
provider/live proof, public-sync, adapter implementation, package activation,
certification, Policy_Local implementation, Document Translator implementation,
MPI-T6 runtime work, registry mutation, checker implementation,
generated-state mutation, production readiness, public readiness, or universal
governed control.
