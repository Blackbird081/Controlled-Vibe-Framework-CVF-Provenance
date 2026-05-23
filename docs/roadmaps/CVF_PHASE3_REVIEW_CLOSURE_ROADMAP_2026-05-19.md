# CVF Phase 3 — Review CVF Closure Roadmap

Memory class: SUMMARY_RECORD

Status: READY_FOR_REBUTTAL

Date: 2026-05-19

Predecessor authority:
`docs/reviews/archive/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`
`docs/roadmaps/CVF_RUNTIME_MATURITY_DELTA_ROADMAP_V2_2026-05-19.md` (Phase 2 closed)

---

## Purpose

Close the remaining open items from `Review CVF.md` that Phase 1 + Phase 2 did
not address. The reviewer's verdict: CVF has a Control System but lacks a
Governed Capability System. Phase 1–2 closed the control plane. Phase 3 closes
the capability surface.

Three work streams run in parallel:

- **W1 — Provider Method Parity (Problem D completion):** Add the remaining
  provider method contracts to `CVF_MODEL_GATEWAY` so the adapter layer covers
  the full method surface the Review identified. Contract definition only — no
  provider implementation.
- **W2 — Workflow Pack System (Problem B core):** Add a `WorkflowPack`
  governance layer to the 3 existing high-use templates (`strategy_analysis`,
  `documentation`, `app_builder_complete`). Each pack gets a machine-readable
  spec, execution policy, receipt schema, and failure recovery record. The
  `Template` type gains optional `workflowPack` field — no breaking change.
- **W3 — Governance Benchmark Live Run (Problem E completion):** Extend
  `governance-reliability-metrics.ts` from 4 metrics to 9. Add `cvf benchmark
  run` command to the CLI. The command reads a JSONL audit log from
  `docs/evidence/` and outputs a governance reliability report covering all 9
  Review-required metrics.

---

## Scope / Target / Owner Boundary

In scope:

- **W1:** `EXTENSIONS/CVF_MODEL_GATEWAY/src/` — new contract files only;
  `CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/llm.adapter.interface.ts` — stubs only.
  No GC-018 required (same pattern as D2, pure contract + type guard, no
  enforcement surface change).
- **W2:** `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/workflow-packs/`
  (new directory); `src/types/index.ts` — optional `workflowPack` field added.
  No route change. No execute path change. GC-018 required — new governance
  artifact class introduced.
- **W3:** `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`
  — extend metrics; `src/command.registry.ts` — add `benchmark run` subcommand
  wiring. No GC-018 required — hardening of existing `benchmark` command, R0
  scope (same as C2).

Out of scope:

- Provider implementation (no live AI call for reasoning/json_mode/embedding/tool_call)
- Modifying existing template `intentPattern` or `outputTemplate` fields
- New template categories or new templates beyond the 3 target packs
- Persistent memory or memory reinjection
- Public-sync repo edits under this roadmap (separate sync step after closure)
- Marking Problems B/D/E globally `CLOSED_IMPLEMENTED` — per-slice closure only

---

## Adjustment 1 Inventory (source-fidelity pre-scan)

### W1 — Provider Method Parity

What exists in `CVF_MODEL_GATEWAY/src/`:

- `stream-contract.ts` (35 lines) — StreamRequest, StreamContract, isStreamContract
- `vision-contract.ts` (40 lines) — VisionRequest, VisionContract, isVisionContract — just delivered (D2)
- `llm.adapter.interface.ts` (51 lines) — generate(), stream?(), vision?()

True gap (Review Problem D requires):

- `complete()` → covered by `generate()` — **already exists, no action needed**
- `stream()` → D1 done — **exists**
- `vision()` → D2 done — **exists**
- `reasoning()` → **missing** — no contract, no stub
- `json_mode()` → **missing** — no contract, no stub
- `tool_call()` → **missing** — no contract, no stub
- `embedding()` → **missing** — no contract, no stub
- `retry()` → handled by `fallback-policy.ts` at gateway level — **covered**
- `receipt()` → handled by `gateway-receipt.ts` — **covered**
- `cost()` → **missing** — no contract
- `risk()` → handled by `gateway-policy.ts` risk scoring — **partially covered**

Net new contracts needed: `reasoning-contract.ts`, `json-mode-contract.ts`,
`tool-call-contract.ts`, `embedding-contract.ts`. Cost and risk are gateway-
level concerns already covered; no new files needed for those.

Done criterion:

- 4 new contract files (≤ 50 lines each), pattern mirrors `stream-contract.ts`
- `LLMAdapter` gains 4 new optional stubs (`reasoning?`, `jsonMode?`, `toolCall?`, `embedding?`)
- `llm.adapter.interface.ts` ≤ 75 lines after additions
- All 4 exported from `index.ts`
- Test file per contract (≤ 60 lines each, 4–5 tests each)
- `npm test` PASS, `npm run check` PASS

### W2 — Workflow Pack System

What exists:

- `Template` interface in `src/types/index.ts` (18–34 lines): `id`, `name`,
  `category`, `fields`, `intentPattern`, `outputExpected`, `outputTemplate`,
  `sampleOutput`, `difficulty` — **no governance pack fields**
- 3 target templates in v1.5 `templates.ts`:
  - `strategy_analysis` (business.ts in v1.6) — full `intentPattern` +
    `outputExpected` + `outputTemplate` + `sampleOutput` + `difficulty: medium`
  - `documentation` — full template definition (line 211)
  - `app_builder_complete` — full template definition (line 1032)
- `CVF_v1.2_CAPABILITY_EXTENSION/` — `SKILL_CONTRACT_SPEC.md`,
  `EXTERNAL_SKILL_INGESTION_RULES.md` — docs only, no executable schema
- `CVF_ECO_v3.0_TASK_MARKETPLACE/` — marketplace runtime code, no workflow packs

True gap:

- No `workflow.spec.md`, `execution.policy.json`, `receipt.schema.json`,
  `failure.recovery.md` exists for any template
- `Template` type has no field to reference a workflow pack
- No `WorkflowPack` type defined anywhere

Done criterion:

- New `WorkflowPack` interface defined in
  `cvf-web/src/types/workflow-pack.ts` (≤ 80 lines)
- `Template` interface gains optional `workflowPack?: WorkflowPackRef` — no
  breaking change; existing templates work without it
- 3 workflow pack directories created under
  `cvf-web/src/lib/workflow-packs/`:
  - `strategy-analysis/` — `workflow.spec.ts`, `execution-policy.ts`,
    `receipt-schema.ts`, `failure-recovery.ts`
  - `documentation/` — same 4 files
  - `app-builder-complete/` — same 4 files
- Each pack file is TypeScript (not JSON/markdown) so it can be imported,
  typed, and tested — aligns with existing codebase conventions
- `workflow-packs/index.ts` exports all 3 packs + `getWorkflowPack(templateId)`
- 1 test file: `workflow-packs/index.test.ts` (≤ 100 lines) — verifies pack
  shape, required fields, policy consistency
- `npm run build` PASS, `npm run test:run` PASS
- GC-018 filed before implementation begins

### W3 — Governance Benchmark Live Run

What exists in `CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`:

- 94 lines, 4 metrics: `receiptIntegrityRate`, `policyDecisionRate`,
  `stepTraceCompletionRate`, `auditEventCaptureRate`
- `parseAuditJsonl(content)` already implemented
- `computeGovernanceReliabilityReport()` already implemented (4 metrics)

What exists in `command.registry.ts`:

- `benchmark` command at line 135 — calls `benchmarkCommand()` which calls
  `computeGovernanceReliabilityReport` on parsed JSONL

True gap (Review requires 9 metrics):

- **Have:** receipt integrity, policy decision, step trace completion, audit
  event capture (4/9)
- **Missing:** task completion rate, retry/recovery rate, policy violation rate,
  cross-session continuity rate, deterministic consistency rate (5/9)
- `benchmark run` subcommand does not exist — current `cvf benchmark` takes
  `--input <jsonl>` flag; no `run` subcommand with live execute path

Done criterion:

- `governance-reliability-metrics.ts` gains 5 new metric functions:
  `taskCompletionRate`, `retryRecoveryRate`, `policyViolationRate`,
  `crossSessionContinuityRate`, `deterministicConsistencyRate`
- `GovernanceReliabilityReport` interface gains all 5 new fields
- `computeGovernanceReliabilityReport()` includes all 9 metrics
- `governance-reliability-metrics.ts` ≤ 180 lines after additions
- 5 new tests added to existing test file (≤ 220 lines total)
- `cvf benchmark run --input <path>` subcommand added to `command.registry.ts`
  — reads JSONL, runs `computeGovernanceReliabilityReport`, outputs markdown
  or JSON report to stdout
- `npm test` PASS (all existing + 5 new), `npm run check` PASS

---

## GC-018 Requirements

| Stream | GC-018 required | Reason |
|---|---|---|
| W1 — Provider Contracts | No | Pure contract + type guard, same pattern as D2, no enforcement surface change |
| W2 — Workflow Packs | Yes | New governance artifact class (`WorkflowPack`) introduced into cvf-web type system |
| W3 — Benchmark Extension | No | Hardening of existing `benchmark` command, R0 scope (same as C2) |

GC-018 path for W2: `docs/baselines/CVF_GC018_W2_WORKFLOW_PACK_SYSTEM_2026-05-19.md`

---

## Execution Sequence

W1 and W3 start immediately (no GC-018). W2 starts after GC-018 accepted.

```
W1 (Provider Contracts) ────────────────────────────────► CLOSED
W3 (Benchmark Extension) ───────────────────────────────► CLOSED
W2 (GC-018) ─────────────────────────────────────────────► CLOSED
```

---

## Review CVF Closure Map

After Phase 3 completes:

| Problem | Before Phase 3 | After Phase 3 |
|---|---|---|
| A — Internal Coherence | CLOSED_VERIFIED | CLOSED_VERIFIED (unchanged) |
| B — Skill → Workflow Pack | Foundation only | `W2_WORKFLOW_PACK_CLOSED` — 3 packs with full 4-artifact set |
| C — CLI Runtime | CLOSED (Phase 2) | CLOSED (unchanged) |
| D — Provider Parity | D1+D2 only | `D3_D6_PROVIDER_CONTRACTS_CLOSED` — 7/11 methods covered; cost/risk/retry covered by gateway |
| E — Benchmark | 4 metrics, no live run | `E_GOVERNANCE_BENCHMARK_CLOSED` — 9 metrics, live CLI run |
| F — Noncoder UX | Component exists | `F_NONCODER_UX_CLOSED` — OutcomeQuickActions backed by W2 workflow packs |
| G — Execution Identity | CLOSED (Phase 2) | CLOSED (unchanged) |
| H — Memory Runtime | CLOSED (Phase 2) | CLOSED (unchanged) |

---

## Non-Goals

Non-goals for Phase 3:

- Provider implementation (no live reasoning/embedding/tool_call call authorized)
- New template categories or template creation beyond the 3 target packs
- Capability Intake Pipeline (external skill ingestion) — separate phase,
  requires separate demand gate and product decision
- Persistent or archive memory
- Public catalog update (separate governed sync step after Phase 3 closure)
- Marking B/D/E globally `CLOSED_IMPLEMENTED` at problem level

---

## Work Plan

| Step | Stream | Prerequisite | Target repo |
|---|---|---|---|
| 1a | W1 — Provider Contracts | None | CVF governance repo (MODEL_GATEWAY) |
| 1b | W3 — Benchmark Extension | None | CVF governance repo (CLI extension) |
| 2 | W2 — Workflow Packs | GC-018 accepted | CVF governance repo (cvf-web lib) |

---

## Acceptance Criteria

- [ ] W1: 4 new contract files in `CVF_MODEL_GATEWAY/src/` (≤ 50 lines each); 4 type guards correct; `llm.adapter.interface.ts` ≤ 75 lines; all 4 exported from `index.ts`; `npm test` PASS (existing + new); `npm run check` PASS
- [ ] W2: `WorkflowPack` type defined; 3 packs (strategy_analysis, documentation, app_builder_complete) with `workflow.spec + execution-policy + receipt-schema + failure-recovery` (4 TS files each); `Template` type gains optional `workflowPack?` field; `npm run build` PASS; `npm run test:run` PASS
- [ ] W3: `GovernanceReliabilityReport` gains 9 metrics; `computeGovernanceReliabilityReport` computes all 9; `cvf benchmark run --input <path>` command works; `governance-reliability-metrics.ts` ≤ 180 lines; `npm test` PASS; `npm run check` PASS

---

## Verification / Evidence

Each work stream completion review must include:

1. `npm test` or `npm run test:run` output — all tests PASS including new
2. `npm run check` or `npm run build` output — PASS
3. Line count proof for all governed files
4. Confirmation: no provider implementation in W1, no HTTP call, no image fetch
5. W2: import graph showing workflow packs load without circular deps
6. W3: sample `cvf benchmark run` output showing all 9 metrics

---

## Authorization / Decision

Authority: Orchestrator role (Claude), 2026-05-19.

Predecessor authority chain:

- `docs/reviews/archive/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md` —
  operator-approved strategic anchor; established 3 required adjustments and
  the correct next-phase sequence.
- `docs/roadmaps/CVF_RUNTIME_MATURITY_DELTA_ROADMAP_V2_2026-05-19.md` —
  Phase 2 closed (M1/C2/D2/H2). Phase 3 is the direct continuation.

This roadmap is filed READY_FOR_REBUTTAL. Codex must return a verdict
(no-blocking or blocking findings) before GC-018 is filed for W2 or any
implementation begins.

W1 and W3 do not require GC-018. They may be implemented after Codex returns
a no-blocking verdict on this roadmap. W2 requires GC-018 filed and accepted
before Worker implementation begins.

Operator direction (2026-05-19): close all 8 Review CVF pain points — "chưa
có thì chúng ta tìm giải pháp." This roadmap is the solution design for the
three remaining open problems (B/D/E) and their downstream (F).

---

## Claim Boundary

This roadmap covers W1 (4 provider method contracts), W2 (3 workflow packs as
TypeScript governance artifacts), and W3 (9-metric benchmark CLI). It does not
authorize provider execution, Capability Intake Pipeline, new template creation,
memory reinjection, or public-sync edits.

After Phase 3 closes, all 8 Review CVF problems are addressed at the contract
and governance layer. The remaining open frontier (Capability Intake Pipeline,
external skill certification) is a Phase 4 item requiring a separate product
decision and demand gate.
