# CVF GC-018 Baseline - ACEL G1 T3C-C1 R1 Group 3 Observation Transaction Correction

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: ACEL-G1-T3C-C1-R1-GROUP3-OBSERVATION-TRANSACTION-CORRECTION

Dispatch base head: `2b171c8c57a7d7e7646711ae47e04f59736ed94d`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: Local orchestrator/reviewer

successorTrancheOpened: NO

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize one consolidated R1 correction of the four uncommitted T3C-C1
outputs. R1 closes exact-append corruption, post-write rollback, locked-chain
race, strict JSONL and packet-manifest findings. No real Group 3 source may be
read or created by the worker.

## Decision / Baseline / Proposed Tranche

The current return is `REWORK_REQUIRED`. R1 retains the original exact
four-path manifest and repairs it in place. The worker may use disposable
fixtures only and must not request credentials, invoke `runas`, execute as
Party B, read the real Group 1 registry, create the real observation log,
stage or commit.

The corrected writer must use one coherent exclusive transaction: validate
the exact locked old bytes, derive the prior hash, append exactly one new line,
harden and verify security, and report success. Any failure after mutation
begins must restore the exact prior data and security state or remove a new
artifact. The checker must reject blank JSONL lines rather than normalize them.

## Evidence / Verification

| Evidence | Result / required correction |
|---|---|
| worker Python suite | 38/38 PASS retained for unaffected semantics |
| checker self-test | PASS retained for published vector/genesis behavior |
| writer self-test | 21/21 PASS but exact append oracle is insufficient |
| Local source probe | non-genesis append writes `old + old + new`, not `old + new` |
| transaction inspection | DACL hardening occurs after flush without rollback |
| parser inspection | blank/whitespace lines are skipped despite rejection contract |
| manifest reconciliation | three support files exceeded the exact four-path manifest and were removed by Local |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ACEL-G1-T3C-C1-R1-GROUP3-OBSERVATION-TRANSACTION-CORRECTION --title "ACEL G1 T3C-C1 R1 Group 3 Observation Transaction Correction" --date 2026-09-21 --base 2b171c8c5 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id acel-g1-t3c-c1-observation-transaction-integrity --prior-finding-set-digest 58851938894a1f72acbe0d4f23f38a1842610bd34fd3d481eacc2331401e0544 --new-independent-critical-evidence EXACT_APPEND_AND_ROLLBACK_FAILURES --scec-problem-key acel-g1-t3c-c1-group3-observation-log-tooling-problem --scec-chain-mode SUCCESSOR --scec-chain-ordinal 2 --scec-predecessor-path docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_INDEPENDENT_REVIEW_2026-09-21.md --scec-predecessor-sha256 58851938894a1f72acbe0d4f23f38a1842610bd34fd3d481eacc2331401e0544 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --no-evidence-readiness-applicable --stdout` |
| generatedProfile | protected-governance-path plus no-commit rework profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with five consolidated findings, original four-path manifest and exact transaction/rollback probes |
| checkerReadAheadConfirmation | dispatch-quality, core-guard, gate-to-role, worker-return, scaffold-provenance and operation-trace sources inspected before authoring |
| docOnlyNewFields | none |
| claimBoundary | correction dispatch only; no source, observation, runtime, provider, public or deployment claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| Group 3 contract | accepted T2F Source Group 3 | unchanged | RELEASED |
| five review findings | independent review SHA-256 `58851938894a1f72acbe0d4f23f38a1842610bd34fd3d481eacc2331401e0544` | repair together | RELEASED_FOR_REWORK |
| Party B identity | appointment and OS verification already accepted | no alternate-user use in R1 | RELEASED_FOR_TOOLING_ONLY |
| real observation | Local acceptance then explicit operator checkpoint | forbidden now | PARKED_OPERATOR_EXECUTION |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | exact four R1 worker outputs | hermetic correction only; no credentials, real source, staging or commit | baseline, work order and independent review | local PowerShell/Python | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | no owner in R1 | no external ingress, authentication, mutation, receipt, runtime or public claim | no accepted adapter | fresh governed packet required | DEFERRED_WITH_REASON |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`.

Returned defects: NONE_RETURNED. The current findings are carried by the named
independent review.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | dispatch status; Source Verification columns; protected paths; convergence; return and no-commit fields |
| gateRunPurpose | confirmation after source-authored R1 contract, not first discovery |
| claimBoundary | packet structure only; not implementation correctness or source establishment |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| five returned defects | review finding | `docs/reviews/CVF_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_INDEPENDENT_REVIEW_2026-09-21.md` | Findings / Position; Consolidated Correction Contract | T3C-C1-RV-1 through T3C-C1-RV-5 | Local review | ACCEPT |
| transactional durable source requirement | contract invariant | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_2026-09-21.md` | Real-mode lock and filesystem boundary | exact append and fail-closed DACL | initial dispatch | ACCEPT |
| exact four-path scope | dispatch invariant | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3C_C1_GROUP3_OBSERVATION_LOG_TOOLING_2026-09-21.md` | Required Artifact Manifest | writer; checker; test; return | initial dispatch | ACCEPT |
| append-only Group 3 chain | contract invariant | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 3 | `LOG.jsonl`; `priorEntryHashHex` | operational source contract | ACCEPT |

## Negative Search And Collision Discipline

The four initial outputs remain the sole worker targets. The paired R1
baseline/work-order/review paths are dispatcher-owned and read-only to the
worker. Thirteen unrelated parked paths remain byte-untouched. The real Group
3 `LOG.jsonl` must remain absent. Disposable fixtures are unique and removed.

## Finding-To-Governance Learning Disposition

| Finding group | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| append/rollback/race oracle gap | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | exact-byte and forced-failure regressions in R1; promote only on recurrence |
| evidence-readiness/manifest contradiction | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | declare evidence readiness not applicable and enforce exact four outputs |

## Claim Boundary

This baseline authorizes only correction of four uncommitted tooling outputs
with hermetic evidence. It does not authorize passwords, alternate-user
execution, real registry reads, real Group 3 creation, Party C/Group 4, T3E,
admission, staging, worker commit, provider/live/public/deployment or an
automatic successor.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private corrective dispatch; no public artifact or sync authority.
