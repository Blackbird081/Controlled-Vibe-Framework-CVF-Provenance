# CVF TPGR-T0 Shadow Router Implementation Review

Memory class: governed-review

Status: REVIEWER_ACCEPTED_T0_SHADOW_ACTIVE

Date: 2026-08-17

Review-Cost Telemetry: REQUIRED

## Purpose

Authorize and record the bounded TPGR-T0 implementation that converts the
accepted task-proportional design into an active classification standard,
registry/schema, deterministic fail-closed router, tests, and shadow gate
wiring without skipping any legacy guard.

## Target / Source

Target: TPGR-T0 shadow classification and mandatory post-activation work-order
manifest enforcement.

Source authority: the operator's explicit rule-upgrade instruction and
`docs/assessments/CVF_TASK_PROPORTIONAL_GOVERNANCE_AND_ABSORPTION_PROCESS_REDESIGN_2026-08-17.md`.

## Scope

The change is `P3_ELEVATED` because it creates a canonical standard and edits
checker/hook catalogs. It does not implement TPGR-T2 selective execution.

## Core Guard Self-Protection Authorization

Protected paths:

- `governance/compat/CVF_TASK_GOVERNANCE_ROUTE_REGISTRY.json`
- `governance/compat/CVF_TASK_GOVERNANCE_ROUTE_MANIFEST.schema.json`
- `governance/compat/route_task_governance.py`
- `governance/compat/check_task_governance_route.py`
- `governance/compat/test_route_task_governance.py`
- `governance/compat/test_check_task_governance_route.py`
- `governance/compat/agent_autorun_command_catalog.py`
- `governance/compat/local_governance_hook_catalog_pre_commit.py`
- `governance/compat/local_governance_hook_catalog_reviewer_fast.py`
- `governance/compat/local_governance_hook_catalog_pre_push.py`
- `AGENTS.md`
- `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`

Operator authorization: the operator explicitly required the proportional
design to become mandatory rules before the next absorption tranche.

Authorized guard-maintenance scope: TPGR-T0 registry, schema, read-only router,
focused tests, and shadow checker wiring only.

Rollback boundary: remove the four catalog entries and retain the legacy full
gate; do not authorize selective execution.

## Findings / Position

Implementation is accepted for TPGR-T0 shadow use. Deterministic routing,
trigger escalation, fail-closed contradictions, mandatory post-activation
work-order manifests, unchanged legacy command execution, and zero
runtime/provider/public effects were verified.

Focused proof establishes deterministic routing, required escalation,
closed-shape rejection, normalized repo-relative path validation, changed-path
reconciliation, and selected-file absorption full-read enforcement. The
activation range returns `SHADOW_ACTIVATION_COMMIT`, keeps
`selectiveExecutionAuthorized: false`, and selects `RUN_FULL_LEGACY_BUNDLE`.

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| a low profile suppresses a relevant guard | profile floors, protected-path triggers, changed-path reconciliation and fail-closed P3 fallback |
| shadow routing changes legacy behavior | catalog entries add the checker without deleting or reordering any existing command |
| manifest claims paths outside the task | checker compares every changed path with declared path families |
| activation is mistaken for selective execution | machine receipt fixes `selectiveExecutionAuthorized` to false and requires the full legacy bundle |
| future rule drift bypasses the front door | canonical owner is routed through `AGENTS.md` and the instruction-carrier routing index |

## Source Verification Block

| Claimed item | Source file | Verified section or symbol | Disposition |
| --- | --- | --- | --- |
| canonical routing semantics | `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md` | profiles, triggers, activation, full-gate interlock | ACCEPT |
| deterministic registry | `governance/compat/CVF_TASK_GOVERNANCE_ROUTE_REGISTRY.json` | profiles, dimensions, bundles and fallback | ACCEPT |
| closed manifest contract | `governance/compat/CVF_TASK_GOVERNANCE_ROUTE_MANIFEST.schema.json` | `cvf.taskGovernanceManifest.v1` | ACCEPT |
| pure classification | `governance/compat/route_task_governance.py` | `route_manifest` | ACCEPT |
| post-activation enforcement | `governance/compat/check_task_governance_route.py` | range activation and changed-path reconciliation | ACCEPT |
| autorun shadow binding | `governance/compat/agent_autorun_command_catalog.py` | task-proportional governance shadow route | ACCEPT |
| pre-commit shadow binding | `governance/compat/local_governance_hook_catalog_pre_commit.py` | task-proportional governance shadow route | ACCEPT |
| reviewer-fast shadow binding | `governance/compat/local_governance_hook_catalog_reviewer_fast.py` | task-proportional governance shadow route | ACCEPT |
| pre-push shadow binding | `governance/compat/local_governance_hook_catalog_pre_push.py` | task-proportional governance shadow route | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_instruction_carriers.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/run_local_governance_hook_chain.py` |
| literalTokensReviewed | Target / Source; Risk / Corrective Action; Checker Source Read-Ahead Block; Agent Operation Trace Block; Epistemic Process Block; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation/evidence after independent semantic inspection and focused tests, not first discovery |
| claimBoundary | checker conformance does not authorize selective execution or runtime effects |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | independent orchestrator/reviewer |
| Provider or surface | local private provenance repository |
| Session or invocation | TPGR-T0 rules implementation and review, 2026-08-17 |
| Working directory | repository root at activation base `31631706b` |
| Command or tool surface | governed reads, `apply_patch`, Python tests/checkers, reviewer-fast hook, Git inspection |
| Target paths | exact 16-path TPGR-T0 material batch |
| Allowed scope source | operator instruction to make the proportional design mandatory before the next tranche |
| Before status evidence | clean post-T11 HEAD `31631706b` |
| After status evidence | exact TPGR-T0 batch pending acceptance |
| Diff evidence | `git status --short`, `git diff --check`, focused pytest and reviewer-fast output |
| Approval boundary | TPGR-T0 shadow routing only; TPGR-T1 through TPGR-T4 remain unauthorized |
| Claim boundary | local classification/checking only; no runtime, provider/live, public or deploy effect |
| Agent type | Codex orchestrator/reviewer |
| Invocation ID | `tpgr-t0-shadow-router-2026-08-17` |
| Expected manifest | `AGENTS.md`; `docs/assessments/CVF_TASK_PROPORTIONAL_GOVERNANCE_AND_ABSORPTION_PROCESS_REDESIGN_2026-08-17.md`; `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`; `docs/reference/CVF_AGENT_INSTRUCTION_CARRIER_ROUTING_INDEX_2026-08-11.md`; `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md`; `docs/reviews/CVF_TPGR_T0_SHADOW_ROUTER_IMPLEMENTATION_REVIEW_2026-08-17.md`; `governance/compat/CVF_TASK_GOVERNANCE_ROUTE_MANIFEST.schema.json`; `governance/compat/CVF_TASK_GOVERNANCE_ROUTE_REGISTRY.json`; `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/local_governance_hook_catalog_pre_push.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `governance/compat/route_task_governance.py`; `governance/compat/test_check_task_governance_route.py`; `governance/compat/test_route_task_governance.py` |
| Actual changed set | `AGENTS.md`; `docs/assessments/CVF_TASK_PROPORTIONAL_GOVERNANCE_AND_ABSORPTION_PROCESS_REDESIGN_2026-08-17.md`; `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`; `docs/reference/CVF_AGENT_INSTRUCTION_CARRIER_ROUTING_INDEX_2026-08-11.md`; `docs/reference/CVF_TASK_PROPORTIONAL_GOVERNANCE_ROUTING_STANDARD_2026-08-17.md`; `docs/reviews/CVF_TPGR_T0_SHADOW_ROUTER_IMPLEMENTATION_REVIEW_2026-08-17.md`; `governance/compat/CVF_TASK_GOVERNANCE_ROUTE_MANIFEST.schema.json`; `governance/compat/CVF_TASK_GOVERNANCE_ROUTE_REGISTRY.json`; `governance/compat/agent_autorun_command_catalog.py`; `governance/compat/check_task_governance_route.py`; `governance/compat/local_governance_hook_catalog_pre_commit.py`; `governance/compat/local_governance_hook_catalog_pre_push.py`; `governance/compat/local_governance_hook_catalog_reviewer_fast.py`; `governance/compat/route_task_governance.py`; `governance/compat/test_check_task_governance_route.py`; `governance/compat/test_route_task_governance.py` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Epistemic Process Block

### Expected Result / Prediction

The same valid manifest should always yield the same route; mandatory triggers
must raise the profile floor; malformed, contradictory, under-profiled or
path-mismatched input must fail closed without suppressing legacy gates.

### Evidence Comparison

Fifteen focused tests passed. The activation range was compliant and returned
the expected shadow-only/full-legacy interlock. Direct catalog tests passed
36/36. Reviewer-fast initially found only packet-structure and carrier-budget
issues; no routing semantic failure was reported.

### Contradiction Or Gap Disposition

REPAIRED_AND_CONFIRMED: review sections were completed, the root
carrier pointer was compacted within its fixed budget, and the unchanged Guard
Orientation file was removed from the material batch. The complete
reviewer-fast rerun then passed 65/65.

### Claim Update

TPGR-T0 shadow routing is accepted after the repaired reviewer-fast rerun
passed 65/65. Selective routing remains unauthorized.

## Review Cost Telemetry And Stop Disposition

- `reviewRoundCount`: 1
- `workerRepairTurnCount`: 0
- `newRootCauseCountThisRound`: 0
- `dependentFindingCountThisRound`: 0
- `providerCallCount`: 0
- `valueDelta`: deterministic shadow classification with explicit full-legacy fallback
- `stopDisposition`: COMPLETE_REVIEW
- `preRepairAuditDisposition`: COMPLETE_BEFORE_FIRST_REPAIR
- `latencyDisposition`: WITHIN_FAST_PATH_TARGET
- `avoidableDelayClass`: NONE

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance-control implementation; no public sync authorized.

## Claim Boundary

TPGR-T0 shadow enforcement only. No selective guard execution, runtime action,
provider/live call, public write, deployment, or production authority follows.
