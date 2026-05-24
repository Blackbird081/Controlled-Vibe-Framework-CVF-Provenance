# CVF Post-AIF Operational Readiness Matrix

Memory class: POINTER_RECORD

Status: ACTIVE_REFERENCE

Date: 2026-05-24

## Purpose

Provide a compact Post-AIF readiness table for agents scoping memory, graph,
provider, public-sync, or hosted/product work after the Post-AIF next-value
roadmap closed.

## Owner / Source

Owner: Codex.

Sources:

- `docs/roadmaps/CVF_POST_AIF_NEXT_VALUE_ROADMAP_2026-05-24.md`
- `docs/roadmaps/CVF_POST_AIF_OPERATIONALIZATION_ROADMAP_2026-05-24.md`
- `docs/reference/CVF_OPERATIONAL_REFERENCE_INDEX_2026-05-23.md`

## Scope / Target / Owner Boundary

This matrix is an internal operational reference. It does not authorize public
claims, provider reruns, route changes, persistence expansion, hosted readiness,
production readiness, or freeze release.

## Readiness Matrix

| Surface | Current status | Evidence | Next allowed move |
| --- | --- | --- | --- |
| Skill corpus test path | Proven bug fix | `docs/reviews/CVF_N4_SKILL_CORPUS_TEST_REPAIR_COMPLETION_2026-05-24.md` | Normal regression maintenance. |
| Technical product catalog AIF rows | Proven private catalog update | `docs/reviews/CVF_N5_CATALOG_AIF_UPDATE_COMPLETION_2026-05-24.md` | Public-sync requires separate authorization and public-sync clone. |
| Memory Gateway Phase 2a | Proven local in-memory policy surface | `docs/reviews/CVF_AIF_C_MEMORY_GATEWAY_PHASE2_COMPLETION_2026-05-24.md` | Live reinjection requires fresh GC-018/work order. |
| `graph_search` retrieval | Proven local advisory retrieval | `docs/reviews/CVF_N6_AIF_GRAPH_SEARCH_ACTIVATION_COMPLETION_2026-05-24.md` | Graph scoring/authority requires fresh GC-018 and must not bypass governance. |
| Graph SQLite symbol-index persistence | Proven optional graph index persistence | `docs/reviews/CVF_PBR04_GRAPH_SQLITE_PERSIST_COMPLETION_2026-05-24.md` | Non-graph durable memory remains gated. |
| AIF operational context preview | Proven local summary-only harness; public-sync code availability now proven by C1 | `docs/reviews/CVF_O1_AIF_OPERATIONAL_CONTEXT_PREVIEW_COMPLETION_2026-05-24.md`; `docs/reviews/CVF_C1_PUBLIC_AIF_PREVIEW_RUNTIME_AVAILABILITY_COMPLETION_2026-05-24.md`; public-sync commit `ea889a46` | Route integration/live reinjection requires fresh GC-018. |
| OpenAI `gpt-4o` provider lane | One bounded governed live receipt | `docs/reviews/CVF_N7_THIRD_PROVIDER_EXPANSION_COMPLETION_2026-05-24.md` | Provider repeatability/stability requires fresh GC-018 and live evidence window. |
| Alibaba / DeepSeek lanes | Prior bounded repeatability windows only | Active state registry provider-stability entries | Broad provider stability remains unclaimed. |
| Public repository | C1 public-sync preview harness availability proven | `docs/reviews/CVF_C1_PUBLIC_AIF_PREVIEW_RUNTIME_AVAILABILITY_COMPLETION_2026-05-24.md`; public-sync commit `ea889a46` | Further public product claims still require public-sync clone after `git remote -v`. |
| Hosted/product readiness | Not proven by AIF/Post-AIF | Active state hosted proof boundaries | Hosted readiness requires dedicated roadmap and live hosted proof. |

## Risk / Corrective Action

Risk: one bounded receipt or local harness is overread as production readiness.
Corrective action: each row names the exact next gate rather than expanding the
claim.

## Decision / Recommendation / Disposition

Disposition: ACTIVE_REFERENCE.

Recommended next choices are demand-gated: live memory reinjection proof,
bounded tri-provider repeatability window, graph-authority decision, or hosted
readiness decision. Public-sync preview harness availability is already closed
by C1.

## Claim Boundary

This matrix improves operational scoping only. It does not prove additional
runtime governance behavior, provider stability, public readiness, hosted
readiness, production readiness, or freeze release.
