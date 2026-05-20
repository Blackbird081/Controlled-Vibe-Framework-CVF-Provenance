# Work Order — N2: Workflow-Chain Governance V2 Reviewer Rebuttal

Memory class: FULL_RECORD

Status: DISPATCHED

docType: work_order

Worker role: Codex (Reviewer)

Orchestrator: Claude

Date dispatched: 2026-05-20

Predecessor:

- `docs/roadmaps/CVF_POST_RESIDUAL_CLOSURE_NEXT_ROADMAP_2026-05-20.md` (REBUTTAL_FILED_NON_BLOCKING_WITH_GATE_UPDATE)
- `docs/reviews/CVF_POST_RESIDUAL_CLOSURE_NEXT_ROADMAP_CODEX_REBUTTAL_2026-05-20.md` (Codex verdict on N2: NON_BLOCKING_AS_REBUTTAL_ONLY_WITH_QUEUE_CORRECTION)
- `docs/roadmaps/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md` (READY_FOR_REBUTTAL since 2026-05-19; queue priority 2)
- `docs/reviews/CVF_WORKFLOW_CHAIN_GOVERNANCE_PROPOSAL_REVIEWER_REBUTTAL_2026-05-19.md` (first-round rebuttal on V1 that triggered V2)
- `docs/reviews/CVF_N1_PUBLIC_SYNC_CATALOG_UPDATE_CLOSURE_REVIEW_2026-05-20.md` (N1 closed at public commit `d11c772a`)

Authority chain: Codex rebuttal on the post-residual roadmap accepted N2 as
rebuttal-only work; no GC-018 is required for this tranche, but each accepted
candidate inside V2 may require its own downstream GC-018.

---

## Purpose

File the second-round Reviewer-role rebuttal on the workflow-chain
governance V2 roadmap so that the four V2 candidates (C1 / C2 / C3 / C4)
each carry a per-candidate verdict before any GC-018 is dispatched or any
Worker implementation begins.

This work order is reviewer/intake work only. It does not authorize any
implementation of C1, C2, C3, or C4. It does not change any guard,
registry, runtime, or public claim. It produces exactly one new file: the
rebuttal artifact at the expected response path.

---

## Scope / Target / Owner Boundary

In scope:

- Read the V2 roadmap end-to-end.
- File the rebuttal at the queue's `expectedResponsePath`:
  `docs/reviews/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_CODEX_REBUTTAL_2026-05-19.md`.
- Per-candidate verdict for C1 (public-sync guard hardening), C2 (governed
  pack contract guard), C3 (execute route step sequence guard), C4
  (continuation chain guard).
- Cite the post-Lane-G closure work that resolved earlier C1–C4 work
  orders if it materially changes the V2 verdict.
- Update `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` for the
  `workflow-chain-governance-v2` item after the rebuttal is filed.

Out of scope (forbidden):

- Implementing any V2 candidate.
- Filing GC-018 for any V2 candidate.
- Dispatching a downstream work order from this rebuttal alone.
- Modifying any guard file (`check_*.py`), registry JSON, or runtime code
  in either repo.
- Touching the public-sync repo at all (this is a governance-repo-only
  tranche).
- Reopening any A–H Review-CVF pain point.
- Modifying the V2 roadmap content. V2 is the artifact under review; it is
  not edited by N2.

Owner boundary:

- This work order touches only the governance repo and only adds the
  rebuttal file plus a queue-item status update.

---

## Per-Candidate Rebuttal Requirements

For each of C1, C2, C3, C4, the rebuttal must produce a section that
includes:

1. **Stated risk class** in V2 (R0 or higher).
2. **GC-018 obligation** as stated in V2 (Yes / No).
3. **Verdict**: `BLOCKING`, `NON_BLOCKING`, or
   `NON_BLOCKING_WITH_GATE_UPDATE`.
4. **Evidence cited** — at least one of:
   - Specific file path under `governance/compat/` or
     `governance/toolkit/05_OPERATION/`.
   - Specific test file path.
   - Specific commit SHA or section anchor in V2.
5. **Hidden-scope check** — at least one named risk surface that the
   candidate must NOT touch (e.g., "must not modify
   `execute-role-resolver.ts`", "must not change pack policy
   `allowedActorRoles`").
6. **Downstream gate** — what each candidate needs before implementation
   (GC-018, fast-lane audit, work order, none).

If any candidate cannot reach a clear verdict from V2 alone, return to
Orchestrator before filing the rebuttal. Do not invent verdicts.

---

## Deliverables

### Step N2.1 — Read V2 + Predecessor Evidence

Read in order:

1. `docs/roadmaps/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md` —
   the artifact under review.
2. `docs/reviews/CVF_WORKFLOW_CHAIN_GOVERNANCE_PROPOSAL_REVIEWER_REBUTTAL_2026-05-19.md` —
   first-round rebuttal that triggered V2.
3. The four governance/compat surfaces named by V2 candidates:
   - `governance/compat/check_workflow_orchestration_guard.py` (C1 target —
     public-sync only; do not modify, just read for context)
   - `governance/compat/check_governed_pack_contract.py` if present (C2)
   - `governance/compat/check_execute_route_step_sequence.py` if present (C3)
   - `governance/compat/check_continuation_chain.py` (C4)
4. The three governed pack policy files (C2 context):
   - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/app_builder_complete/execution.policy.json`
   - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/documentation/execution.policy.json`
   - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/strategy_analysis/execution.policy.json`
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` (C3 context only).

If `MEMORY.md` notes that C1/C2/C3/C4 were already closed earlier (commit
`f253db00` neighborhood), cite that history in the rebuttal and adjust per-
candidate verdicts accordingly. A candidate already CLOSED is grounds for a
`CLOSED_BY_PRIOR_TRANCHE` disposition rather than a fresh rebuttal verdict.

### Step N2.2 — Author Rebuttal File

File path: `docs/reviews/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_CODEX_REBUTTAL_2026-05-19.md`

Required structure (per CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD review
type):

- Frontmatter: `Memory class: FULL_RECORD`, `Status: REBUTTAL_FILED_<verdict>`, `Reviewer: Codex`, `Date: 2026-05-20`.
- `## Purpose`
- `## Scope / Target / Owner Boundary`
- `## Source / Target` (V2 roadmap path + queue item id)
- `## Scope / Methodology`
- `## Findings / Position` (must contain four candidate subsections C1/C2/C3/C4)
- `## Per-Candidate Verdict Table` (summary table of the four verdicts)
- `## Risk / Corrective Action`
- `## Final Disposition` (overall verdict + queue disposition instructions)
- `## Claim Boundary`

The Per-Candidate Verdict Table must use this shape:

| Candidate | V2 stated risk | V2 stated GC-018 | Verdict | Required downstream gate |
| --- | --- | --- | --- | --- |
| C1 | … | … | … | … |
| C2 | … | … | … | … |
| C3 | … | … | … | … |
| C4 | … | … | … | … |

### Step N2.3 — Update Queue Item

After the rebuttal file is committed, update
`CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` for the `workflow-chain-governance-v2`
item:

- `status`: change from `READY_FOR_REBUTTAL` to one of:
  - `REBUTTAL_FILED_NON_BLOCKING`
  - `REBUTTAL_FILED_NON_BLOCKING_WITH_GATE_UPDATE`
  - `REBUTTAL_FILED_BLOCKING`
  - `REBUTTAL_FILED_MIXED` (use if candidates have different verdicts)
  - `REBUTTAL_FILED_CLOSED_BY_PRIOR_TRANCHE` (use if all four candidates
    were already closed before V2 was filed)
- Add `responsePath` pointing to the rebuttal file path.
- Adjust `priority` if the queue ordering changes after this rebuttal.
- Update `notes` with the one-line per-candidate verdict summary.

### Step N2.4 — Closure Review

File path: `docs/reviews/CVF_N2_WORKFLOW_CHAIN_V2_REBUTTAL_CLOSURE_REVIEW_2026-05-20.md`

Required structure: Purpose, Target, Scope/Methodology, Findings,
Decision/Disposition, Claim Boundary.

The closure review must confirm:

- Rebuttal file filed at the queue's `expectedResponsePath`.
- Per-candidate verdict present for C1, C2, C3, C4.
- Per-candidate verdict cites at least one concrete evidence surface.
- Queue item `workflow-chain-governance-v2` updated.
- No V2 candidate was implemented in this tranche.
- No guard / registry / runtime / pack policy file was modified.
- No GC-018 was filed from this tranche.
- Pre-commit and pre-push hooks PASS on the governance repo.

---

## Acceptance Criteria

All of the following must be true before this work order is CLOSED:

- [ ] Rebuttal file exists at
      `docs/reviews/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_CODEX_REBUTTAL_2026-05-19.md`
      with all required structural sections.
- [ ] Per-candidate verdict table present and complete for C1, C2, C3, C4.
- [ ] Every candidate verdict cites at least one concrete evidence surface
      (file path / commit SHA / V2 section anchor).
- [ ] `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` updated for
      `workflow-chain-governance-v2`: `status`, `responsePath`, `notes`.
- [ ] Closure review filed at
      `docs/reviews/CVF_N2_WORKFLOW_CHAIN_V2_REBUTTAL_CLOSURE_REVIEW_2026-05-20.md`.
- [ ] No new GC-018, no work order, no guard / registry / runtime changes.
- [ ] No public-sync push.
- [ ] Pre-commit hook PASS (11/11).
- [ ] Pre-push hook PASS (43/43).
- [ ] Handoff GC-020 HEAD SHA synced after closure commit.

---

## Forbidden Actions

- Do NOT implement any V2 candidate.
- Do NOT file GC-018 for any V2 candidate.
- Do NOT dispatch a downstream work order from this tranche.
- Do NOT modify any guard file under `governance/compat/`.
- Do NOT modify any policy file under `governance/toolkit/05_OPERATION/`.
- Do NOT modify any pack policy JSON or runtime route.
- Do NOT touch the public-sync repo.
- Do NOT edit the V2 roadmap itself.
- Do NOT bundle N3 work into this tranche.
- Do NOT use `git add -A` or `git add .`.
- Do NOT reopen any A–H Review-CVF pain point.

---

## Authority Chain

- Authorized by: Codex rebuttal verdict NON_BLOCKING_AS_REBUTTAL_ONLY_WITH_QUEUE_CORRECTION
  on N2 candidate, 2026-05-20.
- Roadmap: `docs/roadmaps/CVF_POST_RESIDUAL_CLOSURE_NEXT_ROADMAP_2026-05-20.md`
  (REBUTTAL_FILED_NON_BLOCKING_WITH_GATE_UPDATE).
- Queue item: `workflow-chain-governance-v2` (priority 2).
- Orchestrator: Claude; Worker: Codex (Reviewer role); Operator approval not
  required for a rebuttal cycle.

---

## Agent Roles

- Worker (Codex Reviewer): reads V2 + predecessor evidence, files
  per-candidate rebuttal, updates queue item, files closure review.
- Orchestrator (Claude): reviews closure review; dispatches downstream
  GC-018 / work order only after operator decision per accepted candidate.

---

## Required First Reads

1. `docs/roadmaps/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_2026-05-19.md` —
   the artifact under review.
2. `docs/reviews/CVF_WORKFLOW_CHAIN_GOVERNANCE_PROPOSAL_REVIEWER_REBUTTAL_2026-05-19.md` —
   first-round rebuttal on V1.
3. `docs/roadmaps/CVF_POST_RESIDUAL_CLOSURE_NEXT_ROADMAP_2026-05-20.md` —
   N2 scope.
4. `docs/reviews/CVF_POST_RESIDUAL_CLOSURE_NEXT_ROADMAP_CODEX_REBUTTAL_2026-05-20.md` —
   N2 verdict + boundary.
5. `MEMORY.md` Project Timeline entries naming C1/C2/C3/C4 closures (if any).
6. `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md` —
   required review structure.

---

## Pre-Flight Checks

- [ ] Governance repo working tree CLEAN before starting.
- [ ] Confirm rebuttal file does not already exist at the expected path.
- [ ] Confirm V2 roadmap status is still `READY_FOR_REBUTTAL` in the queue
      before filing.
- [ ] Read the V2 roadmap in full before drafting any verdict.
- [ ] If C1/C2/C3/C4 were already CLOSED in a prior tranche, plan to use
      the `CLOSED_BY_PRIOR_TRANCHE` disposition pattern.

---

## Write Ownership

May create only:

- `docs/reviews/CVF_WORKFLOW_CHAIN_GOVERNANCE_ROADMAP_V2_CODEX_REBUTTAL_2026-05-19.md`
  (new — the rebuttal file)
- `docs/reviews/CVF_N2_WORKFLOW_CHAIN_V2_REBUTTAL_CLOSURE_REVIEW_2026-05-20.md`
  (new — the closure review)

May modify only:

- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json` (queue item status update)
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` (next-allowed-move update after
  closure)
- `AGENT_HANDOFF_V10_2026-05-19.md` (status line + GC-020 HEAD SHA sync)

No other files may be created or modified in either repo.

---

## Execution Plan

1. Pre-flight checks (Section: Pre-Flight Checks).
2. Read V2 + predecessor evidence (Step N2.1).
3. Author rebuttal file with per-candidate verdicts (Step N2.2).
4. Update queue item (Step N2.3).
5. File closure review (Step N2.4).
6. Update session state nextAllowedMove + handoff.
7. Commit + GC-020 sync.

---

## Evidence Requirements

- Rebuttal file with per-candidate verdict table, every cell filled.
- Every candidate verdict cites a concrete evidence surface.
- Queue item status updated and JSON parses cleanly.
- Closure review confirms zero implementation, zero GC-018, zero
  guard/runtime/pack changes.

---

## Review Gate

Stop and return to Orchestrator if:

- V2 roadmap requires reading source files outside the V2-named surfaces to
  reach a verdict (suggests V2 has hidden-scope inflation).
- Any candidate cannot reach a clear verdict from V2 + predecessor evidence.
- Filing the rebuttal would require modifying any V2 candidate's target
  surface to disambiguate the verdict.
- A V2 candidate name (C1, C2, C3, C4) is already CLOSED with a closure
  review filed, but V2 does not acknowledge that closure — flag as
  `CLOSED_BY_PRIOR_TRANCHE` and report.

---

## Non-Goals

- Implementing V2 candidates (C1 hardening, C2 pack contract guard,
  C3 execute-route step sequence guard, C4 continuation chain guard).
- Filing GC-018 for any V2 candidate.
- Modifying any guard file or registry JSON.
- Touching the public-sync repository.
- Filing N3 work or skill corpus repair roadmap.
- Reopening any closed A–H pain point.

---

## Work Plan

Sequential:

1. Read V2 + predecessors (Step N2.1).
2. Draft per-candidate verdicts in a scratch outline.
3. Author the rebuttal file with all required structural sections
   (Step N2.2).
4. Update queue item JSON (Step N2.3).
5. File closure review (Step N2.4).
6. Update session state + handoff.
7. Commit using HEREDOC commit message; do not amend.

If any review-gate condition fires, stop and report to Orchestrator before
proceeding.

---

## Closure Checklist

- [ ] Rebuttal file filed with all required structural sections.
- [ ] Per-candidate verdict table complete for C1/C2/C3/C4.
- [ ] Queue item `workflow-chain-governance-v2` updated.
- [ ] Closure review filed.
- [ ] Session state nextAllowedMove updated.
- [ ] Handoff GC-020 HEAD SHA synced.
- [ ] Pre-commit + pre-push hooks PASS.
- [ ] No guard / registry / runtime / pack change.
- [ ] No GC-018, no downstream work order.
- [ ] No public-sync push.

---

## Return-To-Orchestrator Conditions

Return if:

- V2 verdict requires touching files outside the V2-named surfaces.
- Any V2 candidate is already CLOSED and V2 does not acknowledge it.
- Markdown structural completeness hook blocks the rebuttal file and the
  fix is not obvious from existing closure reviews.
- Queue JSON parse fails after the update.
- Hook failure outside this scope.

---

## Claim Boundary

This work order covers a single Reviewer-role rebuttal cycle on the V2
workflow-chain roadmap plus its closure review, queue update, and
GC-020-compatible handoff sync. It does not authorize new code, new tests,
new policy, new GC-018, new work orders, runtime changes, pack policy
changes, or any public claim expansion. It does not preempt N3 (skill
corpus repair roadmap) in the post-residual roadmap.
