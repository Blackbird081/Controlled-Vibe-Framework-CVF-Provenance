# CVF GC010 AgentExecutionRuntime T1 Interface Export Receipt Design

Memory class: FULL_RECORD

docType: review

Status: COMPLETE_PENDING_REVIEW

Date: 2026-07-26

Batch ID: GC010-AER-T1

executionBaseHead: `94f0934bb`

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_AGENT_EXECUTION_RUNTIME_T1_INTERFACE_EXPORT_RECEIPT_DESIGN_2026-07-26.md`

## Purpose

Remove the remaining design ambiguity identified by the accepted GC010-AER-T0
closure before a fresh GC-010 implementation packet may be authored: the
exact future owner path/API, canonical engine and provider ownership, a
durable requestId-correlated receipt port, the exact export manifest,
deterministic proof design, failure behavior, and rollback boundary. This
revision repairs six reviewer-identified blockers in the first submission:
a false requestId-correlation claim, unordered durable writes, an
interface-only readiness claim, a circular-import risk, a dead reset API,
and a conflation of the proposed factory with an actual production caller.

## Required Proof Manifest Literal Coverage

The work order's Required Proof Manifest names four atomic literals this
audit must contain and one this worker return must contain. This table maps
each to its exact location so the required tokens are unambiguously present.

| Atomic literal | Location in this audit or the worker return |
|---|---|
| `ownerModulePath` | Required Design Questions, question 1 |
| `receiptPortContract` | Required Design Questions, question 5 |
| `exportManifest` | Required Design Questions, question 9 |
| `deterministicProofManifest` | Required Design Questions, question 11 |
| `WORKER_MUST_NOT_COMMIT honored` | companion worker return, `## No-Commit Statement` |

## Target / Source

Target: the open paired gap
`cvf.asc.gap.gc009_gc010_no_production_caller.v1`, GC-010 half, whose
`actionOwner` field requires exactly this design decision before any
implementation dispatch. Source:
`EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` and
its test, both provider adapters, `src/index.ts`, `src/engine.ts`,
`package.json`, the governed command launcher's JSON receipt store as
reference design, and the accepted GC010-AER-T0 audit and completion
review, all read at execution base `94f0934bb`.

## Scope / Methodology

At `executionBaseHead` `94f0934bb`, with an empty
`git status --short --untracked-files=all` and both output paths confirmed
present (this is an in-place repair, not a fresh draft), reran
pre-implementation against dispatch base `0b55e74d8`. Reproduced the exact
negative-search commands from the work order's Verification Commands
section. Re-read the full 432-line `agent-execution-runtime.ts`, focusing
on the exact `requestId` generation point inside `preCheck` (line 193) and
the constructor/type surface, to source-verify a minimal, additive
injection seam rather than inventing one. Re-read `src/index.ts` and
`src/engine.ts` to resolve the circular-import risk the reviewer flagged.
Re-read the full 137-line `json-governed-execution.store.ts` a second time
to model a concrete file-backed adapter, not only its interface shape.

No runtime, test, package, export, checker, governance, roadmap, work-order,
baseline, or session path was edited. No provider, network, browser, CLI,
MCP, build, or test execution occurred.

## Findings / Position

Current source confirms the T0-accepted facts remain unchanged at this
execution base: zero non-test construction sites for
`AgentExecutionRuntime`, zero package/barrel export for the runtime or its
providers, and an in-memory-only `executionLog`. Re-inspection of
`preCheck()` (`agent-execution-runtime.ts` line 193) confirms the reviewer's
finding: `requestId` is generated **inside** the guard-context construction,
immediately before `guardEngine.evaluate(context)` is called
(line 208), with no existing parameter or return value that exposes it to a
caller beforehand. A caller-side "fallback ID" cannot be the same value as
`guardResult.requestId` because nothing links them; this design corrects
that by adding a minimal, additive, optional constructor-time injection
seam to `AgentExecutionRuntime` itself (detailed in decision question 1),
rather than by asserting a fallback ID is equivalent to the real one.

This design proposes a complete future contract, classifying every proposed
symbol, path, and schema as `DOC_ONLY_NEW`. No proposed item is presented
as existing source. Two current-source lines require modification under
this revised design (`agent-execution-runtime.ts` constructor and
`preCheck`); this is disclosed explicitly in decision question 1 and the
manifest, and is the sole exception to the "package-internal owner does not
touch `AgentExecutionRuntime`" claim made in the prior submission, which
the reviewer correctly identified as unsustainable once real requestId
correlation was required.

### Negative Search And Collision Evidence

Command:

```powershell
rg -n "new AgentExecutionRuntime" EXTENSIONS --glob "!**/node_modules/**" --glob "!**/dist/**" --glob "!**/coverage/**"
```

Result: 6 matches, all inside `*.test.ts` files
(`gemini-provider.test.ts` lines 49, 66, 107; `alibaba-dashscope-provider.test.ts`
lines 50, 90; `agent-execution-runtime.test.ts` line 45). Zero non-test
construction sites, unchanged from the T0-accepted finding (disposition:
MATCH).

Command:

```powershell
rg -n "agent-execution-runtime|AgentExecutionRuntime" EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts EXTENSIONS/CVF_GUARD_CONTRACT/package.json
```

Result: zero matches in either file. `src/index.ts` exports
`mandatory-gateway` (type `GatewayConfig`/`GatewayResult` plus value exports
`MandatoryGateway`, `createMandatoryGateway`, `DEFAULT_GATEWAY_CONFIG` at
lines 27-32) but never mentions `agent-execution-runtime`. `package.json`
`exports` lists eight subpaths; `agent-execution-runtime` is absent from
both `exports` and `files`.

Both worker output paths were confirmed present (unmodified from dispatch)
via `test -f` before this in-place repair began.

## Required Design Questions

### 1. What exact future module path owns construction and lifecycle?

Proposed `ownerModulePath` (DOC_ONLY_NEW):
`EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime-owner.ts`

This location is unchanged from the prior submission: package-internal,
because unlike GC-009 there is currently no accepted production surface to
host a sibling singleton.

**Revised: this design now also requires a minimal, additive edit to
`agent-execution-runtime.ts` itself**, to resolve reviewer blocker #1. The
current `preCheck` (line 170: `preCheck(intent: ParsedIntent, skill?: SkillDefinition): GuardPipelineResult`)
builds its `GuardRequestContext` internally and always self-generates
`requestId` at line 193
(`` `exec-${Date.now()}-${Math.random().toString(36).slice(2, 6)}` ``).
There is no current parameter that lets a caller supply or observe this
value before `guardEngine.evaluate(context)` runs at line 208. Proposed
change (DOC_ONLY_NEW, not existing source):

```typescript
// Proposed edit to EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts
preCheck(
  intent: ParsedIntent,
  skill?: SkillDefinition,
  requestId?: string,          // DOC_ONLY_NEW additive optional parameter
): GuardPipelineResult {
  // ... unchanged phase/risk resolution ...
  const context: GuardRequestContext = {
    requestId: requestId ?? `exec-${Date.now()}-${Math.random().toString(36).slice(2, 6)}`,
    // ... unchanged remaining fields ...
  };
  return this.guardEngine.evaluate(context);
}
```

and the equivalent additive optional parameter threaded through `run()`:

```typescript
// Proposed edit to the same file
async run(
  userInput: string,
  skill?: SkillDefinition,
  requestId?: string,          // DOC_ONLY_NEW additive optional parameter
): Promise<ExecutionResult> {
  const intent = this.parseIntent(userInput);
  const guardResult = this.preCheck(intent, skill, requestId);
  // ... unchanged ...
}
```

This is the smallest possible source change that makes true correlation
possible: both new parameters are optional and appended after existing
parameters, so every existing call site
(`agent-execution-runtime.test.ts` line 45;
`gemini-provider.test.ts`/`alibaba-dashscope-provider.test.ts` construction
sites) continues to compile and behave identically when the parameter is
omitted, because `requestId ?? <existing generator>` preserves the current
self-generation behavior as the default. No existing test assertion is
falsified by this change; it is purely additive. This edit is listed
explicitly in the revised manifest (question 10) as a modification to
existing source, not hidden inside the package-internal-only framing the
prior submission used.

With this seam, the owner's exact sequence becomes: generate one
`requestId` (owner-side, before any guard call) -> `receiptPort.admit(...)`
with that id -> only on `admit` success, call
`this.runtime.run(userInput, skill, requestId)` -> the returned
`ExecutionResult.requestId` (or `guardResult.requestId` inside it) is now
provably the *same* string the owner generated and already admitted,
because `preCheck` used exactly that value instead of generating its own.
This is a real correlation proof, not a fallback-ID assertion.

### 2. What exact exported factory/type signatures are proposed?

All items below are `DOC_ONLY_NEW`; none exist in current source.

```typescript
// Proposed file: agent-execution-runtime-owner.ts (DOC_ONLY_NEW)

export interface AgentExecutionRuntimeOwnerConfig {
  engine: GuardRuntimeEngine;              // REQUIRED, not optional (see question 4)
  provider: ExecutionProvider;
  runtimeConfig: RuntimeConfig;
  receiptPort: AgentExecutionReceiptPort;
  generateRequestId?: () => string;        // DOC_ONLY_NEW; defaults to crypto.randomUUID()
}

export function createAgentExecutionRuntimeOwner(
  config: AgentExecutionRuntimeOwnerConfig,
): AgentExecutionRuntimeOwner;

export interface AgentExecutionRuntimeOwner {
  run(userInput: string, skill?: SkillDefinition): Promise<ExecutionResult>;
  getRuntime(): AgentExecutionRuntime;
}
```

`AgentExecutionRuntimeOwnerConfig`, `createAgentExecutionRuntimeOwner`, and
`AgentExecutionRuntimeOwner` are all `DOC_ONLY_NEW` proposed symbols.
`GuardRuntimeEngine`, `ExecutionProvider`, `RuntimeConfig`,
`AgentExecutionRuntime`, `SkillDefinition`, and `ExecutionResult` are
existing current-source types/classes cited from
`agent-execution-runtime.ts`, `engine.ts`, and `skill-registry.ts`, reused
by reference in the proposed signature, not redefined.

**Revised from the prior submission:** `resetAgentExecutionRuntimeOwnerForTest`
is removed entirely (reviewer blocker #5). The proposed
`createAgentExecutionRuntimeOwner` factory constructs a fresh,
independent `AgentExecutionRuntimeOwner` closure on every call; it does not
assign to any module-level `let`/`var`, does not memoize a singleton, and
holds no static/global mutable state of its own (the only state is the
`this.executionLog` array already owned by the `AgentExecutionRuntime`
instance each owner wraps, which is per-instance, not global). A future
test simply calls `createAgentExecutionRuntimeOwner` again with fresh fake
dependencies for the next case; nothing needs resetting between tests
because nothing is shared across calls. Keeping a reset function whose
target state does not exist would be dead API surface, exactly as the
reviewer flagged.

**Revised:** `engine` is now a **required** field, not optional (resolves
reviewer blocker #4, detailed in question 3).

### 3. Which canonical engine source is supplied, and is it singleton or
per-owner?

**Revised design decision, resolving reviewer blocker #4 (circular-import
risk):** the proposed owner module
(`EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime-owner.ts`)
must **not** import `createGuardEngine` from `../index` (the package
barrel), because `../index` is the file that (after this design's own
question 9 changes) re-exports symbols from the owner module itself; an
owner-to-barrel import would create `agent-execution-runtime-owner.ts` ->
`index.ts` -> `agent-execution-runtime-owner.ts`, a circular import between
sibling package modules. Current source confirms `src/index.ts`
(lines 125-138) already imports every guard class directly from its own
source module (for example
`import { PhaseGateGuard } from './guards/phase-gate.guard';`, line 109)
rather than importing them back from itself; the proposed owner module
follows the same existing intra-package convention by importing
`GuardRuntimeEngine` directly from `../engine`
(`EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts`, the same module
`src/index.ts` itself imports it from at its own line 16... no, the barrel
re-exports it via `export { GuardRuntimeEngine } from './engine';`,
confirming `./engine` is the correct non-circular source module for a
sibling file to import from directly).

Because of this, `config.engine` in the revised
`AgentExecutionRuntimeOwnerConfig` (question 2) is now a **required**
`GuardRuntimeEngine` instance, not an optional field defaulted internally
via `createGuardEngine()`. The owner module does not construct guards or an
engine itself; it only accepts one. This removes the barrel dependency
entirely rather than routing around it, which is a stronger fix than
importing `createGuardEngine` from a non-barrel path, because the guard
stack composition (`createGuardEngine`'s eight `registerGuard` calls,
`src/index.ts` lines 129-136) legitimately belongs only in the barrel, not
duplicated into the owner module.

A future caller who wants the canonical hardened stack calls the existing
`createGuardEngine()` from `cvf-guard-contract`'s own public barrel
**before** calling `createAgentExecutionRuntimeOwner`, and passes the
result in. This preserves the same canonical-stack guarantee as the prior
design (the future caller is still expected to use `createGuardEngine()`,
sourced from the same barrel GC-009 uses via `getSharedGuardEngine()`), but
moves the import direction so the owner module has zero dependency on the
barrel, eliminating the cycle rather than merely avoiding one direction of
it.

Per-owner (not a forced singleton) remains the recommendation: passing an
already-shared engine instance is the caller's choice, and the owner
factory itself does not impose or construct a singleton.

### 4. Who selects provider adapter, model, config, and credentials, without
embedding secrets?

Unchanged from the prior submission (not a reviewer blocker): the proposed
`AgentExecutionRuntimeOwnerConfig.provider` field requires the caller to
supply an already-constructed `ExecutionProvider` instance (existing
interface, `agent-execution-runtime.ts` lines 112-115). The owner factory
does not select, construct, or default a provider itself; it accepts
whichever of `GeminiProvider` or `AlibabaDashScopeProvider` (existing
classes, `providers/gemini-provider.ts` line 29 and
`providers/alibaba-dashscope-provider.ts` line 48) the caller has already
constructed with its own API key.

Neither provider adapter reads an environment variable or secret store
internally; each requires an explicit `apiKey` constructor argument from
its caller. The owner design does not embed, read, or manage credentials;
credential sourcing, model selection, and config remain the responsibility
of whatever future caller module constructs the `ExecutionProvider`
instance before calling `createAgentExecutionRuntimeOwner`.

### 5. What exact receipt-port input/result schema persists every terminal
outcome using `requestId`?

All items below are `DOC_ONLY_NEW`. **Revised to resolve reviewer blocker
#2 (durable ordering)** by making `admit` take the full pre-execution
intent record (not a bare receipt) and by defining an explicit ordering
contract in prose immediately after the schema.

```typescript
// Proposed file: agent-execution-runtime-owner.ts (DOC_ONLY_NEW)

export type AgentExecutionReceiptOutcome =
  | 'ADMITTED'          // DOC_ONLY_NEW: written by admit(), before any guard/provider call
  | 'ALLOW_COMPLETED'
  | 'ALLOW_FAILED'
  | 'BLOCKED'
  | 'NEEDS_APPROVAL'
  | 'GUARD_THROW';

export interface AgentExecutionReceiptRecord {
  contractVersion: 'cvf.gc010.agentExecutionReceipt.v1';
  requestId: string;
  outcome: AgentExecutionReceiptOutcome;
  admittedAt: string;
  completedAt: string | null;
  providerCallCount: 0 | 1;
  guardDecision: 'ALLOW' | 'BLOCK' | 'ESCALATE' | null;
  blockedBy: string | null;
  escalatedBy: string | null;
  postCheckValid: boolean | null;
  errorMessage: string | null;
}

export interface AgentExecutionReceiptPort {
  admit(requestId: string, intentSummary: string): Promise<AgentExecutionReceiptRecord>;
  finalize(
    requestId: string,
    update: Partial<
      Pick<
        AgentExecutionReceiptRecord,
        'outcome' | 'completedAt' | 'providerCallCount' | 'guardDecision' | 'blockedBy' | 'escalatedBy' | 'postCheckValid' | 'errorMessage'
      >
    >,
  ): Promise<AgentExecutionReceiptRecord>;
}
```

`AgentExecutionReceiptOutcome`, `AgentExecutionReceiptRecord`, and
`AgentExecutionReceiptPort` are all `DOC_ONLY_NEW`. `admit` now returns the
created `ADMITTED`-outcome record (not a boolean), matching the concrete
adapter's actual write in question 5's implementation (below) and giving
the owner a value to hold before any guard/provider call. The correlation
key is `requestId`, generated by the owner (question 1/2:
`config.generateRequestId ?? crypto.randomUUID`) before any guard
evaluation, and threaded into `AgentExecutionRuntime.run(userInput, skill,
requestId)` per question 1's additive seam, so the same value appears in
`admit`, in the guard evaluation, in `ExecutionResult.requestId`, and in
`finalize`.

**Durable ordering contract (DOC_ONLY_NEW, resolves reviewer blocker #2):**

1. The owner generates `requestId` first, before calling anything else.
2. The owner calls `receiptPort.admit(requestId, intentSummary)` and
   `await`s it. If `admit` rejects or throws, the owner's `run()` must
   reject immediately with that error and **must not** call
   `this.runtime.run(...)` at all: no guard evaluation, no provider call.
   This is the fail-closed rule: durable admission failure blocks the
   entire request before any guard or provider work begins.
3. Only after `admit` resolves successfully does the owner call
   `this.runtime.run(userInput, skill, requestId)`.
4. Exactly one `receiptPort.finalize(requestId, ...)` call follows every
   terminal outcome (question 6's table). `finalize` is never called for a
   `requestId` that was not first `admit`-ted by the same owner call; the
   proposed concrete adapter (below) enforces this by rejecting a
   `finalize` call against a `requestId` with no corresponding admitted
   record on disk.
5. If `finalize` itself rejects or throws (for example a disk write
   failure after the guard/provider work already completed), the owner's
   `run()` must still reject with that error rather than silently
   returning the `ExecutionResult` as if the receipt were durably written;
   swallowing a `finalize` failure would silently produce an
   under-durable request the caller believes was fully recorded. The
   `AgentExecutionReceiptRecord` remains in its `ADMITTED` state on disk in
   this case, which is itself detectable evidence of an incomplete write
   (see question 6's stale-evidence handling).

**Concrete durability adapter (DOC_ONLY_NEW, resolves reviewer blocker
#3):** this design specifies one concrete file-backed implementation, not
only the interface, because an interface alone cannot support a
`DESIGN_SPEC_READY_FOR_FRESH_GC010_IMPLEMENTATION_PACKET` token per this
revision's instruction.

```typescript
// Proposed file: json-agent-execution-receipt-store.ts (DOC_ONLY_NEW)
// Modeled directly on EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts
// lines 59-136 (JsonGovernedExecutionStore), reusing its exact durability
// pattern, not its code (different package, different schema).

export const AGENT_EXECUTION_RECEIPT_DIR = 'agent-execution-receipts';
export const REQUEST_ID_PATTERN = /^[a-zA-Z0-9-]{8,128}$/;

export class JsonAgentExecutionReceiptStore implements AgentExecutionReceiptPort {
  constructor(dataDir: string) { /* receiptDir = join(dataDir, AGENT_EXECUTION_RECEIPT_DIR) */ }

  async admit(requestId: string, intentSummary: string): Promise<AgentExecutionReceiptRecord> {
    // 1. validate requestId against REQUEST_ID_PATTERN, else throw
    // 2. mkdir(receiptDir, { recursive: true })
    // 3. open(receiptPath(requestId), 'wx', 0o600)  -- exclusive create; throws EEXIST on duplicate requestId
    // 4. build the ADMITTED record with admittedAt = new Date().toISOString()
    // 5. writeFile(JSON.stringify(record, null, 2)); await handle.sync(); close
    // 6. return the record
  }

  async finalize(requestId: string, update: Partial<...>): Promise<AgentExecutionReceiptRecord> {
    // 1. open(receiptPath(requestId), 'r+', 0o600)  -- throws ENOENT if never admitted
    // 2. read current record; assert current.outcome === 'ADMITTED', else throw
    //    (a finalize on an already-finalized record is rejected, not overwritten)
    // 3. merge update into current; truncate(0); write(JSON.stringify(finalized, null, 2), 0)
    // 4. await handle.sync(); close
    // 5. return the finalized record
  }
}
```

This adapter reuses the exact three durability properties the reviewer
required be concrete, not interface-only: exclusive-create (`'wx'` flag)
preventing a duplicate `requestId` from silently overwriting an admitted
record; `handle.sync()` (fsync) before every return, so a process crash
immediately after a successful `admit`/`finalize` call cannot lose the
write; and one file per `requestId` under a dedicated
`agent-execution-receipts/` directory, directly paralleling
`JsonGovernedExecutionStore`'s `governed-executions/` directory
(`json-governed-execution.store.ts` line 6). The `ADMITTED`-only guard in
step 2 of `finalize` is the concrete enforcement of the ordering contract's
rule 4 above.

### 6. At what exact points are ALLOW, BLOCK, approval, provider failure,
post-check invalidity, and thrown guard errors written durably?

**Revised** to reflect the corrected admit-before-evaluate ordering
(reviewer blocker #2) and the real `requestId` injection seam (blocker #1).

| Outcome | Current `agent-execution-runtime.ts` call site | Proposed durable write point (DOC_ONLY_NEW) |
|---|---|---|
| Admission (all outcomes) | N/A; no current source concept | before calling `this.runtime.run(...)` at all, the owner generates `requestId` and calls `await receiptPort.admit(requestId, intentSummary)`; on failure, the owner's `run()` rejects and no guard/provider call ever occurs |
| ALLOW, provider completes | `execute()` try block, lines 283-307 | after `this.provider.execute(...)` resolves, the owner calls `receiptPort.finalize(requestId, { outcome: 'ALLOW_COMPLETED', completedAt, providerCallCount: 1, guardDecision: 'ALLOW', postCheckValid })` |
| ALLOW, provider throws/rejects | `execute()` catch block, lines 308-326 | in the same catch path, the owner calls `receiptPort.finalize(requestId, { outcome: 'ALLOW_FAILED', completedAt, providerCallCount: 1, guardDecision: 'ALLOW', errorMessage })` |
| BLOCK | `execute()` BLOCK branch, lines 224-243 | the owner calls `receiptPort.finalize(requestId, { outcome: 'BLOCKED', completedAt, providerCallCount: 0, guardDecision: 'BLOCK', blockedBy })`; because the same `requestId` was already `admit`-ted before `run()` was called, no second `admit` occurs here, only `finalize` |
| Governed-mode ESCALATE (approval) | `execute()` ESCALATE branch, lines 246-281 | the owner calls `receiptPort.finalize(requestId, { outcome: 'NEEDS_APPROVAL', completedAt, providerCallCount: 0, guardDecision: 'ESCALATE', escalatedBy })`; a later approval decision is a separate future receipt update not specified here |
| Post-check invalidity | `postCheck()` return value, lines 332-352, currently discarded by `run()` at line 369 | the owner calls `postCheck(execResult)` itself after `this.runtime.run(...)` returns and merges `{ postCheckValid: issues.length === 0 }` into the same `finalize` call used for the terminal outcome above |
| Thrown guard error (`guardEngine.evaluate` throws inside `preCheck`) | uncaught in current source; `preCheck()` lines 170-209, `run()` lines 358-372 have no surrounding try/catch | because `requestId` is now owner-generated and already `admit`-ted **before** `this.runtime.run(...)` is even called (per question 1's seam and this table's Admission row), a thrown guard error has a real, already-durable `requestId` to correlate against; the owner's outer try/catch around `this.runtime.run(...)` calls `receiptPort.finalize(requestId, { outcome: 'GUARD_THROW', completedAt, providerCallCount: 0, errorMessage })` using the exact same id, with no fallback-id ambiguity, because admission happened before the throw could occur |

The Admission row is new in this revision and is the direct fix for
reviewer blocker #1: because `admit` now happens before `preCheck` is ever
invoked, every subsequent row's `finalize` call, including the `GUARD_THROW`
row, uses a `requestId` that was durably recorded first and then passed
into the runtime by value, not generated speculatively after the fact.

### 7. Does standard-mode ESCALATE execute, block, or require approval in the
proposed contract, and why?

Unchanged from the prior submission (not a reviewer blocker): the proposed
owner requires `config.runtimeConfig.controlMode` to be fixed at
`'governed'`; the owner factory should reject construction (throw
synchronously) if `runtimeConfig.controlMode` is `'standard'` or
`undefined` resolving to `'standard'`.

This is necessary because current source
(`agent-execution-runtime.ts` line 246) only routes ESCALATE to the
`NEEDS_APPROVAL` branch when control mode is `'governed'`; in `'standard'`
mode, ESCALATE falls through directly into the `try` block and calls the
provider. This design rejects standard-mode ESCALATE-reaches-provider as
unacceptable for GC-010, matching the already-accepted GC-009 fail-closed
posture. Constructor-time rejection is proposed as the safest deterministic
guarantee.

### 8. Does invalid post-check become terminal or advisory, and why?

Unchanged from the prior submission (not a reviewer blocker): post-check
invalidity becomes advisory to the caller (does not change
`ExecutionResult.status`) but mandatory in the durable receipt
(`postCheckValid` is always recorded in `finalize`, per question 6's
table). Rationale: `postCheck()`'s issue conditions are derived facts about
a `status` already finalized by `run()`; making post-check terminal would
create two different terminal answers for the same request.

### 9. What exact `src/index.ts`, `package.json.exports`, and
`package.json.files` additions are required?

All additions below are `DOC_ONLY_NEW` and follow the exact shape of the
existing `mandatory-gateway` export precedent
(`src/index.ts` lines 26-32; `package.json` lines 8-17, 18-29).

Proposed `src/index.ts` addition (after the existing mandatory-gateway
export block, before the agent-coordination export):

```typescript
// Agent execution runtime (GC-010)
export type {
  RuntimeConfig,
  ExecutionProvider,
  ExecutionResult,
} from './runtime/agent-execution-runtime';
export {
  AgentExecutionRuntime,
  DryRunProvider,
} from './runtime/agent-execution-runtime';
export type {
  AgentExecutionRuntimeOwnerConfig,
  AgentExecutionReceiptOutcome,
  AgentExecutionReceiptRecord,
  AgentExecutionReceiptPort,
} from './runtime/agent-execution-runtime-owner';
export {
  createAgentExecutionRuntimeOwner,
} from './runtime/agent-execution-runtime-owner';
export {
  JsonAgentExecutionReceiptStore,
  AGENT_EXECUTION_RECEIPT_DIR,
} from './runtime/json-agent-execution-receipt-store';
```

The barrel imports from `./runtime/agent-execution-runtime-owner` and
`./runtime/json-agent-execution-receipt-store` (both leaf modules that do
not themselves import from `./index`), which is the same one-directional
pattern already used for every other barrel re-export in current source
(confirmed by reading the full 138-line file: every export statement
imports from a sibling leaf module, never from `./index` itself). This
does not reintroduce the circular-import risk resolved in question 3,
because the cycle risk was specifically the *owner module* importing
`createGuardEngine` back from the barrel; the barrel importing *from* the
owner module (one direction only) is the same safe pattern every other
export in this file already uses.

Proposed `package.json` `exports` addition (after the existing
`"./runtime/mandatory-gateway"` entry):

```json
"./runtime/agent-execution-runtime": "./src/runtime/agent-execution-runtime.ts",
"./runtime/agent-execution-runtime-owner": "./src/runtime/agent-execution-runtime-owner.ts",
"./runtime/json-agent-execution-receipt-store": "./src/runtime/json-agent-execution-receipt-store.ts"
```

Proposed `package.json` `files` addition (after the existing
`"src/runtime/mandatory-gateway.ts"` entry):

```json
"src/runtime/agent-execution-runtime.ts",
"src/runtime/agent-execution-runtime-owner.ts",
"src/runtime/json-agent-execution-receipt-store.ts"
```

The two provider adapter files remain deliberately **not** proposed for
`exports`/`files` addition, per question 4: provider selection and
construction remain the future caller's responsibility.

### 10. What exact future source/test/package manifest is smallest and
complete?

All paths below are `DOC_ONLY_NEW` proposed future paths, not created by
this audit. **Revised** to add the concrete receipt store, its test, and
the disclosed `agent-execution-runtime.ts` modification (items 1, 4, and 6
below are new or changed from the prior submission).

| # | Path | Action | Purpose |
|---|---|---|---|
| 1 | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | **modify** | add the two additive optional `requestId` parameters from question 1; no other behavior changes |
| 2 | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.test.ts` | modify | add a focused case proving the injected `requestId` flows through unchanged when supplied, and that omitting it preserves the current self-generation behavior (regression guard for item 1) |
| 3 | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime-owner.ts` | create | owner factory, receipt-port interface, and receipt-record schema from questions 2 and 5 |
| 4 | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime-owner.test.ts` | create | deterministic proof suite from question 11 |
| 5 | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/json-agent-execution-receipt-store.ts` | create | concrete file-backed `AgentExecutionReceiptPort` implementation from question 5 |
| 6 | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/json-agent-execution-receipt-store.test.ts` | create | deterministic proof suite for the concrete adapter (exclusive-create rejection of duplicate `requestId`, fsync-before-return, `finalize`-without-`admit` rejection, `finalize`-after-`finalize` rejection) |
| 7 | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | modify | add the export block from question 9 |
| 8 | `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` | modify | add the three `exports` entries and three `files` entries from question 9 |

This eight-item manifest is the smallest set that satisfies every
requirement in questions 1-9 **and** provides a concrete, testable durable
store, not only a port interface, resolving reviewer blocker #3. It grew
from the prior four-item manifest specifically to close the three source
gaps the reviewer identified (real requestId injection, a concrete
adapter, and that adapter's own test coverage); no item was added for any
reason outside those blockers.

### 11. What deterministic tests prove one guard evaluation, ALLOW provider
once, BLOCK/approval provider zero, durable writes, correlation, and
failures?

All test names below are `DOC_ONLY_NEW` proposed cases. **Revised** to add
admission-ordering and concrete-adapter cases (new rows marked below).

For `agent-execution-runtime.test.ts` (item 2 in the manifest):

| Proposed test case | Required assertion |
|---|---|
| `preCheck uses the supplied requestId when provided` (NEW) | calling `preCheck(intent, skill, 'fixed-id-123')` results in `guardResult.requestId === 'fixed-id-123'`, not a generated value |
| `preCheck still self-generates a requestId when omitted` (NEW) | calling `preCheck(intent, skill)` with no third argument produces a `guardResult.requestId` matching the existing generator's shape, proving the additive parameter did not remove the default behavior |

For `agent-execution-runtime-owner.test.ts` (item 4 in the manifest):

| Proposed test case | Required assertion |
|---|---|
| `owner requires a caller-supplied engine at construction` (NEW) | passing `config` without `engine` is a TypeScript compile-time error (required field), and at runtime a fake owner-config object missing `engine` throws a defined construction error, proving no implicit `createGuardEngine()` fallback exists inside the owner module |
| `owner generates one requestId and admits it before any guard evaluation` (NEW) | a spy `receiptPort.admit` records a call with a `requestId` string; a spy `GuardRuntimeEngine.evaluate` is asserted to have zero calls at the moment `admit` resolves, then exactly one call after, proving strict before/after ordering |
| `owner rejects construction when controlMode is standard` | constructor throws synchronously; no `ExecutionProvider.execute` call occurs |
| `owner proves exactly one guard evaluation per run` | a spy `GuardRuntimeEngine.evaluate` is called exactly once for an ALLOW request, exactly once for a BLOCK request, and exactly once for a governed-ESCALATE request |
| `owner proves ALLOW reaches provider exactly once` | a mock `ExecutionProvider.execute` is called exactly once; `receiptPort.finalize` receives `outcome: 'ALLOW_COMPLETED'` and `providerCallCount: 1` |
| `owner proves BLOCK reaches provider zero times` | mock `ExecutionProvider.execute` is called zero times; `receiptPort.finalize` receives `outcome: 'BLOCKED'` and `providerCallCount: 0` |
| `owner proves governed ESCALATE reaches provider zero times` | mock `ExecutionProvider.execute` is called zero times; `receiptPort.finalize` receives `outcome: 'NEEDS_APPROVAL'` and `providerCallCount: 0` |
| `owner proves provider failure is durably recorded` | mock `ExecutionProvider.execute` rejects; `receiptPort.finalize` receives `outcome: 'ALLOW_FAILED'` and a populated `errorMessage`; no unhandled rejection escapes the owner's `run()` |
| `owner proves post-check invalidity is recorded without changing status` | a fixture producing a missing-`requestId` post-check issue still returns the original `ExecutionResult.status` to the caller, while `receiptPort.finalize` receives `postCheckValid: false` |
| `owner proves a thrown guard-engine error is durably recorded against the pre-admitted requestId` (REVISED) | a spy `GuardRuntimeEngine.evaluate` that throws synchronously results in `receiptPort.finalize` being called with `outcome: 'GUARD_THROW'` and the same `requestId` that `receiptPort.admit` already recorded before the throw, with no fallback or mismatched id |
| `owner fails closed when admit rejects` (NEW) | a mock `receiptPort.admit` that rejects causes the owner's `run()` to reject with that error; `GuardRuntimeEngine.evaluate` and `ExecutionProvider.execute` are both asserted to have zero calls |
| `owner surfaces a finalize failure instead of swallowing it` (NEW) | a mock `receiptPort.finalize` that rejects after a successful ALLOW causes the owner's `run()` to reject, proving the caller is not told a request completed durably when the final write failed |
| `owner correlates every receipt record to the owner-generated requestId` | for each of the above cases, the `requestId` passed to `receiptPort.admit`/`finalize` equals the value the owner itself generated, and that value equals `guardResult.requestId` inside the returned `ExecutionResult`, proving true correlation rather than incidental matching |
| `owner never embeds or logs the ExecutionProvider's constructor arguments` | receipt records and any owner-level logging never contain the provider's API key or other constructor fields |

For `json-agent-execution-receipt-store.test.ts` (item 6 in the manifest,
all NEW):

| Proposed test case | Required assertion |
|---|---|
| `admit rejects a duplicate requestId` | calling `admit` twice with the same `requestId` causes the second call to reject with an `EEXIST`-derived error, proving the exclusive-create guard works |
| `admit writes durably before resolving` | after `admit` resolves, reading the receipt file directly from disk (bypassing the store) shows the `ADMITTED` record, proving the write is not buffered only in memory |
| `finalize rejects a requestId that was never admitted` | calling `finalize` on a `requestId` with no prior `admit` call rejects with an `ENOENT`-derived error |
| `finalize rejects a requestId that was already finalized` | calling `finalize` twice on the same `requestId` causes the second call to reject, because the stored record's `outcome` is no longer `'ADMITTED'` |
| `finalize writes durably before resolving` | after `finalize` resolves, reading the receipt file directly from disk shows the merged final record, not the original `ADMITTED` record |

All cases across the three test files use fake/mock `GuardRuntimeEngine`
and `ExecutionProvider` instances; the `json-agent-execution-receipt-store.test.ts`
cases are the only ones in this manifest that touch a real (temporary,
test-scoped) filesystem path, and even those require no live provider,
network call, or CLI/MCP process.

### 12. What is the rollback boundary and which evidence becomes stale?

**Revised** to reflect the now-eight-item manifest and the disclosed
`agent-execution-runtime.ts` edit.

Because no implementation exists yet, there is nothing to roll back today.
For a future implementation following this design: the rollback boundary
is the eight-item manifest from question 10. Seven items are newly created
files with no prior data to migrate. The one modified existing file
(`agent-execution-runtime.ts`, manifest item 1) is a strictly additive,
backward-compatible change (two new optional trailing parameters with
defaults that preserve current behavior); reverting it restores the exact
current three-argument-maximum signature verified by this audit's source
reads, with no call-site breakage, because no current call site (all six
constructor-search matches plus the runtime's own internal calls) passes a
third argument to `preCheck` or `run` today.

Stale-evidence handling (DOC_ONLY_NEW, addresses question 5's ordering
contract): if a future implementation is rolled back after some receipt
files already exist under `agent-execution-receipts/` on disk, those files
become orphaned historical evidence, not migrated data; they are not read
by any other current CVF surface, so their presence after rollback is
inert. A record left permanently in the `ADMITTED` outcome (never reaching
`finalize`) is itself the concrete signal of an incomplete request from
question 5's rule 5; any future implementation packet's own operational
runbook, not this design, decides whether to retain or prune such orphaned
records.

### 13. Does the complete design avoid the GC-009 Web route and MCP-local
engine?

Yes, on both counts, source-verified as unchanged from the T0 audit's
rejection evidence and re-verified against the revised design:

- GC-009 Web route: the proposed owner and receipt-store modules live
  entirely inside `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/`; nothing in
  this revised design touches, imports from, or is imported by
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
  or `route-guard-gateway.ts`. The minimal `agent-execution-runtime.ts`
  edit (question 1) is also confined to `CVF_GUARD_CONTRACT`; it does not
  touch cvf-web.
- MCP-local engine: the revised canonical-engine design (question 3) now
  requires the future caller to supply an already-constructed
  `GuardRuntimeEngine`, sourced from `cvf-guard-contract`'s own
  `createGuardEngine()`. Nothing in this design references or constructs
  `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/engine.ts`. The concrete
  receipt store (question 5) is modeled on, but does not import from or
  depend on, `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts`;
  it is a new, package-local file.

### 14. Which terminal design-readiness token is supported?

`DESIGN_SPEC_READY_FOR_FRESH_GC010_IMPLEMENTATION_PACKET`, conditioned
explicitly on the Production-Caller Boundary declared immediately below,
which this revision treats as a required, load-bearing part of the
readiness claim rather than an afterthought.

Every item in the T0 completion review's nine-point Successor Boundary,
plus all six reviewer blockers from this revision round, is now addressed
with an exact, source-bounded, doc-only-new proposal: a real requestId
injection seam with a disclosed minimal runtime edit (blocker #1); a
strict admit-before-evaluate, fail-closed ordering contract (blocker #2);
a concrete file-backed receipt adapter with its own test plan, not only an
interface (blocker #3); a non-circular engine-dependency direction with a
required caller-supplied engine (blocker #4); removal of the dead reset API
(blocker #5); and the explicit Production-Caller Boundary below (blocker
#6). This token releases only the authoring of a fresh implementation work
order; it does not release implementation itself, and per the boundary
below, it does not release a claim that implementing this manifest closes
the GC-010 paired-gap entry.

## Production-Caller Boundary

**This section directly resolves reviewer blocker #6 and is a required
reading for evaluating the terminal token above.**

The eight-item manifest in question 10 builds a **library foundation**: a
factory (`createAgentExecutionRuntimeOwner`), a receipt-port contract, and
one concrete durable adapter (`JsonAgentExecutionReceiptStore`), all
package-internal to `CVF_GUARD_CONTRACT`. None of these eight items is, or
claims to be, a **non-test production caller**. A "production caller" in
this repository's own accepted vocabulary (per the T0 audit's candidate
comparison and the paired gap entry's `closeCondition`) means a real,
non-test, already-invoked CVF execution channel that constructs and calls
the owner with a real user or agent request; examples of what such a
caller could be, none of which this design creates or names as accepted:
a new CLI command, a new MCP tool, or a new Web route or Web action.

This design deliberately does **not** select or design that caller,
because doing so is out of the scope this work order authorized (which is
interface/export/receipt design, not caller selection) and because
selecting one without the same level of source verification given to the
owner/receipt questions would repeat the exact mistake the reviewer is
correcting here: asserting a contract is "ready" while a load-bearing piece
remains unverified.

**Explicit disposition:** implementing the eight-item manifest, even with
every deterministic test in question 11 passing, produces a
**tested-but-uninvoked library**, structurally identical in kind to the
current state of `AgentExecutionRuntime` itself (implemented and
unit-tested, zero non-test callers) that the T0 audit and the paired gap
entry both already document as insufficient for GC-010 closure. Completing
this manifest does **not** close
`cvf.asc.gap.gc009_gc010_no_production_caller.v1`, does not change its
`currentStatus` from `IMPLEMENTED_NOT_INVOCATION_PROVEN`, and does not
satisfy its `closeCondition`, which requires "bounded invocation evidence"
for `AgentExecutionRuntime`, not merely an owner wrapper around it.

A future implementation packet built from this design must choose one of
two explicit framings before it may claim any progress toward GC-010
closure:

1. **Bounded-foundation framing (recommended default):** the
   implementation packet explicitly states it delivers only the
   library-foundation manifest from question 10, with all eleven-plus-nine
   tests in question 11 passing, and explicitly does **not** claim GC-010
   closure or invocation proof; a separate, later, source-verified packet
   must still identify the exact non-test caller and produce deterministic
   invocation proof through it, mirroring the GC-009 roadmap's own T1
   (composition) / T2 (invocation proof) split.
2. **Caller-inclusive framing:** the implementation packet additionally
   names one exact non-test caller module (for example a new
   `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/` command, source-verified
   against that package's existing launcher patterns) and includes it, plus
   a deterministic invocation-proof test exercising that real caller
   end-to-end, in the same manifest; only this framing may cite GC-010
   invocation progress.

This audit does not select between the two framings; that choice belongs
to the future implementation packet's own dispatcher and reviewer, informed
by how much value-per-risk the operator wants in a single tranche. This
audit's own terminal token, `DESIGN_SPEC_READY_FOR_FRESH_GC010_IMPLEMENTATION_PACKET`,
certifies only that the contract itself (owner, engine, provider, receipt,
export, tests, rollback) is ready to be built under either framing; it does
not certify, and this audit explicitly rejects, any reading that the
foundation manifest alone satisfies the production-caller gap.

## Terminal Design-Readiness Enum Reference

The work order's four-token Terminal Design-Readiness Enum
(`DESIGN_SPEC_READY_FOR_FRESH_GC010_IMPLEMENTATION_PACKET`;
`PARTIAL_DESIGN_REQUIRES_FURTHER_SOURCE_DECISION`;
`NOT_READY_DESIGN_CONTRADICTION`; `NO_CURRENT_VALUE_WITH_REOPEN_CONDITION`)
selection is recorded in decision question 14 above. This audit selects
`DESIGN_SPEC_READY_FOR_FRESH_GC010_IMPLEMENTATION_PACKET`, conditioned on
the Production-Caller Boundary section immediately above being read as part
of that token, not as a separate optional note.

## Risk / Corrective Action

**Revised** to reflect the six repaired blockers; two risks from the prior
submission are marked RESOLVED with a pointer to the fix, and new residual
risks introduced by the revision itself are added.

| Residual risk | Corrective action |
|---|---|
| RESOLVED (prior blocker #1): the prior submission's `GUARD_THROW` case relied on "a fallback requestId" with no proof it matched the real one | this revision's Admission row (question 6) and additive `preCheck`/`run` seam (question 1) make the owner generate and durably admit `requestId` before any guard call, so no fallback id is ever needed |
| RESOLVED (prior blocker #3): the prior submission specified only a port interface and explicitly deferred a concrete store | this revision specifies `JsonAgentExecutionReceiptStore` concretely, with its own file, schema, and five-case test plan (question 5, question 11) |
| The disclosed `agent-execution-runtime.ts` edit (manifest item 1), though additive and backward-compatible, is still a change to already-shipped source that a future implementer could get wrong (for example by making the new parameter required instead of optional, breaking existing callers) | question 1 and question 11's two new `agent-execution-runtime.test.ts` cases explicitly require proving both the injected-value path and the omitted-parameter default-behavior path before this edit may be considered complete |
| The concrete `JsonAgentExecutionReceiptStore` writes to a local filesystem path with no specified retention, rotation, or size-bound policy | out of scope for this design; a future implementation packet's own operational review must decide retention before any production caller is authorized to write through it at volume |
| Constructor-time rejection of `standard` control mode (question 7) is a new safety constraint not present in `AgentExecutionRuntime` itself; a future implementer could bypass it by constructing `AgentExecutionRuntime` directly instead of through the proposed owner | the export manifest (question 9) exports both the raw `AgentExecutionRuntime` class and the owner; a future implementation packet must decide whether to also restrict or discourage direct construction |
| A future implementation packet could complete the eight-item manifest and informally treat it as GC-010 "done" without picking either framing in the Production-Caller Boundary section | that section's explicit disposition and two named framings exist specifically to make this misreading require an active, documented choice rather than a silent default |
| The twenty-plus proposed deterministic tests across three files (question 11) are a proof plan only; none are authored by this audit | a future implementation packet must author and pass every case, plus any additional cases its own review requires |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T0 releases design only | VALUE_SET | `docs/reviews/CVF_GC010_AGENT_EXECUTION_RUNTIME_T0_OWNER_PROVIDER_RECEIPT_DECISION_COMPLETION_2026-07-26.md` | Findings / Position | `PARTIAL_READY_REQUIRES_EXPORT_OR_RECEIPT_DESIGN` | completion review | ACCEPT |
| T0 Successor Boundary names nine required design items | VALUE_SET | `docs/reviews/CVF_GC010_AGENT_EXECUTION_RUNTIME_T0_OWNER_PROVIDER_RECEIPT_DECISION_COMPLETION_2026-07-26.md` | Successor Boundary, items 1-9 | `Successor Boundary` | completion review | ACCEPT |
| Runtime pipeline exists and constructor accepts engine/provider/config | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | class line 130; constructor lines 136-144 | `AgentExecutionRuntime` | agent runtime | ACCEPT |
| `preCheck` self-generates `requestId` immediately before `evaluate`, with no current injection parameter | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | signature line 170; generation line 193; evaluate call line 208 | `preCheck` | agent runtime | ACCEPT |
| `run()` calls `preCheck` once then `execute` once | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | lines 358-372 | `run` | agent runtime | ACCEPT |
| BLOCK branch returns before provider call | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | lines 224-243 | `execute` | agent runtime | ACCEPT |
| Governed-mode ESCALATE branch returns before provider call | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | lines 246-281 | `execute` | agent runtime | ACCEPT |
| Standard-mode ESCALATE falls through to provider call | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | line 246 condition, line 283 fallthrough | `execute` | agent runtime | ACCEPT |
| Provider try/catch records COMPLETED/FAILED | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | lines 283-326 | `execute` | agent runtime | ACCEPT |
| `postCheck` result is computed but not branched on by `run` | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | lines 332-352 (`postCheck`); line 369 (return unused) | `postCheck`; `run` | agent runtime | ACCEPT |
| `executionLog` is in-memory only | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | field line 134; getter lines 376-378 | `executionLog` | agent runtime | ACCEPT |
| Existing test uses `createGuardEngine()` from package index | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.test.ts` | line 20 import; line 44 usage | `createGuardEngine` | test helper | ACCEPT |
| Barrel imports every guard class directly from its own leaf module, never back from itself | LITERAL_INVARIANT | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | import block lines 107-116; `GuardRuntimeEngine` re-export line 16 | `createGuardEngine`; import statements | guard-contract barrel | ACCEPT |
| `GuardRuntimeEngine` is defined in a sibling non-barrel module | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` | class export | `GuardRuntimeEngine` | guard-contract engine module | ACCEPT |
| Provider adapters require explicit constructor API key, no secret embedding | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/providers/gemini-provider.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/providers/alibaba-dashscope-provider.ts` | class declarations, lines 29 and 48 respectively | `GeminiProvider`; `AlibabaDashScopeProvider` | provider adapters | ACCEPT |
| JSON governed execution store is two-phase, exclusive-create, fsync durable, with a dedicated receipt directory | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts` | directory constant line 6; `beginExecution` lines 73-101; `finalizeExecution` lines 103-131 | `JsonGovernedExecutionStore`; `GOVERNED_EXECUTION_DIR` | launcher persistence | ACCEPT |
| Package exports omit the runtime and its providers | LITERAL_INVARIANT | `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` | `exports` lines 8-17; `files` lines 18-29 | `exports`; `files` | guard-contract package | ACCEPT |
| Barrel exports mandatory-gateway but omits the runtime | LITERAL_INVARIANT | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | mandatory-gateway export lines 26-32; full 138-line file has no `agent-execution-runtime` reference | `createGuardEngine`; export block | guard-contract barrel | ACCEPT |
| MCP guard engine is a separate, non-canonical implementation | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/engine.ts` | class declaration | `GuardRuntimeEngine` | MCP local guard engine | ACCEPT |
| Paired gap `actionOwner` requires exactly this design decision before implementation dispatch | VALUE_SET | `docs/reference/system_chain/gaps/entries/gc009_gc010_no_production_caller.json` | `actionOwner` field | `actionOwner` | gap entry | ACCEPT |
| Paired gap `closeCondition` requires bounded invocation evidence, not only an owner/wrapper | VALUE_SET | `docs/reference/system_chain/gaps/entries/gc009_gc010_no_production_caller.json` | `closeCondition.conditionText` | `closeCondition` | gap entry | ACCEPT |

## New Doc-Only Fields

| Item | Meaning | Runtime/source status |
|---|---|---|
| `GC010-AER-T1` | governed batch identifier | DOC_ONLY_NEW |
| `ownerModulePath` | proposed future owner file path | DOC_ONLY_NEW |
| optional `requestId` parameter on `preCheck`/`run` | proposed additive, backward-compatible runtime edit | DOC_ONLY_NEW |
| `AgentExecutionRuntimeOwnerConfig`; `createAgentExecutionRuntimeOwner`; `AgentExecutionRuntimeOwner` | proposed owner factory/type signatures | DOC_ONLY_NEW |
| `AgentExecutionReceiptOutcome`; `AgentExecutionReceiptRecord`; `AgentExecutionReceiptPort` | proposed receipt-port schema and interface | DOC_ONLY_NEW |
| `JsonAgentExecutionReceiptStore`; `AGENT_EXECUTION_RECEIPT_DIR`; `REQUEST_ID_PATTERN` | proposed concrete durable adapter | DOC_ONLY_NEW |
| proposed `src/index.ts` and `package.json` export/files additions | exact future package surface | DOC_ONLY_NEW |
| twenty-plus proposed deterministic test case names across three files | future proof plan | DOC_ONLY_NEW |
| Production-Caller Boundary's two named framings (bounded-foundation, caller-inclusive) | future packet scoping options | DOC_ONLY_NEW |
| `DESIGN_SPEC_READY_FOR_FRESH_GC010_IMPLEMENTATION_PACKET` | selected terminal design-readiness token | DOC_ONLY_NEW |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_equivalence_claim_evidence.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | review structural heading families (target/source, scope/methodology, findings/position, risk/corrective action, decision/recommendation/disposition); Delta block Field/Disposition table shape; Machine Closure Package required column set; External Knowledge Intake Routing seven row labels and canonical Input type phrase; Finding-To-Governance defect-class and learning-lane enum tokens; equivalence-claim trigger words (identical, unchanged, verbatim, same as) paired with adjacent evidence commands or disposition tokens; ASCII prose discipline |
| gateRunPurpose | confirm required output shape and repaired literal-format traps before rerunning gates, using the first submission's equivalence-claim violation as direct precedent for this revision's phrasing discipline |
| claimBoundary | checker compliance evidence only; no owner, provider, receipt, export, or implementation readiness claim is proven by gate passage |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Claude documentation worker |
| Provider or surface | Claude, invoked by operator using the canonical committed work order |
| Session or invocation | GC010-AER-T1 in-place repair round, 2026-07-26 |
| Working directory | repository root |
| Command or tool surface | read-only source and git inspection, `rg` negative searches, governance gate scripts, in-place patch editing of the two already-existing worker-owned documentation files |
| Target paths | `docs/audits/CVF_GC010_AGENT_EXECUTION_RUNTIME_T1_INTERFACE_EXPORT_RECEIPT_DESIGN_2026-07-26.md`; `docs/reviews/CVF_GC010_AGENT_EXECUTION_RUNTIME_T1_INTERFACE_EXPORT_RECEIPT_DESIGN_WORKER_RETURN_2026-07-26.md` |
| Allowed scope source | committed dispatch-ready work order at base `0b55e74d8`; explicit reviewer repair instruction naming six blockers |
| Before status evidence | HEAD `94f0934bb` unchanged from the prior submission; both worker output paths present and untracked, containing the rejected first-draft content |
| After status evidence | exactly the same two worker-owned paths, in-place rewritten, still unstaged |
| Diff evidence | `git status --short`; `git diff --name-status`; `git diff --cached --name-status`; `git diff --check` |
| Approval boundary | documentation-only T1 interface/export/receipt design repair |
| Claim boundary | no implementation, export, construction, provider call, receipt creation, or GC-010 closure |
| Agent type | documentation worker |
| Invocation ID | `gc010-aer-t1-claude-repair-2026-07-26` |
| Expected manifest | audit and worker return (unchanged paths from the first submission) |
| Actual changed set | matches expected manifest |
| Manifest delta | none |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred; both paths are rewritten in place |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | documentation-only GC-010 interface/export/receipt design, revised to repair six reviewer-identified blockers |
| claimDisposition | `CLAIM_REJECTED`: no runtime control is implemented or claimed |
| receiptEvidence | `CLAIM_REJECTED_NO_RECEIPT`: no receipt is created or consumed by this audit; the receipt port and its concrete adapter are proposed design only |
| actionEvidence | `CLAIM_REJECTED_NO_ACTION`: no runtime, provider, or process action occurs |
| invocationBoundary | local read-only source and git inspection only |
| interceptionBoundary | no provider, CLI, MCP, Web, or process interception |
| claimLanguage | design recommendation pending Codex independent review |
| forbiddenExpansion | no source/test/package/export/live/public behavior; no construction or GC-010 closure claim; the Production-Caller Boundary section explicitly forbids reading the foundation manifest as production-caller evidence |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance design packet only; no public-sync authorization
exists for this artifact.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external artifact was consumed as an evidence source; this audit synthesizes only repository-local source, accepted predecessor decisions, and the reviewer's own repair instructions |
| Matching local-view guard | N/A with reason: no external artifact was consumed as an evidence source |
| Owner surface | this audit |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | repo-governed source and accepted predecessor evidence only |

## Machine Closure Package

This audit is `COMPLETE_PENDING_REVIEW`, not closed. Every row below is
`N/A with reason` or `BLOCKED with reason` pending reviewer/closer action
after material commit; no row asserts closure.

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_AGENT_EXECUTION_RUNTIME_T1_INTERFACE_EXPORT_RECEIPT_DESIGN_2026-07-26.md` | work order remains `REVIEWER_ACCEPTED_DISPATCH_READY`; this audit does not change its status | PASS: worker did not mutate work-order status; reviewer owns closure status |
| Completion or reviewer artifact | `docs/reviews/CVF_GC010_AGENT_EXECUTION_RUNTIME_T1_INTERFACE_EXPORT_RECEIPT_DESIGN_COMPLETION_2026-07-26.md` | not yet created | BLOCKED with reason: reviewer creates the completion review after independent acceptance; worker is forbidden from creating this path |
| Roadmap state | `docs/roadmaps/CVF_GC009_GC010_PRODUCTION_CALLER_AND_BOUNDED_E2E_RUNTIME_ROADMAP_2026-07-25.md` | roadmap unedited by this worker; this audit's terminal token is `DESIGN_SPEC_READY_FOR_FRESH_GC010_IMPLEMENTATION_PACKET` | PASS: roadmap correctly left unedited; reviewer owns the actual roadmap-state update |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | this tranche performed no corpus scan and read no legacy/external corpus folder | PASS: no registry update required because no corpus-scan-registry-governed action occurred |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | this tranche performed no corpus scan and read no legacy/external corpus folder | PASS: no registry update required because no corpus-scan-registry-governed action occurred |
| External evidence digest | N/A | no external artifact was consumed as evidence | BLOCKED with reason: not applicable; no external evidence source exists for this tranche |
| System loop interlock | `docs/reference/system_chain/gaps/entries/gc009_gc010_no_production_caller.json` | gap entry unedited by this worker | BLOCKED with reason: reviewer decides whether this audit's evidence changes the gap entry's `actionOwner`/`lastReviewed` fields |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION_MEMORY.md` | unedited by this worker | BLOCKED with reason: reviewer owns session continuity updates after closure decision |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Both worker-owned paths rewritten in place, no other path changed | exactly two documentation paths | `git status --short` shows exactly two `??` entries for the two worker-owned paths; `git diff --name-status` shows no tracked-file modification | PASS |
| No commit or staging occurred | HEAD unchanged, nothing staged | `git rev-parse --short HEAD` unchanged at `94f0934bb`; `git diff --cached --name-status` empty | PASS |
| Negative searches reproduced with matching results | zero non-test constructors, zero exports | `rg` for `new AgentExecutionRuntime` returns 6 test-only matches; `rg` for the runtime name in `src/index.ts`/`package.json` returns zero matches | PASS |
| All fourteen decision questions answered, with six blockers repaired | fourteen numbered answers, each blocker traceable to a specific question | all fourteen present in `## Required Design Questions`; each blocker cross-referenced by number | PASS |
| Every proposed symbol/path/schema classified DOC_ONLY_NEW | no proposed item claimed as existing source | `## New Doc-Only Fields` table plus inline `DOC_ONLY_NEW` labels throughout | PASS |
| Production-Caller Boundary present and load-bearing on the terminal token | dedicated section distinguishing foundation from caller | `## Production-Caller Boundary` section, cross-referenced from question 14 | PASS |
| Exactly one terminal design-readiness token selected | one token from the fixed four-token enum | `DESIGN_SPEC_READY_FOR_FRESH_GC010_IMPLEMENTATION_PACKET` recorded once in question 14, conditioned on the boundary section | PASS |

## Epistemic Process Block

### Expected Result / Prediction

A reviewer-driven repair round would find that the six named blockers are
each traceable to a specific current-source gap (no requestId seam, no
ordering contract, no concrete adapter, a barrel-direction dependency, an
unused reset function, and an unstated caller/foundation boundary), and
that each is repairable within the same documentation-only scope by adding
precision, not by inventing new existing-source facts.

### Evidence Comparison

The prediction is confirmed for all six blockers. Re-reading `preCheck`
confirmed the exact line (193) where `requestId` is self-generated,
supporting a minimal additive parameter rather than a larger rewrite.
Re-reading `src/index.ts`'s existing import pattern (every export sources
from a sibling leaf module, never from itself) confirmed the
non-circular-import fix direction without requiring invention. Re-reading
`JsonGovernedExecutionStore` a second time, focused on its exact
`'wx'`-flag and `sync()` calls, supported specifying a concrete sibling
adapter rather than continuing to defer it.

### Contradiction Or Gap Disposition

No contradiction was found between the reviewer's six blockers and current
source; each blocker was a real gap in the *design*, not a misreading of
source, and each is now closed by an explicit design decision or a
disclosed minimal source edit, both classified `DOC_ONLY_NEW`. The one
place this revision changes its own prior claim (that the design "does not
modify `AgentExecutionRuntime` itself") is disclosed explicitly in the
Findings / Position section and question 1, not silently dropped.

### Claim Update

This audit may recommend only a design specification and one readiness
token, conditioned on the Production-Caller Boundary, for a future
implementation packet. It does not implement, export, construct, invoke, or
close GC-010, and its recommendation, including the repaired six blockers,
is subject to Codex independent review before any implementation work order
may be authored.

## Claim Boundary

This audit defines a complete, revised future contract for
`AgentExecutionRuntime`'s owner, canonical engine, provider ownership,
durable receipt port and its one concrete adapter, terminal write points
with a fail-closed admission ordering, export manifest, deterministic proof
plan, rollback boundary, and an explicit foundation-versus-production-caller
boundary, and selects one terminal design-readiness token conditioned on
that boundary. Every proposed symbol, path, and schema is explicitly
classified `DOC_ONLY_NEW`. This audit does not authorize exports,
construction, provider execution, tests, receipt implementation, GC-010
closure, public-sync, push, deployment, or production readiness, and it
explicitly does not claim that implementing its own manifest alone closes
the GC-010 paired-gap entry. All findings are pending Codex independent
review, which may accept, repair, or reject this recommendation.
