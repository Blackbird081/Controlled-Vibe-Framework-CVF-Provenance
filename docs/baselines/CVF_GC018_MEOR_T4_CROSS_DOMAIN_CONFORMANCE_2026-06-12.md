# CVF GC-018 Baseline: MEOR-T4 Cross-Domain Conformance

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-06-12

Author: Codex

baseHead: `7b2204dc`

## Purpose

Authorize a bounded conformance tranche that proves the MEOR contract and DSCP
requirement bridge preserve profile ownership across legal-policy and
technical-project synthetic fixtures.

## Scope / Target / Owner Boundary

Target owners:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` for profile declaration checks;
- `EXTENSIONS/CVF_EXTRACTION_FOUNDATION` for evidence evaluation checks;
- `docs/reference` for one shared machine-readable synthetic fixture.

Allowed:

- one shared JSON fixture;
- one focused TypeScript conformance test;
- one focused Python conformance test;
- registry, completion, roadmap, and continuity updates.

Forbidden:

- runtime source changes;
- real Policy_Local files, candidate identifiers, or legal metadata;
- new global defaults, metadata inference, profile mutation, or gate
  activation;
- OCR, corpus ingestion, retrieval, provider/API-key use, or public-sync.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Result |
| --- | --- | --- | --- |
| MEOR-T1 semantics | `docs/reference/CVF_METADATA_EVIDENCE_AND_OPERATOR_RESOLUTION_SEMANTICS_2026-06-12.json` | `f3c7ff11` | PASS |
| MEOR-T2 evaluator | `EXTENSIONS/CVF_EXTRACTION_FOUNDATION/src/metadata_evidence.py` | `d18a3e47` | PASS |
| MEOR-T3 bridge | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.metadata.requirement.bridge.ts` | `0c4997a5` | PASS |
| MEOR-T3 completion | `docs/reviews/CVF_MEOR_T3_DSCP_PROFILE_REQUIREMENT_BRIDGE_COMPLETION_2026-06-12.md` | `5f328d11` | PASS |
| Session sync | active handoff/state/memory | `7b2204dc` | PASS |

## Source / Predecessor Evidence

- T1 locks the exact observed-state, evidence-basis, resolution-state,
  downstream-disposition, and failure-token values.
- T2 implements deterministic evaluation and cross-profile rejection in
  Python.
- T3 implements profile-scoped declarations, deterministic owner maps, and
  owner-mismatch rejection in TypeScript.
- T3 closure and the dedicated session sync release T4 without releasing T5 or
  any downstream adapter/use-case lane.

## Decision

Use one repository-owned JSON fixture as the shared authority for both language
test suites. The fixture must declare two disjoint profiles and four synthetic
cases: resolved, unresolved, conflict, and not-applicable. It must contain no
raw content and no real use-case records.

## Required Evidence

- exact legal-policy and technical-project requirement sets;
- negative assertions that neither requirement set appears in the other
  profile result;
- owner-mismatch rejection in both implementation surfaces;
- exact resolution and downstream disposition for all four cases;
- JSON parse, focused tests, full package tests, TypeScript check,
  reviewer-fast, and closure gates.

## Closure Evidence

- material commit: `bfd38775`;
- focused TypeScript conformance: 4/4 PASS;
- focused Python conformance: 6/6 PASS;
- full control-plane suite: 144 files / 3716 tests PASS;
- full extraction-foundation suite: 82/82 tests PASS;
- TypeScript check: PASS;
- runtime source edits: none.

## Claim Boundary

This baseline authorizes deterministic synthetic conformance only. It does not
prove metadata truth, source authenticity, domain expertise, Policy_Local
integration, gate activation, retrieval quality, provider behavior,
production readiness, or public readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private foundation conformance; no public-sync authorized.
