# CVF GC-018 — LHW11 Workflow Connector Wave 11

Memory class: FULL_RECORD

Status: ACTIVE

docType: gc018_baseline

Date: 2026-05-28

---

## Purpose

Authorize LHW11 Workflow Connector Wave 11: three documentation-only connector
specs that perform second-order binding — connecting *outputs of prior LHW
connector specs* into higher-level advisory aggregates. LHW1-LHW10 produced
~15 named advisory types; LHW11 maps combinations of those advisory outputs
into coherent session-level and workflow-level governance records.

---

## Scope

Three documentation-only connector specs:

- T1 — Session Governance Posture Aggregator Connector
- T2 — Spec-Change Governance Decision Connector
- T3 — Memory Context Seed Decay Advisory Connector

No `.ts` / `.tsx` / `.js` / `.py` file change. No `EXTENSIONS/` source file
change. No receipt envelope schema change. No public-sync repo change. No MCP
transport, tool execution, CLI invocation, memory reinjection, new role
taxonomy, or RBAC change.

---

## Source / Predecessor Evidence

- LHW10 GC-018:
  `docs/baselines/CVF_GC018_LHW10_WORKFLOW_CONNECTOR_WAVE10_2026-05-28.md`
  — Status: ACTIVE; LHW10 CLOSED_PASS_BOUNDED
- LHW10 roadmap:
  `docs/roadmaps/CVF_LHW10_WORKFLOW_CONNECTOR_WAVE10_ROADMAP_2026-05-28.md`
  — Status: CLOSED_PASS_BOUNDED
- LH1 ledger:
  `docs/reference/archive/CVF_LEGACY_HARVEST_CLOSEOUT_LEDGER_2026-05-25.md`
  — Remaining triggers for `Review CVF_5.md`, `CVF_EDIT_ANALYSIS.md`,
    `tolaria`
- Active session: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
  — `nextAllowedMove` names LHW10 as latest CLOSED_PASS_BOUNDED

Prior LHW connector outputs used as inputs (all CLOSED_PASS_BOUNDED at HEAD
`d3e01013`):

| Source surface | Contract version | Key output field used |
| --- | --- | --- |
| LHW10-T1 | `cvf.workflowTransitionEnforcementAdvisory.lhw10.t1.v1` | `transitionEnforcementAdvisoryType` |
| LHW10-T3 | `cvf.providerHealthDegradationAdvisory.lhw10.t3.v1` | `providerHealthAdvisoryType` |
| LHW9-T1 | `cvf.mcpToolApprovalAdvisory.lhw9.t1.v1` | `mcpApprovalAdvisoryType` |
| LHW8-T2 | `cvf.executionIdentityAuthorityChainReadout.lhw8.t2.v1` | `authorityChainAdvisoryType` |
| LHW7-T3 | `cvf.failureSimSpecChangeReIntake.lhw7.t3.v1` | `faultToRespecAdvisoryType` |
| LHW7-T2 | `cvf.projectMemoryContextBudgetHandoff.lhw7.t2.v1` | `signalsStillMissing`, `contaminationRiskAfterSeed` |
| LHW8-T1 | `cvf.memoryEventHookGovernanceSnapshot.lhw8.t1.v1` | `memorySnapshotAdvisoryType` |
| AIF-C `MemoryGatewayDecision` | Runtime-proven | `decision`, `canReinject=false` |

---

## Decision / Baseline

LHW11 is authorized. Each tranche is documentation-only, binds surfaces already
CLOSED_PASS_BOUNDED in HEAD, adds no runtime authority, and extends no receipt
envelope schema.

T2 is gated on T1 CLOSED_PASS. T3 is gated on T1 + T2 CLOSED_PASS.

The blocked-work-class list in `ACTIVE_SESSION_STATE.json` remains in force.

## New Source Family: CVF 28.05 (added 2026-05-29)

`.private_reference/legacy/CVF 28.05/` — 5 files added by operator 2026-05-29.

**Disposition: PARTIALLY_ABSORBED** (new family, not yet in LH1 ledger)

**Files:** `CLI & MCP.md`, `CVF Multi-Agent Visual Flowchart.md`, `cvf_cli.py`,
`test_result.md`, `vibe-posture.config.json`

**What it is:** A runnable prototype (Python CLI) demonstrating a 5-stage CVF
pipeline — Intake Gate → Orchestrator → Workers → Reviewer → Closure Gate —
with 3 posture tiers (Eco/Balanced/Premium), per-role model assignment, and
exception handling (WorkerTimeoutException, ReviewDeadlockException,
IntakePolicyViolation).

**Operator context:** Written to explore cost optimization through model mixing
(different models per role) and to prove the pipeline chain works end-to-end.

**What CVF already has (absorbed or partial):**
- Provider routing by risk level (R0-R3) — `provider-router-adapter.ts`
- Context budget readout (CB1 `budgetTier`, `readiness`) — advisory only
- W5 provider fallback posture — advisory only
- G1 role gate per request — not dynamic assignment
- MA1 multi-agent transfer packet — document standard, not execution binding

**What CVF does NOT have (confirmed by grep 2026-05-29):**
- `vibe-posture` config: posture tier → per-role model assignment — **absent**
- `ReviewDeadlockException`: retry counter + deadlock detection + escalation — **absent**
- `WorkerTimeoutException`: timeout → sandbox restart → re-dispatch loop — **absent**
- `IntakePolicyViolation`: hard chain stop (CVF returns BLOCK but does not stop chain) — **partial**
- Sequential pipeline chain dispatching: the 5 surfaces exist separately but nothing chains them — **absent**

**4 remaining triggers for future wave:**

1. **`vibe-posture` tier config** — map posture tier (E/B/O) × role → model
   assignment → CVF execution boundary. Eligible for a connector spec or
   a new governance surface once LHW waves are exhausted.
2. **Worker timeout + recovery loop** — WR1 has `escalate_to_governance` but
   no timeout detection → sandbox restart → re-dispatch chain. Requires
   live execution scope, not doc connector.
3. **ReviewDeadlockException + micro-task decomposition** — retry counter
   threshold → escalation → work order decomposition. Requires execution scope.
4. **Pipeline chain execution binding** — the biggest gap: no surface chains
   governance advisories into sequential dispatch. This is the execution layer
   missing between CVF governance surfaces and actual agent orchestration.

**Scope classification:** Triggers 2-4 require live execution scope — eligible
for a separate execution-layer roadmap after LHW connector absorption is
complete. Trigger 1 may be feasible as a connector spec (doc-only).

---

## LH1 Remaining Families — Post-LHW Queue (operator direction 2026-05-28)

After LHW waves exhaust all doc-connector value, 4 LH1 families remain. These
are NOT abandoned — they are explicitly parked with known unlock conditions.

**Group A — Needs live route execution (eligible after LHW waves exhausted):**

| Family | LH1 trigger | Unlock condition |
| --- | --- | --- |
| `abtop` | Runtime observability dashboard or live failure-class trend readout | Open a live-proof roadmap after LHW waves exhausted. API keys available. |
| `gridex` | Read-only database action proof; mutation remains blocked | Same. Read-only boundary only. |

**Group B — Needs operator demand or concrete file (eligible when specified):**

| Family | LH1 trigger | Unlock condition |
| --- | --- | --- |
| `Review CVF.md` | Next pack only after usage evidence or operator demand | Operator names a specific new pack to add (e.g. `legal_brief_writer`). No ceremony required — explicit operator demand is sufficient. Alternatively: a live usage receipt from an existing pack. |
| `Review CVF_5.md` | Reopen when a concrete enforcement owner file is selected | Partially consumed by LHW11 T1+T2 (session governance posture aggregator is the "concrete enforcement owner"). If further value remains, it will surface as a new LHW gap naturally. |

Any agent encountering these families in a rejection log must cite this table
rather than writing bare "rejected" labels.

## LHW Rejection Language Rule (operator direction 2026-05-28)

When writing a rejection log entry: "rejected *from this LHW wave* (doc-only
scope) — eligible for live-proof roadmap after LHW waves exhausted" — never
bare "rejected: requires live route." `abtop` and `gridex` remain NOT
permanently blocked. API keys available.

---

## Required Evidence

Per tranche before CLOSED_PASS_BOUNDED: connector spec (5 sections S1–S5);
Fast Lane audit; work order with Source Verification Table (full paths, no
`same` shorthand, individual rows per enum value); completion review with all
required sections; governance gates PASS; no code file in diff; spec < 250
lines per GC-023; session continuity updated.

---

## Verification

Pre-closure governance gate:

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base d3e01013 --head <lhw11-commit> --enforce
python governance/compat/check_markdown_structural_completeness.py --base d3e01013 --head <lhw11-commit> --enforce
python governance/compat/check_docs_governance_compat.py --base d3e01013 --head <lhw11-commit> --enforce
```

---

## Claim Boundary

LHW11 is a second-order connector-normalization wave. It does not claim MCP
transport, tool execution, CLI invocation, workflow re-execution, memory
reinjection, raw memory release, new execution authority, new role taxonomy,
RBAC changes, receipt envelope extensions, external skill ingestion, provider
behavior changes, hosted readiness, production readiness, or public release
readiness.
