# CVF Agent Work Order: G-GM-08 + G-GM-06 Named Guard Annotation

Memory class: FULL_RECORD

docType: work_order

Status: CLOSED

Date: 2026-06-07

Worker: Claude

Dispatch base head: `b32feb73`

Execution base head: `b32feb73`

Closure base head: `cdadedf7`

dispatchBaseHead: b32feb73
executionBaseHead: b32feb73
closureBaseHead: cdadedf7

Commit mode: WORKER_MAY_COMMIT

Risk class: R1_TEST_AND_COMMENT_ONLY

Authority: Closes §First Enforcement Candidate from
`docs/reference/CVF_GRAPHIFY_GUARD_ENFORCEMENT_SOURCE_MAP_2026-06-07.md`.

---

## Purpose

Add explicit named `G-GM-08` and `G-GM-06` guard annotations to
`memory-retrieval-policy.kgr.test.ts`. The behavior already exists;
the bounded step is making the guard ID explicit in test descriptions.

---

## Authority Chain

| Authority item | Path |
|---|---|
| Session front door | `CVF_SESSION_MEMORY.md` |
| Machine state registry | `CVF_SESSION/ACTIVE_SESSION_STATE.json` |
| Active handoff | `AGENT_HANDOFF_V16_2026-06-06.md` |
| Source map authority | `docs/reference/CVF_GRAPHIFY_GUARD_ENFORCEMENT_SOURCE_MAP_2026-06-07.md` |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` |

---

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Orchestrator | Claude (self-dispatch) | Scope owner |
| Worker | Claude | Add test assertions + optional comments; commit |
| Reviewer / closer | Codex or operator | Verify correctness if escalated |

---

## Worker Autonomy / No-Question Rule

Claude must proceed autonomously inside Allowed Scope. In-scope test failures, line-count checks, and gate commands are worker-owned. Claude must stop only when an action would exceed Allowed Scope, touch forbidden paths, or consume secrets/quota.

## Required First Reads

Before edits, read:

1. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-retrieval-policy.kgr.test.ts` (full, 93 lines)
2. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` (full, 258 lines)
3. `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/knowledge-graph-store.ts` (L225–244 — G-GM-06 and G-GM-08 entries)

---

## Pre-Flight Checks

Before edits, capture:

```powershell
git rev-parse --short HEAD
git status --short
```

Confirm no dirty paths intersect the target files. Expected base: `b32feb73`.

---

## Write Ownership

| Path | Ownership |
|---|---|
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-retrieval-policy.kgr.test.ts` | Claude may add tests |
| `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/memory-retrieval-policy.ts` | Claude may add one-line comments only (optional) |
| `docs/reviews/CVF_G_GM_08_G_GM_06_NAMED_GUARD_ANNOTATION_COMPLETION_2026-06-07.md` | Reviewer/closer may create closure packet |
| `AGENT_HANDOFF_V16_2026-06-06.md` | Reviewer/closer may update current HEAD record in a session-sync step |
| All other files | FORBIDDEN |

---

## Allowed / Forbidden Scope

**Allowed:**
- Add `[G-GM-08 Compliance Guard]` named test to `memory-retrieval-policy.kgr.test.ts`
- Add `[G-GM-06 Confidentiality Guard]` named test to `memory-retrieval-policy.kgr.test.ts`
- Add up to 2 one-line comments in `memory-retrieval-policy.ts` referencing guard IDs (optional)
- Create closure packet `docs/reviews/CVF_G_GM_08_G_GM_06_NAMED_GUARD_ANNOTATION_COMPLETION_2026-06-07.md`
- Update active handoff `AGENT_HANDOFF_V16_2026-06-06.md` HEAD record during reviewer closure/session sync
- Harden canonical work-order template `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` for future guard claim-language discipline

**Forbidden:**
- New runtime logic, new functions, new exports, new branches
- Changes to `knowledge-graph-store.ts`
- Changes to `CVF_SESSION_MEMORY.md`, handoff, or session state
- Public-sync, live proof, provider calls
- CLI graph commands

---

## Guard Claim-Language Discipline

Use `source-visible behavior connection` or `named guard test linkage` for this
work. Do not claim `functionally enforced`, `directly enforced`, `already
enforced`, or broad `runtime enforcement behavior`.

Allowed claim wording:

> `G-GM-08` and `G-GM-06` have named tests and comments linking guard IDs to
> existing retrieval-policy behavior.

Forbidden claim wording:

> `G-GM-08` and `G-GM-06` prove full runtime Graphify guard enforcement.

Metadata such as policy IDs, registry entries, or owner paths proves only
registry/owner presence. The named tests prove a bounded source/test linkage to
existing behavior, not full Graphify enforcement readiness.

---

## Execution Plan

| Step | Required action |
|---|---|
| 1 | Read three source files (required first reads) |
| 2 | Add `[G-GM-08 Compliance Guard]` test — assert `PENDING_REVIEW` node excluded with `reason: "disputed"` |
| 3 | Add `[G-GM-06 Confidentiality Guard]` test — assert `containsSecret: true` candidate excluded with `reason: "privacy_filtered"` |
| 4 | Optionally add one-line G-GM-08/G-GM-06 comments in `memory-retrieval-policy.ts` |
| 5 | Run `npx vitest run` on the test file; confirm all pass |
| 6 | Commit with the two changed files only |

### G-GM-08 test specification

Append inside the existing `describe` block:

```typescript
it("[G-GM-08 Compliance Guard] excludes non-compliant nodes as disputed", () => {
  // disputed node has governanceTag: "PENDING_REVIEW" → lifecycleState: "disputed" → excluded
  const result = evaluateRetrievalRequest(
    {
      method: "graph_search",
      query: "providerRoutingDraft",
      scope: "project",
      actorAuthorized: true,
      candidates: [],
    },
    { kgrStore: store },
  );
  expect(result.excluded).toContainEqual({ id: disputed.id, reason: "disputed" });
  expect(result.selected.map((c) => c.id)).not.toContain(disputed.id);
  expect(result.rawMemoryReleased).toBe(false);
});
```

### G-GM-06 test specification

Use the `keyword` method path where `containsSecret` filtering at L226 is directly exercised:

```typescript
it("[G-GM-06 Confidentiality Guard] excludes secret-bearing candidates from retrieval", () => {
  const secretCandidate: import("../src/memory-retrieval-policy").MemoryRetrievalCandidate = {
    id: "secret-node",
    scope: "project",
    summary: "secret summary",
    createdAt: 0,
    auditTrust: 0.8,
    lifecycleState: "semantic",
    containsSecret: true,
  };
  const result = evaluateRetrievalRequest({
    method: "keyword",
    query: "",
    scope: "project",
    actorAuthorized: true,
    candidates: [secretCandidate],
  });
  expect(result.excluded).toContainEqual({ id: "secret-node", reason: "privacy_filtered" });
  expect(result.selected.map((c) => c.id)).not.toContain("secret-node");
  expect(result.rawMemoryReleased).toBe(false);
});
```

---

## Evidence Requirements

After implementation, record in the completion review:

```powershell
git rev-parse --short HEAD
npx vitest run EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/memory-retrieval-policy.kgr.test.ts
git diff --name-status b32feb73 HEAD
```

All tests must pass. The diff must contain only the allowed files.

---

## Review Gate

Close only if: new tests exist with `[G-GM-08` and `[G-GM-06` in descriptions; all tests pass; no forbidden files changed; line counts within bounds.

---

## Closure Checklist

| Item | Required close state |
|---|---|
| G-GM-08 named test | PRESENT |
| G-GM-06 named test | PRESENT |
| All tests pass | VERIFIED |
| No forbidden file edits | VERIFIED |
| Line count bounds | VERIFIED |
| Implementation commit contains only allowed implementation files; closure packet and handoff sync are reviewer-owned | VERIFIED |

---

## Return-To-Orchestrator Conditions

Return if: test file exceeds 140 lines after additions; tests fail and root cause exceeds Allowed Scope; or a needed action would touch forbidden paths.

---

## Operator Checkpoint

`operator.checkpoint.waiver` — R1 test-and-comment-only work; no live proof, no public-sync, no runtime change, no secret use, no provider call required. Worker may proceed without separate operator approval.

---

## Source Verification Table

| Token / Symbol | Source file | Verified line |
|---|---|---|
| `kgrNodeToMemoryCandidate` compliance-tag branch | `memory-retrieval-policy.ts` | L93 |
| `lifecycleState: "disputed"` result | `memory-retrieval-policy.ts` | L93 |
| `BLOCKED_STATES` exclusion in `graph_search` path | `memory-retrieval-policy.ts` | L146 |
| `containsSecret === true` filter | `memory-retrieval-policy.ts` | L226 (keyword/semantic path) |
| `rawMemoryReleased: false` contract | `memory-retrieval-policy.ts` | L49 |
| `G-GM-08` registry entry | `knowledge-graph-store.ts` | L238–244 |
| `G-GM-06` registry entry | `knowledge-graph-store.ts` | L225–231 |
| `disputed` node fixture | `memory-retrieval-policy.kgr.test.ts` | L28–34 |
| `store` fixture | `memory-retrieval-policy.kgr.test.ts` | L36 |

---

## Acceptance Criteria

- At least one test contains `[G-GM-08` in its description and asserts compliance-tag exclusion
- At least one test contains `[G-GM-06` in its description and asserts secret-candidate exclusion
- `npx vitest run` on the test file: all tests pass (was 3, will be 5)
- No new runtime logic (no new functions, no new branches, no new exports)
- `memory-retrieval-policy.ts` increases by 0–4 lines (comment-only changes)
- `memory-retrieval-policy.kgr.test.ts` stays at or below 140 lines
- Pre-commit hook chain passes

---

## Claim Boundary

This work order claims only:

> G-GM-08 compliance-tag exclusion and G-GM-06 secret-candidate exclusion are
> explicitly named in test assertions in `memory-retrieval-policy.kgr.test.ts`,
> creating a machine-verifiable link from guard spec ID to existing retrieval
> behavior.

Does not claim:
- Full Graphify guard enforcement
- G-GM-01 / G-GM-02 / G-GM-03 / G-GM-04 / G-GM-07 implemented
- CLI graph command implementation
- New runtime guard logic beyond existing behavior
- Public readiness or production readiness

---

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_G_GM_08_G_GM_06_NAMED_GUARD_ANNOTATION_FOR_CLAUDE_2026-06-07.md` | Status `CLOSED`, claim-language discipline recorded, no stale dispatch residue | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_G_GM_08_G_GM_06_NAMED_GUARD_ANNOTATION_COMPLETION_2026-06-07.md` | Final disposition, changed files, claim boundary, gate evidence | PASS |
| Roadmap state | `N/A with reason` | Source-map follow-up candidate did not require roadmap state mutation in this bounded test/comment tranche | N/A with reason |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | GC-051 registry state unchanged by this implementation tranche; `check_corpus_scan_registry.py` passes | PASS |
| Registry Markdown | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` | Human registry surface unchanged by this implementation tranche; no new corpus intake registered | PASS |
| External evidence digest | `N/A with reason` | No external evidence or provider/service output used | N/A with reason |
| System loop interlock | `N/A with reason` | No system-loop interlock mutation or new runtime loop introduced | N/A with reason |
| Session continuity | `AGENT_HANDOFF_V16_2026-06-06.md` | Active handoff HEAD record updated to implementation commit `cdadedf7` | PASS |
