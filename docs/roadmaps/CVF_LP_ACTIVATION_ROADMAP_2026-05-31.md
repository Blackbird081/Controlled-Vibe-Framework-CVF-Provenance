# CVF Learning Plane Activation Roadmap

Memory class: POINTER_RECORD

Status: CLOSED_PASS_BOUNDED (RT1+RT2+RT3).

Date: 2026-05-31

---

## Purpose

Define the full activation path for the CVF Learning Plane, covering two scopes:

- **Scope A — Runtime wiring proof:** Verify that `learning-plane-readout.ts` is correctly
  wired into `/api/execute` ALLOW responses with WD1 doctrine applied. This scope has
  code already written (untracked); it needs a commit, live proof, and GC-018 closure.

- **Scope B — Finding-to-Learning bridge:** Wire the governance finding guard
  (`check_finding_to_governance_learning.py`) taxonomy into the Learning Signal Intake Bridge
  (`learning-signal-intake-bridge.ts`) so that governance findings flow as typed signals
  into the Learning Plane feedback ledger. Currently protocol-coupled only; no live code path.

---

## Scope / Target / Owner Boundary

Target: CVF Learning Plane activation across two scopes:

- Scope A: `cvf-web/src/lib/learning-plane-readout.ts` wiring into `/api/execute`
- Scope B: `finding-to-learning-bridge.ts` adapter connecting finding guard taxonomy to `LearningSignalIntakeBridge`

Owner: CVF Web UI surface (RT1/RT2) + LPF (intake bridge consumer).

Non-implementation: RT3 (feedback ledger write) is FUTURE and requires a separate GC-018.

## Authorization / Decision

RT1: AUTHORIZED per `docs/baselines/CVF_GC018_RT1_LEARNING_PLANE_RUNTIME_WIRING_2026-05-31.md`.
RT2: Requires fresh GC-018 after RT1 CLOSED_PASS_BOUNDED.
RT3: Blocked — `autonomousMutationAuthorized=false` until operator explicit authorization.

---

## Background

### What exists today (pre-roadmap)

| Component | Location | Status |
| --- | --- | --- |
| `buildLearningPlaneReadout()` | `cvf-web/src/lib/learning-plane-readout.ts` | Written, untracked, not committed |
| `learning-plane-readout.test.ts` | `cvf-web/src/lib/` | 8 tests, untracked |
| `/api/execute` wiring (line 952) | `route.ts` | Active — calls `buildLearningPlaneReadout()` |
| `LearningSignalIntakeBridge` | `LPF/src/learning-signal-intake-bridge.ts` | Committed, 181 lines, `autonomousMutationAuthorized=false` |
| Finding-to-governance guard | `governance/compat/check_finding_to_governance_learning.py` | Machine-enforced, validates taxonomy |
| WD1 `applyWeightingDoctrine()` | `LPF/src/weighting-doctrine.ts` | Committed, closed (WD1 GC-018) |

### The gap

The finding guard enforces that governance docs classify findings using the same
`LearningSignalLane` and `LearningSignalDefectClass` enums as the intake bridge — but
no code path currently calls `LearningSignalIntakeBridge.intake()` from a governance
finding workflow. The bridge is a typed receiver with no live caller.

---

## Tranche Plan

### RT1 — Runtime Wiring Proof (Scope A)

**Contract:** `cvf.learningPlaneRuntimeWiring.rt1.v1`

**Allowed scope:**

- Commit `learning-plane-readout.ts` + test (73 + 49 lines, untracked)
- Run full cvf-web test suite to confirm 8 new tests pass alongside existing suite
- Live proof: one `/api/execute` call (alibaba/qwen-turbo/R1) confirming
  `learningPlaneReadout` field present in ALLOW response with `outcome=DOCTRINE_APPLIED`,
  `isProvisional=false`, `runtimeScoringAuthorized=false`
- Fast Lane audit (R1 risk — additive advisory readout only, no route behavior change)

**Blocked expansion:**

- No route.ts behavior change (route.ts is at hard limit 1000 lines)
- No mutation of `confidenceLevel` default without fresh GC-018
- No `runtimeScoringAuthorized=true` path
- No feedback ledger write from this tranche

**Prerequisites:** WD1 CLOSED_PASS_BOUNDED (satisfied), LP-LP1+LP-LP2 (satisfied)

**Deliverables:**

- [x] `learning-plane-readout.ts` committed (73 lines, inline doctrine logic)
- [x] 8/8 unit tests PASS
- [x] Live proof receipt `rcpt-env-mptbpftd-1yfw15` (alibaba/qwen-turbo, ALLOW, outcome=DOCTRINE_APPLIED)
- [x] Fast Lane audit PASS
- [x] Completion review CLOSED_PASS_BOUNDED
- [x] GC-018 baseline AUTHORIZED

---

### RT2 — Finding-to-Learning Signal Bridge (Scope B)

**Contract:** `cvf.findingToLearningSignalBridge.rt2.v1`

**Prerequisite:** RT1 CLOSED_PASS_BOUNDED

**Allowed scope:**

- New module: `cvf-web/src/lib/finding-to-learning-bridge.ts` — a typed adapter that
  accepts a governance finding record (lane + defectClass + disposition + nextAction)
  and calls `LearningSignalIntakeBridge.intake()` to produce a `LearningSignalIntakeRecord`
- The adapter is **advisory only**: `autonomousMutationAuthorized=false` always
- Unit tests for the adapter (separate test file, ≤80 lines)
- `buildFindingToLearningReadout()` added to `/api/execute` ALLOW response as additive
  field (only if route.ts can absorb — check line count gate before implementation)
- Fast Lane audit (R1 risk — no enforcement, no route blocking)

**Blocked expansion:**

- No autonomous feedback ledger write without separate GC-018
- No route.ts edit if it would exceed 1000-line hard limit (requires rotation first)
- No Python guard code change — guard already enforces taxonomy correctly
- No new governance enums — reuse existing `LearningSignalLane` values

**Deliverables:**

- [x] GC-018 baseline (fresh, referencing RT1 closure)
- [x] `finding-to-learning-bridge.ts` (new file, 102 lines)
- [x] Unit tests (76 lines, 10/10 PASS)
- [x] route.ts line count pre-flight check (1000 = hard limit; wiring deferred)
- [x] Live proof — `finding-to-learning-bridge.live.test.ts` 1/1 PASS
- [x] Completion review CLOSED_PASS_BOUNDED

---

### RT3 — Feedback Ledger Write Authorization (Scope C, FUTURE)

**Contract:** `cvf.feedbackLedgerWriteAuthorization.rt3.v1`

**Status:** CLOSED_PASS_BOUNDED — Operator authorized 2026-05-31. New route
`/api/learning-plane/readout` POST endpoint implemented, 6/6 unit tests PASS,
1/1 live proof PASS, `autonomousMutationAuthorized=false` always.
Boundary doc: `docs/reviews/CVF_RT3_FEEDBACK_LEDGER_WRITE_AUTHORIZATION_BOUNDARY_2026-05-31.md`
GC-018: `docs/baselines/CVF_GC018_RT3_FEEDBACK_LEDGER_WRITE_AUTHORIZATION_2026-05-31.md`

Note: RT3 implements the advisory readout surface only. Full feedback ledger
mutation requires a separate future R2–R3 GC-018 + operator checkpoint.

---

## Risk Classification

| Tranche | Risk | Rationale |
| --- | --- | --- |
| RT1 | R1 | Commit of already-written additive readout; no route behavior change |
| RT2 | R1 | New adapter file + additive advisory readout only; no enforcement |
| RT3 | R2–R3 | Ledger mutation; requires separate GC-018 |

---

## Architecture (post-RT2)

```text
governance/compat/check_finding_to_governance_learning.py
    └─ Validates: lane + defectClass + disposition in finding docs
    └─ Taxonomy matches LearningSignalLane / LearningSignalDefectClass enums

cvf-web/src/lib/finding-to-learning-bridge.ts  [RT2 NEW]
    └─ buildFindingToLearningReadout(findingRecord) → LearningSignalIntakeRecord
    └─ Calls: LearningSignalIntakeBridge.intake()
    └─ autonomousMutationAuthorized = false

LPF/src/learning-signal-intake-bridge.ts
    └─ intake(input) → LearningSignalIntakeRecord + LearningFeedbackInput
    └─ Feeds: Feedback Ledger (RT3, FUTURE)

cvf-web/src/lib/learning-plane-readout.ts  [RT1 — commit]
    └─ buildLearningPlaneReadout(role, confidenceLevel)
    └─ Imports: TruthModelContract + applyWeightingDoctrine() from LPF
    └─ Wired in /api/execute line 952 → learningPlaneReadout field

/api/execute ALLOW response
    └─ learningPlaneReadout: { outcome, compositeScore, isProvisional, runtimeScoringAuthorized=false }
    └─ findingToLearningReadout: { intakeRecord, autonomousMutationAuthorized=false }  [RT2]
```

---

## Non-Goals

The following are explicitly out of scope for this roadmap:

- No autonomous feedback ledger mutation (RT3 is FUTURE)
- No `runtimeScoringAuthorized=true` path at any tranche
- No new governance enums — existing `LearningSignalLane` values reused
- No route.ts logic change beyond additive advisory fields
- No framework-specific adapter (IS1 is complete; frameworks connect IN)
- No hosted readiness, production readiness, or public release readiness claim

---

## Work Plan

| Tranche | Contract | Prerequisite | Risk | Authorized |
| --- | --- | --- | --- | --- |
| RT1 | `cvf.learningPlaneRuntimeWiring.rt1.v1` | WD1 CLOSED | R1 | CLOSED_PASS_BOUNDED — rcpt-env-mptbpftd-1yfw15 |
| RT2 | `cvf.findingToLearningSignalBridge.rt2.v1` | RT1 CLOSED | R1 | CLOSED_PASS_BOUNDED — live.test.ts 1/1 PASS |
| RT3 | `cvf.learningPlaneReadoutRoute.rt3.v1` | RT2 CLOSED + operator auth | R1 | CLOSED_PASS_BOUNDED — new /api/learning-plane/readout route |

---

## Acceptance Criteria

**RT1 complete when:**

- `learning-plane-readout.ts` committed (73 lines)
- 8/8 unit tests PASS
- Live receipt from alibaba/qwen-turbo with `learningPlaneReadout.outcome=DOCTRINE_APPLIED`, `isProvisional=false`, `runtimeScoringAuthorized=false`

**RT2 complete — CLOSED_PASS_BOUNDED:**

- `finding-to-learning-bridge.ts` committed (102 lines) ✓
- 10/10 unit tests PASS ✓
- Live proof `finding-to-learning-bridge.live.test.ts` 1/1 PASS, autonomousMutationAuthorized=false ✓
- GC-018 AUTHORIZED before implementation ✓
- Note: route.ts wiring deferred (1000-line hard limit)

**RT3 complete — CLOSED_PASS_BOUNDED:**

- New `/api/learning-plane/readout` POST route (87 lines) ✓
- 6/6 unit tests PASS ✓
- 1/1 live proof PASS, `autonomousMutationAuthorized=false` ✓
- Operator explicit auth 2026-05-31 ✓

---

## Verification / Evidence

| Tranche | Evidence path |
| --- | --- |
| RT1 GC-018 | `docs/baselines/CVF_GC018_RT1_LEARNING_PLANE_RUNTIME_WIRING_2026-05-31.md` |
| RT1 Fast Lane | `docs/reviews/CVF_RT1_LEARNING_PLANE_RUNTIME_WIRING_FAST_LANE_2026-05-31.md` |
| RT1 Completion | `docs/reviews/CVF_RT1_LEARNING_PLANE_RUNTIME_WIRING_COMPLETION_2026-05-31.md` |
| RT2 GC-018 | `docs/baselines/CVF_GC018_RT2_FINDING_TO_LEARNING_SIGNAL_BRIDGE_2026-05-31.md` |
| RT2 Fast Lane | `docs/reviews/CVF_RT2_FINDING_TO_LEARNING_SIGNAL_BRIDGE_FAST_LANE_2026-05-31.md` |
| RT2 Completion | `docs/reviews/CVF_RT2_FINDING_TO_LEARNING_SIGNAL_BRIDGE_COMPLETION_2026-05-31.md` |
| RT3 Boundary | `docs/reviews/CVF_RT3_FEEDBACK_LEDGER_WRITE_AUTHORIZATION_BOUNDARY_2026-05-31.md` |
| RT3 GC-018 | `docs/baselines/CVF_GC018_RT3_FEEDBACK_LEDGER_WRITE_AUTHORIZATION_2026-05-31.md` |
| RT3 Fast Lane | `docs/reviews/CVF_RT3_LEARNING_PLANE_READOUT_ROUTE_FAST_LANE_2026-05-31.md` |
| RT3 Completion | `docs/reviews/CVF_RT3_LEARNING_PLANE_READOUT_ROUTE_COMPLETION_2026-05-31.md` |

---

## Claim Boundary

This roadmap is a planning document only. RT1 is authorized; RT2 and RT3 each
require a fresh GC-018 before implementation begins.

No claim of:

- Hosted readiness, production readiness, or public release readiness
- Autonomous mutation or live feedback ledger write (RT3 only with separate GC-018)
- Universal Learning Plane activation beyond the advisory readout surface
- Cross-agent memory transfer, provider behavior change, or runtime enforcement

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: This roadmap is internal governance provenance only. No public-sync export is
required or performed at the roadmap stage. RT1/RT2 capability additions (advisory
readout fields in `/api/execute`) are internal Web UI surface changes; they will be
assessed for public catalog update after each tranche reaches CLOSED_PASS_BOUNDED.

---

## Next Step

RT1 CLOSED_PASS_BOUNDED (receipt rcpt-env-mptbpftd-1yfw15). RT2 CLOSED_PASS_BOUNDED
(1/1 live proof PASS). RT3 CLOSED_PASS_BOUNDED (1/1 live proof PASS, operator explicit auth
2026-05-31). LP Activation Roadmap fully complete — RT1+RT2+RT3 all closed.
Future: feedback ledger write mutation requires separate R2–R3 GC-018 + operator checkpoint.
