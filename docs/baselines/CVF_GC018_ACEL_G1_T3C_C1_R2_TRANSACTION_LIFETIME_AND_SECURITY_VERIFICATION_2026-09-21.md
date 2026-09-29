# CVF GC-018 Baseline - ACEL G1 T3C-C1 R2 Transaction Lifetime And Security Verification

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: ACEL-G1-T3C-C1-R2-TRANSACTION-LIFETIME-AND-SECURITY-VERIFICATION

Dispatch base head: `dcba5f7f017af96ae2f61c1ddc5cbf54fe69945d`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: Local orchestrator/reviewer

successorTrancheOpened: NO

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize one consolidated R2 correction of the same four uncommitted T3C-C1
outputs. R2 closes the transaction-wide exclusion, pre-write artifact cleanup
and applied owner/DACL verification gaps found by Local after R1.

## Decision / Baseline / Proposed Tranche

R1 is `REWORK_REQUIRED`. Its five original repairs and passing evidence are
retained; the worker must not restart them. R2 changes only the transaction
lifetime and its regression oracles. One process-wide or cross-process guard
must remain held from before the first possible durable artifact creation
through final data/security validation, or through completed rollback.

The exact original four-path manifest remains in force. No credentials,
`runas`, Party B execution, real Group 1 read, real Group 3 creation, staging
or worker commit is authorized.

## Evidence / Verification

| Evidence | Result / required correction |
|---|---|
| R1 Python suite | 42/42 PASS retained |
| R1 writer self-test | 31/31 PASS retained, but no guard-lifetime adversary |
| worker-return fast gate | COMPLIANT retained as structural evidence |
| Local lock-order probe | exclusive stream ends before DACL and post-validation |
| Local creation-boundary probe | directory/OpenOrCreate can mutate before rollback ownership starts |
| Local ACL probe | no post-set read-back; only Access state snapshotted |
| real source check | `LOG.jsonl` absent |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ACEL-G1-T3C-C1-R2-TRANSACTION-LIFETIME-AND-SECURITY-VERIFICATION --title "ACEL G1 T3C-C1 R2 Transaction Lifetime And Security Verification" --date 2026-09-21 --base dcba5f7f0 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 2 --root-cause-cluster-id acel-g1-t3c-c1-observation-transaction-integrity --prior-finding-set-digest 877e0a0301b640337e3f6d5c716451c81bc0c08187a7bdb7b02b508a47d7f4e8 --new-independent-critical-evidence TRANSACTION_GUARD_RELEASED_BEFORE_SECURITY_AND_POSTVALIDATION --scec-problem-key acel-g1-t3c-c1-group3-observation-log-tooling-problem --scec-chain-mode SUCCESSOR --scec-chain-ordinal 4 --scec-predecessor-path docs/reviews/CVF_ACEL_G1_T3C_C1_R1_GROUP3_OBSERVATION_TRANSACTION_CORRECTION_COMPLETION_2026-09-21.md --scec-predecessor-sha256 877e0a0301b640337e3f6d5c716451c81bc0c08187a7bdb7b02b508a47d7f4e8 --scec-required-disposition ROOT_CONTRACT_REQUIRED --scec-successor-scope INTEGRATED_ROOT_CONTRACT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | protected-governance-path plus no-commit R2 rework profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with three residual findings, exact four-path scope, guard lifetime and security read-back oracles |
| checkerReadAheadConfirmation | dispatch-quality, core-guard, gate-to-role, worker-return, scaffold-provenance, convergence and operation-trace sources retained from R1 and rechecked by the dispatch gates |
| docOnlyNewFields | none |
| claimBoundary | correction dispatch only; no source, runtime, provider, public or deployment claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| R1 record-level repairs | R1 return plus Local 42/42 and 31/31 reruns | preserve without regression | RELEASED_FOR_REUSE |
| three R1 residual findings | completion review SHA-256 `877e0a0301b640337e3f6d5c716451c81bc0c08187a7bdb7b02b508a47d7f4e8` | repair together under an integrated root contract | RELEASED_FOR_REWORK |
| real observation | Local acceptance then explicit operator checkpoint | forbidden now | PARKED_OPERATOR_EXECUTION |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | exact four R2 worker outputs | hermetic correction only; no credentials, real source, staging or commit | baseline, work order and R1 completion review | local PowerShell/Python | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | no owner in R2 | no external ingress, mutation, receipt or runtime claim | no accepted adapter | fresh governed packet required | DEFERRED_WITH_REASON |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`.

Returned defects: NONE_RETURNED. The three current findings are carried by the
named R1 completion review.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | dispatch status; protected paths; convergence; return/no-commit fields; trace and public disposition |
| gateRunPurpose | confirmation after source-authored R2 contract, not first discovery |
| claimBoundary | packet structure only; not implementation correctness or source establishment |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| three residual defects | review finding | `docs/reviews/CVF_ACEL_G1_T3C_C1_R1_GROUP3_OBSERVATION_TRANSACTION_CORRECTION_COMPLETION_2026-09-21.md` | Findings / Position | T3C-C1-R1-RV-1 through RV-3 | Local review | ACCEPT |
| original five repairs | retained worker evidence | `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_WORKER_RETURN_2026-09-21.md` | Findings / Position; Command Evidence | R1 repair matrix | internal worker | ACCEPT_NARROWLY |
| exact four-path scope | dispatch invariant | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_R1_GROUP3_OBSERVATION_TRANSACTION_CORRECTION_2026-09-21.md` | Required Artifact Manifest | writer; checker; focused test; return | R1 dispatch | ACCEPT |
| append-only Group 3 source | contract invariant | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 3 | `LOG.jsonl` | operational source contract | ACCEPT |

## Negative Search And Collision Discipline

The new R2 baseline, work order and R1 completion review did not exist before
authoring. The four worker outputs remain the sole worker targets; thirteen
unrelated parked paths remain byte-untouched. The real Group 3 log remains
absent. No worker output is renamed or split.

## Finding-To-Governance Learning Disposition

| Finding group | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| transaction lifetime underspecified in R1 | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | exact lifetime and adversarial scheduling oracle required by R2; carry into the parked post-acceptance CVF foundation tranche |
| security applied without read-back | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | R2 must compare actual owner/protection/ACE set to policy and restore captured state |

## Claim Boundary

This baseline authorizes only the three-finding correction of four uncommitted
tooling outputs using disposable fixtures. It does not authorize passwords,
alternate-user execution, real source access, Party C/Group 4, T3E, admission,
staging, worker commit, provider/live/public/deployment or automatic successor.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private corrective dispatch; no public artifact or sync authority.
