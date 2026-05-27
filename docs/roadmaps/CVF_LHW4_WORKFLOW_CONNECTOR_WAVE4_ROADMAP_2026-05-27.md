# CVF LHW4 Workflow Connector Wave 4 Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: roadmap

Date: 2026-05-27

---

## Authorization / Decision

Authorized by operator direction on 2026-05-27: "Tiếp tục roadmap mới, quy tắc
cũ: yêu cầu 'nạp kiến thức từ legacy, hoàn chỉnh thêm các workflow — ưu tiên
flow đã có miếng rời rạc, chỉ còn thiếu chuẩn kết nối' để có giá trị."

LHW3 is CLOSED_PASS_BOUNDED. Session state `nextAllowedMove` confirms:
"Next legacy workflow connector work requires fresh GC-018, roadmap, source-
verified work orders, and Knowledge Absorption Blind-Spot Control before
implementation." LHW4 is the direct continuation under those rules.

## Scope / Target / Owner Boundary

Target: three documentation connector specs binding existing proven runtime
pieces into coherent readout and handoff chains.

Owner: CVF session-continuity and roadmap steering surface.

Allowed files per tranche: connector spec (new), work order (status update),
session continuity. No `.ts`/`.tsx`/`.js`/`.py` file. No `EXTENSIONS/`. No
receipt envelope schema. No public-sync repo.

## Purpose

LHW4 closes the fourth legacy workflow connector wave. LHW1–LHW3 established
horizontal connectors (skill → workflow → context), vertical connectors (memory
event loop, recovery packet, tool-approval handoff), and output connectors
(failure trend, clarification re-intake, spec-change packet). LHW4 fills the
next tier of gaps where runtime surfaces (AIF-B graph, AIF-C memory gateway,
M1 durable memory, G1 execution identity, W3 taxonomy, W4 scorecard, CB1
shaping, C8 selection) are all proven and closed, but no connector standard
ties them into a readable chain for agents and operators:

- T1 — Memory Snapshot Governance Connector
- T2 — Execution Authority Chain Readout Connector
- T3 — Noncoder Friction Advisory Packet Connector

All three tranches are documentation-only. No source code, runtime module, live
provider route, or provider behavior is changed in LHW4.

## Operator Direction

The operator requested: "Tiếp tục roadmap mới, quy tắc cũ — ưu tiên flow đã
có miếng rời rạc, chỉ còn thiếu chuẩn kết nối."

LHW4 follows this direction by targeting flows where the proven runtime pieces
already exist but no connector standard ties them into a coherent handoff or
advisory readout.

## Authority Chain

- LHW3 roadmap: `docs/roadmaps/CVF_LHW3_WORKFLOW_CONNECTOR_WAVE3_ROADMAP_2026-05-27.md`
  — Status: CLOSED_PASS_BOUNDED
- LHW2 roadmap: `docs/roadmaps/CVF_LHW2_WORKFLOW_CONNECTOR_COMPLETION_ROADMAP_2026-05-27.md`
  — Status: CLOSED_PASS_BOUNDED_AFTER_CLEANUP
- LH1 ledger: `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  — Remaining triggers for `tolaria`, `Claude Kit`, `AI-first vs Human-first`
- Active session: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
  — nextAllowedMove: "Next legacy workflow connector work requires fresh GC-018,
    roadmap, source-verified work orders, and Knowledge Absorption Blind-Spot
    Control before implementation"

## Knowledge Absorption Blind-Spot Control Block

Control standard:
`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`

Scope sources resolved before this roadmap:

- `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
- `docs/reviews/CVF_AIF_B_GRAPH_KNOWLEDGE_PHASE1_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_AIF_C_MEMORY_GATEWAY_PHASE2_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_M1_DURABLE_CROSS_SESSION_MEMORY_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_G1_EXECUTION_IDENTITY_RUNTIME_GATE_COMPLETION_2026-05-22.md`
- `docs/reviews/CVF_W3_TOOL_MCP_DATABASE_ACTION_TAXONOMY_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_W4_OPERATIONAL_BENCHMARK_SCORECARD_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_CB1_CONTEXT_BUDGET_REQUEST_SHAPING_READOUT_COMPLETION_2026-05-25.md`
- `docs/reviews/CVF_LHW3_T1_OPERATIONAL_FAILURE_TREND_READOUT_CONNECTOR_COMPLETION_2026-05-27.md`

Source families addressed per LH1 ledger triggers:

| Family | LH1 disposition | LH1 remaining trigger | LHW4 tranche |
| --- | --- | --- | --- |
| `tolaria` | PARTIALLY_ABSORBED | Reopen for governed memory snapshot packaging or graph context readout; no reinjection | T1 |
| `Claude Kit` | PARTIALLY_ABSORBED | Reopen only for a concrete identity/runtime authority gap, not another role catalog | T2 |
| `AI-first vs Human-first` | PARTIALLY_ABSORBED | Reopen for noncoder friction scoring or anti-overconstraint UX | T3 |

Accepted-source rule: each tranche reads the detailed legacy source files for
its family before implementation. Do not scope from summaries alone.

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
new source family is opened without a ledger trigger; Candidate 7 remains
demand-gated; no runtime, provider, or memory reinjection surface is claimed
in T1/T2/T3.

## Candidate Screen

| Priority | Connector | Existing runtime pieces | Gap being closed | Disposition |
| --- | --- | --- | --- | --- |
| 1 | Memory Snapshot Governance | AIF-B graph schema, AIF-C memory gateway, M1 durable memory, VI3 capture record, H2 hierarchy | All memory surfaces exist and are proven; no connector defines the governed snapshot package — what to include, what boundary rules apply, what the receipt looks like when a snapshot is taken | ACCEPT for T1 |
| 2 | Execution Authority Chain Readout | G1 execution identity, W3 tool taxonomy, TA1 approval readout, MA1 transfer packet | G1 resolves actorId/role/boundary; W3 classifies tool actions; TA1 maps approval state — but no connector ties these into a single authority-chain readout packet that an Orchestrator can read to understand who can do what before dispatching | ACCEPT for T2 |
| 3 | Noncoder Friction Advisory Packet | W4 scorecard, CB1 request shaping, LHW3-T1 trend readout, C8 no-match, AI-first vs Human-first | LHW3-T1 maps failure trends; CB1 identifies missing signals — but no connector defines the advisory packet a non-coder receives when constraints are too tight or the request is unresolvable, with plain-language next actions | ACCEPT for T3 |

## Recommended Sequence

### LHW4-T1 — Memory Snapshot Governance Connector

Deliverables:

- A connector spec defining the governed memory snapshot package standard:
  - what surfaces contribute to a snapshot: AIF-B graph index, AIF-C gateway
    retrieval result, M1 durable tiers, VI3 capture record
  - boundary rules: which tiers are includable vs. blocked
    (`canReinject=false` preserved; rawMemoryReleased=false preserved)
  - receipt shape: what fields a snapshot receipt must contain (evidence path,
    tier list, captureDecision, boundary flags)
  - boundary table: doc-only versus runtime-proven rows
- Source Verification Table covering every AIF-B, AIF-C, M1, and VI3 field
  cited.

No `.ts`/`.tsx` or `EXTENSIONS/` file modified.

### LHW4-T2 — Execution Authority Chain Readout Connector

Deliverables:

- A connector spec binding G1 execution identity fields → W3 tool action
  taxonomy → TA1 approval state → MA1 role assignment into a single authority-
  chain readout packet:
  - field mapping: G1 actorId/cvfRole/executionBoundary → W3 actionCategory →
    TA1 approvalState → MA1 ##4 Role Assignment
  - authority chain packet minimum fields
  - dissent path: what happens when G1 denies an actor and TA1 reports
    `blocked_by_policy` — how the packet signals stop condition to Orchestrator
  - boundary table: doc-only versus runtime-proven rows
- Source Verification Table covering every G1, W3, TA1, and MA1 field cited.

Dispatch only after T1 is CLOSED_PASS.

### LHW4-T3 — Noncoder Friction Advisory Packet Connector

Deliverables:

- A connector spec turning LHW3-T1 overconstraint/underspecification trend
  signals and CB1 advisory readout into a plain-language friction advisory
  packet for non-coders:
  - signal-to-advisory table: which LHW3-T1 trend signal + CB1 nextAction
    combination triggers which advisory type (overconstraint, missing-context,
    no-match, instability)
  - advisory packet minimum fields: plain-language message, signal source,
    recommended next step (in operator language, not technical terms)
  - explicit statement: "This connector does not block workflow execution. It
    produces an advisory record only."
  - boundary table: doc-only versus runtime-proven rows
- Source Verification Table covering every LHW3-T1 signal token and CB1
  field cited.

Dispatch only after T1 + T2 are CLOSED_PASS.

## Non-Goals

- Runtime enforcement of any connector binding
- Extension of AIF-B, AIF-C, M1, G1, W3, W4, CB1, or VI3 runtime behavior
- New memory tiers, raw memory reinjection, or `canReinject=true`
- Live memory snapshot execution or automated snapshot scheduling
- New role taxonomy or RBAC change
- Receipt envelope schema changes
- External skill ingestion or Candidate 7 ingestion
- Provider behavior changes
- Hosted readiness, production readiness, or public release readiness
- Any tranche beyond T3 without a fresh roadmap and GC-018

## Work Plan

| Tranche | Deliverable | Gate |
| --- | --- | --- |
| T1 | Memory Snapshot Governance Connector spec (5 sections) | None — open |
| T2 | Execution Authority Chain Readout Connector spec (5 sections) | T1 CLOSED_PASS |
| T3 | Noncoder Friction Advisory Packet Connector spec (5 sections) | T1 + T2 CLOSED_PASS |

Each tranche: Fast Lane audit → work order → spec → completion review → session
continuity update → commit.

## Acceptance Criteria

- [ ] T1 spec created; AIF-B/AIF-C/M1/VI3 field names used verbatim;
  `canReinject=false` and `rawMemoryReleased=false` explicit; Source
  Verification Table complete
- [ ] T2 spec created; G1/W3/TA1/MA1 field names used verbatim; authority
  chain packet minimum fields present; boundary table honest
- [ ] T3 spec created; LHW3-T1 signal tokens and CB1 field names used verbatim;
  plain-language advisory fields present; advisory-only (no blocking) explicit;
  LHW4 roadmap updated to `CLOSED_PASS_BOUNDED`
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

LHW4 is a connector-normalization tranche. It does not claim live memory
snapshot execution, automated snapshot scheduling, new execution authority,
new role taxonomy, RBAC changes, memory reinjection, tool/MCP/database
execution, provider behavior changes, receipt envelope extensions, external
skill ingestion, hosted readiness, production readiness, or public release
readiness.
