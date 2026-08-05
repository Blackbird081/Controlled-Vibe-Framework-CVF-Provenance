# CVF Agent Work Order - GLP T3 Disposable Fresh Workspace Propagation Proof

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: work_order

Date: 2026-08-05

Batch ID: GLP-T3

dispatchBaseHead: `34dfbdb0c`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_TO_SET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

Role: bounded local propagation-proof worker.

Commit mode: `WORKER_MUST_NOT_COMMIT`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_GLP_T3_DISPOSABLE_FRESH_WORKSPACE_PROPAGATION_PROOF_2026-08-05.md`

Paired baseline: `docs/baselines/CVF_GC018_GLP_T3_DISPOSABLE_FRESH_WORKSPACE_PROPAGATION_PROOF_BASELINE_2026-08-05.md`

Current-time notes: released from clean provenance HEAD `34dfbdb0c` after
GLP-T2R1 independently closed at material commit `f59457b9a`; operator release
is recorded on 2026-08-05.

Do-not-misread notes: this packet releases one no-commit proof worker only after
the committed non-empty release range passes pre-dispatch. It never authorizes
source edits, persistent downstream mutation, provider/network use, public
sync, or worker commit.

Required first actions: after release, complete startup acknowledgment; capture
HEAD and clean status; read this packet, baseline, roadmap, T2R1 completion,
harness, template, helper support source, guard orientation, literal gotchas,
and checker sources; run pre-implementation from the captured base.

Return contract: run the existing harness once, create exactly the audit and
worker return, leave both uncommitted, and return `COMPLETE_PENDING_REVIEW` or
`BLOCKED_WITH_REASON`.

## Purpose

Prove, without implementation changes, that the accepted governance-latency
carrier propagates into a disposable fresh workspace with the expected
manifest/artifacts, zero private leakage, and complete cleanup.

## Required First Reads

- startup front doors and active handoff;
- guard orientation and governed-artifact literal gotchas;
- this work order, paired baseline, GLP roadmap, and T2R1 completion review;
- golden harness, support library, bootstrap CP1 source, and downstream AGENTS
  template;
- checker sources listed in the read-ahead block.

## Pre-Flight Checks

- explicit release and committed non-empty dispatch range;
- pre-dispatch PASS and clean captured execution base;
- both output paths absent before execution;
- provider/network count fixed at zero;
- existing disposable cleanup guard present and unchanged.

## Write Ownership

The worker may create only the audit and worker return in the Required Artifact
Manifest. The worker may not edit an existing file, stage, commit, push, or
update continuity. The reviewer/closer owns accepted closure conversion.

## Authority Chain

| Authority layer | Evidence | Disposition |
|---|---|---|
| roadmap authority | GLP roadmap T3 row | proof tranche defined |
| predecessor release | T2R1 completion at `f59457b9a` | ACCEPT |
| packet-authoring authority | active session next move | ACCEPT |
| proof-execution authority | explicit operator release recorded on 2026-08-05 | ACCEPT |
| review/commit authority | independent reviewer/closer after worker return | ACCEPT |

## Agent Roles

| Role | Ownership |
|---|---|
| dispatcher | authors and validates the held packet |
| worker | after release, runs one local proof and authors two uncommitted evidence artifacts |
| independent reviewer/closer | recomputes claims, records disagreement, and owns closure commit |
| session-sync steward | updates continuity separately using accepted material evidence |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeRole | dispatcher |
| executionRole | bounded proof worker |
| reviewRole | independent reviewer/closer |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| selected role route | dispatcher -> no-commit worker -> independent reviewer/closer -> session-sync steward |
| routingReason | worker and reviewer must not collapse proof production and acceptance into one role |
| workerSelfSelection | FORBIDDEN |
| escalation condition | source contradiction, additional path, source edit, persistent mutation, cleanup failure, provider/network/public action, risk change, or commit-owner change |

## Worker Autonomy / No-Question Rule

The worker resolves same-scope evidence-shape defects without requesting
operator confirmation. Return to the orchestrator only for a source
contradiction, forbidden-path need, changed risk/external-effect/commit-owner
boundary, unsafe cleanup, or missing authority that makes completion impossible.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id GLP-T3 --title "Disposable Fresh Workspace Propagation Proof" --date 2026-08-05 --base 10319c7dc --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | fixed exact owners, two-output manifest, one-run proof matrix, held dependency, reviewer route, and stop conditions |
| checkerReadAheadConfirmation | dispatch-quality, ADIF, handoff, trace, public disposition, file-size, roadmap freshness, and worker-return sources |
| docOnlyNewFields | callLevelResult; generatedManifestReadout; expectedArtifactAssertionLedger; guidanceReadout; privateLeakageReadout |
| claimBoundary | held dispatch packet only; no execution or propagation claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --surface-selector scripts/test_cvf_golden_downstream_bootstrap.ps1 --risk-ceiling MEDIUM --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional ADIF control beyond canonical packet rules |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | source-verification table columns and dispositions; ADIF resolver query; no-commit route and reviewer conversion; operation-trace labels; public-export token; worker-return shape |
| gateRunPurpose | confirm dispatch shape and source fidelity before release |
| claimBoundary | held local proof packet only |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T3 output and decisions | VALUE_SET | `docs/roadmaps/CVF_WORKSPACE_GOVERNANCE_LEARNING_PROPAGATION_ROADMAP_2026-08-05.md` | Work Plan GLP-T3 row | `GLP-T3` | GLP roadmap | ACCEPT |
| T2R1 prerequisite accepted | VALUE_SET | `docs/reviews/CVF_GLP_T2R1_CP1_BYTE_PRESERVING_MERGE_REPAIR_COMPLETION_2026-08-05.md` | Findings / Position | `CLOSED_PASS_BOUNDED` | T2R1 completion review | ACCEPT |
| hermetic fresh-project setup | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | setup lines 75-89 | `New-CvfHermeticCoreClone`; `projectA` | golden harness | ACCEPT |
| expected generated surfaces | VALUE_SET | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | AC-01 lines 91-102 | `requiredSurfaces` | golden harness | ACCEPT |
| generated manifest assertions | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | BSL-R3 lines 120-124 | `manifestA`; `requiredDocs` | golden harness | ACCEPT |
| five-rule guidance readout | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | helper lines 63-70; fresh/refresh assertions | `Test-CvfCarrierContent` | golden harness | ACCEPT |
| private leakage scan | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | lines 352-369 | `privateSentinels`; `privateHits` | golden harness | ACCEPT |
| path-safe cleanup and residue assertion | RUNTIME_BEHAVIOR | `scripts/test_cvf_golden_downstream_bootstrap.ps1` | lines 551-578 | `Test-CvfSafeCleanupTarget`; `residue` | golden harness | ACCEPT |

## New Doc-Only Fields

| Field | Purpose | Runtime claim |
|---|---|---|
| callLevelResult | separate harness invocation result from assertion denominator | none |
| generatedManifestReadout | record observed manifest keys/requiredDocs without retaining fixture | none |
| expectedArtifactAssertionLedger | map required surfaces to observed assertion | none |
| guidanceReadout | map each of five semantics to generated guidance evidence | none |
| privateLeakageReadout | record sentinel set, consumer scope, and hit count | none |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| output path existence | all four planned GLP-T3 baseline/work-order/audit/return paths were checked before authoring; none existed | ACCEPT |
| token search | `rg -n "GLP-T3|disposable fresh workspace|generated manifest|private-leakage|guidance readout" docs/roadmaps scripts governance/toolkit/05_OPERATION/CVF_DOWNSTREAM_AGENTS_TEMPLATE.md` | ACCEPT |
| collision decision | extend the existing golden harness as proof owner; create no new test or helper | ACCEPT |

## Dependency Release Evidence

| Dependency | Artifact | Commit / decision | Disposition |
|---|---|---|---|
| GLP-T2R1 | `docs/reviews/CVF_GLP_T2R1_CP1_BYTE_PRESERVING_MERGE_REPAIR_COMPLETION_2026-08-05.md` | `f59457b9a`; `CLOSED_PASS_BOUNDED` | ACCEPT |
| GLP-T3 execution | this packet | explicit operator release on 2026-08-05 | ACCEPT |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher -> no-commit proof worker -> independent reviewer/closer -> session-sync steward |
| phase | released pre-dispatch |
| baseHeadFor(phase) | dispatchBaseHead=`34dfbdb0c`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| changedSetScope(phase) | worker may create only the audit and worker return after release |
| traceScope(phase, actor) | each actor records its own command, path, changed-set, and claim boundary |
| commitOwner(phase) | worker forbidden; reviewer/closer owns accepted material commit |
| crossBatchIsolation | no unrelated worktree path may be present or absorbed |
| nextMoveSurfaces | session-sync steward updates canonical state using accepted material evidence |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_GLP_T3_DISPOSABLE_FRESH_WORKSPACE_PROPAGATION_PROOF_COMPLETION_2026-08-05.md` |
| reviewerOwnedClosurePaths | worker return, completion review, this work order, and roadmap status only |
| closureOwner | independent reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | disposable generated `AGENTS.md` | guidance inspection only; no action authority | audit plus harness evidence | local bootstrap projection | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | none | no CLI/MCP ingress, auth, receipt, mutation, or runtime claim | exact proof scope | external adapter excluded | `DEFERRED_WITH_REASON` |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Evidence owner | Fail condition |
|---|---|---|---|
| disposable fresh workspace | run existing hermetic harness once | audit call-level result | non-disposable path or persistent residue |
| generated manifest | record parsed manifest assertions | audit generated-manifest readout | missing/invalid manifest or requiredDocs |
| expected artifacts | record AC-01 list and missing count | audit assertion ledger | any missing required surface |
| negative private leakage | record sentinel scope and zero-hit result | audit leakage readout | any hit or incomplete scope |
| project guidance readout | record heading cardinality and five semantics separately | audit guidance readout | missing/duplicate/incomplete carrier |
| bounded decision | recommend one T3 exit token | worker return | unsupported or expanded claim |

## Required Artifact Manifest

Work-Order Fulfillment Manifest: exactly the two rows below.

| Artifact | Required worker action |
|---|---|
| `docs/audits/CVF_GLP_T3_DISPOSABLE_FRESH_WORKSPACE_PROPAGATION_PROOF_2026-08-05.md` | create the call-level, manifest, artifact, guidance, leakage, isolation, cost, and decision ledgers |
| `docs/reviews/CVF_GLP_T3_DISPOSABLE_FRESH_WORKSPACE_PROPAGATION_PROOF_WORKER_RETURN_2026-08-05.md` | return complete evidence and bounded recommendation for independent review |

No implementation/source/test/template file may change.

## Execution Plan

Execution has one preparation phase, one harness call, one consolidated
evidence-authoring phase, and one worker-return gate. No iterative
implementation or exploratory rerun loop is authorized.

## Execution Instructions

1. Confirm the packet is released, capture `executionBaseHead`, and require a
   clean worktree.
2. Run pre-implementation on the committed release range.
3. Read the harness before execution and record its expected 79-assertion
   denominator as a prediction, not a result.
4. Invoke the existing golden harness once. Do not edit it.
5. Classify any failure before considering a rerun. A second run is forbidden
   to the worker unless the reviewer later authorizes it for an independently
   stated reason.
6. Record call-level exit separately from assertion-level denominator.
7. Record manifest, expected artifacts, five guidance semantics, leakage scan,
   cleanup, and governance-cost evidence separately.
8. Create only the audit and worker return; run worker-return fast gate; commit
   nothing.

## Acceptance Criteria

- [ ] exactly one harness call exits zero and reports all assertions passing;
- [ ] generated manifest is parsed and required catalog/script entries are present;
- [ ] every AC-01 required surface is accounted for with missing count zero;
- [ ] generated `AGENTS.md` contains exactly one carrier and all five semantics;
- [ ] exact private-sentinel scan scope is named and hit count is zero;
- [ ] disposable cleanup residue count is zero;
- [ ] no source/test/template/session/downstream/public path changes;
- [ ] audit reports elapsed time, command count, harness-call count, provider/network count, mutation scope, and review expectation;
- [ ] worker recommends `PROPAGATION_PROVEN_BOUNDED` or `PROPAGATION_PROOF_FAILED` without adoption/causality overclaim;
- [ ] worker leaves artifacts uncommitted for independent review.

## Evidence Requirements

The audit must preserve command, exit code, assertion numerator/denominator,
manifest fields, exact required-surface list, carrier heading cardinality, five
separate semantic checks, leakage scope/hit count, cleanup residue count,
elapsed time when available, changed-set evidence, and bounded recommendation.

## Closure Checklist

- [ ] operator execution authority recorded;
- [ ] dependency and anchors refreshed before dispatch;
- [ ] pre-dispatch passes on the committed packet range;
- [ ] worker captures clean execution base;
- [ ] exactly one harness call is accounted for;
- [ ] every acceptance criterion is terminal;
- [ ] exact two-output worker manifest is preserved;
- [ ] independent reviewer disposition is recorded;
- [ ] worker makes no commit;
- [ ] material closure and continuity remain separate;
- [ ] public export remains deferred unless separately authorized.

## Operator Checkpoint

Checkpoint disposition: operator released GLP-T3 execution on 2026-08-05 and
selected the worker through the execution routing layer. No repeated
confirmation is needed unless objective,
allowed artifact class, R1 ceiling, external-effect class, or commit owner
changes.

## Worker Output Checker Read-Ahead Mandate

Before authoring the audit or return, read every checker applicable to its path,
docType, headings, trace, corpus/value/rescan language, public disposition, and
no-commit status. Required section names must be used as real headings only,
not repeated in a preliminary checklist with heading syntax.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_GLP_T3_DISPOSABLE_FRESH_WORKSPACE_PROPAGATION_PROOF_WORKER_RETURN_2026-08-05.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
powershell -ExecutionPolicy Bypass -File scripts/test_cvf_golden_downstream_bootstrap.ps1
python governance/compat/run_worker_return_fast_gate.py
git status --short
```

## Governance Cost Ledger

The audit must report:

- packet-reading and execution command count;
- harness call count and assertion denominator;
- elapsed wall time when available;
- provider/network call count, expected zero;
- disposable filesystem and Git mutation scope;
- number of repair/rerun loops;
- expected independent-review work.

## Review Gate

Independent review must recompute the complete manifest/artifact/guidance/
leakage/cleanup matrix before the first repair. The reviewer preserves any
disagreement and stops at repair round three unless a genuinely independent new
root cause exists.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for missing release authority, dirty worktree,
source contradiction, additional path or source edit, unsafe/non-disposable
mutation, cleanup failure, private leakage, provider/network need, unclear run
failure, or changed commit ownership.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author |
| Provider or surface | local private provenance repository |
| Session or invocation | GLP-T3 packet release, 2026-08-05 |
| Working directory | repository root |
| Command or tool surface | startup reads, source verification, scaffold helper, ADIF resolver, apply_patch, dispatch gates |
| Target paths | paired baseline and this work order |
| Allowed scope source | canonical next move permits packet authoring only |
| Before status evidence | HEAD `10319c7dc`; clean worktree |
| After status evidence | exact paired packet is dispatch-ready for one no-commit worker |
| Diff evidence | `git diff --name-status` limited to paired packet paths |
| Approval boundary | one bounded GLP-T3 proof execution only |
| Claim boundary | no proof execution, source edit, downstream/public/provider/network/push/deployment action |
| Agent type | dispatcher |
| Invocation ID | `glp-t3-held-packet-authoring-2026-08-05` |
| Expected manifest | paired baseline and this work order |
| Actual changed set | paired baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | released local disposable-workspace proof dispatch |
| claimDisposition | CLAIM_REJECTED: no completed propagation or runtime enforcement is claimed |
| receiptEvidence | N/A with reason: no provider/runtime receipt applies |
| actionEvidence | ACTION_EVIDENCE_PRESENT: packet source verification only |
| invocationBoundary | documentation authoring before execution release |
| interceptionBoundary | no direct interception, wrapper, runtime gate, or coding-control claim |
| claimLanguage | future bounded local proof, not adoption or causal effectiveness |
| forbiddenExpansion | no source/test/template edit, persistent workspace, downstream, provider/live, public-sync, push, or deployment |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: one existing harness call will show complete
fresh-project propagation, zero leakage, and zero cleanup residue.

Evidence Comparison Requirement: compare every proof dimension separately and
report both call-level and assertion-level denominators.

Contradiction Handling Requirement: preserve failures and disagreement; do not
convert a partial pass into a propagation claim.

Claim Update Requirement: recommend only one roadmap T3 exit token with the
local disposable-fixture boundary intact.

## Foundation Storage Layout Block

| Field | Value |
|---|---|
| foundationChange | NOT_APPLICABLE_WITH_REASON |
| reason | the worker creates dated execution evidence only; no durable governance foundation owner is created, split, relocated, or refactored |
| durableOwner | existing GLP roadmap, harness, bootstrap, and downstream template remain unchanged |
| indexOrRegistryChange | none authorized |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this private provenance work order authorizes no public-sync action.

## Claim Boundary

This work order releases one bounded no-commit GLP-T3 proof. It never authorizes implementation edits,
persistent downstream mutation, adoption claims, provider/network use, public
sync, push, or deployment.
