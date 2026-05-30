# CVF Work Order: O1 AIF Operational Context Preview

Memory class: FULL_RECORD

Status: CLOSED_PASS

docType: work_order

Date: 2026-05-24

Tranche: O1

Roadmap: `docs/roadmaps/CVF_POST_AIF_OPERATIONALIZATION_ROADMAP_2026-05-24.md`

---

## Purpose

Add an internal LPF harness that composes the closed AIF-C retrieval policy,
N6 advisory `graph_search`, and memory context packager into a single
summary-only operational context preview.

---

## Authorization

Operator authorized Codex to create the roadmap, work orders, and perform the
workflow on 2026-05-24. O1 touches memory/graph operationalization, so a fresh
GC-018 is required.

GC-018:
`docs/baselines/CVF_GC018_O1_AIF_OPERATIONAL_CONTEXT_PREVIEW_2026-05-24.md`

---

## Authority Chain

Operator -> Codex Planner -> Codex Governance Reviewer -> Codex Implementer ->
Codex QA -> Codex Release Manager.

---

## Agent Roles

- Planner: select bounded operationalization scope.
- Governance Reviewer: file and enforce GC-018.
- Implementer: add LPF preview harness.
- QA: verify targeted/full LPF tests.
- Release Manager: update pointers and commit.

---

## Owner / Source

Owner: Codex as Planner, Governance Reviewer, Implementer, QA, and Release
Manager.

Sources:

- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge/graph/`
- `docs/reviews/CVF_N6_AIF_GRAPH_SEARCH_ACTIVATION_COMPLETION_2026-05-24.md`

---

## Required First Reads

- `docs/roadmaps/CVF_POST_AIF_NEXT_VALUE_ROADMAP_2026-05-24.md`
- `docs/reviews/CVF_N6_AIF_GRAPH_SEARCH_ACTIVATION_COMPLETION_2026-05-24.md`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts`
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-context-packager.ts`

---

## Pre-Flight Checks

- Confirm GC-018 exists.
- Confirm no web route/provider/receipt files are in scope.
- Confirm `canReinject=false` remains a required invariant.

---

## Write Ownership

Codex owns the new LPF preview module, targeted tests, index export, and O1
closure docs.

---

## Scope / Target / Owner Boundary

In scope:

- Add `aif-operational-context-preview.ts`.
- Export the preview contract from LPF.
- Add targeted tests.

Out of scope:

- Live route integration.
- Prompt reinjection.
- Provider calls.
- Receipt-envelope changes.
- Graph authority or scoring.
- Public-sync.

---

## Execution Plan

1. File GC-018.
2. Implement a preview builder that calls `evaluateRetrievalRequest()`.
3. Package selected summaries through `packageMemoryContext()`.
4. Mark evidence as `rawMemoryReleased=false`, `canReinject=false`,
   `liveRouteInjected=false`, and `graphAdvisoryOnly=true`.
5. Add tests for ready, partial, denied, and token-budget behavior.
6. Run targeted LPF tests, full LPF tests, and TypeScript check.
7. File completion review.

---

## Evidence Requirements

- Targeted LPF tests pass.
- Full LPF tests pass.
- LPF TypeScript check passes.
- Preview evidence preserves summary-only/no-reinjection invariants.

---

## Acceptance Criteria

- [x] GC-018 filed.
- [x] Preview builder implemented.
- [x] Summary-only package output verified.
- [x] Unauthorized actor path denies without approved memory.
- [x] Missing graph service yields partial status, not unsafe fallback.
- [x] Token-budget exclusion preserved.
- [x] LPF targeted/full/check PASS.

---

## Risk / Corrective Action

Risk: preview could be treated as live reinjection. Corrective action: explicit
evidence fields and claim boundary prevent that interpretation.

---

## Review Gate

O1 can close only when tests pass and the preview contract exposes no live route
integration or graph authority.

---

## Closure Checklist

- [x] GC-018 filed.
- [x] Required first reads complete.
- [x] Implementation complete.
- [x] Tests pass.
- [x] Completion review filed.

---

## Return-To-Orchestrator Conditions

Return to the operator only if the preview requires route/provider/receipt
changes or cannot preserve summary-only constraints.

---

## Operator Checkpoint

Operator authorization was provided in-session on 2026-05-24 for Codex to
create and execute the roadmap/work orders.

---

## Decision / Recommendation / Disposition

Disposition: CLOSED_PASS.

---

## Claim Boundary

O1 proves a local summary-only preview harness only. It does not authorize or
prove live memory reinjection, graph authority, route changes, provider changes,
public-sync, hosted readiness, production readiness, or freeze release.
