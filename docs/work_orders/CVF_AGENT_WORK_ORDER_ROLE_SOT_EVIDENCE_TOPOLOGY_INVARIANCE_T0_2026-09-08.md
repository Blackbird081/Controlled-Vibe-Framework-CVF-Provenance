# CVF Agent Work Order - Role SOT Evidence Topology Invariance T0
Memory class: governed-worker-dispatch
docType: work_order
Status: DISPATCH_READY
Date: 2026-09-08
Batch ID: ROLE-SOT-EVIDENCE-T0
Dispatch base head: `4ba46aa505836b49f0051dbe58c1446f4fac4434`
dispatchBaseHead: 4ba46aa505836b49f0051dbe58c1446f4fac4434
executionBaseHead: WORKER_MUST_CAPTURE_AT_START
closureBaseHead: REVIEWER_TO_SET
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN
externalAgentCliInvocationAuthority: ALLOWED_ONCE_ONLY_AFTER_EXPLICIT_OPERATOR_RELAY

## Dispatch Prompt Envelope

Role: external documentation worker; orchestrator/reviewer owns acceptance and commits.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ROLE_SOT_EVIDENCE_TOPOLOGY_INVARIANCE_T0_2026-09-08.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

Base: capture `executionBaseHead` before editing.

Current-time notes: documentation-only T0; external usage 0/1 before operator relay.

Do-not-misread notes: edit exactly two existing owners and create one return;
no new roadmap, baseline, standard, assessment, source or continuity path.

Required first actions: read every Required First Read in full, capture HEAD and
full status, confirm staging empty, then run the pre-implementation command.

Return contract: `COMPLETE_PENDING_REVIEW` with full execution base, exact
three-path status and final gate evidence, or `BLOCKED_WITH_REASON`.

## Purpose

Make CVF role governance explicitly topology-neutral and evidence-centered in
its two existing canonical owner standards. Preserve the operator's right to
choose one agent or many agents, assign one or many roles to an agent, and map
different models to different roles, while keeping every active role's
responsibility, authority, evidence output, forbidden actions, transition gate,
and escalation boundary explicit.

## Authority Chain

1. `ECOSYSTEM/doctrine/`, `ECOSYSTEM/operating-model/`, and `AGENTS.md`.
2. Operator decision on 2026-09-08 approving the compact topology-invariance
   tranche and explicitly avoiding a new roadmap or baseline.
3. The canonical seven-step loop in `README.md`, section `What CVF Is`.
4. Existing role owner
   `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md`.
5. Existing same-actor owner
   `docs/reference/CVF_SINGLE_AGENT_MULTI_ROLE_CONTROL_STANDARD_2026-06-11.md`.
6. RABA-F01-F02 terminal evidence in
   `docs/reviews/CVF_WP_ARCH_003_RABA_F01_F02_ROOT_EVIDENCE_REASSESSMENT_COMPLETION_2026-09-08.md`
   at material commit `0767a16e586699ab45d8f42057c62aea386490ca`.

GC-018 disposition: operator-approved R0 documentation-only direct work order;
no additional baseline is required for this bounded existing-owner correction.

## Dependency Release Evidence

| Dependency | Immutable evidence | Status | Disposition |
|---|---|---|---|
| RABA-F01-F02 terminal decision | completion review at material commit `0767a16e586699ab45d8f42057c62aea386490ca`; SHA-256 `d1945cb6830a6e01b4a0b30de82f8245e77b37f95802cb4248b8533a6411eafe` | root remains parked; F01/F02 resolved | SATISFIED |
| operator topology decision | operator messages on 2026-09-08 summarized in this packet | compact existing-owner correction selected | SATISFIED |

RABA-T1 through RABA-T3 are `NOT_OPENED_PRECONDITION_ABSENT`. This T0 neither
relabels them as executed nor releases them.

## Intake Role Routing Decision

Route mode: `MULTI_AGENT_MULTI_ROLE`.

Intake summary: the operator approved a compact existing-owner correction after
RABA reached its truthful terminal park.

Scope classification: bounded R0 documentation work on exactly three paths.

Risk sensitivity: no production, secret, provider, live or public-sync action;
semantic role-boundary drift remains the main risk.

Selected role route: the operator selects `MULTI_AGENT_MULTI_ROLE` for this
use case - one external worker edits the owners and one orchestrator/reviewer
reviews evidence and commits if accepted. This is not a mandatory topology.

Escalation condition: stop for a required extra path, doctrine conflict,
change to a risk-specific separate-review rule, or any non-documentation effect.

## Agent Roles

| Role | Responsibility | Limit |
|---|---|---|
| Operator | selects topology and authorizes this bounded packet | does not substitute preference for evidence |
| Dispatcher | fixes scope, evidence contract, invocation ceiling and stop rules | does not perform the worker edits |
| External worker | modifies the two named standards and creates the return | no self-acceptance, staging, commit or scope expansion |
| Reviewer/closer | reconstructs claims from sources, diff and gates; accepts, makes permitted closure edits, or returns | does not claim different-actor independence beyond the actual topology |
| Session-sync steward | updates continuity only if reviewer accepts | no material standard editing in the sync commit |

## Single-Agent Multi-Role Control Block

Applicability: the current execution route uses different actors, but the
subject and required owner text explicitly cover single-agent multi-role work.

Role separation ledger: each stage retains its role-by-role duty, evidence and
transition boundary even when the same actor holds multiple roles.

Evidence basis: source, diff, test and gate evidence must be reconstructed; a
memory-only assertion is insufficient.

Self-review boundary: same-actor self-review must disclose that different-actor
independent review is not claimed. That disclosure is assurance metadata, not
an identity-based truth verdict.

Escalation conditions: stop for any explicit different-actor requirement,
higher risk, scope expansion, external effect or operator decision boundary.

Gate sequence: pre-dispatch -> pre-implementation -> reviewer-fast -> committed
material pre-closure -> separate continuity verification when applicable.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL

dispatchSurface: EXTERNAL_AGENT_CLI_MCP

parentAssignmentId: ROLE-SOT-EVIDENCE-T0

reviewRoundCount: 0

priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH

dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX

reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH

newIndependentCriticalEvidence: NONE

regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED

cumulativeExternalInvocationCount: 0

externalInvocationCeiling: 1

usageAvailability: KNOWN_FOR_ADMISSION

quotaAdmissionDisposition: ADMITTED_WITHIN_CUMULATIVE_CEILING

nextDispatchDisposition: INITIAL_DISPATCH

rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH

reworkGeneration: 0

consolidatedDefectClassSweep: COMPLETE_INITIAL_ACCEPTANCE_MATRIX

successorTrancheOpened: NO

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION

preExecutionReviewTrigger: NONE

nextRoutineReviewBoundary: WORKER_RETURN

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "ROLE_SOT_EVIDENCE_TOPOLOGY_INVARIANCE",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": [
      "ROLE_OBLIGATIONS_NOT_EXPLICITLY_TOPOLOGY_INVARIANT",
      "REVIEW_VALIDITY_AND_ACTOR_INDEPENDENCE_CONFLATED"
    ],
    "reopened": [],
    "current": [
      "ROLE_OBLIGATIONS_NOT_EXPLICITLY_TOPOLOGY_INVARIANT",
      "REVIEW_VALIDITY_AND_ACTOR_INDEPENDENCE_CONFLATED"
    ]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [
    {
      "claimId": "ROLE-SOT-EVIDENCE-T0-DISPATCH",
      "claimClass": "DOCUMENTATION_ONLY",
      "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS",
      "evidenceRef": "docs/work_orders/CVF_AGENT_WORK_ORDER_ROLE_SOT_EVIDENCE_TOPOLOGY_INVARIANCE_T0_2026-09-08.md"
    }
  ],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## Scope / Target / Owner Boundary

Allowed scope:

- clarify and extend the two existing role-control standards;
- add a seven-step role responsibility matrix to the role-assignment owner;
- correct actor-count language in the same-actor owner without weakening any
  separately authorized risk or independence requirement;
- create the one required worker return and run local documentation gates.

Forbidden scope:

- new roadmap, baseline, standard, assessment, policy, ADR, registry or index;
- changes to `README.md`, `ARCHITECTURE.md`, `AGENTS.md`, source, tests,
  checkers, hook catalogs, session state or active handoff;
- external corpus intake or repository absorption;
- RABA-T1 through RABA-T3, runtime, provider, live, secrets, public-sync,
  deployment, destructive action, nested delegation, staging or commit.

Risk ceiling: R0 documentation-only.

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_EXTERNAL_LOW_RISK_WITH_REASON:DOCS_ONLY_EXISTING_OWNER_CLARIFICATION_NO_RUNTIME_ARCHITECTURE

Reason: the worker changes governance prose in existing owner surfaces only.
No architecture binding, runtime path, producer, consumer or implementation is
created or selected.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`, bootstrap read model, and active handoff named there.
2. `docs/reference/guard_orientation/README.md`.
3. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`.
4. This work order in full.
5. `README.md`, section `What CVF Is`, including the seven-step table.
6. `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md` in full.
7. `docs/reference/CVF_SINGLE_AGENT_MULTI_ROLE_CONTROL_STANDARD_2026-06-11.md` in full.
8. `docs/reference/CVF_AGENT_DELEGATION_AND_SUBAGENT_BOUNDARY_STANDARD_2026-05-19.md`, especially Core Principle, delegation packet and evidence boundaries.
9. `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`, section `Single-Agent Multi-Role Rule`.
10. The RABA-F01-F02 completion review named in the Authority Chain.
11. Checker sources listed in the Checker Source Read-Ahead Block, applied to
    each output path before editing.

## Pre-Flight Checks

Run from repository root before edits:

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
git diff --cached --name-status
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 4ba46aa505836b49f0051dbe58c1446f4fac4434 --head HEAD
```

The committed packet should be the captured HEAD and the worktree/staging area
must be clean. A contradiction or unrelated dirty path is a stop condition.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ROLE-SOT-EVIDENCE-T0","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"DOC_CHANGE","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/work_orders/","docs/reference/","docs/reviews/"],"claims":["topology-neutral role obligations and evidence-centered review validity"],"requiredProof":["seven-step responsibility matrix","validity-independence distinction","exact three-path diff","no-commit worker return"],"operatorCheckpoints":["explicit relay","reviewer semantic disposition"],"forbiddenEffects":["new owner artifact","runtime or test mutation","provider or live call","RABA successor release","repository absorption","public sync","deployment","worker commit"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"N/A with reason: named current owner files only; no corpus claim","completenessClaimChanged":false}}
```

Expected route: `ROUTED_SHADOW`, profile `P3_ELEVATED`, selective execution
false, full legacy bundle required.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| canonical seven-step loop and stage outputs | `README.md` | `What CVF Is` | `What CVF Is` | repository front door | ACCEPT |
| current role assignment owner and lane duties | `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md` | `Core Assignment Rule`; `Role Assignment Flow` | `Core Assignment Rule` | CVF role assignment matrix | ACCEPT |
| current same-actor phase/evidence owner | `docs/reference/CVF_SINGLE_AGENT_MULTI_ROLE_CONTROL_STANDARD_2026-06-11.md` | `Protocol`; `Failure Modes` | `Protocol` | single-agent multi-role standard | ACCEPT |
| delegation is bounded execution, not authority transfer | `docs/reference/CVF_AGENT_DELEGATION_AND_SUBAGENT_BOUNDARY_STANDARD_2026-05-19.md` | `Core Principle`; `Mandatory Delegation Packet` | `Core Principle` | delegation boundary standard | ACCEPT |
| current RABA terminal and unreleased successors | `docs/reviews/CVF_WP_ARCH_003_RABA_F01_F02_ROOT_EVIDENCE_REASSESSMENT_COMPLETION_2026-09-08.md` | `Decision / Disposition` | `PARK_NO_TRUTHFUL_AUTHORITY_ROOT` | RABA completion review | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| new work-order path | `Test-Path` returned False before authoring | PASS_NO_COLLISION |
| worker-return path | `Test-Path` returned False before authoring | PASS_NO_COLLISION |
| batch token | `rg -n --fixed-strings "ROLE-SOT-EVIDENCE-T0" docs CVF_SESSION` returned zero matches before authoring | PASS_NO_COLLISION |
| owner collision | two existing standards above already own the subject | EXTEND_EXISTING_NO_THIRD_OWNER |

## Planned Worker Fulfillment Manifest

| Path | Action | Required at handoff | Purpose |
|---|---|---|---|
| `docs/reference/CVF_AGENT_ROLE_ASSIGNMENT_MATRIX_2026-05-19.md` | MODIFY | YES | topology invariant plus seven-step responsibility matrix |
| `docs/reference/CVF_SINGLE_AGENT_MULTI_ROLE_CONTROL_STANDARD_2026-06-11.md` | MODIFY | YES | evidence-operation validity and actor-independence distinction |
| `docs/reviews/CVF_ROLE_SOT_EVIDENCE_TOPOLOGY_INVARIANCE_T0_WORKER_RETURN_2026-09-08.md` | CREATE | YES | exact diff, source, gate and no-commit evidence |

Work-Order Fulfillment Manifest: the three rows above are the complete worker
changed-set contract.

## Write Ownership

Owned paths are exactly the three Planned Worker Fulfillment Manifest rows.

Write mode: modify-listed for the two standards; create-only for the return.

Every other repository path is forbidden. Temporary analysis stays outside the
repository and cannot be cited as CVF authority.

## Execution Plan

1. Capture `executionBaseHead`, clean status and empty staging, then complete
   every Required First Read and checker read-ahead.
2. Run the pre-implementation gate once from the captured base.
3. Extend the Role Assignment Matrix with one canonical topology-invariance
   rule and one seven-step responsibility matrix.
4. Amend the Single-Agent Multi-Role Standard so evidence-operation validity
   is distinct from actor-independence metadata and risk-specific routing.
5. Create the worker return from the fast documentation scaffold, fill every
   field, and reconcile its exact manifest to Git status.
6. Run the required checks after the last edit. Perform allowed-scope
   remediation within the three owned paths and execute the failed check again.
7. Leave all output unstaged and uncommitted and return to the reviewer.

## Normative Content Contract

The two owner standards together must establish all of the following:

1. The operator chooses execution topology. CVF does not mandate one agent,
   many agents, one model, many models, or a fixed role-to-model mapping.
2. Role requirements are topology invariant. Combining roles in one actor does
   not merge, erase, or weaken their individual duties and boundaries.
3. Every active seven-step role assignment records responsibility, authority
   inputs, expected evidence/output, forbidden actions, transition gate, and
   escalation owner. An inactive role is explicitly N/A with reason.
4. `INTAKE`, `DESIGN`, `SPEC`, `WORK ORDER`, `BUILD`, `REVIEW`, and `FREEZE`
   remain distinct evidence phases even when one actor performs several.
5. A role may have an operator-selected model assignment, but model identity is
   execution metadata and not canonical source authority.
6. All roles resolve claims against the same named CVF SOT paths, immutable
   anchors, receipts, diffs, tests, and accepted evidence available in the
   shared workspace. Provider-local memory is not SOT.
7. Shared SOT does not imply that different models or agents must reach the
   same conclusion. CVF supplies common evidence and claim boundaries; it does
   not homogenize reasoning ability or output.
8. Review validity comes from reconstructing the reviewed claim from current
   sources, receipts, diffs, tests, and authority boundaries. Actor count alone
   neither proves nor disproves semantic validity.
9. Review independence is disclosed separately as assurance metadata, such as
   same actor with phase-separated evidence or different actor. It must not be
   silently inferred from a role label.
10. If a governing risk rule, work order, or operator decision specifically
    requires a different actor, same-actor review cannot satisfy that routing
    gate. Its evidence may remain candidate input; the restriction is not a
    claim that actor count creates truth.
11. Same-actor multi-role work retains phase declarations, base anchors,
    evidence separation, commit ownership, and stop/escalation boundaries.
12. No text may claim universal runtime enforcement, model equivalence,
    automatic role routing, provider behavior, public readiness, or production
    readiness from these documentation changes.

## Design Control Carry-Forward

| Control | Source | Handling | Verdict |
|---|---|---|---|
| scope | operator decision and this packet | only two existing owners plus return | PASS |
| non-goals | Dispatch Prompt Envelope and Scope | no new owner or runtime behavior | PASS |
| evidence plan | Normative Content Contract | source/diff/gate reconstruction required | PASS |
| topology choice | operator decision | current external-worker route is use case only | PASS |
| successor boundary | RABA completion review | T1-T3 stay unopened | PASS |
| roadmap | operator explicitly chose compact direct packet | N/A with reason: no roadmap-derived work | N/A with reason |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact or field | Verification command or check | Status |
|---|---|---|---|---|
| N/A with reason: operator selected a direct compact docs-only packet | Authority Chain and Normative Content Contract | two existing owner standards plus worker return | exact changed-set and reviewer-return gates | N/A with reason |

## Evidence Requirements

- exact before/after quotations or line locators for every changed normative
  statement;
- one responsibility matrix covering all seven stages and all six role fields;
- explicit reconciliation of current phrases that conflate same-actor review
  with semantic validity;
- `git diff --check`, exact three-path `git diff --name-status`, and actual
  `git status --short --untracked-files=all`;
- worker-return fast gate and pre-implementation autorun PASS after final edit;
- no provider, live, network, public-sync, commit or staging action.

## Acceptance Criteria

- [ ] Exactly the three owned paths are modified or created.
- [ ] The Role Assignment Matrix contains all twelve Normative Content Contract items applicable to the general role system.
- [ ] The seven-step matrix contains responsibility, authority input, evidence/output, forbidden action, transition gate and escalation owner for every stage.
- [ ] The Single-Agent Multi-Role Standard distinguishes evidence validity, actor independence and risk-specific separate-review routing.
- [ ] No rule claims shared SOT forces identical conclusions.
- [ ] No new canonical owner or runtime/public/provider claim is introduced.
- [ ] All required final gates pass and all outputs remain unstaged/uncommitted.

Fail conditions:

- any third owner artifact, source/test/checker/continuity edit, role erasure,
  automatic model selection, identity-based truth claim, RABA release, external
  effect, staging or commit;
- any mandatory final check remains failed after allowed-scope remediation.

## Worker Autonomy / No-Question Rule

Proceed autonomously for reads, bounded edits, diff/hash/status checks,
documentation-format remediation, and repeated checks inside the three owned
paths. Escalate only when the necessary change exceeds those paths, changes
the claim/risk boundary, conflicts with doctrine, or requires an external
effect. Routine allowed-scope remediation proceeds without a new decision.

## Pending Artifact Evidence Finality

Pending files must show their real dirty status. Do not cite a committed-only
range as proof for uncommitted worker edits. `COMPLETE_PENDING_REVIEW` is not a
closure decision.

## Self-Reported Gate Evidence Consistency

After the last edit, execute every required command again and update the return
with the actual final result. A required failure that cannot be satisfied inside scope
requires `BLOCKED_WITH_REASON`.

## Commit Mode And Base-Anchor Lifecycle

| Anchor | Owner | Required value |
|---|---|---|
| `dispatchBaseHead` | dispatcher | `4ba46aa505836b49f0051dbe58c1446f4fac4434` |
| `executionBaseHead` | worker | full committed HEAD captured before worker edits |
| `closureBaseHead` | reviewer | captured before any reviewer material commit |

The worker must not stage or commit. Reviewer material and later continuity
commits use separate ranges.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` selected by operator for this assignment |
| rolePattern | dispatcher -> operator-relayed external worker -> reviewer/closer -> session-sync steward |
| phase | docs-only T0 existing-owner correction |
| baseHeadFor(phase) | dispatch base fixed above; worker and reviewer capture later anchors |
| changedSetScope(phase) | exactly three owned paths |
| traceScope(phase, actor) | one external invocation plus local reads, edits and gates |
| commitOwner(phase) | reviewer/closer only |
| crossBatchIsolation | RABA, repository absorption and every runtime lane remain parked |
| nextMoveSurfaces | reviewer decision; no automatic successor |

Two-Stage Handoff Finality: the worker return is candidate evidence. Reviewer
acceptance and committed-range proof are separate later operations.

## Reviewer Closure Conversion

completionReviewPath: N/A with reason: optional; reviewer should record the
decision in the corrected worker return when sufficient and avoid an extra
closure artifact.

reviewerOwnedClosurePaths: the two standards and worker return only, followed
by a separate continuity projection if accepted.

closureOwner: orchestrator/reviewer.

workerCommitPermission: FORBIDDEN.

## Worker Output Checker Read-Ahead Mandate

Before writing, apply checker-source constants separately to both existing
reference owners and the new review-class worker return. Dispatch packet
compliance is not a substitute for output-artifact compliance.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FAST_DOC_V1

scopeClassification: DOCUMENTATION_AND_EVIDENCE_ONLY_NO_COMMIT

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

publicSyncDisposition: FORBIDDEN

liveRuntimeDisposition: FORBIDDEN

checkerMutationDisposition: FORBIDDEN

workerSelfSelection: FORBIDDEN

Create the return skeleton before long prose:

```powershell
python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_ROLE_SOT_EVIDENCE_TOPOLOGY_INVARIANCE_T0_WORKER_RETURN_2026-09-08.md --title "Role SOT Evidence Topology Invariance T0 Worker Return" --profile WORKER_RETURN_FAST_DOC_V1
```

The return must include the fast-profile required sections plus Target / Source,
Scope / Methodology, Findings / Position, Risk / Corrective Action, Decision /
Disposition, Checker Source Read-Ahead Block, Agent Operation Trace Block,
Delta Execution Claim Boundary Control Block, Finding-To-Governance Learning
Disposition, Epistemic Process Block, Public Export Disposition, Claim Boundary,
actual Git status, exact Changed Files, Command Evidence, No-Commit Statement,
and Conditional Controls Disposition. Do not omit N/A-with-reason sections.

The return must repeat the Review Dispatch fields needed for a worker return,
use terminalReadinessVerdict `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`,
and keep both SCEC blockers retained until reviewer acceptance.

## Verification Commands

Run after the final material edit:

```powershell
git diff --check
git diff --name-status
git diff --cached --name-status
git status --short --untracked-files=all
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
```

Expected: diff check PASS; changed set exactly three owned paths; staging empty;
worker-return fast gate PASS; pre-implementation PASS or only the explicitly
recognized pending-finality disposition permitted by the work order standard.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_WP_ARCH_003_RABA_F01_F02_ROOT_EVIDENCE_REASSESSMENT_COMPLETION_2026-09-08.md`

priorVerificationAnchor: material commit `0767a16e586699ab45d8f42057c62aea386490ca`; SHA-256 `d1945cb6830a6e01b4a0b30de82f8245e77b37f95802cb4248b8533a6411eafe`

recomputeReason: current owner text, diff and gate evidence must be read again;
only the cited RABA terminal identity is immutable predecessor evidence.

freshRecomputeRequired: YES

unicodePathHandling: use literal repository-relative paths, UTF-8-safe readers
and ASCII-default authored prose.

extractedTextAuthority: N/A with reason: no extracted external text.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`role governance standard update`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class "role governance standard update" --role dispatcher --lifecycle-phase pre-dispatch --json`

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_core.py`; `governance/compat/check_work_order_dispatch_quality_range.py`; `governance/compat/check_work_order_dispatch_quality_source.py`; `governance/compat/check_work_order_dispatch_quality_architecture_schema.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | dispatch status and anchors; Source Verification columns and dispositions; review convergence scalar fields; low-risk architecture declaration; fast documentation return profile; structural work-order/review headings; trace labels; Delta eight-field table; private export token; semantic convergence JSON fields |
| gateRunPurpose | confirmation and dispatch evidence after checker read-ahead, not first discovery of packet shape or semantic acceptance |
| claimBoundary | structural compliance cannot prove semantic correctness, identical model conclusions, runtime enforcement or future tranche authority |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ROLE-SOT-EVIDENCE-T0 --title "Role SOT Evidence Topology Invariance T0" --date 2026-09-08 --base 4ba46aa505836b49f0051dbe58c1446f4fac4434 --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_WP_ARCH_003_RABA_F01_F02_ROOT_EVIDENCE_REASSESSMENT_COMPLETION_2026-09-08.md --stdout --include-worker-return-skeleton --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --scec-problem-key ROLE_SOT_EVIDENCE_TOPOLOGY_INVARIANCE --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED` |
| generatedProfile | generic external no-commit initial dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | compacted to one direct operator-authorized work order; filled existing-owner scope, evidence-validity contract and exact three-path return |
| checkerReadAheadConfirmation | checker sources and literal-format gotchas were read before authoring |
| docOnlyNewFields | none; all new concepts are normative prose inside existing owners |
| claimBoundary | scaffold provenance only; no runtime or semantic acceptance claim |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | orchestrator/reviewer and committed packet | review/closure only | current sources, diff and gates | N/A with reason: no runtime adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | operator-relayed worker | one invocation, three paths, no commit | execution anchor, exact diff and return | relay transports candidate evidence only | CONTRACT_ONLY |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent packet request |
| Chain map route | committed work order -> operator relay -> pending three-path return -> reviewer disposition |
| Matching local-view guard | `governance/compat/check_worker_return_quality_gate.py` |
| Owner surface | this work order and the two existing role standards |
| Disposition | worker output remains candidate evidence until reviewer acceptance |
| Claim boundary | no external repository absorption or worker self-acceptance |

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION: no outside repository, copied folder, mirror or
external corpus is read or absorbed. The external worker is an execution role,
not an authority source.

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: this is a two-owner correction with no corpus-wide,
all-files-read, repository scan or absorption-completeness claim.

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: no legacy input or legacy owner is used.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - bounded full reads of named
  owner files do not claim complete repository or corpus coverage.

## Foundation Storage Layout Block

N/A with reason: no new owner, directory, aggregate, registry, storage layout or
relocation is introduced.

## Near-Threshold Owner Maintainability Plan

N/A with reason: the work modifies two small documentation owners and creates
one bounded return; no registered near-threshold source entrypoint is touched.

## Current Runtime Freshness Verification

runtimeClaimPresent: NO

runtimeMutationAuthorized: NO

freshnessVerificationMode: CURRENT_DOCUMENT_OWNER_READS_ONLY

claim limit: procedural governance semantics only; no runtime behavior claim.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | orchestrator/dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | ROLE-SOT-EVIDENCE-T0 dispatch authoring, 2026-09-08 |
| Working directory | repository root at `4ba46aa505836b49f0051dbe58c1446f4fac4434` |
| Command or tool surface | governed reads, Git, `rg`, hashes, ADIF resolver, scaffold stdout and `apply_patch` |
| Target paths | `docs/work_orders/CVF_AGENT_WORK_ORDER_ROLE_SOT_EVIDENCE_TOPOLOGY_INVARIANCE_T0_2026-09-08.md` |
| Allowed scope source | operator authorization for the recommended compact packet on 2026-09-08 |
| Before status evidence | HEAD `4ba46aa505836b49f0051dbe58c1446f4fac4434`; clean worktree; empty staging |
| After status evidence | one new work order only; no worker invocation or external effect |
| Diff evidence | `git status --short`; `git diff --check`; pre-dispatch and local hook evidence |
| Approval boundary | packet authoring and commit only; worker execution requires operator relay |
| Claim boundary | no standard mutation, worker execution, RABA release, runtime/provider/live/public/deploy action |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `role-sot-evidence-t0-dispatch-authoring-2026-09-08` |
| Expected manifest | `docs/work_orders/CVF_AGENT_WORK_ORDER_ROLE_SOT_EVIDENCE_TOPOLOGY_INVARIANCE_T0_2026-09-08.md` |
| Actual changed set | `docs/work_orders/CVF_AGENT_WORK_ORDER_ROLE_SOT_EVIDENCE_TOPOLOGY_INVARIANCE_T0_2026-09-08.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | documentation-only role-control owner correction |
| claimDisposition | `CLAIM_REJECTED`: no execution-control or runtime-enforcement claim |
| receiptEvidence | `CLAIM_REJECTED_NO_RECEIPT`: no runtime receipt is created or consumed |
| actionEvidence | `CLAIM_REJECTED_NO_ACTION`: no protected action is executed or observed |
| invocationBoundary | one later operator-relayed worker invocation plus local reads, edits and gates |
| interceptionBoundary | no IDE, shell, Git, filesystem, provider or network interception claim |
| claimLanguage | shared SOT and evidence-operation procedural rules only |
| forbiddenExpansion | automatic role routing, model selection, runtime enforcement, provider/live/public/deploy and RABA successor claims |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the two existing owners can carry the rule without
a third standard, but their current wording needs an explicit topology
invariant and a validity-versus-independence distinction.

Evidence Comparison Requirement: compare the final owner text and diff against
all twelve Normative Content Contract items.

Contradiction Handling Requirement: record any source conflict as a
Contradiction Or Gap Disposition and stop if fixing it needs another owner.

Claim Update Requirement: state whether the prediction was confirmed, narrowed,
revised or invalidated.

## Operator Checkpoint

Operator approval for this exact compact packet is already recorded. A new
checkpoint is required only for more paths, another invocation, higher risk,
separate-review rule changes, external effects, or a successor tranche.

## Review Gate

Worker handoff is not acceptance. Reviewer must consume returned source/diff/
gate evidence, run the reviewer-return fast path, and issue one consolidated
decision. Routine review must not recreate the worker edits.

## Machine Closure Package

NOT_APPLICABLE_WITH_REASON: this is a dispatch-ready work order. Reviewer owns
any later material commit, committed-range gate and continuity projection.

## Closure Checklist

- [x] Operator authorization and direct docs-only waiver recorded.
- [x] Exact two owners and one worker return fixed.
- [x] Role/model topology remains operator-selected.
- [x] Evidence validity and actor independence are separated.
- [x] Invocation ceiling and no-commit boundary fixed.
- [x] RABA successors and external effects remain parked.

## Return-To-Orchestrator Conditions

Return without continuing if doctrine conflicts, the work needs a fourth path,
the operator-selected topology would be replaced by a mandatory topology, a
risk-specific different-actor rule would be weakened, a required check cannot
be satisfied inside scope, or any external effect becomes necessary.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance role-governance dispatch; no public-sync authority.

## Claim Boundary

This packet authorizes one operator-relayed external-worker invocation and
exactly three pending documentation paths. It does not itself change the two
standards, validate a future worker result, force identical conclusions across
models, establish universal runtime role enforcement, reopen RABA-T1 through
T3, begin repository absorption, call a provider, publish, push or deploy.
