# CVF Agent Work Order - GLP T1 Workspace Governance Learning Carrier Design

## Dispatch Prompt Envelope

Role: documentation and source-verification design worker.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_GLP_T1_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_DESIGN_2026-08-05.md`

Paired baseline: `docs/baselines/CVF_GC018_GLP_T1_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_DESIGN_2026-08-05.md`

dispatchBaseHead: `bdc6540ca`

executionBaseHead: CURRENT_HEAD_AT_WORKER_START

closureBaseHead: REVIEWER_TO_SET_AFTER_RETURN

Commit mode: WORKER_MUST_NOT_COMMIT

Current-time notes: packet authored 2026-08-05 from provenance HEAD
`bdc6540ca`; worker must capture current HEAD immediately before pre-flight.

Do-not-misread notes: this is design evidence, not permission to create or edit
a carrier, catalog entry, profile, template, bootstrap, workspace, or project.

Required first actions: complete startup acknowledgment, capture HEAD/status,
read roadmap/T0/baseline/current candidate owners/checkers, then run the
pre-implementation gate against the captured current HEAD before writing.

Return contract: create exactly the design audit and worker return, leave both
uncommitted, and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_WITH_CORRECTIONS

docType: work_order

Date: 2026-08-05

Batch ID: GLP-T1

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GLP-T1 --title "Workspace Governance Learning Carrier Design" --date 2026-08-05 --base bdc6540ca --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic worker dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with GLP-T1 carrier candidates, design schema, two-output manifest, and no-implementation boundary |
| checkerReadAheadConfirmation | dispatch-quality, prompt-envelope, handoff, ADIF, trace, structural, worker-return, Delta, foundation-layout, and public-disposition checkers |
| docOnlyNewFields | carrierOwnerPath; carrierForm; publicSafeContentBoundary; profileExposure; propagationConsumer; implementationProofPlan |
| claimBoundary | dispatch authoring only; no design execution or implementation |

## Purpose

Independently select or reject the smallest safe carrier design for the
governance-latency learning confirmed by GLP-T0.

## Authority Chain

- Operator authority: accepted continued execution of the GLP roadmap.
- Roadmap: `docs/roadmaps/CVF_WORKSPACE_GOVERNANCE_LEARNING_PROPAGATION_ROADMAP_2026-08-05.md`.
- Accepted prerequisite: GLP-T0 material commit `60884f5c0`, decision
  `PROCEED_DOC_ONLY`.
- GC-018: paired GLP-T1 baseline.
- Active state and handoff route packet authoring only until this dispatch is
  committed and synchronized.

## Agent Roles

- Dispatcher: orchestrator role.
- Worker: documentation and source-verification design worker.
- Reviewer/closer: independent from the worker.
- Commit owner: reviewer/closer only after acceptance.

## Scope / Target / Owner Boundary

Allowed writes are exactly:

- `docs/audits/CVF_GLP_T1_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_DESIGN_2026-08-05.md`
- `docs/reviews/CVF_GLP_T1_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_DESIGN_WORKER_RETURN_2026-08-05.md`

All carrier, reference, catalog, profile, template, bootstrap, source, test,
checker, hook, session-state, workspace, downstream, and public-sync paths are
read-only. No provider/network call, push, deployment, or live proof is allowed.

Risk ceiling: R1 documentation and local read-only design evidence.

## Dependency Release Evidence

| Dependency | Evidence | Commit | Disposition |
|---|---|---|---|
| GLP-T0 accepted evidence | audit plus independent reviewer addendum | `60884f5c0` | ACCEPT |
| GLP roadmap T1 objective | Work Plan row and post-T0 next move | `60884f5c0` | ACCEPT |
| continuity route | active state and handoff | `bdc6540ca` | ACCEPT |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`design specification`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Command: `python governance/compat/run_adif_defect_resolver.py --task-class "design specification" --role dispatcher --lifecycle-phase pre-dispatch --json`

## Required First Reads

Read the roadmap, paired baseline, T0 audit/reviewer return, startup and guard
front doors, literal gotchas, every Source Verification file, worker-return
checker, and dispatch-quality checker before authoring outputs.

## Pre-Flight Checks

```powershell
$glpT1ExecutionBase = git rev-parse --short HEAD
git status --short --untracked-files=all
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base $glpT1ExecutionBase --head HEAD
```

Run before material worker edits. HEAD must be the captured execution base and
status must be clean. Record the concrete SHA in both worker outputs.

## Source Verification Block

The paired GC-018 Source Verification Block is incorporated by reference. The
worker must repeat every catalog/path/section check and correct stale facts.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | accepted T0 evidence releases a bounded carrier-design comparison |
| scope classification | documentation-only, two changed paths, R1 blast radius |
| risk sensitivity | public/private content design matters; no mutation or external action |
| selected role route | route mode `MULTI_AGENT_MULTI_ROLE` |
| role separation basis | dispatcher authors packet, worker designs, independent reviewer/closer decides |
| escalation condition | stop for unsafe content, missing owner, forbidden edit, external effect, or authority expansion |

## New Doc-Only Fields

| Field | Meaning |
|---|---|
| carrierOwnerPath | one canonical existing or proposed owner path |
| carrierForm | existing-owner amendment or new compact carrier |
| publicSafeContentBoundary | exact included semantics and excluded private evidence |
| profileExposure | exact catalog tags and profile consumers proposed for T2 |
| propagationConsumer | workspace/project surface that must read the carrier |
| implementationProofPlan | bounded T2 paths, positive tests, negative leakage tests, rollback |

## Execution Plan

1. Capture execution base and clean status; run pre-implementation once.
2. Reproduce current catalog membership for all four carrier candidates.
3. Extract exact source-backed semantics from ADIF-0026, review-cost, Fast Doc,
   governance control index, R72C/R84, and guard orientation.
4. Build one decision rubric covering fit, discoverability, public safety,
   duplication, drift cost, profile reach, consumer reach, and rollback.
5. Select one owner or stop; specify exact content and exclusion boundary.
6. Specify a bounded T2 changed-set and focused deterministic proof plan without
   editing any proposed implementation path.
7. Write the audit and worker return; run the worker-return fast gate once after
   focused corrections.

## Required Design Schema

| Field | Required answer |
|---|---|
| selectedCandidate | guard orientation, control matrix, downstream template, compact carrier, or none |
| carrierOwnerPath | one exact path or `N/A with reason` when stopping |
| semanticFit | why the owner is the right operational decision point |
| includedSemantics | exact short rules, not references to private context |
| excludedEvidence | exact private/provenance details forbidden from distribution |
| catalogDisposition | reuse existing entry, add one entry in T2, or no change |
| profileExposure | exact tags and derived profile reach |
| projectConsumer | exact generated workspace/project read path |
| driftOwner | source owner and trigger for carrier refresh |
| T2AllowedPaths | proposed bounded implementation manifest |
| positiveProof | deterministic expected-inclusion assertions |
| negativeProof | private leakage and unrelated-profile exclusion assertions |
| rollback | exact revert/removal behavior |
| exitRecommendation | one allowed T1 token |

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| GLP-T1 carrier-design audit path | CREATE |
| GLP-T1 carrier-design worker-return path | CREATE |

## Write Ownership

The worker owns only the two manifest paths and leaves both unstaged and
uncommitted. The reviewer owns accepted conversion and any optional completion
review required by a real unresolved disagreement.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| foundationChange | NONE |
| ownerSurface | existing roadmap, audit, and review families |
| newDurableFoundation | N/A with reason: T1 only compares and specifies a carrier |
| indexOrRegistryChange | N/A with reason: no owner, catalog, or registry is changed in T1 |
| claimBoundary | no split, relocation, refactor, carrier creation, or durable implementation |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Closure evidence | Status |
|---|---|---|---|
| smallest safe carrier | execution steps 2-5 and design schema | candidate decision matrix | SATISFIED |
| existing owner preferred when fit | four-candidate comparison | semantic-fit and cost rows | SATISFIED |
| exact public/private boundary | design schema | included/excluded ledger | SATISFIED |
| one T1 decision | acceptance criteria | worker return plus independent review | SATISFIED |
| no T1 implementation | scope and forbidden paths | Git changed-set evidence | SATISFIED |

## Worker Autonomy / No-Question Rule

Proceed without operator confirmation for all non-destructive allowed-scope
reads, evidence corrections, design comparisons, checker-shape repairs, and
gate reruns. Escalate only for a real scope, public/private ambiguity, external
effect, secret/quota, commit-owner, or destructive boundary change.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | dispatcher -> no-commit worker -> independent reviewer/closer -> session-sync steward |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatchBaseHead=bdc6540ca; executionBaseHead=current HEAD captured before edits; closureBaseHead=reviewer captures worker-return base |
| changedSetScope(phase) | dispatch=paired packets; execution=two worker outputs; closure=accepted outputs and bounded reviewer repairs; session sync=canonical continuity only |
| traceScope(phase, actor) | each actor records its own phase-local trace |
| commitOwner(phase) | dispatcher commits packets; worker must not commit; reviewer owns accepted material; steward owns continuity |
| crossBatchIsolation | one GLP-T1 batch on a clean worktree |
| nextMoveSurfaces | reviewer/closer updates only after accepted T1 decision |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_GLP_T1_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_DESIGN_COMPLETION_2026-08-05.md` (optional; use only for unresolved disagreement) |
| reviewerOwnedClosurePaths | design audit and worker return, plus optional completion review when required |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_GLP_T1_WORKSPACE_GOVERNANCE_LEARNING_CARRIER_DESIGN_WORKER_RETURN_2026-08-05.md`

contractProfile: WORKER_RETURN_FAST_DOC_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

scopeClassification: DOCUMENTATION_AND_EVIDENCE_ONLY_NO_COMMIT

publicSyncDisposition: FORBIDDEN

liveRuntimeDisposition: FORBIDDEN

checkerMutationDisposition: FORBIDDEN

workerSelfSelection: FORBIDDEN

## Worker Output Checker Read-Ahead Mandate

Before writing, derive exact design-audit and worker-return headings, trace
labels, no-commit fields, epistemic fields, learning disposition, and public-
export requirements from current checker sources.

The worker return must use `## Conditional Controls Disposition` with
`conditionalControlsDisposition: EKI_NA; RIH_NA; CCRI_NA`. This is the compact
N/A instruction for External Knowledge Intake Routing, Rescan Intelligence
Hardening, and Corpus Completeness And Report Integrity; the worker must not
add the three full conditional headings unless evidence makes one applicable.

## Acceptance Criteria

- [x] current membership and profile reach are command-backed;
- [x] all four candidates receive the same decision rubric;
- [x] selected owner and semantic fit are exact;
- [x] included and excluded content boundaries are explicit;
- [x] T2 paths, tests, leakage negatives, drift owner, and rollback are bounded;
- [x] exactly one T1 exit recommendation is returned;
- [x] only two worker paths were pending at worker return;
- [x] worker-return fast gate passes;
- [x] worker makes no commit.

## Review Gate

The independent reviewer recomputes candidate membership and profile exposure,
challenges semantic fit and public-safety exclusions, then performs one
consolidated repair batch. Gate PASS alone is not semantic acceptance.

## Evidence Requirements

- current command/result/path evidence for every decision-driving row;
- supporting and contradicting evidence for every candidate;
- exact included/excluded content ledger;
- exact proposed T2 changed-set and proof matrix;
- actual pending Git status, review-cost telemetry, and no-commit statement.

## Closure Checklist

- [x] two required outputs exist and no other worker path changed;
- [x] acceptance criteria are resolved;
- [x] worker-return fast gate passes after final worker edit;
- [x] independent reviewer disposition is recorded;
- [x] material and continuity commits remain reviewer/steward owned.

## Operator Checkpoint

No repeated checkpoint applies inside GLP-T1. Fresh operator authority is
required before GLP-T2 implementation, public-sync, provider/network use, push,
deployment, or a real expansion of objective, risk, path class, or ownership.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for unsafe content, missing canonical owner,
unexpected worktree state, forbidden path need, external effect, or authority
above R1 design evidence.

## R1 Focused Redispatch - Consumer Chain Repair

Reviewer decision: `REVIEW_CHANGES_REQUIRED_R1`.

The same no-commit worker must revise only the existing design audit and worker
return. Do not create another artifact and do not edit any implementation path.

Required corrections:

1. Replace the false generated path `.cvf-rule-pack/...` with the source-backed
   default `CVF_RULE_PACKS/<profile>/source/...` path.
2. Separate `copiedToWorkspaceRulePack` from `mandatoryProjectConsumer`.
   `docs/reference/CVF_WORKSPACE_RULES.md` states that rule packs do not replace
   project `AGENTS.md`, manifests, policies, or handoffs; the generated project
   manifest's `requiredDocs` list does not include guard orientation.
3. Re-score all four candidates against the roadmap's full terminal chain:
   `workspace guidance -> project bootstrap/adoption`. The originating operator
   finding was a downstream project repeating governance-latency behavior, so
   downstream project agents are an in-scope audience, not a wrong audience.
4. Treat broad project reach as a safety question to classify, not as automatic
   disqualification. Determine whether the five provider-neutral operational
   rules are public-safe; absence of a Public Export Disposition in a candidate
   is not safety proof.
5. Correct active-Markdown maintainability evidence to advisory `> 900` and
   hard `> 1200` lines.
6. Select one canonical carrier only if the consumer chain is mandatory and
   source-backed. If the downstream AGENTS template is selected, specify the
   exact public-safe subsection, existing-project refresh behavior, T2 path/test
   manifest, negative private-leakage assertions, and rollback. If no single
   owner can satisfy both workspace and project consumption without duplication,
   return `STOP_NO_SAFE_CARRIER`.
7. Preserve the original guard-orientation recommendation and every reviewer
   disagreement in the audit and return; do not rewrite history as first-pass
   agreement.

R1 remains documentation-only and `WORKER_MUST_NOT_COMMIT`. The worker runs the
pre-implementation gate from current HEAD before edits and the worker-return
fast gate once after the consolidated correction.

## Verification Commands

```powershell
git status --short --untracked-files=all
python governance/compat/run_worker_return_fast_gate.py
git diff --check
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | accepted T0 evidence -> current CVF carrier owners -> bounded T1 design comparison |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | GLP roadmap, T0 evidence, T1 baseline, work order, design audit, and worker return |
| Disposition | ADAPT accepted CVF-owned learning into a carrier design; no new external intake or authority promotion |
| Claim boundary | all T1 decision evidence comes from current local CVF sources; downstream remains non-authoritative and unchanged |

## Finding-To-Governance Learning Disposition

The propagation gap is already owned by the GLP roadmap and accepted T0
evidence. T1 must record any new repeated/non-obvious execution defect in ADIF,
but must not duplicate the existing `PHASE_GATE_PLACEMENT_GAP` finding.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | prompt-envelope fields, Source Verification schema, ADIF query, Fast Doc terms, handoff route, trace fields, conditional-control dispositions, and decision tokens |
| gateRunPurpose | confirm dispatch shape after source-backed design requirements were written |
| claimBoundary | GLP-T1 no-commit design dispatch only |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: an existing distributed owner may be cheaper than
a new carrier, but only if it can hold self-contained semantics at the point of
action without becoming an overloaded index or template.

Evidence Comparison Requirement: apply one rubric to all four candidates and
retain evidence against the selected candidate.

Contradiction Or Gap Disposition: stop if every candidate either duplicates
ownership, leaks private evidence, lacks discoverability, or has excessive
maintenance cost.

Claim Update Requirement: accept one bounded design or return
`STOP_NO_SAFE_CARRIER`.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | GLP-T1 documentation/source design only |
| claimDisposition | N/A with reason: no runtime execution-control claim is made |
| receiptEvidence | N/A with reason: no runtime receipt is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local file reads, catalog/profile queries, and Git evidence only |
| invocationBoundary | governed local document analysis |
| interceptionBoundary | no shell, filesystem, provider, or agent interception claim |
| claimLanguage | source-verified design recommendation only |
| forbiddenExpansion | carrier implementation, runtime, provider/live, public-sync, generated workspace, downstream, push, deployment |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher |
| Provider or surface | local private provenance repository |
| Session or invocation | GLP-T1 work-order authoring, 2026-08-05 |
| Working directory | repository root |
| Command or tool surface | local reads, catalog queries, ADIF resolver, apply_patch, pre-dispatch gates |
| Target paths | paired GLP-T1 baseline and work order |
| Allowed scope source | GLP roadmap plus accepted T0 at `60884f5c0` |
| Before status evidence | HEAD `bdc6540ca`; clean worktree |
| After status evidence | paired GLP-T1 packet pending dispatcher commit |
| Diff evidence | exact two-path `git diff --name-status` |
| Approval boundary | documentation-only design dispatch |
| Claim boundary | no design execution, implementation, workspace/downstream/public mutation, or external effect |
| Agent type | dispatcher |
| Invocation ID | `glp-t1-work-order-authoring-2026-08-05` |
| Expected manifest | paired GLP-T1 baseline and work order |
| Actual changed set | paired GLP-T1 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This work order authorizes only two local no-commit design artifacts. It does
not authorize carrier/catalog/profile/template/bootstrap implementation,
generated workspace or downstream edits, provider/network use, public-sync,
push, deployment, or production claims.
