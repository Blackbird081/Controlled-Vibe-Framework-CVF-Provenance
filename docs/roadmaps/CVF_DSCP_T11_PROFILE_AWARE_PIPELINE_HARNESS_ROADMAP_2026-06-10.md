# CVF DSCP-T11 Profile-Aware Pipeline Harness Roadmap

Memory class: SUMMARY_RECORD

Status: DISPATCHED

docType: roadmap

Date: 2026-06-10

---

## Authorization

GC-018:

`docs/baselines/CVF_GC018_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_2026-06-10.md`

Operator instruction 2026-06-10: prove profile metadata and gate keys flow
through descriptor, ECO/LPF package, and retrieval receipt without release or
bleed, and prove `BLOCKED_UNTIL_*` stops at profile application.

## Purpose

Close the local proof gap between the DSCP-T10 domain-profile contract and the
existing DSCP context package/receipt surfaces.

## Scope / Target / Owner Boundary

In scope:

- focused CPF test harness only;
- GC-051 registry coverage for the new test path;
- worker return and Codex closure review.

Out of scope:

- external `Policy_Local` edits;
- new runtime source contract;
- cvf-web, provider routing, corpus ingestion, vector retrieval, OCR, T12,
  public-sync, hosted readiness, production readiness, public readiness, or
  live governance proof.

## Work Plan

| Step | Deliverable | Status |
|---|---|---|
| 1 | GC-018 baseline | DISPATCHED |
| 2 | Work order for Claude | DISPATCHED |
| 3 | Focused profile-aware pipeline harness test | DISPATCHED |
| 4 | GC-051 registry JSON and Markdown updates | DISPATCHED |
| 5 | Worker return packet | DISPATCHED |
| 6 | Codex reviewer closure and session sync | PENDING |

## Implementation Targets

Expected new test path:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.profile.aware.pipeline.harness.test.ts`

Expected registry paths:

- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`

Expected worker return:

- `docs/reviews/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_WORKER_RETURN_2026-06-10.md`

## Non-Goals

- Do not change existing DSCP source contracts.
- Do not modify external `Policy_Local`.
- Do not ingest corpus files or create vector retrieval.
- Do not run providers or use API keys.
- Do not author T12 or make current-law, legal-quality, public, hosted, or
  production readiness claims.

## Acceptance Criteria

| Criterion | Gate |
|---|---|
| `legal_policy` metadata and `ec02Gate` flow through descriptor -> ECO pack -> receipt | focused vitest |
| `technical_project` metadata and `stabilityGate` flow through descriptor -> LPF package -> receipt | focused vitest |
| raw source/content/memory release remains false in package/receipt evidence | focused vitest |
| legal-policy gates do not appear in technical-project outputs, and technical gates do not appear in legal-policy outputs | focused vitest |
| `BLOCKED_UNTIL_*` short-circuits before descriptor/package/receipt creation | focused vitest |
| New test path is registered in GC-051 JSON and Markdown | registry checks |
| No forbidden paths are modified | diff evidence |

## Verification

| Check | Command | Required result |
|---|---|---|
| CPF package check | `npm run check` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| Focused DSCP-T11 test | `npm run test -- tests/dscp.profile.aware.pipeline.harness.test.ts` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| Reviewer-fast gate | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS |
| Pre-closure autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 0f75ff6f --head HEAD` | PASS before closure claim |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_FOR_CLAUDE_2026-06-10.md` | `Status: DISPATCHED` | READY |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T11_PROFILE_AWARE_PIPELINE_HARNESS_COMPLETION_2026-06-10.md` | reviewer-authored after material commit | PENDING |
| Roadmap state | this file | `Status: DISPATCHED` | READY |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | DSCP-T11 test coverage | PENDING |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | DSCP-T11 quick lookup row | PENDING |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V17_2026-06-07.md` | updated after closure | PENDING |

## Claim Boundary

This roadmap claims only a local deterministic test-harness plan. It does not
claim provider behavior, live governance proof, retrieval quality, semantic
correctness, corpus ingestion, OCR, vector search, PolicyLocal T12 readiness,
current-law status, legal advice quality, public readiness, hosted readiness,
production readiness, public-sync, memory reinjection, high-risk promotion, or
autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance roadmap; not public-synced.
