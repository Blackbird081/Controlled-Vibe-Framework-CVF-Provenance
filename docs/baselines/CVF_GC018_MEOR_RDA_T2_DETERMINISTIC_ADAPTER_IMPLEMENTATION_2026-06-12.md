# CVF GC-018 Baseline: MEOR-RDA-T2 Deterministic Adapter Implementation

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-12

Owner: Codex

baseHead: `6a9a5703`

## Purpose

Authorize a bounded local deterministic implementation tranche for the
regulated-domain adapter defined by RDA-T1.

RDA-T2 may add a Control Plane Foundation helper that converts a
`DscpDomainProfile` with regulated lifecycle support into profile-owned MEOR
metadata requirement declarations. It must not mutate profiles, descriptors,
corpus records, external Policy_Local files, EC gate values, retrieval
behavior, OCR, or provider paths.

## Scope / Target / Owner Boundary

In scope:

- new local deterministic CPF adapter helper;
- focused CPF tests for regulated and non-regulatory profiles;
- GC-051 registry coverage for any new source/test files;
- RDA-T2 completion review and continuity updates.

Out of scope:

- external Policy_Local mutation;
- candidate metadata correction;
- EC-T5/EC-T6 activation or `QUERY_CLASS_GATED` write;
- retrieval disclosure, OCR installation, corpus ingestion, provider/API-key
  use, public-sync, production readiness, or public readiness.

## Authority Chain

| Authority | Path | Status |
| --- | --- | --- |
| RDA roadmap | `docs/roadmaps/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_ROADMAP_2026-06-12.md` | ACTIVE_RDA_T1_CLOSED_RDA_T2_AUTHORIZATION_READY |
| RDA-T1 completion | `docs/reviews/CVF_MEOR_RDA_T1_REGULATED_DATE_ADAPTER_CONTRACT_COMPLETION_2026-06-12.md` | CLOSED_PASS_BOUNDED |
| RDA-T1 contract | `docs/reference/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_CONTRACT_2026-06-12.md` | ACTIVE |
| RDA-T1 semantics | `docs/reference/CVF_MEOR_REGULATED_DOMAIN_ADAPTER_SEMANTICS_2026-06-12.json` | ACTIVE |
| DSCP domain profile contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | ACCEPT |
| DSCP metadata bridge | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.metadata.requirement.bridge.ts` | ACCEPT |

## Source / Predecessor Evidence

Predecessor release:

- RDA-T1 completion:
  `docs/reviews/CVF_MEOR_RDA_T1_REGULATED_DATE_ADAPTER_CONTRACT_COMPLETION_2026-06-12.md`
- Material commit: `6a6b343f`
- Session sync commit: `6a9a5703`

Source evidence:

- `DscpDomainProfile` owns `supportsDocumentStatus` and
  `metadataRequirements`.
- `DscpMetadataRequirement` owns requirement identity, owner profile,
  metadata key, required flag, and acceptable evidence bases.
- `buildDscpMetadataRequirementBridge` validates owner-profile alignment,
  duplicate requirement IDs, and evidence-basis values.
- RDA-T1 semantics define adapter mappings and forbid runtime activation in
  T1.

## Decision / Baseline / Proposed Tranche

Decision: authorize and close RDA-T2 as a bounded implementation tranche.

Baseline:

- implementation surface: Control Plane Foundation only;
- worker mode: `WORKER_MUST_NOT_COMMIT`;
- reviewer-owned closure: Codex;
- next tranche after RDA-T2, if closed, is RDA-T3 conformance.

Proposed tranche output:

- local deterministic adapter helper;
- focused tests;
- GC-051 registry coverage;
- completion packet and continuity update.

Closure output:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.regulated.domain.adapter.ts`
  implements local deterministic regulated requirement generation.
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts`
  exports the adapter surface for later CPF consumers.
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.regulated.domain.adapter.test.ts`
  covers regulated, non-regulatory, ownership, bridge, and no-gate-activation
  behavior.
- GC-051 registry JSON/Markdown cover the new source/export and test surfaces.
- Completion packet records bounded closure.

## Design Control Gate

Design verdict: `PASS_BOUNDED`.

Selected design:

- implement one local deterministic adapter helper in CPF;
- keep regulated lifecycle requirements profile-owned;
- use the existing DSCP metadata requirement bridge for validation;
- fail closed when regulated fields appear on profiles without
  `supportsDocumentStatus=true`;
- keep `QUERY_CLASS_GATED` as a candidate token only.

Rejected design:

- editing external Policy_Local files;
- changing EC gate values or retrieval behavior;
- adding OCR/provider dependencies;
- treating RDA-T2 as metadata truth, legal status, production readiness, or
  public readiness.

## Dispatch Boundary

This baseline authorizes dispatch of a source-verified RDA-T2 work order only.
The worker may implement local deterministic CPF source/tests inside the work
order's allowed scope. Any need to touch Policy_Local, EC activation,
retrieval, OCR, provider/API-key paths, public-sync, or readiness claims
returns to Orchestrator.

## Acceptance Criteria

1. New helper emits deterministic `DscpMetadataRequirement` declarations for
   regulated profiles.
2. Non-regulatory profiles do not inherit regulated lifecycle fields.
3. Requirement owner IDs match the source profile ID.
4. The existing bridge validates generated requirements.
5. Invalid profile combinations fail closed with explicit tokens.
6. Focused CPF tests cover regulated pass, non-regulatory no-op, and failure
   cases.
7. No external Policy_Local or EC gate value changes occur.

## Evidence / Verification

Required verification:

- focused CPF tests for the adapter helper;
- `npm run check` or the local CPF TypeScript check command if available;
- GC-051 registry check after adding source/test files;
- reviewer-fast before Codex closure review;
- pre-closure autorun gate before final closed claim.

Observed verification:

- `npm run check` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION`: PASS.
- `npm run test -- tests/dscp.regulated.domain.adapter.test.ts`: PASS
  16/16.
- `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast`:
  PASS 11/11.

## Claim Boundary

This baseline authorizes local deterministic adapter implementation only. It
does not prove metadata truth, legal/current status, source authenticity,
Policy_Local readiness, EC activation, retrieval quality, provider behavior,
production readiness, public readiness, or autonomous correction.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private implementation dispatch baseline; no public-sync authorized.
