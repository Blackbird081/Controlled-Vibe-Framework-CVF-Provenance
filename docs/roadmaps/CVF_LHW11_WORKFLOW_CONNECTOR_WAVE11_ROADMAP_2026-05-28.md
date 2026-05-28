# CVF LHW11 Workflow Connector Wave 11 Roadmap

Memory class: SUMMARY_RECORD

Status: ACTIVE

docType: roadmap

Date: 2026-05-28

---

## Authorization / Decision

Authorized by operator direction on 2026-05-28: continuation of the LHW
connector wave pattern after LHW10 CLOSED_PASS_BOUNDED at commit `f2dc8559`.

Fresh GC-018:
`docs/baselines/CVF_GC018_LHW11_WORKFLOW_CONNECTOR_WAVE11_2026-05-28.md`

Dispatch status: T1 WORK_ORDER_READY. T2 HOLD until T1 CLOSED_PASS.
T3 HOLD until T1 + T2 CLOSED_PASS.

## Scope / Target / Owner Boundary

Target: three second-order documentation connector specs — each binds *outputs
of prior LHW connector specs* into higher-level advisory aggregates.

Owner: CVF session-continuity and roadmap steering surface.

Allowed files per tranche: connector spec (new), work order (new), Fast Lane
audit (new), completion review (new), session continuity update. No
`.ts`/`.tsx`/`.js`/`.py` file. No `EXTENSIONS/` source. No receipt envelope
schema. No public-sync repo.

## Purpose

LHW1-LHW10 produced ~15 named advisory types across 30 connector specs. Each
advisory type answers one specific governance question. But no connector maps
*combinations* of those advisory outputs into a session-level posture or a
workflow-level governance decision.

LHW11 closes that second-order gap:

- T1 — Session Governance Posture Aggregator Connector
- T2 — Spec-Change Governance Decision Connector
- T3 — Memory Context Seed Decay Advisory Connector

## Operator Direction

LHW connector wave rule: bind proven but disconnected surfaces. LHW11 extends
this to second-order: the "surfaces" are themselves prior LHW advisory outputs.
Every cited advisory type is defined in a CLOSED_PASS_BOUNDED spec at HEAD
`d3e01013`.

## Authority Chain

- LHW10 roadmap: `docs/roadmaps/CVF_LHW10_WORKFLOW_CONNECTOR_WAVE10_ROADMAP_2026-05-28.md`
  — Status: CLOSED_PASS_BOUNDED
- LH1 ledger: `docs/reference/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  — Triggers for `Review CVF_5.md`, `CVF_EDIT_ANALYSIS.md`, `tolaria`
- Active session: `CVF_SESSION/ACTIVE_SESSION_STATE.json`

## Knowledge Absorption Blind-Spot Control Block

Control standard:
`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`

Prior connector specs used as input sources (all CLOSED_PASS_BOUNDED):

- `docs/reference/CVF_LHW10_T1_WORKFLOW_TRANSITION_ENFORCEMENT_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
- `docs/reference/CVF_LHW10_T3_PROVIDER_HEALTH_DEGRADATION_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
- `docs/reference/CVF_LHW9_T1_MCP_TOOL_APPROVAL_ADVISORY_CONNECTOR_SPEC_2026-05-28.md`
- `docs/reference/CVF_LHW8_T2_EXECUTION_IDENTITY_AUTHORITY_CHAIN_READOUT_CONNECTOR_SPEC_2026-05-28.md`
- `docs/reference/CVF_LHW8_T1_MEMORY_EVENT_HOOK_GOVERNANCE_SNAPSHOT_CONNECTOR_SPEC_2026-05-28.md`
- `docs/reference/CVF_LHW7_T3_FAILURE_SIM_SPEC_CHANGE_REINTAKE_CONNECTOR_SPEC_2026-05-28.md`
- `docs/reference/CVF_LHW7_T2_PROJECT_MEMORY_CONTEXT_BUDGET_HANDOFF_CONNECTOR_SPEC_2026-05-28.md`

Source families addressed per LH1 ledger triggers:

| Family | LH1 disposition | LH1 remaining trigger | LHW11 tranche |
| --- | --- | --- | --- |
| `Review CVF_5.md` | PARTIALLY_ABSORBED | Reopen when a concrete enforcement owner file is selected | T1, T2 |
| `CVF_EDIT_ANALYSIS.md` | PARTIALLY_ABSORBED | Reopen when selecting next runtime workflow hardening tranche | T2 |
| `tolaria` | PARTIALLY_ABSORBED | Reopen for governed memory snapshot packaging or graph context readout | T3 |

Blind-spot adversarial roles:

- Workflow Architect: aggregated posture must be actionable, not just a
  concatenation of prior outputs.
- Non-Coder Value Reviewer: the aggregate should reduce cognitive load — one
  posture field instead of 15 advisory lookups.
- Governance Auditor: aggregation must not claim more certainty than the
  component advisories provide.
- Integration Maintainer: aggregator fields must be independently derivable
  from prior spec outputs without re-running the source surfaces.

Stop rule: if any tranche requires runtime execution, raw memory reinjection,
MCP transport, external skill ingestion, or provider behavior changes, stop.

Blind-spot verdict: CLEAR.

## Candidate Screen

| Priority | Connector | Input surfaces (all CLOSED_PASS_BOUNDED) | Gap being closed | Disposition |
| --- | --- | --- | --- | --- |
| 1 | Session Governance Posture Aggregator | LHW10-T1 `transitionEnforcementAdvisoryType` (5 values); LHW10-T3 `providerHealthAdvisoryType` (9 values); LHW9-T1 `mcpApprovalAdvisoryType` (6 values); LHW8-T2 `authorityChainAdvisoryType` (4 values) | 10 waves produced ~15 advisory outputs. An Orchestrator reading these individually must evaluate 4+ advisory dimensions manually to decide "what is the overall governance posture of this session?" No connector maps the combination into a single `sessionGovernancePostureType` + `highestRiskAdvisory`. LH1: `Review CVF_5.md` trigger — "concrete enforcement owner file selected." | ACCEPT for T1 |
| 2 | Spec-Change Governance Decision | LHW7-T3 `faultToRespecAdvisoryType` (from failure-sim respec); LHW10-T1 `transitionEnforcementAdvisoryType`; LHW3-T3 `changePacketStatus` (from spec-change workflow packet) | When a failure-sim triggers a spec change AND a workflow transition enforcement advisory is active, no connector maps both into a named `specChangeGovernanceDecision` + `rollbackRecommended` boolean. LH1: `Review CVF_5.md` (code-level enforcement themes) + `CVF_EDIT_ANALYSIS.md` (next hardening tranche). | ACCEPT for T2 |
| 3 | Memory Context Seed Decay Advisory | LHW8-T1 `memorySnapshotAdvisoryType` (5 values); LHW7-T2 `signalsStillMissing` + `contaminationRiskAfterSeed`; AIF-C `MemoryGatewayDecision.decision` | LHW8-T1 gives memory snapshot advisory; LHW7-T2 gives context seed missing signals and contamination risk; AIF-C gives gateway policy outcome. No connector maps these three into a `memoryContextSeedDecayAdvisoryType` + `promotionGateRecommendation` that tells Orchestrator "has the memory context degraded below promotion threshold?" LH1: `tolaria` trigger — "governed memory snapshot packaging or graph context readout." | ACCEPT for T3 |

Rejection log:

- `abtop` runtime observability dashboard — rejected *from this LHW wave*
  (doc-only scope). NOT a permanent block — eligible for live-proof roadmap
  after LHW waves exhausted. API keys available.
- `gridex` database action proof — rejected *from this LHW wave* (doc-only
  scope). NOT a permanent block — eligible for live-proof roadmap post-LHW.
- `Review CVF.md` — rejected: trigger requires "next pack after usage evidence
  or operator demand"; no current usage evidence present.

## Recommended Sequence

### LHW11-T1 — Session Governance Posture Aggregator Connector

Deliverables:

- Connector spec (5 sections) with field mapping:
  LHW10-T1 `transitionEnforcementAdvisoryType` (5 values) ×
  LHW10-T3 `providerHealthAdvisoryType` (9 values) ×
  LHW9-T1 `mcpApprovalAdvisoryType` (6 values) ×
  LHW8-T2 `authorityChainAdvisoryType` (4 values) →
  `sessionGovernancePostureType` + `highestRiskAdvisory` +
  `advisoryCount` + `runtimeExecutionAuthorized=false`
- Explicit statement: "This connector aggregates advisory outputs. It does not
  re-evaluate source surfaces or change their values."
- Boundary table; Source Verification Table with individual rows per enum value
  for all 4 input advisory types

### LHW11-T2 — Spec-Change Governance Decision Connector

Deliverables:

- Connector spec (5 sections) with field mapping:
  LHW7-T3 `faultToRespecAdvisoryType` ×
  LHW10-T1 `transitionEnforcementAdvisoryType` ×
  LHW3-T3 `changePacketStatus` →
  `specChangeGovernanceDecision` + `rollbackRecommended` +
  `runtimeExecutionAuthorized=false`
- Boundary table; Source Verification Table

Dispatch only after T1 is CLOSED_PASS.

### LHW11-T3 — Memory Context Seed Decay Advisory Connector

Deliverables:

- Connector spec (5 sections) with field mapping:
  LHW8-T1 `memorySnapshotAdvisoryType` ×
  LHW7-T2 `signalsStillMissing` + `contaminationRiskAfterSeed` ×
  AIF-C `MemoryGatewayDecision.decision` →
  `memoryContextSeedDecayAdvisoryType` + `promotionGateRecommendation` +
  `canReinject=false` (preserved)
- Boundary table; Source Verification Table

Dispatch only after T1 + T2 are CLOSED_PASS.

## Non-Goals

- Re-evaluation of component advisory surfaces
- Runtime aggregation engine or live dashboard
- Memory reinjection or `canReinject=true`
- New role taxonomy or RBAC change
- Receipt envelope extension
- External skill ingestion or provider behavior changes
- Hosted readiness, production readiness, or public release readiness
- Any tranche beyond T3 without a fresh roadmap and GC-018

## Work Plan

| Tranche | Deliverable | Gate |
| --- | --- | --- |
| T1 | Session Governance Posture Aggregator spec (5 sections) | None — open after GC-018 + dispatch-quality gate |
| T2 | Spec-Change Governance Decision spec (5 sections) | HOLD until T1 CLOSED_PASS |
| T3 | Memory Context Seed Decay Advisory spec (5 sections) | HOLD until T1 + T2 CLOSED_PASS |

## Acceptance Criteria

- [ ] T1 spec: all 4 input advisory types individually row-verified in S5; no
  aggregate rows; `runtimeExecutionAuthorized=false` explicit
- [ ] T2 spec: LHW7-T3/LHW10-T1/LHW3-T3 field names verbatim; `rollbackRecommended` boolean explicit
- [ ] T3 spec: `canReinject=false` preserved; LHW8-T1/LHW7-T2/AIF-C field names verbatim
- [ ] No `.ts`/`.tsx`/`.js`/`.py` file in diff across all three tranches
- [ ] No `EXTENSIONS/` source file in diff
- [ ] Each spec < 250 lines per GC-023
- [ ] Dispatch-quality gate PASS for each work order
- [ ] Session continuity updated after each tranche

## Verification

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base d3e01013 --head <lhw11-commit> --enforce
python governance/compat/check_markdown_structural_completeness.py --base d3e01013 --head <lhw11-commit> --enforce
python governance/compat/check_docs_governance_compat.py --base d3e01013 --head <lhw11-commit> --enforce
```

## Claim Boundary

LHW11 is a second-order connector-normalization wave. It does not claim runtime
aggregation, re-evaluation of component advisories, memory reinjection, MCP
transport, tool execution, CLI invocation, new execution authority, new role
taxonomy, RBAC changes, receipt envelope extensions, external skill ingestion,
provider behavior changes, hosted readiness, production readiness, or public
release readiness.
