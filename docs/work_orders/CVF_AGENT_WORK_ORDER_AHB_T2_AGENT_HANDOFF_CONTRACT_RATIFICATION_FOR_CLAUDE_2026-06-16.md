# CVF Agent Work Order - AHB-T2 Agent Handoff Contract Ratification

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-16

Batch ID: AHB-T2

Owner: Claude worker (contract author); Codex reviewer/closer

rawMemoryReleased: false

dispatchBaseHead: 88111c19

executionBaseHead: 88111c19

closureBaseHead: 88111c19

EPISTEMIC_PROCESS_NA_WITH_REASON: This is a governance contract-ratification
packet. No model behavior prediction is required. All source facts must be
verified against governed artifacts.

## Dispatch Prompt Envelope

Role: Claude contract author; Codex reviewer/closer

Canonical packet: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: `88111c19`

Current-time notes: 2026-06-16; AHB-T1 and AHB-T1A are closed; AOT-T3 is
closed at material commit `08659a5d` and is now a clean input to AHB-T2.

Do-not-misread notes: this work order dispatches contract ratification
authoring only. Do not implement checkers, wire gates, edit runtime/source/test
files, edit registries, build the workspace, run providers/live proof,
public-sync, or claim production/public readiness. AOT-T3 is not pending; treat
it as a closed input.

Required first actions: read the Required First Reads table; run the Pre-Flight
Checks; confirm the worktree is clean at `88111c19`; author only the allowed
worker-owned files; return with HEAD unchanged.

Return contract: Claude returns the ratification packet and worker return under
WORKER_MUST_NOT_COMMIT. Codex reviews actual files, performs allowed reviewer
repairs, commits accepted material, runs closure gates, and updates session
continuity separately if the next move changes.

## Return-To-Orchestrator Conditions

Claude returns to Codex when:

- the ratification packet is authored at the required path;
- the worker return is authored at the required path;
- HEAD is unchanged from `88111c19`;
- changed paths are limited to the two Claude-owned worker outputs;
- any unresolved ratification decision is marked `DEFERRED_WITH_REASON` with a
  concrete blocker.

Worker-phase return status was expected to be complete-pending-review if all
acceptance criteria were met or boundedly deferred. Worker-phase return status
was expected to be blocked only when a required source artifact was missing, the
same-purpose contract already existed, or a required decision could not be
expressed within this work order's scope.

## Operator Checkpoint

No operator checkpoint is required during Claude authoring unless Claude finds a
same-purpose ratified contract, a missing source artifact that blocks AC1-AC7, or
an unresolved governance decision that cannot be safely marked
`DEFERRED_WITH_REASON`.

Codex will surface any unresolved `DEFERRED_WITH_REASON` decision to the
operator during review. AHB-T3 machine-check implementation and workspace design
remain separate future operator-authorized tranches.

## Purpose

Author the AHB-T2 Agent Handoff Contract ratification packet. The packet must
turn the AHB-T1 proposed model into a governed contract decision by reconciling
MA1, dispatch envelope, commit steward, AOT trace, and session-sync next-move
surfaces under one Central Core contract with Local View evidence per batch.

## Scope / Target / Owner Boundary

Target: the CVF Agent Handoff Contract decision.

Scope: one ratification packet under `docs/reference/` plus one worker return
under `docs/reviews/`.

Owner boundary: Claude authors under `WORKER_MUST_NOT_COMMIT`. Codex reviews
and closes. Claude must not commit.

Out of scope:

- checker implementation or gate wiring;
- runtime/source/test mutation;
- system-loop/interlock or provider registry edits;
- public-sync;
- provider/API/OCR/live proof;
- building or scaffolding the dedicated agent-interaction workspace;
- production/public readiness claims.

## Authority Chain

| Level | Artifact | Status |
|---|---|---|
| Operator instruction | 2026-06-16 operator authorization: proceed with AHB-T2 after AOT-T3 | ACCEPTED |
| GC-018 baseline | `docs/baselines/CVF_GC018_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | CLOSURE_SATISFIED |
| AHB roadmap | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` AHB-T2 row | CLOSURE_SATISFIED |
| AHB-T1 audit | `docs/audits/CVF_AHB_T1_HANDOFF_BOUNDARY_AUDIT_2026-06-16.md` | PREDECESSOR_SATISFIED |
| AHB-T1 Codex rebuttal | `docs/reviews/CVF_AHB_T1_HANDOFF_BOUNDARY_AUDIT_CODEX_REBUTTAL_2026-06-16.md` | PREDECESSOR_SATISFIED |
| AOT-T3 completion | `docs/reviews/CVF_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_COMPLETION_2026-06-16.md` | PREDECESSOR_SATISFIED |

## Intake Role

Claude is the contract author. Codex is the reviewer/closer.

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker Autonomy / No-Question Rule: Claude should not pause for operator
confirmation inside this bounded authoring scope. If a decision cannot be
ratified from the required sources, mark that field `DEFERRED_WITH_REASON` and
explain the blocking reason.

## Intake Role Routing Decision

Route mode: `MULTI_AGENT_MULTI_ROLE`

Intake summary: Codex dispatches AHB-T2 after operator authorization. Claude
authors the contract packet without commit. Codex reviews and closes.

Scope classification: bounded governed markdown. No runtime, checker, provider,
registry, workspace, public-sync, or live-proof work is authorized.

Risk sensitivity: low for repository runtime; high for governance semantics,
because this contract becomes the Central Core that future handoff local views
will cite.

Selected role route: `MULTI_AGENT_MULTI_ROLE` (role pattern: Claude author /
no-commit, Codex reviewer / closer).

Role separation basis: the contract itself governs handoffs, so the author and
reviewer roles stay explicit and auditable.

Escalation condition: if AC1 through AC7 cannot be satisfied from governed
sources, return a blocker in the worker return rather than inventing semantics.

## Agent Roles

| Role | Actor | Responsibility |
|---|---|---|
| Contract author | Claude | Author ratification packet and worker return; no commit |
| Reviewer / closer | Codex | Review actual files, decide accepted material, commit, closure gate |
| Operator | Human | Authorized AHB-T2 after AOT-T3; resolves unresolved contract decisions if needed |

## Required First Reads

Before authoring, Claude must read:

| # | File | Purpose |
|---|---|---|
| R1 | `docs/baselines/CVF_GC018_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | authorization, scope, acceptance criteria |
| R2 | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB tranche sequence and AHB-T2 purpose |
| R3 | `docs/audits/CVF_AHB_T1_HANDOFF_BOUNDARY_AUDIT_2026-06-16.md` | proposed contract model, gap ledger, surface mapping |
| R4 | `docs/reviews/CVF_AHB_T1_HANDOFF_BOUNDARY_AUDIT_CODEX_REBUTTAL_2026-06-16.md` | Codex critique, cross-batch and C3 requirements |
| R5 | `docs/reviews/CVF_AHB_T1_HANDOFF_BOUNDARY_AUDIT_COMPLETION_2026-06-16.md` | bounded closure and follow-up routing |
| R6 | `docs/reviews/CVF_AHB_T1A_FINDING_CLEANUP_COMPLETION_2026-06-16.md` | cleanup findings that should inform contract wording |
| R7 | `docs/reviews/CVF_AOT_T3_DISPATCH_MANIFEST_SCOPE_CHECK_COMPLETION_2026-06-16.md` | closed AOT-T3 dispatch-manifest rule |
| R8 | `docs/reference/CVF_AGENT_DISPATCH_PROMPT_ENVELOPE_STANDARD_2026-06-15.md` | dispatch envelope surface |
| R9 | `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md` | commit ownership and split rules |
| R10 | `docs/reference/CVF_AGENT_OPERATION_TRACE_AND_WORKSPACE_INTEGRITY_STANDARD_2026-06-13.md` | trace scope and manifest delta |
| R11 | `docs/reference/archive/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | MA1 predecessor vocabulary |
| R12 | `docs/reference/CVF_NEXT_MOVE_FRESHNESS_CHECKER_STANDARD_2026-06-16.md` | session-sync next-move surfaces |
| R13 | `AGENTS.md` | session startup and active handoff authority |

## Pre-Flight Checks

Before authoring, Claude must:

1. Confirm `git rev-parse --short HEAD` equals `88111c19`.
2. Confirm `git status --short` is clean.
3. Confirm all Required First Reads exist.
4. Run:
   ```powershell
   rg -n "Agent Handoff Contract|handoff contract|crossBatchIsolation|AHB-T2" docs
   ```
5. Confirm no same-purpose already-ratified contract exists. Predecessor AHB-T1
   and AOT-T3 artifacts are inputs, not collisions.

## Write Ownership

| Path | Owner | Mode |
|---|---|---|
| `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | Claude author, Codex commit | CREATE |
| `docs/reviews/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_WORKER_RETURN_2026-06-16.md` | Claude author, Codex commit | CREATE |

No other paths may be written. Claude must not update session state or handoff
files.

Codex-owned closure paths are named in Reviewer Closure Conversion, not in this
dispatch Write Ownership table. That keeps dispatch trace manifest scope
separate from future closure deliverables.

## Execution Plan

1. Claude reads R1-R13.
2. Claude runs Pre-Flight Checks.
3. Claude authors the ratification packet.
4. Claude authors the worker return with HEAD unchanged evidence.
5. Codex reviews actual files and either accepts with repairs, returns to
   Claude, or escalates unresolved operator decisions.
6. Codex commits accepted material, runs pre-closure gates, and session-syncs if
   the next allowed move changes.

## Required Ratification Packet Contents

The ratification packet must include:

- `## Scope / Applies-To`
- `## Source Authority`
- `## Ratified Contract Field Set`
- `## Surface Reconciliation Matrix`
- `## AOT-T3 Absorption`
- `## Cross-Batch Isolation Decision`
- `## C3 Three-Or-More-Agent Semantics`
- `## AHB-T3 Implementation Boundary`
- `## Claim Boundary`
- `## Public Export Disposition`
- `## Finding-To-Governance Learning Disposition`
- Rescan Intelligence Hardening section with delta ledger, routing matrix, and
  semantic sampling
- Agent Operation Trace Block with Agent type and Invocation ID rows

Field decisions must use exactly one of: `RATIFIED`, `RATIFIED_WITH_BOUNDARY`,
or `DEFERRED_WITH_REASON`.

## Evidence Requirements

| Evidence item | Source or command | Boundary |
|---|---|---|
| Required first reads complete | read ledger in ratification packet | source authority complete |
| Negative search result | `rg -n "Agent Handoff Contract|..." docs` summary | no same-purpose ratified contract |
| HEAD unchanged | `git rev-parse --short HEAD` before and after | worker no-commit honored |
| Changed set | `git status --short` | worker-owned files only |
| AOT-T3 absorption | cite AOT-T3 completion and AOT standard | closed input, not reopened |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Expected worker output | Disposition |
|---|---|---|---|
| AHB-T2 ratifies the contract | Purpose and Required Ratification Packet Contents | ratification packet under `docs/reference/` | DISPATCHED |
| Reconcile MA1/envelope/steward/AOT | Required first reads and AC2 | surface reconciliation matrix | DISPATCHED |
| Absorb AOT-T3 as closed input | Current-time notes, AC3, evidence requirements | AOT-T3 absorption section | DISPATCHED |
| Decide cross-batch isolation | AC4 | explicit decision or bounded deferral | DISPATCHED |
| Decide C3 semantics | AC5 | explicit decision or bounded deferral | DISPATCHED |
| Keep enforcement/workspace out of scope | Forbidden scope and AC7 | no forbidden paths changed | DISPATCHED |

## Review Gate

Codex reviewer gate after worker return:

```powershell
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_agent_operation_trace.py --base 88111c19 --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 88111c19 --head HEAD
```

Post-commit closure gate:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 88111c19 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode closure --base 88111c19 --head HEAD --enforce
```

## Closure Checklist

- [x] Required first reads R1-R13 are confirmed.
- [x] Pre-flight checks passed.
- [x] Ratification packet authored at required path.
- [x] Every contract field is resolved as RATIFIED, RATIFIED_WITH_BOUNDARY, or DEFERRED_WITH_REASON.
- [x] Surface reconciliation matrix has no orphaned MA1/envelope/steward/AOT/session-sync surface.
- [x] AOT-T3 is absorbed as closed input.
- [x] Cross-batch isolation is explicitly decided or deferred with blocking reason.
- [x] C3 semantics are explicitly decided or deferred with blocking reason.
- [x] Worker return states HEAD unchanged.
- [x] No forbidden runtime/checker/registry/provider/public/workspace work is claimed.

## Reviewer Closure Conversion

This is a `WORKER_MUST_NOT_COMMIT` dispatch. Claude writes only the ratification
packet and worker return; Codex converts accepted material into a closed tranche.

completionReviewPath: `docs/reviews/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_COMPLETION_2026-06-16.md`

reviewerOwnedClosurePaths: `docs/reviews/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_COMPLETION_2026-06-16.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md`; `docs/baselines/CVF_GC018_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_FOR_CLAUDE_2026-06-16.md`

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| GC-018 status | `docs/baselines/CVF_GC018_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_FOR_CLAUDE_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion review | `docs/reviews/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_COMPLETION_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_COMPLETION_2026-06-16.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Ratified contract | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` | `Status: ACTIVE_RATIFIED` | PASS |
| Worker return | `docs/reviews/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_WORKER_RETURN_2026-06-16.md` | `Status: ACCEPTED_BY_CODEX_WITH_REVIEWER_REPAIRS` | PASS |
| Roadmap state | `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` | AHB-T2 row `CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | BLOCKED with reason: no registry edit authorized for AHB-T2 documentation-only contract ratification | N/A | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown edit authorized for AHB-T2 documentation-only contract ratification | N/A | BLOCKED with reason |
| External evidence digest | N/A with reason: no external source/live proof | N/A | N/A with reason |
| System loop interlock | N/A with reason: AHB-T2 does not edit the registry | N/A | N/A with reason |
| Session continuity | N/A with reason: follows material closure commit separately if next move changes | N/A | N/A with reason |

## Current Runtime Freshness Verification

Runtime freshness is N/A with reason: AHB-T2 is a governed markdown contract
ratification packet. Do not touch runtime/source/test files, provider registry
files such as `provider-registry.ts`, `PROVIDER_CAPABILITY_REGISTRY`, interlock
registries, live proof, or public-sync surfaces.

## Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `RULE_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `CONTRACT_RATIFICATION_DISPATCHED`; `STANDARD_CANDIDATE` |
| Next control action | Claude authoring; Codex review; later AHB-T3 only after accepted contract |
| Worker blame | `N/A_WITH_REASON`: the target is a shared handoff seam, not individual worker fault |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order. No public-sync batch is authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-16 AHB-T2 work-order dispatch |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, governance gates |
| Target paths | `docs/baselines/CVF_GC018_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_FOR_CLAUDE_2026-06-16.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` |
| Allowed scope source | operator instruction 2026-06-16 to proceed with AHB-T2 after AOT-T3 |
| Before status evidence | HEAD `88111c19`; clean worktree |
| After status evidence | AHB-T2 dispatch batch pending commit |
| Diff evidence | `git diff --name-status 88111c19..HEAD` |
| Approval boundary | dispatch packet only |
| Claim boundary | no checker/runtime/provider/public/registry/workspace mutation |
| Agent type | Codex dispatcher |
| Invocation ID | `ahb-t2-agent-handoff-contract-ratification-work-order-codex-2026-06-16` |
| Expected manifest | `docs/baselines/CVF_GC018_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_FOR_CLAUDE_2026-06-16.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` |
| Actual changed set | `docs/baselines/CVF_GC018_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_FOR_CLAUDE_2026-06-16.md`; `docs/roadmaps/CVF_AGENT_HANDOFF_BOUNDARY_SYSTEMIZATION_ROADMAP_2026-06-16.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Claim Boundary

This work order dispatches AHB-T2 contract ratification authoring only. It does
not close AHB-T2, implement AHB-T3, wire gates, build the workspace, edit
runtime/source or registry files, run providers, public-sync, or claim
production/public readiness.
