Memory class: GOVERNANCE_BASELINE

# CVF Document Artifact Renderer Source Adoption Matrix - 2026-05-16

Status: active matrix for the Artifact Renderer absorption tranche.

## Purpose

Map CVF 16.5 renderer source ideas to CVF-owned implementation behavior.

## Scope

This matrix covers only the first Control Plane runtime adoption.

## Source

| Source item | CVF adoption |
|---|---|
| Rendering policy | Preserve source meaning, risk, approval, failed checks, and claim boundary |
| Rendering protocol | Resolve input, classify type, render HTML, verify, attach metadata |
| Component catalog | Allowlist components and reject forbidden governance-bypassing widgets |
| Template spec | Single-file offline HTML with metadata, claims, content, verification, provenance |
| Verification checklist | Runtime verification checks produce PASS, PASS_WITH_WARNINGS, or FAIL |
| Sandboxed preview lesson | Preview note and adapter-origin boundary are explicit |
| Agent/CLI adapter lesson | Adapter origin is metadata only and never trust authority |
| Export surface lesson | HTML only in this tranche; PNG/PDF/PPTX/social export deferred |

## Baseline

Prior state was documentation-only classification.

## Classification

Fit: Medium/High.

Adoption state after implementation: `runtime-owned`.

## Evidence

Runtime owner:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/document.artifact.renderer.contract.ts`

Test owner:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/document.artifact.renderer.contract.test.ts`

## Verification

The focused tests must cover metadata, verification, security blocks, claim
boundary preservation, adapter boundary, and deterministic IDs.

## Claim Boundary

The source is adapted into CVF semantics. It is not copied as a generic
Markdown-to-HTML converter.
