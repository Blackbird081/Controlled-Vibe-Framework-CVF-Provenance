# CVF ACEL G1 T2B Calibration Root Contract Architecture Reassessment Independent Review

Status: REVIEW_REJECTED_PARKED

Terminal disposition: `PARKED_TRUST_ANCHOR_ARCHITECTURE_REQUIRED`

Memory class: FULL_RECORD

Date: 2026-09-17

Review base HEAD: `6d646b8f63ebcf3af8b93f39e00517799c8abf72`

Decision owner: Local orchestrator/reviewer

## Purpose

Independently disposition the G1 T2B three-output worker return after the
operator requested direct verification and parking of any unresolved authority
boundary for another tranche. This review is a terminal Local decision on T2B,
not acceptance of its proposed root contract.

## Target / Source

| Source | SHA-256 or authority |
|---|---|
| `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md` | `5147bf905113e4c750f6b7f4aa84e1aeb4575417299258ad10dcf8ebbbb5575a` |
| `docs/audits/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_MANIFEST_2026-09-17.json` | `5bfe577495bac91b99344827172d859ff0389cf1f67e14097d5af113a16eaeb9` |
| `docs/reviews/CVF_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_WORKER_RETURN_2026-09-17.md` | `25963195262048746436daee2ab4b2304fa96d54c8197ed375ab98e5e7dd29ce` |
| `docs/work_orders/CVF_AGENT_WORK_ORDER_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md` | governing work order; Local owns independent review and every commit |
| `docs/baselines/CVF_GC018_ACEL_G1_T2B_CALIBRATION_ROOT_CONTRACT_ARCHITECTURE_REASSESSMENT_2026-09-17.md` | four selected architecture decisions; no implementation authority |

## Scope / Methodology

Local reviewed the returned human/JSON/worker packet and focused on the
remaining authority-admission claim. The review consumed worker evidence
without recreating the three-output design or running provider/live proof.
The reviewer constructed one read-only adversarial `IssuerVerificationReceipt`
from the contract's exact fields and independently computed its profile hash.
No repository file was changed by that probe.

## Findings / Position

### T2B-RV-F1 - Receipt integrity is not verifier authentication - CRITICAL

The proposed `IssuerVerificationReceipt` contains a self-declared
`verifiedBy` role literal, a self-declared positive `lookupResult`, authority
and registry-snapshot hashes, a timestamp, and an ordinary SHA-256
`receiptHash`. Human contract lines 177-201 and the JSON
`issuerVerificationAdmissionRule` say recomputing this hash rejects a
fabricated receipt. It does not: any writer who can construct the fields can
compute a matching SHA-256. No signature, MAC, authenticated verifier-owned
registry retrieval, or trusted issuance ledger is part of the five admission
conditions. The separate verifier role is therefore a claim, not proven
provenance.

Read-only counterexample using the published authority vector's hash and
registry snapshot hash:

```text
receiptId=self-authored-demo
verifiedAuthorityHash=549530d9f5d97d6d3ea07f91f48e334fb31957c7756d2a16b4e1fad25af11456
verifiedBy=CALIBRATION_ROUND_DECISION_OWNER_VERIFIER
verifiedRegistrySnapshotHash=7777777777777777777777777777777777777777777777777777777777777777
verifiedAtUtc=2026-09-17T00:00:01Z
lookupResult=IDENTITY_CONFIRMED_DECISION_OWNER_ROLE
receiptHash=caf154924cba4740bd990695e9724f834d218ade8e5a40d316540d548149f6f0
all_five_declared_admission_checks=True
trusted_registry_lookup_performed=False
```

The digest was computed as SHA-256 over UTF-8 JCS for the exact
`IssuerVerificationReceipt` profile object; these ASCII-only fields make the
key-sorted compact JSON preimage unambiguous. This is an integrity-valid but
unauthenticated receipt. It falsifies the claim that hash recomputation alone
rejects fabrication. The Python checker responsibility table checks the same
contents and relations, not the origin of the receipt. Gate conformance does
not close this semantic gap.

## Accepted Returned Evidence

| Evidence | Disposition |
|---|---|
| Three T2B outputs exist, HEAD stayed `6d646b8f63e`, staging empty, and the ten previously parked paths remained hash-frozen | ACCEPT_AS_WORKER_SCOPE_EVIDENCE |
| Human/JSON corrections for schema-valid JCS vector, two-phase evidence placement, sticky invalidation, and snapshot reference in the acceptance fingerprint | ACCEPT_AS_DESIGN_DIRECTION_ONLY |
| Ordinary SHA-256 receipt content binding | ACCEPT_AS_INTEGRITY_ONLY |
| Claim that this receipt proves verifier issuance or a live registry lookup | REJECT_T2B_RV_F1 |
| Worker `COMPLETE_PENDING_REVIEW` and passing structural gates | ACCEPT_RETURN_FOR_REVIEW_NOT_CLOSURE |

## Acceptance Resolution And Deferred Boundary

T2B is not an accepted G1 calibration root contract. Do not run another
same-tranche repair or use these outputs as implementation authority. Preserve
the three untracked worker outputs and ten prior parked paths as evidence;
do not edit, stage, delete, or commit them as accepted material in this
closure. The operator selected a later tranche for the remaining trust-anchor
architecture. A future Local decision must bind verifier issuance to an
independently authenticated source, such as trusted verifier-owned receipt
retrieval or a signature/MAC with explicit trust anchor, key ownership,
revocation and verification rules. An ordinary content hash remains useful
for integrity but cannot establish issuer identity. No future tranche is
opened by this review.

G1 implementation/R3, G4 implementation/experiment, real calibration,
provider/live execution, configuration mutation, Core runtime, package
lifecycle, public sync and deployment remain parked.

## Review Cost Telemetry And Stop Disposition

| Field | Value |
|---|---|
| reviewRoundCount | 4 focused Local review turns for T2B |
| workerRepairTurnCount | 3 returned repair rounds after initial T2B return |
| newRootCauseCountThisRound | 0; same issuer-authentication defect persisted in a new receipt form |
| dependentFindingCountThisRound | 1; content hash mislabeled as fabrication protection |
| providerCallCount | 0 |
| tokenOrQuotaUsage | `NOT_AVAILABLE_WITH_REASON: provider-neutral usage telemetry is unavailable` |
| valueDelta | concrete fabricated-receipt counterexample prevents unsafe root-contract acceptance |
| stopDisposition | `PARKED_TRUST_ANCHOR_ARCHITECTURE_REQUIRED` |
| successorTrancheOpened | NO |

## Risk / Corrective Action

Accepting the current contract would allow a caller to self-author both the
claimed verifier outcome and its matching content hash. The bounded corrective
action is to reject its authority-admission claim and park the design until
an independently authenticated receipt source is selected in a separately
governed tranche. Do not weaken the other useful fail-closed design rules.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | review status and headings; Agent Operation Trace labels; Delta Execution eight-field block; review cost telemetry labels |
| gateRunPurpose | confirm review packet structure after the independent semantic counterexample, not discover the authority defect |
| claimBoundary | machine checks establish artifact conformance, not cryptographic authentication of a worker-proposed receipt |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace only |
| Session or invocation | G1 T2B independent return review, 2026-09-17 |
| Working directory | repository root |
| Command or tool surface | governed file reads, JSON inspection, SHA-256 counterexample, Git status and governance gates |
| Target paths | three T2B worker outputs read-only; this review authored; ten frozen inputs read-only |
| Allowed scope source | T2B work order reviewer ownership and operator instruction to verify then park for another tranche |
| Before status evidence | HEAD `6d646b8f63e`; thirteen untracked paths comprising ten parked plus three T2B outputs; staging empty |
| After status evidence | this independent review is the only Local material output; worker/frozen paths unchanged |
| Diff evidence | exact review path only; read-only counterexample above |
| Approval boundary | Local review decision and parking, not worker acceptance or new dispatch |
| Claim boundary | no implementation, provider/live, runtime, public-sync or deployment effect |
| Agent type | reviewer/closer |
| Invocation ID | `acel-g1-t2b-independent-review-20260917` |
| Expected manifest | this review path only |
| Actual changed set | this review path only |
| Manifest delta | MATCH |
| Deletion or rename disposition | none |

## Epistemic Process Block

- Expected Result / Prediction: a separately named verifier receipt plus a
  content hash should reject a self-authored positive lookup claim if its
  admission proof is genuinely authenticated.
- Evidence Comparison: an ordinary SHA-256 of self-authored fields satisfied
  all five declared receipt checks without any registry lookup or verifier
  participation.
- Contradiction or Gap Disposition: reject the receipt-authentication claim;
  retain content hashing as integrity evidence only and park issuer trust
  architecture for a separate Local decision.
- Claim Update: T2B supplies bounded design evidence, not an accepted root
  contract or implemented calibration owner.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | independent T2B review and terminal parking only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: review counterexample and stop disposition only |
| receiptEvidence | CVF_RECEIPT_PRESENT: worker artifacts and Local read-only digest counterexample consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: independent review artifact only |
| invocationBoundary | private repository and offline local computation; zero provider calls |
| interceptionBoundary | no runtime, CLI-worker, OS, provider or MCP interception claim |
| claimLanguage | returned design rejected as G1 root contract; trust-anchor architecture parked |
| forbiddenExpansion | same-tranche repair, implementation, G4, live calibration, runtime, public sync, deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private Local review; no public-sync authority.

## Claim Boundary

This review does not reject every useful T2B design idea, prove a model-quality
ranking, modify worker/frozen evidence, or open a successor. It records the
specific unclosed authentication boundary and the operator-selected park.
