# CVF Mixed-Origin Derived Synthesis Absorption Standard

Memory class: FULL_RECORD

Status: ACTIVE_REFERENCE

docType: reference

Date: 2026-08-16

## Purpose

Define the source-of-truth treatment for a local pack whose content combines
upstream repository evidence, public CVF material, operator requirements,
operator-agent co-design, and new synthesis. Such a pack is neither upstream
authority nor an arbitrary unsupported proposal.

Mixed-origin derived synthesis: REQUIRED

## Canonical Source Graph

`pinned upstream + governed/public CVF snapshot + operator requirements +
operator-agent design + novel synthesis -> provenance-backed derived synthesis
candidate -> current CVF owner review -> selective promotion`

Each edge has its own evidence obligation. Provenance establishes why a design
exists; it does not make the design canonical or prove runtime behavior.

## Scope / Applies To

Applies to governed intake, audit, roadmap, work-order, review, and closeout
artifacts evaluating a local pack with more than one declared origin class or
operator/agent-created synthesis. Pure upstream-only intake continues through
the external absorption core without this additional evidence block.

## Origin Classes

| Origin class | Meaning | Minimum evidence |
| --- | --- | --- |
| `UPSTREAM_REPOSITORY_BACKED` | Fact or concept traceable to original repository material. | URL or pinned mirror commit plus path/symbol |
| `CVF_PUBLIC_DERIVED` | Adaptation based on a public CVF snapshot. | snapshot identity and relevant public owner path |
| `OPERATOR_REQUIREMENT` | Constraint or desired outcome explicitly supplied by the operator. | operator attestation or governed decision record |
| `OPERATOR_AGENT_CO_DESIGNED` | Design produced through operator-agent evaluation and iteration. | attestation, rationale, alternatives, and intended owner |
| `NOVEL_SYNTHESIS` | New design not claimed to originate in an external repository. | rationale, invariants, owner fit, and validation plan |
| `MIXED_ORIGIN` | One concept materially combines two or more classes. | component-level source graph and evidence for each component |
| `ORIGIN_UNRESOLVED` | Origin cannot yet be established. | explicit blocker; no authority promotion |

## Authority And Maturity Boundary

The canonical artifact classification for an operator/agent-created local pack
with declared evidence is:

`artifactClass: PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE`

Its authority before promotion is:

`authorityStatus: NON_AUTHORITATIVE_UNTIL_REVIEWED`

`UNREVIEWED`, `UNMERGED`, `UNPROVEN_BASELINE`, or absence from current owner
paths describes maturity, not value. These facts may limit authority or runtime
readiness; they cannot alone justify `NO_NEW_VALUE`, `REJECT`, or a tranche-wide
`STOP_COST_EXCEEDS_VALUE` result.

No GitHub URL is required for `OPERATOR_REQUIREMENT`,
`OPERATOR_AGENT_CO_DESIGNED`, or `NOVEL_SYNTHESIS`. A source URL remains
mandatory when the artifact asserts an upstream fact.

## Claim-Specific Evidence Rule

| Claim type | Required validation |
| --- | --- |
| Upstream fact | pinned repository evidence |
| CVF constraint or owner statement | current governed CVF source; public snapshot may establish historical design input only |
| Operator requirement | operator attestation or decision record |
| Co-designed or novel design | rationale, alternatives, invariants, owner fit, and review evidence |
| Runtime behavior or effectiveness | tests, receipts, or live proof appropriate to the claim |

## Required Mixed-Origin Derived Synthesis Provenance

Every applicable governed absorption artifact must include:

```text
## Mixed-Origin Derived Synthesis Provenance

artifactClass: PROVENANCE_BACKED_DERIVED_SYNTHESIS_CANDIDATE
authorityStatus: NON_AUTHORITATIVE_UNTIL_REVIEWED

| Input or concept | Origin class | Evidence basis | Claim type | Validation method | Current CVF owner | Disposition |
|---|---|---|---|---|---|---|
| ... | MIXED_ORIGIN | ... | ... | ... | ... | ... |
```

Use `ORIGIN_UNRESOLVED` rather than inventing provenance. The whole local pack
must not be called "secondary proposal only" when its component source graph is
known.

## Required Absorption Decision Vector

One aggregate value/cost verdict is forbidden when it collapses heterogeneous
sources or decision axes. Record at least these independent axes:

```text
## Absorption Decision Vector

| Decision axis | Decision | Evidence | Cost boundary |
|---|---|---|---|
| Knowledge absorption | ... | ... | ... |
| Direct import | ... | ... | ... |
| Runtime activation | ... | ... | ... |
| Authority promotion | ... | ... | ... |
```

Rejecting direct import does not reject CVF-native adaptation. Deferring
runtime does not erase doctrine, contract, schema, fixture, checker, or package
value. Compare the cost of each selected conversion lane with the value of that
lane; do not compare documentation absorption against the cost of full runtime.

## Required System-Chain Value Review

Evaluate local derived synthesis as a composed capability chain before using
file counts or per-file maturity to decide value:

```text
## System-Chain Value Review

| Chain component | Evidence path | Existing CVF owner/gap | Value disposition | Readiness disposition | Next action |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |
```

Typical components include profile, contracts, schemas/policies,
approval/acquisition, execution plane, adapters, interaction projection,
fixtures/checkers, review, and freeze. A large number of rejected upstream
files cannot outweigh an independently valuable local system chain by count.

## Current Consumer And Blocked-Workflow Evidence

Claims such as `NO_CURRENT_CONSUMER` or `NO_BLOCKED_WORKFLOW` require recorded
searches across current roadmaps, work orders, worker returns, completion
reviews, runtime owners, and environment-failure evidence. Absence of a public
route or deployed consumer is not proof that no internal consumer or blocked
workflow exists.

## Adaptation Materialization Rule

Use `ADAPTED` only when the value is present in a named current CVF owner path.
Otherwise use `ADAPT_CANDIDATE`, name the target owner, and keep the next action
visible. Audit prose alone is evidence of evaluation, not materialized
absorption.

## Reviewer Semantic Audit

The reviewer must challenge four false-negative patterns after structural
gates pass:

- provenance class collapsed into "proposal";
- maturity used as a value rationale;
- direct-import or runtime cost used to reject lower-cost knowledge value;
- per-file counts used instead of composed system-chain value.

Machine checks make these distinctions reviewable. They do not prove the
correct value judgment.

## Machine Guard

Forward, range-aware enforcement:

`governance/compat/check_mixed_origin_derived_synthesis_absorption.py`

The guard applies to this standard and changed governed artifacts carrying
`Mixed-origin derived synthesis: REQUIRED`. It requires provenance, separate
decision axes, system-chain review, exact authority tokens, and rejects common
maturity-as-value phrasing.

## External Absorption Core

| Field | Value |
| --- | --- |
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | mixed-origin derived synthesis task class definition |
| Enumeration command | inline canonical taxonomy and required evidence blocks |
| Manifest artifact or inline manifest | inline Origin Classes and claim-specific evidence tables |
| Processing ledger artifact or inline ledger | inline reviewer audit and required decision-vector rules |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` and this standard |
| Unresolved items | 0 in the standard definition |
| Completion claim boundary | evidence-shape definition only |

## Corpus Completeness And Report Integrity

- Corpus task class: single governance-standard definition.
- Corpus root: this file.
- Snapshot time: 2026-08-16.
- Enumeration command: `Get-Content -Raw docs/reference/external_agent_review/CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md`.
- Manifest artifact or inline manifest: inline sections and tables.
- Manifest hash: not generated for a single definition artifact.
- Processing ledger artifact or inline ledger: inline requirements.
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE.
- Reconciliation: manifest=1; ledger_terminal=1; exclusions=0; unresolved=0.
- Unresolved files: 0.
- Declared exclusions: none.
- Unreadable or unsupported files: 0.
- Aggregation check: one standard equals one processed definition.
- Drift check: paired tests assert mandatory tokens.
- Output traceability: checker and tests cite this path.
- Adversarial verification: negative fixtures cover false-negative patterns.
- Corpus verdict: COMPLETE_VERIFIED

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
| --- | --- | --- | --- | --- | --- |
| mixed-origin source model | provenance doctrine | DOCTRINE_ADAPTED | this standard | use in future intake | no runtime |
| derived reusable shapes | package evaluation discipline | PACKAGE_CANDIDATE | governed package owner | fresh work order | no activation |
| synthesized behavior | runtime evaluation discipline | RUNTIME_CANDIDATE | current runtime owner | tests/live proof first | no mutation |
| false-negative patterns | machine evidence shape | CHECKER_CANDIDATE | governance/compat checker | implement with tests | no semantic-proof claim |
| direct copied implementation | authority boundary | REJECT_DIRECT_IMPORT | external absorption core | CVF-native rewrite only | no import |
| unsupported inventory | no conversion value | NO_PACKAGE_OR_RUNTIME_VALUE | existing owner or blocker | close with evidence | no runtime/package |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| external absorption semantics | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` | ENRICH_EXISTING | adds mixed-origin, maturity/value, split-decision, and system-chain rules | route core to this SOT |
| over-defer defect | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0019.md` | ENRICH_EXISTING | adds the provenance and decision-collapse subtype | record ADIF-0053 |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | External repo or copied folder |
| Chain map route | mixed source graph -> origin classification -> claim-specific validation -> decision vector -> system-chain review -> owner promotion |
| Matching local-view guard | `governance/compat/check_mixed_origin_derived_synthesis_absorption.py` |
| Owner surface | this standard |
| Disposition | ENRICH_EXISTING |
| Claim boundary | governance routing and evidence shape only |

## Epistemic Process Block

Epistemic Process Applicability: EPISTEMIC_PROCESS_NA_WITH_REASON: normative
governance definition; empirical corpus and runtime claims belong to applying
assessments.

Expected Result / Prediction: the evidence shape prevents the known category
error from closing without visible split decisions.

Evidence Comparison: paired unit tests and corrective assessments provide
implementation evidence.

Contradiction Or Gap Disposition: semantic truth remains reviewer-owned.

Claim Update: mixed-origin synthesis is now a first-class intake category.

## Claim Boundary

This standard does not make a local pack canonical, authorize direct import,
execute source code, activate packages, mutate runtime, prove live behavior,
publish artifacts, or establish production readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance standard; public sync is not authorized here.
