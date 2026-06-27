# CVF Review: ASSF Lifecycle T2 Generated Index Regeneration And Drift Proof

Memory class: FULL_RECORD

Status: COMPLETE

Date: 2026-06-26

docType: review

Batch ID: ASSF-LIFECYCLE-T2

## Purpose

Record generated-index regeneration and drift proof after the registry source
update.

## Target / Source

Generated aggregate:
`docs/reference/agent_system_skills/generated/skill-index.json`.

## Scope / Methodology

Ran `python governance/compat/generate_assf_skill_index.py --generate`, then
ran `python governance/compat/check_assf_skill_index_drift.py`.

## Findings / Position

The generated index is in sync with per-entry sources. The target generated
entry now carries `uatState: PASSED`, `certificationState: CERTIFIED`, and
three review artifacts.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| Hand-edited generated index | Prevented: generator command was used |
| Drift after source update | Prevented: drift checker PASS |
| Generated metadata interpreted as runtime activation | Prevented: index claim boundary remains metadata-only |

## Decision / Recommendation

Decision: `GENERATED_INDEX_REGENERATED_DRIFT_PASS`.

Next step: resolver projection verification.

## Command Evidence

| Command | Result |
|---|---|
| `python governance/compat/generate_assf_skill_index.py --generate` | generated `docs/reference/agent_system_skills/generated/skill-index.json` |
| `python governance/compat/check_assf_skill_index_drift.py` | PASS - skill index is in sync with registry entry sources |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance generated metadata update; no public-sync
authorization.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | T2 generated index regeneration |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE -- generated metadata only |
| receiptEvidence | CVF_RECEIPT_PRESENT - drift checker PASS |
| actionEvidence | ACTION_EVIDENCE_PRESENT -- generated index updated by generator |
| invocationBoundary | governed local generator and drift check |
| interceptionBoundary | no runtime, provider, adapter, Web, or external mutation claim |
| claimLanguage | generated index is in sync |
| forbiddenExpansion | no package instance, activation, runtime behavior, resolver source mutation, Web projection, CLI/MCP adapter, provider/live proof, public-sync, push, package execution, or package integration |

## Claim Boundary

T2 proves generated metadata sync only. It does not modify resolver source or
activate any package.
