# CVF Agent Work Order MSEA R82 Workspace Distribution And Update Release

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: MSEA-R82

Commit mode: WORKER_MAY_COMMIT

Worker: implementation worker role

Reviewer/closer: reviewer/closer role

## Dispatch Prompt Envelope

Role: implementation worker role

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_MSEA_R82_WORKSPACE_DISTRIBUTION_AND_UPDATE_RELEASE_2026-07-10.md`

Commit mode: WORKER_MAY_COMMIT

Current-time notes: R81 is RC_PASS_BOUNDED at `c067328d5` and both repository
worktrees were clean at dispatch authoring.

Do-not-misread notes: public Windows distribution proof is not hosted,
cross-platform, paid-user production, provider, or downstream-app proof.

Required first actions: read required sources and run pre-implementation before
the first product-file edit or disposable install command.

Return contract: implement, verify, review, commit, and public-sync only when
all boundary checks pass; otherwise return `BLOCKED_WITH_REASON`.

executionBaseHead: capture current HEAD before implementation.

closureBaseHead: current dispatch material commit.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R82 --title "Workspace Distribution And Update Release" --date 2026-07-10 --base 297cb02c4 --commit-mode WORKER_MAY_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch with WORKER_MAY_COMMIT |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | Replaced placeholders with verified installer/update/public-sync contracts. |
| checkerReadAheadConfirmation | Read structural, dispatch, handoff, public-export, trace, and Delta checker sources. |
| docOnlyNewFields | distributionVersion; supportedShells; profileArtifacts |
| claimBoundary | integrated R82 execution only |

## Purpose

Execute R82A-R82F as one integrated product batch without tranche-by-tranche
operator pauses.

## Authority Chain

Operator authorization -> R82 roadmap -> paired GC-018 baseline -> integrated
worker execution -> reviewer closure -> bounded public-sync steward action.

## Agent Roles

| Role | Responsibility |
|---|---|
| dispatcher | source verification and bounded packet |
| implementation worker | product files and disposable proof |
| reviewer/closer | evidence audit, roadmap decision, continuity |
| public-sync steward | remote verification, bounded commit, public push |

## Single-Agent Multi-Role Control Block

Role route: SINGLE_AGENT_MULTI_ROLE. The same operator-authorized agent may
perform all roles, while phase gates, exact diffs, and separate repository
commits preserve decision boundaries. Independent review is not claimed.

Role separation ledger: dispatcher authors authority; worker implements and
records commands; reviewer audits evidence; public-sync steward verifies the
public remote and changed set.

Self-review boundary: same-agent review is allowed by the operator for this
bounded batch, but independent review is not claimed and command evidence is
required for every acceptance statement.

Escalation conditions: boundary leak, wrong remote, rollback failure, or an
external authority gap. Gate sequence: pre-dispatch, pre-implementation,
pre-closure, and pre-push.

## Required First Reads

| File | Required action |
|---|---|
| `CVF_SESSION_MEMORY.md` | READ |
| `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | READ |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | READ |
| `AGENT_HANDOFF_V40_2026-07-10.md` | READ |
| `docs/reference/guard_orientation/README.md` | READ |
| `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md` | READ |
| `docs/reference/CVF_AGENTS_CRITICAL_REPOSITORY_BOUNDARY_2026-06-23.md` | READ |
| paired R82 roadmap and baseline | READ |

## Scope / Methodology

Build the minimum public-safe Windows installer/profile surface, prove it on
disposable workspaces, exercise existing update/restore behavior, export the
bounded changed set to public-sync, and close from command evidence.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Bootstrap clones the public repository into the hidden core. | `scripts/new-cvf-workspace.ps1` | initial bootstrap flow | `cvfCorePath` | workspace bootstrap script | ACCEPT |
| Reconciler validates public remote and restores backup on failure. | `scripts/update_cvf_workspace_public_core.ps1` | required core, backup, try/catch flow | `Assert-PathInsideWorkspace`; `backupPath`; `publicRemote` | workspace update script | ACCEPT |
| Public wrapper installer writes root update and project wrappers. | `scripts/install_cvf_workspace_root_wrappers_public.ps1` | generated artifact writes | `Set-WorkspaceArtifact`; `workspaceUpdateWrapper` | public wrapper source | ACCEPT |
| Public-sync script exports only allowlisted scripts and mapped files. | `scripts/cvf-public-sync.ps1` | allowlist and mapped export declarations | `ALLOWED_SCRIPT_FILES`; `MAPPED_FILES`; `WORKSPACE_KIT_FILES` | public-sync script | ACCEPT |
| Public and paid profile source documents exist. | `docs/reference/CVF_WORKSPACE_PROFILE_TIERS.md` | Product Profile Matrix | `public-free`; `paid-user-safe` | workspace profile reference | ACCEPT |

## New Doc-Only Fields

| Field | Purpose |
|---|---|
| distributionVersion | version of the standalone distribution contract |
| supportedShells | bounded Windows shell compatibility claim |
| profileArtifacts | public-safe profile-to-artifact mapping |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`documentation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, riskCeiling=`MEDIUM`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class documentation --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling MEDIUM --json` |
| Returned defect count | 0 |
| Disclosed defectIds | N/A with reason: no matching resolver result. |
| Dispatch impact | direct source verification and exact changed-set proof remain required |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

route: WORKER_MAY_COMMIT

rolePattern: SINGLE_AGENT_MULTI_ROLE

phase: dispatch, implementation, reviewer closure, public-sync

baseHeadFor(phase): dispatch current HEAD; execution captured before edits;
closure execution base; public-sync refreshed public head

changedSetScope(phase): named R82 product/docs paths, then exact public-safe
public-sync projection

traceScope(phase, actor): command evidence and exact repository diffs

commitOwner(phase): worker for product material; reviewer/closer for closure
and continuity; public-sync steward for public commit

dispatchBaseHead: `297cb02c4`

executionBaseHead: capture before implementation

closureBaseHead: dispatch material commit

| Field | Value |
|---|---|
| route | WORKER_MAY_COMMIT |
| rolePattern | SINGLE_AGENT_MULTI_ROLE |
| phase | dispatch then implementation then reviewer/public closure |
| baseHeadFor(phase) | dispatch `297cb02c4`; later phases command-captured |
| changedSetScope(phase) | R82 product files, closure docs, public-safe projection |
| traceScope(phase, actor) | exact diffs and commands for each repository |
| commitOwner(phase) | assigned worker/reviewer/public-sync steward roles |
| crossBatchIsolation | no Policy_Local, operator-local export, provider, runtime app, checker, hook, or Fast Lane work |
| nextMoveSurfaces | reviewer/closer session-sync only after final decision |

Before status evidence: clean worktree; provenance `main...origin/main` and
public-sync `main...origin/main` returned no pending paths.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| Intake summary | operator selected full R82A-R82F completion |
| Scope classification | bounded Windows workspace product distribution and public export |
| Risk sensitivity | filesystem, update rollback, and repository boundary; no provider/secret/runtime claim |
| Selected role route | SINGLE_AGENT_MULTI_ROLE |
| Role separation basis | phase gates and exact repository evidence |
| Escalation condition | wrong remote, leakage, failed restore, or forbidden scope |

## Worker Autonomy / No-Question Rule

Repair allowed-scope implementation and artifact-shape defects directly. Ask
the operator only when a required decision exceeds the explicit R82 authority.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order implementation | Disposition |
|---|---|---|
| R82A manifest/version | create stable public distribution manifest and README | ACCEPT |
| R82B installer/profile sync | implement standalone installer and public profile materializer | ACCEPT |
| R82C shell proof | run clean-room install with available required shells | ACCEPT |
| R82D update/rollback | run successful update and forced invalid replacement restore | ACCEPT |
| R82E profile proof | prove public profiles and reject operator-local | ACCEPT |
| R82F public decision | sync bounded files, run public checks, commit/push only on PASS | ACCEPT |

## Write Ownership

Allowed provenance product paths:

- `docs/reference/workspace_distribution/`;
- `scripts/install_cvf_workspace.ps1`;
- `scripts/sync_cvf_workspace_public_profile.ps1`;
- `scripts/build_cvf_workspace_distribution.ps1`;
- `scripts/install_cvf_workspace_root_wrappers_public.ps1`;
- `scripts/update_cvf_workspace_public_core.ps1`;
- `scripts/cvf-public-sync.ps1`;
- `docs/reference/CVF_REFERENCE_ARTIFACT_INDEX.md`;
- R82 roadmap and final review.

Disposable targets and the sibling public-sync clone are allowed only for the
named evidence and public projection.

## Pre-Flight Checks

- capture execution base;
- confirm both repository remotes and clean worktrees;
- run pre-implementation;
- confirm PowerShell executable availability without treating an absent
  optional executable as a pass.

## Evidence Requirements

Record shell executable/version, command, target, exit status, profile,
manifest/checksum, hidden-core HEAD/remote, backup/restore disposition, public
changed set, gate results, commit IDs, and post-push equality.

## Evidence Reuse And Encoding Plan

verificationMode: REUSE_PRIOR_VERIFICATION

priorVerificationArtifact: `docs/reviews/CVF_MSEA_R81B_WORKSPACE_RC_INTEGRATED_SMOKE_AND_CLOSURE_REVIEW_2026-07-10.md`

priorVerificationAnchor: `c067328d5`

freshRecomputeRequired: installer, profile, update, rollback, shell, leakage,
public diff, and public gate evidence

unicodePathHandling: use literal paths and UTF-8-safe readers; verify the
Vietnamese generated guide under both available Windows shells

extractedTextAuthority: current source files and command output only

## Execution Plan

1. Capture execution head and run pre-implementation.
2. Implement manifest, profile sync, standalone installer, builder, and root
   wrapper/update integration.
3. Parse scripts and run isolated build/install/profile/update/rollback proof.
4. Create the integrated completion review and close the roadmap only on PASS.
5. Commit provenance material, run pre-closure/pre-push, project the bounded
   public-safe set, run public checks, commit and push both authorized repos.
6. Session-sync once after final material/public commits.

## Acceptance Criteria

| Criterion | Required result |
|---|---|
| Version contract | machine-readable manifest and checksum-bearing built package |
| Installer | public remote only; supported profile allowlist; secret-free receipt |
| Shell proof | Windows PowerShell 5.1 and PowerShell 7 pass when installed |
| Update | current public core refresh and wrappers/profile reapply successfully |
| Rollback | forced invalid replacement restores prior core and usable wrappers |
| Profiles | public-free and paid-user-safe pass leakage scan; operator-local rejected |
| Public sync | exact bounded diff, public checks pass, public push succeeds |
| Closure | provenance/public commits, gates, and remaining boundaries recorded |

## Return-To-Orchestrator Conditions

Return only for a wrong remote, boundary leak, rollback failure, unavailable
required external authority, or a gate failure outside allowed remediation.

## Review Gate

Reviewer must compare roadmap, work order, final source, disposable proof,
public diff, and commit/push evidence before issuing R82F disposition.

## Closure Checklist

- [ ] R82A manifest/version contract complete.
- [ ] R82B installer/profile materializer complete.
- [ ] R82C available-shell clean-room proof complete.
- [ ] R82D update and rollback proof complete.
- [ ] R82E profile boundary proof complete.
- [ ] R82F public-sync and final decision complete.

## Operator Checkpoint

Operator authorized full R82A-R82F execution including bounded public-sync and
push as proposed. No production, hosted, provider, or downstream-app decision
is implied.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; section name: Dispatch Prompt Envelope; section name: Source Verification Block; section name: ADIF Defect Registry Disclosure; section name: Agent Handoff Contract Control Block; section name: Execution Plan; section name: Agent Operation Trace Block; section name: Delta Execution Claim Boundary Control Block |
| gateRunPurpose | confirmation before integrated dispatch |
| claimBoundary | R82 Windows distribution execution only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | provenance repository |
| Session or invocation | MSEA-R82 integrated work order, 2026-07-10 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, git, rg, apply_patch, governance gates |
| Target paths | R82 roadmap, baseline, and work order |
| Allowed scope source | operator authorization to complete R82A-R82F |
| Before status evidence | clean worktree; main tracking origin/main at `297cb02c4` |
| After status evidence | dispatch artifacts only before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | bounded Windows distribution and public-sync |
| Claim boundary | no implementation or public result claimed at dispatch |
| Agent type | dispatcher |
| Invocation ID | `msea-r82-integrated-work-order-2026-07-10` |
| Expected manifest | R82 roadmap, baseline, and work order |
| Actual changed set | R82 roadmap, baseline, and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | Windows workspace distribution and update proof |
| claimDisposition | CLAIM_REJECTED: no mandatory interception or runtime enforcement claim is made. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: installation metadata is an operational file, not a CVF runtime receipt. |
| actionEvidence | ACTION_EVIDENCE_PRESENT: install, profile, update, rollback, build, and git commands. |
| invocationBoundary | manually invoked local PowerShell and git commands |
| interceptionBoundary | no IDE, provider, network proxy, or downstream-app interception claim |
| claimLanguage | bounded public-safe Windows distribution result only |
| forbiddenExpansion | no hosted, production SLA, cross-platform, provider, or operator-local release claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: dispatch artifacts remain private. Product files may become `EXPORTED`
only in the final review after public commit and remote evidence exist.

## Claim Boundary

This work order authorizes integrated R82 execution and bounded public-sync. It
does not authorize any claim beyond the tested Windows workspace surface.
