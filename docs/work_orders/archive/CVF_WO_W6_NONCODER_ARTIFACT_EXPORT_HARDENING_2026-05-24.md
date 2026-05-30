# CVF Work Order W6 Noncoder Artifact Export Hardening

Memory class: SUMMARY_RECORD

Status: DISPATCHED_W6_NONCODER_ARTIFACT_EXPORT_HARDENING

docType: work_order

Date: 2026-05-24

---

## Purpose

Implement W6 by adding deterministic artifact verification/provenance metadata
to the existing noncoder deliverable pack and markdown export.

## Authority Chain

- Operator instruction: continue the roadmap in priority order and commit each
  completed part.
- W5 closure:
  `docs/reviews/CVF_W5_PROVIDER_METHOD_FALLBACK_NORMALIZATION_COMPLETION_2026-05-24.md`
- WC roadmap:
  `docs/roadmaps/CVF_WC_WORKFLOW_CHAIN_AND_PAIN_POINT_ROADMAP_2026-05-24.md`
- W6 GC-018:
  `docs/baselines/CVF_GC018_W6_NONCODER_ARTIFACT_EXPORT_HARDENING_2026-05-24.md`

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Orchestrator | Keep W6 product-facing and commit authorization/closure separately. |
| Legacy Source Extractor | Reuse md2html verification/provenance concepts without opening renderer scope. |
| Implementer | Extend `deliverable-pack.ts` and focused tests. |
| QA | Run focused tests, TypeScript check, and session/docs guards. |
| Skeptic/Auditor | Reject fake evidence, risk downgrade, public-readiness, and renderer claims. |
| Product/Operator Advocate | Ensure exported pack is clearer for noncoders and handoff recipients. |
| Safety/Boundary Owner | Confirm missing receipts and failed checks remain visible. |

## Scope / Allowed Scope / Forbidden Scope

Allowed files:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/deliverable-pack.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/deliverable-pack.test.ts`
- W6 completion review, WC roadmap, session state, and handoff updates

Forbidden files/classes:

- `/api/execute`, provider routing, Model Gateway, receipt-envelope schema;
- new HTML/PDF renderer or ArtifactExportPanel replacement;
- auth/RBAC, memory reinjection, public-sync, hosted/production/freeze-release
  surfaces.

## Required First Reads

- W6 GC-018
- WC-3 map
- WC-4 blind-spot standard
- W130 export activation contract
- `deliverable-pack.ts` and focused tests
- md2html/Human System Harness source files listed in W6 GC-018

## Pre-Flight Checks

- Confirm W5 is closed.
- Confirm W6 Control Block is CLEAR.
- Confirm no live proof is needed for local serialization-only work.

## Write Ownership

Implementation ownership:

- `deliverable-pack.ts`
- `deliverable-pack.test.ts`

Documentation ownership:

- W6 completion review
- WC roadmap/session/handoff progress updates

## Execution Plan

1. Add pack artifact verification/provenance types.
2. Generate deterministic checks from output, scope boundary, receipt, and
   handoff fields.
3. Serialize verification/provenance into markdown.
4. Add focused tests for PASS and PASS_WITH_WARNINGS.
5. Run focused tests and TypeScript check.
6. File completion and commit.

## Evidence Requirements

- focused deliverable-pack tests PASS;
- `npm run check` in `cvf-web` PASS;
- docs/session guards PASS;
- completion packet includes Evidence Trace and claim boundary.

## Acceptance Criteria

- [ ] Pack includes artifact verification/provenance metadata.
- [ ] Missing receipt is visible as warning, not upgraded to proof.
- [ ] Markdown export includes an Artifact Verification section.
- [ ] Existing pack sections remain compatible.
- [ ] Focused tests and TypeScript check PASS.

## Review Gate

Reject W6 if it invents evidence, hides failed checks, changes governance
receipt schema, opens a new renderer, or claims public/production readiness.

## Closure Checklist

- [ ] Authorization commit created before implementation.
- [ ] Pack metadata implemented and tested.
- [ ] Completion review filed.
- [ ] Roadmap/session/handoff updated.
- [ ] Closure commit created.

## Return-To-Orchestrator Conditions

Return instead of closing if useful hardening requires HTML renderer changes,
receipt-envelope changes, live provider proof, or public catalog graduation.

## Operator Checkpoint

operator.checkpoint.waiver: W6 is local pack serialization hardening with no
provider, route, receipt-envelope, or public claim expansion.

## Claim Boundary

This work order authorizes only local deliverable-pack verification/provenance
metadata. It does not authorize new renderer/runtime behavior, public-sync,
provider behavior, live governance proof, hosted readiness, production
readiness, or freeze release.
