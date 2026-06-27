# CVF DSCP-T11E Domain Profile Registry Roadmap

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-10

---

## Authorization

GC-018:

`docs/baselines/CVF_GC018_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_2026-06-10.md`

Operator instruction 2026-06-10: check the DSCP-T11E worker return, commit if
clean, then audit and author the next bounded roadmap/work order for Claude.

## Purpose

Add a local deterministic domain-profile registry so the scan layer can select
domain profiles by criteria before applying them to governed descriptor inputs.

## Scope / Target / Owner Boundary

In scope:

- CPF source registry and selector;
- CPF barrel export;
- focused CPF tests;
- GC-051 registry coverage;
- worker return and Codex completion review.

Out of scope:

- external `Policy_Local` edits;
- corpus ingestion, OCR, vector retrieval, T12, provider calls, API keys,
  cvf-web route changes, public-sync, hosted readiness, production readiness,
  public readiness, or legal advice quality claims.

## Non-Goals

- Do not ingest or classify new corpus content.
- Do not update external `Policy_Local`.
- Do not author or unblock LPCI2-T12.
- Do not run live provider calls or load API keys.
- Do not make legal-quality, current-law, hosted, public, production, or
  release-readiness claims.

## Work Plan

| Step | Deliverable | Status |
|---|---|---|
| 1 | GC-018 baseline | CLOSED_PASS_BOUNDED |
| 2 | Work order for Claude | CLOSED_PASS_BOUNDED |
| 3 | CPF domain profile registry source | CLOSED_PASS_BOUNDED |
| 4 | CPF focused registry tests | CLOSED_PASS_BOUNDED |
| 5 | GC-051 registry JSON and Markdown updates | CLOSED_PASS_BOUNDED |
| 6 | Worker return packet | CLOSED_PASS_BOUNDED |
| 7 | Codex reviewer closure and session sync | CLOSED_PASS_BOUNDED |

## Implementation Targets

Expected source path:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.registry.ts`

Expected export path:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.context.barrel.ts`

Expected test path:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.registry.test.ts`

Expected worker return:

- `docs/reviews/CVF_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_WORKER_RETURN_2026-06-10.md`

## Acceptance Criteria

| Criterion | Gate |
|---|---|
| Registry can register, reject duplicate IDs, replace, unregister, list, and get profiles | focused vitest |
| Selection returns exactly one profile only when criteria identify one match | focused vitest |
| Ambiguous and no-match criteria return `matched=false` and `profile=null` with diagnostics | focused vitest |
| Selection can match facet keys in common or domain facet maps | focused vitest |
| Select-then-apply flow proves legal-policy and technical-project profiles remain isolated | focused vitest |
| New source and test paths are registered in GC-051 JSON and Markdown | registry checks |
| No forbidden path is modified | diff evidence |

## Verification

| Check | Command | Required result |
|---|---|---|
| CPF package check | `npm run check` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| Focused DSCP-T11E test | `npm run test -- tests/dscp.domain.profile.registry.test.ts` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| Reviewer-fast gate | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS |
| Pre-closure autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 6a1cce6b --head HEAD` | PASS before closure claim |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_FOR_CLAUDE_2026-06-10.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T11E_DOMAIN_PROFILE_REGISTRY_COMPLETION_2026-06-10.md` | reviewer-authored before material commit | PASS |
| Roadmap state | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry source | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.registry.ts` | staged before material commit | PASS |
| Focused tests | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.registry.test.ts` | 18/18 PASS | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | DSCP-T11E source/test coverage | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | DSCP-T11E quick lookup rows | PASS |
| External evidence digest | N/A | N/A with reason: no external product, corpus, provider, or public-sync artifact consumed or produced | N/A with reason |
| System loop interlock | no system-loop mutation | local CPF registry only | N/A with reason |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V17_2026-06-07.md` | reviewer-owned final sync | PASS |

## Closure Summary

DSCP-T11E closes the local registry/selector gap after T11. Result:

- `DscpDomainProfileRegistry` and factory added;
- selection by profile ID, domain family, language code, and facet key added;
- ambiguous and no-match selections stop with `profile=null`;
- select-then-apply integration proves profile isolation before descriptor
  construction;
- CPF TypeScript PASS, focused vitest 18/18 PASS, reviewer-fast 11/11 PASS.

## Claim Boundary

This roadmap claims only a local deterministic CPF registry and selector. It
does not claim provider behavior, live governance proof, retrieval quality,
semantic correctness, corpus ingestion, OCR, vector search, PolicyLocal T12
readiness, current-law status, legal advice quality, public readiness, hosted
readiness, production readiness, public-sync, memory reinjection, high-risk
promotion, Learning Orchestrator runtime behavior, or autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance roadmap; not public-synced.
