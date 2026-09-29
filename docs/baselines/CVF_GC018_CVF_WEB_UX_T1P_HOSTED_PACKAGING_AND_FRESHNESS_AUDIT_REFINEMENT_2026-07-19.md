# CVF Baseline - CVF Web UX T1P Audit Refinement

Memory class: governed-baseline

Status: DISPATCH_READY

Date: 2026-07-19

## Purpose
Establishes the GC-018 source verification baseline for the T1P read-only audit refinement.

## Source Verification Manifest

The following sources were verified at HEAD `0a46eafa0`:
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/next.config.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/netlify.toml`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/cvf-workspace-read-model.ts`
- `docs/reviews/evidence/CVF_WEB_UX_T0_R3_LOCALHOST_2026-07-19`
- `docs/reviews/evidence/CVF_WEB_UX_T1_R1_LOCALHOST_2026-07-19`

## Claim Boundary
This baseline records the existence of current deployment configurations and UX evidence to support the T1P read-only packaging audit. It does not authorize any mutation or public release.

## Decision/Baseline/Proposed Tranche
- Baseline represents local execution configuration versus production deployment.
- Tranche: T1P.

## Evidence/Verification
Verification is delegated to the worker execution via Source Verification.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | baseline section requirements |
| gateRunPurpose | state confirmation |
| claimBoundary | structural compliance only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`audit-refinement`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class audit-refinement --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no additional defect-specific control returned |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-UX-T1P --title "CVF Web UX T1P Hosted Packaging And Freshness Audit Refinement" --date 2026-07-19 --base 0a46eafa0 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | `generic-worker-dispatch` |
| generatedSkeletonStatus | `USED_AS_STARTING_POINT` |
| manualEditsAfterScaffold | baseline-specific source manifest and boundaries |
| checkerReadAheadConfirmation | `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| docOnlyNewFields | none |
| claimBoundary | scaffold provenance only; no execution or readiness claim |
