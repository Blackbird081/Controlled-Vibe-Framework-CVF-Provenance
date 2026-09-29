# CVF GC-018 Baseline - MSEA-R72G/R72H Read Chain And Separability

Memory class: governed-dispatch-baseline
Status: DISPATCH_READY
Batch ID: MSEA_R72G_R72H_READ_CHAIN_AND_SEPARABILITY
Dispatch base head: b896cc759
Commit mode: WORKER_MUST_NOT_COMMIT
Decision owner: Operator
Reviewer owner: Codex reviewer/closer
Worker target: Codex combined worker/reviewer role

## Purpose

Dispatch a bounded documentation-and-evidence-only R72G/R72H tranche. R72G measures human/operator read-chain and bus-factor risk. R72H inventories product/governance separability without extracting, repackaging, releasing, or publicly claiming any product surface.

This baseline does not authorize checker edit, hook edit, runtime/source/test edit, public-sync mutation, product extraction, package creation, provider/live proof, merge, push, or public/production claim.

## Decision / Baseline

Decision: `DISPATCH_R72G_R72H_DOCS_ONLY_EVIDENCE`.

Baseline: R72G and R72H are combined because both are read-only governance rebalance evidence tasks derived from the same R72 roadmap coverage gap. Combining them reduces unnecessary commit stacking while preserving source verification and closure evidence.

## Proposed Tranche

| Field | Value |
| --- | --- |
| trancheId | MSEA-R72G/R72H |
| trancheName | Human/operator read-chain and product/governance separability evidence |
| workerMode | WORKER_MUST_NOT_COMMIT |
| outputType | combined reference matrix plus worker return |
| protectedControls | public/private boundary; source verification; no-commit plus reviewer separation; closure evidence |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id MSEA_R72G_R72H_READ_CHAIN_AND_SEPARABILITY --title "MSEA R72G/R72H Read Chain And Separability" --date 2026-07-08 --base b896cc759 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Filled R72G/R72H authority, source verification, allowed scope, forbidden scope, worker output path, and combined no-implementation boundary. |
| checkerReadAheadConfirmation | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_dispatch_scaffold_provenance.py; governance/compat/check_agent_handoff_boundary.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_public_export_disposition.py |
| docOnlyNewFields | readChainTier; operatorMinimumGuidance; separabilityClass; extractionDisposition |
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
| claimBoundary | Read-ahead covers dispatch artifact shape only; R72G/R72H conclusions must be command-backed in the worker output. |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R72 roadmap assigns R72G to human/operator onboarding and bus-factor reduction | EXISTS | docs/roadmaps/CVF_MSEA_R72_EA_ASSESSMENT_INTAKE_AND_GOVERNANCE_LOAD_REBALANCING_ROADMAP_2026-07-07.md | line 244 | `R72G` | R72 roadmap Work Plan | ACCEPT |
| R72 roadmap assigns R72H to product/governance separability assessment | EXISTS | docs/roadmaps/CVF_MSEA_R72_EA_ASSESSMENT_INTAKE_AND_GOVERNANCE_LOAD_REBALANCING_ROADMAP_2026-07-07.md | line 245 | `R72H` | R72 roadmap Work Plan | ACCEPT |
| R72 roadmap trace seed requires R72G read-chain table and tiered guide proposal | EXISTS | docs/roadmaps/CVF_MSEA_R72_EA_ASSESSMENT_INTAKE_AND_GOVERNANCE_LOAD_REBALANCING_ROADMAP_2026-07-07.md | line 280 | `Own human/operator bus-factor risk` | R72 roadmap trace seed | ACCEPT |
| R72 roadmap trace seed requires R72H separability matrix with no-runtime and no-public claim boundary | EXISTS | docs/roadmaps/CVF_MSEA_R72_EA_ASSESSMENT_INTAKE_AND_GOVERNANCE_LOAD_REBALANCING_ROADMAP_2026-07-07.md | line 281 | `Own product/governance separability risk` | R72 roadmap trace seed | ACCEPT |
| GCI records R72F as the first retirement/consolidation pilot and keeps later work evidence-based | EXISTS | docs/reference/governance_control_index/CVF_GOVERNANCE_CONTROL_INDEX.md | line 190 | `R72F` | Governance Control Index | ACCEPT |
| Startup front door requires session memory, bootstrap read model, state registry, active handoff, guard orientation, and literal gotchas before governed work | EXISTS | AGENTS.md | Session Memory Front Door and Guard Orientation sections | startup read chain | AGENTS.md | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| R72G/R72H target artifact paths | `Test-Path` must return False for the planned combined baseline, work order, reference matrix, and worker return before authoring. | PASS |
| R72G/R72H collision search | `rg -n "MSEA_R72G_R72H_READ_CHAIN_AND_SEPARABILITY" docs CVF_SESSION governance scripts` must find no existing governed packet before authoring. | PASS |
| Collision decision | Use combined R72G/R72H paths because no existing packet owns this batch ID. | PASS |

## Acceptance Criteria

| ID | Criterion | Required disposition |
| --- | --- | --- |
| AC1 | Create a source-backed read-chain and bus-factor simplification table for R72G. | PASS |
| AC2 | Create a source-backed product/governance separability matrix for R72H. | PASS |
| AC3 | Preserve protected controls: public/private boundary, source verification, no-commit plus reviewer separation, and closure evidence. | PASS |
| AC4 | Do not edit checker, hook, runtime/source/test, public-sync, product package, or generated session state paths in worker output. | PASS |
| AC5 | Run worker-return fast gate and pre-implementation autorun before reviewer closure. | PASS |

## Verification / Evidence

| Evidence item | Command or source | Required result |
| --- | --- | --- |
| Dispatch base | `git rev-parse --short HEAD` | b896cc759 |
| R72G/R72H source search | `rg -n "R72G|R72H|Own human|Own product" docs/roadmaps/CVF_MSEA_R72_EA_ASSESSMENT_INTAKE_AND_GOVERNANCE_LOAD_REBALANCING_ROADMAP_2026-07-07.md` | roadmap authority found |
| Worker return | `python governance/compat/run_worker_return_fast_gate.py` | PASS |
| Autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base b896cc759 --head HEAD` | PASS |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance dispatch baseline; it does not mutate public-sync or publish public artifacts.

## Claim Boundary

This baseline authorizes only R72G/R72H evidence authoring. It does not authorize implementation, extraction, packaging, checker retirement, checker edit, hook edit, runtime/source/test edit, public-sync mutation, provider/live proof, merge, push, or public/production claim.
