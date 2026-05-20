# CVF Work Order — CDH-H Delta Rebuttal

Memory class: SUMMARY_RECORD

Status: READY_FOR_REBUTTAL_EXECUTION

GC-018 required: No — reviewer rebuttal only. Any later implementation needs
a fresh CDH-H-specific GC-018 and a separate implementation work order.

## Authority Chain

- Active session state:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Active review queue item: `cdh-h-delta`
- CDH delta meta-roadmap:
  `docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md#per-slice-section-h`
- Original CDH blocking rebuttal:
  `docs/reviews/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
- H2 completion anchor:
  `docs/reviews/CVF_H2_AUDIT_MEMORY_POLICY_REFINEMENT_COMPLETION_2026-05-19.md`

## Agent Roles

- Operator: selects CDH-H as the next slice for review.
- Codex reviewer: performs the read-only CDH-H rebuttal and files the rebuttal
  packet.
- Orchestrator: may file a later GC-018 only if the rebuttal returns a
  non-blocking disposition.
- Worker: must not implement anything from this work order.

## Purpose

Produce the reviewer-role rebuttal for the CDH-H delta slice.

The rebuttal must decide whether the H delta may proceed to a slice-specific
GC-018 and implementation work order for audit-memory receipt policy/readout
hardening, while preserving the capture-vs-reinjection boundary.

## Scope

Allowed scope:

- Read-only review of the CDH-H slice in the delta meta-roadmap.
- Read-only review of existing audit-memory receipt source and tests.
- Read-only review of H2 baseline/completion evidence.
- Filing one rebuttal packet at:
  `docs/reviews/CVF_CDH_H_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- Updating `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` and
  `CVF_SESSION/ACTIVE_SESSION_STATE.json` after the rebuttal is filed.
- Updating `AGENT_HANDOFF_V10_2026-05-19.md` only if needed for continuity.

Forbidden scope:

- No implementation.
- No GC-018 baseline for implementation.
- No route, provider, memory-runtime, or receipt-envelope changes.
- No persistent/archive memory enablement.
- No prompt reinjection or context reinjection.
- No new memory tier.
- No frozen memory-policy rewrite.
- No public-sync or public claim update.

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
2. `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
3. `docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md`
4. `docs/reviews/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
5. `docs/baselines/CVF_GC018_H2_AUDIT_MEMORY_POLICY_REFINEMENT_2026-05-19.md`
6. `docs/reviews/CVF_H2_AUDIT_MEMORY_POLICY_REFINEMENT_COMPLETION_2026-05-19.md`
7. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts`
8. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.test.ts`
9. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
   only enough to confirm the existing audit-memory receipt path wiring.

## Pre-Flight Checks

Before writing the rebuttal, Codex must verify:

- `cdh-h-delta` is still the highest-priority `READY_FOR_REBUTTAL` item.
- H2 completion evidence says `reinjectionAllowed` is absent from
  `audit-memory-receipt.ts`.
- Current source still preserves `canReinject: false`.
- Current source exposes or can be evaluated for `writesRequireReceipt` and
  `privacyFilters`.
- Any proposed continuation is policy/readout hardening only, not memory
  runtime expansion.

## Write Ownership

Codex reviewer may create:

- `docs/reviews/CVF_CDH_H_DELTA_CODEX_REBUTTAL_2026-05-20.md`

Codex reviewer may update:

- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V10_2026-05-19.md`

Codex reviewer must not modify:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- Any provider, gateway, memory classifier, public-sync, or Maika file.

## Execution Plan

1. Confirm active queue order and CDH-H scope.
2. Read the CDH-H meta-roadmap section and original CDH blocking finding 2.
3. Read H2 baseline and completion review.
4. Inspect current audit-memory receipt source and tests.
5. Decide one of:
   - `NON_BLOCKING_WITH_SCOPE_REFINEMENT`
   - `NON_BLOCKING_WITH_EXISTING_EVIDENCE`
   - `BLOCKING`
6. File the rebuttal packet with findings, risks, required corrections, and
   explicit claim boundary.
7. Update active review queue/state/handoff routing.
8. Run JSON parse and active-session state checks.
9. Run docs governance and Markdown structural checks if new docs were filed.

## Tasks

- [ ] Confirm queue status for `cdh-h-delta`.
- [ ] Verify the H delta is limited to audit-memory receipt policy/readout
  refinement.
- [ ] Verify `reinjectionAllowed` is not used as a write gate.
- [ ] Verify `canReinject: false` remains load-bearing.
- [ ] Verify `writesRequireReceipt` and `privacyFilters` visibility.
- [ ] Evaluate whether degraded capture readout needs new work or is already
  sufficient.
- [ ] File rebuttal at
  `docs/reviews/CVF_CDH_H_DELTA_CODEX_REBUTTAL_2026-05-20.md`.
- [ ] Update active queue/state routing.
- [ ] Run required verification.

## Acceptance Criteria

The rebuttal is acceptable only if it:

- Names the disposition clearly.
- Separates existing H2 closure from any new H delta continuation.
- Preserves capture vs reinjection boundary.
- Explicitly forbids `reinjectionAllowed` as a capture/write gate.
- Does not authorize implementation by itself.
- Requires a later CDH-H-specific GC-018 before code changes if continuation
  is non-blocking.
- States whether live proof is required later and, if so, that it must use the
  existing governed `/api/execute` audit-memory receipt path.

## Evidence Requirements

The rebuttal must cite:

- CDH-H meta-roadmap section.
- Original CDH rebuttal Finding 2.
- H2 completion review.
- Current `audit-memory-receipt.ts` source inspection.
- Current `audit-memory-receipt.test.ts` source inspection.

If the rebuttal recommends continuation, it must list seed acceptance criteria
for the later implementation GC-018, including:

- receipt preserves `canReinject: false`;
- `writesRequireReceipt` and `privacyFilters` remain visible;
- degraded capture readout is explicit;
- tests prove no `reinjectionAllowed` write gate;
- any live proof uses existing governed execute path.

## Review Gate

Stop and return `BLOCKING` if any of these are true:

- CDH-H would require a new memory tier.
- CDH-H would require persistent/archive memory enablement.
- CDH-H would enable prompt or context reinjection.
- CDH-H would use `reinjectionAllowed` to decide capture/write permission.
- CDH-H would require provider-side memory behavior.
- CDH-H would require changing receipt envelope semantics broadly rather than
  improving the existing audit-memory receipt readout.

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

- the existing source contradicts H2 completion evidence;
- `reinjectionAllowed` appears in the capture/write decision path;
- the requested continuation cannot be done without memory runtime expansion;
- the delta depends on broad receipt-envelope redesign;
- the reviewer cannot inspect the required source files;
- the proposed continuation implies changes to `route.ts` — route hardening
  is out of scope; return to orchestrator.

## Claim Boundary

This work order authorizes only a reviewer-role rebuttal. It does not authorize
implementation, GC-018 filing, memory runtime changes, prompt reinjection,
provider behavior changes, public claims, or CDH closure.
