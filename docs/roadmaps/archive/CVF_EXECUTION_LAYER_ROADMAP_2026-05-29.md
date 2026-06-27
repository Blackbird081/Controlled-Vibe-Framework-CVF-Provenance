# CVF Execution Layer Roadmap

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS

docType: roadmap

Date: 2026-05-29

---

## Purpose

Define the execution-layer scope needed to close CVF 28.05 Gaps B/C/D and
complete absorption of the CVF 28.05 prototype (`cvf_cli.py`). This roadmap
is a planning record only. No tranche may begin without explicit operator
authorization and a fresh GC-018.

## Source

- CVF 28.05 prototype: `.private_reference/legacy/CVF 28.05/cvf_cli.py`
- CVF 28.05 gap record: `docs/baselines/CVF_GC018_LHW11_WORKFLOW_CONNECTOR_WAVE11_2026-05-28.md`
  section "New Source Family: CVF 28.05"
- Cross-reference audit: 2026-05-29 — confirmed all 3 gaps absent from
  CVF runtime by grep

## Why This Roadmap Exists

LHW waves (doc-only connectors) cannot close Gaps B/C/D because they require
**live execution scope**: actual timeout detection, sandbox restart, retry
counter, and pipeline chain dispatch. These are runtime behaviors, not advisory
governance records.

After LHW12/LHW13 close, CVF 28.05 Gap A (posture tier) will be absorbed via
LHW12-T1. Gaps B/C/D require this separate roadmap.

## Scope

### EL-1 — Pipeline Chain Orchestrator Contract

**Gap:** CVF has 5+ governance surfaces (W1 state machine, WR1 recovery, G1
identity gate, MA1 role transfer, LHW connectors) but nothing chains them into
a sequential dispatch: Intake Gate → Orchestrator → Worker (Draft/Execute) →
Reviewer → Closure Gate.

**What to build:** A single orchestration contract that:
- Accepts operator prompt
- Runs CVF Intake Gate (policy check, risk level, Guard Contract scan)
- Dispatches Work Orders to worker agents
- Chains Worker → Reviewer loop with rollback
- Routes to Closure Gate with evidence receipt
- Emits governance receipt at each stage

**Boundary:** Doc-first — define the contract shape and state machine before
any runtime wiring. Runtime execution binding is a separate sub-tranche.

**Prerequisites:** LHW12/LHW13 CLOSED_PASS_BOUNDED; fresh GC-018.

**Risk class:** R1 — governance contract extension; no new provider calls.

---

### EL-2 — WorkerTimeoutException Handler

**Gap:** CVF 28.05 defines `WorkerTimeoutException` (cvf_cli.py line 19) and
recovery logic (lines 111–114: clear sandbox → restart → re-dispatch). None
of this is in CVF runtime.

**What to build:**
- Timeout detection bound to worker execution step
- Sandbox cleanup signal (clear context cache, release session state)
- Automatic re-dispatch to fresh worker context
- Max retry limit (2 attempts before escalating to Orchestrator)
- Receipt entry: `WorkerTimeout` diagnostic class + recovery outcome

**Prerequisites:** EL-1 Pipeline Chain Contract; fresh GC-018.

**Risk class:** R1 — execution diagnostic extension.

---

### EL-3 — ReviewDeadlockException Handler + Micro-Task Decomposition

**Gap:** CVF 28.05 defines `ReviewDeadlockException` (cvf_cli.py line 23) and
`review_retry_counter` (lines 37, 124–132). After 3 Reviewer rejections, the
system should: escalate to Orchestrator → decompose Work Order into micro-tasks
→ re-dispatch to higher-capability agent or simpler sub-tasks.

**What to build:**
- `reviewRetryCounter` bound to reviewer step output
- Threshold trigger (>3 rejections → `ReviewDeadlockException`)
- Work Order decomposition logic: split into sub-tasks or escalate model tier
  (reference LHW12-T1 `modelTierAdvisoryType` for tier upgrade advisory)
- Human-Intervention-Required signal if decomposition still fails
- Receipt entry: `ReviewDeadlock` diagnostic class + decomposition outcome

**Prerequisites:** EL-2 WorkerTimeout; LHW12-T1 CLOSED_PASS (for tier advisory);
fresh GC-018.

**Risk class:** R2 — modifies workflow dispatch logic.

---

## Sequencing

```
EL-1 (Pipeline Chain Contract)
  └── EL-2 (WorkerTimeout Handler)
        └── EL-3 (ReviewDeadlock + Decomposition)
```

Each sub-tranche requires its own GC-018 + work order + completion review.

## CVF 28.05 Absorption Closure Condition

CVF 28.05 (`.private_reference/legacy/CVF 28.05/`) will be fully absorbed when:

- [x] LHW12-T1 CLOSED_PASS_BOUNDED (Gap A — posture tier)
- [x] EL-1 CLOSED_PASS (Gap D — pipeline chain)
- [x] EL-2 CLOSED_PASS (Gap B — WorkerTimeout)
- [x] EL-3 CLOSED_PASS (Gap C — ReviewDeadlock)

## Unlock Conditions

- Operator explicitly authorizes at least EL-1
- LHW12 and LHW13 are both CLOSED_PASS_BOUNDED (connector absorption first)
- Fresh GC-018 issued per sub-tranche

## Authorization / Decision

Status: CLOSED_PASS. All four EL tranches delivered and verified in commit
`4ff94dcb`. CVF 28.05 Gaps A/B/C/D absorbed. No further EL work pending.

## Non-Goals

- Any implementation before operator authorization
- Modifying existing governance surfaces or connector specs
- Claiming runtime behavior for pipeline chain, timeout handling, or deadlock
  handling before they are built and proven
- Merging this roadmap with LHW waves (execution scope is separate)

## Work Plan

| Tranche | Deliverable | Gate |
| --- | --- | --- |
| EL-1 | Pipeline Chain Orchestrator Contract | Operator authorization + fresh GC-018 |
| EL-2 | WorkerTimeout Handler | EL-1 CLOSED_PASS |
| EL-3 | ReviewDeadlock + Decomposition | EL-2 CLOSED_PASS |

## Acceptance Criteria

EL-1: pipeline contract spec + GC-018 + work order + completion review;
governance gates PASS; no unauthorized execution claimed.

EL-2: timeout handler evidence with receipt; GC-018 + work order; governance
gates PASS.

EL-3: deadlock handler evidence with receipt + decomposition logic; GC-018 +
work order; governance gates PASS; CVF 28.05 Gap D + B + C all CLOSED_PASS.

## Verification

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base <pre-EL-commit> --head <EL-commit> --enforce
python governance/compat/check_markdown_structural_completeness.py --base <pre-EL-commit> --head <EL-commit> --enforce
```

## Claim Boundary

This roadmap is a planning record. It does not authorize implementation, does
not claim runtime behavior, and does not modify any existing surface.
