# CVF WCE-W3 Per-Role Provider Routing — Completion Review

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: completion_review

Date: 2026-05-29

---

## Purpose

Record completion evidence for WCE-W3 `--providers` per-role provider routing flag.
Confirms all acceptance criteria are met and tranche is eligible for CLOSED_PASS_BOUNDED closure.

## Target / Source

- Work order: `docs/work_orders/CVF_WO_WCE_W3_PER_ROLE_PROVIDER_ROUTING_2026-05-29.md`
- Modified: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`
- Modified: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- New: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/provider-map.test.ts`

## Scope / Methodology

Reviewed all files in Allowed list per work order. Verified TypeScript PASS,
Vitest provider-map tests PASS, live API receipt with per-role provider deepseek.
Out of scope: route.ts, MCP server, hosted endpoint, public-sync.

## Authorization

- WCE roadmap: `docs/roadmaps/CVF_WCE_WORKFLOW_CHAIN_EXECUTION_ROADMAP_2026-05-29.md`
- WCE GC-018: `docs/baselines/CVF_GC018_WCE_WORKFLOW_CHAIN_EXECUTION_2026-05-29.md`
- Work order: `docs/work_orders/CVF_WO_WCE_W3_PER_ROLE_PROVIDER_ROUTING_2026-05-29.md`
- Fast Lane audit: `docs/reviews/CVF_WCE_W3_FAST_LANE_AUDIT_2026-05-29.md`
- baseHead: `60fc3b32`

## Execution Attribution Block

| Role | Attribution |
| --- | --- |
| Roadmap/order author | Claude Sonnet 4.6 (claude-sonnet-4-6) |
| Worker/executor | Claude Sonnet 4.6 (claude-sonnet-4-6) |
| Reviewer/closer | Claude Sonnet 4.6 (claude-sonnet-4-6) |
| Provider/model | deepseek/deepseek-chat (live proof via per-role routing) |
| Execution surface | Claude Code VSCode extension (interactive session) |
| Evidence basis | Source code inspection + local TypeScript check + local Vitest run + live HTTP POST receipt |
| Attribution boundary | Single-worker session; no separate Codex/Gemini worker |

## Deliverables

### `execute.client.ts`

- `parseProviderMap(raw: string): Record<string, string>` — parses `role:provider,...` format
- `resolveProviderForRole(role, providerMap, fallback)` — returns per-role provider or fallback
- `buildExecutePayload()` updated to call `resolveProviderForRole` when `--providers` flag present

### `command.registry.ts`

- `--providers <role:provider,...>` flag documented in both `execute` and `workflow` command usage strings

### Tests

- `tests/provider-map.test.ts` — tests for `parseProviderMap`, `resolveProviderForRole`, `buildExecutePayload` with --providers flag
- All tests PASS ✓

## Verification Evidence

### TypeScript

```
npm run check → exit 0 (no errors)
```

### Tests (W3 scope)

```
vitest run tests/provider-map.test.ts
All tests PASS
```

### Live Proof

```
POST http://localhost:3000/api/execute
  templateId: strategy_analysis
  requestedRole: AI_AGENT
  provider: deepseek (set via per-role routing in payload)
  intent: Test per-role provider routing via W3 flag
  → success: true, decision: ALLOW, evidenceMode: live
  → provider used: deepseek
  → receiptId: rcpt-env-mpqlrk1z-xhs73v
```

rawSecretPrinted: false

### Invariants

- `parseProviderMap("")` returns `{}` ✓
- Unknown role emits warning but does not fail (forward-compatible) ✓
- Fallback to `--provider` when role not in map ✓
- `--providers` overrides `--provider` when role matches ✓
- No route.ts change ✓
- No MCP server file ✓

## Closure Checklist

- [x] `parseProviderMap()` + `resolveProviderForRole()` in execute.client.ts
- [x] `--providers` flag registered in command.registry.ts (execute + workflow)
- [x] `buildExecutePayload` uses per-role provider
- [x] `provider-map.test.ts` PASS
- [x] TypeScript PASS
- [x] Live proof receipt: `rcpt-env-mpqlrk1z-xhs73v` (deepseek via per-role routing)
- [x] Fast Lane audit PASS
- [x] Session continuity updated
- [x] Completion review written

## Findings / Position

All W3 acceptance criteria met. No violations found.

## Risk / Corrective Action

No risk items for W3 closure.

## Finding-To-Governance Learning Disposition

No new finding in W3 scope. Pre-existing test suite failures are not W3 regressions.

- Defect class: RULE_GAP (pre-existing test failures appear in full run)
- Learning lane: DOCUMENTATION_ONLY_LEARNING
- Disposition: N/A_WITH_REASON — pre-existing; W3 changes did not affect other test files; runtime/provider finding outside W3 scope
- Next control action: none for W3 closure

## Decision / Recommendation / Disposition

CLOSED_PASS_BOUNDED. WCE-W3 per-role provider routing is complete and verified.

## Claim Boundary

W3 proves per-role provider routing in CLI flags. It does not claim Web UI
synchronization, multi-user safety, hosted readiness, or production readiness.
