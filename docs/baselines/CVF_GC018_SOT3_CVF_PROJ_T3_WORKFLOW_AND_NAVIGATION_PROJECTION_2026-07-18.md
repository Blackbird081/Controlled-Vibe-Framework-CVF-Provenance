# CVF GC-018 Baseline - SOT3 CVF Workflow And Navigation Projection

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: SOT3-CVF-PROJ-T3

Dispatch base head: `dd93a913c`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: CVF operator through standing roadmap-continuation instruction

Reviewer owner: independent reviewer/closer

Worker target: delegated documentation worker

## Purpose

Close the accepted T0 row-8 operational lookup gap by adding one bounded SOT3
routing row, while preserving the accepted row-10 no-change disposition for
the forward-only reference artifact index.

## Proposed Tranche / Decision

Authorize one documentation-only edit to the operational reference index and
one full worker return. Do not create a new workflow authority: route readers
to the SOT3 front door and the already-accepted T2 architecture projections.

## Scope / Target / Owner Boundary

Allowed worker paths are
`docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` and
`docs/reviews/CVF_SOT3_CVF_PROJ_T3_WORKER_RETURN_2026-07-18.md`.
`docs/reference/CVF_REFERENCE_ARTIFACT_INDEX.md` is read-only and must receive
a terminal `NO_CHANGE_WITH_REASON` decision. All other paths are forbidden.

## Dependency Release Evidence

| Dependency | Accepted artifact | Material commit | Disposition |
|---|---|---|---|
| T2 independent acceptance | `docs/reviews/CVF_SOT3_CVF_PROJ_T2_COMPLETION_REVIEW_2026-07-18.md` | `d510274b2` | PASS |
| roadmap release state | `docs/roadmaps/CVF_SOT3_CVF_AUTHORITY_SURFACE_AND_MASTER_ARCHITECTURE_PROJECTION_ROADMAP_2026-07-18.md` | `d510274b2` | PASS |
| clean session-sync base | protected continuity commit | `dd93a913c` | PASS |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| operational index owns mandatory scoping lookup rows | EXISTS | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | Lookup Table, line 36 | `Lookup Table` | operational routing reference | ACCEPT |
| new operational front doors require same-commit index update | LITERAL_INVARIANT | `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md` | Maintenance Rule, line 64 | `Maintenance Rule` | operational routing reference | ACCEPT |
| SOT3 canonical entry point exists | EXISTS | `docs/reference/sot_three_layer/README.md` | Purpose and Authority Surface Map | `docs/reference/sot_three_layer/` | SOT3 reference family | ACCEPT |
| bounded cross-plane architecture overlay exists | EXISTS | `docs/reference/CVF_ARCHITECTURE_MAP.md` | SOT3 Bounded Cross-Plane Overlay, line 60 | `SOT3 Bounded Cross-Plane Overlay` | architecture navigation map | ACCEPT |
| reference artifact index is explicitly non-exhaustive | LITERAL_INVARIANT | `docs/reference/CVF_REFERENCE_ARTIFACT_INDEX.md` | Claim boundary and Purpose | `Reference Artifact Index` | IDX-2 forward-only index | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime boundary |
|---|---|---|
| SOT3 operational lookup row | route operator/agent scoping to accepted authority and lifecycle surfaces | documentation only |

## Verification / Evidence

Worker must show the exact two-path changed set, one SOT3 lookup row, the
read-only index no-change decision, worker-fast PASS, file-size PASS, no staged
files, and unchanged HEAD.

## Acceptance Criteria

- One SOT3 row identifies required first reads, current owner surfaces, and a
  bounded lifecycle boundary.
- The row distinguishes contract, runtime owners, activation/proof, and
  downstream application evidence without claiming universal activation.
- The forward-only artifact index remains unchanged with accepted reason.
- No runtime, provider/live, Web, public, production, push, or session action.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture-design`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class architecture-design --role dispatcher --lifecycle-phase pre-dispatch --surface-selector sot-three-layer --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Returned defect count | 0 |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | standing guards remain binding |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | Status; Scope / Target / Owner Boundary; Dependency Release Evidence; Source Verification Block; ADIF Defect Registry Disclosure; Machine Closure Package; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation after direct source and checker read-ahead |
| claimBoundary | structural dispatch evidence only; semantic acceptance remains reviewer-owned |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id SOT3-CVF-PROJ-T3 --title "SOT3 CVF Workflow And Navigation Projection" --date 2026-07-18 --base dd93a913c --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | exact source, dependency, scope, evidence, and boundary tables added |
| checkerReadAheadConfirmation | checker paths listed above |
| docOnlyNewFields | SOT3 operational lookup row only |
| claimBoundary | dispatch-authoring provenance only |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this baseline | `Status: DISPATCH_READY` | PASS |
| Work order status | paired T3 work order | `Status: DISPATCH_READY` | PASS |
| Completion or reviewer artifact | T3 completion review | reviewer-owned | N/A with reason |
| Worker return | T3 worker return | worker-owned uncommitted | N/A with reason |
| Roadmap state | SOT3-CVF projection roadmap | `Status: SOT3_CVF_PROJ_T3_DISPATCH_READY` | PASS |
| Registry JSON | existing GC-051 coverage | reviewer verifies changed-corpus coverage | N/A with reason |
| Registry Markdown | existing registry front door | no new corpus family | N/A with reason |
| External evidence digest | repository-local evidence only | none | N/A with reason |
| System loop interlock | no loop owner changed | none | N/A with reason |
| Session continuity | protected surfaces | separate sync | N/A with reason |

## Current Runtime Freshness Verification

Current SOT3 owner and architecture references were directly reread. This
packet changes routing documentation only and makes no new runtime assertion.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private-provenance navigation dispatch only.

## Claim Boundary

Exactly one operational-index edit plus one worker return. No runtime, test,
provider/live, Web, public, production, push, or session authority.
