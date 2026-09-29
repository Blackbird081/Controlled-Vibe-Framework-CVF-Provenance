# CVF Agent Work Order MSEA R84 Lean Governance Follow-Through

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work-order

Date: 2026-07-10

Batch ID: MSEA-R84

Commit mode: WORKER_MAY_COMMIT

Worker: implementation worker role

Reviewer/closer: evidence-bound reviewer role

## Dispatch Prompt Envelope

Role: sequential dispatcher, implementer, tester, reviewer, and closer

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R84_LEAN_GOVERNANCE_FOLLOW_THROUGH_2026-07-10.md`

Commit mode: WORKER_MAY_COMMIT

Current-time notes: R83 is closed and public-synced; provenance begins clean at
`d04b64c6c`; R73F remains parked.

Do-not-misread notes: compact docs-only return routing is not global checker
demotion, checker retirement, public-sync, or runtime authorization.

Required first actions: read the named sources, capture the execution base,
and pass pre-implementation before behavioral edits.

executionBaseHead: capture after the dispatch commit.

Return contract: complete R84A-R84D without pausing while evidence remains in
scope; otherwise return `BLOCKED_WITH_REASON`.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R84 --title "Lean Governance Follow-Through" --date 2026-07-10 --base d04b64c6c --commit-mode WORKER_MAY_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | Replaced placeholders with source-backed integrated R84 execution controls. |
| checkerReadAheadConfirmation | Read all checker sources listed below before dispatch. |
| docOnlyNewFields | compact profile, scope classification, conditional controls disposition |
| claimBoundary | integrated R84 work order |

## Purpose

Implement the smallest useful R72 follow-through: a dispatch-authorized compact
docs-only worker-return profile and a source-backed lifecycle disposition for
the existing worker-return quality checker.

## Authority Chain

Operator authorization -> R84 roadmap -> R84 GC-018 -> this work order ->
focused tests and A/B evidence -> completion review -> session sync.

## Agent Roles

The assigned agent acts sequentially as dispatcher, implementer, tester, reviewer/closer,
and session-sync steward. Command evidence and commit ranges preserve the phase
boundaries; independent review is not claimed.

## Single-Agent Multi-Role Control Block

Role route: SINGLE_AGENT_MULTI_ROLE.

Role separation ledger: dispatch defines authority; implementation changes the
contract; tests prove behavior; review compares source and evidence; closure
updates state.

Self-review boundary: same-agent review is authorized for this bounded pilot,
but no independent-review claim is allowed.

Escalation conditions: any fail condition in the GC-018 baseline.

Gate sequence: pre-dispatch, pre-implementation, pre-closure, and pre-push.

## Required First Reads

| Source | Disposition |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V40_2026-07-10.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| R72B inventory and R72C case matrix | READ |

## Scope / Methodology

Define the compact profile in existing standards and dispatch machinery,
generate a compact scaffold, validate it in the existing quality checker, and
prove both backward compatibility and fail-closed protected controls.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| R72C compact eligibility is dispatch-time and excludes public/live/runtime actions. | `docs/reference/CVF_MSEA_R72C_FAST_LANE_CALIBRATION_AND_RISK_CLASS_ROUTER_CASE_MATRIX_2026-07-08.md` | Risk-Class Routing Design | `FAST_DOC_LANE` | R72C routing proposal | ACCEPT |
| The three consolidatable sections are explicitly named. | `docs/reference/CVF_MSEA_R72C_FAST_LANE_CALIBRATION_AND_RISK_CLASS_ROUTER_CASE_MATRIX_2026-07-08.md` | Risk-Class Routing Design | conditional sections | R72C routing proposal | ACCEPT |
| Protected evidence must remain required. | `docs/reference/CVF_MSEA_R72C_FAST_LANE_CALIBRATION_AND_RISK_CLASS_ROUTER_CASE_MATRIX_2026-07-08.md` | Protected-Control Preservation Matrix | source verification; command evidence; no-commit; trace | R72C routing proposal | ACCEPT |
| The quality checker owns required return headings. | `governance/compat/check_worker_return_quality_gate.py` | constants and `diagnose` | `REQUIRED_HEADINGS`; `diagnose` | worker-return quality gate | ACCEPT |
| Dispatch quality owns no-commit profile literals. | `governance/compat/check_work_order_dispatch_quality.py` | worker-return contract constants | `WORKER_RETURN_FULL_GATE_PROFILE` | work-order dispatch gate | ACCEPT |
| Return scaffolds own generated heading shape. | `governance/compat/run_worker_return_scaffold.py`; `governance/compat/build_worker_return_skeleton_scaffold.py` | scaffold section declarations | `WORKER_RETURN_SCAFFOLD_SECTIONS`; `build_worker_return_skeleton` | worker-return scaffold helpers | ACCEPT |

## New Doc-Only Fields

| Field | Purpose |
|---|---|
| `scopeClassification` | exact dispatch eligibility token |
| `contractProfile` | full or compact worker-return contract selector |
| `conditionalControlsDisposition` | compact reason for the three non-applicable controls |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`governance-control`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class governance-control --role dispatcher --lifecycle-phase dispatch --max-results 20 --json` |
| Returned defect count | 0 |
| Disclosed defectIds | N/A with reason: no matching resolver result. |
| Dispatch impact | source-backed profile and negative eligibility tests are mandatory |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

route: WORKER_MAY_COMMIT

rolePattern: SINGLE_AGENT_MULTI_ROLE

phase: dispatch, implementation, reviewer closure, session-sync

baseHeadFor(phase): dispatch `d04b64c6c`; later phases command-captured

changedSetScope(phase): named R84 standards, helpers, checkers, tests, index,
closure, and session paths

traceScope(phase, actor): exact commands, diffs, tests, and commits

commitOwner(phase): assigned agent in the active sequential role

dispatchBaseHead: `d04b64c6c`

executionBaseHead: capture after dispatch commit

closureBaseHead: implementation material commit

| Field | Value |
|---|---|
| route | WORKER_MAY_COMMIT |
| rolePattern | SINGLE_AGENT_MULTI_ROLE |
| phase | dispatch through session sync |
| baseHeadFor(phase) | dispatch `d04b64c6c`; later phases command-captured |
| changedSetScope(phase) | R84 contract/checker/scaffold/test/index/closure paths, then session-only paths |
| traceScope(phase, actor) | exact commands and changed sets per role |
| commitOwner(phase) | assigned agent in each declared sequential role |
| crossBatchIsolation | no public-sync, runtime, provider/live, R73F, workspace distribution, or use-case work |
| nextMoveSurfaces | closer updates only after final evidence |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| Intake summary | operator authorized bounded Lean Governance Follow-Through |
| Scope classification | governance authoring/checker calibration |
| Risk sensitivity | protected evidence and dispatch eligibility |
| Selected role route | SINGLE_AGENT_MULTI_ROLE |
| Escalation condition | any weakening, false eligibility, or backward incompatibility |

## Worker Autonomy / No-Question Rule

Repair allowed-scope code, test, and artifact-shape defects without operator
interruption. Revert or block rather than widen the authorized design.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order action | Disposition |
|---|---|---|
| R84A profile | ratify exact dispatch and return tokens | ACCEPT |
| R84B behavior | implement conditional checker/scaffold routing | ACCEPT |
| R84C proof | run full/compact/negative tests and measure shape | ACCEPT |
| R84D closure | update GCI, review, push, and session-sync | ACCEPT |

## Allowed Scope

- worker-return quality/full-gate standards and work-order template;
- existing dispatch/return scaffold helpers and their focused tests;
- existing dispatch-quality and worker-return quality checkers and tests;
- Governance Control Index and R84 artifacts;
- final active session continuity paths.

## Write Ownership

Write ownership is limited to the paths and path families named in Allowed
Scope. Generated state must be changed through its source fragments and
generator during final session sync.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| durableFoundationFiles | existing worker-return standards and GCI only |
| storageClass | ACTIVE_REFERENCE in existing canonical directories |
| indexDisposition | update existing GCI row/table; no new front door |
| relocationDisposition | N/A with reason: no file move, rename, or new foundation directory |
| publicBoundary | DEFERRED_PRIVATE_ONLY |

## Forbidden Scope

No new checker/hook, global demotion, checker retirement, public-sync,
runtime/provider/live proof, product source, R73F, workspace distribution,
Memory/RAG, retrieval, or downstream use case.

## Execution Plan

1. Gate and commit the integrated dispatch packet.
2. Add the compact profile with dispatch-authenticated eligibility.
3. Add focused full, compact, and fail-closed tests.
4. Measure old versus compact conditional format tax.
5. Record the checker disposition in GCI, close, push, and session-sync.

## Pre-Flight Checks

- capture execution base and clean status;
- run pre-implementation;
- confirm no public-sync or product path is present;
- read the exact checker and scaffold functions before editing.

## Evidence Requirements

Record focused test output, negative cases, generated scaffold shape counts,
full-profile compatibility, autorun results, changed paths, commits, and remote
equality. Claims without command evidence fail closure.

## Acceptance Criteria

- full returns remain accepted unchanged;
- compact returns need one disposition block instead of three headings;
- compact profile without matching work-order evidence fails;
- protected evidence omissions fail in both profiles;
- conditional heading/line burden falls at least 30 percent;
- no forbidden path changes.

## Verification Commands

- `python -m unittest governance.compat.test_check_worker_return_quality_gate`
- `python -m unittest governance.compat.test_check_work_order_dispatch_quality_worker_return_contract`
- `python -m unittest governance.compat.test_run_worker_return_scaffold`
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation`
- `python governance/compat/run_agent_commit_steward_preflight.py --mode implementation --base <base> --head HEAD --enforce`

## Review Gate

Compare roadmap, baseline, work order, source diff, focused tests, A/B measure,
negative cases, GCI disposition, and forbidden-scope diff before closure.

## Closure Checklist

- [ ] Compact profile is dispatch-authenticated.
- [ ] Full profile remains backward compatible.
- [ ] Protected controls fail closed.
- [ ] Conditional format tax reduction meets threshold.
- [ ] GCI and closure/session state are aligned.

## Return-To-Orchestrator Conditions

Return only for a baseline fail condition or authority missing outside this
work order. Allowed-scope implementation and formatting defects are repaired
autonomously.

## Operator Checkpoint

The operator authorized complete bounded R84 execution. No intermediate pause
is required while work remains inside scope.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `WORKER_MAY_COMMIT`; `Source Verification Block`; `Agent Handoff Contract Control Block`; `Roadmap-To-Work-Order Trace Matrix` |
| gateRunPurpose | confirmation before integrated execution |
| claimBoundary | R84 lean worker-return contract only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | provenance repository |
| Session or invocation | MSEA-R84 integrated work order, 2026-07-10 |
| Working directory | repository root |
| Command or tool surface | PowerShell, git, rg, apply_patch, governance gates |
| Target paths | R84 dispatch artifacts |
| Allowed scope source | operator authorization for Lean Governance Follow-Through |
| Before status evidence | clean worktree at `d04b64c6c` |
| After status evidence | dispatch artifacts only before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | one compact profile and one checker disposition |
| Claim boundary | no implementation result at dispatch |
| Agent type | dispatcher |
| Invocation ID | `msea-r84-integrated-work-order-2026-07-10` |
| Expected manifest | R84 roadmap, baseline, and work order |
| Actual changed set | R84 roadmap, baseline, and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | worker-return authoring and validation behavior |
| claimDisposition | CLAIM_REJECTED: no runtime/provider enforcement is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: dispatch creates no runtime receipt. |
| actionEvidence | ACTION_EVIDENCE_PRESENT: planned local tests, gates, git, and scaffold commands. |
| invocationBoundary | manually invoked local tooling only |
| interceptionBoundary | no IDE, shell, provider, CLI, MCP, Web, or runtime interception |
| claimLanguage | bounded authoring/checker pilot |
| forbiddenExpansion | no public/runtime/provider/product or global checker change |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance-control implementation only.

## Claim Boundary

This work order authorizes R84 only; it does not claim that a general Lean
Governance program or checker-retirement program is complete.
