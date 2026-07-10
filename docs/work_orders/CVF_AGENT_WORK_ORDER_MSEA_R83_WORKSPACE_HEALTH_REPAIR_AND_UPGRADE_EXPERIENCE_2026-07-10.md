# CVF Agent Work Order MSEA R83 Workspace Health Repair And Upgrade Experience

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work-order

Date: 2026-07-10

Batch ID: MSEA-R83

Commit mode: WORKER_MAY_COMMIT

Worker: implementation worker role

Reviewer/closer: reviewer/closer role

## Dispatch Prompt Envelope

Role: implementation worker role

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R83_WORKSPACE_HEALTH_REPAIR_AND_UPGRADE_EXPERIENCE_2026-07-10.md`

Commit mode: WORKER_MAY_COMMIT

Current-time notes: R82 is `RC_PASS_BOUNDED_AND_PUBLIC_SYNCED`; both repository
worktrees were clean at R83 dispatch authoring.

Do-not-misread notes: workspace health and recovery proof is not production,
cross-platform, hosted, entitlement, provider, or downstream-app proof.

Required first actions: read the required sources, capture executionBaseHead,
and run pre-implementation before product edits.

Return contract: execute R83A-R83E, verify, review, commit, and public-sync only
when all boundaries pass; otherwise return `BLOCKED_WITH_REASON`.

executionBaseHead: capture current HEAD after dispatch commit.

closureBaseHead: R83 implementation material commit.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R83 --title "Workspace Health Repair And Upgrade Experience" --date 2026-07-10 --base 6de398232 --commit-mode WORKER_MAY_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | Replaced placeholders with source-backed R83 execution controls. |
| checkerReadAheadConfirmation | Read the listed checker sources before dispatch. |
| docOnlyNewFields | health verdict, issue code, repair action, remote-check mode |
| claimBoundary | integrated R83 work order |

## Purpose

Deliver a supportable Windows workspace health and recovery experience on top
of the accepted R82 distribution candidate.

## Authority Chain

Operator authorization -> R83 roadmap -> R83 GC-018 baseline -> this work
order -> command evidence -> completion review -> session sync.

## Agent Roles

The assigned agent acts sequentially as dispatcher, implementer, tester,
reviewer/closer, public-sync steward, and session-sync steward. Evidence and
commit ranges must remain phase-separated.

## Single-Agent Multi-Role Control Block

Role route: SINGLE_AGENT_MULTI_ROLE. The same operator-authorized agent may
perform all roles, while phase gates, exact diffs, and separate repository
commits preserve decision boundaries. Independent review is not claimed.

Role separation ledger: dispatcher authors authority; worker implements;
tester records disposable proof; reviewer audits source and evidence;
public-sync steward verifies remote and changed set; closer session-syncs.

Self-review boundary: same-agent review is allowed for this bounded batch, but
each acceptance claim requires command evidence and no independent review
claim may be made.

Escalation conditions: wrong remote, status mutation, repair changing core or
profile, failed rollback, leakage, or missing external authority.

Gate sequence: pre-dispatch, pre-implementation, pre-closure, and pre-push.

## Required First Reads

| Source | Disposition |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V40_2026-07-10.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` | READ |
| paired R83 roadmap and baseline | READ |

## Scope / Methodology

Implement the smallest status/repair/management surface that reuses the R82
manifest, profile checksum, wrapper generator, and update reconciler. Prove it
on disposable workspaces, export an exact public bundle, and close from fresh
evidence.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Public profile state records selected profile and source commit. | `scripts/sync_cvf_workspace_public_profile.ps1` | active manifest write | `activeProfile`; `sourceCommit`; `artifactCount` | public profile materializer | ACCEPT |
| Profile artifact hashes are recorded for drift comparison. | `scripts/sync_cvf_workspace_public_profile.ps1` | copied artifact record | `sourcePath`; `sha256` | rule-pack manifest | ACCEPT |
| Update validates remote, backup, fast-forward, and restoration. | `scripts/update_cvf_workspace_public_core.ps1` | public remote and try/catch update flow | `publicRemote`; `backupPath`; `workspaceWrapperInstallerPath` | workspace reconciler | ACCEPT |
| Root wrappers are generated from a public-safe source. | `scripts/install_cvf_workspace_root_wrappers_public.ps1` | generated wrapper declarations and writes | `workspaceUpdateWrapper`; `Set-WorkspaceArtifact` | wrapper installer | ACCEPT |
| Public workspace export is allowlisted. | `scripts/cvf-public-sync.ps1` | public script and workspace-kit lists | `ALLOWED_SCRIPT_FILES`; `WORKSPACE_KIT_FILES`; `MAPPED_FILES` | public-sync script | ACCEPT |
| R82 distribution version and supported profiles are machine-readable. | `docs/reference/workspace_distribution/CVF_WORKSPACE_DISTRIBUTION_MANIFEST.json` | root fields | `distributionVersion`; `supportedProfiles`; `requiredCoreFiles` | distribution manifest | ACCEPT |

## New Doc-Only Fields

| Field | Purpose |
|---|---|
| healthVerdict | one of the four R83 workspace health results |
| checkMode | local-only or remote-aware status execution |
| issueCode | stable diagnostic identifier for repair guidance |
| repairAction | bounded regeneration action taken by repair |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`workspace-distribution`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class workspace-distribution --role dispatcher --lifecycle-phase dispatch --max-results 20 --json` |
| Returned defect count | 0 |
| Disclosed defectIds | N/A with reason: no matching resolver result. |
| Dispatch impact | direct source verification and exact changed-set proof remain mandatory |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

route: WORKER_MAY_COMMIT

rolePattern: SINGLE_AGENT_MULTI_ROLE

phase: dispatch, implementation, reviewer closure, public-sync, session-sync

baseHeadFor(phase): dispatch `6de398232`; later phases command-captured

changedSetScope(phase): named R83 product paths, closure docs, and exact
public-safe projection

traceScope(phase, actor): commands, disposable targets, and repository diffs

commitOwner(phase): assigned agent in the active sequential role

dispatchBaseHead: `6de398232`

executionBaseHead: capture after dispatch commit

closureBaseHead: implementation material commit

| Field | Value |
|---|---|
| route | WORKER_MAY_COMMIT |
| rolePattern | SINGLE_AGENT_MULTI_ROLE |
| phase | dispatch through session sync |
| baseHeadFor(phase) | dispatch `6de398232`; later phases command-captured |
| changedSetScope(phase) | R83 product, closure, public-safe projection, then session-only paths |
| traceScope(phase, actor) | exact commands and diffs per role |
| commitOwner(phase) | assigned agent in each declared sequential role |
| crossBatchIsolation | no Policy_Local, operator-local, provider/live, runtime app, checker, hook, Fast Lane, or cross-platform work |
| nextMoveSurfaces | closer updates only after the final public decision |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| Intake summary | operator authorized complete R83 execution |
| Scope classification | Windows workspace product operability and bounded public release |
| Risk sensitivity | filesystem repair, update rollback, and repository boundary |
| Selected role route | SINGLE_AGENT_MULTI_ROLE |
| Escalation condition | wrong remote, mutation by status, profile/core change by repair, failed rollback, or leakage |

## Worker Autonomy / No-Question Rule

Repair allowed-scope implementation, proof, and artifact-shape defects without
operator interruption. Do not widen product or claim scope.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order implementation | Disposition |
|---|---|---|
| R83A status | implement deterministic local and optional remote health output | ACCEPT |
| R83B repair | regenerate missing/drifted public artifacts without changing core/profile | ACCEPT |
| R83C unified UX | generate one root status/update/repair command and update guides | ACCEPT |
| R83D migration | prove stale, missing, drift, repair, update, and rollback cases | ACCEPT |
| R83E release | exact public projection, checks, push, review, and session sync | ACCEPT |

## Write Ownership

Allowed product paths:

- `docs/reference/workspace_distribution/`;
- `scripts/get_cvf_workspace_status.ps1`;
- `scripts/repair_cvf_workspace.ps1`;
- `scripts/manage_cvf_workspace.ps1`;
- `scripts/install_cvf_workspace_root_wrappers_public.ps1`;
- `scripts/update_cvf_workspace_public_core.ps1`;
- `scripts/install_cvf_workspace.ps1`;
- `scripts/cvf-public-sync.ps1`;
- R83 roadmap and completion review;
- final session continuity paths.

Disposable proof roots and the sibling public-sync clone are allowed only for
R83 evidence and public projection.

## Pre-Flight Checks

- capture execution base and both repository remotes/status;
- run pre-implementation;
- parse every changed PowerShell script in both available shells;
- confirm proof targets are disposable and outside `Policy_Local`.

## Evidence Requirements

Record command, shell, target, verdict, issue codes, before/after profile and
core commit, file hashes, remote revision, rollback result, public changed set,
gate results, commits, and remote equality.

## Execution Plan

1. Commit and push the gated dispatch packet.
2. Implement status, repair, management wrappers, manifest version update, and
   public allowlists/guides.
3. Run clean, stale, missing, drift, repair, update, and rollback proof.
4. Commit/push provenance product material only after local proof passes.
5. Project and validate the exact public bundle, then commit/push public.
6. Close R83, run closure/push gates, commit, push, and session-sync once.

## Acceptance Criteria

| Criterion | Required result |
|---|---|
| Status contract | exact four-verdict vocabulary and valid JSON output |
| Read-only behavior | local and remote-aware status preserve workspace hashes and git state |
| Repair | active profile and core HEAD preserved; generated drift removed |
| Update | newer public revision detected and valid fast-forward succeeds |
| Rollback | invalid replacement restores exact prior core and usable wrappers |
| Public boundary | exact allowlisted diff and no private/provenance token |
| Closure | roadmap, review, commits, gates, and residual boundaries aligned |

## Return-To-Orchestrator Conditions

Return only for a fail condition named by the baseline or missing authority
outside this work order.

## Review Gate

Compare current source, roadmap, work order, disposable proof, exact public
diff, commits, remotes, and gates before issuing R83E disposition.

## Closure Checklist

- [ ] R83A status contract complete.
- [ ] R83B doctor and repair complete.
- [ ] R83C unified upgrade UX complete.
- [ ] R83D migration and rollback proof complete.
- [ ] R83E public release decision complete.

## Operator Checkpoint

Operator explicitly authorized complete R83 execution. No pause is required
between tranches when evidence remains inside this packet.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; section name: Dispatch Prompt Envelope; section name: Source Verification Block; section name: ADIF Defect Registry Disclosure; section name: Agent Handoff Contract Control Block; section name: Execution Plan; section name: Agent Operation Trace Block; section name: Delta Execution Claim Boundary Control Block |
| gateRunPurpose | confirmation before integrated dispatch |
| claimBoundary | R83 Windows workspace operability only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | provenance repository |
| Session or invocation | MSEA-R83 integrated work order, 2026-07-10 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, git, rg, apply_patch, governance gates |
| Target paths | R83 roadmap, baseline, and work order |
| Allowed scope source | operator authorization for complete R83 execution |
| Before status evidence | clean worktree in both repositories at dispatch base `6de398232` |
| After status evidence | dispatch artifacts only before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | bounded Windows workspace operability and public export |
| Claim boundary | no implementation or release claim at dispatch |
| Agent type | dispatcher |
| Invocation ID | `msea-r83-integrated-work-order-2026-07-10` |
| Expected manifest | R83 roadmap, baseline, and work order |
| Actual changed set | R83 roadmap, baseline, and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | Windows workspace status, repair, update UX, and public release evidence |
| claimDisposition | CLAIM_REJECTED: no provider interception or runtime-governance behavior is claimed. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: dispatch creates no operational receipt. |
| actionEvidence | ACTION_EVIDENCE_PRESENT: planned status, repair, update, rollback, git, and gate commands. |
| invocationBoundary | manually invoked local PowerShell and git commands |
| interceptionBoundary | no IDE, provider, proxy, hosted, or downstream-app interception claim |
| claimLanguage | bounded Windows workspace operability result only |
| forbiddenExpansion | no production, cross-platform, entitlement, operator-local, provider, or use-case claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: dispatch artifacts remain private. Product files become `EXPORTED`
only after a passing public commit exists.

## Claim Boundary

This work order authorizes integrated R83 execution only within the named
Windows product and repository boundaries.
