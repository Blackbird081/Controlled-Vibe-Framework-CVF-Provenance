# CVF GC-018 Baseline - ACEL G1 T3B Group 2 Source-Creation Tooling

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: ACEL-G1-T3B-GROUP2-SOURCE-CREATION-TOOLING

Dispatch base head: `a4c77bd0f`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner and reviewer: Local orchestrator/reviewer

Worker target: shared-workspace `INTERNAL_AGENT`

## Purpose

Authorize a bounded worker to implement and hermetically test the two-principal
tooling for later creation of the Group 2 verification-authority specification
and its independent approval/activation history. The worker must not log on as
either principal or create the real Group 2 source.

## Decision / Baseline / Proposed Tranche

Decision: dispatch one tooling-only tranche. Baseline: Group 1 is
`SOURCE_CREATED_LOCAL_VERIFIED`; Group 2 remains `SOURCE_NOT_CREATED`; the
exact v1 policy bytes and both concrete principals are now fixed. Proposed
tranche: implement exact-path author/approver tools, an independent checker,
focused tests and a worker return, then return for Local review.

## Evidence / Verification

Party A is `LAM-RUBY\cvf-g1-party-a`, SID
`S-1-5-21-1644666849-912006174-747199667-1006`. The activation approver is
`LAM-RUBY\cvf-g1-approver`, SID
`S-1-5-21-1644666849-912006174-747199667-1008`; it is enabled,
password-required, expiring and non-admin. Both launchers pass `--check`.
The two real source paths and all five worker outputs were absent before
dispatch.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T3B-GROUP2-SOURCE-CREATION-TOOLING --title "ACEL G1 T3B Group 2 Source Creation Tooling" --date 2026-09-20 --base a4c77bd0f --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with the approved Group 2 content contract, exact two-principal topology, five-path manifest and operator execution boundary |
| checkerReadAheadConfirmation | work-order dispatch quality, gate-to-role closeability, worker-return quality, scaffold provenance and operation-trace checker sources read before authoring |
| docOnlyNewFields | none |
| claimBoundary | dispatch provenance only; no source, activation, runtime, provider, public or deployment behavior exists from this baseline |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| T2F Group 2 contract | accepted dual-hash schemas, state machine, paths and unique-active invariant | exact contract remains current | RELEASED |
| v1 policy bytes | operator decision at `ef29dbc1f`, corrected principal record at `16a6273dc` | exact compact UTF-8 JCS and freshness value fixed | RELEASED |
| Party A identity | Group 1 verified source and launcher | exact name/SID remain valid | RELEASED |
| activation approver identity | read-only Local account verification on 2026-09-20 | enabled, password-required, non-admin and separate SID | RELEASED |
| actual source writes | Party A authors; approver separately approves/activates | Local must first accept tooling | PARKED_OPERATOR_EXECUTION |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | five exact worker artifacts in the paired work order | tooling and hermetic fixtures only; no credentials, alternate-principal execution, source write, staging or commit | T2F contract, operator decision and verified local account posture | internal filesystem/PowerShell/Python only | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | no external adapter owner in this tranche | no external ingress, authentication, mutation, receipt, runtime or public claim | no accepted source authorizes such an interface | deferred; a fresh source-verified work order is required | DEFERRED_WITH_REASON |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class CODE_CHANGE --role dispatcher --lifecycle-phase dispatch`.

Returned defects: NONE_RETURNED. Dispatch impact: none.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | dispatch-ready status, exact Source Verification columns, Scaffold Provenance fields, Gate-To-Role graph, trace labels and no-commit return terms |
| gateRunPurpose | confirmation after source-driven authoring, not first discovery |
| claimBoundary | packet structure and owned-path compatibility only; not implementation correctness |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Group 2 schemas and event order | contract invariant | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Two Distinct Group 2 Hashes; Source Group 2; Explicit Approval, Activation And Supersession | `cvf.specFile`; `cvf.specDecisionEvent` | Group 2 operational-source contract | ACCEPT |
| exact v1 decoded bytes and freshness | literal policy | `docs/reviews/CVF_ACEL_G1_T3B_PRINCIPAL_POLICY_OPERATOR_DECISION_2026-09-20.md` | Operator Decision | `freshnessThresholdSeconds`; compact JCS payload | operator-approved v1 content | ACCEPT |
| Party A principal | identity value | `docs/audits/CVF_ACEL_G1_T3A_C2_GROUP1_SOURCE_LOCAL_VERIFICATION_2026-09-20.md` | Source Verification Result | `LAM-RUBY\cvf-g1-party-a`; SID ending 1006 | Party A source authority | ACCEPT |
| approver principal | identity value | `docs/reviews/CVF_ACEL_G1_T3B_PRINCIPAL_POLICY_OPERATOR_DECISION_2026-09-20.md` | Operator Decision; Launcher Artifacts | `LAM-RUBY\cvf-g1-approver`; SID ending 1008 | Contract 2 activation authority | ACCEPT |
| output and source paths absent | collision fact | `docs/audits/CVF_ACEL_G1_T3B_GROUP2_SOURCE_READINESS_ROUTE_2026-09-20.md` | Readiness Evidence; Negative Search And Collision Discipline | Group 2 proposed paths | Local route audit | ACCEPT |

## Negative Search And Collision Discipline

Nine exact `Test-Path` probes returned `False`: paired dispatch paths, five
worker outputs and two real source paths. Exact batch/tool/checker token search
returned no predecessor. The existing T2F/readiness/decision prose is source
authority, not a path collision.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| prior principal proposal exceeded Windows identity limits and initial account creation left the separate password-required flag false | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | this dispatch source-verifies exact platform-representable names/SIDs and requires executable identity/posture preflights before real mode |

Runtime/provider/cost learning: `N/A_WITH_REASON`; this dispatch performs no
provider call or runtime-service evaluation.

## Claim Boundary

This baseline authorizes tooling and hermetic tests only. It does not authorize
the worker to run as Party A or the approver, access either password, create
real Group 2 files, approve or activate a policy, stage, commit, wire T3E,
admit a candidate, claim live proof, export publicly or deploy.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private two-principal source-control preparation; no public artifact or
public-sync authority exists.
