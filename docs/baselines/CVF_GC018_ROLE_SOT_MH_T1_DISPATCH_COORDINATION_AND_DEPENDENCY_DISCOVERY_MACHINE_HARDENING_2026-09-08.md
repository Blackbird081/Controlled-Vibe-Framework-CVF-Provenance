# CVF GC-018 Baseline - ROLE-SOT-MH-T1 Dispatch Coordination And Dependency Discovery Machine Hardening

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Batch ID: ROLE-SOT-MH-T1

Dispatch base head: `6d98b1a27be0b25646ceb395a6faa64c83d47219`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

Decision owner: operator

Reviewer owner: internal orchestrator/reviewer

successorTrancheOpened: NO

## Purpose

Authorize one bounded local machine-hardening successor to
ROLE-SOT-EVIDENCE-T0. The successor converts three observed dispatcher control
gaps into forward-only pre-dispatch checks: execution-anchor substitution,
shared-worktree lane coordination, and dated-owner dependency discovery.

## Scope / Target / Owner Boundary

The batch enriches the existing dispatch-quality and Agent Handoff Boundary
owners. It may update the ADIF-0056 disposition only after the focused machine
proof passes. It creates no third role-governance owner and does not modify the
accepted topology-invariance semantics at `6bcdeaca8`.

The implementation is limited to two existing checker domains, their focused
tests, two existing reference owners, ADIF-0056, and one worker return. It does
not modify the canonical work-order template or dispatch scaffold because both
are maintainability-sensitive owners and the machine prevention can be added
without growing them.

## Accepted Authority And Findings

| Authority | Accepted fact |
|---|---|
| `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0056.md` | A worker-captured execution anchor was declared but an executable pre-implementation command reused the older dispatch anchor. |
| `docs/reviews/CVF_ROLE_SOT_EVIDENCE_TOPOLOGY_INVARIANCE_T0_WORKER_RETURN_2026-09-08.md` | The active worker paths were temporarily removed by concurrent dispatcher activity in the same worktree, and a dated canonical owner dependency was discovered only at material commit. |
| <!--archive-name-exception-->`docs/reference/agent_handoff/CVF_AGENT_HANDOFF_BOUNDARY_MACHINE_CHECK_STANDARD.md` | `crossBatchIsolation` is already an Agent Handoff Boundary concern and its checker is already wired into autorun and hooks. |
| `docs/reference/CVF_WORK_ORDER_DEPENDENCY_RELEASE_EVIDENCE_STANDARD_2026-06-03.md` | Dispatch readiness requires source-backed dependency resolution before worker handoff. |
| `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json` | This registry is the machine-readable source for `BINDING_REFERENCE_ACTIVE_WINDOW` membership. |

## Decision / Baseline

ROLE-SOT-MH-T1 selects three bounded controls:

1. Dispatch quality rejects a real Verification Commands pre-implementation
   command that consumes the packet's dispatch-base literal or symbolic
   `dispatchBaseHead` when the packet says the worker captures
   `executionBaseHead` at start.
2. Agent Handoff Boundary requires a dispatch-ready no-commit handoff to select
   `SEPARATE_GIT_WORKTREE` or `EXPLICIT_LANE_HANDOFF`. The latter must declare
   lane owner, owned paths, no-mutation-while-active boundary, and release
   evidence. This is packet-contract prevention, not filesystem interception.
3. Dispatch quality requires every dated `docs/reference/` path in worker write
   ownership to appear in a Dated Owner Dependency Discovery table. A path
   classified `BINDING_REFERENCE_ACTIVE_WINDOW` must already be present in the
   active-window registry; a non-binding classification requires a reason.

The controls are forward-only for changed dispatch packets. Historical packets
are not rewritten. The work-order template and scaffold remain untouched.

## Acceptance Matrix

| Case | Required result |
|---|---|
| worker-capture plus `<executionBaseHead>` | PASS |
| worker-capture plus `$executionBaseHead` | PASS |
| worker-capture plus dispatch SHA | FAIL |
| worker-capture plus symbolic `dispatchBaseHead` | FAIL |
| explicit lane handoff with all lane fields | PASS |
| explicit lane handoff missing mutation boundary or release evidence | FAIL |
| separate Git worktree coordination | PASS |
| dated binding owner registered in active-window registry | PASS |
| dated binding owner absent from registry | FAIL |
| dated non-binding owner with reason | PASS |
| dated owner omitted from discovery table | FAIL |
| ordinary non-dated reference ownership | unchanged |

## Evidence / Verification

The worker runs the two focused checker suites, existing lifecycle regressions,
Python automation size enforcement, ADIF integrity, the worker-return fast
gate, and exact changed-set checks. The reviewer consumes that evidence and
reruns only the bounded hostile cases needed to challenge the three controls.
No live-provider proof applies to this repository-local packet contract.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| execution-anchor defect is active guidance | current defect evidence | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0056.md` | field block and Remediation | `checkerBindings` | ADIF entry | ACCEPT |
| shared-worktree and dated-owner findings occurred in T0 | accepted worker evidence | `docs/reviews/CVF_ROLE_SOT_EVIDENCE_TOPOLOGY_INVARIANCE_T0_WORKER_RETURN_2026-09-08.md` | Finding-To-Governance Learning Disposition | `ORCHESTRATOR_PACKET_GAP` | accepted T0 return | ACCEPT |
| handoff checker owns cross-batch isolation | executable control | `governance/compat/check_agent_handoff_boundary.py` | `_validate_work_order` | `crossBatchIsolation` | Agent Handoff Boundary gate | ACCEPT |
| dispatch-quality gate owns work-order readiness | executable control | `governance/compat/check_work_order_dispatch_quality.py` | implementation module loader | `IMPLEMENTATION_MODULES` | dispatch-quality gate | ACCEPT |
| active-window membership has a canonical registry | machine source | `governance/compat/CVF_ACTIVE_WINDOW_REGISTRY.json` | `windows` | `activePath` | active-window registry | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order dispatch machine hardening`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Source-directed disclosure: `ADIF-0056` remains the accepted root finding even
though the current resolver vocabulary returns zero candidates for this query.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ROLE-SOT-MH-T1","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"KNOWN_PATTERN"},"pathFamilies":["governance/compat","docs/reference","docs/reviews","docs/baselines","docs/work_orders"],"claims":["forward-only dispatch packet machine hardening"],"requiredProof":["anchor negative cases","lane coordination negative cases","dated-owner registry negative cases","focused tests","independent review"],"operatorCheckpoints":["scope expansion","hook or autorun change","runtime or external effect"],"forbiddenEffects":["template or scaffold growth","hook or autorun wiring","runtime or provider execution","public sync","worker commit"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"N/A with reason: bounded named control cluster","completenessClaimChanged":false}}
```

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ROLE-SOT-MH-T1 --title "Role SOT Dispatch Coordination And Dependency Discovery Machine Hardening" --date 2026-09-08 --base 6d98b1a27be0b25646ceb395a6faa64c83d47219 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | protected-governance no-commit baseline profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced placeholders with the exact three-defect boundary, source pins, acceptance cases, and rollback. |
| checkerReadAheadConfirmation | Applicable dispatch, ADIF, structural, routing, handoff, self-protection and export checkers were read. |
| docOnlyNewFields | shared-worktree and dated-owner packet fields only; no runtime field |
| claimBoundary | Scaffold provenance proves authoring origin only, not implementation correctness. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; Source Verification columns; `Core Guard Self-Protection Authorization`; `DEFERRED_PRIVATE_ONLY`; protected-path list; task manifest enums |
| gateRunPurpose | Confirmation and dispatch evidence after source read-ahead, not first discovery of artifact shape. |
| claimBoundary | Structural compliance cannot prove implementation correctness or actual worktree isolation. |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: enrich only the existing dispatch-quality
and Agent Handoff Boundary checkers, focused tests, their existing standards,
ADIF-0056, and the bounded worker return.

Protected paths:

- `governance/compat/check_work_order_dispatch_quality_core.py`
- `governance/compat/test_check_work_order_dispatch_quality_machine_hardening.py`
- `governance/compat/check_agent_handoff_boundary.py`
- `governance/compat/test_check_agent_handoff_boundary.py`

Operator authorization: on 2026-09-08 the operator instructed the agent to
open a ROLE-SOT machine-hardening successor for ADIF-0056, shared-worktree
coordination, and dispatch dependency discovery.

Rollback boundary: revert only ROLE-SOT-MH-T1 material if rejected; preserve
ROLE-SOT-EVIDENCE-T0 at `6bcdeaca8`, ADIF learning at `b8268100a`, RABA park at
`0767a16e5`, and P4-C1 at `b9bdba712`.

Not authorized: no template, scaffold, active-window registry, autorun, hook,
session, runtime, provider/live, public-sync, deploy, push, or production edit.

## Risk / Corrective Action

The main risk is claiming prevention beyond what repository-local packet gates
can observe. Acceptance therefore distinguishes machine-checked packet shape
from actual filesystem/process isolation. Any need for a daemon, lock manager,
Git wrapper, hook wiring, or registry mutation returns to the operator.

## Claim Boundary

This baseline authorizes one bounded internal no-commit implementation and
independent review. It does not open RABA-T1 through RABA-T3, change role SOT
semantics, intercept Git/filesystem operations, or authorize runtime,
provider/live, public, deployment, push, or production work. No successor opens
automatically.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private-provenance governance hardening with no public-sync authority.
