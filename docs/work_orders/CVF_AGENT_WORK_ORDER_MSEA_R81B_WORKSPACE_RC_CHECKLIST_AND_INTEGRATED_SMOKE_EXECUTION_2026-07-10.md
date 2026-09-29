# CVF Agent Work Order MSEA R81B Workspace RC Checklist And Integrated Smoke Execution

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA-R81B

Dispatch base head: 0eb40983e

Commit mode: WORKER_MAY_COMMIT

Worker: worker role

Reviewer/closer: reviewer/closer role

## Dispatch Prompt Envelope

Role: worker role

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R81B_WORKSPACE_RC_CHECKLIST_AND_INTEGRATED_SMOKE_EXECUTION_2026-07-10.md`

Commit mode: WORKER_MAY_COMMIT

Current-time notes: R81A is reviewer accepted at `60dfb0495`.

Do-not-misread notes: local workspace evidence is not public, hosted, or production release proof.

Required first actions: read required sources, paired baseline, and listed checker sources before edits or workspace commands.

Return contract: commit only allowed artifacts after gates and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` with command evidence.

Create the compact R81 workspace RC checklist, then execute fresh bootstrap,
adopt-existing, profile-boundary, and workspace-update smoke evidence. Keep all
project targets disposable and outside `Policy_Local`. Return an exact bounded
RC decision, not a hosted or production claim.

executionBaseHead: worker must capture with `git rev-parse --short HEAD` before
the first allowed edit or disposable-workspace command.

closureBaseHead: `0eb40983e`

## Purpose

Complete the value-bearing R81 evidence path without turning its sequential
roadmap rows into unnecessary approval pauses. R81B defines the reusable
checklist; the same bounded packet executes R81C-R81E evidence; R81F is the
reviewer decision based on those command results.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R81B --title "Workspace Productization RC Checklist Definition" --date 2026-07-10 --base 0eb40983e --commit-mode WORKER_MAY_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch with WORKER_MAY_COMMIT |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | Replaced placeholders with source-verified R81 workspace evidence controls. |
| checkerReadAheadConfirmation | Read dispatch-quality, structural, handoff, read-ahead, export, and Delta checker sources. |
| docOnlyNewFields | Workspace RC checklist; integrated smoke review; bounded RC decision. |
| claimBoundary | Dispatch authoring only; no provider, runtime, public-sync, or downstream-app behavior claim. |

## Authority Chain

Operator authorization -> R81 roadmap -> R81A accepted source map -> paired
baseline -> worker execution -> reviewer/closer decision.

## Agent Roles

| Role | Responsibility |
|---|---|
| dispatcher | source-verified packet authoring |
| worker | local evidence commands and allowed artifacts |
| reviewer/closer | bounded R81F decision and session continuity |

## Single-Agent Multi-Role Control Block

Role route: SINGLE_AGENT_MULTI_ROLE. The same operator-authorized agent may
dispatch, execute, and review this low-risk local evidence batch, but phase
gates and the final evidence review remain separate decisions.

Role separation ledger: dispatcher authors the packet; worker records source
and command evidence; reviewer/closer checks the recorded diff and gates.
Evidence basis: source verification, command output, git diff, and gates rather
than agent memory. Self-review boundary: independent review is not claimed.
Escalation conditions: stop and return BLOCKED for forbidden scope, leakage, or
unsafe restoration. Gate sequence: pre-dispatch, pre-implementation,
pre-closure, then pre-push only when a remote push is authorized.

## Required First Reads

| File | Required action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V39_2026-07-08.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| paired MSEA-R81B baseline | READ |
| R81 roadmap and R81A source map | READ |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Checklist areas for hidden core, root wrappers, profiles, boundary, continuity, and update proof. | `docs/reference/CVF_MSEA_R81A_WORKSPACE_PRODUCTIZATION_RC_SOURCE_MAP_AND_BOUNDARY_CONFIRMATION_2026-07-09.md` | R81B Readiness Recommendation | `R81B Readiness Recommendation` | R81A reference artifact | ACCEPT |
| Fresh project bootstrap. | `scripts/new-cvf-workspace.ps1` | bootstrap flow | `new-cvf-workspace.ps1` | workspace bootstrap script | ACCEPT |
| Workspace update. | `scripts/update_cvf_workspace_public_core.ps1` | wrapper installer invocation | `workspaceWrapperInstallerPath` | workspace update script | ACCEPT |
| Paid and operator profile selection. | `scripts/sync_cvf_workspace_rule_pack.ps1` | profile resolution and continuity gate | `ProfileName`; `AllowProvenanceContinuity` | rule-pack sync script | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`documentation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, riskCeiling=`LOW`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class documentation --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling LOW --json` |
| Returned defect count | 0 |
| Disclosed defectIds | N/A with reason: no matching resolver result. |
| Dispatch impact | Direct source verification and command evidence remain required. |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

route: WORKER_MAY_COMMIT
rolePattern: SINGLE_AGENT_MULTI_ROLE
phase: dispatch, implementation, reviewer closure
baseHeadFor(phase): dispatch `0eb40983e`; execution captured at start; closure execution base
changedSetScope(phase): baseline/work order at dispatch; checklist/review/roadmap at execution
traceScope(phase, actor): exact governed paths and local command evidence for each role
commitOwner(phase): worker for allowed artifacts; reviewer/closer for final decision and session sync
dispatchBaseHead: `0eb40983e`
executionBaseHead: capture before execution
closureBaseHead: `0eb40983e`
Before status evidence: clean worktree; `git status --short --branch` returned `main...origin/main`.

| Field | Value |
|---|---|
| route | WORKER_MAY_COMMIT |
| rolePattern | dispatcher/worker/reviewer-closer |
| phase | dispatch then implementation then reviewer closure |
| baseHeadFor(phase) | dispatch `0eb40983e`; execution captured at start; closure execution base |
| changedSetScope(phase) | baseline/work order at dispatch; checklist/review/roadmap at execution |
| traceScope(phase, actor) | exact governed paths and local command evidence for each role |
| commitOwner(phase) | worker for allowed artifacts; reviewer/closer for final decision and session sync |
| crossBatchIsolation | no public-sync, Policy_Local, runtime, provider, or R73F work |
| nextMoveSurfaces | reviewer/closer session-sync after R81F decision |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| Intake summary | operator request for autonomous R81 completion after accepted R81A evidence. |
| Scope classification | bounded local workspace checklist and disposable smoke evidence; no app, public-sync, or runtime paths. |
| Risk sensitivity | local filesystem and workspace update risk only; public-sync, provider/live, secret, legal, and production risk are forbidden. |
| Selected role route | SINGLE_AGENT_MULTI_ROLE; role route is dispatcher -> worker -> reviewer/closer. |
| Role separation basis | one agent may perform the roles, with phase-gate and review evidence separating decisions. |
| Escalation condition | BLOCKED or stop for private-token leakage, unsafe restoration, forbidden scope, or required external authority. |

## Worker Autonomy / No-Question Rule

Worker must repair allowed-scope artifact-shape gate failures directly. Return
to orchestrator only for a source contradiction, forbidden-scope requirement,
or missing operator authority.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Source roadmap location | Work-order implementation | Disposition |
|---|---|---|---|
| R81B compact checklist | R81B tranche row | create reusable checklist reference | ACCEPT |
| R81C fresh-project smoke | R81C tranche row | disposable fresh project and doctor proof | ACCEPT |
| R81D adoption smoke | R81D tranche row | disposable existing project enforcement proof | ACCEPT |
| R81E update proof | R81E tranche row | local update wrapper and final gate proof | ACCEPT |
| R81F decision | R81F tranche row | integrated review and roadmap decision | ACCEPT |

## Pre-Flight Checks

clean worktree Before status evidence: `git status --short --branch` returned
`main...origin/main` at dispatch base `0eb40983e`. Run pre-implementation
autorun before any allowed workspace command.

## Write Ownership

Worker may write only the fulfillment-manifest artifacts and the R81 roadmap.
Disposable workspace targets may be created outside the provenance repository.

## Evidence Requirements

Record command, target path, result, profile, and restoration disposition for
every local smoke. Record exact git changed paths before the closure decision.

## Execution Plan

1. Capture execution base and run pre-implementation.
2. Create the compact checklist with commands and pass/fail meanings.
3. Create a disposable fresh project and prove bootstrap, project doctor, and
   `paid-user-safe` profile boundary behavior.
4. Create a disposable existing project and prove adopt-existing enforcement
   without reading or changing `Policy_Local`.
5. Run the local workspace update wrapper, confirm wrappers/guides remain
   present, and restore `operator-local` if any profile smoke changed it.
6. Run leakage scans on disposable public-free and paid-user-safe output.
7. Create the integrated review and update R81 roadmap only if every required
   command passes; otherwise write `RC_BLOCKED_WITH_REASON`.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| `docs/reference/CVF_WORKSPACE_RELEASE_CANDIDATE_CHECKLIST_2026-07-10.md` | Create compact reusable checklist with commands and pass/fail meanings. |
| `docs/reviews/CVF_MSEA_R81B_WORKSPACE_RC_INTEGRATED_SMOKE_AND_CLOSURE_REVIEW_2026-07-10.md` | Create source-backed R81C-R81F evidence and bounded decision. |
| `docs/roadmaps/CVF_MSEA_R81_WORKSPACE_PRODUCTIZATION_RELEASE_CANDIDATE_ROADMAP_2026-07-09.md` | Update tranche status and final roadmap status only after command evidence. |

## Acceptance Criteria

| Criterion | Required result |
|---|---|
| Checklist | concise commands cover core freshness, wrappers, profiles, continuity, doctor, and update. |
| Fresh proof | disposable fresh project passes doctor and paid-user-safe output has no private continuity token. |
| Adoption proof | disposable existing project passes adopt-existing enforcement without app-specific source. |
| Update proof | workspace update refreshes the hidden core/wrappers and final workspace gate passes. |
| Boundary | public-free and paid-user-safe outputs exclude private continuity; operator-local remains explicitly local-only. |
| Closure | review states `RC_PASS_BOUNDED` only if all listed commands pass; otherwise exact blocker. |

## Review Gate

Reviewer/closer checks command evidence, forbidden-scope status, profile
restoration, and pre-closure before accepting R81F.

## Closure Checklist

- [ ] Checklist reference created.
- [ ] Fresh and adoption smoke evidence recorded.
- [ ] Update proof and final workspace state recorded.
- [ ] R81 roadmap receives evidence-backed R81F decision.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for source contradiction, unsafe update failure,
private-token leakage, or a required command failure outside allowed remediation.

## Operator Checkpoint

N/A with reason: operator granted autonomous R81 completion; this packet does
not authorize a public, production, credential, or destructive decision.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_epistemic_process_packet.py` |
| literalTokensReviewed | section name: Purpose; section name: Scope / Methodology; section name: Findings / Position; section name: Risk / Corrective Action; section name: Agent Operation Trace Block; section name: Delta Execution Claim Boundary Control Block; `DEFERRED_PRIVATE_ONLY`; `RC_PASS_BOUNDED` |
| gateRunPurpose | confirmation evidence before authoring and closure, not first discovery |
| claimBoundary | applies only to R81B-F bounded workspace artifacts |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <executionBaseHead> --head HEAD
git diff --name-status
git status --short
```

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher role |
| Provider or surface | local provenance workspace |
| Session or invocation | MSEA-R81B dispatch authoring, 2026-07-10 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, git, rg, apply_patch, governance gates |
| Target paths | paired R81B baseline and work order |
| Allowed scope source | R81 roadmap, accepted R81A, and operator autonomous-roadmap authorization |
| Before status evidence | clean worktree: `git status --short --branch` returned `main...origin/main` at `0eb40983e` |
| After status evidence | dispatch pair only before material commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | workspace RC checklist and local smoke evidence only |
| Claim boundary | no public-sync, provider/live, runtime, or downstream application mutation |
| Agent type | dispatcher role |
| Invocation ID | `msea-r81b-workspace-rc-integrated-dispatch-2026-07-10` |
| Expected manifest | paired R81B baseline and work order |
| Actual changed set | paired R81B baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch authoring |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | workspace RC checklist and local smoke evidence |
| claimDisposition | CLAIM_REJECTED: no execution-control, mandatory-wrapper, direct-interception, or runtime-enforcement claim is made. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed. |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local wrapper, doctor, and rule-pack commands only. |
| invocationBoundary | manually invoked local PowerShell commands in disposable or existing operator workspace locations. |
| interceptionBoundary | no IDE, shell, provider, network, or downstream-app interception claim. |
| claimLanguage | bounded local workspace RC evidence only. |
| forbiddenExpansion | no public release, hosted readiness, provider/live proof, or Policy_Local mutation. |

## Claim Boundary

This work order authorizes a bounded local workspace release-candidate proof.
It does not authorize CVF public release, paid-user production deployment,
public-sync mutation, provider/live behavior, or downstream project changes.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: all outputs are private provenance evidence; public-sync needs a
separate packet and public repository decision.
