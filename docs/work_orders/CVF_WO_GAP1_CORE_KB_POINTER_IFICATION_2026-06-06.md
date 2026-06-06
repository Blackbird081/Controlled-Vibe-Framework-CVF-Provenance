# CVF Work Order: GAP1 Core Knowledge Base Pointer-ification

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-06

dispatchBaseHead: `d6bc3553`

closureBaseHead: `d6bc3553`

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Purpose

Dispatch Claude to execute GAP 1 from the external-review gap analysis: convert
`docs/CVF_CORE_KNOWLEDGE_BASE.md` from a self-contained 769-line document into
a navigation index (pointer doc) by moving duplicated content to its canonical
owner and replacing each moved section with a one-line pointer.

This work order does not authorize: runtime changes, code, tests, dependencies,
governance-rule removal, new governance semantics, public-sync, provider proof,
hosted/production/public readiness claims, or autonomous mutation.

## Authority Chain

| Authority | Evidence | Status |
| --- | --- | --- |
| Operator instruction | 2026-06-06: "Next clean move vẫn là Core KB pointer-ification work order riêng từ GAP1 map" | ACCEPT |
| External-review gap analysis | `docs/audits/CVF_EXTERNAL_REVIEW_GAP_ANALYSIS_AND_PROPOSED_SOLUTIONS_2026-06-05.md` — GAP 1 | ACCEPT |
| Active session state | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | ACCEPT |
| Work-order template | `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md` | ACCEPT |
| GC-023 File Size Guard | `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` — active_markdown hard limit 1200L | ACCEPT |

## Worker Autonomy / No-Question Rule

Claude must implement allowed-scope edits, run required governance gates, and
repair in-scope gate failures directly. Escalate before: changing scope,
touching runtime/source code, modifying governance semantics, removing canonical
rules/principles (Sections XI–XIV extension rules), creating new canonical
owner files, changing public-sync, using secrets/quota, or touching `.git/`.

## Pre-Flight Checks

Before editing, the worker must confirm:

- `git rev-parse --short HEAD` equals `d6bc3553` or record the actual
  `executionBaseHead` if a reviewer/session-sync commit has advanced HEAD.
- `docs/CVF_CORE_KNOWLEDGE_BASE.md` exists and its current line count is
  recorded.
- Every pointer target named in the Overlap Map is checked with `Test-Path` or
  equivalent before its section is pointer-ified.
- `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/README.md` still declares
  `62 active skills`.
- `python governance/compat/run_agent_autorun_workflow_gate.py --phase
  pre-implementation --base <executionBaseHead> --head HEAD` passes before
  material edits, or any failure is repaired inside this work order's allowed
  scope.

## Write Ownership

Allowed write ownership is limited to:

- `docs/CVF_CORE_KNOWLEDGE_BASE.md`
- one completion review under `docs/reviews/`

This work order packet may be corrected by the orchestrator/reviewer before
dispatch only for source-fidelity, structural-gate, or dispatch-quality
compliance. No runtime/source, dependency, public-sync, or new canonical-owner
file writes are authorized.

## Operator Checkpoint

Operator checkpoint is required before:

- creating or editing any canonical owner file outside the allowed paths;
- deleting or paraphrasing Sections XI, XII, or XIV Extension Rules;
- changing governance semantics or mandatory rules;
- public-sync or public push;
- live/provider proof or secret/quota use;
- runtime/source code, dependency, lockfile, or `.git/` changes;
- claiming public, hosted, production, provider-quality, cost, or performance
  readiness.

## Agent Roles

| Role | Assignment |
| --- | --- |
| Worker | Claude |
| Reviewer / committer | Codex or operator after Claude returns completion evidence |
| Operator checkpoint | Required before public-sync, GC-018 expansion, canonical-owner creation, or governance-rule removal |

---

## Overlap Map (pre-verified before dispatch)

The following table was derived from a full read of all 19 sections of
`docs/CVF_CORE_KNOWLEDGE_BASE.md` (769 lines, HEAD d6bc3553).

### Sections to KEEP in Core KB (non-redundant, no external canonical owner)

| Section | Lines (approx) | Keep reason |
| --- | --- | --- |
| I — ĐỊNH DANH & ĐỊNH VỊ CVF | 17–61 | Identity table + IS/IS NOT + Product Value Doctrine — unique, frequently referenced by agents as navigation anchor |
| II — KIẾN TRÚC 5 LAYERS | 62–172 | ASCII layer diagram is the canonical visual map; not duplicated verbatim elsewhere |
| XI — NGUYÊN TẮC BẤT BIẾN | 535–551 | 11 immutable principles — referenced by CLAUDE.md and governance guards; must stay |
| XII — CHECKLIST ĐỊNH VỊ EXTENSION MỚI | 553–586 | 9-question architecture check — enforced by `CVF_ARCHITECTURE_CHECK_GUARD`; must stay |
| XIV (second, lines 691+) — EXTENSION RULES | 691–805 | Rule 1–4 including KB auto-update mandate — enforced by guard chain; must stay |

### Sections to REPLACE WITH POINTER (canonical owner exists elsewhere)

| Section | Lines (approx) | Canonical owner | Pointer target |
| --- | --- | --- | --- |
| III — LỊCH SỬ CÁC VERSION | 174–216 | `docs/reference/CVF_MODULE_INVENTORY.md` | Link + one-line description |
| IV — 4-PHASE PROCESS | 217–232 | `v1.0/` + `CLAUDE.md` architecture table | Link to CLAUDE.md layer model section |
| V — RISK MODEL R0–R3 | 233–263 | `docs/concepts/risk-model.md` (if exists) or `CLAUDE.md` | Link + one-sentence summary |
| VI — 5-LAYER SAFETY KERNEL | 264–293 | Section II already covers it; also `docs/reference/CVF_ARCHITECTURE_DIAGRAMS.md` | Merge note into Section II pointer or remove redundancy |
| VII — GOVERNANCE SYSTEM | 294–406 | `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` + `governance/toolkit/05_OPERATION/` | Link table with 5-row summary only |
| VIII — SKILL LIBRARY | 407–421 | `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/README.md` | One-line pointer with current count |
| IX — CẤU TRÚC FILE HỆ THỐNG | 423–505 | `ARCHITECTURE.md` (public) + `CLAUDE.md` key directories | Pointer + note "see CLAUDE.md for current authoritative list" |
| X — QUALITY METRICS | 508–533 | `docs/reference/CVF_RELEASE_READINESS_STATUS_2026-03-20.md` + CHANGELOG | Pointer only — metrics decay fast, central doc is canonical |
| XIII — CVF MCP SERVER | 589–676 | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/README.md` | One-line pointer |
| XIV (first, lines 678–689) — KEY DOCS | 678–689 | Navigation index — fold into new navigation section at end of pointer doc | Keep as compact table, deduplicate |
| XV — QUALITY ASSESSMENT CANON | 809–834 | `docs/reference/CVF_QUALITY_ASSESSMENT_STANDARD.md` | Link only |
| XVI — PRE-PUBLIC P3 EXECUTION ISOLATION | 836–858 | `docs/reference/CVF_PREPUBLIC_P3_READINESS.md` | Link only |
| XVII — MARKDOWN STRUCTURAL COMPLETENESS | 861–893 | `docs/reference/CVF_MARKDOWN_STRUCTURAL_COMPLETENESS_STANDARD.md` | Link only |
| XVIII — SESSION MEMORY FRONT DOOR | 896–917 | `CVF_SESSION_MEMORY.md` + `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Link only |
| XIX — GOVERNED FILE MAINTAINABILITY PLANNING | 920–end | `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` | Link only |

### IMPORTANT: Section XI auto-update rule (Rule 4 / Section XIV Rule 4)

Section XIV Rule 4 states: "Mỗi khi version/layer mới được implement, phải cập nhật Section II, III, X ngay."
After pointer-ification, Section III and X will become pointer rows.
Claude must update Rule 4 text to say "cập nhật Section II và `docs/reference/CVF_MODULE_INVENTORY.md`" to reflect the new structure. This is an in-scope consequential update — do not skip it.

---

## Scope

### Allowed scope

- Edit `docs/CVF_CORE_KNOWLEDGE_BASE.md` only:
  - Replace each "REPLACE WITH POINTER" section with a one-line pointer row in a
    unified navigation table at the end of the file (or inline, whichever reads
    more clearly — Claude's judgment)
  - Keep all "KEEP" sections verbatim — do not paraphrase, shorten, or
    restructure their content
  - Fix the one remaining stale skill count in Section VIII and Section II
    Layer 1 box: `131 active skills` → `62 active skills`
    (source: `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/README.md` line 16)
  - Update Section XIV Rule 4 text as described in the IMPORTANT note above
  - Target: ≤ 400 lines after pointer-ification (from 769)
    Hard constraint: must stay below GC-023 active_markdown hard limit of 1200L

- Produce one completion review under `docs/reviews/`

### Forbidden scope

- Creating new canonical owner files — pointer targets must already exist
- Editing any file other than `docs/CVF_CORE_KNOWLEDGE_BASE.md` and the
  completion review
- Removing or paraphrasing Sections XI, XII, or XIV Extension Rules content
- Changing governance semantics, runtime contracts, policy definitions
- Touching tests, source code, dependencies, lockfiles, public-sync, `.git/`
- Making public/hosted/production readiness claims

Risk ceiling: R1 documentation restructure only.

---

## Required First Reads

| Required read | Reason | Status |
| --- | --- | --- |
| `docs/CVF_CORE_KNOWLEDGE_BASE.md` | Target file — full read required before edit | READ (769 lines, all 19 sections confirmed) |
| `docs/audits/CVF_EXTERNAL_REVIEW_GAP_ANALYSIS_AND_PROPOSED_SOLUTIONS_2026-06-05.md` | Source gap packet, GAP 1 | READ |
| `docs/reference/CVF_MODULE_INVENTORY.md` | Pointer target for Section III — must confirm path exists | SOURCE_VERIFY BEFORE EDIT |
| `docs/reference/CVF_GOVERNANCE_CONTROL_MATRIX.md` | Pointer target for Section VII | SOURCE_VERIFY BEFORE EDIT |
| `docs/reference/CVF_QUALITY_ASSESSMENT_STANDARD.md` | Pointer target for Section XV | SOURCE_VERIFY BEFORE EDIT |
| `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/README.md` | Source of truth for skill count | READ (62 active skills, line 16) |

**Pre-edit verification rule:** Before replacing any section with a pointer,
Claude must confirm the pointer target file exists at the stated path. If a
target file does not exist, do NOT delete the section — keep it and flag it in
the completion review as "pointer target missing, section retained."

---

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Disposition |
| --- | --- | --- | --- | --- | --- |
| Core KB is 769 lines at HEAD d6bc3553 | LINE_COUNT | `docs/CVF_CORE_KNOWLEDGE_BASE.md` | full file | 769 lines | ACCEPT |
| Core KB has 19 sections (I–XIX) | EXISTS | `docs/CVF_CORE_KNOWLEDGE_BASE.md` | section headings | I through XIX | ACCEPT |
| Skill count in Section II Layer 1 box line ~145 | VALUE_SET | `docs/CVF_CORE_KNOWLEDGE_BASE.md` | line 145 | `131 active skills, 12 domains` | STALE — must be updated to 62 |
| Skill count in Section VIII line ~411 | VALUE_SET | `docs/CVF_CORE_KNOWLEDGE_BASE.md` | line 411 | `131 active skills` | STALE — must be updated to 62 |
| Skill count source of truth | VALUE_SET | `EXTENSIONS/CVF_v1.5.2_SKILL_LIBRARY_FOR_END_USERS/README.md` | line 16 | `62 active skills` | ACCEPT |
| GC-023 active_markdown hard limit | LINE_COUNT | `governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md` | lines 88–97 | `> 1200` lines hard threshold | ACCEPT |
| Section XI (immutable principles) must be kept verbatim | LITERAL_INVARIANT | `docs/CVF_CORE_KNOWLEDGE_BASE.md` | lines 535–551 | `## XI. NGUYÊN TẮC BẤT BIẾN` | ACCEPT — do not alter |
| Section XII (architecture checklist) must be kept verbatim | LITERAL_INVARIANT | `docs/CVF_CORE_KNOWLEDGE_BASE.md` | lines 553–586 | `## XII. CHECKLIST ĐỊNH VỊ EXTENSION MỚI` | ACCEPT — do not alter |
| Section XIV Extension Rules (Rule 1–4) must be kept verbatim except Rule 4 text update | LITERAL_INVARIANT | `docs/CVF_CORE_KNOWLEDGE_BASE.md` | lines 691–805 | `## XIV. CVF EXTENSION RULES` | ACCEPT — only Rule 4 body text may be adjusted |

---

## Execution Instructions For Claude

1. Capture `executionBaseHead` before editing.
2. Read `docs/CVF_CORE_KNOWLEDGE_BASE.md` in full (already done in overlap map;
   refresh line numbers if file changed since HEAD d6bc3553).
3. For each pointer target in the Overlap Map, run `Test-Path` or equivalent
   to confirm the file exists. Log result per row.
4. For each "REPLACE WITH POINTER" section where target exists:
   - Replace the section body with a single pointer line
   - Format: `→ See [Title](path) — one-sentence description of what's there`
5. For sections where target does NOT exist: retain section verbatim, flag in
   completion review.
6. Fix skill count in Section II (Layer 1 box) and Section VIII: `131` → `62`.
7. Update Section XIV Rule 4 body text to reference `CVF_MODULE_INVENTORY.md`
   instead of Section III for version history updates.
8. Verify final line count is below 1200 (GC-023 hard limit).
9. Run governance gates listed below.
10. Return completion review without committing.

---

## Execution Plan

| Step | Action | Owner | Evidence |
| --- | --- | --- | --- |
| 1 | Capture executionBaseHead | Claude | recorded in completion review |
| 2 | Verify all pointer target paths exist | Claude | per-row Test-Path log in completion review |
| 3 | Replace pointer sections (targets confirmed) | Claude | git diff |
| 4 | Retain sections with missing pointer targets, flag | Claude | flagged list in completion review |
| 5 | Fix stale skill counts (Sections II and VIII) | Claude | grep negative check |
| 6 | Update Rule 4 text in Section XIV | Claude | diff of that paragraph |
| 7 | Verify final line count ≤ 1200 | Claude | line count in completion review |
| 8 | Run governance gates | Claude | command output |
| 9 | Write completion review | Claude | `docs/reviews/` artifact |
| 10 | Return without committing | Claude | WORKER_MUST_NOT_COMMIT respected |

---

## Evidence Requirements

Minimum before returning completion:

```powershell
# Line count check
(Get-Content docs/CVF_CORE_KNOWLEDGE_BASE.md | Measure-Object -Line).Lines

# Stale skill count negative check
rg -n "131 active skills" docs/CVF_CORE_KNOWLEDGE_BASE.md

# Governance gates
python governance/compat/check_markdown_structural_completeness.py --base <executionBaseHead> --head HEAD --enforce
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <executionBaseHead> --head HEAD
```

---

## Review Gate

Reviewer must confirm:

- Sections XI, XII, XIV Extension Rules are verbatim-unchanged;
- all pointer rows lead to files that exist and are correctly described;
- stale skill counts are gone from Sections II and VIII;
- Rule 4 body text correctly reflects new pointer structure;
- no governance semantics or canonical rules were removed;
- final line count is below 1200;
- governance gates passed;
- public export disposition is `DEFERRED_PRIVATE_ONLY`.

---

## Acceptance Criteria

| Criterion | Evidence |
| --- | --- |
| Final line count ≤ 400 (target) and < 1200 (hard limit) | `wc -l` or PowerShell count in completion review |
| No `131 active skills` remains in Core KB | `rg "131 active skills" docs/CVF_CORE_KNOWLEDGE_BASE.md` → no output |
| Sections XI, XII, XIV Extension Rules unchanged | reviewer diff check |
| All pointer rows are verified-existing paths | per-row Test-Path log |
| Governance gates pass | command output in completion review |

---

## Fail Conditions

Return to reviewer if:

- Any pointer target does not exist and retaining the full section would keep
  the file above 600 lines — escalate for operator decision on whether to create
  the missing target or keep the section
- Any gate fails outside allowed scope
- Editing Sections XI/XII/XIV Extension Rules body would be required to stay
  within line limit — do not compress these sections; escalate instead
- The file cannot reach below 1200 lines without touching forbidden content

---

## Closure Checklist

| Item | Required evidence |
| --- | --- |
| Changed files listed | `git diff --name-status <executionBaseHead> HEAD` |
| Pointer target verification log | per-row Test-Path results in completion review |
| Stale skill count removed | grep negative evidence |
| Governance gates run | command output |
| Line count confirmed | final count in completion review |
| WORKER_MUST_NOT_COMMIT | no commit by worker |

---

## Return-To-Orchestrator Conditions

| Return condition | Meaning |
| --- | --- |
| `IMPLEMENTATION_COMPLETE_PENDING_REVIEW` | Pointer-ification done, evidence supplied, no commit |
| `BLOCKED_MISSING_POINTER_TARGET` | One or more pointer targets do not exist; full section retained; operator decision needed |
| `BLOCKED_LINE_LIMIT_WITHOUT_COMPRESSION` | Cannot reach target line count without touching protected sections |
| `BLOCKED_SCOPE_EXPANSION_REQUIRED` | Fix requires changes outside allowed scope |

---

## Public Export Disposition

Disposition: `DEFERRED_PRIVATE_ONLY`

Reason: internal documentation restructure. Not authorized for public-sync
as a standalone batch.

## Claim Boundary

This work order authorizes only: replacing redundant sections in
`docs/CVF_CORE_KNOWLEDGE_BASE.md` with verified pointer rows, fixing two stale
skill count values, and updating one Rule 4 sentence. It does not authorize
new canonical owner files, governance-rule changes, runtime changes, or
public-sync.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_GAP1_CORE_KB_POINTER_IFICATION_COMPLETION_2026-06-06.md` | completion review created | PASS |
| Roadmap state | `docs/audits/CVF_EXTERNAL_REVIEW_GAP_ANALYSIS_AND_PROPOSED_SOLUTIONS_2026-06-05.md` | GAP1 work order created and closed in this batch | PASS |
| Registry JSON | `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` | registry checker passed; registry unchanged for Core KB pointerification | PASS |
| Registry Markdown | N/A | no markdown registry surface is required for Core KB pointerification | PASS |
| External evidence digest | N/A | source gap packet is already cited; no external evidence digest changed | N/A with reason |
| System loop interlock | `docs/reference/CVF_SYSTEM_LOOP_INTERLOCK_REGISTRY_2026-06-02.json` | checker passed during pre-closure rerun | PASS |
| Session continuity | active handoff/state after material commit | to be updated in a dedicated session-sync commit after material commit | PASS |
