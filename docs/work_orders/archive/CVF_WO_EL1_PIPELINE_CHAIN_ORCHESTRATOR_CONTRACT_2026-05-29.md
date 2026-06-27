# CVF Work Order — EL-1 Pipeline Chain Orchestrator Contract

Memory class: FULL_RECORD

Status: HOLD_UNTIL_LHW12_AND_LHW13_PASS

docType: work_order

Date: 2026-05-29

---

## Purpose

Define and partially implement the Pipeline Chain Orchestrator Contract: a
single orchestration contract binding CVF's 5 governance surfaces (Intake Gate
→ Orchestrator → Worker Draft/Execute → Reviewer → Closure Gate) into a
sequential dispatch with state handoff and receipt at each stage.

Source: CVF 28.05 Gap D — pipeline stages documented but nothing chains them.
`cvf_cli.py` prototype (lines 56–166) proves the chain is viable; EL-1 makes
it governed.

EL-1 is doc-first: define the contract shape and state machine. Runtime binding
is included as a bounded implementation within this tranche.

## Authority Chain

- EL GC-018: `docs/baselines/CVF_GC018_EXECUTION_LAYER_2026-05-29.md`
- EL Roadmap: `docs/roadmaps/CVF_EXECUTION_LAYER_ROADMAP_2026-05-29.md`
- CVF 28.05 prototype: `.private_reference/legacy/CVF 28.05/cvf_cli.py`
  — pipeline orchestration at lines 56–166
- LHW12-T1 posture advisory: planned spec
  `docs/reference/CVF_LHW12_T1_POSTURE_TO_MODEL_TIER_ADVISORY_CONNECTOR_SPEC_2026-05-29.md`
- LHW12-T3 worker lifecycle: planned spec
  `docs/reference/CVF_LHW12_T3_ASYNC_WORKER_LIFECYCLE_BOUNDARY_CONNECTOR_SPEC_2026-05-29.md`
- MA1 transfer standard: `docs/reference/archive/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
- **Gate: LHW12 AND LHW13 must both be CLOSED_PASS_BOUNDED before dispatch**

## Agent Roles

Implementer writes contract spec and wires CVF governance surfaces into the
pipeline. Reviewer checks: each stage has a governance receipt gate; MA1 role
handoff used between stages; `runtimeExecutionAuthorized=false` for any stage
that requires separate approval. Auditor confirms no autonomous agent spawning;
human-intervention signal defined. No self-review.

## Scope

**Allowed:**

- `docs/contracts/CVF_PIPELINE_CHAIN_ORCHESTRATOR_CONTRACT.md` (new)
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts`
  (new — contract interface and state machine only; no provider call logic)
- Corresponding test file
- `docs/reviews/CVF_EL1_PIPELINE_CHAIN_ORCHESTRATOR_CONTRACT_COMPLETION_2026-05-29.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** New receipt envelope schema, new role taxonomy, new provider
execution semantics beyond existing `executeReal()`, autonomous agent spawning
without gate, public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `.private_reference/legacy/CVF 28.05/cvf_cli.py` — pipeline structure
   lines 56–166; exception classes lines 15–25; config pattern lines 31–38
4. `docs/reference/archive/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md`
   — MA1 role lanes (Orchestrator/Implementer/Reviewer/Auditor)
5. `docs/reference/CVF_LHW12_T1_POSTURE_TO_MODEL_TIER_ADVISORY_CONNECTOR_SPEC_2026-05-29.md`
   — required after LHW12-T1 closure; `modelTierAdvisoryType`
6. `docs/reference/CVF_LHW12_T3_ASYNC_WORKER_LIFECYCLE_BOUNDARY_CONNECTOR_SPEC_2026-05-29.md`
   — required after LHW12-T3 closure; `workerLifecycleAdvisoryType` and
   `spawnAuthorizationAdvisory`
7. Gate evidence: LHW12 roadmap CLOSED_PASS_BOUNDED + LHW13 roadmap
   CLOSED_PASS_BOUNDED (confirm before dispatch)

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| CVF 28.05 pipeline structure | canonical-contract: `.private_reference/legacy/CVF 28.05/cvf_cli.py` | lines 56–166 | `run_workflow` | `CVFOrchestratorCLI` | ACCEPT |
| CVF 28.05 exception classes | canonical-contract: `.private_reference/legacy/CVF 28.05/cvf_cli.py` | lines 15–25 | exception classes | `CVFOrchestratorCLI` | ACCEPT |
| MA1 `Orchestrator` role | `docs/reference/archive/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | line 96 | `Orchestrator` | MA1 role lane | ACCEPT |
| MA1 `Implementer` role | `docs/reference/archive/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | line 97 | `Implementer` | MA1 role lane | ACCEPT |
| MA1 `Reviewer` role | `docs/reference/archive/CVF_INTERNAL_MULTI_AGENT_WORK_TRANSFER_PACKET_STANDARD_2026-05-26.md` | line 98 | `Reviewer` | MA1 role lane | ACCEPT |
| `modelTierAdvisoryType` field | `docs/reference/CVF_LHW12_T1_POSTURE_TO_MODEL_TIER_ADVISORY_CONNECTOR_SPEC_2026-05-29.md` | pending LHW12-T1 closure | `modelTierAdvisoryType` | LHW12-T1 doc-only field | BLOCKED_SOURCE_NOT_FOUND |
| `workerLifecycleAdvisoryType` field | `docs/reference/CVF_LHW12_T3_ASYNC_WORKER_LIFECYCLE_BOUNDARY_CONNECTOR_SPEC_2026-05-29.md` | pending LHW12-T3 closure | `workerLifecycleAdvisoryType` | LHW12-T3 doc-only field | BLOCKED_SOURCE_NOT_FOUND |
| EL GC-018 authorization | `docs/baselines/CVF_GC018_EXECUTION_LAYER_2026-05-29.md` | full document | EL-1 authorization | EL GC-018 | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| Pipeline contract 5 stages | Deliverable | contract doc + TS interface | All stages defined | OPEN |
| MA1 handoff between stages | Deliverable | contract references MA1 | Reviewer checks | OPEN |
| Receipt gate at each stage | Deliverable | contract spec | Each stage has receipt requirement | OPEN |
| Human-intervention signal defined | Deliverable | contract spec | `HumanInterventionRequired` event defined | OPEN |
| LHW12 + LHW13 gate confirmed | Authority Chain | both roadmap CLOSED | Read roadmaps | BLOCKED |

## Deliverable

`docs/contracts/CVF_PIPELINE_CHAIN_ORCHESTRATOR_CONTRACT.md` must define:
- 5 pipeline stages with input/output schema per stage
- MA1 role assignment per stage
- Receipt requirement per stage (governance evidence)
- State handoff fields between stages
- `HumanInterventionRequired` escalation condition
- Reference to `modelTierAdvisoryType` for model selection per stage
- Reference to `workerLifecycleAdvisoryType` for worker scope

`EXTENSIONS/.../pipeline-chain-orchestrator.ts` must define:
- `PipelineChainState` type (5 stage values)
- `PipelineStageResult` interface (output + receipt + nextStage)
- `PipelineChainOrchestrator` interface (no implementation — contract only)
- Tests: 5 state transition tests PASS

## Pre-Flight

- [ ] Working tree clean
- [ ] All required first reads done
- [ ] Gate confirmations checked

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be modified.

## Return-To-Orchestrator Conditions

Stop if: required gate evidence missing; a cited source file cannot be found; implementing the deliverable requires a forbidden file change.

## Execution Plan

1. Read all required first reads; confirm LHW12 + LHW13 gates.
2. Design 5-stage contract with MA1 handoff and receipt gates.
3. Write contract doc.
4. Write TypeScript interface + tests.
5. Run `npm run test:run` in cvf-web; verify tests PASS.
6. Write completion review.
7. Run governance gates.
8. Update session continuity.
9. Commit.

## Evidence Requirements

- Contract doc with 5 stages, MA1 handoff, receipt gates
- TypeScript interface file with stage types
- Tests PASS
- LHW12 + LHW13 gates confirmed

## Acceptance Criteria

- [ ] LHW12 AND LHW13 CLOSED_PASS_BOUNDED confirmed
- [ ] Contract doc created with 5 stages + MA1 handoff
- [ ] TypeScript interface file with `PipelineChainState` + `PipelineStageResult`
- [ ] Tests PASS
- [ ] Human-intervention escalation defined
- [ ] Session continuity updated

## Review Gate

LHW12/LHW13 gates; 5 stages defined; MA1 handoff; receipt per stage; tests PASS.

## Closure Checklist

- [ ] LHW12 + LHW13 gates confirmed
- [ ] Contract doc created
- [ ] TypeScript interface + tests PASS
- [ ] Completion review written
- [ ] Governance gates PASS
- [ ] Session continuity updated

## EL-2 Gate Output

EL-2 (WorkerTimeout) gates on EL-1 CLOSED_PASS. After EL-1 closes, the
pipeline contract's Worker Execute stage is the integration point for the
timeout handler.

## Operator Checkpoint

Operator authorized live execution and API key use 2026-05-29.

## Claim Boundary

EL-1 produces a pipeline contract and TypeScript interface. It does not claim
full autonomous pipeline execution, new provider semantics beyond existing
`executeReal()`, new receipt envelope schema, hosted readiness, production
readiness, or public release readiness.
