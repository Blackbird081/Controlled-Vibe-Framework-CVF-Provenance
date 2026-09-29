# CVF GC-018 Baseline - DARA T2 R1 Consolidated Rework Amendment

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-09-07

Batch ID: DARA-T2-R1-CONSOLIDATED-REWORK

Dispatch base head: 491396f361dec5c2127f67384d0b5d706b401026

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator; dispatch author: orchestrator/dispatcher role; reviewer: reviewer/closer role; worker target: delegated implementation worker.

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize one consolidated, no-commit external rework of the held DARA-T2
implementation. The tranche closes the five committed R1 findings under the
accepted root-contract amendment while preserving reviewer non-duplication,
MFRP ownership, and the cumulative two-invocation ceiling.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id DARA-T2-R1-CONSOLIDATED-REWORK --title "DARA T2 R1 Consolidated Architecture Readiness Admission Rework" --date 2026-09-07 --base 491396f361dec5c2127f67384d0b5d706b401026 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --dispatch-kind REWORK --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 1 --root-cause-cluster-id DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION --prior-finding-set-digest 57b8e57cf888f3228fff7c322066373fb250bf71de454e84ddb18722827e665f --cumulative-external-invocation-count 1 --external-invocation-ceiling 2 --new-independent-critical-evidence DARA-T2-R1-01,DARA-T2-R1-02,DARA-T2-R1-03,DARA-T2-R1-04,DARA-T2-R1-05 --stdout` |
| generatedProfile | protected-governance-path plus no-commit external REWORK profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with the accepted amendment, exact thirteen-path final manifest, cleanup invariant, AM-01 through AM-10, and final-invocation stop rule |
| checkerReadAheadConfirmation | dispatch-quality, convergence, review-cost, protected-path, source, worker-return, trace, size, and public guards |
| docOnlyNewFields | cleanup-only path distinction and accepted-contract identity digest explanation |
| claimBoundary | dispatch-authoring provenance only; no implementation or acceptance proof |

## Decision / Baseline / Proposed Tranche

The original DARA-T2 return is rejected at review commit
`6746abf74e7ee691275a7979f78aa1b84b8b2c5a`. The corrected root contract is
frozen at `203e9e6f7bc63873da008284688f7b533f65fbf9` and accepted bounded at
review commit `1316ea7340541ab8e675c5b1965f5a1ff3ef52d0`. One consolidated R1 rework may
therefore use invocation 2 of 2. No further automatic external rework is
authorized.

## Authorized Scope

- Repair R1-01 through R1-04 in the held implementation.
- Satisfy R1-05 by extracting the dispatch renderer and all new DARA tests into
  the three exact new owner paths authorized by the amendment.
- Preserve behavior outside DARA and keep both worker-return generator routes
  aligned.
- Update the existing worker return in place with truthful first/final evidence.
- Produce final evidence for AM-01 through AM-10 and exact final-manifest equality.

## Forbidden Scope

No fourth new path, exception-registry increase, MFRP receipt/readout/collector,
roadmap, ADIF, session, active-handoff, baseline, work-order, accepted review,
WP-ARCH-003, runtime/provider/live, public-sync, deployment, commit, or push
change is authorized. The worker may not create a second return or completion
review.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| committed rejected-return review | `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_COMPLETION_2026-09-06.md`; SHA-256 `57b8e57cf888f3228fff7c322066373fb250bf71de454e84ddb18722827e665f` | one consolidated finding set exists | ACCEPT |
| corrected root contract | `docs/assessments/CVF_DARA_T2_R1_ROOT_CONTRACT_AND_MANIFEST_AMENDMENT_2026-09-07.md`; commit `203e9e6f7bc63873da008284688f7b533f65fbf9`; SHA-256 `8d82ed44b5f5e66576639e54e610f4bd659210561fe6a2b6ac1a4b8b15b221b2` | fail-closed semantics and feasible manifest are frozen | ACCEPT |
| amendment review | `docs/reviews/CVF_DARA_T2_R1_ROOT_CONTRACT_AND_MANIFEST_AMENDMENT_REVIEW_2026-09-07.md`; commit `1316ea7340541ab8e675c5b1965f5a1ff3ef52d0`; SHA-256 `677a7647a810fd78340b217c319dfbb7201da7ee5d3426889c503435b1008984` | one consolidated REWORK packet is released | ACCEPT |
| MFRP P4-C1 | `docs/work_orders/CVF_AGENT_WORK_ORDER_MFRP_P4_C1_AUTOMATIC_EVIDENCE_COLLECTION_2026-09-02.md`; activation `b9bdba712` | remains the sole automatic reviewer-evidence collector | ACCEPT |

## Accepted Architecture Identity Echo

Architecture-Readiness Admission: NOT_APPLICABLE_ACCEPTED_DESIGN_ECHO

architectureMatrixSchema: cvf.dara.architectureBindingMatrix.v1

architectureMatrixCanonicalDigest: 8d82ed44b5f5e66576639e54e610f4bd659210561fe6a2b6ac1a4b8b15b221b2

architectureSemanticReviewPath: docs/reviews/CVF_DARA_T2_R1_ROOT_CONTRACT_AND_MANIFEST_AMENDMENT_REVIEW_2026-09-07.md

architectureSemanticReviewCommit: 1316ea7340541ab8e675c5b1965f5a1ff3ef52d0

architectureSemanticReviewFileSha256: 677a7647a810fd78340b217c319dfbb7201da7ee5d3426889c503435b1008984

architectureBindingEchoDisposition: EXACT_MATCH

For this documentation-only rework transcription, the canonical digest is the
raw SHA-256 of the committed accepted root-contract amendment. It is not a
worker-authored matrix or machine-created semantic acceptance. All six values
must echo unchanged in the paired work order and worker return.

## Exact Final Changed-Set Manifest

1. `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`
2. `docs/reference/CVF_ARCHITECTURE_READINESS_ADMISSION_STANDARD_2026-09-07.md`
3. `governance/compat/build_dispatch_packet_scaffold.py`
4. `governance/compat/build_dispatch_packet_architecture_readiness.py`
5. `governance/compat/build_worker_return_skeleton_scaffold.py`
6. `governance/compat/check_work_order_dispatch_quality.py`
7. `governance/compat/check_work_order_dispatch_quality_range.py`
8. `governance/compat/check_work_order_dispatch_quality_source.py`
9. `governance/compat/run_worker_return_scaffold.py`
10. `governance/compat/test_build_dispatch_packet_scaffold.py`
11. `governance/compat/test_check_work_order_dispatch_quality_architecture_readiness.py`
12. `governance/compat/test_run_worker_return_scaffold.py`
13. `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_WORKER_RETURN_2026-09-06.md`

Cleanup-only authorization:
`governance/compat/test_check_work_order_dispatch_quality.py` may be restored
during rework but must finish byte-identical to the execution-base blob and
must not appear in the final diff.

## Maintainability Outcomes

| Owner | Required final result |
|---|---|
| `governance/compat/build_dispatch_packet_scaffold.py` | at or below 874 physical lines; extracted renderer in the exact new helper; size gate PASS |
| `governance/compat/test_check_work_order_dispatch_quality.py` | byte-identical to execution base; absent final diff |
| `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | compact pointer to same-directory active standard; Markdown size guard PASS |
| exception registries | unchanged |

## Acceptance Matrix

| ID | Required outcome |
|---|---|
| AM-01 | active external packet without an architecture declaration blocks as unclassified |
| AM-02 | accepted echo with genuine committed review identity passes without a second review |
| AM-03 | fake, non-ancestor, stale, wrong-path, wrong-blob-hash, and missing-criterion identities block |
| AM-04 | missing trust source/locator, carrier field, rollback containment, dated output, and authority boundary each block |
| AM-05 | all sixteen original hostile families pass with corrected HT-02 and HT-09 meaning |
| AM-06 | both return scaffold routes emit exact echo parity and block identity drift |
| AM-07 | Python and Markdown size guards report zero violations |
| AM-08 | pre-implementation and automation-assist gates pass with unrelated files isolated |
| AM-09 | no nonzero mandatory command is labeled PASS and terminal status matches all results |
| AM-10 | final diff equals the thirteen paths and excludes the cleanup-only file |

## Evidence Measurement Contract

The updated return must report invocation before=1 and after=2, all R1/AM
dispositions, exact command exit states, line counts, base-blob restoration,
final manifest, defect attribution, elapsed time/usage or exact unavailability,
and any natural P4 observation. No new telemetry surface may be created.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0051, ADIF-0052, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024,
ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006.

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json --max-results 50` |
| Returned defect count | 22 |
| Disclosed defectIds | all IDs listed above |
| Dispatch impact | source-first authoring, feasible split paths, protected authorization, exact final manifest, truthful return evidence, and no-commit boundary |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_python_automation_size.py` |
| literalTokensReviewed | dispatch status, REWORK convergence scalars, exact Source Verification columns, protected-path authorization, size rotation/split outcomes, return profile, trace labels, private export disposition |
| gateRunPurpose | confirm the completed source-verified rework packet before the final external dispatch |
| claimBoundary | gate conformance proves packet shape only, not implementation effectiveness |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| five consolidated findings | committed review evidence | `docs/reviews/CVF_DARA_T2_ARCHITECTURE_READINESS_ADMISSION_IMPLEMENTATION_COMPLETION_2026-09-06.md` | Findings / Position | DARA-T2-R1-01 through DARA-T2-R1-05 | R1 reviewer | ACCEPT |
| corrected contract and manifest | design authority | `docs/assessments/CVF_DARA_T2_R1_ROOT_CONTRACT_AND_MANIFEST_AMENDMENT_2026-09-07.md` | Revised Final Changed-Set Manifest | CVF_ARCHITECTURE_READINESS_ADMISSION_STANDARD_2026-09-07.md | DARA R1 amendment | ACCEPT |
| bounded rework release | review authority | `docs/reviews/CVF_DARA_T2_R1_ROOT_CONTRACT_AND_MANIFEST_AMENDMENT_REVIEW_2026-09-07.md` | Decision / Disposition | DESIGN_ACCEPTED_BOUNDED_FOR_ONE_CONSOLIDATED_REWORK | amendment reviewer | ACCEPT |
| current Python limits | machine policy | `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` | exceptions | governance/compat/test_check_work_order_dispatch_quality.py | Python size registry | ACCEPT |
| current Markdown rotation | machine policy | `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` | proactiveOwnerSurfaces | docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md | governed file-size registry | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| baseline and work-order paths | exact `Test-Path -LiteralPath` returned false before authoring | ACCEPT_NO_COLLISION |
| batch token | `rg -n --hidden --no-ignore` across `docs` and `CVF_SESSION` returned no prior packet | ACCEPT_NO_COLLISION |
| worker return | existing rejected-return artifact must be modified in place | REUSE_EXACT_PATH |
| extra output or evidence store | forbidden; P4-C1 remains sole collector | REJECT_PARALLEL_OWNER |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: repair DARA-T2 only on the protected code
paths in the exact final manifest plus the named cleanup-only path.

Protected paths:

- `governance/compat/build_dispatch_packet_scaffold.py`
- `governance/compat/build_dispatch_packet_architecture_readiness.py`
- `governance/compat/test_build_dispatch_packet_scaffold.py`
- `governance/compat/build_worker_return_skeleton_scaffold.py`
- `governance/compat/run_worker_return_scaffold.py`
- `governance/compat/test_run_worker_return_scaffold.py`
- `governance/compat/check_work_order_dispatch_quality.py`
- `governance/compat/check_work_order_dispatch_quality_range.py`
- `governance/compat/check_work_order_dispatch_quality_source.py`
- `governance/compat/test_check_work_order_dispatch_quality_architecture_readiness.py`
- `governance/compat/test_check_work_order_dispatch_quality.py` (cleanup only; absent final diff)

Operator authorization: on 2026-09-07 the operator authorized the sequential
orchestrator/reviewer route and delegated agent-to-agent exchange without
operator intervention.

Rollback boundary: revert only the eventual accepted DARA-T2 rework material;
preserve committed design/reviews, MFRP P4-C1, continuity, and parked WP files.

Not authorized: exception bump, extra path, MFRP/session/roadmap/ADIF change,
provider/live/public action, worker commit, or automatic third invocation.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | orchestrator/dispatch author after bounded sequential design review |
| Provider or surface | local private CVF workspace |
| Session or invocation | DARA-T2 R1 consolidated rework dispatch authoring, 2026-09-07 |
| Working directory | repository root |
| Command or tool surface | committed review reads, size-registry/checker reads, ADIF resolver, scaffold preview, collision checks, apply_patch, pre-dispatch gate |
| Target paths | this baseline and paired work order |
| Allowed scope source | operator authorization for sequential orchestration/review and inter-agent exchange |
| Before status evidence | clean worktree at HEAD `491396f361dec5c2127f67384d0b5d706b401026`; held worker delta remains in named stash; WP files remain hash-preserved outside worktree |
| After status evidence | exactly two dispatch artifacts; no worker implementation restored or executed during authoring |
| Diff evidence | `git diff --name-status`; `git status --short` |
| Approval boundary | one consolidated DARA-T2 rework dispatch only |
| Claim boundary | no implementation, worker acceptance, runtime/provider/live/public effect |
| Agent type | orchestrator/dispatcher; future role reviewer |
| Invocation ID | `dara-t2-r1-consolidated-rework-dispatch-2026-09-07` |
| Expected manifest | this baseline and paired work order |
| Actual changed set | same two paths |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundation rework dispatch; no public-sync authority.

## Claim Boundary

This baseline authorizes only one consolidated no-commit rework of the held
DARA-T2 candidate. It does not accept the implementation, change MFRP, consume
a provider/live call, authorize a third external invocation, resume
`WP-ARCH-003`, open DARA-T3, publish, deploy, or claim production readiness.
