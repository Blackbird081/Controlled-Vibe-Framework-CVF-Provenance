# CVF GC-018 Baseline - MFRP P3-R1B Actual-Seam Replay Runner

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Date: 2026-09-02

Batch ID: MFRP-P3-R1B

Dispatch base head: `bfea86038a888e3b7715dff9df33bb4c0c5c971a`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Operator

Reviewer owner: independent reviewer appointed by Operator

Worker target: delegated implementation worker; provider and role label are non-authoritative

## Purpose

Authorize a bounded R1B implementation packet that replays the committed R1A
oracle through the real P2 receipt validator and readout seam. The machine
output is evidence for later independent review, not semantic truth, review
authority, or permission to open P4.

## Root Problem

R1A ratified a static normative oracle. R1B must now prove, case by case, what
the current P2 seam actually observes without copying the seam into a local
evaluator or converting agreement into a correctness claim. The control plane
governs source identity, coverage, observable invariants, evidence shape and
terminal candidates; it does not prescribe the worker's internal reasoning or
general coding workflow.

## Accepted Authority

| Authority | Frozen identity / disposition |
| --- | --- |
| R1 actual-seam redesign | `docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md`; SHA-256 `22a086d7742dbdaec5b887fd377890962ad34396953f48287ce865f743766011` |
| Ratified R1A oracle | `governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json`; containing commit `7f607d353bdec11e456731793f181e72abddc297`; file SHA-256 `6aa32c3157092c974441c269d17e85aed20d5ba535479523eda5b64d23b3fbf2` |
| Oracle canonical identities | all-field JCS SHA-256 `8d64ed3414959ca281cc47daf7067047d79776819b44df16c81dff7a6cbfa80c`; required-set digest `04be6dc1fa061e13af195c5490769bf88fba3309e2ddb4aa0ed24a8fd6440fca`, computed as SHA-256 of UTF-8 RFC 8785 JCS bytes for exactly one three-key object containing `requiredCaseIds`, `requiredFamilies`, and `requiredZeroToleranceClasses`, with each value copied unchanged from the oracle |
| P2 receipt owner | `governance/compat/agent_autorun_machine_verification.py`; SHA-256 `8280a95e0985bd1273aa359afff455be1d18346e8b49cb92e9746922d835d022` |
| P2 readout owner | `governance/compat/agent_automation_machine_verification_readout.py`; SHA-256 `ff6088bf8144deec4582ce9faf62384b314346c9cbbb87f6b3349a2d23f7e7c3` |
| Accepted P4 canary design | `docs/assessments/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_2026-09-02.md`; SHA-256 `65698a95dc7bb7f437fe061a81559701b91a3e611c445f5122ad8145c5f13df5`; R1B same-payload proof is receipt-local only |
| Independent canary design acceptance | `docs/reviews/CVF_MFRP_P4_SHADOW_CANARY_AND_GOVERNANCE_TAX_BUDGET_DESIGN_REVISION_1_INDEPENDENT_REREVIEW_2026-09-02.md`; SHA-256 `ae7c68c09ad4e7cfc688275dc896ec455f5c25a8771fa552fadac793717e4d7d` |

## Decision / Baseline

R1B is one exact-manifest, no-commit implementation tranche. Its output may
declare only one worker terminal candidate:

- `REPLAY_EVIDENCE_COMPLETE_PASS_CANDIDATE`;
- `REPLAY_EVIDENCE_COMPLETE_RETURN_TO_DESIGN_CANDIDATE`; or
- `BLOCKED_EVIDENCE_INCOMPLETE`.

Only an independent reviewer may select `REPLAY_PASS` or `RETURN_TO_DESIGN`.
No machine result changes route authority, reviewer jurisdiction, P2 behavior,
or the status of the accepted canary design.

## Exact R1B Artifact Manifest

| Path | Ownership | Required action |
| --- | --- | --- |
| `governance/compat/mfrp_actual_seam_replay.py` | worker | create runner |
| `governance/compat/test_mfrp_actual_seam_replay.py` | worker | create focused hostile tests |
| `governance/compat/fixtures/mfrp_p3_r1b_actual_seam_replay_result.json` | worker | create deterministic post-run ledger |
| `docs/reviews/CVF_MFRP_P3_R1B_ACTUAL_SEAM_REPLAY_WORKER_RETURN_2026-09-02.md` | worker | create full-gate return |

No rename, deletion, staging, commit, sixth path, cache artifact, provider call,
network call, live proof, credential use, or runtime receipt write is allowed.

## Actual-Seam Contract

For each admitted representable oracle case, one causal call chain must:

1. construct a valid deterministic P2 v3 receipt using the canonical P2
   object and digest owners;
2. prove the unmutated control passes `_validate_receipt_integrity`;
3. apply the oracle's typed mutation in memory and prove serialized bytes
   changed when the mutation contract requires a changed payload;
4. invoke the real `_validate_receipt_integrity` on that mutated object;
5. pass that identical in-memory receipt object to
   `build_machine_verification_readout`, then serialize only through
   `machine_readout_to_dict`; and
6. normalize only secret-safe observed fields before evaluating the committed
   predicate.

Both P2 owners must be imported. A copied validator, copied readout builder,
standalone allowlist, normative-label substitution, or locally weakened
evaluator is a hard failure.

The same-payload assertion is deliberately narrow: it proves only that the
validator and readout consumed the identical receipt object within one call
chain. It does not prove that a seven-phase return and an autorun receipt are
the same object, nor that consistency implies correctness.

## Coverage And Result Contract

The runner must freeze and recompute the oracle containing commit, file hash,
all-field JCS hash, required-set digest, and both P2 owner byte hashes before
replay. Coverage must reconcile exactly to 19 unique case IDs, 18 required
families, seven required zero-tolerance classes, and 19 total cases. Every
admitted mutation is consumed and every representable case has exactly one
validator/readout observation. Zero-case execution is a hard failure.

Cases `C07`, `C08`, and `C18` remain
`NOT_REPRESENTABLE_BY_CURRENT_P2`. They remain visible in totals and residual
risk, but can never count as detected, satisfied, passed, or machine-covered.

The result ledger schema is `cvf.mfrp.actualSeamReplayResult.v1`. It must
separate identity/coverage/execution completeness from predicate observations,
limitations, terminal candidate, and reviewer-owned disposition. It may not
contain a reviewer disposition or manufactured observation.

## Required Hostile Proof Families

Focused tests must cover at least: one-case execution cannot pass; missing
family; missing zero-tolerance class; source/locator/excerpt drift; oracle hash
drift; unknown mutation; normative labels cannot manufacture observations;
digest tamper reaches the actual validator; attacker-rebound structural gap;
no real credential or environment secret reaches output; C15's fixed
non-secret test sentinel is honestly recorded as a predicate miss and current
P2 limitation without suppressing the observed copy-through; readout preserves
required observed fields; zero totals hard fail; runner cannot emit reviewer `REPLAY_PASS`; both
P2 owners remain byte-identical; repeated runs are deterministic and write no
receipt/cache/provider artifacts; and a weakened local evaluator is caught.

## Stop Conditions

Stop and return `BLOCKED_EVIDENCE_INCOMPLETE` if any frozen identity differs,
the committed oracle or P2 owner would need modification, an oracle mutation
cannot be represented honestly, the exact manifest would expand, a real
credential or environment secret may be emitted, or evidence cannot reconcile.
C15's fixed non-secret test sentinel is observation evidence, not a real-secret
stop trigger. A newly exposed P2 limitation is
recorded for a later separately authorized hardening tranche; it is not repaired
inside R1B.

## Reviewer Strategy

The reviewer verifies frozen identities, exact coverage reconciliation,
representative hostile-test evidence, the actual imports/call chain, the
receipt-local identical-object proof, deterministic ledger recomputation, and
the absence of forbidden writes. The reviewer does not rebuild the runner or
repeat every worker action; bounded independent recomputation is the control.

## Review Admission Boundary

The completed packet review is corrective evidence, not a reusable mandatory
stage. No second packet review or separate operator micro-checkpoint is required
before dispatch after the listed findings are repaired and machine gates pass.
The next routine reviewer admission point is the R1B worker return. Earlier
review is admitted only for a frozen-identity mismatch, source contradiction,
manifest expansion, secret/irreversible-effect risk, or another new independent
critical authority boundary. Role handoff, artifact authoring, deterministic
gate success, and session sync alone do not admit another review.

## Evidence / Verification

- Focused unit tests for the new runner.
- `python governance/compat/run_worker_return_fast_gate.py`.
- pre-implementation autorun gate against the captured execution base.
- exact `git status --short`, `git diff --name-status`, and unchanged HEAD.

No latency, quota, correctness, safety improvement, P4 readiness, provider,
live, public, deployment, or production claim follows from these checks.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| R1B is the executable actual-seam tranche | normative | `docs/assessments/CVF_MFRP_P3_R1_ACTUAL_SEAM_REPLAY_AND_COMMITTED_ORACLE_REDESIGN_2026-09-01.md` | MFRP-P3-R1B; Actual P2 Seam Contract; Result Ledger | R1B | `cvf.mfrp.actualSeamReplayResult.v1` | ACCEPT |
| receipt validation owner | source | `governance/compat/agent_autorun_machine_verification.py` | lines 17-19, 131 onward | `_validate_receipt_integrity` | `cvf.autorun.pass-receipt.v3` | ACCEPT |
| readout owner | source | `governance/compat/agent_automation_machine_verification_readout.py` | lines 63, 125 | `build_machine_verification_readout`; `machine_readout_to_dict` | P2 readout seam | ACCEPT |
| three current-P2 blind spots | committed oracle | `governance/compat/fixtures/mfrp_p3_r1a_r1_static_only_oracle.json` | cases C07, C08, C18 | `feasibilityDisposition` | R1A oracle | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| exact paired authoring paths | `Test-Path` returned false for both before authoring | CREATE_NEW |
| existing R1B authority token | `rg -n "MFRP P3-R1B|MFRP-P3-R1B|ACTUAL_SEAM_REPLAY_RUNNER" docs CVF_SESSION` found only the roadmap and R1 redesign | NO_COLLISION |
| worker output paths | all four exact manifest paths were absent before authoring | CREATE_NEW_ONLY |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`actual-seam replay runner`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "actual-seam replay runner" --role dispatcher --lifecycle-phase dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no matching ADIF item changed this bounded packet |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py` and split modules; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | headings Source Verification Block, Negative Search And Collision Discipline, Core Guard Self-Protection Authorization, Claim Boundary, Public Export Disposition; fields docType, executionBaseHead, changedSetScope(phase), manifest delta; enums WORKER_MUST_NOT_COMMIT, DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | Confirmed checker-facing shape and literal vocabulary before finalizing the paired authoring artifacts; gates are confirmation evidence. |
| claimBoundary | Read-ahead covers this dispatch/baseline shape only; it does not prove future worker behavior or replay correctness. |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id MFRP-P3-R1B --title "Actual-Seam Replay Runner" --date 2026-09-02 --base bfea86038a888e3b7715dff9df33bb4c0c5c971a --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | protected-governance-path plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with R1B identities, exact manifest, actual-seam/coverage contracts, hostile proofs, stop rules, and bounded claim language. |
| checkerReadAheadConfirmation | Checker sources listed in the preceding block were inspected before final authoring. |
| docOnlyNewFields | actual-seam, coverage, result-ledger, and R1B terminal-candidate terms are documentation contracts only until worker execution. |
| claimBoundary | Dispatch authoring provenance only; no runtime/provider/live/public/Web/MCP/model-router behavior claim. |

## Core Guard Self-Protection Authorization

`governance/compat/mfrp_actual_seam_replay.py`,
`governance/compat/test_mfrp_actual_seam_replay.py`, and
`governance/compat/fixtures/mfrp_p3_r1b_actual_seam_replay_result.json` are
explicitly authorized new files. No existing checker, hook, catalog, standard,
P2 owner, oracle, roadmap, or session surface is authorized for modification.

## Claim Boundary

This baseline supports dispatch of the paired R1B work order after its
corrections and machine gates pass. It does not itself execute the worker,
accept replay evidence, emit
`REPLAY_PASS`, open P4, change P2, or claim runtime/provider/live/public/
deployment/production readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R1B is private provenance governance work; no public-sync artifact or
public catalog claim is authorized.
