# CVF Review: ASSF Lifecycle T0 Source Authority And Mutation Protocol

Memory class: FULL_RECORD

Status: COMPLETE

Date: 2026-06-26

docType: review

Batch ID: ASSF-LIFECYCLE-T0

## Purpose

Define the source authority and mutation protocol for updating
`cvf-dispatch-quality-reviewer` lifecycle metadata.

## Target / Source

Target source:
`docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json`.

## Scope / Methodology

Verified the active lifecycle guard, registry source, certification-decision
completion, generator, drift checker, and resolver. The current authority for
UAT success is T7's `PASSED` token; the older promotion bridge's `COMPLETE`
wording is treated as advisory historical residue for this tranche.

## Findings / Position

The mutation protocol is source-first: edit the selected registry source,
regenerate the generated index, run drift proof, then verify resolver readout.
No resolver source, Web, adapter, runtime, provider/live, public-sync, or
session-sync path belongs in the material commit.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| `PASSED` versus older `COMPLETE` wording | T7 lifecycle guard governs this update |
| Generated index hand-edit | generator-only regeneration required |
| Metadata update overclaim | non-active status and adapter deferral preserved |

## Decision / Recommendation

Decision: `MUTATION_PROTOCOL_APPROVED`.

Next step: T1 registry source update.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| T7 defines `PASSED` for `uatState` | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | line 86 | `PASSED` | ASSF lifecycle guard | VALUE_SET | ACCEPT |
| T7 defines `CERTIFIED` for `certificationState` | `docs/reference/agent_system_skills/CVF_ASSF_CERTIFICATION_LIFECYCLE_GUARD_CONTRACT.md` | line 81 | `CERTIFIED` | ASSF lifecycle guard | VALUE_SET | ACCEPT |
| source entry owns lifecycle fields | `docs/reference/agent_system_skills/registry/entries/cvf-dispatch-quality-reviewer.json` | lines 67-68 before update | `uatState` | ASSF registry entry | VALUE_SET | ACCEPT |
| generator owns aggregate write | `governance/compat/generate_assf_skill_index.py` | line 94 | `generate_index` | ASSF index generator | EXISTS | ACCEPT |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance source-state update; no public-sync authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | T0 source authority protocol |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- protocol only |
| receiptEvidence | CVF_RECEIPT_PRESENT - source verification table |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- protocol decision |
| invocationBoundary | governed local documentation review |
| interceptionBoundary | no runtime, provider, adapter, Web, or external mutation claim |
| claimLanguage | source authority for metadata update only |
| forbiddenExpansion | no package instance, activation, runtime behavior, resolver source mutation, Web projection, CLI/MCP adapter, provider/live proof, public-sync, push, package execution, or package integration |

## Claim Boundary

T0 approves the mutation protocol only; it does not itself prove generated-index
or resolver freshness.
