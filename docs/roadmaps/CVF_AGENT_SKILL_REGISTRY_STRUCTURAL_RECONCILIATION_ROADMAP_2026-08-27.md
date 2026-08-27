# CVF Agent Skill Registry Structural Reconciliation Roadmap

Memory class: governed-roadmap

Status: AGTR_R1_DISPATCH_READY_SINGLE_TRANCHE_CAP

Date: 2026-08-27

## Purpose

Remove the remaining truthful public required-check blocker by reconciling the
fourteen malformed or structurally incomplete agent-skill records from
`AGT-021` through `AGT-034`. Treat the fourteen records as one owner family and
one worker pass, not fourteen tranches.

## Authorization / Decision

The operator directed continuation and has standing authority for serious,
high-value repairs with strict time and quota discipline. Exact-SHA hosted run
`33053902261` proves Governance Registry Validation and its dependent Status
Check are the only failures inside Documentation & Testing. This roadmap
admits AGTR-R1 only and creates no automatic successor.

## Current Evidence

- Final PSRR public SHA is `d27d3db261404e8f594f130702ca7ef2c86a0ee7`.
- Public Surface, Static CI, Public Sync Preflight, and CVF CI pass at that SHA.
- The unchanged registry validator reports 89 errors, all against
  `AGT-021` through `AGT-034`.
- The corresponding fourteen private and public records are byte-identical.
- `AGT-021` and `AGT-022` contain flattened/duplicated material; later records
  retain readable content but lack some canonical structural fields.
- `AGT-001` through `AGT-020` already satisfy the validator and are read-only
  structural exemplars, not rewrite targets.

## Scope / Target / Owner Boundary

AGTR-R1 may modify only the fourteen named agent records in both the private
provenance repository and public-sync clone, plus one named private worker
return. The final private/public versions of each record must be byte-identical.

The worker may use committed history and the readable content already present
in each file to recover structure. It must preserve IDs, titles, provenance,
source URLs, capabilities, constraints, risk meaning, autonomy meaning,
dependencies, UAT references, and licensing statements. It may remove only
demonstrably duplicated or format-corrupted representations of retained
content.

Validator, workflows, indexes, source skills, examples, mapping records,
public-surface manifest, product code, dependencies, and all other registry
families are read-only.

## Design Control Gate

Each repaired record must have exactly one leading AGT title and canonical
sections `Source`, `Capability`, `Governance`, `Risk Justification`, and
`UAT Binding`. Governance must expose parseable `Risk Level` and `Autonomy`
table rows. No repair may invent a stronger capability, broader autonomy,
lower risk, new runtime eligibility, or new source claim.

The worker must build a fourteen-row before/after ledger recording retained
source evidence, risk/autonomy fidelity, removed duplication, and validator
result. Any record whose semantics cannot be recovered confidently returns
`BLOCKED_WITH_REASON` rather than receiving guessed content.

## Tranche Value Admission

| Factor | Decision |
| --- | --- |
| outcome consumer | public maintainers and users relying on required PR status |
| severity | P1 release blocker and corrupted governance metadata |
| evidence | exact-SHA hosted failure plus local 89-error reproduction |
| marginal value | one owner-family repair can remove the final known required-check blocker |
| cost ceiling | one worker return, fourteen mirrored records, zero providers |
| stop condition | stop on semantic ambiguity, validator change, non-AGT target, or second tranche |
| disposition | CONTINUE_HIGH_VALUE as AGTR-R1 only |

## Work Plan

1. Capture both HEADs, status, staging, and hashes for all fourteen records.
2. Build the semantic-preservation ledger before editing.
3. Repair the private canonical records, then mirror exact bytes to public.
4. Prove canonical headings, risk/autonomy rows, ID/title fidelity, and zero
   duplicated leading title for all fourteen.
5. Run public validator, private AGT-only error reconciliation, public-surface
   scan, public-sync preflight, and byte-identity comparison.
6. Return all changes uncommitted for independent review.

## Acceptance Criteria

- Public unchanged validator exits zero.
- Private validator emits zero AGT-family errors; unrelated private USR debt
  remains disclosed and outside scope.
- All fourteen private/public pairs are byte-identical.
- IDs, titles, source/provenance, risk and autonomy meaning remain traceable to
  pre-edit material or committed history.
- No `AGT-001..020`, index, validator, workflow, product, dependency, source
  skill, example, mapping record, or manifest changes.
- Both staging areas remain empty and both HEADs remain unchanged.
- Reviewer owns commits, public push, and fresh exact-SHA hosted proof.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| `INTERNAL_AGENT` | private/public AGT governance records | documentation structure only; no runtime activation | before/after ledger and validator | N/A with reason: no adapter behavior changes | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | public repository records | public documentation consumption only | exact mirrored Markdown | runtime/CLI/MCP eligibility remains outside scope | `DEFERRED_WITH_REASON` |

## Verification / Evidence

Evidence must include dual HEAD/status/staging, fourteen-pair hashes, the
semantic-preservation ledger, exact changed paths, public validator output,
private AGT-only reconciliation, public-surface scan, authorized public-sync
preflight, diff hygiene, and the worker-return fast gate.

## Non-Goals

No validator weakening, workflow change, new generator, index rewrite,
semantic capability expansion, package-skill promotion, source absorption,
provider/live call, secret access, dependency upgrade, merge, deploy, Netlify
action, public-main mutation, AGTR-R2, or automatic successor.

## Package Skill Productionization Control Block

SOP source: `docs/reference/agent_system_skills/CVF_PACKAGE_SKILL_PRODUCTIONIZATION_SOP.md`

Current phase: N/A with reason: legacy agent registry documentation repair is
not ASSF package-skill lifecycle work.

Target lifecycle state: unchanged.

Prior phase evidence: existing AGT records and validator only.

Next forbidden skip: no promotion, activation, loading, or runtime eligibility claim.

Runtime/provider proof: N/A with reason: static Markdown reconciliation only.

Claim boundary: registry structure, not package productionization.

## Public Export Disposition

BLOCKED_MISSING_PUBLIC_ARTIFACTS

Reason: AGTR-R1 is private dispatch authority. Export requires independent
acceptance, a public commit, and exact-SHA hosted proof.

## Next Allowed Move

Execute exactly AGTR-R1 under its paired GC-018 baseline and work order. Close
after one accepted mirrored candidate or one honest semantic-recovery blocker.
Do not create AGTR-R2.

## Claim Boundary

This roadmap authorizes one no-commit structural reconciliation candidate. It
does not authorize content invention, risk reduction, autonomy expansion,
validator/workflow weakening, merge, deployment, secrets, providers, or any
successor tranche.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/skill-library/registry/validate_registry.py`; `governance/compat/check_governed_artifact_authoring.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_package_skill_productionization_pipeline.py` |
| literalTokensReviewed | roadmap status, tranche value, dual-agent rows, package control, public disposition and claim boundary |
| gateRunPurpose | confirm one-tranche roadmap shape after source verification |
| claimBoundary | structural conformance does not prove semantic preservation or hosted success |
