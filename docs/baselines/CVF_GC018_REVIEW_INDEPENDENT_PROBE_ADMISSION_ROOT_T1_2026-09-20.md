# CVF GC-018 Baseline - Independent Probe Admission Integrated Root Contract

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: REVIEW-INDEPENDENT-PROBE-ADMISSION-ROOT-T1

Dispatch base head: 672e41cda

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Local orchestrator/reviewer

Reviewer owner: Local reviewer/closer

Worker target: shared-workspace INTERNAL_AGENT implementation worker

## Purpose

Authorize the integrated root-contract successor required after two corrections
of the same independent-probe admission claim. Replace inconsistent ad hoc
parsing and declaration-only evidence binding with one reusable typed contract.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
| --- | --- | --- | --- |
| RIPA-T1 R2 return | Local disposition records five independent bypasses | reject narrow closure and retain implementation for integrated repair | RELEASED_TO_ROOT_CONTRACT_ONLY |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`protected-governance-path`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_independent_review_probe_admission.py` |
| literalTokensReviewed | dispatch envelope placement; SCEC successor/hash/counters; exact probe contract fields |
| gateRunPurpose | confirm dispatch shape after source-level hostile review |
| claimBoundary | checker shape read-ahead only; semantic acceptance remains Local-owned |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified section | Verified symbol | Disposition |
| --- | --- | --- | --- | --- | --- |
| repeated same-claim correction requires integrated scope | governance contract | `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md` | Enforcement Invariants 5 and 7 | `ROOT_CONTRACT_REQUIRED` | ACCEPT |
| R2 parser accepts five hostile variants | executable observation | `docs/reviews/CVF_REVIEW_INDEPENDENT_PROBE_ADMISSION_T1_R2_LOCAL_DISPOSITION_2026-09-20.md` | Findings / Position | RIPA-ROOT-01..05 | ACCEPT |

## Baseline Decision / Proposed Tranche

Dispatch one integrated root-contract tranche with the exact seven-path worker
manifest in the paired work order. Narrow R3 rework is rejected.

## Evidence / Verification

Required proof is the focused parameterized suite, direct checker result,
worker-return fast gate, Local unseen hostile probes, exact changed-set
reconciliation and reviewer-owned material commit.

## Scope / Owner Boundary

Allowed: the existing seven RIPA implementation paths, one replacement worker
return, and explicit compatibility handling for the three parked artifacts.
Forbidden: editing any other parked artifact, Party A/source creation,
credentials, provider/live execution, runtime release, public-sync and commit.

## Claim Boundary

This baseline authorizes a repository-local structural governance contract and
tests only. It creates no operational source or universal interception claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance hardening.
