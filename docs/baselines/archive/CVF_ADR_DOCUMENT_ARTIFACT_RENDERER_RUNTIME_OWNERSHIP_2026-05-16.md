Memory class: GOVERNANCE_BASELINE

# CVF ADR Document Artifact Renderer Runtime Ownership - 2026-05-16

Status: accepted for bounded CVF 16.5 absorption.

## Purpose

Record the owner decision for the first living Document Artifact Renderer
primitive.

## Scope

This ADR covers one deterministic TypeScript contract in:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/`

## Source

Source influence:

- CVF 16.5 `md2html` renderer protocol and policy;
- the additional html-anything lessons captured in intake notes: sandboxed
  preview, adapter-origin boundary, and hard anti-slop constraints.

## Baseline

Creating `EXTENSIONS/CVF_DOCUMENT_ARTIFACT_RENDERER/` would be accurate but
heavier than needed for the first tranche. The public value is in verifying
claims/evidence visibility, not in shipping a new renderer app.

## Context

The operator requested that absorbed knowledge must become living CVF behavior.
For this lane, the smallest living behavior is a contract that can render and
verify governed artifacts without changing source truth.

## Alternatives

Alternative A: create a new extension root.

Disposition: deferred because it adds lifecycle overhead before a product UI or
export service exists.

Alternative B: keep the lane documentation-only.

Disposition: rejected because the user explicitly asked that selected knowledge
must not remain dormant.

Alternative C: implement in Control Plane.

Disposition: accepted for the first tranche.

## Decision

Control Plane owns the first runtime primitive:

- `document.artifact.renderer.contract.ts`

Rationale:

- artifact rendering is governance-adjacent;
- the first value is source/evidence/claim preservation;
- package-level checks already exist;
- future UI or export lanes can consume this contract later.

## Consequences

Positive:

- the knowledge becomes executable and testable;
- claim boundary, risk, approval, and failed checks become runtime fields;
- no new extension lifecycle registration is needed.

Tradeoff:

- this is not a full md2html clone or visual editor.

## Evidence

Evidence is recorded in the lane closure packet.

## Verification

The owner package must pass typecheck and focused contract tests.

## Claim Boundary

This ADR does not authorize a production renderer service. It authorizes a
bounded Control Plane primitive for governed artifact presentation.
