# CVF LHW7 Workflow Connector Wave 7 Roadmap

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-05-28

---

## Authorization / Decision

Authorized by operator direction on 2026-05-28: "LHW6 đã hoàn tất, tiếp tục xây
dựng roadmap mới, quy tắc cũ: nạp kiến thức từ legacy, nhưng ưu tiên cho những
cái nào đã có sẵn mà còn rời rạc, thiếu 1 chút, để tạo thành workflow chain
chuẩn."

LHW6 is CLOSED_PASS_BOUNDED. Session state `nextAllowedMove` confirms: future
connector waves require fresh GC-018, roadmap, source-verified work orders,
roadmap-to-work-order trace matrix, dispatch-quality gate, closure-quality gate,
and governed file-size maintainability planning. LHW7 is the direct continuation
under those rules.

Fresh GC-018:
`docs/baselines/CVF_GC018_LHW7_WORKFLOW_CONNECTOR_WAVE7_2026-05-28.md`

Dispatch status: T1 CLOSED_PASS_BOUNDED. T2 CLOSED_PASS_BOUNDED. T3 CLOSED_PASS_BOUNDED. LHW7 wave CLOSED_PASS_BOUNDED.

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

LHW6 closed the tool-bridge, CLI-onboarding, and project-memory connector tier.
LHW7 fills the next layer of disconnected-but-proven pairs:

- T1 — Workflow Recovery → Tool Bridge Re-Entry Connector
- T2 — Project Memory Readout → Context Budget Handoff Connector
- T3 — Failure Simulation → Spec-Change Re-Intake Connector

Each tranche binds two or three already-closed runtime surfaces into one
Orchestrator-readable readout packet. All tranches are documentation-only. No
source code, runtime module, live provider route, or provider behavior is
changed in LHW7.

## Operator Direction

The operator requested: "ưu tiên cho những cái nào đã có sẵn mà còn rời rạc,
thiếu 1 chút, để tạo thành workflow chain chuẩn."

LHW7 follows this direction by selecting only flows where every cited surface
is already CLOSED_PASS_BOUNDED in HEAD and the only missing artifact is a
connector standard.

## Authority Chain

- LHW6 roadmap: `docs/roadmaps/CVF_LHW6_WORKFLOW_CONNECTOR_WAVE6_ROADMAP_2026-05-28.md`
  — Status: CLOSED_PASS_BOUNDED
- LHW5 roadmap: `docs/roadmaps/CVF_LHW5_WORKFLOW_CONNECTOR_WAVE5_ROADMAP_2026-05-27.md`
  — Status: CLOSED_PASS_BOUNDED_AFTER_QUALITY_FIX
- LH1 ledger: `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  — Remaining triggers for `Agent Harnesses`, `OpenAgentd`, `caveman`,
    `Workflow GoClaw`, `Review CVF_1.md`, `CVF Edit`, `Review CVF_3.md`
- Active session: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
  — nextAllowedMove: "future connector waves require fresh GC-018, roadmap,
    source-verified work orders, trace matrix, dispatch-quality gate,
    closure-quality gate, and governed file-size maintainability planning."

## Knowledge Absorption Blind-Spot Control Block

Control standard:
`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`

Scope sources resolved before this roadmap (each already closed):

- `docs/reviews/CVF_WR1_WORKFLOW_RECOVERY_STATE_PROOF_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_LHW6_T1_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_COMPLETION_2026-05-28.md`
- `docs/reviews/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_LHW6_T3_PROJECT_MEMORY_READOUT_CONNECTOR_COMPLETION_2026-05-28.md`
- `docs/reviews/CVF_CB1_CONTEXT_BUDGET_REQUEST_SHAPING_READOUT_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_VI2_ROUTE_REQUEST_CONTEXT_PROFILE_READOUT_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_LHW5_T3_*_COMPLETION_2026-05-27.md` (failure simulation scenario packet)
- `docs/reviews/CVF_LHW3_*_SPEC_CHANGE_*_COMPLETION_2026-05-27.md`
- `docs/reviews/CVF_LHW3_*_CLARIFICATION_RE_INTAKE_*_COMPLETION_2026-05-27.md`

Source families addressed per LH1 ledger triggers:

| Family | LH1 disposition | LH1 remaining trigger | LHW7 tranche |
| --- | --- | --- | --- |
| `Agent Harnesses` | PARTIALLY_ABSORBED | Reopen for workflow recovery proof tied to tool-bridge advisory | T1 |
| `OpenAgentd` | PARTIALLY_ABSORBED | Reopen only for read-only tool runtime bridge design; execution remains blocked | T1 |
| `caveman` | PARTIALLY_ABSORBED | Reopen for context-budget readout already absorbed; project-memory handoff connector is next | T2 |
| `Workflow GoClaw` | PARTIALLY_ABSORBED | Reopen for context profile/packaging concepts already absorbed; cross-session handoff connector is next | T2 |
| `Review CVF_1.md` | PARTIALLY_ABSORBED | Reopen for project memory readout — partial absorption via LHW6-T3; handoff into context budget remains | T2 |
| `CVF Edit` | PARTIALLY_ABSORBED | Reopen when selecting next runtime workflow hardening tranche | T3 |
| `Review CVF_3.md` | PARTIALLY_ABSORBED | Reopen for route-level invalid-transition enforcement and spec-change traceability | T3 |

Accepted-source rule: each tranche must read current runtime/canonical source
files first for any field, enum, interface, schema key, or token already in
source. Completion reviews may be used to confirm closure posture only. Do not
scope from summaries alone.

Blind-spot adversarial roles:

- Workflow Architect: each connector must produce an actionable chain, not
  another inventory or catalog.
- Non-Coder Value Reviewer: connected flows must help a non-coder or agent
  understand what happened and what action is safe.
- Governance Auditor: receipts, boundaries, and no hidden runtime claim in any
  section.
- Integration Maintainer: connector fields must be wirable to existing CVF
  owner surfaces without broad rewrites.

Stop rule: if any tranche requires runtime execution, raw memory reinjection,
external skill ingestion, database mutation, or provider behavior changes, stop
and return to Orchestrator.

Blind-spot verdict: CLEAR.

Basis: all scope sources exist as CLOSED_PASS_BOUNDED packets in HEAD; LH1
ledger triggers are named per family; no new source family is opened without a
ledger trigger; no runtime, provider, or memory reinjection surface is claimed
in T1/T2/T3.

## Candidate Screen

| Priority | Connector | Existing runtime pieces (already CLOSED) | Gap being closed | Disposition |
| --- | --- | --- | --- | --- |
| 1 | Workflow Recovery → Tool Bridge Re-Entry Connector | WR1 `lastRestorableCheckpoint` + `recoveryAction` + `validationGate`; LHW6-T1 tool bridge advisory `bridgeAdvisoryType`; TA1 `approvalState` (6 states) | WR1 says which step to restart and recoveryAction; LHW6-T1 says how each tool surface is bridged; TA1 says whether the action needs approval — but no connector says, "if the restart target contains a tool call, is its prior approval still valid or must it be re-approved?" Agents currently must infer this. | ACCEPT for T1 |
| 2 | Project Memory Readout → Context Budget Handoff Connector | LHW6-T3 project memory readout packet (`includedTiers`, `summaryOnly`, `lastRestorableCheckpoint`, `memoryIdsAffected`, `canReinject=false`); CB1 `cvf.productSkillPackRequestContext.v1` (`budgetTier`, `signalDensity`, `missingSignals`, `contaminationFlags`); VI2 `requestContextReadout.missingSignals` | LHW6-T3 says what prior session contains; CB1/VI2 say what the current request lacks — but no connector says, "when resuming a session, which project-memory summary fields seed which CB1 missing signals while preserving `canReinject=false` and `rawMemoryReleased=false`?" This is the most expensive disconnect — cross-session resume currently leaves the agent to ad-hoc the handoff. | ACCEPT for T2 |
| 3 | Failure Simulation → Spec-Change Re-Intake Connector | LHW5-T3 failure simulation scenario packet (`simulationSteps`, `boundaryStatement`, planning thresholds); LHW3 spec-change packet; LHW3 clarification re-intake packet | LHW5-T3 produces failure scenarios; LHW3 produces spec-change and clarification re-intake packets — but no connector says, "when a failure scenario implies a spec change, which spec-change packet field maps to which re-intake field and which recovery action triggers." | ACCEPT for T3 |

Rejection log:

- External skill intake connector — rejected: Candidate 7 ingestion remains
  demand-gated; not a "rời rạc + chỉ thiếu kết nối" case.
- Provider stability connector — rejected: requires live provider behavior
  evidence beyond doc connector scope.
- Hosted readiness connector — rejected: parked under VI5-T4/T5 checkpoint.

## Recommended Sequence

### LHW7-T1 — Workflow Recovery → Tool Bridge Re-Entry Connector

Deliverables:

- A connector spec defining the recovery re-entry advisory packet:
  - field mapping: WR1 `lastRestorableCheckpoint.stepId` + `recoveryAction` +
    `validationGate` → LHW6-T1 `bridgeAdvisoryType` →
    TA1 `approvalState` → re-entry advisory type
  - explicit statement: "This connector does not re-execute tool calls. The
    re-entry packet is a non-blocking governance record advising whether prior
    approval state should be reused or invalidated on restart."
  - boundary table: doc-only versus runtime-proven rows
  - explicit `runtimeExecutionAuthorized=false` invariant statement
- Source Verification Table covering every WR1, LHW6-T1, and TA1 field cited.

Owner surface (planned for future runtime adoption, not LHW7): cvf-web
workflow-resolver recovery section + governance/contracts tool-action-taxonomy
read paths. LHW7 changes none of these.

No `.ts`/`.tsx`/`.js`/`.py` or `EXTENSIONS/` file modified.

### LHW7-T2 — Project Memory Readout → Context Budget Handoff Connector

Deliverables:

- A connector spec tying LHW6-T3 project memory readout, CB1 request context,
  and VI2 request context readout into a cross-session handoff packet:
  - field mapping: LHW6-T3 `includedTiers` + `summaryOnly` +
    `memoryIdsAffected` → CB1 `budgetTier` + `signalDensity` +
    `missingSignals` + `contaminationFlags` → VI2 `missingSignals` →
    handoff packet fields (`seedableSummaryFields`, `signalsSeededBySummary`,
    `signalsStillMissing`, `contaminationRiskAfterSeed`)
  - explicit `canReinject=false` and `rawMemoryReleased=false` preserved
  - explicit statement: "This connector does not inject memory into the
    prompt. Seeding is a summary-only signal map advising the agent which CB1
    missing signals the project memory summary can populate; raw memory is
    never released."
  - boundary table: doc-only versus runtime-proven rows
- Source Verification Table covering every LHW6-T3, CB1, and VI2 field cited.

Dispatch only after T1 is CLOSED_PASS.

### LHW7-T3 — Failure Simulation → Spec-Change Re-Intake Connector

Deliverables:

- A connector spec tying LHW5-T3 failure simulation + LHW3 spec-change +
  LHW3 clarification re-intake into one fault-to-respec chain:
  - field mapping: LHW5-T3 `simulationSteps` + `boundaryStatement` →
    spec-change packet field → clarification re-intake packet field →
    WR1 `recoveryAction` recommendation
  - explicit statement: "This connector does not execute spec changes or
    re-intake actions. It is an advisory packet mapping a failure scenario
    onto an existing spec-change and re-intake record."
  - boundary table: doc-only versus runtime-proven rows
- Source Verification Table covering every LHW5-T3 and LHW3 field cited.

Dispatch only after T1 + T2 are CLOSED_PASS.

## Non-Goals

- Runtime tool execution, command bridging, or CLI invocation
- Raw memory reinjection, `canReinject=true`, or `rawMemoryReleased=true`
- New memory tiers beyond Lane-H scope
- Extension of WR1, TA1, LHW6-T1, LHW6-T3, CB1, VI2, LHW5-T3, or LHW3
  runtime behavior
- New role taxonomy or RBAC change
- Receipt envelope schema changes
- External skill ingestion or Candidate 7 ingestion
- Provider behavior changes
- Hosted readiness, production readiness, or public release readiness
- Any tranche beyond T3 without a fresh roadmap and GC-018

## Work Plan

| Tranche | Deliverable | Gate |
| --- | --- | --- |
| T1 | Workflow Recovery → Tool Bridge Re-Entry Connector spec (5 sections) | None — open after GC-018 + dispatch-quality gate |
| T2 | Project Memory Readout → Context Budget Handoff Connector spec (5 sections) | HOLD until T1 CLOSED_PASS |
| T3 | Failure Simulation → Spec-Change Re-Intake Connector spec (5 sections) | HOLD until T1 + T2 CLOSED_PASS |

Each tranche: Fast Lane audit → work order (with Source Verification Table +
Roadmap-to-Work-Order Trace Matrix) → spec → completion review → session
continuity update → commit. Each commit must pass
`check_work_order_dispatch_quality.py --enforce` and the closure-quality gate.

## Acceptance Criteria

- [x] T1 spec created; WR1/LHW6-T1/TA1 field names used verbatim;
  tool-re-execution-blocked explicit; Source Verification Table complete
- [x] T2 spec created; LHW6-T3/CB1/VI2 field names used verbatim;
  `canReinject=false` and `rawMemoryReleased=false` explicit;
  Source Verification Table complete
- [x] T3 spec created; LHW5-T3/LHW3 field names used verbatim;
  spec-change-execution-blocked explicit; Source Verification Table complete
- [x] No `.ts`/`.tsx`/`.js`/`.py` file in diff across all three tranches
- [x] No `EXTENSIONS/` source file in diff across all three tranches
- [x] Session continuity updated after each tranche
- [x] Each spec < 250 lines per GC-023 (split at 200 if needed)
- [x] Dispatch-quality gate PASS for each work order
- [x] Closure-quality gate PASS for each completion review

## Verification

Roadmap-level:

- source files cited and LH1 triggers mapped per family;
- connector specs use existing CVF field names only;
- every boundary table row is honest about current status (doc-only vs proven);
- no runtime, provider, or memory claim without live proof.

Implementation-level (per work order):

- Source Verification Table required for any field cited from a runtime source;
  guessed or "confirm later" fields block closure;
- Roadmap-to-Work-Order Trace Matrix required before ready/dispatch;
- no `.ts`, `.tsx`, `.js`, `.py` file modified in T1/T2/T3;
- GC-023 file size guard: each spec < 250 lines; split at 200 if needed.

Pre-dispatch verification (per work order):

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base HEAD --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce
python governance/compat/check_docs_governance_compat.py --base HEAD --head HEAD --enforce
```

## Claim Boundary

LHW7 is a connector-normalization wave. It does not claim tool execution, CLI
invocation, workflow re-execution, memory reinjection, raw memory release,
spec-change automation, re-intake automation, new execution authority, new role
taxonomy, RBAC changes, receipt envelope extensions, external skill ingestion,
provider behavior changes, hosted readiness, production readiness, or public
release readiness.
