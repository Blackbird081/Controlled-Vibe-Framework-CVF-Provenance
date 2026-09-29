# CVF SOT3-T2 Completion Review

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_BOUNDED

docType: completion_review

Date: 2026-07-12

Review ID: SOT3-T2-COMPLETION-REVIEW

## Purpose

Review the SOT3-T2 canonical inter-layer documentation contracts against the
accepted T0R architecture, the accepted T1 owner reconciliation, and the T2
work order. This review does not authorize implementation.

## Target / Source

Targets are the five worker-owned T2 outputs. Authority is the accepted T0R
and T1 review chain, the T2 work order, and the source evidence cited by the
worker's contract-source reconciliation.

## Scope / Target / Owner Boundary

The worker owns bounded repair of the same five output paths. The reviewer owns
this completion review and final acceptance. No runtime, schema, test, guard,
checker, public-sync, or session-state implementation is authorized.

## Scope / Methodology

The reviewer inspected all eight contracts, all ten invariants, all fourteen
negative cases, the compatibility ledger, and the worker return; compared key
tokens and producer boundaries with T0R/T1; and ran the worker-return fast
gate.

## Gate Result

- Worker base HEAD remains `8e318cc92`.
- Worker changed set contains exactly the five planned outputs.
- Worker-return fast gate: PASS.
- Published hash test vector independently recomputed: 522 UTF-8 bytes and
  SHA-256 `bc32424380bd483ca208edd8ee18bcaaa874b109584341e8febc01b5e46ab5a3`.
- Semantic reviewer disposition: REVIEWER_ACCEPTED_BOUNDED.

Machine conformance is necessary but does not establish semantic contract
correctness.

## Findings / Position

### R1 - Compatibility count is internally false

Severity: HIGH.

The reconciliation table lists six contract names under primary `ADAPT` but
reports a count of five. The explanatory note does not make six contract-level
primary dispositions equal five. The worker return repeats the same mismatch.

Required repair: report six primary `ADAPT` contracts and reconcile every
derived count and narrative. Keep shape-level `REJECT_DIRECT_IMPORT`
sub-decisions separate from the eight contract-level primary dispositions.

### R2 - Refinery lifecycle status is conflated with failure tokens

Severity: HIGH.

`RefineryPacket.status` currently includes `REFINERY_NO_STAGES_EXECUTED` and
`REFINERY_FAILED`, while the same contract separately defines
`failure_tokens`. T0R retained `READY_FOR_KERNEL`, `REVIEW_REQUIRED`, and
`BLOCKED` as the boundary statuses. The current form makes an error token serve
two incompatible roles.

Required repair: use lifecycle statuses such as `IN_PROGRESS`,
`READY_FOR_KERNEL`, `REVIEW_REQUIRED`, and `BLOCKED`. Keep
`REFINERY_NO_STAGES_EXECUTED` and other error codes in `failure_tokens`. Zero
executed stages must yield `BLOCKED`, include the explicit failure token, and
never reach Kernel. Update NC-01 and every derived statement consistently.

### R3 - Verification-result ownership and transport are undefined

Severity: HIGH.

`KernelDecision` forbids acceptance when `verification_results` referenced by
the request are empty, but `KernelEvaluationRequest` defines no such field or
reference. `TruthReceipt` then requires verification results without defining
whether Kernel creates them, resolves them, or receives them.

Required repair: define one unambiguous documentation-only ownership and
transport model. If Kernel produces verification results during evaluation,
say so and bind their identifiers/hash into `KernelDecision` and
`TruthReceipt`; do not claim they were referenced by the request. If the
request carries references, add and define that field consistently. Preserve
fail-closed behavior for empty required evidence and empty required
verification results.

### R4 - A rejected receipt can currently mint a TruthReference

Severity: CRITICAL.

The chain allows a `TruthReceipt` to record multiple decision outcomes, but
`TruthReference` issuance requires only an `ISSUED`, non-revoked receipt. That
permits a receipt recording `REJECT`, `ESCALATE`, or
`REQUIRE_ADDITIONAL_EVIDENCE` to satisfy the written issuance precondition.

Required repair: state that receipts may record every Kernel outcome, while a
`TruthReference` may be issued only from a receipt bound to the explicit
eligible acceptance outcome, with all mandatory obligations satisfied and no
blocking verification failure. Add a negative case or extend an existing case
to prove that non-acceptance receipts cannot mint a reference.

### R5 - TruthReference state fields have no implementable vocabulary

Severity: HIGH.

The contract requires both `supersession_state` and `revocation_state` but
assigns the composite vocabulary `ACTIVE`, `SUPERSEDED`, `REVOKED`, `EXPIRED`
to both fields. It does not define legal values per field or whether expiry is
stored or derived.

Required repair: choose one explicit state model. Either use one lifecycle
state field with exact transitions, or retain separate fields with exact
per-field vocabularies and precedence rules. Define expiry as stored or
derived, and update NC-09/NC-10 plus DistributionPackage eligibility.

### R6 - Generic ACCEPT weakens the bounded truth claim

Severity: HIGH.

T0R source evidence names `ACCEPT_EVIDENCE_CANDIDATE`. Renaming it to generic
`ACCEPT` removes the boundary that Kernel accepts an evidence-backed candidate,
not universal or final truth. "Chain-wide consistency" is not sufficient
source justification for this semantic broadening.

Required repair: retain `ACCEPT_EVIDENCE_CANDIDATE` across the contract chain,
invariants, and negative cases, or provide a source-backed narrower token with
equivalent bounded semantics. Do not use unqualified `ACCEPT` as a truth claim.

Repair verification: SATISFIED. The bounded repair restores
`ACCEPT_EVIDENCE_CANDIDATE` consistently.

### R7 - Receipt hash does not bind the evidence decision basis

Severity: CRITICAL.

The repaired `TruthReceipt` carries `evidence_refs`, `obligation_refs`, and
`verification_result_refs`, but its `receipt_hash` rule binds only evaluated
content hash, decision, versions, and predecessor hash. An actor could
therefore substitute the evidence, obligation, or verification-result bindings
without violating the documented receipt hash. That contradicts the work
order's receipt minimum and the contract's own claim that the receipt is a
tamper-evident record of the decision context.

Required repair: define the canonical receipt-hash payload to include all
authority-bearing receipt fields, including `decision_id`, `decision`,
`evaluated_content_hash`, `evidence_refs`, `obligation_refs`,
`verification_result_refs`, policy/rule versions, decision/issuance times,
and predecessor hash. State deterministic serialization/order handling for
collections at documentation-contract level. Update Invariant 5, NC-05, and
all summaries consistently.

### R8 - Reference eligibility cites an unresolved failed_obligations field

Severity: HIGH.

`failed_obligations` belongs to `KernelDecision`, not the defined
`TruthReceipt` field minimum. The Eligible-Acceptance-Only Issuance Rule says
none may be present but does not say whether the receipt copies that field or
how `decision_id` resolves the authoritative decision. The issuance rule is
therefore not self-contained.

Required repair: choose one explicit model. Either add `failed_obligations` to
`TruthReceipt` and bind it into `receipt_hash`, or require Kernel to resolve
the immutable `KernelDecision` identified by `decision_id` and verify its
`failed_obligations` before issuance. If using resolution, state that the
receipt's decision and result bindings must exactly match the resolved
decision, and make mismatch fail closed. Update the reference issuance rule,
Invariant 5/6, and a negative case accordingly.

### R9 - Decision-resolution comparison targets fields KernelDecision does not define

Severity: CRITICAL.

Round 2 says `TruthReceipt.evidence_refs` and `obligation_refs` must exactly
match the resolved `KernelDecision`'s corresponding bindings. The defined
`KernelDecision` minimum contains neither `evidence_refs` nor
`obligation_refs`; it contains only `request_id`, `packet_hash`,
`failed_obligations`, and `verification_result_refs` among the relevant
fields. Therefore the stated comparison cannot be executed from the contract.

Required repair: choose and document one complete authority path. Either add
`evidence_refs` and `obligation_refs` to `KernelDecision`, or resolve the
immutable `KernelEvaluationRequest` through `KernelDecision.request_id` and
compare the receipt bindings to that request while comparing
`verification_result_refs`, decision, and failed obligations to the decision.
Every missing record, broken link, or mismatch must fail closed. Update NC-04B
and all R8 summaries so they name only fields actually defined on each record.

### R10 - Receipt serialization is ordered but not canonical

Severity: CRITICAL.

Round 2 fixes field coverage and collection order, but permits a future
implementation to choose canonical JSON, length-prefixed concatenation, or a
tagged structure. Those encodings produce different byte sequences and hashes
for the same receipt. Plain concatenation also has boundary ambiguity unless
field tags, lengths, escaping, null representation, timestamp normalization,
and hash algorithm/version are fixed. An independent verifier cannot reproduce
one canonical `receipt_hash` from the current text.

Required repair: define exactly one versioned canonical preimage contract at
documentation level. It must fix field tags/order, UTF-8 or other exact text
encoding, scalar normalization, UTC timestamp form, null/empty distinction,
collection ordering, element boundaries, and the digest algorithm identifier.
The contract may define a version such as `receipt_hash_profile`; it must not
allow each implementation to choose a different encoding. Update Invariant 5,
NC-05, and all R7 summaries consistently. This remains documentation-only and
does not authorize runtime implementation.

### R11 - Canonical preimage omits receipt identity and leaves JSON string bytes ambiguous

Severity: CRITICAL.

Round 3 defines one profile but omits `receipt_id` from the preimage even
though it is the receipt's required identity and an authority-bearing field.
The profile also says "standard JSON escaping", which permits multiple valid
JSON spellings for the same string, such as a literal Unicode character versus
an escaped form. Therefore the claim that any two independent verifiers must
produce the same digest is still stronger than the specification.

Required repair: include `receipt_id` in the fixed preimage. Replace generic
"standard JSON escaping" with one named canonical JSON algorithm or an equally
exact escaping and Unicode-normalization rule. If using a named standard, cite
its exact canonicalization behavior and make the local fixed-field/profile
rules non-contradictory with it. Add one complete illustrative canonical
preimage example and expected SHA-256 digest so the profile is testable by a
future implementation tranche. Update Invariant 5, NC-05, and summaries.

### R12 - Receipt content and version bindings are not checked against the resolved chain

Severity: CRITICAL.

Round 3 checks decision/request identity and evidence/result bindings, but it
does not require `TruthReceipt.evaluated_content_hash` to equal the resolved
decision/request packet hash. It also does not compare the receipt's
`policy_version` and `rule_version` with the resolved decision and request.
Consequently a self-consistent receipt hash could still attest a different
content hash or policy/rule version than the evaluation chain it cites.

Required repair: extend the Decision-Resolution Model and issuance rule so
`TruthReceipt.evaluated_content_hash`, `KernelDecision.packet_hash`, and
`KernelEvaluationRequest.packet_hash` match exactly; and so receipt,
decision, and request policy/rule versions match exactly. Missing or mismatched
values fail closed. Update NC-04B or NC-07, Invariants 5/6, README,
reconciliation, and worker return consistently.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| arithmetic reconciliation cannot be audited | correct primary disposition counts |
| failure code is mistaken for lifecycle state | separate status from `failure_tokens` |
| verification evidence appears from an undefined boundary | define result ownership and binding |
| non-acceptance decision gains distribution authority | bind reference issuance to eligible accepted receipt |
| reference validity cannot be evaluated deterministically | define exact state vocabularies and precedence |
| candidate acceptance is overread as canonical truth | restore bounded acceptance semantics |
| receipt bindings can be substituted without hash failure | bind all authority-bearing receipt fields with deterministic serialization |
| reference issuance checks a field with no defined owner path | define copy-or-resolve handling for `failed_obligations` |
| receipt-to-decision comparison names nonexistent decision fields | define a complete request/decision/receipt authority path |
| valid implementations compute different receipt hashes | define one versioned canonical preimage and digest profile |
| receipt identity can be substituted without digest failure | bind `receipt_id` and provide a reproducible hash vector |
| receipt cites different content or policy than its resolved evaluation | compare content hash and versions across receipt, decision, and request |

## Disposition

`REVIEWER_ACCEPTED_BOUNDED`.

R1 through R12 are satisfied. The final review confirms:

- six `ADAPT` and two `NEW_DOC_ONLY` primary contract dispositions;
- Refinery lifecycle status is separate from failure tokens;
- Kernel owns verification-result production;
- only an eligible `ACCEPT_EVIDENCE_CANDIDATE` receipt may back a reference;
- the reference lifecycle has one deterministic state model;
- receipt identity and every authority-bearing field are bound by one
  versioned RFC 8785 JCS/SHA-256 profile with a reproducible test vector;
- receipt, decision, and request resolve through defined fields and require
  exact content, policy, rule, evidence, obligation, result, and decision
  consistency with empty failed obligations;
- all empty, mismatch, replay, expiry, revocation, unauthorized-producer, and
  direct-mutation cases fail closed.

T2 is accepted as a documentation-contract foundation. Runtime implementation
and later SOT3 tranches require their own authorization.

## Review Cost Telemetry And Stop Disposition

| Signal | Result |
|---|---|
| `reviewRoundCount` | 5 reviewer dispositions including final acceptance |
| `workerRepairTurnCount` | 4 bounded-repair worker turns |
| `newRootCauseCountThisRound` | 0; round 4 closed R11-R12 |
| `dependentFindingCountThisRound` | 0 new findings in final review |
| `elapsedReviewMinutes` | `NOT_AVAILABLE_WITH_REASON`: no canonical cross-agent wall-clock receipt was captured for the full sequence |
| `providerCallCount` | 0 live/provider calls; documentation review used local tools only |
| `tokenOrQuotaUsage` | `NOT_AVAILABLE_WITH_REASON`: provider-neutral exact token usage is not exposed in the governed workspace |
| `valueDelta` | R11-R12 closed receipt identity/canonicalization and cross-record content/version integrity; final acceptance reached |
| Stop disposition | `REVIEW_COST_ESCALATION_REQUIRED` acknowledged retrospectively; no further micro-repair branches opened; T2 closes and future work moves to a fresh tranche |

## Reverse Architecture Projection

| Absorbed capability or gap | Existing catalog/GAP owner checked | Projection disposition | Target source path | Claim class | Evidence |
|---|---|---|---|---|---|
| SOT three-layer contract architecture | no accepted as-built SOT three-layer entry | DEFER_PENDING_ACCEPTANCE resolved by this review; next tranche must add bounded catalog projection | `docs/reference/system_architecture_catalog/entries/` | CONTRACT_ONLY | this review and three accepted reference outputs |
| independent CVF Refinery | OWNER_SURFACE_NOT_FOUND | ADD_GAP_ENTRY in a separately authorized reverse-projection tranche | `docs/reference/system_chain/gaps/entries/` | OWNER_CANDIDATE | T0R/T1 and contract-chain Refinery boundary |
| Truth Kernel runtime | truth-foundation doctrine owner exists; runtime owner not implemented | ADD_GAP_ENTRY in a separately authorized reverse-projection tranche | `docs/reference/system_chain/gaps/entries/` | RUNTIME_CANDIDATE | T1 CAP-05 disposition |
| post-Kernel Truth Flow | OWNER_SURFACE_NOT_FOUND | ADD_GAP_ENTRY in a separately authorized reverse-projection tranche | `docs/reference/system_chain/gaps/entries/` | OWNER_CANDIDATE | T0R/T1 and contract-chain Flow boundary |
| retained competing packet/boolean/direct-mutation shapes | no canonical owner import allowed | ADD_CATALOG_ENTRY or bounded exclusion projection in the next tranche | `docs/reference/system_architecture_catalog/entries/` | REJECTED_COMPETING_SHAPE | source reconciliation `REJECT_DIRECT_IMPORT` rows |

No Catalog/GAP aggregate is edited in T2. Reverse projection is explicitly
routed to the fresh tranche requested by the operator, where generated-source
discipline and exact owner paths can be handled without widening T2 closure.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: the eight-contract chain would preserve T0R's
bounded candidate semantics and make every cross-layer authority transition
deterministic.

Evidence Comparison Requirement: contract fields, status vocabularies,
producer/consumer ownership, compatibility counts, invariants, and negative
cases were compared against the accepted T0R/T1 packets.

Contradiction Or Gap Disposition: R1-R12 are repaired and independently
re-reviewed; no critical contract contradiction remains.

Claim Update Requirement: T2 is accepted as bounded documentation-contract
evidence; implementation and as-built runtime claims remain unauthorized.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | REVIEWER_ACCEPTED_BOUNDED; COMPLETE_PENDING_REVIEW; ADAPT; REJECT_DIRECT_IMPORT; NOT_AUTHORIZED; Public Export Disposition |
| gateRunPurpose | confirm reviewer-return shape after independent semantic review |
| claimBoundary | machine conformance does not decide semantic contract correctness |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | CVF reviewer/closer |
| Provider or surface | local private provenance workspace |
| Session or invocation | SOT3-T2 final completion and bounded-repair review, 2026-07-12 |
| Working directory | repository root |
| Command or tool surface | source reads, token searches, worker-return fast gate, apply_patch |
| Target paths | five worker outputs and this completion review |
| Allowed scope source | SOT3-T2 Reviewer Closure Conversion |
| Before status evidence | HEAD `8e318cc92`; exactly five untracked worker outputs |
| After status evidence | R1-R12 accepted; implementation remains unauthorized |
| Diff evidence | git status lists five worker outputs plus reviewer-owned completion review |
| Approval boundary | documentation-contract acceptance only |
| Claim boundary | no implementation, runtime, provider/live, public, release, or readiness claim |
| Agent type | reviewer/closer |
| Invocation ID | `sot3-t2-initial-review-2026-07-12` |
| Expected manifest | three reference outputs; source reconciliation; worker return; completion review |
| Actual changed set | three reference outputs; source reconciliation; worker return; completion review |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Implementation Boundary

Implementation, T3, runtime/schema/test/guard work, provider/live proof, and
public-sync remain `NOT_AUTHORIZED`.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private retained-source reconciliation and internal contract evidence.

## Claim Boundary

This review accepts T2 as a bounded documentation-contract foundation. It makes
no runtime, canonical-truth, release, readiness, or public claim and does not
authorize T3 or implementation.
