# CVF Review: ASSF Admission T2 Gate Execution And Read Model Proof

Memory class: FULL_RECORD

Status: COMPLETE

Date: 2026-06-26

docType: review

Batch ID: ASSF-CERTIFIED-METADATA-ADMISSION

## Purpose

Record direct gate execution and current read-model proof for the admission
checker.

## Target / Source

Target gate: `governance/compat/check_assf_certified_metadata_admission.py`.
Target read model:
`docs/reference/agent_system_skills/generated/skill-index.json`.

## Scope / Methodology

Ran the focused unit tests, direct admission gate with `--require-certified`,
existing ASSF generated index drift checker, and ASSF resolver readout command.

## Findings / Position

The current registry/index state passes certified metadata admission. Resolver
readout returns one metadata-only candidate and does not include activation,
adapter, provider, or Web authority.

## Risk / Corrective Action

| Risk | Disposition |
|---|---|
| gate proof could rely on stale generated index | drift checker passed after direct admission proof |
| resolver proof could overclaim lifecycle fields | recorded as metadata-only readout; checker uses registry/index, not resolver packet lifecycle fields |

## Verification / Evidence

| Command | Result |
|---|---|
| `python -m unittest governance.compat.test_check_assf_certified_metadata_admission` | PASS - 6 tests |
| `python governance/compat/check_assf_certified_metadata_admission.py --require-certified` | PASS |
| `python governance/compat/check_assf_skill_index_drift.py` | PASS |
| `python governance/compat/run_assf_skill_resolver.py --task-class dispatch-authoring --role reviewer --phase PRE_DISPATCH --surface governance/compat --risk-ceiling R0` | PASS - one candidate |

## Decision / Disposition

T2 disposition: COMPLETE. Proceeded to T3 Web projection decision.

## Claim Boundary

T2 proves gate/read-model state only. It does not change runtime, Web, resolver,
adapter, provider/live, public-sync, or session surfaces.
