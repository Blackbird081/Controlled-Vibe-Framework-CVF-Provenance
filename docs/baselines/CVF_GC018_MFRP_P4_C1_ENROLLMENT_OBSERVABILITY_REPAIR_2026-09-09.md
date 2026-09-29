# CVF GC-018 Baseline - MFRP P4-C1 Enrollment And Observability Repair

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Date: 2026-09-09

Batch ID: MFRP_P4_C1_ENROLLMENT_OBSERVABILITY_REPAIR

Dispatch base head: `bd85cc281de6d2a1d5e9d710060d9839f3d3ba4c`

Commit mode: WORKER_MAY_COMMIT

Decision owner: operator

Reviewer owner: Internal Agent evidence reviewer

Worker target: Internal Agent bounded implementation role

providerExecutionAuthority: FORBIDDEN

successorTrancheOpened: NO

## Purpose

Repair the active P4-C1 measurement path so deterministic reviewer-owned
evidence can enroll without manual positive self-selection and every
post-commit attempt remains observable, including skips and historical
starvation. Preserve the existing P2/P4 owners and trusted-route authority.

## Decision / Baseline

The operator explicitly authorized sequential complete remediation on
2026-09-09, beginning with P4-C1 before WP-ARCH-003 status synchronization or
public/external packet work. This baseline opens only that first bounded lane.

## Scope / Target / Owner Boundary

The existing `mfrp_shadow_canary_autocollect.py` remains the sole post-commit
collection owner. One pure helper may own enrollment selection, attempt-ledger
normalization, counter derivation, and measurement-health projection. P2
receipt validation and P4 comparison/append behavior remain read-only owners.

The ignored v2 journal must distinguish:

- `attemptCount`: unique disclosure commits observed;
- `candidateCount`: source-proven reviewer candidates discovered;
- `eligibleCount`: unique attempts with one deterministically selected
  reviewer-owned candidate;
- `collectedCount`: validated non-ineligible P4 rows actually appended.

Only `collectedCount` drives M5/M10/M20. Historical diagnostic rows never
become collected samples.

## Source / Predecessor Evidence

| Source | SHA-256 or commit | Disposition |
| --- | --- | --- |
| active P4-C1 baseline | `a66ae2739e8fc71d3024e1fbb7c4cbd0aa2e5cdaf843b27012bedf4ee2ab9359` | ACCEPT |
| active P4-C1 work order | `b07f18326522511208ddcaf2955e134da221cd8da7268308d8ee05aa2da7686d` | ACCEPT |
| collector source | `d8cc996345175985e66254d252f5586fafbfcf4ca796194bf5612a753c5886b4` | ACCEPT |
| collector tests | `0cf4fa7700a8d5a31932399ba16f5961d28be408e4ba18ec39ba06fdebf317dd` | ACCEPT |
| activation commit | `b9bdba71290a9d94a12438b413401ecb4c6a72a7` | ACCEPT |
| audit sequence record | `docs/reference/CVF_2026_09_09_AUDIT_AND_REMEDIATION_SEQUENCE.md` | ACCEPT_CURRENT_BATCH |

## Acceptance Boundary

Acceptance requires deterministic priority selection, immutable-blob-only
fallback metadata, idempotent attempt identity, v1 journal migration, v2
all-attempt visibility, historical opportunity backfill, a non-blocking
five-attempt starvation state, unchanged safety-marker semantics, future
scaffold default `AUTO`, legacy valid `YES` readability, and zero fabricated
historical samples.

Multiple same-priority candidates must fail closed. Worker-owned readiness
status can never become a trusted outcome. No new receipt family, tracked
runtime state, daemon, watcher, provider/network call, public sync, or P5/P6
activation is authorized.

## Verification / Evidence

Focused helper, collector, and scaffold tests must prove selection priority,
ambiguity rejection, v1 migration, all-attempt journaling, history diagnostics,
starvation health, duplicate idempotency, and unchanged safety blocking. The
material range must also pass the worker-return fast gate, Python size guard,
ASCII scan, diff hygiene, and committed-range autorun gate.

## Required Artifact Manifest

| Path | Action |
| --- | --- |
| `governance/compat/mfrp_p4_enrollment_observability.py` | CREATE |
| `governance/compat/test_mfrp_p4_enrollment_observability.py` | CREATE |
| `governance/compat/mfrp_shadow_canary_autocollect.py` | MODIFY |
| `governance/compat/test_mfrp_shadow_canary_autocollect.py` | MODIFY |
| `governance/compat/build_worker_return_skeleton_scaffold.py` | MODIFY |
| `governance/compat/run_worker_return_scaffold.py` | MODIFY |
| `governance/compat/test_run_worker_return_scaffold.py` | MODIFY |
| `docs/reference/CVF_2026_09_09_AUDIT_AND_REMEDIATION_SEQUENCE.md` | MODIFY |
| `docs/reviews/CVF_MFRP_P4_C1_ENROLLMENT_OBSERVABILITY_REPAIR_WORKER_RETURN_2026-09-09.md` | CREATE |
| `docs/reviews/CVF_MFRP_P4_C1_ENROLLMENT_OBSERVABILITY_REPAIR_COMPLETION_2026-09-09.md` | CREATE |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: the existing ignored P4-C1 post-commit
collector, one bounded helper, its two scaffold producers, and focused tests.

Protected paths:

- `governance/compat/mfrp_p4_enrollment_observability.py`
- `governance/compat/mfrp_shadow_canary_autocollect.py`
- `governance/compat/build_worker_return_skeleton_scaffold.py`
- `governance/compat/run_worker_return_scaffold.py`

Operator authorization: explicit 2026-09-09 sequential remediation direction.

Rollback boundary: revert only this ten-path material batch if rejected; do
not revert the accepted P4-C1 predecessor, hook installation, P2/P4 owners,
committed evidence, or unrelated closures.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP_P4_C1_ENROLLMENT_OBSERVABILITY_REPAIR --title "MFRP P4-C1 Enrollment And Observability Repair" --date 2026-09-09 --base bd85cc281de6d2a1d5e9d710060d9839f3d3ba4c --commit-mode WORKER_MAY_COMMIT --stdout` |
| generatedProfile | protected-governance-path plus WORKER_MAY_COMMIT profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with audited root cause, exact source hashes, manifest, counters and forbidden boundaries |
| checkerReadAheadConfirmation | dispatch, core self-protection, lifecycle, handoff, active-state and task-governance checker sources were inspected through the scaffold/gate failure evidence |
| docOnlyNewFields | attemptCount; candidateCount; eligibleCount; collectedCount; measurementHealth |
| claimBoundary | dispatch provenance only; no implementation or runtime-effect proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`protected governance path implementation`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "protected governance path implementation" --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | N/A with reason: resolver returned zero items |
| Dispatch impact | no defect-specific constraint beyond the source-proven starvation repair |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_active_session_state.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | dispatch status; prompt position; protected paths; exact manifest; task path families; active handoff; claim-boundary fields |
| gateRunPurpose | confirm the new successor packet after the first rejected historical-packet amendment exposed lifecycle and prompt-position conflicts |
| claimBoundary | checker shape only; no semantic implementation acceptance |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| manual-only positive enrollment | `governance/compat/mfrp_shadow_canary_autocollect.py` | candidate discovery | `ParsedObservation.is_eligible`; `find_eligible_candidate` | P4-C1 collector | ACCEPT |
| default negative scaffold | `governance/compat/build_worker_return_skeleton_scaffold.py` | observation block renderer | `FIELD_ELIGIBILITY` | worker-return scaffold | ACCEPT |
| skip precedes journal write | `governance/compat/mfrp_shadow_canary_autocollect.py` | top-level entrypoint | `run_collection`; `_atomic_write_json` | P4-C1 collector | ACCEPT |
| checkpoints currently use eligible rows | `governance/compat/mfrp_shadow_canary_core.py` | append seam | `append_observation`; `checkpoint_for_population` | P4 core | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| successor packet path collision | exact new baseline/work-order paths did not exist before authoring | CREATE_NEW_SUCCESSOR |
| implementation helper collision | no existing `mfrp_p4_enrollment_observability.py` path | CREATE_BOUNDED_HELPER |
| owner collision | existing collector remains sole post-commit owner; helper has no CLI/hook entrypoint | NO_PARALLEL_RUNTIME_OWNER |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | deterministic enrollment and ignored measurement-journal behavior inside the existing post-commit collector |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: existing P2 receipt remains required before sample collection |
| actionEvidence | ACTION_EVIDENCE_PRESENT: focused unit/integration tests and post-commit-compatible history diagnostic |
| invocationBoundary | existing local post-commit launcher only |
| interceptionBoundary | no new hook, wrapper, IDE, shell, filesystem, provider, or network interception |
| claimLanguage | this repair observes committed Git evidence and writes only ignored P4 runtime diagnostics |
| forbiddenExpansion | no P2/P4 owner replacement, tracked runtime, P5/P6 activation, public sync, provider/live action, or production claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private measurement repair dispatch; public projection is ordered only
after private acceptance and WP-ARCH-003 status synchronization.

## Claim Boundary

This baseline authorizes only the exact P4-C1 repair manifest. It does not
prove the repair, accept a sample, unpark WP-ARCH-003, publish public content,
refresh the external packet, or authorize any external effect.
