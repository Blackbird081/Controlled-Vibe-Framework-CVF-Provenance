# CVF GC-018 GC-009/GC-010 Production Caller T0 Source-Verified Architecture Decision

Memory class: FULL_RECORD

Status: REVIEWER_ACCEPTED_DISPATCH_READY_WITH_REPAIRS

Batch ID: GC009-GC010-PCALLER-T0

Date: 2026-07-25

Dispatch base head: `4569a301d`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Authorize a bounded, documentation-only T0 tranche that identifies and
compares plausible existing production caller owners for `MandatoryGateway`
(GC-009) and `AgentExecutionRuntime` (GC-010), then issues a source-backed
architecture decision without changing runtime. This baseline does not
authorize implementation, caller wiring, package export changes, provider
calls, or CLI/MCP invocation. It authorizes only the T0 no-commit worker
described in the companion work order.

## Scope / Target / Owner Boundary

Allowed material paths for the T0 worker are exactly the two outputs named in
the companion work order's Write Ownership section
(`docs/audits/CVF_GC009_GC010_PRODUCTION_CALLER_T0_SOURCE_VERIFIED_ARCHITECTURE_DECISION_2026-07-25.md`
and
`docs/reviews/CVF_GC009_GC010_PRODUCTION_CALLER_T0_WORKER_RETURN_2026-07-25.md`).
No runtime, package export, barrel, test, checker, hook, session-state,
handoff, or other roadmap edit is authorized. Adding a caller, exporting a new
package surface, or invoking any CLI/MCP tool is explicitly outside this
tranche.

## Decision / Baseline / Proposed Tranche

Decision: dispatch a bounded, no-commit T0 architecture-decision packet. The
worker compares plausible existing non-test execution-channel owners already
present in current source (for example the `cvf-web` `/api/execute` route
family, the `cvf-guard-contract` Web adapters, and the MCP server's CLI/guard
surfaces) against the GC-009/GC-010 helper contracts, then issues exactly one
terminal disposition from the fixed enum in the companion work order. The
worker does not implement, wire, or export anything.

## Evidence / Verification

This packet-author pass source-verified the following before dispatch (full
citations in the companion roadmap's Source Verification Block):

- `MandatoryGateway`/`createMandatoryGateway` at
  `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` lines 66
  and 219; `AgentExecutionRuntime` at its class-definition section in
  `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts`.
- `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` `exports`/`files` (lines 8-27)
  and `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` (full file, 130 lines) omit
  both runtime modules.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-engine-singleton.ts`
  imports `createGuardEngine`/`GuardRuntimeEngine` from the canonical
  `cvf-guard-contract` package (lines 13, 21-26), and
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
  (959 lines) already calls `getSharedGuardEngine().evaluate(...)` at lines
  561 and 578 inside a real, currently-invoked `POST` handler with
  authentication, enforcement, and evidence-receipt logic -- but does not call
  `MandatoryGateway` or `AgentExecutionRuntime`.
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/engine.ts` defines a
  *separate*, non-canonical `GuardRuntimeEngine` (own local `types.js`, not
  `cvf-guard-contract`), and
  `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts`
  imports that local engine (lines 6-7), not the canonical package -- so the
  MCP/CLI surface is a plausible but currently-disconnected-from-GC-009/010
  candidate.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` is
  a registered GC-023 near-hard-threshold owner entrypoint
  (`governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` lines
  42-47), which bears on the T0 worker's minimal-T1-changed-set analysis: any
  future T1 wiring should avoid growing this file further and should prefer a
  new thin helper module.

The T0 worker must independently recompute this evidence at its own
`executionBaseHead` rather than trusting this baseline's snapshot, per the
Current Runtime Freshness Verification requirement.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | N/A with reason: this baseline was authored directly from the work-order template and a prior comparable baseline shape (`docs/baselines/CVF_GC018_MSEA_R94_T1B_GATEWAY_HELPER_OWNERSHIP_DISPOSITION_2026-07-11.md`) rather than the generic dispatch-packet scaffold generator. |
| generatedProfile | N/A with reason: not scaffold-generated. |
| generatedSkeletonStatus | N/A with reason: not scaffold-generated. |
| manualEditsAfterScaffold | N/A with reason: not scaffold-generated. |
| checkerReadAheadConfirmation | dispatch-quality, structural-completeness, handoff-boundary, worker-return-quality, agent-operation-trace, and Delta claim-boundary checker sources read before authoring; see `## Checker Source Read-Ahead Block` below |
| docOnlyNewFields | N/A with reason: no runtime or schema field is introduced by this baseline |
| claimBoundary | Dispatch baseline only; does not itself constitute T0 execution or T0 acceptance |

## Dependency Release Evidence

| Dependency | Artifact | Material commit | Final disposition | Status |
|---|---|---|---|---|
| Accepted T2 exhaustive caller-verification corpus | `docs/reviews/CVF_SYSTEM_CHAIN_EXHAUSTIVE_PROOF_T2_CALLER_VERIFICATION_COMPLETION_2026-07-15.md` | `498413cc9` | reviewer-accepted closure routing a fresh paired architecture-GAP packet as the only released next move | PASS |
| GAP entry recording the accepted no-caller finding | `docs/reference/system_chain/gaps/entries/gc009_gc010_no_production_caller.json` | `4858129d5`; refreshed at dispatch base `4569a301d` | `IMPLEMENTED_NOT_INVOCATION_PROVEN`; `actionOwner: PARKED_WITH_REASON` pending a fresh source-verified work packet | PASS (this GC-018 is that fresh work packet's dispatch authority) |
| MSEA-R94-T1B prior disposition of the same two matrix rows | `docs/baselines/CVF_GC018_MSEA_R94_T1B_GATEWAY_HELPER_OWNERSHIP_DISPOSITION_2026-07-11.md` | `3c5e87d7b` | corrected matrix rows to `IMPLEMENTED_NOT_INVOCATION_PROVEN`, matching this baseline's evidence | PASS (no conflict; this baseline extends rather than reopens that closure) |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| GAP entry current status is `IMPLEMENTED_NOT_INVOCATION_PROVEN` | VALUE_SET | `docs/reference/system_chain/gaps/entries/gc009_gc010_no_production_caller.json` | `currentStatus` field | `currentStatus` | system-chain gap registry | ACCEPT |
| GC-009 control matrix row | VALUE_SET | `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` | line 46 | `GC-009` | Governance Control Matrix | ACCEPT |
| GC-010 control matrix row | VALUE_SET | `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` | line 47 | `GC-010` | Governance Control Matrix | ACCEPT |
| MandatoryGateway implementation | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/mandatory-gateway.ts` | lines 66, 219 | `MandatoryGateway`; `createMandatoryGateway` | guard-contract runtime helper | ACCEPT |
| AgentExecutionRuntime implementation | EXISTS | `EXTENSIONS/CVF_GUARD_CONTRACT/src/runtime/agent-execution-runtime.ts` | line 129 | `AgentExecutionRuntime` | guard-contract runtime helper | ACCEPT |
| Public package surface omits both helpers | VALUE_SET | `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` | `exports`, `files`, lines 8-27 | `exports`; `files` | package manifest | ACCEPT |
| Main barrel factory omits both helpers | LITERAL_INVARIANT | `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | lines 117-130 (no `./runtime/mandatory-gateway` or `./runtime/agent-execution-runtime` export anywhere in the file) | `createGuardEngine` | guard-contract barrel | ACCEPT |
| cvf-web execute route already calls the shared canonical guard engine | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | lines 561, 578 | `getSharedGuardEngine`; `guardEngine.evaluate` | cvf-web execute route | ACCEPT |
| Shared guard engine singleton sources from canonical package | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/guard-engine-singleton.ts` | lines 13, 21-26 | `getSharedGuardEngine`; `createGuardEngine` | cvf-web guard singleton | ACCEPT |
| MCP server guard engine is a separate non-canonical implementation | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/engine.ts` | lines 1-17 | `GuardRuntimeEngine` | MCP server guard engine | ACCEPT |
| Governed CLI launcher imports the MCP-local engine, not cvf-guard-contract | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | lines 6-7 | `GuardRuntimeEngine` | MCP CLI launcher | ACCEPT |
| Execute route is a GC-023 registered near-threshold owner entrypoint | VALUE_SET | `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` | lines 42-47 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | GC-023 file-size exception registry | ACCEPT |

## Current Runtime Freshness Verification

Fresh searches at `4569a301d` (this packet-author's own pass) confirm the same
disposition the accepted T2 corpus recorded: `MandatoryGateway` and
`AgentExecutionRuntime` are constructed only inside their own co-located test
files (`mandatory-gateway.test.ts`, `agent-execution-runtime.test.ts`) and two
provider test files; the two non-test provider source files
(`gemini-provider.ts`, `alibaba-dashscope-provider.ts`) import only the
`ExecutionProvider` type. No non-test file constructs or invokes either class.
Separately, this pass identified that `cvf-web`'s `/api/execute` route and its
shared guard-engine singleton already consume the canonical
`cvf-guard-contract` package's base `GuardRuntimeEngine`/`createGuardEngine`
(but not `MandatoryGateway`/`AgentExecutionRuntime`), and that the MCP
server's CLI/guard surface uses a separate, non-canonical engine
implementation. The T0 worker must recompute this evidence at its own
`executionBaseHead` rather than trusting this baseline's snapshot.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`,
lifecyclePhase=`pre-dispatch`

Resolver command:
`python governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --json --max-results 50`

Returned defects (20 total): ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015,
ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045,
ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043,
ADIF-0049, ADIF-0006.

Per-defect avoidance is recorded in the companion roadmap's `## ADIF Defect
Registry Disclosure` section and the companion work order's own disclosure
section; this baseline does not repeat the full per-item note to avoid
duplicated literal-format risk across three artifacts citing the same list.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_active_session_state.py` |
| literalTokensReviewed | `Status: REVIEWER_ACCEPTED_DISPATCH_READY_WITH_REPAIRS`; `Source Verification Block`; `Dependency Release Evidence`; `ADIF Defect Registry Disclosure`; `Public Export Disposition`; `Claim Boundary`; `ROLE_ROUTING_MODES` route tokens; `HOLD_*`/`DRAFT`/`PROPOSED` must-not-contain-`CLOSED` rule |
| gateRunPurpose | Confirm packet compliance after source verification, not first discovery of requirements via failure |
| claimBoundary | Baseline and dispatch authority only; does not itself execute T0 |

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | Compare plausible existing production caller owners for GC-009/GC-010 and issue a source-backed architecture decision without runtime mutation. |
| scopeClassification | bounded source-comparison audit and architecture-decision documentation |
| riskSensitivity | R0; no runtime, package, or checker mutation |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | packet-author authors roadmap/GC-018/work order; independent reviewer/dispatcher reviews and releases; no-commit worker executes T0; independent reviewer/closer accepts and commits |
| escalationCondition | any proposed caller wiring, package export/barrel change, test edit, CLI/MCP invocation, or provider/live claim discovered during T0 |

## Dual Agent Surface Matrix

| Agent surface | Role | Interface | Authority and risk boundary | Required evidence | Adapter boundary and disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | packet-author, worker, reviewer/closer | local source reads, gap registry, control matrix, work order, worker return | two-output documentation boundary only; no runtime mutation authority | source-verified comparison, negative-search evidence, terminal disposition | native governed route; ALLOWED |
| EXTERNAL_AGENT_CLI_MCP | not invoked in T0; T0 may name an existing MCP/CLI surface (for example `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/`) as a candidate caller or projection target for a later T1/T3 tranche | bounded evidence-comparison only; no invocation in this tranche | no mutation, invocation, or closure authority in T0 | T0 architecture decision must cite exact candidate paths without invoking them | adapter not authorized in T0; `DEFERRED_WITH_REASON` pending a dedicated T1/T3 authorization |

## Negative Search And Collision Discipline

All absence claims (for example "no non-test caller constructs
MandatoryGateway/AgentExecutionRuntime") require searches that exclude tests,
generated coverage output, dependencies, archives, and the audit artifacts
themselves. A type-only import (`import type { ExecutionProvider } from
'../agent-execution-runtime'`) or a test-file construction is not production
invocation. A package source file existing on disk is not an exported/callable
consumer surface unless the manifest `exports`/`files` or the barrel
`index.ts` expose it.

Search root: `EXTENSIONS/` (excluding `node_modules`, `dist`, `coverage`).

Search command run by this packet-author pass:
`rg -n "new MandatoryGateway|createMandatoryGateway\(|new AgentExecutionRuntime" EXTENSIONS --glob "!**/node_modules/**" --glob "!**/dist/**" --glob "!**/coverage/**"`

Same-token collision recorded: the MCP server's own class
`EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/engine.ts` defines a class
literally named `GuardRuntimeEngine` (lines 1-17), the same bare name as the
canonical package's `EXTENSIONS/CVF_GUARD_CONTRACT/src/engine.ts` class. This
is a same-token, distinct-implementation collision, not evidence of either
class calling GC-009/GC-010; a bare-name search must not conflate the two.

Absent-versus-collision disposition: `MandatoryGateway`, `createMandatoryGateway`,
and `AgentExecutionRuntime` are ABSENT from every non-test production file in
the searched root (matches occur only in `mandatory-gateway.test.ts`,
`agent-execution-runtime.test.ts`, and two provider test files).
`GuardRuntimeEngine` is a COLLISION (two distinct classes share the bare
name; neither collision instance constructs or invokes `MandatoryGateway` or
`AgentExecutionRuntime`). The T0 worker must record its own search roots,
exact commands, and any further same-token collisions before recording an
absence disposition for any additional candidate symbol.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance architecture-decision baseline only; no
public-sync batch is authorized by this artifact.

## Claim Boundary

This baseline authorizes source-verified comparison and one terminal
architecture disposition for the GC-009/GC-010 production-caller gap. It does
not authorize a caller, export, implementation, test, Web, protocol, provider,
CLI/MCP invocation, public-sync, lifecycle, checker, hook, session, or any
other change. It does not claim T0 has been executed, reviewed, or accepted;
this baseline is reviewer-accepted for T0 dispatch after bounded repairs. T0
has not been executed, and T1-T4 remain held behind independent predecessor
closure.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_GC009_GC010_PRODUCTION_CALLER_T0_SOURCE_VERIFIED_ARCHITECTURE_DECISION_2026-07-25.md` | `Status: REVIEWER_ACCEPTED_DISPATCH_READY_WITH_REPAIRS` | PASS |
| Completion or reviewer artifact | N/A with reason | T0 worker return and any reviewer completion review do not exist yet | N/A with reason |
| Roadmap state | `docs/roadmaps/CVF_GC009_GC010_PRODUCTION_CALLER_AND_BOUNDED_E2E_RUNTIME_ROADMAP_2026-07-25.md` | T0 dispatch accepted with repairs; T1-T4 recorded `HOLD_*` | PASS |
| Registry JSON | N/A with reason | no corpus state change | N/A with reason |
| Registry Markdown | N/A with reason | no corpus state change | N/A with reason |
| External evidence digest | N/A with reason | no external evidence ingested | N/A with reason |
| System loop interlock | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_GAP_INDEX.json` | gap entry remains `IMPLEMENTED_NOT_INVOCATION_PROVEN` pending T0 acceptance | N/A with reason: gap closure requires independent reviewer acceptance of T0, not this baseline |
| Session continuity | active front doors | this baseline does not update `CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`, or the active handoff | N/A with reason: session-sync is a separate reviewer/closer-owned step after independent T0 acceptance |
