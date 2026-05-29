# CVF WCE-W3 Fast Lane Audit

Memory class: FULL_RECORD

Status: PASS

docType: fast_lane_audit

Date: 2026-05-29

---

## Purpose

Verify that WCE-W3 (`--providers` per-role provider routing flag) satisfies its
work order scope, invariants, and evidence requirements before CLOSED_PASS_BOUNDED closure.

## Target / Source Under Review

- Work order: `docs/work_orders/CVF_WO_WCE_W3_PER_ROLE_PROVIDER_ROUTING_2026-05-29.md`
- WCE roadmap: `docs/roadmaps/CVF_WCE_WORKFLOW_CHAIN_EXECUTION_ROADMAP_2026-05-29.md`
- WCE GC-018: `docs/baselines/CVF_GC018_WCE_WORKFLOW_CHAIN_EXECUTION_2026-05-29.md`
- baseHead: `60fc3b32`

## Fast Lane Classification

Risk class: R0 (additive flag parsing; no route.ts change; no governance bypass; fallback preserved)

Change type: New `parseProviderMap`/`resolveProviderForRole` functions in `execute.client.ts`; `--providers` flag in `command.registry.ts`; new `provider-map.test.ts`.

## Scope / Methodology

Reviewed: source diff, TypeScript check, Vitest W3-scope tests, live API receipt with per-role provider. Did not review: MCP server files, route.ts, hosted endpoint, public-sync.

## Scope Verification

Changed files in W3 scope:

| File | Action | In Allowed list? |
| --- | --- | --- |
| `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts` | Modified (parseProviderMap, resolveProviderForRole, buildExecutePayload update) | Yes |
| `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts` | Modified (--providers flag on execute + workflow) | Yes |
| `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/provider-map.test.ts` | Created (note: in src/ not tests/ but vitest picks it up) | Yes |
| `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/provider-map.test.ts` | Created | Yes |
| `docs/reviews/CVF_WCE_W3_FAST_LANE_AUDIT_2026-05-29.md` | Created | Yes |
| `docs/reviews/CVF_WCE_W3_PER_ROLE_PROVIDER_ROUTING_COMPLETION_2026-05-29.md` | Created | Yes |

`route.ts`: NOT touched. MCP server: NOT touched. ✓

## Constraint Verification

| Constraint | Result |
| --- | --- |
| `--providers` flag accepted on `cvf execute` | Registered in command registry usage string ✓ |
| `parseProviderMap()` correctly parses `role:provider` format | 10 tests PASS ✓ |
| Per-role provider used in `ExecuteRequestPayload.provider` | `buildExecutePayload` calls `resolveProviderForRole` ✓ |
| Fallback to `--provider` when role not in map | `resolveProviderForRole` returns fallback ✓ |
| Unknown roles produce warning not failure | `process.stderr.write` warning emitted ✓ |
| No route.ts change | Confirmed ✓ |
| No MCP server change | Confirmed ✓ |

## Findings / Position

No violations found. All W3 acceptance criteria satisfied.

## Evidence

- `parseProviderMap()` + `resolveProviderForRole()` in `execute.client.ts`
- `buildExecutePayload` uses per-role provider via `resolveProviderForRole`
- `--providers` flag registered on both `execute` and `workflow` commands
- W3-scope tests: all PASS (`tests/provider-map.test.ts`)
- TypeScript: PASS
- Live proof receipt: `rcpt-env-mpqlrk1z-xhs73v` (provider `deepseek` routed via per-role payload, ALLOW, evidenceMode=live)

## Risk / Corrective Action

No risk items for W3 closure.

## Finding-To-Governance Learning Disposition

No new finding in W3 scope. Pre-existing test failures in other files are not W3 regressions.

- Defect class: RULE_GAP (pre-existing test suite failures appear in full run)
- Learning lane: DOCUMENTATION_ONLY_LEARNING
- Disposition: N/A_WITH_REASON — pre-existing; W3 made no change to affected modules; runtime/provider finding outside W3 scope
- Next control action: none for W3 closure

## Decision / Recommendation / Disposition

PASS. W3 satisfies all work order acceptance criteria. Eligible for CLOSED_PASS_BOUNDED closure.

## Claim Boundary

W3 proves per-role provider routing in CLI flags. It does not claim Web UI
synchronization, multi-user safety, hosted readiness, or production readiness.
