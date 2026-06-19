# CVF Agent Work Order - Delta-T4A Approval-Backed Mutating Profile Boundary For Codex

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

Date: 2026-06-19

docType: work_order

Batch ID: DELTA-T4A

Owner: Codex dispatcher, implementer, reviewer, closer, and session-sync actor

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `5c718d46`

executionBaseHead: `22f35116`

closureBaseHead: `136b9095`

rawMemoryReleased: false

## Dispatch Prompt Envelope

Role: Codex single-agent multi-role executor. Keep dispatch authoring,
implementation/review, closure conversion, and protected session sync as
separate evidence phases.

Mission: implement Delta-T4A as one approval-backed mutating profile for
`cvf-governed-exec`. The only authorized mutation is a fixed workspace-local
approval marker write after durable Delta-T1 preflight, Delta-T2 consumption,
Delta-T3 execution intent, and Delta-T4A approval evidence.

Do not add arbitrary command passthrough, shell execution, env overrides, npm
scripts, EDIT/COMMIT profiles, provider calls, public-sync, queue, daemon, IDE
interception, direct filesystem interception, or universal enforcement claims.

Required first actions: resolve session startup, read this work order and the
matching GC-018, source-verify every named runtime symbol, run pre-dispatch,
commit dispatch, sync dispatch continuity, then run pre-implementation before
runtime edits.

Completion contract: focused and full tests/build plus a secret-safe local
binary smoke pass; completion review and evidence JSON record exact changed
sets and bounded claims; closure and session sync remain phase-separated.

## Purpose

Implement the smallest useful Delta-T4A mutation boundary after Delta-T3:
approval-backed wrapper-owned execution for a single fixed marker-write profile.

## Required First Reads

| Artifact | Required use |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | current mode and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | machine-readable continuity |
| `AGENT_HANDOFF_V20_2026-06-19.md` | active handoff and parked boundaries |
| matching Delta-T4A GC-018 | exact authorization and claim boundary |
| Delta-T1, Delta-T2, and Delta-T3 completion reviews | predecessor contracts and residual risk |
| `docs/reference/agent_workspace/README.md` | Local Workspace Runtime front door |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | runtime expansion boundary |
| `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | runtime/MCP claim routing boundary |

## Scope / Target / Owner Boundary

Target: one approval policy module, one fixed mutating profile, launcher wiring,
focused tests, completion review, and evidence JSON.

Owner boundary: Delta-T1/T2 contracts, Governance CLI v2.2, Model Gateway,
CVF Web, generated workspace state, provider runtime, public-sync, arbitrary
commands, EDIT/COMMIT, and external interception remain outside this work
order.

Risk ceiling: R2 local implementation. The only allowed mutation is a
workspace-local marker file at a profile-owned fixed path in test/smoke
workspaces.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| intake summary | operator accepted the recommendation to continue Delta Execution Control with a narrow T4A boundary |
| scope classification | bounded Local Workspace Runtime mutating profile |
| risk sensitivity | R2 because this tranche owns a real mutation boundary even though the mutation is fixed and workspace-local |
| selected role route | `SINGLE_AGENT_MULTI_ROLE` |
| role separation basis | Codex separates dispatch, implementation, adversarial review, closure, and session-sync evidence phases |
| escalation condition | arbitrary command, caller-supplied target, shell/interpreter escape, EDIT/COMMIT, provider/live, public-sync, workspace-state mutation, daemon/queue, or broader enforcement claim |

## Agent Roles

| Role | Actor | Responsibility |
| --- | --- | --- |
| Dispatcher | Codex | author, source-verify, gate, and commit dispatch packet |
| Implementer | Codex | implement only allowed modular runtime/test scope |
| Reviewer / closer | Codex | adversarial self-review using repo-visible tests, diffs, and gates |
| Session-sync actor | Codex | update protected continuity in separate commits |
| Operator | Human | authorize any forbidden scope expansion |

## Authority Chain

| Level | Artifact | Status |
| --- | --- | --- |
| Operator authorization | current request on 2026-06-19 | ACCEPTED for Delta-T4A dispatch and bounded implementation |
| Active session | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Delta-T4A accepted material pending closure at closure base |
| Active handoff | `AGENT_HANDOFF_V20_2026-06-19.md` | Delta-T4A accepted material pending closure at closure base |
| Delta-T1 prerequisite | `docs/reviews/CVF_DELTA_T1_GOVERNANCE_ACTION_PREFLIGHT_RECEIPT_COMPLETION_2026-06-19.md` | `CLOSED_PASS_BOUNDED` |
| Delta-T2 prerequisite | `docs/reviews/CVF_DELTA_T2_GOVERNANCE_ACTION_RECEIPT_CONSUMPTION_COMPLETION_2026-06-19.md` | `CLOSED_PASS_BOUNDED` |
| Delta-T3 prerequisite | `docs/reviews/CVF_DELTA_T3_GOVERNED_COMMAND_LAUNCHER_COMPLETION_2026-06-19.md` | `CLOSED_PASS_BOUNDED` |
| Composition proof prerequisite | `docs/reviews/CVF_MCP_MODEL_GATEWAY_COMPOSITION_PROOF_COMPLETION_2026-06-19.md` | `CLOSED_PASS_BOUNDED` |
| EKA-R1 prerequisite | `docs/reviews/CVF_EKA_R1_EXTERNAL_KNOWLEDGE_INTAKE_ROUTING_GUARD_COMPLETION_2026-06-19.md` | `CLOSED_PASS_BOUNDED` |
| GC-018 | `docs/baselines/CVF_GC018_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_2026-06-19.md` | `CLOSED_PASS_BOUNDED` |
| Roadmap | N/A with reason: Delta-T4A follows active-session operator authorization, not a numbered roadmap tranche | N/A with reason |

## Agent Handoff Contract Control Block

| Field | Disposition |
| --- | --- |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one-agent-many-roles: Codex holds dispatcher, implementer, reviewer, closer, and session-sync roles across distinct phases |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatch=`5c718d46`; execution=`22f35116`; closure=`136b9095` |
| changedSetScope(phase) | dispatch baseline/work order; implementation named MCP source/tests/completion/evidence; closure status conversion; protected continuity only in session-sync |
| traceScope(phase, actor) | Codex records exact phase-local manifests, commands, and commit anchors |
| commitOwner(phase) | Codex for every phase |
| crossBatchIsolation | one Delta-T4A batch in a clean worktree; no concurrent batch mixing |
| nextMoveSurfaces | update only in separate session-sync commits after dispatch/material/closure as required |
| closerDesignation | Codex is designated closer |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
| --- | --- |
| Role separation ledger | dispatch author -> implementation worker -> adversarial reviewer -> closer -> session-sync steward |
| Evidence basis independence | each later role rereads committed source/diff and reruns its matching gates |
| Self-review challenge | prove the mutating runner is unreachable before approval and cannot change caller-selected files |
| Commit choreography | dispatch, dispatch sync, material, accepted-material sync, closure, final sync |
| Forbidden shortcut | no combined material/session commit and no closure claim from uncommitted changes |
| Gate sequence | pre-dispatch -> dispatch commit -> dispatch sync -> pre-implementation -> tests/review -> material commit -> closure -> session sync -> pre-push |
| Escalation conditions | fresh human authorization for arbitrary/mutating command expansion, shell/interpreter, EDIT/COMMIT, risk or claim expansion, provider/live, public-sync, queue/daemon, or external interception |

## Workspace Two-Layer Control Block

| Field | Disposition |
| --- | --- |
| targetLayer | `CVF_LOCAL_WORKSPACE_RUNTIME` |
| operatorSurface | N/A with reason: no CVF Web UI or dashboard change |
| agentExecutionSurface | `cvf-governed-exec` static approval-backed marker-write profile only |
| sourceOfTruth | T1 persisted audit, T2 one-time marker, T3 execution receipt, and T4A approval evidence |
| mutationBoundary | modular MCP package source/test plus user-local execution/approval receipts outside repo |
| receiptBoundary | execution receipt proves only wrapper-owned marker-write profile admission/result |
| forbiddenConflationCheck | wrapper execution does not prove direct IDE/shell/git/filesystem interception |

## Agent Workspace Design Control Block

| Field | Disposition |
| --- | --- |
| Workspace purpose | add the first bounded approval-backed mutation path to Local Workspace Runtime |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Storage class | MCP runtime source/test; user-local audit/consumption/execution/approval receipts outside repo; dated execution evidence |
| Handoff fields | Agent Handoff Contract Control Block above |
| State ownership | no generated workspace state, queue, inbox, lane, or dashboard mutation |
| Guard owner | existing T1/T2/T3 owners plus new T4A approval policy and focused tests |
| Build boundary | one fixed marker-write profile only; no UI, queue, provider proof, public-sync, registry edits, EDIT/COMMIT, arbitrary command, or readiness work |

## Runtime Expansion Control Block

| Field | Disposition |
| --- | --- |
| runtimeMode | `RUNTIME_IMPLEMENTATION_REQUESTED` |
| contractSource | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` |
| frontDoor | `docs/reference/agent_workspace/README.md` |
| stateSourceOfTruth | existing Delta audit directory plus T2/T3/T4A receipt subdirectories; no workspace-state mutation |
| queueBoundary | N/A with reason: no queue, scheduler, worker, or daemon |
| operatorViewBoundary | N/A with reason: no Web UI |
| providerBoundary | no provider or Model Gateway call |
| publicBoundary | private-only; no public-sync |
| guardOwner | T1 persisted audit, T2 atomic marker, T3 intent/final receipt, T4A approval evidence, package tests, and governance gates |

## External Knowledge Intake Routing

| Required row | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | Runtime/MCP claim must cite current runtime proof, MCP boundary, and work-order source verification before implementation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_workspace_runtime_boundary.py` |
| Owner surface | this Delta-T4A work order |
| Disposition | `DO_NOW` only for bounded wrapper-owned marker mutation; `BLOCKED_UNTIL_CVF_PROOF` for universal or external interception claims |
| Claim boundary | no universal governed-coding, external interception, provider/live, public, production, release, or readiness claim |

## Delta-T4A Execution Control Block

| Field | Disposition |
| --- | --- |
| actionClass | `RUN` only |
| profiles | existing: `git-status`, `git-diff-check`; new: `approval-marker-write`; still forbidden: npm scripts, arbitrary commands, EDIT, COMMIT |
| mutating target | fixed workspace-relative marker path owned by `approval-marker-write` |
| action binding | deterministic canonical profile/executable/args/workspace-relative cwd/target string |
| preflight owner | existing `preflightGovernanceAction` |
| consumption owner | existing `consumeGovernanceActionReceipt` |
| execution-intent owner | existing Delta-T3 create-exclusive receipt store |
| approval owner | new T4A approval policy/evidence module |
| process owner | injected runner with production direct-process adapter and `shell:false` |
| cwd owner | existing real workspace root plus existing real child cwd check |
| output owner | bounded capture; known-pattern redaction; no raw output persistence |
| failure posture | fail closed before runner on validation, preflight, consumption, intent, approval, or target mismatch |
| claim boundary | wrapper-owned marker write only; no external interception claim |

## Source Verification Block

| Claimed item | Verification type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Delta-T3 profile registry currently contains only `git-status` and `git-diff-check`. | VALUE_SET | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 26-29 and 42-55 | `GOVERNED_COMMAND_PROFILE_IDS`; `getGovernedCommandProfile` | Delta-T3 launcher | ACCEPT |
| Delta-T3 profile shape owns id, executable, args, and risk level. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 32-37 | `GovernedCommandProfile` | Delta-T3 launcher | ACCEPT |
| Direct runner uses `spawn` with exact args and `shell:false`. | LITERAL_INVARIANT | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 88-104 | `shell` | Delta-T3 runner | ACCEPT |
| Launcher resolves workspace/cwd by real paths inside the workspace root. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 212-226 | `resolveWorkspaceCwd` | Delta-T3 launcher | ACCEPT |
| Launcher calls Delta-T1 preflight before Delta-T2 consumption. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 255-278 | `preflightGovernanceAction`; `consumeGovernanceActionReceipt` | `launchGovernedCommand` | ACCEPT |
| Launcher persists Delta-T3 execution intent before runner invocation. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 299-339 | `beginExecution`; `dependencies.runner.run` | `launchGovernedCommand` | ACCEPT |
| Launcher finalizes execution receipt after runner returns. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 342-368 | `finalizeExecution` | `launchGovernedCommand` | ACCEPT |
| Delta-T1 source-declares `RUN`, `EDIT`, and `COMMIT`; T4A selects only `RUN`. | VALUE_SET | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts` | lines 30-34 | `PREFLIGHT_ACTION_CLASSES` | Delta-T1 preflight | ACCEPT |
| Guard request context supports target files, mutation count, mutation budget, scope, and metadata. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/types.ts` | lines 27-40 | `GuardRequestContext` | guard runtime types | ACCEPT |
| Delta-T2 consumer validates one matching receipt and exposes `executionAdmissionEligible`. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-receipt-consumer.ts` | lines 139-260 | `consumeGovernanceActionReceipt`; `executionAdmissionEligible` | Delta-T2 receipt consumer | ACCEPT |
| Delta-T2 marker store uses create-exclusive marker files. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-receipt-consumption.store.ts` | lines 73-91 | `claimReceipt` | receipt consumption store | ACCEPT |
| Delta-T3 execution store persists admitted/finalized receipts and forces external interception false. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts` | lines 73-127 | `beginExecution`; `finalizeExecution` | governed execution store | ACCEPT |
| Thin CLI currently accepts only profile, workspace, cwd, and JSON flags. | VALUE_SET | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts` | lines 18-53 | `parseGovernedExecArgs` | `cvf-governed-exec` CLI | ACCEPT |
| Package manifest publishes the governed exec binary. | VALUE_SET | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package.json` | lines 7-10 | `cvf-governed-exec` | npm package manifest | ACCEPT |
| Runtime expansion work orders must include runtime and workspace control blocks. | LITERAL_INVARIANT | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | lines 57-72 and 102-109 | `Required Runtime-Readiness Fields`; `Work Order Requirement` | runtime expansion readiness contract | ACCEPT |

## Current Runtime Freshness Verification

Dispatch reread material source after EKA-R1 closure at HEAD `5c718d46`.
Delta-T3 currently exposes only two read-only Git profiles and a strict CLI.
No T4A approval module, mutating profile, or marker-write target exists yet.
Delta-T1/T2 owners, dependencies, lockfiles, Model Gateway, CVF Web,
provider/live, public-sync, queue, and workspace state remain outside this
dispatch.

## New Doc-Only Fields

| Proposed field or symbol | Disposition |
| --- | --- |
| `approval-marker-write` | new Delta-T4A profile id authorized by GC-018 |
| `cvf.delta.mutatingProfileApprovalPolicy.v1` | new approval policy/evidence contract |
| `MutatingProfileApprovalPolicy`, `MutatingProfileApprovalRecord`, `MutatingProfileApprovalVerdict` | new local approval-policy surface |
| `MUTATING_FIXED_WORKSPACE_FILE` | new profile-kind classification |
| `approvalBackedMutationProved` | new bounded response/evidence marker true only for the wrapper-owned marker profile |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
| --- | --- |
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Stable row | `MCP-GW-001` |
| Parent gateway row | `MGW-001`; retained for stable-row checker vocabulary |
| Coverage status | `COVERED_SOURCE_BACKED` |
| Delta-T4A use | approval-backed mutating wrapper boundary after T1/T2/T3 |
| Deferred legacy value | arbitrary/mutating command families, EDIT/COMMIT, and wider interception remain separate tranches |

## Roadmap-To-Work-Order Trace Matrix

Applicability: N/A with reason: no numbered roadmap owns Delta-T4A. Trace chain
is active session -> operator authorization -> Delta-T1/T2/T3 closure ->
MCP composition proof -> EKA-R1 -> fresh GC-018 -> this work order.

| Upstream requirement | Work order section | Deliverable | Verification | Closure state |
| --- | --- | --- | --- | --- |
| approval-backed mutation | Delta-T4A Execution Control Block | approval policy plus fixed marker profile | focused approval/target tests | PASS |
| no arbitrary shell | Scope and control blocks | static profile registry and direct runner | negative CLI/profile tests | PASS |
| durable evidence | Delta-T4A Execution Control Block | T1/T2/T3 plus T4A approval/evidence | temp-directory readback | PASS |
| no universal claim | Claim Boundary | bounded response/completion language | text and diff review | PASS |
| source verification and autorun | source/pre-flight blocks | command evidence | governance gates | PASS |

## Write Ownership

Codex may create or modify only:

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.test.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.test.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/mutating-profile-approval.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/mutating-profile-approval.test.ts`
- matching Delta-T4A GC-018, work order, completion review, and evidence JSON;
- protected session continuity only in separate session-sync commits.

Forbidden: dependencies/lockfiles, Delta-T1/T2 source/tests, Gamma contracts,
Governance CLI v2.2, Model Gateway, CVF Web, workspace state, queue/runtime
skeleton, governance checkers, public-sync, provider files, credential files,
and unrelated paths.

## Worker Autonomy / No-Question Rule

If a machine gate fails inside the Allowed scope, Codex must repair the packet
or implementation and rerun the failed gate. Escalation is reserved for changes
that exceed Allowed scope, change the claim boundary, release a parked
prerequisite, add provider/live or public-sync work, consume secrets or quota,
touch forbidden paths, or perform destructive or irreversible action.

## Review Gate

Before material acceptance, Codex must reread the changed source, run the
focused T4A tests, run the full MCP package tests, run the MCP package build,
run a bounded temporary-workspace smoke proof, inspect the exact diff, and
record any reviewer finding in the completion review.

## Return-To-Orchestrator Conditions

Closure is valid only when every required artifact exists, all acceptance
criteria are resolved as PASS, PASS_BOUNDED, or N/A with reason, and the
material range has focused/full test evidence.

Return `BLOCKED_WITH_REASON` if implementation requires arbitrary command
construction, caller-selected target paths, shell/interpreter execution,
EDIT/COMMIT semantics, provider/live calls, public-sync, queue/daemon work, or
any forbidden path.

## Operator Checkpoint

Human approval is required for any expansion beyond the single fixed
`approval-marker-write` profile, any provider/live or public-sync work, any
destructive or irreversible action, any direct IDE/shell/git/filesystem
interception claim, and any universal governed-coding claim.

## Closure Checklist

- [x] Dispatch packet includes source verification for every existing runtime
  symbol named in the implementation instructions.
- [x] Work order includes Agent Handoff, Workspace, Runtime Expansion, External
  Knowledge Intake Routing, and Worker Autonomy control blocks.
- [x] Allowed scope is limited to one fixed approval-backed marker-write
  profile.
- [x] Forbidden scope names arbitrary commands, EDIT/COMMIT, provider/live,
  public-sync, queue/daemon, external interception, and universal control.
- [x] Closure requires completion review, evidence JSON, focused/full tests,
  build, smoke proof, and governance gates.

## Work-Order Fulfillment Manifest

| Artifact | Closure result |
| --- | --- |
| approval policy module | PASS: approval record/verdict validation, target allowlist, expiry, profile binding |
| launcher module | PASS: fixed mutating profile, canonical binding, admission sequence, approval gate, injected runner |
| focused tests | PASS: missing approval, expired approval, target mismatch, runner unreachable before approval, fixed target mutation |
| CLI | PASS: remains strict; no arbitrary executable, args, env, shell, EDIT, or COMMIT |
| completion/evidence | PASS: exact changed set, assertions, commands, and bounded closure claim |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
| --- | --- | --- | --- |
| full admission precedes process | T1 audit, T2 marker, T3 intent, T4A approval before runner | ordering and failure-injection tests | PASS |
| arbitrary execution unavailable | strict profile registry/parser | unknown profile and extra args reject | PASS |
| marker target fixed | no caller target path | source, tests, and smoke readback | PASS |
| approval failure blocks runner | runner not called | missing-policy and missing-approval tests | PASS |
| failure evidence is durable | failed approval/runner finalizes receipt | focused failure tests | PASS |
| execution claim stays bounded | wrapper marker true; interception false | response and marker assertions | PASS |

## Required Artifact Manifest

| Path | Required at closure | Owner | Purpose |
| --- | --- | --- | --- |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/mutating-profile-approval.ts` | YES | Codex | approval policy/evidence module |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/mutating-profile-approval.test.ts` | YES | Codex | focused approval proof |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | YES | Codex | launcher wiring |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.test.ts` | YES | Codex | focused deterministic proof |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts` | YES | Codex | strict CLI boundary if approval flag is added |
| `docs/reviews/CVF_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_COMPLETION_2026-06-19.md` | YES | Codex | completion review |
| `docs/reviews/evidence/delta-t4a-approval-backed-mutating-profile-boundary-2026-06-19.json` | YES | Codex | machine-readable evidence |

## Pre-Flight Checks

Run from repository root:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base 5c718d46 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base 5c718d46 --head HEAD --enforce
```

After dispatch commit and separate dispatch continuity sync, run
pre-implementation from the refreshed execution base before runtime edits.

## Execution Instructions

1. Re-read every source symbol in the Source Verification Block.
2. Add a small approval-policy module for profile-bound, target-bound,
   time-bounded approval evidence.
3. Add only the `approval-marker-write` profile and keep existing T3 profiles
   unchanged.
4. Ensure the profile writes only one fixed marker target inside the resolved
   workspace root.
5. Generate the exact canonical action from profile, executable, args, cwd, and
   target path.
6. Persist T1 preflight and require its ALLOW governed claim.
7. Atomically consume the matching T2 receipt with the same action binding.
8. Persist a create-exclusive T3 execution intent before approval and runner
   invocation.
9. Require T4A approval verdict before invoking the runner.
10. Invoke the exact executable/args with direct-process semantics and no shell,
    detached mode, env override, or arbitrary argument extension.
11. Finalize the receipt after success or failure; never persist stdout/stderr.
12. Bound captured output and redact known credential patterns in the response.
13. Run focused/full tests, build, binary smoke, reviewer-fast, closure gates,
    and exact-range commit choreography.

## Execution Plan

1. Commit and session-sync the source-verified dispatch packet.
2. Recompute pre-implementation gates from the refreshed execution base.
3. Implement approval policy/evidence and fixed marker target validation.
4. Wire the approval gate into the launcher before runner invocation.
5. Add focused adversarial tests and bounded smoke proof.
6. Run focused/full tests, build, and bounded local binary smoke.
7. Author completion/evidence, self-review exact manifests, and commit material.
8. Convert closure artifacts, run closure/pre-push gates, and sync continuity.

## Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC1 | Exactly one new mutating profile exists: `approval-marker-write`. |
| AC2 | No process starts before T1 ALLOW, T2 consumption, T3 durable intent, and T4A approval verdict. |
| AC3 | The profile writes only the fixed profile-owned marker file inside the workspace root. |
| AC4 | Missing, expired, wrong-profile, wrong-target, or malformed approval blocks before runner. |
| AC5 | CLI and launcher still reject arbitrary executable, caller-supplied args, env override, shell, EDIT, and COMMIT. |
| AC6 | Approval and execution evidence stores only bounded ids, hashes, timestamps, status, and diagnostics. |
| AC7 | Runner failures finalize as failed and propagate a non-zero launcher result. |
| AC8 | Known credential patterns are redacted from returned stdout/stderr. |
| AC9 | Focused tests, full MCP tests, build, binary smoke, reviewer-fast, and governance gates pass. |
| AC10 | No provider/live/public/queue/workspace-state/external-interception or universal governed-coding claim is added. |

## Evidence Requirements

Run from `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER`:

```powershell
npx vitest run src/cli/mutating-profile-approval.test.ts src/cli/governed-command-launcher.test.ts --reporter verbose
npm run test:run
npm run build
```

Run from repository root:

```powershell
git diff --check
python governance/compat/run_worker_return_fast_gate.py --pytest-target governance/compat/test_check_external_knowledge_intake_routing.py
python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <executionBaseHead> --head HEAD
```

Binary smoke must run only in a temporary workspace and must use a temporary
`CVF_MCP_DELTA_AUDIT_DIR`. Do not run against the provenance repo as the target
workspace for the mutating profile.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex closer |
| Provider or surface | local provenance workspace |
| Session or invocation | `delta-t4a-closure-codex-2026-06-19` |
| Working directory | repository root |
| Command or tool surface | PowerShell, apply_patch, governance gates |
| Target paths | this work order, matching GC-018, completion review, and evidence JSON |
| Allowed scope source | user authorization to follow Delta continuation recommendation |
| Before status evidence | accepted-material session sync `136b9095` |
| After status evidence | closure artifacts converted to `CLOSED_PASS_BOUNDED` |
| Diff evidence | `git diff --name-status`; `git diff --check`; closure gates |
| Approval boundary | one fixed approval-backed marker-write profile only |
| Claim boundary | no arbitrary command, EDIT/COMMIT, provider/live, public-sync, queue, daemon, interception, or universal governed coding |
| Agent type | single-agent multi-role Codex closure phase |
| Invocation ID | `delta-t4a-approval-backed-mutating-profile-boundary-closure-codex-2026-06-19` |
| Expected manifest | `docs/baselines/CVF_GC018_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_2026-06-19.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_FOR_CODEX_2026-06-19.md`; `docs/reviews/CVF_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_COMPLETION_2026-06-19.md`; `docs/reviews/evidence/delta-t4a-approval-backed-mutating-profile-boundary-2026-06-19.json` |
| Actual changed set | `docs/baselines/CVF_GC018_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_2026-06-19.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_FOR_CODEX_2026-06-19.md`; `docs/reviews/CVF_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_COMPLETION_2026-06-19.md`; `docs/reviews/evidence/delta-t4a-approval-backed-mutating-profile-boundary-2026-06-19.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none planned |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Delta runtime tranche. Public-sync is not authorized.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| GC-018 baseline | `docs/baselines/CVF_GC018_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_2026-06-19.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Material implementation | MCP package source/tests and completion evidence | material commit `d2fc4f5b` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DELTA_T4A_APPROVAL_BACKED_MUTATING_PROFILE_BOUNDARY_COMPLETION_2026-06-19.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | N/A with reason: active-session/operator-derived tranche | no roadmap mutation | N/A with reason |
| Registry JSON | BLOCKED with reason: no corpus registry edit authorized | no registry path changed | BLOCKED with reason |
| Registry Markdown | BLOCKED with reason: no registry Markdown edit authorized | no registry path changed | BLOCKED with reason |
| External evidence digest | N/A with reason: no new external source consumed | repo-local sources only | N/A with reason |
| System loop interlock | N/A with reason: no queue/scheduler/loop added | no interlock mutation | N/A with reason |
| Evidence JSON | `docs/reviews/evidence/delta-t4a-approval-backed-mutating-profile-boundary-2026-06-19.json` | `status: PASS_BOUNDED` | PASS |
| Session continuity | active handoff and session state | accepted-material session sync `136b9095` | PASS |
| Provider/live proof | N/A with reason: no provider claim | no live provider command | N/A with reason |
| Public-sync | N/A with reason: not authorized | `DEFERRED_PRIVATE_ONLY` | N/A with reason |

## Claim Boundary

This work order authorizes only a bounded approval-backed wrapper mutation:
one fixed workspace-local marker-write profile after durable T1/T2/T3/T4A
controls. It does not make MCP mandatory, intercept direct IDE/shell/git or
filesystem actions, execute arbitrary commands, implement EDIT/COMMIT, run live
providers, public-sync, or establish universal governed-coding control.
