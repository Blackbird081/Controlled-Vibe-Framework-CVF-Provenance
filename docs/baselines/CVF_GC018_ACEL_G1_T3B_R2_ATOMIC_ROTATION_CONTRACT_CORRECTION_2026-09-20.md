# CVF GC-018 Baseline - ACEL G1 T3B R2 Atomic Rotation Contract Correction

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: ACEL-G1-T3B-R2-ATOMIC-ROTATION-CONTRACT-CORRECTION

Dispatch base head: `12d2d0d7437db746e4c4c038cf88eb881e03c23d`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: Local orchestrator/reviewer

Reviewer owner: Local orchestrator/reviewer

successorTrancheOpened: NO

providerExecutionAuthority: FORBIDDEN

## Purpose

Correct the controlling Group 2 lifecycle contract and its uncommitted tooling
so version rotation is one durable atomic transition. Preserve accepted R1 ACL
and per-version hash work. No real source or principal execution is authorized.

## Decision / Baseline / Proposed Tranche

R1 is rejected only for supersession/rotation. Its prerequisite state is
unreachable because full-history replay rejects two active versions, while its
guard requires the replacement already be active. Its event schema also drops
the replacement citation before append.

R2 selects an atomic `SUPERSEDED` rotation event with two new required nullable
closed-preimage fields: `replacementSpecVersion` and
`replacementRecomputedHashHex`. For a rotation both are non-null. The event
binds the active old version and a strictly greater, independently validated,
approved and inactive replacement. Applying the event removes old and adds
replacement in one replay step. All other event types require both fields null.

There is no Group 2 operational source, so this proposed-contract correction
has no migration target and no backward-compatibility debt.

## Evidence / Verification

| Evidence | Result / R2 requirement |
|---|---|
| R1 spec writer | 48/48 PASS; accepted and frozen outside R2 worker ownership |
| R1 decision writer | 63/63 PASS but supersession positive is non-discriminating |
| R1 Python suite | 47/47 PASS; per-version binding accepted, atomic rotation absent |
| Local independent probe | two active versions rejected; already-superseded old incorrectly accepted by replacement guard |
| schema inspection | no durable replacement version/hash in `cvf.specDecisionEvent` |
| real Group 2 sources | absent and must remain absent |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ACEL-G1-T3B-R2-ATOMIC-ROTATION-CONTRACT-CORRECTION --title "ACEL G1 T3B R2 Atomic Rotation Contract Correction" --date 2026-09-20 --base 12d2d0d74 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 2 --root-cause-cluster-id acel-g1-t3b-group2-atomic-rotation --prior-finding-set-digest 64475b405e5f7886f2f9faecf6f50be13c95c8c7a6e5c1cd97260219630fe62e --new-independent-critical-evidence UNREACHABLE_SUPERSESSION_STATE_AND_UNBOUND_REPLACEMENT --scec-problem-key acel-g1-t3b-group2-source-creation-tooling-problem --scec-chain-mode SUCCESSOR --scec-chain-ordinal 4 --scec-predecessor-path docs/reviews/CVF_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_COMPLETION_2026-09-20.md --scec-predecessor-sha256 64475b405e5f7886f2f9faecf6f50be13c95c8c7a6e5c1cd97260219630fe62e --scec-required-disposition STOP_REASSESS_ARCHITECTURE --scec-successor-scope INTEGRATED_ROOT_CONTRACT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | protected-governance-path plus no-commit rework profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | selected atomic rotation, exact five-path R2 manifest, durable two-hash binding and negative probes |
| checkerReadAheadConfirmation | dispatch, protected-path, convergence, worker-return and trace checkers read before authoring |
| docOnlyNewFields | none |
| claimBoundary | contract/tooling correction only; no source establishment or runtime effect |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| R1 independent review | completion review SHA-256 `64475b405e5f7886f2f9faecf6f50be13c95c8c7a6e5c1cd97260219630fe62e` | correct both consolidated findings | RELEASED_FOR_ROOT_CONTRACT_REWORK |
| accepted R1 partial work | explicit ACLs and per-version hash validation | preserve without redesign | RELEASED_FOR_REUSE |
| operational migration | both Group 2 source paths absent | no compatibility layer required | NOT_APPLICABLE_WITH_REASON |
| real principal execution | operator checkpoint after later Local acceptance | forbidden in R2 | PARKED_OPERATOR_EXECUTION |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | exact five R2 paths | local contract/tooling correction; no credentials, real source, staging or commit | this baseline, R2 work order and R1 review | local Markdown/PowerShell/Python only | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | no R2 owner | no external ingress, mutation, runtime or public claim | no adapter authority | fresh governed packet required | DEFERRED_WITH_REASON |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`.

Returned defects: NONE_RETURNED. The controlling findings come from the named
Local completion review.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | dispatch status, Source Verification columns, protected-path authorization, convergence fields, return and trace labels |
| gateRunPurpose | confirmation after source-authored architecture selection |
| claimBoundary | packet structure only; not implementation correctness |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| unreachable R1 rotation and absent durable citation | independent review | `docs/reviews/CVF_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_COMPLETION_2026-09-20.md` | Findings / Position; Independent Probe Evidence | T3B-R1-RV-1 and T3B-R1-RV-2 | Local reviewer | ACCEPT |
| contradictory lifecycle and closed schema | proposed source contract | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 2; Explicit Approval, Activation And Supersession | `cvf.specDecisionEvent` | Group 2 contract | ACCEPT |
| accepted ACL and per-version partial work | returned implementation | `docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-20.md` | Findings / Position; Command Evidence | T3B-RV-1 and T3B-RV-2 | R1 worker return | ACCEPT |
| exact principal identities | operator decision | `docs/reviews/CVF_ACEL_G1_T3B_PRINCIPAL_POLICY_OPERATOR_DECISION_2026-09-20.md` | Operator Decision | Party A 1006; Approver 1008; Local 1001 | identity decision | ACCEPT |

## Negative Search And Collision Discipline

The R2 baseline/work-order paths were absent before authoring. R2 owns five
named existing/new paths only. The returned spec writer and thirteen unrelated
parked paths remain read-only. Both real Group 2 source paths remain absent.

## Finding-To-Governance Learning Disposition

| Finding group | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| unreachable transition plus unbound durable replacement | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | repair the earliest owning T2F contract and make the atomic rotation sequence an executable regression |

## Claim Boundary

This baseline authorizes only the five-path R2 correction. It does not
authorize passwords, alternate-user execution, real sources, activation,
consumer wiring, admission, worker commit, provider/live/public/deployment or
automatic successor work.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private contract/tooling correction with no public-sync authority.
