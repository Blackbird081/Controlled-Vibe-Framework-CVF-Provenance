# CVF Agent Work Order Projection Automation T2 Three-Root Proof And Closure

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: CVF-PROJECTION-AUTO-T2

Dispatch base head: `67aefb4eb`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker return path: `docs/reviews/CVF_PROJECTION_AUTOMATION_T2_WORKER_RETURN_2026-07-18.md`

## Dispatch Prompt Envelope

Role: delegated proof-and-documentation worker.

Canonical packet: this work order.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: must equal the committed T2 dispatch/session-sync HEAD named
by the dispatcher prompt.

Current-time notes: T1 closure `aa699742b`; handoff sync `67aefb4eb`; T2 is the
final roadmap tranche.

Do-not-misread notes: disposable proof only. No apply/copy, real public-sync or
cvf-web mutation, commit, push, provider/network call, deployment, or production.

Required first actions: read startup front doors, guard orientation, literal
gotchas, paired baseline, this work order, T1 completion review, mapper/policy/
schema, and applicable checker source.

Return contract: leave exactly five outputs uncommitted and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Operator Checkpoint

N/A with reason: standing authorization covers this disposable no-push proof;
any future apply or public action requires a separate explicit batch.

## Purpose

Prove the accepted T1 mapper across three disposable roots, document safe
operator use, reconcile the complete roadmap, and return closure evidence.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-PROJECTION-AUTO-T2 --title "Projection Automation Three-Root Proof And Closure" --date 2026-07-18 --base 67aefb4eb --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | populated five-path scope, proof matrix, operator guide, final audit, and closure boundary |
| checkerReadAheadConfirmation | dispatch-quality, structural, handoff, worker-return, receipt, closure, and public-disposition checkers |
| docOnlyNewFields | audit totals and proof-run labels only; receipt uses existing schema |
| claimBoundary | final tranche dispatch provenance only |

## Authority Chain

Standing continuation -> roadmap -> accepted T1 completion review -> paired T2
baseline -> this packet -> no-commit worker -> independent reviewer/closer.

## Agent Roles

Dispatcher owns packet. Worker owns five outputs. Reviewer/closer owns rerun,
acceptance, material commit, full-roadmap closure, and session sync.

## Required First Reads

Read paired baseline, T1 completion review, mapper, policy, T1 test runner,
receipt schema/accepted receipt, roadmap, guard orientation, literal gotchas,
and checker sources named below.

## Pre-Flight Checks

Confirm exact executionBaseHead, clean worktree, five-path scope, committed T1
artifacts, and pre-implementation autorun PASS before writing.

## Write Ownership

Worker may create exactly:

1. `scripts/test_cvf_projection_three_root_proof.ps1`
2. `docs/guides/CVF_PROJECTION_MAPPING_OPERATOR_GUIDE_2026-07-18.md`
3. `docs/reviews/CVF_PROJECTION_AUTOMATION_T2_THREE_ROOT_PROOF_RECEIPT_2026-07-18.json`
4. `docs/reviews/CVF_PROJECTION_AUTOMATION_T2_FINAL_CLOSURE_AUDIT_2026-07-18.md`
5. `docs/reviews/CVF_PROJECTION_AUTOMATION_T2_WORKER_RETURN_2026-07-18.md`

Every other path is read-only.

## Forbidden Scope

Do not modify mapper, policy, T1 tests/schema/receipt, public-sync script,
workspace updater, cvf-web, real public-sync clone, registries, generated state,
session surfaces, hooks/checkers, or dependencies. Do not add apply/copy code,
use real roots as proof targets, stage, commit, push, call network/providers,
deploy, or perform production action.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Final disposition |
|---|---|---|---|
| accepted T1 | `docs/reviews/CVF_PROJECTION_AUTOMATION_T1_COMPLETION_REVIEW_2026-07-18.md` | `aa699742b` | REVIEWER_ACCEPTED_BOUNDED |
| continuity release | active handoff sync | `67aefb4eb` | PASS |

## Source Verification Block

Use and reconfirm all ACCEPT rows in the paired T2 baseline. A contradiction
requires `BLOCKED_WITH_REASON`; do not alter committed T1 source to work around it.

## Required Implementation

### Three-root proof runner

Create a self-contained PowerShell script that:

- creates one unique temp parent with provenance, public-sync, cvf-web, and
  receipt-output subdirectories;
- initializes provenance/public roots as git repos with exact policy origins,
  without fetching or contacting a network;
- copies current `scripts/cvf-public-sync.ps1` into the disposable provenance
  root strictly as parity source and commits all fixture inputs;
- builds a bounded candidate set covering absent, changed, unchanged, denied,
  not-allowlisted, mapped export, and all three SOT3 observations;
- invokes committed `scripts/get_cvf_projection_map.ps1` twice using committed
  `scripts/cvf_projection_policy.json`;
- writes the governed proof receipt only to the exact allowed review path when
  an explicit `GovernedReceiptPath` parameter is supplied; default is temp only;
- validates schema 1.0.0, exact root labels, all eight parity values MATCH,
  zero errors, count reconciliation, deterministic bytes/receipt ID, and
  containment-count reconciliation;
- captures git status and recursive file inventory for all three roots before
  and after mapper invocation and proves zero delta;
- proves no BOM and no secret-like fixture content in the receipt;
- deletes its unique temp parent in `finally` and returns nonzero on failure.

It must print named PASS/FAIL assertions and a final total.

### Operator guide

Document prerequisites, exact dry-run stdout command, optional receipt command,
root/remote/clean requirements, action meanings, semantic-review workflow,
receipt interpretation, failure codes, safe cleanup, and explicit boundaries:
no apply/copy, no target mutation, no automatic Web repair, no commit/push.

### Final closure audit

Reconcile T0, T1, T2 artifacts/commits, roadmap AC-01 through AC-06, five T1
action classes, T2 proof assertions, exact changed set, public disposition, and
remaining boundary. Every row must be terminal `PASS`, `DEFERRED_PRIVATE_ONLY`,
or `N/A with reason`; no open row or unchecked checklist.

### Worker return

Use the full worker-return profile, record execution base, proof totals, receipt
ID/counts/parity, temp cleanup, exact five paths, unchanged HEAD, nothing staged,
required gates, and no-commit statement.

## Acceptance Criteria

- All paired baseline AC-01 through AC-07 pass.
- Proof runner has at least 20 named assertions and zero failures.
- Governed receipt is no-BOM schema 1.0.0, all parity MATCH, zero errors,
  reconciled, and stable across repeated runs.
- Before/after status/file inventory is unchanged across all three roots.
- Temp parent is absent after success and failure-path self-test.
- Operator guide and final audit preserve no-apply/no-push boundaries.
- Worktree contains exactly five allowed paths, nothing staged, HEAD unchanged.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work-order implementation | Evidence |
|---|---|---|
| disposable three-root proof | dedicated proof runner | named assertions |
| operator guide | governed guide | exact commands/boundaries |
| closure audit | final T0-T2 reconciliation | terminal audit rows |
| no push | forbidden scope and proof isolation | git/root evidence |
| exact plan/receipt reconciliation | schema/parity/count/determinism assertions | governed receipt |
| roadmap closure | independent reviewer conversion | T2 completion review |

## Work-Order Fulfillment Manifest

| Required artifact | Required proof literal |
|---|---|
| proof runner | three roots, repeated receipt, cleanup, zero delta |
| operator guide | stdout command, receipt command, no apply/push |
| governed proof receipt | schema 1.0.0, MATCH parity, zero errors |
| final audit | AC-01 through AC-06 and T0-T2 terminal rows |
| worker return | COMPLETE_PENDING_REVIEW and no-commit evidence |

## Required Artifact Manifest

| Artifact | Required disposition | Worker evidence |
|---|---|---|
| proof runner | present and all assertions pass | worker-owned |
| operator guide | present and bounded | worker-owned |
| proof receipt | present and reconciled | worker-owned |
| final closure audit | present and terminal | worker-owned |
| worker return | full profile and exact scope | worker-owned |

## Evidence Requirements

Record commands, assertion names/counts, receipt ID/schema/parity/counts/errors,
three-root before/after hashes/status/inventory, cleanup proof, exact changed set,
staged state, unchanged HEAD, and governed gate output.

## Execution Plan

Reconfirm source, implement proof runner, run temp-only proof, author guide,
generate governed receipt, author final audit/return, rerun proof and gates, and
reconcile exactly five paths.

## Review Gate

Reviewer reruns proof and T1 regression suite, validates receipt/audit/guide,
recomputes root deltas and cleanup, inspects exact five paths, and runs
reviewer-fast before closure.

## Closure Checklist

- [x] T1 dependency committed and accepted.
- [x] T2 scope is exactly five outputs.
- [x] Real roots, apply/copy, commit/push, provider/network remain forbidden.
- [x] Independent review owns roadmap closure.

## Return-To-Orchestrator Conditions

Return only after every allowed-scope defect is remediated and gates pass, or
with one source-backed blocker requiring a forbidden path or authority expansion.

## Stop Conditions

Stop before forbidden mutation if committed T1 source contradicts the baseline,
proof cannot isolate all roots under temp, mapper produces non-MATCH parity or
target delta, receipt cannot remain outside roots, or closure requires apply,
network, real-root mutation, public push, or another forbidden path.

## Worker Autonomy / No-Question Rule

Independently remediate all proof, fixture, documentation, and gate defects
inside the five allowed paths. Stop only for a listed genuine blocker.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | final disposable proof and closure tranche |
| scope classification | repository-local proof/documentation with temp fixtures |
| risk sensitivity | R2; executable local proof, no real target mutation |
| escalation condition | committed-source contradiction or forbidden authority need |
| canonical route mode | `MULTI_AGENT_SINGLE_ROLE` |
| selected role route | no-commit proof worker to independent reviewer/closer |

## Dual Agent Surface Matrix

| Surface | Interface | Authority/risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | local PowerShell proof CLI | temp roots and governed receipt only | proof output | committed T1 mapper | ACCEPT |
| EXTERNAL_AGENT_CLI_MCP | operator guide CLI | no MCP/provider/remote authority | guide and receipt schema | same local mapper | DEFER_WITH_REASON |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | dispatcher -> no-commit proof worker -> independent reviewer/closer |
| phase | EXECUTION |
| baseHeadFor(phase) | dispatchBaseHead=`67aefb4eb`; executionBaseHead=committed dispatch/session-sync HEAD from prompt; closureBaseHead=reviewer sets |
| changedSetScope(phase) | exactly five Write Ownership paths |
| traceScope(phase, actor) | base, fixture/proof, receipt, audit, guide, commands, diff, no-commit evidence |
| commitOwner(phase) | reviewer/closer; worker forbidden |
| crossBatchIsolation | clean worktree required; foreign changes block execution |
| nextMoveSurfaces | reviewer/session-sync steward only |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_PROJECTION_AUTOMATION_T2_COMPLETION_REVIEW_2026-07-18.md` |
| reviewerOwnedClosurePaths | five worker outputs, baseline, work order, roadmap, completion review, later session sync |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_PROJECTION_AUTOMATION_T2_WORKER_RETURN_2026-07-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`projection automation closure proof`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "projection automation closure proof" --role dispatcher --lifecycle-phase pre-dispatch --json`

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Public/simple CVF vocabulary |
| Chain map route | source-verify local contract -> disposable proof -> independent review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired T2 baseline and this work order |
| Disposition | QUESTION_OR_HYPOTHESIS until source-verified; T2 uses committed local source |
| Claim boundary | repository-local source and temp fixtures only |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | one flat proof script, one guide, and private review evidence |
| Storage decision | reuse existing T1 mapper/policy/schema; no second runtime or package |
| Existing aggregate impact | none |
| Generated state impact | none during worker execution |
| Durable governance boundary | local proof and documentation only; no apply/MCP/provider/Web/public authority |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Operator Checkpoint; Source Verification Block; Required Implementation; Roadmap-to-Work-Order Trace Matrix; Required Artifact Manifest; Reviewer Closure Conversion; Worker Return Packet Shape Contract; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation and evidence for T2 dispatch completeness, not first discovery |
| claimBoundary | disposable final proof dispatch |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/test_cvf_projection_three_root_proof.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/test_get_cvf_projection_map.ps1
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_governed_file_size.py --enforce
git status --short
```

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | private provenance workspace |
| Session or invocation | projection automation T2 dispatch, 2026-07-18 |
| Working directory | repository root |
| Command or tool surface | source reads, apply_patch, ADIF resolver, governed gates |
| Target paths | roadmap, paired T2 baseline, this work order |
| Allowed scope source | standing continuation and accepted T1 completion review |
| Before status evidence | clean worktree at HEAD `67aefb4eb` |
| After status evidence | three-path T2 dispatch packet pending material commit |
| Diff evidence | git status/diff and eventual committed diff |
| Approval boundary | T2 disposable proof dispatch only |
| Claim boundary | no proof execution, real-root mutation, apply, push, provider, or production action by dispatcher |
| Agent type | dispatcher |
| Invocation ID | `projection-automation-t2-dispatch-2026-07-18` |
| Expected manifest | roadmap, T2 baseline, T2 work order |
| Actual changed set | same three paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | disposable three-root closure proof |
| claimDisposition | CLAIM_REJECTED_PENDING_EVIDENCE until worker proof and review |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT until T2 governed proof receipt exists |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: proof/classification only |
| invocationBoundary | local PowerShell and unique temp fixtures |
| interceptionBoundary | no IDE/provider/MCP/runtime interception |
| claimLanguage | prove, reconcile, document, and close bounded |
| forbiddenExpansion | apply, copy, real-root mutation, registry repair, commit/push, provider/network, production |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | paired T2 GC-018 | `Status: DISPATCH_READY` | PASS |
| Work order status | this work order | `Status: DISPATCH_READY` | PASS |
| Completion or reviewer artifact | future T2 review | dependency-held | N/A with reason |
| Worker return | future T2 return | worker-owned | N/A with reason |
| Roadmap state | automation roadmap | `Status: T1_PASS_BOUNDED_T2_DISPATCH_READY` | PASS |
| Registry JSON | existing GC-051 coverage | aggregate drift checked | PASS |
| Registry Markdown | existing registry front door | no new family required | PASS |
| External evidence digest | repository-local evidence only | none | N/A with reason |
| System loop interlock | no loop owner changed | none | N/A with reason |
| Session continuity | protected session surfaces | separate sync | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| parity | all MATCH | worker-owned | N/A with reason |
| errors | zero | worker-owned | N/A with reason |
| three-root delta | zero | worker-owned | N/A with reason |
| deterministic receipt | same bytes and ID | worker-owned | N/A with reason |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: T2 dispatch and proof remain private; no public-sync action is allowed.

## Commit Prompt Readiness

Worker must not stage or commit. Reviewer/closer may commit only after proof,
receipt/audit/guide review, exact scope reconciliation, worker/reviewer gates,
and full roadmap closure diff PASS.

## Claim Boundary

This work order authorizes exactly five proof/documentation outputs. It does
not authorize apply/copy, real provenance/public-sync/cvf-web mutation, public
commit/push, provider/network calls, deployment, production, or availability.
