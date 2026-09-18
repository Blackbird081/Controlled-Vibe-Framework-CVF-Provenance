# CVF Agent Work Order - ACEL G1 T2F R1 Contract Coherence Correction

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

Date: 2026-09-18

Batch ID: ACEL-G1-T2F-R1-CONTRACT-COHERENCE-CORRECTION

Dispatch base HEAD: `bcc346d0c15f5270ec350736b6407f72023650ef`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker role: one shared-workspace `INTERNAL_AGENT`

Reviewer/closer: Local orchestrator/reviewer

Worker return path: `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_WORKER_RETURN_2026-09-18.md`

## Dispatch Prompt Envelope

Role: internal source-contract designer correcting one rejected documentation
return; not source owner, implementer, reviewer or closer.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2F_R1_CONTRACT_COHERENCE_CORRECTION_2026-09-18.md`

Paired baseline: `docs/baselines/CVF_GC018_ACEL_G1_T2F_R1_CONTRACT_COHERENCE_CORRECTION_2026-09-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture `git rev-parse HEAD`, full status and staging before edits.

Current-time notes: the two initial T2F outputs already exist untracked and
are rejected for five consolidated design findings. Thirteen unrelated G1
paths remain parked and uncommitted.

Do-not-misread notes: modify the existing pair in place. Do not create a new
return, operational source, implementation file, key, credential, registry,
lookup, runtime behavior or successor tranche.

Required first actions: read startup/bootstrap/handoff, guard orientation,
literal gotchas, paired R1 baseline, this order, Local completion review,
initial two outputs, T2E design, T2C verifier contract and applicable checker
sources; capture initial output hashes and verify staging plus 13/13 parked
hashes before editing.

Return contract: close all five findings in the existing two outputs, run the
named gates, keep staging empty and return `COMPLETE_PENDING_REVIEW` only if
every acceptance row passes; otherwise return `BLOCKED_WITH_REASON`.

## Purpose

Correct the integrated T2F contract so every canonical hash is independently
recomputable, every referenced field is declared, all four operational-source
groups join the accepted T2C consumer contract, specification activation is
explicit and fail-closed, and every proposed path has literal collision
evidence. Preserve all valid initial evidence and all source-not-created
boundaries.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind held-dependency --batch-id ACEL-G1-T2F-R1-CONTRACT-COHERENCE-CORRECTION --title "ACEL G1 T2F R1 Contract Coherence Correction" --date 2026-09-18 --base bcc346d0c15f5270ec350736b6407f72023650ef --commit-mode WORKER_MUST_NOT_COMMIT --dependency ACEL-G1-T2F-INITIAL-RETURN-REJECTED --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id acel-g1-t2f-source-contract-design-first-authoring --prior-finding-set-digest d84f6bd23f9fa9e52c71b0aeeb924a4af89b0b7b31263f2231fb465e39b0f4b0 --cumulative-external-invocation-count 0 --external-invocation-ceiling 0 --new-independent-critical-evidence T2F-R1-01,T2F-R1-02,T2F-R1-03,T2F-R1-04,T2F-R1-05 --scec-problem-key acel-g1-t2f-r1-contract-coherence --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INTEGRATED_ROOT_CONTRACT --stdout` |
| generatedProfile | held-dependency plus internal REWORK and no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | bound the Local finding digest, exact existing pair, five-finding correction matrix, consumer joins and stop rules |
| checkerReadAheadConfirmation | dispatch-quality, convergence, closeability, review-cost, worker-return, trace and structural checker sources |
| docOnlyNewFields | source-record canonicalization profile; active-head/fork contract; explicit activation events; path collision ledger |
| claimBoundary | dispatch-authoring provenance only; no repair or source existence is predeclared |

## Authority Chain And Dependency Release Evidence

| Dependency | Evidence | Release condition | Disposition |
|---|---|---|---|
| initial T2F dispatch | material `1909c5a72`; continuity `bcc346d0c` | exact two output paths and no-commit rule | ACCEPT |
| initial returned pair | audit SHA-256 `eb169f99a39d43050e15102c7bcdc2294a274b1cde524fcc23f261e4101e38e6`; return SHA-256 `8735b7b7c5874e30219fd55599d5f6af508caf9d81cc19e87d535792f512fbb4` | modify in place; not accepted authority | ACCEPT_AS_REWORK_INPUT |
| consolidated finding set | `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_COMPLETION_2026-09-18.md`; SHA-256 `d84f6bd23f9fa9e52c71b0aeeb924a4af89b0b7b31263f2231fb465e39b0f4b0` | T2F-R1-01 through T2F-R1-05 closed together | ACCEPT |
| accepted consumer | T2C verifier trust-anchor design, Signature/Key-ID and Genuine Lookup Provenance sections | exact schema joins, not narrative similarity | ACCEPT |
| source creation or implementation | no verified authorization | later separate operator/Local packet | PARKED_NO_SOURCE_CREATION_AUTHORITY |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| intake summary | same-scope internal documentation rework |
| scope classification | integrated architecture/schema correction |
| risk sensitivity | high trust-boundary semantics; zero operational effect |
| selected route mode | `SINGLE_AGENT_MULTI_ROLE`: one worker followed by independent Local review |
| role separation basis | worker edits evidence but cannot accept, stage or commit it |
| escalation condition | new authority contradiction, forbidden path need, parked drift or operational effect |

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: REWORK

dispatchSurface: INTERNAL_AGENT

parentAssignmentId: ACEL-G1-T2F-OPERATIONAL-SOURCE-ESTABLISHMENT-CONTRACT

reviewRoundCount: 1

priorFindingSetDigest: d84f6bd23f9fa9e52c71b0aeeb924a4af89b0b7b31263f2231fb465e39b0f4b0

dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR

reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS

newIndependentCriticalEvidence: T2F-R1-01,T2F-R1-02,T2F-R1-03,T2F-R1-04,T2F-R1-05

regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT

cumulativeExternalInvocationCount: 0

externalInvocationCeiling: 0

usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT

quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT

nextDispatchDisposition: ONE_CONSOLIDATED_REWORK

rootCauseClusterId: acel-g1-t2f-source-contract-design-first-authoring

reworkGeneration: 1

consolidatedDefectClassSweep: COMPLETE_BEFORE_REWORK_DISPATCH

successorTrancheOpened: NO

implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY

preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION

preExecutionReviewTrigger: NONE

nextRoutineReviewBoundary: WORKER_RETURN

reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Consolidated R1 Correction Matrix

### T2F-R1-01 - Canonical Hash And Chain Profile

Define one reusable profile, `cvf.source-record-canonicalization@1`, with:

- RFC 8785 JCS over a named JSON object; UTF-8; no BOM;
- lowercase 64-hex SHA-256 digest;
- explicit `domain` and `profileVersion` literals inside every preimage;
- exact preimage field list and nested/list ordering rules;
- a stored digest excluded from its own preimage;
- for chained records, explicit `priorEntryHashHex`, with `null` at genesis,
  included as a normal JCS field rather than ambiguous byte concatenation;
- fail-closed rejection of unknown profile, extra/missing preimage fields,
  malformed digest, duplicate identity or recomputation mismatch.

Apply this profile consistently to Groups 1-4. Do not silently change the T2C
receipt's already accepted `cvf.verifierReceipt` RFC 8785 JCS profile. Add a
compact positive recomputation example and negative mutations for self-hash,
prior-hash, field omission and canonicalization/profile drift. Cryptographic
examples prove only internal design consistency, never source existence.

### T2F-R1-02 - Complete Schemas And Durable Receipt Sources

Group 1 must declare exact proposed paths for both the registry and append-only
lifecycle receipts. Its key row and registry envelope must include every field
used by versioning and T2C: global `registrySnapshotId`, monotonic
`registrySnapshotVersion`, `writeTimestamp`, `keyId`, Ed25519 public key,
algorithm, role/authorized verification authorities, issued/expiry/revocation
times, status and row hash. Define duplicate-key-ID and public-key-alias
rejection. Lifecycle rows bind transition ID, snapshot before/after, actor,
time, prior entry hash and entry hash.

Group 2 must declare all specification and decision-event fields used by
proposal, approval, activation, rejection and supersession. Group 3 must
declare every snapshot/log field in R1-03. Group 4 must declare a global
registry snapshot identity/version/hash, per-entry version, canonical issuer
content hash and every lookup-response binding in R1-03.

No table may reference a version, timestamp, hash, role, result or receipt
field absent from its own declared schema.

### T2F-R1-03 - Exact T2C Consumer Joins

Reconcile the T2F schemas field-for-field with T2C:

- Group 1 supports exact `signatureKeyId`, single exact match, duplicate ID and
  public-key-alias rejection, active-time checks and a key role that authorizes
  issuance for `verificationAuthority`.
- Group 3 provides a stable `snapshotId`, registry name/version, immutable
  snapshot bytes or exact immutable artifact reference plus retrievable bytes,
  `snapshotHashHex`, `observedAt`, source `authority`, observer identity,
  correction/supersession fields, `priorEntryHashHex` and `entryHashHex`.
- Define `lookup(snapshotId)` and `countObservationsFor(snapshotId)` exactly.
  Historical corrections must not make every corrected snapshot permanently
  forked: return exactly one non-superseded active head; zero or multiple
  unresolved heads fail closed. Original records remain readable.
- Group 4 registry lookup consumes the exact observed snapshot bytes and
  returns one of `IDENTITY_CONFIRMED`, `IDENTITY_REJECTED`, or
  `IDENTITY_UNRESOLVED`. Its durable response binds lookup ID, issuer identity,
  claimed issuer hash, snapshot ID/hash/version, entry version, result/error,
  queried time, consumer identity, observation ID and response-chain hashes.
- Bind the freshness threshold to an activated authority-specification field
  or another exact decision-owner governed source; missing, malformed or
  conflicting policy fails closed.

Include a consumer-binding table showing every T2C input, its exact T2F source
field and failure result. Add negative probes for missing/ambiguous snapshot,
hash mismatch, stale observation, wrong authority, unresolved fork, wrong key
role, duplicate key/alias and response-to-snapshot mismatch.

### T2F-R1-04 - Explicit Approval, Activation And Supersession

Replace automatic "most recent approved" activation with append-only decision
events. Approval does not activate. Only the independent activation approver
may append `ACTIVATED` or `SUPERSEDED` events over exact `specVersion` plus
canonical hash. Define deterministic ordering, immutable decision identity and
an invariant that exactly zero or one specification is active. Two active
heads, duplicate/conflicting decisions, author self-activation or a decision
whose recomputed hash differs must reject; never resolve by latest timestamp or
largest version automatically.

### T2F-R1-05 - Literal Proposed-Path Collision Ledger

For every proposed file or bounded path family, record:

- normalized repository-relative path/family;
- exact `Test-Path -LiteralPath` result where a literal path exists;
- exact `rg -n --hidden --no-ignore -F` token search, roots and relevant
  matches for both the full path and stable owner token;
- collision classification and Local-review disposition;
- explicit reminder that absence is not creation or implementation proof.

Do not reuse the generic tranche-token query as path-collision evidence.

## Required Artifact Manifest

| Artifact | Required worker action |
|---|---|
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | MODIFY in place: close all five findings and reconcile every dependent section |
| `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_WORKER_RETURN_2026-09-18.md` | MODIFY in place: truthful R1 evidence, updated hashes/status/gates and no-commit return |

Exact equality is required between these two paths, worker-owned changes and
the Changed Files table. No new worker path, deletion or rename is allowed.

## Work-Order Fulfillment Manifest

| Required path | Required action | Fulfillment proof |
|---|---|---|
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | rewrite in place to close T2F-R1-01 through T2F-R1-05 | finding-to-locator ledger, final SHA-256, exact two-path diff and gates |
| `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_WORKER_RETURN_2026-09-18.md` | replace rejected status/evidence with the R1 successor return | successor SCEC, before/after hashes, command evidence, empty staging and no-commit statement |

The two rows above are the exact fulfillment set. Every other path is read-only.

## Write Ownership

Worker owns uncommitted edits only to the exact two paths above. Local owns
review, minor evidence-only corrections after return, final disposition,
material commit and continuity commit. Existing dispatch/review/continuity,
all proposed operational paths and all thirteen parked G1 paths are read-only.

## Agent Roles

| Role | Responsibility |
|---|---|
| operator | retains every later source-creation, principal, key and credential checkpoint |
| Local orchestrator/dispatcher | freezes the five-finding R1 contract and commits dispatch/continuity |
| INTERNAL_AGENT worker | corrects exactly two documentation outputs without staging or commit |
| Local reviewer/closer | evaluates returned evidence, applies only minor evidence-determined corrections and owns final disposition/commit |
| session-sync steward | updates continuity only after a material review or dispatch state change |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| actor | one shared-workspace INTERNAL_AGENT worker |
| role set | source-contract designer and evidence author; not authority owner, reviewer or closer |
| delegation depth | zero; no nested subagent |
| evidence basis | exact governed CVF sources; provider memory is `NOT_CVF_SOURCE` |
| gate sequence | frozen reconciliation; pre-implementation; worker-return fast; Local review |
| self-review boundary | worker repairs owned documents but cannot accept, stage or commit them |
| role separation ledger | worker returns pending; Local reviews, closes and commits; operator retains new authority decisions |
| escalation condition | authority conflict, third output, parked drift, source creation or forbidden external effect |

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`,
   `CVF_SESSION_MEMORY.md` and the active handoff.
2. `docs/reference/guard_orientation/README.md` and the governed literal
   gotchas reference.
3. Paired R1 baseline, this work order and the Local completion review.
4. Both current worker outputs, T2E four-owner design, all appointments and
   the accepted T2C verifier design.
5. Applicable checker sources named in the read-ahead block.

## Pre-Flight Checks

- Capture full HEAD and complete status; record initial hashes for both worker
  outputs.
- Confirm staging is empty and both R1 dispatch artifacts are committed.
- Recompute the thirteen parked hashes against the current return ledger.
- Confirm no third T2F worker output or proposed operational path exists.
- Run pre-implementation before editing and record the exact outcome.

## Worker Autonomy / No-Question Rule

Repair all dependent narrative, matrices, schemas, negative cases and worker
evidence needed by the five findings without asking the operator. Stop only if
the correction requires a third output, operational source creation, a changed
party/authority decision, forbidden external effect or a parked-path mutation.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| exact five-finding repair boundary | REVIEWED_DECISION | `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_COMPLETION_2026-09-18.md` | Findings / Position | T2F-R1-01 through T2F-R1-05 | Local reviewer | ACCEPT |
| key-registry fields and checks | CURRENT_AUTHORITY | `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` | Key Identity And Lifecycle; Signature Validity | `SignatureValidityCheck` | accepted T2C design | ACCEPT |
| observation and registry lookup joins | CURRENT_AUTHORITY | `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` | Genuine Lookup Provenance | `LookupProvenanceCheck` | accepted T2C design | ACCEPT |
| operational sources exist | SOURCE_EXISTENCE | initial T2F audit | source group dispositions | proposed paths only | future owners | REJECT |

## Negative Search And Collision Discipline

| Field | Evidence / disposition |
|---|---|
| exact path probes | `Test-Path -LiteralPath docs/baselines/CVF_GC018_ACEL_G1_T2F_R1_CONTRACT_COHERENCE_CORRECTION_2026-09-18.md` and the corresponding exact work-order-path probe each returned `False` before authoring |
| exact command/query | `rg -n --hidden --no-ignore -F "ACEL-G1-T2F-R1-CONTRACT-COHERENCE-CORRECTION" docs governance EXTENSIONS ECOSYSTEM CVF_SESSION -g '*.md' -g '*.json' -g '*.py' -g '*.ts'` |
| searched roots | `docs`, `governance`, `EXTENSIONS`, `ECOSYSTEM`, `CVF_SESSION` |
| coverage | Markdown, JSON, Python and TypeScript source, test, governed-document and evidence surfaces |
| result | only the newly authored Local review and paired dispatch packet references; `ACCEPT_PLANNED_REFERENCE_ONLY` |
| authoritative-input occurrence | the pre-existing T2C design path/token is accepted authority input and is not an R1 output-path collision |
| absent-versus-collision disposition | exact new packet paths were absent at the pre-authoring probe; later same-token occurrences are the one intentional packet family; `ACCEPT_NO_COLLISION` |
| worker obligation | perform and publish the separate literal proposed-operational-path collision ledger required by T2F-R1-05 |

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T2F-R1-CONTRACT-COHERENCE-CORRECTION","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"DOC_CHANGE","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"KNOWN_PATTERN"},"pathFamilies":["docs/audits/","docs/reviews/","docs/reference/","docs/work_orders/","docs/baselines/","governance/compat/","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/"],"claims":["same two-path T2F contract can close one consolidated finding set"],"requiredProof":["T2F-R1-01 through T2F-R1-05","exact two-path delta","13/13 parked hashes","worker-return fast gate"],"operatorCheckpoints":["new authority decision","third worker output","source creation or external effect"],"forbiddenEffects":["source or code creation","key or credential action","provider/live/network","worker commit","public sync","deployment"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"N/A with reason: bounded named files","completenessClaimChanged":false}}
```

Expected route: `P3_ELEVATED`; shadow routing only. Full legacy gates remain required.

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t2f-r1-contract-coherence","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["canonical_hash_profile_incoherent","declared_schemas_incomplete","t2c_consumer_join_unsatisfied","activation_conflict_semantics_incoherent","proposed_path_collision_evidence_missing"],"reopened":[],"current":["canonical_hash_profile_incoherent","declared_schemas_incomplete","t2c_consumer_join_unsatisfied","activation_conflict_semantics_incoherent","proposed_path_collision_evidence_missing"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[{"claimId":"ACEL-G1-T2F-R1-CORRECTION-DISPATCH","claimClass":"DOCUMENTATION_ONLY","proofClass":"PROPOSAL_ONLY_NO_RUNTIME_READINESS","evidenceRef":"docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_COMPLETION_2026-09-18.md"}],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INTEGRATED_ROOT_CONTRACT"}
```

The R1 worker return must replace its current independent SCEC block with a
`SUCCESSOR` block for this problem key, ordinal 1, binding the committed R1
work-order bytes and truthfully resolving or retaining each finding blocker.
Operational-source-not-created facts remain claim boundaries; they are not
design-defect blockers to launder as resolved source establishment.

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | Local review plus paired R1 packet | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired R1 packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact two existing outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | existing worker-return ADIF disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact two existing outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact two outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | returned pair and Local disposition | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local completion review | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | authorized continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | `SINGLE_AGENT_MULTI_ROLE`: one INTERNAL_AGENT repair worker, then Local reviewer/closer |
| rolePattern | Local dispatcher -> no-commit worker -> Local reviewer/commit owner |
| phase | consolidated R1 documentation repair |
| baseHeadFor(phase) | dispatchBaseHead=`bcc346d0c15f5270ec350736b6407f72023650ef`; worker captures committed execution HEAD |
| closureBaseHead | Local records after accepted return |
| changedSetScope(phase) | exact same two uncommitted T2F output paths |
| traceScope(phase, actor) | source reads, before/after hashes, collision commands, gates and status |
| commitOwner(phase) | Local only; worker forbidden to stage or commit |
| crossBatchIsolation | thirteen parked paths remain byte-identical and uncommitted |
| nextMoveSurfaces | Local continuity only after returned R1 disposition |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT T2F R1 contract designer after dispatch

laneOwnedPaths: exact two Required Artifact Manifest paths

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: updated worker return, empty staging, exact two-path delta and 13/13 frozen reconciliation

## Foundation Storage Layout Block

N/A with reason: R1 designs proposed source/storage contracts but creates no
storage path, directory, registry, log or runtime layout.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_WORKER_RETURN_2026-09-18.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required sections: Purpose; Target / Source; Scope / Methodology; Findings /
Position; Risk / Corrective Action; Decision / Disposition; Review-Dispatch
Convergence Control; Semantic Convergence Outcome; Source Inventory; Checker
Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim
Boundary Control Block; External Knowledge Intake Routing; Rescan Intelligence
Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance
Learning Disposition; Epistemic Process Block; Public Export Disposition;
Claim Boundary; Return-Time Closeability Recheck; Frozen-Path Reconciliation;
git status; Changed Files; Command Evidence; Worker Experience Retrospective;
No-Commit Statement.

Update `reworkGeneration` to 1, preserve the root-cause cluster, record the
prior/final audit and return hashes, enumerate every finding-to-repair locator,
and replace initial evidence rather than appending contradictory status.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/check_markdown_structural_completeness.py --base <executionBaseHead> --head HEAD --all-changed --enforce
git diff --check
git diff --cached --name-only
git status --short --untracked-files=all
```

## Execution Plan

1. Freeze the initial pair and parked-path identities.
2. Define the single source-record canonicalization profile and repair all
   hash/preimage rows together.
3. Complete Groups 1-4 schemas, receipts and explicit activation events.
4. Reconcile every T2C consumer input and fork/freshness failure rule.
5. Execute and record the literal proposed-path collision ledger.
6. Update every dependent matrix, checklist, decision and claim boundary.
7. Rewrite the existing worker return with R1 evidence, run named gates and
   return without staging or commit.

## Evidence Requirements

Return a five-row finding-to-repair ledger; exact canonical-preimage field
lists; at least one recomputable positive digest plus the required mutation
probes; complete source/consumer field mapping; approval/activation conflict
probes; literal proposed-path collision commands/results; before/final hashes
for the two outputs; 13/13 parked reconciliation; exact two-path delta; empty
staging; zero external effects; and final gate results after the last edit.

## Acceptance Criteria

- [ ] All five finding IDs map to corrected contract locators and adversarial probes.
- [ ] One non-self-referential RFC 8785 JCS source-record profile governs all new source digests.
- [ ] Every field used by lifecycle, versioning, integrity, access or consumers appears in its schema.
- [ ] T2C key, observation and issuer-lookup inputs map field-for-field to T2F sources.
- [ ] Approval, activation and supersession are explicit; conflicts never resolve latest-wins.
- [ ] Literal proposed-path collision ledger covers every exact path/family.
- [ ] All four groups remain `SOURCE_NOT_CREATED`; candidate admission remains `UNVERIFIED`.
- [ ] Existing two paths only; 13/13 parked hashes match; staging empty; no commit.
- [ ] Named commands pass or the return is truthfully blocked.

Fail conditions: self-referential hash; serializer ambiguity; undeclared
consumed field; non-joinable T2C consumer; automatic latest-wins activation;
generic-token-only path evidence; third output; parked drift; source/code/key/
credential/live/runtime/public/deployment effect; false acceptance claim.

## Review Gate

Local reviews all five finding closures as one dependency matrix covering
canonical preimages, schemas, T2C joins, authority/state transitions, collision
evidence, negative probes, exact range and commit plan. Worker gate success is
necessary but not semantic acceptance. Reviewer-fast and pre-commit run only
after the returned pair is coherent.

## Closure Checklist

- [ ] Five findings are closed without introducing a new independent defect.
- [ ] Positive digest recomputes and every mutation probe fails closed.
- [ ] Schema-to-consumer matrix has no missing or invented field.
- [ ] Approval/activation/supersession has one unambiguous active head.
- [ ] Collision ledger covers every proposed path/family.
- [ ] Exact two worker paths only; thirteen parked hashes preserved.
- [ ] Worker return fast and Local reviewer gates pass.
- [ ] Material and continuity commits remain split.
- [ ] No implementation successor opens automatically.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for a new source/authority contradiction, required
third path, operational source or code need, parked drift, forbidden effect or
any acceptance requirement impossible within the exact two-path scope. Do not
stop for ordinary in-scope schema and documentation decisions governed by the
five-finding contract.

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | reuse `docs/reviews/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_COMPLETION_2026-09-18.md`; Local may update only after R1 return |
| reviewerOwnedClosurePaths | returned pair, Local disposition and separate continuity |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | REWORK convergence scalars; SCEC chain fields; closeability graph; exact manifest; worker-return required headings; trace labels |
| gateRunPurpose | confirm the fully authored packet before dispatch, not discover requirements or prove correction |
| claimBoundary | checker PASS cannot accept the worker's semantic design |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`DOC_CHANGE`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class DOC_CHANGE --role dispatcher --lifecycle-phase pre-dispatch`

Returned defects: NONE_RETURNED

Returned defect count: 0

Dispatch impact: no matched ADIF entry; all five Local findings remain mandatory.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/dispatcher after independent review |
| Provider or surface | private CVF workspace |
| Session or invocation | T2F consolidated R1 dispatch authoring, 2026-09-18 |
| Working directory | repository root |
| Command or tool surface | governed reads, SHA-256 reconciliation, focused semantic probes, scaffold preview, ADIF resolver, apply_patch and gates |
| Target paths | Local completion review plus paired R1 baseline and this work order |
| Allowed scope source | standing operator orchestration authority and committed initial T2F packet |
| Before status evidence | tracked worktree clean at HEAD `bcc346d0c`; initial pair plus thirteen parked paths are explicitly isolated untracked evidence; staging empty |
| After status evidence | exact three Local dispatch paths pending; worker and parked paths excluded from staging |
| Diff evidence | exact staged Local packet before material commit |
| Approval boundary | one documentation-only INTERNAL_AGENT R1 |
| Claim boundary | no source, key, credential, implementation, live/runtime/public effect |
| Agent type | Local orchestrator/dispatcher and future reviewer/closer |
| Invocation ID | `acel-g1-t2f-r1-contract-coherence-dispatch-20260918` |
| Expected manifest | Local completion review, paired R1 baseline and this work order |
| Actual changed set | reconciled before commit |
| Manifest delta | pending exact staging reconciliation |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | consolidated correction of two documentation artifacts |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | N/A with reason: dispatch claims no runtime/source receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: Local review and dispatch documentation only |
| invocationBoundary | internal shared-workspace documentation task |
| interceptionBoundary | no IDE/provider/CLI/MCP/runtime interception claim |
| claimLanguage | rework-ready, not repaired or source-established |
| forbiddenExpansion | source/code creation, keys, credentials, live lookup, admission, runtime, public sync, deployment |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Chain map route | initial packet -> INTERNAL_AGENT return -> Local rejection -> INTERNAL_AGENT R1 -> Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this R1 work order and Local completion review |
| Internal source | `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` |
| Disposition | `NOT_APPLICABLE_INTERNAL_ONLY_WITH_REASON`: no external source admitted |
| Claim boundary | Local remains final technical decision owner |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Legacy Absorption Coverage Index Disposition

`NOT_APPLICABLE_WITH_REASON`

Reason: this bounded rework modifies two first-party governed documents and
does not intake, enumerate, absorb or claim coverage of a legacy or external
repository corpus.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: one consolidated R1 can make the four proposed
contracts internally recomputable and T2C-consumable without changing the
source-not-created boundary.

Evidence Comparison Requirement: map each finding ID to exact corrected
fields, consumer joins, negative probes and final gate evidence.

Contradiction Handling Requirement: stop rather than invent an authority,
source, implementation or third output.

Claim Update Requirement: distinguish corrected design coherence from future
source existence, operational verification and candidate admission.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private internal R1 dispatch; no public-sync authority.

## Operator Checkpoint

No operator checkpoint is needed for this same-scope documentation R1. Return
to the operator only if repair requires a new authority decision, third output,
source creation, key/credential action, provider/live/network/public effect or
implementation authorization.

## Claim Boundary

This work order authorizes only in-place correction of two uncommitted
documentation outputs. It does not approve the proposed operational paths or
authorize any source, schema/code implementation, key, credential, registry,
lookup, candidate admission, runtime, provider, public-sync or deployment
effect.
