# ADR: Context Profile Advisory Metadata

Date: 2026-05-17

## Purpose

Define the relationship between ADD-B `ContextProfile` metadata and existing
Control Plane context, knowledge, and policy surfaces.

## Decision

`ContextProfile` is an advisory record owned by Control Plane Foundation. It
helps Context Builder rank existing source IDs, apply context budget hints,
preserve reinjection approval hints, and surface evidence sensitivity for
upstream policy validation.

The profile does not create a source registry. `sourceRelevance.sourceId` and
`reinjectionEligibility.sourceId` must refer to source IDs already owned by
the relevant knowledge or intake surface.

Restricted `evidenceSensitivity` is represented as a
`requiresPolicyValidation` flag in the builder output. The flag is intentionally
not runtime enforcement; the caller or Policy Engine integration must act on
it.

## Consequences

- Context assembly can become more deterministic without adding execution
  authority.
- Policy-sensitive evidence handling is visible as a typed signal instead of
  hidden convention.
- Knowledge intake remains the owner of source identity and source metadata.
- No prompt injection, approval, routing, or provider behavior changes are
  introduced by this ADR.
