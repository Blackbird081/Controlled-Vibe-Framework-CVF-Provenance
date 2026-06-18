# CVF Agent Work Order - PRFC-T3 PLCS Companion Routing Checker Interlock

Memory class: POINTER_RECORD

Status: DISPATCH_READY

## Dispatch Prompt Envelope

Role: Codex combined worker/reviewer/committer/closer.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_PRFC_T3_PLCS_COMPANION_ROUTING_CHECKER_INTERLOCK_FOR_CODEX_2026-06-18.md`

Commit mode: `WORKER_MAY_COMMIT`

dispatchBaseHead: `15816000`

executionBaseHead: `PENDING_AFTER_DISPATCH_COMMIT`

closureBaseHead: `PENDING_AFTER_IMPLEMENTATION_BASE`

Current-time notes: PRFC-T2 is closed at material commit `051b491e` and
session-sync commit `15816000`. PRFC-T3 is the next allowed move through fresh
GC-018 and source-verified work order. Runtime/provider/live, public-sync,
registry mutation, Model Gateway, and provider-registry work remain parked.

Do-not-misread notes: this task adds a checker/interlock for future work-order
structure only. It must not edit the system-loop interlock registry, provider
registry, runtime source, provider configuration, public-sync surfaces, or any
FPC C01-C04 registry entry.

Required first actions: read this work order, read the PRFC-T3 GC-018, read the
PRFC roadmap, read the PLCS-T3 decision, read the PLCS-T2 decision, inspect the
autorun and local hook-chain runner surfaces, then run pre-implementation gates
from Section 6.

Return contract: Codex may commit material and closure evidence after gates
pass. Any session/front-door sync must be a later separate session-sync range.

## Purpose

Implement PRFC-T3 by promoting the PLCS-T3 companion-block requirement into a
narrow machine checker/interlock for future FPC-T2 C01-C04 registry-edit work
orders.

## Scope / Target / Owner Boundary

Target: pre-dispatch work-order structure only.

Owner boundary: Codex owns implementation, tests, review, commit, and closure.
No other agent handoff is required for this tranche.

## Intake Role Routing Decision

intake summary: Dispatch PRFC-T3 as a bounded checker/interlock hardening task
for future FPC-T2 C01-C04 registry-edit work-order structure.

scope class: governance checker hardening; no runtime, provider/live,
public-sync, registry mutation, Model Gateway, UI, or production release scope.

risk sensitivity: R1; no secrets, live proof, provider call, public release,
legal/current-law claim, production claim, or user-data handling.

selected role route: `SINGLE_AGENT_MULTI_ROLE`

role separation basis: Codex performs worker, reviewer, committer, and closer
roles in one bounded local implementation lane because no cross-agent handoff
is needed.

escalation condition: stop only if completion requires forbidden paths,
protected session state in the material range, runtime/provider/live proof,
public-sync, registry mutation, Model Gateway work, destructive action, or claim
boundary expansion.

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| route | `SINGLE_AGENT_MULTI_ROLE` |
| actor | Codex |
| role set | worker; reviewer; committer; closer |
| Role separation ledger | Codex owns all roles, but dispatch, implementation, closure, and optional session-sync remain separate evidence ranges |
| Evidence basis independent of memory | source verification, git diff, focused tests, pre-dispatch, pre-implementation, pre-closure, and steward gates |
| Gate sequence | pre-dispatch before commit; pre-implementation before checker work; focused tests; pre-closure; closure steward; optional later session-sync gate |
| Self-review boundary | independent cross-agent review is not claimed; machine gates and source-backed trace are the self-review boundary |
| dispatch owner | Codex |
| implementation owner | Codex |
| review owner | Codex |
| commit owner | Codex |
| session-sync owner | Codex, only in a separate later sync range if needed |
| separation method | material implementation range and optional session-sync range stay split |
| authority boundary | this work order and GC-018; no operator inference beyond written scope |

## Agent Handoff Contract Control Block

| Field | Disposition |
|---|---|
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | Codex worker/reviewer/committer/closer |
| phase | dispatch phase; implementation phase; closure phase; optional later session-sync |
| baseHeadFor(phase) | `dispatchBaseHead=15816000`; `executionBaseHead=PENDING_AFTER_DISPATCH_COMMIT`; `closureBaseHead=PENDING_AFTER_IMPLEMENTATION_BASE` |
| changedSetScope(phase) | dispatch batch may change only GC-018, work order, and PRFC roadmap; implementation batch may change only owned paths in Section 4 |
| traceScope(phase, actor) | dispatch trace covers dispatch changed set only; implementation trace covers checker/test/wiring/closure changed set |
| commitOwner(phase) | Codex |
| crossBatchIsolation | one clean worktree per batch; stop if unrelated dirty files appear |
| nextMoveSurfaces | session/front-door surfaces are out of material scope; sync later only if closure changes next move |
| Closer designation | Codex |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED
priorVerificationArtifact: `N/A with reason: PLCS-T3 decision is authority, not reused command output`
priorVerificationAnchor: `N/A with reason: source facts are recomputed from current governed artifacts`
freshRecomputeRequired: YES
recomputeReason: `PRFC-T3 implementation must verify the current PRFC roadmap, PLCS decisions, and gate runner surfaces`
unicodePathHandling: `use literal repo-relative paths and UTF-8-safe readers`
extractedTextAuthority: N/A with reason

Evidence reuse is limited to CVF-governed artifacts named in the Authority Chain
and Source Verification Block. Provider-local memory, chat summaries, and
worker-private notes are not canonical evidence.

New governed markdown must use ASCII. No external evidence, API proof, or
Unicode-path evidence is authorized.

## Current Runtime Freshness Verification

Runtime, provider-registry, hardcoded model, queue, scheduler, UI, API,
provider/live behavior, and provider configuration are explicitly out of scope
and untouched. This work order must not make provider-registry absence,
hardcoded model, or runtime readiness claims.

Current provider-registry/accounting surfaces checked for boundary only:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts`: exists and remains
  untouched by PRFC-T3.
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`:
  declares `PROVIDER_CAPABILITY_REGISTRY` and remains untouched by PRFC-T3.

## Core Guard Self-Protection Authorization

Protected session and handoff paths are not authorized in the material
implementation batch. Codex may update those paths only in a separate
session-sync range after accepted material closure if next-move surfaces change.

Authorized guard-maintenance scope: none in the material batch.

Protected paths:

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `AGENT_HANDOFF_V19_2026-06-15.md`
- `governance/compat/check_plcs_companion_routing_block.py`
- `governance/compat/test_plcs_companion_routing_block.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/run_local_governance_hook_chain.py`

Operator authorization: PRFC-T3 is authorized by the active next move and this
GC-018. Protected session edits are not authorized until a separate sync range.

Rollback boundary: if implementation is rejected, revert only PRFC-T3
implementation and closure artifacts. Do not revert PRFC-T2 material or
session-sync commits.

## Foundation Storage Layout Block

This dispatch uses existing indexed foundation surfaces:

- GC-018 under `docs/baselines/`
- work order under `docs/work_orders/`
- checker and test under `governance/compat/`
- completion review under `docs/reviews/`
- stable PLCS decisions under `docs/reference/`

No new foundation folder is created. No stable foundation addendum is moved.
If implementation discovers that the companion-block template needs a stable
front door beyond the PLCS-T3 decision, stop and record a finding instead of
creating an unindexed folder.

## 1. Mission

Add a focused checker/interlock so future FPC-T2 C01-C04 registry-edit work
orders cannot dispatch without the PLCS companion routing block approved by
PLCS-T3.

Success means:

- the checker detects in-scope future C01-C04 registry-edit work orders;
- missing or incomplete PLCS companion blocks fail;
- unrelated work orders are exempt;
- C05 remains deferred and is not decided by the checker;
- pre-dispatch autorun/hook-chain placement catches the issue before worker
  dispatch;
- no registry edit, runtime source mutation, provider/live proof, or public-sync
  is introduced.

## 2. Authority Chain

- Operator instruction: continue after PRFC-T2 closure
- Active session next move: PRFC-T3 fresh GC-018 and source-verified work order
- GC-018:
  `docs/baselines/CVF_GC018_PRFC_T3_PLCS_COMPANION_ROUTING_CHECKER_INTERLOCK_2026-06-18.md`
- Parent roadmap:
  `docs/roadmaps/CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md`
- PLCS-T3 decision:
  `docs/reference/CVF_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_2026-06-16.md`
- PLCS-T2 decision:
  `docs/reference/CVF_PLCS_T2_REGISTRY_COMPANION_DECISION_2026-06-16.md`
- PLCS-T1 routing matrix:
  `docs/reference/CVF_PLCS_T1_ABSORPTION_TO_WORKFLOW_CHAIN_ROUTING_MATRIX_2026-06-16.md`
- Autorun workflow gate runner:
  `governance/compat/run_agent_autorun_workflow_gate.py`
- Local hook chain:
  `governance/compat/run_local_governance_hook_chain.py`

Authority boundary: if any authority artifact conflicts with this work order,
stop and return `BLOCKED_CONFLICTING_AUTHORITY`.

## 3. Agent Roles

- Dispatcher: Codex
- Worker / reviewer / committer / closer: Codex
- Operator approval required for: any registry mutation, runtime/provider/live,
  public-sync, Model Gateway, protected session state during material phase, or
  scope expansion

## Worker Autonomy / No-Question Rule

Any governance gate failure inside Allowed implementation scope and Write
Ownership must be repaired and rerun by Codex without asking the operator. Ask
the operator only if repair would exceed Allowed scope, change the claim
boundary, release a hold prerequisite, alter risk level, open public-sync, run
live/provider proof, consume secrets/quota, touch forbidden paths, or perform
destructive/irreversible actions.

## 4. Scope

Allowed implementation scope:

- add checker:
  `governance/compat/check_plcs_companion_routing_block.py`
- add focused tests:
  `governance/compat/test_plcs_companion_routing_block.py`
- wire checker into pre-dispatch autorun/local hook surfaces:
  `governance/compat/run_agent_autorun_workflow_gate.py`
  `governance/compat/run_local_governance_hook_chain.py`
- add completion review:
  `docs/reviews/CVF_PRFC_T3_PLCS_COMPANION_ROUTING_CHECKER_INTERLOCK_COMPLETION_2026-06-18.md`
- update PRFC roadmap PRFC-T3 row and closure note only:
  `docs/roadmaps/CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md`
- update this work order and GC-018 status/evidence fields if gates require
  closure conversion

Forbidden scope:

- system-loop interlock registry edits
- FPC C01-C04 registry-entry implementation
- C05 ruling or implementation
- provider-registry source or provider configuration edits
- runtime queue, scheduler, worker daemon, UI implementation
- provider/live proof, secrets, network calls
- public-sync, Model Gateway work, production release, or public release claims
- protected session/front-door/handoff edits in the material range

## Required First Reads

| ID | Required source | Purpose |
|---|---|---|
| R1 | `docs/baselines/CVF_GC018_PRFC_T3_PLCS_COMPANION_ROUTING_CHECKER_INTERLOCK_2026-06-18.md` | authorization and claim boundary |
| R2 | `docs/roadmaps/CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md` | PRFC-T3 acceptance criteria |
| R3 | `docs/reference/CVF_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_2026-06-16.md` | checker disposition and seven-field template |
| R4 | `docs/reference/CVF_PLCS_T2_REGISTRY_COMPANION_DECISION_2026-06-16.md` | C01-C04 companion ruling |
| R5 | `docs/reference/CVF_PLCS_T1_ABSORPTION_TO_WORKFLOW_CHAIN_ROUTING_MATRIX_2026-06-16.md` | candidate routing source |
| R6 | `governance/compat/run_agent_autorun_workflow_gate.py` | autorun placement surface |
| R7 | `governance/compat/run_local_governance_hook_chain.py` | local hook placement surface |

## Pre-Flight Checks

Before implementation, Codex must run:

- `git status --short`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <implementationBaseHead> --head HEAD`
- `git diff --check`

## Write Ownership

| Path | Ownership | Notes |
|---|---|---|
| `governance/compat/check_plcs_companion_routing_block.py` | add/update | checker implementation |
| `governance/compat/test_plcs_companion_routing_block.py` | add/update | focused tests |
| `governance/compat/run_agent_autorun_workflow_gate.py` | bounded update | pre-dispatch gate wiring |
| `governance/compat/run_local_governance_hook_chain.py` | bounded update | local hook-chain wiring |
| `docs/reviews/CVF_PRFC_T3_PLCS_COMPANION_ROUTING_CHECKER_INTERLOCK_COMPLETION_2026-06-18.md` | add | completion review |

## 5. Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| PRFC-T3 is authorized as the next source-verified tranche | `docs/roadmaps/CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md` | `## Tranche Plan`; `## PRFC-T3 Acceptance Criteria` | `PRFC-T3`; T3-AC1..T3-AC5 | PRFC roadmap | ACCEPT |
| Checker must enforce seven-field companion block | `docs/reference/CVF_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_2026-06-16.md` | `## Reusable Companion-Block Template` | seven required field names | PLCS-T3 decision | ACCEPT |
| Checker applies only to C01-C04 future registry-edit work orders | `docs/reference/CVF_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_2026-06-16.md` | `## Scope / Applies-To`; `## Enforcement Placement Recommendation` | C01-C04; pre-dispatch | PLCS-T3 decision | ACCEPT |
| C05 remains deferred | `docs/reference/CVF_PLCS_T3_COMPANION_ROUTING_CHECKER_TEMPLATE_DECISION_2026-06-16.md` | `## C05 Boundary` | `DEFERRED_PENDING_FPC_T3_C01` | PLCS-T3 decision | ACCEPT |
| PLCS-T2 required companion blocks for C01-C04 | `docs/reference/CVF_PLCS_T2_REGISTRY_COMPANION_DECISION_2026-06-16.md` | `## Per-Candidate Decision Table`; `## Registry-Edit Work Order Dispatch Constraint` | C01-C04 `REQUIRED` | PLCS-T2 decision | ACCEPT |
| Pre-dispatch autorun is a valid placement surface | `governance/compat/run_agent_autorun_workflow_gate.py` | phase command list | pre-dispatch gate list | autorun runner | ACCEPT |
| Local hook chain is a valid placement surface | `governance/compat/run_local_governance_hook_chain.py` | command list | local hook-chain command list | local hook-chain runner | ACCEPT |

## Execution Plan

1. Capture implementation base with `git rev-parse --short HEAD` after the
   dispatch commit.
2. Run pre-implementation gate:
   `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <implementationBaseHead> --head HEAD`
3. Implement checker and tests within Section 4 scope.
4. Wire checker into pre-dispatch autorun and local hook-chain surfaces.
5. Run focused tests:
   `pytest governance/compat/test_plcs_companion_routing_block.py`
6. Run pre-closure gate and closure steward on the implementation range.
7. Commit material closure only after gates pass.
8. If next-move surfaces need updating, perform a separate session-sync commit.

## Evidence Requirements

- Focused pytest output for the PLCS companion routing checker.
- Pre-closure autorun gate output on the implementation range.
- Closure steward output on the implementation range.
- `git diff --check`.
- `git status --short` after commit.
- Completion review with public export disposition and claim boundary.

## Review Gate

Codex must review the implementation against Section 7 trace rows and Section 8
acceptance criteria before committing. No handwritten PASS claim may override a
failing machine gate.

## Closure Checklist

- [ ] Required first reads completed
- [ ] Checker added inside Write Ownership
- [ ] Focused tests added and passing
- [ ] Autorun/local hook-chain placement wired or bounded alternative recorded
- [ ] No registry mutation, provider-registry edit, runtime source mutation,
  provider/live proof, public-sync, production readiness, or public readiness
- [ ] Completion review added
- [ ] Pre-closure gate and closure steward pass

## Return-To-Orchestrator Conditions

Return/close only after implementation evidence is committed and the worktree
is clean. If a required fix exceeds Write Ownership or forbidden scope, stop and
return `BLOCKED_SCOPE_EXPANSION_REQUIRED` with the exact path and reason.

## Operator Checkpoint

Operator checkpoint is required only for forbidden-scope expansion, live/provider
proof, public-sync, registry mutation, Model Gateway work, protected session
edits inside the material range, destructive action, or runtime/product claims.

## 7. Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order implementation hook | Evidence target |
|---|---|---|
| T3-AC1 seven-field PLCS block only for future C01-C04 work orders | Section 4 checker scope and Section 5 source verification | checker tests for required fields |
| T3-AC2 unrelated work orders exempt | Section 6 focused tests | unrelated exemption test |
| T3-AC3 missing/incomplete/wrong-scope coverage | Section 6 focused tests | pytest output |
| T3-AC4 hook/autorun placement | Section 4 runner wiring | pre-dispatch gate output |
| T3-AC5 no registry/runtime/public claim | Forbidden scope and completion review | closure gate and completion claim boundary |

## 8. Acceptance Criteria

- Checker fails an in-scope C01-C04 work order missing the PLCS companion block.
- Checker fails an in-scope block missing any of the seven required fields.
- Checker does not require the block for unrelated work orders.
- Checker does not treat C05 as in-scope beyond confirming the deferral
  boundary when C05 text appears in an in-scope block.
- Autorun/local hook wiring runs the checker before dispatch closure.
- Completion review records no registry edit, runtime mutation, provider/live
  proof, public-sync, production readiness, or public readiness.

## 9. Finding-To-Governance Learning Disposition

| Field | Disposition |
|---|---|
| Defect class | `RULE_INTERPRETATION_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `MACHINE_CHECK_DISPATCHED` |
| Next control action | Implement PRFC-T3 checker/interlock and wire it into pre-dispatch gates |
| Worker blame | `N/A_WITH_REASON`: this is planned machine promotion of PLCS-T3 guidance |

## 10. Public Export Disposition

Disposition: DEFERRED_PRIVATE_ONLY

Reason: private provenance governance checker hardening. No public-sync batch is
authorized.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatch author |
| Provider or surface | Codex local workspace |
| Session or invocation | 2026-06-18 PRFC-T3 dispatch |
| Working directory | `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, rg, apply_patch, governance gates |
| Target paths | `docs/baselines/CVF_GC018_PRFC_T3_PLCS_COMPANION_ROUTING_CHECKER_INTERLOCK_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_PRFC_T3_PLCS_COMPANION_ROUTING_CHECKER_INTERLOCK_FOR_CODEX_2026-06-18.md`; `docs/roadmaps/CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md` |
| Allowed scope source | active next move plus PRFC roadmap PRFC-T3 row |
| Before status evidence | clean worktree at dispatch base `15816000` |
| After status evidence | dispatch packet authored; pending dispatch gate and commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch only; no checker implementation, registry mutation, runtime, provider/live proof, or public-sync in this batch |
| Claim boundary | source-verified work order dispatch only |
| Agent type | Codex dispatch author |
| Invocation ID | `prfc-t3-plcs-companion-routing-checker-interlock-dispatch-codex-2026-06-18` |
| Expected manifest | `docs/baselines/CVF_GC018_PRFC_T3_PLCS_COMPANION_ROUTING_CHECKER_INTERLOCK_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_PRFC_T3_PLCS_COMPANION_ROUTING_CHECKER_INTERLOCK_FOR_CODEX_2026-06-18.md`; `docs/roadmaps/CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md` |
| Actual changed set | `docs/baselines/CVF_GC018_PRFC_T3_PLCS_COMPANION_ROUTING_CHECKER_INTERLOCK_2026-06-18.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_PRFC_T3_PLCS_COMPANION_ROUTING_CHECKER_INTERLOCK_FOR_CODEX_2026-06-18.md`; `docs/roadmaps/CVF_PRE_RUNTIME_FOUNDATION_CLEANUP_AND_PILOT_ROADMAP_2026-06-17.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## 12. Dispatch Checklist

- [ ] GC-018 exists
- [ ] Source Verification Block has ACCEPT rows for all source facts
- [ ] Roadmap row moves to DISPATCH_READY
- [ ] Pre-dispatch autorun gate passes
- [ ] `git diff --check` passes
- [ ] No implementation files are included in this dispatch batch

## Claim Boundary

This work order authorizes only PRFC-T3 checker/interlock implementation after
this dispatch packet passes. The dispatch batch itself creates no checker,
runtime behavior, registry edit, public-sync, provider/live proof, production
readiness, or public readiness claim.
