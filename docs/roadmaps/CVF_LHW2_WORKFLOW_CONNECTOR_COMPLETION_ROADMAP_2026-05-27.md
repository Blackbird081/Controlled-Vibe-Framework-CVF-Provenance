# CVF LHW2 Workflow Connector Completion Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-05-27

---

## Authorization / Decision

Authorized by operator direction on 2026-05-27: "nạp kiến thức từ legacy,
hoàn chỉnh thêm các workflow. Ưu tiên các flow đã có các miếng rời rạc, chỉ
còn thiếu chuẩn kết nối."

LHW1 is CLOSED_PASS_BOUNDED. Session state `nextAllowedMove` confirms: "next
legacy absorption should prioritize high-value workflow connectors with existing
disconnected pieces." LHW2 is the direct continuation.

## Scope / Target / Owner Boundary

Target: three documentation connector specs binding existing proven runtime
pieces into coherent handoff chains.

Owner: CVF session-continuity and roadmap steering surface.

Allowed files per tranche: connector spec (new), work order (status update),
session continuity. No `.ts`/`.tsx`/`.js`/`.py` file. No `EXTENSIONS/`. No
receipt envelope schema. No public-sync repo.

## Purpose

LHW2 closes the second legacy workflow connector wave. LHW1 established the
horizontal layer: skill pack → workflow chain → context profile. LHW2 completes
the vertical connectors that were left as documented boundaries in LHW1:

- T1 — Memory Event Capture → Workflow Receipt Loop Connector
- T2 — Workflow Recovery Action Packet Connector
- T3 — Tool Approval → MA1 Handoff Connector

All three tranches are documentation-only. No source code, runtime module, live
provider route, or provider behavior is changed in LHW2.

## Operator Direction

The operator requested: "nạp kiến thức từ legacy, hoàn chỉnh thêm các workflow.
Ưu tiên các flow đã có các miếng rời rạc, chỉ còn thiếu chuẩn kết nối."

LHW2 follows this direction by targeting flows where the runtime pieces
(W2, WR1, TA1, VI3, M1, MA1) already exist as proven closed tranches but no
connector standard ties them together into a coherent handoff chain.

## Authority Chain

- LHW1 roadmap: `docs/roadmaps/CVF_LHW1_LEGACY_WORKFLOW_CONNECTOR_ABSORPTION_ROADMAP_2026-05-27.md`
  — Status: CLOSED_PASS_BOUNDED
- LH1 ledger: `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  — Remaining triggers for `agentmemory`, `Agent Harnesses`, `pancake-pos-mcp`
- Active session: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
  — nextAllowedMove confirms: "next legacy absorption should prioritize
    high-value workflow connectors with existing disconnected pieces"

## Knowledge Absorption Blind-Spot Control Block

Control standard:
`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`

Scope sources resolved before this roadmap:

- `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
- `docs/reviews/CVF_W2_MEMORY_EVENT_HOOKS_CONTEXT_PACKAGER_COMPLETION_2026-05-24.md`
- `docs/reviews/archive/CVF_WR1_WORKFLOW_RECOVERY_STATE_PROOF_COMPLETION_2026-05-25.md`
- `docs/reviews/archive/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`
- `docs/reviews/archive/CVF_VI3_AGENTMEMORY_CAPTURE_RECORD_READOUT_COMPLETION_2026-05-25.md`
- `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
- `docs/reviews/CVF_LHW1_T2_WORKFLOW_CHAIN_STATE_CONNECTOR_COMPLETION_2026-05-27.md`

Source families addressed per LH1 ledger triggers:

| Family | LH1 disposition | LH1 remaining trigger | LHW2 tranche |
| --- | --- | --- | --- |
| `agentmemory` | PARTIALLY_ABSORBED | Reopen for capture/read packaging improvements | T1 |
| `Agent Harnesses` | PARTIALLY_ABSORBED | Reopen for workflow resume/recovery runtime proof on one existing workflow | T2 |
| `pancake-pos-mcp` | PARTIALLY_ABSORBED | Reopen only for MCP approval proof; no transport/runtime execution yet | T3 |
| `deepagents` | ACCEPT_AS_DOCTRINE | Reopen only for bounded worker delegation proof | T2 advisory |
| `Workflow GoClaw` | PARTIALLY_ABSORBED | Reopen for context profile packaging after selector/memory traffic | T1 advisory |

Accepted-source rule: each tranche reads the detailed legacy source files for
its family before implementation. Do not scope from summaries alone.

Blind-spot adversarial roles:

- Workflow Architect: each connector must create an actual handoff chain, not
  another prose inventory.
- Non-Coder Value Reviewer: connected flows must help a non-coder or agent
  understand what happened and what to do next.
- Governance Auditor: receipts, boundaries, and no hidden runtime claim in any
  section.
- Integration Maintainer: connector fields must be wirable to existing CVF
  owner surfaces without broad rewrites.

Stop rule: if any tranche requires runtime execution, raw memory reinjection,
external skill ingestion, database mutation, or provider behavior changes, stop
and return to Orchestrator.

Blind-spot verdict: CLEAR.

Basis: all scope sources exist; LH1 ledger triggers are named per family;
no new source family is opened without a ledger trigger; Candidate 7 external
ingestion remains HOLD; adversarial roles above completed; no runtime,
provider, or memory reinjection surface is claimed in T1/T2/T3.

## Candidate Screen

| Priority | Connector | Existing runtime pieces | Gap being closed | Disposition |
| --- | --- | --- | --- | --- |
| 1 | Memory Event Capture → Workflow Receipt Loop | W2 hooks, VI3 capture record, M1 durable memory, H2 hierarchy | No connector ties event hooks → capture record → receipt into a traceable loop | ACCEPT for T1 |
| 2 | Workflow Recovery Action Packet | WR1 readout, W1 state machine, LHW1-T2 phase table, Agent Harnesses | WR1 classifies transition states but provides no packet template for escalate/retry/hold/abort actions | ACCEPT for T2 |
| 3 | Tool Approval → MA1 Handoff | W3 taxonomy, TA1 approval readout, MA1 transfer packet | TA1 outputs approval state but no connector defines how a pending_approval state routes into a MA1 handoff packet | ACCEPT for T3 |

## Recommended Sequence

### LHW2-T1 — Memory Event Capture Workflow Receipt Loop Connector

Deliverables:

- A canonical connector spec binding W2 event hook classes → VI3 capture record
  fields → controlled-memory receipt fields.
- Field mapping table: event hook class → capture record field → receipt field →
  propagation rule.
- Loop completion standard: when `canReinject=false` and `rawMemoryReleased=false`
  are enforced, what evidence trail is expected in the receipt.
- Boundary table: which steps are currently doc-only versus runtime-proven.

No LPF, cvf-web, or audit-memory-receipt.ts file is modified.

### LHW2-T2 — Workflow Recovery Action Packet Connector

Deliverables:

- A connector spec turning each WR1 transition class into a concrete MA1-
  compatible recovery action packet:
  - `no_requested_transition` → advisory hold packet
  - `configured_deferred_gate` → reviewer gate hold packet
  - `valid_from_current_state` → advance packet
  - `invalid_from_current_state` → escalate-to-governance packet
- Required fields per packet type.
- Mapping from `lastRestorableCheckpoint` to the restore packet input.
- Boundary table: doc-only versus runtime-enforced rows.

Dispatch only after T1 is CLOSED_PASS.

### LHW2-T3 — Tool Approval MA1 Handoff Connector

Deliverables:

- A connector spec mapping each TA1 approval state to its MA1 transfer packet
  outcome:
  - `pending_approval` → approval request packet (who approves, what evidence,
    which MA1 sections are R/O/N/A)
  - `blocked_by_policy` → block notification packet
  - `satisfied_but_not_executable` → readiness-confirmed-but-not-yet packet
- Boundary table: doc-only versus runtime-enforced rows.
- Explicit statement: `runtimeExecutionAuthorized=false` is preserved;
  this connector does not grant execution authority.

Dispatch only after T2 is CLOSED_PASS.

## Non-Goals

- Runtime enforcement of any connector binding
- Extension of W2, WR1, TA1, or VI3 runtime behavior
- New memory tiers, raw memory reinjection, or `canReinject=true`
- Tool/MCP/database execution authority
- Receipt envelope schema changes
- External skill ingestion or Candidate 7 ingestion
- Provider behavior changes
- Hosted readiness, production readiness, or public release readiness
- Any tranche beyond T3 without a fresh roadmap and GC-018

## Work Plan

| Tranche | Deliverable | Gate |
| --- | --- | --- |
| T1 | Memory Event Capture Workflow Receipt Loop Connector spec (6 sections) | None — open |
| T2 | Workflow Recovery Action Packet Connector spec (5 sections) | T1 CLOSED_PASS |
| T3 | Tool Approval MA1 Handoff Connector spec (5 sections) | T1 + T2 CLOSED_PASS |

Each tranche: Fast Lane audit → work order → spec → completion review → session
continuity update → commit.

## Acceptance Criteria

- [ ] T1 spec created; S2 field mapping uses W2 + VI3 names verbatim; Source
  Verification Table complete; `canReinject=false` explicit
- [ ] T2 spec created; all 4 WR1 transition classes mapped to MA1 packet
  templates; boundary table honest
- [ ] T3 spec created; all 6 TA1 approval states mapped; `runtimeExecutionAuthorized=false`
  explicit; demand-gated items listed; LHW2 roadmap updated to `CLOSED_PASS_BOUNDED`
- [ ] No `.ts`/`.tsx`/`.js`/`.py` file in diff across all three tranches
- [ ] Session continuity updated after each tranche

## Verification

Roadmap-level:

- source files cited and LH1 triggers mapped per family;
- connector specs are in English and use existing CVF field names only;
- every boundary table row is honest about current status (doc-only vs proven);
- no runtime, provider, or memory claim without live proof.

Implementation-level (per work order):

- Source Verification Table required for any field cited from a runtime source;
  guessed or "confirm later" fields block closure;
- no `.ts`, `.tsx`, `.js`, `.py` file modified in T1/T2/T3;
- GC-023 file size guard: each spec < 250 lines; split at 200 if needed.

## Claim Boundary

LHW2 is a connector-normalization tranche. It does not claim runtime workflow
enforcement, memory reinjection, tool/MCP/database execution, provider behavior
changes, receipt envelope extensions, external skill ingestion, hosted readiness,
production readiness, or public release readiness.
