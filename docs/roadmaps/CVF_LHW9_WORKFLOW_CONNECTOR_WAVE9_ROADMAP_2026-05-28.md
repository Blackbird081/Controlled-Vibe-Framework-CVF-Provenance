# CVF LHW9 Workflow Connector Wave 9 Roadmap

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-05-28

---

## Authorization / Decision

Authorized by operator direction on 2026-05-28: "Tiếp tục audit để mở roadmap
mới LHW9" — continuation of the LHW connector wave pattern after LHW8
CLOSED_PASS_BOUNDED at commit `00008651`.

Fresh GC-018:
`docs/baselines/CVF_GC018_LHW9_WORKFLOW_CONNECTOR_WAVE9_2026-05-28.md`

Dispatch status: T1 CLOSED_PASS_BOUNDED. T2 CLOSED_PASS_BOUNDED.
T3 CLOSED_PASS_BOUNDED. LHW9 wave CLOSED_PASS_BOUNDED.

## Scope / Target / Owner Boundary

Target: three documentation connector specs binding existing proven runtime
pieces into coherent chains where connectors are missing.

Owner: CVF session-continuity and roadmap steering surface.

Allowed files per tranche: connector spec (new), work order (new or status
update), Fast Lane audit, completion review, session continuity. No
`.ts`/`.tsx`/`.js`/`.py` file. No `EXTENSIONS/` source. No receipt envelope
schema. No public-sync repo.

## Purpose

LHW8 closed the memory-snapshot, authority-chain, and benchmark-reintake
connector tier. LHW9 fills the next layer of disconnected-but-proven pairs:

- T1 — MCP Tool Approval Advisory Connector
- T2 — Noncoder Friction Advisory Connector
- T3 — Integration Layer Packaging Connector

Each tranche binds two or three already-closed runtime surfaces into one
Orchestrator-readable readout packet. All tranches are documentation-only.

## Operator Direction

LHW connector wave rule: "nạp kiến thức từ legacy, nhưng ưu tiên cho những
cái nào đã có sẵn mà còn rời rạc, thiếu 1 chút, để tạo thành workflow chain
chuẩn." LHW9 follows by selecting only flows where every cited surface is
already CLOSED_PASS_BOUNDED in HEAD.

## Authority Chain

- LHW8 roadmap: `docs/roadmaps/CVF_LHW8_WORKFLOW_CONNECTOR_WAVE8_ROADMAP_2026-05-28.md`
  — Status: CLOSED_PASS_BOUNDED
- LHW7 roadmap: `docs/roadmaps/CVF_LHW7_WORKFLOW_CONNECTOR_WAVE7_ROADMAP_2026-05-28.md`
  — Status: CLOSED_PASS_BOUNDED
- LH1 ledger: `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  — Remaining triggers for `pancake-pos-mcp`, `AI-first vs Human-first`,
    `Human System Harness`, `Review CVF_2.md`, `De_xuat.md`
- Active session: `CVF_SESSION/ACTIVE_SESSION_STATE.json`

## Knowledge Absorption Blind-Spot Control Block

Control standard:
`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`

Scope sources resolved before this roadmap (each already closed):

- `docs/reviews/CVF_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_LHW6_T1_TOOL_RUNTIME_BRIDGE_ADVISORY_CONNECTOR_COMPLETION_2026-05-28.md`
- `docs/reviews/CVF_CB1_CONTEXT_BUDGET_REQUEST_SHAPING_READOUT_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_C8_PRODUCT_SKILL_PACK_SELECTION_READOUT_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_LHW3_T2_REQUEST_CLARIFICATION_RE_INTAKE_LOOP_CONNECTOR_COMPLETION_2026-05-27.md`
- `docs/reviews/CVF_G1_EXECUTION_IDENTITY_RUNTIME_GATE_COMPLETION_2026-05-22.md`
- `docs/reviews/CVF_LHW6_T2_CLI_TOOL_ONBOARDING_GOVERNANCE_CONNECTOR_COMPLETION_2026-05-28.md`
- `docs/reviews/CVF_LHW7_T1_WORKFLOW_RECOVERY_TOOL_REENTRY_CONNECTOR_COMPLETION_2026-05-28.md`

Source families addressed per LH1 ledger triggers:

| Family | LH1 disposition | LH1 remaining trigger | LHW9 tranche |
| --- | --- | --- | --- |
| `pancake-pos-mcp` | PARTIALLY_ABSORBED | Reopen only for MCP approval proof; no transport/runtime execution yet | T1 |
| `OpenAgentd` | PARTIALLY_ABSORBED | Reopen only for read-only tool runtime bridge design; execution remains blocked | T1 |
| `AI-first vs Human-first` | PARTIALLY_ABSORBED | Reopen for noncoder friction scoring or anti-overconstraint UX | T2 |
| `Human System Harness` | PARTIALLY_ABSORBED | Reopen for noncoder request clarification or workflow recovery proof | T2 |
| `Review CVF_2.md` | PARTIALLY_ABSORBED | Reopen for integration-layer packaging only after tool/MCP boundary proof | T3 |
| `De_xuat.md` | PARTIALLY_ABSORBED | Reopen for integration SDK/runtime readiness only with concrete user flow | T3 |

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
| 1 | MCP Tool Approval Advisory Connector | W3 `ToolActionSurface='mcp_tool'` + `ToolActionApprovalRecord`; TA1 `ToolActionApprovalState` (6 values); LHW6-T1 `bridgeAdvisoryType` (3 values) | W3 classifies MCP tool actions as surface `mcp_tool`; TA1 says approval state; LHW6-T1 says bridge advisory — but no connector maps `mcp_tool` surface × approval state → a named `mcpApprovalAdvisoryType` and required approval evidence list. Agents must infer this, leading to inconsistent MCP onboarding governance records. | ACCEPT for T1 |
| 2 | Noncoder Friction Advisory Connector | CB1 `ProductSkillPackRequestContextReadout` (`missingSignals`, `contaminationFlags`, `readiness`); C8 `ProductSkillPackSelectionStatus` (`selected`, `no_certified_pack_match`); LHW3-T2 clarification packet types (4 values) | CB1 says what context signals are missing; C8 says whether a pack was matched; LHW3-T2 says what re-intake packet to use — but no connector maps CB1 friction signals + C8 selection failure to a named `frictionAdvisoryType` with an `antiOverconstraintRecommendation` for non-coder operators. | ACCEPT for T2 |
| 3 | Integration Layer Packaging Connector | G1 `ExecutionIdentityDecision` (`executionBoundary`, `cvfRole`); LHW6-T2 `onboardingClassification` (5 values); LHW7-T1 `reEntryAdvisoryType` | G1 says who the actor is and what boundary applies; LHW6-T2 says how CLI tools are onboarded; LHW7-T1 says how re-entry is advised after recovery — but no connector maps these three into an `integrationLayerAdvisoryType` that packages a new integration's readiness posture and first onboarding step recommendation. | ACCEPT for T3 |

Rejection log:

- Runtime observability dashboard (`abtop`) — rejected *from this LHW wave*
  (LHW scope is documentation-only; `abtop` needs live route execution). NOT a
  permanent block — eligible for live-proof roadmap after LHW waves exhausted.
  LH1 trigger: "Reopen only for runtime observability dashboard or live
  failure-class trend readout." API keys available.
- External skill ingestion — rejected: Candidate 7 remains demand-gated.
- Database action proof (`gridex`) — rejected *from this LHW wave* (same reason:
  read-only database proof requires actual query execution, out of LHW scope).
  NOT a permanent block — eligible for live-proof roadmap post-LHW, read-only
  boundary only; mutation remains blocked. LH1 trigger: "Reopen only for
  read-only database action proof."

## Recommended Sequence

### LHW9-T1 — MCP Tool Approval Advisory Connector

Deliverables:

- A connector spec with field mapping:
  W3 `ToolActionSurface='mcp_tool'` + `sideEffect` →
  TA1 `ToolActionApprovalState` →
  LHW6-T1 `bridgeAdvisoryType` →
  `mcpApprovalAdvisoryType` + `approvalEvidenceRequired`
- Explicit statement: "This connector does not execute MCP tool calls or
  bridge to any MCP transport. The advisory packet is a governance planning
  record only."
- Boundary table: doc-only versus runtime-proven rows
- Explicit `runtimeExecutionAuthorized=false` invariant
- Source Verification Table covering every W3, TA1, and LHW6-T1 field cited.

### LHW9-T2 — Noncoder Friction Advisory Connector

Deliverables:

- A connector spec with field mapping:
  CB1 `missingSignals` + `contaminationFlags` + `readiness` →
  C8 `ProductSkillPackSelectionStatus` →
  LHW3-T2 clarification packet type →
  `frictionAdvisoryType` + `antiOverconstraintRecommendation`
- Explicit `canReinject=false` and `rawMemoryReleased=false` preserved
- Boundary table and Source Verification Table.

Dispatch only after T1 is CLOSED_PASS.

### LHW9-T3 — Integration Layer Packaging Connector

Deliverables:

- A connector spec with field mapping:
  G1 `executionBoundary.boundary` + `cvfRole` →
  LHW6-T2 `onboardingClassification` →
  LHW7-T1 `reEntryAdvisoryType` →
  `integrationLayerAdvisoryType` + `onboardingStepRecommended`
- Explicit `runtimeExecutionAuthorized=false` invariant
- Boundary table and Source Verification Table.

Dispatch only after T1 + T2 are CLOSED_PASS.

## Non-Goals

- MCP transport, MCP client, or MCP server execution
- Runtime tool execution or CLI invocation
- Raw memory reinjection or `canReinject=true`
- New role taxonomy or RBAC change
- Receipt envelope extension
- External skill ingestion or provider behavior changes
- Hosted readiness, production readiness, or public release readiness
- Any tranche beyond T3 without a fresh roadmap and GC-018

## Work Plan

| Tranche | Deliverable | Gate |
| --- | --- | --- |
| T1 | MCP Tool Approval Advisory Connector spec (5 sections) | None — open after GC-018 + dispatch-quality gate |
| T2 | Noncoder Friction Advisory Connector spec (5 sections) | HOLD until T1 CLOSED_PASS |
| T3 | Integration Layer Packaging Connector spec (5 sections) | HOLD until T1 + T2 CLOSED_PASS |

## Acceptance Criteria

- [x] T1 spec created; W3/TA1/LHW6-T1 field names verbatim;
  MCP-execution-blocked explicit; Source Verification Table complete
- [x] T2 spec created; CB1/C8/LHW3-T2 field names verbatim;
  `canReinject=false` preserved; Source Verification Table complete
- [x] T3 spec created; G1/LHW6-T2/LHW7-T1 field names verbatim;
  `runtimeExecutionAuthorized=false` explicit; Source Verification Table complete
- [x] No `.ts`/`.tsx`/`.js`/`.py` file in diff across all three tranches
- [x] No `EXTENSIONS/` source file in diff across all three tranches
- [x] Session continuity updated after each tranche
- [x] Each spec < 250 lines per GC-023
- [x] Dispatch-quality gate PASS for each work order
- [x] Closure-quality gate PASS for each completion review

## Verification

Pre-dispatch verification (per work order):

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 00008651 --head c245bc5a --enforce
python governance/compat/check_markdown_structural_completeness.py --base 00008651 --head c245bc5a --enforce
python governance/compat/check_docs_governance_compat.py --base 00008651 --head c245bc5a --enforce
```

## Claim Boundary

LHW9 is a connector-normalization wave. It does not claim MCP transport, tool
execution, CLI invocation, workflow re-execution, memory reinjection, raw
memory release, new execution authority, new role taxonomy, RBAC changes,
receipt envelope extensions, external skill ingestion, provider behavior
changes, hosted readiness, production readiness, or public release readiness.
