# CVF Runtime Maturity Roadmap — C / D / H + Maika AI Proof

Memory class: SUMMARY_RECORD

Status: READY_FOR_REBUTTAL — filed by Orchestrator role 2026-05-19.
No Worker implementation may begin before the Reviewer-role rebuttal returns
no-blocking findings and each GC-018-required candidate has its GC-018 filed.

> Status update 2026-05-20: REPLACED_BY_META. This roadmap is superseded by
> docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md per Claude rebuttal
> NON_BLOCKING_WITH_PER_SLICE_GATING. BLOCKING_FINDINGS from
> docs/reviews/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md
> remain load-bearing on each slice. Do not file GC-018 against this
> roadmap; use the meta-roadmap's per-slice gates instead.

Predecessor authority:
`docs/reviews/archive/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`
(Section: "Candidate post-decision implementation lanes", Problems C/D/H)

---

## Purpose

Close the three remaining open problems from the Adjustment 1 assessment
(`CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`): C (CLI execution
gateway), D (provider reasoning/vision contracts), and H (memory runtime
enforcement). Adds Maika AI daily-summary as the named consuming use case that
satisfies the demand-gate conditions for C and D.

---

## Scope / Target / Owner Boundary

In scope:

- **C — CLI Execution Gateway:** `cvf run/execute` as a CLI entry point backed
  by the governed `/api/execute` path, with Maika AI daily-summary generation
  as the named consuming use case.
- **D — Provider Method Parity:** `reasoning()` and `vision()` method contracts
  in `CVF_MODEL_GATEWAY`, extending Lane D's `stream-contract.ts`. Demand-gated
  on Maika vision use case (daily report photo description).
- **H — Memory Runtime:** Wire `MemoryTierOwner` policy check and
  `MemoryReinjectionPolicy` enforcement into the `/api/execute` live path for
  the `session` tier already captured by `buildRouteAuditMemoryCapture()`.
- **Maika AI Proof:** Supabase Edge Function `generate-daily-summary` in the
  Nha tre Maika workspace — calls CVF governed execution path, provides
  real-user evidence for C and D consuming use cases.

Out of scope:

- Replacing or modifying `MEMORY_TIER_OWNER_POLICIES` contract definitions
  (Phase D contracts are frozen — this roadmap only wires them into runtime).
- New CVFRole taxonomy or RBAC changes.
- Full Agent OS, multi-tenant cloud, or streaming SSE route implementation.
- Maika application features beyond the AI daily-summary Edge Function and
  optional photo-description feature.
- Public-sync promotion of Maika source code.

Owner: Orchestrator role files GC-018s and work orders; Worker role implements
per work order; Reviewer role rebuts each candidate independently.

---

## Authorization / Decision

Operator direction 2026-05-19: build Maika AI features as parallel track,
use Maika as consuming use case to unlock CVF D and H demand gates.

Assessment baseline:
`docs/reviews/archive/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`

Demand-gate conditions now satisfied:

| Gap | Required condition | Satisfying artifact |
| --- | --- | --- |
| C — CLI gateway | Named use case | Maika `generate-daily-summary` edge function calls CVF `/api/execute` |
| D — vision method | Named vision use case | Maika daily report photo → AI description |
| H — memory runtime | Flow that writes memory | `buildRouteAuditMemoryCapture()` at route.ts step 7 already writes `session` tier |

---

## Why This Tranche

**The central claim of the Assessment baseline** (2026-05-18) was:

> CVF has a Control System but not a Governed Capability System.

Phase A–G addressed this for the governed execute chain and actor-role gate.
C/D/H are the three remaining gaps before CVF can claim a complete Runtime
Maturity tier:

- **C** closes the CLI surface gap — CVF's governed execution is only reachable
  via the Next.js web route. No programmatic, CI, or edge-function entry point
  exists. Adding `cvf run/execute` makes CVF callable from any context.
- **D** closes the provider method parity gap — `stream()` contract exists
  (Lane D) but `reasoning()` and `vision()` have no standardized contract.
  Without them, multi-modal and extended-thinking providers cannot be governed.
- **H** closes the memory enforcement gap — `MEMORY_TIER_OWNER_POLICIES` and
  `MEMORY_REINJECTION_POLICIES` are defined in Phase D contracts but never
  consulted at runtime. `buildRouteAuditMemoryCapture()` in route.ts already
  uses the `session` tier — adding a policy check at that call site closes H
  without touching the frozen contract layer.

**Maika AI** is not just a test vehicle — it is the first real-user governed AI
feature built on CVF. Teacher enters structured data; CVF governs the AI call;
parent receives a natural Vietnamese sentence. This is the "governed capability
system" the Assessment baseline demanded.

---

## What Already Exists (Adjustment 1 inventory)

### C — CLI Execution Gateway

| Item | Path | Lines / Tests |
| --- | --- | --- |
| Governance CLI | `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/` | `cvf-guard evaluate/audit/session/report` — 59 tests PASS |
| Governed execute path | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | 1001 lines, 8-step pipeline |
| Execution role resolver | `src/lib/execute-role-resolver.ts` | resolveExecutionCVFRole, actor-role gate |
| Stream contract | `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts` | StreamRequest, StreamContract, StreamCapableProvider |

**True gap (one sentence):** No `cvf run` / `cvf execute` CLI command exists
that routes a governed execution request through the 8-step pipeline.

**Done criterion:** `cvf execute --template app_builder_complete --provider alibaba`
exits 0 with a receipt JSONL line and a governance audit event appended.

### D — Provider Method Parity

| Item | Path | Status |
| --- | --- | --- |
| LLMAdapter interface | `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/llm.adapter.interface.ts` | `generate()` + optional `stream?()` — 45 lines |
| StreamCapableProvider | `CVF_MODEL_GATEWAY/src/stream-contract.ts` | Lane D DONE |
| reasoning / vision / embedding | Not present in MODEL_GATEWAY or RUNTIME_ADAPTER_HUB | **GAP** |

**True gap:** `ReasoningContract`, `VisionContract` method interfaces do not exist
in `CVF_MODEL_GATEWAY`. Lane D covered `stream()`; the remaining three methods
are unstandarized. Maika photo description is the vision consuming use case.

**Done criterion (scoped to this tranche):** `VisionContract` and
`ReasoningContract` interfaces exist in `CVF_MODEL_GATEWAY/src/` with tests;
`isVisionContract()` and `isReasoningContract()` type guards exported from
`index.ts`; Maika edge function uses `VisionContract` to describe a daily
report photo.

Embedding deferred — no consuming use case identified yet.

### H — Memory Runtime

| Item | Path | Status |
| --- | --- | --- |
| Phase D contracts | `CVF_GUARD_CONTRACT/src/contracts/memory-continuity.contract.ts` | `MemoryTierOwnerPolicy`, `MemoryReinjectionPolicy`, `MEMORY_TIER_OWNER_POLICIES`, `MEMORY_REINJECTION_POLICIES` defined |
| Live path write | `route.ts` line 927: `buildRouteAuditMemoryCapture()` | Writes `session` tier — `privacyFilter`, `reinjectionAllowed` from Phase D policies |
| Tier owner check | Not called at runtime | **GAP** |
| Reinjection check | Not called at runtime | **GAP** |

**True gap:** `buildRouteAuditMemoryCapture()` at route.ts step 7 reads the
`session` tier policy to build the receipt, but does NOT check
`reinjectionAllowed` or `privacyFilters` before writing. A contaminated or
unauthorized memory write could succeed silently.

**Done criterion:** `buildRouteAuditMemoryCapture()` (or its call site in
route.ts) calls a new `enforceMemoryTierPolicy(tier, cvfRole)` helper that
reads `MEMORY_TIER_OWNER_POLICIES[tier]` and returns a typed gate result;
if gate fails, execution continues but memory capture is degraded with an
explicit `decision: 'policy_rejected'` in the receipt. One test confirms
rejection for `archive` tier (reinjectionAllowed = false).

---

## Non-Goals

- Do NOT wire `persistent` or `archive` tier memory into any live path — only
  `session` tier is in scope for H this tranche.
- Do NOT implement `embedding()` method — no consuming use case named.
- Do NOT modify `MEMORY_TIER_OWNER_POLICIES` or `MEMORY_REINJECTION_POLICIES`
  data — these are frozen Phase D contracts.
- Do NOT add streaming SSE to the Next.js execute route.
- Do NOT create new CVF roles or modify `KNOWN_CVF_ROLES`.
- Do NOT add Maika features beyond daily-summary Edge Function and optional
  vision photo-description.

---

## Work Plan

### Candidate M — Maika AI Daily Summary Edge Function

**Target repo:** `CVF-Workspace/Nha tre Maika`
**GC-018 required:** No — this is a Maika product feature, not a CVF governance
enforcement surface. No GC-018 needed.
**Parallel with:** C (M is the consuming use case that unlocks C's demand gate)

**What exists:**
- `supabase/functions/send-push/` — Deno edge function pattern confirmed
- `DailyReports.jsx` line 654–695 — rule-based "✨ Tạo tóm tắt" generates
  Vietnamese sentences from dropdown values via string concatenation
- Fields available: `studentName`, `mood`, `breakfast`, `lunch`, `snack`,
  `napDuration`, `activities[]`, `health`, `note`

**Tasks:**

1. Create `supabase/functions/generate-daily-summary/index.ts` — Deno edge
   function that accepts `{studentName, mood, breakfast, lunch, snack,
   napDuration, activities, health, existingNote}`, calls Alibaba qwen-turbo
   via CVF `/api/execute` governed path (or directly if CVF CLI not ready yet),
   returns `{summary: string, governed: boolean, receiptId?: string}`.

2. In `DailyReports.jsx` — replace the rule-based string concat at line
   654–682 with an async call to the edge function. Add loading state on the
   "✨ Tạo tóm tắt" button. Fallback: if edge function fails → use existing
   string concat (offline-safe).

3. Add `VITE_CVF_EXECUTE_URL` env var pointing to CVF `/api/execute` endpoint.

**Acceptance criteria:**
- Edge function returns a natural Vietnamese sentence for a test payload
- Button shows loading state during AI call
- Fallback activates when edge function is unreachable (offline test)
- No new Supabase migration required

---

### Candidate C — CLI Execution Gateway

**Target repo:** `Controlled-Vibe-Framework-CVF` (governance repo) +
`CVF_ECO_v2.2_GOVERNANCE_CLI` extension
**GC-018 required:** Yes — new enforcement surface, R0 extension of existing CLI
**GC-018 path:** `docs/baselines/CVF_GC018_C_CLI_EXECUTION_GATEWAY_2026-05-19.md`
**Depends on:** Maika M (consuming use case named and proven)

**Tasks:**

1. Add `cvf execute` command to `CVF_ECO_v2.2_GOVERNANCE_CLI`:
   - Accepts `--template <id>`, `--provider <name>`, `--input <json>`,
     `--format json|table`
   - Routes through the same 8-step pipeline logic as `/api/execute` route
   - Emits receipt JSONL line and governance audit event
   - Returns exit 0 on compliant execution, exit 2 on policy violation

2. Add `cvf execute --dry-run` mode — validates pack contract and role gate
   without calling the provider.

3. Update `CVF_ECO_v2.2_GOVERNANCE_CLI` test suite — minimum 6 new tests:
   - compliant execution with mocked provider
   - policy violation → exit 2
   - missing template → clear error
   - dry-run mode → no provider call
   - receipt JSONL appended
   - JSON output mode

**Acceptance criteria:**
- `cvf execute --template app_builder_complete --provider alibaba --dry-run`
  exits 0 and prints policy check result
- Governance CLI `npm test` all pass including new tests
- Receipt JSONL line appended on `--enforce` run
- Maika edge function can use `cvf execute` as execution backend

---

### Candidate D — Provider Method Parity (vision + reasoning)

**Target repo:** `Controlled-Vibe-Framework-CVF` (governance repo),
`CVF_MODEL_GATEWAY` extension
**GC-018 required:** Yes — new enforcement surface extending Lane D
**GC-018 path:** `docs/baselines/CVF_GC018_D2_PROVIDER_VISION_REASONING_2026-05-19.md`
**Depends on:** Maika photo-description use case identified

**Tasks:**

1. In `CVF_MODEL_GATEWAY/src/`, create `reasoning-contract.ts`:
   ```
   ReasoningRequest, ReasoningContract, ReasoningCapableProvider,
   isReasoningContract() type guard
   REASONING_CONTRACT_REQUIRED_FIELDS
   ```
   Pattern mirrors `stream-contract.ts`. Fields: `thinking`, `summary`,
   `done`, `receiptObligation?`.

2. In `CVF_MODEL_GATEWAY/src/`, create `vision-contract.ts`:
   ```
   VisionRequest (prompt + imageBase64 or imageUrl), VisionContract,
   VisionCapableProvider, isVisionContract() type guard
   VISION_CONTRACT_REQUIRED_FIELDS
   ```
   Fields: `description`, `confidence?`, `done`, `receiptObligation?`.

3. Export both from `CVF_MODEL_GATEWAY/src/index.ts`.

4. Update `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/llm.adapter.interface.ts`
   — add optional `reasoning?()` and `vision?()` method stubs with JSDoc
   linking to the new contracts. Do NOT change `generate()` or `stream?()`.

5. Add tests in `CVF_MODEL_GATEWAY/tests/`:
   - `reasoning-contract.test.ts` — isReasoningContract type guard, required fields
   - `vision-contract.test.ts` — isVisionContract type guard, required fields

**Acceptance criteria:**
- `CVF_MODEL_GATEWAY` `npm test` all pass including new contract tests
- `CVF_MODEL_GATEWAY` `npm run check` PASS
- `isVisionContract()` and `isReasoningContract()` exported and importable
- Maika edge function can import `VisionContract` for photo description

---

### Candidate H — Memory Runtime Enforcement

**Target repo:** `Controlled-Vibe-Framework-CVF` (governance repo),
`cvf-web` extension
**GC-018 required:** Yes — new enforcement surface on live execute path
**GC-018 path:** `docs/baselines/CVF_GC018_H_MEMORY_RUNTIME_2026-05-19.md`
**Depends on:** None (consuming flow already exists in route.ts step 7)

**Tasks:**

1. Create `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/memory-tier-gate.ts`:
   ```typescript
   import { MEMORY_TIER_OWNER_POLICIES, MEMORY_REINJECTION_POLICIES }
     from '@cvf/guard-contract';

   export type MemoryTierGateResult =
     | { decision: 'captured'; tier: string; privacyFilter: string }
     | { decision: 'policy_rejected'; tier: string; reason: string };

   export function enforceMemoryTierPolicy(
     tier: MemoryContinuityTier,
     cvfRole: CVFRole
   ): MemoryTierGateResult
   ```
   Logic: check `ownerRole` matches, check `reinjectionAllowed`, return typed result.
   File must be ≤ 80 lines.

2. In `route.ts` at the `buildRouteAuditMemoryCapture()` call site (step 7,
   line ~927): call `enforceMemoryTierPolicy('session', resolvedRole)` before
   building the receipt. If result is `policy_rejected`, set receipt `decision:
   'policy_rejected'` and skip memory write. Log gate result in audit event.
   Do NOT change route.ts line count beyond ±10 lines.

3. Create `src/lib/memory-tier-gate.test.ts`:
   - `test_session_tier_captured` — BUILDER role → `decision: captured`
   - `test_archive_tier_rejected` — any role → `decision: policy_rejected`
     (archive has `reinjectionAllowed: false`)
   - `test_gate_result_shape` — result has `tier` and typed decision fields

**Acceptance criteria:**
- `npm run test:run -- src/lib/memory-tier-gate.test.ts` PASS (3 tests)
- `npm run build` PASS
- `npm run lint` PASS
- route.ts stays ≤ 1011 lines
- Memory capture receipt includes `decision` field in audit event
- `archive` tier test confirms rejection without touching Phase D contract data

---

## Candidate execution sequence

```
M (Maika Edge Function)          ─── no GC-018, ~3 days, Maika repo
    ↓ provides consuming evidence
C (CLI Gateway)                  ─── GC-018 required, after M, CVF repo
D (Vision + Reasoning contracts) ─── GC-018 required, parallel with C, CVF repo
H (Memory Runtime gate)          ─── GC-018 required, parallel with C, CVF repo
```

C3 and C4 (workflow chain governance) run independently and do not block
or depend on any candidate in this roadmap.

---

## Acceptance Criteria

### M — Maika AI Daily Summary
- [ ] Edge function returns natural Vietnamese sentence for test payload
- [ ] UI fallback to string-concat when function unreachable
- [ ] `VITE_CVF_EXECUTE_URL` env var documented in `.env.example`

### C — CLI Execution Gateway
- [ ] `cvf execute --dry-run` exits 0 with policy check output
- [ ] Receipt JSONL appended on live run
- [ ] Governance CLI `npm test` all pass
- [ ] No governance/provenance repo files modified beyond CLI extension

### D — Vision + Reasoning Contracts
- [ ] `isVisionContract()` and `isReasoningContract()` exported from MODEL_GATEWAY
- [ ] `npm test` PASS in MODEL_GATEWAY
- [ ] `npm run check` PASS in MODEL_GATEWAY
- [ ] LLMAdapter interface has `vision?()` and `reasoning?()` optional stubs

### H — Memory Runtime Gate
- [ ] `enforceMemoryTierPolicy()` returns `policy_rejected` for `archive` tier
- [ ] route.ts memory capture step calls gate and reflects decision in receipt
- [ ] 3 memory-tier-gate tests pass
- [ ] `npm run build` and `npm run lint` PASS in cvf-web
- [ ] route.ts line count ≤ 1011

---

## Verification / Evidence

Each candidate produces a completion review in `docs/reviews/`:

- `docs/reviews/CVF_M_MAIKA_AI_DAILY_SUMMARY_COMPLETION_2026-05-19.md`
- `docs/reviews/CVF_C_CLI_EXECUTION_GATEWAY_COMPLETION_2026-05-19.md`
- `docs/reviews/CVF_D2_PROVIDER_VISION_REASONING_COMPLETION_2026-05-19.md`
- `docs/reviews/CVF_H_MEMORY_RUNTIME_COMPLETION_2026-05-19.md`

Each review must include: command → stdout → verdict per acceptance criterion.
GC-020 handoff HEAD SHA must be updated after each candidate commit.

---

## Claim Boundary

This roadmap covers:
- CLI entry point for governed execution (C)
- `vision()` and `reasoning()` method contracts only — not embedding (D)
- `session` tier memory policy enforcement only — not persistent or archive (H)
- Maika daily-summary edge function as the named consuming use case

It does not:
- Claim a complete Agent OS runtime
- Authorize provider implementations (only contracts and type guards)
- Change Phase D frozen contracts (`MEMORY_TIER_OWNER_POLICIES` data)
- Authorize multi-modal provider routing in the live web execute path
- Replace or modify any C1/C2/C3/C4 workflow chain guard work

Each candidate that requires GC-018 must have its own GC-018 filed and
accepted before Worker implementation begins.

After completion of M + C + D + H, the Assessment baseline
(`CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`) problems C, D,
and H may be marked `CLOSED_IMPLEMENTED`. Problem B remains open (governed
pack contract — addressed by C2 work order). Problem G (full actor lifecycle)
remains deferred.
