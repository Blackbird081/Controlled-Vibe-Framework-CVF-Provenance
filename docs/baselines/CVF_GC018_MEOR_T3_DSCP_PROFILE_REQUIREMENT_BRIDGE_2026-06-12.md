# CVF GC-018 Baseline: MEOR-T3 DSCP Profile Requirement Bridge

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-12

Author: Codex

baseHead: `472c474d`

## Purpose

Authorize a bounded control-plane implementation that lets each DSCP domain
profile declare its own metadata requirements and exposes a validated owner
map for the MEOR-T2 evaluator.

## Scope / Target / Owner Boundary

Target owner: `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION`.

Allowed:

- one optional profile-scoped requirement declaration field;
- one deterministic requirement bridge module;
- one focused test module;
- barrel exports, GC-051, roadmap, completion, and continuity updates.

Forbidden:

- global metadata requirements or domain defaults;
- metadata value inference, descriptor mutation, or gate activation;
- changes to external Policy_Local, LPCI, EC, extraction evaluation, or report
  rendering;
- provider/API-key use, OCR, corpus ingestion, retrieval, or public-sync.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Result |
| --- | --- | --- | --- |
| MEOR-T1 contract | `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_CONTRACT_2026-06-12.md` | `f3c7ff11` | PASS |
| MEOR-T2 implementation | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/metadata_evidence.py` | `d18a3e47` | PASS |
| MEOR-T2 completion | `docs/reviews/CVF_MEOR_T2_EXTRACTION_METADATA_FINDING_NORMALIZATION_COMPLETION_2026-06-12.md` | `69ec7574` | PASS |
| Session sync | active handoff/state/memory | `472c474d` | PASS |

## Source Verification Summary

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Profile identity | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | lines 7-8, 23-28 | `DomainProfileId`, `domainProfileId` | DSCP profile contract | ACCEPT |
| Profile metadata maps | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | lines 33-49 | `commonFacetFields`, `domainFacetFields`, `defaultMetadata` | `DscpDomainProfile` | ACCEPT |
| Explicit profile application | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | lines 19-22, 96-100 | `applyDomainProfileToDescriptorInput` | function | ACCEPT |
| Context barrel | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts` | lines 77-98 | DSCP profile exports | barrel | ACCEPT |
| T1 requirement ownership | `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_CONTRACT_2026-06-12.md` | `Canonical Record`, `Profile Ownership` | `requirementId`, `ownerProfileId` | canonical contract | ACCEPT |

## Decision

Add optional `metadataRequirements` declarations to each profile and validate
them through a separate pure bridge. The bridge must reject empty identifiers,
duplicate requirement IDs, owner mismatches, empty acceptable-evidence sets,
and unsupported evidence values. It must not read or mutate descriptor data.

## Required Evidence

- focused tests for empty, duplicate, mismatched-owner, and invalid-evidence
  declarations;
- deterministic owner-map and declaration-list results;
- proof that omitted requirements produce an empty valid bridge result;
- proof that input profile/declaration objects are not mutated;
- TypeScript check, focused vitest, full control-plane tests, reviewer-fast,
  and closure gates.

## Closure Evidence

- material commit: `0c4997a5`;
- focused vitest: 12/12 PASS;
- full control-plane suite: 143 files / 3712 tests PASS;
- TypeScript check: PASS;
- source and test sizes: 155 and 153 lines;
- descriptor/profile application behavior changes: none.

## Claim Boundary

This baseline authorizes profile declaration and validation only. It does not
prove metadata truth, source authenticity, domain eligibility, report quality,
gate behavior, retrieval, Policy_Local readiness, production readiness, or
public readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundation implementation; no public-sync authorized.
