# CVF LHW8 Workflow Connector Wave 8 Roadmap

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-05-28

---

## Authorization / Decision

Authorized by operator direction on 2026-05-28: "do follow work_order" —
continuation of LHW connector wave pattern after LHW7 CLOSED_PASS_BOUNDED.

LHW7 is CLOSED_PASS_BOUNDED at commit `1ca009f6`. Session state
`nextAllowedMove` confirms: future connector waves require fresh GC-018,
roadmap, source-verified work orders, roadmap-to-work-order trace matrix,
dispatch-quality gate, closure-quality gate, and governed file-size
maintainability planning. LHW8 is the direct continuation under those rules.

Fresh GC-018:
`docs/baselines/CVF_GC018_LHW8_WORKFLOW_CONNECTOR_WAVE8_2026-05-28.md`

Dispatch status: T1 CLOSED_PASS_BOUNDED. T2 CLOSED_PASS_BOUNDED. T3 CLOSED_PASS_BOUNDED. LHW8 wave CLOSED_PASS_BOUNDED.

Completion status: All three tranches (T1, T2, T3) are CLOSED_PASS_BOUNDED with completion reviews filed. LHW8 wave is CLOSED_PASS_BOUNDED.

## Scope / Target / Owner Boundary

Target: three documentation connector specs binding existing proven runtime
pieces into coherent chains where the runtime pieces already exist but no
connector ties them together.

Owner: CVF session-continuity and roadmap steering surface.

Allowed files per tranche: connector spec (new), work order (new or status
update), Fast Lane audit, completion review, session continuity. No
`.ts`/`.tsx`/`.js`/`.py` file. No `EXTENSIONS/` source. No receipt envelope
schema. No public-sync repo.

## Purpose

LHW7 closed the workflow-recovery-tool-reentry, project-memory-context-budget,
and failure-sim-spec-change connector tier. LHW8 fills the next layer of
disconnected-but-proven pairs:

- T1 — Memory Event Hook → Governance Snapshot Connector
- T2 — Execution Identity → Authority Chain Readout Connector
- T3 — Operational Benchmark → Failure Class Re-Intake Connector

Each tranche binds two or three already-closed runtime surfaces into one
Orchestrator-readable readout packet. All tranches are documentation-only.

## Operator Direction

LHW connector wave rule: "nạp kiến thức từ legacy, nhưng ưu tiên cho những
cái nào đã có sẵn mà còn rời rạc, thiếu 1 chút, để tạo thành workflow chain
chuẩn." LHW8 follows by selecting only flows where every cited surface is
already CLOSED_PASS_BOUNDED in HEAD.

## Authority Chain

- LHW7 roadmap: `docs/roadmaps/CVF_LHW7_WORKFLOW_CONNECTOR_WAVE7_ROADMAP_2026-05-28.md`
  — Status: CLOSED_PASS_BOUNDED
- LHW6 roadmap: `docs/roadmaps/CVF_LHW6_WORKFLOW_CONNECTOR_WAVE6_ROADMAP_2026-05-28.md`
  — Status: CLOSED_PASS_BOUNDED
- LH1 ledger: `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  — Remaining triggers for `agentmemory`, `tolaria`, `Claude Kit`,
    `Review CVF_4.md`, `CVF AUDIT LOG_md`, `Failure Simulation cho CVF.md`
- Active session: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
  — nextAllowedMove: "future connector waves require fresh GC-018, roadmap,
    source-verified work orders, trace matrix, dispatch-quality gate,
    closure-quality gate, and autorun gate evidence."

## Knowledge Absorption Blind-Spot Control Block

Control standard:
`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`

Scope sources resolved before this roadmap (each already closed):

- `docs/reviews/CVF_W2_MEMORY_EVENT_HOOKS_CONTEXT_PACKAGER_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_AIF_C_MEMORY_GATEWAY_PHASE2_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_VI3_AGENTMEMORY_CAPTURE_RECORD_READOUT_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_G1_EXECUTION_IDENTITY_RUNTIME_GATE_COMPLETION_2026-05-22.md`
- `docs/reviews/CVF_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_MA1_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_COMPLETION_2026-05-26.md`
- `docs/reviews/CVF_W4_OPERATIONAL_BENCHMARK_SCORECARD_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_V3_EXECUTION_DIAGNOSTIC_CONTRACT_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_LHW3_T2_REQUEST_CLARIFICATION_RE_INTAKE_LOOP_CONNECTOR_COMPLETION_2026-05-27.md`

Source families addressed per LH1 ledger triggers:

| Family | LH1 disposition | LH1 remaining trigger | LHW8 tranche |
| --- | --- | --- | --- |
| `agentmemory` | PARTIALLY_ABSORBED | Reopen for capture/read packaging improvements; raw reinjection remains blocked | T1 |
| `tolaria` | PARTIALLY_ABSORBED | Reopen for governed memory snapshot packaging or graph context readout; no reinjection | T1 |
| `Claude Kit` | PARTIALLY_ABSORBED | Reopen only for a concrete identity/runtime authority gap, not another role catalog | T2 |
| `Review CVF_4.md` | PARTIALLY_ABSORBED | Reopen for structured runtime maturity review | T2 |
| `CVF AUDIT LOG_md` | PARTIALLY_ABSORBED | Reopen for user-facing audit timeline/readout | T3 |
| `Failure Simulation cho CVF.md` | PARTIALLY_ABSORBED | Reopen for failure-simulation harness over existing evidence | T3 |

Accepted-source rule: each tranche must read current runtime/canonical source
files first for any field, enum, interface, schema key, or token already in
source.

Blind-spot adversarial roles:

- Workflow Architect: each connector must produce an actionable chain, not
  another inventory.
- Non-Coder Value Reviewer: connected flows must help a non-coder or agent
  understand what happened and what action is safe.
- Governance Auditor: receipts, boundaries, and no hidden runtime claim.
- Integration Maintainer: connector fields must be wirable to existing CVF
  owner surfaces without broad rewrites.

Stop rule: if any tranche requires runtime execution, raw memory reinjection,
external skill ingestion, database mutation, or provider behavior changes, stop
and return to Orchestrator.

Blind-spot verdict: CLEAR.

Basis: all scope sources exist as CLOSED_PASS_BOUNDED packets in HEAD; LH1
ledger triggers are named per family; no new source family is opened without a
ledger trigger; no runtime, provider, or memory reinjection surface is claimed.

## Candidate Screen

| Priority | Connector | Existing runtime pieces (already CLOSED) | Gap being closed | Disposition |
| --- | --- | --- | --- | --- |
| 1 | Memory Event Hook → Governance Snapshot Connector | W2 `MemoryEventHookDecision` (5 values); AIF-C `MemoryGatewayDecision` (`operation`, `decision`, `canReinject`, `rawMemoryReleased`); VI3 `AgentMemoryCaptureRecord` (`captureDecision`, `policyContext`, `privacyFilters`) | W2 says how each hook event is evaluated; AIF-C says how the gateway decides on memory operations; VI3 says what was captured — but no connector says "given a W2 event + AIF-C gateway decision, what is the advisory snapshot type and what fields must appear in the governance snapshot record?" Agents must infer this gap, leading to inconsistent capture audit trails. | ACCEPT for T1 |
| 2 | Execution Identity → Authority Chain Readout Connector | G1 `ExecutionIdentityDecision` (`cvfRole`, `contextScope`, `executionBoundary`, `receiptOwnership`, `authority`); W3 `ToolActionApprovalState` (6 values); MA1 `cvf.internalMultiAgentTransfer.ma1.v1` role assignment | G1 says who the actor is and whether they can execute; W3 says what approval state a tool action is in; MA1 says how to transfer work across roles — but no connector says "given an execution identity decision + tool approval state, what is the authority chain advisory type and which MA1 role should receive the handoff?" Orchestrators must infer this, losing governance traceability across role boundaries. | ACCEPT for T2 |
| 3 | Operational Benchmark → Failure Class Re-Intake Connector | W4 `OperationalBenchmarkScorecard` (`policyViolationRate`, `retryCount`, `taskCompletionRate`, `clarityStatus`); V3 `ExecutionDiagnosticClass` (22 values) and `ExecutionDiagnosticUserAction` (11 values); LHW3-T2 clarification re-intake packet types | W4 says how the current run is performing; V3 says what failure class was diagnosed; LHW3-T2 says what re-intake packet type is appropriate — but no connector says "when W4 signals degradation and V3 identifies a failure class, which LHW3-T2 re-intake type is recommended and which recovery advisory is appropriate?" | ACCEPT for T3 |

Rejection log:

- Provider stability connector — rejected: requires live provider behavior
  evidence beyond doc connector scope.
- External skill ingestion connector — rejected: Candidate 7 remains
  demand-gated.
- UI / hosted readiness connector — rejected: parked under VI5-T4/T5
  checkpoint.

## Recommended Sequence

### LHW8-T1 — Memory Event Hook → Governance Snapshot Connector

Deliverables:

- A connector spec defining the governance snapshot advisory packet:
  - field mapping: W2 `MemoryEventHookDecision` + `eventType` →
    AIF-C `MemoryGatewayDecision.operation` + `decision` →
    VI3 `AgentMemoryCaptureRecord.captureDecision` + `policyContext` →
    snapshot advisory type + `captureDecisionSummary`
  - explicit statement: "This connector does not re-execute memory operations.
    The snapshot packet is a non-blocking governance record advising what
    capture decision was taken and whether the snapshot is promotion-eligible."
  - boundary table: doc-only versus runtime-proven rows
  - explicit `runtimeExecutionAuthorized=false` and `canReinject=false`
    invariant statements
- Source Verification Table covering every W2, AIF-C, and VI3 field cited.

### LHW8-T2 — Execution Identity → Authority Chain Readout Connector

Deliverables:

- A connector spec tying G1 execution identity, W3 tool approval state,
  and MA1 role assignment into one authority chain readout packet:
  - field mapping: G1 `cvfRole` + `contextScope.scope` +
    `authority.canExecute` + `executionBoundary.boundary` →
    W3 `ToolActionApprovalState` →
    MA1 role assignment → `authorityChainAdvisoryType` +
    `handoffRoleRecommendation`
  - explicit `runtimeExecutionAuthorized=false` invariant statement
  - boundary table: doc-only versus runtime-proven rows
- Source Verification Table covering every G1, W3, and MA1 field cited.

Dispatch only after T1 is CLOSED_PASS.

### LHW8-T3 — Operational Benchmark → Failure Class Re-Intake Connector

Deliverables:

- A connector spec tying W4 benchmark scorecard + V3 diagnostic class +
  LHW3-T2 clarification re-intake into a failure-to-reintake advisory packet:
  - field mapping: W4 `OperationalBenchmarkScorecard.clarityStatus` +
    `policyViolationRate` + `taskCompletionRate` →
    V3 `ExecutionDiagnosticClass` + `ExecutionDiagnosticUserAction` →
    LHW3-T2 re-intake packet type → `benchmarkTriggerAdvisoryType` +
    `reIntakePacketTypeRecommended`
  - explicit `runtimeExecutionAuthorized=false` and `scenarioPlanningOnly=true`
    invariant statements
  - boundary table: doc-only versus runtime-proven rows
- Source Verification Table covering every W4, V3, and LHW3-T2 field cited.

Dispatch only after T1 + T2 are CLOSED_PASS.

## Non-Goals

- Runtime tool execution, command bridging, or CLI invocation
- Raw memory reinjection, `canReinject=true`, or `rawMemoryReleased=true`
- New memory tiers beyond Lane-H scope
- Extension of W2, AIF-C, VI3, G1, W3, MA1, W4, V3, or LHW3-T2 runtime behavior
- New role taxonomy or RBAC change
- Receipt envelope schema changes
- External skill ingestion or provider behavior changes
- Hosted readiness, production readiness, or public release readiness
- Any tranche beyond T3 without a fresh roadmap and GC-018

## Work Plan

| Tranche | Deliverable | Gate |
| --- | --- | --- |
| T1 | Memory Event Hook → Governance Snapshot Connector spec (5 sections) | None — open after GC-018 + dispatch-quality gate |
| T2 | Execution Identity → Authority Chain Readout Connector spec (5 sections) | HOLD until T1 CLOSED_PASS |
| T3 | Operational Benchmark → Failure Class Re-Intake Connector spec (5 sections) | HOLD until T1 + T2 CLOSED_PASS |

Each tranche: Fast Lane audit → work order → spec → completion review →
session continuity update → commit.

## Acceptance Criteria

- [x] T1 spec created; W2/AIF-C/VI3 field names used verbatim;
  memory-re-execution-blocked explicit; Source Verification Table complete
- [x] T2 spec created; G1/W3/MA1 field names used verbatim;
  `runtimeExecutionAuthorized=false` explicit; Source Verification Table complete
- [x] T3 spec created; W4/V3/LHW3-T2 field names used verbatim;
  `scenarioPlanningOnly=true` explicit; Source Verification Table complete
- [x] No `.ts`/`.tsx`/`.js`/`.py` file in diff across all three tranches
- [x] No `EXTENSIONS/` source file in diff across all three tranches
- [x] Session continuity updated after each tranche
- [x] Each spec < 250 lines per GC-023
- [x] Dispatch-quality gate PASS for each work order
- [x] Closure-quality gate PASS for each completion review

## Verification

Pre-dispatch verification (per work order):

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 9964d24e --head 00008651 --enforce
python governance/compat/check_markdown_structural_completeness.py --base 9964d24e --head 00008651 --enforce
python governance/compat/check_docs_governance_compat.py --base 9964d24e --head 00008651 --enforce
```

## Claim Boundary

LHW8 is a connector-normalization wave. It does not claim memory reinjection,
raw memory release, tool execution, CLI invocation, workflow re-execution,
spec-change automation, re-intake automation, new execution authority, new role
taxonomy, RBAC changes, receipt envelope extensions, external skill ingestion,
provider behavior changes, hosted readiness, production readiness, or public
release readiness.
