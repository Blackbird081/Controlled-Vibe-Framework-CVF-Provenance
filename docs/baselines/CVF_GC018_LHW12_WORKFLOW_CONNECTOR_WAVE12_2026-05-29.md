# CVF GC-018 — LHW12 Workflow Connector Wave 12

Memory class: FULL_RECORD

Status: ACTIVE

docType: gc018_baseline

Date: 2026-05-29

---

## Purpose

Authorize LHW12 Workflow Connector Wave 12: three documentation-only connector
specs addressing product-layer gaps identified in CVF 25.05 Gop_y.md and
CVF 28.05 prototype audit. LHW12 closes the posture-to-model tier advisory,
outcome pack taxonomy grouping advisory, and async worker lifecycle boundary —
all doc-only connector gaps where multiple proven surfaces exist but no
connector normalizes them.

---

## Scope

Three documentation-only connector specs:

- T1 — Posture-to-Model Tier Advisory Connector
- T2 — Outcome Pack Taxonomy Grouping Connector
- T3 — Async Worker Lifecycle Boundary Connector

No `.ts` / `.tsx` / `.js` / `.py` file change. No `EXTENSIONS/` source file
change. No receipt envelope schema change. No public-sync repo change. No MCP
transport, tool execution, CLI invocation, memory reinjection, new role
taxonomy, or RBAC change.

---

## Source / Predecessor Evidence

- LHW11 GC-018:
  `docs/baselines/CVF_GC018_LHW11_WORKFLOW_CONNECTOR_WAVE11_2026-05-28.md`
  — Status: ACTIVE; LHW11 CLOSED_PASS_BOUNDED
- LHW11 roadmap:
  `docs/roadmaps/CVF_LHW11_WORKFLOW_CONNECTOR_WAVE11_ROADMAP_2026-05-28.md`
  — Status: CLOSED_PASS_BOUNDED
- CVF 25.05 Gop_y.md review:
  `.private_reference/legacy/CVF 25.05/CLAUDE_REVIEW_OF_GOP_Y_2026-05-25.md`
  — GAP 2 (Outcome Pack Taxonomy), GAP 7 (Async Worker Lifecycle),
    GAP 5 (Operations Cockpit — partially addressed)
- CVF 28.05 prototype gap record:
  `docs/baselines/CVF_GC018_LHW11_WORKFLOW_CONNECTOR_WAVE11_2026-05-28.md`
  — Section "New Source Family: CVF 28.05" — Gap A (posture tier config)
- Active session: `CVF_SESSION/ACTIVE_SESSION_STATE.json`

Source surfaces confirmed at HEAD `7de75901`:

| Surface | File | Key symbol |
| --- | --- | --- |
| LHW11-T1 `sessionGovernancePostureType` | `docs/reference/CVF_LHW11_T1_SESSION_GOVERNANCE_POSTURE_AGGREGATOR_CONNECTOR_SPEC_2026-05-28.md` | `posture_clear`, `posture_hold`, `posture_blocked` |
| LHW11-T1 `highestRiskAdvisory` | same | S3 field |
| CB1 `RouteRequestContextBudgetTier` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts` | line 6: `minimal`, `standard`, `expanded` |
| G1 `CVFRole` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-identity.ts` | line 1 import from `cvf-guard-contract` |
| Skill pack registry (10 entries) | `governance/registries/cvf-certified-skill-pack-registry.json` | fields: `id`, `domain`, `riskLevel`, `outcomeKey` |
| LH1 `deepagents` trigger | `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md` | line 156: "bounded worker delegation proof" |
| WR1 `WorkflowRecoveryAction` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflows/workflow-resolver.ts` | line 50–54 |
| MA1 role lanes | `docs/reference/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | section `## 4. Role Assignment` |

---

## Decision / Baseline

LHW12 is authorized. Each tranche is documentation-only, binds surfaces already
CLOSED_PASS_BOUNDED in HEAD, adds no runtime authority, and extends no receipt
envelope schema.

T2 is gated as `HOLD_UNTIL_T1_PASS`. T3 is gated as
`HOLD_UNTIL_T1_AND_T2_PASS`.

The blocked-work-class list in `ACTIVE_SESSION_STATE.json` remains in force.
LHW12 does NOT implement posture-based model routing in runtime. The connector
is advisory only — `modelTierAdvisoryType` is a governance planning record,
not a dispatch instruction.

## LHW Rejection Language Rule

When writing a rejection log entry: "rejected *from this LHW wave* (doc-only
scope)" — never bare "rejected." `abtop` and `gridex` remain eligible for
live-proof roadmap after LHW waves exhausted.

---

## Required Evidence

Per tranche before CLOSED_PASS_BOUNDED: connector spec (5 sections S1–S5);
Fast Lane audit; work order with Source Verification Table (full paths, no
`same` shorthand, individual rows per enum value); completion review with all
required sections; both governance gates PASS; no code file in diff; spec
< 250 lines per GC-023; session continuity updated.

---

## Verification

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 7de75901 --head <lhw12-commit> --enforce
python governance/compat/check_markdown_structural_completeness.py --base 7de75901 --head <lhw12-commit> --enforce
python governance/compat/check_docs_governance_compat.py --base 7de75901 --head <lhw12-commit> --enforce
```

---

## Claim Boundary

LHW12 does not claim posture-based runtime model routing, outcome pack
execution, subagent spawning, worker lifecycle enforcement, MCP transport,
tool execution, CLI invocation, memory reinjection, new role taxonomy, RBAC
changes, receipt envelope extensions, external skill ingestion, provider
behavior changes, hosted readiness, production readiness, or public release
readiness.
