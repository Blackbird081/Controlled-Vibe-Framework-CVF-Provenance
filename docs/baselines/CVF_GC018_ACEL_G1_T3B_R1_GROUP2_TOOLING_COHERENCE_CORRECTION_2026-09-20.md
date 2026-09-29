# CVF GC-018 Baseline - ACEL G1 T3B R1 Group 2 Tooling Coherence Correction

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: ACEL-G1-T3B-R1-GROUP2-TOOLING-COHERENCE-CORRECTION

Dispatch base head: `b8d23fdd362322686b77c53dd2b11b5cb1e65d55`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: Local orchestrator/reviewer

successorTrancheOpened: NO

providerExecutionAuthority: FORBIDDEN

## Purpose

Authorize one consolidated R1 correction of the uncommitted T3B Group 2
tooling. The correction closes four independent-review findings: cross-
principal read access, per-version spec binding, real supersession entry and
worker-return gate readiness. No real Group 2 source may be created.

## Decision / Baseline / Proposed Tranche

The current five worker outputs remain unaccepted. R1 keeps the same exact
five-path manifest and corrects it in place. The worker may use only hermetic
fixtures and read-only OS facts. It must not request credentials, invoke
`runas`, execute as Party A/Approver, touch either real Group 2 source path,
stage or commit.

R1 must make the operational handoff possible: Party A owns and can write each
immutable spec; Approver can read but never modify it; Local SID 1001 can read
both artifacts in a normal non-elevated process. Every history event binds to
the independently validated `SPEC_v{n}.json` for its own version. A v1
supersession is legal only when an explicitly cited, independently valid and
already activated newer version exists.

## Evidence / Verification

| Evidence | Result / required correction |
|---|---|
| spec-writer self-test | 42/42 PASS retained; add cross-principal ACL assertions |
| decision-writer self-test | 49/49 PASS retained; add explicit newer-version supersession cases |
| Python suite | 43/43 PASS retained; replace v2-reuses-v1-hash positive with real per-version resolution |
| Local DACL/account probe | Approver is non-admin; Local non-elevated Administrators SID is deny-only; explicit SID grants required |
| worker-return fast gate | FAIL on current return's evidence binding; R1 must repair and pass |
| real Group 2 sources | absent; must remain absent |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ACEL-G1-T3B-R1-GROUP2-TOOLING-COHERENCE-CORRECTION --title "ACEL G1 T3B R1 Group 2 Tooling Coherence Correction" --date 2026-09-20 --base b8d23fdd3 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id acel-g1-t3b-group2-operational-coherence --prior-finding-set-digest bd8845bf9bf7d3c898d56096f2ea596ec2fd854a2d13b5d5ff7fb036ab16df51 --new-independent-critical-evidence CROSS_PRINCIPAL_DACL_AND_PER_VERSION_BINDING_FAILURES --scec-problem-key acel-g1-t3b-group2-source-creation-tooling-problem --scec-chain-mode SUCCESSOR --scec-chain-ordinal 2 --scec-predecessor-path docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_INDEPENDENT_REVIEW_2026-09-20.md --scec-predecessor-sha256 bd8845bf9bf7d3c898d56096f2ea596ec2fd854a2d13b5d5ff7fb036ab16df51 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --no-evidence-readiness-applicable --stdout` |
| generatedProfile | protected-governance-path plus no-commit rework profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with the four consolidated findings, same five-path manifest, exact SID/DACL and per-version binding requirements |
| checkerReadAheadConfirmation | dispatch-quality, core-guard, gate-to-role, worker-return, scaffold-provenance and operation-trace sources inspected before authoring |
| docOnlyNewFields | none |
| claimBoundary | correction dispatch only; no real source, activation, runtime, provider, public or deployment claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| outer Group 2 contract | accepted T2F Source Group 2 and lifecycle | unchanged | RELEASED |
| four consolidated findings | independent review SHA-256 `bd8845bf9bf7d3c898d56096f2ea596ec2fd854a2d13b5d5ff7fb036ab16df51` | all repaired atomically | RELEASED_FOR_REWORK |
| exact Windows SIDs | Party A 1006; Approver 1008; Local reviewer 1001 | immutable inputs to ACL tests | RELEASED |
| real principal execution | separate operator checkpoints after Local acceptance | forbidden in R1 | PARKED_OPERATOR_EXECUTION |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | exact five R1 worker outputs | hermetic correction only; no credentials, real source, staging or commit | this baseline, work order and independent review | local PowerShell/Python only | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | no owner in R1 | no external ingress, authentication, mutation, receipt, runtime or public claim | no source authorizes an adapter | fresh governed packet required | DEFERRED_WITH_REASON |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`.

Returned defects: NONE_RETURNED. The four current findings are carried by the
named independent review, not inferred from an external defect registry.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | dispatch status; Source Verification columns; protected-path authorization; convergence fields; return evidence readiness and trace labels |
| gateRunPurpose | confirmation/evidence after source-authored correction design, not first discovery of required fields |
| claimBoundary | packet structure only; not implementation correctness or source establishment |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| four returned defects | review finding | `docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_INDEPENDENT_REVIEW_2026-09-20.md` | Findings / Position; Consolidated Correction Contract | T3B-RV-1 through T3B-RV-4 | Local independent review | ACCEPT |
| immutable per-version paths and lifecycle | contract invariant | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 2; Explicit Approval, Activation And Supersession | `SPEC_v{n}.json`; `cvf.specDecisionEvent` | Group 2 source contract | ACCEPT |
| initial five-path manifest | dispatch scope | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_2026-09-20.md` | Required Artifact Manifest | two writers; checker/test; return | original T3B dispatch | ACCEPT |
| exact principal identities | OS/source identity | `docs/reviews/CVF_ACEL_G1_T3B_PRINCIPAL_POLICY_OPERATOR_DECISION_2026-09-20.md` | Operator Decision | Party A SID 1006; Approver SID 1008 | principal decision | ACCEPT |
| Local reader SID | OS identity | `docs/audits/CVF_ACEL_G1_T3A_C2_GROUP1_SOURCE_LOCAL_VERIFICATION_2026-09-20.md` | Source Verification Result | Local operator/reviewer environment | Local source verification | ACCEPT |

## Negative Search And Collision Discipline

The five R1 outputs already exist only as the uncommitted initial return and
are the sole worker-owned mutation targets. The paired R1 baseline/work-order/
review paths were absent before authoring. The 13 unrelated parked paths are
read-only and byte-untouched. Both real Group 2 source paths remain absent.

## Finding-To-Governance Learning Disposition

| Finding group | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| DACL, per-version binding, supersession and return-gate gaps | DISPATCH_AND_WORKER_CONTRACT_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | encode each existing rule as an executable R1 regression; elevate to a general checker only if the class recurs |

## Claim Boundary

This baseline authorizes only correction of five uncommitted tooling artifacts
with hermetic evidence. It does not authorize passwords, alternate-user
execution, real Group 2 files, approval/activation, T3E, admission, staging,
worker commit, provider/live/public/deployment effects or automatic successor.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private corrective dispatch; no public artifact or sync authority.
