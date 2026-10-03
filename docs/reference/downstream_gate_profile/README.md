# CVF Downstream Gate Profile - Folder Index

Memory class: POINTER_RECORD

Status: ACTIVE_REFERENCE

docType: reference

Date: 2026-10-03

**Applies to:** dispatchers, workers, reviewers and closers changing the portable
downstream gate profile, the generated-project bootstrap or the project finding
intake.

## Purpose

Front door for `cvf.downstreamGateProfile@1.0.0`: the portable, versioned control
profile that generated downstream projects inherit, with its continuity contract,
status-applicability grammar, reviewer-local repair route, truthful coverage
states and project-to-parent finding intake.

## Scope / Applies To

Applies to the stable family in this folder and the runner family in
`scripts/lib/downstream_governance/`. It reuses, and does not reopen, the Golden
Downstream Bootstrap and Workspace Governance Learning Propagation closures.

## Read Order

1. `CVF_DOWNSTREAM_GATE_PROFILE_STANDARD.md` - canonical standard.
2. `CVF_DOWNSTREAM_GATE_PROFILE_MIGRATION.md` - upgrade and existing-project migration.
3. Schemas: `downstream_gate_profile.schema.json`, `downstream_continuity_contract.schema.json`,
   `downstream_finding_intake.schema.json`; template `DOWNSTREAM_FINDING_INTAKE_TEMPLATE.json`.
4. `downstream_finding_intake_registry.json` - parent dedup, admission and back-links.

## Owner And Archive

Owner: CVF Core governance maintainers (parent). Stable file names carry no dates;
history lives in git and completion reviews. Superseded content is archived under
`docs/reference/archive/`, never duplicated here.

## Machine Surfaces

| Surface | Path |
|---|---|
| Runner and modules | `scripts/lib/downstream_governance/` |
| Pinned status grammar and closeability | `governance/compat/check_gate_to_role_closeability.py` |
| Focused Python tests | `governance/compat/test_downstream_gate_profile.py`; `governance/compat/test_check_gate_to_role_closeability.py` |
| Offline golden harness | `scripts/test_cvf_downstream_gate_profile.ps1` |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

Navigation pointer only. It implements no enforcement, and claims no hosted CI,
Linux, real-project adoption, public rollout or runtime AI behavior.
