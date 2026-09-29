# CVF GC-018 Baseline - MSEA-R72F First Retirement Or Consolidation Pilot

Memory class: governed-dispatch-baseline
Status: DISPATCH_READY
Batch ID: MSEA_R72F_FIRST_RETIREMENT_OR_CONSOLIDATION_PILOT
Dispatch base head: 4050b0a37
Commit mode: WORKER_MUST_NOT_COMMIT
Decision owner: Operator
Reviewer owner: Codex reviewer/closer
Worker target: worker role

## Purpose

Dispatch a bounded R72F retirement/consolidation decision pilot using R72B-R72E evidence. The worker must select one non-`PROTECTED` checker/control candidate, prove whether retirement or consolidation criteria are satisfied, and return either a safe disposition or a source-backed hold reason.

This baseline does not authorize checker deletion, checker disablement, hook edit, Fast Lane standard edit, public-sync mutation, runtime/source/test edit, provider/live proof, merge, push, or public/production claim.

## Decision / Baseline

Decision: `DISPATCH_R72F_DECISION_PILOT`.

Baseline: R72F is authorized as a documentation-and-evidence-only decision pilot. Actual retirement, deletion, disablement, consolidation, hook edit, or checker source mutation remains outside this dispatch.

## Proposed Tranche

| Field | Value |
| --- | --- |
| trancheId | MSEA-R72F |
| trancheName | First Retirement Or Consolidation Pilot |
| workerMode | WORKER_MUST_NOT_COMMIT |
| outputType | decision matrix plus worker return |
| protectedControls | public/private boundary; source verification; no-commit plus reviewer separation; closure evidence |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R72F_FIRST_RETIREMENT_OR_CONSOLIDATION_PILOT --title "MSEA R72F First Retirement Or Consolidation Pilot" --date 2026-07-08 --base 4050b0a37 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Filled R72F source verification, candidate scope, no-delete boundary, and worker-return shape fields for a decision-only pilot. |
| checkerReadAheadConfirmation | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_dispatch_scaffold_provenance.py; governance/compat/check_agent_handoff_boundary.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_public_export_disposition.py |
| docOnlyNewFields | candidateControlRow; candidateCheckerFamily; retirementDisposition; missingEvidence |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order-authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work-order-authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | No ADIF-specific dispatch repair required. |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_dispatch_scaffold_provenance.py; governance/compat/check_agent_handoff_boundary.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_public_export_disposition.py |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Source Verification Block`; `Negative Search And Collision Discipline`; `Scaffold Provenance Block`; `Agent Handoff Contract Control Block`; `Reviewer Closure Conversion`; `WORKER_MUST_NOT_COMMIT`; `Public Export Disposition`; `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | Confirmation after checker-source read-ahead; gates are verification evidence, not first discovery. |
| claimBoundary | Read-ahead covers dispatch artifact shape only and does not prove retirement safety. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R72F must select one non-PROTECTED candidate or name a WATCH row with exact missing evidence | EXISTS | docs/reference/governance_control_index/CVF_GOVERNANCE_CONTROL_INDEX.md | R72 Routing table | `R72F` | Governance Control Index | ACCEPT |
| R72 roadmap requires fresh GC-018 and work order for R72F | EXISTS | docs/roadmaps/CVF_MSEA_R72_EA_ASSESSMENT_INTAKE_AND_GOVERNANCE_LOAD_REBALANCING_ROADMAP_2026-07-07.md | Work Plan row R72F | `R72F` | R72 roadmap | ACCEPT |
| R72B names cross-family approval artifact checkers as the strongest retirement-review candidate class | EXISTS | docs/reference/CVF_MSEA_R72B_GOVERNANCE_CONTROL_CHECKER_LIFECYCLE_INVENTORY_2026-07-08.md | R72F No-Silent-Zero-Retirement Guardrail | `R72F_RETIREMENT_REVIEW_CANDIDATE` | R72B inventory | ACCEPT |
| R72E preserves public/private boundary, source verification, no-commit plus reviewer separation, and closure evidence | EXISTS | docs/reference/CVF_MSEA_R72E_ABSORB_LANE_CEREMONY_RECLASSIFICATION_TAXONOMY_AND_TRACE_SEED_2026-07-08.md | Protected Control Preservation Matrix | `Protected control` | R72E taxonomy | ACCEPT |
| Cross-family approval artifact authority checker uses default manifest and packet paths | EXISTS | governance/compat/check_cross_family_approval_artifact_authority.py | constants near top of file | `DEFAULT_MANIFEST`, `DEFAULT_PACKET` | checker source | ACCEPT |
| Cross-family conformance script references the approval-artifact checker family but is not a local hook-catalog control | EXISTS | scripts/run_cvf_cross_family_packet_coverage_conformance.py | constant list and main command sequence | `APPROVAL_ARTIFACT_AUTHORITY_GATE` | conformance script | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| R72F target artifact paths | `Test-Path` returned False for all four planned R72F artifact paths before authoring. | PASS |
| R72F collision search | `rg -n "MSEA_R72F_FIRST_RETIREMENT_OR_CONSOLIDATION_PILOT" docs CVF_SESSION governance scripts` before authoring found no existing governed R72F packet. | PASS |
| Collision decision | Use the planned R72F paths because no existing R72F packet owns this batch ID. | PASS |

## Acceptance Criteria

| ID | Criterion | Required disposition |
| --- | --- | --- |
| AC1 | Select one non-`PROTECTED` candidate row or child row from R72B/GCI evidence. | PASS |
| AC2 | Prove whether retirement or consolidation criteria are satisfied using current source search, not R72B memory alone. | PASS |
| AC3 | If no candidate passes, name the `WATCH` row or child row and exact missing evidence. | PASS |
| AC4 | Do not delete, disable, rename, consolidate, or edit any checker/hook/source/test/runtime file. | PASS |
| AC5 | Preserve public/private boundary, source verification, no-commit plus reviewer separation, and closure evidence. | PASS |

## Verification / Evidence

| Evidence item | Command or source | Required result |
| --- | --- | --- |
| R72E worker readiness | `python governance/compat/run_worker_return_fast_gate.py` | PASS |
| R72F dispatch quality | `python governance/compat/check_work_order_dispatch_quality.py --base 4050b0a37 --head HEAD --enforce` | PASS |
| R72F worker return | `python governance/compat/run_worker_return_fast_gate.py` | PASS |
| R72F autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 4050b0a37 --head HEAD` | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch baseline; it does not mutate public-sync or publish public artifacts.

## Claim Boundary

This baseline authorizes a no-commit docs-only decision pilot for R72F. It does not authorize actual checker retirement, deletion, disablement, consolidation, hook edit, Fast Lane standard edit, runtime/source/test edit, public-sync mutation, provider/live proof, merge, push, or public/production claim.
