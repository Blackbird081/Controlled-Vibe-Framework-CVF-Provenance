# CVF Agent Work Order - RSE-T4-H1-R1 Acceptance Chain Root Correction

Memory class: FULL_RECORD

Status: APPROVED_FOR_EXECUTION

Date: 2026-09-28

Batch ID: RSE-T4-H1-R1

Execution base: `cf0bbc1b2`

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

dispatchSurface: INTERNAL_AGENT

assignedRole: Local implementation worker, then phase-separated Local reviewer/closer

commitMode: WORKER_MUST_NOT_COMMIT_UNTIL_REVIEW_PHASE

mission: implement the ADIF-0062 acceptance chain and the retained ADIF-0061
recovery contract; prove the complete route with hostile fixtures; keep NCR
parked.

authorityCeiling: local reversible governance files and tests only

returnRoute: Local phase-separated review; no Claude dispatch and no operator
technical question

## Purpose

Implement one end-to-end acceptance chain joining dispatcher-owned required
deliverables to Git-observed artifacts, bound proof and a deterministically
reduced worker terminal status. Restore the tool/classifier recovery semantics
that H1 attempted, while treating its four false negatives as hostile fixtures
rather than the complete problem.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id RSE-T4-H1-R1 --title "Acceptance Chain Root Correction" --date 2026-09-28 --base cf0bbc1b2 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id RSE-T4-ACCEPTANCE-CHAIN-JOIN --prior-finding-set-digest 532e49a72 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence ADIF-0062 --scec-problem-key RSE-T4-ACCEPTANCE-CHAIN-JOIN --scec-chain-mode SUCCESSOR --scec-chain-ordinal 1 --scec-predecessor-path docs/reviews/CVF_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ENFORCEMENT_COMPLETION_2026-09-28.md --scec-predecessor-sha256 FILL_AFTER_SOURCE_READ --scec-required-disposition ROOT_CONTRACT_REQUIRED --scec-successor-scope NO_SUCCESSOR --stdout` |
| generatedProfile | protected-governance-path, internal Local execution |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | root contract, exact ledger/path/proof scope and phase-separated review |
| checkerReadAheadConfirmation | named gates inspected before packet authoring |
| docOnlyNewFields | strict acceptance-ledger JSON and RSE recovery fields |
| claimBoundary | scaffold provenance only |

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"RSE-T4-ACCEPTANCE-CHAIN-JOIN","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["missing end-to-end acceptance join"],"reopened":[],"current":["missing end-to-end acceptance join"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":1,"sameClaimCorrections":1,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"RSE-T4-ACCEPTANCE-CHAIN","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0062.md"}],"requiredDisposition":"ROOT_CONTRACT_REQUIRED","successorScope":"NO_SUCCESSOR"}
```

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"RSE-T4-H1-R1","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"CREATES_OR_CHANGES_AUTHORITY","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"NEW_AUTHORITY"},"pathFamilies":["docs/baselines/","docs/work_orders/","docs/reference/work_order_template/","docs/reference/role_switch_envelope/","docs/reference/","governance/compat/","docs/reviews/"],"claims":["required deliverables join actual artifacts proof and terminal status","tool classifier recovery evidence is locally validated"],"requiredProof":["focused hostile tests","Git observed set","acceptance reducer","worker-return fast","Local review probe"],"operatorCheckpoints":[],"forbiddenEffects":["Claude dispatch","provider call","NCR mutation","classifier bypass","platform prompt suppression","public sync","deployment"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0062.md","completenessClaimChanged":false}}
```

## Authority Chain

- Operator instruction: 2026-09-28 Local completes this foundation lane before NCR and does not transfer it to Claude.
- Baseline: `docs/baselines/CVF_GC018_RSE_T4_H1_R1_ACCEPTANCE_CHAIN_ROOT_CORRECTION_2026-09-28.md`
- Learning: `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0061.md`; `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0062.md`
- Rejected evidence: `docs/reviews/CVF_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ENFORCEMENT_COMPLETION_2026-09-28.md`; `docs/reviews/evidence/rse-t4-h1-independent-probe-2026-09-28.json`
- Learning philosophy: `docs/reference/CVF_AGENT_ERROR_TO_GOVERNANCE_LEARNING_PHILOSOPHY_2026-05-28.md`
- Active continuity: `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF_V63_2026-09-18.md`

Authority boundary: the baseline and this order authorize only the exact local
foundation repair. A contradiction outside this envelope returns
`BLOCKED_WITH_REASON`; it does not open NCR or an operator technical choice.

## Roles And Single-Agent Multi-Role Control

| Phase | Role | Allowed action | Separation control |
|---|---|---|---|
| authoring | Local dispatcher | freeze contract, manifest and tests | commit packet before implementation |
| implementation | Local worker | edit exact implementation manifest | no material commit and no closure claim |
| review | Local reviewer | inspect diff; run fresh hostile probe not copied from implementation assertions | record independent probe artifact |
| closure | Local closer/session steward | commit accepted material and continuity separately | only after reducer and all gates pass |

No independent-person claim is made. Independence means phase-separated oracle
inputs: dispatcher ledger and Git facts are not replaced by worker prose, and
the review probe is authored/run after implementation freeze.

## Scope And Risk

Risk ceiling: HIGH because protected governance checkers/templates change.

Allowed paths are exactly the Required Artifact Manifest. Forbidden: every
other source/document/session path during implementation, especially NCR,
provider/live, public-sync and deployment surfaces.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling HIGH`

Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020,
ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044. Origin defects:
ADIF-0061 and ADIF-0062. This packet uses exact bounded paths, checker
read-ahead, protected-path authorization, strict applicability literals,
phase-separated roles and no external invocation.

## Required First Reads

- paired GC-018 baseline;
- ADIF-0061 and ADIF-0062;
- H1 completion and independent probe;
- work-order template and machine-closure addendum;
- `check_agent_operation_trace.py`, `check_worker_return_quality_gate.py`,
  `check_dispatch_prompt_envelope.py`, `check_work_order_dispatch_quality.py`,
  and `run_worker_return_fast_gate.py`.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | exact status and route tokens; JSON fences; manifest paths; trace labels; near-hard threshold; protected authorization |
| gateRunPurpose | source-first contract design and author confirmation |
| claimBoundary | local checker behavior only |

## Pre-Flight Checks

Before implementation: capture clean committed HEAD, verify it contains the
packet commit, run pre-implementation autorun with this active work order,
verify all expected existing paths and confirm no forbidden NCR path is dirty.
Any failure is repaired inside scope or returned `BLOCKED_WITH_REASON`.

## Write Ownership

Write mode: modify/create only the exact artifact union in the acceptance
ledger. The Local implementation phase owns those paths; the Local reviewer
alone owns the later completion/probe and continuity paths. No rename/delete.

## Execution Plan

Implement standard and pure checker first; integrate dispatch/return/trace
gates; update scaffolds and template extraction; add focused hostile fixtures;
freeze the implementation; create the worker return from checker-derived
facts; then switch to reviewer phase for a fresh probe and closure.

## Evidence Requirements

Evidence must include exact Git changed paths, one evidence-ledger row per
requirement, all four proof IDs, focused results, template line count, H1
mutation rejection, worker-return fast PASS and zero external calls.

## Acceptance Criteria

Every root-contract rule, artifact row and proof row passes; terminal status is
reducer-consistent; the template is at most 1,131 lines; focused and hostile
tests pass; no NCR or external-effect path changes.

## Review Gate

Implementation output is not accepted by self-report. Review consumes the
frozen diff and checker output, runs a fresh hostile probe, reconciles the exact
Git set and only then authors completion and commits material.

## Closure Checklist

- strict ledger and reducer enforced at dispatch/return;
- trace parse fails closed;
- four H1 mutations reject;
- template shrink target met;
- exact manifest and proof bindings reconcile;
- material and continuity commits split;
- NCR remains parked until foundation closure is recorded.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for any stop condition, missing mandatory row,
unparseable ledger/manifest, outside-scope path or gate failure not repairable
inside the exact manifest.

## Operator Checkpoint

NOT_REQUIRED_WITH_REASON: authority is already granted for this bounded local
tranche. No further operator action is requested. Business, authority, cost
and external-effect expansion remains forbidden.

## Source Verification Block

| Source fact | Evidence | Disposition |
|---|---|---|
| template is 1,181 lines | `(Get-Content ...).Count` | ACCEPT |
| expected manifest fails open when no path parses | `_check_manifest_delta` source | ACCEPT |
| completion status check uses phrase matching | `_required_gate_consistency_issues` source | ACCEPT |
| no acceptance-ledger gate is in worker-return fast | `build_commands` source | ACCEPT |
| H1 has four recorded semantic false negatives | independent probe JSON | ACCEPT |

Current Runtime Freshness Verification: repository-local checker behavior only;
no provider or external classifier runtime claim is present.

## Required Root Contract

ledgerSchemaVersion: `cvf.workOrderAcceptanceLedger@1.0.0`

reducerVersion: `cvf.workOrderAcceptanceReducer@1.0.0`

actualArtifactOracle: `GIT_OBSERVED_CHANGED_SET`

expectedArtifactOracle: `DISPATCHER_OWNED_WORK_ORDER_LEDGER`

proofBinding: `REQUIREMENT_ID_AND_PROOF_ID`

parseFailureDisposition: `FAIL_CLOSED`

completeStatusRule: `ALL_MANDATORY_ROWS_PASS`

blockedStatusRule: `ANY_MANDATORY_ROW_NOT_PASS`

Tool/classifier contract:

- applicability is exactly `APPLICABLE` or `NOT_APPLICABLE_WITH_REASON - ...`;
- worker-authored operator questions are forbidden;
- platform-forced prompts are recorded, never claimed suppressed;
- retry count and all event counts are nonnegative integers;
- forced-prompt and worker-question counts cannot exceed event count;
- `NO_EVENT` requires all counts zero and reasoned non-event evidence;
- any event requires a non-`NO_EVENT` allowed disposition and evidence;
- exhausted recovery routes `BLOCKED_WITH_REASON` to Local.

## Work-Order Acceptance Requirement Ledger

```acceptance-ledger-json
{
  "schemaVersion": "cvf.workOrderAcceptanceLedger@1.0.0",
  "requirements": [
    {
      "requirementId": "REQ-STANDARD",
      "mandatory": true,
      "expectedArtifacts": [
        "docs/reference/work_order_template/CVF_WORK_ORDER_ACCEPTANCE_LEDGER_ADDENDUM_2026-09-28.md",
        "docs/reference/role_switch_envelope/CVF_RSE_T4_TOOL_CLASSIFIER_BLOCK_RECOVERY_ADDENDUM.md"
      ],
      "requiredProofIds": ["PROOF-FOCUSED"]
    },
    {
      "requirementId": "REQ-TEMPLATE-SCAFFOLD",
      "mandatory": true,
      "expectedArtifacts": [
        "docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md",
        "docs/reference/work_order_template/README.md",
        "governance/compat/build_dispatch_packet_scaffold.py",
        "governance/compat/build_worker_return_skeleton_scaffold.py"
      ],
      "requiredProofIds": ["PROOF-TEMPLATE-SIZE", "PROOF-FOCUSED"]
    },
    {
      "requirementId": "REQ-CHECKERS",
      "mandatory": true,
      "expectedArtifacts": [
        "governance/compat/check_work_order_acceptance_ledger.py",
        "governance/compat/check_work_order_dispatch_quality.py",
        "governance/compat/check_dispatch_prompt_envelope.py",
        "governance/compat/check_worker_return_quality_gate.py",
        "governance/compat/check_agent_operation_trace.py",
        "governance/compat/run_worker_return_fast_gate.py"
      ],
      "requiredProofIds": ["PROOF-FOCUSED", "PROOF-END-TO-END"]
    },
    {
      "requirementId": "REQ-TESTS",
      "mandatory": true,
      "expectedArtifacts": [
        "governance/compat/test_check_work_order_acceptance_ledger.py",
        "governance/compat/test_check_work_order_dispatch_quality.py",
        "governance/compat/test_check_dispatch_prompt_envelope.py",
        "governance/compat/test_check_worker_return_quality_gate.py",
        "governance/compat/test_check_agent_operation_trace.py",
        "governance/compat/test_build_dispatch_packet_scaffold.py",
        "governance/compat/test_run_worker_return_scaffold.py",
        "governance/compat/test_run_worker_return_fast_gate.py"
      ],
      "requiredProofIds": ["PROOF-FOCUSED", "PROOF-H1-HOSTILE"]
    },
    {
      "requirementId": "REQ-RETURN",
      "mandatory": true,
      "expectedArtifacts": [
        "docs/reviews/CVF_RSE_T4_H1_R1_ACCEPTANCE_CHAIN_ROOT_CORRECTION_WORKER_RETURN_2026-09-28.md"
      ],
      "requiredProofIds": ["PROOF-END-TO-END"]
    }
  ],
  "proofCatalog": [
    {"proofId": "PROOF-FOCUSED", "kind": "COMMAND", "locator": "focused-pytest"},
    {"proofId": "PROOF-H1-HOSTILE", "kind": "COMMAND", "locator": "h1-hostile-probe"},
    {"proofId": "PROOF-TEMPLATE-SIZE", "kind": "COMMAND", "locator": "template-line-count"},
    {"proofId": "PROOF-END-TO-END", "kind": "COMMAND", "locator": "worker-return-fast"}
  ]
}
```

## Required Artifact Manifest

The exact worker implementation manifest is the union of all
`expectedArtifacts` in the acceptance ledger above. No prose alias, path
family or implicit helper path is allowed.

## Forbidden Path Manifest

| Path | Reason |
|---|---|
| `docs/reviews/CVF_CVF_NCR_R1_*` | NCR remains parked at P9 |
| `CVF_SESSION/**` and `AGENT_HANDOFF_V63_2026-09-18.md` | reviewer/session-sync phase only |
| provider, public-sync and deployment surfaces | no external effect authorized |

## Required Proof Manifest

| Proof ID | Required evidence | Required at handoff |
|---|---|---|
| PROOF-FOCUSED | focused Python suites pass | Yes |
| PROOF-H1-HOSTILE | four H1 mutations plus chain mutations reject | Yes |
| PROOF-TEMPLATE-SIZE | template count at most 1,131 | Yes |
| PROOF-END-TO-END | worker-return fast gate including ledger reducer passes | Yes |

## Implementation Requirements

1. Add a canonical addendum defining strict JSON blocks, schema validation,
   Git observation, proof binding and reducer semantics.
2. Add a pure checker with reusable functions and a CLI. Reject duplicate or
   unknown keys where practical, wrong types, duplicate IDs, missing rows,
   extra rows, missing actual files/changes, undeclared proof IDs, incomplete
   proof binding and terminal-status contradictions.
3. Integrate work-order ledger validation into dispatch quality and return
   validation into the worker-return quality gate. Add the dedicated checker to
   worker-return fast with the active work-order argument.
4. Change operation-trace manifest parsing from fail-open to fail-closed when
   a non-N/A expected manifest contains no concrete repo path.
5. Add RSE recovery semantics to the dispatch and return gates with exact
   scalar and integer/count invariants, including every H1 hostile mutation.
6. Project both contracts from dispatch/return scaffolds.
7. Extract at least 50 lines from the work-order template into the new
   addendum; update the addendum index.
8. Preserve compatibility for work orders that predate this tranche: the
   ledger is mandatory for changed executable work orders after this packet,
   not retroactively for unchanged history.

## Verification Commands

```powershell
python -m pytest governance/compat/test_check_work_order_acceptance_ledger.py governance/compat/test_check_work_order_dispatch_quality.py governance/compat/test_check_dispatch_prompt_envelope.py governance/compat/test_check_worker_return_quality_gate.py governance/compat/test_check_agent_operation_trace.py governance/compat/test_build_dispatch_packet_scaffold.py governance/compat/test_run_worker_return_scaffold.py governance/compat/test_run_worker_return_fast_gate.py -q
python governance/compat/check_work_order_acceptance_ledger.py --work-order docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T4_H1_R1_ACCEPTANCE_CHAIN_ROOT_CORRECTION_2026-09-28.md --return docs/reviews/CVF_RSE_T4_H1_R1_ACCEPTANCE_CHAIN_ROOT_CORRECTION_WORKER_RETURN_2026-09-28.md --enforce
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_RSE_T4_H1_R1_ACCEPTANCE_CHAIN_ROOT_CORRECTION_2026-09-28.md
python governance/compat/check_governed_file_size.py --enforce
git diff --check
git status --short --untracked-files=all
```

## Near-Threshold Owner Maintainability Plan

Active owner entrypoint: `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`.
Pre-change count: 1,181; hard threshold: 1,200. Extract detailed section 6G
rules into the new addendum and retain a compact mandatory pointer. Minimum
shrink target: 50 lines; required post-change maximum: 1,131. The entrypoint is
explicitly in Allowed scope and Write Ownership.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | acceptance-ledger artifact union | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | checker/test manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | ledger, return and Git observation | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material set | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material set | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | completion review | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity | EXACT_PATHS | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | EXACT_PATHS | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Review-Dispatch Convergence Control

dispatchKind: REWORK

reviewRoundCount: 1

rootCauseClusterId: RSE-T4-ACCEPTANCE-CHAIN-JOIN

cumulativeExternalInvocationCount: 0

externalInvocationCeiling: 0

newIndependentCriticalEvidence: YES - H1 Local probe and ADIF-0062

convergenceDisposition: LOCAL_ROOT_CORRECTION_AUTHORIZED

## Worker Autonomy / No-Question Rule

Local repairs every allowed-scope failure and reruns its gate. Technical
contradictions return internally as `BLOCKED_WITH_REASON`; they are not sent to
the operator as choices. No Claude/external agent invocation is allowed.

## Return-Time Closeability Recheck

Required in the worker return. `COMPLETE_PENDING_REVIEW` requires
`closeabilityDisposition: CLOSEABLE`, `outsideAuthorityBlockers: NONE`, exact
ledger reconciliation and reducer PASS.

## Independent Review Probe Admission Contract

independentProbeRequired: YES

probeExecutorRole: LOCAL_REVIEWER_PHASE

implementationOracleSeparation: freeze implementation first; construct fresh
temporary ledgers/returns and Git-set inputs from the canonical contract, not
from implementation test expectations

negativeMutationClasses: malformed/duplicate/missing/unknown ledger rows;
artifact mismatch; unbound proof; terminal contradiction; unparseable trace
manifest; all four H1 classifier mutations

expectedInformationGain: prove the whole acceptance route rejects semantic
contradictions that component-shape gates previously admitted

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: modify exactly the acceptance-ledger
artifact union and focused tests declared above, then create the named Local
return/review evidence. Protected paths: every expected artifact in the ledger
and the paired packet. Operator authorization: explicit instruction that Local
perform and complete this repair before NCR. Rollback boundary: revert only
RSE-T4-H1-R1; preserve ADIF-0061/0062, H1 evidence and NCR P9.

## High-Risk Local Transaction Proof Applicability

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON -
no concurrent durable writer, DACL mutation, provider call or external-state
transaction is authorized.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | Local implementation worker -> phase-separated Local reviewer/closer |
| phase | RSE_T4_H1_R1_LOCAL_FOUNDATION_ROOT_CORRECTION |
| baseHeadFor(phase) | dispatchBaseHead=`cf0bbc1b2`; executionBaseHead=capture after packet commit; closureBaseHead=Local-set |
| changedSetScope(phase) | exact acceptance-ledger artifact union |
| traceScope(phase, actor) | standard/checker/test diffs, Git observation, command evidence and fresh review probe |
| commitOwner(phase) | Local closer only after review |
| crossBatchIsolation | clean worktree at authoring base; NCR and all unrelated paths untouched |
| nextMoveSurfaces | completion then continuity; NCR only after foundation closure |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Internal governed input (no external intake) |
| Internal source | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0062.md` |
| Chain map route | N/A with reason: no external intake is used |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | Local dispatcher/reviewer and existing CVF governance owners |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | coordination declaration only; no external authority or evidence |

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation surface | existing work-order template/RSE references and governance compatibility checkers |
| Storage decision | add one work-order-template addendum, one RSE addendum and one dedicated checker/test; integrate existing owners |
| Stable filename disposition | exact ledger paths; no dynamic filenames |
| Generated aggregate discipline | none created |
| Authority boundary | standards own semantics; checkers validate repository artifacts; Git owns observed changed set |
| Forbidden expansion | no service, daemon, database, provider adapter, UI interceptor or NCR mutation |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace |
| Session or invocation | RSE-T4-H1-R1 packet authoring, 2026-09-28 |
| Working directory | repository root |
| Command or tool surface | governed reads, ADIF resolver, source inspection, apply_patch, Git and author gates |
| Target paths | paired R1 baseline and work order |
| Allowed scope source | operator instruction and active continuity |
| Before status evidence | clean worktree; `git status --short` empty at HEAD `cf0bbc1b2`; H1 closed blocked; NCR parked P9 |
| After status evidence | paired packet pending author verification and commit |
| Diff evidence | exact two-path authoring diff |
| Approval boundary | packet authoring only before commit |
| Claim boundary | no implementation or external effect yet |
| Agent type | INTERNAL_AGENT Local dispatcher |
| Invocation ID | `rse-t4-h1-r1-author-20260928` |
| Expected manifest | paired R1 baseline and work order |
| Actual changed set | paired R1 baseline and work order |
| Manifest delta | MATCH |

## Epistemic Process Block

Expected Result / Prediction: strict requirement identities, independent Git
observation, proof binding and one reducer should prevent the false complete
state that passed H1's structural gates.

Evidence Comparison Requirement: compare focused fixtures and a fresh Local
hostile probe against the canonical root contract and Git-observed dirty set.

Contradiction Handling Requirement: fail closed and retain exact evidence; do
not narrow the repair to a matching phrase or one use case.

Claim Update Requirement: distinguish repository machine enforcement from
external classifier/platform behavior.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this work order | final closed status after review | BLOCKED pending execution |
| Completion or reviewer artifact | `docs/reviews/CVF_RSE_T4_H1_R1_ACCEPTANCE_CHAIN_ROOT_CORRECTION_COMPLETION_2026-09-28.md` | review decision and probe | BLOCKED pending review |
| Roadmap state | N/A with reason: foundation correction outside NCR execution | NCR stays parked P9 | N/A with reason |
| Registry JSON | N/A with reason: no corpus registry mutation | none | N/A with reason |
| Registry Markdown | N/A with reason: no corpus registry mutation | none | N/A with reason |
| External evidence digest | N/A with reason: no external evidence | providerCallCount 0 | N/A with reason |
| System loop interlock | completion review | foundation PASS required before NCR | BLOCKED pending review |
| Session continuity | active state/front door/handoff | separate continuity commit | BLOCKED pending closure |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Stop Conditions

Stop with `BLOCKED_WITH_REASON` for any required path outside the ledger,
inability to shrink the template, incompatible Git observation, gate regression
that cannot be repaired inside scope, provider/network requirement, or any need
to touch NCR. Do not silently remove a mandatory deliverable.

## Claim Boundary

This order authorizes exact local governance standard, template, scaffold,
checker, test and evidence changes. It does not suppress an external UI,
weaken a classifier, prove universal adoption, reopen NCR, call providers,
publish or deploy.
