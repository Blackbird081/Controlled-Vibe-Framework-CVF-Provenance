# CVF GC-018 VI5-T4/T5 Surface 1 Export Acceptance And Portable Handoff

Memory class: BASELINE_RECORD

docType: baseline

Date: 2026-05-26

Status: APPROVED

## Purpose

Authorize the bounded VI5-T4/T5 implementation for Surface 1
`app_builder_complete` English markdown export readiness.

## Source / Predecessor Evidence

- `docs/reviews/CVF_SURFACE1_WEB_EXPORT_RENDERER_TRACE_AND_LEAK_INVENTORY_2026-05-26.md`
- `docs/reviews/CVF_VI5_SURFACE_FIDELITY_CODEX_RESPONSE_2026-05-26.md`
- Operator instruction on 2026-05-26 to complete VI5-T4 and VI5-T5 before a
  single real non-coder web export plus external-agent review.

## Decision / Baseline / Proposed Tranche

Baseline: Surface 1 web export had been corrected for deterministic English
chrome, but the exported packet still needed an explicit external-agent
handoff readiness frame for the operator's acceptance test.

Proposed tranche: implement VI5-T4/T5 as a bounded deterministic renderer
change, then stop at `READY_FOR_OPERATOR_ACCEPTANCE`.

## Scope / Target / Owner Boundary

Owner surface:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/SpecExport.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/spec-export-portable-handoff.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/template-i18n.ts`

Allowed changes:

- deterministic export content;
- focused tests;
- roadmap/work-order/completion docs;
- handoff/session state updates.

Blocked changes:

- `/api/execute` route behavior;
- provider/model adapters;
- receipt envelope schema;
- live governance benchmarks;
- broad template catalog changes;
- cross-agent memory auto-load implementation.

## Surface Fidelity Control Block

| Control | Result |
| --- | --- |
| Surface verified | Surface 1 web export markdown |
| Previous wrong target avoided | yes; Surface 2 `englishSpecFreeze` is not the target |
| Audience verified | non-coder operator and external agent |
| Language invariant | English packet chrome, original user source values preserved |
| Operator test dependency | final acceptance remains pending operator manual export/review |

## Knowledge Absorption Blind-Spot Control Block

This tranche does not absorb external knowledge. It continues the already
verified Surface 1 renderer trace from
`docs/reviews/CVF_SURFACE1_WEB_EXPORT_RENDERER_TRACE_AND_LEAK_INVENTORY_2026-05-26.md`.

| Control | Result |
| --- | --- |
| Prior absorption evidence resolved | yes; no new external source intake |
| Detailed source files read | `SpecExport.tsx`, `template-i18n.ts`, current exported sample |
| Accept/defer/reject dispositions | accept bounded portable handoff block; defer all-template coverage |
| Adversarial role review | require tests to preserve source values and reject chrome leakage |
| Blind-spot delta | low; remaining blind spot is operator/external-agent subjective acceptance |

## Required Proof

- `npm run test:run -- src/components/SpecExport.test.tsx src/lib/template-i18n.test.ts`
- `npm run check`

## Claim Boundary

Approved claim is bounded to deterministic export readiness. The operator's
external-agent test is the acceptance surface for whether the exported spec is
actually understandable enough outside CVF.

## Evidence / Verification

Required verification is deterministic only:

- focused `SpecExport` and `template-i18n` tests;
- `npm run check`;
- docs governance and active-session checks;
- operator manual acceptance after a fresh web export.
