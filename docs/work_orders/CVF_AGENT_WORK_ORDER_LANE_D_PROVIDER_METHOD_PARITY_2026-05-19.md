# CVF Agent Work Order — Lane D: Provider Method Parity

Memory class: POINTER_RECORD

Status: CLOSED — implemented as contract-and-flag Lane D; see completion packet.

## Purpose

Dispatch Codex to implement Lane D (Provider Method Parity) as defined in
`docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_D_E_F_G_2026-05-19.md`.

Lane D adds a `StreamContract` interface to `CVF_MODEL_GATEWAY`, a `stream()`
method stub to `LLMAdapter`, and wires `--stream` flag to the CLI. It does not
implement live SSE streaming in the Next.js route — that is deferred.

## Source

- `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_D_E_F_G_2026-05-19.md` — lane D spec
- `docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md` —
  corrected problem map, Problem D
- `AGENT_HANDOFF_V9_2026-05-18.md` — active session posture
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` — current mode

## 1. Mission

Add a standardized `stream()` method contract to the gateway layer and wire
the CLI `--stream` flag to pass `stream: true` in execute POST body.

Success means: `cvf execute --stream` sends the correct payload, the
`StreamContract` interface is defined and tested, and `LLMAdapter` declares
a `stream()` stub. No live SSE in this lane.

## 2. Authority Chain

- Operator instruction: 2026-05-19 — implement Lane D/E/F/G in sequence
- Roadmap: `docs/roadmaps/CVF_NEXT_PHASE_ROADMAP_LANE_D_E_F_G_2026-05-19.md`
- Decision pack: `docs/reviews/CVF_MULTI_AGENT_DECISION_PACK_REVIEW_CVF_NEXT_PHASE_2026-05-18.md`
- Active session: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Active handoff: `AGENT_HANDOFF_V9_2026-05-18.md`

Authority boundary:

- GC-018 must be filed before implementation
- This work order does not authorize Lane E/F/G — those begin after Lane D closes
- No live SSE streaming implementation in this lane

## 3. Agent Roles

- Orchestrator / dispatcher: operator and coordinating agent (Claude)
- Implementer: Codex
- Reviewer: Claude
- Operator approval required for: scope expansion, live streaming, new provider

## 4. Required First Reads

Before filing GC-018:

1. `EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-output-contract.ts` — existing
   method contracts; understand what is there before adding
2. `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts` — exported surface
3. `EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts` — how providers are
   selected; `stream()` must respect existing routing
4. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts` — the
   HTTP caller added in Lane C; `--stream` flag wires into this
5. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/arg.parser.ts` — how flags
   are currently parsed
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/` —
   each pack's `execution.policy.json` needs a `streamingEnabled` field
7. `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` —
   check line limits before editing any governed file

Anti-duplication grep before writing:

```powershell
rg -n "stream|StreamContract|LLMAdapter|ProviderOutput" EXTENSIONS/CVF_MODEL_GATEWAY/src/
rg -n "stream" EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/
```

## 5. Pre-Flight Checks

Run before filing GC-018:

```powershell
python governance/compat/check_active_session_state.py --enforce
python governance/compat/check_markdown_structural_completeness.py
python governance/compat/check_docs_governance_compat.py
Test-Path "EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-output-contract.ts"
Test-Path "EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts"
git status --short
```

Expected: all pass, no unrelated changes.

## 6. GC-018 Requirements

Before implementation, file:

```
docs/baselines/CVF_GC018_LANE_D_PROVIDER_METHOD_PARITY_2026-05-19.md
```

The GC-018 must record:

- exact interface name (`StreamContract`) and file path in MODEL_GATEWAY
- exact method stub name (`stream()`) and where it is added
- exact CLI flag name (`--stream`) and argument parser change
- R1 risk statement
- explicit no-live-SSE-in-route boundary
- acceptance criteria
- Tranche Closure Checklist (from GC-018 template)

## 7. Write Ownership

Allowed scope:

```
EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts        (NEW)
EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts                  (MODIFY — export StreamContract)
EXTENSIONS/CVF_MODEL_GATEWAY/tests/stream-contract.test.ts (NEW)
EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/arg.parser.ts   (MODIFY — add --stream)
EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts (MODIFY — pass stream flag)
EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/execute.client.test.ts (MODIFY — add stream tests)
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/*/execution.policy.json (MODIFY — add streamingEnabled)
docs/baselines/CVF_GC018_LANE_D_PROVIDER_METHOD_PARITY_2026-05-19.md (NEW)
docs/reviews/CVF_LANE_D_PROVIDER_METHOD_PARITY_COMPLETION_2026-05-19.md (NEW)
```

Forbidden scope:

```
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts
  (no live SSE handler — deferred)
EXTENSIONS/CVF_MODEL_GATEWAY/src/routing-policy.ts
  (routing logic unchanged)
EXTENSIONS/CVF_MODEL_GATEWAY/src/provider-registry.ts
  (no new providers)
```

Write mode: create StreamContract file; modify index, arg.parser, execute.client,
governed packs; create GC-018 and completion packet.

## 8. Execution Plan

Steps are sequential unless marked parallel-safe.

1. Read all required first-read files. Grep for existing stream interfaces.
   Input: source files above. Output: confirmed understanding of gaps.
   Stop if: existing `StreamContract` or `stream()` stub already exists
   (report to reviewer — do not duplicate).

2. Create `stream-contract.ts` in MODEL_GATEWAY with `StreamContract` interface.
   Interface must define: `chunk: string`, `role: string`, `done: boolean`,
   `receiptObligation?: string`.
   Output: `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts`.
   Validation: TypeScript compiles with no errors.

3. Add `stream(request: StreamRequest): AsyncIterable<StreamContract>` stub to
   the existing `LLMAdapter` export if it exists. If the source-fidelity pass
   confirms no `LLMAdapter` interface currently exists, do not invent a broad
   provider adapter taxonomy; instead add the smallest provider-method parity
   type beside `provider-output-contract.ts` and record the exact source
   finding in the GC-018/completion packet.
   Output: modified existing adapter interface or a new minimal contract file.
   Stop if: would exceed GC-023 line limit for the file.

4. Export `StreamContract` from `CVF_MODEL_GATEWAY/src/index.ts`.
   Check line count before and after. Stop if would breach exception cap.

5. Add `--stream` boolean flag to `arg.parser.ts` in GOVERNANCE_CLI.
   Add `stream?: boolean` field to the execute options type in `types.ts`.
   Pass `stream: true` in `execute.client.ts` POST body when flag is set.
   Output: modified arg.parser, types, execute.client.

6. Add `streamingEnabled` boolean field to each governed pack's
   `execution.policy.json` (3 packs). Set `streamingEnabled: false` for
   now — the field exists for Lane D+1 to enable without schema change.

7. Write unit tests:
   - `stream-contract.test.ts`: verify interface shape, required fields
   - Update `execute.client.test.ts`: verify `--stream` passes `stream: true`
   All tests must pass with `npm test`.

8. File GC-018 baseline. File completion packet.
   Update GC-020 handoff.

Each step must state input, output, validation, and stop condition.

## 9. Evidence Requirements

Required evidence in completion packet:

```
Test-Path "EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts"
Test-Path "EXTENSIONS/CVF_MODEL_GATEWAY/tests/stream-contract.test.ts"
rg -n "StreamContract" EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts
rg -n "stream" EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/arg.parser.ts
rg -n "streamingEnabled" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/app_builder_complete/execution.policy.json
npm test (CVF_MODEL_GATEWAY) — all pass
npm test (CVF_ECO_v2.2_GOVERNANCE_CLI) — all pass
python governance/compat/run_local_governance_hook_chain.py --hook pre-commit
```

Evidence Trace Block required in completion packet:
- Claim:
- Command:
- Result:
- Key path:
- Verdict:

## 10. Acceptance Criteria

- [x] `stream-contract.ts` exists in `CVF_MODEL_GATEWAY/src/` with
      `StreamContract` interface (chunk, role, done, optional receiptObligation)
- [x] Existing adapter surface is checked with `rg`; completion packet records
      that `LLMAdapter.stream()` already exists in Runtime Adapter Hub and adds
      only the minimal gateway stream-capable contract authorized by GC-018
- [x] `StreamContract` is exported from MODEL_GATEWAY `index.ts`
- [x] `--stream` flag parses in GOVERNANCE_CLI arg.parser
- [x] `execute.client.ts` passes `stream: true` in POST body when flag set
- [x] `streamingEnabled` field added to all 3 governed pack `execution.policy.json`
- [x] Unit tests pass for StreamContract and stream flag
- [x] No live SSE streaming added to route.ts
- [x] GC-023 line limits respected for all modified files
- [x] Current governance pre-commit hook chain passes without bypassing hooks

## 11. Review Gate

Reviewer: Claude.

Reviewer checks:
- StreamContract interface is minimal and correct
- LLMAdapter stub does not implement live streaming
- route.ts is not modified
- All acceptance criteria evidenced with Test-Path and test runs

Operator approval required for: any scope expansion beyond stream contract
definition and CLI flag wiring.

## 12. Closure Checklist

- [x] GC-018 filed and referenced in completion packet
- [x] All implementation acceptance criteria PASS
- [x] Evidence Trace Block present in completion packet
- [x] Current governance hook chain passes without bypassing hooks
- [x] GC-020 handoff updated with pending Lane D continuity base
- [x] Public catalog: no update needed for this lane (contract definition only,
      not a new proven capability)
- [ ] Reviewer disposition: pending Claude/operator review after Codex commit

## 13. Return-To-Orchestrator Conditions

Stop and return if:

- Pre-flight checks fail for unrelated reasons
- Existing `stream()` or `StreamContract` found — report to reviewer, do not
  duplicate
- route.ts would be modified for live SSE — stop, flag to operator
- Any governed file would exceed GC-023 line limit
- GC-018 conflicts with the roadmap scope definition

## Claim Boundary

Lane D closes with: stream contract defined, CLI flag wired — `defined`

Not claimed: live streaming in the execute route, reasoning/vision/embedding
parity, production-ready streaming.
