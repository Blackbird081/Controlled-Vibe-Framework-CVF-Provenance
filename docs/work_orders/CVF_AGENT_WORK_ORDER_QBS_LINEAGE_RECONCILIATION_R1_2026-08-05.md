# CVF Agent Work Order - QBS Lineage Reconciliation R1

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: CVF-QBS-LINEAGE-R1

dispatchBaseHead: `4494d6cce`

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: implementation worker

Reviewer/closer: reviewer/closer

Worker return path: `docs/reviews/CVF_QBS_LINEAGE_RECONCILIATION_R1_WORKER_RETURN_2026-08-05.md`

## Dispatch Prompt Envelope

Role: implementation worker for CVF-QBS-LINEAGE-R1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_QBS_LINEAGE_RECONCILIATION_R1_2026-08-05.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: worker captures current HEAD before edits.

Current-time notes: 2026-08-05 bounded provenance reconciliation only.

Do-not-misread notes: no provider/live proof, benchmark rerun, public mutation,
downstream edit, governance-latency work, or F-1 reopening.

Required first actions: read startup surfaces, guard orientation, literal
gotchas, paired baseline, current source, and historical public diffs.

Return contract: leave the exact allowed changed set uncommitted and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Reconcile the bounded QBS contracts into current provenance source, adapting
historical behavior to current interfaces and proving it with offline tests.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-QBS-LINEAGE-R1 --title "QBS Lineage Reconciliation R1" --date 2026-08-05 --base 4494d6cce --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic no-commit worker |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added exact lineage evidence, source verification, path manifest, offline gates, and role separation. |
| checkerReadAheadConfirmation | Dispatch-quality, handoff, ADIF, worker-return, trace, and public-export checkers reviewed. |
| docOnlyNewFields | None. |
| claimBoundary | Dispatch authoring evidence only. |

## Authority Chain

| Authority | Evidence |
| --- | --- |
| Operator | explicit confirmation on 2026-08-05 |
| Baseline | `docs/baselines/CVF_GC018_QBS_LINEAGE_RECONCILIATION_R1_2026-08-05.md` |
| Runtime authority | current provenance source at `4494d6cce` |
| Read-only lineage evidence | public commits `4e37e8644`, `f196bc04b`, `37b01a953`, `57fd8c3f5`, `d44517cd0`, `791b07e5c`, `188e6fd73` |

## Agent Roles

| Role | Ownership |
| --- | --- |
| Worker | Implements exact allowed paths and returns no-commit evidence. |
| Reviewer/closer | Recomputes evidence, accepts or rejects, and owns commits. |
| Session-sync steward | Updates protected continuity in a separate commit following accepted material review. |

## Required First Reads

- `AGENTS.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V53_2026-07-26.md`
- `docs/reference/guard_orientation/README.md`
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
- paired baseline and this work order

## Pre-flight Checks

1. Confirm provenance HEAD `4494d6cce` and no unrelated worktree changes.
2. Confirm public-sync HEAD `27137db4d`, expected public remote, and clean worktree.
3. Run pre-implementation autorun using the captured execution base.
4. Confirm provider keys are removed from every test process.

## Write Ownership

The worker owns only the fourteen paths in Scope / Applies To and must not
commit. The reviewer owns material closure. The session-sync steward owns
protected continuity paths in a separate commit.

## Worker Autonomy / No-Question Rule

Repair allowed-scope checker and test failures directly. Return to the
orchestrator only for source contradiction, an additional required path,
provider/live need, public mutation, or inability to preserve the boundary.

## Scope / Applies To

Allowed changed paths:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governance-family.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governance-family.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.qbs-allow-output.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.qbs-hard-gates.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-router.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-router.qbs-f7.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/qbs/front-door-clarification/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/qbs/front-door-clarification/route.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.qbs-hard-gates.test.ts`
- `docs/reviews/CVF_QBS_LINEAGE_RECONCILIATION_R1_WORKER_RETURN_2026-08-05.md`

Forbidden scope: every other implementation path, public-sync mutation,
downstream mutation, provider/network call, live test, QBS benchmark rerun,
governance-latency L0, and F-1 tuning.

## Source Verification Block

| Claimed item | Claim type | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Request family metadata seam | EXISTS | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/ai/types.ts` | `ExecutionRequest` | `qbsFamily` | `ExecutionRequest` | ACCEPT |
| Family resolver is new provenance source | DOC_ONLY_NEW | DOC_ONLY_NEW | `docs/baselines/CVF_GC018_QBS_LINEAGE_RECONCILIATION_R1_2026-08-05.md` | Scope / Applies To | `resolveGovernanceFamily` | new bounded helper | ACCEPT |
| Prompt contract owner | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execute-prompt-contract.ts` | exported prompt builder | `buildExecutionPrompt` | prompt builder | ACCEPT |
| Declared risk input | EXISTS | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.ts` | `EnforcementInput` | `cvfRiskLevel` | `EnforcementInput` | ACCEPT |
| Synchronous enforcement owner | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enforcement.ts` | exported evaluator | `evaluateEnforcement` | enforcement runtime | ACCEPT |
| Intent routing owner | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-router.ts` | exported router | `routeIntent` | intent router | ACCEPT |
| Clarification helpers exist | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-router-clarification.ts` | exported helpers | `startClarification` | clarification helper | ACCEPT |
| Execute response owner | RUNTIME_BEHAVIOR | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | route handler | `POST` | execute API route | ACCEPT |
| Front-door API is new provenance source | DOC_ONLY_NEW | DOC_ONLY_NEW | `docs/baselines/CVF_GC018_QBS_LINEAGE_RECONCILIATION_R1_2026-08-05.md` | Scope / Applies To | `POST` | new bounded route | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039,
ADIF-0043, ADIF-0049, ADIF-0006.

Disclosure count: 20

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch lifecycle status, Source Verification Block, ADIF Defect Registry Disclosure, Agent Handoff Contract Control Block, Reviewer Closure Conversion, Public Export Disposition |
| gateRunPurpose | Confirm packet shape before worker implementation. |
| claimBoundary | Read-ahead evidence only. |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | SINGLE_AGENT_MULTI_ROLE |
| rolePattern | worker returns no-commit evidence; reviewer/closer decides acceptance |
| phase | pre-implementation through reviewer closure |
| baseHeadFor(phase) | dispatchBaseHead=4494d6cce; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exactly fourteen allowed paths including worker return |
| traceScope(phase, actor) | worker return records commands, status, and exact diff |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns commit |
| crossBatchIsolation | clean worktree confirmed at provenance `4494d6cce` and public `27137db4d`; public export, downstream, governance-latency L0, live benchmark, and F-1 remain separate |
| nextMoveSurfaces | session-sync steward updates active continuity only after accepted material closure |

## Reviewer Closure Conversion

| Field | Value |
| --- | --- |
| completionReviewPath | `docs/reviews/CVF_QBS_LINEAGE_RECONCILIATION_R1_COMPLETION_2026-08-05.md` |
| reviewerOwnedClosurePaths | allowed source/test paths plus worker return; continuity paths only in a separate session-sync commit |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Intake Role Routing Decision

| Field | Decision |
| --- | --- |
| intake summary | First-party source/test reconciliation using public history as read-only lineage evidence. |
| scope classification | Bounded runtime reconciliation across four behavior groups and their shared metadata. |
| risk sensitivity | Runtime behavior changes; no provider, live, public, or production claim. |
| selected role route | SINGLE_AGENT_MULTI_ROLE |
| role separation basis | No-commit worker return precedes reviewer recomputation and commit ownership. |
| escalation condition | Stop for any extra path, contract contradiction, live/provider need, public mutation, or claim expansion. |

## Single-Agent Multi-Role Control Block

| Control | Disposition |
| --- | --- |
| role separation ledger | Worker produces no-commit evidence; reviewer/closer accepts, repairs, and commits. |
| evidence basis independent of memory | Current source, historical diffs, focused tests, full non-live suite, and machine gates are recomputed. |
| self-review boundary | Independent review is not claimed. |
| escalation conditions | Stop for scope, secrets, network/provider, destructive action, public mutation, or claim-boundary change. |
| gate sequence | pre-dispatch, pre-implementation, worker-return fast gate, reviewer-fast, pre-closure, commit steward, and separate session sync. |

## Work-Order Fulfillment Manifest

| Artifact group | Required worker action |
| --- | --- |
| intent routing and front door | preserve ambiguous F7 clarification without guessing a target |
| enforcement | honor declared risk, approval-gate bounded R2 content, and block bounded R3 bypass/audit evasion |
| execute route | return useful BLOCK, CLARIFY, and NEEDS_APPROVAL outputs with evidence receipts |
| family metadata and prompt contract | resolve bounded family metadata and append ALLOW-only output requirements |
| tests | restore the paired historical contract tests in provenance and keep negative controls |
| worker return | record lineage adaptation, commands, exact diff, failures, and no-commit status |

## Execution Plan

1. Capture execution HEAD/status and run pre-implementation autorun.
2. Recreate each historical contract against current provenance interfaces;
   do not wholesale replace newer source files.
3. Run the six focused test files, typecheck, and diff hygiene with all known
   provider-key variables cleared.
4. Run the full non-live cvf-web suite once. Classify failures before any rerun.
5. Create the worker return, run its fast gate, and stop without commit.

## Verification Commands

```powershell
node_modules/.bin/vitest.cmd run src/lib/intent-router.qbs-f7.test.ts src/lib/enforcement.qbs-hard-gates.test.ts src/app/api/qbs/front-door-clarification/route.test.ts src/lib/governance-family.test.ts src/lib/execute-prompt-contract.qbs-allow-output.test.ts src/app/api/execute/route.qbs-hard-gates.test.ts
node_modules/.bin/tsc.cmd --noEmit
node_modules/.bin/vitest.cmd run --exclude "src/**/*.live.test.ts"
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
```

The worker must clear `DASHSCOPE_API_KEY`, `ALIBABA_API_KEY`,
`CVF_ALIBABA_API_KEY`, `CVF_BENCHMARK_ALIBABA_KEY`, and `DEEPSEEK_API_KEY`
inside every test process.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_QBS_LINEAGE_RECONCILIATION_R1_WORKER_RETURN_2026-08-05.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The worker return must preserve these sections:

- Purpose
- Scope / Methodology
- Findings / Position
- Risk / Corrective Action
- Claim Boundary
- Agent Operation Trace Block
- Delta Execution Claim Boundary Control Block
- Public Export Disposition
- External Knowledge Intake Routing
- Rescan Intelligence Hardening
- Corpus Completeness And Report Integrity
- Finding-To-Governance Learning Disposition
- Epistemic Process Block
- Machine Closure Package

Every conditional section remains present with `N/A with reason` when it does
not apply. The return records `executionBaseHead`, exact commands, and
`git status --short` evidence.

## External Knowledge Intake Routing

| Field | Disposition |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Public/simple CVF vocabulary |
| Chain map route | N/A with reason: repository lineage is source history, not external knowledge intake |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this bounded provenance work order |
| Disposition | N/A with reason: no provider output or external-agent report is absorbed |
| Claim boundary | historical diffs identify candidate contracts; current provenance tests decide acceptance |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: restoring the paired contracts in current
provenance resolves the known 15 failures without provider use.

Evidence Comparison Requirement: compare focused and full non-live results
with the prediction and preserve any contradiction.

Contradiction Handling Requirement: stop if a newer provenance contract needs
an extra path or makes a historical behavior unsafe.

Claim Update Requirement: worker records confirmed, narrowed, or invalidated.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher |
| Provider or surface | local provenance plus read-only sibling Git history |
| Session or invocation | qbs-lineage-r1-dispatch-2026-08-05 |
| Working directory | provenance repository root |
| Command or tool surface | governed reads, git history inspection, ADIF resolver, scaffold helper, and packet authoring |
| Target paths | paired baseline and work order |
| Allowed scope source | operator confirmation on 2026-08-05 |
| Before status evidence | provenance `4494d6cce` and public `27137db4d`; `git status --short` empty in each clean worktree |
| After status evidence | paired dispatch packet pending gate |
| Diff evidence | `git diff --name-status` |
| Approval boundary | dispatch authoring only |
| Claim boundary | no implementation, provider call, benchmark, public mutation, commit, or push |
| Agent type | dispatcher |
| Invocation ID | `qbs-lineage-r1-dispatch-2026-08-05` |
| Expected manifest | paired baseline and work order |
| Actual changed set | paired baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local QBS source/test lineage reconciliation |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no live runtime receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: source diff and offline test results only |
| invocationBoundary | local governed commands inside provenance |
| interceptionBoundary | no IDE, shell, git, provider, or agent interception claim |
| claimLanguage | reconciliation may prove only the bounded source/test contracts |
| forbiddenExpansion | no benchmark score, provider/live, public push, downstream edit, governance-latency, or F-1 work |

## Acceptance Criteria

- [ ] The six focused test files pass offline.
- [ ] Typecheck passes.
- [ ] Full non-live cvf-web suite passes or preserves separately evidenced pre-existing failures.
- [ ] Exact changed set matches the fourteen worker-owned paths.
- [ ] Public-sync HEAD/status remain unchanged.
- [ ] Worker return fast gate passes.

Fail conditions:

- [ ] N/A with reason: unresolved until worker return; no provider/live or public mutation may occur.
- [ ] N/A with reason: unresolved until worker return; no test deletion or weakening may occur.
- [ ] N/A with reason: unresolved until worker return; any extra path returns to orchestrator.

## Review Gate

Implementation requires this work order plus passing pre-dispatch and
pre-implementation gates. Closure requires reviewer recomputation under
`SINGLE_AGENT_MULTI_ROLE`, material pre-closure, commit steward, and separate
continuity sync. Independent review is not claimed.

## Evidence Requirements

- Exact before/after SHA and `git status --short --untracked-files=all`.
- Focused test, typecheck, and full non-live suite results with keys cleared.
- Exact source/test manifest and `git diff --check` result.
- Public-sync HEAD/status proving no mutation.
- Worker-return fast-gate result.

## Operator Checkpoint

Operator confirmation releases this provenance reconciliation only. Public
projection/export remains a separate checkpoint following accepted closure.

## Closure Checklist

- [ ] Worker return is complete and no-commit.
- [ ] Every focused command passes following the last implementation edit.
- [ ] Exact worker allowed changed set matches.
- [ ] Reviewer recomputes evidence from disk; independence is not claimed.
- [ ] Material pre-closure and commit steward pass on a real changed range.
- [ ] Public-sync remains clean and unchanged.

## Return-To-Orchestrator Conditions

- Source contradiction or missing authority.
- Need for any path outside Allowed changed paths.
- Any provider/network/live proof or public mutation requirement.
- Any proposal to rerun the QBS benchmark or reopen F-1.
- Any gate failure not repairable inside allowed scope.

## Claim Boundary

This work order authorizes only bounded local QBS lineage reconciliation and
offline verification. It does not authorize public export.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: a separate reviewed projection/export tranche must follow provenance
closure.
