# CVF Agent Work Order - Delta-T7 Receipt-To-Execution Evidence Auditor

Memory class: FULL_RECORD
Status: DISPATCH_READY
Date: 2026-06-19
docType: work_order
Batch ID: DELTA-T7
Owner: Codex multi-role executor
Commit mode: WORKER_MAY_COMMIT
dispatchBaseHead: `f3219048`
executionBaseHead: N/A with reason: captured from dispatch continuity bridge
closureBaseHead: N/A with reason: captured after material commit
rawMemoryReleased: false

## Dispatch Prompt Envelope

Role: Codex dispatcher, implementer, reviewer, closer, and session-sync actor.

Canonical packet: this work order and matching Delta-T7 GC-018.

Commit mode: `WORKER_MAY_COMMIT`.

executionBaseHead: N/A with reason: captured from dispatch continuity bridge.

Current-time notes: GGL-T1 closed at `913c8c9b`; session sync is `f3219048`.

Do-not-misread notes: pure supplied-evidence audit only; no tool registration,
execution, file observation, mandatory invocation, or interception proof.

Required first actions: startup, source verification, pre-dispatch, dispatch
commit, handoff bridge, then pre-implementation before TypeScript edits.

Return contract: return `BLOCKED` if runtime contracts cannot support a
fail-closed pure audit without changing launcher/store/tool behavior.

## Purpose

Implement the source-verified Delta-T7 pure evidence auditor selected by the
operator and Delta capability roadmap.

## Required First Reads

| Artifact | Use |
| --- | --- |
| session front door/state/active handoff | current authority and parked scope |
| matching Delta-T7 GC-018 | exact authorization |
| Delta capability roadmap | Delta-T7 evidence classes |
| guard types | preflight audit schema |
| receipt consumption store | consumption marker schema |
| governed execution store | execution receipt schema |
| governed launcher and approval module | profile and marker ownership |

## Scope / Target / Owner Boundary

Allowed scope: one pure module, one focused test file, completion review,
evidence JSON, and status conversion in this packet.

Forbidden scope: launcher/store/preflight/consumer/profile/marker behavior,
MCP registration/index, CLI registration, provider/live, public-sync, UI,
queue/daemon, direct interception, and universal control claims.

## Intake Role Routing Decision

| Field | Disposition |
| --- | --- |
| intake summary | operator selected receipt-to-execution evidence auditor after GGL-T1 |
| scope classification | pure runtime-evidence consistency audit |
| risk sensitivity | R1; read-only pure object validation |
| selected role route | `SINGLE_AGENT_MULTI_ROLE` |
| role separation basis | phase-separated dispatch, implementation, review, closure, sync |
| escalation condition | any runtime mutation, tool registration, live/provider/public scope, or claim expansion |

## Authority Chain

| Level | Artifact | Status |
| --- | --- | --- |
| Operator | current request | ACCEPTED |
| Session | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | auditor ready |
| Roadmap | Delta capability roadmap Delta-T7 row | high-value candidate |
| GC-018 | matching Delta-T7 baseline | DISPATCH_READY |

## Agent Roles

| Role | Actor | Responsibility |
| --- | --- | --- |
| Dispatcher | Codex | source-verified packet and dispatch |
| Implementer | Codex | pure module and tests only |
| Reviewer/closer | Codex | adversarial chain tests and closure gates |
| Session-sync actor | Codex | separate continuity update |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: N/A with reason: this tranche adds MCP
package source/tests but does not edit governance guard or session source until
separate session sync.

Protected paths:

- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/receipt-to-execution-evidence-auditor.ts`
- `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/audit/receipt-to-execution-evidence-auditor.test.ts`

Operator authorization: current request releases Delta-T7 pure auditor only.

Rollback boundary: revert Delta-T7 module/tests and matching artifacts only.

## Agent Handoff Contract Control Block

| Field | Disposition |
| --- | --- |
| Contract source | `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md` |
| route | `SINGLE_AGENT_MULTI_ROLE` |
| rolePattern | one-agent-many-roles with phase-separated evidence |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, SESSION_SYNC |
| baseHeadFor(phase) | dispatch=`f3219048`; later anchors recorded by commit |
| changedSetScope(phase) | dispatch packet; implementation module/tests/completion/evidence; closure conversion; separate sync |
| traceScope(phase, actor) | exact manifests and commands per phase |
| commitOwner(phase) | Codex |
| crossBatchIsolation | clean worktree before dispatch |
| nextMoveSurfaces | update only in final separate session sync |
| closerOwner | Codex is designated closer |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
| --- | --- |
| Role separation ledger | dispatcher -> implementer -> reviewer -> closer -> sync |
| Evidence basis independence | committed source and phase-local reruns |
| Self-review challenge | mismatch every chain identity and changed-set boundary |
| Commit choreography | dispatch, bridge, material, bridge, closure, sync |
| Forbidden shortcut | no combined material/session commit or uncommitted closure claim |
| Gate sequence | pre-dispatch -> pre-implementation -> tests -> material -> pre-closure -> closure -> sync |
| Escalation conditions | any runtime/tool/profile/provider/public/interception or claim expansion |

## Receipt-To-Execution Audit Control Block

| Field | Disposition |
| --- | --- |
| chain | preflight audit -> consumption marker -> execution receipt -> optional approval marker -> changed set |
| identity | exact receipt/request/consumption/profile/binding correlation |
| chronology | ordered evidence timestamps |
| finalization | COMPLETED or FAILED durable evidence required |
| expectedChangedSetSource | static profile target policy |
| observedChangedSetAuthority | caller-supplied evidence only |
| claimBoundary | consistency audit, not action observation or interception |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | pure evidence auditor |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT through existing typed chain |
| actionEvidence | ACTION_EVIDENCE_PRESENT only for internally consistent finalized evidence |
| invocationBoundary | cooperating caller supplies evidence |
| interceptionBoundary | no IDE/shell/git/filesystem/provider interception |
| claimLanguage | bounded evidence consistency only |
| forbiddenExpansion | runtime/tool/profile/provider/public/queue/direct-interception scope parked |

## Delta Mutating Profile Boundary Control Block

| Field | Disposition |
| --- | --- |
| profileScope | existing static profile metadata is read only |
| fixedTargetPolicy | existing approval-marker target only |
| approvalEvidenceSource | optional supplied approval marker typed from existing writer contract |
| callerPathInput | CALLER_PATH_INPUT_FORBIDDEN as target authority; observed changed set is evidence only |
| commandAuthority | no command authority added |
| receiptChain | audit existing receipt/consumption/execution identity |
| claimBoundary | no new mutation or execution capability |
| forbiddenExpansion | arbitrary targets, EDIT/COMMIT, provider/live, public-sync, and interception parked |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | current source contracts -> verified pure auditor |
| Matching local-view guard | `governance/compat/check_delta_execution_claim_boundary.py` |
| Owner surface | Delta-T7 work order |
| Disposition | `DO_NOW` pure audit only |
| Claim boundary | no runtime/provider/public/interception/readiness claim |

## Source Verification Block

| Claimed item | Verification type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Preflight evidence schema exists. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/guards/types.ts` | interfaces | `GuardAuditEntry`; `GuardPipelineResult` | guard types | ACCEPT |
| Consumption marker schema exists. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-receipt-consumption.store.ts` | interface | `ReceiptConsumptionMarker` | receipt store | ACCEPT |
| Execution receipt schema exists. | EXISTS | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/persistence/json-governed-execution.store.ts` | interface | `GovernedExecutionReceipt` | execution store | ACCEPT |
| Static profile target owner exists. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | profile registry | `getGovernedCommandProfile` | launcher | ACCEPT |
| Approval marker contract and writer exist. | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/mutating-profile-approval.ts` | marker writer | `APPROVAL_MARKER_CONTRACT`; `writeApprovalMarkerFile` | approval module | ACCEPT |
| Delta-T7 is recommended. | LITERAL_INVARIANT | `docs/roadmaps/CVF_DELTA_EXECUTION_CONTROL_CAPABILITY_ROADMAP_2026-06-19.md` | Delta-T7 row | `Delta-T7 Receipt-To-Execution Evidence Auditor` | roadmap | ACCEPT |

## New Doc-Only Fields

| Item | Shape | Purpose |
| --- | --- | --- |
| Receipt-To-Execution Audit Control Block | required table | evidence/claim boundary |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: current runtime symbols and all audit outcomes must be computed
from current source.

unicodePathHandling: literal paths and UTF-8-safe readers.

## Foundation Storage Layout Block

| Field | Disposition |
| --- | --- |
| stable source | existing MCP `src/audit/` owner surface |
| dated execution artifacts | baseline, work order, completion, evidence JSON |
| generated aggregate | N/A with reason: none added |
| index | N/A with reason: source module imported directly by tests only |

## Current Runtime Freshness Verification

| Surface | Evidence |
| --- | --- |
| base | clean `f3219048` |
| package | MCP server v2.5 source currently contains Delta T1-T4A contracts |
| live/provider | N/A with reason: forbidden and unnecessary |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order owner | Evidence |
| --- | --- | --- |
| receipt, admission, execution marker, audit record, expected changed set | pure auditor module | focused tests and completion |
| preserve claim boundary | audit output | false interception/mandatory invocation fields |

## Allowed Changed Set

Dispatch: matching GC-018 and this work order.

Implementation: two module/test paths, this work order, matching completion
review, and matching evidence JSON.

Session sync: active handoff/front door/generated state only in separate phase.

## Acceptance Criteria

- [x] dispatch sources verified;
- [ ] valid non-mutating chain passes;
- [ ] valid fixed marker chain passes;
- [ ] identity/binding/chronology/finalization/profile mismatches fail;
- [ ] expected/observed changed-set mismatch fails;
- [ ] focused tests, package tests, and build pass;
- [ ] claim boundary remains explicit;
- [ ] continuity updated after closure.

## Verification Commands

```powershell
npx vitest run src/audit/receipt-to-execution-evidence-auditor.test.ts --reporter verbose
npm run test:run
npm run build
```

## Pre-Flight Checks

- [x] startup and clean base confirmed;
- [x] source facts verified;
- [x] runtime/tool/provider/public expansion forbidden.

## Write Ownership

Codex owns only the allowed changed set.

## Execution Plan

1. Dispatch and bridge continuity.
2. Implement pure auditor and adversarial tests.
3. Run focused/full/build and governance gates.
4. Commit material, bridge handoff, close artifacts, and sync continuity.

## Evidence Requirements

Exact source symbols, focused/full/build results, changed set, AOT, public
disposition, and bounded claim statement are mandatory.

## Review Gate

Reject if any mismatch can pass, unknown profile passes, ADMITTED-only evidence
passes, marker target is caller-controlled, or output implies interception.

## Closure Checklist

- [ ] acceptance criteria resolved;
- [ ] tests and build pass;
- [ ] exact manifests pass;
- [ ] no forbidden scope;
- [ ] continuity synchronized.

## Return-To-Orchestrator Conditions

Return blocked for missing source contract, unsafe inference, scope expansion,
or failing gate.

## Operator Checkpoint

No human checkpoint applies inside the pure audit scope. Runtime mutation,
provider/live, public-sync, or interception stays outside this packet.

## Worker Autonomy / No-Question Rule

Allowed-scope failures remain Codex-owned until passing. Forbidden expansion
is not executable under this packet.

## Closure Quality Gate

Closure requires committed evidence, resolved checklist, exact manifests,
machine closure package, and synchronized next move.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance evidence auditor.

## Machine Closure Package

| Field | Value |
| --- | --- |
| Status | DISPATCH_READY |
| Base | `f3219048` |
| Public export | `DEFERRED_PRIVATE_ONLY` |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex dispatcher |
| Provider or surface | Codex local workspace |
| Session or invocation | Delta-T7 dispatch, 2026-06-19 |
| Working directory | repository root |
| Command or tool surface | source reads, apply_patch, governance gates |
| Target paths | matching Delta-T7 GC-018 and work order |
| Allowed scope source | operator request and current session state |
| Before status evidence | worktree clean at base `f3219048` before dispatch authoring |
| After status evidence | two dispatch artifacts |
| Diff evidence | exact dispatch diff and pre-dispatch output |
| Approval boundary | dispatch only |
| Claim boundary | pure supplied-evidence audit; no runtime/interception claim |
| Agent type | single-agent multi-role |
| Invocation ID | `delta-t7-dispatch-codex-2026-06-19` |
| Expected manifest | `docs/baselines/CVF_GC018_DELTA_T7_RECEIPT_TO_EXECUTION_EVIDENCE_AUDITOR_2026-06-19.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_DELTA_T7_RECEIPT_TO_EXECUTION_EVIDENCE_AUDITOR_FOR_CODEX_2026-06-19.md` |
| Actual changed set | `docs/baselines/CVF_GC018_DELTA_T7_RECEIPT_TO_EXECUTION_EVIDENCE_AUDITOR_2026-06-19.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_DELTA_T7_RECEIPT_TO_EXECUTION_EVIDENCE_AUDITOR_FOR_CODEX_2026-06-19.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

Delta-T7 audits consistency of supplied evidence only. It does not observe or
force external execution and does not prove universal governed coding.
