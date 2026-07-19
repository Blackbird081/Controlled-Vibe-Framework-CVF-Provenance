# CVF GC-018 Continuous Projection T0 Three-Root Drift Contract

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: CVF-CONTINUOUS-PROJECTION-T0

Dispatch base head: `0145218a2`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Freeze the current read-only projection mapper, its policy and proof seams, and
the Web UX closure dependency before a worker defines the continuous
three-root drift contract. This baseline releases a documentation audit only.

## Decision / Baseline / Proposed Tranche

Decision: release T0 after the Web UX roadmap reached bounded closure at
`d757fe5ac`. Baseline: the accepted projection mapper remains read-only and
fail-closed. Proposed tranche: a terminal three-root contract ledger and a
worker return; T1 implementation remains held.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-CONTINUOUS-PROJECTION-T0 --title "Continuous Projection Three-Root Drift Contract Baseline" --date 2026-07-20 --base 0145218a2 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source verification, dependency release, exact output scope, closure ownership, and mutation boundary |
| checkerReadAheadConfirmation | dispatch-quality, handoff, worker-return, machine-closure, and public-disposition checkers |
| docOnlyNewFields | T0 contract fields and future receipt fields are documentation proposals only |
| claimBoundary | scaffold provenance does not prove runtime or execution behavior |

## Scope / Target / Owner Boundary

The worker may create only the paired T0 ledger and worker return. Provenance,
the sibling public-sync clone, cvf-web, scripts, policy, tests, registries,
session files, and roadmap remain read-only.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| CVF Web UX remediation | `docs/reviews/CVF_WEB_UX_T4_COMPLETION_2026-07-20.md`; commit `d757fe5ac` | reviewer-accepted localhost current-source acceptance | PASS |
| projection mapper foundation | `docs/reviews/CVF_PROJECTION_AUTOMATION_T2_FINAL_CLOSURE_AUDIT_2026-07-18.md`; foundation commit `5df0c6f77` | accepted read-only three-root proof exists | PASS |
| current session release | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | next move authorizes T0 packet authoring only | PASS |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| mapper accepts three explicit roots | EXISTS | `scripts/get_cvf_projection_map.ps1` | parameter block, lines 65-79 | `ProvenanceRoot` | mapper parameter contract | ACCEPT |
| candidate actions are classifications only | LITERAL_INVARIANT | `scripts/get_cvf_projection_map.ps1` | description, lines 21-28 | `FLAG_SEMANTIC_REVIEW_CHANGED` | mapper action vocabulary | ACCEPT |
| policy parity inspection owner exists | EXISTS | `scripts/get_cvf_projection_map.ps1` | function, lines 249-328 | `Get-PolicyParityReport` | mapper policy parity read model | ACCEPT |
| cvf-web observation owner exists | EXISTS | `scripts/get_cvf_projection_map.ps1` | function, lines 330-376 | `Get-CvfWebObservation` | mapper Web observation read model | ACCEPT |
| missing, wrong-remote, and dirty root states fail closed | RUNTIME_BEHAVIOR | `scripts/get_cvf_projection_map.ps1` | main validation, lines 388-425 | `WRONG_PROVENANCE_REMOTE` | mapper validation path | ACCEPT |
| automatic semantic approval is forbidden | VALUE_SET | `scripts/cvf_projection_policy.json` | semanticReviewBoundary, lines 138-141 | `autoApproveForbidden` | projection policy schema | ACCEPT |
| deterministic and negative proof seams exist | EXISTS | `scripts/test_get_cvf_projection_map.ps1` | wrong-public, dirty-public, and repeated-run assertions, lines 300, 318, 440-441 | `deterministic_repeated_run_receipt_id` | focused mapper proof suite | ACCEPT |

## Evidence / Verification

Worker evidence must include direct source locations, current root/remote/status
observations, terminal row totals, secret-free hashes where stable, exact diff,
staged state, unchanged HEAD, worker-fast, and file-size results.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`continuous projection three-root baseline audit`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "continuous projection three-root baseline audit" --role dispatcher --lifecycle-phase pre-dispatch --json`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | Status; Dependency Release Evidence; Source Verification Block; ADIF Defect Registry Disclosure; Public Export Disposition; Claim Boundary |
| gateRunPurpose | validate T0 baseline dispatch shape and evidence |
| claimBoundary | checker compliance confirms packet structure only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance audit baseline; T0 authorizes no export.

## Claim Boundary

This baseline releases documentation-only source inspection. It does not
authorize implementation, semantic edits, apply, commit, push, deployment,
public-sync mutation, provider/live use, production action, or unattended work.
