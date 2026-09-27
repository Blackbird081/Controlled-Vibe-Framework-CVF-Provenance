# CVF GC-018 Baseline - NCR-R1/S10 Test Evidence Audit Instruction-Use Proof

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: CVF-NCR-R1-S10

Dispatch base head: `acfe300bb`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local orchestrator/reviewer; operator released exactly one live provider call on 2026-09-28.

Reviewer owner: Local independent reviewer/closer.

Worker target: one shared-workspace `INTERNAL_AGENT` worker after checkpoint release.

## Purpose

Define the bounded P9 instruction-use proof for
`cvf-engineering-test-evidence-audit`: one dry adapter proof followed by at
most one live Alibaba/DashScope provider call, one file-backed
`CVF_ASSF_PACKAGE_USE_PROOF_RECEIPT`, and one worker return. Provider authority
is limited to the exact one-call grant carried by the paired work order.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind package-skill --batch-id CVF-NCR-R1-S10 --title "Test Evidence Audit P9 Instruction-Use Proof" --date 2026-09-28 --base acfe300bb --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | package-skill plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact held P9 scope, source evidence, live checkpoint and claim boundary |
| checkerReadAheadConfirmation | dispatch quality, autorun, target-state feasibility, use-proof adapter and receipt-trace owners read |
| docOnlyNewFields | `liveReleaseCheckpoint`; `providerCallCeiling` |
| claimBoundary | packet authoring only; no package body read or provider call |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| `docs/reviews/CVF_CVF_NCR_R1_S09_R1_ACTIVE_EXTERNAL_ADAPTER_ADMISSION_ROOT_RECONCILIATION_2026-09-28.md` | P8 `CLOSED_PASS_BOUNDED`; material `218093215`; internal `ACTIVATION_READY`; external body/output denied | P9 may be authored without altering lifecycle or external adapter posture | RELEASED_FOR_AUTHORING |
| operator live checkpoint | operator gave an affirmative response on 2026-09-28 after Local stated exact model, one-call ceiling and no-retry boundary | paired packet binds the exact executable provider grant | RELEASED_EXACTLY_ONE_CALL |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| P9 exit requires use-proof receipt and live proof when behavior is claimed | lifecycle contract | `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md` | End-To-End Phase Ladder P9 | `USE_PROOF_PASSED` | package productionization SOP | ACCEPT |
| dry mode cannot prove use | runtime behavior | `governance/compat/run_assf_package_use_proof_adapter.py` | `build_package_use_proof_packet` | `DRY_RUN_READY_FOR_LIVE_PROVIDER_USE_PROOF` | use-proof adapter | ACCEPT |
| live success emits the receipt | runtime behavior | `governance/compat/run_assf_package_use_proof_adapter.py` | `_build_use_proof_receipt` | `LIVE_PROVIDER_USE_PROOF_PASS` | use-proof adapter | ACCEPT |
| current permitted free-quota model is unexpired on 2026-09-28 | value set | `docs/reference/model_gateway/CVF_ALIBABA_FREE_QUOTA_MODEL_LEDGER.json` | `models` | `qwen3.7-flash-2026-07-15`; expiry `2026-10-22` | free-quota ledger | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_package_skill_target_state_feasibility.py`; `governance/compat/check_package_skill_productionization_pipeline.py`; `governance/compat/check_cvf_skill_usage_receipt_trace.py` |
| literalTokensReviewed | held status; P9 phase; dry/live dispositions; receipt and return tokens |
| gateRunPurpose | confirm held packet shape and semantic feasibility |
| claimBoundary | checker read-ahead is not execution evidence |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`package_skill_productionization`, role=`dispatcher`, lifecyclePhase=`dispatch`.

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class package_skill_productionization --role dispatcher --lifecycle-phase dispatch --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no registered defect changes the released exact one-call boundary |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| four planned S10 paths | `Test-Path` returned false before authoring | NO_COLLISION |
| batch/token search | `rg -n "CVF-NCR-R1-S10|NCR_R1_S10_TEST_EVIDENCE_AUDIT_INSTRUCTION_USE_PROOF" docs CVF_SESSION` returned no prior artifact | NO_COLLISION |
| collision decision | new bounded phase packet, not a repair | CREATE_NEW |

## Decision / Baseline

1. P9 requires a real instruction-use result; dry readiness alone is not completion.
2. The live command is capped at one call using the exact ledger-backed model.
3. No rerun follows a failed or ambiguous live call until a secret-safe diagnostic is recorded and Local authorizes it.
4. Lifecycle, truth, package source, external adapter posture and generated projections remain unchanged.
5. Worker scope after release is exactly the use-proof JSON and worker return.

## Evidence / Verification

Authoring evidence is the exact source-verification table, collision search,
target-state feasibility gate, dispatch author fast gate, reviewer-fast gate
and pre-commit result. Execution evidence remains unavailable before the worker and
must not be inferred from packet completeness.

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: P8 `ACTIVATION_READY`; lifecycle status `ACTIVE`.

Target lifecycle state: P9 `USE_PROOF_PASSED` after checkpoint release.

Prior phase evidence: S09 root-reconciliation completion.

Next forbidden skip: P10 production runtime.

Runtime/provider proof: released exact one-call proof; evidence pending worker.

Claim boundary: baseline is not a use-proof receipt.

## Claim Boundary

This baseline authorizes one internal worker to run the exact dry proof and at
most one granted live provider call, then return evidence without commit. It
does not authorize retry, P10, external adapter, public sync, deployment or
production use.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private P9 dispatch packet and future secret-safe proof evidence.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | paired S10 work order | `DISPATCH_READY` | PASS |
| Completion or reviewer artifact | future worker return | not executed | N/A with reason: pending worker |
| Roadmap state | NCR D013 P9 | packet authored; P10 closed | PASS |
| Registry JSON | target registry/truth/index | unchanged | PASS |
| Registry Markdown | target package | unchanged | PASS |
| External evidence digest | future use-proof JSON | pending worker execution | N/A with reason: pending execution |
| System loop interlock | active resolver and external projection | internal ready; external denied | PASS |
| Session continuity | active session surfaces | pending packet commit | BLOCKED with reason: commit pending |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| packet state | released only after explicit checkpoint | `DISPATCH_READY` after operator release | PASS |
| dry proof | exact dry readiness token | not run | N/A with reason: pending worker |
| live receipt | `LIVE_PROVIDER_USE_PROOF_PASS` and receipt | not run | N/A with reason: pending worker |
| provider calls | at most one under exact grant | zero before worker start | PASS |

