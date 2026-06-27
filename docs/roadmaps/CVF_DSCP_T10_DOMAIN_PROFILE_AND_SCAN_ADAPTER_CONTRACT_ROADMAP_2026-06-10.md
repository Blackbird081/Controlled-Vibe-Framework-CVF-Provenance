# CVF DSCP-T10 Domain Profile And Scan Adapter Contract Roadmap

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-06-10

---

## Authorization

GC-018:

`docs/baselines/CVF_GC018_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_2026-06-10.md`

Operator instruction 2026-06-10: `Policy_Local` is using CVF scan and memory
rules, but current practical rules are still Vietnamese/policy-specific; CVF
foundation must continue moving toward reusable scan/memory context for any
domain.

## Purpose

Add a small DSCP domain-profile layer so CVF can separate:

- common scan/memory evidence discipline;
- domain-specific language, facets, gates, and boundary rules;
- product-specific corpus data.

Policy_Local should become one profile consumer. It should not define the global
shape of CVF scan and memory.

## Scope / Target / Owner Boundary

In scope:

- deterministic local CPF source contract for DSCP domain profiles;
- focused CPF tests for profile-family behavior;
- CPF export update for the new contract;
- GC-051 JSON and Markdown registry updates for new source/test paths;
- worker return packet.

Out of scope:

- external `Policy_Local` workspace edits;
- cvf-web, provider routing, ECO retrieval runtime, or LPF memory runtime edits;
- corpus ingestion, OCR, vector retrieval, semantic search, provider calls,
  API keys, public-sync, PolicyLocal T12, hosted readiness, production
  readiness, public readiness, current-law claims, or legal advice quality
  claims.

## Problem Statement

Current Policy_Local evidence shows useful CVF scan/memory behavior, but much of
the product logic is correctly domain-specific:

- Vietnamese legal/policy date and article patterns;
- `VN_NATIONAL` jurisdiction filtering;
- EC-01 through EC-04 legal escalation behavior;
- legal/policy facet names such as jurisdiction, authority level, effective
  date, source authority, and answer boundary.

That is acceptable inside Policy_Local. It is not acceptable as the implied
generic CVF scan/memory foundation.

## Work Plan

| Step | Deliverable | Status |
|---|---|---|
| 1 | GC-018 baseline | CLOSED_PASS_BOUNDED |
| 2 | Work order for Claude | CLOSED_PASS_BOUNDED |
| 3 | DSCP domain-profile source contract | CLOSED_PASS_BOUNDED |
| 4 | Focused contract tests across three profile families | CLOSED_PASS_BOUNDED |
| 5 | GC-051 registry JSON and Markdown updates | CLOSED_PASS_BOUNDED |
| 6 | Worker return packet | CLOSED_PASS_BOUNDED |
| 7 | Codex reviewer closure and session sync | CLOSED_PASS_BOUNDED |

## Implementation Targets

Expected new source/test paths:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.contract.test.ts`

Expected existing export owner:

- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/index.ts` or the appropriate
  CPF barrel file selected by source inspection.

Expected registry paths:

- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md`

Expected worker return:

- `docs/reviews/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_WORKER_RETURN_2026-06-10.md`

## Non-Goals

- Do not make Policy_Local a mandatory global CVF profile.
- Do not migrate Policy_Local code in this tranche.
- Do not ingest or reclassify any external corpus.
- Do not introduce vector search, semantic ranking, OCR, or provider-backed
  answer behavior.
- Do not claim legal correctness, current-law status, public readiness, hosted
  readiness, production readiness, or live governance proof.

## Acceptance Criteria

| Criterion | Gate |
|---|---|
| Profile contract supports common plus domain-specific facets | focused vitest |
| Profile contract supports multiple language tags without assuming Vietnamese | focused vitest |
| PolicyLocal legal-policy profile is represented as profile data, not global DSCP behavior | focused vitest |
| Internal company docs and technical/project docs profiles can be represented | focused vitest |
| Profile application copies only allowed gate keys into DSCP `customGates` | focused vitest |
| Unknown gate keys are rejected or surfaced as diagnostics without raw-content release | focused vitest |
| New source/test paths are registered in GC-051 JSON and Markdown | registry checks |
| No external `Policy_Local` workspace files are modified | diff evidence |

## Verification

| Check | Command | Required result |
|---|---|---|
| CPF package check | `npm run check` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| Focused DSCP-T10 test | `npm run test -- tests/dscp.domain.profile.contract.test.ts` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION` | PASS |
| Reviewer fast gate | `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast` | PASS |
| Pre-closure autorun | `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base 6c6964e0 --head HEAD` | PASS before closure commit |

## Closure Summary

DSCP-T10 closed at material commit `0afa8737` with reviewer completion:

`docs/reviews/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_COMPLETION_2026-06-10.md`

Result:

- `DscpDomainProfile` contract added in CPF;
- `applyDomainProfileToDescriptorInput` helper added;
- CPF barrel export added;
- focused test coverage PASS, 18/18;
- GC-051 source/export/test coverage completed;
- no external `Policy_Local` edit, provider call, corpus ingestion, T12, or
  readiness claim.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_FOR_CLAUDE_2026-06-10.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T10_DOMAIN_PROFILE_AND_SCAN_ADAPTER_CONTRACT_COMPLETION_2026-06-10.md` | reviewer completion authored | PASS |
| Roadmap state | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | DSCP-T10 source/export/test coverage | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | DSCP-T10 quick lookup coverage | PASS |
| External evidence digest | GC-018 external product evidence digest | sha256:c1699f4bcb36eb4523605fb0e2f2baacfb83a5838f910100f9f3ca53ddecbbb8; sha256:ab2d0045f2e6e271a9060a86c3895e08ee5ff9a1361533bff3814f0279383100; sha256:77fd13ba3397b6fdaca32e4246a85598117891fa754f05f243884fd5a2699602; sha256:7b1ec0f74f8578a46dd4a7419fe1478cb5c490d38b60853d2e137728a5c11b78 | PASS |
| System loop interlock | no system-loop mutation | domain-profile helper only | N/A with reason: no runtime loop changed |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`, `CVF_SESSION_MEMORY.md`, `AGENT_HANDOFF_V17_2026-06-07.md` | mode and next allowed move updated | PASS |

## Claim Boundary

This roadmap claims a local deterministic contract plan only. It does not claim
provider behavior, live governance proof, retrieval quality, semantic
correctness, corpus ingestion, OCR, vector search, PolicyLocal T12 readiness,
current-law status, legal advice quality, public readiness, hosted readiness,
production readiness, public-sync, memory reinjection, high-risk promotion, or
autonomous mutation.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance roadmap; not public-synced.
