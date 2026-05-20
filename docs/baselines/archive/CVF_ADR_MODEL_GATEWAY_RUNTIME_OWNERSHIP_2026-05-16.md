<!-- Memory class: SUMMARY_RECORD -->

# ADR Candidate - CVF Model Gateway Runtime Ownership - 2026-05-16

Status: ACCEPTED FOR LOCAL IMPLEMENTATION - uncommitted working state pending
operator review.

Related authorization:
`docs/baselines/CVF_GC018_MODEL_GATEWAY_RUNTIME_AUTHORIZATION_2026-05-16.md`

Related roadmap:
`docs/roadmaps/CVF_MODEL_GATEWAY_RUNTIME_ADOPTION_ROADMAP_2026-05-16.md`

## Context

`EXTENSIONS/CVF_MODEL_GATEWAY/` is currently the approved `B* Merge 3`
wrapper/re-export package for runtime adapter hub and external integration
entrypoints.

The CVF 16.5 intake and Claude rebuttal identified 8 useful TypeScript gateway
artifacts in:

`.private_reference/legacy/CVF 16.5/freellmapi/`

Those artifacts cover provider registry, provider health, quota ledger, routing
policy, fallback policy, sticky session, credential boundary, and gateway
receipt.

## Decision

Decision: **implementation-owner upgrade**.

`EXTENSIONS/CVF_MODEL_GATEWAY/` should become the implementation owner for the
adapted gateway runtime primitives in this tranche, while preserving lineage to
`CVF_v1.7.3_RUNTIME_ADAPTER_HUB` and `CVF_v1.2.1_EXTERNAL_INTEGRATION`.

## Alternatives

### Wrapper-only-kept

Rejected for this tranche unless roadmap review finds a hard blocker.

Reason: wrapper-only would keep the current package shape but would not satisfy
the runtime adoption goal. The 8 legacy artifacts would remain references only,
and future agents would still be likely to rewrite or misplace gateway logic.

### New Gateway Package

Rejected.

Reason: CVF already has `EXTENSIONS/CVF_MODEL_GATEWAY/`. A second gateway would
create owner ambiguity and contradict the intake rebuttal.

## Consequences

Implementation-owner upgrade requires:

- adapted CVF-owned source files, not wholesale source copy;
- Guard Contract integration;
- vitest coverage for every adopted runtime primitive;
- package-level `npm run check` and `npm test`;
- GC-023 split discipline for any file approaching governed thresholds;
- live governance proof before enforcement claims.

The upgrade does not authorize:

- free-provider or bypass claims;
- hidden model substitution;
- public-facing provider claims without evidence;
- raw credential logging or browser key storage;
- live governance enforcement claims from unit tests alone.

## Implementation Note

Initial local implementation was added under `EXTENSIONS/CVF_MODEL_GATEWAY/`
on 2026-05-16. The package now preserves the original wrapper/re-export
lineage while owning adapted gateway runtime primitives for provider registry,
provider health, quota ledger, routing policy, fallback policy, sticky session,
credential boundary, and gateway receipt.

The implementation remains uncommitted because the operator requested continued
work without committing while Claude's rerun is pending.

## ADR Finalization Gate

This ADR is accepted for the local implementation tranche. Public or release
claims still require the closure packet and the relevant verification evidence.
