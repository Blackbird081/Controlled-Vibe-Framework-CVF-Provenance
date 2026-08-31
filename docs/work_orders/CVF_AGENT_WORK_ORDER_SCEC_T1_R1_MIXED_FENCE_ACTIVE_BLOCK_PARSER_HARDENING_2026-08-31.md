# CVF Agent Work Order - SCEC-T1-R1 Mixed-Fence Active-Block Parser Hardening

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Batch ID: SCEC_T1_R1_MIXED_FENCE_ACTIVE_BLOCK_PARSER_HARDENING

Dispatch base head: `8b5ae0d144c498cbaf492ec21352c947568a2a56`

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

Worker: one operator-mediated external governance implementation worker

Reviewer/closer: local orchestrator/reviewer

Worker return path: `docs/reviews/CVF_SCEC_T1_R1_MIXED_FENCE_ACTIVE_BLOCK_PARSER_HARDENING_WORKER_RETURN_2026-08-31.md`

## Dispatch Prompt Envelope

Role: external governance implementation worker for SCEC-T1-R1.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_SCEC_T1_R1_MIXED_FENCE_ACTIVE_BLOCK_PARSER_HARDENING_2026-08-31.md`.

Paired baseline: `docs/baselines/CVF_GC018_SCEC_T1_R1_MIXED_FENCE_ACTIVE_BLOCK_PARSER_HARDENING_2026-08-31.md`.

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture the full current HEAD at start.

Current-time notes: packet authored on 2026-08-31 from committed SCEC-T1
closure and a fresh local mixed-fence reproducer.

Do-not-misread notes: repair only SCEC fenced-block discovery and focused
regressions. Do not change semantic thresholds, progression outcomes, product
code, runtime behavior, provider/live surfaces, session state, or public files.

Required first actions: read startup continuity, guard orientation, literal
gotchas, paired packet, SCEC standard, checker and complete focused test file,
ADIF-0055, and every checker named in read-ahead before editing.

Return contract: change exactly the four authorized paths, run every required
gate after the last edit, leave all changes uncommitted, and return
`COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Purpose

Replace or correct the active-block extraction mechanism so an ordinary
closing fence can never be treated as a new opening fence. Prove that a valid
SCEC JSON block is found exactly once when other fenced blocks occur before or
after it, without weakening marker immunity or malformed-block handling.

## Semantic Convergence Outcome

Standard: `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "scec-mixed-fence-active-block-detection",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": ["mixed-fence-parser-skips-valid-active-block"],
    "reopened": [],
    "current": ["mixed-fence-parser-skips-valid-active-block"]
  },
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [
    {
      "claimId": "mixed-fence-parser-defect-reproduced",
      "claimClass": "DOCUMENTATION_ONLY",
      "proofClass": "PROPOSAL_ONLY_NO_RUNTIME_READINESS",
      "evidenceRef": "docs/baselines/CVF_GC018_SCEC_T1_R1_MIXED_FENCE_ACTIVE_BLOCK_PARSER_HARDENING_2026-08-31.md#root-problem"
    }
  ],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

The worker return must be successor ordinal one, bind the exact raw SHA-256 of
this work order, copy predecessor `current` into successor `prior`, resolve the
named blocker only with executable focused-test evidence, and use
`READY_WITH_EXECUTABLE_PROOF / EXECUTABLE_IMPLEMENTATION` only when all required
tests and gates pass.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: EXTERNAL_AGENT_CLI_MCP
parentAssignmentId: SCEC-T1-R1
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

## Scope / Target / Owner Boundary

Allowed:

- repair active fenced-JSON discovery in the existing SCEC checker;
- add focused tests for the direct reproducer and adjacent boundaries;
- update ADIF-0055 with this observed failure and prevention;
- create the exact worker return;
- make bounded refactoring needed only to keep the checker under file-size
  limits while preserving behavior.

Forbidden:

- changing SCEC schema fields, thresholds, blocker algebra, claim/proof mapping,
  dispositions, successor scopes, activation boundary, or required surface set;
- editing standards, catalogs, scaffolds, fixtures, session state, handoff, any
  product/runtime file, or any path outside the exact manifest;
- weakening, bypassing, skipping, or conditionally suppressing an existing
  gate;
- provider/API/network/live action, secrets, public sync, deploy, production,
  staging, commit, push, or destructive action.

Risk ceiling: `R2_PROTECTED_GOVERNANCE_PATH_LOCAL_REVERSIBLE`.

## Authority Chain

- Operator direction: turn exposed foundation gaps into CVF controls and
  harden before continuing product work.
- Material closure: `bd4ac2882482a9c38c4e8b97d1cae265028c4368`.
- Continuity closure: `8b5ae0d144c498cbaf492ec21352c947568a2a56`.
- Paired GC-018 baseline: named above.
- Active SCEC standard and checker: named in required reads.
- Active handoff: `AGENT_HANDOFF_V59_2026-08-11.md`.

Any contradiction requiring a semantic contract change or an extra path is a
hard stop and must be returned to the orchestrator.

## Agent Roles

- Dispatcher: local orchestrator/reviewer.
- Implementer: one external governance worker.
- Reviewer/closer/committer: local orchestrator/reviewer independently.
- Operator checkpoint: scope expansion, semantic change, public/live/runtime
  authority, destructive action, or new problem-chain release.

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
2. `CVF_SESSION_MEMORY.md`
3. `AGENT_HANDOFF_V59_2026-08-11.md`
4. `docs/reference/guard_orientation/README.md`
5. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
6. paired baseline and this work order
7. `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`
8. complete `governance/compat/check_semantic_convergence_control.py`
9. complete `governance/compat/test_check_semantic_convergence_control.py`
10. `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0055.md`
11. each applicable checker in Checker Source Read-Ahead Block

## Pre-Flight Checks

Before editing, capture full HEAD and status, verify the worker-return path is
absent, then run the pre-implementation autorun gate and focused SCEC suite.
Stop on undisclosed drift or a source contradiction.

## Task Governance Routing Manifest

```json
{
  "schemaVersion": "cvf.taskGovernanceManifest.v1",
  "taskId": "SCEC-T1-R1",
  "requestedProfile": "P3_ELEVATED",
  "classification": {
    "taskKind": "PURE_LOCAL_IMPLEMENTATION",
    "authorityImpact": "CREATES_OR_CHANGES_AUTHORITY",
    "externalEffect": "NONE",
    "dataSensitivity": "PRIVATE_REPO",
    "reversibility": "GIT_REVERSIBLE",
    "sourceScale": "BOUNDED_CLUSTER",
    "delegation": "MULTI_ROLE_NO_COMMIT",
    "novelty": "KNOWN_PATTERN"
  },
  "pathFamilies": ["docs/baselines", "governance/compat", "docs/reference", "docs/reviews"],
  "claims": ["mixed-fence active-block extraction repair"],
  "requiredProof": [
    "direct reproducer regression",
    "mixed-fence ordering variants",
    "marker-immunity preservation",
    "malformed-block preservation",
    "all prior focused tests",
    "independent reviewer closure"
  ],
  "operatorCheckpoints": [
    "semantic contract change",
    "extra protected path",
    "runtime or provider action",
    "public sync or deployment"
  ],
  "forbiddenEffects": [
    "semantic threshold change",
    "product or runtime edit",
    "provider or live execution",
    "public sync or deployment",
    "worker staging or commit"
  ],
  "sourceEvidence": {
    "selectedFilesFullyRead": true,
    "corpusReceiptRef": null,
    "completenessClaimChanged": false
  }
}
```

## Intake Role Routing Decision

routeMode: MULTI_AGENT_MULTI_ROLE

intakeSummary: one bounded protected-governance parser and regression repair

scopeClassification: PROTECTED_GOVERNANCE_IMPLEMENTATION_NO_EXTERNAL_EFFECT_NO_COMMIT

riskSensitivity: high because the defect creates a false missing-control result
on valid governed work orders

escalationCondition: semantic change, required extra path, source contradiction,
guard weakening, product/runtime work, provider/live need, or dirty overlap

## Work-Order Fulfillment Manifest

| Artifact | Required action | Required proof |
|---|---|---|
| `governance/compat/check_semantic_convergence_control.py` | MODIFY | structural fence extraction; no closing fence as opener; prior semantics preserved |
| `governance/compat/test_check_semantic_convergence_control.py` | MODIFY | direct reproducer plus ordering, immunity, malformed and full regression tests |
| `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0055.md` | MODIFY | observed defect, root cause, prevention and checker binding |
| `docs/reviews/CVF_SCEC_T1_R1_MIXED_FENCE_ACTIVE_BLOCK_PARSER_HARDENING_WORKER_RETURN_2026-08-31.md` | CREATE | complete no-commit evidence and valid successor SCEC block |

Expected changed set: exactly four paths. Every other path is forbidden.

## Write Ownership

Worker owns exactly the four fulfillment-manifest paths. The existing checker,
focused test, and ADIF entry may be modified; the worker return may be created.
No other file may be modified, created, deleted, renamed, staged, or committed.

## Execution Plan

1. Capture execution base and clean status; run pre-implementation gates.
2. Add the direct failing mixed-fence regression before changing extraction.
3. Implement the smallest structural parser repair.
4. Add the remaining order/immunity/malformed regression cases.
5. Update ADIF-0055 with observed root cause and prevention.
6. Create a valid successor worker return and run every final command.
7. Return four uncommitted paths for independent review.

Each step stops on a semantic-contract change, extra required path, source
contradiction, or forbidden external effect.

## Implementation Requirements

1. Add a failing regression that models a governed work order with a non-JSON
   fenced block before one valid active SCEC JSON block.
2. Prove the pre-repair behavior would return zero active blocks or the
   equivalent missing-block violation.
3. Implement a structural fence scanner or an equally explicit parser that
   distinguishes opening fences from closing fences. Do not rely on fence
   pairing side effects.
4. Support at least untagged JSON and `json`-tagged JSON as the current contract
   requires. Ignore non-JSON fenced bodies unless they parse as a real active
   SCEC object under the existing activation rule.
5. Preserve immunity for inline/backticked schema mentions, table cells, and
   non-active JSON objects.
6. Preserve fail-closed validation once a real active block is found.
7. Cover non-JSON fence before, after, and on both sides of the SCEC block;
   multiple ordinary fenced blocks; untagged active JSON; quoted marker; and
   malformed active candidate behavior already owned by the suite.
8. Keep the checker and focused test files within governed Python hard limits.
9. Update ADIF-0055 without broadening its claim beyond observed evidence.

## Evidence Requirements

- Record the exact direct reproducer input and pre-repair result.
- Map the parser change to every new focused test.
- Record the complete focused-suite count after the final edit.
- Prove quoted marker immunity and malformed-block behavior were not weakened.
- Record Python size, compile, direct checker, worker-fast, diff and status
  results after the last material edit.
- Record the exact work-order raw SHA-256 used by the successor SCEC block.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Regex treats a closing fence as a possible opener | source behavior | `governance/compat/check_semantic_convergence_control.py` | `CODE_FENCE_JSON_RE` | `CODE_FENCE_JSON_RE` | SCEC checker | ACCEPT |
| Extraction iterates regex matches then parses captured bodies | source behavior | `governance/compat/check_semantic_convergence_control.py` | `find_active_blocks` | `find_active_blocks` | SCEC checker | ACCEPT |
| Valid active block requires a real fenced JSON object | contract | `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md` | Activation Sentinel | `CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md` | SCEC control plane | ACCEPT |
| Existing focused suite is the regression owner | test ownership | `governance/compat/test_check_semantic_convergence_control.py` | active-block extraction cases | `ValidInitialChainBlockTests` | SCEC focused tests | ACCEPT |
| ADIF-0055 is the semantic convergence defect record | learning ownership | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0055.md` | full entry | `CVF_ADIF-0055.md` | ADIF registry | ACCEPT |

Refresh line evidence at execution base. Do not cite provider-local summaries.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_SCEC_T1_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_FOUNDATION_WORKER_RETURN_2026-08-31.md`

priorVerificationAnchor: `bd4ac2882482a9c38c4e8b97d1cae265028c4368`

freshRecomputeRequired: yes

unicodePathHandling: literal repository-relative paths and UTF-8-safe readers;
new prose and test names use ASCII

extractedTextAuthority: current local CVF-governed source only; provider memory
or side-channel text is not authority

## Legacy Absorption Coverage Index Disposition

| Field | Value |
|---|---|
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Reason | This is a current active-checker regression repair based on a direct local reproducer. It does not intake, migrate, map, or claim coverage of any legacy corpus or workflow chain. |
| Coverage index | N/A with reason: no legacy source is in scope. |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External-agent packet request |
| Chain map route | external-agent review front door, governed work order, uncommitted return, independent local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | paired SCEC-T1-R1 baseline and this work order |
| Disposition | PACKET_READY |
| Claim boundary | the future worker return is non-authoritative until independent local review; no external source, corpus, provider output, or public artifact is promoted automatically |

## ADIF Defect Registry Disclosure

- Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 30 --json`
- Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
- Returned defects: `ADIF-0001`, `ADIF-0002`, `ADIF-0006`, `ADIF-0007`,
  `ADIF-0014`, `ADIF-0015`, `ADIF-0016`, `ADIF-0017`, `ADIF-0020`,
  `ADIF-0021`, `ADIF-0024`, `ADIF-0028`, `ADIF-0029`, `ADIF-0031`,
  `ADIF-0033`, `ADIF-0039`, `ADIF-0043`, `ADIF-0044`, `ADIF-0045`,
  `ADIF-0049`, `ADIF-0051`, `ADIF-0052`.
- Resolver truncation: `false`.
- Additional directly applicable entry: `ADIF-0055`.
- Disposition: `APPLIED` through bounded protected paths, exact test contract,
  source read-ahead, no-commit split, and independent review.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_closure_packaging_preflight.py`; `governance/compat/check_python_automation_size.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_adif_entry_integrity.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Commit mode: WORKER_MUST_NOT_COMMIT`; prompt envelope fields; Work-Order Fulfillment Manifest; source-verification columns and bare dispositions; exact SCEC block; core authorization labels and protected paths; worker-return profile and no-commit terms; Python hard-size limits |
| gateRunPurpose | Confirm the source-derived bounded repair and final evidence, not discover required shape. |
| claimBoundary | Parser extraction repair only; no semantic threshold, product/runtime, provider/live, or public claim. |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id SCEC-T1-R1 --title "Mixed-Fence Active-Block Parser Hardening" --date 2026-08-31 --base 8b5ae0d14 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface EXTERNAL_AGENT_CLI_MCP --review-round-count 0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 1 --scec-problem-key scec-mixed-fence-active-block-detection --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --stdout` |
| generatedProfile | protected-governance-path, no-commit external-worker dispatch |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Replaced generic placeholders with exact reproducer, four-path manifest, parser contract, regression matrix and self-protection authorization. |
| checkerReadAheadConfirmation | Applicable checker sources were inspected before authoring. |
| docOnlyNewFields | N/A with reason: no new contract field is introduced. |
| claimBoundary | Dispatch provenance only; no implementation result claimed. |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: repair only SCEC fenced active-block
discovery, focused regressions, and the directly owning ADIF entry.

Protected paths:

- `governance/compat/check_semantic_convergence_control.py`
- `governance/compat/test_check_semantic_convergence_control.py`

Operator authorization: operator explicitly instructed CVF foundation
hardening and correction whenever following tranches expose ineffectiveness.

Rollback boundary: reject or revert only the exact four-path worker batch; do
not rewrite SCEC-T1 closure commits or any GC010 historical evidence.

Not authorized: standard semantics, hook catalogs, scaffold changes, session
state, product/runtime edits, provider/live, public sync, deployment,
production, worker staging or commit.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | one external governance worker; independent local reviewer/closer |
| phase | committed dispatch to uncommitted worker return |
| baseHeadFor(phase) | dispatchBaseHead=`8b5ae0d144c498cbaf492ec21352c947568a2a56`; executionBaseHead=worker capture; closureBaseHead=reviewer capture |
| changedSetScope(phase) | exact four-path fulfillment manifest |
| traceScope(phase, actor) | worker records reproducer, tests, gates, status and no-commit evidence; reviewer independently probes mixed fences |
| commitOwner(phase) | reviewer/closer only |
| crossBatchIsolation | no unrelated edit, staging, commit or provider-local file |
| nextMoveSurfaces | continuity changes only after accepted material commit |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SCEC_T1_R1_MIXED_FENCE_ACTIVE_BLOCK_PARSER_HARDENING_COMPLETION_2026-08-31.md` (optional; prefer reviewer correction inside worker return when sufficient) |
| reviewerOwnedClosurePaths | exact four-path returned diff; continuity separately authorized after material commit |
| closureOwner | local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

Reviewer must independently run a direct mixed-fence probe not copied from the
worker test, verify no semantic validation branch changed, and rerun the full
focused suite and governance gates.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_SCEC_T1_R1_MIXED_FENCE_ACTIVE_BLOCK_PARSER_HARDENING_WORKER_RETURN_2026-08-31.md`
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Decision / Disposition; Source Inventory;
Source Verification Block; Checker Source Read-Ahead Block; External Knowledge
Intake Routing; Rescan Intelligence Hardening; Epistemic Process Block; Agent
Operation Trace Block; Delta Execution Claim Boundary Control Block; Core Guard
Self-Protection Authorization; Semantic Convergence Outcome; Public Export
Disposition; executionBaseHead; git status --short; Changed Files; No-Commit
Statement; Claim Boundary.

Use `N/A with reason` for non-applicable conditional blocks.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: a structural fence scanner will find exactly one
active SCEC block in the direct reproducer while preserving all existing test
behavior.

Evidence Comparison Requirement: record pre-repair reproducer behavior and
post-repair focused/full-suite results.

Contradiction Handling Requirement: identify any fence syntax or legacy test
whose contract cannot be preserved without broader semantics and stop.

Claim Update Requirement: report whether the parser defect is fixed, narrowed,
or remains unresolved.

## System Loop Interlock Routing

- Governance plane: `SEMANTIC_PROGRESSION_CONTROL`.
- Repair lane: active-block extraction only.
- Duplicate-control prohibition: do not create a second parser/checker or move
  semantic validation into another plane.
- Runtime interlock: none; product/runtime execution remains parked.

## Foundation Storage Layout Block

- Repair the existing checker and focused test owner in place.
- Update the existing ADIF-0055 entry in place.
- Store the return only at the exact named review path.
- Do not create helper modules, new standards, fixtures, catalogs, or state.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | local orchestrator/dispatcher |
| Provider or surface | local private provenance workspace |
| Session or invocation | SCEC-T1-R1 dispatch authoring, 2026-08-31 |
| Working directory | repository root |
| Command or tool surface | governed reads, direct parser probe, ADIF resolver, apply_patch, local governance gates |
| Target paths | paired GC-018 baseline and this work order |
| Allowed scope source | operator foundation-hardening instruction and observed SCEC-E1 pre-dispatch failure |
| Before status evidence | HEAD `8b5ae0d144c498cbaf492ec21352c947568a2a56`; clean worktree |
| After status evidence | exactly two dispatch artifacts pending validation and commit |
| Diff evidence | `git status --short --untracked-files=all` and `git diff --check` |
| Approval boundary | bounded repair packet authoring and dispatch only |
| Claim boundary | local reproducer and dispatch evidence; no worker implementation result claimed |
| Agent type | orchestrator/dispatcher |
| Invocation ID | `scec-t1-r1-dispatch-2026-08-31` |
| Expected manifest | paired baseline and work order only |
| Actual changed set | paired baseline and work order only |
| Manifest delta | MATCH pending final gate confirmation |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | local SCEC mixed-fence extraction repair and regression proof |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no provider or runtime receipt applies. |
| actionEvidence | ACTION_EVIDENCE_PRESENT: checker diff, focused tests, local command output and worker return |
| invocationBoundary | four authorized repository files only |
| interceptionBoundary | no IDE, shell, filesystem, provider, runtime, wrapper or agent-action interception claim |
| claimLanguage | correct local fenced-block parsing under mixed markdown fences |
| forbiddenExpansion | semantic threshold change, product/runtime work, provider/live, public sync, deploy, production, worker commit |

## Verification Commands

Run after the last material edit:

```powershell
python -m unittest governance.compat.test_check_semantic_convergence_control
python governance/compat/check_semantic_convergence_control.py
python governance/compat/check_python_automation_size.py --enforce
python -m py_compile governance/compat/check_semantic_convergence_control.py governance/compat/test_check_semantic_convergence_control.py
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
```

## Acceptance Criteria

- [ ] Exact four-path worker manifest and no other change.
- [ ] Direct mixed-fence reproducer passes and returns exactly one active block.
- [ ] Before/after/both-side and multiple-fence order variants pass.
- [ ] Untagged and `json`-tagged active objects remain supported.
- [ ] Quoted/table/non-active markers remain immune.
- [ ] Malformed and incomplete real active blocks remain fail-closed under the
  existing contract.
- [ ] All prior focused SCEC tests pass without semantic expectation changes.
- [ ] Python hard-size and compile checks pass.
- [ ] Worker-return fast gate and diff check pass after final edit.
- [ ] Worker return has a valid successor block bound to this work order.
- [ ] HEAD unchanged; nothing staged or committed by worker.

Fail conditions: semantic vocabulary or threshold changes, test weakening,
missing direct reproducer, an extra path, unresolved hard-size violation,
failed required gate, or any forbidden external/product action.

## Review Gate

Worker completion is not closure. Reviewer must inspect the parser algorithm,
run an independent mixed-fence probe and the full focused suite, verify exact
scope and no semantic drift, then repair/reject or commit. Continuity is a
separate later commit.

## Operator Checkpoint

No operator checkpoint is needed for repair and rerun inside the exact four
paths. Stop for operator direction only if completion requires a semantic SCEC
change, an additional path, product/runtime authority, provider/live action,
public sync, deployment, production, destructive action, or risk-ceiling
increase.

## Closure Checklist

- [ ] No placeholders or stale gate evidence.
- [ ] All final commands rerun after the last edit.
- [ ] Exact work-order raw SHA-256 used in successor block.
- [ ] Four-path status and no-commit evidence recorded.
- [ ] Reviewer disposition pending, not self-closed.

## Return-To-Orchestrator Conditions

Return only for a semantic-contract contradiction, required extra path,
unrecoverable gate failure outside scope, or authority conflict. Repair routine
test, lint, citation, literal and return-shape failures within scope.

## Worker Autonomy / No-Question Rule

Implement the bounded parser/test repair without asking preference questions.
Do not broaden scope or redesign SCEC. If structural parsing cannot satisfy the
current contract, return exact evidence instead of weakening the gate.

## Claim Boundary

This work order authorizes a local parser correctness repair. Passing tests
prove the named fenced-block behaviors only; they do not prove semantic truth,
GC010 product readiness, runtime behavior, provider/live execution, public
readiness, deployment, or production.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance governance repair with no public-sync authority.
