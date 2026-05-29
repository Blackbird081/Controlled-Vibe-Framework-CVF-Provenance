# CVF Delta CLI/MCP Wire-In Roadmap

Memory class: SUMMARY_RECORD

Status: ACTIVE

docType: roadmap

Date: 2026-05-29

---

## Authorization / Decision

Authorized by operator direction 2026-05-29. Closes the verified gap between
CVF's existing MCP governance layer (14 read-only tools) and CLI execution
layer — specifically the "MCP điều khiển CLI" architecture described in
`.private_reference/legacy/CVF 28.05/CLI & MCP.md`.

Fresh GC-018:
`docs/baselines/CVF_GC018_DELTA_CLI_MCP_WIREIN_2026-05-29.md`

Dispatch status: D1 CLOSED_PASS_BOUNDED (commit 478e2de6). D2 READY_FOR_IMPLEMENTATION (operator authorized 2026-05-29; security boundary doc required before code). D3 READY_FOR_IMPLEMENTATION (operator authorized 2026-05-29; D2 CLOSED_PASS + sandbox spec required before code).

## Verified Gap

At HEAD `8b1f5992`, source review confirmed:

- `pipeline-chain-orchestrator.ts` (EL-1): contract + types exist, **not
  imported anywhere** in the app outside its test file.
- `route.ts` (1000 lines, at hard limit): **no pipeline reference**.
- MCP server (14 tools, 551 lines): all tools are **read-only**; no write,
  submit, or CLI-invocation tool exists.
- `runCli()` in MCP SDK: exists but **not exposed** via any MCP tool.

## Purpose

Wire the three layers together per the CVF 28.05 design intent:

```
MCP (governance/guard) ──controls──► CLI (execution plane)
     ↑                                      ↓
  Reviewer/Closure                     Worker/Orchestrator
  submit receipts                     execute pipeline stages
```

Three phases — each bounded, sequentially gated:

- **D1** — Pipeline Chain Readout in `/api/execute` (additive code, R1)
- **D2** — MCP Write/Submit Tools (write-path tools, R2, DEMAND_GATED)
- **D3** — MCP → CLI Bridge (process spawning, R2/R3, DEMAND_GATED)

## Scope / Target / Owner Boundary

Target: three implementation tranches wiring the existing MCP governance layer
and CLI execution plane together. Owner: CVF execution surface and MCP server.

Allowed per tranche: see individual work orders. No public-sync repo.
D1 allowed: `pipeline-chain-readout.ts` (new) + `route.ts` additive import +
new test file. D2 allowed: MCP server new tools + tests. D3 allowed: MCP server
`cvf_invoke_cli_stage` + sandbox wrapper + integration test.

## Authority Chain

- GC-018: `docs/baselines/CVF_GC018_DELTA_CLI_MCP_WIREIN_2026-05-29.md`
- EL-1 contract: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts`
  — contract version `cvf.pipelineChainOrchestrator.el1.v1` (line 11 comment)
- MCP server: `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts`
- Source design intent: `.private_reference/legacy/CVF 28.05/CLI & MCP.md`
- Cross-agent memory roadmap: `docs/roadmaps/CVF_CROSS_AGENT_MEMORY_PROGRESSION_ROADMAP_2026-05-26.md`
  — Delta production hardening cited as parked

## Critical Constraint — route.ts Hard Limit

`route.ts` is at exactly 1000 lines (hard limit for `general_source` class).
**D1 cannot add lines directly to `route.ts`.** Implementation must extract a
`pipeline-chain-readout.ts` module and import it — keeping `route.ts` net-zero
or shrinking it. This is a pre-implementation design decision locked in D1 work
order.

---

## D1 — Pipeline Chain Readout in /api/execute

**Risk:** R1 — additive readout; same pattern as VI1/VI2/VI3/VI4.

**Gap closed:** EL-1 `PipelineChainState` types exist but are never returned
in any API response. Orchestrators and external agents calling `/api/execute`
have no visibility into pipeline stage state.

**Deliverables:**

1. New module: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-readout.ts`
   — builds `pipelineChainReadout` using `createPipelineState()` + infers
   stage from existing `workflowStateMachine` fields already in the response
2. `route.ts`: import and add `pipelineChainReadout` field to response
   (net-zero via extraction, no line count increase)
3. New tests: `route.pipeline-chain-readout.test.ts`
4. Session continuity update

**Contract version:** `cvf.pipelineChainReadout.delta.d1.v1`

**Response fields added:**

```typescript
pipelineChainReadout: {
  contractVersion: 'cvf.pipelineChainReadout.delta.d1.v1';
  currentStage: PipelineStage;           // derived from workflow state
  running: boolean;
  workerRetryCount: number;
  reviewerRetryCount: number;
  humanInterventionRequired: boolean;
  runtimeExecutionAuthorized: false;     // advisory only
}
```

Gate: None — open after GC-018.

---

## D2 — MCP Write/Submit Tools

**Risk:** R2 — write-path MCP tools require security boundary review.

**Status:** DEMAND_GATED. Operator must authorize after D1 CLOSED_PASS.

**Gap closed:** MCP Reviewer/Closure Gate agents cannot submit receipts through
the governance control plane — they must bypass it. Per `CLI & MCP.md`:
"Reviewer không tự viết file báo cáo, mà nó phải gọi Tool
`cvf_submit_review_receipt()` qua MCP."

**Deliverables (pending authorization):**

1. `cvf_submit_review_receipt` MCP tool — accepts structured review receipt,
   validates against governance schema, writes to audit store
2. `cvf_advance_pipeline_stage` MCP tool — accepts current state + stage result,
   calls `advancePipelineStage()`, returns updated state
3. MCP tests for both tools
4. Security boundary document: what agents can call these tools, what
   input validation is enforced, what audit trail is created

**Pre-authorization requirements:**

- D1 CLOSED_PASS
- Security review of write-path MCP tools
- Operator explicit authorization
- Fresh pre-dispatch gate run

Gate: DEMAND_GATED (D1 must close first).

---

## D3 — MCP → CLI Bridge

**Risk:** R2/R3 — process spawning, sandbox design required.

**Status:** DEMAND_GATED. Do not dispatch without full sandbox boundary design.

**Gap closed:** `runCli()` exists in MCP SDK but is never exposed via any tool.
Per `CLI & MCP.md` architecture, Orchestrator and Worker agents should receive
work orders and invoke CLI execution through the governed MCP surface.

**Deliverables (pending authorization):**

1. Sandbox boundary specification document (must come before any code)
2. `cvf_invoke_cli_stage` MCP tool — invokes `runCli()` with governed
   constraints: timeout, sandbox flag, allowed commands whitelist
3. Worker isolation design: each invocation is sandboxed, logs captured,
   no cross-invocation state leakage
4. Integration test: full Operator → Intake → Orchestrator → Worker (CLI) →
   Reviewer (MCP submit) → Closure flow on one existing workflow

**Pre-authorization requirements:**

- D2 CLOSED_PASS
- Sandbox boundary specification reviewed and approved
- Process-spawning security review
- Operator explicit authorization

Gate: DEMAND_GATED (D2 must close first).

---

## Non-Goals (all phases)

- Automatic provider routing or model selection
- Cross-session memory reinjection
- Public SaaS hosting or production release
- Broad multi-user transport or remote MCP deployment
- Any tranche beyond D3 without a fresh roadmap and GC-018

## Work Plan

| Tranche | Deliverable | Risk | Gate |
| --- | --- | --- | --- |
| D1 | Pipeline chain readout in `/api/execute` | R1 | None — open |
| D2 | MCP write/submit tools | R2 | DEMAND_GATED (D1 closed + operator auth) |
| D3 | MCP → CLI bridge + sandbox | R2/R3 | DEMAND_GATED (D2 closed + sandbox spec + operator auth) |

## Acceptance Criteria

- [ ] D1: `pipelineChainReadout` in `/api/execute` response; `route.ts` net-zero lines; tests PASS; live proof receipt
- [ ] D2: `cvf_submit_review_receipt` + `cvf_advance_pipeline_stage` MCP tools; security review PASS; MCP tests PASS
- [ ] D3: sandbox boundary spec approved; `cvf_invoke_cli_stage` implemented; integration flow E2E test PASS

## Verification

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 8b1f5992 --head <delta-commit> --enforce
python governance/compat/check_markdown_structural_completeness.py --base 8b1f5992 --head <delta-commit> --enforce
python governance/compat/check_docs_governance_compat.py --base 8b1f5992 --head <delta-commit> --enforce
```

## Claim Boundary

This roadmap does not claim that sandboxed terminal execution is designed or
safe, that MCP write tools are security-reviewed, that the CLI/MCP architecture
is production-ready, or that any hosted/public readiness is achieved.
D1 closure claim is bounded to additive readout only.
