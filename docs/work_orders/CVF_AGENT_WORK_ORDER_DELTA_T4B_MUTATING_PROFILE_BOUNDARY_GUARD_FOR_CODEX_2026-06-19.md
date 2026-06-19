# CVF Agent Work Order - Delta-T4B Mutating Profile Boundary Guard For Codex

Memory class: FULL_RECORD

Status: DISPATCH_READY_FOR_CODEX

Date: 2026-06-19

docType: work_order

Batch ID: DELTA-T4B

Owner: Codex dispatcher, implementer, reviewer, closer, and session-sync actor

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `bbb84de0`

executionBaseHead: `bbb84de0` initial dispatch anchor; replace with the
dispatch session-sync commit before implementation

closureBaseHead: `NOT_OPEN_UNTIL_MATERIAL_ACCEPTANCE`

rawMemoryReleased: false

## Dispatch Prompt Envelope

Role: Codex single-agent multi-role executor. Keep dispatch authoring,
implementation/review, closure conversion, and protected session sync as
separate evidence phases.

Mission: implement Delta-T4B as a repo-local machine guard for future
mutating-profile, approval-backed mutation, EDIT profile, COMMIT profile, or
governed mutation-boundary artifacts. The guard must require a stable control
block before such artifacts can be dispatched or closed.

Do not add or modify runtime execution profiles, CLI behavior, approval runtime
policy, provider calls, public-sync, queues, daemons, CVF Web action execution,
direct IDE/shell/git/filesystem interception, or universal enforcement claims.

Required first actions: resolve session startup, read this work order and the
matching GC-018, source-verify every named checker/hook symbol, run
pre-dispatch, commit dispatch, sync dispatch continuity, then run
pre-implementation before checker edits.

Completion contract: focused checker tests, reviewer-fast, commit steward,
pre-closure, exact manifest evidence, completion review, evidence JSON, closure
conversion, and final session sync.

## Purpose

Promote the Delta-T4A machine-check candidate into an early guard. Future
mutating-profile work must state fixed target policy, approval evidence source,
caller path-input boundary, command authority, receipt chain, claim boundary,
and forbidden expansions before implementation or closure.

## Required First Reads

| Artifact | Required use |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | current mode and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | machine-readable continuity |
| `AGENT_HANDOFF_V20_2026-06-19.md` | active handoff and parked boundaries |
| matching Delta-T4B GC-018 | exact authorization and claim boundary |
| `docs/reviews/CVF_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_COMPLETION_2026-06-19.md` | source learning that creates this guard |
| `governance/compat/check_external_knowledge_intake_routing.py` | range-aware checker implementation pattern |
| `governance/compat/run_local_governance_hook_chain.py` | local hook registration owner |
| `governance/compat/run_agent_autorun_workflow_gate.py` | autorun registration owner |

## Scope / Target / Owner Boundary

Target: one governance checker, focused tests, hook/autorun wiring, completion
review, and evidence JSON.

Owner boundary: MCP runtime, Delta runtime profile source, approval runtime
policy, Model Gateway, CVF Web, generated workspace state, provider runtime,
public-sync, arbitrary commands, EDIT/COMMIT execution, and external
interception remain outside this work order.

Risk ceiling: R1 governance-control implementation. The guard is forward-only
and range-aware over changed governed Markdown artifacts.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| intake summary | operator agreed to follow the recommended high-foundation steps after EKA-R1 and Delta-T4A closure |
| scope classification | governance checker hardening |
| risk sensitivity | R1 because this tranche only checks governed artifacts |
| selected role route | `SINGLE_AGENT_MULTI_ROLE` |
| role separation basis | Codex separates dispatch, implementation, adversarial review, closure, and session-sync evidence phases |
| escalation condition | any runtime profile, CLI behavior, provider/live, public-sync, queue/daemon, CVF Web action, direct interception, or universal enforcement expansion |

## Authority Chain

| Level | Artifact | Status |
| --- | --- | --- |
| Operator authorization | current request on 2026-06-19 | ACCEPTED for recommended next steps |
| Active session | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Delta-T4A closed; next high-leverage foundation selection ready |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | Delta-T3, EKA-R1, and Delta-T4A closed bounded |
| Delta-T4A learning source | `docs/reviews/CVF_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_COMPLETION_2026-06-19.md` | `CLOSED_PASS_BOUNDED` |
| EKA-R1 guard pattern | `governance/compat/check_external_knowledge_intake_routing.py` | existing range-aware checker |
| GC-018 | `docs/baselines/CVF_GC018_DELTA_T4B_MUTATING_PROFILE_BOUNDARY_GUARD_2026-06-19.md` | `DISPATCH_READY` |
| Roadmap | N/A with reason: Delta-T4B follows active-session/operator-derived foundation selection, not a numbered roadmap tranche | N/A with reason |

## Agent Roles

| Role | Actor | Responsibility |
| --- | --- | --- |
| Dispatcher | Codex | author, source-verify, gate, and commit dispatch packet |
| Implementer | Codex | implement only allowed checker/test/hook scope |
| Reviewer / closer | Codex | adversarial self-review using focused tests, diffs, and gates |
| Session-sync actor | Codex | update protected continuity in separate commits |
| Operator | Human | authorize any forbidden scope expansion |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: add one new governance checker and register
it in the existing local hook and autorun guard bundles.

Protected paths authorized in this tranche:

- `governance/compat/check_delta_mutating_profile_boundary.py`
- `governance/compat/test_check_delta_mutating_profile_boundary.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`

Allowed mutation: additive checker/test creation and additive hook/autorun
registration only.

Forbidden mutation: deleting, disabling, weakening, or bypassing existing
guards; changing unrelated guard semantics; changing runtime/profile/provider
source; changing public-sync behavior.

Rollback boundary: revert only the Delta-T4B checker/test/hook wiring and
matching dispatch/completion/session-sync artifacts if rejected.

## Agent Handoff Contract Control Block

| Field | Disposition |
| --- | --- |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one-agent-many-roles: Codex holds dispatcher, implementer, reviewer, closer, and session-sync roles across distinct phases |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatch=`bbb84de0`; execution=`bbb84de0` initial dispatch anchor to refresh after dispatch session sync; closure=`NOT_OPEN_UNTIL_MATERIAL_ACCEPTANCE` |
| changedSetScope(phase) | dispatch baseline/work order; implementation checker/test/hook/completion/evidence; closure status conversion; protected continuity only in session-sync |
| traceScope(phase, actor) | Codex records exact phase-local manifests, commands, and commit anchors |
| commitOwner(phase) | Codex for every phase |
| crossBatchIsolation | one Delta-T4B batch in a clean worktree; no concurrent batch mixing |
| nextMoveSurfaces | update only in separate session-sync commits after dispatch/material/closure as required |
| closerDesignation | Codex is designated closer |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
| --- | --- |
| Role separation ledger | dispatch author -> implementation worker -> adversarial reviewer -> closer -> session-sync steward |
| Evidence basis independence | each later role rereads committed source/diff and reruns its matching gates |
| Self-review challenge | prove the checker catches missing/weak mutating-profile boundary claims and ignores unrelated docs |
| Commit choreography | dispatch, dispatch sync, material, closure, final sync |
| Forbidden shortcut | no combined material/session commit and no closure claim from uncommitted changes |
| Gate sequence | pre-dispatch -> dispatch commit -> dispatch sync -> pre-implementation -> tests/review -> material commit -> closure -> session sync -> pre-push |
| Escalation conditions | fresh human authorization for runtime profile, CLI, risk/claim expansion, provider/live, public-sync, queue/daemon, Web action, or direct interception |

## Delta Mutating Profile Boundary Control Block

| Field | Disposition |
| --- | --- |
| profileScope | `MACHINE_GUARD_ONLY`: no new runtime profile |
| fixedTargetPolicy | future applicable artifacts must state fixed target or `N/A with reason` |
| approvalEvidenceSource | future applicable artifacts must state approval evidence source or `N/A with reason` |
| callerPathInput | future applicable artifacts must state `NO_CALLER_PATH_INPUT`, `CALLER_PATH_INPUT_FORBIDDEN`, or `N/A with reason` |
| commandAuthority | future applicable artifacts must state static profile/command authority or `N/A with reason` |
| receiptChain | future applicable artifacts must state T1/T2/T3/T4-style receipt chain or `N/A with reason` |
| claimBoundary | future applicable artifacts must reject universal governed-coding and direct interception claims unless separately authorized |
| forbiddenExpansion | this tranche forbids new runtime profiles, EDIT/COMMIT execution, arbitrary commands, provider/live, public-sync, queue, daemon, and direct interception |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | Runtime/MCP claim must cite current proof, work-order source verification, and local-view guard before implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; proposed `governance/compat/check_delta_mutating_profile_boundary.py` |
| Owner surface | this Delta-T4B work order |
| Disposition | `DO_NOW` only for guard-only machine enforcement; runtime mutation expansion is blocked |
| Claim boundary | no runtime/provider/live/public-sync/direct interception/universal governed-coding control claim |

## Source Verification Block

| Claimed item | Verification type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Delta-T4A recorded a future machine-check candidate for mutating profiles to declare fixed target, approval evidence source, and no caller path input. | LITERAL_INVARIANT | `docs/reviews/CVF_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_COMPLETION_2026-06-19.md` | line 118 | `Machine-check action` | Delta-T4A Finding-To-Governance Learning Disposition | ACCEPT |
| Delta-T4A kept arbitrary, EDIT, COMMIT, and external interception scope parked. | LITERAL_INVARIANT | `docs/reviews/CVF_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_COMPLETION_2026-06-19.md` | line 120 | `Next action` | Delta-T4A Finding-To-Governance Learning Disposition | ACCEPT |
| Local hook chain contains reviewer-fast, pre-commit, and pre-push checker registration lanes. | EXISTS | `governance/compat/run_local_governance_hook_chain.py` | lines 24, 143, 151, and 368 | `REVIEWER_FAST_CHECKS`; `HOOK_CHAINS` | local governance hook chain | ACCEPT |
| Autorun common commands are the correct owner for a range-aware governance checker. | EXISTS | `governance/compat/run_agent_autorun_workflow_gate.py` | lines 52 and 399 | `_common_commands` | autorun workflow gate | ACCEPT |
| Existing EKA-R1 checker provides the range-aware changed-governed-Markdown pattern. | EXISTS | `governance/compat/check_external_knowledge_intake_routing.py` | module `CVF external knowledge intake routing guard` | `_get_changed_paths`; `check_text`; `main` | EKA-R1 checker | ACCEPT |

## New Doc-Only Fields

| Proposed field or symbol | Disposition |
| --- | --- |
| `Delta Mutating Profile Boundary Control Block` | new governed Markdown block enforced by this tranche |
| `profileScope` | new control-block row |
| `fixedTargetPolicy` | new control-block row |
| `approvalEvidenceSource` | new control-block row |
| `callerPathInput` | new control-block row |
| `commandAuthority` | new control-block row |
| `receiptChain` | new control-block row |
| `claimBoundary` | new control-block row |
| `forbiddenExpansion` | new control-block row |

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| Foundation file class | machine guard and focused test under existing `governance/compat/` owner surface |
| Stable path policy | use stable, non-dated checker path `governance/compat/check_delta_mutating_profile_boundary.py` |
| Index/front-door impact | N/A with reason: governance compat checkers are indexed through hook/autorun wiring rather than a new stable docs front door |
| Dated execution evidence | completion review and evidence JSON remain dated under `docs/reviews/` and `docs/reviews/evidence/` |
| Archive policy | N/A with reason: no archive movement or historical rewrite |
| Claim boundary | guard storage only; no runtime/provider/public readiness claim |

## Current Runtime Freshness Verification

Current runtime/source state at dispatch:

- Delta-T4A is already closed bounded and has one fixed
  `approval-marker-write` profile.
- This work order does not authorize changing MCP runtime profile source,
  `cvf-governed-exec`, approval-policy runtime source, or Model Gateway code.
- Provider registry surfaces are not part of this tranche:
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and
  `PROVIDER_CAPABILITY_REGISTRY` remain unchanged and are not evidence for this
  repo-local guard.
- Any provider/live or runtime-provider capability claim is N/A with reason:
  this tranche checks governed Markdown artifacts only.

## Roadmap-To-Work-Order Trace Matrix

Applicability: N/A with reason: no numbered roadmap owns Delta-T4B. Trace chain
is active session -> operator authorization -> Delta-T4A closure learning ->
fresh GC-018 -> this work order.

| Upstream requirement | Work order section | Deliverable | Verification | Closure state |
| --- | --- | --- | --- | --- |
| T4A machine-check candidate | Delta Mutating Profile Boundary Control Block | new checker and tests | focused tests | OPEN |
| no runtime expansion | Scope / Target / Owner Boundary | no runtime paths touched | diff review | OPEN |
| hook enforcement | Acceptance Criteria | hook/autorun wiring | reviewer-fast/pre-closure | OPEN |
| no universal claim | Claim Boundary | bounded completion language | text review | OPEN |

## Work-Order Fulfillment Manifest

| Artifact | Required result |
| --- | --- |
| checker | new range-aware checker exists and enforces the Delta mutating-profile control block |
| focused tests | positive, negative, missing-field, caller-path, and unrelated-doc cases pass |
| local hook wiring | checker appears in reviewer-fast, pre-commit, and pre-push chains |
| autorun wiring | checker appears in common autorun commands |
| completion/evidence | exact changed set, commands, and bounded claim are recorded |

## Write Ownership

Codex may create or modify only:

- `governance/compat/check_delta_mutating_profile_boundary.py`
- `governance/compat/test_check_delta_mutating_profile_boundary.py`
- `governance/compat/run_local_governance_hook_chain.py`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- matching Delta-T4B GC-018, work order, completion review, and evidence JSON;
- protected session continuity only in separate session-sync commits.

Forbidden: MCP runtime source, Delta CLI/runtime profile source, Model Gateway,
CVF Web, workspace state, queue/runtime skeleton, provider files, credential
files, public-sync, dependencies/lockfiles, and unrelated paths.

## Worker Autonomy / No-Question Rule

If a machine gate fails inside the Allowed scope, Codex must repair the packet
or implementation and rerun the failed gate. Escalation is reserved for changes
that exceed Allowed scope, change the claim boundary, release a parked
prerequisite, add provider/live or public-sync work, consume secrets or quota,
touch forbidden paths, or perform destructive or irreversible action.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if implementation requires runtime profile source,
CLI behavior change, provider/live call, public-sync, queue/daemon, CVF Web
action execution, direct interception, or any forbidden path.

## Closure Checklist

- [ ] Dispatch packet includes source verification for every existing symbol
  named in implementation instructions.
- [ ] Work order includes Agent Handoff, Single-Agent, Delta Mutating Profile,
  External Knowledge Intake Routing, and Worker Autonomy control blocks.
- [ ] Allowed scope is limited to one governance checker and hook wiring.
- [ ] Forbidden scope names runtime profiles, EDIT/COMMIT execution,
  provider/live, public-sync, queue/daemon, direct interception, and universal
  control.
- [ ] Closure requires completion review, evidence JSON, focused tests,
  reviewer-fast, commit steward, and governance gates.

## Required Artifact Manifest

| Path | Required at closure | Owner | Purpose |
| --- | --- | --- | --- |
| `governance/compat/check_delta_mutating_profile_boundary.py` | YES | Codex | range-aware checker |
| `governance/compat/test_check_delta_mutating_profile_boundary.py` | YES | Codex | focused checker tests |
| `governance/compat/run_local_governance_hook_chain.py` | YES | Codex | local hook wiring |
| `governance/compat/run_agent_autorun_workflow_gate.py` | YES | Codex | autorun wiring |
| `docs/reviews/CVF_DELTA_T4B_MUTATING_PROFILE_BOUNDARY_GUARD_COMPLETION_2026-06-19.md` | YES | Codex | completion review |
| `docs/reviews/evidence/delta-t4b-mutating-profile-boundary-guard-2026-06-19.json` | YES | Codex | machine-readable evidence |

## Pre-Flight Checks

Run from repository root:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base bbb84de0 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base bbb84de0 --head HEAD --enforce
```

After dispatch commit and separate dispatch continuity sync, run
pre-implementation from the refreshed execution base before checker edits.

## Execution Instructions

1. Re-read every source symbol in the Source Verification Block.
2. Add a range-aware checker based on changed governed Markdown paths.
3. Trigger on explicit marker text and on mutating-profile, approval-backed
   mutation, EDIT profile, COMMIT profile, and governed mutation-boundary text.
4. Require `## Delta Mutating Profile Boundary Control Block`.
5. Require non-empty rows for `profileScope`, `fixedTargetPolicy`,
   `approvalEvidenceSource`, `callerPathInput`, `commandAuthority`,
   `receiptChain`, `claimBoundary`, and `forbiddenExpansion`.
6. Reject `callerPathInput` unless it contains `NO_CALLER_PATH_INPUT`,
   `CALLER_PATH_INPUT_FORBIDDEN`, or `N/A with reason`.
7. Add focused tests and wire the checker into reviewer-fast, pre-commit,
   pre-push, and autorun common gates.
8. Author completion/evidence and commit material separately from session sync.

## Execution Plan

1. Commit and session-sync the source-verified dispatch packet.
2. Recompute pre-implementation gates from the refreshed execution base.
3. Implement the range-aware checker and focused tests.
4. Wire the checker into local hook and autorun bundles.
5. Run focused tests, reviewer-fast, steward preflight, and pre-closure gates.
6. Author completion review and evidence JSON.
7. Commit material, convert closure artifacts, and sync continuity separately.

## Review Gate

Before material acceptance, Codex must reread the changed checker, tests, and
hook wiring; run focused tests; run reviewer-fast; inspect the exact diff; and
record any reviewer finding in the completion review.

## Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC1 | Applicable changed governed Markdown without the control block fails. |
| AC2 | Applicable changed governed Markdown with all required rows passes. |
| AC3 | Missing row or empty row fails. |
| AC4 | Caller path-input row fails unless it states no caller path input, caller path input forbidden, or N/A with reason. |
| AC5 | Unrelated governed Markdown is ignored. |
| AC6 | The checker is wired into reviewer-fast, pre-commit, pre-push, and autorun common gates. |
| AC7 | No runtime/source/profile/provider/public/direct-interception behavior changes occur. |

## Evidence Requirements

Run from repository root:

```powershell
python -m unittest governance.compat.test_check_delta_mutating_profile_boundary
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_delta_mutating_profile_boundary.py
python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <implementationBaseHead> --head HEAD
```

## Operator Checkpoint

Human approval is required for any expansion beyond guard-only enforcement,
including runtime profile source changes, CLI behavior changes, EDIT/COMMIT
execution, arbitrary commands, provider/live calls, public-sync, queue/daemon,
CVF Web action execution, direct IDE/shell/git/filesystem interception, or
universal governed-coding claims.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | local provenance workspace |
| Session or invocation | `delta-t4b-dispatch-codex-2026-06-19` |
| Working directory | repository root |
| Command or tool surface | PowerShell, rg, apply_patch, governance gates |
| Target paths | this work order and matching GC-018 |
| Allowed scope source | user authorization to follow recommended high-foundation steps after Delta-T4A |
| Before status evidence | clean worktree at `bbb84de0` |
| After status evidence | Delta-T4B dispatch packet ready |
| Diff evidence | `git diff --name-status`; pre-dispatch gates |
| Approval boundary | governance checker dispatch only |
| Claim boundary | no runtime/provider/live/public-sync/direct interception/universal governed coding |
| Agent type | single-agent multi-role Codex dispatch phase |
| Invocation ID | `delta-t4b-mutating-profile-boundary-guard-dispatch-codex-2026-06-19` |
| Expected manifest | `docs/baselines/CVF_GC018_DELTA_T4B_MUTATING_PROFILE_BOUNDARY_GUARD_2026-06-19.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_DELTA_T4B_MUTATING_PROFILE_BOUNDARY_GUARD_FOR_CODEX_2026-06-19.md` |
| Actual changed set | `docs/baselines/CVF_GC018_DELTA_T4B_MUTATING_PROFILE_BOUNDARY_GUARD_2026-06-19.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_DELTA_T4B_MUTATING_PROFILE_BOUNDARY_GUARD_FOR_CODEX_2026-06-19.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none planned |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance guard dispatch. Public-sync is not
authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: DISPATCH_READY_FOR_CODEX` | OPEN |
| GC-018 baseline | `docs/baselines/CVF_GC018_DELTA_T4B_MUTATING_PROFILE_BOUNDARY_GUARD_2026-06-19.md` | `Status: DISPATCH_READY` | OPEN |
| Material implementation | checker, test, hook wiring, completion evidence | pending | OPEN |
| Completion or reviewer artifact | `docs/reviews/CVF_DELTA_T4B_MUTATING_PROFILE_BOUNDARY_GUARD_COMPLETION_2026-06-19.md` | pending | OPEN |
| Roadmap state | N/A with reason: active-session/operator-derived tranche | no roadmap mutation | N/A with reason |
| Registry JSON | BLOCKED with reason: no corpus registry edit authorized | no registry path planned | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown edit authorized | no registry path planned | BLOCKED with reason |
| Provider/live proof | N/A with reason: no provider claim | no live provider command | N/A with reason |
| Public-sync | N/A with reason: not authorized | `DEFERRED_PRIVATE_ONLY` | N/A with reason |

## Claim Boundary

This work order authorizes only a range-aware governance checker for future
mutating-profile boundary artifacts. It does not make MCP mandatory, intercept
direct IDE/shell/git/filesystem actions, execute arbitrary commands, implement
EDIT/COMMIT, run live providers, public-sync, or establish universal
governed-coding control.
