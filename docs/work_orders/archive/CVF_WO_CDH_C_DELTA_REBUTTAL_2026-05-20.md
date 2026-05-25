# CVF Work Order — CDH-C Delta Rebuttal

Memory class: SUMMARY_RECORD

Status: READY_FOR_REBUTTAL_EXECUTION

GC-018 required: No — reviewer rebuttal only. Any later implementation needs
a fresh CDH-C-specific GC-018 and a separate implementation work order.

## Authority Chain

- Active session state:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Active review queue item: `cdh-c-delta`
- CDH delta meta-roadmap:
  `docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md#per-slice-section-c`
- Original CDH blocking rebuttal:
  `docs/reviews/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
- C2 completion anchor:
  `docs/reviews/archive/CVF_C2_CLI_EXECUTE_HARDENING_COMPLETION_2026-05-19.md`
- Lane C baseline/completion evidence:
  `docs/baselines/CVF_GC018_LANE_C_EXECUTION_GATEWAY_2026-05-19.md`
  and `docs/reviews/CVF_LANE_C_EXECUTION_GATEWAY_COMPLETION_2026-05-19.md`

## Agent Roles

- Operator: selects CDH-C as a remaining CDH delta slice.
- Codex reviewer: performs the read-only CDH-C rebuttal and files the
  rebuttal packet.
- Orchestrator: may file a later GC-018 only if the rebuttal returns a
  non-blocking disposition.
- Worker: must not implement anything from this work order.

## Purpose

Produce the reviewer-role rebuttal for the CDH-C delta slice.

The rebuttal must decide whether C may proceed to a slice-specific GC-018 for
CLI execute proof/hardening while preserving the corrected baseline: `cvf
execute` already exists and must not be described as missing.

## Scope

Allowed scope:

- Read-only review of the CDH-C slice in the delta meta-roadmap.
- Read-only review of current governance CLI execute source/tests.
- Read-only review of Lane C and C2 completion evidence.
- Filing one rebuttal packet at:
  `docs/reviews/CVF_CDH_C_DELTA_CODEX_REBUTTAL_2026-05-20.md`
- Updating `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` and
  `CVF_SESSION/ACTIVE_SESSION_STATE.json` after the rebuttal is filed.
- Updating `AGENT_HANDOFF_V10_2026-05-19.md` only if needed for continuity.

Forbidden scope:

- No implementation.
- No GC-018 baseline for implementation.
- No new CLI verb family.
- No reimplementation or duplication of `cvf execute`.
- No claim that `cvf execute` is missing.
- No provider/runtime behavior change.
- No public-sync or public release claim.
- No live CLI claim unless a later GC-018 explicitly authorizes live proof.

## Required First Reads

1. `CVF_SESSION/ACTIVE_SESSION_STATE.json`
2. `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
3. `docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md`
4. `docs/reviews/archive/CVF_RUNTIME_MATURITY_CDH_ROADMAP_CODEX_REBUTTAL_2026-05-19.md`
5. `docs/reviews/CVF_LANE_C_EXECUTION_GATEWAY_COMPLETION_2026-05-19.md`
6. `docs/reviews/archive/CVF_C2_CLI_EXECUTE_HARDENING_COMPLETION_2026-05-19.md`
7. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`
8. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
9. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/execute.client.test.ts`
10. `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/command.registry.test.ts`

## Pre-Flight Checks

Before writing the rebuttal, Codex must verify:

- `cdh-c-delta` remains a `READY_FOR_REBUTTAL` item.
- `cvf execute` is present in the command registry.
- `execute.client.ts` implements an HTTP caller for the governed `/api/execute`
  route.
- C2 completion evidence already covers dry-run redaction and JSONL receipt
  persistence locally.
- Any proposed continuation is framed as proof/hardening over the existing
  command, not first implementation.

## Write Ownership

Codex reviewer may create:

- `docs/reviews/CVF_CDH_C_DELTA_CODEX_REBUTTAL_2026-05-20.md`

Codex reviewer may update:

- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V10_2026-05-19.md`

Codex reviewer must not modify:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/*`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/*`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- Any provider, memory, Maika, or public-sync file.

## Execution Plan

1. Confirm active queue order and CDH-C scope.
2. Read the CDH-C meta-roadmap section and original CDH blocking finding 1.
3. Read Lane C and C2 completion evidence.
4. Inspect current CLI execute source and tests.
5. Decide one of:
   - `NON_BLOCKING_WITH_SCOPE_REFINEMENT`
   - `NON_BLOCKING_WITH_EXISTING_EVIDENCE`
   - `BLOCKING`
6. File the rebuttal packet with findings, risks, required corrections, and
   explicit claim boundary.
7. Update active review queue/state/handoff routing.
8. Run JSON parse and active-session state checks.
9. Run docs governance and Markdown structural checks if new docs were filed.

## Tasks

- [ ] Confirm queue status for `cdh-c-delta`.
- [ ] Verify `cvf execute` exists and is wired.
- [ ] Verify dry-run redaction and JSONL receipt persistence evidence.
- [ ] Verify no continuation claims first implementation of execute.
- [ ] Decide whether continuation should be live CLI proof, local-only proof
  hardening, or closed by existing evidence.
- [ ] File rebuttal at
  `docs/reviews/CVF_CDH_C_DELTA_CODEX_REBUTTAL_2026-05-20.md`.
- [ ] Update active queue/state routing.
- [ ] Run required verification.

## Acceptance Criteria

The rebuttal is acceptable only if it:

- Names the disposition clearly.
- States that `cvf execute` already exists.
- Treats C as CLI hardening/proof only, not missing-command work.
- Separates local unit/type evidence from any live CLI proof claim.
- Does not authorize implementation by itself.
- Requires a later CDH-C-specific GC-018 before code or live-proof changes if
  continuation is non-blocking.
- Keeps dry-run output secret-redacted and receipt persistence bounded to
  schema-relevant fields.

## Evidence Requirements

The rebuttal must cite:

- CDH-C meta-roadmap section.
- Original CDH rebuttal Finding 1.
- Lane C completion review.
- C2 completion review.
- Current `command.registry.ts` source inspection — must quote the exact
  registration line or symbol name proving `execute` is registered.
- Current `execute.client.ts` source inspection.
- Current execute-client test inspection.

If the rebuttal recommends continuation, it must list seed acceptance criteria
for the later implementation/proof GC-018, including:

- current `cvf execute` baseline remains intact;
- dry-run remains secret-redacted;
- JSONL receipt persistence is verified;
- live or local-only proof boundary is explicit;
- CLI tests and type checks pass.

## Review Gate

Stop and return `BLOCKING` if any of these are true:

- The proposed C delta claims `cvf execute` is missing.
- The proposed C delta requires new provider/runtime semantics.
- The proposed C delta creates a new CLI verb family instead of hardening the
  current execute path.
- The proposed C delta would print raw service tokens/signatures.
- The proposed C delta depends on public-sync or release claims.

## Closure Checklist

- [ ] Rebuttal packet filed.
- [ ] Queue item status updated.
- [ ] State registry next move updated.
- [ ] Handoff updated if continuity needs it.
- [ ] JSON parse passes for changed registry files.
- [ ] `python governance/compat/check_active_session_state.py --enforce`
  passes.
- [ ] `python governance/compat/check_docs_governance_compat.py` passes.
- [ ] `python governance/compat/check_markdown_structural_completeness.py`
  passes.

## Return-To-Orchestrator Conditions

Return without filing a non-blocking rebuttal if:

- the current CLI source cannot be inspected;
- the current source contradicts Lane C/C2 completion evidence;
- a continuation cannot be framed without claiming `cvf execute` is missing;
- the continuation requires provider/runtime behavior changes;
- the continuation requires public release work.

## Claim Boundary

This work order authorizes only a reviewer-role rebuttal. It does not authorize
implementation, GC-018 filing, live CLI proof, provider/runtime behavior
changes, public claims, or CDH closure.
