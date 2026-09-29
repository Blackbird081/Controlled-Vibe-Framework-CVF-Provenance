# CVF SOT3-T2 Worker Return

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

docType: review_context

Date: 2026-07-12

Return ID: SOT3-T2-RETURN

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_T2_CANONICAL_INTER_LAYER_CONTRACTS_2026-07-12.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_T2_CANONICAL_INTER_LAYER_CONTRACTS_2026-07-12.md`

executionBaseHead: `8e318cc92`

## Purpose

Worker return for the SOT3-T2 canonical inter-layer contract authoring
tranche. Confirms exact scope executed, evidence coverage, gate results,
actual changed set, and no-commit state, per the paired work order's Worker
Return Packet Shape Contract.

## Target / Source

Accepted T0R architecture recommendation and T1 owner/value reconciliation
(material closure `520ffb4cc`), TKG-T1 upstream doctrine contract, the SOT3
roadmap and paired GC-018 baseline, and the three companion worker outputs
authored this tranche.

## Scope / Methodology

Executed exactly the work order's Execution Plan: captured a clean execution
base and verified the T0R/T1/continuity dependency commits
(`ae7d53385`, `520ffb4cc`, `cc64c8e07`); read current doctrine (TKG-T1) and
the accepted T0R Producer/Consumer Packet And Receipt Mapping table and
Capability Absorption Matrix; created the compact owner front door and
authority map; defined all eight canonical contracts with sole producer,
allowed consumers, field minimums, status vocabulary, valid/invalid
transitions, authority boundary, source provenance, and compatibility/
exclusion decision; mapped all ten baseline invariants to at least one
negative case and one contract field/status rule each; produced fourteen
negative cases (twelve originally required plus NC-04A added by the R4
repair and NC-04B added by the R8 repair) with source-backed evidence that
each failure mode is real, not hypothetical; produced field-level source
and collision reconciliation with an explicit `REJECT_DIRECT_IMPORT`/`ADAPT`/`NEW_DOC_ONLY`
decision for every contract and competing retained shape; repaired the
twelve findings (R1-R6 in round 1, R7-R8 in round 2, R9-R10 in round 3,
R11-R12 in round 4) from the SOT3-T2 completion review's bounded-repair
disposition; and produced exactly five outputs without staging or
committing.

## Findings / Position

All eight canonical contract types were defined with one sole producer each,
satisfying the no-duplicate-authority requirement. Three results are worth
highlighting for CVF review:

- Kernel is the exclusive producer of `KernelDecision`, `TruthReceipt`, and
  `TruthReference` across all eight contracts; no other layer produces a
  competing instance of any of these three types anywhere in the contract
  chain, satisfying Acceptance Criteria AC-02 and AC-05.
- Five retained competing shapes are recorded `REJECT_DIRECT_IMPORT` with
  named source evidence: the Flow-embedded `RefineryPacket`
  (`packetId`/camelCase/`READY_FOR_VERIFICATION`), the Flow
  `attach-source.ts` second source-capture point, the open
  `truth.packet.schema.json` boundary, the `publish-gate.ts`
  caller-supplied `truthKernelAccepted: boolean`, and the `source-score.ts`
  direct-mutation path. None of these five shapes were imported or merged
  into the canonical contracts.
- All twelve negative-case categories required by the work order are present
  (zero Refinery stages; empty evidence; empty verification results;
  packet-hash mismatch; receipt-content mismatch; policy/rule-version
  mismatch; cross-packet evidence; replayed receipt; expired
  TruthReference; revoked/superseded reference; caller-supplied approval
  boolean; direct feedback mutation), each mapped to a source-backed
  retained-prototype gap from the roadmap's Known Prototype Gaps table or
  T0R's Axis 4/6 evidence, so the negative cases are not invented risks. A
  thirteenth case, NC-04A, was added in round 1 per completion review
  finding R4 (a non-accepting receipt must never mint a `TruthReference`).
  A fourteenth case, NC-04B, was added in round 2 per completion review
  finding R8 (decision-resolution mismatch or non-empty `failed_obligations`
  must fail closed before reference issuance).

## Eight-Contract Inventory And Reconciliation Summary

| Metric | Value |
|---|---:|
| Required canonical contract types (work order) | 8 |
| Defined contract types (contract chain file) | 8 |
| Contract types with exactly one sole producer | 8 |
| Contract types with a source-provenance citation | 8 |
| Contract types with a compatibility/exclusion decision | 8 |
| Baseline invariants required | 10 |
| Baseline invariants defined and mapped | 10 |
| Negative cases required (minimum) | 12 |
| Negative cases defined | 14 (12 originally required plus NC-04A added by the R4 repair and NC-04B added by the R8 repair) |

Full per-contract and per-invariant detail is in the two companion reference
outputs; this return does not repeat the full field tables, per the work
order's five-output boundary.

## Compatibility/Exclusion Decision Distribution

| Decision token | Count |
|---|---:|
| `ADAPT` (contract-level primary disposition) | 6 |
| `NEW_DOC_ONLY` | 2 |
| `REJECT_DIRECT_IMPORT` (competing retained shapes) | 5 |
| Total contracts | 8 |

`DistributionPackage` and `FeedbackProposal` each carry a primary `ADAPT`
disposition for their canonical field set plus an additional
`REJECT_DIRECT_IMPORT` sub-decision for their specific competing retained
shape (`publish-gate.ts` boolean and `source-score.ts` mutation,
respectively); this compound recording is explained in full in the source
reconciliation review's Compatibility/Exclusion Decision Summary section.
The `ADAPT` count is corrected to 6 in this repair round: the initial return
reported 5 while the contract-chain file already named all six ADAPT
contracts, an internally false reconciliation identified as completion
review finding R1. 6 `ADAPT` + 2 `NEW_DOC_ONLY` = 8 total contract-level
primary dispositions, matching the 8-contract inventory.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| a retained competing packet shape is mistaken for an acceptable variant | every competing shape identified in T0R's Producer/Consumer table is explicitly `REJECT_DIRECT_IMPORT` in both the contract-chain file and the source reconciliation review |
| Kernel's sole authority over decision/receipt/reference is diluted by an ambiguous consumer role | the Producer/Consumer Uniqueness Table in the contract-chain file lists Kernel as sole producer for all three types with Refinery and Flow explicitly named as forbidden producers |
| an empty-collection or replay case is left as an implicit assumption rather than a named negative case | all fourteen negative cases are enumerated in a single table with contract, input condition, expected fail-closed outcome, and bound invariant |
| TKG-T1 field minimums are silently restated as new doctrine instead of referenced | the source reconciliation review's TKG-T1 Field Dependency Reconciliation table explicitly defers field-by-field reconciliation to a future tranche rather than claiming this chain redefines TKG-T1's vocabulary |
| a non-accepting receipt is assumed sufficient to mint a TruthReference | the contract-chain file's Eligible-Acceptance-Only Issuance Rule and Negative Case NC-04A require `decision: ACCEPT_EVIDENCE_CANDIDATE`, satisfied obligations, and no blocking verification failure before any reference is minted |
| the RefineryPacket lifecycle status is read as also carrying failure reasons | `status` is now a lifecycle-only field (`IN_PROGRESS`/`READY_FOR_KERNEL`/`REVIEW_REQUIRED`/`BLOCKED`); every reason code lives in the separate `failure_tokens` field |
| a receipt hash is narrowed to a partial-field subset, missing receipt identity, or non-canonical encoding/escaping, allowing evidence/obligation/verification-result substitution or divergent digests | the contract-chain file's Receipt Hash Canonical Preimage Profile subsection binds every authority-bearing receipt field (including `receipt_id`) under one fixed canonical preimage profile (`cvf.sotThreeLayer.receiptHash.v1`, SHA-256, UTF-8 RFC 8785 JCS-canonical JSON, no insignificant whitespace, fixed named fields in fixed order, ISO 8601 UTC timestamps, `null` for absent scalars, `[]` for empty collections, lexicographic collection sorting, `receipt_hash` excluded from its own preimage) with a published test vector (522-byte illustrative preimage, SHA-256 `bc32424380bd483ca208edd8ee18bcaaa874b109584341e8febc01b5e46ab5a3`) so any two independent verifiers produce the same digest; Invariant 5 and NC-05 updated accordingly |
| a TruthReference is minted without resolving the complete receipt-to-decision-to-request chain, without content/version equality, or when failed_obligations is non-empty | the contract-chain file's Decision-Resolution Model and Negative Case NC-04B require Kernel to resolve the immutable `KernelDecision` via `TruthReceipt.decision_id` and the immutable `KernelEvaluationRequest` via `KernelDecision.request_id`, compare `evidence_refs`/`obligation_refs` to the request (not the decision), compare `decision`/`verification_result_refs` to the decision, verify `evaluated_content_hash`/`packet_hash`, `policy_version`, and `rule_version` equality across receipt, decision, and request, and confirm `failed_obligations` is empty before reference issuance; every missing record, broken link, or field mismatch fails closed |

## Decision / Disposition

Worker disposition: `COMPLETE_PENDING_REVIEW`. All required evidence is
delivered across the five owned outputs. No runtime, schema, test, guard, or
checker was created or mutated, no package was activated, and no direct
import of retained competing shapes occurred. All eight contracts, ten
invariants, and fourteen negative cases remain pending CVF reviewer
acceptance, revision, or rejection. This return reflects the bounded repair
of completion review findings R1-R6 (round 1), R7-R8 (round 2), R9-R10
(round 3), and R11-R12 (round 4); see the Bounded Repair Round sections
below for the exact repair-to-finding mapping.

## Rescan Intelligence Hardening

- Original source artifact: `docs/reviews/CVF_SOT3_T0R_THREE_LAYER_ARCHITECTURE_DECISION_RECOMMENDATION_2026-07-12.md`
- Predecessor intake artifact: `docs/reviews/CVF_SOT3_T1_OWNER_NOVELTY_MAP_2026-07-12.md`
- Delta ledger status: NOT_APPLICABLE_WITH_REASON
- Routing matrix status: NOT_APPLICABLE_WITH_REASON
- Semantic sampling status: NOT_APPLICABLE_WITH_REASON
- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

N/A with reason: this tranche is canonical contract authoring from
already-accepted T0R/T1 evidence, not a corpus rehash or file-level
re-intake of the retained three-folder source. The work order's do-not-
misread instruction explicitly forbids TypeScript, JSON Schema, tests,
runtime, guards, checkers, packages, provider calls, or public artifacts; no
305-file rescan was performed or required, since the input for this tranche
is the already-accepted T0R Producer/Consumer table and T1 owner decisions,
not the retained source files themselves. `git status` was clean at
`executionBaseHead` and remained clean throughout, aside from the five
worker-owned outputs.

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | accepted T0R/T1 evidence and TKG-T1 upstream doctrine |
| Enumeration command | direct parse of the T0R Producer/Consumer Packet And Receipt Mapping table (8 rows) and the T1 owner map CAP-01 decision |
| Manifest artifact or inline manifest | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md` (reused as this return's manifest) |
| Processing ledger artifact or inline ledger | `docs/reviews/CVF_SOT3_T2_CONTRACT_SOURCE_RECONCILIATION_2026-07-12.md` |
| Ledger terminal statuses | ADAPT, NEW_DOC_ONLY, REJECT_DIRECT_IMPORT |
| Disposition taxonomy | ADAPT, NEW_DOC_ONLY, REJECT_DIRECT_IMPORT |
| Owner-surface map | Authority Map table in `docs/reference/sot_three_layer/README.md` |
| Unresolved items | 0; all 8 contracts have a terminal compatibility/exclusion decision |
| Completion claim boundary | documentation contract authoring only; no runtime creation |

## Corpus Completeness And Report Integrity

- Corpus task class: SOT3 canonical inter-layer contract authoring,
  worker-return summary level.
- Corpus root: accepted T0R Producer/Consumer table (8 rows) and T1 owner
  map CAP-01 decision.
- Snapshot time: 2026-07-12, T2 execution.
- Enumeration command: filesystem-backed direct file reads of the 8
  Producer/Consumer table rows and the T1 CAP-01 owner-decision entry.
- Manifest artifact or inline manifest: `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md`.
- Manifest hash: N/A with reason - this return reconciles against the
  companion output's contract-key set, not a hashed file corpus.
- Processing ledger artifact or inline ledger: `docs/reviews/CVF_SOT3_T2_CONTRACT_SOURCE_RECONCILIATION_2026-07-12.md`.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, REJECTED, BLOCKED_UNREADABLE
- Reconciliation: manifest=8; ledger_terminal=8; exclusions=0; unresolved=0
- Unresolved files: 0; all 8 contracts carry a terminal compatibility/
  exclusion decision in the source reconciliation review.
- Declared exclusions: none.
- Unreadable or unsupported files: none encountered.
- Aggregation check: 8 contract types in, 8 compatibility/exclusion
  decisions out, 8 unique contract names, 0 missing, 0 extra, 0 duplicate
  (independently re-derived directly from the contract-chain file's
  Contract Inventory table).
- Drift check: T0R, T1, and TKG-T1 source evidence unchanged throughout this
  return's authoring.
- Output traceability: every contract cites its T0R Producer/Consumer table
  row or its `NEW_DOC_ONLY` roadmap design-label source.
- Adversarial verification: every retained competing shape named in T0R's
  Producer/Consumer table was checked against the canonical contract
  definitions to confirm it is explicitly `REJECT_DIRECT_IMPORT`, not
  silently merged or omitted.
- Corpus verdict: PARTIAL - the 8-contract canonical chain reconciliation is
  COMPLETE_VERIFIED for this tranche's scope; the underlying 305-file
  per-file closeout remains a later SOT3-T7 lane.

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| 8 T0R Producer/Consumer contract rows | canonical field minimums, producer/consumer roles, and named competing-shape rejections | contract authoring | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md` | CVF reviewer accepts, revises, or rejects each of the 8 contracts | no implementation |
| roadmap Known Prototype Gaps and T0R Axis 4/6 evidence | 12 source-backed negative cases with fail-closed expected outcomes | invariant/negative-case authoring | `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md` | CVF reviewer reproduces the fail-closed rationale directly | no runtime action |
| TKG-T1 evidence/obligation/verification-result minimums | upstream doctrine field-shape dependency for `evidence_refs`/`obligation_refs` | dependency reconciliation, deferred | source reconciliation review, TKG-T1 Field Dependency Reconciliation table | reopen only when a future TKG-T2-style tranche performs field-by-field reconciliation | no runtime or package action |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Three-layer architecture topology (CAP-01) | `docs/reference/sot_three_layer/` (new, this tranche) | NEW_OWNER_CREATED_THIS_TRANCHE | eight-contract canonical chain did not exist before SOT3-T2; TKG-T1 remains a dependency, not the owner | CVF reviewer accepts, revises, or rejects the new owner surface |
| Truth-foundation doctrine (CAP-04, CAP-09) | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | ENRICH_EXISTING_OWNER, unchanged from T1 | referenced by relation for evidence/obligation/verification-result field shapes; not restated or replaced | preserve TKG-T1 as upstream doctrine owner; defer field reconciliation |
| Skill-specific truth packet | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | vertical owner, confirmed narrower, unchanged from T1 | not a general SOT owner candidate; no interaction with this tranche's contracts | preserve compatibility boundary |
| Receipt binding | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts` | REJECT_DIRECT_IMPORT, field-level confirmed, unchanged from T1 | workflow-step execution receipt, not truth-verification receipt; `TruthReceipt` does not collide with it | no action; different owner confirmed again |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | T0R acceptance -> T1 owner and value reconciliation -> SOT3-T2 canonical contract authoring -> CVF reviewer decision -> possible fresh implementation tranche |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_truth_foundation_claim_guard.py`; `governance/compat/check_agent_handoff_boundary.py` |
| Owner surface | this return for execution evidence; CVF reviewer for acceptance |
| Disposition | ADAPT through bounded canonical contract authoring |
| Claim boundary | no external output becomes CVF authority directly; no runtime symbol is claimed to exist |

## Finding-To-Governance Learning Disposition

| Finding | defectClass | learningLane | disposition | nextAction |
|---|---|---|---|---|
| the retained corpus concentrates its fail-open gaps in exactly the empty-collection and unbound-hash cases the work order asked to be covered as negative cases | RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | CVF reviewer should confirm whether a future SOT3-T3/T4 contract-test suite should be seeded directly from this tranche's fourteen negative cases rather than re-deriving them |
| `DistributionPackage` and `FeedbackProposal` each carry both a primary `ADAPT` and a shape-level `REJECT_DIRECT_IMPORT` sub-decision, and the initial draft's contract-level `ADAPT` count (5) did not match the six contracts actually named `ADAPT`, an internally false reconciliation (completion review R1) | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | RUNTIME_LEARNING_CANDIDATE | preserve the corrected 6/2/8 count and the compound-disposition explanation as a documented example for future owner/compatibility reconciliation tranches; independently re-derive contract-level counts by counting the source file's own decision cells rather than trusting a prior draft's summary |
| a documentation-only contract can still contain an internal logical gap (undefined verification-result transport; a non-eligible receipt able to satisfy a downstream issuance precondition; a composite state field with no per-field vocabulary) even when every field traces to a cited source | WORKER_EXECUTION_ERROR | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | future documentation-contract tranches should explicitly trace each field's producer-to-consumer data flow end to end, not only its source citation, before returning for review |

Runtime/provider/cost learning lane: N/A_WITH_REASON - none of the findings
above are a runtime-behavior, provider-output, or cost/token/latency-
economics finding; all are governance-control-plane design observations
about contract authoring, reconciliation-table shape, and internal
consistency, so `GOVERNANCE_CONTROL_PLANE` is the correct and complete
learning lane for this tranche.

Next action: route the eight contracts, ten invariants, and fourteen
negative cases to the CVF reviewer for acceptance, revision, or rejection
before any implementation tranche (SOT3-T3 or later) is authorized.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: one canonical chain can preserve TKG-T1
doctrine while adding the missing three-module boundaries without duplicate
authority.

Evidence Comparison Requirement: every field and invariant was compared
against T0R's Producer/Consumer Packet And Receipt Mapping table, T1's CAP-01
owner decision, TKG-T1's Evidence/Obligation/Verification Result Minimums,
the skill truth-packet standard's narrower scope, the Guard Contract receipt
collision, and the retained specs cited in T0R's evidence-for/evidence-
against columns.

Contradiction Or Gap Disposition: the prediction held at the structural
level: eight contract types were defined with exactly one sole producer
each, Kernel retained exclusive decision/receipt/reference authority, and
TKG-T1's governing chain was preserved by reference rather than restated or
duplicated. The remaining TKG-T1 field-by-field reconciliation gap is
recorded as a deferred dependency, consistent with T1's CAP-04 finding, not
a contradiction of this tranche's prediction. The completion review found
twelve genuine internal-consistency contradictions/gaps at the semantic level
across four bounded-repair rounds. Round 1 (R1-R6): a false ADAPT count, a
lifecycle status conflated with failure reason codes, an undefined
verification-result ownership/transport boundary, a rejected/escalated
receipt able to satisfy a downstream reference-issuance precondition, an
unimplementable composite TruthReference state model, and an unqualified
`ACCEPT` token. Round 2 (R7-R8): the receipt hash did not bind the
evidence/obligation/verification-result decision basis, and the reference
eligibility rule cited an unresolved `failed_obligations` field with no
defined owner path. Round 3 (R9-R10): the round 2 decision-resolution
comparison targeted `evidence_refs`/`obligation_refs` on `KernelDecision`,
which does not define those fields, and the round 2 receipt hash
serialization permitted multiple encodings that produce different digests
for the same receipt. Round 4 (R11-R12): the canonical preimage omitted
`receipt_id` and left JSON string bytes ambiguous under generic "standard
JSON escaping", and the resolution chain did not compare
`evaluated_content_hash`/`packet_hash`, `policy_version`, or `rule_version`
across receipt, decision, and request. This fourth bounded repair round
corrects R11 and R12 directly in the contract-chain and invariants files,
adding `receipt_id` to the canonical preimage, replacing generic JSON
escaping with RFC 8785 JCS string serialization, publishing one complete
test vector with its verified SHA-256 digest, and extending the resolution
chain to require exact equality of `evaluated_content_hash`/`packet_hash`,
`policy_version`, and `rule_version` across receipt, decision, and request.

Claim Update Requirement: every one of the 8 contracts carries an explicit
sole producer, allowed consumers, field minimums, status vocabulary,
transitions, authority boundary, source provenance, and compatibility/
exclusion decision in the contract-chain file; every one of the 10 baseline
invariants is mapped to at least one negative case and one contract field/
status rule in the companion invariants file; none remain unclassified.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_truth_foundation_claim_guard.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | Self-declared worker-return artifact: yes; Responds to work order; dispatchWorkOrder; executionBaseHead; COMPLETE_PENDING_REVIEW; COMPLETE_VERIFIED; PARTIAL; NOT_AUTHORIZED; hash/receipt/truth claim-boundary phrasing patterns; External Absorption Core; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block |
| gateRunPurpose | confirm exact worker-return and corpus evidence shape after checker source review, informed directly by the T1 worker-return repair lessons and the truth-foundation claim guard's overclaim-pattern regex |
| claimBoundary | checker-shape conformance does not prove contract or runtime correctness |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude no-commit documentation-contract worker |
| Provider or surface | local authorized private provenance workspace |
| Session or invocation | SOT3-T2 canonical inter-layer contract authoring execution, 2026-07-12 |
| Working directory | repository root |
| Command or tool surface | filesystem-backed direct file reads, Grep, git read-only |
| Target paths | accepted T0R/T1 evidence, TKG-T1 contract, SOT3 roadmap and GC-018 baseline, 5 worker-owned outputs |
| Allowed scope source | SOT3-T2 work order Planned Worker Fulfillment Manifest |
| Before status evidence | executionBaseHead `8e318cc92`; clean worktree at worker start |
| After status evidence | five worker-owned outputs created; no runtime, schema, test, guard, checker, package, session, or public-sync mutation |
| Diff evidence | `git status --short` and `git diff --name-status` both list only the five owned outputs, all as additions |
| Approval boundary | canonical inter-layer contract documentation authoring only |
| Claim boundary | no owner-surface implementation, contract ratification claim, runtime, direct import, provider/live proof, public action, or readiness claim |
| Agent type | no-commit documentation-contract worker |
| Invocation ID | `sot3-t2-canonical-inter-layer-contracts-execution-2026-07-12` |
| Expected manifest | README; contract chain reference; invariants and negative cases reference; contract source reconciliation review; worker return |
| Actual changed set | README; contract chain reference; invariants and negative cases reference; contract source reconciliation review; worker return |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: create-only worker outputs; no source or governed artifact deleted or renamed |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | SOT3-T2 canonical inter-layer contract documentation authoring only |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - contract chain and invariants files record source citations, T0R/T1 table row references, and terminal compatibility decisions |
| actionEvidence | ACTION_EVIDENCE_PRESENT - README, contract chain reference, invariants reference, source reconciliation review, and this return are the tranche's actions |
| invocationBoundary | local read-only source evidence review plus owned-output authoring |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, or runtime interception behavior claimed |
| claimLanguage | bounded no-commit documentation-only contract authoring |
| forbiddenExpansion | runtime, schema, test, guard, checker, package implementation, direct import, provider/live proof, public-sync, commit, release, readiness |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this return cites private retained source context and internal
contract design; it is intended for a local authorized CVF reviewer surface
only.

## Claim Boundary

This return is advisory external evidence. It proves complete 8-contract
canonical chain authoring, 10 invariants mapped to negative cases, 14
source-backed negative cases, and full field-level source/collision
reconciliation with named `REJECT_DIRECT_IMPORT` decisions for every
competing retained shape. It does not authorize implementation, package
activation, direct import, provider/live proof, public-sync, commit, push,
release, or production readiness. All contracts, invariants, and negative
cases remain PENDING_CVF_REVIEWER.

## Bounded Repair Round 1 (2026-07-12)

Responds to: `docs/reviews/CVF_SOT3_T2_COMPLETION_REVIEW_2026-07-12.md`,
Disposition `RETURN_FOR_BOUNDED_REPAIR`, findings R1-R6 (round 1).

- **R1** - the contract-level `ADAPT` count was corrected from 5 to 6 in the
  source reconciliation review and this return, matching the six contracts
  the contract-chain file already named `ADAPT`
  (`SourceEnvelope`/`RefineryPacket`/`KernelDecision`/`TruthReceipt`/
  `DistributionPackage`/`FeedbackProposal`). Shape-level
  `REJECT_DIRECT_IMPORT` sub-decisions for `DistributionPackage` and
  `FeedbackProposal`'s competing retained shapes remain in the separate
  5-count shape ledger, not folded into the contract-level count.
- **R2** - `RefineryPacket.status` narrowed to lifecycle-only values
  (`IN_PROGRESS`/`READY_FOR_KERNEL`/`REVIEW_REQUIRED`/`BLOCKED`);
  `REFINERY_NO_STAGES_EXECUTED` and other reason codes moved exclusively
  into `failure_tokens`. Zero executed stages now yields `status: BLOCKED`
  plus `failure_tokens: [REFINERY_NO_STAGES_EXECUTED]`. NC-01 updated to
  match.
- **R3** - `KernelEvaluationRequest` no longer implies it carries
  verification results. A new Verification-result ownership and transport
  model states that Kernel produces verification results during evaluation
  and binds them into the new `KernelDecision.verification_result_refs`
  field and the existing `TruthReceipt.verification_result_refs` field.
- **R4** - `TruthReceipt` may record every Kernel decision outcome, but a
  new Eligible-Acceptance-Only Issuance Rule on `TruthReference` requires
  `decision: ACCEPT_EVIDENCE_CANDIDATE`, satisfied mandatory obligations,
  and no blocking verification failure before Kernel may mint a reference.
  New Negative Case NC-04A proves a non-accepting receipt cannot mint a
  reference.
- **R5** - `TruthReference`'s composite `supersession_state`/
  `revocation_state` fields were replaced with a single `reference_state`
  field, exact vocabulary `ACTIVE`/`SUPERSEDED`/`REVOKED`/`EXPIRED`, and an
  explicit precedence rule (`REVOKED > SUPERSEDED > EXPIRED > ACTIVE`).
  Expiry is defined as derived from `valid_until_utc`, not a separately
  stored flag; `REVOKED`/`SUPERSEDED` remain explicit stored transitions.
- **R6** - `KernelDecision.decision` and `TruthReceipt.decision` were
  restored to `ACCEPT_EVIDENCE_CANDIDATE` everywhere the initial draft used
  unqualified `ACCEPT`. No unqualified `ACCEPT` token remains in either
  reference file.
- All derived summaries were reconciled across the five outputs: the
  negative-case count is now 14 (12 originally required plus NC-04A from R4
  and NC-04B from R8); the Compatibility/Exclusion Decision Summary and
  Compatibility/Exclusion Decision Distribution tables both read `ADAPT: 6`,
  `NEW_DOC_ONLY: 2`, `REJECT_DIRECT_IMPORT: 5`; Epistemic Process Blocks in
  all three affected files record the R1-R8 findings as
  genuinely-found-and-repaired contradictions rather than silently rewriting
  history.
- Only the five worker-owned outputs were edited. No sixth artifact was
  created, no runtime/schema/test/guard/checker was created or mutated, and
  no commit was made. `executionBaseHead` `8e318cc92` remains HEAD.

## Bounded Repair Round 2 (2026-07-12)

Responds to: `docs/reviews/CVF_SOT3_T2_COMPLETION_REVIEW_2026-07-12.md`,
Disposition `RETURN_FOR_BOUNDED_REPAIR`, findings R7-R8 (round 2). Note:
round 3 below corrects two gaps in this round's R7/R8 repair.

- **R7** - `TruthReceipt.receipt_hash` payload widened from
  `evaluated_content_hash` + `decision` + `policy_version`/`rule_version` +
  `predecessor_receipt_hash` to every authority-bearing receipt field:
  `decision_id`, `decision`, `evaluated_content_hash`, `evidence_refs`,
  `obligation_refs`, `verification_result_refs`, `policy_version`,
  `rule_version`, `decided_at_utc`, `issued_at_utc`, and
  `predecessor_receipt_hash`. A new Receipt Hash Payload And Deterministic
  Serialization subsection in the contract-chain file's `TruthReceipt`
  section specifies fixed canonical field order, lexicographic collection
  ordering by reference identifier, and documentation-contract-level
  serialization (concrete byte-level encoding deferred to implementation).
  Invariant 5 and NC-05 in the invariants file updated to require every
  authority-bearing field under deterministic collection ordering. An actor
  can no longer substitute evidence, obligation, or verification-result
  bindings without violating `receipt_hash`.
- **R8** - `failed_obligations` authority path made explicit via model 2
  (decision resolution). `TruthReceipt` does not carry a
  `failed_obligations` field; that field belongs to `KernelDecision` only.
  A new Decision-Resolution Model subsection in the contract-chain file's
  `TruthReference` section requires Kernel to resolve the immutable
  `KernelDecision` identified by `TruthReceipt.decision_id` and verify:
  (a) the decision exists; (b) `TruthReceipt.decision` exactly matches
  `KernelDecision.decision`; (c) `TruthReceipt`'s `evidence_refs`/
  `obligation_refs`/`verification_result_refs` exactly match the resolved
  decision's bindings; (d) `KernelDecision.failed_obligations` is empty.
  Missing decision, binding mismatch, or non-empty `failed_obligations`
  fails closed. The Eligible-Acceptance-Only Issuance Rule expanded from
  three to four conditions to include decision resolution and empty
  `failed_obligations`. Invariant 6 updated to require decision resolution
  with empty `failed_obligations`. New Negative Case NC-04B proves
  decision-resolution mismatch or non-empty `failed_obligations` fails
  closed.
- All derived summaries were reconciled across the five outputs: the
  negative-case count is now 14 (12 originally required plus NC-04A from R4
  and NC-04B from R8); the README Authority Map Kernel row reflects both
  the widened receipt hash and the decision-resolution requirement; the
  source reconciliation review's Bounded Repair Reconciliation table now
  covers R1-R8; Epistemic Process Blocks in all affected files record the
  R7-R8 findings as genuinely-found-and-repaired gaps rather than silently
  rewriting history.
- Only the five worker-owned outputs were edited. No sixth artifact was
  created, no runtime/schema/test/guard/checker was created or mutated, and
  no commit was made. `executionBaseHead` `8e318cc92` remains HEAD.

## Bounded Repair Round 3 (2026-07-12)

Responds to: `docs/reviews/CVF_SOT3_T2_COMPLETION_REVIEW_2026-07-12.md`,
Disposition `RETURN_FOR_BOUNDED_REPAIR`, findings R9-R10 (round 3). Note:
round 4 below corrects two gaps in this round's R10/R12 repair.

- **R9** - the round 2 Decision-Resolution Model compared
  `TruthReceipt.evidence_refs`/`obligation_refs` to `KernelDecision`'s
  "corresponding bindings", but `KernelDecision` does not define
  `evidence_refs` or `obligation_refs`; those fields belong to
  `KernelEvaluationRequest` only. The Decision-Resolution Model is
  corrected to resolve the immutable `KernelEvaluationRequest` via
  `KernelDecision.request_id` and compare:
  - `TruthReceipt.decision` to `KernelDecision.decision`;
  - `TruthReceipt.verification_result_refs` to
    `KernelDecision.verification_result_refs`;
  - `TruthReceipt.evidence_refs` to
    `KernelEvaluationRequest.evidence_refs`;
  - `TruthReceipt.obligation_refs` to
    `KernelEvaluationRequest.obligation_refs`;
  - `KernelDecision.packet_hash` to
    `KernelEvaluationRequest.packet_hash`;
  - `KernelDecision.failed_obligations` must be empty.

  The Eligible-Acceptance-Only Issuance Rule condition (1) is updated to
  name the complete resolution chain and the correct comparison targets.
  NC-04B is updated to name only fields actually defined on each contract.
  Invariant 6 is updated to bind `KernelEvaluationRequest` and use the
  complete resolution chain. Every missing record, broken link, or field
  mismatch fails closed.
- **R10** - the round 2 Receipt Hash Payload And Deterministic
  Serialization subsection permitted a future implementation to choose
  canonical JSON, length-prefixed concatenation, or a tagged structure;
  those encodings produce different byte sequences and hashes for the same
  receipt. The subsection is replaced by the Receipt Hash Canonical
  Preimage Profile (`cvf.sotThreeLayer.receiptHash.v1`), which defines
  exactly one canonical preimage: SHA-256 digest, UTF-8 canonical JSON
  with no insignificant whitespace, fixed named fields in fixed order
  (`receipt_hash_profile`, `digest_algorithm`, `decision_id`, `decision`,
  `evaluated_content_hash`, `evidence_refs`, `obligation_refs`,
  `verification_result_refs`, `policy_version`, `rule_version`,
  `decided_at_utc`, `issued_at_utc`, `predecessor_receipt_hash`), ISO
  8601 UTC timestamps (`YYYY-MM-DDTHH:MM:SSZ`), JSON `null` for absent
  scalars and `[]` for empty collections, collection arrays sorted
  lexicographically by reference identifier (Unicode code point order,
  ascending), `receipt_hash` itself excluded from the preimage, and the
  profile identifier and digest algorithm included in the preimage. A
  future implementation tranche must not choose a different encoding,
  digest, field order, or collection representation. Invariant 5 and
  NC-05 are updated to require the one canonical profile. Any two
  independent verifiers computing `receipt_hash` from the same receipt
  field values now produce the same digest.
- All derived summaries were reconciled across the five outputs: the
  README Authority Map Kernel row reflects the complete resolution chain
  and the one canonical preimage profile; the source reconciliation
  review's Bounded Repair Reconciliation table now covers R1-R10;
  Epistemic Process Blocks in all affected files record the R9-R10
  findings as genuinely-found-and-repaired gaps rather than silently
  rewriting history.
- Only the five worker-owned outputs were edited. No sixth artifact was
  created, no runtime/schema/test/guard/checker was created or mutated, and
  no commit was made. `executionBaseHead` `8e318cc92` remains HEAD.

## Bounded Repair Round 4 (2026-07-12)

Responds to: `docs/reviews/CVF_SOT3_T2_COMPLETION_REVIEW_2026-07-12.md`,
Disposition `RETURN_FOR_BOUNDED_REPAIR`, findings R11-R12 (round 4).

- **R11** - the round 3 Receipt Hash Canonical Preimage Profile omitted
  `receipt_id` from the preimage even though it is the receipt's required
  identity and an authority-bearing field, and used generic "standard JSON
  escaping" which permits multiple valid JSON spellings for the same
  string (literal Unicode versus escaped form). The profile is corrected:
  - `receipt_id` is added to the fixed preimage field order (after
    `digest_algorithm`, before `decision_id`), so receipt identity
    substitution now violates `receipt_hash`.
  - Generic "standard JSON escaping" is replaced with RFC 8785 (JSON
    Canonicalization Scheme, JCS) string serialization: characters
    U+0000 through U+001F escaped as `\uXXXX` (lowercase hex), double-quote
    and backslash escaped as `\"` and `\\`, all other characters
    (including non-ASCII Unicode) emitted as literal UTF-8 bytes without
    `\u` escaping. No Unicode pre-normalization (NFC or otherwise) is
    applied; strings are serialized as-is.
  - One complete illustrative canonical preimage (522 bytes, UTF-8, JCS,
    no insignificant whitespace) is published in the contract-chain file
    with its expected SHA-256 digest
    `bc32424380bd483ca208edd8ee18bcaaa874b109584341e8febc01b5e46ab5a3`,
    computed and verified locally with Python `hashlib.sha256` before
    recording. A future implementation tranche must reproduce this digest
    from this exact preimage as a profile conformance test.
  - Invariant 5 and NC-05 are updated to require `receipt_id` inclusion
    and JCS string serialization, and to reference the published test
    vector.
- **R12** - the round 3 Decision-Resolution Model checked
  decision/request identity and evidence/result bindings but did not
  require `TruthReceipt.evaluated_content_hash` to equal the resolved
  decision/request packet hash, and did not compare the receipt's
  `policy_version` and `rule_version` with the resolved decision and
  request. The resolution chain is extended to require exact equality:
  - `TruthReceipt.evaluated_content_hash` ==
    `KernelDecision.packet_hash` ==
    `KernelEvaluationRequest.packet_hash` (all three equal);
  - `TruthReceipt.policy_version` ==
    `KernelDecision.policy_version` ==
    `KernelEvaluationRequest.policy_version` (all three equal);
  - `TruthReceipt.rule_version` ==
    `KernelDecision.rule_version` ==
    `KernelEvaluationRequest.rule_version` (all three equal).

  The Eligible-Acceptance-Only Issuance Rule condition (1) is updated to
  include content/version equality. NC-04B is updated to include
  content/version mismatch as a fail-closed condition. Invariant 6 is
  updated to require content/version equality and now binds NC-07. Every
  missing value, broken link, or mismatch fails closed.
- All derived summaries were reconciled across the five outputs: the
  README Authority Map Kernel row reflects `receipt_id` inclusion, JCS
  serialization, the published test vector, and content/version equality;
  the source reconciliation review's Bounded Repair Reconciliation table
  now covers R1-R12; Epistemic Process Blocks in all affected files record
  the R11-R12 findings as genuinely-found-and-repaired gaps rather than
  silently rewriting history.
- Only the five worker-owned outputs were edited. No sixth artifact was
  created, no runtime/schema/test/guard/checker was created or mutated, and
  no commit was made. `executionBaseHead` `8e318cc92` remains HEAD.

## Command Evidence

Range: `8e318cc92..HEAD` (executionBaseHead to current worktree state).

```text
git rev-parse --short HEAD
8e318cc92

git status --short --untracked-files=all
?? docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md
?? docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md
?? docs/reference/sot_three_layer/README.md
?? docs/reviews/CVF_SOT3_T2_CONTRACT_SOURCE_RECONCILIATION_2026-07-12.md
?? docs/reviews/CVF_SOT3_T2_WORKER_RETURN_2026-07-12.md
```

All matching content checkers listed in the Checker Source Read-Ahead Block
were run against this range after each in-place repair of this return's own
shape. `python governance/compat/run_worker_return_fast_gate.py` (61/61
checks) and `python governance/compat/check_markdown_structural_completeness.py
--base 8e318cc92 --head HEAD --enforce` (5/5 files) both ran clean against
all five outputs on the final pass.

Note: the standalone `check_truth_foundation_claim_guard.py --base
8e318cc92 --head HEAD --enforce` CLI invocation only auto-discovered 2 of 5
changed files, because its worktree scan uses `git status --short` without
`--untracked-files=all`, which collapses a brand-new untracked directory
(`docs/reference/sot_three_layer/`) into one non-`.md` directory line rather
than three per-file entries. The bundled `run_worker_return_fast_gate.py`
run does reach all five files and passed. To close this gap directly, the
guard's own `diagnose_truth_foundation_claims()` function was invoked
manually against all five files' current content and returned 0 violations
for each, confirming full content-level compliance independent of the CLI
discovery-path gap. This is a checker discovery-path observation, not a
worker-content defect; no checker file was modified, per the work order's
no-guard-mutation boundary.

Disposition: PASS for every checker scoped to the five worker-owned
outputs.

## git status --short

```text
?? docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md
?? docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md
?? docs/reference/sot_three_layer/README.md
?? docs/reviews/CVF_SOT3_T2_CONTRACT_SOURCE_RECONCILIATION_2026-07-12.md
?? docs/reviews/CVF_SOT3_T2_WORKER_RETURN_2026-07-12.md
```

## Changed Files

`git diff --name-status 8e318cc92..HEAD` equivalent (comparing the clean
executionBaseHead worktree to the current worktree; the worker did not
commit, so this reflects working-tree additions, not a committed diff):

```text
A  docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md
A  docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md
A  docs/reference/sot_three_layer/README.md
A  docs/reviews/CVF_SOT3_T2_CONTRACT_SOURCE_RECONCILIATION_2026-07-12.md
A  docs/reviews/CVF_SOT3_T2_WORKER_RETURN_2026-07-12.md
```

- `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_CONTRACT_CHAIN.md` (created)
- `docs/reference/sot_three_layer/CVF_SOT_THREE_LAYER_INVARIANTS_AND_NEGATIVE_CASES.md` (created)
- `docs/reference/sot_three_layer/README.md` (created)
- `docs/reviews/CVF_SOT3_T2_CONTRACT_SOURCE_RECONCILIATION_2026-07-12.md` (created)
- `docs/reviews/CVF_SOT3_T2_WORKER_RETURN_2026-07-12.md` (created)

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. The no-commit documentation-contract worker
did not commit. HEAD remains at executionBaseHead `8e318cc92`. Only the five
worker-owned outputs are present in the changed set. Any accepted material
commit is owned by the CVF reviewer/closer.
