# CVF Workflow Chain Governance — Proposal for Reviewer Rebuttal

Memory class: SUMMARY_RECORD

Status: PROPOSAL — 2026-05-19. Not yet authorized. Filed by Orchestrator
role for Reviewer-role rebuttal before any GC-018 is opened.

## Purpose

Propose four bounded guard candidates that close workflow-chain integrity
gaps identified after `check_workflow_orchestration_guard.py` was added.
Goal: turn CVF from "collection of guards" into "workflow chain system"
without duplicating existing 94-guard inventory.

## Scope / Target / Owner Boundary

Scope: workflow chain integrity at four layers of the CVF surface.
Owner: any agent in `Orchestrator` role may file the GC-018 packets;
implementation owner per packet TBD.
Out of scope: replacing existing guards, modifying canonical role
taxonomy, introducing persona-named roles.

## Non-goals

- Do not authorize any implementation from this proposal alone.
- Do not replace the existing guard inventory with one wide guard.
- Do not introduce persona-named roles or agent-vendor-specific workflow
  rules.
- Do not claim full workflow-chain enforcement until the accepted candidate
  guards have their own GC-018 packets, tests, and hook-chain evidence.

## Role Vocabulary Used in This Document

This document uses canonical CVF role names from `cvf-guard-contract`:

- `OPERATOR` — human owner of the session/repo (final authority)
- `Orchestrator` — agent role that files GC-018, dispatches work orders
- `Reviewer` — agent role that rebuts proposals, audits deliveries
- `Worker` — agent role that implements changes per work order
- `Auditor` — agent role that signs evidence

These are NOT persona names (not "Claude", not "Codex", not "Alibaba").
Any agent may inhabit any role on any tranche.

Canonical sources:
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` lines 33-42 — `CVFRole`:
  `OBSERVER | ANALYST | BUILDER | REVIEWER | GOVERNOR | HUMAN |
   AI_AGENT | OPERATOR | SERVICE_AGENT`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/phase2b-wireup.contract.ts`
  line 47-56 — `AgentFunctionRole`:
  `executor | observer | orchestrator | architect | builder | reviewer | ...`

When this proposal says "Worker", it maps to `BUILDER` (CVFRole) or
`builder`/`executor` (AgentFunctionRole). When it says "Reviewer", it
maps to both `REVIEWER` taxa.

## Source / Predecessor Evidence

- `governance/compat/check_workflow_orchestration_guard.py` (added by
  Worker role, commit `111daaab` in public-sync repo) — canonical entry
  point for workflow-chain governance; this proposal extends its pattern
- OPERATOR feedback 2026-05-19: CVF only becomes a "system" when
  workflow chains across module/layer are routed through canonical gates
- OPERATOR direction 2026-05-19: do NOT use persona-named guards;
  use role-based naming; check duplicates before adding new guards

## The four workflow chain layers

CVF currently has guards at the **node level** (94 atomic checks) but
not at the **chain level** (multi-node integrity). The four layers
below are chain-level gaps.

| # | Layer | Existing coverage (post-check) | Chain gap |
|---|---|---|---|
| 1 | CI/Release YAML ↔ canonical runner | `check_workflow_orchestration_guard.py` (NEW) | Brittle string match, no test, hard-coded REQUIRED_COMMANDS |
| 2 | Governed Pack 3-file contract (`workflow.spec.md` ↔ `execution.policy.json` ↔ `receipt.schema.json`) | `check_template_skill_standard_guard_compat.py` enforces template/skill companion docs but does NOT validate the 3-file pack contract or pack-id ↔ template-id binding | No guard ensures pack folder has all 3 files; no guard ensures pack `id` matches template `id` |
| 3 | Execute Route step sequence (resolve role → check permission → build prompt → guard pipeline → provider call → receipt → audit) | None — each step is implemented; sequence is not enforced | `route.ts` is at the 1001-line cap; refactor can reorder/skip steps without test failure |
| 4 | Continuation Chain (work order → review packet → GC-018 closure → handoff sync) | `check_agent_handoff_guard_compat.py` (handoff template chain), `check_depth_audit_continuation_compat.py` (GC-018 reopen) — neither validates the upstream work-order → review → handoff sequence | Orphan work orders or orphan reviews not detected; handoff HEAD SHA drift after closure not caught |

## Duplication audit (must read before approving any new guard)

Before any new guard is added, the Orchestrator role MUST reconcile
against this duplicate-check table:

| Proposed guard | Existing guard with potential overlap | Verdict after read |
|---|---|---|
| Layer 2 — Governed Pack Contract | `check_template_skill_standard_guard_compat.py` | DIFFERENT — existing guard validates "template/skill companion documentation" (markdown standards, roadmaps). Does NOT validate pack-folder 3-file contract or pack ↔ template id binding. Adding Layer 2 guard does NOT duplicate; but Layer 2 guard MUST cite this existing guard as adjacent. |
| Layer 3 — Execute Chain Step Sequence | None found in 94-guard scan | NEW SURFACE — no existing guard reads `route.ts` for step ordering |
| Layer 4 — Continuation Chain | `check_agent_handoff_guard_compat.py` + `check_depth_audit_continuation_compat.py` | OVERLAP RISK — existing two guards cover handoff template + GC-018 reopen; do not cover work-order → review packet binding. Layer 4 guard MUST start by referencing both and explicitly scope to the upstream gap (work order ↔ review packet). |
| Layer 1 hardening (test + JSON registry) | `check_workflow_orchestration_guard.py` itself | NOT a new guard — improvement to the existing one; no duplication |

Reviewer role MUST verify this table during rebuttal and reject any
proposal where overlap is not explicitly carved out.

## Proposed work — four candidates

Each candidate is a separate GC-018. The Orchestrator role files them
in the order shown. The Reviewer role may rebut any candidate.

## Work Plan

The work plan is deliberately split into four independently reviewable
candidates:

1. Harden the existing workflow orchestration guard with tests, registry data,
   and receipt emission.
2. Add a governed pack contract guard only after duplicate-surface review
   against existing template and guard-contract checks.
3. Add execute-route sequence enforcement after recording current route order
   in a registry and proving broken fixtures fail.
4. Add continuation-chain enforcement after reconciling with active-session,
   handoff, and depth-audit guards.

Candidate 1 is the preferred first tranche because it strengthens the
self-protecting guard surface that later candidates would join.

---

### Candidate 1 — Harden Layer 1 guard (`check_workflow_orchestration_guard.py`)

**Type:** Improvement to existing guard. No new guard file.
**Risk:** R0 — documentation, tests, refactor of literal string match.
**GC-018 required:** No — R0 hardening of existing guard is in-scope for
the Worker role under the existing META_GUARD policy. File a one-page
preflight if uncertain.

**Detailed solution:**

1. **Test file:** `governance/compat/test_check_workflow_orchestration_guard.py`
   with at least these cases:
   - compliant fixture (all REQUIRED_COMMANDS present) → `compliant == True`
   - missing required workflow file → 1 violation with `path` set
   - command fragment missing in present file → 1 violation
   - fragmented static marker in workflow YAML → 1 violation
   - file path normalization (backslash vs forward slash on Windows) → no false positive
   - JSON output mode → emits valid JSON with `compliant` boolean

2. **Robustness:** replace `_normalize()` collapse-whitespace approach
   with **token-presence** check:
   - Tokenize required fragment by whitespace
   - Check each token appears in target file (order independent within line)
   - Catches accidental quoting (`"scripts/foo.py"` vs `scripts/foo.py`)

3. **Externalize REQUIRED_COMMANDS:** move to
   `governance/compat/CVF_WORKFLOW_ORCHESTRATION_REGISTRY.json` so the
   list is audit-friendly and changes to required surfaces are tracked
   as data, not code edits. Guard reads JSON, validates schema, then
   applies same logic. Schema includes `surface`, `requiredFragments`,
   `addedAt`, `addedBy` (role, not persona).

4. **Receipt emission:** when `--enforce`, append a one-line JSONL
   entry to `docs/evidence/workflow-orchestration-guard.jsonl` recording
   `timestamp`, `compliant`, `violationCount`. Matches the audit-trail
   pattern of other guards.

**Acceptance:** `python governance/compat/check_workflow_orchestration_guard.py`
PASS; new test file PASS via `pytest`; JSON registry validates;
JSONL receipt appears on enforce run.

---

### Candidate 2 — Governed Pack Contract Guard

**File:** `governance/compat/check_governed_pack_contract.py`
**Policy:** `governance/toolkit/05_OPERATION/CVF_GOVERNED_PACK_CONTRACT_GUARD.md`
**Risk:** R0 — read-only validation; does not modify packs.
**GC-018 required:** Yes — new guard adds enforcement surface.

**Adjacent existing guards (must cite, do not duplicate):**
- `check_template_skill_standard_guard_compat.py` — companion docs
- `check_guard_contract_compat.py` — guard contract compatibility

**Detailed solution:**

1. **Discover packs:** scan
   `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/`
   directory; each subfolder is a pack candidate.

2. **Per-pack invariants (4 rules):**
   - Rule A: folder MUST contain exactly `workflow.spec.md`,
     `execution.policy.json`, `receipt.schema.json` (other files allowed
     but the three MUST exist).
   - Rule B: `execution.policy.json` MUST be valid JSON with `templateId`
     field; `templateId` MUST appear as an `id:` value in some
     `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates/*.ts`
     file (verified by grep, not full TS parse).
   - Rule C: `workflow.spec.md` MUST contain a `## Steps` section with
     at least 1 step; each step name MUST appear as a key in
     `execution.policy.json`.
   - Rule D: `receipt.schema.json` MUST be valid JSON Schema (draft-07
     or later) with a `stepTraces` field; the schema for `stepTraces`
     MUST accept one entry per step declared in `workflow.spec.md`.

3. **Acceptance test fixtures:** add fixtures for all 3 existing packs
   (`app_builder_complete`, `documentation`, `strategy_analysis`) — they
   MUST pass. Add a synthetic broken pack fixture to prove the guard
   catches violations.

4. **Wire-in:** add to
   `governance/compat/run_local_governance_hook_chain.py` as a new step;
   add to `scripts/run_cvf_static_ci_gate.py` if mirroring to public-sync.

**Acceptance:** all 3 existing packs PASS; synthetic broken pack FAIL;
new pack added in Lane F (`OutcomeQuickActions`) automatically validated.

---

### Candidate 3 — Execute Route Step Sequence Guard

**File:** `governance/compat/check_execute_route_step_sequence.py`
**Policy:** `governance/toolkit/05_OPERATION/CVF_EXECUTE_ROUTE_STEP_SEQUENCE_GUARD.md`
**Risk:** R1 — guard reads source code; brittle to refactor; high value.
**GC-018 required:** Yes — new enforcement surface on critical runtime path.

**Adjacent existing guards (must cite, do not duplicate):**
- None reads `route.ts` for ordering. Existing guards read
  `route.ts` only for handoff/audit imports.

**Detailed solution:**

1. **Canonical step list** (read from `route.ts` current line numbers
   recorded in `CVF_EXECUTE_ROUTE_STEP_SEQUENCE_REGISTRY.json`):

   ```
   1. resolveExecutionCVFRole          (role identity)
   2. checkExecuteRolePermissionGate   (output permission)
   3. buildExecutePromptContract       (intake binding)
   4. executeRouteGuards               (R-class evaluation)
   5. provider call (via gateway)      (provider invocation)
   6. buildRouteAuditMemoryCapture     (receipt)
   7. emit audit event                 (audit ledger)
   ```

2. **Detection method:** read `route.ts` as text; for each step, find
   the line number of its canonical call site (use a regex per step name
   to avoid false positives on import lines). Assert that line numbers
   are strictly increasing in the canonical order. Permit branches
   (conditional skips) as long as the ORDER of calls that DO happen
   matches canon.

3. **Externalize step registry:**
   `governance/compat/CVF_EXECUTE_ROUTE_STEP_SEQUENCE_REGISTRY.json`
   stores `{stepName, callPattern, requiredOrder, addedAt}`. When CVF
   adds a new mandatory step (e.g., memory capture in Lane H), register
   it here.

4. **Two-mode operation:**
   - `--check` (default): pass if canonical order found in route.ts
   - `--enforce`: exit 2 on any violation

5. **Test fixtures:** snapshot current `route.ts` as a passing fixture;
   add 3 broken fixtures (skipped step, reordered step, duplicate step)
   to prove the guard catches each.

**Acceptance:** current `route.ts` PASS; all 3 broken fixtures FAIL;
guard runs in <2 seconds; covered by test file.

---

### Candidate 4 — Continuation Chain Guard

**File:** `governance/compat/check_continuation_chain.py`
**Policy:** `governance/toolkit/05_OPERATION/CVF_CONTINUATION_CHAIN_GUARD.md`
**Risk:** R0 — process guard; reads file existence and grep patterns only.
**GC-018 required:** Yes — new enforcement surface, but R0.

**Adjacent existing guards (must cite, do NOT duplicate):**
- `check_agent_handoff_guard_compat.py` — handoff template chain
  (does not check work-order → review binding)
- `check_depth_audit_continuation_compat.py` — GC-018 reopen
  (does not check work-order → review binding)
- `check_active_session_state.py` — front-door pointers
  (does not check work-order → review binding)

This guard fills the gap **upstream** of those three: from work-order
delivered → review packet exists → GC-018 closure exists → handoff updated.

**Detailed solution:**

1. **Chain definition** — for any file matching
   `docs/work_orders/CVF_AGENT_WORK_ORDER_*.md`:
   - Step A: MUST reference a GC-018 baseline file path (regex match
     against `docs/baselines/CVF_GC018_*.md`)
   - Step B: when work order body contains `Status: DELIVERED` or
     `Status: COMPLETE`, a matching review packet MUST exist at
     `docs/reviews/CVF_*_WORK_ORDER_COMPLETION_REVIEW_*.md` referencing
     the work order by filename
   - Step C: the latest commit touching the work order or review packet
     MUST be followed by a handoff commit (`AGENT_HANDOFF_V*.md` change
     within next 5 commits)

2. **Orphan detection:**
   - Orphan work order: `Status: DELIVERED` but no review packet exists
   - Orphan review packet: review packet exists but its referenced work
     order file does not exist
   - Stale handoff: most recent work order closure (review packet) is
     more than 10 commits behind current handoff HEAD SHA

3. **Externalize chain map:**
   `governance/compat/CVF_CONTINUATION_CHAIN_REGISTRY.json` records the
   3-step contract and exemption list (e.g., legacy work orders that
   close differently).

4. **Reuse, do not duplicate:** import path constants from
   `check_active_session_state.py` for handoff location; import GC-018
   detection logic from `check_depth_audit_continuation_compat.py`.

**Acceptance:** scan of current `docs/work_orders/` produces 0 orphans
(or a documented exemption list); guard catches 3 synthetic broken
fixtures (missing review, missing GC-018, stale handoff).

---

## Ordering and dependencies

```
Candidate 1 (R0, no GC-018) ──► Candidate 2 (R0, GC-018) ──► Candidate 3 (R1, GC-018)
                              ──► Candidate 4 (R0, GC-018) ──┘
```

- Candidate 1 must complete first because Candidates 2–4 are added to
  the `REQUIRED_COMMANDS` self-protecting list of Candidate 1.
- Candidates 2 and 4 can proceed in parallel (independent layers).
- Candidate 3 is highest impact, file last because it touches the
  most-changed file (`route.ts`).

## Acceptance Criteria

- Reviewer role either accepts, rejects, or narrows each candidate separately.
- Any accepted new guard has its own GC-018 before implementation.
- Each accepted guard cites adjacent existing guards and states why it is not a
  duplicate surface.
- Each implementation includes passing positive and negative tests.
- Hook-chain wiring is present only for guards that have passed local evidence.
- Handoff/session memory records the accepted claim boundary and unresolved
  blockers.

## Verification/Evidence

Minimum evidence for this proposal packet:

- `python governance/compat/check_markdown_structural_completeness.py` passes
  for this roadmap file.
- `python governance/compat/run_local_governance_hook_chain.py --hook
  pre-commit` passes before commit.
- Any later candidate implementation records command, result, key paths, and
  verdict in its own review or completion packet.
- No public claim may cite this proposal as implementation proof; it is only a
  reviewer-rebuttal source artifact.

## Why four bounded guards, not one wide guard

| Reason | Detail |
|---|---|
| Single responsibility | Each guard owns one chain layer; failure isolation |
| Audit independence | Each guard emits its own receipt JSONL |
| Reuse the existing pattern | All 94 existing guards follow `check_<one_thing>.py`; one wide guard would break the convention |
| Self-protecting list works | Candidate 1's `REQUIRED_COMMANDS` references the other three; if any of 2/3/4 is deleted, Candidate 1 fails |
| Role-symmetry | Each chain layer has a different primary actor role; one guard cannot model that |

## Open questions for the Reviewer role

1. Is the role taxonomy used here (Orchestrator/Reviewer/Worker/Operator
   /Auditor) sufficient, or should we adopt the full `CVFRole` enum
   (`OBSERVER | ANALYST | BUILDER | REVIEWER | GOVERNOR | HUMAN |
   AI_AGENT | OPERATOR | SERVICE_AGENT`) verbatim?
2. Should Candidate 3 (Execute Route Step Sequence) be deferred until
   `route.ts` is refactored below 900 lines per GC-023, or run now and
   accept the brittleness?
3. Should Candidate 4 (Continuation Chain) include the
   `START_WITH_CVF.md` GC-018 (filed 2026-05-19) as a chain validation
   target, or is that a public-sync concern outside the governance repo?
4. Are there any of the 94 existing guards that we missed in the
   duplication audit above?

## Risk

- Risk of guard sprawl if all four are accepted: 94 → 97 guards. Mitigation: each guard MUST cite the duplication-audit table in its policy file before merge.
- Risk of brittleness in Candidate 3 (string-based detection of step
  sequence in `route.ts`): mitigated by externalized registry and
  snapshot fixture.
- Risk that this proposal itself becomes the next workflow drift if not
  routed through GC-018 → work order → review → handoff. Mitigation:
  this file is the source artifact; Reviewer role rebuts; Orchestrator
  files GC-018 packets per accepted candidate.

## Decision / Recommendation / Disposition

PROPOSAL ONLY. Awaits Reviewer-role rebuttal before Orchestrator role
files any GC-018. Acceptance of any candidate is independent — partial
acceptance is fine.

## Claim Boundary

This proposal does not authorize implementation. It does not modify any
existing guard. It does not change role taxonomy. It does not commit
public claims. It is a chain-integrity proposal filed for Reviewer
rebuttal under the standard CVF Orchestrator → Reviewer → Worker
workflow chain that this very document also seeks to formalize.
