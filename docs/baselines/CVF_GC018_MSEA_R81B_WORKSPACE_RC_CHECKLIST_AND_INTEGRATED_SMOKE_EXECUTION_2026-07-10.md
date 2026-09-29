# CVF GC-018 MSEA R81B Workspace RC Checklist And Integrated Smoke Execution

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: MSEA-R81B

Dispatch base head: 0eb40983e

Commit mode: WORKER_MAY_COMMIT

Decision owner: operator-authorized orchestrator

Reviewer owner: reviewer/closer role

## Purpose

Define the compact Workspace release-candidate checklist and execute the
roadmap's R81C, R81D, and R81E local smoke evidence as one bounded sequence.
The integrated sequence is authorized to avoid unnecessary document-only
tranche pauses after R81A established the source map and boundary controls.

## Decision / Baseline / Proposed Tranche

Dispatch one bounded packet: define the checklist, run only the roadmap-listed
local smoke commands, and issue an evidence-backed R81F decision.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA-R81B --title "Workspace Productization RC Checklist Definition" --date 2026-07-10 --base 0eb40983e --commit-mode WORKER_MAY_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch with WORKER_MAY_COMMIT |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | Replaced placeholders with source-verified workspace-only scope. |
| checkerReadAheadConfirmation | Read dispatch-quality, structural, handoff, read-ahead, export, and Delta checker sources. |
| docOnlyNewFields | Workspace RC checklist; integrated local smoke evidence; bounded RC decision. |
| claimBoundary | Dispatch authoring only; no runtime, provider, live, public-sync, Web, MCP, or downstream-app behavior claim. |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| R81A source map | `60dfb0495`; R81A completion review | Reviewer accepted R81A and session state routes to R81B. | ACCEPT |
| R81 roadmap | roadmap R81A/R81B-R81F rows | R81A evidence permits checklist authoring; operator authorized autonomous completion of the R81 roadmap. | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`documentation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, riskCeiling=`LOW`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class documentation --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling LOW --json`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Returned defect count | 0 |
| Disclosed defectIds | N/A with reason: resolver returned no matching defects. |
| Dispatch impact | Use checker read-ahead and direct command evidence; no ADIF-specific remediation applies. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| R81 requires checklist, fresh-project, adoption, and update proof before RC closure. | LITERAL_INVARIANT | `docs/roadmaps/CVF_MSEA_R81_WORKSPACE_PRODUCTIZATION_RELEASE_CANDIDATE_ROADMAP_2026-07-09.md` | Roadmap Tranches; Acceptance Criteria | `R81B`; `R81C`; `R81D`; `R81E`; `R81F` | R81 roadmap | ACCEPT |
| Bootstrap creates a governed project from the local workspace root. | RUNTIME_BEHAVIOR | `scripts/new-cvf-workspace.ps1` | parameter block and bootstrap flow | `new-cvf-workspace.ps1` | workspace bootstrap script | ACCEPT |
| Public-core reconcile refreshes workspace wrappers and rules. | RUNTIME_BEHAVIOR | `scripts/update_cvf_workspace_public_core.ps1` | wrapper installer invocation | `workspaceWrapperInstallerPath` | workspace update script | ACCEPT |
| Rule-pack sync accepts profile selection and requires explicit continuity allowance for private material. | RUNTIME_BEHAVIOR | `scripts/sync_cvf_workspace_rule_pack.ps1` | parameter block; profile resolution | `ProfileName`; `AllowProvenanceContinuity` | workspace rule-pack sync | ACCEPT |
| Project doctor and workspace-wide gate are local workspace evidence commands. | EXISTS | `scripts/check_cvf_workspace_agent_enforcement.ps1`; `scripts/check_cvf_workspace_new_project_enforcement.ps1` | parameter blocks | `check_cvf_workspace_agent_enforcement.ps1`; `check_cvf_workspace_new_project_enforcement.ps1` | workspace verification scripts | ACCEPT |

## Scope And Stop Lines

Allowed actions:

- create one compact checklist reference and one integrated smoke/closure review;
- use disposable projects outside `Policy_Local` for fresh bootstrap and
  existing-project adoption proof;
- run the documented local workspace update wrapper and restore the existing
  `operator-local` profile after profile smoke;
- update the R81 roadmap only with evidence-backed status and closure result.

Forbidden actions:

- edit runtime, provider, checker, hook, Fast Lane, or downstream app source;
- mutate public-sync, push public output, or make hosted/production claims;
- read private/generated MinerU output or perform Memory/RAG, retrieval,
  vectorization, legal workflow, or provider/live proof.

## Work Plan

1. Define the checklist.
2. Run only disposable fresh/adoption and documented workspace-update commands.
3. Close R81 only from recorded command evidence.

## Acceptance Criteria

Fresh bootstrap, adopt-existing enforcement, profile boundary safety, and
update repeatability must pass, or the final decision must name the blocker.

## Verification / Evidence

Use command output, exact changed paths, and phase-gate results from the
integrated worker review.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | WORKER_MAY_COMMIT |
| rolePattern | Codex orchestrator/worker/reviewer-closer with explicit command evidence |
| dispatchBaseHead | `0eb40983e` |
| executionBaseHead | worker must capture before local smoke execution |
| changedSet | baseline, work order, checklist, review, and R81 roadmap only |
| traceDisposition | every committed governed artifact carries an Agent Operation Trace Block |
| commitOwner | Codex worker for bounded documentation and local smoke evidence |
| crossBatchIsolation | no R73F, public-sync, Policy_Local, runtime, provider, or use-case work |
| nextMoveSurfaces | reviewer/closer updates them only after evidence-backed R81F decision |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `Status:`; `Source Verification Block`; `ADIF Defect Registry Disclosure`; `Agent Handoff Contract Control Block`; `Execution Plan`; `Acceptance Criteria`; `Public Export Disposition` |
| gateRunPurpose | confirmation evidence before dispatch, not first discovery |
| claimBoundary | dispatch-shape confirmation only; no checker semantic change |

## Claim Boundary

This baseline authorizes bounded local workspace product evidence only. It does
not authorize public export, public release, provider/live proof, production
readiness, or downstream application behavior changes.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance dispatch packet; no public-sync work is
authorized.
