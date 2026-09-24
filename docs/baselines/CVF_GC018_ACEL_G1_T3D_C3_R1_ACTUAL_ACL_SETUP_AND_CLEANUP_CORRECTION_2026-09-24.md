# CVF GC-018 Baseline - ACEL G1 T3D-C3 R1 Actual ACL Setup And Cleanup Correction

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY_LOCAL_IMPLEMENTATION

Batch ID: ACEL-G1-T3D-C3-R1-ACTUAL-ACL-SETUP-AND-CLEANUP-CORRECTION

Dispatch base head: `a31ec4bcd13fb69b0fc76d6f4b261e48e0d68396`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator

Reviewer owner: Local reviewer distinct from implementation phase

Worker target: Local implementation role

## Purpose

Repair the actual-mode coordinator defect proven by the approved prepare-only
attempt: root-first protected non-inheriting ACL setup made pre-created children
inaccessible, and catch cleanup then masked the primary exception. Limit the
repair to ordering, exception preservation, exact-root cleanup and regressions.

## Source / Predecessor Evidence

| Source | Verified fact | Disposition |
|---|---|---|
| `scripts/acel_g1_group4_actual_token_coordinator.ps1` | `Add-Ace` uses no inheritance; actual setup currently applies root ACL before child ACLs; catch directly removes the tree | ACCEPT |
| `CVF_SESSION/state/entries/acelG1T3dC3ActualTokenPrepareOnlyFailure20260923.json` | approved payload passed; setup failed before packet materialization; exact partial root was verified and removed | ACCEPT |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C3_ACTUAL_TOKEN_DISPOSABLE_RUNNER_2026-09-23.md` | predecessor high-risk proof contract and containment/principal boundaries remain controlling | ACCEPT |
| `docs/reviews/CVF_ACEL_G1_T3D_C3_ACTUAL_TOKEN_DISPOSABLE_RUNNER_COMPLETION_2026-09-23.md` | reusable runner was accepted only for bounded TestPolicy evidence, not actual ACL behavior | ACCEPT |

## Decision / Baseline

The operator selected one bounded G1 repair tranche and parked G2-G6. The
repair may change only the coordinator and one worker return. It must:

1. apply explicit ACLs to pre-created children before protecting the root;
2. restore exact cleanup access only inside the validated disposable root;
3. preserve the primary setup exception if cleanup succeeds;
4. report both primary and cleanup failures if cleanup also fails;
5. add hermetic regression assertions for ordering and primary-error retention;
6. leave the independent actual-mode prepare-only probe pending Local review.

No Party B/C process, password, account mutation, real Group 4 source, T3E,
provider/live, public-sync or deployment action is authorized during worker
implementation. A later Local reviewer may run exactly one fresh elevated
prepare-only probe under an exact absent root using the already approved
secret-free payload; principal execution remains forbidden.

## Evidence / Verification

Required worker evidence:

- coordinator self-test PASS with the new regressions;
- probe and finalizer self-tests remain PASS;
- TestPolicy packet remains 22/22 and claims no actual-token proof;
- source diff contains only the coordinator and worker return;
- worker return remains `COMPLETE_PENDING_REVIEW` with the independent probe
  explicitly pending.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T3D-C3-R1-ACTUAL-ACL-SETUP-AND-CLEANUP-CORRECTION --title "ACEL G1 T3D-C3 R1 Actual ACL Setup And Cleanup Correction" --date 2026-09-24 --base a31ec4bcd --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id ACEL-G1-T3D-C3-R1-ACL-ORDERING --prior-finding-set-digest 6cb7547879201819361278efbb5c52910151f8b859a3bdbb3d94a3ebeb4aac99 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence true --scec-problem-key ACEL-G1-T3D-C3-ACTUAL-ACL-SETUP --scec-chain-mode SUCCESSOR --scec-chain-ordinal 1 --scec-predecessor-path docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3D_C3_ACTUAL_TOKEN_DISPOSABLE_RUNNER_2026-09-23.md --scec-predecessor-sha256 6dc845e66df98b645f6116fafc1a07e8930429b45ddefc5193f99fd7280bbc4d --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope EXECUTABLE_IMPLEMENTATION --no-evidence-readiness-applicable --stdout` |
| generatedProfile | generic worker rework dispatch with no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with the exact failure evidence, two-path scope, stop conditions and verification boundary |
| checkerReadAheadConfirmation | predecessor checker read-ahead plus current high-risk, dispatch-quality, closeability, trace and structural sources |
| docOnlyNewFields | none |
| claimBoundary | dispatch baseline only; no successful repair or actual-token proof is claimed |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`high-risk-local-transaction-repair`, role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "high-risk-local-transaction-repair" --role worker --lifecycle-phase implementation --max-results 8 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | retain predecessor high-risk proof and add direct regressions for the observed failure |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | dispatch envelope, source-verification columns, no-question rule, high-risk applicability and nine-key contract, operator checkpoint, manifests, trace labels, worker-return contract and closeability graph |
| gateRunPurpose | confirm the completed packet against machine admission; gates do not supply source evidence |
| claimBoundary | static authoring admission only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: machine-specific ACL failure and repair planning remain private.

## Claim Boundary

This baseline authorizes only a reversible Local code/test correction and a
pending worker return. It does not establish successful actual-mode setup,
Party B/C behavior, source authority, runtime readiness or production safety.
