# CVF Agent Work Order - GGL-T2 Git Hook Lane And Worktree Finality Reliability For Codex

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-19

docType: work_order

Batch ID: GGL-T2

Owner: Codex dispatcher, implementer, reviewer, closer, and session-sync actor

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `5077cea5`

executionBaseHead: `01836f18`

closureBaseHead: `02678968`

rawMemoryReleased: false

## Dispatch Prompt Envelope

Role: Codex single-agent multi-role executor with phase-separated dispatch,
implementation, review, closure, and session-sync evidence.

Canonical packet: this work order and
`docs/baselines/CVF_GC018_GGL_T2_GIT_HOOK_LANE_AND_WORKTREE_FINALITY_RELIABILITY_2026-06-19.md`.

Commit mode: `WORKER_MAY_COMMIT`.

executionBaseHead: `01836f18`

Current-time notes: base `5077cea5`; current mode is
`delta_t7_receipt_to_execution_evidence_auditor_closed_next_foundation_ready`;
GGL-T2 is selected because pre-commit remains serial and Git stderr can be
misclassified as dirty-worktree output.

Do-not-misread notes: this is hook-lane/finality reliability only, not checker
suppression, hook bypass, runtime enforcement, provider/live proof, or a
universal speed/readiness claim.

Mission: remove the installed pre-commit hook's hardcoded serial lane and make
autorun pre-closure finality stderr-safe while preserving checker coverage and
fail-closed behavior.

Do not remove or suppress a checker, bypass git hooks, edit runtime/provider/UI
source, run provider/live proof, use secrets/quota, perform public-sync, or make
universal performance/readiness/governed-coding claims.

Required first actions: resolve startup, read this work order and matching
GC-018, source-verify named symbols, run pre-dispatch from `5077cea5`, commit
dispatch, then run pre-implementation before source edits.

Return contract: return `BLOCKED` if complete checker coverage, explicit serial
debugging, or fail-closed finality cannot be preserved.

Completion contract: focused tests, direct hook/finality smoke where feasible,
worker-return fast gate, implementation/closure steward, committed-range
pre-closure, exact changed-set evidence, completion review, evidence JSON, and
final session sync naming the next foundation route.

## Purpose

Turn the post-GGL-T1 reliability finding into a bounded CVF control-plane
hardening tranche. The tranche aligns the installed Git hook with the hook
runner's parallel default and prevents Git diagnostic stderr from masquerading
as dirty worktree status.

## Required First Reads

| Artifact | Required use |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | current mode and next move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | machine continuity |
| `AGENT_HANDOFF_V20_2026-06-19.md` | parked boundaries |
| matching GGL-T2 GC-018 | authorization and safety boundary |
| `.githooks/pre-commit` | installed hook invocation |
| `governance/compat/run_local_governance_hook_chain.py` | hook runner parallel/serial semantics |
| `governance/compat/run_agent_autorun_workflow_gate.py` | pre-closure finality owner |

## Scope / Target / Owner Boundary

Target: installed pre-commit hook, autorun finality helper, focused tests,
completion review, and evidence JSON.

Owner boundary: checker implementations, runtime profiles, MCP runtime, Model
Gateway, CVF Web, provider/live behavior, public-sync, queues, daemons, and
direct interception remain outside this work order.

Risk ceiling: R1 governance-control implementation.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| intake summary | operator asked to continue processing the finding after GGL-T1 and Delta-T7 |
| scope classification | governance hook/finality reliability hardening |
| risk sensitivity | R1 because coverage and fail conditions remain unchanged |
| selected role route | `SINGLE_AGENT_MULTI_ROLE` |
| role separation basis | distinct committed dispatch, implementation, closure, and continuity phases |
| escalation condition | any checker suppression, hook bypass, runtime/provider/public/UI change, or claim expansion |

## Authority Chain

| Level | Artifact | Status |
| --- | --- | --- |
| Operator authorization | current request on 2026-06-19: continue processing finding | ACCEPTED |
| Active session | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Delta-T7 closed; next foundation selection allowed |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | GGL-T2 leading candidate through fresh GC-018 |
| GC-018 | `docs/baselines/CVF_GC018_GGL_T2_GIT_HOOK_LANE_AND_WORKTREE_FINALITY_RELIABILITY_2026-06-19.md` | `CLOSED_PASS_BOUNDED` |

## Agent Roles

| Role | Actor | Responsibility |
| --- | --- | --- |
| Dispatcher | Codex | source verification and dispatch commit |
| Implementer | Codex | bounded hook/finality reliability fix |
| Reviewer / closer | Codex | adversarial tests, diff, gates, closure conversion |
| Session-sync actor | Codex | protected continuity in separate commit |
| Operator | Human | authorize forbidden expansion only |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: bounded Git hook lane and autorun
worktree-finality reliability with unchanged checker coverage and fail
conditions.

Protected paths authorized in this tranche:

- `.githooks/pre-commit`
- `governance/compat/run_agent_autorun_workflow_gate.py`
- `governance/compat/test_run_agent_autorun_workflow_gate.py`
- `governance/compat/test_run_local_governance_hook_chain.py`

Allowed completion/evidence paths:

- `docs/reviews/CVF_GGL_T2_GIT_HOOK_LANE_AND_WORKTREE_FINALITY_RELIABILITY_COMPLETION_2026-06-19.md`
- `docs/reviews/evidence/ggl-t2-git-hook-lane-and-worktree-finality-reliability-2026-06-19.json`

Forbidden mutation: checker removal, changed fail conditions, hook bypass,
runtime/provider/public behavior, broad hook-chain rewrite, or unrelated
governance semantics.

Rollback boundary: revert only GGL-T2 implementation and matching artifacts.

## Agent Handoff Contract Control Block

| Field | Disposition |
| --- | --- |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one-agent-many-roles with phase-separated evidence |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatch=`5077cea5`; execution set from dispatch commit; closure set from accepted material commit |
| changedSetScope(phase) | dispatch baseline/work order; implementation hook/autorun/tests/completion/evidence; continuity only in session-sync |
| traceScope(phase, actor) | Codex records exact manifests, commands, timing, and commit anchors |
| commitOwner(phase) | Codex |
| crossBatchIsolation | one GGL-T2 batch in a clean worktree; `git status --short` before dispatch showed no changed paths and only a global Git ignore warning in this host environment |
| nextMoveSurfaces | separate session-sync when GGL-T2 records `CLOSED_PASS_BOUNDED` |
| closerOwner | Codex is the designated closer |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
| --- | --- |
| Role separation ledger | dispatcher -> implementer -> adversarial reviewer -> closer -> session-sync steward |
| Evidence basis independence | each phase rereads committed source and uses phase-local gates |
| Self-review challenge | prove Git stderr warnings cannot create false dirty-worktree failures |
| Commit choreography | dispatch, material, closure, final sync |
| Forbidden shortcut | no combined material/session commit; no hook bypass |
| Gate sequence | pre-dispatch -> dispatch commit -> pre-implementation -> tests -> material commit -> pre-closure -> closure -> session sync |
| Escalation conditions | checker/hook/runtime/provider/public/UI/claim expansion |

## Hook Lane Reliability Control Block

| Field | Disposition |
| --- | --- |
| hookDefault | installed pre-commit should call `--hook pre-commit` and rely on the runner default |
| serialEscapeHatch | `run_local_governance_hook_chain.py --hook pre-commit --serial` remains available for debugging |
| checkerCoverage | unchanged hook chain and unchanged command list |
| stderrPolicy | successful Git status stderr is diagnostic-only; dirty status comes from stdout |
| failurePolicy | non-zero Git status remains fail-closed for finality |
| claimBoundary | bounded local hook/finality reliability only |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | `GOVERNANCE_HOOK_FINALITY_ONLY`: no runtime execution control added |
| claimDisposition | `BOUNDED_CLAIM_WITH_EVIDENCE` only after focused tests and gates pass |
| receiptEvidence | N/A with reason: this tranche does not create execution-control receipts |
| actionEvidence | ACTION_EVIDENCE_PRESENT through focused tests, hook invocation, and pre-closure gate output |
| invocationBoundary | cooperating local Git hook and autorun invocation only |
| interceptionBoundary | no direct IDE/shell/git/filesystem/provider interception beyond existing local hook invocation |
| claimLanguage | bounded hook/finality reliability only; no universal governed-coding control claim |
| forbiddenExpansion | runtime profiles, arbitrary commands, EDIT/COMMIT execution, provider/live, public-sync, queue, daemon, CVF Web action, and direct interception remain parked |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | finding -> CVF-owned baseline/work order -> guarded implementation -> evidence |
| Matching local-view guard | `.githooks/pre-commit`; `governance/compat/run_agent_autorun_workflow_gate.py`; `governance/compat/run_local_governance_hook_chain.py` |
| Owner surface | GGL-T2 work order |
| Disposition | `DO_NOW` |
| Claim boundary | no provider/runtime/public/readiness or universal speed/control claim |

## Source Verification Block

| Claimed item | Verification type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Installed pre-commit hook forces serial execution. | LITERAL_INVARIANT | canonical-contract: `.githooks/pre-commit` | line 7 command body | `pre-commit hook invocation` | local git hook | ACCEPT |
| Local hook runner already defaults `pre-commit`, `pre-push`, and `reviewer-fast` to parallel unless `--serial` is passed. | RUNTIME_BEHAVIOR | `governance/compat/run_local_governance_hook_chain.py` | `PARALLEL_BY_DEFAULT_HOOKS`; `main` | `PARALLEL_BY_DEFAULT_HOOKS`; `use_parallel` | local governance hook chain | ACCEPT |
| Local hook runner preserves explicit serial debugging behavior. | RUNTIME_BEHAVIOR | `governance/compat/run_local_governance_hook_chain.py` | `main` argument parsing | `--serial` | local governance hook chain | ACCEPT |
| Autorun worktree-finality helper currently merges Git stderr into stdout. | RUNTIME_BEHAVIOR | `governance/compat/run_agent_autorun_workflow_gate.py` | `_git_status_short` | `stderr` | autorun workflow gate | ACCEPT |
| Autorun pre-closure treats any non-empty `_git_status_short()` result as unclean worktree output. | RUNTIME_BEHAVIOR | `governance/compat/run_agent_autorun_workflow_gate.py` | `_run_phase` pre-closure finality block | `_git_status_short`; `closure worktree finality` | autorun workflow gate | ACCEPT |
| Autorun focused test module exists for function-level coverage. | EXISTS | `governance/compat/test_run_agent_autorun_workflow_gate.py` | module | `test_valid_receipt_requires_exact_context` | autorun focused tests | ACCEPT |
| Local hook runner focused test module exists and already verifies parallel defaults. | EXISTS | `governance/compat/test_run_local_governance_hook_chain.py` | module | `test_latency_sensitive_hooks_default_to_parallel` | local hook chain focused tests | ACCEPT |

## New Doc-Only Fields

| New item | Required value or shape | Purpose |
| --- | --- | --- |
| `Hook Lane Reliability Control Block` | required table in GGL-T2 artifacts | safety and reliability boundary |
| `hookDefault` | pre-commit uses runner default | avoid duplicated serial latency |
| `stderrPolicy` | diagnostics reported separately from status stdout | prevent false dirty-worktree claims |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: hook invocation, Git status diagnostics, and gate behavior must
be computed from the current source and worktree for this tranche.

unicodePathHandling: use literal repository paths and UTF-8-safe readers; no
Unicode path is promoted as authority.

| Field | Disposition |
| --- | --- |
| reused evidence | source symbols re-verified from repository source at base `5077cea5` |
| canonical authority | runtime source and canonical hook/autorun standards, not provider memory |
| verificationMode | direct source read plus focused machine checks before dispatch and implementation |
| local receipt authority | N/A with reason: this tranche does not add receipt reuse |
| stale evidence handling | stale, warning-only, or memory-only findings must be rechecked against source |

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| stable foundation path | existing hook and autorun source paths |
| dated execution artifacts | GC-018, work order, completion review, evidence JSON |
| generated aggregate | N/A with reason: no governed aggregate added in material scope |
| index/README | N/A with reason: no new stable folder added |

## Current Runtime Freshness Verification

| Surface | Verification |
| --- | --- |
| HEAD anchor | `5077cea5` before dispatch edits |
| worktree | clean except Git global ignore warning produced by `git status --short` in this environment |
| current hook invocation | `.githooks/pre-commit` calls `run_local_governance_hook_chain.py --hook pre-commit --serial` |
| hook runner default | `PARALLEL_BY_DEFAULT_HOOKS` includes `pre-commit` |
| finality helper | `_git_status_short()` merges stderr into stdout |

Provider registry surfaces are not part of this tranche:
`EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts` and
`PROVIDER_CAPABILITY_REGISTRY` remain unchanged and are not evidence for this
hook/finality reliability work. Any provider/live or runtime-provider
capability claim is N/A with reason: this tranche changes local governance hook
and autorun finality behavior only.

## Roadmap-To-Work-Order Trace Matrix

| Upstream requirement | Work-order instruction | Evidence required |
| --- | --- | --- |
| GGL-T1 left hook lane outside optimized autorun receipt reuse | AC1 and hook diff | `.githooks/pre-commit` diff and pre-commit run |
| Delta-T7 closure recorded stderr dirty-status finding | AC3-AC5 and autorun tests | focused tests and pre-closure proof |
| Maintain bounded claim boundary | claim boundary blocks | completion review and evidence JSON |

## Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC1 | The installed pre-commit hook no longer forces `--serial`; it uses the runner's existing default for `pre-commit`. |
| AC2 | Explicit serial debugging remains available through the hook runner CLI. |
| AC3 | Pre-closure finality treats dirty worktree evidence as Git status stdout only. |
| AC4 | Successful Git status stderr diagnostics are printed or surfaced separately but do not cause dirty-worktree failure. |
| AC5 | Non-zero Git status remains fail-closed. |
| AC6 | Focused tests cover hook invocation shape, parallel default preservation, stderr-only clean status, dirty stdout, and non-zero status failure. |
| AC7 | Existing hook command coverage and autorun checker coverage remain unchanged. |

## Evidence Requirements

Required evidence:

- focused pytest/unittest for autorun and hook-chain behavior;
- direct hook invocation proof;
- worker-return fast gate;
- implementation commit steward;
- pre-commit hook proof;
- committed-range pre-closure proof;
- completion review and evidence JSON.

Provider/live and public-sync evidence are not applicable because both are
forbidden by this work order.

## Work-Order Fulfillment Manifest

| Path | Required at handoff | Purpose |
| --- | --- | --- |
| `docs/baselines/CVF_GC018_GGL_T2_GIT_HOOK_LANE_AND_WORKTREE_FINALITY_RELIABILITY_2026-06-19.md` | true | authorization baseline |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_GGL_T2_GIT_HOOK_LANE_AND_WORKTREE_FINALITY_RELIABILITY_FOR_CODEX_2026-06-19.md` | true | material authorization and work-order state |
| `.githooks/pre-commit` | true | installed pre-commit hook lane |
| `governance/compat/run_agent_autorun_workflow_gate.py` | true | worktree-finality owner |
| `governance/compat/test_run_agent_autorun_workflow_gate.py` | true | focused finality tests |
| `governance/compat/test_run_local_governance_hook_chain.py` | true | focused hook lane tests |
| `docs/reviews/CVF_GGL_T2_GIT_HOOK_LANE_AND_WORKTREE_FINALITY_RELIABILITY_COMPLETION_2026-06-19.md` | true | completion review |
| `docs/reviews/evidence/ggl-t2-git-hook-lane-and-worktree-finality-reliability-2026-06-19.json` | true | machine-readable evidence |

## Required Artifact Manifest

The Work-Order Fulfillment Manifest above is the required artifact manifest
for this tranche.

## Pre-Flight Checks

Before implementation, Codex must run:

- pre-dispatch autorun gate on `5077cea5..HEAD`;
- dispatch commit steward preflight;
- dispatch pre-commit hook;
- pre-implementation autorun from the committed dispatch head.

## Write Ownership

Codex owns only the GGL-T2 dispatch, hook/finality source change, focused
tests, completion/evidence, closure conversion, and separate session-sync paths
named in this work order. Runtime, provider, public-sync, CVF Web, Model
Gateway, MCP execution behavior, queue/daemon, and direct interception surfaces
remain outside write ownership.

## Execution Plan

1. Repair and commit this GC-018/work order dispatch packet.
2. Run pre-implementation from the dispatch commit.
3. Update `.githooks/pre-commit` to rely on the runner default.
4. Update autorun finality so Git status stdout and stderr are separated.
5. Add focused tests for hook invocation and stderr-safe finality.
6. Run focused tests, worker-return fast gate, implementation steward, and
   pre-closure gates.
7. Convert closure artifacts and keep protected session sync separate.

## Review Gate

Codex must self-review at least these cases: hook invocation no longer contains
`--serial`, hook runner still supports explicit `--serial`, stderr-only Git
diagnostics do not fail clean finality, dirty stdout fails finality, and
non-zero Git status fails closed.

## Closure Checklist

- [x] Focused hook/finality tests pass.
- [x] Worker-return fast gate passes.
- [x] Implementation steward passes.
- [x] Pre-commit hook passes.
- [x] Pre-closure autorun passes on a committed range.
- [x] Completion review and evidence JSON include exact changed-set evidence.
- [x] No runtime/provider/live/public/direct-interception/universal-control
      claim is introduced.

## Return Conditions

Return to orchestrator instead of implementing if source verification fails,
pre-dispatch fails outside allowed dispatch repair, required hook/autorun owner
symbols are absent, or the tranche would need runtime/profile/provider/live/
public-sync/direct-interception scope.

## Worker Autonomy / No-Question Rule

Within the authorized hook/finality/test/completion/evidence boundary, Codex
must handle machine-check failures and repeat the relevant validations
autonomously.
Escalation applies only outside allowed scope, for claim-boundary change,
parked runtime/provider/public/interception scope, or secrets/quota.

## Operator Checkpoint

Human checkpoint is required for checker removal, local hook bypass, runtime
profile expansion, arbitrary command execution, EDIT/COMMIT execution,
provider/live call, public-sync, queue/daemon, CVF Web action execution, direct
IDE/shell/git/filesystem interception, wrapper/proxy enforcement, or universal
governed-coding claim.

## Closure Quality Gate

Before any closure claim:

- Roadmap-to-work-order trace rows must be resolved to PASS, N/A with reason,
  or BLOCKED.
- Completion review must include Machine Closure Package and Public Export
  Disposition.
- Agent Operation Trace manifest must match the implementation/closure changed
  set.
- Worktree must be clean or explicitly N/A with reason for untracked files.
- No runtime/provider/live/public/direct-interception/universal-control claim
  may be introduced.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 status | `docs/baselines/CVF_GC018_GGL_T2_GIT_HOOK_LANE_AND_WORKTREE_FINALITY_RELIABILITY_2026-06-19.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GGL_T2_GIT_HOOK_LANE_AND_WORKTREE_FINALITY_RELIABILITY_COMPLETION_2026-06-19.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Material commit | GGL-T2 implementation | `02678968` | PASS |
| Material handoff bridge | active handoff pointer bridge | `96a3611b` | PASS |
| Evidence JSON | `docs/reviews/evidence/ggl-t2-git-hook-lane-and-worktree-finality-reliability-2026-06-19.json` | status closed bounded | PASS |
| Roadmap state | N/A with reason: no roadmap changed | no roadmap path in closure set | N/A with reason |
| Registry JSON | BLOCKED with reason: no registry JSON mutation authorized | no registry JSON path changed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown mutation authorized | no registry Markdown path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: repo-local hook/finality evidence only | no external digest consumed | N/A with reason |
| System loop interlock | N/A with reason: no loop registry change | no interlock path changed | N/A with reason |
| Public export | private provenance only | `DEFERRED_PRIVATE_ONLY` | PASS |
| Session continuity | active session source/aggregate and handoff | separate post-closure session sync required | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
| --- | --- | --- |
| receiptEvidence | N/A with reason: this tranche does not create execution-control receipts | PASS |
| actionEvidence | focused tests, direct hook output, worker-return fast gate, implementation steward, material commit hook, and pre-closure output | PASS |
| hookDefault | installed pre-commit uses runner default without `--serial` | PASS |
| stderrPolicy | warning-only Git status stderr is diagnostic-only | PASS |
| failurePolicy | dirty stdout and non-zero Git status fail closed | PASS |
| claimBoundary | no runtime/provider/public/direct-interception/universal-control claim | PASS |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | GGL-T2 dispatch authoring, 2026-06-19 |
| Working directory | repository root |
| Command or tool surface | PowerShell, apply_patch, governance gates |
| Target paths | GGL-T2 GC-018 and work order |
| Allowed scope source | operator request to continue processing finding; active session next allowed move |
| Before status evidence | base `5077cea5`; clean worktree confirmed: `git status --short` showed no changed paths and only a host Git global ignore warning |
| After status evidence | GGL-T2 dispatch artifacts added for source-verified implementation |
| Diff evidence | `git diff --name-status 5077cea5..HEAD` before dispatch commit |
| Approval boundary | dispatch authoring only; material implementation starts after pre-implementation |
| Claim boundary | no runtime/profile/provider/live/public/direct-interception/universal-control claim |
| Agent type | single-agent multi-role |
| Invocation ID | `ggl-t2-dispatch-codex-2026-06-19` |
| Expected manifest | N/A with reason: dispatch artifact authoring only; future implementation deliverables are listed in Work-Order Fulfillment Manifest |
| Actual changed set | N/A with reason: dispatch artifact authoring only; changed set is checked by pre-dispatch range and commit steward |
| Manifest delta | N/A with reason: dispatch artifact authoring only; no material execution manifest is claimed in dispatch phase |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance control-plane reliability optimization.
Public-sync is not authorized.

## Claim Boundary

GGL-T2 may prove only bounded local hook-lane latency reliability and
stderr-safe closure finality with unchanged checker coverage. It does not prove
runtime execution governance, provider behavior, hosted freshness, public
readiness, production readiness, release readiness, universal speedup, or
universal governed-coding control.
