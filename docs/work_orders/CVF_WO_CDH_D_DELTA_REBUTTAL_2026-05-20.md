# CVF Work Order — CDH-D Delta Rebuttal

Memory class: SUMMARY_RECORD

Status: READY_FOR_REBUTTAL_EXECUTION

GC-018 required: No — reviewer rebuttal only. Any later implementation needs
a fresh CDH-D-specific GC-018 for exactly one selected D sub-surface and a
separate implementation work order.

## Authority Chain

- Active session state:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Active review queue item: `cdh-d-delta`
- CDH delta meta-roadmap:
  `docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md#per-slice-section-d`
- Original CDH blocking rebuttal:
  `docs/reviews/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
- D2 completion anchor:
  `docs/reviews/CVF_D2_VISION_CONTRACT_COMPLETION_2026-05-19.md`
- Lane D provider-method parity evidence:
  `docs/reviews/CVF_LANE_D_PROVIDER_METHOD_PARITY_COMPLETION_2026-05-19.md`

## Agent Roles

- Operator: selects CDH-D as a remaining CDH delta slice.
- Codex reviewer: performs the read-only CDH-D rebuttal and files the rebuttal
  packet.
- Orchestrator: may file a later GC-018 only if the rebuttal returns a
  non-blocking disposition and names exactly one D sub-surface.
- Worker: must not implement anything from this work order.

## Purpose

Produce the reviewer-role rebuttal for the CDH-D delta slice.

The rebuttal must prevent provider-method claim bundling by separating:

1. Vision contract — typed shape only, no provider call.
2. Vision runtime — provider call plus audit-event capture.
3. Reasoning contract — typed shape only, no runtime claim.

Reasoning runtime is out of scope for this CDH-D delta.

## Scope

Allowed scope:

- Read-only review of the CDH-D slice in the delta meta-roadmap.
- Read-only review of current model-gateway vision/reasoning contract source
  and tests.
- Read-only review of D2 and Lane D completion evidence.
- Filing one rebuttal packet at:
  `docs/reviews/CVF_CDH_D_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- Updating `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` and
  `CVF_SESSION/ACTIVE_SESSION_STATE.json` after the rebuttal is filed.
- Updating `AGENT_HANDOFF_V10_2026-05-19.md` only if needed for continuity.

Forbidden scope:

- No implementation.
- No GC-018 baseline for implementation.
- No bundled D implementation.
- No vision runtime claim from contract-only evidence.
- No reasoning runtime.
- No Maika photo proof unless a later vision-runtime GC-018 separately
  authorizes it.
- No hidden provider routing change.
- No public-sync or public claim update.

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
2. `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
3. `docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md`
4. `docs/reviews/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
5. `docs/reviews/CVF_LANE_D_PROVIDER_METHOD_PARITY_COMPLETION_2026-05-19.md`
6. `docs/baselines/CVF_GC018_D2_VISION_CONTRACT_2026-05-19.md`
7. `docs/reviews/CVF_D2_VISION_CONTRACT_COMPLETION_2026-05-19.md`
8. `EXTENSIONS/CVF_MODEL_GATEWAY/src/vision-contract.ts`
9. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/vision-contract.test.ts`
10. `EXTENSIONS/CVF_MODEL_GATEWAY/src/reasoning-contract.ts`
11. `EXTENSIONS/CVF_MODEL_GATEWAY/tests/reasoning-contract.test.ts`
12. `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`

## Pre-Flight Checks

Before writing the rebuttal, Codex must verify:

- `cdh-d-delta` remains a `READY_FOR_REBUTTAL` item.
- D2 completion evidence is contract/type-only and does not claim vision
  runtime.
- Vision contract source/tests contain no provider implementation or image
  fetch.
- Reasoning contract source/tests, if present, are contract-only.
- Any proposed continuation names exactly one of the three D sub-surfaces.

## Write Ownership

Codex reviewer may create:

- `docs/reviews/CVF_CDH_D_DELTA_CODEX_REBUTTAL_2026-05-20.md`

Codex reviewer may update:

- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V10_2026-05-19.md`

Codex reviewer must not modify:

- `EXTENSIONS/CVF_MODEL_GATEWAY/src/*`
- `EXTENSIONS/CVF_MODEL_GATEWAY/tests/*`
- `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/*`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- Any Maika, provider runtime, public-sync, or CLI file.

## Execution Plan

1. Confirm active queue order and CDH-D scope.
2. Read the CDH-D meta-roadmap section and original CDH blocking finding 3.
3. Read Lane D and D2 completion evidence.
4. Inspect current vision and reasoning contract source/tests.
5. Decide one of:
   - `NON_BLOCKING_WITH_SUBSURFACE_SPLIT`
   - `NON_BLOCKING_WITH_EXISTING_EVIDENCE`
   - `BLOCKING`
6. If non-blocking, state which sub-surface may proceed next and what remains
   gated separately.
7. File the rebuttal packet with findings, risks, required corrections, and
   explicit claim boundary.
8. Update active review queue/state/handoff routing.
9. Run JSON parse and active-session state checks.
10. Run docs governance and Markdown structural checks if new docs were filed.

## Tasks

- [ ] Confirm queue status for `cdh-d-delta`.
- [ ] Verify D2 is contract-only.
- [ ] Verify D must remain split into vision contract, vision runtime, and
  reasoning contract.
- [ ] Verify reasoning runtime is out of scope.
- [ ] Verify Maika photo proof remains out of scope unless vision runtime is
  separately accepted later.
- [ ] Decide whether any D sub-surface may proceed to a later GC-018. If yes,
  name exactly one and state why the other two are deferred.
- [ ] File rebuttal at
  `docs/reviews/CVF_CDH_D_DELTA_CODEX_REBUTTAL_2026-05-20.md`.
- [ ] Update active queue/state routing.
- [ ] Run required verification.

## Acceptance Criteria

The rebuttal is acceptable only if it:

- Names the disposition clearly.
- Explicitly splits D into the three sub-surfaces.
- States that contract-only work cannot claim runtime behavior.
- Excludes reasoning runtime.
- Excludes Maika photo proof unless a later vision-runtime GC-018 authorizes
  it.
- Does not authorize implementation by itself.
- Requires a later CDH-D-specific GC-018 for exactly one selected sub-surface.

## Evidence Requirements

The rebuttal must cite:

- CDH-D meta-roadmap section.
- Original CDH rebuttal Finding 3.
- Lane D completion review.
- D2 completion review.
- Current vision contract source/test inspection.
- Current reasoning contract source/test inspection, if present.

If the rebuttal recommends continuation, it must list seed acceptance criteria
for the later GC-018, including:

- selected D sub-surface is named before GC-018;
- contract-only work has type/test evidence and no provider call;
- vision runtime work has live provider evidence and audit capture;
- reasoning runtime remains excluded;
- completion review states exact provider/runtime claim boundary.

## Review Gate

Stop and return `BLOCKING` if any of these are true:

- D continuation bundles contract-only and runtime claims.
- D continuation claims live vision behavior from D2 contract evidence.
- D continuation includes reasoning runtime.
- D continuation uses Maika photo proof without a separate vision-runtime
  gate.
- D continuation requires hidden provider routing changes.
- D continuation cannot name a single selected sub-surface.

## Closure Checklist

- [ ] Rebuttal packet filed.
- [ ] Queue item status updated.
- [ ] State registry next move updated.
- [ ] Handoff updated if continuity needs it.
- [ ] JSON parse passes for changed registry files.
- [ ] `python governance/compat/check_active_session_state.py --enforce`
  passes.
- [ ] `python governance/compat/check_docs_governance_compat.py` passes.
- [ ] `python governance/compat/check_markdown_structural_completeness.py`
  passes.

## Return-To-Orchestrator Conditions

Return without filing a non-blocking rebuttal if:

- current model-gateway source cannot be inspected;
- D2 evidence is contradicted by current source;
- a continuation cannot separate contract and runtime claims;
- a continuation requires reasoning runtime;
- a continuation requires provider routing changes outside the selected
  sub-surface.

## Claim Boundary

This work order authorizes only a reviewer-role rebuttal. It does not authorize
implementation, GC-018 filing, provider runtime behavior, Maika photo proof,
reasoning runtime, public claims, or CDH closure.
