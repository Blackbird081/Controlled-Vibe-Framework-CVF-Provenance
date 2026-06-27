# CVF Work Order — PM-3 Tool Call Boundary Documentation

Memory class: FULL_RECORD

Status: HOLD_UNTIL_PM2_PASS

docType: work_order

Date: 2026-05-29

---

## Purpose

Document the `tool_call` method boundary: `tool_call` is declared as a
`ProviderMethodName` in the CVF capability registry but is absent from all
provider `supportedMethods` arrays. PM-3 formalizes this gap as a boundary
record, defines the unlock path, and closes CVF 25.05 Gap 3 together with
PM-1 and PM-2.

This is a documentation-only tranche. No live call is made. No provider
currently supports `tool_call` in the CVF registry.

## Authority Chain

- PM GC-018: `docs/baselines/CVF_GC018_PROVIDER_METHOD_LIVE_PROOF_2026-05-29.md`
- PM Roadmap: `docs/roadmaps/CVF_PROVIDER_METHOD_LIVE_PROOF_ROADMAP_2026-05-29.md`
- Capability registry: `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
  — `tool_call` declared at line 10 (ProviderMethodName type); absent from
    all supportedMethods arrays (lines 52, 57, 62, 67, 80, 93)
- CVF 25.05 review: `.private_reference/legacy/CVF 25.05/CLAUDE_REVIEW_OF_GOP_Y_2026-05-25.md`
  — GAP 3 section
- **PM-2 gate: `docs/reviews/CVF_PM2_STREAMING_LIVE_PROOF_COMPLETION_2026-05-29.md`
  must be CLOSED_PASS**

## Agent Roles

Implementer writes boundary record documenting `tool_call` gap and unlock path.
Reviewer checks: registry lines cited accurately; no live proof claimed;
unlock condition explicit. No self-review.

## Scope

**Allowed:**

- `docs/evidence/provider-methods/tool-call/boundary-record.md` (new)
- `docs/reviews/CVF_PM3_TOOL_CALL_BOUNDARY_COMPLETION_2026-05-29.md` (new)
- this work order (status update only)
- session continuity files

**Forbidden:** Any EXTENSIONS/ source change, provider routing change,
receipt envelope schema change, public-sync repo.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`
2. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
3. `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts`
   — confirm `tool_call` at line 10 (type only); confirm absence from all
   `supportedMethods` arrays at lines 52, 57, 62, 67, 80, 93
4. `docs/reviews/CVF_PM2_STREAMING_LIVE_PROOF_COMPLETION_2026-05-29.md`
   — confirm PM-2 CLOSED_PASS

## Pre-Dispatch Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| `tool_call` method name | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 10 | `tool_call` | `ProviderMethodName` type | ACCEPT |
| `tool_call` absent from qwen-turbo | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 52 | supportedMethods array | alibaba qwen-turbo entry | ACCEPT |
| `tool_call` absent from deepseek-chat | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 80 | supportedMethods array | deepseek deepseek-chat entry | ACCEPT |
| `tool_call` absent from gpt-4o | `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-capability-registry.ts` | line 93 | supportedMethods array | openai gpt-4o entry | ACCEPT |
| PM GC-018 authorization | `docs/baselines/CVF_GC018_PROVIDER_METHOD_LIVE_PROOF_2026-05-29.md` | full document | tool_call boundary scope | PM GC-018 | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order section | Output artifact | Verification | Status |
| --- | --- | --- | --- | --- |
| tool_call boundary documented | Scope | boundary-record.md | Reviewer confirms gap cited | OPEN |
| Registry lines verified | Pre-Dispatch | source verification table | Lines 10, 52, 80, 93 cited | OPEN |
| Unlock path defined | Boundary Record | explicit unlock condition | Reviewer checks | OPEN |
| PM-2 gate confirmed | Authority Chain | PM-2 completion review | Read PM-2 review | OPEN |

## Deliverable — Boundary Record

File: `docs/evidence/provider-methods/tool-call/boundary-record.md`

Content must include:
- Method: `tool_call`
- Status: `schema_defined_unsupported` — declared in `ProviderMethodName` type
  at registry line 10; absent from all provider `supportedMethods` arrays
- Registry evidence: cite lines 52, 57, 62, 67, 80, 93 confirming absence
- No live receipt collected (no provider supports this method)
- Unlock condition: "A provider/model with `tool_call` in `supportedMethods`
  must be added to `provider-capability-registry.ts` before live proof is
  possible. Operator demand required to select the provider and authorize
  the registry addition."
- Claim boundary: "This record does not claim CVF supports tool_call execution.
  `runtimeExecutionAuthorized=false`."

## Pre-Flight

- [ ] Working tree clean
- [ ] All required first reads done
- [ ] Gate confirmations checked

## Write Ownership

Implementer owns all new files. No file outside the Allowed list may be modified.

## Return-To-Orchestrator Conditions

Stop if: required gate evidence missing; a cited source file cannot be found; implementing the deliverable requires a forbidden file change.

## Execution Plan

1. Read all required first reads; confirm PM-2 gate.
2. Read registry lines 10, 52, 80, 93 to confirm absence.
3. Write boundary record.
4. Write completion review including CVF 25.05 Gap 3 overall closure summary
   (PM-1 + PM-2 + PM-3 together close Gap 3).
5. Run governance gates.
6. Update session continuity.
7. Commit.

## Evidence Requirements

- Boundary record present with registry line citations
- Absence of `tool_call` from all supportedMethods confirmed
- Unlock path explicit
- PM-2 gate confirmed
- No code file in diff

## Acceptance Criteria

- [ ] PM-2 CLOSED_PASS confirmed
- [ ] `docs/evidence/provider-methods/tool-call/boundary-record.md` created
- [ ] Registry lines cited accurately
- [ ] Unlock condition explicit and actionable
- [ ] No live proof claimed
- [ ] Completion review includes Gap 3 overall closure summary
- [ ] No code file in diff

Fail conditions:
- PM-2 gate not confirmed
- Live receipt claimed for tool_call (no provider supports it)
- Registry lines misquoted

## Review Gate

PM-2 confirmed; registry absence documented; unlock path explicit; no
live proof claimed; no code file.

## Closure Checklist

- [ ] PM-2 CLOSED_PASS confirmed
- [ ] Boundary record created
- [ ] Registry absence documented at correct lines
- [ ] Completion review with Gap 3 overall closure summary written
- [ ] Governance gates PASS
- [ ] Session continuity updated

## Gap 3 Overall Closure Summary (for completion review)

CVF 25.05 Gap 3 is closed when PM-1 + PM-2 + PM-3 are all CLOSED_PASS:

| Method | Provider/Model | Status |
| --- | --- | --- |
| json_mode | deepseek-chat + gpt-4o | PM-1 CLOSED_PASS |
| stream | qwen-turbo | PM-2 CLOSED_PASS |
| tool_call | (none — gap documented) | PM-3 CLOSED_PASS |

## Operator Checkpoint

operator.checkpoint.waiver: Documentation-only tranche; no live call; no risk.

## Claim Boundary

PM-3 produces a boundary documentation record only. It does not claim tool_call
execution, provider support, receipt evidence, hosted readiness, production
readiness, or public release readiness.
