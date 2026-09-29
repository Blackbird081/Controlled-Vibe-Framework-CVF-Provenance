# CVF SOT3-T1 Owner And Novelty Map

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

docType: review_context

Date: 2026-07-12

Map ID: SOT3-T1-OWNER-MAP

## Purpose

Produce a complete, source-backed current-CVF owner and novelty decision for
every capability group accepted in the T0R Capability Absorption Matrix
(`docs/reviews/CVF_SOT3_T0R_THREE_LAYER_ARCHITECTURE_DECISION_RECOMMENDATION_2026-07-12.md`),
before any canonical contract (SOT3-T2) or implementation tranche. This map
does not create an owner surface; it recommends one terminal owner-decision
token per capability for CVF reviewer acceptance.

## Target / Source

- Input: `docs/reviews/CVF_SOT3_T0R_THREE_LAYER_ARCHITECTURE_DECISION_RECOMMENDATION_2026-07-12.md`,
  section `## Capability Absorption Matrix (Refreshed)` (12 rows).
- Current CVF owner roots searched: `docs/reference`, `EXTENSIONS`, `governance`,
  schema files (`*.json` under `EXTENSIONS`), test files (`*.test.ts` under
  `EXTENSIONS`), and `docs/corpus-intelligence/registry/entries/`.
- Dependency: T0R material closure `ae7d53385`
  (`docs/reviews/CVF_SOT3_T0R_COMPLETION_REVIEW_2026-07-12.md`,
  Disposition `REVIEWER_ACCEPTED_BOUNDED`).

## Scope / Methodology

For each of the 12 accepted capability groups: searched current CVF
`docs/reference`, `EXTENSIONS` (`.ts`, `.md`, `.json`), `governance`, and the
corpus-intelligence registry for an existing owner; recorded the exact path,
section, or symbol found; distinguished path existence from actual semantic
ownership (a matching file or token does not by itself prove the same
responsibility); ran a negative search for every candidate before proposing
`NEW_OWNER_CANDIDATE`; and assigned exactly one terminal owner-decision token
per capability. No file hashing was repeated; no retained source was read
beyond what T0R already cited.

## Findings / Position

All 12 accepted T0R capability groups received a source-backed terminal
owner-decision token this tranche. The most significant finding is that
`docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md`
(TKG-T1, committed 2026-06-28, predating SOT3) already independently absorbs
general Truth Kernel doctrine and already `REJECT_DIRECT_IMPORT`s the
retained Kernel's strict-mode runtime code (Source Conversion Matrix line
63), reaching the same runtime-reject conclusion SOT3-T0/T0R reached
independently via the empty-evidence fail-open finding. This elevates CAP-04
and CAP-09 to `ENRICH_EXISTING_OWNER` rather than `NEW_OWNER_CANDIDATE`.
CAP-01, the three-module topology itself, remains a `NEW_OWNER_CANDIDATE`
with TKG-T1 recorded only as its upstream doctrine dependency (see CAP-01
below). All four mandatory negative-search tokens
(`RefineryPacket`, `TruthReceipt`/receipt binding, `TruthReference`,
`Truth Flow`/post-Kernel) returned zero matches across `docs/reference`,
`EXTENSIONS`, and `governance`, except the receipt-binding same-token
collision, which was opened and field-compared and confirmed as a different
owner (workflow-step receipt, not truth-verification receipt). No capability
required `BLOCKED_MISSING_OWNER_EVIDENCE`.

## Capability Key Inventory (12/12)

Stable keys, extracted in the exact row order of the T0R Capability
Absorption Matrix:

| # | Capability key | T0R row (verbatim capability group text) |
|---|---|---|
| CAP-01 | `three_layer_separation_doctrine` | Three-layer separation doctrine (prepare / evaluate / distribute) |
| CAP-02 | `refinery_deterministic_primitives` | Refinery deterministic primitives (envelope, normalize, dedupe, conflict, quality, integrity, lineage) |
| CAP-03 | `refinery_no_ai_core_invariant` | Refinery no-AI Core invariant |
| CAP-04 | `kernel_provenance_evidence_obligation_verification_receipt_doctrine` | Kernel provenance/evidence/obligation/verification/receipt doctrine |
| CAP-05 | `kernel_receipt_gate_schema_implementation` | Kernel receipt/gate/schema implementation |
| CAP-06 | `flow_post_kernel_lifecycle` | Flow post-Kernel lifecycle (route, dose, distribute, consume, observe, recall, retire) |
| CAP-07 | `flow_embedded_refinery` | Flow embedded refinery (spec, schema, 5 source files, 1 test) |
| CAP-08 | `derived_enrichment_structural_only_claim_tag_pattern` | `DERIVED_ENRICHMENT` / `STRUCTURAL_ONLY_NOT_TRUTH_APPROVAL` claim-tag pattern |
| CAP-09 | `kernel_evidence_approval_status_strict_requirement` | Kernel `evidence approval status` STRICT requirement |
| CAP-10 | `prototype_guards_checkers_negative_case_tests` | Prototype guards, checkers, negative-case tests |
| CAP-11 | `tests_scripts_config_examples` | Tests, scripts, config, examples across all layers |
| CAP-12 | `kernel_external_knowledge_absorption_maps` | Kernel external-knowledge-absorption maps (4 files) |

## Negative Search And Collision Discipline

All four mandatory searches were executed exactly as specified in the work
order, across `docs/reference`, `EXTENSIONS` (`.ts` and `.md`), and
`governance`.

| Search token | Command | Matches found | Same-token collision result | Disposition |
|---|---|---|---|---|
| `RefineryPacket` | `rg -n "RefineryPacket" docs/reference EXTENSIONS governance` | 0 in `docs/reference`; 0 in `EXTENSIONS` (`.ts`, `.md`, `.json`); 0 in `governance` | none | ABSENT_CONFIRMED |
| `TruthReceipt` / receipt binding | `rg -n "TruthReceipt\|truth receipt\|receipt binding" docs/reference EXTENSIONS governance` | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` line 147 ("truth receipts"); `docs/reference/archive/CVF_LHW2_MEMORY_EVENT_CAPTURE_WORKFLOW_RECEIPT_LOOP_CONNECTOR_SPEC_2026-05-27.md`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/contracts.phaseE-receipt-binding.test.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | `receipt-binding.contract.ts` defines `StepReceiptObligation`/`StepReceiptEmission`/`StepReceiptBindingResult` (lines 31-60), keyed by `workflowId`/`stepId`/`role`/`actionClass`, bound to `WorkflowStepExecutionTrace` - a workflow-step execution receipt, not a truth-evaluation receipt (`evidence_ids`/`obligation_ids`/`verification_results`/hash chain). The skill-packet's "truth receipts" (line 147) is a generic phrase for its own `receipt: {hash: sha256:...}` metadata field, not the retained corpus's `TruthReceipt` shape. | COLLISION_REVIEWED_NOT_SAME_OWNER |
| `TruthReference` | `rg -n "TruthReference\|truth reference" docs/reference EXTENSIONS governance` | 0 in `docs/reference`; 0 in `EXTENSIONS` (`.ts`); 0 in `governance` | none | ABSENT_CONFIRMED |
| `Truth Flow` / post-Kernel / distribution lifecycle | `rg -n "Truth Flow\|post-Kernel\|distribution lifecycle" docs/reference EXTENSIONS governance` | 0 in `docs/reference`; 0 in `EXTENSIONS` (`.ts`); 0 in `governance` | none | ABSENT_CONFIRMED |

Additional targeted searches performed for capabilities without a dedicated
mandatory token:

| Search token | Roots | Matches | Disposition |
|---|---|---|---|
| `DERIVED_ENRICHMENT`, `STRUCTURAL_ONLY_NOT_TRUTH_APPROVAL` | `docs/reference`, `EXTENSIONS` (`.ts`) | 0 | ABSENT_CONFIRMED |
| `claim-boundary utility`, `shared claim boundary` | `docs/reference` | 0 | ABSENT_CONFIRMED |
| `no-truth-claim`, `refinery-boundary`, `refinery-packet-required` (retained-corpus guard names) | `EXTENSIONS` (`.ts`) | 0 | ABSENT_CONFIRMED |
| evidence approval status / approved evidence STRICT | `docs/reference/truth_foundation` | 0 exact-phrase match; doctrine-level analog found (see CAP-09) | SEE_CAP_09 |
| `sot3` | `docs/corpus-intelligence/registry/entries/` | 1 (`sot3-t0-retained-three-layer-advisory-scan.json`); no T1-level owner-decision entry exists | NO_PRIOR_T1_DECISION |

A same-token or same-word match is never treated as ownership proof by
itself; every match above was opened and compared field-by-field or
concept-by-concept before a disposition was assigned.

## Owner And Novelty Decisions (12/12)

### CAP-01: three_layer_separation_doctrine

- **Current owner search:** `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md`
  (TKG-T1), Purpose (line 17-20): the contract states it absorbs useful Agent
  Governance Toolkit and Truth Kernel doctrine without copying external code,
  without adopting external distributable runtime components, and without
  creating a parallel evidence or truth system.
  Governing chain (line 22-26): `source authority -> provenance label ->
  evidence or obligation record -> verification result -> bounded claim
  movement` - a single-chain doctrine, not the three-module topology CAP-01
  itself names.
- **Path-versus-semantic-ownership distinction:** TKG-T1 is a real, dated,
  committed reference contract (2026-06-28, predates SOT3), not a
  coincidental filename match, and it is a genuine upstream doctrine
  dependency for CAP-01. But TKG-T1 does not define or own an independent
  Refinery module, the Refinery-to-Kernel boundary, a post-Kernel Flow
  module, the three-module responsibility split, or the canonical
  cross-layer topology accepted by T0R; it also explicitly keeps Truth
  Kernel runtime, SOT index runtime, verifier service, and monitor out of
  scope. TKG-T1's Source Conversion Matrix (line 55-63) converting "Truth
  Kernel doctrine" and `REJECT_DIRECT_IMPORT`-ing the "Truth Kernel
  strict-mode package code" is evidence for the CAP-04/CAP-09 doctrine
  ownership below, not for CAP-01's module-topology ownership.
- **Same-token collisions:** none beyond the confirmed TKG-T1 dependency
  relationship.
- **Terminal owner decision: `NEW_OWNER_CANDIDATE`** for a CVF-owned SOT
  three-layer architecture/contract family (independent Refinery prepares,
  Kernel evaluates trust, post-Kernel Flow distributes and manages
  lifecycle). TKG-T1 is recorded as an `ENRICH_EXISTING_OWNER` dependency
  and upstream doctrine owner for the underlying governing chain, not as the
  owner of CAP-01's three-module topology itself.
- **Novelty / delta:** the three-module boundary split (independent
  Refinery, Kernel, post-Kernel Flow) is the core SOT3 delta and is not
  present in TKG-T1's single governing chain; TKG-T1 supplies upstream
  doctrine that a future three-layer architecture owner should build on, not
  a pre-existing owner of that architecture.

### CAP-02: refinery_deterministic_primitives

- **Current owner search:** zero matches for `RefineryPacket` (mandatory
  search) across all three roots; targeted search for
  `source-envelope|normalize-record|duplicate-group|conflict-set` also
  returned zero in `docs/reference` and `EXTENSIONS` `.ts`.
- **Path-versus-semantic-ownership distinction:** N/A - no path exists to
  distinguish from ownership.
- **Same-token collisions:** none.
- **Terminal owner decision: `NEW_OWNER_CANDIDATE`** (negative search
  confirmed absent; no current CVF surface owns source-envelope,
  normalization, duplicate-grouping, conflict-detection, quality, integrity,
  or lineage primitives as a bundled deterministic preparation module).

### CAP-03: refinery_no_ai_core_invariant

- **Current owner search:** zero matches for Refinery-specific tokens
  (see CAP-02). TKG-T1's "LLM Output Is Not Self-Trusting" section
  (line 106-117) states a related but more general principle (LLM must not
  be the sole verifier for hard claims), not a no-AI-in-preparation-module
  invariant specific to a deterministic intake layer.
- **Path-versus-semantic-ownership distinction:** TKG-T1's LLM-boundary
  doctrine is real and CVF-owned, but it governs verification, not
  preparation; the no-AI Core invariant is a narrower, preparation-specific
  rule that TKG-T1 does not state.
- **Same-token collisions:** none.
- **Terminal owner decision: `NEW_OWNER_CANDIDATE`** for the invariant as a
  standalone Refinery-scoped rule, with `ENRICH_EXISTING_OWNER` noted as a
  secondary relationship to TKG-T1's general LLM-boundary doctrine (see
  Overlap table below).

### CAP-04: kernel_provenance_evidence_obligation_verification_receipt_doctrine

- **Current owner search:** `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md`,
  Evidence Record Minimum (line 171-195), Obligation Record Minimum
  (line 197-222), Verification Result Minimum (line 224-257), Provenance
  Label Contract (line 137-169). These four sections directly cover the same
  four doctrine areas as the retained Kernel's Evidence Registry, Obligation
  Registry, Provenance Label, and Independent Verifier specs.
- **Path-versus-semantic-ownership distinction:** field-level comparison
  confirms real overlap, not a coincidental heading match: TKG-T1's evidence
  record minimum (`evidence_id`, `source_type`, `provenance_label`,
  `validity_boundary`, `status`) and the retained `EVIDENCE_REGISTRY_SPEC.md`
  required fields (`evidence_id`, `type`, `status`, `approved_by`,
  `valid_from`/`valid_until`) cover materially the same concept with
  different field names.
- **Same-token collisions:** the retained corpus's `TruthReceipt` runtime
  shape is not covered by TKG-T1 (TKG-T1 is doc-only, no receipt hash-chain
  field minimum) - see CAP-05 for the receipt-specific gap.
- **Terminal owner decision: `ENRICH_EXISTING_OWNER`** -
  `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md`,
  Evidence/Obligation/Verification Result Minimums and Provenance Label
  Contract sections.
- **Novelty / delta:** TKG-T1 lacks a receipt/hash-chain field minimum and a
  `SOT_INDEX_SPEC`-equivalent reference-map contract; these are gaps to
  reconcile in a future TKG-T2-style tranche, not new CVF owners.

### CAP-05: kernel_receipt_gate_schema_implementation

- **Current owner search:** TKG-T1 Source Conversion Matrix line 63:
  "Truth Kernel strict-mode package code | runtime candidate shows incomplete
  spec alignment | direct import rejected until future source-verified
  tranche | `REJECT_DIRECT_IMPORT`." TKG-T1 itself already rejected importing
  the retained Kernel's runtime gate/receipt code, independently of SOT3.
  No current CVF runtime implements a verification gate, receipt hash-chain,
  or truth-packet schema.
- **Path-versus-semantic-ownership distinction:** TKG-T1 owns the *doctrine*
  language (CAP-04) but explicitly does not own or contain a runtime
  implementation; `receipt-binding.contract.ts` (Guard Contract) is a
  workflow-step receipt, not a truth-verification receipt (see collision
  table above) and is not a candidate owner for this runtime.
- **Same-token collisions:** `receipt binding` collision reviewed and
  rejected as the same owner (see Negative Search table).
- **Terminal owner decision: `NEW_OWNER_CANDIDATE`** for the runtime
  implementation (gate logic, receipt hash-chain, schema); doctrine already
  has an `ENRICH_EXISTING_OWNER` via CAP-04.

### CAP-06: flow_post_kernel_lifecycle

- **Current owner search:** zero matches for "Truth Flow", "post-Kernel", or
  "distribution lifecycle" (mandatory search) across all three roots.
  Targeted search for `information-dose|routing-policy|distribution-package`
  also returned zero in `docs/reference` and `EXTENSIONS` `.ts`.
- **Path-versus-semantic-ownership distinction:** N/A - no path exists.
- **Same-token collisions:** none.
- **Terminal owner decision: `NEW_OWNER_CANDIDATE`** (negative search
  confirmed absent; no current CVF surface owns post-Kernel routing, dose
  control, distribution, consumption, observation, recall, or retirement as a
  bundled lifecycle module).

### CAP-07: flow_embedded_refinery

- **Current owner search:** this capability was disposed `REJECT` by T0R
  itself (negative value; integration-risk evidence, weaker algorithm than
  dedicated Refinery). No owner search is required for a rejected item, per
  the work order's Fail Conditions ("path existence treated as ownership
  proof" is the failure to avoid, not a requirement to search for an owner of
  something already rejected). A confirmatory check found zero current CVF
  reference to the specific incompatible packet fields (`packetId`,
  `intakeId`, `normalizedPayload`) that would indicate accidental import.
- **Path-versus-semantic-ownership distinction:** N/A.
- **Same-token collisions:** covered by the `RefineryPacket` mandatory search
  (zero matches; the retained Flow-embedded packet's distinct field names
  were also independently confirmed absent from current CVF).
- **Terminal owner decision: `REJECT_DIRECT_IMPORT`** (T0R disposition
  reconfirmed; no current CVF surface risks accidental collision).

### CAP-08: derived_enrichment_structural_only_claim_tag_pattern

- **Current owner search:** zero matches for `DERIVED_ENRICHMENT` or
  `STRUCTURAL_ONLY_NOT_TRUTH_APPROVAL` in `docs/reference` or `EXTENSIONS`
  `.ts`. Targeted search for "claim-boundary utility" and "shared claim
  boundary" also returned zero.
- **Path-versus-semantic-ownership distinction:** N/A - no path exists. CVF
  does have many individual `Claim Boundary` sections as a documentation
  convention (used throughout this very map), but no single shared runtime
  or schema primitive that tags a value as derived-versus-original or
  structural-only-versus-truth-approved at the type level.
- **Same-token collisions:** none.
- **Terminal owner decision: `SHARED_PRIMITIVE_CANDIDATE`** (this is a
  small, cross-cutting typing pattern rather than a capability that needs its
  own module; it is a candidate for extraction into an existing or future
  shared utility rather than a standalone new owner).

### CAP-09: kernel_evidence_approval_status_strict_requirement

- **Current owner search:** `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md`,
  Label semantics table (line 156-166): `MISSING_EVIDENCE` "blocks strict
  movement" (line 164); Claim Movement Semantics (line 266-268): "Strict
  movement must block on: missing hard evidence... missing hard-obligation
  verification."
- **Path-versus-semantic-ownership distinction:** TKG-T1's blocking rule is a
  doctrine-level generalization of the retained Kernel's specific
  `EVIDENCE_REGISTRY_SPEC.md` rule ("Only approved evidence may be used in
  STRICT verification," line 51 in the retained spec per T0R matrix row 20).
  No current CVF runtime or checker enforces either version; the ownership at
  this stage is doctrinal only.
- **Same-token collisions:** none found for the exact retained-spec field
  name (`status: approved`).
- **Terminal owner decision: `ENRICH_EXISTING_OWNER`** -
  `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md`,
  Label Semantics and Claim Movement Semantics sections. The specific
  approved-status field-level requirement remains an unreconciled delta for
  a future TKG-T2-style field reconciliation tranche.

### CAP-10: prototype_guards_checkers_negative_case_tests

- **Current owner search:** this capability was disposed `DEFER` by T0R with
  owner candidate "future checker owner decision." A search for
  `no-truth-claim|refinery-boundary|refinery-packet-required` (retained guard
  names) confirmed zero current CVF guards under those names.
- **Path-versus-semantic-ownership distinction:** N/A - no path exists; T0R
  already correctly deferred this rather than claiming a false owner.
- **Same-token collisions:** none.
- **Terminal owner decision: `DEFER_WITH_REOPEN_CONDITION`** (see Value
  Conversion Ledger for the exact reopen condition).

### CAP-11: tests_scripts_config_examples

- **Current owner search:** T0R disposed this `DEFER` ("re-author after
  contract ratification"). No owner search applies to generic
  supporting-artifact classes; this decision follows T0R's own disposition
  directly.
- **Path-versus-semantic-ownership distinction:** N/A.
- **Same-token collisions:** none.
- **Terminal owner decision: `DEFER_WITH_REOPEN_CONDITION`** (see Value
  Conversion Ledger for the exact reopen condition).

### CAP-12: kernel_external_knowledge_absorption_maps

- **Current owner search:** these 4 files
  (`SOT_KERNEL_MAP.md`, `AGENT_HARNESS_FAIL_STOP_MAP.md`,
  `MICROSOFT_AGENT_GOVERNANCE_TOOLKIT_MAP.md`,
  `SANTANDER_MECHANICAL_GOVERNANCE_MAP.md`) were disposed
  `NO_NEW_VALUE for SOT3 scope` by T0R; their content is provenance/context
  for CVF's own knowledge-absorption learning lane, already addressed by
  TKG-T0/TKG-T1's own external-absorption pattern (the CVF chain map at
  `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md`).
- **Path-versus-semantic-ownership distinction:** the CVF chain map is a
  process owner (how external absorption is routed), not a content owner for
  these four specific maps' subject matter.
- **Same-token collisions:** none.
- **Terminal owner decision: `NO_NEW_VALUE`** (confirmed; no SOT3-specific
  owner action required; any future action on these 4 files belongs to a
  separate, non-SOT3 knowledge-absorption review, consistent with T0R).

## Overlap And Novelty Classification (Refreshed For T1)

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| Truth-foundation doctrine (CAP-04, CAP-09) | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` | `ENRICH_EXISTING_OWNER` | TKG-T1 already absorbs the general doctrine (source authority, integrity-is-not-truth, LLM-not-self-trusting, evidence/obligation/verification minimums, provenance labels); SOT3's delta is the receipt hash-chain/SOT-index field gaps | field-level reconciliation in a future TKG-T2-style tranche, not a new owner |
| Three-layer architecture topology (CAP-01) | `docs/reference/truth_foundation/CVF_TRUTH_FOUNDATION_SOURCE_PROVENANCE_AND_VERIFICATION_CONTRACT.md` (dependency only, not owner) | `NEW_OWNER_CANDIDATE` | TKG-T1's single governing chain is an upstream doctrine dependency, not an owner of the independent Refinery/Kernel/post-Kernel-Flow module split; the three-module boundary is the SOT3 delta itself | recommend a CVF-owned SOT three-layer architecture/contract family; reviewer decides whether/when to create |
| Skill-specific truth packet | `docs/reference/agent_system_skills/CVF_SKILL_SOURCE_OF_TRUTH_PACKET_STANDARD.md` | vertical owner, not general | confirmed narrower via its own Claim Boundary section, which limits scope to six existing runtime-eligible ASSF-registered skill roots | preserve compatibility; not a candidate general-truth owner |
| Receipt binding (Guard Contract) | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts` | `REJECT_DIRECT_IMPORT` confirmed at field level | `StepReceiptObligation`/`StepReceiptEmission` are workflow-step execution receipts (workflowId/stepId/role/actionClass), materially different shape from a truth-verification `TruthReceipt` (evidence_ids/obligation_ids/verification_results/hash chain) | adaptation only if ever attempted; no direct import |
| Independent Refinery Core (CAP-02, CAP-03) | none found | `NEW_OWNER_CANDIDATE` | confirmed again this tranche via mandatory negative search; zero matches across all roots | recommend; CVF reviewer decides whether/when to create |
| Post-Kernel Flow lifecycle (CAP-06) | none found | `NEW_OWNER_CANDIDATE` | confirmed again this tranche via mandatory negative search; zero matches across all roots | recommend; CVF reviewer decides whether/when to create |
| Kernel receipt/gate runtime (CAP-05) | TKG-T1 already `REJECT_DIRECT_IMPORT`s the retained runtime independently of SOT3 | `NEW_OWNER_CANDIDATE` for a fresh runtime; doctrine already enriched | TKG-T1's own Source Conversion Matrix line 63 predates SOT3 and reaches the same runtime-reject conclusion | no runtime action; doctrine relationship already recorded |
| Claim-tag pattern (CAP-08) | none found | `SHARED_PRIMITIVE_CANDIDATE` | small cross-cutting typing pattern, not a module-sized capability | candidate for extraction into a future shared utility |

## Capability Key Reconciliation

- Input capability keys (from T0R Capability Absorption Matrix rows): 12.
- Output decision keys (CAP-01 through CAP-12 above): 12.
- Unique keys: 12.
- Missing (input keys with no output decision): 0.
- Extra (output decisions with no matching input key): 0.
- Duplicate keys: 0.

```text
input_keys  = {CAP-01..CAP-12}  (12, derived 1:1 from T0R matrix row order)
output_keys = {CAP-01..CAP-12}  (12, one terminal decision section each)
input_keys == output_keys: True
len(input_keys) == len(output_keys) == len(input_keys | output_keys) == 12: True
missing = input_keys - output_keys = {} (0)
extra   = output_keys - input_keys = {} (0)
duplicate_check: len(output_keys) == len(set(output_keys)) == 12 (0 duplicates)
```

## Owner-Decision Token Summary

| Capability key | Owner-decision token |
|---|---|
| CAP-01 | `NEW_OWNER_CANDIDATE` |
| CAP-02 | `NEW_OWNER_CANDIDATE` |
| CAP-03 | `NEW_OWNER_CANDIDATE` |
| CAP-04 | `ENRICH_EXISTING_OWNER` |
| CAP-05 | `NEW_OWNER_CANDIDATE` |
| CAP-06 | `NEW_OWNER_CANDIDATE` |
| CAP-07 | `REJECT_DIRECT_IMPORT` |
| CAP-08 | `SHARED_PRIMITIVE_CANDIDATE` |
| CAP-09 | `ENRICH_EXISTING_OWNER` |
| CAP-10 | `DEFER_WITH_REOPEN_CONDITION` |
| CAP-11 | `DEFER_WITH_REOPEN_CONDITION` |
| CAP-12 | `NO_NEW_VALUE` |

All seven allowed owner-decision tokens from the work order are used at
least once except `BLOCKED_MISSING_OWNER_EVIDENCE`, which was not needed
because every capability had sufficient T0R-cited or current-CVF search
evidence to reach a terminal decision.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| a same-named file or token is mistaken for ownership | every ENRICH_EXISTING_OWNER decision above cites the specific section/field compared, not just the file path |
| TKG-T1's prior, independent rejection of the same runtime is missed | CAP-05 and the Overlap table explicitly cross-reference TKG-T1 Source Conversion Matrix line 63 |
| skill truth packet is mistaken for a general truth owner | CAP-04/CAP-09 and the Overlap table both cite its own Claim Boundary language limiting it to six ASSF-registered skill roots |
| upstream doctrine dependency is mistaken for ownership of a downstream architecture topology | CAP-01 is kept as `NEW_OWNER_CANDIDATE` with TKG-T1 recorded only as its enrich-existing-owner dependency, separated from CAP-04/CAP-09 in both the Owner-Decision Token Summary and the Overlap table |
| DEFER capabilities (CAP-10, CAP-11) treated as vaguely parked | see Value Conversion Ledger for exact, checkable reopen conditions |

## Decision / Disposition

Map disposition: `COMPLETE_PENDING_REVIEW`. All 12 accepted T0R capability
groups received one terminal owner-decision token, backed by an exact
current-CVF search (path/section/symbol where found, negative-search
evidence where absent), and an explicit path-existence-versus-semantic-
ownership distinction. No owner surface was created. All decisions remain
`PENDING_CVF_REVIEWER`.

## External Repository Absorption Entry Control

| Field | Value |
|---|---|
| Source type | retained legacy family plus accepted T0R evidence |
| Upstream or source-mirror disposition | `LEGACY_REFERENCE_ONLY_WITH_REASON`: operator-authored retained patch without verified upstream repository identity |
| Enumeration or manifest plan | reuse committed T0/T0R evidence; capability-level reconciliation only, no 305-row rewrite |
| Per-file terminal-ledger plan | N/A at this tranche granularity; capability-group reconciliation only |
| Owner or overlap route | exact current owner, new-owner candidate, shared primitive, defer, reject, or no-value per capability above |
| Value-disposition route | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Claim boundary | `COMPARISON_ONLY_NO_ABSORPTION`: owner/novelty recommendation only; no direct import, owner creation, or implementation |

## Mandatory Blind-Spot Control Block

| Field | Disposition |
|---|---|
| Trigger source | accepted T0R capability/conversion matrices |
| Control disposition | APPLICABLE |
| Corpus completeness section | PRESENT |
| Completeness trigger model | exact input capability-key set equals T1 decision-key set (12 = 12) |
| Blind-spot prevention action | mandatory negative searches for all 4 collision tokens plus 5 additional targeted searches; zero silent merging of capabilities |
| Residual gap | canonical contracts (SOT3-T2) and implementation remain future lanes |
| Blind-spot verdict | COMPLETE_PENDING_REVIEW |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | accepted T0R artifacts plus current CVF owner roots |
| Enumeration command | parse accepted capability tables; run current-owner searches per capability |
| Manifest artifact or inline manifest | accepted T0R capability matrices (12 rows) |
| Processing ledger artifact or inline ledger | `docs/reviews/CVF_SOT3_T1_VALUE_CONVERSION_LEDGER_2026-07-12.md` |
| Ledger terminal statuses | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Disposition taxonomy | ENRICH_EXISTING_OWNER, NEW_OWNER_CANDIDATE, SHARED_PRIMITIVE_CANDIDATE, DEFER_WITH_REOPEN_CONDITION, REJECT_DIRECT_IMPORT, NO_NEW_VALUE, BLOCKED_MISSING_OWNER_EVIDENCE |
| Owner-surface map | Owner And Novelty Decisions section above |
| Unresolved items | 0; all 12 capabilities received a terminal decision |
| Completion claim boundary | evidence recommendation only; no owner or runtime creation |

## Corpus Completeness And Report Integrity

- Corpus task class: SOT3 owner and novelty reconciliation.
- Corpus root: accepted T0R capability evidence and current CVF owner roots
  (`docs/reference`, `EXTENSIONS`, `governance`, schemas, tests, registries).
- Snapshot time: 2026-07-12, T1 execution.
- Enumeration command: filesystem-backed `rg -n` searches per capability
  across the named roots, plus direct parse of the 12 accepted T0R capability
  rows.
- Manifest artifact or inline manifest: accepted T0R Capability Absorption
  Matrix (12 rows).
- Manifest hash: committed T0R evidence at `ae7d53385`.
- Processing ledger artifact or inline ledger: `docs/reviews/CVF_SOT3_T1_VALUE_CONVERSION_LEDGER_2026-07-12.md`.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, REJECTED, BLOCKED_UNREADABLE
- Reconciliation: manifest=12; ledger_terminal=12; exclusions=0; unresolved=0
- Unresolved files: 0; all 12 capability owner decisions complete.
- Declared exclusions: none; low-value per-file evidence remains T0/T7-owned
  per work order Legacy Absorption Coverage Index Disposition.
- Unreadable or unsupported files: none encountered.
- Aggregation check: 12 capability rows in, 12 owner decisions out, 12 unique
  keys, 0 missing, 0 extra, 0 duplicate.
- Drift check: T0R evidence and current CVF owner roots unchanged throughout;
  `git status` clean at start and end.
- Output traceability: every decision cites T0R row provenance plus current
  CVF search evidence (path/section/symbol or negative-search confirmation).
- Adversarial verification: same-token collisions for receipt/truth/flow/
  refinery terms were opened and semantically compared, not accepted at face
  value; TKG-T1's own prior independent runtime rejection was cross-checked.
- Corpus verdict: PARTIAL - the 12-capability owner/novelty reconciliation is
  COMPLETE_VERIFIED for this tranche's scope; full 305-file per-file closeout
  remains a later T7 lane per the work order's Legacy Absorption Coverage
  Index Disposition.

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: truth doctrine capabilities enrich an existing
CVF owner while independent Refinery and post-Kernel Flow capabilities remain
new-owner candidates, per the work order's own stated prediction.

Evidence Comparison Requirement: the prediction was tested against current
CVF source searches (not same-token matches) for all 12 capabilities. It held
for CAP-04 and CAP-09 (`ENRICH_EXISTING_OWNER`, truth-foundation doctrine)
and for CAP-01, CAP-02, CAP-03, CAP-05, and CAP-06 (`NEW_OWNER_CANDIDATE`,
three-layer architecture topology plus independent Refinery and post-Kernel
Flow). The comparison additionally surfaced that TKG-T1 independently
reached the same runtime-reject conclusion as SOT3-T0/T0R before SOT3 began,
strengthening rather than merely confirming the CAP-04/CAP-09 enrich-owner
decisions; the initial CAP-01 draft over-extended that same finding to the
three-module topology, which the evidence does not support (see R2 repair).

Contradiction Or Gap Disposition: CAP-01 was initially drafted as
`ENRICH_EXISTING_OWNER` alongside CAP-04/CAP-09; closer field comparison
showed TKG-T1's single governing chain does not define the independent
Refinery module, the Refinery-to-Kernel boundary, a post-Kernel Flow module,
or the three-module responsibility split, so CAP-01 was corrected to
`NEW_OWNER_CANDIDATE` with TKG-T1 recorded as an upstream doctrine
dependency. CAP-07 (Flow embedded refinery, `REJECT_DIRECT_IMPORT`), CAP-08
(claim-tag pattern, `SHARED_PRIMITIVE_CANDIDATE`), CAP-10/CAP-11 (`DEFER_WITH_REOPEN_CONDITION`),
and CAP-12 (`NO_NEW_VALUE`) fall outside the original two-bucket prediction;
this is recorded as scope refinement, not contradiction, since the work
order's prediction covered only the doctrine-versus-independent-module split,
not every capability.

Claim Update Requirement: every one of the 12 capabilities carries an
explicit terminal owner-decision token in the Owner And Novelty Decisions
section above; none remain unclassified or implicitly assumed.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_equivalence_claim_evidence.py` |
| literalTokensReviewed | External Absorption Core; Corpus Completeness And Report Integrity; Overlap And Novelty Classification; External Absorption Value Conversion Matrix; COMPLETE_PENDING_REVIEW; COMPLETE_VERIFIED; PARTIAL; ENRICH_EXISTING_OWNER; NEW_OWNER_CANDIDATE; SHARED_PRIMITIVE_CANDIDATE; DEFER_WITH_REOPEN_CONDITION; REJECT_DIRECT_IMPORT; NO_NEW_VALUE |
| gateRunPurpose | confirm exact map shape after checker source review, informed by the T0/T0R path-collision and equivalence-claim lessons |
| claimBoundary | checker-shape conformance does not prove semantic ownership correctness |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | T0R acceptance -> T1 owner/novelty reconciliation -> CVF reviewer decision -> possible fresh T2 packet |
| Matching local-view guard | `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_corpus_completeness_report_integrity.py` |
| Owner surface | this map for evidence; CVF reviewer for acceptance |
| Disposition | ADAPT through bounded owner reconciliation |
| Claim boundary | worker output is advisory until CVF review |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private retained source and internal owner planning.

## Claim Boundary

This map is an advisory owner and novelty recommendation only. It does not
create, rename, or move an owner surface, author canonical contracts, import
retained code, or authorize implementation. All 12 decisions remain
`PENDING_CVF_REVIEWER`.
