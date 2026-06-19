# CVF Agent Work Order - Delta-T3 Governed Command Launcher For Codex

Memory class: FULL_RECORD

Status: DISPATCH_READY_FOR_CODEX

Date: 2026-06-19

docType: work_order

Batch ID: DELTA-T3

Owner: Codex dispatcher, implementer, reviewer, closer, and session-sync actor

Commit mode: WORKER_MAY_COMMIT

dispatchBaseHead: `f50e2903`

executionBaseHead: `f50e2903`

closureBaseHead: `f50e2903`

rawMemoryReleased: false

## Dispatch Prompt Envelope

Role: Codex single-agent multi-role executor. Keep dispatch authoring,
implementation/review, closure conversion, and protected session sync as
separate evidence phases.

Mission: implement `cvf-governed-exec`, a bounded local command launcher that
can invoke only static CVF-owned non-destructive profiles after a durable
Delta-T1 ALLOW receipt, Delta-T2 atomic consumption, and Delta-T3 execution
intent persistence.

Do not add arbitrary command passthrough, shell execution, env overrides,
EDIT/COMMIT profiles, mutating commands, provider calls, public-sync, queue,
daemon, IDE interception, or universal enforcement claims.

Required first actions: resolve session startup, read this work order and the
matching GC-018, source-verify every named runtime symbol, run pre-dispatch,
commit dispatch, sync dispatch continuity, then run pre-implementation before
runtime edits.

Completion contract: focused and full tests/build plus a secret-safe local
binary smoke pass; completion review and evidence JSON record exact changed
sets and bounded claims; closure and session sync remain phase-separated.

## Purpose

Implement Delta-T3 as the first wrapper-owned execution path that composes the
existing Delta-T1 issuer and Delta-T2 consumer before a direct child process.

## Required First Reads

| Artifact | Required use |
| --- | --- |
| `CVF_SESSION_MEMORY.md` | current mode and next allowed move |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | machine-readable continuity |
| `AGENT_HANDOFF_V19_2026-06-15.md` | active handoff and parked boundaries |
| matching Delta-T3 GC-018 | exact authorization and claim boundary |
| Delta-T1 and Delta-T2 completion reviews | predecessor contracts and residual risk |
| `docs/reference/agent_workspace/README.md` | Local Workspace Runtime front door |
| `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | runtime expansion boundary |

## Scope / Target / Owner Boundary

Target: modular profile registry/launcher, execution receipt store, injected
process runner, thin CLI entrypoint, package bin registration, focused tests,
completion review, and evidence JSON.

Owner boundary: Delta-T1/T2 contracts, Governance CLI v2.2, Model Gateway,
CVF Web, generated workspace state, provider runtime, public-sync, mutating
commands, and external interception remain outside this work order.

Risk ceiling: R2 local implementation. Shipped profiles are R0/R1 and
non-destructive. No network authorization, credentials, quota, public action,
destructive action, or irreversible external action.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| intake summary | operator explicitly authorized continuing from Delta-T2 into Delta-T3 |
| scope classification | bounded Local Workspace Runtime command launcher |
| risk sensitivity | R2 because this tranche owns a real child-process boundary |
| selected role route | `SINGLE_AGENT_MULTI_ROLE` |
| role separation basis | Codex separates dispatch, implementation, adversarial review, closure, and session-sync evidence phases |
| escalation condition | arbitrary or mutating command, shell/interpreter escape, provider/live, public-sync, workspace-state mutation, daemon/queue, or broader enforcement claim |

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
| Operator authorization | current request on 2026-06-19 | ACCEPTED for Delta-T3 implementation |
| Active session | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Delta-T2 closed; launcher decision ready |
| Active handoff | `AGENT_HANDOFF_V19_2026-06-15.md` | Delta-T3 requires operator authorization now granted |
| Legacy absorption | `MCP-GW-001` in `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` | source-backed execution-control direction |
| Workspace authority | `docs/reference/agent_workspace/CVF_WORKSPACE_TWO_LAYER_ARCHITECTURE_STANDARD.md` | local MCP/CLI ingress uses guards and receipts |
| Delta-T1 prerequisite | `docs/reviews/CVF_DELTA_T1_GOVERNANCE_ACTION_PREFLIGHT_RECEIPT_COMPLETION_2026-06-19.md` | `CLOSED_PASS_BOUNDED` |
| Delta-T2 prerequisite | `docs/reviews/CVF_DELTA_T2_GOVERNANCE_ACTION_RECEIPT_CONSUMPTION_COMPLETION_2026-06-19.md` | `CLOSED_PASS_BOUNDED`; material `d3bf3594`; closure `22ad256e` |
| GC-018 | `docs/baselines/CVF_GC018_DELTA_T3_GOVERNED_COMMAND_LAUNCHER_2026-06-19.md` | DISPATCH_READY |
| Roadmap | N/A with reason: Delta-T3 follows active-session operator authorization, not a numbered roadmap tranche | N/A with reason |

## Agent Handoff Contract Control Block

| Field | Disposition |
| --- | --- |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one-agent-many-roles: Codex holds dispatcher, implementer, reviewer, closer, and session-sync roles across distinct phases |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatch=`f50e2903`; execution=post-dispatch session-sync HEAD; closure=post-material session-sync HEAD |
| changedSetScope(phase) | dispatch baseline/work order; implementation named MCP source/tests/package/completion/evidence; closure status conversion; protected continuity only in session-sync |
| traceScope(phase, actor) | Codex records exact phase-local manifests, commands, and commit anchors |
| commitOwner(phase) | Codex for every phase |
| crossBatchIsolation | one Delta-T3 batch in a clean worktree; no concurrent batch mixing |
| nextMoveSurfaces | update only in separate session-sync commits after dispatch/material/closure as required |
| closerDesignation | Codex is designated closer |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
| --- | --- |
| Role separation ledger | dispatch author -> implementation worker -> adversarial reviewer -> closer -> session-sync steward |
| Evidence basis independence | each later role rereads committed source/diff and reruns its matching gates |
| Self-review challenge | prove runner is unreachable before durable admission and no arbitrary process surface exists |
| Commit choreography | dispatch, dispatch sync, material, accepted-material sync, closure, final sync |
| Forbidden shortcut | no combined material/session commit and no closure claim from uncommitted changes |
| Gate sequence | pre-dispatch -> dispatch commit -> dispatch sync -> pre-implementation -> tests/review -> material commit -> closure -> session sync -> pre-push |
| Escalation conditions | operator checkpoint for arbitrary/mutating command, shell/interpreter, EDIT/COMMIT, risk or claim expansion, provider/live, public-sync, queue/daemon, or external interception |

## Workspace Two-Layer Control Block

| Field | Disposition |
| --- | --- |
| targetLayer | `CVF_LOCAL_WORKSPACE_RUNTIME` |
| operatorSurface | N/A with reason: no CVF Web UI or dashboard change |
| agentExecutionSurface | `cvf-governed-exec` static-profile wrapper only |
| sourceOfTruth | T1 persisted audit, T2 one-time marker, and T3 execution receipt |
| mutationBoundary | modular MCP package source/test plus user-local execution receipt outside repo |
| receiptBoundary | execution receipt proves only wrapper-owned child-process admission/result |
| forbiddenConflationCheck | wrapper execution does not prove direct IDE/shell/git/filesystem interception |

## Agent Workspace Design Control Block

| Field | Disposition |
| --- | --- |
| Workspace purpose | add a bounded wrapper-owned command execution path to Local Workspace Runtime |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`; `docs/reference/agent_workspace/README.md`; `docs/reference/agent_workspace/CVF_AGENT_INTERACTION_WORKSPACE_DESIGN_STANDARD.md`; `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` |
| Front door | `docs/reference/agent_workspace/README.md` |
| Storage class | MCP runtime source/test; user-local audit/consumption/execution receipts outside repo; dated execution evidence |
| Handoff fields | Agent Handoff Contract Control Block above |
| State ownership | no generated workspace state, queue, inbox, lane, or dashboard mutation |
| Guard owner | existing T1/T2 owners plus new T3 execution receipt, focused tests, and governance gates |
| Build boundary | static non-destructive RUN launcher only; no UI, queue, provider proof, public-sync, registry edits, mutating command, or readiness work |

## Runtime Expansion Control Block

| Field | Disposition |
| --- | --- |
| runtimeMode | `RUNTIME_IMPLEMENTATION_REQUESTED` |
| contractSource | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` |
| frontDoor | `docs/reference/agent_workspace/README.md` |
| stateSourceOfTruth | existing Delta audit directory plus T2/T3 receipt subdirectories; no workspace-state mutation |
| queueBoundary | N/A with reason: no queue, scheduler, worker, or daemon |
| operatorViewBoundary | N/A with reason: no Web UI |
| providerBoundary | no provider or Model Gateway call |
| publicBoundary | private provenance only; no public-sync |
| guardOwner | T1 persisted audit, T2 atomic marker, T3 intent/final receipt, package tests, and governance gates |

## Delta-T3 Execution Control Block

| Field | Disposition |
| --- | --- |
| actionClass | `RUN` only |
| profiles | `git-status`, `git-diff-check`, `npm-test`, `npm-build`, `npm-check` |
| action binding | deterministic canonical profile/executable/args/workspace-relative cwd string |
| preflight owner | existing `preflightGovernanceAction` |
| consumption owner | existing `consumeGovernanceActionReceipt` |
| execution-intent owner | new create-exclusive Delta-T3 receipt store |
| process owner | injected runner with production direct-process adapter and `shell:false` |
| cwd owner | existing real workspace root plus existing real child cwd check |
| output owner | bounded capture; known-pattern redaction; no raw output persistence |
| failure posture | fail closed before runner on validation, preflight, consumption, or intent failure |
| claim boundary | wrapper-owned child process only; no external interception claim |

## Source Verification Block

| Claimed item | Verification type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Pure Delta-T1 preflight accepts injected engine/persistence. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts` | `preflightGovernanceAction` declaration | `preflightGovernanceAction` | Delta-T1 handler | ACCEPT |
| Delta-T1 RUN is a source-declared action class. | VALUE_SET | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts` | `PREFLIGHT_ACTION_CLASSES` | `RUN` | `PreflightActionClass` | ACCEPT |
| Pure Delta-T2 consumer accepts injected receipt store. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-receipt-consumer.ts` | `consumeGovernanceActionReceipt` declaration | `consumeGovernanceActionReceipt` | Delta-T2 handler | ACCEPT |
| Delta-T2 eligibility follows a successful one-time marker claim. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-receipt-consumer.ts` | successful return path | `executionAdmissionEligible` | `ReceiptConsumptionResponse` | ACCEPT |
| Receipt store uses one file per receipt and create-exclusive open. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-receipt-consumption.store.ts` | lines 66-91 | `markerPath`; `claimReceipt` | `JsonReceiptConsumptionStore` | ACCEPT |
| JSON audit adapter persists and reads request-filtered entries. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-file.adapter.ts` | lines 62-84 | `saveAuditEntry`; `getAuditEntries` | `JsonFileAdapter` | ACCEPT |
| Guard factory registers the current deterministic pipeline. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/index.ts` | lines 24-38 | `createGuardEngine` | guard runtime factory | ACCEPT |
| Known credential patterns have an existing redaction helper. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/tools/governance-action-preflight.ts` | `redactText` declaration | `redactText` | Delta-T1 secret handling | ACCEPT |
| MCP package manifest owns npm binary publication. | VALUE_SET | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package.json` | `bin` | `cvf-mcp-server` | npm manifest | ACCEPT |
| T2 closure names launcher execution as later separately authorized work. | LITERAL_INVARIANT | `docs/reviews/CVF_DELTA_T2_GOVERNANCE_ACTION_RECEIPT_CONSUMPTION_COMPLETION_2026-06-19.md` | `## Risk / Corrective Action` | `executionAdmissionEligible` | Delta-T2 completion | ACCEPT |

## New Doc-Only Fields

| Proposed field or symbol | Disposition |
| --- | --- |
| `cvf-governed-exec` | new Delta-T3 package binary authorized by GC-018 |
| `cvf.delta.governedCommandLauncher.v1` | new launcher result contract |
| `cvf.delta.governedExecutionReceipt.v1` | new durable execution receipt contract |
| `GovernedCommandProfile`, `GovernedCommandRunner`, `GovernedExecutionStore` | new modular Delta-T3 ports |
| `executionStarted`, `executionCompleted`, `externalInterceptionProved` | new bounded execution claim fields |

## Legacy Absorption Coverage Index Disposition

| Field | Disposition |
| --- | --- |
| Coverage index | `docs/reference/CVF_LEGACY_ABSORPTION_COVERAGE_INDEX_2026-06-13.md` |
| Stable row | `MCP-GW-001` |
| Parent gateway row | `MGW-001`; retained for stable-row checker vocabulary |
| Coverage status | `COVERED_SOURCE_BACKED` |
| Delta-T3 use | wrapper-owned preflight/consume/execute chain and durable execution receipt |
| Deferred legacy value | arbitrary/mutating command and wider interception remain separate tranches |

## Roadmap-To-Work-Order Trace Matrix

Applicability: N/A with reason: no numbered roadmap owns Delta-T3. Trace chain
is active session -> operator authorization -> Delta-T1/T2 closure -> fresh
GC-018 -> this work order.

| Upstream requirement | Work order section | Deliverable | Verification | Dispatch state |
| --- | --- | --- | --- | --- |
| receipt-gated execution | Delta-T3 Execution Control Block | modular governed launcher | focused sequence tests | READY |
| no arbitrary shell | Scope and control blocks | static profile registry and direct runner | negative parser/runner tests | READY |
| durable execution evidence | Delta-T3 Execution Control Block | intent/final receipt store | temp-directory readback | READY |
| no universal claim | Claim Boundary | bounded response/completion language | text and diff review | READY |
| source verification and autorun | source/pre-flight blocks | command evidence | governance gates | READY |

## Write Ownership

Codex may create or modify only:

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.test.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.test.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package.json`
- matching Delta-T3 GC-018, work order, completion review, and evidence JSON;
- protected session continuity only in separate session-sync commits.

Forbidden: dependencies/lockfiles, Delta-T1/T2 source/tests, Gamma contracts,
Governance CLI v2.2, Model Gateway, CVF Web, workspace state, queue/runtime
skeleton, governance checkers, public-sync, provider files, credential files,
and unrelated paths.

## Work-Order Fulfillment Manifest

| Artifact | Required result |
| --- | --- |
| launcher module | static profiles, canonical binding, admission sequence, injected runner |
| execution receipt store | create-exclusive intent plus atomic finalization |
| thin binary | strict parser, secret-safe JSON/text result, exit-code propagation |
| package manifest | additive `cvf-governed-exec` bin entry only |
| focused tests | success, every pre-run failure, cwd escape, exact invocation, failure receipt, redaction |
| completion/evidence | exact changed set, assertions, commands, and bounded closure claim |

## Required Artifact Manifest

| Path | Required at closure | Owner | Purpose |
| --- | --- | --- | --- |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | YES | Codex | modular launcher |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.test.ts` | YES | Codex | focused deterministic proof |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts` | YES | Codex | thin package binary |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts` | YES | Codex | durable intent/final receipt |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.test.ts` | YES | Codex | persistence proof |
| `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/package.json` | YES | Codex | binary publication |
| `docs/reviews/CVF_DELTA_T3_GOVERNED_COMMAND_LAUNCHER_COMPLETION_2026-06-19.md` | YES | Codex | completion review |
| `docs/reviews/evidence/delta-t3-governed-command-launcher-2026-06-19.json` | YES | Codex | machine-readable evidence |

## Pre-Flight Checks

Run from repository root:

```powershell
git rev-parse --short HEAD
git status --short
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch --base f50e2903 --head HEAD
python governance/compat/run_agent_commit_steward_preflight.py --mode dispatch --base f50e2903 --head HEAD --enforce
```

After dispatch commit and separate dispatch continuity sync, run
pre-implementation from the refreshed execution base before runtime edits.

## Execution Instructions

1. Re-read every source symbol in the Source Verification Block.
2. Implement a frozen static profile registry; reject unknown profiles.
3. Resolve real workspace and cwd paths and reject escape or missing paths.
4. Generate the exact canonical action from profile plus relative cwd.
5. Persist T1 preflight and require its ALLOW governed claim.
6. Atomically consume the matching T2 receipt with the same action binding.
7. Persist a create-exclusive T3 execution intent before invoking the runner.
8. Invoke the exact executable/args with direct-process semantics and no shell,
   detached mode, env override, or arbitrary argument extension.
9. Finalize the receipt after success or failure; never persist stdout/stderr.
10. Bound captured output and redact known credential patterns in the response.
11. Add a strict CLI parser exposing only profile, cwd, workspace, and JSON mode.
12. Run focused/full tests, build, binary smoke, reviewer-fast, closure gates,
    and exact-range commit choreography.

## Execution Plan

1. Commit and session-sync the source-verified dispatch packet.
2. Recompute pre-implementation gates from the refreshed execution base.
3. Implement the execution receipt store and frozen profile registry.
4. Implement the admission-sequenced launcher and thin CLI entrypoint.
5. Add package bin registration and focused adversarial tests.
6. Run focused/full tests, build, and bounded local binary smoke.
7. Author completion/evidence, self-review exact manifests, and commit material.
8. Convert closure artifacts, run closure/pre-push gates, and sync continuity.

## Acceptance Criteria

| ID | Criterion |
| --- | --- |
| AC1 | New binary is published without changing Delta-T1/T2 contracts. |
| AC2 | No process starts before T1 ALLOW, T2 consumption, and T3 durable intent. |
| AC3 | Only five exact non-destructive profiles exist; arbitrary execution is rejected. |
| AC4 | Direct runner always uses `shell:false`, exact args, bounded output, and no env override. |
| AC5 | Real-path validation rejects workspace and symlink escape. |
| AC6 | Execution receipt stores only ids/profile/hash/timestamps/status/exit diagnostics, never command output. |
| AC7 | Runner failures finalize as failed and propagate a non-zero launcher result. |
| AC8 | Known credential patterns are redacted from returned stdout/stderr. |
| AC9 | Focused tests, full MCP tests, build, binary smoke, reviewer-fast, and governance gates pass. |
| AC10 | No mutating command, provider/live/public/queue/workspace action or broad interception claim is added. |

## Evidence Requirements

Run from `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER`:

```powershell
npx vitest run src/cli/governed-command-launcher.test.ts src/persistence/json-governed-execution.store.test.ts --reporter verbose
npm run test:run
npm run build
node dist/cli/governed-exec.js --profile git-status --workspace <temporary-workspace> --json
```

Then run repo gates with real base/head anchors. Evidence must include exact
runner call ordering, durable receipt readback, no raw output persistence,
unknown-profile/cwd-escape rejection, exact changed set, and clean worktree at
closure.

## Review Gate

Reject closure if any caller can supply executable/args/env, any shell mode is
used, cwd can escape, runner can execute before all durable stages, receipt
stores output, known secret patterns return raw, Delta-T1/T2 behavior changes,
tests/gates fail, or claims imply direct-shell/IDE interception.

## Worker Autonomy / No-Question Rule

Codex repairs all allowed-scope source, test, type, formatting, and gate defects
without asking the operator. Return to operator only for forbidden scope, claim
expansion, provider/live/public work, secrets/quota, destructive action, or a
need to alter the Delta-T1/T2 contract.

## Return-To-Orchestrator Conditions

Return to the operator if correct implementation requires arbitrary/mutating
commands, shell/interpreter execution, EDIT/COMMIT, a new dependency, T1/T2
contract mutation, provider/live behavior, credentials or quota, public-sync,
workspace-state mutation, queue/daemon, destructive action, or broader claim.

## Operator Checkpoint

No further operator checkpoint is required inside the authorized Delta-T3
scope. Any mutating profile, arbitrary process, EDIT/COMMIT owner, or external
interception requires a new checkpoint, fresh GC-018, and source-verified work
order.

## Closure Checklist

| Item | Dispatch state |
| --- | --- |
| Dispatch Prompt Envelope first | PASS |
| Fresh GC-018 | PASS |
| Source Verification Block | PASS |
| Agent Handoff Contract Control Block | PASS |
| Single-Agent Multi-Role Control Block | PASS |
| Work-Order Fulfillment Manifest | PASS |
| Runtime implementation | REQUIRED |
| Focused/full verification and binary smoke | REQUIRED |
| Completion/evidence and closure gates | REQUIRED |
| Separate session continuity | REQUIRED |

## Finding-To-Governance Learning Disposition

| Field | Disposition |
| --- | --- |
| Finding | Delta-T2 yields admission eligibility but no process owner requires it before execution |
| Defect class | `RUNTIME_SIGNAL_GAP` |
| Learning lane | `GOVERNANCE_CONTROL_PLANE` |
| Escalation state | `DISPATCHED_BOUNDED_DELTA_T3` |
| Current control action | add wrapper-owned static-profile execution after T1/T2 durable admission |
| Machine-check action | later wider execution surfaces must compose the same admission chain rather than bypass it |
| Worker blame | N/A with reason: planned architecture progression |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance Delta runtime implementation. No public-sync.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | local provenance workspace |
| Session or invocation | `delta-t3-governed-command-launcher-dispatch-2026-06-19` |
| Working directory | repository root |
| Command or tool surface | PowerShell, rg, apply_patch, Python governance gates |
| Target paths | matching Delta-T3 GC-018 and this work order |
| Allowed scope source | operator request, Delta-T1/T2 closures, `MCP-GW-001` |
| Before status evidence | clean worktree at `f50e2903` |
| After status evidence | dispatch artifacts authored and source-verified |
| Diff evidence | `git diff --name-status`; `git diff --check`; pre-dispatch gates |
| Approval boundary | bounded static-profile RUN launcher only |
| Claim boundary | no arbitrary/mutating command, external interception, provider/live, public-sync, or universal governed-coding claim |
| Agent type | single-agent multi-role Codex dispatch phase |
| Invocation ID | `delta-t3-governed-command-launcher-dispatch-codex-2026-06-19` |
| Expected manifest | `docs/baselines/CVF_GC018_DELTA_T3_GOVERNED_COMMAND_LAUNCHER_2026-06-19.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_DELTA_T3_GOVERNED_COMMAND_LAUNCHER_FOR_CODEX_2026-06-19.md` |
| Actual changed set | `docs/baselines/CVF_GC018_DELTA_T3_GOVERNED_COMMAND_LAUNCHER_2026-06-19.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_DELTA_T3_GOVERNED_COMMAND_LAUNCHER_FOR_CODEX_2026-06-19.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none authorized |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order | this file | `Status: DISPATCH_READY_FOR_CODEX` | PASS |
| GC-018 | matching baseline | `Status: DISPATCH_READY` | PASS |
| Completion review | reviewer-owned path | final bounded disposition | REQUIRED |
| Evidence JSON | reviewer-owned path | acceptance assertion results | REQUIRED |
| Runtime source/tests | Required Artifact Manifest | exact changed-set evidence | REQUIRED |
| Provider/live proof | N/A with reason: forbidden and unnecessary | no live command | N/A with reason |
| Public-sync | N/A with reason: not authorized | `DEFERRED_PRIVATE_ONLY` | N/A with reason |
| Session continuity | separate phase | dispatch/material/closure continuity | REQUIRED |

## Execution Admission Assertion Matrix

| Assertion | Required observation | Dispatch state |
| --- | --- | --- |
| process requires full admission chain | runner call occurs only after T1/T2/T3 durable success | REQUIRED |
| arbitrary execution unavailable | unknown profile and extra args rejected | REQUIRED |
| cwd stays inside workspace | lexical and symlink escape rejected | REQUIRED |
| failure receipt is durable | runner error finalizes failed state | REQUIRED |
| execution claim stays bounded | wrapper-owned process true; external interception false | REQUIRED |

## Claim Boundary

Delta-T3 may prove only wrapper-owned execution of an exact registered
non-destructive RUN profile after durable T1/T2/T3 controls. It does not make
the wrapper mandatory outside its own path, execute EDIT/COMMIT, intercept
external tools, or prove universal governed coding.
