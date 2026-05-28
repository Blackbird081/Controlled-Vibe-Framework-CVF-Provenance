# CVF LHW10 Workflow Connector Wave 10 Roadmap

Memory class: SUMMARY_RECORD

Status: ACTIVE

docType: roadmap

Date: 2026-05-28

---

## Authorization / Decision

Authorized by operator direction on 2026-05-28: "Tiếp tục audit để mở roadmap
mới LHW10" — continuation of the LHW connector wave pattern after LHW9
CLOSED_PASS_BOUNDED at commit `c245bc5a`.

Fresh GC-018:
`docs/baselines/CVF_GC018_LHW10_WORKFLOW_CONNECTOR_WAVE10_2026-05-28.md`

Dispatch status: T1 WORK_ORDER_READY. T2 HOLD until T1 CLOSED_PASS.
T3 HOLD until T1 + T2 CLOSED_PASS.

## Scope / Target / Owner Boundary

Target: three documentation connector specs binding existing proven runtime
pieces into coherent chains where connectors are missing.

Owner: CVF session-continuity and roadmap steering surface.

Allowed files per tranche: connector spec (new), work order (new), Fast Lane
audit (new), completion review (new), session continuity update. No
`.ts`/`.tsx`/`.js`/`.py` file. No `EXTENSIONS/` source. No receipt envelope
schema. No public-sync repo.

## Purpose

LHW9 closed the MCP approval advisory, noncoder friction advisory, and
integration layer packaging connector tier. LHW10 fills the next layer of
disconnected-but-proven pairs:

- T1 — Workflow Transition Enforcement Advisory Connector
- T2 — Runtime Maturity Evidence Chain Connector
- T3 — Provider Health Degradation Advisory Connector

Each tranche binds two or three already-closed runtime surfaces into one
Orchestrator-readable readout packet. All tranches are documentation-only.

## Operator Direction

LHW connector wave rule: bind proven but disconnected surfaces — select only
flows where every cited surface is already CLOSED_PASS_BOUNDED in HEAD.
LHW10 follows by selecting only flows where all cited surfaces are confirmed
present at HEAD `118b8d48`.

## Authority Chain

- LHW9 roadmap: `docs/roadmaps/CVF_LHW9_WORKFLOW_CONNECTOR_WAVE9_ROADMAP_2026-05-28.md`
  — Status: CLOSED_PASS_BOUNDED
- LHW8 roadmap: `docs/roadmaps/CVF_LHW8_WORKFLOW_CONNECTOR_WAVE8_ROADMAP_2026-05-28.md`
  — Status: CLOSED_PASS_BOUNDED
- LH1 ledger: `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  — Triggers for `Agent Harnesses`, `Review CVF_3.md`, `Review CVF_4.md`,
    `cortex-hub`, `free Claude Code`, `freellmapi`, `CVF_EDIT_ANALYSIS.md`
- Active session: `CVF_SESSION/ACTIVE_SESSION_STATE.json`

## Knowledge Absorption Blind-Spot Control Block

Control standard:
`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`

Scope sources resolved before this roadmap (each already closed):

- `docs/reviews/CVF_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_WR1_WORKFLOW_RECOVERY_READOUT_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_COMPLETION_2026-05-28.md`
- `docs/reviews/CVF_VI1_W_SERIES_VERTICAL_EXECUTE_CHAIN_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_G1_EXECUTION_IDENTITY_RUNTIME_GATE_COMPLETION_2026-05-22.md`
- `docs/reviews/CVF_LHW8_T2_EXECUTION_IDENTITY_AUTHORITY_CHAIN_READOUT_CONNECTOR_COMPLETION_2026-05-28.md`
- `docs/reviews/CVF_W5_PROVIDER_METHOD_FALLBACK_NORMALIZATION_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_W4_OPERATIONAL_BENCHMARK_SCORECARD_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_COMPLETION_2026-05-28.md`

Source families addressed per LH1 ledger triggers:

| Family | LH1 disposition | LH1 remaining trigger | LHW10 tranche |
| --- | --- | --- | --- |
| `Agent Harnesses` | PARTIALLY_ABSORBED | Workflow resume/recovery runtime proof on one existing workflow | T1 |
| `Review CVF_3.md` | PARTIALLY_ABSORBED | Reopen for route-level invalid-transition enforcement | T1 |
| `Review CVF_4.md` | PARTIALLY_ABSORBED | Reopen for structured runtime maturity review | T2 |
| `cortex-hub` | PARTIALLY_ABSORBED | Reopen for code-intelligence adapter boundary, not engine import | T2 |
| `free Claude Code` | PARTIALLY_ABSORBED | Reopen for selected provider method or public claim | T3 |
| `freellmapi` | PARTIALLY_ABSORBED | Reopen for credential/quota/health UX with provider-specific boundary | T3 |
| `CVF_EDIT_ANALYSIS.md` | PARTIALLY_ABSORBED | Reopen when selecting next runtime workflow hardening tranche | T3 |

Blind-spot adversarial roles:

- Workflow Architect: each connector must produce an actionable chain.
- Non-Coder Value Reviewer: connected flows must help a non-coder understand
  what happened and what action is safe.
- Governance Auditor: receipts, boundaries, and no hidden runtime claim.
- Integration Maintainer: connector fields must be wirable without broad rewrites.

Stop rule: if any tranche requires runtime execution, raw memory reinjection,
MCP transport, external skill ingestion, or provider behavior changes, stop.

Blind-spot verdict: CLEAR.

## Candidate Screen

| Priority | Connector | Existing runtime pieces (already CLOSED) | Gap being closed | Disposition |
| --- | --- | --- | --- | --- |
| 1 | Workflow Transition Enforcement Advisory Connector | W1 `WorkflowStateMachineProjection.finalState`; WR1 `WorkflowRecoveryAction` (4 values); WR1 `WorkflowRequestedTransitionDisposition` (4 values); LHW7-T1 `reEntryAdvisoryType` | W1 knows the current workflow state; WR1 classifies whether a requested transition is valid or invalid and picks a recovery action (`escalate_to_governance`, `hold_for_reviewer_gate`, etc.). But no connector maps `invalid_from_current_state` × `escalate_to_governance` → a named `transitionEnforcementAdvisoryType` with an `invalidTransitionDisposition` and concrete recommended next step for Orchestrator. LHW7-T1 covered tool re-entry after recovery but not the transition enforcement decision itself. | ACCEPT for T1 |
| 2 | Runtime Maturity Evidence Chain Connector | VI1 `integratedSurfaceCount` + `requiredSurfaceCount`; G1 `ExecutionIdentityDecision.authority.canExecute`; LHW8-T2 `authorityChainAdvisoryType` (4 values) | VI1 counts how many surfaces are integrated; G1 says who can execute and at what boundary; LHW8-T2 says the authority chain advisory — but no connector maps these three into a named `runtimeMaturityAdvisoryType` that identifies which surface gap exists and what evidence is missing before a full maturity claim can be made. `Review CVF_4.md` asked "are layers actually enforced at runtime?" — this connector answers that question in a planning record. | ACCEPT for T2 |
| 3 | Provider Health Degradation Advisory Connector | W5 `ProviderMethodFallbackEvaluation.status` (5 values: `ready`, `missing_provider_model`, `not_supported`, `blocked_quota`, `stop_and_diagnose`); W4 `OperationalBenchmarkScorecard.clarityStatus` (3 values); LHW9-T1 `mcpApprovalAdvisoryType` | W5 knows provider method fallback posture; W4 knows benchmark clarity (and degradation signal); LHW9-T1 knows MCP tool approval state. No connector maps W5 fallback status × W4 clarity degradation signal → a named `providerHealthAdvisoryType` + `fallbackRecoveryStep` for Orchestrators to consult when a provider is degraded but the workflow should continue with advisory guidance. `free Claude Code` / `freellmapi` triggers: health UX and fallback/error/health concepts. | ACCEPT for T3 |

Rejection log:

- `abtop` runtime observability dashboard — rejected: requires live provider
  route beyond doc connector scope.
- `gridex` database mutation proof — rejected: requires live route.
- `md2html` renderer expansion — rejected: no connector gap; W6 artifact export
  fully closed.
- `OpenSpec` spec-change workflow — rejected: LHW3-T3 already closed spec-change
  packet connector.

## Recommended Sequence

### LHW10-T1 — Workflow Transition Enforcement Advisory Connector

Deliverables:

- A connector spec with field mapping:
  W1 `finalState` (current state of workflow) →
  WR1 `WorkflowRequestedTransitionDisposition` (4 values) →
  WR1 `WorkflowRecoveryAction` (4 values) →
  LHW7-T1 `reEntryAdvisoryType` (5 values) →
  `transitionEnforcementAdvisoryType` + `invalidTransitionDisposition`
- Explicit statement: "This connector does not execute workflow transitions or
  modify workflow state. The enforcement advisory is a governance planning record
  only."
- Boundary table: Runtime-proven (W1, WR1) / Doc-proven (LHW7-T1) / Doc-only
  (new fields) / Not authorized rows
- Explicit `runtimeExecutionAuthorized=false` invariant
- Source Verification Table: individual row per enum value for
  `WorkflowRecoveryAction` (4 rows) and `WorkflowRequestedTransitionDisposition`
  (4 rows) and `reEntryAdvisoryType` (5 rows)

### LHW10-T2 — Runtime Maturity Evidence Chain Connector

Deliverables:

- A connector spec with field mapping:
  VI1 `integratedSurfaceCount` (numeric) + `requiredSurfaceCount` →
  G1 `ExecutionIdentityDecision.authority.canExecute` (boolean) →
  LHW8-T2 `authorityChainAdvisoryType` (4 values) →
  `runtimeMaturityAdvisoryType` + `surfaceGapIdentified`
- Explicit `runtimeExecutionAuthorized=false` invariant
- Boundary table and Source Verification Table.

Dispatch only after T1 is CLOSED_PASS.

### LHW10-T3 — Provider Health Degradation Advisory Connector

Deliverables:

- A connector spec with field mapping:
  W5 `ProviderMethodFallbackEvaluation.status` (5 values) →
  W4 `OperationalBenchmarkScorecard.clarityStatus` (3 values) →
  LHW9-T1 `mcpApprovalAdvisoryType` (if tool-based provider) →
  `providerHealthAdvisoryType` + `fallbackRecoveryStep`
- Explicit `runtimeExecutionAuthorized=false` invariant; no provider routing
  change, no retry execution
- Boundary table and Source Verification Table.

Dispatch only after T1 + T2 are CLOSED_PASS.

## Non-Goals

- Workflow transition execution or workflow state mutation
- Runtime enforcement of transition rules
- Provider routing changes or retry execution
- Raw memory reinjection or `canReinject=true`
- New role taxonomy or RBAC change
- Receipt envelope extension
- External skill ingestion or provider behavior changes
- Hosted readiness, production readiness, or public release readiness
- Any tranche beyond T3 without a fresh roadmap and GC-018

## Work Plan

| Tranche | Deliverable | Gate |
| --- | --- | --- |
| T1 | Workflow Transition Enforcement Advisory Connector spec (5 sections) | None — open after GC-018 + dispatch-quality gate |
| T2 | Runtime Maturity Evidence Chain Connector spec (5 sections) | HOLD until T1 CLOSED_PASS |
| T3 | Provider Health Degradation Advisory Connector spec (5 sections) | HOLD until T1 + T2 CLOSED_PASS |

## Acceptance Criteria

- [ ] T1 spec created; W1/WR1/LHW7-T1 field names verbatim; transition-execution-blocked
  explicit; Source Verification Table complete with individual rows per enum value
- [ ] T2 spec created; VI1/G1/LHW8-T2 field names verbatim;
  `runtimeExecutionAuthorized=false` explicit; Source Verification Table complete
- [ ] T3 spec created; W5/W4/LHW9-T1 field names verbatim;
  `runtimeExecutionAuthorized=false` explicit; Source Verification Table complete
- [ ] No `.ts`/`.tsx`/`.js`/`.py` file in diff across all three tranches
- [ ] No `EXTENSIONS/` source file in diff across all three tranches
- [ ] Session continuity updated after each tranche
- [ ] Each spec < 250 lines per GC-023
- [ ] Dispatch-quality gate PASS for each work order
- [ ] Closure-quality gate PASS for each completion review

## Verification

Pre-dispatch verification (per work order):

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 118b8d48 --head <lhw10-commit> --enforce
python governance/compat/check_markdown_structural_completeness.py --base 118b8d48 --head <lhw10-commit> --enforce
python governance/compat/check_docs_governance_compat.py --base 118b8d48 --head <lhw10-commit> --enforce
```

## Claim Boundary

LHW10 is a connector-normalization wave. It does not claim workflow transition
execution, workflow state mutation, provider routing change, retry execution,
runtime enforcement of transitions, CLI invocation, memory reinjection, raw
memory release, new execution authority, new role taxonomy, RBAC changes,
receipt envelope extensions, external skill ingestion, provider behavior
changes, hosted readiness, production readiness, or public release readiness.
