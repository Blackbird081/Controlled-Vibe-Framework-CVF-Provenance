# CVF GC-018 O1 - AIF Operational Context Preview

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

Date: 2026-05-24

## Purpose

Authorize a bounded internal LPF harness that composes AIF memory retrieval,
advisory graph search, and memory context packaging into a local operational
context preview.

## Source / Predecessor Evidence

- `docs/roadmaps/CVF_AGENT_INTELLIGENCE_FOUNDATIONS_ROADMAP_2026-05-23.md`
- `docs/roadmaps/CVF_POST_AIF_NEXT_VALUE_ROADMAP_2026-05-24.md`
- `docs/reviews/CVF_N6_AIF_GRAPH_SEARCH_ACTIVATION_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_PBR04_GRAPH_SQLITE_PERSIST_COMPLETION_2026-05-24.md`

## Decision / Baseline / Proposed Tranche

Decision: continue with O1.

Baseline: AIF-C Phase 2a memory gateway and N6 `graph_search` are local and
summary-only. PBR-04 provides optional SQLite symbol-index persistence, not
live memory persistence.

Proposed tranche: add `buildAifOperationalContextPreview()` in LPF.

## Scope / Target / Owner Boundary

In scope:

- local preview builder;
- summary-only memory context block;
- advisory graph result packaging;
- targeted tests.

Out of scope:

- live `/api/execute` reinjection;
- provider calls;
- route/provider/receipt changes;
- graph scoring or approval authority;
- non-graph durable memory;
- public-sync.

## Legacy Spec Scan Block

| Source | Classification | Decision |
| --- | --- | --- |
| `.private_reference/legacy/CVF 16.5/agentmemory/` | partially absorbed | Use only local summary packaging concepts already delivered by AIF-C; durable/live/cross-session memory remains out of scope. |
| `.private_reference/legacy/CVF ADD/code-review-graph/` | runtime-owned Phase 1/2b | Use graph results as advisory evidence only; no authority or scoring expansion. |

## Acceptance Criteria

O1 passes only if the preview harness preserves `rawMemoryReleased=false`,
`canReinject=false`, `liveRouteInjected=false`, and `graphAdvisoryOnly=true`,
with targeted LPF tests, full LPF tests, and TypeScript check passing.

## Evidence / Verification

Verification requires targeted LPF tests, full LPF tests, LPF TypeScript check,
and roadmap/review closure evidence.

## Risk / Corrective Action

Risk: the harness is mistaken for live route integration. Corrective action:
the contract exposes `liveRouteInjected=false` and no web route files are in
scope.

## Claim Boundary

O1 can claim only local operational preview readiness. It does not claim live
reinjection, graph authority, provider stability, public readiness, hosted
readiness, production readiness, or freeze release.
