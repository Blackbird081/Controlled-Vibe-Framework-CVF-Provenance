# CVF GC-009/GC-010 Production Caller T0 Source-Verified Architecture Decision

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

Batch ID: GC009-GC010-PCALLER-T0

Date: 2026-07-25

executionBaseHead: `eefe1e1e2`

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_GC009_GC010_PRODUCTION_CALLER_T0_SOURCE_VERIFIED_ARCHITECTURE_DECISION_2026-07-25.md`

## Terminal Disposition

`NOT_READY_MISSING_SOURCE_VERIFIED_OWNER`

Neither GC-009 (`MandatoryGateway`/`createMandatoryGateway`) nor GC-010
(`AgentExecutionRuntime`) has a non-test production caller today. The
strongest candidate channel (`cvf-web` `/api/execute`) already evaluates
guards through a different, already-wired seam
(`getSharedGuardEngine`/`GuardRuntimeEngine.evaluate`), not through either
helper under decision. Composing either helper into that route requires a
minimal-changed-set T1 proposal and fresh operator authorization; T0 does not
authorize that composition itself.

## Purpose

Answer the seven T0 questions with source citations and issue one terminal
architecture disposition for the paired GC-009/GC-010 production-caller gap
(`cvf.asc.gap.gc009_gc010_no_production_caller.v1`), per
`docs/work_orders/CVF_AGENT_WORK_ORDER_GC009_GC010_PRODUCTION_CALLER_T0_SOURCE_VERIFIED_ARCHITECTURE_DECISION_2026-07-25.md`.

## Scope / Methodology

Bounded, targeted re-verification at `executionBaseHead` `eefe1e1e2`:
direct reads of the two GC-009/GC-010 source files, the package
export/barrel surface, the two strongest current candidate callers
(`cvf-web` execute-route family; MCP server CLI/guard family), the GC-023
exception registry entry for the execute route, and one `rg` negative
search across `EXTENSIONS/` for constructor/invocation call sites of both
helpers. This is not a repeat of the 22,026-file exhaustive T2 scan; it
relies on the accepted T2 corpus for repository-wide absence evidence and
adds only fresh, named-target confirmation.

## Source Map

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` - 
 `MandatoryGateway` class (line 66), `createMandatoryGateway` factory
 (line 219).
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` - 
 `AgentExecutionRuntime` class (line 130), full
 `parseIntent -> preCheck -> execute -> postCheck` pipeline via `run()`
 (lines 358-372).
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` - barrel export list (lines
 12-129); neither `./runtime/mandatory-gateway` nor
 `./runtime/agent-execution-runtime` appears anywhere in the file.
- `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` - `exports` (lines 8-16)
 and `files` (lines 17-27) both omit `runtime/mandatory-gateway.ts` and
 `runtime/agent-execution-runtime.ts`; only `runtime/agent-handoff.ts` and
 `runtime/agent-coordination.ts` are exported from `runtime/`.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
 (959 lines) - imports `getSharedGuardEngine` (line 11), calls it at line
 561 (`const guardEngine = getSharedGuardEngine();`) and evaluates guards
 at line 578 (`const guardResult: GuardPipelineResult =
 guardEngine.evaluate(guardContext);`). No reference to `MandatoryGateway`,
 `createMandatoryGateway`, or `AgentExecutionRuntime` anywhere in the file.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-engine-singleton.ts`
 - `getSharedGuardEngine()` (lines 21-26) lazily constructs and caches one
 `GuardRuntimeEngine` via `createGuardEngine()` from `cvf-guard-contract`
 (line 13, 23). This is the actual wired seam; it does not construct
 either GC-009 or GC-010 helper.
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/engine.ts` - a second,
 separate `GuardRuntimeEngine` class (line 17) local to the MCP server
 package, distinct from `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts`'s
 class of the same name (named collision recorded below).
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts`
 - imports the MCP-local `GuardRuntimeEngine` type (line 6), not the
 canonical `cvf-guard-contract` package; no reference to either GC-009 or
 GC-010 helper.
- `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` -
 active-owner entry at lines 42-47 for
 `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`,
 plus a resolved exception tombstone at lines 159-172. The tombstone's
 `approvedMaxLines: 1001` is explicitly non-usable; the active-owner entry
 requires shrink or split evidence for future adjacent route work. Current
 file length is 959 lines, 41 lines below the 1000-line hard threshold.

## Caller-Candidate Comparison

| Candidate | Current wiring | GC-009/GC-010 relationship | Verdict |
|---|---|---|---|
| `cvf-web` `/api/execute` route + `guard-engine-singleton` | Already calls `getSharedGuardEngine().evaluate(...)` (`route.ts:561,578`) via the canonical `createGuardEngine()` factory (`index.ts:117-130`) | Does not construct or invoke `MandatoryGateway`/`createMandatoryGateway` or `AgentExecutionRuntime` anywhere | Strongest candidate host - already a proven, canonical, non-test production execution channel; but currently bypasses both helpers under decision |
| MCP server CLI/guard family (`guards/engine.ts`, `cli/governed-command-launcher.ts`, `cli/governed-exec.ts`) | Uses a separate, non-canonical `GuardRuntimeEngine` implementation local to the MCP package (`guards/engine.ts:17`), not the `cvf-guard-contract` package | Does not construct or invoke either helper; not even wired to the canonical package the helpers live in | Weaker candidate - would require first unifying the MCP server onto the canonical `cvf-guard-contract` engine before either helper could be composed |
| Other bounded search | `rg` search below found only test files and the factory's own internal `new MandatoryGateway(...)` inside `createMandatoryGateway` (`mandatory-gateway.ts:223`) | No other non-test candidate discovered | No discrepancy from the accepted T2 finding |

**Q1 answer:** the `cvf-web` `/api/execute` route family, via its shared
`guard-engine-singleton`, is the best host for the smallest production
caller. It is already a live, canonical, non-test production execution
channel wired to the same `cvf-guard-contract` package both GC-009 and
GC-010 helpers live in - unlike the MCP server family, which runs a
separate non-canonical guard engine and would need its own unification
work first.

## Owner / Authority Boundary

No file currently owns a non-test call to either helper. If T1 is
authorized, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-engine-singleton.ts`
or a new sibling module in the same `lib/` directory is the natural owner
location - not `route.ts` itself, since `route.ts` is already a
near-threshold GC-023 active-owner file (959/1000 hard-threshold lines).
Future adjacent route work must carry shrink or split evidence; the resolved
1001-line tombstone is not a usable cap.

## Composition Decision

**Q2 answer:** GC-009 and GC-010 should be proven through two explicitly
related but separately callable seams, not force-composed into one caller
in T1. `MandatoryGateway` wraps a single synchronous `check()`/
`assertAllowed()` call against an existing `GuardRuntimeEngine` instance;
`AgentExecutionRuntime` is a multi-step async pipeline
(`parseIntent -> preCheck -> execute -> postCheck`) that itself calls
`guardEngine.evaluate()` directly (`agent-execution-runtime.ts:208`),
duplicating rather than depending on `MandatoryGateway`. They are
independent consumers of the same `GuardRuntimeEngine`, not a composition
chain - a single combined caller would conflate two different execution
models (single-check gateway vs. full agent pipeline) without source
evidence that either needs the other.

## Existing Enforcement / Receipt / Projection Seams

**Q3 answer:**

- Enforcement seam: `getSharedGuardEngine()` returns one cached
 `GuardRuntimeEngine` (via `createGuardEngine()`, `index.ts:117-130`,
 pre-loaded with all 8 hardened guards). `MandatoryGateway.check()`
 (`mandatory-gateway.ts:80-180`) and `AgentExecutionRuntime.preCheck()`
 (`agent-execution-runtime.ts:170-209`) both accept a `GuardRuntimeEngine`
 by constructor injection, so either could be composed with the existing
 singleton engine without changing its construction.
- Receipt seam: `MandatoryGateway` keeps an in-memory `auditLog:
 GatewayResult[]` (`mandatory-gateway.ts:69,178,195-197`);
 `AgentExecutionRuntime` keeps an in-memory `executionLog: ExecutionResult[]`
 (`agent-execution-runtime.ts:134,241,279,306,324,376-378`). Neither
 persists to a durable store; `route.ts` has its own separate receipt/audit
 path (`buildEvidenceReceipt`, `appendAuditEvent`, imports at lines 19, 24)
 that is unrelated to either helper's internal log.
- Operator projection seam: none exists for either helper today; no UI or
 CLI surface reads `MandatoryGateway.getAuditLog()` or
 `AgentExecutionRuntime.getExecutionLog()`.

## Minimal T1 Changed-Set Proposal (not authorized by T0)

**Q4 answer:** the smallest plausible T1 changed set, if a future
work order is authorized, is: one new or extended module beside
`guard-engine-singleton.ts` that constructs `createMandatoryGateway(getSharedGuardEngine())`
once and exposes a `check()`/`assertAllowed()` call; `route.ts` itself must
not grow (959/1000-line hard-threshold headroom is 41 lines, and the
active-owner entry requires future adjacent route work to carry shrink or
split evidence). `AgentExecutionRuntime` composition is out of scope
for this minimal proposal since it duplicates the guard-evaluation call
`route.ts` already performs directly.

## Deterministic Proof Seams

**Q5 answer:** a positive case (`MandatoryGateway.check()` returns
`decision: 'ALLOW'` for a benign action) and a fail-closed negative case
(`check()` returns `decision: 'BLOCK'` with `allowed: false` for a
protected-path action, per `hardBlock: true` default,
`mandatory-gateway.ts:55,150-153`) can both be proven with existing unit
fixtures and a new integration test against the real singleton engine - 
no live provider call is required, since `GuardRuntimeEngine.evaluate()`
is fully deterministic guard logic.

## Unavailable / Live-Provider-Dependent Items

**Q6 answer:** nothing in this T0 decision requires live/provider
authority; all evidence is static source and one guard-evaluation call
path, both provable without a network or provider call. Live/provider
proof only becomes relevant at T2 (invocation proof) per the companion
roadmap, which remains `HOLD_*` and is not authorized by this T0 decision.

## NOT_READY Determination

**Q7 answer:** yes, `NOT_READY_MISSING_SOURCE_VERIFIED_OWNER` is correct.
No source file currently owns a non-test call to either GC-009 or GC-010
helper. The missing owner is precisely the T1 composition module described
above (a `guard-engine-singleton.ts`-adjacent module wiring
`createMandatoryGateway` to the existing shared engine); until that module
exists and is proven, no `READY` disposition is supportable from current
source.

## Negative Search And Collision Discipline

Command:

```
rg -n "new MandatoryGateway|createMandatoryGateway\(|new AgentExecutionRuntime" EXTENSIONS --glob "!**/node_modules/**" --glob "!**/dist/**" --glob "!**/coverage/**"
```

Result: 16 matches, all inside `*.test.ts` files
(`gemini-provider.test.ts` x3, `alibaba-dashscope-provider.test.ts` x2,
`mandatory-gateway.test.ts` x7, `agent-execution-runtime.test.ts` x1)
except the factory's own internal construction inside
`createMandatoryGateway` (`mandatory-gateway.ts:219,223`), which is not a
caller. Zero non-test callers found - consistent with the accepted T2
finding; no discrepancy to flag.

Known collision recorded: `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/engine.ts`
defines a `GuardRuntimeEngine` class (line 17) that shares a bare name with
`EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts`'s `GuardRuntimeEngine` class
but is a distinct, non-canonical implementation. This search targeted only
`MandatoryGateway`/`createMandatoryGateway`/`AgentExecutionRuntime`
identifiers, which do not collide with this class-name pair, so the
collision does not affect the result above; it is recorded per the work
order's explicit instruction.

## Export/Barrel/Package-Surface Disposition

Both helpers remain unexported from the canonical package surface:
`src/index.ts` (lines 12-129) and `package.json` `exports`/`files` (lines
8-27) omit `runtime/mandatory-gateway` and `runtime/agent-execution-runtime`
entirely. A future T1 would need to add both to `package.json` `exports`
and `files`, and add corresponding named exports to `src/index.ts`, before
any consumer outside the package could import them by package specifier
(current test files import by relative path only, bypassing the barrel).

## Rollback Boundary

T0 makes no source change, so there is no rollback boundary for this
artifact itself. For the T1 proposal sketched above (informational only,
not authorized here): rollback would mean deleting the new composition
module and reverting any `package.json`/`index.ts` export additions, with
no data migration since both helpers are stateless in-memory classes.

## Latency/Complexity Risks

Composing `MandatoryGateway` on top of the already-evaluated
`guardEngine.evaluate()` call in `route.ts` would double-evaluate guards
per request unless the composition reuses the same `GuardPipelineResult`
rather than re-running `check()`. `AgentExecutionRuntime.run()` runs a full
`parseIntent -> preCheck -> execute -> postCheck` pipeline including its own
`guardEngine.evaluate()` call (`agent-execution-runtime.ts:208`) - using it
alongside the route's existing direct evaluation would similarly duplicate
guard evaluation. Any T1 proposal must resolve this before composition, not
after.

## No-Provider/No-External-Invocation Boundary

This decision cites only static source reads and one read-only `rg`
search. No provider, network, browser, CLI, or MCP invocation was
performed in producing it.

## Unresolved Facts

- Whether a T1 composition should reuse the route's existing
 `GuardPipelineResult` (avoiding double evaluation) or call
 `MandatoryGateway.check()` independently is not resolved by source
 alone; it requires a design decision in a future T1 packet.
- No operator projection surface exists for either helper's internal log
 today; whether T1 needs one is unresolved and out of scope for T0.

## Findings / Position

Terminal disposition `NOT_READY_MISSING_SOURCE_VERIFIED_OWNER` is
supported by fresh source evidence gathered at `executionBaseHead`
`eefe1e1e2`: neither GC-009 nor GC-010 has a non-test production caller,
confirming and refreshing the accepted T2 finding rather than
contradicting it. See `## Caller-Candidate Comparison` and `## Source
Verification Block` above for the full evidence chain.

## Risk / Corrective Action

No corrective action required from this T0 decision itself; it makes no
runtime change. If T1 is authorized in future, the `## Minimal T1
Changed-Set Proposal` section above already flags the primary risk: any
composition module must avoid double-evaluating guards against
`route.ts`'s existing `guardEngine.evaluate()` call, and `route.ts`
(959/1000 hard-threshold lines) must not grow; future adjacent route work
must carry shrink or split evidence under the GC-023 active-owner entry.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Category | Learning lane | Disposition | Next control action |
|---|---|---|---|---|---|
| No non-test caller exists for either GC-009 or GC-010 helper as of `eefe1e1e2`, confirmed by fresh targeted re-verification consistent with the accepted T2 corpus | RUNTIME_SIGNAL_GAP | SOURCE_FIDELITY | N/A_WITH_REASON - this is a confirmed absence finding already recorded in the gap entry and control matrix, not a new runtime, provider, token, latency, or cost-economics finding requiring a new governance rule | NO_ACTION_REQUIRED | next action: none - the accepted T2 gap entry and control matrix already record this finding; no new control is created by this reconfirmation |

Runtime/provider/cost learning lane: N/A_WITH_REASON - this finding
reconfirms an already-accepted architecture-discoverability gap; it does
not describe new runtime behavior, provider output, or cost/economics
data requiring a `RUNTIME_BEHAVIOR_LEARNING`, `PROVIDER_OUTPUT_LEARNING`,
or `COST_ECONOMICS_LEARNING` lane.

## Explicit T1 Release-Or-Hold Decision

**HOLD.** T1 is not released by this T0 decision. The companion roadmap's
`HOLD_*` gate for T1 remains in force. A fresh work order and fresh
operator authorization are required before any package-export,
barrel-export, or new-composition-module change may be made, per the
Minimal T1 Changed-Set Proposal above (informational only).

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Source fact type | Disposition |
|---|---|---|---|---|---|
| `MandatoryGateway` class and `createMandatoryGateway` factory | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 66, 219 | `MandatoryGateway`; `createMandatoryGateway` | EXISTS | ACCEPT |
| `AgentExecutionRuntime` class | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | line 130 | `AgentExecutionRuntime` | EXISTS | ACCEPT |
| Barrel omits both runtime modules | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | lines 12-129 | `export *`; named exports | LITERAL_INVARIANT | ACCEPT |
| Package exports/files omit both runtime modules | `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` | lines 8-27 | `exports`; `files` | LITERAL_INVARIANT | ACCEPT |
| `route.ts` calls shared guard engine directly | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 11, 561, 578 | `getSharedGuardEngine`; `guardEngine.evaluate` | RUNTIME_BEHAVIOR | ACCEPT |
| Shared guard engine singleton sources canonical factory | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-engine-singleton.ts` | lines 13, 21-26 | `getSharedGuardEngine`; `createGuardEngine` | EXISTS | ACCEPT |
| Canonical factory registers 8 hardened guards | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | lines 117-130 | `createGuardEngine` | EXISTS | ACCEPT |
| MCP server guard engine is separate, non-canonical | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/engine.ts` | lines 1-17 | `GuardRuntimeEngine` | EXISTS | ACCEPT |
| Governed CLI launcher imports MCP-local engine type only | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 1-6 | `GuardRuntimeEngine` | EXISTS | ACCEPT |
| `route.ts` is a GC-023 active owner; its prior exception is a resolved, non-usable tombstone | `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` | lines 42-47; 159-172 | `activeOwners`; `status`; `removalProcedure` | LITERAL_INVARIANT | ACCEPT |
| `route.ts` current line count | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | `wc -l` output | 959 | RUNTIME_BEHAVIOR | ACCEPT |
| Gap entry status is `IMPLEMENTED_NOT_INVOCATION_PROVEN` with an open close condition | `docs/reference/system_chain/gaps/entries/gc009_gc010_no_production_caller.json` | `currentStatus`; `closeCondition.conditionText` | `currentStatus`; `closeCondition.conditionText` | VALUE_SET | ACCEPT |
| T2 accepted no-caller finding for GC-009 and GC-010 | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_EXHAUSTIVE_PROOF_T2_CALLER_VERIFICATION.json` | `targetDecisions[0]`; `targetDecisions[1]` | `callerVerificationDisposition` | VALUE_SET | ACCEPT |
| Fresh `rg` negative search finds only test-file and factory-internal construction | (search command, not a single file) | see Negative Search And Collision Discipline | `MandatoryGateway`; `createMandatoryGateway`; `AgentExecutionRuntime` | RUNTIME_BEHAVIOR | ACCEPT |

## Claim Boundary

This artifact is a bounded T0 documentation-only architecture decision. It
does not authorize, perform, or claim any package-export change, barrel
change, new module creation, CLI/MCP invocation, provider/live proof, or
public-sync. Its terminal disposition is
`NOT_READY_MISSING_SOURCE_VERIFIED_OWNER`; no `READY` composition is
claimed or implied to exist in current source.
