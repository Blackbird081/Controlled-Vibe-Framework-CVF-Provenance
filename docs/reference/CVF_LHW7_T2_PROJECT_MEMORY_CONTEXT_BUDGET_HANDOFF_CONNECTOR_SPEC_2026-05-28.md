# CVF LHW7-T2 Project Memory Readout → Context Budget Handoff Connector Spec

Memory class: FULL_RECORD

docType: reference

Contract version: `cvf.projectMemoryContextBudgetHandoff.lhw7.t2.v1`

Date: 2026-05-28

Status: CLOSED_PASS_BOUNDED

---

## Purpose

Connector spec binding LHW6-T3 project memory readout → CB1 context budget
readout → VI2 route-level `missingSignals` into a cross-session handoff packet
that defines which summary fields can seed CB1 `missingSignals` on resume
without violating `canReinject=false`.

## Scope / Applies To

Applies to: Orchestrator agents resuming a prior session who need to determine
which project memory summary fields to use as CB1 signal seeds.
Documentation-only; no runtime enforcement.

---

## S1 — Purpose and Claim Boundary

This connector is a normative documentation standard binding LHW6-T3 project
memory readout packet fields → CB1 `RouteRequestContextReadout` fields → VI2
`missingSignals` into a cross-session handoff packet for Orchestrator use on
session resume.

### Problem it solves

When an Orchestrator resumes a prior session, LHW6-T3 says what the prior
session contained (`durableTierSummary`, `canReinject=false`). CB1/VI2 say what
the current request lacks (`missingSignals`, `contaminationFlags`, `budgetTier`).
No standard says which project memory summary fields can populate which CB1
missing signals without violating `canReinject=false`.

This connector defines that seeding rule.

### What this connector is not

- Not a LHW6-T3, CB1, or VI2 runtime extension.
- Not a memory injection path.
- Not a prompt-seeding executor.

Explicit invariants:

- "This connector does not inject memory into the prompt."
- "Seeding is a summary-only signal map; raw memory is never released."
- `canReinject=false` is invariant throughout.
- `rawMemoryReleased=false` is invariant throughout.
- `runtimeExecutionAuthorized=false` is invariant throughout.

T2 gate confirmed: `docs/reviews/CVF_LHW7_T2_FAST_LANE_AUDIT_2026-05-28.md`
— Status: FAST_LANE_READY. T1 gate: `CLOSED_PASS_BOUNDED`.

---

## S2 — Session-Resume Memory-to-Signal Seeding Map

Input: LHW6-T3 `durableTierSummary` tier value + `allowed` gateway state +
CB1/VI2 `missingSignals` → derived `seedableSummaryFields`,
`signalsSeededBySummary`, `signalsStillMissing`, `contaminationRiskAfterSeed`.

Seeding rule: a tier summary may only populate `missingSignals` entries where
the signal class matches the tier's summary scope and `summaryOnly=true`.
The agent reads the summary description — never the underlying memory record.

| LHW6-T3 tier | `canReinject` | `summaryOnly` | Gateway `allowed` | Signals seedable | `contaminationRiskAfterSeed` |
| --- | --- | --- | --- | --- | --- |
| `skill` | `false` | `true` | `true` | `selected_pack`, `workflow_goal` | `low` |
| `long-term` | `false` | `true` | `true` | `actor_role`, `domain_context` | `medium` |
| `skill` and `long-term` both present | `false` | `true` | `true` | union of both rows | `medium` — check `noiseFlags` |
| any tier | `false` | `true` | `false` (gateway denied) | none — `signalsSeededBySummary=[]` | `none` |
| any tier | `false` | `true` | `true`, `memoryIdsAffected` empty | none — `signalsSeededBySummary=[]` | `none` |

If seeding introduces domain-context signals that conflict with current request
signals, set `contaminationRiskAfterSeed=high` and preserve all entries in
`signalsStillMissing`. Never reduce `contaminationFlags` via seeding.

`canReinject=false` and `rawMemoryReleased=false` hold in every row.

---

## S3 — Handoff Packet Minimum Fields

Every Project Memory → Context Budget Handoff packet must contain the following
fields. All fields are doc-only. `canReinject=false` and
`rawMemoryReleased=false` are invariant. The packet does not extend
`GovernanceEvidenceReceipt` or any existing receipt envelope.

- `handoffPacketId`: unique doc-only token
- `sessionResumeContext`: label for the prior session being resumed
- `durableTierSummary`: list of LHW6-T3 tier values present, each with
  `summaryOnly=true` — from M1 `DurableMemoryReceipt.tier`
- `gatewayMemoryIds`: from LHW6-T3 / AIF-C `MemoryGatewayDecision.memoryIdsAffected`
- `canReinject`: always `false`
- `rawMemoryReleased`: always `false`
- `priorBudgetTier`: CB1 `RouteRequestContextBudgetTier` from prior session,
  or `null` if unavailable — values: `minimal` | `standard` | `expanded`
- `currentBudgetTier`: CB1 `RouteRequestContextBudgetTier` for current request
- `missingSignalsBeforeSeed`: CB1/VI2 `missingSignals` before any seeding
- `seedableSummaryFields`: derived list of summary fields that can cover missing
  signals (new doc-only field)
- `signalsSeededBySummary`: derived list of `missingSignals` entries the
  summary populates (new doc-only field)
- `signalsStillMissing`: derived list of `missingSignals` remaining after
  seeding (new doc-only field)
- `contaminationRiskAfterSeed`: derived risk level — `low` | `medium` | `high`
  | `none` (new doc-only field)
- `runtimeExecutionAuthorized`: always `false`
- `recommendedNextAction`: plain-language guidance for Orchestrator

---

## S4 — Boundary Table

| Surface | Doc-only | Runtime-proven (source) |
| --- | --- | --- |
| LHW6-T3 `durableTierSummary` and `gatewayMemoryIds` | — | Yes — LHW6-T3 spec S3; `controlled-memory-gateway.ts` lines 40–51 |
| LHW6-T3 `canReinject=false` | — | Yes — `controlled-memory-gateway.ts` line 50 |
| LHW6-T3 `rawMemoryReleased=false` | — | Yes — `controlled-memory-gateway.ts` line 50 |
| CB1 `budgetTier` (`minimal`, `standard`, `expanded`) | — | Yes — `route-request-context-readout.ts` line 6, 16 |
| CB1 `missingSignals`, `contaminationFlags`, `noiseFlags` | — | Yes — `route-request-context-readout.ts` lines 22–24 |
| VI2 `missingSignals`, `contaminationFlags` | — | Yes — `route-request-context-readout.ts` lines 22–24 |
| `seedableSummaryFields` | New doc-only field | — |
| `signalsSeededBySummary` | New doc-only field | — |
| `signalsStillMissing` | New doc-only field | — |
| `contaminationRiskAfterSeed` | New doc-only field | — |
| Memory injection or prompt seeding | Not authorized | Not authorized |
| `canReinject=true` | Not authorized | Not authorized |

---

## S5 — Source Verification Table

| Token | Source file | Line | Interface/type | Connector location | Decision |
| --- | --- | --- | --- | --- | --- |
| LHW6-T3 `durableTierSummary` | `docs/reference/CVF_LHW6_PROJECT_MEMORY_READOUT_CONNECTOR_SPEC_2026-05-28.md` | S3 line 82 | LHW6-T3 packet | S3 field | ACCEPT |
| LHW6-T3 `gatewayMemoryIds` | same | S3 line 83 | LHW6-T3 packet | S3 field | ACCEPT |
| LHW6-T3 `canReinject=false` | same | S3 line 84 | invariant | S3 invariant | ACCEPT |
| LHW6-T3 `rawMemoryReleased=false` | same | S3 line 85 | invariant | S3 invariant | ACCEPT |
| M1 `DurableMemoryReceipt` (`summaryOnly`, `canReinject`, `rawMemoryReleased`, `tier`) | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/durable-memory-store.ts` | lines 35–49 | `DurableMemoryReceipt` | S2 tier context | ACCEPT |
| AIF-C `MemoryGatewayDecision.memoryIdsAffected` | `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/controlled-memory-gateway.ts` | lines 40–51 | `MemoryGatewayDecision` | S3 `gatewayMemoryIds` | ACCEPT |
| AIF-C `rawMemoryReleased=false` hardcoded | same | line 50 | `MemoryGatewayDecision` | S3 invariant | ACCEPT |
| CB1 `RouteRequestContextBudgetTier` values | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-request-context-readout.ts` | line 6 | `RouteRequestContextBudgetTier` | S3 `budgetTier` | ACCEPT |
| CB1 `budgetTier` field | same | line 16 | `RouteRequestContextReadout` | S3 `currentBudgetTier` | ACCEPT |
| CB1 `missingSignals` | same | line 22 | `RouteRequestContextReadout` | S3 `missingSignalsBeforeSeed` | ACCEPT |
| CB1 `contaminationFlags` | same | line 24 | `RouteRequestContextReadout` | S2 contamination risk | ACCEPT |
| CB1 `noiseFlags` | same | line 23 | `RouteRequestContextReadout` | S2 noise check | ACCEPT |
| VI2 `missingSignals` (route-level) | same | line 22 | `RouteRequestContextReadout` | S3 `missingSignalsBeforeSeed` | ACCEPT |
| `RouteRequestContextReadiness` values | same | lines 7–11 | `RouteRequestContextReadiness` | S2 context | ACCEPT |
| `seedableSummaryFields` | N/A — new doc-only | S3 new fields | doc-only | S3 | ACCEPT |
| `signalsSeededBySummary` | N/A — new doc-only | S3 new fields | doc-only | S3 | ACCEPT |
| `signalsStillMissing` | N/A — new doc-only | S3 new fields | doc-only | S3 | ACCEPT |
| `contaminationRiskAfterSeed` | N/A — new doc-only | S3 new fields | doc-only | S3 | ACCEPT |

## Claim Boundary

This connector normalizes cross-session memory-to-context-budget handoff
between three existing closed surfaces. It does not claim memory injection,
prompt seeding from raw memory, memory reinjection, `canReinject=true`,
receipt-envelope extension, CB1/VI2 runtime change, provider behavior change,
public-sync work, hosted readiness, production readiness, or public release
readiness.
