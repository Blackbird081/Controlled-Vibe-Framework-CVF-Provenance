# CVF GC-018 Baseline - ACEL G6 T1 Impact-Derived Verification Experiment

Memory class: governed-experiment-baseline

Status: READY_TO_EXECUTE_LOCAL

docType: baseline

Date: 2026-09-16

Batch ID: ACEL-G6-T1-IMPACT-DERIVED-VERIFICATION-EXPERIMENT

Execution base head: `ecfb6c2032ad2ade6ff330400c36c15073c82b6b`

Commit mode: LOCAL_REVIEWER_OWNS_MATERIAL_COMMIT

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize one hermetic G6 experiment comparing the current fixed verification
bundle with an impact-derived verification plan on identical synthetic change
cases, acceptance criteria, seeded regressions, and authority. Measure defect
detection, missed regressions, selected-verifier cost, and deterministic
latency units. Do not wire the experiment into autorun, hooks, CI, or runtime.

## Decision / Baseline / Proposed Tranche

Decision: select G6 as the next non-provider Local value cluster after G2 T2B
closed without a release candidate. Baseline A uses one fixed verifier bundle
for every case. Treatment B derives a verifier subset from normalized changed
paths and declared impact classes, with conservative fail-closed fallback.

The experiment uses eight cases, two policies, and two repetitions: exactly 32
deterministic records. It proves only experiment-contract behavior and local
comparative evidence, not production-safe verifier selection.

## Source Verification Block

| Claimed item | Source file | Verified section/symbol | Disposition |
|---|---|---|---|
| G6 is Local-accepted `ADAPT` | `docs/reviews/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_COMPLETION_2026-09-15.md` | Findings / Position | ACCEPT |
| smallest G6 experiment compares fixed and impact-derived plans | `docs/audits/CVF_AGENT_CAPABILITY_ENGINEERING_LAB_LOCAL_GAP_AUDIT_T0_2026-09-15.md` | Proposed smallest experiments | ACCEPT |
| current autorun catalog is phase-fixed | `governance/compat/agent_autorun_command_catalog.py` | phase command catalogs | ACCEPT |
| closeability mandatory gate IDs are fixed | `governance/compat/check_gate_to_role_closeability.py` | `REQUIRED_GATE_IDS` | ACCEPT |
| exact revision evidence is already fail-closed | `governance/compat/run_agent_autorun_workflow_gate.py` | receipt context and validity checks | ACCEPT |

## Scope / Target / Owner Boundary

Local owns an isolated Control Plane Foundation experiment module, focused
tests, deterministic runner, receipt, result audit, and completion review.
Production barrels, existing autorun/checker/hook owners, package dependencies,
provider/network surfaces, session runtime, public sync, and deployment are
read-only or forbidden.

## Exact Material Manifest

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/impact.verification.experiment.contract.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/impact.verification.experiment.contract.test.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/scripts/run-acel-g6-t1-impact-verification-experiment.ts`
- `docs/audits/CVF_ACEL_G6_T1_IMPACT_DERIVED_VERIFICATION_EXPERIMENT_32_RUN_RECEIPT_2026-09-16.json`
- `docs/audits/CVF_ACEL_G6_T1_IMPACT_DERIVED_VERIFICATION_EXPERIMENT_RESULT_2026-09-16.md`
- `docs/reviews/CVF_ACEL_G6_T1_IMPACT_DERIVED_VERIFICATION_EXPERIMENT_COMPLETION_2026-09-16.md`
- GC-051 source entry and generated aggregate.

## Experiment Contract

Eight versioned cases cover documentation, TypeScript source/test, governance
checker/test, continuity state, provider-adapter, and public-workflow changes.
Each case declares normalized changed paths, impact classes, seeded regression
classes, and the verifier capabilities required to detect them.

Policy `FIXED_BUNDLE` always selects the same closed verifier bundle. Policy
`IMPACT_DERIVED` must select universal safety checks plus every verifier implied
by path/impact mapping. Unknown or conflicting inputs must select the complete
fixed bundle and record a fail-closed fallback reason.

Every record must preserve the same case authority and acceptance oracle.
Comparative summaries may include only admitted rows with zero missed seeded
regressions. The runner must reject duplicates, omissions, unstable output, or
anything other than 32 unique `(caseId, policy, repetition)` rows.

## Acceptance Criteria

- Exactly 32 unique records: 8 cases x 2 policies x 2 repetitions.
- Both policies detect every seeded regression; missed-regression total is 0.
- Impact-derived selection never omits a required verifier capability.
- Unknown-impact negative fixture falls back to the complete bundle.
- At least one known-impact case selects fewer verifiers and lower deterministic
  cost than the fixed bundle without reducing detection.
- Two runner executions are byte-identical.
- Focused tests and TypeScript pass.
- No production export, autorun/hook/checker mutation, provider, network,
  subagent, runtime, public, or deployment effect occurs.

## Evidence / Verification

- Pre-dispatch and pre-implementation autorun gates on the exact base.
- Focused deterministic tests covering both policies and fail-closed fallback.
- TypeScript `--noEmit` for the owning package.
- Exactly 32 unique receipt rows and two byte-identical runner outputs.
- Independent Local recomputation of aggregate detection and cost metrics.
- Reviewer-fast, pre-commit, split-range pre-closure, and clean final status.

## Stop Conditions

Stop blocked if the fixed catalog cannot be represented without changing its
owner, path-to-impact mapping is ambiguous for the closed fixture set, any
seeded regression is missed, the receipt is nondeterministic, or implementation
would require production wiring or external execution.

## Negative Search And Collision Discipline

Before implementation, exact target paths must be absent and searches for
`ACEL-G6-T1-IMPACT-DERIVED-VERIFICATION-EXPERIMENT` and
`impact.verification.experiment` must show no competing owner. Existing G6
audit prose is source authority, not a collision.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`pure local implementation`, role=`dispatcher`,
lifecyclePhase=`pre-dispatch`.

Returned defects: NONE_RETURNED (`totalCandidates=0`).

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_changed_corpus_registry_coverage.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_active_session_state.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | status, exact manifest, stop conditions, claim boundary, provider prohibition, `DEFERRED_PRIVATE_ONLY` |
| gateRunPurpose | confirm a bounded hermetic experiment before implementation |
| claimBoundary | experiment evidence only; no production verifier-selection claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local reviewer/orchestrator |
| Provider or surface | private CVF workspace only |
| Session or invocation | ACEL-G6-T1 baseline selection, 2026-09-16 |
| Working directory | repository root |
| Command or tool surface | continuity reads, source inspection, `rg`, apply_patch, pre-dispatch gates |
| Target paths | this baseline, followed only by the exact material manifest |
| Allowed scope source | operator continuation after T2B closure plus accepted ACEL T0 G6 experiment proposal |
| Before status evidence | clean HEAD `ecfb6c2032ad2ade6ff330400c36c15073c82b6b` |
| After status evidence | this single baseline pending pre-dispatch verification |
| Diff evidence | `git status --short`; `git diff --check` |
| Approval boundary | bounded non-provider Local experiment |
| Claim boundary | no production wiring, runtime, provider/live, public, or deploy claim |
| Agent type | INTERNAL_AGENT Local multi-role |
| Invocation ID | `acel-g6-t1-baseline-20260916` |
| Expected manifest | this baseline only before experiment implementation |
| Actual changed set | this baseline only |
| Manifest delta | MATCH |

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

Reason: private proposal-only experiment with no public artifact authority.

## Claim Boundary

This baseline authorizes only an isolated deterministic comparison. A passing
result cannot alter production verification selection, reduce mandatory gates,
or claim real defect-detection superiority without a separately reviewed
integration tranche.
