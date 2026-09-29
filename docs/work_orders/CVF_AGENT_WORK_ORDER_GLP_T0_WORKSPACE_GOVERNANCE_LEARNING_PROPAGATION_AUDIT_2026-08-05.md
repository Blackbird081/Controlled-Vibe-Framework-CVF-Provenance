# CVF Agent Work Order - GLP T0 Workspace Governance Learning Propagation Audit

## Dispatch Prompt Envelope

Role: documentation and source-verification worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_GLP_T0_WORKSPACE_GOVERNANCE_LEARNING_PROPAGATION_AUDIT_2026-08-05.md`

Paired baseline: `docs/baselines/CVF_GC018_GLP_T0_WORKSPACE_GOVERNANCE_LEARNING_PROPAGATION_AUDIT_2026-08-05.md`

dispatchBaseHead: `ace02fda7`

executionBaseHead: `9acec42b5`

closureBaseHead: `9acec42b5`

Commit mode: WORKER_MUST_NOT_COMMIT

Current-time notes: packet authored 2026-08-05 from provenance HEAD
`ace02fda7`; all external state and generated workspace mutation are excluded.

Do-not-misread notes: this is a documentation/source audit, not permission to
change the propagation chain or to run a provider, network, or public action.

Required first actions: complete startup acknowledgment, capture HEAD/status,
read the roadmap, baseline, source files, guard orientation, literal gotchas,
and checker sources, then run pre-flight checks.

Return contract: create exactly the audit and worker return, leave both
uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_BOUNDED

docType: work_order

Date: 2026-08-05

Batch ID: GLP-T0

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GLP-T0 --title "Workspace Governance Learning Propagation Audit" --date 2026-08-05 --base ace02fda7 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with GLP authority, source audit, output manifest, and exact decision contract |
| checkerReadAheadConfirmation | dispatch-quality, prompt-envelope, handoff, ADIF, trace, structural, Delta, foundation-layout, and public-disposition checkers |
| docOnlyNewFields | authorityClass; carrierStatus; alternativeCost; T0Decision |
| claimBoundary | dispatch authoring only; no worker execution or implementation |

## Purpose

Independently reproduce the GLP-R0 propagation evidence and decide whether the
smallest next action is bootstrap alignment, documentation-only alignment, or
no change.

## Authority Chain

- Operator decision: accepted GLP-R0 and continuation on 2026-08-05.
- Roadmap: `docs/roadmaps/CVF_WORKSPACE_GOVERNANCE_LEARNING_PROPAGATION_ROADMAP_2026-08-05.md` at `3b8781b3b`.
- GC-018: paired GLP-T0 baseline.
- Active state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V54_2026-08-05.md`.

## Agent Roles

- Dispatcher: orchestrator role.
- Worker: documentation and source-verification worker.
- Reviewer/closer: independent from the worker.
- Commit owner: reviewer/closer only after acceptance.

## Scope / Target / Owner Boundary

Allowed scope is read-only provenance inspection plus exactly:

- `docs/audits/CVF_GLP_T0_WORKSPACE_GOVERNANCE_LEARNING_PROPAGATION_AUDIT_2026-08-05.md`
- `docs/reviews/CVF_GLP_T0_WORKSPACE_GOVERNANCE_LEARNING_PROPAGATION_AUDIT_WORKER_RETURN_2026-08-05.md`

Forbidden scope includes every bootstrap, catalog, profile, template, source,
test, checker, hook, session-state, workspace, downstream, and public-sync path.
No provider/network call, push, deployment, or live proof is authorized.

Risk ceiling: R1 documentation and local read-only evidence.

## Dependency Release Evidence

| Dependency | Evidence | Commit | Disposition |
|---|---|---|---|
| GLP-R0 roadmap | `docs/roadmaps/CVF_WORKSPACE_GOVERNANCE_LEARNING_PROPAGATION_ROADMAP_2026-08-05.md` | `3b8781b3b` | ACCEPT |
| continuity route and worker execution base | active state and handoff | `9acec42b5` | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`source audit`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

## Required First Reads

Read the roadmap, paired baseline, active startup surfaces, guard orientation,
literal gotchas, all Source Verification files, and output-artifact checkers.

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 9acec42b5 --head HEAD
```

All must pass with an isolated worktree before material worker edits.

## Source Verification Block

The paired GC-018 Source Verification Block is incorporated by reference. The
worker must re-run every cited search and record fresh evidence in the audit.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | operator accepted a bounded local source audit |
| scope classification | documentation-only, two changed paths, R1 blast radius |
| risk sensitivity | no public-sync, provider/live, secret, legal, production, or readiness action |
| selected role route | route mode `MULTI_AGENT_MULTI_ROLE` |
| role separation basis | orchestrator dispatches, worker audits, independent reviewer/closer decides |
| escalation condition | stop for forbidden scope, external effect, public/private ambiguity, or missing authority |

## New Doc-Only Fields

| Field | Meaning |
|---|---|
| authorityClass | provenance, public core, workspace root, rule pack, or project |
| carrierStatus | full owner, pointer only, equivalent carrier, or absent |
| alternativeCost | recurring governance and maintenance cost |
| T0Decision | exactly one allowed decision token |

## Execution Plan

1. Capture execution base and clean status.
2. Resolve initializer, synchronizer, catalog, and profile chain from source.
3. Build exact selected-artifact inventories for relevant profiles.
4. Compare learning owners, pointers, carriers, and project template.
5. Compare four cheap alternatives and governance cost.
6. Write the audit, then worker return; run gates once after focused checks.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| GLP-T0 audit path | CREATE |
| GLP-T0 worker-return path | CREATE |

## Write Ownership

The worker owns only the two manifest paths and must leave both unstaged and
uncommitted. The reviewer owns accepted material conversion and any required
completion review.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| foundationChange | NONE |
| ownerSurface | existing roadmap, audit, and review families |
| newDurableFoundation | N/A with reason: T0 creates evidence only |
| indexOrRegistryChange | N/A with reason: no new foundation owner or registry entry |
| claimBoundary | no split, relocation, refactor, or durable foundation implementation |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Closure evidence | Status |
|---|---|---|---|
| authority chain map | execution steps 2-4 | audit chain matrix | SATISFIED |
| exact profile inventory | execution step 3 | audit inventory | SATISFIED |
| cheap alternatives | execution step 5 | audit alternative matrix | SATISFIED |
| one T0 decision | acceptance criteria | worker return plus independent review | SATISFIED |
| no T0 implementation | forbidden scope | Git changed-set evidence | SATISFIED |

## Worker Autonomy / No-Question Rule

Proceed without operator confirmation for all non-destructive allowed-scope
reads, evidence corrections, checker-shape repairs, and gate reruns. Escalate
only for real scope, risk, external-effect, secret/quota, commit-owner, or
destructive boundary changes.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> no-commit worker -> independent reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=ace02fda7; executionBaseHead=9acec42b5; closureBaseHead=9acec42b5 |
| changedSetScope(phase) | dispatch=paired packets; execution=two worker outputs; closure=accepted outputs; session sync=canonical continuity only |
| traceScope(phase, actor) | each actor records its own phase-local trace |
| commitOwner(phase) | dispatcher commits packets; worker must not commit; reviewer owns accepted material; steward owns continuity |
| crossBatchIsolation | one GLP-T0 batch on a clean worktree |
| nextMoveSurfaces | reviewer/closer updates only after accepted T0 decision |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_GLP_T0_WORKSPACE_GOVERNANCE_LEARNING_PROPAGATION_AUDIT_COMPLETION_2026-08-05.md` (optional; use only if worker return cannot safely carry reviewer disposition) |
| reviewerOwnedClosurePaths | audit and worker return, plus optional completion review when required |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing, derive exact audit and review headings, trace labels, no-commit
fields, epistemic fields, learning disposition, and public-export requirements
from the applicable checker sources.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_GLP_T0_WORKSPACE_GOVERNANCE_LEARNING_PROPAGATION_AUDIT_WORKER_RETURN_2026-08-05.md`

contractProfile: WORKER_RETURN_FAST_DOC_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

scopeClassification: DOCUMENTATION_AND_EVIDENCE_ONLY_NO_COMMIT

publicSyncDisposition: FORBIDDEN

liveRuntimeDisposition: FORBIDDEN

checkerMutationDisposition: FORBIDDEN

workerSelfSelection: FORBIDDEN

## Acceptance Criteria

- [x] exact chain and profile inventories are command-backed;
- [x] pointer, owner, carrier, and consumer are not conflated;
- [x] four cheap alternatives and governance cost are compared;
- [x] exactly one T0 decision is returned;
- [x] disagreement is retained for reviewer inspection;
- [x] worker initially changed only two allowed paths;
- [x] worker fast gate passes after reviewer corrections;
- [x] no commit was made by the worker.

## Review Gate

The independent reviewer recomputes catalog/profile membership, performs one
consolidated semantic review before repair, and applies the existing review-cost
stop rule. Gate PASS alone is not semantic acceptance.

## Evidence Requirements

- current command/result/path evidence for every decision-driving row;
- exact resolved profile tags and catalog membership counts;
- explicit supporting and contradicting evidence;
- actual pending Git status after both outputs exist;
- review-cost telemetry and no-commit statement.

## Closure Checklist

- [x] two required outputs exist; reviewer-owned closure repairs are disclosed;
- [x] acceptance criteria are resolved;
- [x] worker-return fast gate passes after final edit;
- [x] independent reviewer disposition is recorded;
- [x] material and continuity commits remain reviewer/steward owned.

## Operator Checkpoint

No repeated checkpoint applies inside GLP-T0. Operator authority is required
only for T1 implementation, public-sync, provider/network use, push, deployment,
or a real expansion of objective, risk, path class, or commit ownership.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for source contradiction, unexpected worktree
state, forbidden path need, public/private ambiguity that cannot be resolved
read-only, or any requirement exceeding R1.

## Verification Commands

```powershell
python -m json.tool workspace_overlay_catalog.json
python governance/compat/run_worker_return_fast_gate.py
git status --short --untracked-files=all
```

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | dispatch envelope placement, dependency evidence, source verification, autonomy, fulfillment manifest, handoff fields, reviewer conversion, worker-return contract, trace labels, and public-export token |
| gateRunPurpose | confirm source-verified dispatch readiness |
| claimBoundary | GLP-T0 no-commit documentation audit only |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a bounded carrier gap exists, but full owner-file
copying will not be the cheapest safe remedy.

Evidence Comparison Requirement: compare the prediction with exact source.

Contradiction Handling Requirement: preserve contrary evidence and narrow the claim.

Claim Update Requirement: return one allowed decision token.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | previously accepted downstream learning -> CVF-owned ADIF/review-cost owner -> local workspace propagation audit |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | GLP roadmap, baseline, work order, audit, and worker return |
| Disposition | ADAPT previously accepted learning into a CVF-owned propagation audit; no new external evidence intake |
| Claim boundary | current T0 evidence comes from CVF-owned local source; downstream remains non-authoritative and unchanged |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | GLP-T0 packet authoring, 2026-08-05 |
| Working directory | repository root |
| Command or tool surface | local reads, resolver, exact searches, apply_patch, dispatch gates |
| Target paths | paired GLP-T0 baseline and work order |
| Allowed scope source | operator continuation and GLP-R0 at `3b8781b3b` |
| Before status evidence | HEAD `ace02fda7`; clean worktree |
| After status evidence | paired dispatch packet pending commit |
| Diff evidence | `git diff --name-status` |
| Approval boundary | GLP-T0 dispatch only |
| Claim boundary | no worker execution or implementation |
| Agent type | dispatcher |
| Invocation ID | `glp-t0-packet-authoring-2026-08-05` |
| Expected manifest | paired GLP-T0 baseline and work order |
| Actual changed set | paired GLP-T0 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | GLP-T0 documentation/source audit |
| claimDisposition | N/A with reason: no runtime execution-control claim |
| receiptEvidence | N/A with reason: no runtime receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local file and Git evidence only |
| invocationBoundary | governed local document editing |
| interceptionBoundary | no shell, filesystem, provider, or agent interception claim |
| claimLanguage | dispatch-ready audit packet only |
| forbiddenExpansion | runtime, provider/live, public-sync, generated workspace mutation, downstream edit, push, and deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This work order authorizes only two uncommitted GLP-T0 documentation outputs.
It does not authorize implementation, external effects, worker commit, or T1+.
