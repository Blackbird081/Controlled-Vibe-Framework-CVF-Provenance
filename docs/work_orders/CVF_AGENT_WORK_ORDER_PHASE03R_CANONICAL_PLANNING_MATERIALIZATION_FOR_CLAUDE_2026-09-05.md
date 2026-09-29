# CVF Agent Work Order - Phase-03R Canonical Planning Materialization

Memory class: ACTIVE_WORK_ORDER

docType: work_order

Status: CLOSED_PASS_BOUNDED

Date: 2026-09-05

Batch ID: CVF-PHASE03R-MATERIALIZATION-T1

Risk ceiling: R1

dispatchBaseHead: c527b71ce009a682d094ad735113c79113f7b5a1

closureBaseHead: c527b71ce009a682d094ad735113c79113f7b5a1

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

```text
Role: worker/implementer; an independent reviewer/closer owns acceptance.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_PHASE03R_CANONICAL_PLANNING_MATERIALIZATION_FOR_CLAUDE_2026-09-05.md.
Commit mode: WORKER_MUST_NOT_COMMIT.
executionBaseHead: capture current git rev-parse HEAD before the first edit.
Current-time notes: no live key, provider call, network research, runtime change,
  public-sync, push, or implementation of any Phase-04 WP is authorized. This
  is REWORK round 1 for the consolidated semantic-completeness finding set.
Do-not-misread notes: create four complete 03R successor documents; do not edit
  the four original 03 files or the three local correction-review artifacts.
  Incorporation by reference is not a complete or self-contained successor.
Required first actions: read AGENTS.md, the bootstrap read model, session front
  door, active handoff, paired GC-018, this packet, guard orientation, literal
  gotchas, four original Phase-03 files, and three local Phase-03R review files;
  then capture HEAD, status, hashes, and run pre-implementation checks.
Return contract: COMPLETE_PENDING_REVIEW or BLOCKED_WITH_REASON with
  executionBaseHead, exact changed paths, hashes, reconciliation results,
  gates, git status, no-commit evidence, and the worker-return artifact.
```

## Purpose

Create a complete candidate canonical Phase-03R planning set from the original
Phase-03 documents and the accepted local correction overlay. Success means
four self-contained successor artifacts reconcile exactly, preserve every
backlog obligation, encode the corrected WP/edge/wave decisions, and pass all
applicable documentation and graph checks without modifying implementation.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "CVF-PHASE03R-MATERIALIZATION-T1",
  "requestedProfile": "P2_BOUNDED",
  "classification": {
    "taskKind": "DOC_CHANGE",
    "authorityImpact": "USES_EXISTING_OWNER",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "NAMED_FILES",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "OWNER_COMPOSITION"
  },
  "pathFamilies": ["docs/baselines/", "docs/work_orders/", "docs/reviews/", ".private_reference/legacy/CVF 05.09/"],
  "claims": ["four complete Phase-03R successor planning artifacts can be materialized from reconciled local authority"],
  "requiredProof": ["38 WPs", "68 backlog obligations", "51-edge DAG", "exact-five output manifest", "authority-input byte identity", "independent post-execution review"],
  "operatorCheckpoints": ["scope expansion", "authority-decision reversal", "implementation", "provider or live work", "public sync", "commit mode change"],
  "forbiddenEffects": ["source mutation", "runtime mutation", "provider call", "worker commit", "push", "public export", "automatic Phase-04 dispatch"],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": ".private_reference/legacy/CVF 05.09/03R_CVF_LOCAL_PHASE03R_VERIFICATION_RECEIPT.json",
    "completenessClaimChanged": false
  }
}
```

## Authority Chain

1. Operator instruction on 2026-09-05 authorizes creation and dispatch of this
   work order.
2. `docs/baselines/CVF_GC018_PHASE03R_CANONICAL_PLANNING_MATERIALIZATION_2026-09-05.md`
   authorizes the bounded tranche.
3. The four original Phase-03 files are the source planning set.
4. The local Phase-03R correction review, corrected edge delta, and JSON receipt
   are the accepted correction authority.
5. This work order controls worker scope and return conditions.

Authority boundary: external-agent prose is advisory only. When it conflicts
with the local correction review, the local correction review controls.

## Agent Roles

- Orchestrator/dispatcher: dispatcher role.
- Implementer: delegated worker, one implementation role only.
- Reviewer/closer: independent reviewer/closer after worker return.
- Operator intervention: only for requested scope expansion, destructive work,
  provider/live/public work, commit-mode change, or an authority contradiction.

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| Intake source | locally reviewed external Phase-03R correction packet |
| Route | `MULTI_AGENT_MULTI_ROLE` |
| canonical route mode | `MULTI_AGENT_MULTI_ROLE` |
| scope classification | R1 private planning-document materialization |
| risk sensitivity | low operational risk but high planning-integrity sensitivity; exact counts, owner bindings, and claim boundaries fail closed |
| selected role route | dispatcher; delegated worker; independent reviewer/closer |
| Runtime/source modification | forbidden |
| External evidence intake | already reconciled; no new external intake authorized |
| Disposition | bounded no-commit materialization |
| escalation condition | authority conflict or required change outside exact-five worker manifest |

## Scope

Allowed worker scope:

- create the four Phase-03R planning successors listed in the fulfillment
  manifest;
- create one worker-return artifact;
- read any repository file needed to verify existing paths and symbols;
- run non-mutating local parsers, hashes, searches, and governance checks;
- repair only the five worker-owned outputs when an applicable gate fails.

Forbidden worker scope:

- edit, delete, rename, or overwrite any original `03_CVF_*` file;
- edit the local Phase-03R review, corrected edge delta, or verification receipt;
- edit source, runtime, tests, governance checkers, registries, session state,
  active handoff, memory front door, AGENTS.md, or this dispatch packet;
- stage, commit, push, publish, deploy, install packages, use secrets/quota, or
  call providers/external services;
- implement any of the 38 WPs or claim Phase-04 dispatch readiness.

## Write Ownership

The worker owns only the exact five output paths in the Work-Order Fulfillment
Manifest and must leave them uncommitted. The reviewer/closer owns review, any completion
artifact, any accepted commit, and any later session synchronization. All
authority inputs and every other repository path are read-only to the worker.

## Required First Reads

1. `AGENTS.md`
2. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
3. `CVF_SESSION_MEMORY.md`
4. `AGENT_HANDOFF_V59_2026-08-11.md`
5. `docs/reference/guard_orientation/README.md`
6. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
7. paired GC-018 baseline and this work order
8. four original Phase-03 files under `.private_reference/legacy/CVF 05.09/`
9. three local Phase-03R correction/reconciliation artifacts in the same folder

Read current source-owner files cited in the correction review only as targeted
verification; do not perform a full repository corpus scan.

## Pre-Flight Checks

Before edits:

```powershell
git rev-parse HEAD
git status --short
Test-Path -LiteralPath ".private_reference/legacy/CVF 05.09/03_CVF_GLOBAL_IMPLEMENTATION_PLAN.md"
Test-Path -LiteralPath ".private_reference/legacy/CVF 05.09/03R_CVF_LOCAL_PHASE03R_CORRECTION_REVIEW.md"
Get-FileHash -Algorithm SHA256 -LiteralPath ".private_reference/legacy/CVF 05.09/03_CVF_GLOBAL_IMPLEMENTATION_PLAN.md", ".private_reference/legacy/CVF 05.09/03_CVF_IMPLEMENTATION_ACCEPTANCE_MATRIX.md", ".private_reference/legacy/CVF 05.09/03_CVF_IMPLEMENTATION_DEPENDENCY_MAP.md", ".private_reference/legacy/CVF 05.09/03_CVF_IMPLEMENTATION_WORK_PACKAGE_LEDGER.md", ".private_reference/legacy/CVF 05.09/03R_CVF_LOCAL_PHASE03R_CORRECTION_REVIEW.md", ".private_reference/legacy/CVF 05.09/03R_CVF_LOCAL_PHASE03R_CORRECTED_EDGE_DELTA.md", ".private_reference/legacy/CVF 05.09/03R_CVF_LOCAL_PHASE03R_VERIFICATION_RECEIPT.json"
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base c527b71ce009a682d094ad735113c79113f7b5a1 --head HEAD
```

Stop if HEAD differs and the authority inputs changed, if tracked edits from
another task overlap scope, if an authority input is missing, or if the
pre-implementation gate reports an unresolved blocking failure.

## Source-Fidelity Pass

Existing paths verified: all four original Phase-03 files, all three local
Phase-03R review files, and every cited source-owner path exist at dispatch.

Planned new paths clearly marked as NEW: the four Phase-03R successors and one
worker return in the fulfillment manifest.

Canonical role/type values verified from: work-order template, dispatch prompt
envelope standard, and intake role routing standard.

Canonical template or pack IDs verified from: this work order and paired
GC-018 use batch ID `CVF-PHASE03R-MATERIALIZATION-T1`.

Runtime/source facts verified from current source or canonical contract: MAO
event/retention ownership, Guard capability admission/readiness, MCP invariant
baseline, and Model Gateway routing request shape.

Completion review facts used only when no runtime/source contract exists:
none.

Draft-only tokens that appear nowhere else in repo: the five NEW output paths.

Same-token collisions with different meaning: none found for the output names.

Any missing or ambiguous source fact: none blocking materialization; consumer
wiring remains an acceptance boundary, not an implementation claim.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS - MAO event ledger owner | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | line 155 | `MaoEventLedger` | MAO event-ledger contract | ACCEPT |
| EXISTS - event identity entry | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts` | line 53 | `MaoEventLedgerEntry` | MAO event-ledger contract | ACCEPT |
| EXISTS - retention decision | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | line 330 | `MaoRetentionDecision` | MAO evidence readout | ACCEPT |
| EXISTS - retention evaluation | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | line 347 | `evaluateRetention` | MAO evidence readout | ACCEPT |
| EXISTS - capability owner binding version | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts` | line 11 | `CAPABILITY_OWNER_BINDING_CONTRACT_VERSION` | capability-owner binding contract | ACCEPT |
| EXISTS - durable grant projection | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts` | line 60 | `CapabilityOwnerGrantProjection` | capability-owner binding contract | ACCEPT |
| EXISTS - grant binding function | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts` | line 121 | `bindCommittedCapabilityOwnerGrant` | capability-owner binding contract | ACCEPT |
| EXISTS - fail-closed readiness evaluation | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-route-readiness.contract.ts` | line 311 | `evaluateCapabilityReadiness` | capability route-readiness contract | ACCEPT |
| EXISTS - MCP protocol version | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.protocol.invariant.profile.ts` | line 2 | `MCP_PROTOCOL_VERSION_2026_07_28` | MCP protocol invariant profile | ACCEPT |
| EXISTS - MCP request profile | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.protocol.invariant.profile.ts` | line 36 | `MCPProtocolRequestProfile` | MCP protocol invariant profile | ACCEPT |
| EXISTS - MCP invariant evaluator | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.protocol.invariant.profile.ts` | line 162 | `MCPProtocolInvariantProfile` | MCP protocol invariant profile | ACCEPT |
| EXISTS - routing receives resolved policy | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy-pipeline.ts` | line 17 | `RoutingPolicyPipelineRequest` | Model Gateway routing pipeline | ACCEPT |
| EXISTS - routing pipeline entry | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy-pipeline.ts` | line 73 | `runRoutingPolicyPipeline` | Model Gateway routing pipeline | ACCEPT |

## Current Runtime Freshness Verification

Targeted searches at dispatch confirmed the MAO, Guard, MCP, and routing
symbols listed above. The work order does not claim that all downstream
consumers are wired. It requires the planning set to preserve the explicit
preimplementation and consumer-wiring gates from the local correction review.

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| Five output-path existence check | `Test-Path -LiteralPath` returned `False` for all five planned outputs before dispatch authoring | NEW_PATHS_CONFIRMED |
| Output-name collision search | targeted `rg` over `docs` and `.private_reference/legacy/CVF 05.09` found no pre-existing output artifact | NO_COLLISION |
| Collision decision | create exactly the five planned outputs; do not select alternate names | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap/correction requirement | Work-order coverage | Output evidence | Verification | Status |
|---|---|---|---|---|
| Complete successor planning set | Purpose; fulfillment manifest | four `03R_CVF_*` planning files | exact manifest and cross-link check | MAPPED |
| Preserve 38 WPs | Acceptance AC-01 | ledger and plan | unique WP parse = 38 | MAPPED |
| Preserve 68 backlog obligations | Acceptance AC-02 | ledger | unique backlog parse = 68, missing/extra/duplicate = 0 | MAPPED |
| Correct ARCH-009 disposition | Acceptance AC-03 | ledger, acceptance, plan | status and gate text search | MAPPED |
| Collapse ARCH-003 safely | Acceptance AC-04 | ledger, acceptance, dependency map | baseline symbol and redistributed criteria audit | MAPPED |
| Narrow MCP-001 | Acceptance AC-05 | all four outputs | lifecycle-only scope and one retained WP edge | MAPPED |
| Narrow GEN-001 | Acceptance AC-06 | ledger and acceptance | delta-audit/readmission wording | MAPPED |
| Reject ARCH-007 to ARCH-008 HARD edge | Acceptance AC-07 | dependency map and plan | edge absence plus acceptance seam | MAPPED |
| Correct DAG and waves | Acceptance AC-08 | dependency map | 51/39/12, topo 38, cycles 0, violations 0, waves 6/12/13/5/2 | MAPPED |
| Preserve source set | Acceptance AC-09 | worker return | before/after hashes | MAPPED |
| No implementation/readiness overclaim | Acceptance AC-10 | all outputs and return | reviewer claim-boundary inspection | MAPPED |

## Work-Order Fulfillment Manifest

| Artifact | Ownership | Required action |
|---|---|---|
| `.private_reference/legacy/CVF 05.09/03R_CVF_GLOBAL_IMPLEMENTATION_PLAN.md` | worker | NEW complete successor plan |
| `.private_reference/legacy/CVF 05.09/03R_CVF_IMPLEMENTATION_ACCEPTANCE_MATRIX.md` | worker | NEW complete 38-WP acceptance matrix |
| `.private_reference/legacy/CVF 05.09/03R_CVF_IMPLEMENTATION_DEPENDENCY_MAP.md` | worker | NEW corrected full dependency map and wave proof |
| `.private_reference/legacy/CVF 05.09/03R_CVF_IMPLEMENTATION_WORK_PACKAGE_LEDGER.md` | worker | NEW complete 38-WP/68-backlog ledger |
| `docs/reviews/CVF_PHASE03R_CANONICAL_PLANNING_MATERIALIZATION_WORKER_RETURN_2026-09-05.md` | worker | NEW no-commit evidence return |

Required proof literals: `38 / 38`, `68 / 68`, `51`, `39 HARD`, `12 SOFT`,
`DEPENDENCY CYCLES = 0`, `HARD WAVE VIOLATIONS = 0`,
`DEFERRED_PRIVATE_ONLY`, and `COMPLETE_PENDING_REVIEW` in the worker return.

## Required Materialization Rules

1. Start from the complete original files; do not reduce Phase-03R to a delta.
2. Preserve each WP ID and each primary backlog assignment exactly once.
3. Apply all local dispositions and exact baseline-owner bindings.
4. Keep original dependency reasons as downstream acceptance obligations when
   a WP edge becomes a non-WP baseline prerequisite.
5. Keep `WP-MCP-001 -> WP-MCP-006` HARD and explain lifecycle-only semantics.
6. Do not add `WP-ARCH-007 -> WP-ARCH-008`; record only a non-blocking
   configuration/routing convergence acceptance seam.
7. Preserve the original wave allocation and mark collapsed/blocked WPs as
   non-dispatch where applicable.
8. Include source authority, claim boundary, and public export disposition in
   every successor artifact.
9. Use ASCII for new prose unless an exact existing source literal requires a
   documented exception.
10. Do not copy unsupported external-agent owner wording over local evidence.
11. Every unchanged contract, acceptance row, test row, evidence row, gate,
    wave criterion, and registry section must be reproduced in the appropriate
    successor. A statement that content is unchanged or incorporated by
    reference is not a substitute for the content itself.

## Rework Round 1 Mandatory Findings

Prior finding-set digest: `ca19f6a93609924d57e2d537bc355af797e0d573146f48baa2a250e4668207ab`

| Finding ID | Blocking evidence | Required repair | Reverification |
|---|---|---|---|
| `F-01` | New ledger is 530 lines/35,496 bytes versus 3,419 lines/249,741 bytes; it has zero full `WP-*` contract headings versus 38 originally and labels its contract section `Local Phase-03R Delta Layer`. | Rebuild from the complete original ledger. Preserve all 38 full per-WP contract blocks and every original register; apply Phase-03R modifications in place. Remove incorporation-by-reference as a content substitute. | 38 full per-WP headings; field-by-field section preservation; local corrections integrated. |
| `F-02` | New acceptance matrix is 162 lines/9,820 bytes versus 240 lines/103,063 bytes; it contains only the six-row readiness overlay while five original 38-WP matrices are incorporated by reference. | Rebuild from the complete original acceptance matrix. Preserve every WP acceptance/test/security/migration/evidence row and integrate the six Phase-03R gates directly. | Compare every original matrix row/key against successor; no omitted row except an explicitly replaced row with mapped successor. |
| `F-03` | Dependency map Section 10 and global plan Waves 1-4/high-risk text delegate unchanged gate/entry/exit content back to original files. | Reproduce the exact unchanged content inside both successors and apply only the approved corrections. Cross-references may provide provenance but may not carry required semantics exclusively. | Search all four successors for omission phrases and verify each referenced semantic block is also present locally. |
| `F-04` | Worker return says all ACs pass and no corrective action is required although `F-01` through `F-03` violate the complete/self-contained successor contract. | Update the same worker return after repairing all four files. Record this rework round, before/after size/section evidence, the finding digest, and an honest final disposition. | Worker return must map and close `F-01` through `F-04`; rerun direct parse and worker-return gate. |

Canonical finding-set serialization used for the digest, UTF-8 and LF joined:

```text
F-01 successor WP ledger omits all 38 full per-WP contracts and substitutes incorporation by reference
F-02 successor acceptance matrix omits the original 38-WP acceptance/test/evidence matrices and substitutes incorporation by reference
F-03 successor dependency map and global plan omit exact unchanged gate/wave text by reference instead of remaining self-contained
F-04 worker return claims all acceptance criteria pass and no correction is required despite F-01 through F-03
```

Rework is confined to the same exact-five worker manifest. Do not create a
sixth artifact, modify authority inputs, or broaden Phase-03R decisions.

## Execution Plan

1. Capture execution HEAD, tracked status, and authority-input hashes.
2. Create the complete Phase-03R WP ledger first and reconcile all identifiers.
3. Create the corrected full dependency map and independently validate its DAG.
4. Create the full acceptance matrix from the corrected ledger and edge model.
5. Create the global implementation plan last so every summary count and wave
   points to the already reconciled subordinate artifacts.
6. Verify exact-five containment, unchanged authority hashes, structural gates,
   and worker-return shape; then stop without staging or committing.

## Acceptance Criteria

- AC-01: exactly 38 unique WP rows are present and cross-artifact consistent.
- AC-02: exactly 68 unique backlog IDs have one primary owner; no missing,
  extra, or duplicate primary mapping.
- AC-03: `WP-ARCH-009` is `MODIFY` with
  `PREIMPLEMENTATION_GATE_REQUIRED`, preserving its original edges.
- AC-04: `WP-ARCH-003` is collapsed; its three backlog obligations and
  security acceptance semantics are redistributed to exact existing owners.
- AC-05: `WP-MCP-001` owns lifecycle/deprecation enrichment only; seven former
  consumer edges use the current MCP invariant baseline.
- AC-06: `WP-GEN-001` requires a local delta audit for re-admission trigger and
  consumer wiring, not a duplicate admission system.
- AC-07: no direct WP edge exists from ARCH-007 to ARCH-008; both remain in
  original Wave 0 and the config/routing seam is non-blocking.
- AC-08: corrected graph is 51 edges = 39 HARD + 12 SOFT, 38/38 topological
  sort, zero cycles, zero HARD wave violations, waves 6/12/13/5/2.
- AC-09: four original Phase-03 files and three local correction artifacts are
  byte-identical before and after worker execution.
- AC-10: exactly five output paths change; no implementation, dispatch-ready,
  runtime, provider/live, public, commit, or push claim is made.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `.private_reference/legacy/CVF 05.09/03R_CVF_LOCAL_PHASE03R_VERIFICATION_RECEIPT.json`

priorVerificationAnchor: `c527b71ce009a682d094ad735113c79113f7b5a1`

freshRecomputeRequired: true

unicodePathHandling: use PowerShell literal paths and UTF-8-safe readers; keep
new authored prose ASCII unless a source literal requires an exception.

extractedTextAuthority: repository bytes, parsed tables, hashes, and local gate
output; OCR or screenshots are non-authoritative.

## Worker Autonomy / No-Question Rule

Proceed without operator confirmation for reads, exact-five edits, parsing,
hashing, DAG recomputation, formatting repair, and rerunning applicable local
gates. Escalate only when completion requires changing a forbidden path,
changing a local correction decision, expanding risk/effects, using external
services/secrets, committing, deleting, or overwriting authority evidence.

## Evidence Requirements

The worker return must provide command/result/path evidence for the execution
base, exact-five changed set, authority-input hashes before and after, all WP
and backlog counts, status counts, edge/hardness counts, topological result,
wave counts, applicable gate results, `git diff --check`, actual Git status,
no staging, no commit, and zero external calls. Narrative assertions without
the underlying command and result are insufficient.

## Verification Commands

After materialization, run equivalent deterministic checks that prove:

```powershell
git status --short
git diff --check
python governance/compat/check_markdown_structural_completeness.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_agent_packet_authority_and_encoding.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_agent_operation_trace.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_finding_to_governance_learning.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/run_worker_return_fast_gate.py
```

Because `.private_reference` is ignored, the worker must additionally run a
direct parser over the four Phase-03R outputs and report WP, backlog, status,
edge, hardness, topological, wave, and source-hash results. A Git-range checker
PASS alone is not evidence for ignored files.

## Review Gate

The reviewer/closer must independently inspect all four outputs, recompute the reconciliation
and DAG, verify source hashes and exact-five containment, and return `PASS` or
`CHANGES_REQUIRED`. Worker self-report is not canonical acceptance.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_PHASE03R_CANONICAL_PLANNING_MATERIALIZATION_WORKER_RETURN_2026-09-05.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

The return must include Purpose, Scope / Methodology, Findings / Position,
Risk / Corrective Action, Claim Boundary, Checker Source Read-Ahead Block,
Agent Operation Trace Block, Delta Execution Claim Boundary Control Block,
Public Export Disposition, executionBaseHead, actual `git status --short`,
changed files, reconciliation table, first/final gate results, hashes, and
no-commit/no-external-call evidence. Non-applicable conditional sections must
use `N/A with reason`.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when all AC rows pass and all repairable
in-scope gates pass. Return `BLOCKED_WITH_REASON` for authority drift,
unresolvable source contradiction, required forbidden-scope change, or a gate
failure that cannot be repaired inside exact-five scope.

Stop after return. Do not stage, commit, push, or begin Phase-04 work.

## Operator Checkpoint

No routine checkpoint is required during exact-five execution. A new operator
decision is mandatory for scope expansion, authority-decision reversal,
original-file overwrite, implementation work, provider/live/public action,
destructive action, or commit-mode change. Reviewer/closer acceptance is mandatory before
the Phase-03R successors may be treated as accepted canonical planning.

## Closure Checklist

- [x] Operator authority and GC-018 are cited.
- [x] Exact worker-owned and forbidden paths are explicit.
- [x] Roadmap/correction requirements map to observable evidence.
- [x] Source facts and exact symbols were verified before dispatch.
- [x] Worker autonomy, no-commit return, and reviewer conversion are explicit.
- [x] Live/provider/public/implementation claims are forbidden.

This checklist proves dispatch completeness only, not worker completion.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK

dispatchSurface: EXTERNAL_AGENT_CLI_MCP

parentAssignmentId: CVF-PHASE03R-MATERIALIZATION-T1

reviewRoundCount: 1

priorFindingSetDigest: ca19f6a93609924d57e2d537bc355af797e0d573146f48baa2a250e4668207ab

dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR

reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS

newIndependentCriticalEvidence: SEMANTIC_COMPLETENESS_F01_F04

regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT

cumulativeExternalInvocationCount: 1

externalInvocationCeiling: 2

usageAvailability: KNOWN_FOR_ADMISSION

quotaAdmissionDisposition: ADMITTED_WITHIN_CUMULATIVE_CEILING

nextDispatchDisposition: ONE_CONSOLIDATED_REWORK

rootCauseClusterId: phase03r-successor-by-reference-compression

reworkGeneration: 1

consolidatedDefectClassSweep: COMPLETE_BEFORE_REWORK_DISPATCH

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
  "problemKey": "cvf-phase03r-materialization-t1-problem",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": [],
    "reopened": [],
    "current": []
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`roadmap-materialization`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class roadmap-materialization --role dispatcher --lifecycle-phase pre-dispatch --surface-selector ".private_reference/legacy/CVF 05.09" --risk-ceiling MEDIUM --max-results 20 --json`

## Agent Handoff Contract Control Block

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher; delegated worker; independent reviewer/closer |
| phase | `T1_DISPATCH`, `T1_BUILD`, `T1_REVIEW`, `T1_CLOSE_OR_REWORK` |
| baseHeadFor(phase) | dispatchBaseHead=`c527b71ce009a682d094ad735113c79113f7b5a1`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exact-five worker output paths only |
| traceScope(phase, actor) | worker traces materialization; reviewer traces acceptance/closure |
| commitOwner(phase) | worker forbidden; reviewer decides later material/session-sync commits |
| crossBatchIsolation | all Phase-04 implementation and current active-session work remain separate |
| nextMoveSurfaces | unchanged until reviewer acceptance |

## Reviewer Closure Conversion Block

completionReviewPath: `docs/reviews/CVF_PHASE03R_CANONICAL_PLANNING_MATERIALIZATION_COMPLETION_2026-09-05.md`

reviewerOwnedClosurePaths:

- `docs/work_orders/CVF_AGENT_WORK_ORDER_PHASE03R_CANONICAL_PLANNING_MATERIALIZATION_FOR_CLAUDE_2026-09-05.md`
- `docs/reviews/CVF_PHASE03R_CANONICAL_PLANNING_MATERIALIZATION_WORKER_RETURN_2026-09-05.md`
- `docs/reviews/CVF_PHASE03R_CANONICAL_PLANNING_MATERIALIZATION_COMPLETION_2026-09-05.md`
- current active handoff/session state only if a separate session-sync decision is made

pendingStatusTokensAllowedBeforeReview: COMPLETE_PENDING_REVIEW, IMPLEMENTATION_COMPLETE_PENDING_REVIEW, DRAFT, HOLD_*

predecessorClosureFactSource: local Phase-03R correction review and verification receipt, not mutable session state alone

## Evidence Reuse And Encoding Plan Claim Boundary

Prior local verification may seed expected counts but cannot replace fresh
worker and reviewer recomputation. Ignored private files require direct path
hashing/parsing because ordinary Git changed-range discovery does not see them.

## Legacy Absorption Coverage Index Disposition

N/A with reason: this tranche does not absorb a new legacy corpus. It creates
successor planning artifacts from an already reconciled, explicitly bounded
legacy planning set and preserves the prior 68/68 mapping.

## Provider Memory Authority Boundary

Provider-specific memory and IDE context are execution aids only. They are not
CVF source authority. Every output claim must trace to the authority chain or
current repository source named in this work order.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | versioned private planning successors under the established `.private_reference/legacy/CVF 05.09/` family |
| Storage decision | create four `03R_CVF_*` successors beside, not over, the four original `03_CVF_*` planning files |
| Existing aggregate impact | none; no generated aggregate or index is changed by the worker |
| Generated state impact | none |
| Durable governance boundary | the tracked work order and worker return carry dispatch/evidence; private successors remain planning authority candidates until review |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | private Phase-03R planning-document materialization |
| claimDisposition | N/A with reason: no execution-control or runtime-enforcement claim is made |
| receiptEvidence | N/A with reason: the JSON input is a planning verification receipt, not a runtime execution receipt |
| actionEvidence | N/A with reason: file creation, hash, parse, graph, and local gate evidence are documentation proof only |
| invocationBoundary | local filesystem and repository commands |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, or runtime interception claim |
| claimLanguage | candidate canonical planning successor subject to post-execution reviewer evaluation |
| forbiddenExpansion | runtime implementation, Phase-04 dispatch, live/provider, public-sync, commit, push, deployment, and production readiness |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_finding_to_governance_learning.py` |
| literalTokensReviewed | Dispatch Prompt Envelope; Source Verification Block columns; Worker Autonomy / No-Question Rule; Review Gate; Closure Checklist; Return Conditions; Reviewer Closure Conversion Block; worker-return profile; Agent Operation Trace Block; Public Export Disposition |
| gateRunPurpose | confirmation/evidence after source-verified authoring, not first discovery of required shape |
| claimBoundary | read-ahead covers dispatch and expected worker-return shape only; direct parsing remains required for ignored private outputs |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-PHASE03R-MATERIALIZATION-T1 --title "Phase-03R Canonical Planning Materialization" --date 2026-09-05 --base c527b71c --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 2 --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced every placeholder with source-verified Phase-03R authority, scope, acceptance, and return evidence |
| checkerReadAheadConfirmation | applicable checker sources and template addenda were read before filing |
| docOnlyNewFields | none; tranche-specific labels are planning content, not runtime schema |
| claimBoundary | scaffold provenance only; helper output does not prove dispatch correctness |

## External Repository Absorption Entry Control

- Source type: reconciled external-agent planning return already converted into local CVF evidence
- Upstream or source-mirror disposition: no source mirror required; packet identity and member hashes are fixed in the local correction review
- Enumeration or manifest plan: reuse the verified five-member packet manifest and seven named local planning authorities
- Per-file terminal-ledger plan: reuse local review ledger; worker hashes all seven local authority inputs before and after
- Owner or overlap route: original Phase-03 owners plus exact MAO, Guard, MCP, and Model Gateway source bindings
- Value-disposition route: materialize accepted/adapted decisions; preserve rejected claims as explicit non-goals
- Claim boundary: no new external corpus intake or runtime absorption is authorized

## Mandatory Blind-Spot Control Block

- External-history blind spot: hidden agent context is not authority; only the hashed return and local review are used.
- Private-source blind spot: material claims were rechecked against current local source owners.
- Freshness blind spot: evidence is pinned to dispatch base `c527b71ce009a682d094ad735113c79113f7b5a1`.
- Coverage blind spot: the bounded authority set is not a full repository corpus scan.
- Runtime blind spot: planning materialization does not prove consumer wiring or implementation.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent returned output |
| Chain map route | external return to local source verification to planning materialization |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; local correction review plus exact owner-symbol verification |
| Owner surface | four candidate Phase-03R planning successors |
| Disposition | ADAPT_WITH_LOCAL_CORRECTIONS |
| Claim boundary | worker receives no authority to reopen external review or change accepted local decisions |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`; `cvf.external-agent-round-trip@1.2.0` |
| Input root or repository | hashed Phase-03R packet represented by the local correction review |
| Enumeration command | reuse verified packet manifest; run `rg --files --hidden --no-ignore -- ".private_reference/legacy/CVF 05.09"` and filter the seven named local authority artifacts |
| Manifest artifact or inline manifest | `.private_reference/legacy/CVF 05.09/03R_CVF_LOCAL_PHASE03R_VERIFICATION_RECEIPT.json` |
| Processing ledger artifact or inline ledger | `.private_reference/legacy/CVF 05.09/03R_CVF_LOCAL_PHASE03R_CORRECTION_REVIEW.md` packet ledger |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `.private_reference/legacy/CVF 05.09/03R_CVF_LOCAL_PHASE03R_CORRECTED_EDGE_DELTA.md` |
| Unresolved items | four successor artifacts and independent post-execution acceptance |
| Absorption maturity | SOURCE_RECONCILED |
| Named runtime consumer | NONE_PLANNING_ONLY |
| Integration evidence | N/A with reason: no runtime integration is authorized |
| Use proof | local correction review, corrected edge delta, and verification receipt |
| Operator checkpoint | scope or authority-decision change only; normal next review is the worker return |
| Absorption completion status | ABSORPTION_NOT_COMPLETE |
| Completion claim boundary | source reconciliation is complete; planning materialization and any implementation remain unclosed |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| Accepted local Phase-03R corrections | exact status, edge, wave, and owner decisions | DOCTRINE_ADAPTED | four Phase-03R planning successors | materialize in this bounded worker tranche | documentation only |
| Package potential | no package need identified | PACKAGE_CANDIDATE | separate future package work order if evidence emerges | keep closed in this tranche | no package creation or activation |
| Runtime potential | implementation needs remain represented by WPs | RUNTIME_CANDIDATE | future WP-specific work orders | keep parked until Phase-03R acceptance | no runtime mutation |
| Checker potential | direct parser is needed for ignored planning files | CHECKER_CANDIDATE | worker-return verification only | run an ephemeral deterministic parser; do not add a checker | no checker mutation |
| Unsupported direct config-to-routing edge | no exact consumer wiring | REJECT_DIRECT_IMPORT | Phase-03R dependency map | omit the WP edge and retain a non-blocking seam | no runtime claim |
| External checklist prose | review aid with no independent package/runtime value | NO_PACKAGE_OR_RUNTIME_VALUE | local review provenance | retain as evidence only | no package or runtime action |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| broad authority WP | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts` | CONFIRMED_EXISTING | acceptance redistribution and consumer binding | ADAPT into Phase-03R |
| signed event/persistence WP | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/event.ledger.contract.ts`; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts` | ENRICH_EXISTING | signing, durable atomic persistence, replay, and deletion gate | ADAPT into Phase-03R |
| direct config-to-routing dependency | `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy-pipeline.ts`; `EXTENSIONS/CVF_MODEL_GATEWAY/src/sticky-session.ts` | REJECT_DIRECT_IMPORT | no proven WP dependency | omit edge |
| MCP core/lifecycle | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mcp.protocol.invariant.profile.ts` | ENRICH_EXISTING | lifecycle/deprecation only | narrow WP scope |

## Corpus Completeness And Report Integrity

- Corpus task class: bounded planning-authority reuse
- Corpus root: seven named Phase-03 and local Phase-03R authority artifacts
- Snapshot time: 2026-09-05 dispatch authoring
- Enumeration command: `rg --files --hidden --no-ignore -- ".private_reference/legacy/CVF 05.09"` followed by exact seven-name filtering, literal-path hashes, and targeted table parsing
- Manifest artifact or inline manifest: Authority Chain and Work-Order Fulfillment Manifest
- Manifest hash: N/A with reason: no new aggregate corpus manifest is created
- Processing ledger artifact or inline ledger: Source Verification Block and local correction-review ledger
- Allowed terminal statuses: READ | ADAPTED | DEFERRED | REJECTED | NO_NEW_VALUE | BLOCKED_UNREADABLE | SKIPPED_WITH_REASON
- Reconciliation: manifest=7; ledger_terminal=7; exclusions=0 within named scope; unresolved=0
- Unresolved files: 0
- Declared exclusions: full repository corpus scan and any new external intake
- Unreadable or unsupported files: none
- Aggregation check: PASS for the bounded named set
- Drift check: worker must prove before/after byte identity at the pinned base
- Output traceability: four successors trace to the original set and local correction overlay
- Adversarial verification: unsupported ownerless and direct-HARD-edge claims remain rejected
- Corpus verdict: PARTIAL

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/work-order author |
| Provider or surface | local CVF workspace |
| Session or invocation | Phase-03R materialization work-order authoring, 2026-09-05 |
| Working directory | repository root |
| Command or tool surface | local reads, `rg`, ADIF resolver, scaffold preview, apply_patch, dispatch gates |
| Target paths | paired GC-018 baseline and this work order |
| Allowed scope source | operator instruction dated 2026-09-05 |
| Before status evidence | HEAD `c527b71ce009a682d094ad735113c79113f7b5a1`; tracked worktree clean |
| After status evidence | exactly two dispatch artifacts created pending gate validation |
| Diff evidence | `git status --short`; `git diff --name-status` |
| Approval boundary | dispatch authoring only; delegated worker owns exact-five materialization |
| Claim boundary | no worker materialization, implementation, provider/live/public action, commit, or push |
| Agent type | dispatcher |
| Invocation ID | `cvf-phase03r-materialization-t1-work-order-2026-09-05` |
| Expected manifest | `docs/baselines/CVF_GC018_PHASE03R_CANONICAL_PLANNING_MATERIALIZATION_2026-09-05.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_PHASE03R_CANONICAL_PLANNING_MATERIALIZATION_FOR_CLAUDE_2026-09-05.md` |
| Actual changed set | `docs/baselines/CVF_GC018_PHASE03R_CANONICAL_PLANNING_MATERIALIZATION_2026-09-05.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_PHASE03R_CANONICAL_PLANNING_MATERIALIZATION_FOR_CLAUDE_2026-09-05.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in dispatch authoring |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: Phase-03R targets private provenance planning files only.

## Claim Boundary

This work order authorizes the delegated worker to create four complete candidate canonical
Phase-03R planning successors and one evidence return. It does not authorize
overwriting Phase-03, implementing any WP, modifying runtime/source/tests,
calling providers, using secrets/quota, staging/committing/pushing, deployment,
public export, or any closed/readiness claim before reviewer/closer acceptance.

## Acceptance Receipt Assertion Matrix

| Required value | Observed value | Status |
|---|---|---|
| Verification receipt authority inputs | seven exact input hashes unchanged | PASS |
| Corrected dependency registry | 51 edges = 39 HARD + 12 SOFT | PASS |
| Corrected wave distribution | 6 / 12 / 13 / 5 / 2 | PASS |
| Worker-return status | `COMPLETE_PENDING_REVIEW`, accepted by independent reviewer | PASS |
| Public export evidence | N/A with reason: private-only closure | N/A_WITH_REASON |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_PHASE03R_CANONICAL_PLANNING_MATERIALIZATION_FOR_CLAUDE_2026-09-05.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_PHASE03R_CANONICAL_PLANNING_MATERIALIZATION_COMPLETION_2026-09-05.md` | independent reviewer decision and direct comparison evidence | PASS |
| Roadmap state | N/A | bounded standalone local planning materialization has no owning repository roadmap row | N/A with reason |
| Registry JSON | N/A | no GC-051 registry update was authorized in the exact closure manifest | BLOCKED with reason: registry admission requires a separate governed tranche |
| Registry Markdown | N/A | no GC-051 registry update was authorized in the exact closure manifest | BLOCKED with reason: registry admission requires a separate governed tranche |
| External evidence digest | local correction review and receipt | SHA-256 `b51d66c5ee664e878ed538cad3d3eb2786a22f1ee2a0a36b6b8770cbaf780d0f`; receipt SHA-256 `c734565d69cc9e03639a019aa6d9d8f5e124bd2695ca98d4675e6f7089759824` | PASS |
| System loop interlock | N/A | documentation-only planning closure changes no runtime or cross-loop machine input | N/A with reason |
| Session continuity | active front door/state/handoff | independent lane changes neither current mode nor next allowed move | N/A with reason |
