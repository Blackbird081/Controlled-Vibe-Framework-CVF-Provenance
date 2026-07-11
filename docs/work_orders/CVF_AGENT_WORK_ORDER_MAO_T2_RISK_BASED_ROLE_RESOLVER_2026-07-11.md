# CVF Agent Work Order - MAO-T2 Risk-Based Role Resolver

Memory class: governed-work-order

Status: DISPATCH_READY

Date: 2026-07-11

Batch: MAO-T2

dispatchBaseHead: `8b9f8f528`

executionBaseHead: capture actual clean post-dispatch-sync HEAD before editing.

closureBaseHead: N/A with reason: reviewer conversion has not occurred.

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: delegated MAO-T2 worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_T2_RISK_BASED_ROLE_RESOLVER_2026-07-11.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

Current-time notes: artifact date is 2026-07-11; capture actual clean HEAD.

executionBaseHead: capture the actual clean post-dispatch-sync HEAD before editing.

Do-not-misread notes: local resolver only; no provider, adapter, queue, UI,
public, workspace/session, root-barrel, or MAO-T3 work.

Required first actions: complete startup reads, capture HEAD/status, read the
paired baseline and every ACCEPT source, then run pre-implementation gate.

Return contract: exactly four outputs; run all commands; return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` without commit.

## Purpose

Implement and test a provider-neutral, deterministic control-plane policy that
chooses single-worker admission, a bounded role plan, operator approval, or
rejection, with explicit risk, cost, and exclusion reasons.

## Authority Chain

1. `AGENTS.md`.
2. `docs/roadmaps/CVF_MULTI_AGENT_ORCHESTRATION_RUNTIME_FOUNDATION_ROADMAP_2026-07-11.md` MAO-T2.
3. `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md`.
4. `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_SCHEMA.json`.
5. `docs/baselines/CVF_GC018_MAO_T2_RISK_BASED_ROLE_RESOLVER_2026-07-11.md`.

## Agent Roles

| Role | Owner |
|---|---|
| worker | implements/tests and returns uncommitted material |
| reviewer/closer | independently reviews, repairs allowed-scope defects, and commits accepted material |
| session-sync steward | updates continuity in a separate commit once material is reviewer-accepted |

## Scope / Target / Owner Boundary

### Allowed worker paths

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/role.resolver.contract.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/mao.role.resolver.contract.test.ts`
- `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts`
- `docs/reviews/CVF_MAO_T2_RISK_BASED_ROLE_RESOLVER_WORKER_RETURN_2026-07-11.md`

### Forbidden paths and behavior

- No provider router change or invocation, adapter, queue, UI, workspace/session,
  public-sync, roadmap, checker/hook, package-root barrel, or MAO-T3+ change.
- No commit, push, live proof, secret access, provider branding, or production claim.
- Do not redefine AHB route tokens or closer ownership.

## Write Ownership

Worker owns only the four allowed paths. Reviewer owns closure conversion and
minimum GC-051 source/aggregate registration if a registry gate requires it.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Final disposition | Refreshed base |
|---|---|---|---|---|
| MAO-T1 | `docs/reviews/CVF_MAO_T1_TASK_GRAPH_AND_STATE_CONTRACT_COMPLETION_2026-07-11.md` | `01618e9dc` | `REVIEWER_ACCEPTED_BOUNDED` | `8b9f8f528` |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MAO-T2 --title "Risk-Based Role Resolver" --date 2026-07-11 --base 8b9f8f528 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | all placeholders replaced with MAO-T2 source-backed controls |
| checkerReadAheadConfirmation | applicable checker sources read before final authoring |
| docOnlyNewFields | resolver-local reason vocabulary is a new implementation output |
| claimBoundary | dispatch provenance only |

## Required First Reads

- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- all Authority Chain and Source Verification ACCEPT files

## Pre-Flight Checks

Run `git rev-parse HEAD`, `git status --short`, source token searches, then
`python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD` before material edits.

## Worker Autonomy / No-Question Rule

Repair and rerun any allowed-scope failure. Return blocked only for missing
authority/source, forbidden-path necessity, scope expansion, or operator-only
provider/public/live action.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| MAO-T2 outputs and no-provider boundary | `docs/roadmaps/CVF_MULTI_AGENT_ORCHESTRATION_RUNTIME_FOUNDATION_ROADMAP_2026-07-11.md` | Work Plan And Dependencies / MAO-T2 | `MAO-T2 - Risk-Based Role Resolver` | roadmap tranche | ACCEPT |
| four resolver decisions | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Role Resolver Ownership | `role resolver` | MAO T0 contract | ACCEPT |
| route conditions and evidence | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Risk-Based Role Model | `Risk-Based Role Model` | MAO T0 contract | ACCEPT |
| fan-out ceilings and stop behavior | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md` | Cost / Token / Latency Controls | `Cost / Token / Latency Controls` | MAO T0 contract | ACCEPT |
| decision, risk, budget, task fields | `docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_SCHEMA.json` | definitions | `roleResolutionReceipt`, `riskLevel`, `budgetAllocation`, `taskDefinition` | Draft 2020-12 schema | ACCEPT |
| compiled authority/task input | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | exports | `MaoCompiledTaskGraph`, `MaoAuthorityEnvelope`, `MaoTaskDefinition` | MAO-T1 task graph contract | ACCEPT |
| route tokens and closer ownership | `docs/reference/agent_handoff/README.md` | Ratified Central Core and contract-field index | `route`, `commitOwner(phase)` | Agent Handoff Contract front door | ACCEPT |

## Current Runtime Freshness Verification

Verified at `8b9f8f528`. All ACCEPT files and symbols exist. New resolver types,
reason codes, and helper functions are implementation outputs and are not
misrepresented as existing source.

## Negative Search And Collision Discipline

Search current control/execution planes for role resolver, admission decision,
and receipt vocabulary. Reuse authoritative route/risk values; keep new local
reason-code vocabulary inside the MAO-T2 module and document collisions.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`runtime implementation`, role=`worker`, lifecyclePhase=`implementation`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "runtime implementation" --role worker --lifecycle-phase implementation --surface-selector "multi-agent orchestration role resolver" --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

Disclosed defectIds: N/A with reason: NONE_RETURNED.

The empty result is not evidence that a caller consumed the packet.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_corpus_scan_registry.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | dispatch envelope fields; canonical AHB fields; full-gate contract tokens; ADIF query; trace manifest fields |
| gateRunPurpose | confirmation and evidence after source-backed authoring; not first discovery |
| claimBoundary | dispatch compatibility only |

## Intake Role Routing Decision

Selected route: `MULTI_AGENT_MULTI_ROLE`

rolePattern: `worker-no-commit split`

Intake summary: bounded local control-plane policy implementation with independent review.

Scope classification: `RUNTIME_FOUNDATION_LOCAL_NO_PROVIDER`

Risk sensitivity: HIGH because authority and role admission fail closed.

Escalation condition: source contradiction, authority widening, forbidden path,
provider requirement, or an out-of-scope gate failure.

| Surface | Interface | Authority/risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | local TypeScript policy function | accepted graph/authority only | focused tests and receipt assertions | no invocation adapter | IMPLEMENT_LOCAL |
| EXTERNAL_AGENT_CLI_MCP | none | external agent cannot become authority | N/A with reason: no CLI/MCP call | separate future packet required | CONTRACT_ONLY |

## Dual Agent Surface Matrix

| Surface | Intended use | Interface | Authority/risk boundary | Required evidence | Adapter boundary |
|---|---|---|---|---|---|
| INTERNAL_AGENT | deterministic admission evaluation | direct local function | cannot widen authority, budget, route, or closer | unit and negative tests | no provider selection |
| EXTERNAL_AGENT_CLI_MCP | not implemented | none | no external execution claim | N/A with reason: excluded | MAO-T3 requires fresh authorization |

## Agent Handoff Contract Control Block

Contract source, active and not archive:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Disposition |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | worker implements; independent reviewer/closer accepts |
| phase disposition | dispatch -> implementation -> reviewer closure -> separate session sync |
| baseHeadFor(phase) | dispatch `8b9f8f528`; worker captures clean execution base |
| changedSetScope(phase) | four worker paths only; reviewer GC-051 coverage only if required |
| traceScope(phase, actor) | work order, worker return, and completion review preserve exact manifests |
| commitOwner(phase) | reviewer/closer; worker must not commit |
| crossBatchIsolation | MAO-T3+ and unrelated changes forbidden; clean worktree required |
| Before status evidence | `git status --short` empty; clean worktree at dispatch authoring start |
| nextMoveSurfaces | session-sync steward updates only after accepted material commit |

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_MAO_T2_RISK_BASED_ROLE_RESOLVER_COMPLETION_2026-07-11.md`

reviewerOwnedClosurePaths: baseline, work order, completion review, and minimum
GC-051 source/aggregate coverage if required. Reviewer must independently test
semantics and may repair only allowed implementation/test paths.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work-order handling | Status |
|---|---|---|
| single-worker default | explicit default decision and tests | PASS |
| specialist/reviewer admission | bounded risk/capability/evidence gates | PASS |
| human checkpoint | approval-required result for high-risk fan-out | PASS |
| rejection reasons | deterministic reason codes and receipt text | PASS |
| budget plan | validate and echo bounded allocation/exclusion evidence | PASS |
| no provider invocation | forbidden scope and dependency scan | PASS |

## Work-Order Fulfillment Manifest

Worker produces exactly four allowed paths and no others.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must include Target, Scope, Findings, Risk / Corrective Action,
Decision / Disposition, External Knowledge Intake Routing, Epistemic Process
Block, Public Export Disposition, Machine Closure Package, Source Inventory,
Agent Operation Trace Block, and actual untracked status.

## Execution Plan

1. Capture execution base, verify sources, run pre-implementation gate.
2. Define provider-neutral resolver input/output and deterministic reason codes.
3. Implement fail-closed admission with single-worker default.
4. Test R0/R1 default, R2 review, R3 specialist/reviewer/closer/checkpoint,
   overlap/decomposition/capability/budget/closer/source-packet rejection, and
   deterministic replay.
5. Update only the local MAO barrel, create worker return, run all gates, stop.

## Verification Commands

- From `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION`:
  `npx vitest run --config vitest.config.ts tests/mao.role.resolver.contract.test.ts`
- From the same package: `npx tsc -p tsconfig.json --noEmit`
- From repo root: `python governance/compat/check_governed_file_size.py --enforce`
- From repo root: `python governance/compat/run_worker_return_fast_gate.py`
- From repo root: `git diff --check`

## Acceptance Criteria

- [ ] Four resolver decisions are deterministic and carry explicit reasons.
- [ ] Single-worker is the default and fan-out cannot exceed authority/budget.
- [ ] High-risk fan-out requires specialist, reviewer, closer, and checkpoint.
- [ ] Invalid overlap, decomposition, capability, packet, closer, or budget fails closed.
- [ ] No provider/router/adapter call or provider-specific branch exists.
- [ ] Focused tests, typecheck, fast gate, and final self-audit pass.

## Evidence Requirements

- Exact focused-test and typecheck commands with working directory and result.
- Deterministic replay plus negative cases for every fail-closed admission gate.
- `git status --short --untracked-files=all` after the worker return exists.
- Evidence Trace Block with Claim, Command, Result, Key path, and Verdict.
- Material-only and later session-sync ranges recorded separately.

## Negative And Fail-Condition Scan

Closure fails for guessed source facts, authority widening, silent review
degradation, auto-commit, provider invocation, missing reason receipt,
non-determinism, forbidden changed paths, or unresolved checklist items.

## Review Gate

Worker stops at `COMPLETE_PENDING_REVIEW`. Reviewer reruns focused tests and
`python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <executionBaseHead> --head HEAD --enforce` before acceptance.

## Closure Checklist

- [ ] Roadmap trace rows remain satisfied.
- [ ] Required commands pass after the final edit.
- [ ] Closure Diff Gate compares roadmap, work order, outputs, and claims.
- [ ] Changed-set evidence is exact and inside allowed/reviewer-owned scope.
- [ ] Public export remains deferred and continuity is synced separately.

## Return-To-Orchestrator Conditions

Return blocked for missing source, need for forbidden path/provider/live/public
action, risk ceiling expansion, or irreparable gate failure outside allowed scope.

## Operator Checkpoint

No checkpoint is required for this local no-provider execution. Any expansion
to provider invocation, public sync, live quota, or higher concurrency requires
fresh operator authorization and a new packet.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | MAO-T2 dispatch authoring at `8b9f8f528` |
| Working directory | repository root |
| Command or tool surface | source reads, ADIF resolver, apply patch, governance gates, git |
| Target paths | paired MAO-T2 baseline and work order |
| Allowed scope source | operator request plus roadmap next tranche |
| Before status evidence | clean worktree; `git status --short` empty at HEAD `8b9f8f528` |
| After status evidence | two new governed dispatch artifacts pending commit |
| Diff evidence | `git diff --name-status` and pre-dispatch range |
| Approval boundary | packet authoring and dispatch only; no implementation |
| Claim boundary | repo-local trace; no provider, OS-user, or production attribution |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
| Agent type | dispatcher |
| Invocation ID | mao-t2-dispatch-2026-07-11 |
| Expected manifest | paired MAO-T2 baseline and work order |
| Actual changed set | paired MAO-T2 baseline and work order |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | MAO-T2 local role-admission policy and focused tests |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: dispatch defines a future local role-resolution receipt but proves no execution receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT through focused tests and changed-set evidence at worker return |
| invocationBoundary | local TypeScript function only |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, or network interception claim |
| claimLanguage | deterministic policy admission, not runtime orchestration |
| forbiddenExpansion | provider, adapter, queue, UI, commit, public, production, MAO-T3+ |

## Foundation Storage Layout Block

| Question | Disposition |
|---|---|
| Generated aggregate | N/A with reason: no aggregate is introduced. |
| Storage plane | control-plane source plus focused package test |
| Runtime persistence | N/A with reason: resolver is pure and stateless. |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | NOT_APPLICABLE_WITH_REASON |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired MAO-T2 baseline and work order |
| Disposition | NOT_APPLICABLE_WITH_REASON: CVF-governed source only |
| Claim boundary | no external knowledge absorption claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Next action: retain in provenance until MAO-T9 and require a separate public-safe
projection packet.

## Machine Closure Package

| Field | Value |
|---|---|
| Work-order state | `DISPATCH_READY` |
| Commit mode | `WORKER_MUST_NOT_COMMIT` |
| Dependency | MAO-T1 accepted at `01618e9dc` |
| Worker terminal status | `COMPLETE_PENDING_REVIEW` only |
| Next action | delegated execution from clean post-sync HEAD |

## Acceptance Receipt Assertion Matrix

| Assertion | Evidence |
|---|---|
| route decision valid | exact decision enum assertion |
| reasons complete | risk/cost/excluded-role assertions |
| budget bounded | positive/negative ceiling tests |
| no provider call | import/dependency scan and changed-set evidence |

## Claim Boundary

This dispatch authorizes only a deterministic local role resolver and focused
tests. It does not prove multi-agent runtime operation, provider support,
external-agent execution, independent-review effectiveness, live governance,
public readiness, or production orchestration.
