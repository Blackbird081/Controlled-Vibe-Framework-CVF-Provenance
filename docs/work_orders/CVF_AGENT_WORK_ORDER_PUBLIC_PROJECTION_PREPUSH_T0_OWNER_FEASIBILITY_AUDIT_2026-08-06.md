# CVF Agent Work Order - Public Projection Pre-Push T0 Owner Feasibility Audit

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

Batch ID: CVF-PUBLIC-PROJECTION-PREPUSH-T0

dispatchBaseHead: `68fbd0442`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: REVIEWER_MUST_CAPTURE_AT_CLOSURE

Commit mode: WORKER_MUST_NOT_COMMIT

Worker: documentation and source-verification audit worker

Reviewer/closer: independent reviewer/closer

## Dispatch Prompt Envelope

Role: documentation and source-verification audit worker.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_PUBLIC_PROJECTION_PREPUSH_T0_OWNER_FEASIBILITY_AUDIT_2026-08-06.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: capture current `git rev-parse --short HEAD` before edits.

Current-time notes: no provider/network call, public mutation, secret use, or
checker implementation is authorized.

Do-not-misread notes: the public clone is read-only evidence; a profile mismatch
does not establish that a new profile has positive value.

Required first actions: complete startup acknowledgment, read the paired
baseline, guard orientation, literal gotchas, source-verification and finality
addenda, then capture HEAD and full Git status.

Return contract: create exactly the audit and worker return, leave both
uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON` with
changed paths, execution base, exact commands, gate results, and HEAD unchanged.

## Purpose

Recompute the public projection pre-push mismatch from current source and decide
whether a new projection-aware proof path has enough incremental coverage to
justify its recurring governance cost.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-PUBLIC-PROJECTION-PREPUSH-T0 --title "Public Projection Pre-Push Owner Feasibility Audit" --date 2026-08-06 --base 68fbd0442 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with exact two-output ownership, four-option comparison, reviewer independence, and no-build boundary |
| checkerReadAheadConfirmation | dispatch-quality, checker-read-ahead, structural, trace, handoff, lifecycle, ADIF, and prompt-envelope checker sources inspected |
| docOnlyNewFields | optionId; incrementalCoverage; projectionOwnership; recurringCost; T0Decision |
| claimBoundary | dispatch authoring only; no worker execution or implementation claim |

## Authority Chain

- Operator instruction: continue the roadmap on 2026-08-06 while avoiding
  repeated low-value approval waits.
- Predecessor evidence:
  `docs/reviews/CVF_GLP_PUBLIC_R1_GOVERNANCE_LATENCY_CARRIER_REFRESH_COMPLETION_2026-08-06.md`.
- GC-018:
  `docs/baselines/CVF_GC018_PUBLIC_PROJECTION_PREPUSH_T0_OWNER_FEASIBILITY_AUDIT_2026-08-06.md`.
- Active state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`.
- Active handoff: `AGENT_HANDOFF_V55_2026-08-05.md`.

Authority boundary: T0 evidence only. No later design or implementation is
released by a worker recommendation.

## Agent Roles

- Dispatcher: orchestrator role.
- Worker: documentation and source-verification audit worker.
- Reviewer/closer: agent independent from the worker recommendation.
- Commit owner: reviewer/closer only after acceptance.
- Operator approval required for: scope expansion, implementation, public
  mutation, provider/network use, push, destructive action, or higher risk.

## Scope / Target / Owner Boundary

Allowed scope:

- read current provenance sources and the sibling public projection;
- run local read-only inventory, Git, and documentation gate commands;
- create exactly the two fulfillment-manifest artifacts;
- repair formatting and evidence defects inside those two paths;
- compare options A-D and return exactly one allowed decision.

Forbidden scope:

- checker, hook, test, script, session, handoff, roadmap, registry, or catalog edits;
- any public clone edit, stage, commit, push, or remote mutation;
- provider/network calls, keys, live proof, deployment, or downstream edits;
- design implementation, specification implementation, or build work;
- weakening or replacing provenance pre-push coverage.

Risk ceiling: R1 documentation and local read-only evidence.

## Required First Reads

- `AGENTS.md`, session front doors, and active handoff for current authority.
- `docs/reference/guard_orientation/README.md` for task/role guard routing.
- `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
- paired baseline and predecessor completion review.
- the hook runner/catalog and public-sync projection source cited below.
- applicable checker sources listed in the read-ahead block.

## Pre-Flight Checks

```powershell
git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 68fbd0442 --head HEAD
```

Expected: worker captures a fresh execution base after the packet commit, the
worktree contains no unrelated changes, and pre-implementation passes. Repair
allowed-scope failures and rerun; stop if repair requires a forbidden path.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| named hook chain entrypoint | EXISTS | `governance/compat/run_local_governance_hook_chain.py` | lines 117-121 and 218-250 | `HOOK_CHAINS` | hook-chain runner | ACCEPT |
| generic pre-push mapping | VALUE_SET | `governance/compat/local_governance_hook_catalog.py` | lines 16-22 | `pre-push` | `HOOK_CHAINS` | ACCEPT |
| generic pre-push catalog | EXISTS | `governance/compat/local_governance_hook_catalog_pre_push.py` | line 6 | `PRE_PUSH_CHECKS` | pre-push catalog | ACCEPT |
| private-dependent checks in generic profile | VALUE_SET | `governance/compat/local_governance_hook_catalog_pre_push.py` | lines 259-263 and 408-415 | `PRE_PUSH_CHECKS` | pre-push catalog | ACCEPT |
| projection selection owner | EXISTS | `scripts/cvf-public-sync.ps1` | lines 37, 103, 118, 215, and 225 | `ALLOWED_TREES`; `MAPPED_FILES`; `WORKSPACE_KIT_FILES`; `Test-Denied`; `Get-AllowedFiles` | public-sync projection script | ACCEPT |
| separately authorized candidate finding | VALUE_SET | `docs/reviews/CVF_GLP_PUBLIC_R1_GOVERNANCE_LATENCY_CARRIER_REFRESH_COMPLETION_2026-08-06.md` | Finding-To-Governance row at line 131 | `PUBLIC_PROJECTION_GATE_PROFILE_MISMATCH` | completion review | ACCEPT |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: the worker must derive decision evidence from the current
execution worktree and current read-only public projection, not reuse the
dispatcher inventory as completion proof.

unicodePathHandling: use literal repo-relative paths and UTF-8-safe readers;
the repository root contains spaces but the planned output paths are ASCII.

extractedTextAuthority: N/A with reason: no extracted external text is used.

freshRecomputeRequired: YES

## Current Runtime Freshness Verification

Dispatcher evidence at provenance `68fbd0442` and public `9b039ea6b` found the
generic runner/catalog in both projections and found no public
`CVF_SESSION_MEMORY.md` or `CVF_SESSION/ACTIVE_SESSION_STATE.json`. The worker
must recompute path presence and must distinguish intentional projection
absence from a material coverage gap.

## Negative Search And Collision Discipline

Search current provenance source, tests, docs, and public projection for any
existing public-specific profile or focused equivalent. Report exact commands,
roots, partial matches, and semantic collisions. Do not use a source-not-found
disposition unless the full search is command-backed.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039,
ADIF-0043, ADIF-0049, ADIF-0006.

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 30 --json`

Disclosure count: 20. This packet avoids the returned patterns through exact
path inventories, source-backed commands, explicit role separation, current
Git evidence, and a forbidden protected-path manifest.

## Intake Role Routing Decision

| Field | Value |
| --- | --- |
| intake summary | bounded local feasibility audit of an accepted profile mismatch |
| scope classification | documentation and evidence only, two output paths, R1 |
| risk sensitivity | no public mutation, provider/live, secret, production, or runtime action |
| selected role route | MULTI_AGENT_MULTI_ROLE |
| role separation basis | dispatcher authors packet, worker audits, independent reviewer decides and commits |
| escalation condition | source contradiction, forbidden path need, external effect, or risk/claim expansion |

## Worker Autonomy / No-Question Rule

Proceed without operator confirmation for every non-destructive read, exact
inventory, evidence correction, formatting repair, and gate rerun inside
Allowed scope. Do not create approval latency for routine in-scope work.
Escalate only for a real boundary change listed in Agent Roles.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
| --- | --- |
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> no-commit worker -> independent reviewer/closer -> optional session-sync steward |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, optional SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=68fbd0442; executionBaseHead=WORKER_MUST_CAPTURE_AT_START; closureBaseHead=REVIEWER_MUST_CAPTURE_AT_CLOSURE |
| changedSetScope(phase) | dispatch=paired packet; execution=two outputs; closure=accepted outputs and reviewer-owned status conversion; session sync=only if next move changes |
| traceScope(phase, actor) | every actor records phase-local commands, paths, status, and claim boundary |
| commitOwner(phase) | dispatcher commits packet; worker must not commit; reviewer owns accepted material; steward owns any later continuity sync |
| crossBatchIsolation | one T0 batch on a clean provenance worktree; public clone remains read-only and clean |
| Before status evidence | provenance and public worktrees were clean at dispatch authoring; worker must recheck before execution |
| nextMoveSurfaces | reviewer updates next-move surfaces only after accepted T0 decision and only in a separate authorized closure/sync batch |

## Reviewer Closure Conversion

completionReviewPath:
`docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T0_OWNER_FEASIBILITY_AUDIT_COMPLETION_2026-08-06.md`

reviewerOwnedClosurePaths:

- this work order;
- the audit and worker-return paths;
- the completion review;
- paired baseline status only if reviewer acceptance requires conversion.

pendingStatusTokensAllowedBeforeReview: COMPLETE_PENDING_REVIEW,
IMPLEMENTATION_COMPLETE_PENDING_REVIEW, DRAFT, HOLD_*

forbiddenClosedEquivalentResidue: COMPLETE_PENDING_REVIEW,
NOT_EXECUTED_YET, WORKER_RETURNS_PENDING, PRE_CLOSURE_NOT_RUN,
FAIL_EXPECTED_PENDING_FINALITY, DISPATCHED as current status

predecessorClosureFactSource: GLP-PUBLIC-R1 completion review, not mutable
active-session current mode

closureOwner: independent reviewer/closer

workerCommitPermission: FORBIDDEN

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
| --- | --- |
| `docs/audits/CVF_PUBLIC_PROJECTION_PREPUSH_T0_OWNER_FEASIBILITY_AUDIT_2026-08-06.md` | CREATE |
| `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T0_OWNER_FEASIBILITY_AUDIT_WORKER_RETURN_2026-08-06.md` | CREATE |

## Write Ownership

The worker owns only the two fulfillment-manifest paths in create-only mode and
must leave them unstaged and uncommitted. The reviewer owns the completion
review and any accepted status conversion. Every other path is forbidden.

## Execution Plan

1. Capture execution HEAD and full Git status; stop on unrelated dirt.
2. Recompute generic pre-push check inventory and classify each check owner.
3. Recompute public projection presence/absence and existing focused proof.
4. Compare options A-D on incremental coverage, latency, maintenance, drift,
   false confidence, and provenance-boundary safety.
5. Identify a source-backed owner/test boundary only if option C wins.
6. Write the audit using supporting and contradicting evidence.
7. Scaffold and complete the worker return, then run the exact fast gate once
   after final edits and return without commit.

## Worker Output Checker Read-Ahead Mandate

Before writing the audit and review output, inspect checker source for each path
family and conditional finding class. The review must contain Target, Scope,
Findings, Risk / Corrective Action, Decision, External Knowledge Intake
Routing, Epistemic Process Block, operation trace, learning disposition, and
public export disposition sections. Use the Fast Doc scaffold before long prose.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T0_OWNER_FEASIBILITY_AUDIT_WORKER_RETURN_2026-08-06.md`

contractProfile: WORKER_RETURN_FAST_DOC_V1

scopeClassification: DOCUMENTATION_AND_EVIDENCE_ONLY_NO_COMMIT

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

publicSyncDisposition: FORBIDDEN

liveRuntimeDisposition: FORBIDDEN

checkerMutationDisposition: FORBIDDEN

workerSelfSelection: FORBIDDEN

## Evidence Requirements

- current exact check inventory with ownership rationale;
- current public path-presence inventory and exact focused proof commands;
- normalized four-option comparison and recurring governance cost;
- supporting and contradicting evidence for the selected decision;
- actual `git status --short --untracked-files=all` after both outputs exist;
- complete operation trace and no-commit statement.

## Acceptance Criteria

- [ ] generic pre-push checks are inventoried and ownership-classified;
- [ ] intentional projection absence is separated from uncovered risk;
- [ ] existing focused proof and coverage limits are source-backed;
- [ ] all four cheap alternatives and governance cost are compared;
- [ ] provenance pre-push coverage is not weakened or redefined;
- [ ] exactly one allowed T0 decision is returned;
- [ ] supporting and contradicting evidence are preserved;
- [ ] only the two worker-owned paths are changed;
- [ ] worker fast gate passes and the worker makes no commit.

Fail conditions: invented command signatures, missing source owners, ambiguous
coverage claims, public/provenance boundary errors, forbidden runtime/security
claims, or any changed path outside worker ownership.

## Review Gate

The independent reviewer recomputes at least one sample from each ownership
class and the decision-driving coverage gap. The reviewer must reject a new
profile recommendation that lacks a named uncovered risk, stable owner,
focused test boundary, and lower expected cost than the existing proof path.

## Closure Checklist

- [ ] two required outputs exist and no other worker path changed;
- [ ] every acceptance item is resolved or blocked with action;
- [ ] worker-return fast gate passes after the last edit;
- [ ] worker leaves artifacts pending and does not claim pre-closure PASS;
- [ ] independent reviewer records semantic disposition;
- [ ] committed-range pre-closure remains reviewer/committer work;
- [ ] continuity changes, if any, remain a separate authorized sync.

## Operator Checkpoint

The operator's continuation instruction releases packet authoring and this
bounded T0 audit. No repeated same-scope confirmation applies. Fresh operator
authority is required only for implementation, public mutation/push,
provider/network use, higher risk, destructive action, or broader ownership.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for source contradiction, unrelated dirty state,
forbidden path need, public/private ambiguity that cannot be resolved read-only,
or any requirement exceeding R1. Routine in-scope gate repair is not a return
condition.

## Verification Commands

```powershell
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T0_OWNER_FEASIBILITY_AUDIT_WORKER_RETURN_2026-08-06.md --title "Public Projection Pre-Push T0 Owner Feasibility Audit Worker Return" --profile WORKER_RETURN_FAST_DOC_V1
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git diff --name-status
git status --short --untracked-files=all
```

## Roadmap-To-Work-Order Trace Matrix

| Predecessor requirement | Work-order instruction | Output evidence | Status |
| --- | --- | --- | --- |
| separately authorize candidate | paired T0 baseline and this packet | committed dispatch packet | SATISFIED |
| avoid premature checker change | forbidden scope | exact changed-set evidence | SATISFIED |
| test cheap alternatives first | execution step 4 | normalized option matrix | SATISFIED |
| preserve provenance authority | acceptance and review gates | ownership inventory and claim boundary | SATISFIED |
| retain as future candidate only if valuable | one decision token | worker return plus independent review | SATISFIED |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | provenance-local audit and read-only public projection inspection | two uncommitted documentation outputs only | source, Git, and local gate evidence | local command/file boundary | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external adapter in T0 | no authentication, approval, mutation, receipt, or provider authority | N/A with reason: no external interface is required | no CLI/MCP adapter is designed or invoked | N/A_WITH_REASON |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_dispatch_packet_lifecycle_hygiene.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_dispatch_prompt_envelope.py` |
| literalTokensReviewed | dispatch envelope fields, source table columns, ADIF query line, route tokens, handoff fields, reviewer conversion, Fast Doc terms, trace labels, structural groups, and public disposition |
| gateRunPurpose | confirm source-verified dispatch readiness after the packet scope was written |
| claimBoundary | structural confirmation only; no worker result or semantic decision |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: existing focused public proof plus authoritative
provenance pre-push may be the lowest-cost adequate control.

Evidence Comparison Requirement: compare exact current source and proof output
against the prediction.

Contradiction Handling Requirement: preserve evidence for a material uncovered
risk, a safer thin profile, or no stable owner.

Claim Update Requirement: confirm, narrow, revise, or invalidate the prediction
and return exactly one allowed decision.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Public/simple CVF vocabulary |
| Chain map route | completion finding -> provenance source verification -> bounded T0 audit -> independent review -> optional later packet |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired provenance baseline, work order, audit, worker return, and completion review |
| Disposition | ADAPT as a feasibility question; do not promote the public clone or finding as a proven implementation need |
| Claim boundary | provenance remains authoritative; no autonomous checker, public, downstream, provider, runtime, or session mutation |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | dispatcher role |
| Provider or surface | local private provenance repository and read-only sibling public projection |
| Session or invocation | CVF-PUBLIC-PROJECTION-PREPUSH-T0 packet authoring, 2026-08-06 |
| Working directory | provenance repository root; public sibling inspected read-only |
| Command or tool surface | local source reads, Git inspection, ADIF resolver, scaffold stdout, apply_patch, governance gates |
| Target paths | paired T0 baseline and work order |
| Allowed scope source | operator continuation and accepted GLP-PUBLIC-R1 completion finding |
| Before status evidence | clean worktree in provenance at HEAD `68fbd0442`; clean worktree in public projection with HEAD equal to origin/main `9b039ea6b` |
| After status evidence | paired dispatch packet pending commit |
| Diff evidence | `git diff --name-status` before commit |
| Approval boundary | bounded T0 documentation/source audit dispatch only |
| Claim boundary | no checker, hook, public, provider, network, runtime, or session mutation |
| Agent type | dispatcher |
| Invocation ID | `cvf-public-projection-prepush-t0-dispatch-2026-08-06` |
| Expected manifest | paired T0 baseline and work order |
| Actual changed set | paired T0 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | T0 local documentation/source feasibility audit |
| claimDisposition | CLAIM_REJECTED: no execution-control or runtime-enforcement behavior is claimed |
| receiptEvidence | N/A with reason: no runtime receipt is created |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local file, command, and Git evidence only |
| invocationBoundary | governed local document editing and read-only inspection |
| interceptionBoundary | no IDE, shell, filesystem, provider, agent, wrapper, or proxy interception claim |
| claimLanguage | dispatch-ready feasibility audit packet only |
| forbiddenExpansion | checker/hook implementation, public mutation, runtime/provider/live, downstream edit, push, deployment, and T1+ |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | reviewer converts status only following semantic acceptance | N/A with reason: pending execution |
| Completion or reviewer artifact | completion review path in reviewer conversion | final decision and committed-range evidence | N/A with reason: reviewer owned |
| Roadmap state | N/A with reason: standalone bounded follow-up to a completion finding | no roadmap mutation | N/A with reason |
| Registry JSON | N/A with reason: no corpus or runtime registry changes | no registry mutation | N/A with reason |
| Registry Markdown | N/A with reason: no corpus registry changes | no registry mutation | N/A with reason |
| External evidence digest | N/A with reason: no external intake or mutable external evidence | public clone path facts are recomputed read-only | N/A with reason |
| System loop interlock | completion finding -> T0 audit -> reviewer decision | explicit route, no autonomous mutation | N/A with reason: documentation route only |
| Session continuity | canonical continuity surfaces | separate reviewer/steward decision following accepted review | N/A with reason: not worker owned |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this private work order authorizes no public artifact or public-sync
action.

## Claim Boundary

This work order authorizes only two uncommitted documentation outputs and their
local evidence. It does not authorize implementation, a gate-profile claim,
public mutation, provider/network use, live proof, downstream edit, commit,
push, deployment, or T1+.
