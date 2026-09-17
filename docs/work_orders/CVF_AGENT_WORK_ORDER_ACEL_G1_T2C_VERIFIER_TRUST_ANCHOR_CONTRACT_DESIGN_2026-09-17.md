# CVF Agent Work Order - ACEL G1 T2C Verifier Trust-Anchor Contract Design

Memory class: governed-worker-dispatch

docType: work_order

Status: APPROVED_FOR_EXECUTION

Date: 2026-09-17

Batch ID: ACEL-G1-T2C-VERIFIER-TRUST-ANCHOR-CONTRACT-DESIGN

dispatchBaseHead: 17b3cb0fbc11e8b97b42223b57f0f98f5f2e1273

Authoring base head: `3796ff4ce85b2343b857be7da5bc69cb9447266f`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker role: one shared-workspace `INTERNAL_AGENT`

Reviewer/closer: Local orchestrator/reviewer

## Dispatch Prompt Envelope

Role: hypothetical trust-anchor contract designer and evidence producer, not reviewer.

Canonical packet: `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

executionBaseHead: capture `git rev-parse HEAD` and status before edits.

Current-time notes: 2026-09-18; the operator authorized Local audit and dispatch of this hypothetical-only documentation task.

Do-not-misread notes: no existing G1 key registry or genuine lookup owner was source-verified. Describe proposed interfaces only. No actual keys, registry lookup, runtime or candidate admission.

Required first actions: read startup surfaces, guard orientation, literal gotchas, paired baseline, this work order, named sources and applicable checker sources; verify the thirteen frozen hashes and three output-path absences.

Return contract: create exactly three outputs, run required gates, do not stage or commit, and return `COMPLETE_PENDING_REVIEW` only with passing evidence. Otherwise return `BLOCKED_WITH_REASON`.

## Purpose

Design a bounded hypothetical documentation-only contract for verifier-authenticated issuer receipts. The Local architecture decision selects Ed25519 but has not verified a CVF owner for the trusted public-key registry or genuine issuer-registry lookup. The worker must keep those operational facts absent and admission fail-closed.

## Authority Chain And Dependency Release Evidence

The operator's 2026-09-18 instruction authorizes Local audit and dispatch after the explicit hypothetical-only design question. Local selected a design direction at `1c5c01675`; V62 previously allowed Local GC-018/work-order authoring only, so this new instruction is the release authority for this bounded worker task. The paired baseline is `docs/baselines/CVF_GC018_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md`. T2B review `4bb04c836` remains terminally parked. No statement in this chain grants keys, live lookup, implementation or automatic successor dispatch.

| Dependency | Evidence | Release condition | Current disposition |
|---|---|---|---|
| Separate-tranche architecture selection | `docs/reviews/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_LOCAL_ARCHITECTURE_DECISION_2026-09-17.md` | Selected topology only | SATISFIED_FOR_AUTHORING |
| Trusted G1 verifier public-key registry owner | Paired baseline Source Verification Block and targeted search | Existing owner is rejected; proposed interface only, never an admission source | SATISFIED_FOR_HYPOTHETICAL_DESIGN_ONLY |
| Genuine lookup provenance owner | T2B-RV-F1 counterexample and paired baseline search | Existing owner is rejected; proposed provenance only and all actual admission remains `UNVERIFIED` | SATISFIED_FOR_HYPOTHETICAL_DESIGN_ONLY |
| Dispatch authority | Operator's 2026-09-18 audit-and-dispatch instruction | Local release decision, fresh base/status/forbidden-state evidence and passing pre-dispatch gate | ACCEPT_FOR_DOCUMENTATION_ONLY |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| intake summary | documentation-only hypothetical G1 trust-anchor contract |
| scope classification | hypothetical design only, no operational owner claim |
| risk sensitivity | high: authentication and issuer admission; no key handling now |
| selected route mode | `SINGLE_AGENT_MULTI_ROLE`: one worker designs and self-checks; Local independently reviews/closes |
| role separation basis | worker cannot commit or accept own contract; Local owns source admission and final disposition |
| escalation condition | source owner absent/contradictory, key or live action needed, or any T2B same-tranche repair |

## Roles, Write Ownership And Scope

Local is dispatch author, source-verification owner and independent reviewer. The worker may write only the three required outputs below. The worker must not edit or claim acceptance of the 13 parked G1 evidence paths. No nested delegation, network lookup, key generation/import, credential access, TypeScript/Python runtime implementation, checker/test mutation, configuration change, public sync or deployment is in scope. The worker's Claude invocation is the explicitly authorized internal execution surface, not a grant to call another provider from the task.

## Required First Reads

The worker reads the active bootstrap/front door/handoff, paired baseline, Local T2C decision, T2B independent review, the work-order template, guard orientation and applicable checker sources before writing. Provider memory is `NOT_CVF_SOURCE`.

## Pre-Flight Checks

Pre-flight requires fresh HEAD/status, exact three-output path absence, 13-path hash reconciliation, actual forbidden filesystem state, ADIF resolver refresh and pre-dispatch gate. A gate pass does not establish an operational owner; the work is hypothetical documentation only.

## Write Ownership

Worker write ownership is exactly the three Required Artifact Manifest paths. All existing G1 evidence, source, tests, checkers, continuity and secret stores are read-only. Local owns review, commits and handoff.

## Proposed Design Requirements If Released

1. Specify a versioned, domain-separated deterministic UTF-8 JCS signing preimage with exact field types and ordering. Bind round, authority and issuer identity, authority-attestation hash, source-owned registry snapshot identity/hash, lookup result, observation/issuance times and unique receipt identity. Define the signature/key-ID envelope, duplicate-key-ID and key-alias rules. No receipt-supplied public key or candidate-supplied registry path may become trust authority.
2. Separate three predicates: canonical/content integrity; verifier signature under a CVF-trusted key with role/validity/revocation checks; and genuine lookup provenance from a source-owned registry observation. A passing signature without the third predicate remains `UNVERIFIED` and inadmissible.
3. Specify exact TypeScript decision-time and Python persisted-evidence verification ownership. Both must independently recompute the same preimage and fail closed on unknown/revoked/expired/ambiguous keys, malformed encodings, wrong domain/round/authority/snapshot, time ordering, stale/forked provenance and missing trust material.
4. Include positive and adversarial vectors: self-authored receipt with a correct SHA-256 but no signature; signature under receipt-supplied key; valid signature under revoked/wrong-role key; modified `keyId`/alias; true signature with fabricated or mismatched lookup; stale/forked snapshot; cross-round replay; invalid canonicalization; and unavailable trust registry. State expected `UNVERIFIED`/admission denial for each negative case.
5. Define proposed key custody, rotation, revocation, historical validation and registry snapshot provenance as explicitly hypothetical interfaces. Record existing-owner evidence as absent; do not manufacture a registry or sign test receipts with operational keys. Do not return a positive admission outcome for a hypothetical receipt.
6. Reconcile the T2B human/JSON contract and all thirteen parked paths as rejected or deferred evidence, never as accepted implementation. No automatic G1 implementation successor is permitted.

## Execution Plan

The worker sequence is source/frozen-hash capture, design of human and JSON hypothetical contracts, self-consistency and adversarial-vector checks, worker-return evidence, then stop without commit for Local review. It never includes live lookup or key creation.

## Required Artifact Manifest

| Path | Required action |
|---|---|
| `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` | human trust-anchor contract, owner ledger and adversarial matrix |
| `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_MANIFEST_2026-09-17.json` | matching machine-readable schema, predicates, source and vector ledger |
| `docs/reviews/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_WORKER_RETURN_2026-09-17.md` | no-commit source/gate/frozen-hash evidence and terminal return |

All returned artifacts must remain uncommitted until independent Local review. Local checks these three paths are absent and records actual filesystem state of every forbidden path before dispatch.

## Forbidden Filesystem State At Dispatch

| Path family | Expected state | Actual state at Local 2026-09-18 audit | Worker action |
|---|---|---|---|
| three Required Artifact Manifest paths | ABSENT | ABSENT, each checked with `Test-Path -LiteralPath` | create only these outputs |
| thirteen frozen G1 evidence paths | PRESENT_READ_ONLY | PRESENT; 13/13 SHA-256 matched the Parked Evidence Freeze ledger | read and rehash; never edit, stage or commit |
| all other repository paths | NO_WORKER_WRITE | existing tracked/untracked state is not worker-owned | do not alter |

## Work-Order Fulfillment Manifest

Required artifacts are exactly the three Required Artifact Manifest paths. Forbidden mutations are the thirteen frozen paths, all existing tracked files, staging, commits, credentials, runtime/configuration and any fourth worker output. Required proof literals: `executionBaseHead`, start/end `git status --short`, 13/13 hash reconciliation, human/JSON parity, negative matrix, worker-return fast gate, no-commit statement and `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

## Parked Evidence Freeze

The ten exact paths and expected SHA-256 values in `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md` under Parked Evidence Freeze remain read-only. The three T2B outputs also remain read-only: human audit SHA-256 `5147bf905113e4c750f6b7f4aa84e1aeb4575417299258ad10dcf8ebbbb5575a`; JSON manifest SHA-256 `5bfe577495bac91b99344827172d859ff0389cf1f67e14097d5af113a16eaeb9`; worker return SHA-256 `25963195262048746436daee2ab4b2304fa96d54c8197ed375ab98e5e7dd29ce`. Local verified all 13 hashes match on 2026-09-17. A released worker must recheck before and after; any drift blocks the return.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified locator | Disposition |
|---|---|---|---|---|
| Local-selected Ed25519 direction | DESIGN_AUTHORITY | `docs/reviews/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_LOCAL_ARCHITECTURE_DECISION_2026-09-17.md` | Local Architecture Decision | ACCEPT |
| T2B public-hash receipt forgery | REJECTION_AUTHORITY | `docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_INDEPENDENT_REVIEW_2026-09-17.md` | T2B-RV-F1 | ACCEPT |
| Existing G1 verifier key and lookup owners | OWNER_CLAIM | `docs/baselines/CVF_GC018_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` | Source Verification and Negative Search sections | REJECT |
| HMAC live manifest and Web service token as G1 owner | ADJACENT_PATTERN | `docs/reference/CVF_LIVE_EVIDENCE_MANIFEST_AND_RERUN_STANDARD_2026-06-06.md`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | Signature Boundary; `computeServiceRequestSignature` | REJECT |

## Negative Search And Collision Discipline

Search roots: `docs`, `governance`, `EXTENSIONS`, `ECOSYSTEM`, and targeted `CVF_SESSION` pointers. Exact search command and source/tests/docs/JSON coverage are in the paired baseline; the same query was executed before the original held packet was authored and reconfirmed on 2026-09-18. Same-token collision disposition: rejected T2B receipt/status declarations and adjacent HMAC/token mechanisms do not constitute a G1 trust registry or genuine lookup owner. The three worker-output paths did not exist at Local release audit. This is a bounded negative owner search, not complete-corpus absence proof.

Checker-token collision ledger (each occurrence is non-authoritative for G1):

- Same-token collision `CVF_LIVE_EVIDENCE_MANIFEST_AND_RERUN_STANDARD_2026`: separate HMAC manifest standard.
- Same-token collision `CVF_v1`: older Web extension prefix with separate service-token purpose.
- Same-token collision `NOT_GRANTED`: held dispatch disposition, not a registry lookup result.
- Same-token collision `OWNER_CLAIM`: Source Verification claim class, not a key-owner implementation.
- Same-token collision `ADJACENT_PATTERN`: Source Verification classification used elsewhere, not a G1 key or lookup owner.
- Same-token collision `RV`: predecessor review identifier fragment, not a verifier role.
- Same-token collision `dispatchBaseHead`: work-order lifecycle field, not a current executable base.

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

dispatchKind: INITIAL
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: ACEL-G1-T2C-VERIFIER-TRUST-ANCHOR-CONTRACT-DESIGN
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

This initial dispatch is limited to hypothetical documentation. It does not release missing operational dependencies.

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t2c-verifier-trust-anchor-contract-design","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["g1_verifier_key_owner_not_source_verified","g1_issuer_lookup_provenance_not_source_verified"],"reopened":[],"current":["g1_verifier_key_owner_not_source_verified","g1_issuer_lookup_provenance_not_source_verified"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"ROOT_CONTRACT_REQUIRED","successorScope":"INTEGRATED_ROOT_CONTRACT"}
```

This is a separate initial design problem, not a successor that resolves T2B's stopped chain. No operational blocker is resolved by this hypothetical documentation packet.

providerExecutionAuthority: FORBIDDEN

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"ACEL-G1-T2C-VERIFIER-TRUST-ANCHOR-CONTRACT-DESIGN","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"DOC_CHANGE","authorityImpact":"USES_EXISTING_OWNER","externalEffect":"NONE","dataSensitivity":"PRIVATE_REPO","reversibility":"GIT_REVERSIBLE","sourceScale":"BOUNDED_CLUSTER","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["docs/audits/","docs/reviews/","docs/baselines/","docs/work_orders/","docs/reference/agent_system_skills/","EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/","governance/compat/"],"claims":["hypothetical G1 T2C contract design only; no existing key or lookup owner"],"requiredProof":["thirteen-path frozen hash reconciliation","three-output path isolation","human/JSON parity","non-operational canonicalization vectors","adversarial negative matrix","worker-return fast gate","Local review"],"operatorCheckpoints":["operational key","genuine lookup","G1 implementation","real calibration","provider/live","runtime","public sync","deployment"],"forbiddenEffects":["edit parked evidence","downstream provider call","network lookup","credential access","configuration mutation","worker commit","nested subagent","automatic successor"],"sourceEvidence":{"selectedFilesFullyRead":true,"corpusReceiptRef":"docs/reviews/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_LOCAL_ARCHITECTURE_DECISION_2026-09-17.md","completenessClaimChanged":false}}
```

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | exact three documentation outputs in Required Artifact Manifest | one shared-workspace worker, no commit, keys, lookup or implementation; Local independently reviews | operator 2026-09-18 instruction, paired baseline, Local design decision | N/A with reason: internal document-only work has no external adapter | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no selected external adapter owner | no remote execution, ingress, credentials, mutation or public claim | external/local coordination method and this explicit exclusion | `DEFERRED_WITH_REASON`: adapter is outside this G1 design packet | `DEFERRED_WITH_REASON` |

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline and work order | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired baseline and work order | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V62_2026-09-17.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | exact three outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| source_reconciliation | WORKER_RETURN | worker | IMPLEMENTATION | exact three outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| frozen_input_integrity | WORKER_RETURN | worker | IMPLEMENTATION | read-only thirteen-path ledger | NO_MUTATION | closer | MATERIAL_COMMIT | source_reconciliation |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact three outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | frozen_input_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact three outputs | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker-return ADIF disclosure | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | worker outputs and optional completion review | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | adif_integrity |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material | BOUNDED_PATH_FAMILY | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | Local completion disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | authorized continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Worker Autonomy / No-Question Rule

The worker may repair only the three documentation outputs without routine operator questions. Return on contradictory source authority, frozen drift, failing gate outside write scope or any forbidden expansion. Do not ask Local to re-create in-scope design work.

## Agent Handoff Contract Control Block

| Field | Held disposition |
|---|---|
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one internal design worker; independent Local reviewer |
| phase | dispatch -> hypothetical design -> Local review -> optional continuity |
| baseHeadFor(phase) | dispatchBaseHead=`17b3cb0fbc11e8b97b42223b57f0f98f5f2e1273`; executionBaseHead=worker captures |
| closureBaseHead | unset; Local reviewer must set only after an authorized worker return |
| changedSetScope(phase) | exact three worker outputs only |
| traceScope(phase, actor) | worker captures start/end HEAD/status, source and frozen hashes; Local captures review evidence |
| commitOwner(phase) | Local only |
| crossBatchIsolation | 13 G1 paths frozen; unrelated worktree paths not acquired |
| nextMoveSurfaces | Local updates active handoff/state after disposition; operator release is documentation-only |

Handoff contract authority: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

Before status evidence: tracked worktree clean at dispatch base `17b3cb0fb`; thirteen named frozen untracked paths were present, all thirteen hashes matched, staging empty, and the three future worker paths were absent.

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: INTERNAL_AGENT design worker after dispatch

laneOwnedPaths: exact three Required Artifact Manifest paths

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: worker return, empty staging, exact worker delta and byte-identical thirteen-path hash reconciliation

## Foundation Storage Layout Block

N/A with reason: this work order creates no foundation file and authorizes no split, move, or rename under `docs/reference/`. The three worker outputs are limited to `docs/audits/` and `docs/reviews/`; the paired baseline and work order remain in their existing governed families.

## Reviewer Closure Conversion

| Field | Held disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_COMPLETION_2026-09-17.md` only if reviewer acceptance requires it |
| reviewerOwnedClosurePaths | worker outputs, completion disposition and separate continuity after review |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_WORKER_RETURN_2026-09-17.md`

contractProfile: `WORKER_RETURN_FULL_GATE_V1`

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

Required sections: Purpose; Scope / Methodology; Findings / Position; source and thirteen-path frozen hash reconciliation; human/JSON parity; adversarial self-check; Risk / Corrective Action; Semantic Convergence Outcome; Return-Time Closeability Recheck; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; Epistemic Process Block; Claim Boundary; command evidence; `git status --short`; no-commit/no-subagent statement. Conditional non-applicable sections must state N/A with reason.

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
python governance/compat/run_worker_return_fast_gate.py
python -m json.tool docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_MANIFEST_2026-09-17.json
git diff --check
git status --short
git diff --cached --name-only
```

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`DOC_CHANGE`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`. `python governance/compat/run_adif_defect_resolver.py --task-class DOC_CHANGE --role dispatcher --lifecycle-phase pre-dispatch` returned zero candidates and `NONE_RETURNED` on initial authoring. Local reruns before dispatch.

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_range.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | held status, dispatch-envelope applicability, source disposition, negative-search evidence, closeability applicability and no-commit ownership |
| gateRunPurpose | confirm held packet shape, not release missing authority |
| claimBoundary | no checker pass creates a trusted key or lookup owner |

## Verification And Release Gate

The operator has authorized a hypothetical-only design without existing-owner claims. Local must pin actual forbidden filesystem state, reconcile frozen hashes and run the pre-dispatch autorun gate. A passing gate releases only the three documentation outputs. Any implementation, operational key, genuine lookup or candidate admission remains parked.

## Evidence Requirements

The worker return requires exact source paths/locators, negative-search collisions, 13-path unchanged hashes, output topology, `executionBaseHead`, actual `git status --short`, human/JSON parity, published canonical preimage/signature vectors using non-operational test material, full negative matrix and secret-safe command evidence. No actual verifier receipt or lookup claim may be fabricated.

## Acceptance Criteria

- [ ] Missing owner and lookup provenance are resolved by independently verifiable source evidence or the packet stays explicitly hypothetical and fail-closed.
- [ ] Human/JSON design outputs agree on every signed field, trust-source, key-lifecycle and admission predicate.
- [ ] Forged content-hash receipt, receipt-supplied key and signed false-lookup vectors all fail candidate admission.
- [ ] Both TypeScript and Python verification responsibilities are specified without claiming either is implemented.
- [ ] All 13 frozen evidence hashes match and no forbidden path changes.

These are future design-review criteria, not a current completion checklist.

## Review Gate

The worker must run `python governance/compat/run_worker_return_fast_gate.py`; Local independently evaluates returned evidence without recreating the design, then applies reviewer-fast and pre-commit. Passing these gates checks declared structure only; genuine lookup remains unestablished and needs separate source-owned observation evidence.

## Closure Checklist

- [x] Local architecture direction and T2B rejection are source-linked.
- [x] Missing key/lookup owner remains an operational hold; hypothetical design alone is released.
- [x] Thirteen parked paths are excluded from write ownership.
- [x] Operator released hypothetical documentation only; operational dependencies remain absent.
- [ ] Worker return, independent review and committed-range closure.

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` for contradictory source owner, frozen-path drift, required operational key/live/implementation work or an unrepairable gate. Missing existing owner or lookup provenance is an expected premise of the hypothetical design, not a worker failure; never turn it into a positive candidate-admission claim. Return `COMPLETE_PENDING_REVIEW` only for the exact documentation outputs with evidence and no worker commit.

## Operator Checkpoint

The operator's 2026-09-18 audit-and-dispatch instruction releases hypothetical design only. Before any key creation, signer wiring, genuine registry lookup or implementation, a separate operator-governed authority is mandatory. Local confirms this packet is not evidence of an existing CVF owner.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/dispatch author |
| Provider or surface | private CVF workspace; official RFC Editor read-only references |
| Session or invocation | G1 T2C held packet authoring, 2026-09-17 |
| Working directory | repository root |
| Command or tool surface | current continuity/source reads, targeted `rg`, scaffold stdout, apply_patch, gates |
| Target paths | paired held baseline and work order only |
| Allowed scope source | V62 next allowed move: Local documentation-only GC-018/work-order authoring |
| Before status evidence | tracked clean worktree at dispatchBaseHead `17b3cb0fb`; 13 frozen untracked evidence paths; staging empty; three worker output paths absent |
| After status evidence | paired dispatch amendment paths only, no worker output created |
| Diff evidence | exact paired-document changed set |
| Approval boundary | operator-authorized hypothetical design dispatch, subject to pre-dispatch gate |
| Claim boundary | no key, lookup, implementation, provider/live, runtime, public or deployment |
| Agent type | Local dispatch author |
| Invocation ID | `acel-g1-t2c-held-contract-packet-authoring-20260917` |
| Expected manifest | paired held baseline and work order |
| Actual changed set | paired held baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | hypothetical dispatch documentation only |
| claimDisposition | CLAIM_REJECTED: no implemented execution-control or issuer-verification capability claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime/provider receipt created |
| actionEvidence | ACTION_EVIDENCE_PRESENT: Local source audit and bounded dispatch authoring only |
| invocationBoundary | one internal documentation worker only after pre-dispatch admission |
| interceptionBoundary | no OS/IDE/provider/CLI/MCP interception claim |
| claimLanguage | proposed trust-anchor contract only, with no existing owner assertion |
| forbiddenExpansion | keys, lookup, G1 implementation, live, runtime, public sync and deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private held authoring packet; no public-sync authority.

## Claim Boundary

This packet authorizes exactly one internal hypothetical-documentation worker dispatch after passing pre-dispatch admission. It grants no G1 implementation, issuer authority, key creation/use, live registry lookup, downstream provider call, public export or deployment. T2B and the thirteen parked paths remain unaccepted evidence.
