# Work Order — Multi-Role Codex Quality Hardening

Memory class: FULL_RECORD

Status: READY_FOR_IMPLEMENTATION

docType: work_order

Worker role: Codex

Date dispatched: 2026-05-21

---

## Purpose

Close two quality gaps confirmed by Claude's post-tranche audit and Codex's
rebuttal (`docs/reviews/CVF_WO_MULTI_ROLE_QUALITY_HARDENING_CLAUDE_AUDIT_REBUTTAL_2026-05-21.md`):

1. **Confirmed: false positive in `check_markdown_structural_completeness.py`**
   — the classifier mis-classifies `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`
   as `baseline` because the file has no `docType:` frontmatter field, causing
   5 spurious violations in retrospective scans (`--all-changed` mode).
   Evidence: retrospective scan `--base 6a45310e --head HEAD --all-changed`
   shows exactly this violation and no others.

2. **Confirmed: no operator-checkpoint mechanism in work order gate** — the
   pre-commit hook checks only files in the current staging area
   (`--base HEAD --head HEAD`), so a fast multi-commit Codex run can land many
   slices without any operator sign-off between them. No existing GC-045
   section enforces this.

Note: two other concerns raised in Claude's initial audit were rejected by
Codex rebuttal and are NOT targets of this work order:

- HN2.b/HN2.c work-order format: both files are fully compliant in the current
  repository; Claude's reading was from a stale untracked state.
- `docs/assessments/` governance recognition: folder is already present in
  `docs/INDEX.md` and governance scripts; CLAUDE.md is not the authoritative
  docs taxonomy source.

---

## Authority Chain

- Audit source: Claude post-tranche quality assessment, 2026-05-21
- Codex rebuttal: `docs/reviews/CVF_WO_MULTI_ROLE_QUALITY_HARDENING_CLAUDE_AUDIT_REBUTTAL_2026-05-21.md`
- Governance guard: `governance/toolkit/05_OPERATION/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_GUARD.md`
- Completeness standard: `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md`
- Hook chain: `governance/compat/run_local_governance_hook_chain.py`
- Control matrix: `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`

---

## Agent Roles

- Orchestrator: Codex converts this work order into a sequenced execution plan.
- Reviewer: Codex files the non-blocking rebuttal for each sub-task before
  implementing.
- Implementer: Codex applies the code and document changes.
- Auditor: Codex runs all affected checks with `--enforce` and records results
  in the closure checklist.

No Claude participation required; this is a Codex-only closure.

---

## Scope / Target / Owner Boundary

In scope:

- Fix 1: add `docType: reference` to `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`.
- Fix 2: add a `reference` classifier branch to
  `governance/compat/check_markdown_structural_completeness.py` so that
  `docs/reference/` files with `docType: reference` are checked against a
  minimal reference-document section set (purpose + scope/applies-to +
  claim/final boundary) instead of the `baseline` template.
- Fix 3: add an `## Operator Checkpoint` section to the `work_order` template
  in `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md` and
  to the `work_order` section group in
  `governance/compat/check_markdown_structural_completeness.py`, so that every
  new work order must declare either a required operator checkpoint or an
  explicit waiver with justification.
- Update the `docs/INDEX.md` and any cross-reference if the standard or guard
  documents change.
- File a completion review.

Out of scope:

- Retroactively patching any already-committed work order to add the new
  section (grandfathered; only new work orders are enforced by the gate).
- Changing the pre-commit hook's `--base HEAD --head HEAD` range to a
  full-branch retrospective scan (high-cost, not recommended).
- Adding new governance controls beyond the three fixes above.
- Any runtime, provider, memory, Maika, doctrine, or freeze-posture change.
- Public-sync update.

---

## Required First Reads

- `governance/compat/check_markdown_structural_completeness.py` (full file)
- `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md`
- `governance/toolkit/05_OPERATION/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_GUARD.md`
- `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` (first 15 lines)
- `governance/compat/run_local_governance_hook_chain.py` (pre-commit chain entry)

---

## Pre-Flight Checks

- Confirm `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` has no `docType:`
  field today (root cause of false positive).
- Confirm `_classify()` in the completeness script has no `reference` branch
  today.
- Confirm `SECTION_GROUPS` in the completeness script has no `reference` key
  today.
- Confirm `work_order` SECTION_GROUPS has no `operator_checkpoint` entry today.
- Run `python governance/compat/check_markdown_structural_completeness.py
  --base HEAD --head HEAD --enforce` before starting; must be COMPLIANT (0
  violations for staged files).

---

## Write Ownership

Permitted writes:

| File | Change |
| --- | --- |
| `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` | Add `docType: reference` after `Memory class:` line |
| `governance/compat/check_markdown_structural_completeness.py` | (a) add `reference` branch in `_classify()`; (b) add `reference` key in `SECTION_GROUPS`; (c) add `operator_checkpoint` tuple to `work_order` section group |
| `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md` | Add `## Operator Checkpoint` section to the Work Order template block |
| `governance/toolkit/05_OPERATION/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_GUARD.md` | Update guard to note `reference` document type and operator-checkpoint requirement |
| `docs/reviews/CVF_WO_MULTI_ROLE_QUALITY_HARDENING_COMPLETION_2026-05-21.md` | New completion review |

No other files may be modified.

---

## Execution Plan

### Step 1 — Fix 1: add `docType` to control matrix

Add the line `docType: reference` immediately after the `Memory class:` line in
`docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md`.

Verify: `grep "docType" docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` must
return `docType: reference`.

### Step 2 — Fix 2: add `reference` classifier and section group

In `governance/compat/check_markdown_structural_completeness.py`:

a. In `_classify()`, add a branch **before** the final `return "spec"` fallback:

```python
if normalized_path.startswith("docs/reference/"):
    return "reference"
```

b. Add a `reference` key to `SECTION_GROUPS`:

```python
"reference": (
    ("purpose", (r"^##\s+Purpose\b",)),
    (
        "scope/applies-to",
        (
            r"^##\s+Scope\b",
            r"^##\s+Applies To\b",
            r"\*\*Applies to:\*\*",
        ),
    ),
    (
        "claim/final/verification boundary",
        (
            r"^##\s+Claim Boundary\b",
            r"^##\s+Final Clause\b",
            r"^##\s+Verification\b",
            r"^##\s+Current Closure Statement\b",
        ),
    ),
),
```

Verify: run `python governance/compat/check_markdown_structural_completeness.py
--base HEAD --head HEAD --enforce` with `CVF_GOVERNANCE_CONTROL_MATRIX.md`
staged — must show 0 violations for that file.

### Step 3 — Fix 3: add `operator_checkpoint` to work_order section group

a. In `SECTION_GROUPS["work_order"]`, append:

```python
(
    "operator checkpoint",
    (
        r"^##\s+(?:\d+\.\s+)?Operator Checkpoint\b",
        r"operator.checkpoint.waiver",
    ),
),
```

b. In `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md`, add
to the **Work Order** artifact template:

```markdown
## Operator Checkpoint

<!-- Required. Choose one: -->

Checkpoint required: [describe what operator must confirm before Implementer
proceeds, e.g. "operator must confirm scope is bounded to X before Codex opens
the next slice"].

<!-- OR, if genuinely waived: -->

operator.checkpoint.waiver: [one-sentence justification, e.g. "single-commit
documentation-only change; no implementation boundary risk"].
```

c. In `governance/toolkit/05_OPERATION/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_GUARD.md`,
add a bullet noting the `reference` document type and the operator-checkpoint
requirement for work orders.

### Step 4 — GC-023 pre-flight before all edits

Before editing any existing file:

- Check current line count of the file.
- Check `governance/compat/CVF_GOVERNED_FILE_SIZE_EXCEPTION_REGISTRY.json` for
  that file's `approvedMaxLines`.
- If adding lines would exceed the limit, split as required.

### Step 5 — Run full verification suite

Run all of the following and record results in the closure checklist:

```
python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base 6a45310e --head HEAD --all-changed --enforce
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/check_governed_artifact_authoring.py --enforce
python governance/compat/check_docs_governance_compat.py --base HEAD --head HEAD --enforce
```

All five must exit 0.

### Step 6 — File completion review

File `docs/reviews/CVF_WO_MULTI_ROLE_QUALITY_HARDENING_COMPLETION_2026-05-21.md`
with evidence trace block showing each fix and each verification result.

---

## Evidence Requirements

| Claim | Required evidence |
| --- | --- |
| False positive eliminated | `check_markdown_structural_completeness.py` returns 0 violations for `CVF_GOVERNANCE_CONTROL_MATRIX.md` in both HEAD..HEAD and retrospective scan |
| `reference` classifier correct | `_classify("docs/reference/X.md", ...)` returns `"reference"` |
| `reference` section group correct | reference files that lack Purpose/Scope/Boundary produce a violation; files that have them pass |
| Operator-checkpoint gate active | A test work order without `## Operator Checkpoint` or `operator.checkpoint.waiver` produces a `missing work_order section: operator checkpoint` violation |
| Operator-checkpoint gate does not break existing work orders | All currently committed work orders still pass (they are grandfathered by being pre-existing, not new/added files in the diff) |
| GC-023 compliance | `check_governed_file_size.py --enforce` exits 0 after all edits |

---

## Acceptance Criteria

- [ ] `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` has `docType: reference`.
- [ ] `_classify()` returns `"reference"` for `docs/reference/` paths.
- [ ] `SECTION_GROUPS["reference"]` exists with purpose + scope + boundary groups.
- [ ] `SECTION_GROUPS["work_order"]` contains `operator_checkpoint` tuple.
- [ ] Work Order template in the standard document has `## Operator Checkpoint`.
- [ ] Guard document updated.
- [ ] Retrospective scan (`--base 6a45310e --head HEAD --all-changed`) exits 0.
- [ ] Staged-only scan (`--base HEAD --head HEAD`) exits 0.
- [ ] `check_governed_file_size.py --enforce` exits 0.
- [ ] Completion review filed.

---

## Review Gate

Close only after Step 5 verification suite exits 0 on all five commands.
Do not close if any existing work order that was COMPLIANT before this change
becomes non-compliant after.

---

## Closure Checklist

- [ ] Pre-flight checks confirmed.
- [ ] Fix 1 applied (docType field).
- [ ] Fix 2 applied (reference classifier + section group).
- [ ] Fix 3 applied (operator_checkpoint in work_order group + standard + guard).
- [ ] GC-023 line-count pre-flight done for each modified file.
- [ ] All 5 verification commands exit 0.
- [ ] Completion review filed.
- [ ] Active session state / review queue updated if needed.

---

## Return-To-Orchestrator Conditions

Return to Orchestrator (do not close) if:

- Any currently-passing work order becomes non-compliant after Fix 3.
- `check_governed_file_size.py` reports a new hard violation.
- The retrospective scan (`--base 6a45310e`) still shows violations after all
  three fixes.
- The scope requires changing the pre-commit hook range or adding new governance
  controls not listed here.

---

## Operator Checkpoint

Checkpoint required: operator must confirm that the three fixes are acceptable
in scope before Codex proceeds to implementation (Step 1–3). Specifically,
confirm that adding `operator.checkpoint.waiver` as an alternative to
`## Operator Checkpoint` is acceptable (i.e., operator does not want to require
a hard checkpoint on every single-commit doc-only work order).

---

## Claim Boundary

This work order closes only the three targeted quality gaps. It does not
authorize new governance controls beyond what is listed, does not change the
pre-commit hook diff range, does not modify runtime behavior, and does not
lift freeze posture.
