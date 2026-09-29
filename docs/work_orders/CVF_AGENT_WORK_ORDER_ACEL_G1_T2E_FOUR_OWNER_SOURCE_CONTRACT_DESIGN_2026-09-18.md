# CVF Agent Work Order - ACEL G1 T2E Four-Owner Source Contract Design

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-18

Batch ID: ACEL-G1-T2E-FOUR-OWNER-SOURCE-CONTRACT-DESIGN

dispatchBaseHead: `e47fad31191070bed9b57680118978e9a3973cce`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker role: one shared-workspace `INTERNAL_AGENT`

Reviewer/closer: Local orchestrator/reviewer

## Dispatch Prompt Envelope

Role: internal source-contract designer and evidence producer; not an appointed
owner, implementer, reviewer, or closer.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture `git rev-parse HEAD` and full status before edits.

Current-time notes: 2026-09-18; operator approved the four-responsibility model
for contract design only.

Do-not-misread notes: role contracts are proposals, not appointments; no key,
registry implementation, live lookup, signer, runtime, or candidate admission.

Required first actions: read startup/bootstrap/handoff, guard orientation,
literal gotchas, paired baseline, this order, T2C Owner Ledger, T2D matrix,
Local decisions and applicable checker sources; verify exact output absence and
13/13 frozen-path hashes.

Return contract: create only the two owned outputs, run all named gates, do not
stage or commit; return `COMPLETE_PENDING_REVIEW` only when the full four-
contract packet is coherent, otherwise `BLOCKED_WITH_REASON`.

## Purpose

Design four separately accountable source-owner contracts and the evidence
required for later operator appointment and Local verification. This tranche
turns the approved responsibility topology into reviewable documentation; it
does not create operational sources or appoint accountable parties.

## Authority Chain And Dependency Release Evidence

| Dependency | Evidence | Release condition | Current disposition |
|---|---|---|---|
| T2C hypothetical consumers | `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md`, Owner Ledger | design input only | ACCEPT |
| T2D reviewed owner options | `docs/audits/CVF_ACEL_G1_T2D_SOURCE_OWNER_OPTIONS_2026-09-18.md`, Owner-Option Matrix | four responsibility classes; no owner proof | ACCEPT |
| Local bounded T2D acceptance | `docs/reviews/CVF_ACEL_G1_T2D_SOURCE_OWNER_ESTABLISHMENT_LOCAL_REVIEW_2026-09-18.md`, Decision | documentation evidence only | ACCEPT |
| Operator four-role decision | `docs/reviews/CVF_ACEL_G1_T2E_FOUR_OWNER_RESPONSIBILITY_LOCAL_DECISION_2026-09-18.md`, Decision / Disposition | contract-design dispatch only | ACCEPT |
| GC-018 boundary | `docs/baselines/CVF_GC018_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md`, Proposed Tranche | exact two documentation outputs | ACCEPT |
| Actual party appointment or implementation | no verified source | later operator decision plus separate governed packet | BLOCKED_SOURCE_NOT_FOUND |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| intake summary | internal four-owner source-contract design |
| scope classification | documentation-only governance/architecture contract |
| risk sensitivity | high trust-boundary sensitivity; no operational effects |
| selected route mode | `SINGLE_AGENT_MULTI_ROLE`: one designer, independent Local review |
| role separation basis | worker cannot appoint an owner, accept its return, stage or commit |
| escalation condition | authority contradiction, frozen drift, circular authority or forbidden effect |

## Roles, Write Ownership And Scope

Local is dispatcher and reviewer/closer. The worker owns only the two paths in
the Worker Output Inventory. The operator retains appointment of actual
accountable parties. Existing code, governance, continuity, prior reviews,
parked paths and secrets are read-only.

No external research, nested delegation, network access, credential access,
key generation/import, TypeScript/Python implementation, checker change,
configuration mutation, public sync, deployment or provider call is authorized.

## Required First Reads

Read the active bootstrap/front door/handoff; paired baseline and Local
decision; T2C human contract; T2D audit and Local review; guard orientation;
literal gotchas; work-order template; and checker sources named in the
Checker Source Read-Ahead Block. Provider memory is `NOT_CVF_SOURCE`.

## Pre-Flight Checks

Record `git rev-parse HEAD`, `git status --short --untracked-files=all`, empty
staging, absence of both worker output paths, and SHA-256 reconciliation of
all thirteen parked paths against the T2D worker return. Run pre-implementation
before material edits. Stop on output collision or any hash mismatch.

## Worker Output Inventory

| Path | Required at handoff | Purpose |
|---|---|---|
| `docs/audits/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_2026-09-18.md` | Yes | four proposed contracts, separation matrix, evidence-admission rules and unresolved decisions |
| `docs/reviews/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_WORKER_RETURN_2026-09-18.md` | Yes | no-commit trace, source comparison, frozen reconciliation and gate evidence |

## Forbidden Worker Paths

| Path | Reason |
|---|---|
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.class.calibration.owner.contract.ts` | pre-existing parked evidence; read/hash only |
| `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/task.class.calibration.owner.contract.test.ts` | pre-existing parked evidence; read/hash only |
| `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_2026-09-17.md` | pre-existing parked evidence |
| `docs/audits/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_MANIFEST_2026-09-17.json` | pre-existing parked evidence |
| `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md` | pre-existing parked evidence |
| `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_MANIFEST_2026-09-17.json` | pre-existing parked evidence |
| `docs/audits/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_2026-09-17.md` | pre-existing parked evidence |
| `docs/reference/agent_system_skills/CVF_TASK_CLASS_CALIBRATION_OWNER_CONTRACT.md` | pre-existing parked evidence |
| `docs/reviews/CVF_ACEL_G1_T2A_CANDIDATE_EVIDENCE_BINDING_SCHEMA_AMENDMENT_WORKER_RETURN_2026-09-17.md` | pre-existing parked evidence |
| `docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_WORKER_RETURN_2026-09-17.md` | pre-existing parked evidence |
| `docs/reviews/CVF_ACEL_G1_T2_TASK_CLASS_CALIBRATION_OWNER_IMPLEMENTATION_WORKER_RETURN_2026-09-17.md` | pre-existing parked evidence |
| `governance/compat/check_task_class_calibration_owner_evidence.py` | pre-existing parked protected checker |
| `governance/compat/test_check_task_class_calibration_owner_evidence.py` | pre-existing parked protected checker test |
| `CVF_SESSION/**`; `CVF_SESSION_MEMORY.md`; `AGENT_HANDOFF*.md` | Local-only continuity |
| every source, test, checker and governed artifact not in Worker Output Inventory | outside worker write ownership |

## Forbidden Filesystem State At Dispatch

| Forbidden path group | Expected state | Actual state at dispatch | Action if PRESENT |
|---|---|---|---|
| thirteen exact parked paths above | PRESENT_EXEMPTED | PRESENT_EXEMPTED as untracked worktree context | ignore; do not edit, stage, claim or remove |
| two Worker Output Inventory outputs | ABSENT | ABSENT | stop and return if either appears before worker starts |

## Pre-Existing Dirty Path Exemptions

All thirteen exact parked paths in the Forbidden Worker Paths have status `??`
at dispatch. Exemption boundary: byte-read/hash only; do not edit, stage,
commit, delete, rename, reformat or claim them. The dispatcher packet paths may
be committed before execution and are not worker-owned.

## Write Ownership

Owned files are exactly the two Worker Output Inventory paths. Write mode:
create-only, then modify-listed while completing the return. Any other mutation
requires a new Local work order; a gate failure never expands ownership.

## Contract Design Requirements

The audit must define one contract for each responsibility:

1. `VerifierKeyAndRegistryControlOwner` - key custody, generation/import
   ceremony boundaries, rotation, revocation, public-key registry writes and
   separation between custodian and writer when needed.
2. `VerificationAuthoritySpecificationOwner` - versioned authority policy,
   decision approval, canonical bytes/hash production and independent consumer
   binding for `verificationAuthorityHash`.
3. `RegistryObservationOwner` - registry snapshot identity, acquisition time,
   source provenance, append-only observation records, correction chaining and
   rollback resistance.
4. `IssuerRegistryAuthorityOwner` - issuer content, lookup semantics,
   freshness/status responses, correction/revocation and genuine authority
   provenance.

For every contract specify: accountable responsibility; prohibited dual roles;
source-of-truth form; decision maker; write authority; read/verifier consumers;
version/identity scheme; lifecycle transitions; durable evidence; correction,
rotation or revocation route; required admission evidence; fail-closed behavior;
operator inputs; and exact claims still blocked.

Add a cross-contract separation matrix covering self-approval, circular hash
binding, same-party observation and mutation, issuer self-verification, stale
evidence, unavailable source, conflicting versions, and emergency override.
No emergency path may silently admit a candidate.

Do not design cryptographic key bytes, choose secrets, implement schemas/code,
or invent an organization. Use role names as proposals only. If evidence is
missing, preserve `BLOCKED_SOURCE_NOT_FOUND` and `UNVERIFIED`.

## Required Handoff Evidence

| Proof | Path | Required literal | Required at handoff |
|---|---|---|---|
| proposed-role posture | audit output | `PROPOSED_OPERATOR_DECISION` | Yes |
| unresolved-source posture | audit output | `BLOCKED_SOURCE_NOT_FOUND` | Yes |
| admission posture | audit and worker return | `UNVERIFIED` | Yes |
| separation proof | audit output | `Cross-Contract Separation Matrix` | Yes |
| circularity guard | audit output | `CIRCULAR_AUTHORITY_REJECTED` | Yes |
| terminal ready disposition | worker return | `COMPLETE_PENDING_REVIEW` | Conditional: use blocked status honestly when required |
| frozen evidence count | worker return | `13/13` | Yes |
| frozen evidence mismatch result | worker return | `ZERO_MISMATCHES` | Yes |
| commit posture | worker return | `WORKER_MUST_NOT_COMMIT` | Yes |
| staging posture | worker return | `EMPTY_STAGING` | Yes |

## Output Fulfillment Boundary

The Worker Output Inventory is the complete worker changed-set. The
Forbidden Worker Paths and Pre-Existing Dirty Path Exemptions define all
known worktree exclusions. The Required Handoff Evidence contains one atomic
literal per proof except the plain-language empty-staging evidence row, which
is command output rather than a token parser contract.

## Execution Plan

1. Capture HEAD, full status, output-path absence, staging and frozen hashes.
2. Read every required authority source and output-applicable checker source.
3. Map T2C consumer requirements and T2D gaps into four proposed contracts.
4. Perform one consolidated cross-contract authority/circularity audit.
5. Create the audit, scaffold and complete the worker return.
6. Run every Verification Command after the final edit; repair owned paths only.
7. Recheck 13/13 frozen hashes, staging and exact changed set; return to Local.

Stop immediately for a contradictory current authority, parked hash drift,
pre-existing output, forbidden mutation, need for an actual owner appointment,
or any required failure that cannot be repaired within the two owned paths.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| four-responsibility topology approved for design | CURRENT_AUTHORITY | `docs/reviews/CVF_ACEL_G1_T2E_FOUR_OWNER_RESPONSIBILITY_LOCAL_DECISION_2026-09-18.md` | Decision / Disposition | approved topology | operator/Local boundary | ACCEPT |
| four operational-owner gaps documented | REVIEWED_FINDING | `docs/audits/CVF_ACEL_G1_T2D_SOURCE_OWNER_OPTIONS_2026-09-18.md` | Owner-Option Matrix | dependencies 1-4 | T2D analysis | ACCEPT |
| T2D evidence accepted bounded | REVIEWED_FINDING | `docs/reviews/CVF_ACEL_G1_T2D_SOURCE_OWNER_ESTABLISHMENT_LOCAL_REVIEW_2026-09-18.md` | Decision | documentation-only acceptance | Local reviewer | ACCEPT |
| consumer dependencies and hash/lookup fields | DESIGN_INPUT | `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` | Owner Ledger | trust-anchor consumers | hypothetical T2C contract | ACCEPT |

## Negative Search And Collision Discipline

Reuse T2D's accepted bounded search rather than rerunning broad discovery.
Same-token roles, HMAC signers, generic identity stores, provider credential
rotation, approval-packet issuer fields and hypothetical T2C types are not
owner evidence. The worker may perform targeted collision checks for proposed
role names and planned output paths, stating roots, globs and exclusions.

A proposed contract that cites itself as appointment evidence, hashes its own
unapproved bytes as independent authority, lets a registry writer attest its
own observation, or treats an issuer's unverified assertion as live lookup must
be marked `CIRCULAR_AUTHORITY_REJECTED`.

Exact targeted query:
`rg -n --hidden --no-ignore -i 'ACEL-G1-T2E|VerifierKeyAndRegistryControlOwner|VerificationAuthoritySpecificationOwner|RegistryObservationOwner|IssuerRegistryAuthorityOwner|PROPOSED_OPERATOR_DECISION|BLOCKED_SOURCE_NOT_FOUND|UNVERIFIED' docs governance EXTENSIONS ECOSYSTEM CVF_SESSION -g '*.md' -g '*.json' -g '*.py' -g '*.ts'`.
Exact roots cover source, tests, docs, JSON state/evidence and governed Local
evidence. External evidence is explicitly excluded under internal-only intake.
Before authoring, proposed T2E path/role-name matches were absent. Same-token
collision `PROPOSED_OPERATOR_DECISION` occurs in T2D planning dispositions and
is non-authoritative for an appointment. Same-token collision
`BLOCKED_SOURCE_NOT_FOUND` records the existing fail-closed disposition and is
not a new source. Same-token collision `UNVERIFIED` records admission posture,
not owner proof. Same-token collision `BLOCKED_SOURCE_NOT_FO` is a parser
fragment of that canonical disposition and is non-authoritative. Same-token
collision `CKED_SOURCE_NOT_FOUND` is another parser fragment of that canonical
disposition and is non-authoritative. T2C/T2D trust terms are accepted
design-input collisions.
Collision `ACEL` is a program identifier. Collision `CVF_SESSION` is a
continuity root. Collision `ECOSYSTEM` is a governed search root. Collision
`OWNER_CLAIM` is a source-table classification. Collision `PT` is an incidental
parser fragment. Each occurrence is non-authoritative for appointment.
Same-token collision `VerifierKeyAndRegistryControlOwner` occurs as a proposed role in this packet and is non-authoritative.
Same-token collision `VerificationAuthoritySpecificationOwner` occurs as a proposed role and is non-authoritative.
Same-token collision `RegistryObservationOwner` occurs as a proposed role and is non-authoritative.
Same-token collision `IssuerRegistryAuthorityOwner` occurs as a proposed role and is non-authoritative.
Same-token collision `E_CONTRACT_DESIGN_2026` is a parser fragment of a planned artifact path and is non-authoritative.
Disposition: proposed T2E output paths and role names were absent; disclosed
tokens are same-token collisions and not binding owner evidence.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G1-T2E-FOUR-OWNER-SOURCE-CONTRACT-DESIGN
reviewRoundCount: 0
priorFindingSetDigest: NOT_APPLICABLE_INITIAL_DISPATCH
dependencyAuditDisposition: COMPLETE_INITIAL_ACCEPTANCE_MATRIX
reworkFindingDisposition: NOT_APPLICABLE_INITIAL_DISPATCH
newIndependentCriticalEvidence: NONE
regressionGuardDisposition: BASELINE_NEGATIVE_TESTS_PLANNED
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
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

providerExecutionAuthority: FORBIDDEN

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T2E-FOUR-OWNER-SOURCE-CONTRACT-DESIGN","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"DOC_CHANGE","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/audits/","docs/reviews/","docs/baselines/","docs/work_orders/","docs/reference/agent_system_skills/","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/","governance/compat/"],"claims":["four proposed responsibility contracts only; no appointment or runtime source"],"requiredProof":["four-contract matrix","cross-contract separation matrix","circular authority rejection","thirteen-path hash reconciliation","worker-return fast gate","Local review"],"operatorCheckpoints":["actual accountable-party appointment","role combination","key custody","live issuer lookup","G1 implementation","runtime","public sync","deployment"],"forbiddenEffects":["edit parked evidence","credential access","key generation","network lookup","provider call","source implementation","worker commit","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/audits/CVF_ACEL_G1_T2D_SOURCE_OWNER_OPTIONS_2026-09-18.md","completenessClaimChanged":false}}
```

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t2d-source-owner-establishment","chainMode":"SUCCESSOR","chainOrdinal":1,"predecessor":{"path":"docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2D_SOURCE_OWNER_ESTABLISHMENT_2026-09-18.md","sha256":"e447b2852551a484a783d6096f99729c2c4396472d210cba90340f85f42da480"},"blockerDelta":{"prior":["key_registry_owner_unverified","authority_specification_owner_unverified","observation_log_owner_unverified","issuer_lookup_owner_unverified"],"resolved":[],"retained":["key_registry_owner_unverified","authority_specification_owner_unverified","observation_log_owner_unverified","issuer_lookup_owner_unverified"],"new":[],"reopened":[],"current":["key_registry_owner_unverified","authority_specification_owner_unverified","observation_log_owner_unverified","issuer_lookup_owner_unverified"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":1},"claims":[{"claimId":"ACEL-G1-T2E-FOUR-OWNER-DESIGN","claimClass":"OTHER","proofClass":"NAMED_OBSERVABLE_PROOF","evidenceRef":"docs/reviews/CVF_ACEL_G1_T2E_FOUR_OWNER_RESPONSIBILITY_LOCAL_DECISION_2026-09-18.md"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INTEGRATED_ROOT_CONTRACT"}
```

The design may clarify contracts but cannot resolve any operational-owner
blocker. Only later source evidence and explicit operator appointment can do so.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | exact two documentation outputs | design and return only; no appointment, acceptance or commit | paired baseline and reviewed T2D inputs | no runtime adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no selected adapter owner | no external ingress, auth, mutation or public claims | scope exclusion | adapter remains separately deferred | `DEFERRED_WITH_REASON` |

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | decision, baseline, work order | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | dispatch packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V62_2026-09-17.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact two outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| contract_source_reconciliation | WORKER_RETURN | worker | IMPLEMENTATION | exact two outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| frozen_input_integrity | WORKER_RETURN | worker | IMPLEMENTATION | read-only thirteen-path ledger | NO_MUTATION | closer | MATERIAL_COMMIT | contract_source_reconciliation |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker-return disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact two outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | frozen_input_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact two outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted outputs and Local review | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local completion review | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | authorized continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Worker Autonomy / No-Question Rule

The worker resolves ordinary contract-shape and gate defects within the two
owned paths without routine escalation. Missing actual appointments are
expected blockers, not reasons to invent parties. Stop only for source
contradiction, frozen drift, forbidden effects or an unrepairable out-of-scope
gate failure.

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| actor | INTERNAL_AGENT worker |
| role set | contract designer and evidence author; not owner, reviewer or closer |
| delegation depth | zero; no nested subagent |
| evidence basis | exact governed CVF sources; provider memory is `NOT_CVF_SOURCE` |
| gate sequence | source/frozen reconciliation; worker-return fast; Local review |
| self-review boundary | worker repairs owned documents but cannot accept them |
| role separation ledger | worker returns pending; Local reviews; operator appoints actual parties |
| escalation condition | authority conflict, circularity, frozen drift or forbidden effect |

## Agent Handoff Contract Control Block

| Field | Value |
|---|---|
| route | `SINGLE_AGENT_MULTI_ROLE`: one internal designer and independent Local reviewer |
| rolePattern | worker designer; Local reviewer/closer; operator appointment checkpoint |
| phase | dispatch -> contract design -> Local review -> separate continuity |
| baseHeadFor(phase) | dispatchBaseHead=`e47fad31191070bed9b57680118978e9a3973cce`; worker captures executionBaseHead |
| closureBaseHead | unset; Local records after accepted return |
| changedSetScope(phase) | exact two worker output paths only |
| traceScope(phase, actor) | source reads, frozen hashes, commands and start/end status |
| commitOwner(phase) | Local only |
| crossBatchIsolation | thirteen parked paths stay byte-identical and uncommitted |
| nextMoveSurfaces | Local updates active continuity only after disposition |

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT contract designer after dispatch

laneOwnedPaths: exact two Worker Output Inventory paths

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return, empty staging, exact worker delta and 13/13 frozen hash reconciliation

## Foundation Storage Layout Block

N/A with reason: documentation-only design; no durable foundation storage or
source layout is created.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_COMPLETION_2026-09-18.md`; Local-owned and created only if required after return |
| reviewerOwnedClosurePaths | returned outputs, Local disposition and separate continuity |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T2E_FOUR_OWNER_SOURCE_CONTRACT_DESIGN_WORKER_RETURN_2026-09-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required sections: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Decision / Disposition; Source Inventory;
Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution
Claim Boundary Control Block; External Knowledge Intake Routing; Epistemic
Process Block; Public Export Disposition; Claim Boundary; Return-Time
Closeability Recheck; `git status --short`; No-Commit Statement. Conditional
sections must use explicit N/A with reason.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
git diff --check
git status --short --untracked-files=all
git diff --cached --name-only
```

## Evidence Requirements

Return an exact source-to-field mapping for all four contracts; rejected
collision/circularity cases; responsibility/separation matrix; operator-input
ledger; output inventory; 13/13 frozen hashes with zero mismatch; empty staging;
zero external/provider/live calls; and final command results after the last
edit. Do not claim complete-corpus coverage or actual owner verification.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`DOC_CHANGE`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class DOC_CHANGE --role dispatcher --lifecycle-phase pre-dispatch`

Returned defects: NONE_RETURNED

Returned defect count: 0

Dispatch impact: no matched ADIF entry; normal fail-closed controls remain.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind held-dependency --batch-id ACEL-G1-T2E-FOUR-OWNER-SOURCE-CONTRACT-DESIGN --title "ACEL G1 T2E Four Owner Source Contract Design" --date 2026-09-18 --base e47fad31191070bed9b57680118978e9a3973cce --commit-mode WORKER_MUST_NOT_COMMIT --dependency ACEL-G1-T2D-OWNER-OPTIONS-REVIEWED --stdout` |
| generatedProfile | held-dependency and no-commit worker profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | populated exact four-contract scope, manifests, separation cases, evidence and role boundaries |
| checkerReadAheadConfirmation | dispatch, structure, closeability and review-cost checker sources read before authoring |
| docOnlyNewFields | four contract names, admission-evidence rows, cross-contract separation and circularity dispositions |
| claimBoundary | scaffold guides packet shape only |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_external_knowledge_intake_routing.py` |
| literalTokensReviewed | envelope placement/eight fields; Source Verification schema; closeability graph phases; convergence scalars; review headings; internal-only routing token |
| gateRunPurpose | confirmation of dispatch shape before release, not discovery or owner proof |
| claimBoundary | checker PASS cannot appoint owners or authorize source/runtime implementation |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | `internal governed input (no external intake)` |
| Chain map route | reviewed T2C/T2D governed artifacts -> operator choice -> Local work order -> internal worker return -> Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and paired Local decision |
| Internal source | `docs/audits/CVF_ACEL_G1_T2D_SOURCE_OWNER_OPTIONS_2026-09-18.md` |
| Disposition | `NOT_APPLICABLE_INTERNAL_ONLY_WITH_REASON`: no remote or copied external research is used |
| Claim boundary | internal inputs do not prove actual owner appointment or source existence |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: four explicit contracts and separation rules will
make appointment evidence requirements reviewable while retaining all four
operational blockers.

Evidence Comparison Requirement: worker compares actual T2C/T2D evidence with
the prediction for every field and negative case.

Contradiction Handling Requirement: report contradictory existing authority or
overlap with a Contradiction Or Gap Disposition; do not overwrite it.

Claim Update Requirement: mark each claim confirmed, revised, narrowed, or
invalidated and preserve unresolved operational blockers.

## Verification And Release Gate

Local must verify path isolation, paired-artifact consistency, 13/13 frozen
hashes, worker-output absence, pre-dispatch PASS and exact staging before the
dispatch packet is committed. Worker begins only from committed packet and
continuity. Machine PASS never creates an actual owner.

## Acceptance Criteria

- [ ] Exactly four proposed contracts cover all T2D dependencies without role collapse.
- [ ] Every contract states authority, source, writer, consumer, lifecycle, durable evidence, admission proof and fail-closed behavior.
- [ ] Cross-contract separation matrix rejects self-approval and circular authority.
- [ ] Actual accountable parties remain explicitly unappointed and all candidate admission remains `UNVERIFIED`.
- [ ] Only two worker-owned paths change; 13/13 parked hashes match; staging is empty.
- [ ] All named commands pass or the return is honestly `BLOCKED_WITH_REASON`.

Fail conditions: invented party or existing-source claim; implementation or
key material; circular authority admitted; parked drift; unowned mutation;
provider/live/public/deployment effect; false closure or operational admission.

## Review Gate

Local reviews contract completeness, separation of duties, evidence admission,
source fidelity, exact changed set and gates as one consolidated matrix.
Reviewer-fast and pre-commit follow only after bounded acceptance. Worker
handoff is not closure.

## Closure Checklist

- [ ] Contract/schema/path/authority/test/range/commit-plan audit completed.
- [ ] Worker-return fast and reviewer-fast evidence valid for their phases.
- [ ] No actual owner or runtime claim exceeds evidence.
- [ ] Material and continuity commits remain split.
- [ ] No successor opens automatically.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for source contradiction, output collision, frozen
drift, circular authority that cannot be resolved in contract prose, forbidden
effect, missing required evidence, or any out-of-scope failure. Missing actual
party appointment is retained as a blocked field; it does not prevent a
complete design return.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatcher |
| Provider or surface | private CVF workspace |
| Session or invocation | T2E packet authoring, 2026-09-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, hashes/status, scaffold preview, patch authoring, governance gates |
| Target paths | Local decision, paired baseline and this work order |
| Allowed scope source | operator instruction approving the four-responsibility model |
| Before status evidence | tracked worktree clean at HEAD `e47fad31191070bed9b57680118978e9a3973cce`; thirteen parked untracked paths are explicitly exempted; staging empty |
| After status evidence | exact three dispatch artifacts pending validation; worker outputs absent |
| Diff evidence | exact dispatch packet plus unchanged parked worktree context |
| Approval boundary | documentation-only four-contract design |
| Claim boundary | no appointment, key, source implementation, lookup, runtime or public effect |
| Agent type | Local dispatch author |
| Invocation ID | `acel-g1-t2e-four-owner-dispatch-20260918` |
| Expected manifest | Local decision, baseline, work order |
| Actual changed set | verified before dispatch commit |
| Manifest delta | pending final exact-path verification |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | four proposed source-owner contract documents and evidence requirements |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: no runtime receipt is claimed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: dispatch documentation only |
| invocationBoundary | internal shared-workspace documentation task |
| interceptionBoundary | no IDE, shell, filesystem, provider, CLI/MCP or runtime interception claim |
| claimLanguage | contract design is not owner appointment or source existence |
| forbiddenExpansion | keys, credentials, implementation, live lookup, admission, runtime, public sync, deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private contract-design dispatch with no public artifact authorization.

## Claim Boundary

This work order authorizes exactly two documentation outputs. It does not
appoint accountable parties, combine roles, create a key or registry, implement
lookup/observation, admit a candidate, close T2D, or authorize runtime,
provider, public-sync or deployment work.

## Operator Checkpoint

After Local accepts the returned design, the operator must separately name the
actual accountable party for each contract (and explicitly approve any role
combination) before Local may author an implementation or operational-source
establishment work order.
