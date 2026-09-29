# CVF Agent Work Order - ACEL G1 T3B R1 Group 2 Tooling Coherence Correction

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-20

Batch ID: ACEL-G1-T3B-R1-GROUP2-TOOLING-COHERENCE-CORRECTION

Dispatch base head: `b8d23fdd362322686b77c53dd2b11b5cb1e65d55`

dispatchBaseHead: `b8d23fdd362322686b77c53dd2b11b5cb1e65d55`

executionBaseHead: WORKER_MUST_CAPTURE_AT_START

closureBaseHead: N/A_PENDING_REVIEW

Commit mode: WORKER_MUST_NOT_COMMIT

providerExecutionAuthority: FORBIDDEN

## Dispatch Prompt Envelope

Role: shared-workspace `INTERNAL_AGENT` correction worker. The worker repairs
the same five uncommitted T3B outputs; Local independently reviews and commits.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_2026-09-20.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: initial T3B implementation exists uncommitted and passed
42/42, 49/49 and 43/43 self-tests, but Local review found four consolidated
defects. The 13 unrelated parked paths remain outside this lane. Both real
Group 2 source paths are absent.

Do-not-misread notes: passing hermetic tests do not waive the four Local
findings; older parked-path gate debt is not worker scope; no real principal or
real source execution is part of R1; the five existing outputs are mutable
worker inputs, not accepted evidence.

Required first actions: acknowledge startup authority; capture HEAD/status and
empty staging; read this packet, paired R1 baseline, independent review, the
original work order and T2F Group 2 contract; inspect every changed-path
checker; run pre-implementation; then modify only the exact five-path manifest.

Return contract: leave every change uncommitted and staging empty. Return exact
status `COMPLETE_PENDING_REVIEW` only after all focused tests and the worker-
return fast gate pass for this lane. Otherwise use exact status
`BLOCKED_WITH_REASON` and name a blocker that cannot be repaired in scope.

Worker: bounded internal correction worker

Reviewer/closer: CVF Local orchestrator/reviewer

Worker return path: `docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-20.md`

successorTrancheOpened: NO

## Purpose

Repair cross-principal readability, per-version cryptographic binding,
supersession entry and evidence-return readiness without real principal use or
real source creation. Preserve valid initial behavior and add regression proof
for every Local finding.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| operator role instruction | operator authorized Local audit and consolidated worker dispatch | ACCEPT |
| independent rejection | `docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_INDEPENDENT_REVIEW_2026-09-20.md`; SHA-256 `bd8845bf9bf7d3c898d56096f2ea596ec2fd854a2d13b5d5ff7fb036ab16df51` | ACCEPT |
| paired baseline | `docs/baselines/CVF_GC018_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_2026-09-20.md` | ACCEPT |
| outer Group 2 contract | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | ACCEPT |
| initial work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_2026-09-20.md` | ACCEPT_UNAFFECTED_RULES_ONLY |

## Intake Role Routing Decision

Route mode: `MULTI_AGENT_MULTI_ROLE` within one shared workspace.

The worker owns implementation and hermetic evidence only. Local owns the
independent oracle, reviewer disposition, any repair outside this exact
manifest, real principal checkpoints and commit. Provider identity supplies no
authority. External research is not applicable.

Intake summary: one Local-reviewed internal correction lane reuses the original
five-path manifest; no external intake, live run or real principal action is
admitted.

Escalation condition: stop only for a source contradiction, forbidden sixth
path, credential/alternate-user/real-source need, parked drift or irreparable
mandatory gate outside the exact five-path scope.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T3B-R1-GROUP2-TOOLING-COHERENCE-CORRECTION","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"PURE_LOCAL_IMPLEMENTATION","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/baselines/","docs/work_orders/","docs/audits/","docs/reviews/","docs/reference/","scripts/","governance/compat/","EXTENSIONS/"],"claims":["corrected principal-bound Group 2 tooling and hermetic validation only; no real source"],"requiredProof":["cross-principal read-only ACL","per-version immutable source binding","validated newer-version supersession","worker-return fast gate","independent Local probes"],"operatorCheckpoints":["Party A spec creation","Approver decision writes","Local source verification","T3E consumer wiring","candidate admission"],"forbiddenEffects":["credential access","alternate-user execution","real source creation","parked-path mutation","worker commit","provider/live/public/deployment","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_INDEPENDENT_REVIEW_2026-09-20.md","completenessClaimChanged":false}}
```

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id ACEL-G1-T3B-R1-GROUP2-TOOLING-COHERENCE-CORRECTION --title "ACEL G1 T3B R1 Group 2 Tooling Coherence Correction" --date 2026-09-20 --base b8d23fdd3 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id acel-g1-t3b-group2-operational-coherence --prior-finding-set-digest bd8845bf9bf7d3c898d56096f2ea596ec2fd854a2d13b5d5ff7fb036ab16df51 --new-independent-critical-evidence CROSS_PRINCIPAL_DACL_AND_PER_VERSION_BINDING_FAILURES --scec-problem-key acel-g1-t3b-group2-source-creation-tooling-problem --scec-chain-mode SUCCESSOR --scec-chain-ordinal 2 --scec-predecessor-path docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_INDEPENDENT_REVIEW_2026-09-20.md --scec-predecessor-sha256 bd8845bf9bf7d3c898d56096f2ea596ec2fd854a2d13b5d5ff7fb036ab16df51 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --no-evidence-readiness-applicable --stdout` |
| generatedProfile | protected-governance-path plus no-commit rework profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with four consolidated findings, exact five-path manifest, SID/DACL model, per-version resolver and tests |
| checkerReadAheadConfirmation | dispatch-quality, core-guard, gate-to-role, worker-return, scaffold-provenance and operation-trace sources inspected before authoring |
| docOnlyNewFields | none |
| claimBoundary | dispatch provenance only; no source, activation, provider, public or deployment claim |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G1-T3B-GROUP2-SOURCE-CREATION-TOOLING
reviewRoundCount: 1
priorFindingSetDigest: bd8845bf9bf7d3c898d56096f2ea596ec2fd854a2d13b5d5ff7fb036ab16df51
dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR
reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS
newIndependentCriticalEvidence: CROSS_PRINCIPAL_DACL_AND_PER_VERSION_BINDING_FAILURES
regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: ONE_CONSOLIDATED_REWORK
rootCauseClusterId: acel-g1-t3b-group2-operational-coherence
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
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t3b-group2-source-creation-tooling-problem","chainMode":"SUCCESSOR","chainOrdinal":2,"predecessor":{"path":"docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_INDEPENDENT_REVIEW_2026-09-20.md","sha256":"bd8845bf9bf7d3c898d56096f2ea596ec2fd854a2d13b5d5ff7fb036ab16df51"},"blockerDelta":{"prior":["acel_g1_group2_real_source_not_created","cross-principal-dacl-gap","per-version-binding-gap","supersession-entry-gap","worker-return-readiness-gap"],"resolved":["cross-principal-dacl-gap","per-version-binding-gap","supersession-entry-gap","worker-return-readiness-gap"],"retained":["acel_g1_group2_real_source_not_created"],"new":["group2-tooling-r1-not-accepted"],"reopened":[],"current":["acel_g1_group2_real_source_not_created","group2-tooling-r1-not-accepted"]},"resolutionEvidence":{"cross-principal-dacl-gap":{"evidenceClass":"ACCEPTED_REVIEW","evidencePath":"docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_INDEPENDENT_REVIEW_2026-09-20.md","sha256":"bd8845bf9bf7d3c898d56096f2ea596ec2fd854a2d13b5d5ff7fb036ab16df51","locator":"Consolidated Correction Contract"},"per-version-binding-gap":{"evidenceClass":"ACCEPTED_REVIEW","evidencePath":"docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_INDEPENDENT_REVIEW_2026-09-20.md","sha256":"bd8845bf9bf7d3c898d56096f2ea596ec2fd854a2d13b5d5ff7fb036ab16df51","locator":"Consolidated Correction Contract"},"supersession-entry-gap":{"evidenceClass":"ACCEPTED_REVIEW","evidencePath":"docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_INDEPENDENT_REVIEW_2026-09-20.md","sha256":"bd8845bf9bf7d3c898d56096f2ea596ec2fd854a2d13b5d5ff7fb036ab16df51","locator":"Consolidated Correction Contract"},"worker-return-readiness-gap":{"evidenceClass":"ACCEPTED_REVIEW","evidencePath":"docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_INDEPENDENT_REVIEW_2026-09-20.md","sha256":"bd8845bf9bf7d3c898d56096f2ea596ec2fd854a2d13b5d5ff7fb036ab16df51","locator":"Consolidated Correction Contract"}},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":1,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G1-T3B-R1-TOOLING-CORRECTION","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/baselines/CVF_GC018_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_2026-09-20.md"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## Dependency Release Evidence

| Dependency | Evidence | Release condition | Disposition |
|---|---|---|---|
| four Local findings | independent review and source/OS probes | repair together | RELEASED_FOR_REWORK |
| exact SIDs | Party A 1006; Approver 1008; Local 1001 | no caller substitution | RELEASED |
| per-version file pattern | T2F `SPEC_v{n}.json` | strict repository-owned resolver | RELEASED |
| real author/decision execution | operator checkpoints after Local acceptance | forbidden now | PARKED_OPERATOR_EXECUTION |

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: HIGH

independentProbeDispositionAtDispatch: PLAN_ADMITTED_PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: REQUIRED_DIFFERENT_EXECUTION_AND_ASSERTION_PATH

positiveControl: Local creates two distinct hermetic spec versions and checks
their separately recomputed hashes through the checker.

negativeMutationClasses: remove Approver/Local ACL grant; reuse v1 hash for v2;
remove `SPEC_v2`; path-escape version resolution; supersede v1 before v2
approval/activation; malformed return status.

expectedInformationGain: demonstrate operational handoff and version-specific
cryptographic identity rather than repeating the worker's broad suite.

rerunCostReason: bounded mutations directly decide acceptance and avoid real
principal/source execution.

reviewerDecisionOwner: LOCAL

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | five exact paths below | hermetic correction only; no credentials, real source, staging or commit | this packet and paired baseline/review | local PowerShell/Python | IMPLEMENTED |
| `EXTERNAL_AGENT_CLI_MCP` | none | no external ingress, authentication, mutation, runtime or public claim | no accepted adapter source | fresh governed packet required | DEFERRED_WITH_REASON |

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `scripts/acel_g1_party_a_group2_spec_writer.ps1` | MODIFY; cross-principal read-only ACL with explicit Approver and Local SIDs |
| `scripts/acel_g1_approver_group2_decision_writer.ps1` | MODIFY; per-version resolution and explicit validated newer-version supersession |
| `governance/compat/check_acel_g1_verification_authority_spec.py` | MODIFY; validate every cited `SPEC_v{n}.json` independently across full history |
| `governance/compat/test_check_acel_g1_verification_authority_spec.py` | MODIFY; add all R1 regression probes and retain unaffected coverage |
| `docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-20.md` | MODIFY; bind to R1, exact status, remove invalid pseudo-binding and report R1 evidence |

No sixth output is allowed. All 13 parked paths, R1 dispatcher/reviewer
artifacts, session state, real Group 2 source paths and downstream T3E code are
read-only.

## Work-Order Fulfillment Manifest

The five rows above are the complete worker changed set. Existing uncommitted
bytes are predecessor input, not accepted authority. The worker must reconcile
all five at return and disclose any unexpected path without touching it.

## Allowed Scope / Forbidden Scope

Allowed: edit the five paths, use disposable temp fixtures, inspect OS account
and ACL facts read-only, run focused tests/gates and remove own fixtures.

Forbidden: passwords, credential stores, `runas`, alternate-user execution,
real `governance/sources/verification_authority_spec/` writes, parked paths,
R1 packet edits, staging, commit, T3E/admission/provider/live/public/deploy or
successor work.

## Write Ownership

Worker owns only the five-path manifest. Local owns this packet, baseline,
independent review, any final bounded reviewer repair, commits and session sync.
Operator owns credentials and real principal checkpoints.

## Agent Roles

| Role | Responsibility |
|---|---|
| Operator | owns passwords and any later Party A/Approver invocation |
| Dispatcher | fixes the consolidated contract and exact manifest |
| Worker | repairs five uncommitted paths and returns evidence without commit |
| Local reviewer/closer | runs independent probes, accepts/rejects, commits and synchronizes session |

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
2. `CVF_SESSION_MEMORY.md` and active handoff
3. `docs/reference/guard_orientation/README.md`
4. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`
5. paired R1 baseline, this packet and independent review
6. original T3B work order and T2F Group 2 contract
7. all five current outputs in full
8. checker sources in the read-ahead block below

## Pre-Flight Checks

1. Capture exact HEAD and full status; require the five owned outputs plus the
   disclosed 13 parked paths and no staging.
2. Confirm both real Group 2 source paths remain absent.
3. Hash the 13 parked paths and do not modify them.
4. Run pre-implementation. Classify older parked-return findings out-of-lane;
   repair every failure in one of the five owned paths.
5. Stop before any sixth path, credential or real-principal need.

## Implementation Contract

### Cross-principal ACL

- Party A-created `SPEC_v{n}.json`: owner Party A; Party A full control;
  Approver SID 1008 read/read-attributes/read-permissions only; Local SID 1001
  the same read-only rights; SYSTEM and Administrators may retain recovery
  rights. Approver must have no write, append, delete, ownership or DACL-change
  grant.
- Approver-created decisions file: owner Approver; Approver full control;
  Party A must not modify; Local SID 1001 receives explicit read-only rights.
- Tests inspect effective allow rights and forbidden rights for exact SIDs;
  they must not equate group membership text with cross-principal readability.

### Per-version source binding

- Resolve integer `specVersion >= 1` only to repository-local
  `governance/sources/verification_authority_spec/SPEC_v{n}.json`; no caller-
  supplied arbitrary path, traversal, alternate root or latest-file choice.
- Strictly parse each distinct cited file once, reject duplicate members and
  unexpected schema/version mismatch, verify its record digest and recompute
  direct SHA-256 over its decoded content bytes.
- For every decision row, its `recomputedHashHex` must equal that row's cited
  version content hash. A v2 row using v1's hash is invalid even when both
  hashes are well-formed.
- Missing/malformed/unreadable cited versions fail closed. Full history still
  validates unique IDs, exact chain links, per-version transitions and zero or
  one active version without latest/largest inference.

### Supersession entry

- The real decision writer must accept an explicit target version and, only
  for `SUPERSEDED`, an explicit newer replacement version.
- It validates both immutable spec files and all existing decision rows before
  append. Replacement version must be greater than the old version and must
  already have valid `APPROVED` then `ACTIVATED` events bound to its own hash.
- The old version must be the sole other active version and have no prior
  supersession. The resulting state has exactly one active replacement.
- No automatic version choice, in-place spec edit or combined approval/
  activation/supersession event is permitted.

### Return readiness

- Top-level Status is exactly one recognized token, not prose in the value.
- `independentProbeDisposition: PENDING_REVIEWER_EXECUTION` accompanies
  `COMPLETE_PENDING_REVIEW`.
- Evidence readiness is explicitly not applicable because R1 is bounded local
  tooling correction, not a discovery/corpus audit, and its manifest contains
  no JSON audit/manifest artifact. Remove the invalid pseudo-binding; do not
  fabricate a sixth path or evidence-shaped source rows.
- Out-of-lane parked debt is disclosed separately and does not replace the
  owned-lane disposition.

## Worker Autonomy / No-Question Rule

Repair routine allowed-scope code, test and return-gate defects directly
without escalation. Return only for a true source conflict, sixth-path need,
credential/alternate-user/real-source need or irreparable mandatory gate
failure outside the five owned paths.

A gate failure inside Allowed scope is authorization to repair and rerun.
Escalation is reserved for scope expansion, claim-boundary change,
credentials, alternate-user or real-source execution, forbidden paths or
higher-risk external effects.

## Foundation Storage Layout Block

| Field | Disposition |
|---|---|
| Foundation path class | same two writers, checker, focused tests and return |
| Storage decision | no new path or runtime store |
| Existing aggregate impact | none |
| Generated state impact | none |
| Durable governance boundary | real sources remain absent and operator-gated |

## Core Guard Self-Protection Authorization

| Field | Value |
|---|---|
| Authorized guard-maintenance scope | bounded repair of the Group 2 read-only checker and its focused test only; no hook/catalog/general-guard changes |
| Protected path | `governance/compat/check_acel_g1_verification_authority_spec.py` |
| Protected path | `governance/compat/test_check_acel_g1_verification_authority_spec.py` |
| Operator authorization | operator authorized Local to audit and issue worker correction orders; the original committed T3B order already owns these two paths |
| Rollback boundary | both files remain uncommitted until Local accepts; rollback is deletion/reversion of only the five owned uncommitted outputs; parked and committed governance remain untouched |

## ADIF Defect Registry Disclosure

Dispatcher query for `CODE_CHANGE`/dispatcher/dispatch returned
`NONE_RETURNED`. Worker reruns the worker/implementation query and records the
result; this does not replace the four accepted Local findings.

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`dispatch`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py`; current Group 2 checker/test |
| literalTokensReviewed | source-verification columns; protected paths; return status/evidence schema; convergence, probe, trace and no-commit fields |
| gateRunPurpose | confirm the consolidated R1 packet and later the five-path return |
| claimBoundary | structure and focused hermetic behavior only; no real-source acceptance |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| four defects and exact correction | accepted review | `docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_INDEPENDENT_REVIEW_2026-09-20.md` | Findings / Position; Consolidated Correction Contract | T3B-RV-1 through T3B-RV-4 | Local reviewer | ACCEPT |
| per-version immutable spec and lifecycle | contract invariant | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 2; Explicit Approval, Activation And Supersession | `SPEC_v{n}.json`; `cvf.specDecisionEvent` | Group 2 contract | ACCEPT |
| exact initial scope | dispatch manifest | `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_2026-09-20.md` | Required Artifact Manifest | five worker paths | initial dispatch | ACCEPT |
| principal identities | identity | `docs/reviews/CVF_ACEL_G1_T3B_PRINCIPAL_POLICY_OPERATOR_DECISION_2026-09-20.md` | Operator Decision | Party A 1006; Approver 1008 | principal decision | ACCEPT |
| Local read requirement | operational evidence | `docs/audits/CVF_ACEL_G1_T3A_C2_GROUP1_SOURCE_LOCAL_VERIFICATION_2026-09-20.md` | Source Verification Result | Local non-elevated verification | Local reviewer | ACCEPT |

## Negative Search And Collision Discipline

Only the five initial outputs may be modified. R1 dispatcher paths and all
other repo paths are read-only. Real Group 2 source absence is checked before
and after tests. Disposable fixtures use unique temp directories and are
removed. Unexpected collision or parked hash drift stops execution.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired R1 baseline/work order/review | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired R1 baseline/work order/review | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact five outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker-return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact five outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact five outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | returned five paths | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | MULTI_AGENT_MULTI_ROLE |
| rolePattern | Local dispatcher -> no-commit INTERNAL_AGENT worker -> Local reviewer/closer |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC; real Party A/Approver execution excluded |
| baseHeadFor(phase) | dispatchBaseHead=`b8d23fdd362322686b77c53dd2b11b5cb1e65d55`; executionBaseHead captured by worker; closureBaseHead set by Local |
| changedSetScope(phase) | exact five required outputs during execution; three R1 dispatcher artifacts during dispatch |
| traceScope(phase, actor) | reads, commands, tests, hashes, status, cleanup and real-source absence |
| commitOwner(phase) | Local only |
| crossBatchIsolation | thirteen parked paths byte-identical and disclosed |
| nextMoveSurfaces | Local review, then principal-separated operator checkpoint |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT R1 worker after operator forwards this packet

laneOwnedPaths: exact five paths in Required Artifact Manifest

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return, empty staging, exact delta and parked reconciliation

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| actor | one shared-workspace `INTERNAL_AGENT` worker |
| role set | PowerShell/Python correction and evidence author; not reviewer/closer |
| delegation depth | zero |
| evidence basis | named CVF sources and disposable fixtures only |
| gate sequence | pre-implementation, focused tests, worker-return fast, Local review |
| self-review boundary | worker cannot accept, stage or commit output |
| role separation ledger | worker returns pending; Local evaluates and commits |
| escalation condition | credential, alternate-user/real-source, sixth path, parked drift or authority contradiction |

## Worker Output Checker Read-Ahead Mandate

Before editing, read the complete current Group 2 checker/test and the generic
worker-return/core-guard checkers. Do not use gate failures as first discovery
of required return fields.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T3B_GROUP2_SOURCE_CREATION_TOOLING_WORKER_RETURN_2026-09-20.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

evidenceReadinessContract: NOT_APPLICABLE_WITH_REASON: bounded local tooling correction has no discovery audit or manifest artifact

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required sections: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Decision / Disposition; Claim Boundary;
Changed Files; Command Evidence; No-Commit Statement; Checker Source Read-
Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary
Control Block; Machine Closure Package; External Knowledge Intake Routing;
Epistemic Process Block; Public Export Disposition; exact executionBaseHead and
full `git status --short --untracked-files=all`.

## Execution Plan

1. Freeze HEAD/status/staging, parked hashes and real-source absence; run pre-implementation.
2. Repair ACL construction and add exact SID rights assertions.
3. Implement safe per-version spec resolution/validation in writer and checker.
4. Repair supersession invocation/transition logic with explicit validated replacement.
5. Replace/add regressions for every T3B-RV finding; retain unaffected tests.
6. Repair the worker return, run all final commands once, reconcile exactly five paths and leave staging empty.

## Evidence Requirements

Required final evidence: both writer self-tests; Python compile and focused
suite; explicit rights matrix for SIDs 1006/1008/1001; two distinct valid spec
contents/hashes across one full history; v2-hash-reuse rejection; missing/path-
escaped v2 rejection; supersession-before-newer-activation rejection; valid
v1-to-v2 rotation; worker-return fast PASS; real-source absence; parked hash
match; empty staging. Never record passwords or credential-derived content.

## Acceptance Criteria

- Exactly five worker paths change; no parked/R1 dispatcher/real-source path changes.
- Approver can read but cannot modify Party A specs; Local SID 1001 explicitly reads both files.
- Every decision event is validated against its own immutable spec version and content hash.
- Valid distinct v1/v2 history passes; reused/missing/malformed/wrong-version spec fails closed.
- `SUPERSEDED` requires an explicit, greater, independently valid and already activated replacement version.
- Existing tests plus new R1 regressions pass.
- Worker return binds to R1, has exact recognized status, makes no pseudo-binding claim, and fast gate passes.

Fail conditions: any sixth path; caller-controlled arbitrary source path; latest/
largest version choice; ACL grants Approver modification; version event checked
against another version's hash; real principal/source action; staging/commit;
failed owned-lane final gate.

## Review Gate

Local consumes returned evidence, performs only the admitted independent ACL
and per-version mutation probes, checks exact five-path/parked reconciliation
and runs reviewer preflight. Local does not use credentials or write real
Group 2 sources during tooling review.

## Closure Checklist

- [ ] T3B-RV-1 through T3B-RV-4 each have a failing-before/passing-after regression.
- [ ] Exact five paths and all 13 parked hashes reconcile; staging empty.
- [ ] Worker-return fast and Local independent probes pass.
- [ ] Both real Group 2 paths remain absent.
- [ ] Material and continuity commits remain separate.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` only for a source contradiction, forbidden sixth
path, credential/alternate-user/real-source requirement, parked drift or an
irreparable mandatory gate outside allowed scope. Repair all owned-lane gate
failures without operator interruption.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
pwsh -NoProfile -File scripts/acel_g1_party_a_group2_spec_writer.ps1
pwsh -NoProfile -File scripts/acel_g1_approver_group2_decision_writer.ps1
python -m py_compile governance/compat/check_acel_g1_verification_authority_spec.py governance/compat/test_check_acel_g1_verification_authority_spec.py
python governance/compat/test_check_acel_g1_verification_authority_spec.py
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
git diff --cached --name-only
```

No release-gate/provider call applies: this is local hermetic tooling, not a
live AI-governance or production-readiness claim.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G1_T3B_R1_GROUP2_TOOLING_COHERENCE_CORRECTION_COMPLETION_2026-09-20.md` (reviewer-owned; create only if closure evidence requires it) |
| reviewerOwnedClosurePaths | exact five worker outputs plus bounded reviewer repair inside those paths only |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |
| materialCommitBoundary | accepted five-path implementation first |
| sessionSyncBoundary | separate later commit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF dispatcher/orchestrator |
| Provider or surface | local private provenance repository |
| Session or invocation | ACEL G1 T3B R1 dispatch, 2026-09-20 |
| Working directory | repository root |
| Command or tool surface | governed reads, SHA-256, OS read-only facts, hermetic tests, scaffold stdout, apply_patch, git |
| Target paths | R1 baseline/work order/review; worker later owns exact five outputs |
| Allowed scope source | operator audit/delegation authority; original T3B packet; independent review |
| Before status evidence | clean worktree requirement is represented by explicit shared-lane isolation: HEAD `b8d23fdd362322686b77c53dd2b11b5cb1e65d55`; 13 parked plus exact five T3B outputs; staging empty |
| After status evidence | R1 packet authored for commit; worker outputs and parked paths untouched by dispatcher |
| Diff evidence | four-finding correction matrix and exact manifest reconciled before dispatch commit |
| Approval boundary | corrective dispatch only |
| Claim boundary | no credentials, alternate-user execution, real source, activation, admission, provider/live/public/deploy effect |
| Agent type | Local dispatcher/orchestrator |
| Invocation ID | `acel-g1-t3b-r1-group2-tooling-coherence-dispatch-2026-09-20` |
| Expected manifest | R1 baseline, R1 work order, independent review |
| Actual changed set | R1 baseline, R1 work order, independent review |
| Manifest delta | MATCH before commit |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | five-path hermetic tooling correction |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: dispatch and tests create no runtime receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: review probes and final worker tests/gates |
| invocationBoundary | local governed file edits and disposable test fixtures only |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception claim |
| claimLanguage | correct tooling pending Local independent acceptance |
| forbiddenExpansion | credentials, alternate principal, real source, activation, T3E, admission, provider/live/public/deploy |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: no legacy/external corpus absorption occurs.

## External/Local Coordination Binding

Role: `INTERNAL_AGENT`; phase: R1 implementation; decision owner: Local
reviewer. External research ends outside this packet and has no authority here.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` |
| Chain map route | N/A with reason: direct internal contract -> INTERNAL_AGENT correction -> Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | T2F Group 2 contract and this R1 dispatch |
| Disposition | local first-party correction only |
| Claim boundary | no external source authority, corpus, remote implementation or provider claim |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: explicit principal grants and per-version source
resolution will make the valid v1/v2 sequence pass while the four returned
failure modes fail closed.

Evidence Comparison Requirement: worker return compares final observed test
and gate output with this prediction.

Contradiction Handling Requirement: any contradiction requires a
Contradiction Or Gap Disposition and narrowed claim; no silent waiver.

Claim Update Requirement: worker records confirmed, revised, narrowed or
invalidated for each T3B-RV finding.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private corrective tooling dispatch; no public-sync authority.

## Claim Boundary

This work order authorizes correction and hermetic verification of five
uncommitted files only. It does not authorize credentials, `runas`, execution
as Party A/Approver, real Group 2 source creation, approval/activation, T3E,
candidate admission, worker commit, provider/live/network/public/deployment or
automatic successor effects.

## Operator Checkpoint

No operator action is needed for R1 implementation. After Local acceptance,
real Party A creation and Approver decisions remain separate explicit operator
checkpoints under their dedicated launchers; R1 must not perform them.
