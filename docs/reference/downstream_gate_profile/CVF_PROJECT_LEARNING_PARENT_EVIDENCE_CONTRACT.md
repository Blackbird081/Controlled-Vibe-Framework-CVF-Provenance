# CVF Project Learning Parent Evidence Contract

Memory class: FULL_RECORD
Status: ACTIVE_DESIGN_CONTRACT
docType: reference
Date: 2026-10-04
Batch ID: CVF-FLAL-T1
providerExecutionAuthority: FORBIDDEN

## Purpose

Specify the parent evidence layer required by the Project Learning Loop Standard.
This is an extension of F2G's parent registry, not another intake, signal ledger,
acceptance engine or runtime. A conforming evidence record proves declarations
and local byte identity; Local still decides semantic value and acceptance.

## Scope / Applies To

Applies to new opt-in parent-owned evidence for a selected finding. Project
intake generation, profile1.1 locks, ADIF IDs, LSC roots and Learning Plane
feedback remain under their existing owners. CCMA remains parked.

## Owner Reconciliation And Decision

| Capability | Existing owner | Selected disposition |
|---|---|---|
| Finding classes/lanes/disposition and earlier gate routing | F2G standard/checker | REUSE; preserve vocabulary |
| Defect classification/link/proposal | ADIF classify_finding | REUSE; no new classifier or ADIF entry mutation |
| Portable generation and record coherence/hash | cvf_dg_intake.validate_record | RETAIN; do not turn project parser into parent reviewer |
| Signal intake, feedback and autonomousMutationAuthorized=false | LearningSignalIntakeBridge | RETAIN; no TypeScript runtime expansion |
| Dedup/rootCauseGroupId/captureState and advisory promotion | LSC-T1/T4 | REUSE; no new root-cause ID or promotion threshold |
| Five value checks plus independent project/parent/return/application trace | Project Learning Loop Standard | EXTEND this normative owner with the contract below |
| Parent evidence storage | downstream_finding_intake_registry entries/findings | EXTEND opt-in finding member; keep historical entries byte-preserved |
| Parent shape/reference validation | existing F2G compatibility checker | T2 extend through a bounded helper, not a rival command or hook |

The inspected interfaces carry text evidence and disposition; they do not model
these five named checks plus separately pinned delivery/application receipts.
This conclusion is limited to the cited symbols and contracts. T2 must stop for
any contradicting active owner found during implementation.

## Contract / Requirements

Contract identifier: `cvf.parentLearningEvidence@1.0.0`.
NEW_FIELD_INTRODUCED: optional `parentEvidence` on a parent registry finding.
Its version is independent of portable intake/profile version. The outer registry
schemaVersion stays unchanged only if current consumers admit this additive
member; otherwise stop for an explicit compatibility decision before mutation.
No automatic conversion, regeneration or retroactive admission of old entries.

A parentEvidence object has exactly these top-level fields:
`schemaVersion`, `findingId`, `source`, `valueChecks`, `decision`, `implementation`,
`projectResolution`, `returnDelivery`, `projectApplication`, `claimLimits`.
Unknown fields, versions, enum values and duplicate JSON keys fail closed.
All reasons, actor/owner identifiers and claim limits are concrete nonempty strings.
The findingId equals its enclosing finding id; source carries sourceProject and
an evidence reference. No new dedup identity is minted.

### Evidence Reference

Each evidence reference is exactly `{path, sha256, fragment, evidenceClass}`.
path is a repository-relative existing regular file; sha256 is lowercase64hex
SHA-256 of its raw bytes; fragment is a nonempty locator used by the reviewer,
not proof of what the cited passage means. evidenceClass is one of
`OBSERVED_LOCAL`, `ATTRIBUTED_SOURCE`, `SYNTHETIC_OFFLINE`.
Reject absolute/drive/UNC paths, parent traversal, URL/network locators, symlink
or Windows reparse escapes and targets resolving outside the supplied repo root.
A checker never dereferences an external link or executes cited code/commands.
JSON is strictly parsed; filesystem/read/hash errors become validation findings.
Current bytes plus exact hash pin identity, not freshness against an unknown
remote revision. Record that temporal limit; changed pinned bytes require explicit
re-admission, not automatic hash replacement. Revalidate immediately at claimed
closure/use boundary; offline hash validation is not OS race prevention.

### Five Value Checks

valueChecks has exactly `sourceConfidence`, `reusableMechanism`, `existingCoverage`,
`incrementalValue`, `boundedProof`. Each has exactly `status`, `reason`,
`evidence`, `limits`. status is `SUPPORTED`, `INCONCLUSIVE` or `NOT_ASSESSED`;
evidence is a list of references; limits is a concrete nonempty string.
SUPPORTED requires at least one valid pinned reference. ATTRIBUTED_SOURCE alone
cannot support a claim marked observed/reproduced; SYNTHETIC_OFFLINE supports only
synthetic structural claims. The record exposes these classes for Local review;
the checker does not infer semantic truth from text length or hashes.

### Parent Decision And Dedup

Decision is exactly `{state, reason, reviewer, owner, f2gDisposition, evidence}`.
state is `PENDING`, `ACCEPT`, `MERGE`, `DEFER` or `DECLINE`; f2gDisposition uses the
current F2G owner's vocabulary. PENDING permits reviewer=null and no decision
reference; every decided state needs a reviewer identity and pinned Local decision
reference. Identity is a recorded role/actor label, not authentication.
ACCEPT/MERGE require all five value checks SUPPORTED and at least one Local
observed decision reference; human review is still required. DEFER/DECLINE retain
incomplete checks with reasons. MERGE identifies the existing owner and dedup
rationale through existingCoverage; RULE_EXISTS cannot claim new control value
without an evidenced change in discovery/application/control behavior.
Decision/f2gDisposition are different vocabularies: do not equate strings or copy
parent states into portable acceptance without its own parent disposition contract.

### Independent Lifecycle Objects

Each lifecycle object has exactly `{state, reason, evidence}`.

| Object | States | Positive requirement |
|---|---|---|
| projectResolution | UNKNOWN, OPEN, RESOLVED, PARKED_BY_OPERATOR | RESOLVED has source-project resolution evidence; not inferred from parent result |
| implementation | NOT_IMPLEMENTED, IMPLEMENTED_BOUNDED | Positive requires ACCEPT/MERGE, pinned control change and bounded positive/negative proof; evidence alone does not authorize implementation |
| returnDelivery | NOT_RETURNED, RETURNED, PARKED_BY_OPERATOR | RETURNED requires implementation proof plus delivery receipt naming finding, parent control version/hash and recipient |
| projectApplication | NOT_APPLIED, APPLIED, PARKED_BY_OPERATOR | APPLIED requires RETURNED plus project-owner authorization and application verification receipt bound to the same finding/control/recipient |

Delivery/application evidence must be structured JSON receipts, not any arbitrary
existing file carrying a matching hash. Receipt shape: schemaVersion
`cvf.learningLoopReceipt@1.0.0`, kind `DELIVERY` or `APPLICATION`, findingId,
sourceProject, control `{path, sha256}`, actor, authorization, verification,
claimLimits. authorization/verification are pinned evidence references; DELIVERY
verification proves handoff/reception within its declared surface, APPLICATION
verification proves bounded project behavior. Application actor is the project
owner or explicitly delegated actor. The reviewer verifies role/authorization
meaning; structural checks only join identifiers, evidence class and bytes.
Delivery and application receipts are distinct and must not reuse the same file.
Untyped old parent acceptance or RETURNED text cannot synthesize either receipt.

An operator park is a restriction on project effects, not forced absence of an
already achieved historical resolution. If returnDelivery is PARKED_BY_OPERATOR,
projectApplication is PARKED_BY_OPERATOR; no new delivery/application receipt is
admitted until explicit unpark authority. Parent ACCEPT/MERGE/implementation may
remain recorded while loopback is parked. No real project is opened by this design.

## Compatibility And Validation Outcomes

Absent parentEvidence is `LEGACY_UNTYPED_NOT_REVALIDATED`; it remains historical,
never typed PASS or a new admission/application claim. Typed conformance is
`TYPED_STRUCTURAL_VALID`; neither outcome is semantic acceptance. Typed validation
failure blocks the corresponding typed claim. A mixed registry reports typed,
legacy and invalid counts separately, with no whole-registry quality score.
T2 fixtures must include both heterogeneous historical entry shapes without
rewriting the committed registry. No typed evidence is backfilled for CCMA.

## Verification / Enforcement

T2 will extend the existing F2G checker's execution/report path through a bounded
parent-evidence helper plus versioned schema and focused synthetic fixtures.
Read-only validation receives an explicit root/record for tests; production uses
the parent registry. Existing F2G Markdown disposition behavior is retained.
No new daemon, intake command, registry writer, provider invocation or semantic
acceptance/promotion algorithm is part of this contract. T1 does not implement it.

Required negative cases: missing each value check; hash mismatch; unresolved or
escaping/reparse locator; duplicate/unknown keys/version/state; attributed-only
observed proof; ACCEPT without reviewer; implementation without proof; arbitrary
file as receipt; finding/control/recipient join mismatch; APPLIED without separate
receipt or authorization; parked positive transition; legacy silent promotion.
A synthetic positive chain proves only fixture composition; it cannot prove live
AI governance, source-project delivery or production adoption.

## T2 Validation Binding

Batch CVF-FLAL-T2 implements the contract above as read-only structural validation.
It adds no registry writer, intake command, daemon or project effect.

| Surface | Path |
|---|---|
| Closed-shape versioned schema (parentEvidence and receipt) | `docs/reference/downstream_gate_profile/parent_learning_evidence.schema.json` |
| Validator and mixed-registry classifier | `governance/compat/parent_learning_evidence.py` |
| Production binding (existing F2G checker and its JSON/text report, `parentEvidence` member) | `governance/compat/check_finding_to_governance_learning.py` |
| Synthetic fixtures (disposable roots) | `governance/compat/test_parent_learning_evidence.py`; `governance/compat/test_check_finding_to_governance_learning.py` |

Implementation choices that refine, not change, the design:

- The schema is a closed-shape declaration; byte hashes, locator safety, duplicate JSON
  keys and cross-object joins are enforced by the validator, which hand-parses with
  duplicate-key and NaN refusal. Reference path components are checked with `lstat`
  so symlinks and Windows reparse points are refused.
- `source` is `{sourceProject, evidence}`. Receipt recipient is bound to the receipt
  `sourceProject`, which must equal the parent evidence `source.sourceProject`; the
  receipt shape carries no separate recipient field.
- `implementation` evidence must include references whose fragments start with
  `control:`, `proof-positive:` and `proof-negative:`. Delivery and application
  receipts must name that same control path and sha256.
- An observed/reproduced claim in a value-check reason needs an `OBSERVED_LOCAL`
  reference. `ACCEPT` with `RULE_EXISTS` is refused; use `MERGE`.
- A parked returnDelivery or projectApplication admits no receipt evidence.
- Findings without `parentEvidence` are `LEGACY_UNTYPED_NOT_REVALIDATED`. A legacy
  finding whose top-level `returnDelivery` is `RETURNED` or `sourceProjectApplication`
  is `APPLIED` is refused as `legacy_silent_promotion`. Typed-invalid findings are
  F2G violations; legacy findings are not. The checker reports typed, legacy and
  invalid counts separately.
- Validation outcomes are structural. They do not authenticate actors, prove
  semantic truth, or show any project delivery or adoption.

## Risk / Corrective Action

Pins and structural joins prevent accidental unsupported declarations, not a
malicious actor fabricating all evidence. Human source/value review remains
required. Runtime integration is outside scope. Avoid introducing a parallel
learning ledger, historical re-review or silent portable profile migration.

## Claim Boundary

Contract/owner reconciliation (T1) plus offline structural validation with synthetic
fixtures (T2). No semantic acceptance, project edits/tests/migration, CCMA backfill,
real receipt, provider proof, runtime governance proof or public release.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Five checks and independent states | CANONICAL_OWNER | docs/reference/downstream_gate_profile/CVF_PROJECT_LEARNING_LOOP_STANDARD.md | Value Admission; Loopback And Independent States | five checks | PLL standard | ACCEPT |
| Disposition routing already owned | CANONICAL_OWNER | docs/reference/CVF_FINDING_TO_GOVERNANCE_LEARNING_TRIGGER_STANDARD.md | Protocol; Owner Surface | F2G | F2G standard | ACCEPT |
| Finding classifier does not promote entries | CURRENT_SOURCE | governance/compat/run_adif_finding_intake_bridge.py | classify_finding | FindingIntakeRequest/Outcome | ADIF bridge | ACCEPT |
| Portable record validates fields, coherence and digest | CURRENT_SOURCE | scripts/lib/downstream_governance/cvf_dg_intake.py | validate_record | parentLinks.admissionRecord | portable intake | ACCEPT within named function scope |
| Learning Plane produces advisory signal/feedback | CURRENT_SOURCE | EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/learning-signal-intake-bridge.ts | LearningSignalIntakeInput; LearningSignalIntakeBridge.intake | evidenceBasis; autonomousMutationAuthorized | Learning Plane | ACCEPT |
| LSC reuses signal ownership and dedup | CANONICAL_OWNER | docs/reference/learning_signal_chain/CVF_LSC_T1_SIGNAL_LEDGER_SOURCE_LAYOUT_AND_DEDUP_CONTRACT.md | Existing Intake Field Ownership; Disposition And Capture-State Authority Rule | rootCauseGroupId/captureState | LSC | ACCEPT |
| Promotion recommendation remains advisory | CANONICAL_OWNER | docs/reference/learning_signal_chain/CVF_LSC_T4_PROMOTION_THRESHOLD_POLICY.md | Promotion Principles | no autonomous mutation | LSC promotion policy | ACCEPT |
| Existing parent registry is heterogeneous and historical | CURRENT_SOURCE | docs/reference/downstream_gate_profile/downstream_finding_intake_registry.json | entries | parentLinks; findings | F2G parent registry | ACCEPT as compatibility input; historical proof not replayed |
| Existing checker is finding-disposition artifact gate | CURRENT_SOURCE | governance/compat/check_finding_to_governance_learning.py | _validate_path_with_text; main | disposition/artifact validation | F2G checker | ACCEPT within inspected code scope |

## Epistemic Process Block

Expected Result: reuse current owners and identify the smallest parent evidence extension.
Evidence Comparison: F2G owns disposition, ADIF classification, portable intake fields/coherence/hash, Learning Plane advisory signal and LSC dedup/promotion. The PLL standard already requires five checks and separate states.
Contradiction / Gap Disposition: generic evidenceBasis and admissionRecord are not typed receipt validation. Select only the scoped PLL parent evidence extension; no whole-CVF absence claim or portable defect is inferred.
Claim Update: a design contract is selected; implementation, semantic acceptance and adoption remain unproven.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: parent-only contract design; existing public pipeline is separate.
