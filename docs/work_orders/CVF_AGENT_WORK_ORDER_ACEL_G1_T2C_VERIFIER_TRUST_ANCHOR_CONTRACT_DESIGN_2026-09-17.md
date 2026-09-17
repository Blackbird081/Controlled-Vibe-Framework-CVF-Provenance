# CVF Agent Work Order - ACEL G1 T2C Verifier Trust-Anchor Contract Design

Memory class: governed-worker-dispatch

docType: work_order

Status: HOLD_SOURCE_NOT_FOUND

Date: 2026-09-17

Batch ID: ACEL-G1-T2C-VERIFIER-TRUST-ANCHOR-CONTRACT-DESIGN

dispatchBaseHead: NOT_SET_WHILE_HELD

Authoring base head: `3796ff4ce85b2343b857be7da5bc69cb9447266f`

Commit mode if later released: `WORKER_MUST_NOT_COMMIT`

Worker role if later released: one shared-workspace `INTERNAL_AGENT`

Reviewer/closer: Local orchestrator/reviewer

## Dispatch Prompt Envelope

N/A with reason: this packet is `HOLD_SOURCE_NOT_FOUND`, not dispatch-ready. No worker invocation, executionBaseHead or live action is authorized. A future Local amendment must set a real dispatchBaseHead, complete the envelope and rerun pre-dispatch gates before dispatch.

## Purpose

Hold a bounded documentation-only worker contract for verifier-authenticated issuer receipts. The Local architecture decision selects Ed25519 but has not verified a CVF owner for the trusted public-key registry or genuine issuer-registry lookup. This work order cannot be dispatched while those source claims remain blocked.

## Authority Chain And Dependency Release Evidence

Operator authorized handling the prior gate; Local selected a design direction at `1c5c01675`; active V62 continuity permits Local GC-018/work-order authoring only. The paired baseline is `docs/baselines/CVF_GC018_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md`. T2B review `4bb04c836` remains terminally parked. No operator, Local or worker statement in this chain grants keys, live lookup, implementation or automatic dispatch.

| Dependency | Evidence | Release condition | Current disposition |
|---|---|---|---|
| Separate-tranche architecture selection | `docs/reviews/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_LOCAL_ARCHITECTURE_DECISION_2026-09-17.md` | Selected topology only | SATISFIED_FOR_AUTHORING |
| Trusted G1 verifier public-key registry owner | Paired baseline Source Verification Block and targeted search | Source path, owner, independent trust-root provision, authorized writers, key lifecycle, revocation and historical verification semantics verified by Local | BLOCKED_SOURCE_NOT_FOUND |
| Genuine lookup provenance owner | T2B-RV-F1 counterexample and paired baseline search | Source-owned registry/snapshot identity, lookup result and provenance interface verified by Local; signature alone cannot satisfy | BLOCKED_SOURCE_NOT_FOUND |
| Dispatch authority | V62 next move says authoring only | Separate Local release decision, fresh base/status/forbidden-state evidence and pre-dispatch gates | NOT_GRANTED |

## Intake Role Routing Decision

| Field | Decision |
|---|---|
| intake summary | prospective documentation-only G1 trust-anchor contract |
| scope classification | held design packet with missing owner sources |
| risk sensitivity | high: authentication and issuer admission; no key handling now |
| selected route mode | `SINGLE_AGENT_MULTI_ROLE` only if later released: one worker designs and self-checks; Local independently reviews/closes |
| role separation basis | worker cannot commit or accept own contract; Local owns source admission and final disposition |
| escalation condition | source owner absent/contradictory, key or live action needed, or any T2B same-tranche repair |

## Roles, Write Ownership And Scope

Local is dispatch author, source-verification owner and independent reviewer. A later worker may write only the three planned outputs below after this hold is formally released. The worker must not edit or claim acceptance of the 13 parked G1 evidence paths. No nested delegation, provider call, network lookup, key generation/import, credential access, TypeScript/Python runtime implementation, checker/test mutation, configuration change, public sync or deployment is in scope.

## Required First Reads

While held, Local reads the active bootstrap/front door/handoff, paired baseline, Local T2C decision, T2B independent review, the work-order template, guard orientation and applicable checker sources. A future worker must repeat those reads against the then-current authority and source-verification rows before any writing.

## Pre-Flight Checks

Current pre-flight result: `HOLD_SOURCE_NOT_FOUND`; zero worker invocations and zero live calls. Future dispatch requires a clean bounded source/owner finding, fresh HEAD/status, exact three-output path absence, 13-path hash reconciliation, actual forbidden filesystem state, ADIF resolver refresh and pre-dispatch gate. A gate pass cannot substitute for an absent owner.

## Write Ownership

Current Local write ownership is this paired held baseline/work order only. The prospective worker write ownership is the exact three Planned Required Artifact Manifest paths, conditional on a later release. All existing G1 evidence, source, tests, checkers, continuity and secret stores are read-only.

## Proposed Design Requirements If Released

1. Specify a versioned, domain-separated deterministic UTF-8 JCS signing preimage with exact field types and ordering. Bind round, authority and issuer identity, authority-attestation hash, source-owned registry snapshot identity/hash, lookup result, observation/issuance times and unique receipt identity. Define the signature/key-ID envelope, duplicate-key-ID and key-alias rules. No receipt-supplied public key or candidate-supplied registry path may become trust authority.
2. Separate three predicates: canonical/content integrity; verifier signature under a CVF-trusted key with role/validity/revocation checks; and genuine lookup provenance from a source-owned registry observation. A passing signature without the third predicate remains `UNVERIFIED` and inadmissible.
3. Specify exact TypeScript decision-time and Python persisted-evidence verification ownership. Both must independently recompute the same preimage and fail closed on unknown/revoked/expired/ambiguous keys, malformed encodings, wrong domain/round/authority/snapshot, time ordering, stale/forked provenance and missing trust material.
4. Include positive and adversarial vectors: self-authored receipt with a correct SHA-256 but no signature; signature under receipt-supplied key; valid signature under revoked/wrong-role key; modified `keyId`/alias; true signature with fabricated or mismatched lookup; stale/forked snapshot; cross-round replay; invalid canonicalization; and unavailable trust registry. State expected `UNVERIFIED`/admission denial for each negative case.
5. Define key custody, rotation, revocation, historical validation and registry snapshot provenance only to the extent source-verified. If owner/source evidence cannot be established, mark the contract hypothetical and return `BLOCKED_SOURCE_NOT_FOUND`; do not manufacture a registry or sign test receipts with operational keys.
6. Reconcile the T2B human/JSON contract and all thirteen parked paths as rejected or deferred evidence, never as accepted implementation. No automatic G1 implementation successor is permitted.

## Execution Plan

N/A with reason: no execution is authorized in the present HOLD state. If released by a separate Local amendment, the worker sequence is source/frozen-hash capture, design of human and JSON contracts, self-consistency and adversarial-vector checks, worker-return evidence, then stop without commit for Local review. It never includes live lookup or key creation.

## Planned Required Artifact Manifest

| Path | Planned action only after release |
|---|---|
| `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` | human trust-anchor contract, owner ledger and adversarial matrix |
| `docs/audits/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_MANIFEST_2026-09-17.json` | matching machine-readable schema, predicates, source and vector ledger |
| `docs/reviews/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_WORKER_RETURN_2026-09-17.md` | no-commit source/gate/frozen-hash evidence and terminal return |

No planned output path is yet owned by a worker. All returned artifacts must remain uncommitted until independent Local review. A future release amendment must check these three paths are absent and record actual filesystem state of every forbidden path before dispatch.

## Parked Evidence Freeze

The ten exact paths and expected SHA-256 values in `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md` under Parked Evidence Freeze remain read-only. The three T2B outputs also remain read-only: human audit SHA-256 `5147bf905113e4c750f6b7f4aa84e1aeb4575417299258ad10dcf8ebbbb5575a`; JSON manifest SHA-256 `5bfe577495bac91b99344827172d859ff0389cf1f67e14097d5af113a16eaeb9`; worker return SHA-256 `25963195262048746436daee2ab4b2304fa96d54c8197ed375ab98e5e7dd29ce`. Local verified all 13 hashes match on 2026-09-17. A released worker must recheck before and after; any drift blocks the return.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified locator | Disposition |
|---|---|---|---|---|
| Local-selected Ed25519 direction | DESIGN_AUTHORITY | `docs/reviews/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_LOCAL_ARCHITECTURE_DECISION_2026-09-17.md` | Local Architecture Decision | ACCEPT |
| T2B public-hash receipt forgery | REJECTION_AUTHORITY | `docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_INDEPENDENT_REVIEW_2026-09-17.md` | T2B-RV-F1 | ACCEPT |
| Existing G1 verifier key and lookup owners | OWNER_CLAIM | `docs/baselines/CVF_GC018_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_2026-09-17.md` | Source Verification and Negative Search sections | BLOCKED_SOURCE_NOT_FOUND |
| HMAC live manifest and Web service token as G1 owner | ADJACENT_PATTERN | `docs/reference/CVF_LIVE_EVIDENCE_MANIFEST_AND_RERUN_STANDARD_2026-06-06.md`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | Signature Boundary; `computeServiceRequestSignature` | REJECT |

## Negative Search And Collision Discipline

Search roots: `docs`, `governance`, `EXTENSIONS`, `ECOSYSTEM`, and targeted `CVF_SESSION` pointers. Exact search command and source/tests/docs/JSON coverage are in the paired baseline; the same query was executed before this held work order was authored. Same-token collision disposition: rejected T2B receipt/status declarations and adjacent HMAC/token mechanisms do not constitute a G1 trust registry or genuine lookup owner. The three planned worker-output paths were not created in this authoring step. This is a bounded negative owner search, not complete-corpus absence proof.

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

These are initial-dispatch protocol fields only. `INITIAL_DISPATCH` does not override `HOLD_SOURCE_NOT_FOUND` or authorize invocation; dependency release and a later Local dispatch decision are still required.

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"acel-g1-t2c-verifier-trust-anchor-contract-design","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["g1_verifier_key_owner_not_source_verified","g1_issuer_lookup_provenance_not_source_verified"],"reopened":[],"current":["g1_verifier_key_owner_not_source_verified","g1_issuer_lookup_provenance_not_source_verified"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"ROOT_CONTRACT_REQUIRED","successorScope":"INTEGRATED_ROOT_CONTRACT"}
```

This is a held initial problem, not a successor that resolves T2B's stopped chain. No blocker is resolved by this documentation packet.

providerExecutionAuthority: FORBIDDEN

## Worker Autonomy / No-Question Rule

N/A with reason: there is no worker authority while held. If released, the worker may repair only the three planned documentation outputs, must return on missing source authority or any forbidden expansion, and must never ask Local to re-create its in-scope design work.

## Agent Handoff Contract Control Block

| Field | Held disposition |
|---|---|
| route | `SINGLE_AGENT_MULTI_ROLE` prospective, not activated |
| rolePattern | one internal design worker; independent Local reviewer |
| phase | authoring hold only; no execution phase opened |
| baseHeadFor(phase) | authoring base `3796ff4ce85b2343b857be7da5bc69cb9447266f`; dispatchBaseHead and executionBaseHead unset while held |
| closureBaseHead | unset; Local reviewer must set only after an authorized worker return |
| changedSetScope(phase) | paired baseline/work order only now; exact three planned outputs after a separate release |
| traceScope(phase, actor) | Local authoring evidence now; future worker must capture HEAD/status, source and frozen hashes |
| commitOwner(phase) | Local only |
| crossBatchIsolation | 13 G1 paths frozen; unrelated worktree paths not acquired |
| nextMoveSurfaces | V62 continuity remains authoring-only until Local release decision |

Handoff contract authority: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

## Foundation Storage Layout Block

N/A with reason: this held work order creates no foundation file and authorizes no split, move, or rename under `docs/reference/`. The three prospective worker outputs are limited to `docs/audits/` and `docs/reviews/`; the paired baseline and work order remain in their existing governed families.

## Reviewer Closure Conversion

| Field | Held disposition |
|---|---|
| completionReviewPath | `docs/reviews/CVF_ACEL_G1_T2C_VERIFIER_TRUST_ANCHOR_CONTRACT_DESIGN_COMPLETION_2026-09-17.md` only if later reviewer acceptance requires it |
| reviewerOwnedClosurePaths | future worker outputs, completion disposition and separate continuity after review |
| closureOwner | Local orchestrator/reviewer |
| workerCommitPermission | FORBIDDEN |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`DOC_CHANGE`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`. `python governance/compat/run_adif_defect_resolver.py --task-class DOC_CHANGE --role dispatcher --lifecycle-phase pre-dispatch` returned zero candidates and `NONE_RETURNED`. Rerun before any later dispatch.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_range.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | held status, dispatch-envelope applicability, source disposition, negative-search evidence, closeability applicability and no-commit ownership |
| gateRunPurpose | confirm held packet shape, not release missing authority |
| claimBoundary | no checker pass creates a trusted key or lookup owner |

## Verification And Release Gate

Current verification is Markdown/JSON/continuity and reviewer-fast only; no worker or live proof. Before release, Local must: (1) replace both `BLOCKED_SOURCE_NOT_FOUND` dependency rows with source-backed owners or explicitly authorize a hypothetical-only design without existing-owner claims; (2) pin a fresh dispatchBaseHead and actual forbidden filesystem state; (3) complete the dispatch prompt, SCEC, gate-to-role closeability, task-governance manifest and exact planned output proof; (4) run the pre-dispatch autorun gate. Until then terminal disposition is HOLD, not `DISPATCH_READY`.

## Evidence Requirements

The held packet requires exact source paths/locators, negative-search collisions, 13-path unchanged hashes, intended output topology and guard results. A released worker return would additionally require `executionBaseHead`, actual `git status --short`, human/JSON parity, published canonical preimage/signature vectors using non-operational test material, full negative matrix and secret-safe command evidence. No actual verifier receipt or lookup claim may be fabricated.

## Acceptance Criteria

- [ ] Missing owner and lookup provenance are resolved by independently verifiable source evidence or the packet stays explicitly hypothetical and fail-closed.
- [ ] Human/JSON design outputs agree on every signed field, trust-source, key-lifecycle and admission predicate.
- [ ] Forged content-hash receipt, receipt-supplied key and signed false-lookup vectors all fail candidate admission.
- [ ] Both TypeScript and Python verification responsibilities are specified without claiming either is implemented.
- [ ] All 13 frozen evidence hashes match and no forbidden path changes.

These are future design-review criteria, not a current completion checklist.

## Review Gate

Current gate is authoring-only reviewer-fast/pre-commit for a held packet. A future released worker must run `python governance/compat/run_worker_return_fast_gate.py`; Local independently evaluates returned evidence without recreating the implementation, then applies reviewer-fast and pre-commit. Passing these gates checks declared structure only; genuine lookup remains unestablished and needs separate source-owned observation evidence.

## Closure Checklist

- [x] Local architecture direction and T2B rejection are source-linked.
- [x] Missing key/lookup owner is recorded as a dispatch hold.
- [x] Thirteen parked paths are excluded from write ownership.
- [ ] Dispatch dependency release, worker return, independent review and committed-range closure: not attempted while held.

## Return-To-Orchestrator Conditions

No worker has been invoked. If later released, return `BLOCKED_WITH_REASON` for missing/contradictory source owner, unverifiable lookup provenance, frozen-path drift or any key/live/implementation request. Return `COMPLETE_PENDING_REVIEW` only for the exact documentation outputs with evidence and no worker commit.

## Operator Checkpoint

No operator key/secret or live-use choice is requested by this held packet. Before any key creation, signer wiring, genuine registry lookup or implementation, a separate operator-governed authority is mandatory. A hypothetical design-only release also requires an explicit Local scope decision that it is not evidence of an existing CVF owner.

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
| Before status evidence | HEAD `3796ff4ce`; 13 frozen untracked evidence paths; staging empty |
| After status evidence | two held authoring paths only, no worker output created |
| Diff evidence | exact paired-document changed set |
| Approval boundary | Local authoring, not worker invocation |
| Claim boundary | no key, lookup, implementation, provider/live, runtime, public or deployment |
| Agent type | Local dispatch author |
| Invocation ID | `acel-g1-t2c-held-contract-packet-authoring-20260917` |
| Expected manifest | paired held baseline and work order |
| Actual changed set | paired held baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private held authoring packet; no public-sync authority.

## Claim Boundary

This packet is not executable. It grants no worker dispatch, G1 implementation, issuer authority, key creation/use, live registry lookup, provider call, public export or deployment. T2B and the thirteen parked paths remain unaccepted evidence.
