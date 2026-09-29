# CVF SOT3-T0R Three-Layer Architecture Decision Recommendation

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

docType: review_context

Date: 2026-07-12

Recommendation ID: SOT3-T0R-RECOMMENDATION

## Purpose

Recommend one explicit value for each of the eight required decision axes,
present the strongest alternative architecture, map producer/consumer packet
and receipt contracts across layers, classify capabilities for selective
absorption, and state remaining implementation blockers. This is a
recommendation for the CVF reviewer; it does not ratify architecture or
authorize implementation.

## Target / Source

Same evidence base as the companion semantic reconciliation matrix
(`docs/reviews/CVF_SOT3_T0R_SEMANTIC_RECONCILIATION_MATRIX_2026-07-12.md`):
committed SOT3-T0 advisory evidence plus targeted full-text reads of all 61
documentation files and all load-bearing runtime source across the three
retained roots.

## Scope / Methodology

Each axis below states: the recommended value, the strongest evidence for it,
the strongest evidence against it (dissent), and the disposition of the prior
T0 and dispatcher positions (confirmed, narrowed, revised, rejected, or
blocked).

## Findings / Position

Primary architecture verdict:
`THREE_LAYER_MODEL_CONFIRMED_TOPOLOGY_REVISED_CONTRACT_REWRITE_REQUIRED`.

This retains the dispatcher's three-layer premise, narrows the topology to
strictly post-Kernel Flow (revising Flow's own self-description), and requires
a fail-closed, single-canonical-contract rewrite before any implementation.

## Decision Axes

### Axis 1 - Refinery ownership

**Recommendation: `INDEPENDENT_DETERMINISTIC_NO_AI`.**

Evidence for: `docs/reference/refinery/CVF_REFINERY_DOCTRINE.md` (deterministic-
first, line 17-21), `REFINERY_BOUNDARY_SPEC.md` (module boundary table, line
5-11: Refinery owns preparation, must not own truth approval or final routing),
`CLAIM_BOUNDARY.md`, and every Refinery README, all unanimous.

Evidence against (dissent considered): none found in the Refinery layer itself.
The only pressure against this axis comes externally, from Flow's competing
claim to "refinery structure" (`CLAIM_BOUNDARY.md` line 3) - addressed under
Axis 5, not this axis.

Claim update: CONFIRMED. No narrowing needed.

### Axis 2 - Source position

**Recommendation: `SOURCE_ENVELOPE_FIRST_AND_PERSISTENT`.**

Evidence for: `SOURCE_ENVELOPE_SPEC.md` line 3 ("gives every input a stable
identity ... before refinement") and line 28-37 (mandatory validation fields);
`TRANSFORMATION_LINEAGE_SPEC.md` line 9 places `INTAKE` as the first canonical
stage.

Evidence against: Flow's `attach-source.ts` and `REFINERY_SPEC.md` step 2
("Attach source identity...") define a second, parallel source-capture step
inside Flow's own refine stage - which would place source capture twice in the
same conceptual pipeline if Flow's topology were also adopted. This is resolved
by Axis 5 (Flow topology), not by weakening this axis: Refinery's Source
Envelope remains the single canonical capture point once Flow is confined to
post-Kernel.

Claim update: CONFIRMED.

### Axis 3 - Duplicate/conflict order

**Recommendation: `DUPLICATE_BEFORE_CONFLICT`.**

Evidence for: `TRANSFORMATION_LINEAGE_SPEC.md` line 9 stage enum lists `DEDUPE`
before `CONFLICT`; `CONFLICT_SET_SPEC.md` line 21-30 defines conflict detection
preconditions (same subject/field, overlapping scope, overlapping time window,
differing normalized values) that presuppose records have already been grouped
and normalized - conflict detection operates on the output of duplicate
grouping, not the reverse. `CVF_REFINERY_DOCTRINE.md` line 41-52 pipeline
diagram places fingerprinting/duplicate grouping before conflict detection.

Evidence against: none found; Flow's `cross-reference.ts` computes duplicates
and conflicts in a single pass (line 6-17) without an explicit ordering
distinction, but this is a REJECTED implementation, not authoritative evidence
against the Refinery-side ordering.

Claim update: CONFIRMED.

### Axis 4 - Kernel authority

**Recommendation: `SOLE_TRUST_EVALUATION_AND_RECEIPT`, hardening required.**

Evidence for: `CVF_TRUTH_KERNEL_DOCTRINE.md` (fail-stop doctrine, trusted-core
boundary line 31-42); `VERIFICATION_GATE_SPEC.md` (STRICT/RELAXED/BLOCKED
modes); `EVIDENCE_REGISTRY_SPEC.md`, `OBLIGATION_REGISTRY_SPEC.md`,
`PROVENANCE_LABEL_SPEC.md`, `INDEPENDENT_VERIFIER_SPEC.md` all coherently
assign evidence/obligation/provenance/verification/receipt authority to Kernel
alone; no other layer's documentation claims this authority.

Evidence against (hardening required, not axis rejection):
`truth-receipt.ts` lines 26-30 return `status: 'pass'` on an empty
`verification_results` array, contradicting `VERIFICATION_GATE_SPEC.md` line
33 ("Missing required evidence blocks"); `strict-mode.ts` lines 3-8 pass on
empty results for the same reason; `relaxed-mode.ts` line 4 blocks only
`method === 'obligation'` failures, narrower than
`INDEPENDENT_VERIFIER_SPEC.md`'s stated concern for numerical/contractual/legal
claims (line 22); the receipt hash (`hash-chain.ts` via `truth-receipt.ts` line
48) covers receipt metadata, not full packet content;
`truth.packet.schema.json` line 6 `additionalProperties: true` leaves the
shared boundary open; `EVIDENCE_REGISTRY_SPEC.md` line 51 requires
`approved`-status evidence in STRICT mode but no gate code checks evidence
status, only verification-result status.

Claim update: CONFIRMED as sole authority; the receipt/gate/schema
implementation requires the Axis 6 fail-closed rewrite before this authority
can be trusted operationally.

### Axis 5 - Flow topology

**Recommendation: `POST_KERNEL_ONLY`.**

This is the most contested axis and the one where T0R diverges most sharply
from Flow's own self-description.

Evidence for `POST_KERNEL_ONLY`:
`docs/reference/refinery/REFINERY_BOUNDARY_SPEC.md` line 5-11 explicitly denies
Flow "raw normalization" and "truth declaration" and confines it to "scoped
routing, distribution, lifecycle, feedback, retirement." Kernel's own root
diagrams (`EXTENSIONS/CVF_TRUTH_KERNEL/README.md`, `docs/reference/truth/
README.md`) both show `Canonical Sources -> Kernel -> Governance Runtime` with
no Flow or Refinery pre-Kernel role. Flow's own post-Kernel-only capabilities
(routing, dose, distribution, feedback, retirement - `FLOW_ROUTING.md`,
`INFORMATION_DOSE.md`, `CONTEXT_DISTRIBUTION.md`, `MULTI_LEVEL_SOT.md`) are
uncontested, high-value, and require no pre-Kernel role to function.

Evidence against (Flow's own claim, considered in full):
`EXTENSIONS/CVF_TRUTH_FLOW/README.md` line 10 (`Acquire -> Refine -> Verify
through Truth Kernel -> Register...`), `FLOW_PIPELINE.md` line 6-7 (`Refine`
stage: `intake record -> refinery packet`, feeding directly into `Verify`),
`Architecture.md` line 41-52 (`CVF_TRUTH_FLOW -> CVF_TRUTH_KERNEL -> Governance
Runtime`), `TRUTH_FLOW_DOCTRINE.md` line 10 ("Refinement improves usability"),
`CLAIM_BOUNDARY.md` line 3 ("refinery structure" is an allowed claim), and the
embedded `refinery-engine.ts`/`REFINERY_SPEC.md` implementation. This is six
independent, internally-consistent Flow documents, not one ambiguous diagram.

Resolution and reasoning: Two packages (Refinery, Kernel) independently and
unanimously describe a topology that excludes Flow from any pre-Kernel role.
One package (Flow) unanimously describes the opposite, including within its own
package. This is a genuine 2-versus-1 cross-package conflict, not noise. T0R
sides with the 2-package consensus for four source-backed reasons: (1) Refinery
and Kernel's positions require no rewrite of anything outside Flow to remain
correct, while Flow's position would require dismantling and rebuilding an
entire dedicated Refinery layer's worth of already-well-specified doctrine; (2)
Flow's own embedded refinery is measurably weaker than dedicated Refinery
(Axis-3 evidence: no scope/time-overlap conflict preconditions); (3) a
dedicated Refinery layer already exists as a complete, coherent, independently
addressable package - Occam's razor favors not duplicating it; (4) the
`REFINERY_BOUNDARY_SPEC.md` document is titled and structured as the
authoritative cross-package boundary contract, while Flow's conflicting claims
appear only within Flow's own single-package documentation, never citing or
reconciling against the boundary spec.

Claim update: REVISED. The dispatcher's `THREE_LAYER_MODEL_CONFIRMED` premise
survives, but the specific sub-claim that Flow's own documented topology is
merely "ambiguous" is revised to "actively contradictory, resolved against
Flow's pre-Kernel claim." Flow's embedded refinery (spec, schema, 5 source
files, 1 test - REJECT-confirmed in the companion matrix) must be retired as
part of this resolution. Two extracted primitives (`DERIVED_ENRICHMENT`,
`STRUCTURAL_ONLY_NOT_TRUTH_APPROVAL` claim tags) may be adapted into the
canonical Refinery or a shared claim-boundary utility.

### Axis 6 - Empty evidence

**Recommendation: `FAIL_CLOSED_REQUIRED`.**

Evidence for: `VERIFICATION_GATE_SPEC.md` line 33 explicitly requires STRICT
mode to block on missing evidence; `CVF_TRUTH_KERNEL_DOCTRINE.md` line 27-29
"fail-stop beats fail-silent"; `CVF_REFINERY_DOCTRINE.md` line 35-37 fail-closed
principle; the absorbed source doctrine in
`AGENT_HARNESS_FAIL_STOP_MAP.md` line 10-11 names fail-silent as the dangerous
failure mode this entire corpus was built to prevent.

Evidence against: none found in doctrine. The only "evidence against" is
behavioral: every reference implementation, one official quickstart example,
and one committed unit test currently treat the empty-collection case as
passing, which shows the gap is real and pervasive, not that it is intentional
or desirable.

Required invariant, stated precisely from the evidence: a Refinery packet must
not reach `READY_FOR_KERNEL` when zero pipeline stages executed (close the
`TRANSFORMATION_LINEAGE_SPEC.md` "required lineage" vacuous-truth gap and add a
`REFINERY_NO_STAGES_EXECUTED`-class failure token); a Kernel receipt must not
report `status: 'pass'` when `verification_results` is empty; a Kernel STRICT
gate must not return `allowed: true` when `results` is empty.

Claim update: CONFIRMED and elevated from "code defect" to "doctrine
requirement the code fails to meet," based on the direct textual citation in
`VERIFICATION_GATE_SPEC.md` line 33.

### Axis 7 - Contract chain

**Recommendation: `ONE_CANONICAL_CHAIN`.**

Evidence for: `REFINERY_PACKET_SPEC.md` defines the sole canonical Refinery-to-
Kernel handoff; `docs/reference/refinery/README.md` and
`EXTENSIONS/CVF_REFINERY/README.md` both describe a single, linear
`Raw -> Refinery -> Packet -> Kernel -> verified/reject/escalate -> Flow ->
business application` chain with no branching or versioned-adapter language
anywhere in the Refinery or Kernel documentation.

Evidence against `MULTIPLE_VERSIONED_CONTRACTS_WITH_ADAPTER`: this alternative
was considered and rejected. It would functionally preserve Flow's incompatible
packet as a permanently-supported "version," institutionalizing the exact
duplication this recommendation identifies as the core defect. No source
document proposes or requires multiple concurrent packet contracts.

Claim update: REVISED from the roadmap's neutral framing (which listed
`MULTIPLE_VERSIONED_CONTRACTS_WITH_ADAPTER` as an equally allowed value) to a
specific recommendation against it, with reasoning.

### Axis 8 - Implementation readiness

**Recommendation: `BLOCKED_MISSING_DECISION`.**

Three architecture decisions require CVF reviewer ratification before any
implementation tranche (SOT3-T1 or later) may begin: (1) Axis 5, Flow topology
- retire the embedded refinery and adopt post-Kernel-only; (2) Axis 6, the
fail-closed empty-evidence invariant across all three layers; (3) Axis 7, one
canonical packet/receipt/reference contract chain, explicitly rejecting
Flow's competing packet. Until these three are ratified, no contract, schema,
guard, or runtime work has a stable target to build against.

`IMPLEMENTATION_READY` is not used, per work order constraint and because the
evidence itself does not support it: even after the three decisions are
ratified, no contract-test suite, adapter, or CVF-native rewrite exists yet.

Claim update: BLOCKED, consistent with T0's roadmap-level `NOT_AUTHORIZED`
posture, now stated as a decision-axis blocker rather than a general caution.

## Strongest Alternative Architecture

`FLOW_AS_FACADE_PLUS_POST_KERNEL_MODULE`

This is the strongest alternative to `POST_KERNEL_ONLY`, and it is presented
even though the primary recommendation rejects it, per the work order's dissent
requirement.

```text
Governed Intake Adapter (new, thin)
  -> SourceEnvelope
  -> CVF Refinery Core (mandatory ordered stages; fail-closed)
  -> RefineryPacket
  -> CVF Truth Kernel (fail-closed; content-bound receipt)
  -> TruthReference
  -> CVF Truth Flow FACADE (orchestration entrypoint only - no logic)
       delegates intake to Governed Intake Adapter
       delegates refinement to CVF Refinery Core
       delegates verification to CVF Truth Kernel
  -> CVF Truth Flow POST-KERNEL MODULE (routing, dose, distribution,
       consumption, observation, feedback, retirement - unchanged from primary)
  -> Business Application
```

Rationale for considering it: this reading takes Flow's own claim
("orchestration layer for the complete lifecycle," `EXTENSIONS/CVF_TRUTH_FLOW/
README.md` line 3) at face value instead of overriding it, and it would let
existing Flow-side integration points (anything that currently calls into
`CVF_TRUTH_FLOW` as its single entrypoint) keep working, with the facade
purely delegating rather than re-implementing.

Rationale for rejecting it as primary: the facade adds an indirection layer
with no independent value once Refinery and Kernel are called directly - it
would exist purely to preserve Flow's naming primacy, not to solve a
functional problem no other layer already solves. It requires maintaining a
delegation surface that must be kept in lockstep with two other layers'
contracts, doubling maintenance burden for zero new capability. The
`REFINERY_BOUNDARY_SPEC.md` cross-package contract (the most authoritative
single document on this exact question) does not describe or allow a facade
role for Flow. No source document proposes this facade pattern; it is
constructed here specifically to be the strongest available alternative, not
because retained evidence supports it over the primary recommendation.

Verdict: primary recommendation (`POST_KERNEL_ONLY`) retained after
considering the alternative.

## Producer/Consumer Packet And Receipt Mapping

| Contract | Producer | Consumer | Canonical fields (recommended) | Current incompatible variant to retire |
|---|---|---|---|---|
| `SourceEnvelope` | Governed Intake Adapter | CVF Refinery | `source_id, source_type, owner, captured_at, scope, purpose, confidentiality, content_hash, raw_reference` (per `SOURCE_ENVELOPE_SPEC.md`) | Flow `attach-source.ts` `SourceAttachment`/`IntakeRecord` (REJECT) |
| `RefineryPacket` | CVF Refinery | CVF Truth Kernel | `refinery_packet_id, source_envelopes, normalized_records, duplicate_groups, conflict_sets, quality_findings, integrity_results, transformation_lineage, declared_scope, declared_owner, rule_manifest, status, failure_tokens, created_at` (per `REFINERY_PACKET_SPEC.md`) | Flow `refinery-engine.ts` `RefineryPacket` (`packetId`, camelCase, `READY_FOR_VERIFICATION`) (REJECT) |
| Kernel adapter response | CVF Truth Kernel adapter | CVF Refinery | `ACCEPT_EVIDENCE_CANDIDATE \| REJECT \| ESCALATE \| REQUIRE_ADDITIONAL_EVIDENCE` (per `CVF_REFINERY_BINDING_SPEC.md`) | none identified |
| `TruthPacket` | CVF Refinery / evaluation adapter | CVF Truth Kernel | per `truth.packet.schema.json`, tightened to `additionalProperties: false` or an explicit extension point | current open schema (`additionalProperties: true`) - ADAPT, not REJECT |
| `TruthReceipt` | CVF Truth Kernel | CVF Truth Flow, CVF guards | per `truth-receipt.ts` structure, with hash bound to full evaluated packet content, not receipt metadata only; `status` must not be `pass` on empty `verification_results` | current receipt (fail-open, metadata-only hash) - ADAPT |
| `TruthReference` | CVF Truth Kernel | CVF Truth Flow | scoped, versioned, time-bounded, supersession-aware (roadmap design label; no current runtime symbol found) | none identified; new contract |
| `DistributionPackage` | CVF Truth Flow | governed consumer | must include a bound `TruthReceipt` reference per `CONTEXT_DISTRIBUTION.md` line 3, not a caller-supplied boolean | `publish-gate.ts` `PublishGateInput.truthKernelAccepted: boolean` - ADAPT |
| `FeedbackProposal` | CVF Truth Flow | human or governed owner | proposal-only; a `source_score` change must require an approved proposal per `FEEDBACK_LOOP.md` line 5-7 | `source-score.ts` `updateSourceScore()` direct mutation - ADAPT |

## Capability Absorption Matrix (Refreshed)

| Capability group | Value | Owner candidate | Disposition |
|---|---|---|---|
| Three-layer separation doctrine (prepare / evaluate / distribute) | high | SOT3-T2 contract family | ABSORB |
| Refinery deterministic primitives (envelope, normalize, dedupe, conflict, quality, integrity, lineage) | high after fail-closed rewrite | SOT3-T3 Refinery Core | ADAPT |
| Refinery no-AI Core invariant | high governance value | SOT3-T3 | ABSORB (invariant); ADAPT (enforcement) |
| Kernel provenance/evidence/obligation/verification/receipt doctrine | high | SOT3-T4 Kernel | ABSORB |
| Kernel receipt/gate/schema implementation | high after fail-closed and content-binding rewrite | SOT3-T4 | ADAPT |
| Flow post-Kernel lifecycle (route, dose, distribute, consume, observe, recall, retire) | high; largely novel to CVF | SOT3-T5 Flow | ADAPT |
| Flow embedded refinery (spec, schema, 5 source files, 1 test) | negative; integration-risk evidence, weaker algorithm than dedicated Refinery | none | REJECT |
| `DERIVED_ENRICHMENT` / `STRUCTURAL_ONLY_NOT_TRUTH_APPROVAL` claim-tag pattern | medium; novel cross-cutting discipline pattern | future shared claim-boundary utility owner | ADAPT (extract from otherwise-rejected files) |
| Kernel `evidence approval status` STRICT requirement | medium; currently undocumented gap in gate code | SOT3-T4 | ADAPT (new hardening item, not previously ledgered) |
| Prototype guards, checkers, negative-case tests | medium | future checker owner decision | DEFER |
| Tests, scripts, config, examples across all layers | supporting only | re-author after contract ratification | DEFER |
| Kernel external-knowledge-absorption maps (4 files) | context/provenance only | CVF governance-learning lane, not SOT architecture | NO_NEW_VALUE for SOT3 scope; DEFER to a separate knowledge-absorption review |

## Overlap And Current CVF Owner Status

| Item | Current CVF owner status |
|---|---|
| General truth doctrine (evidence/obligation/provenance/verification/receipt) | ENRICH_EXISTING - `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` is narrower than the retained corpus |
| Skill-specific truth packet | ENRICH_EXISTING - `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` is a vertical slice, not general proof |
| General Refinery Core | OWNER_SURFACE_NOT_FOUND - confirmed again this tranche; no current CVF owner |
| Post-Kernel Flow lifecycle | OWNER_SURFACE_NOT_FOUND - confirmed again this tranche; no current CVF owner |
| Receipt binding | REJECT_DIRECT_IMPORT - `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts` is a workflow-step obligation contract, semantically unrelated |

## Remaining Blockers Before Implementation

1. CVF reviewer must ratify or revise Axis 5 (Flow topology) - this is the
   single highest-leverage decision, since it determines whether an entire
   Flow-side module (embedded refinery: 1 spec, 1 schema, 5 source files, 1
   test) is retired or rebuilt around.
2. CVF reviewer must ratify the fail-closed empty-evidence invariant (Axis 6)
   as a cross-layer contract-test requirement before SOT3-T3/T4/T5 begin.
3. CVF reviewer must ratify one canonical packet/receipt/reference contract
   chain (Axis 7) so SOT3-T2 has a single, non-branching target.
4. No current CVF owner exists for the general Refinery or Flow-lifecycle
   modules; SOT3-T1 (not yet authorized) is the appropriate lane to either
   create these owners or fold them into an existing surface.
5. No contract-test suite exists yet for the fail-closed invariants identified
   in this tranche; this is new work for a future SOT3-T3/T4 tranche, not
   something this recommendation can close.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| reviewer treats Axis 5 as already settled by T0 | this recommendation explicitly revises T0's "ambiguity" framing to "contradiction resolved against Flow's pre-Kernel claim," with citation-backed reasoning that must be independently checked |
| alternative architecture read as a soft recommendation | the alternative is stated as genuinely strongest-available and is explicitly rejected with reasons, not left ambiguous |
| fail-closed fix treated as one guard clause | the fix requires closing a taxonomy gap (no zero-stage failure token) and a definitional gap (vacuous "required lineage"), in both Refinery and Kernel, plus a narrower RELAXED-mode fix |
| Flow's embedded refinery treated as pure waste | two claim-tag primitives are called out for extraction before the surrounding code is discarded |

## Decision / Disposition

Recommendation disposition: `COMPLETE_PENDING_REVIEW`. All eight decision axes
are resolved with citations and dissent. The primary recommendation is
`THREE_LAYER_MODEL_CONFIRMED_TOPOLOGY_REVISED_CONTRACT_REWRITE_REQUIRED`,
Flow topology is revised to `POST_KERNEL_ONLY`, and implementation readiness is
`BLOCKED_MISSING_DECISION`. This recommendation does not ratify architecture;
the CVF reviewer decides whether to accept, revise, or reject each axis.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | committed advisory evidence -> T0R architecture decision recommendation -> CVF reviewer decision -> later fresh implementation tranche if authorized |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_work_order_dispatch_quality.py` |
| Owner surface | this recommendation for architecture proposal; CVF reviewer for acceptance |
| Disposition | ADAPT through source-backed recommendation |
| Claim boundary | external recommendation is not CVF authority |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | External Absorption Core; External Absorption Value Conversion Matrix; Overlap And Novelty Classification; Corpus Completeness And Report Integrity; COMPLETE_PENDING_REVIEW; NOT_AUTHORIZED; BLOCKED_MISSING_DECISION |
| gateRunPurpose | confirm exact recommendation shape after checker source review |
| claimBoundary | checker-shape conformance does not decide architecture correctness |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction (per work order baseline): three layers remain
valuable, with Refinery independent/no-AI, Kernel sole trust authority, and
Flow post-Kernel.

Evidence Comparison Requirement: this prediction was tested against 61
documentation files and all previously-disputed source. Axes 1, 2, 3, 4, 6
confirm the prediction directly. Axis 5 confirms the prediction's conclusion
(Flow post-Kernel) only after actively overriding Flow's own six-document
self-description, which asserts the opposite.

Contradiction Handling Requirement: the contradiction is not hidden. It is
named as a genuine 2-versus-1 cross-package conflict in Axis 5, with the
strongest alternative architecture presented and explicitly rejected rather
than the conflict being resolved by silent selection.

Claim Update Requirement: dispatcher verdict marked CONFIRMED for axes 1-4 and
6; REVISED for axis 5 (topology) and axis 7 (contract chain, narrowed away from
the permissive multi-contract option); BLOCKED for axis 8 (implementation
readiness), consistent with but more specific than T0's general
`NOT_AUTHORIZED` posture.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private retained source and pre-implementation architecture decision
work.

## Claim Boundary

This recommendation proposes one primary architecture and one strongest
alternative with explicit reasoning for each of the eight decision axes. It
does not authorize implementation, package activation, contract ratification,
provider/live proof, public-sync, commit, release, or production readiness.
Implementation readiness is `BLOCKED_MISSING_DECISION`; `IMPLEMENTATION_READY`
is not used anywhere in this artifact.
