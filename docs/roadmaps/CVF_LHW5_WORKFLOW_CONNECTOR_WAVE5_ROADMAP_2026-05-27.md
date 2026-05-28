# CVF LHW5 Workflow Connector Wave 5 Roadmap

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED_AFTER_QUALITY_FIX

docType: roadmap

Date: 2026-05-27

---

## Authorization / Decision

Authorized by operator direction on 2026-05-27: "Tiếp tục roadmap mới, quy tắc
cũ: yêu cầu 'nạp kiến thức từ legacy, hoàn chỉnh thêm các workflow — ưu tiên
flow đã có miếng rời rạc, chỉ còn thiếu chuẩn kết nối' để có giá trị."

LHW4 is CLOSED_PASS_BOUNDED. Session state `nextAllowedMove` confirms: "Any
future connector wave requires a fresh GC-018, roadmap, source-verified work
orders." LHW5 is the direct continuation under those rules.

## Scope / Target / Owner Boundary

Target: three documentation connector specs binding existing proven runtime
pieces into coherent readout and handoff chains.

Owner: CVF session-continuity and roadmap steering surface.

Allowed files per tranche: connector spec (new), work order (status update),
session continuity. No `.ts`/`.tsx`/`.js`/`.py` file. No `EXTENSIONS/`. No
receipt envelope schema. No public-sync repo.

## Purpose

LHW5 closes the fifth legacy workflow connector wave. LHW1–LHW4 established
horizontal connectors (skill → workflow → context), vertical connectors (memory
event loop, recovery packet, tool-approval handoff), output connectors
(failure trend, clarification re-intake, spec-change packet), and governance
connectors (memory snapshot governance, execution authority chain readout,
noncoder friction advisory). LHW5 fills the next tier of gaps where runtime
surfaces (W3 database taxonomy, TA1 approval, LHW4-T2 authority chain, W6
artifact verification, V3 diagnostics, W4 scorecard, WR1 recovery, LHW3-T1
trend) are all proven and closed, but no connector standard ties them into
readable chains for agents and operators:

- T1 — Database Action Boundary Connector
- T2 — Artifact Export Boundary Advisory Connector
- T3 — Failure Simulation Scenario Packet Connector

All three tranches are documentation-only. No source code, runtime module, live
provider route, or provider behavior is changed in LHW5.

## Operator Direction

The operator requested: "Tiếp tục roadmap mới, quy tắc cũ — ưu tiên flow đã
có miếng rời rạc, chỉ còn thiếu chuẩn kết nối."

LHW5 follows this direction by targeting flows where the proven runtime pieces
already exist but no connector standard ties them into a coherent boundary
readout, export advisory, or simulation packet.

## Authority Chain

- LHW4 roadmap: `docs/roadmaps/CVF_LHW4_WORKFLOW_CONNECTOR_WAVE4_ROADMAP_2026-05-27.md`
  — Status: CLOSED_PASS_BOUNDED
- LHW3 roadmap: `docs/roadmaps/CVF_LHW3_WORKFLOW_CONNECTOR_WAVE3_ROADMAP_2026-05-27.md`
  — Status: CLOSED_PASS_BOUNDED
- LH1 ledger: `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  — Remaining triggers for `gridex`, `md2html` + artifact renderer,
    `Failure Simulation cho CVF.md`
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
- `docs/reviews/CVF_W6_NONCODER_ARTIFACT_EXPORT_HARDENING_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_LHW4_T2_EXECUTION_AUTHORITY_CHAIN_READOUT_CONNECTOR_COMPLETION_2026-05-27.md`
- `docs/reviews/CVF_LHW3_T1_OPERATIONAL_FAILURE_TREND_READOUT_CONNECTOR_COMPLETION_2026-05-27.md`
- `docs/reviews/CVF_W4_OPERATIONAL_BENCHMARK_SCORECARD_COMPLETION_2026-05-24.md`
- `docs/reviews/CVF_WR1_WORKFLOW_RECOVERY_STATE_PROOF_COMPLETION_2026-05-25.md`

Source families addressed per LH1 ledger triggers:

| Family | LH1 disposition | LH1 remaining trigger | LHW5 tranche |
| --- | --- | --- | --- |
| `gridex` | PARTIALLY_ABSORBED | Reopen only for read-only database action proof; mutation remains blocked | T1 |
| `md2html` + artifact renderer | PARTIALLY_ABSORBED | Reopen for actual renderer/product export expansion; no new renderer by default | T2 |
| `Failure Simulation cho CVF.md` | PARTIALLY_ABSORBED | Reopen for failure-simulation harness over existing evidence | T3 |

Accepted-source rule: each tranche must read current runtime/canonical source
files first for any field, enum, interface, schema key, or token that already
exists in source. Completion reviews may be used to confirm closure posture or
supporting evidence only. Do not scope from summaries alone.

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
| 1 | Database Action Boundary Connector | W3 `database` surface + `databaseFamily` token, TA1 6 approval states, LHW4-T2 authority chain readout spec | W3 classifies database actions and TA1 approves them, but no connector defines the boundary packet that records what is read-only-allowed vs. blocked with evidence path for Orchestrator before any DB operation | ACCEPT for T1 |
| 2 | Artifact Export Boundary Advisory Connector | W6 artifact verification + `artifactVerification` readout, V3 22 diagnostic classes, LHW3-T1 failure trend readout | W6 verifies artifact shape and V3 diagnoses export failure, but no connector defines the export-boundary advisory packet that tells an agent or non-coder what shapes are acceptable, what V3 class was raised, and what the safe next action is | ACCEPT for T2 |
| 3 | Failure Simulation Scenario Packet Connector | W4 operational benchmark scorecard, V3 diagnostic classes, WR1 recovery readout, LHW3-T1 trend readout | W4 measures failure rates, V3 classifies failure classes, WR1 maps recovery paths — but no connector maps these into reproducible simulation scenario packets that Orchestrator can use for pre-run validation planning | ACCEPT for T3 |

## Recommended Sequence

### LHW5-T1 — Database Action Boundary Connector

Deliverables:

- A connector spec defining the database-action boundary packet standard:
  - field mapping: W3 `surface=database` + `databaseFamily` + `sideEffect` →
    TA1 `approvalState` → LHW4-T2 `dispatchDecision` into a single database
    boundary readout packet
  - boundary packet minimum fields
  - mutation guard: explicit statement that `databaseMutationAuthorized=false`
    is invariant; all write/delete/execute actions are `blocked_by_policy`
    unless a future tranche explicitly lifts this
  - boundary table: doc-only versus runtime-proven rows
- Source Verification Table covering every W3, TA1, and LHW4-T2 field cited.

No `.ts`/`.tsx` or `EXTENSIONS/` file modified.

### LHW5-T2 — Artifact Export Boundary Advisory Connector

Deliverables:

- A connector spec binding W6 artifact verification shape → V3 diagnostic
  class → LHW3-T1 failure trend signal into a single export-boundary advisory
  packet:
  - field mapping: W6 `artifactVerification.status` + `verificationClass` →
    V3 `diagnosticClass` export-related values → LHW3-T1 trend signal where
    applicable → advisory type and plain-language message
  - advisory packet minimum fields
  - explicit statement: "This connector does not block artifact export. It
    produces an advisory record only."
  - boundary table: doc-only versus runtime-proven rows
- Source Verification Table covering every W6, V3, and LHW3-T1 field cited.

Dispatch only after T1 is CLOSED_PASS.

### LHW5-T3 — Failure Simulation Scenario Packet Connector

Deliverables:

- A connector spec mapping W4 scorecard failure signals + V3 diagnostic
  classes + WR1 recovery actions + LHW3-T1 trend labels into reproducible
  simulation scenario packets:
  - scenario mapping table: which W4 metric threshold direction + V3 class +
    WR1 recovery action combination produces which scenario type
    (provider_failure, policy_block, overconstraint, recovery_gap,
    output_drift)
  - scenario packet minimum fields: `scenarioId`, `scenarioType`,
    `triggerMetric`, `v3DiagnosticClass`, `wr1RecoveryAction`,
    `thresholdDirection`, `thresholdCriterion`, `simulationSteps`,
    `expectedOutcome`, `boundaryStatement`
  - explicit statement: "Scenario packets are planning records for Orchestrator
    pre-run validation. They do not execute simulations or change runtime state."
  - boundary table: doc-only versus runtime-proven rows
- Source Verification Table covering every W4, V3, WR1, and LHW3-T1 field
  cited.

Dispatch only after T1 + T2 are CLOSED_PASS.

## Non-Goals

- Runtime enforcement of any connector binding
- Database query execution, mutation, or export
- New artifact renderer or export pipeline
- Live failure simulation execution
- Extension of W3, TA1, W6, V3, W4, or WR1 runtime behavior
- New memory tiers, raw memory reinjection, or `canReinject=true`
- Receipt envelope schema changes
- External skill ingestion or Candidate 7 ingestion
- Provider behavior changes
- Hosted readiness, production readiness, or public release readiness
- Any tranche beyond T3 without a fresh roadmap and GC-018

## Work Plan

| Tranche | Deliverable | Gate |
| --- | --- | --- |
| T1 | Database Action Boundary Connector spec (5 sections) | None — open |
| T2 | Artifact Export Boundary Advisory Connector spec (5 sections) | T1 CLOSED_PASS |
| T3 | Failure Simulation Scenario Packet Connector spec (5 sections) | T1 + T2 CLOSED_PASS |

Each tranche: Fast Lane audit → work order → spec → completion review → session
continuity update → commit.

## Acceptance Criteria

- [x] T1 spec created; W3/TA1/LHW4-T2 field names used verbatim;
  `databaseMutationAuthorized=false` explicit; Source Verification Table complete
- [x] T2 spec created; W6/V3/LHW3-T1 field names used verbatim; advisory-only
  (no blocking) explicit; boundary table honest
- [x] T3 spec created; W4/V3/WR1/LHW3-T1 field names used verbatim;
  simulation-planning-only (no execution) explicit; LHW5 roadmap updated to
  `CLOSED_PASS_BOUNDED_AFTER_QUALITY_FIX`
- [x] No `.ts`/`.tsx`/`.js`/`.py` file in diff across all three tranches
- [x] Session continuity updated after each tranche

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

LHW5 is a connector-normalization tranche. It does not claim database mutation
execution, artifact renderer creation, live failure simulation, new execution
authority, new role taxonomy, RBAC changes, memory reinjection, tool/MCP
execution, provider behavior changes, receipt envelope extensions, external
skill ingestion, hosted readiness, production readiness, or public release
readiness.
