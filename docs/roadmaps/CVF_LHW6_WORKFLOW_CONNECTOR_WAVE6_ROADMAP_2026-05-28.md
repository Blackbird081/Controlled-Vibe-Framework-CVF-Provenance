# CVF LHW6 Workflow Connector Wave 6 Roadmap

Memory class: FULL_RECORD

Status: DISPATCHED

docType: roadmap

Date: 2026-05-28

---

## Authorization / Decision

Authorized by operator direction on 2026-05-28: "Tiếp tục roadmap mới, quy tắc
cũ: yêu cầu 'nạp kiến thức từ legacy, hoàn chỉnh thêm các workflow — ưu tiên
flow đã có miếng rời rạc, chỉ còn thiếu chuẩn kết nối' để có giá trị."

LHW5 is CLOSED_PASS_BOUNDED_AFTER_QUALITY_FIX. Session state `nextAllowedMove`
confirms: "Any future connector wave requires a fresh GC-018, roadmap, and
source-verified work orders." LHW6 is the direct continuation under those rules.

## Scope / Target / Owner Boundary

Target: three documentation connector specs binding existing proven runtime
pieces into coherent readout and handoff chains.

Owner: CVF session-continuity and roadmap steering surface.

Allowed files per tranche: connector spec (new), work order (status update),
session continuity. No `.ts`/`.tsx`/`.js`/`.py` file. No `EXTENSIONS/`. No
receipt envelope schema. No public-sync repo.

## Purpose

LHW6 closes the sixth legacy workflow connector wave. LHW1–LHW5 established
horizontal connectors (skill → workflow → context), vertical connectors (memory
event loop, recovery packet, tool-approval handoff), output connectors
(failure trend, clarification re-intake, spec-change packet), governance
connectors (memory snapshot, execution authority chain, noncoder friction
advisory), and boundary connectors (database action boundary, artifact export
advisory, failure simulation scenario packet). LHW6 fills the next tier of gaps
where runtime surfaces (W3 local_tool/command_runtime surfaces, TA1 approval,
LHW4-T2 authority chain, M1 durable tiers, WR1 recovery, AIF-C gateway,
LHW4-T1 memory snapshot) are all proven and closed, but no connector standard
ties them into readable tool-bridge, CLI-onboarding, or project-memory chains:

- T1 — Tool Runtime Bridge Advisory Connector
- T2 — CLI Tool Onboarding Governance Connector
- T3 — Project Memory Readout Connector

All three tranches are documentation-only. No source code, runtime module, live
provider route, or provider behavior is changed in LHW6.

## Operator Direction

The operator requested: "Tiếp tục roadmap mới, quy tắc cũ — ưu tiên flow đã
có miếng rời rạc, chỉ còn thiếu chuẩn kết nối."

LHW6 follows this direction by targeting flows where the proven runtime pieces
already exist but no connector standard ties them into a tool bridge advisory,
CLI onboarding packet, or project-memory summary for Orchestrator.

## Authority Chain

- LHW5 roadmap: `docs/roadmaps/CVF_LHW5_WORKFLOW_CONNECTOR_WAVE5_ROADMAP_2026-05-27.md`
  — Status: CLOSED_PASS_BOUNDED_AFTER_QUALITY_FIX
- LHW4 roadmap: `docs/roadmaps/CVF_LHW4_WORKFLOW_CONNECTOR_WAVE4_ROADMAP_2026-05-27.md`
  — Status: CLOSED_PASS_BOUNDED
- LH1 ledger: `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  — Remaining triggers for `OpenAgentd`, `CLI-Anything`, `Review CVF_1.md`
- Active session: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
  — nextAllowedMove: "Any future connector wave requires a fresh GC-018,
    roadmap, and source-verified work orders."

## Knowledge Absorption Blind-Spot Control Block

Control standard:
`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`

Scope sources resolved before this roadmap:

- `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- `docs/reviews/CVF_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_TA1_TOOL_ACTION_APPROVAL_READOUT_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_LHW4_T2_EXECUTION_AUTHORITY_CHAIN_READOUT_CONNECTOR_COMPLETION_2026-05-27.md`
- `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_WR1_WORKFLOW_RECOVERY_STATE_PROOF_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_AIF_C_MEMORY_GATEWAY_PHASE2_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_LHW4_T1_MEMORY_SNAPSHOT_GOVERNANCE_CONNECTOR_COMPLETION_2026-05-27.md`

Source families addressed per LH1 ledger triggers:

| Family | LH1 disposition | LH1 remaining trigger | LHW6 tranche |
| --- | --- | --- | --- |
| `OpenAgentd` | PARTIALLY_ABSORBED | Reopen only for read-only tool runtime bridge design; execution remains blocked | T1 |
| `CLI-Anything` | PARTIALLY_ABSORBED | Reopen for CLI tool onboarding only after action governance proof | T2 |
| `Review CVF_1.md` | PARTIALLY_ABSORBED | Reopen for project memory readout or workflow recovery proof | T3 |

Accepted-source rule: each tranche must read current runtime/canonical source
files first for any field, enum, interface, schema key, or token that already
exists in source. Completion reviews may be used to confirm closure posture
only. Do not scope from summaries alone.

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

Basis: all scope sources exist; LH1 ledger triggers are named per family; no
new source family is opened without a ledger trigger; no runtime, provider,
or memory reinjection surface is claimed in T1/T2/T3.

## Candidate Screen

| Priority | Connector | Existing runtime pieces | Gap being closed | Disposition |
| --- | --- | --- | --- | --- |
| 1 | Tool Runtime Bridge Advisory Connector | W3 `local_tool`/`command_runtime` surface tokens + sideEffect, TA1 6 approval states, LHW4-T2 authority chain readout | W3 classifies local/command tool actions and TA1 approves them, but no connector defines the tool-bridge advisory packet that records what is read-only-bridgeable vs. blocked for Orchestrator before dispatching a tool call to any non-MCP runtime surface | ACCEPT for T1 |
| 2 | CLI Tool Onboarding Governance Connector | W3 `command_runtime` surface, TA1 approval states, LHW4-T2 authority chain, LHW6-T1 tool bridge advisory | W3 classifies CLI commands; TA1 reports approval state — but no connector defines the CLI onboarding packet that packages first-use governance classification, approval gate state, and boundary advisory into a single Orchestrator-readable onboarding record | ACCEPT for T2 |
| 3 | Project Memory Readout Connector | M1 durable tiers `skill`/`long-term`, WR1 `lastRestorableCheckpoint`, AIF-C `MemoryGatewayDecision.memoryIdsAffected`, LHW4-T1 snapshot receipt | M1 holds durable state, WR1 has the last restorable checkpoint, AIF-C has the memory gateway decision — but no connector defines the project-memory readout packet that ties these into a single project-state summary an Orchestrator can read before resuming a session or workflow | ACCEPT for T3 |

## Recommended Sequence

### LHW6-T1 — Tool Runtime Bridge Advisory Connector

Deliverables:

- A connector spec defining the tool-runtime bridge advisory packet:
  - field mapping: W3 `surface` (`local_tool` or `command_runtime`) +
    `sideEffect` + optional `transport` → TA1 `approvalState` →
    LHW4-T2 `dispatchDecision` → advisory type
  - explicit statement: "This connector does not execute tool calls. The
    advisory packet is a non-blocking governance record."
  - boundary table: doc-only versus runtime-proven rows
- Source Verification Table covering every W3, TA1, and LHW4-T2 field cited.

No `.ts`/`.tsx` or `EXTENSIONS/` file modified.

### LHW6-T2 — CLI Tool Onboarding Governance Connector

Deliverables:

- A connector spec defining the CLI tool onboarding packet:
  - field mapping: W3 `surface=command_runtime` + `sideEffect` →
    TA1 `approvalState` → LHW6-T1 bridge advisory type → onboarding
    classification and plain-language guidance
  - explicit statement: "This connector does not execute CLI commands.
    The onboarding packet is a governance planning record."
  - boundary table: doc-only versus runtime-proven rows
- Source Verification Table covering every W3, TA1, and LHW6-T1 field cited.

Dispatch only after T1 is CLOSED_PASS.

### LHW6-T3 — Project Memory Readout Connector

Deliverables:

- A connector spec tying M1 durable tier state + WR1 recovery checkpoint +
  AIF-C gateway decision into a project-memory readout packet:
  - field mapping: M1 `includedTiers` + `DurableMemoryReceipt.summaryOnly` →
    WR1 `lastRestorableCheckpoint` + `recoveryAction` → AIF-C
    `MemoryGatewayDecision.memoryIdsAffected` + `canReinject` →
    readout packet fields
  - `canReinject=false` and `rawMemoryReleased=false` preserved explicitly
  - boundary table: doc-only versus runtime-proven rows
  - LHW4-T1 snapshot receipt as the evidence anchor
- Source Verification Table covering every M1, WR1, and AIF-C field cited.

Dispatch only after T1 + T2 are CLOSED_PASS.

## Non-Goals

- Runtime tool execution, command bridging, or CLI invocation
- New memory tiers, raw memory reinjection, or `canReinject=true`
- Extension of W3, TA1, M1, WR1, or AIF-C runtime behavior
- New role taxonomy or RBAC change
- Receipt envelope schema changes
- External skill ingestion or Candidate 7 ingestion
- Provider behavior changes
- Hosted readiness, production readiness, or public release readiness
- Any tranche beyond T3 without a fresh roadmap and GC-018

## Work Plan

| Tranche | Deliverable | Gate |
| --- | --- | --- |
| T1 | Tool Runtime Bridge Advisory Connector spec (5 sections) | None — open |
| T2 | CLI Tool Onboarding Governance Connector spec (5 sections) | T1 CLOSED_PASS |
| T3 | Project Memory Readout Connector spec (5 sections) | T1 + T2 CLOSED_PASS |

Each tranche: Fast Lane audit → work order → spec → completion review → session
continuity update → commit.

## Acceptance Criteria

- [ ] T1 spec created; W3/TA1/LHW4-T2 field names used verbatim;
  tool-execution-blocked explicit; Source Verification Table complete
- [ ] T2 spec created; W3/TA1/LHW6-T1 field names used verbatim; CLI
  onboarding planning-only explicit; boundary table honest
- [ ] T3 spec created; M1/WR1/AIF-C field names used verbatim;
  `canReinject=false` and `rawMemoryReleased=false` explicit; LHW6 roadmap
  updated to `CLOSED_PASS_BOUNDED`
- [ ] No `.ts`/`.tsx`/`.js`/`.py` file in diff across all three tranches
- [ ] Session continuity updated after each tranche

## Verification

Roadmap-level:

- source files cited and LH1 triggers mapped per family;
- connector specs use existing CVF field names only;
- every boundary table row is honest about current status (doc-only vs proven);
- no runtime, provider, or memory claim without live proof.

Implementation-level (per work order):

- Source Verification Table required for any field cited from a runtime source;
  guessed or "confirm later" fields block closure;
- no `.ts`, `.tsx`, `.js`, `.py` file modified in T1/T2/T3;
- GC-023 file size guard: each spec < 250 lines; split at 200 if needed.

## Claim Boundary

LHW6 is a connector-normalization tranche. It does not claim tool execution,
CLI invocation, memory reinjection, new execution authority, new role taxonomy,
RBAC changes, receipt envelope extensions, external skill ingestion, provider
behavior changes, hosted readiness, production readiness, or public release
readiness.
