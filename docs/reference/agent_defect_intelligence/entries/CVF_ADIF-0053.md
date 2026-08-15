# ADIF-0053 - Mixed-Origin Synthesis Collapsed Into Low-Value Proposal

Memory class: POINTER_RECORD

Status: ACTIVE

```text
defectId: ADIF-0053
title: Mixed-origin synthesis collapsed into low-value proposal
defectCategory: SOURCE_FIDELITY
defectClass: ORCHESTRATOR_PACKET_GAP
defectRole: dispatcher; reviewer; closer
severity: HIGH
lifecycleState: ACTIVE
taskClasses: External knowledge absorption; Corpus intake; Reviewer closure
roles: dispatcher; worker; reviewer; closer
lifecyclePhases: pre-dispatch; implementation; pre-closure
surfaceSelectors: mixed-origin local packs, external-agent derived synthesis, value/cost decisions, processing ledgers
detectionSignals: local co-designed material is called secondary proposal only; UNREVIEWED or UNMERGED becomes a no-value rationale; one value/cost result spans upstream and local synthesis; full runtime cost is compared against knowledge-only value; file counts replace system-chain review
enforcementLevel: PARTIAL_CHECK
checkerBindings: governance/compat/check_mixed_origin_derived_synthesis_absorption.py; governance/compat/check_external_absorption_value_conversion.py
promotionState: RULE_AND_CHECK_EXIST
supersedes: NONE
lastVerifiedCommit: 3a40397df
roadmapSeedId: NONE
```

## Purpose

Record the false-negative absorption pattern exposed by RSPB-AI-T0. The pinned
upstream repo was valid authority for upstream facts, while the local preflight
pack was produced through upstream/public-CVF input plus operator-agent design.
The intake correctly rejected unsafe direct upstream behavior but incorrectly
used proposal maturity and full runtime cost to suppress the local system
chain's knowledge and contract value.

## Scope / Applies To

Applies to external/copy intake where a local artifact combines upstream,
CVF, operator, co-design, or novel inputs. It does not reduce the authority
review required before promotion.

## Bad Example

> The 205-file local pack is unreviewed and absent from active owner paths, so
> defer 94% of it and stop the whole tranche because implementation is costly.

## Good Example

> Classify each concept's origin and authority. Decide knowledge absorption,
> direct import, runtime activation, and authority promotion separately. Review
> profile -> contracts -> schemas -> approval/acquisition -> execution ->
> adapters -> fixtures/checkers as a system chain, then compare each conversion
> lane's value with that lane's cost.

## Canonical Sources

- `docs/reference/external_agent_review/CVF_MIXED_ORIGIN_DERIVED_SYNTHESIS_ABSORPTION_STANDARD.md`
- `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md`
- `docs/audits/CVF_RSPB_AI_T0_DUAL_CORPUS_INTAKE_AUDIT_2026-08-15.md`
- `.private_reference/legacy/CVF 13.08/CVF_CAPABILITY_PREFLIGHT_BOOTSTRAP/docs/reference/capability_preflight_bootstrap/README.md`

## Remediation

Require origin classification, claim-specific evidence, a split absorption
decision vector, and system-chain value review. `ADAPTED` must cite a current
owner path; otherwise retain `ADAPT_CANDIDATE`. Search current consumers and
blocked workflows before asserting none exist.

## Epistemic Process Block

### Expected Result / Prediction

Without the new distinctions, mature-looking upstream file counts and
unmerged local artifacts can produce a false whole-tranche stop.

### Evidence Comparison

RSPB reconciled all 764 files but its local ledger rows omitted actual value,
overlap, and owner fields, while the audit used 448 rejected upstream files and
unmerged local maturity to support one `STOP_COST_EXCEEDS_VALUE` result.

### Contradiction Or Gap Disposition

No contradiction: corpus completeness was valid; semantic value conversion
was not. The new checker remains a partial evidence-shape check.

### Claim Update

Mixed-origin derived synthesis is now a distinct governed intake class.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | bounded governance worker/reviewer |
| Provider or surface | local private provenance repository |
| Session or invocation | MODS-T0, 2026-08-16 |
| Working directory | repository root |
| Command or tool surface | source reads, rg, apply_patch, Python tests/checkers, git |
| Target paths | this entry, new SOT/checker/test, routing references, corrective assessments |
| Allowed scope source | direct operator request and MODS-T0 work order |
| Before status evidence | no mixed-origin SOT; RSPB collapsed decision |
| After status evidence | rule/checker and corrective reviews in MODS-T0 changed set |
| Diff evidence | `git diff --name-status 43d263d94..HEAD` |
| Approval boundary | governance and assessment repair only |
| Claim boundary | no runtime, provider, public, deployment, or production claim |
| Agent type | worker/reviewer |
| Invocation ID | mods-t0-adif-0053-20260816 |
| Expected manifest | ADIF-0053 and paired foundation/correction paths |
| Actual changed set | reconciled in MODS-T0 completion review |
| Manifest delta | PENDING_COMPLETION_REVIEW |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance learning; no public-sync action authorized.

## Claim Boundary

This entry records the defect and partial machine protection. It does not prove
semantic correctness or authorize source import, runtime, provider, public, or
production behavior.
