Memory class: GOVERNANCE_BASELINE

# CVF GC-018 Document Artifact Renderer Authorization - 2026-05-16

Status: candidate authorized by operator instruction to continue CVF 16.5
knowledge absorption autonomously until selected knowledge is living in CVF.

## Purpose

Authorize a bounded runtime adoption tranche for the CVF 16.5 `md2html`
Document Artifact Renderer material.

## Scope

This tranche may add a Control Plane contract that renders and verifies governed
HTML review artifacts from Markdown source input.

In scope:

- source resolution metadata;
- document type classification;
- approved component catalog enforcement;
- single-file HTML output;
- claims boundary, risk, approval, failed-check, and provenance visibility;
- sandbox preview note and adapter-origin boundary;
- deterministic tests.

Out of scope:

- live provider calls;
- web editor runtime;
- PNG/PDF/PPTX/social export;
- artifact publication pipeline;
- changing CVF governance decisions.

## Source

Primary source:

- `.private_reference/legacy/CVF 16.5/md2html`

Relevant files:

- `CVF_ARTIFACT_RENDERING_POLICY.md`
- `CVF_ARTIFACT_RENDERING_PROTOCOL.md`
- `CVF_ARTIFACT_COMPONENT_CATALOG.md`
- `CVF_ARTIFACT_TEMPLATE_SPEC.md`
- `CVF_ARTIFACT_VERIFICATION_CHECKLIST.md`

## Baseline

The prior state was `docs-classified`: CVF understood the value of governed
artifact rendering but had no owner code enforcing the rules.

## Decision

Proceed with Control Plane ownership rather than creating a new extension
package. This keeps the first tranche small and makes artifact rendering a
governed contract instead of a standalone converter.

## Evidence

Expected evidence:

- new Control Plane source file;
- focused Vitest coverage;
- Control Plane package typecheck;
- governed file-size guard;
- full pre-push chain.

## Verification

Verification must prove deterministic local behavior only. No live provider test
is required because this tranche does not assert provider or live governance
enforcement.

## Claim Boundary

Passing this tranche may claim `runtime-owned` Document Artifact Renderer
primitive. It may not claim production artifact publishing, visual UI preview,
or live evidence generation.
