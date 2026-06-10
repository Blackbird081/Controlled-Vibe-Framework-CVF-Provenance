# CVF DSCP-T11F Profile Selection Adapter Roadmap

Memory class: SUMMARY_RECORD

Status: DISPATCHED

docType: roadmap

Date: 2026-06-10

---

## Authorization

GC-018:

`docs/baselines/CVF_GC018_DSCP_T11F_PROFILE_SELECTION_ADAPTER_2026-06-10.md`

Operator instruction 2026-06-10: after DSCP-T11E review and commit, audit the
next DSCP/PolicyLocal foundation move and create a work order for Claude.

## Purpose

Add a local deterministic profile selection adapter that turns the T11E
registry output into one apply-or-stop result contract for scan-layer callers.

## Scope / Target / Owner Boundary

In scope:

- CPF profile-selection adapter source;
- CPF barrel export;
- focused CPF adapter tests;
- GC-051 registry coverage;
- Claude worker return and later Codex completion review.

Out of scope:

- external `Policy_Local` edits;
- corpus ingestion, OCR, vector retrieval, T12, provider calls, API keys,
  cvf-web route changes, public-sync, hosted readiness, production readiness,
  public readiness, current-law status, or legal advice quality claims.

## Non-Goals

- Do not integrate external `Policy_Local`.
- Do not ingest or classify new corpus content.
- Do not build vector retrieval or semantic ranking.
- Do not author or unblock LPCI2-T12.
- Do not run live provider calls or load API keys.
- Do not make legal-quality, current-law, hosted, public, production, or
  release-readiness claims.

## Work Plan

| Step | Deliverable | Status |
|---|---|---|
| 1 | GC-018 baseline | DISPATCHED |
| 2 | Work order for Claude | DISPATCHED |
| 3 | CPF profile selection adapter source | WORKER_ASSIGNED |
| 4 | CPF focused adapter tests | WORKER_ASSIGNED |
| 5 | GC-051 registry JSON and Markdown updates | WORKER_ASSIGNED |
| 6 | Worker return packet | WORKER_ASSIGNED |
| 7 | Codex reviewer closure and session sync | NOT_STARTED_BY_DESIGN |

## Implementation Targets

Expected source path:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.profile.selection.adapter.ts`

Expected export path:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts`

Expected test path:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.profile.selection.adapter.test.ts`

Expected worker return:

- `docs/reviews/CVF_DSCP_T11F_PROFILE_SELECTION_ADAPTER_WORKER_RETURN_2026-06-10.md`

## Acceptance Criteria

| Criterion | Gate |
|---|---|
| Unique legal-policy selection applies profile and injects expected metadata/gates | focused vitest |
| Unique technical-project selection applies profile without legal-policy gate bleed | focused vitest |
| No-match selection returns a stop result before profile application | focused vitest |
| Ambiguous selection returns a stop result before profile application | focused vitest |
| `BLOCKED_UNTIL_*` profile application returns a blocked stop result | focused vitest |
| `requiredFacetKey` can select by common or domain facet key | focused vitest |
| Adapter exports through CPF barrel | TypeScript check |
| New source and test paths are registered in GC-051 JSON and Markdown | registry checks |
| No forbidden path is modified | diff evidence |

## Verification

| Check | Command | Required result |
|---|---|---|
| CPF package check | `npm run check` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| Focused DSCP-T11F test | `npm run test -- tests/dscp.profile.selection.adapter.test.ts` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| Reviewer-fast gate | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS |
| Pre-closure autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <baseHead> --head HEAD` | PASS before closure claim |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T11F_PROFILE_SELECTION_ADAPTER_FOR_CLAUDE_2026-06-10.md` | `Status: DISPATCHED` before worker execution | READY |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T11F_PROFILE_SELECTION_ADAPTER_COMPLETION_2026-06-10.md` | reviewer-authored on worker-return review | NOT_STARTED_BY_DESIGN |
| Roadmap state | this file | `Status: DISPATCHED` before worker execution | READY |
| Adapter source | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.profile.selection.adapter.ts` | worker-created source | WORKER_ASSIGNED |
| Focused tests | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.profile.selection.adapter.test.ts` | focused test evidence | WORKER_ASSIGNED |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | DSCP-T11F source/test coverage | WORKER_ASSIGNED |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | DSCP-T11F quick lookup rows | WORKER_ASSIGNED |
| External evidence digest | N/A | N/A with reason: no external product, corpus, provider, or public-sync artifact consumed or produced | N/A with reason |
| System loop interlock | no system-loop mutation | local CPF adapter only | N/A with reason |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V17_2026-06-07.md` | reviewer-owned sync in DSCP-T11F closure batch | NOT_STARTED_BY_DESIGN |

## Claim Boundary

This roadmap authorizes only a local deterministic CPF profile selection
adapter and focused tests. It does not claim provider behavior, live governance
proof, retrieval quality, semantic correctness, corpus ingestion, OCR, vector
search, PolicyLocal T12 readiness, current-law status, legal advice quality,
public readiness, hosted readiness, production readiness, public-sync, memory
reinjection, high-risk promotion, Learning Orchestrator runtime behavior, or
autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance roadmap; not public-synced.
