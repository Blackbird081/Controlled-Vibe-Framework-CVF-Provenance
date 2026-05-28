# CVF Work Order — EL-3 ReviewDeadlock Handler + Micro-Task Decomposition

Memory class: FULL_RECORD

Status: HOLD_UNTIL_EL2_PASS

docType: work_order

Date: 2026-05-29

---

## Purpose

Implement ReviewDeadlock detection (retry counter > 3) and micro-task
decomposition escalation bound to the EL-1 pipeline contract's Reviewer stage.
Produces a live receipt showing deadlock detection, decomposition, and re-dispatch
or human-intervention signal.

Source: CVF 28.05 Gap C — `ReviewDeadlockException` class (cvf_cli.py line 23);
retry counter logic (lines 124–132); decomposition on escalation (lines 141–148).
CVF has no equivalent.

## Authority Chain

- EL GC-018: `docs/baselines/CVF_GC018_EXECUTION_LAYER_2026-05-29.md`
- EL Roadmap: `docs/roadmaps/CVF_EXECUTION_LAYER_ROADMAP_2026-05-29.md`
- CVF 28.05: `docs/baselines/CVF_GC018_EXECUTION_LAYER_2026-05-29.md` lines 123–148
- LHW12-T1 posture advisory: reference for model tier upgrade on deadlock
- Live run diagnostic standard: `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
- V3 diagnostics: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts`
- **EL-2 gate: `docs/reviews/CVF_EL2_WORKER_TIMEOUT_HANDLER_COMPLETION_2026-05-29.md`
  must be CLOSED_PASS**

## Agent Roles

Implementer adds `review_deadlock` diagnostic class and deadlock handler. The
handler detects 3+ Reviewer rejections, decomposes Work Order into micro-tasks
or upgrades model tier advisory, and emits `HumanInterventionRequired` if still
failing. Reviewer checks: retry counter threshold correct; decomposition advisory
references LHW12-T1 `modelTierAdvisoryType`; live receipt present. No self-review.

## Scope

**Allowed:**

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts`
  — add `review_deadlock` and `review_deadlock_decomposed` classes
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts`
  — add `ReviewDeadlockHandler` + `WorkOrderDecomposer`
- Corresponding test files
- `docs/evidence/execution-layer/review-deadlock-receipt.md` (new — live proof)
- `docs/reviews/CVF_EL3_REVIEW_DEADLOCK_HANDLER_COMPLETION_2026-05-29.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** New receipt envelope schema, new role taxonomy, autonomous
permanent agent spawning, public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`
4. `docs/baselines/CVF_GC018_EXECUTION_LAYER_2026-05-29.md` — deadlock logic lines 123–148
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts`
   — existing diagnostic classes lines 16–38
6. `docs/roadmaps/CVF_LHW12_WORKFLOW_CONNECTOR_WAVE12_ROADMAP_2026-05-29.md`
   — `modelTierAdvisoryType` for tier upgrade advisory on decomposition
7. `docs/reviews/CVF_EL2_WORKER_TIMEOUT_HANDLER_COMPLETION_2026-05-29.md`
   — confirm EL-2 CLOSED_PASS

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `ExecutionDiagnosticClass` type | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts` | lines 16–38 | `ExecutionDiagnosticClass` | `ExecutionDiagnostic` | ACCEPT |
| CVF 28.05 deadlock logic | `docs/baselines/CVF_GC018_EXECUTION_LAYER_2026-05-29.md` | lines 123–148 | `ReviewDeadlockException` handling | `CVFOrchestratorCLI.run_workflow` | ACCEPT |
| `modelTierAdvisoryType` field | `docs/roadmaps/CVF_LHW12_WORKFLOW_CONNECTOR_WAVE12_ROADMAP_2026-05-29.md` | S3 field list | `modelTierAdvisoryType` | LHW12-T1 doc-only field | ACCEPT |
| Live run diagnostic standard | `docs/reference/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md` | full document | diagnostic classification | CVF live run standard | ACCEPT |
| EL GC-018 authorization | `docs/baselines/CVF_GC018_EXECUTION_LAYER_2026-05-29.md` | full document | EL-3 authorization | EL GC-018 | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Retry counter + deadlock detection | Deliverable | handler logic | Counter threshold = 3 | OPEN |
| Micro-task decomposition or model tier upgrade | Deliverable | `WorkOrderDecomposer` | References LHW12-T1 advisory | OPEN |
| `HumanInterventionRequired` signal | Deliverable | handler logic | Signal defined | OPEN |
| Live receipt with deadlock evidence | Evidence | receipt `.md` | `evidenceMode=live` | OPEN |
| EL-2 gate confirmed | Authority Chain | EL-2 completion review | Read EL-2 | OPEN |
| CVF 28.05 fully absorbed | Closure Checklist | EL-1+EL-2+EL-3+LHW12-T1 | Gap A+B+C+D all CLOSED | OPEN |

## Deliverable

- Add `review_deadlock` and `review_deadlock_decomposed` to `ExecutionDiagnosticClass`
- Implement `ReviewDeadlockHandler`:
  - `reviewRetryCounter`: integer, incremented on each Reviewer rejection
  - Threshold: > 3 rejections → `ReviewDeadlockException`
  - Decomposition: split Work Order into micro-tasks OR emit
    `modelTierAdvisoryType=model_tier_premium_required` for tier upgrade advisory
  - If decomposition still fails: emit `HumanInterventionRequired` signal;
    stop pipeline; notify Orchestrator
  - Receipt entry: `review_deadlock` class + retry count + decomposition outcome
- `WorkOrderDecomposer`: splits a Work Order into 2–3 simpler sub-tasks
- Tests: deadlock detection (1), decomposition (1), human-intervention (1)
- Live proof: one governed pipeline call where 3 Reviewer rejections occur;
  deadlock handler activates; receipt in
  `docs/evidence/execution-layer/review-deadlock-receipt.md`

## Pre-Flight

- [ ] Working tree clean
- [ ] All required first reads done
- [ ] Gate confirmations checked

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be modified.

## Review Gate

Before committing: all source symbols verified; required evidence present; no forbidden files in diff.

## Return-To-Orchestrator Conditions

Stop if: required gate evidence missing; a cited source file cannot be found; implementing the deliverable requires a forbidden file change.

## Execution Plan

1. Read all required first reads; confirm EL-2 gate.
2. Add diagnostic classes to `execution-diagnostics.ts`.
3. Implement `ReviewDeadlockHandler` + `WorkOrderDecomposer`.
4. Write 3 tests; run `npm run test:run`; verify PASS.
5. Make 1 governed pipeline call triggering deadlock; capture receipt.
6. Write evidence record and completion review.
7. Run governance gates.
8. Update session continuity; record CVF 28.05 full absorption status.
9. Commit.

## Evidence Requirements

- `review_deadlock` + `review_deadlock_decomposed` classes added
- Handler with threshold=3 + decomposition + human-intervention
- Tests PASS (3 tests)
- Live receipt with `review_deadlock` diagnostic class
- `rawSecretPrinted=false`
- EL-2 gate confirmed

## Acceptance Criteria

- [ ] EL-2 CLOSED_PASS confirmed
- [ ] `review_deadlock` + `review_deadlock_decomposed` added to diagnostics
- [ ] `ReviewDeadlockHandler` + `WorkOrderDecomposer` implemented
- [ ] Tests PASS
- [ ] Live receipt captured; `rawSecretPrinted=false`
- [ ] `HumanInterventionRequired` signal defined
- [ ] CVF 28.05 Gap C closure documented in completion review
- [ ] Session continuity updated

## CVF 28.05 Full Absorption Closure Checklist

EL-3 is the final tranche completing CVF 28.05 absorption:

- [ ] LHW12-T1 CLOSED_PASS_BOUNDED (Gap A — posture tier)
- [ ] EL-1 CLOSED_PASS (Gap D — pipeline chain)
- [ ] EL-2 CLOSED_PASS (Gap B — WorkerTimeout)
- [ ] EL-3 CLOSED_PASS (Gap C — ReviewDeadlock)

Completing agent must document CVF 28.05 absorption status in
`CVF_SESSION/ACTIVE_SESSION_STATE.json` under a `cvf2805FullAbsorption` key.

## Closure Checklist

- [ ] EL-2 confirmed
- [ ] Diagnostics extended
- [ ] Handler + decomposer implemented + tests PASS
- [ ] Live receipt captured
- [ ] Completion review with CVF 28.05 full absorption summary
- [ ] Governance gates PASS
- [ ] Session continuity updated; `cvf2805FullAbsorption` key added

## Operator Checkpoint

Operator authorized live API key use 2026-05-29.

## Claim Boundary

EL-3 produces a bounded deadlock handler and decomposer. It does not claim
autonomous permanent agent spawning, broad pipeline stability, all-provider
compatibility, new receipt envelope schema, hosted readiness, production
readiness, or public release readiness.
