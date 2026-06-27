# CVF GC-018 — Delta CLI/MCP Wire-In

Memory class: FULL_RECORD

Status: ACTIVE

docType: gc018_baseline

Date: 2026-05-29

---

## Purpose

Authorize Delta CLI/MCP Wire-In: three-phase roadmap closing the gap between
CVF's existing MCP governance layer and CLI execution layer — specifically,
wiring `pipeline-chain-orchestrator.ts` (EL-1 contract) into the execution
surface so Orchestrators can observe pipeline stage state, and wiring MCP
write tools so Reviewer/Closure Gate agents can submit receipts through the
governance control plane rather than bypassing it.

This GC-018 covers the full roadmap authorization. Each phase requires its
own fresh pre-dispatch gate run before implementation begins.

---

## Background — Verified Gap

Source: `.private_reference/legacy/CVF 28.05/CLI & MCP.md` — design intent
for MCP as governance/guard layer + CLI as execution plane.

Verified at HEAD `8b1f5992`:

| Component | Expected | Actual |
| --- | --- | --- |
| `pipeline-chain-orchestrator.ts` | Wired into execution route | Contract + types only; **zero imports** in app outside test file |
| `route.ts` (1000 lines) | Exposes `pipelineChain` readout | No pipeline reference whatsoever |
| MCP server (14 tools) | Includes write/submit tools | All 14 tools are **read-only** governance queries |
| `cvf_submit_review_receipt` | Present as MCP tool | Not implemented |
| MCP → CLI invocation | Present | `runCli()` in SDK but **not exposed** via any MCP tool |

---

## Scope — Three Phases

### Phase 1 (WORK_ORDER_READY) — Pipeline Chain Readout in /api/execute

Documentation + additive code: add `pipelineChainReadout` field to
`/api/execute` response using existing `PipelineChainState` types from
`pipeline-chain-orchestrator.ts`. No new runtime enforcement. Pure readout
extension — same pattern as VI1/VI2/VI3/VI4.

Allowed: `route.ts` additive field only; `route.ts` tests; session continuity.
Forbidden: new MCP tools, sandboxed execution, write/submit tools.

### Phase 2 (DEMAND_GATED) — MCP Submit/Write Tools

Add `cvf_submit_review_receipt` and `cvf_invoke_pipeline_stage` write tools
to MCP server. These are write-path tools requiring security review — higher
risk than Phase 1.

Allowed: `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` new tools;
MCP tests; session continuity.
Forbidden: sandboxed terminal execution, process spawning, provider calls.

### Phase 3 (DEMAND_GATED) — MCP → CLI Bridge

Wire MCP `cvf_invoke_pipeline_stage` tool to actually invoke the CVF CLI
execution plane via `runCli()`. This is the true "MCP controls CLI" wire-up.
Highest risk — spawns processes, requires sandbox boundary design.

---

## Source Verification

| Surface | File | Key symbol | Status |
| --- | --- | --- | --- |
| `PipelineChainState` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts` | line 173 | VERIFIED |
| `PipelineStage` type | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts` | line 21 | VERIFIED |
| `advancePipelineStage()` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts` | line 257 | VERIFIED |
| `handleWorkerTimeout()` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts` | line 348 | VERIFIED |
| `handleReviewDeadlock()` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts` | line 419 | VERIFIED |
| Contract version | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pipeline-chain-orchestrator.ts` | line 11 comment | `cvf.pipelineChainOrchestrator.el1.v1` |
| `route.ts` line count | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | 1000 lines | AT HARD LIMIT — Phase 1 must split or use import |
| MCP server tool count | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | 14 tools, 551 lines | VERIFIED |
| `runCli()` in MCP SDK | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/cli.ts` | line 290 | VERIFIED — not exposed |

---

## Critical Constraint — route.ts at Hard Limit

`route.ts` is at exactly 1000 lines — the hard limit per GC-023 for
`general_source`. Phase 1 **cannot add lines to `route.ts` directly**. The
implementation must either:
1. Extract a `pipeline-chain-readout.ts` helper module and import into route.ts
   (no net line increase in route.ts), or
2. Obtain an exception registry entry for route.ts before adding any lines.

This constraint is a pre-implementation blocker and must be resolved in the
work order before any code is written.

---

## Risk Classification

- Phase 1: R1 — additive route readout; bounded by existing EL-1 types
- Phase 2: R2 — write/submit MCP tools; requires security boundary review
- Phase 3: R2/R3 — process spawning; requires full sandbox design before dispatch

---

## Decision

Delta CLI/MCP Wire-In is authorized at Phase 1 immediately. Phase 2 and Phase 3
are DEMAND_GATED — operator must explicitly unblock each before dispatch.

baseHead: `8b1f5992`

---

## Verification

```powershell
python governance/compat/check_work_order_dispatch_quality.py --base 8b1f5992 --head <delta-commit> --enforce
python governance/compat/check_markdown_structural_completeness.py --base 8b1f5992 --head <delta-commit> --enforce
python governance/compat/check_docs_governance_compat.py --base 8b1f5992 --head <delta-commit> --enforce
```

---

## Claim Boundary

This GC-018 authorizes the roadmap and Phase 1 implementation only. It does
not claim that Phase 2 or Phase 3 are safe to implement without further review,
that sandboxed terminal execution is designed or tested, that MCP write tools
are security-reviewed, or that any production/hosted readiness is achieved.
