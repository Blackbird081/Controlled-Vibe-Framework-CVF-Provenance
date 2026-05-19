
# CVF Runtime Maturity Delta Roadmap V2 — M1 / C2 / D2 / H2

Memory class: SUMMARY_RECORD

Status: READY_FOR_IMPLEMENTATION — rewritten after Codex rebuttal
`CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md` accepted
BLOCKING_FINDINGS; all 5 findings incorporated.

Predecessor authority:
`docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`
`docs/reviews/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`

---

## Purpose

Close the remaining open delta slices of Assessment problems C, D, and H after
Codex rebuttal corrected the first roadmap's current-state claims. Adds Maika
AI text-summary (M1) as the named consuming use case for C2 live proof.
Photo-description (D3) and reasoning (D4) are deferred pending separate demand
gates. Memory reinjection is out of scope.

---

## Scope / Target / Owner Boundary

In scope:

- **M1 — Maika Text Summary:** Supabase Edge Function
  `generate-daily-summary` in the Nha tre Maika workspace. Calls CVF
  `/api/execute` (governed path only; no direct provider fallback). Text
  fields only (mood, meals, sleep, activities, health). No photo description.
  Data minimization payload. Privacy boundary documented.
- **C2 — CLI Execute Hardening:** Starts from existing `cvf execute` command
  in `CVF_ECO_v2.2_GOVERNANCE_CLI`. Adds live HTTP proof test against a real
  CVF endpoint (or a full-stack mock), `--dry-run` flag, JSONL audit receipt
  appended to `docs/evidence/cvf-execute-receipts.jsonl`.
- **D2 — Vision Contract:** New `vision-contract.ts` in
  `CVF_MODEL_GATEWAY/src/`. Defines `VisionRequest`, `VisionContract`,
  `VisionCapableProvider`, `isVisionContract()`. Adds optional `vision?()`
  stub to `LLMAdapter`. No provider implementation, no live call.
- **H2 — Audit Memory Policy Refinement:** Adds explicit
  `writesRequireReceipt` and `privacyFilters` surface to the existing
  `buildAuditMemoryReceipt()` flow. Preserves `canReinject: false`. Adds
  degraded-capture representation when the controlled memory gateway denies
  write. Tests must reflect `session.ownerRole = OPERATOR`.

Out of scope:

- D3 vision runtime / live provider call (separate demand gate required)
- D4 reasoning contract (separate demand gate required)
- Memory reinjection into provider prompts
- Persistent / archive memory writes
- New role taxonomy
- Public-sync edits beyond what C2 live test requires
- Marking C/D/H globally `CLOSED_IMPLEMENTED` from this roadmap

---

## Adjustment 1 Inventory (per candidate)

### M1 — Maika Text Summary

What exists:
- `DailyReports.jsx` lines 654–682: rule-based string concat on click of
  "✨ Tạo tóm tắt" button. Fields: mood, breakfast, lunch, snack,
  napDuration, activities, health. Sets `form.note` synchronously.
- `supabase/functions/send-push/index.ts`: Deno edge function pattern
  confirmed (Deno.env, corsHeadersFor, createClient, jsonResponse helpers).
- `supabase/functions/` directory: send-push, send-zalo-zns, admin-users,
  storage-maintenance, _shared/cors.ts.

True gap:
- No `supabase/functions/generate-daily-summary/` exists yet.
- No CVF AI call wired into DailyReports.jsx.
- No data minimization / privacy boundary defined for child-facing data.

Done criterion:
- `supabase/functions/generate-daily-summary/index.ts` deployed (or
  deployable); calls `POST CVF_EXECUTE_URL/api/execute` from Supabase server
  env with `templateId: "documentation"` and route-compatible minimized
  inputs: `subject`, `currentNotes`, `readerGoal`. `currentNotes` may contain
  mood, meals, sleep, activities, and health only — no names, photos, or
  parent contact data.
- `DailyReports.jsx` button calls edge function; falls back to rule-based
  string on error (network/auth failure only — no direct provider call).
- Privacy notes documented in function file header.
- `CVF_EXECUTE_URL` and `CVF_SERVICE_TOKEN` server env placeholders documented
  in `.env.example`; frontend must not call CVF directly.

### C2 — CLI Execute Hardening

What exists:
- `execute.client.ts` (189 lines): `buildExecutePayload`, `buildExecuteUrl`,
  `buildServiceHeaders`, `executeGovernedTemplateCommand`,
  `buildCliReceipt`. All present and tested.
- `tests/execute.client.test.ts` (148 lines): 5 tests — URL build, payload
  build, stream flag, HMAC header, mock HTTP success. All mock-only.
- `command.registry.ts`: `cvf execute` registered, `executeAsync` wired.

True gap:
- No live HTTP proof test (integration against real endpoint).
- No `--dry-run` flag (would validate payload + auth without sending).
- No JSONL audit receipt persistence (`docs/evidence/cvf-execute-receipts.jsonl`).

Done criterion:
- `execute.client.ts` gains `buildDryRunOutput()` for `--dry-run` mode.
- `command.registry.ts` wires `--dry-run` flag to dry-run path.
- `tests/execute.client.test.ts` gains: `test_dry_run_output_shape`,
  `test_jsonl_receipt_format`.
- `--dry-run` test: validates payload + auth header shape without HTTP call.
- JSONL receipt: `appendExecuteReceipt(receipt, path)` helper; writes one
  JSONL line when `--receipt` flag set.
- Evidence file: `docs/evidence/cvf-execute-receipts.jsonl` created on
  first `--receipt` run.
- No new surface added; `execute.client.ts` stays ≤ 220 lines.

### D2 — Vision Contract

What exists:
- `CVF_MODEL_GATEWAY/src/stream-contract.ts` (35 lines): `StreamRequest`,
  `StreamContract`, `StreamCapableProvider`, `isStreamContract()`. Clean
  pattern to follow exactly.
- `CVF_MODEL_GATEWAY/src/index.ts`: exports stream-contract.
- `llm.adapter.interface.ts` (45 lines): `LLMAdapter` with `generate()` and
  optional `stream?()`. No `vision?()` stub.

True gap:
- `CVF_MODEL_GATEWAY/src/vision-contract.ts` does not exist.
- `LLMAdapter` has no `vision?()` stub.
- `CVF_MODEL_GATEWAY/src/index.ts` does not export vision-contract.

Done criterion:
- `vision-contract.ts` (≤ 50 lines): `VisionRequest`, `VisionContract`,
  `VisionCapableProvider`, `isVisionContract()`, and
  `VISION_CONTRACT_REQUIRED_FIELDS` — pattern mirrors `stream-contract.ts`
  exactly.
- `llm.adapter.interface.ts` gains optional `vision?()` stub (≤ 5 lines
  added; file stays ≤ 55 lines).
- `index.ts` exports vision-contract types.
- New test file `tests/vision-contract.test.ts` (≤ 60 lines): type guard
  pass, type guard fail missing fields, `VisionCapableProvider` shape.
- `npm test` passes; `npm run check` passes.

### H2 — Audit Memory Policy Refinement

What exists:
- `audit-memory-receipt.ts` (178 lines): `buildAuditMemoryReceipt()` reads
  `MEMORY_TIER_OWNER_POLICIES['session']` and
  `MEMORY_REINJECTION_POLICIES['session']`. Passes `canReinject: false`
  deliberately. `ownerRole` in output = `OPERATOR` (from frozen policy).
- `memory-continuity.contract.ts`: `session.ownerRole = 'OPERATOR'`,
  `session.writesRequireReceipt = true`,
  `session.privacyFilters = ['scope_minimization', 'pii_redaction']`,
  `session.reinjectionAllowed = true` (reinjection field — NOT a write gate).

True gap:
- `buildAuditMemoryReceipt()` does not surface `writesRequireReceipt` in
  its output; consumer cannot tell if write was gated or skipped.
- `AuditMemoryReceipt` type does not include `writesRequireReceipt` or
  `privacyFilters` fields.
- No degraded-capture path when write is denied (gateway always returns
  `captured` in current tests — no test for denied write).
- `reinjectionAllowed` from the frozen policy is NOT used as a write gate
  (correct); but there is no explicit comment/assertion to prevent future
  confusion.

Done criterion:
- `AuditMemoryReceipt` type gains `writesRequireReceipt: boolean` and
  `privacyFilters: readonly string[]` from the tier policy.
- `buildAuditMemoryReceipt()` populates both fields from frozen policy data.
- Degraded-capture: if `receipt.decision !== 'captured'`, `auditEventPayload`
  outcome = `'DEGRADED'` (already present for `decision` check) — add
  explicit `writesRequireReceipt` gate check before `capture()` call; if
  false → skip capture and return `decision: 'policy_skipped'` result.
- New test: `test_session_owner_is_operator` asserts
  `receipt.ownerRole === 'OPERATOR'`.
- New test: `test_writes_require_receipt_surface` asserts
  `receipt.writesRequireReceipt === true`.
- `audit-memory-receipt.ts` stays ≤ 220 lines (currently 178).
- `canReinject: false` is preserved in all paths.
- `reinjectionAllowed` field from policy data is never used as write gate.

---

## GC-018 Requirements

| Candidate | GC-018 required | Path |
|---|---|---|
| M1 | No — Maika product feature, no new CVF enforcement surface | — |
| C2 | No — hardening delta of existing `cvf execute`; R0 scope | — |
| D2 | Yes — new enforcement surface in CVF_MODEL_GATEWAY | `docs/baselines/CVF_GC018_D2_VISION_CONTRACT_2026-05-19.md` |
| H2 | Yes — modifies existing enforcement surface in cvf-web lib | `docs/baselines/CVF_GC018_H2_AUDIT_MEMORY_POLICY_REFINEMENT_2026-05-19.md` |

---

## Execution Sequence

M1 and C2 in parallel (no GC-018, independent repos).
D2 and H2 in parallel after GC-018 filed and accepted.

```
M1 ──────────────────────────────────────────► CLOSED
C2 ──────────────────────────────────────────► CLOSED
D2 (GC-018) ─────────────────────────────────► CLOSED
H2 (GC-018) ─────────────────────────────────► CLOSED
```

---

## Closure Language (per-slice, not global)

After completion, assessment baseline statuses become:

- Problem C: `C2_CLI_HARDENING_DELTA_CLOSED` (C1 = mock-tested CLI caller,
  already recorded)
- Problem D: `D2_VISION_CONTRACT_CLOSED` (stream = D1 closed; D3/D4
  deferred)
- Problem H: `H2_AUDIT_MEMORY_POLICY_REFINEMENT_CLOSED` (H1 = runtime
  wired for audit memory receipt, already recorded)

Do not write `CLOSED_IMPLEMENTED` for C, D, or H at the problem level.

---

## Authorization / Decision

Authority: Orchestrator role (Claude), 2026-05-19. Codex rebuttal
`CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md` returned
BLOCKING_FINDINGS; all 5 findings accepted; this V2 roadmap incorporates all
corrections. No further Reviewer rebuttal required before work orders are
dispatched — the rebuttal itself constitutes the review gate for this delta
roadmap.

D2 and H2 require GC-018 before Worker implementation. M1 and C2 do not.

---

## Non-Goals

- D3 vision provider runtime (no live image call authorized)
- D4 reasoning contract (no demand gate yet)
- Memory reinjection or persistent/archive writes
- Global `CLOSED_IMPLEMENTED` marking for problems C, D, or H
- New role taxonomy or auth changes
- Public catalog update (separate governed sync step)

---

## Work Plan

| Step | Candidate | Prerequisite | Target repo |
| ---- | --------- | ------------ | ----------- |
| 1a | M1 | None | Maika workspace |
| 1b | C2 | None | CVF governance repo (CLI extension) |
| 2a | D2 | GC-018 accepted | CVF governance repo (Model Gateway) |
| 2b | H2 | GC-018 accepted | CVF governance repo (cvf-web lib) |

Steps 1a and 1b run in parallel. Steps 2a and 2b run in parallel after their
GC-018s are accepted.

---

## Acceptance Criteria

- [ ] M1: `generate-daily-summary` edge function deployed/deployable; no direct
  provider import; payload contains no child name or photo data
- [ ] M1: `DailyReports.jsx` onClick calls edge function; rule-based string is
  error-only fallback
- [ ] C2: `buildDryRunOutput` and `appendExecuteReceipt` added; 7 CLI tests
  PASS; `npm run check` PASS; `execute.client.ts` ≤ 220 lines
- [ ] D2: `vision-contract.ts` ≤ 50 lines; 5 tests PASS; `llm.adapter.interface.ts`
  ≤ 55 lines; `npm run check` PASS; no provider implementation
- [ ] H2: `AuditMemoryReceipt` gains `writesRequireReceipt` + `privacyFilters`;
  2 new tests PASS; `canReinject: false` preserved; `npm run build` PASS;
  `audit-memory-receipt.ts` ≤ 220 lines

---

## Verification / Evidence

Each work order completion review must include:

- Command → stdout → pass/fail per acceptance criterion
- Line count proof for GC-023 governed files
- Confirmation of invariants (no provider call for D2; `canReinject: false`
  for H2; no direct AI import for M1)

---

## Claim Boundary

This roadmap covers only the four delta slices above. It does not authorize
provider runtime implementation, memory reinjection, photo description, new
role taxonomy, or public-sync edits beyond C2 live proof evidence.
