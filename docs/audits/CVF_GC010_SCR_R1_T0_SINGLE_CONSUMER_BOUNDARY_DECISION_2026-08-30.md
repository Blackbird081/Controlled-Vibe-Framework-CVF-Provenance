# CVF GC-010 SCR-R1-T0 Single-Consumer Boundary Decision Architecture Audit

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

docType: audit

Date: 2026-08-30

Batch ID: GC010-SCR-R1-T0

executionBaseHead: `d7d23b817`

Worker: delegated documentation worker

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R1_T0_SINGLE_CONSUMER_BOUNDARY_DECISION_2026-08-30.md`

Paired baseline: `docs/baselines/CVF_GC018_GC010_SCR_R1_T0_SINGLE_CONSUMER_BOUNDARY_DECISION_2026-08-30.md`

## Purpose

Recompute current GC-010 source facts from the worker's own execution base,
compare all five candidate consumer families named by the roadmap and work
order, answer all sixteen required decision questions, and select exactly one
terminal token. This audit proves only a current-source architecture
decision; it does not implement, invoke, export, or construct
`AgentExecutionRuntime`, and it does not close GC-010 or the paired
gc009-gc010 gap.

## Target / Source

| Surface | Path |
| --- | --- |
| Roadmap | `docs/roadmaps/CVF_GC010_SINGLE_CONSUMER_SYSTEM_CHAIN_PRODUCT_ROADMAP_2026-08-30.md` |
| Baseline | `docs/baselines/CVF_GC018_GC010_SCR_R1_T0_SINGLE_CONSUMER_BOUNDARY_DECISION_2026-08-30.md` |
| Work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_GC010_SCR_R1_T0_SINGLE_CONSUMER_BOUNDARY_DECISION_2026-08-30.md` |
| Historical GC010-AER-T2 completion | `docs/reviews/CVF_GC010_AGENT_EXECUTION_RUNTIME_T2_NON_TEST_CALLER_OWNERSHIP_INVOCATION_BOUNDARY_DECISION_COMPLETION_2026-07-26.md` |
| AER runtime | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` |
| Approval bridge | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/approval-execution-bridge.ts` |
| Package barrel/manifest | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts`; `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` |
| GC-009 Web route | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` |
| Web gateway helper | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-guard-gateway.ts` |
| Web provider-attempt admission | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/provider-attempt-admission.ts` |
| Web mandatory-gateway singleton | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mandatory-gateway-singleton.ts` |
| Execution Plane command runtime | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/command.runtime.contract.ts` |
| MAO operational worker launcher | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/operational.worker.launcher.ts` |
| MCP governed-command-launcher | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` |
| MCP governed-exec CLI entry | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts` |
| Manually runnable pilot script | `scripts/run-brigade-residual-absorption-runtime-pilot.ts` |
| Root package manifest | `package.json` |

## Scope / Methodology

The worker read the roadmap, paired GC-018 baseline, work order, active
session front door, active handoff, guard orientation index, literal-format
gotchas checklist, and the historical GC010-AER-T2 completion review before
recomputing source. The worker then re-ran the four Current Runtime Freshness
Verification searches named by the work order from its own captured
`executionBaseHead`, added three additional targeted searches (non-test `new
AgentExecutionRuntime` construction across the whole repository excluding
`node_modules`/`dist`/`coverage`; the CLI/MCP/Execution-Plane symbol search;
and a root `package.json` scripts-block/CI-workflow search for the one
newly discovered non-test construction site), read the full text of every
file a search returned a non-test hit for, and read the applicable
`governance/compat/check_*.py` checker sources before drafting. All source
citations below are re-derived from the worker's own execution base, not
copied from the historical T2 completion or the paired baseline's Source
Verification Block.

## Current Runtime Freshness Verification (Reproduced Commands And Results)

```text
rg -n "AgentExecutionRuntime|createAgentExecutionRuntime" . --glob '!**/*.test.*' --glob '!**/__tests__/**'
```
Result: matches only inside `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` (class declaration, line 148 at this execution base), governed documentation prose (roadmap/baselines/work-orders/reviews/audits/session-state entries citing the historical decision chain), two provider-source JSDoc comment lines (`gemini-provider.ts:5`, `alibaba-dashscope-provider.ts:5`, comment-only mentions of the interface name), and the active handoff line summarizing this same dispatch. No production, non-test, non-documentation import or construction site.

```text
rg -n "ApprovalExecutionBridge|createApprovalExecutionBridge" EXTENSIONS/CVF_GUARD_CONTRACT --glob '!**/*.test.*'
```
Result: `src/index.ts:363-365,367-372` (named export plus type exports); `src/runtime/agent-execution-runtime.ts:24,124` (type import, optional `approvalBridge` constructor field); `src/runtime/approval-execution-bridge.ts:41,46,52,172-175` (interface, class, constructor, factory). `ApprovalExecutionBridge` is package-exported and consumed as an optional dependency by `AgentExecutionRuntime`; `AgentExecutionRuntime` itself is not exported anywhere in this result set.

```text
rg -n "runExecuteRouteMandatoryGateway|admitAndInvokeProvider" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src --glob '!**/*.test.*'
```
Result: `lib/route-guard-gateway.ts:111` (definition); `lib/provider-attempt-admission.ts:352` (definition); `app/api/execute/route.ts:11` (gateway import), `:35` (admission import), `:594` (gateway invocation call site), `:801` (initial admitted provider call), `:859` (retry admitted provider call). GC-009's route composes exactly one gateway call and admits both the initial and retry provider attempts through the same `admitAndInvokeProvider` helper.

```text
rg -n '"exports"|agent-execution-runtime|approval-execution-bridge' EXTENSIONS/CVF_GUARD_CONTRACT/package.json EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts
```
Result: `package.json:8` declares an `"exports"` map with a `"./runtime/approval-execution-bridge"` subpath (`package.json:17`) and lists the same file under `"files"` (`package.json:31`); `src/index.ts:365,372` re-export the approval bridge from the same relative path. Neither file contains `agent-execution-runtime` in any form. The package barrel and subpath-exports map expose `ApprovalExecutionBridge` but not `AgentExecutionRuntime`.

### Additional worker-added searches

```text
rg -n "new AgentExecutionRuntime" . --glob '!**/node_modules/**' --glob '!**/dist/**' --glob '!**/coverage/**' --glob '!**/.next/**'
```
Result: every non-documentation hit is inside a `*.test.ts` file (`agent-execution-runtime.test.ts:56`; `providers/gemini-provider.test.ts:49,66,107`; `providers/alibaba-dashscope-provider.test.ts:50,90`; `approval-execution-bridge.test.ts:65,88`), **except one**: `scripts/run-brigade-residual-absorption-runtime-pilot.ts:124` constructs `new AgentExecutionRuntime(guardEngine, provider, {...})` with a real `GuardRuntimeEngine`, a real `AlibabaDashScopeProvider`, and a real `ApprovalExecutionBridge`, and calls `runtime.runAwaitingApproval(...)` at line 138 with `liveExecution: true`. This is a genuinely new, non-test, non-documentation construction site that did not exist at the historical GC010-AER-T2 closure (`158fd17ae`, 2026-07-26). See the dedicated classification below.

```text
rg -n "launchGovernedCommand|CommandRuntimeContract|createMandatoryGateway|getMandatoryGateway|new AgentExecutionRuntime" EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src --glob "!**/*.test.*" --glob "!**/node_modules/**"
```
Result: `launchGovernedCommand` is defined and called only inside the MCP CLI tree (`governed-command-launcher.ts:311`; `governed-exec.ts:15,72`). `CommandRuntimeContract`/`createCommandRuntimeContract` are defined and consumed only inside the Execution Plane Foundation tree (`command.runtime.contract.ts`, `command.runtime.batch.contract.ts`, `command.runtime.consumer.pipeline.contract.ts`, `execution.pipeline.contract.ts`, `execution.async.runtime.contract.ts`, `execution.async.runtime.batch.contract.ts`, `epf.dispatch.barrel.ts`). `createMandatoryGateway`/`getMandatoryGateway` are consumed only by `mandatory-gateway-singleton.ts` in `cvf-web`. Zero matches for `new AgentExecutionRuntime` in any of the three searched trees.

```text
python -c "import json; print(json.dumps(json.load(open('package.json',encoding='utf-8')).get('scripts', {}), indent=2))"
rg -ln "run-brigade-residual-absorption-runtime-pilot" .github
```
Result: root `package.json` has an empty `"scripts"` object (`{}`)  -  no npm script registers the pilot file. The `.github` search returns zero matches  -  no CI workflow references or executes it. The only repository reference to the pilot script outside its own file is one prose mention inside `docs/reviews/CVF_BRIGADE_EARTR_LOCAL_RECONCILIATION_AND_ABSORPTION_CLOSURE_2026-08-29.md`'s Agent Operation Trace `Actual changed set` field, recording that the file was added as evidence-generation tooling during a prior absorption closure, not that it is wired to any trigger.

### Classification of the pilot-script construction site

`scripts/run-brigade-residual-absorption-runtime-pilot.ts` requires a live
`ALIBABA_API_KEY`/`CVF_BENCHMARK_ALIBABA_KEY`/`CVF_ALIBABA_API_KEY`
environment variable (asserted at line 33; the script throws and exits
non-zero without one), is not imported by any other source file (`rg -n
"run-brigade-residual-absorption-runtime-pilot" .` returns only the file
itself and the one documentation-prose mention above), is not listed in any
`package.json` `scripts` block at the root or under any extension package
package, is not referenced by any `.github` workflow, and has no HTTP route,
CLI subcommand registration, or MCP tool registration pointing at it. It can
only be executed by a human or agent manually invoking `tsx`/`ts-node`
against the file path from a shell, exactly the same "manually runnable
script" class the roadmap's Design Control Gate and the work order's Current
Runtime Freshness Verification instructions both name as not qualifying as a
production caller by itself ("Tests, fixtures, examples, docs, barrel
exports, factories, and manually runnable scripts are not production callers
by themselves"). It is evidence-generation tooling for a separate, already
closed absorption tranche (`CVF_BRIGADE_EARTR_LOCAL_RECONCILIATION_AND_
ABSORPTION_CLOSURE_2026-08-29.md`), not a registered production invocation
trigger. This construction site is treated as `NOT_A_PRODUCTION_CALLER` for
every candidate row below.

## Historical Four-Fact Reopen Condition Recomputed

| # | Fact | Current-source disposition |
| --- | --- | --- |
| 1 | direct import or construction of `AgentExecutionRuntime` | Present only in test files and in the one classified `NOT_A_PRODUCTION_CALLER` manual pilot script. No production import or construction exists. |
| 2 | a concrete registered production invocation trigger | Absent. No route, CLI subcommand, MCP tool, or scheduled job constructs or imports `AgentExecutionRuntime`. |
| 3 | real `GuardRuntimeEngine` and `ExecutionProvider` wiring on that invoked path | Not applicable; no invoked production path exists to wire. |
| 4 | a durable receipt or audit consumer on the invoked path | Not applicable; no invoked production path exists to consume. |

None of the four facts is satisfied together on a non-test, non-manual-script
production path. The historical reopen condition from GC010-AER-T2 remains
unsatisfied at this execution base.

## Candidate Comparison Contract (5/5)

### Candidate 1: package-native composition adapter consumed by `cvf-web`

| Field | Value |
| --- | --- |
| Classification | `NO_CURRENT_OWNER` |
| Trigger | none exists; would require a new adapter module |
| Caller symbol | none |
| AER construction/import | absent from `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` and `package.json` `exports`/`files` |
| Guard engine | cvf-web already owns a shared `GuardRuntimeEngine` singleton (`lib/mandatory-gateway-singleton.ts`) that is bound to `MandatoryGateway`, not to `AgentExecutionRuntime` |
| Provider adapter | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/providers/{gemini,alibaba-dashscope}-provider.ts` implement `ExecutionProvider` but have no non-test caller |
| Approval owner | `ApprovalExecutionBridge` is exported and could be consumed, but has no current adapter binding it into a cvf-web request path |
| Provider-attempt owner | cvf-web's existing `admitAndInvokeProvider` owns provider-attempt admission for the current GC-009 path; a new adapter would need to either reuse or duplicate this boundary |
| Durable receipt consumer | none exists on any AER path |
| Response mapping | none exists |
| Failure/rollback | N/A, nothing to roll back |
| Exactly-once risk | HIGH if built naively: a package-native adapter invoked from the same request that already calls `runExecuteRouteMandatoryGateway`/`admitAndInvokeProvider` risks a second independent guard evaluation and a second independent provider-attempt admission unless it explicitly reuses the existing Web-owned boundaries instead of re-implementing them |
| Smallest future write/test set | one new `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime-adapter.ts` (or similar) exporting a thin factory that composes the existing `GuardRuntimeEngine` and `ApprovalExecutionBridge` without a second admission boundary, plus a package `exports` entry and one focused unit test asserting no duplicate guard/admission call |

### Candidate 2: direct `cvf-web` caller

| Field | Value |
| --- | --- |
| Classification | `EXISTING_SOURCE_INCOMPATIBLE` |
| Trigger | `POST` handler in `app/api/execute/route.ts` (registered Next.js route, already a concrete production trigger) |
| Caller symbol | `POST` (`app/api/execute/route.ts`) |
| AER construction/import | route.ts has zero references to `AgentExecutionRuntime`, `ApprovalExecutionBridge`, `GuardRuntimeEngine`, or `ExecutionProvider` by name (confirmed by direct search of the route file) |
| Guard engine | route.ts's guard boundary is `runExecuteRouteMandatoryGateway` (line 594), which wraps `MandatoryGateway`/its own `GuardRuntimeEngine` singleton, a parallel, already-accepted GC-009 pipeline distinct from AER's own internal `preCheck`/`run` pipeline |
| Provider adapter | route.ts calls `admitAndInvokeProvider` directly (lines 801, 859) against its own provider abstraction, not against `ExecutionProvider`/AER |
| Approval owner | route.ts's approval handling is independent of `ApprovalExecutionBridge` |
| Provider-attempt owner | `admitAndInvokeProvider` already owns exactly-once attempt admission for both the initial and retry call sites in this route |
| Durable receipt consumer | route.ts's own reconciliation/receipt path, independent of AER |
| Response mapping | route.ts's own response builder |
| Failure/rollback | route.ts already has an accepted fail-closed path; introducing AER here would run two independent guard/admission pipelines in the same request |
| Exactly-once risk | CRITICAL: wrapping the already-accepted GC-009 pipeline with AER's own internal `preCheck`+`run` would double-evaluate guard decisions and double-admit provider attempts inside one logical execution, exactly the roadmap's named highest architectural risk |
| Smallest future write/test set | not applicable; this candidate is rejected as a direct-wrap target. A future T1 must not make `route.ts` construct `AgentExecutionRuntime` directly |

### Candidate 3: Execution Plane or MAO caller

| Field | Value |
| --- | --- |
| Classification | `NO_CURRENT_OWNER` |
| Trigger | `CommandRuntimeContract`/`AsyncCommandRuntimeContract` construction sites inside the Execution Plane Foundation source directory; MAO's `operational.worker.launcher.ts` |
| Caller symbol | `CommandRuntimeContract` (`command.runtime.contract.ts:72`), `createCommandRuntimeContract` (`:208`) |
| AER construction/import | zero matches for `AgentExecutionRuntime` or `ApprovalExecutionBridge` inside `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src` or `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao` |
| Guard engine | `CommandRuntimeContract` has its own dependency-injected command-execution model unrelated to `GuardRuntimeEngine` |
| Provider adapter | none; the Execution Plane Foundation contracts operate on `CommandRuntimeResult`, not `ExecutionProvider` |
| Approval owner | none present in this tree |
| Provider-attempt owner | none present in this tree |
| Durable receipt consumer | not verified as AER-shaped; out of scope to fully audit for this decision since no AER wiring exists at all |
| Response mapping | none |
| Failure/rollback | N/A |
| Exactly-once risk | UNKNOWN/LOW today because there is no wiring at all; a future integration would need its own fresh design, not a small composition |
| Smallest future write/test set | not proposed; this is a `NO_CURRENT_OWNER` family with no existing partial wiring to compose against, so any future manifest would be a new design, not this T0's smallest-manifest target |

### Candidate 4: governed CLI or MCP caller

| Field | Value |
| --- | --- |
| Classification | `EXISTING_SOURCE_INCOMPATIBLE` |
| Trigger | `governed-exec.ts` CLI entry (registered subcommand, calls `launchGovernedCommand`) |
| Caller symbol | `launchGovernedCommand` (`governed-command-launcher.ts:311`) |
| AER construction/import | `governed-command-launcher.ts` imports only `GuardRuntimeEngine` (type-only, line 6) from `cvf-guard-contract`; zero `AgentExecutionRuntime` reference anywhere in `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src` |
| Guard engine | the launcher receives an externally constructed `GuardRuntimeEngine` as a dependency; it does not own AER's `preCheck`/`run` pipeline |
| Provider adapter | the launcher's `run` dependency executes an arbitrary allow-listed subprocess command, not an `ExecutionProvider` |
| Approval owner | none tied to `ApprovalExecutionBridge` |
| Provider-attempt owner | none tied to AER's admission model; the launcher has its own fixed allow-listed command-execution boundary |
| Durable receipt consumer | the launcher's own evidence/log surface, independent of AER |
| Response mapping | CLI stdout/stderr/exit-code, independent of AER's `ExecutionResult` |
| Failure/rollback | the launcher already owns its own fail-closed allow-list boundary; forcing AER underneath it would require redesigning that boundary, not composing it |
| Exactly-once risk | HIGH if naively wrapped: the launcher's own guard evaluation and AER's internal `preCheck` would be two independent guard boundaries around one logical command execution |
| Smallest future write/test set | not proposed; the launcher's fixed subprocess pipeline is structurally incompatible with AER's `ExecutionProvider` model without a redesign, so no smallest-manifest composition exists today |

### Candidate 5: retain parked / exact proposed small path set

| Field | Value |
| --- | --- |
| Classification | `PROPOSED_NEW_DOC_ONLY` (this is the residual candidate the audit selects; see Findings / Position) |
| Trigger | none; this row documents the smallest future non-test caller design rather than an existing owner |
| Caller symbol | proposed: one new package-native factory function (see Candidate 1's smallest manifest), not yet authored |
| AER construction/import | proposed only; zero current source |
| Guard engine | proposed to reuse the existing exported `GuardRuntimeEngine` type and an existing engine instance passed in by the caller, not a new engine |
| Provider adapter | proposed to reuse the existing `ExecutionProvider`-conformant provider classes already present in `runtime/providers/` |
| Approval owner | proposed to reuse the already-exported `ApprovalExecutionBridge` unchanged |
| Provider-attempt owner | proposed: the new adapter must not introduce a second admission boundary; it must either be invoked from a call site that has no other admission boundary, or must explicitly delegate to an existing one |
| Durable receipt consumer | proposed: reuse an existing accepted durable-evidence owner (e.g., the Web reconciliation path) rather than inventing a new one |
| Response mapping | proposed only |
| Failure/rollback | Git-reversible; a small new file plus an `exports` entry can be removed cleanly |
| Exactly-once risk | LOWEST of the five: because nothing currently calls this adapter, a new T1 can be designed from a blank call site with the invariant enforced by construction, rather than retrofitted onto an existing dual-pipeline route |
| Smallest future write/test set | same as Candidate 1's Smallest future write/test set row |

## Sixteen Required Decision Questions

1. **Does current non-test source satisfy each historical reopen fact, separately?** No. Fact 1 (import/construction) is false for every non-test, non-manual-script path; the one non-test construction site (`scripts/run-brigade-residual-absorption-runtime-pilot.ts`) is classified `NOT_A_PRODUCTION_CALLER` per the work order's own manually-runnable-script exclusion. Facts 2-4 are consequently unreachable (there is no invoked production path to check wiring or receipt consumption against).

2. **What concrete registered trigger can own one logical execution?** None currently constructs or imports `AgentExecutionRuntime`. The two closest registered triggers are cvf-web's `POST /api/execute` (Candidate 2, rejected as a direct-wrap target because it already owns a complete, accepted, independent GC-009 pipeline) and the MCP `governed-exec` CLI subcommand (Candidate 4, rejected because its allow-listed subprocess boundary is structurally incompatible with `ExecutionProvider`). No current trigger can safely own AER's pipeline without either duplicating or replacing an already-accepted boundary.

3. **Is AER package-importable by that trigger today?** No. `AgentExecutionRuntime` is absent from `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` and from `package.json`'s `exports`/`files` fields. Only `ApprovalExecutionBridge` (and unrelated modules such as `mandatory-gateway`, `agent-handoff`, `agent-coordination`) are exposed as subpath exports.

4. **Which real `GuardRuntimeEngine` instance would AER receive?** None is currently wired to AER outside tests. cvf-web already owns one shared `GuardRuntimeEngine` singleton (`getSharedGuardEngine()` inside `mandatory-gateway-singleton.ts`), but it is bound to `MandatoryGateway`, and reusing the same engine instance for a second AER-owned guard boundary in the same request would risk double evaluation unless the two boundaries are proven mutually exclusive per request.

5. **Which real `ExecutionProvider` adapter would AER receive?** `GeminiProvider` and `AlibabaDashScopeProvider` under `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/providers/` already implement the `ExecutionProvider` interface and are the only current source-compatible adapters, but neither has a non-test, non-manual-script caller today.

6. **How does approval-required execution preserve exactly-once settlement?** `ApprovalExecutionBridge` (`approval-execution-bridge.ts:46-175`) is already accepted, package-exported, and implements bounded pending-approval tracking with a `settle` method; AER's constructor accepts it as an optional `approvalBridge` dependency (`agent-execution-runtime.ts:124`). This mechanism is source-proven only inside `AgentExecutionRuntime`'s own tests and the manual pilot script; no production trigger exercises it.

7. **Where is the single guard-evaluation boundary?** For the only currently accepted production execution chain (GC-009/cvf-web), the single guard-evaluation boundary is `runExecuteRouteMandatoryGateway` at `route.ts:594`. AER has its own separate, internal guard-evaluation boundary (`preCheck`, which calls `this.guardEngine.evaluate(...)`) that is not currently reachable from any production trigger. A future T1 must ensure exactly one of these boundaries executes per logical request, not both.

8. **Where is the single provider-attempt admission boundary?** For GC-009/cvf-web, it is `admitAndInvokeProvider` (`provider-attempt-admission.ts:352`), invoked once at the initial call site (`route.ts:801`) and once at the retry call site (`route.ts:859`), each call representing one admitted attempt. AER has no current admission boundary of its own beyond directly invoking `this.provider.execute(...)` inside `run`; a future integration must not let AER's direct provider call bypass an existing admission boundary, or must give AER its own equivalent boundary that is proven to run exactly once per admitted attempt.

9. **How are initial and retry calls prevented from double invocation?** In the only current production chain, `admitAndInvokeProvider` is called separately for the initial attempt and for each retry, and each call independently owns admission and invocation pairing (`route.ts:801`, `:859`). AER's own `run` method has no retry loop of its own; retries only exist in the GC-009 caller, not inside AER. No current source combines the two, so there is no live double-invocation risk today, only a design constraint for any future composition.

10. **Which durable receipt/audit consumer handles every terminal outcome?** For GC-009/cvf-web, the route's own reconciliation logic (downstream of `admitAndInvokeProvider`) is the accepted durable-evidence owner. No durable receipt/audit consumer currently exists on any path that constructs `AgentExecutionRuntime`, because no such production path exists.

11. **How are request, actor, session, approval, attempt, and receipt identities linked?** AER's `RuntimeConfig` carries `agentId`, `sessionId`, `cwd`, and `environment` fields used to build the approval binding hash inside `ApprovalExecutionBridge`. GC-009/cvf-web separately links request/actor/session/attempt/receipt identity through its own accepted pipeline. The two identity models are not currently unified; a future T1 would need to decide whether AER's identity fields are populated from the same values the Web route already derives, or kept independent.

12. **How are thrown/rejected calls, denial, timeout, cancellation, and exhaustion mapped?** AER's `run`/`runAwaitingApproval` methods return a typed `ExecutionResult` with a `status` field (observed values include `COMPLETED` in the pilot script's assertion at line 143); the class also logs to an internal `executionLog`. None of this is currently exercised by any production trigger, so no current-source mapping exists between AER's terminal states and any durable receipt consumer.

13. **Which candidate is smallest and source-compatible, or why are all rejected?** All five candidates are rejected as an `EXISTING_SOURCE_COMPATIBLE` production caller today. Candidates 2 and 4 are rejected as unsafe direct-wrap targets (duplicate guard/admission risk against already-accepted pipelines). Candidates 1 and 3 are `NO_CURRENT_OWNER`  -  no existing partial wiring to compose against. Candidate 1 (package-native adapter) is smaller and lower-risk than Candidate 3 (Execution Plane/MAO) because it can reuse the already-exported `ApprovalExecutionBridge` and the already-`ExecutionProvider`-conformant provider classes without touching an unrelated command-execution model.

14. **What exact non-test caller file/symbol or proposed small path set is selected?** No exact non-test caller exists today. The exact missing facts are: (a) no package export of `AgentExecutionRuntime`; (b) no registered trigger constructs it; (c) no current source proves guard/provider wiring on an invoked path; (d) no durable receipt consumer exists on such a path. The smallest proposed future path set (not authorized by this T0) is named in Candidates 1 and 5's Smallest future write/test set rows.

15. **What is the smallest T1 write manifest and focused deterministic test matrix?** Proposed (not authorized), and corrected from an earlier draft that named only an adapter: the manifest must include an actual new non-test consumer, not only composition. One new file `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime-adapter.ts` exporting a factory that composes an injected `GuardRuntimeEngine`, an injected `ExecutionProvider`, and the existing `ApprovalExecutionBridge` without introducing a second admission boundary; one new `package.json` `exports`/`files` entry for that path; one new, currently nonexistent cvf-web route (e.g. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/agent-execution/route.ts`) whose `POST` handler is the sole caller of the adapter and does not call the existing `runExecuteRouteMandatoryGateway`/`admitAndInvokeProvider` boundaries, avoiding duplication against GC-009; one co-located adapter `*.test.ts` asserting (i) the factory constructs exactly one `AgentExecutionRuntime`, (ii) a denied guard decision starts zero provider calls, (iii) an admitted attempt starts at most one provider call, and (iv) approval settlement occurs exactly once with timeout/abort cleanup preserved; one route-level test asserting the new route's single-adapter-call and non-duplication of the existing gateway/admission boundaries. No `route.ts` (`/api/execute`), MCP, or Execution Plane file is proposed for change. This manifest still leaves the new route's own trigger justification (why it should exist, who calls it, and its durable-receipt owner) as an open T1 design question, not resolved by this T0.

16. **Which one terminal token is supported, and what evidence defeats the alternatives?** `NO_VIABLE_CONSUMER_RETAIN_PARKED` is supported. `READY_FOR_T1_SINGLE_CONSUMER_COMPOSITION` is defeated because no candidate is `EXISTING_SOURCE_COMPATIBLE`  -  every current registered trigger either has no AER wiring at all (`NO_CURRENT_OWNER`) or is structurally incompatible with a safe AER composition (`EXISTING_SOURCE_INCOMPATIBLE`). `PARTIAL_READY_REQUIRES_INTERFACE_CHANGE` is defeated because the gap is not an interface mismatch on an otherwise-wired path; it is a complete absence of any current wiring or export. `BLOCKED_SOURCE_CONTRADICTION` is defeated because no binding packet fact was contradicted by current source; the historical four-fact condition and this T0's fresh recomputation agree.

## Findings / Position

Current committed source at `d7d23b817` does not satisfy the historical
four-fact reopen condition on any non-test, non-manual-script production
path, and no candidate family is `EXISTING_SOURCE_COMPATIBLE`. The one new
fact since the historical GC010-AER-T2 closure  -  `scripts/run-brigade-
residual-absorption-runtime-pilot.ts`'s non-test construction of
`AgentExecutionRuntime`  -  is classified `NOT_A_PRODUCTION_CALLER` because it
requires a live provider API key, is invoked by no package script and no CI
workflow, and matches the work order's own manually-runnable-script
exclusion. This finding does not change the terminal token; it changes only
the audit trail versus the historical T2 closure by naming and rejecting
this specific new construction site instead of finding zero non-test hits.

Selected terminal token: **`NO_VIABLE_CONSUMER_RETAIN_PARKED`**.

This retains GC-010 and the paired gc009-gc010 gap open, exactly as the
historical GC010-AER-T2 decision left them, while recording a smaller,
source-compatible proposed future manifest (Candidates 1/5's package-native
adapter) than the historical decision's fully rejected candidate set, for a
future reviewer to weigh if a fresh T1 work order is separately authorized.

## Risk / Corrective Action

| Residual risk | Corrective action |
| --- | --- |
| A future agent treats the pilot script's non-test construction as caller progress | this audit explicitly classifies and rejects it as `NOT_A_PRODUCTION_CALLER`; a future T1 packet must re-verify this classification against its own execution base rather than reuse this audit's finding without re-running the search |
| A future T1 wraps the existing GC-009 route directly with AER | Candidate 2 is explicitly rejected in this audit as `EXISTING_SOURCE_INCOMPATIBLE` with a named duplicate-guard/duplicate-admission risk; a future T1 must select the package-native adapter path or an equally isolated new call site instead |
| The proposed package-native adapter is authored without an explicit no-second-admission-boundary test | the Smallest future write/test set row names this as a required assertion, not an optional one |
| A future reviewer treats this T0's parked token as a mandate to open T1 automatically | the roadmap's Terminal Tokens section and this work order both state a ready/partial token, which this audit does not select, only permits reviewer consideration; `NO_VIABLE_CONSUMER_RETAIN_PARKED` carries no such permission at all |

## Mandatory Invariants Mapping

| Invariant | Current-source owner (only accepted production chain: GC-009/cvf-web) | AER-side status |
| --- | --- | --- |
| Guard evaluation occurs exactly once per admitted logical execution | `runExecuteRouteMandatoryGateway` (`route.ts:594`) | AER's own `preCheck` boundary is unreachable from any production trigger; no double-evaluation risk exists today because AER is never invoked in production |
| Provider-attempt admission occurs exactly once before each actual provider call, including retries | `admitAndInvokeProvider`, called once per attempt (`route.ts:801`, `:859`) | AER's `run` calls `this.provider.execute(...)` directly with no admission boundary of its own; not currently reachable in production |
| A denied attempt starts zero provider calls | enforced by `admitAndInvokeProvider`'s denial path | not exercised in production; unit-tested only inside AER's own test suite |
| An admitted attempt starts at most one provider call | enforced by `admitAndInvokeProvider` | not exercised in production |
| Approval settlement is exactly once and preserves timeout/abort cleanup | GC-009's own approval handling, independent of `ApprovalExecutionBridge` | `ApprovalExecutionBridge.settle` implements this for AER callers; proven only in AER's own tests and the manual pilot script, not in any production trigger |
| Durable receipt/audit projection is reconciled for every terminal outcome | GC-009's own reconciliation path | no AER-invoking production path exists to reconcile |
| No export, factory, facade, or test is counted as a production caller | N/A; GC-009 is a real production trigger | this audit explicitly excludes AER's test files and the manual pilot script from caller status per this rule |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/run_worker_return_fast_gate.py` |
| literalTokensReviewed | `Status`, `Purpose`, `Scope / Methodology`, `Findings / Position`, `Risk / Corrective Action`, `Checker Source Read-Ahead Block`, `Agent Operation Trace Block`, `Delta Execution Claim Boundary Control Block`, `Public Export Disposition`, `Claim Boundary`, required Agent Operation Trace field labels, required Delta field labels, allowed terminal-token vocabulary |
| gateRunPurpose | confirmation evidence after checker-source review, not first discovery of required structure |
| claimBoundary | read-ahead confirms document shape only; it does not establish current caller ownership or runtime behavior |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | current-source architecture decision only |
| claimDisposition | CLAIM_REJECTED: no runtime control is implemented or invoked |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime action or provider call is executed |
| invocationBoundary | local read-only source and governance commands only |
| interceptionBoundary | no direct interception, wrapper, runtime gate, external-agent launch, or provider invocation |
| claimLanguage | candidate recommendation pending independent review |
| forbiddenExpansion | no source, test, package, export, provider, live, public, deploy, GC-010 closure, or T1 work |

## Smallest Future T1 Manifest (Not Authorized By This T0)

The roadmap's T1 tranche scope is "minimal export/composition and one
non-test consumer," and its Mandatory Invariants explicitly state that "no
adapter is accepted merely because it exports or constructs the runtime."
The manifest below therefore names both the composition adapter *and* an
exact minimal non-test consumer that would invoke it, not the adapter alone.
No current source in this repository provides a call site that is both (a)
already registered as a production trigger and (b) free of an existing,
already-accepted guard/admission boundary it would duplicate (see Candidates
2 and 4 in the Candidate Comparison Contract above). The consumer named here
is therefore a **new, currently nonexistent** registered trigger, not a
composition onto an existing route or CLI command.

| Item | Value |
| --- | --- |
| New source file (adapter) | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime-adapter.ts` exporting a factory that composes an injected `GuardRuntimeEngine`, an injected `ExecutionProvider`, and the existing `ApprovalExecutionBridge` |
| New export entry | `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` `exports`/`files`; `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` barrel re-export |
| New non-test consumer (the missing fact) | one new, currently nonexistent cvf-web route, e.g. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/agent-execution/route.ts`, registered as its own Next.js route distinct from `/api/execute`, whose `POST` handler is the sole caller of the new adapter; this route must not call `runExecuteRouteMandatoryGateway` or `admitAndInvokeProvider`, so the adapter's own guard/admission boundary is the only one exercised on this path, with no duplication risk against the existing GC-009 route |
| New focused test (adapter) | one co-located `agent-execution-runtime-adapter.test.ts` asserting single-construction, zero-provider-call-on-denial, at-most-one-provider-call-on-admission, and exactly-once approval settlement with timeout/abort cleanup |
| New focused test (consumer) | one route-level test asserting the new route calls the adapter exactly once per request, calls neither `runExecuteRouteMandatoryGateway` nor `admitAndInvokeProvider`, and produces a durable receipt on every terminal outcome (completed, denied, thrown, timed out, cancelled) |
| Durable receipt consumer for the new route | to be selected by the T1 work order; either a new minimal receipt writer reusing the existing Web reconciliation storage, or an explicit `NO_CURRENT_OWNER` finding if none can be reused safely without duplicating GC-009's own receipt path |
| Explicitly excluded | no change to `route.ts` (`/api/execute`), `route-guard-gateway.ts`, `provider-attempt-admission.ts`, `mandatory-gateway-singleton.ts`, the MCP `governed-command-launcher.ts`/`governed-exec.ts`, or any Execution Plane Foundation contract file |
| Authorization status | proposed only; requires a fresh operator-authorized T1 work order after independent reviewer acceptance of this T0; the new route's trigger condition (who/what calls `/api/agent-execution` and why) is itself an open product-design question this T0 does not resolve |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | current private runtime source verification and independent CVF review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this audit and independent reviewer |
| Disposition | `BLOCKED_UNTIL_CVF_PROOF` for caller, runtime, or readiness claims |
| Claim boundary | this audit's candidate recommendation is pending evidence, not imported external authority |

## Terminal Token

`NO_VIABLE_CONSUMER_RETAIN_PARKED`

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this audit is a private provenance architecture decision with no
public runtime artifact or export change.

## Claim Boundary

This audit proves only a current-source architecture decision reached from
the worker's own captured execution base at `d7d23b817`. It does not
implement, export, construct, or invoke `AgentExecutionRuntime`; does not
create a receipt; does not establish a non-test production caller; does not
close GC-010 or the paired gc009-gc010 gap; does not authorize T1; and makes
no live, public-sync, deployment, or production-readiness claim. Reviewer
consideration of a fresh T1 packet is not authorized by the selected
`NO_VIABLE_CONSUMER_RETAIN_PARKED` token; only the `READY_FOR_T1_SINGLE_
CONSUMER_COMPOSITION` and `PARTIAL_READY_REQUIRES_INTERFACE_CHANGE` tokens
carry that permission, and neither was selected.
