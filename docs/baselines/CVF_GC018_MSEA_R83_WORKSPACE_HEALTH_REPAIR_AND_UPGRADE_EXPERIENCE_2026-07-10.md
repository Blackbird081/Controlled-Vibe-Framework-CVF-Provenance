# CVF GC-018 MSEA R83 Workspace Health Repair And Upgrade Experience

Memory class: governed-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-10

Batch ID: MSEA-R83

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R83 --title "Workspace Health Repair And Upgrade Experience" --date 2026-07-10 --base 6de398232 --commit-mode WORKER_MAY_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | Replaced placeholders with source-backed R83 product and repository boundaries. |
| checkerReadAheadConfirmation | Read structural, dispatch, handoff, public-export, trace, and closure checker sources. |
| docOnlyNewFields | health verdict, check mode, issue code, repair action |
| claimBoundary | dispatch baseline only |

## Purpose

Authorize integrated R83A-R83E implementation, proof, bounded public export,
reviewer closure, and session synchronization.

## Scope / Applies To

Applies to public-safe workspace status, repair, management wrappers, existing
update integration, disposable Windows proof roots, exact public-sync export,
and R83 closure artifacts.

## Baseline Facts

| Fact | Evidence | Disposition |
|---|---|---|
| R82 Windows distribution candidate is public-synced. | R82 review commit `4bd363a81`; public commit `a4d5dba915` | ACCEPT |
| Profile manifests contain source commit, artifact paths, and SHA-256 values. | `scripts/sync_cvf_workspace_public_profile.ps1` | ACCEPT |
| Existing update validates remote and performs backup restoration. | `scripts/update_cvf_workspace_public_core.ps1` | ACCEPT |
| Root wrappers are generated from one public-safe source. | `scripts/install_cvf_workspace_root_wrappers_public.ps1` | ACCEPT |
| Public projection uses explicit allowlists and mapped exports. | `scripts/cvf-public-sync.ps1` | ACCEPT |

## Source / Predecessor Evidence

R82 completion review and the current distribution, profile, wrapper, update,
and public-sync sources were read directly. Chat history and provider-local
memory are not authority for R83 behavior.

## Allowed Scope

- R83 roadmap, baseline, work order, completion review, and session sync;
- `docs/reference/workspace_distribution/`;
- public-safe status, repair, management, wrapper, update, and sync scripts;
- disposable proof roots outside governed repositories;
- sibling public-sync clone after local proof passes.

## Forbidden Scope

No `Policy_Local`, operator-local distribution, provider/live, runtime
application, checker, hook, Fast Lane, cross-platform, hosted, entitlement,
Memory/RAG, retrieval, vectorization, or legal-workflow expansion.

## Fail Conditions

Return `BLOCKED_WITH_REASON` for a wrong remote, status mutation, repair that
changes profile or core HEAD, failed rollback, protected-token leak, or public
changed set outside the named R83 projection.

## Evidence / Verification

Required evidence includes parser checks, status JSON, before/after core and
profile state, artifact hashes, valid repair, valid update, forced rollback,
exact repository diffs, public checks, and pushed SHA equality.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`workspace-distribution`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class workspace-distribution --role dispatcher --lifecycle-phase dispatch --max-results 20 --json` |
| Returned defect count | 0 |
| Disclosed defectIds | N/A with reason: no matching resolver result. |
| Dispatch impact | direct source verification and command-backed product evidence remain required |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; section name: Purpose; section name: Scope / Applies To; section name: ADIF Defect Registry Disclosure; section name: Agent Operation Trace Block; section name: Public Export Disposition |
| gateRunPurpose | confirmation before dispatch |
| claimBoundary | R83 dispatch authority only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex dispatcher |
| Provider or surface | provenance repository |
| Session or invocation | MSEA-R83 integrated dispatch, 2026-07-10 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, git, rg, apply_patch, governance gates |
| Target paths | R83 roadmap, baseline, and work order |
| Allowed scope source | operator authorization to complete all R83 tranches |
| Before status evidence | clean provenance and public-sync worktrees at dispatch base `6de398232` |
| After status evidence | dispatch artifacts only before commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | bounded Windows workspace operability and public export |
| Claim boundary | no implementation or release result claimed at dispatch |
| Agent type | dispatcher |
| Invocation ID | `msea-r83-integrated-dispatch-2026-07-10` |
| Expected manifest | R83 roadmap, baseline, and work order |
| Actual changed set | R83 roadmap, baseline, and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this dispatch baseline remains private provenance authority.

## Claim Boundary

This baseline authorizes R83 execution but proves no status, repair, update, or
public-release behavior by itself.
