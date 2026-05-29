# CVF Work Order — WCE-W3 Per-Role Provider Routing

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Date: 2026-05-29

---

## Purpose

Add `--providers` flag to `cvf execute` and `cvf workflow` CLI commands,
enabling per-role provider assignment matching the `agentProviders` setting
already implemented in the Web UI.

Format: `--providers orchestrator:deepseek,builder:gemini,reviewer:claude`

Contract version: `cvf.perRoleProviderRouting.wce.w3.v1`

This closes Gap C: Web UI has per-role provider assignment, CLI has only a
global `--provider` flag.

**Can run in parallel with WCE-W1** — they touch different parts of the CLI.

## Authority Chain

- WCE roadmap: `docs/roadmaps/CVF_WCE_WORKFLOW_CHAIN_EXECUTION_ROADMAP_2026-05-29.md`
- WCE GC-018: `docs/baselines/CVF_GC018_WCE_WORKFLOW_CHAIN_EXECUTION_2026-05-29.md`
- CLI execute client: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`
  — `ExecuteRequestPayload` at line 16; `buildExecutePayload()` at line 52
- CLI command registry: `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
  — `cvf execute` usage at line 130
- Web UI per-role setting: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Settings.tsx`
  — `agentProviders` at line 71
- `AgentRole` type: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/multi-agent.tsx` line 8

## Agent Roles

Implementer adds `--providers` flag parsing + payload update. Reviewer verifies
correct role-to-provider mapping; confirms no governance bypass; confirms tests
PASS. No self-review.

## Scope

**Allowed:**

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts` (add `parseProviderMap` + update payload)
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts` (add `--providers` flag to execute + workflow)
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/provider-map.test.ts` (new)
- `docs/reviews/CVF_WCE_W3_FAST_LANE_AUDIT_2026-05-29.md` (new)
- `docs/reviews/CVF_WCE_W3_PER_ROLE_PROVIDER_ROUTING_COMPLETION_2026-05-29.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** `route.ts`, MCP server, UI files, receipt envelope schema, public-sync.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`
   — confirm `ExecuteRequestPayload.provider` optional field at line 21
   — confirm `buildExecutePayload()` at line 52 — where provider is set
4. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
   — confirm existing flags on `cvf execute` (line 130)
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Settings.tsx`
   — confirm `agentProviders` record shape at line 71

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `ExecuteRequestPayload.provider` optional field | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts` | line 21 | `provider` | `ExecuteRequestPayload` | ACCEPT |
| `buildExecutePayload()` | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts` | line 52 | `buildExecutePayload` | execute client | ACCEPT |
| `requestedRole` field | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts` | line 24 | `requestedRole` | `ExecuteRequestPayload` | ACCEPT |
| `agentProviders` setting | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Settings.tsx` | line 71 | `agentProviders` | Settings preferences | ACCEPT |
| `AgentRole` type | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/multi-agent.tsx` | line 8 | `AgentRole` | multi-agent module | ACCEPT |

New functions:

| New symbol | Purpose | Runtime claim blocked? |
| --- | --- | --- |
| `parseProviderMap(raw: string)` | Parses `role:provider,role:provider` string into Record | No — runtime function |
| `resolveProviderForRole(role, providerMap)` | Returns provider for a given role, falls back to default | No — runtime function |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| `--providers` flag on `cvf execute` | Scope + implementation | `command.registry.ts` diff | grep `--providers` | OPEN |
| `parseProviderMap()` function | execute.client.ts | `parseProviderMap` export | Tests verify parsing | OPEN |
| Per-role provider used in payload | `buildExecutePayload` update | `provider` field in payload | Test verifies provider value | OPEN |
| Tests PASS | Scope | `provider-map.test.ts` | `npm test` | OPEN |
| Live proof | Evidence | receipt in completion review | receipt ID with correct provider | OPEN |

## Implementation Design

### `parseProviderMap(raw: string): Record<string, string>`

Parses `"orchestrator:deepseek,builder:gemini,reviewer:claude"` into
`{ orchestrator: 'deepseek', builder: 'gemini', reviewer: 'claude' }`.

Validation:
- Each segment must be `role:provider` format
- Unknown roles produce a warning but do not fail (forward-compatible)
- Empty string returns `{}`

### `buildExecutePayload` update

When `--providers` flag present and contains an entry for `requestedRole`,
set `payload.provider` to the mapped provider for that role.

When `--providers` flag present but no entry for `requestedRole`, fall back
to global `--provider` flag or request-default.

### `command.registry.ts`

Add `--providers <map>` flag description to both `execute` and `workflow`
command usage strings. Parse via `stringFlag(args, 'providers')`.

## Pre-Flight

- [ ] Working tree clean
- [ ] `ExecuteRequestPayload.provider` field confirmed as optional at line 21
- [ ] `buildExecutePayload()` confirmed at line 52 — understand where `provider` is currently set
- [ ] `agentProviders` shape confirmed from Settings.tsx line 71

## Write Ownership

Implementer owns all new and modified files. Only files in Allowed list may be
touched.

## Execution Plan

1. Read all required first reads.
2. Confirm `ExecuteRequestPayload.provider` field location.
3. Add `parseProviderMap()` + `resolveProviderForRole()` to execute.client.ts.
4. Update `buildExecutePayload()` to use per-role provider when `--providers` present.
5. Add `--providers` flag to command registry for both `execute` and `workflow`.
6. Write `provider-map.test.ts` — test parse, resolve, fallback.
7. Run `npm test` in CLI package — all PASS.
8. Run TypeScript check.
9. Run live proof: `cvf execute --template strategy_analysis --role AI_AGENT --providers ai_agent:alibaba`.
10. Run governance gates with `--base 60fc3b32`.
11. Update session continuity.
12. Commit.
13. Write Fast Lane audit + completion review.

## Evidence Requirements

- `parseProviderMap()` parses correctly; fallback works
- `--providers` flag accepted by both `execute` and `workflow`
- Per-role provider used in `ExecuteRequestPayload.provider` field
- Tests PASS
- TypeScript PASS
- Live proof receipt showing correct provider routing

## Acceptance Criteria

- [ ] `--providers` flag on `cvf execute` and `cvf workflow`
- [ ] `parseProviderMap()` implemented and tested
- [ ] Per-role provider correctly resolved in `buildExecutePayload`
- [ ] Tests PASS
- [ ] TypeScript PASS
- [ ] Live proof receipt with per-role provider
- [ ] Session continuity updated

Fail conditions:
- `--providers` flag silently ignored
- Wrong provider used for role
- Tests fail

## Review Gate

`parseProviderMap` tests PASS; correct provider in payload for given role;
fallback works; TypeScript PASS; live receipt shows correct provider.

## Closure Checklist

- [ ] `parseProviderMap()` + `resolveProviderForRole()` in execute.client.ts
- [ ] `--providers` flag registered in command.registry.ts
- [ ] `buildExecutePayload` uses per-role provider
- [ ] `provider-map.test.ts` PASS
- [ ] TypeScript PASS
- [ ] Live proof receipt
- [ ] Fast Lane audit PASS
- [ ] Session continuity updated
- [ ] Completion review written

## Return-To-Orchestrator Conditions

Stop if: `ExecuteRequestPayload.provider` field not found or type conflict;
tests fail with no clear fix; TypeScript errors not resolvable in bounded scope.

## Operator Checkpoint

operator.checkpoint.waiver: Operator authorized WCE directly 2026-05-29.

## Claim Boundary

W3 proves per-role provider routing in CLI flags. It does not claim Web UI
synchronization, multi-user safety, hosted readiness, or production readiness.
