# CVF Phase 3 — Review CVF Closure Roadmap V2

Memory class: SUMMARY_RECORD

Status: READY_FOR_REBUTTAL

Date: 2026-05-19

Supersedes: `docs/roadmaps/CVF_PHASE3_REVIEW_CLOSURE_ROADMAP_2026-05-19.md`

Predecessor authority:
`docs/reviews/archive/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`
`docs/roadmaps/CVF_RUNTIME_MATURITY_DELTA_ROADMAP_V2_2026-05-19.md` (Phase 2 closed)

V1 Codex rebuttal: BLOCKING — 4 findings addressed in this V2:

1. `nextAllowedMove` in `ACTIVE_SESSION_STATE.json` stale — updated to authorize Phase 3 V2.
2. W1 originally planned to add stubs to `llm.adapter.interface.ts`, which is blocked by
   `new_provider_execution_semantics`. V2 bounds W1 to `CVF_MODEL_GATEWAY/src/` contract
   files only — no runtime adapter interface touch.
3. W2 source-fidelity wrong — governed-packs already exist with 3 artifacts each
   (`execution.policy.json`, `receipt.schema.json`, `workflow.spec.md`). V2 changes W2 to
   "complete existing governed-packs" by adding the missing `failure-recovery.ts` file to
   each of the 3 packs and creating a typed TypeScript registry (`WorkflowPackRegistry` +
   `getGovernedPack()` loader in `index.ts`).
4. W3 "governance benchmark live run" overclaims — no real audit JSONL exists in
   `docs/evidence/`. V2 renames to "offline 9-metric benchmark extension" and removes all
   live-proof language. The `cvf benchmark run` command reads any JSONL file provided via
   `--input` flag; live proof is not claimed.

---

## Purpose

Close the remaining open items from `Review CVF.md` that Phase 1 + Phase 2 did
not address. The reviewer's verdict: CVF has a Control System but lacks a
Governed Capability System. Phase 1–2 closed the control plane. Phase 3 closes
the capability surface at the bounded contract and artifact layer.

Three work streams run in parallel:

- **W1 — Provider Contract Completion (Problem D partial):** Add the 4 missing
  provider method contracts to `CVF_MODEL_GATEWAY/src/` only. Contract definition
  only — no provider implementation, no runtime adapter interface touch.
- **W2 — Governed-Pack Completion (Problem B core):** Complete the 3 existing
  governed packs (`strategy_analysis`, `documentation`, `app_builder_complete`)
  that already have `execution.policy.json`, `receipt.schema.json`, and
  `workflow.spec.md` — add the missing `failure-recovery.ts` to each pack and
  create a typed TypeScript registry (`WorkflowPackRegistry` interface +
  `getGovernedPack(templateId)` loader in `index.ts`).
- **W3 — Offline 9-Metric Benchmark Extension (Problem E completion):** Extend
  `governance-reliability-metrics.ts` from 4 metrics to 9 and add a `cvf benchmark
  run` subcommand to the CLI that reads any JSONL file via `--input` and outputs a
  9-metric governance reliability report.

---

## Scope / Target / Owner Boundary

In scope:

- **W1:** `EXTENSIONS/CVF_MODEL_GATEWAY/src/` — 4 new contract files only.
  **No touch to `CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/llm.adapter.interface.ts`**
  (blocked by `new_provider_execution_semantics`).
  No GC-018 required — pure contract + type guard, same pattern as D2, no enforcement
  surface change, no adapter interface modification.
- **W2:** `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/`
  (complete existing 3 packs: add `failure-recovery.ts` to each + create `index.ts`
  with typed registry); `src/types/workflow-pack.ts` (new `WorkflowPackRegistry` type).
  No route change. No execute path change. GC-018 required — new TypeScript governance
  artifact class introduced into cvf-web type system.
- **W3:** `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/governance-reliability-metrics.ts`
  — extend from 4 to 9 metrics; `src/command.registry.ts` — add `benchmark run`
  subcommand wiring. No GC-018 required — hardening of existing `benchmark` command,
  R0 scope (same as C2).

Out of scope:

- Provider implementation (no live AI call for reasoning/json_mode/embedding/tool_call)
- Adding stubs to `llm.adapter.interface.ts` (blocked by `new_provider_execution_semantics`)
- Modifying existing governed-pack `execution.policy.json`, `receipt.schema.json`, or
  `workflow.spec.md` files (complete only — no breaking changes)
- New template categories or new governed packs beyond the 3 target packs
- Persistent memory or memory reinjection
- Public-sync repo edits under this roadmap (separate sync step after closure)
- Marking Problems B/D/E globally `CLOSED_IMPLEMENTED` — per-slice closure only
- Live proof of governance benchmark (no real audit JSONL in `docs/evidence/`)

---

## Adjustment 1 Inventory (source-fidelity pre-scan)

### W1 — Provider Contract Completion

What exists in `CVF_MODEL_GATEWAY/src/`:

- `stream-contract.ts` (35 lines) — StreamRequest, StreamContract, isStreamContract
- `vision-contract.ts` (40 lines) — VisionRequest, VisionContract, isVisionContract (D2)
- `llm.adapter.interface.ts` (51 lines) — generate(), stream?(), vision?()

**Blocked surface (do NOT touch):** `llm.adapter.interface.ts` — blocked by
`new_provider_execution_semantics` in `blockedWorkClasses`. W1 does not add
`reasoning?`, `jsonMode?`, `toolCall?`, `embedding?` stubs to the adapter interface.

True gap (gateway contract files only):

- `reasoning()` — **missing** — no contract file
- `json_mode()` — **missing** — no contract file
- `tool_call()` — **missing** — no contract file
- `embedding()` — **missing** — no contract file

Net new contract files needed: `reasoning-contract.ts`, `json-mode-contract.ts`,
`tool-call-contract.ts`, `embedding-contract.ts`. All 4 in `CVF_MODEL_GATEWAY/src/`
only. Pattern mirrors `stream-contract.ts` and `vision-contract.ts`.

Done criterion:

- 4 new contract files (≤ 50 lines each), pattern mirrors `stream-contract.ts`
- All 4 exported from `index.ts`
- Test file per contract (≤ 60 lines each, 4–5 tests each)
- `npm test` PASS, `npm run check` PASS
- No modification to `llm.adapter.interface.ts`

### W2 — Governed-Pack Completion

What already exists in `cvf-web/src/lib/governed-packs/`:

- `app_builder_complete/execution.policy.json` — **exists**
- `app_builder_complete/receipt.schema.json` — **exists**
- `app_builder_complete/workflow.spec.md` — **exists**
- `documentation/execution.policy.json` — **exists**
- `documentation/receipt.schema.json` — **exists**
- `documentation/workflow.spec.md` — **exists**
- `strategy_analysis/execution.policy.json` — **exists**
- `strategy_analysis/receipt.schema.json` — **exists**
- `strategy_analysis/workflow.spec.md` — **exists**

True gap:

- No `failure-recovery.ts` in any of the 3 pack directories
- No `index.ts` — no typed TypeScript registry, no `getGovernedPack()` loader
- No `WorkflowPackRegistry` type defined anywhere

Done criterion:

- New `WorkflowPackRegistry` interface defined in
  `cvf-web/src/types/workflow-pack.ts` (≤ 60 lines) — references pack metadata,
  links to existing JSON/MD artifacts by path
- 3 `failure-recovery.ts` files created (≤ 50 lines each), one per pack directory,
  TypeScript so it can be imported and tested — pattern: `FailureRecoveryPolicy`
  interface + exported const with `packId`, `recoverySteps[]`, `escalationPath`
- `governed-packs/index.ts` exports `WorkflowPackRegistry`, `getGovernedPack(templateId)`,
  and all 3 pack failure-recovery policies
- 1 test file: `governed-packs/index.test.ts` (≤ 100 lines) — verifies pack lookup,
  registry completeness, failure recovery shape
- `npm run build` PASS, targeted `npm run test:run` PASS
- GC-018 filed before implementation begins

### W3 — Offline 9-Metric Benchmark Extension

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
  `--input <jsonl>` flag; no `run` subcommand

No live audit JSONL in `docs/evidence/`. The `cvf benchmark run` command reads
any JSONL file supplied via `--input <path>`. Live proof is not claimed. Tests
use an in-memory fixture JSONL string.

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
| W1 — Provider Contracts | No | Pure contract + type guard, gateway files only, no adapter interface touch, no enforcement surface change |
| W2 — Governed-Pack Completion | Yes | New TypeScript governance artifact class (`WorkflowPackRegistry`, `FailureRecoveryPolicy`) introduced into cvf-web type system |
| W3 — Benchmark Extension | No | Hardening of existing `benchmark` command, R0 scope (same as C2) |

GC-018 path for W2: `docs/baselines/CVF_GC018_W2_GOVERNED_PACK_COMPLETION_2026-05-19.md`

---

## Execution Sequence

W1 and W3 start immediately (no GC-018). W2 starts after GC-018 accepted.

```text
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
| B — Skill → Workflow Pack | Foundation only | `W2_GOVERNED_PACK_CLOSED` — 3 existing packs completed with failure-recovery + typed registry |
| C — CLI Runtime | CLOSED (Phase 2) | CLOSED (unchanged) |
| D — Provider Parity | D1+D2 only | `D3_D6_PROVIDER_CONTRACTS_CLOSED` — gateway contracts only; adapter stubs remain out of scope |
| E — Benchmark | 4 metrics, no `run` subcommand | `E_OFFLINE_BENCHMARK_CLOSED` — 9 metrics, `cvf benchmark run` subcommand |
| F — Noncoder UX | Component exists | `F_NONCODER_UX_CLOSED` — OutcomeQuickActions backed by existing governed packs |
| G — Execution Identity | CLOSED (Phase 2) | CLOSED (unchanged) |
| H — Memory Runtime | CLOSED (Phase 2) | CLOSED (unchanged) |

All 8 Review CVF problems are addressed at the bounded contract and artifact
layer. Provider execution, workflow runtime, and live capability intake are
explicitly out of scope for Phase 3.

---

## Non-Goals

Non-goals for Phase 3:

- Provider implementation (no live reasoning/embedding/tool_call call authorized)
- Adding stubs to `llm.adapter.interface.ts` (blocked by `new_provider_execution_semantics`)
- New governed packs or template categories beyond the 3 existing target packs
- Capability Intake Pipeline (external skill ingestion) — separate phase,
  requires separate demand gate and product decision
- Persistent or archive memory
- Public catalog update (separate governed sync step after Phase 3 closure)
- Marking B/D/E globally `CLOSED_IMPLEMENTED` at problem level
- Live governance benchmark proof (no real audit JSONL exists; offline only)

---

## Work Plan

| Step | Stream | Prerequisite | Target repo |
|---|---|---|---|
| 1a | W1 — Provider Contracts | None | CVF governance repo (MODEL_GATEWAY) |
| 1b | W3 — Benchmark Extension | None | CVF governance repo (CLI extension) |
| 2 | W2 — Governed-Pack Completion | GC-018 accepted | CVF governance repo (cvf-web lib) |

---

## Acceptance Criteria

- [ ] W1: 4 new contract files in `CVF_MODEL_GATEWAY/src/` (≤ 50 lines each); 4 type guards correct; all 4 exported from `index.ts`; `npm test` PASS (existing + new); `npm run check` PASS; `llm.adapter.interface.ts` NOT modified
- [ ] W2: `WorkflowPackRegistry` + `FailureRecoveryPolicy` types defined; 3 `failure-recovery.ts` files (one per pack, ≤ 50 lines each); `governed-packs/index.ts` with `getGovernedPack(templateId)` loader; `npm run build` PASS; targeted `npm run test:run` PASS; existing JSON/MD pack artifacts NOT modified
- [ ] W3: `GovernanceReliabilityReport` gains 9 metrics; `computeGovernanceReliabilityReport` computes all 9; `cvf benchmark run --input <path>` command works; `governance-reliability-metrics.ts` ≤ 180 lines; `npm test` PASS; `npm run check` PASS

---

## Verification / Evidence

Each work stream completion review must include:

1. `npm test` or `npm run test:run` output — all tests PASS including new
2. `npm run check` or `npm run build` output — PASS
3. Line count proof for all governed files
4. W1: Confirmation that `llm.adapter.interface.ts` was NOT modified (grep or line count diff showing 51 lines unchanged)
5. W2: Confirmation that existing JSON/MD artifacts were NOT modified; import graph showing `index.ts` loads without circular deps
6. W3: Sample `cvf benchmark run` stdout showing all 9 metrics

---

## Authorization / Decision

Authority: Orchestrator role (Claude), 2026-05-19.

Predecessor authority chain:

- `docs/reviews/archive/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md` —
  operator-approved strategic anchor; established 3 required adjustments and
  the correct next-phase sequence.
- `docs/roadmaps/CVF_RUNTIME_MATURITY_DELTA_ROADMAP_V2_2026-05-19.md` —
  Phase 2 closed (M1/C2/D2/H2). Phase 3 is the direct continuation.
- `docs/roadmaps/CVF_PHASE3_REVIEW_CLOSURE_ROADMAP_2026-05-19.md` (V1) —
  superseded by this V2 after Codex BLOCKING rebuttal with 4 findings.

This roadmap is filed READY_FOR_REBUTTAL. Codex must return a verdict
(no-blocking or blocking findings) before GC-018 is filed for W2 or any
implementation begins.

W1 and W3 do not require GC-018. They may be implemented after Codex returns
a no-blocking verdict on this roadmap. W2 requires GC-018 filed and accepted
before Worker implementation begins.

Operator direction (2026-05-19): close all 8 Review CVF pain points — "chưa
có thì chúng ta tìm giải pháp." This roadmap is the V2 solution design for
the three remaining open problems (B/D/E) and their downstream (F), with
all 4 Codex blocking findings incorporated.

---

## Claim Boundary

This roadmap covers W1 (4 provider method gateway contracts), W2 (complete
existing governed-packs with failure-recovery + typed registry), and W3
(offline 9-metric benchmark CLI extension). It does not authorize provider
execution, adapter interface stub additions, Capability Intake Pipeline, new
governed pack creation, memory reinjection, or public-sync edits.

After Phase 3 closes, all 8 Review CVF problems are addressed at the bounded
contract and artifact layer. Provider execution, workflow runtime, and
capability intake remain explicitly out of scope — they are Phase 4 items
requiring a separate product decision and demand gate.
