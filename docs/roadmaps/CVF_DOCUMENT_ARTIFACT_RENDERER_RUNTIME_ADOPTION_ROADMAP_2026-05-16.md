Memory class: ROADMAP

# CVF Document Artifact Renderer Runtime Adoption Roadmap - 2026-05-16

Status: completed.

## Purpose

Move the CVF 16.5 Document Artifact Renderer lane from `docs-classified` to
`runtime-owned`.

## Scope

This roadmap covers the first deterministic Control Plane primitive for governed
Markdown-to-HTML artifact rendering.

## Source

Source bundle:

- `.private_reference/legacy/CVF 16.5/md2html`

## Baseline

CVF had renderer policy ideas and review notes, but not an executable owner
surface.

## Authorization / Decision

Authorized by the operator instruction to continue the CVF 16.5 absorption
roadmap autonomously and make selected knowledge live inside CVF.

Decision: implement the first renderer primitive in Control Plane rather than
opening a new extension root.

## Non-Goals

This roadmap does not deliver:

- production renderer UI;
- remote preview service;
- PNG/PDF/PPTX/social export;
- live provider proof;
- new audit evidence generation.

## Work Plan

| Step | Action | Status |
|---|---|---|
| 1 | Create GC-018 authorization and ADR | complete |
| 2 | Write source adoption matrix and proof plan | complete |
| 3 | Implement Control Plane renderer contract | complete |
| 4 | Add focused Vitest coverage | complete |
| 5 | Update living integration summary and handoff | complete |
| 6 | Run package and governance verification | complete |

## Acceptance Criteria

The tranche is accepted when:

- the renderer contract exists in Control Plane;
- focused tests cover metadata, claim boundary, component catalog, security
  blocks, sandbox preview note, and determinism;
- Control Plane typecheck passes;
- full package Vitest passes;
- governed file-size and markdown structural guards pass;
- full pre-push chain passes before push.

## Evidence

Owner files:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/document.artifact.renderer.contract.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/document.artifact.renderer.contract.test.ts`

Governance files:

- `docs/baselines/CVF_GC018_DOCUMENT_ARTIFACT_RENDERER_AUTHORIZATION_2026-05-16.md`
- `docs/baselines/CVF_ADR_DOCUMENT_ARTIFACT_RENDERER_RUNTIME_OWNERSHIP_2026-05-16.md`
- `docs/baselines/CVF_DOCUMENT_ARTIFACT_RENDERER_SOURCE_ADOPTION_MATRIX_2026-05-16.md`
- `docs/baselines/CVF_DOCUMENT_ARTIFACT_RENDERER_TEST_AND_PROOF_PLAN_2026-05-16.md`

## Verification

Verification recorded in the closure packet:

- Control Plane `npm run check` PASS;
- focused renderer Vitest PASS, 1 file / 14 tests;
- full Control Plane Vitest PASS, 124 files / 3404 tests;
- governed file-size guard PASS;
- markdown structural completeness PASS;
- docs governance compatibility PASS.

## Claim Boundary

This roadmap closes the first renderer primitive only. It does not ship a public
HTML renderer app or change canonical CVF source documents.
