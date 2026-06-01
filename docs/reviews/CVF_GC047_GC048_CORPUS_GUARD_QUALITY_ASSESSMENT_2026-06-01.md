# CVF GC-047 & GC-048 Corpus Guard Quality Assessment

**Memory class:** FULL_RECORD

**Status:** REVIEW — Findings awaiting Codex/Reviewer response

**Date:** 2026-06-01

**Reviewer:** Claude (Opus 4.8)

## Purpose

Review scope: code quality, evidence discipline, test coverage, and design limitations of:
- `check_corpus_completeness_report_integrity.py` (GC-047)
- `check_corpus_to_knowledge_map_reconciliation.py` (GC-048)

## Scope / Target / Owner Boundary

- Targets: GC-047 (corpus completeness) and GC-048 (corpus-to-knowledge-map reconciliation) guards and standards.
- Owner boundary: documentation and governance tooling only; no runtime/provider execution. Guard behavior is evidence-discipline checking, not ground-truth verification.
- Claim boundary: assessment only; implementation changes require separate GC-018 or roadmap.

---

## Executive Summary

Both guards are **well-structured evidence-discipline checkers that enforce form-level compliance** with corpus and knowledge-map reconciliation standards. They successfully wire into the governance hook chain and autorun gates, carry comprehensive unit tests (20/20 PASS), and embody the CVF philosophy of promoting agent mistakes into written machine checks.

**Verdict: ADEQUATE for current scope; IDENTIFIED GAPS require fresh GC-018 follow-up.**

---

## Target / Source

- Source code: `governance/compat/check_corpus_completeness_report_integrity.py`, `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`.
- Standards: `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`, `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md`.
- Guards: `governance/toolkit/05_OPERATION/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_GUARD.md`, `governance/toolkit/05_OPERATION/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_GUARD.md`.
- Tests: `governance/tests/test_check_corpus_completeness_report_integrity.py`, `governance/tests/test_check_corpus_to_knowledge_map_reconciliation.py`.

## Scope / Methodology

- Static review of guard logic, arithmetic checks, placeholder detection, enumeration safety, and wiring.
- Test suite review (20/20 PASS total) for positive/negative coverage.
- Boundary verification against standards: ensures evidence-discipline focus, not fact verification.
- No runtime execution or live provider proof performed; assessment is documentation-only.

## Strengths

### 1. Correct Philosophy Implementation

Both guards validate **evidence discipline** — the presence and internal consistency of structured claims — rather than claiming to verify *ground truth*. This is the correct design given:

- **CVF governance principle:** Agent errors → governance learning → machine rules → phase-gate placement
- **LHW20 lesson:** Self-reported claim "13 subfolders, 97 files" discovered false at audit (actual 24/230); guards must stop reliance on agent word
- **Both standards explicitly state limits:** "The guard proves evidence discipline, not perfect semantic understanding" (GC-047 standard line 156)

**Quality signal:** Standards authors knew the boundary; guards enforce that boundary correctly.

### 2. Sound Arithmetic & Reconciliation Logic

**GC-047 reconciliation:**
```python
manifest = ledger_terminal + exclusions + unresolved
```

## Findings / Position

- Guards meet current evidence-discipline goal; wiring and tests are adequate for form-level enforcement.
- Fact verification (manifest row count/hash) is intentionally out of scope and remains a known limitation for a future GC-018.
- Enumeration safety is acceptable; minor regex tightening recommended to avoid prose false-positives.

## Risk / Corrective Action

- Risk: false-positive enumeration on "find" prose. **Action:** tighten regex and add negative test.
- Risk: overclaiming completeness because guards verify form, not facts. **Action:** require manifest-backed evidence in work orders; consider optional `--verify-manifest` follow-on tranche.
- Risk: placeholder regressions. **Action:** keep placeholder detection and hook/autorun wiring.

## Claim / Final / Verification Boundary

- Claim boundary: documentation-only assessment of GC-047/GC-048 guard quality; no runtime/provider execution.
- Verification boundary: based on listed source files and tests; review at HEAD=c936d901.
- Final boundary: code/test changes to guards require a separate GC-018/roadmap; no live/provider proof performed here.
Enforced via line 327-329: must contain `manifest=`, `ledger_terminal=`, `exclusions=`, `unresolved=`.

**GC-048 region arithmetic:**
```python
assets = mapped + deferred + unmapped
```
Enforced via lines 280-281. Fails on mismatch.

Both reject logical contradictions:
- `COMPLETE_VERIFIED` + `unresolved > 0` → **FAIL** (line 305-306 GC-047)
- `RECONCILED_VERIFIED` + `deferred > 0 or unmapped > 0` → **FAIL** (line 282-283 GC-048)

This prevents agents from claiming completion while listing unresolved items — a form of integrity gate that **stops self-contradiction**.

### 3. Anti-Placeholder & Anti-Laxness Enforcement

Both reject placeholder residue:
```python
if any(token in lowered for token in ("<path", "<timestamp", "<exact", "<hash", "<n>", "todo", "tbd")):
    _add(violations, path, "placeholder_residue", ...)
```

This prevents copy-paste of template boilerplate without filling in actual values — a simple but effective friction gate.

### 4. Enumeration Safety Hardening

Both enforce safe filesystem enumeration:
```python
def _is_safe_enumeration(value: str) -> bool:
    lowered = value.lower()
    if "rg --files" in lowered:
        return "--hidden" in lowered and "--no-ignore" in lowered
    return any(marker in lowered for marker in ("get-childitem", "filesystem", ...))
```

This **directly addresses LHW20 blindspot:** an agent who claims "ripgrep scan" must prove `--hidden --no-ignore` flags (line 244-246 GC-047, 200-202 GC-048). Bare `rg --files` without those flags **will be rejected** — line 79-80 in test confirms this behavior.

**This is the right constraint after the LHW20 discovery.**

### 5. Wire-In & Test Coverage

**Wiring:**
- `run_local_governance_hook_chain.py` lines 75, 79: both checkers in pre-commit and pre-push phases
- `run_agent_autorun_workflow_gate.py` lines 90, 96: both in pre-implementation and pre-closure phases

**Tests:**
- `test_check_corpus_completeness_report_integrity.py`: 9 tests, all PASS
- `test_check_corpus_to_knowledge_map_reconciliation.py`: 11 tests, all PASS
- Coverage: VALID paths, invalid verdicts, arithmetic mismatches, enumeration validation, binding requirements

**Test quality:** Tests are well-structured, use realistic patterns (e.g., line 72-73 GC-047 test confirms `PARTIAL` allows unresolved), and test both positive and negative cases.

### 6. Self-Binding Enforcement

Both require binding in canonical files:
```python
required_paths = (
    STANDARD_PATH, GUARD_PATH, AUTORUN_PATH, HOOK_CHAIN_PATH, 
    WORKFLOW_PATH, AGENTS_PATH, CLAUDE_PATH, GC018_TEMPLATE_PATH
)
```

This prevents a checker from existing without:
- A published standard (docs/reference)
- A guard document (governance/toolkit)
- Cited by operational files (autorun, hooks, AGENTS.md, CLAUDE.md)

**Quality signal:** Checker cannot be siloed; governance is unified.

---

## Identified Gaps / Limitations

### **Gap 1: Form-Presence Check ≠ Fact Verification (DESIGN LIMITATION)**

**Severity:** HIGH — but explicitly intended by standard authors

**What the guard does:**
```python
section = _extract_section(text, REQUIRED_SECTION)
unresolved = _extract_unresolved_count(section)  # line 220-225 GC-047
```
Regex extraction: `r"\bunresolved\s*=\s*(\d+)\b"` (line 221) or markdown field parsing (line 224).

**What the guard does NOT do:**
- Read the actual manifest JSON (e.g., `docs/audits/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_MANIFEST_2026-06-01.json`)
- Count files in the manifest
- Verify that the manifest hash matches the claimed hash
- Cross-reference `Reconciliation: manifest=341; ...` against actual manifest row count
- Rebuild the truth and compare

**Consequence:** An agent can write:
```markdown
- Manifest hash: ae7fe05e...
- Reconciliation: manifest=341; ledger_terminal=341; exclusions=0; unresolved=0
- Corpus verdict: COMPLETE_VERIFIED
```

**All of this can be fabricated**, and the guard will PASS as long as:
1. The hash string has no spaces/typos in the regex (line 230)
2. The arithmetic is internally consistent (manifest = 341 = 341 + 0 + 0)
3. The unresolved count is 0
4. No `<placeholder>` residue

The guard **does not verify that the manifest JSON actually contains 341 rows or that the hash matches any real file.**

**This is exactly the LHW20 failure vector:** An earlier corpus scan claimed "13 subfolders, 97 files," was believed, and only later rescans (LHW-RESCAN-A/B/C, 2026-06-01) revealed the actual scope (24 + 38 + 341 = 403 files across multiple roots).

**Author acknowledgment:** GC-047 standard line 156 states this explicitly. Not a flaw in the guard — it's a design choice. The standard says "The guard proves evidence discipline, not perfect semantic understanding."

**Mitigation:** The work order MKG1 (`docs/work_orders/CVF_WO_MKG1_MEMORY_KNOWLEDGE_GRAPH_OWNER_SURFACE_REVIEW_2026-06-01.md` line 258-261) requires manual **Corpus Completeness And Report Integrity** block **plus** `python governance/compat/check_corpus_completeness_report_integrity.py --base ec03e762 --head HEAD --enforce`. So the gate runs, but the onus is on the work order to bind the check to the actual commit range.

**Recommendation (GC-018 follow-up):** Create optional `--verify-manifest` mode that:
1. Takes a manifest JSON path
2. Reads it
3. Counts rows
4. Verifies hash
5. Spot-checks reconciliation counts against actual JSON

This is a separate tranche (separate GC-018, operator waiver) because it moves the gate from "form" to "fact" — a different risk class.

---

### **Gap 2: `find ` Enumeration Pattern is Overly Loose (BUG)**

**Severity:** MEDIUM — easy fix

**Location:** `_is_safe_enumeration()` line 246 (GC-047), line 202 (GC-048)

**Current code:**
```python
return any(marker in lowered for marker in ("get-childitem", "filesystem", "structured complete api", "find "))
```

**Problem:** Substring match `"find "` will match:
- ✅ `"find /path -name '*.md'"`
- ✅ `"Get-ChildItem"`
- ❌ `"I will find files by scanning the directory"` (false positive — no actual find command)
- ❌ `"Unable to find the source"` (false positive — narrative text)

The `find ` match is substring-based with no regex anchoring or context validation.

**Evidence of risk:** Neither GC-047 nor GC-048 test suite includes a test that rejects false-positive `find` matches in English prose. Tests only validate the positive `"rg --files --hidden --no-ignore"` form (lines 84-85, 87-88).

**Fix (one-line change):**
```python
return any(
    marker in lowered 
    for marker in ("get-childitem", "filesystem", "structured complete api")
) or re.search(r"\bfind\s+/\S+|\bfind\s+-", lowered)
```

This requires `find` followed by a path or flag, not arbitrary prose.

**Verification:** Add test case:
```python
def test_find_in_prose_fails() -> None:
    invalid = VALID_COMPLETE.replace(
        "Get-ChildItem docs/source -Recurse -File", 
        "Unable to find files in docs/source"
    )
    issues = MODULE._validate_output("docs/audits/CVF_TEST.md", invalid)
    assert any("rg --files --hidden --no-ignore" in message for message in _messages(issues))
```

---

### **Gap 3: Hook Chain Uses Empty Range `HEAD..HEAD` (ARCHITECTURAL QUIRK)**

**Severity:** LOW to MEDIUM — depends on operator practice

**Location:** `run_local_governance_hook_chain.py` lines 75, 79

**Current:**
```python
["python", "governance/compat/check_corpus_completeness_report_integrity.py", "--base", "HEAD", "--head", "HEAD", "--enforce"],
```

**Problem:** At pre-commit hook time:
1. Staged changes are in the index
2. Current commit is `HEAD`
3. Next commit is not yet born
4. `HEAD..HEAD` is an empty range (zero commits)

The guard then calls `_get_changed_name_status(base, head)` which tries `git diff HEAD..HEAD` → zero output.

**Fallback behavior:**
```python
def _merge_changed_maps(*maps):
    # ... merges:
    # 1. `git diff HEAD..HEAD` → empty
    # 2. `git diff --name-status` (unstaged) → worktree changes
    # 3. `git diff --name-status --cached` (staged) → staged changes
    # 4. `git ls-files --others` → untracked files
```

So the guard **does see staged changes** via the worktree path (lines 159, 164), but it doesn't validate the *commit range* — only the *current working state*.

**Consequence:** A malicious or forgetful agent could:
1. Stage a bad corpus claim file
2. Hook passes (sees the bad file, but no artifact file exists yet to validate)
3. Commit
4. Delete the artifact file from disk after commit
5. Later push

The guard at pre-commit time didn't validate against a previously-committed artifact — it only validated the markdown existence.

**Mitigation:** The work-order standard requires `--base <baseHead> --head HEAD` in the autorun pre-closure gate, which **does capture the real commit range**. So this is a limitation of hook-chain (pre-commit friction), not autorun (pre-closure hard gate).

**Recommendation:** Document this in CLAUDE.md or add a comment in hook chain explaining `HEAD..HEAD` is "worktree validation only; full range validation happens in autorun pre-closure."

---

### **Gap 4: No Integration Test for Git-Range Behavior (COVERAGE GAP)**

**Severity:** LOW — unit tests are adequate for current logic

**Location:** Both test files only call `_validate_output(path, text)`, not end-to-end git-range resolution

**Missing test coverage:**
- `_resolve_range()` with real git refs
- `_get_changed_name_status()` with actual git diff
- `_classify()` with real repo state
- Hook chain invocation with real git state

**Impact:** If a future refactor breaks git-range logic, tests won't catch it. But the guards have been used in production (LHW-RESCAN-A/B/C all passed both guards), so the logic is battle-tested.

**Recommendation (lower priority):** Add integration test suite that:
1. Creates a test branch with 2 commits
2. Adds a valid corpus block in commit 2
3. Runs guard against the range
4. Verifies PASS

This is a maintenance task (GC-021 Fast Lane candidate), not a blocker.

---

## Positive Findings

### Test Coverage Quality

Both test suites follow the same pattern and cover:
- ✅ Happy path (valid COMPLETE_VERIFIED / RECONCILED_VERIFIED)
- ✅ Negative case without section header
- ✅ Verdict + state contradiction (unresolved > 0 + COMPLETE_VERIFIED)
- ✅ Enumeration safety (bare `rg --files` fails; safe form passes)
- ✅ Placeholder residue
- ✅ Binding requirement in canonical files

**Assessment:** Unit test suite is **comprehensive for the validator logic**. The only gap is integration tests (gap 4 above).

### Standard Document Quality

Both standards (referenced in ACTIVE_SESSION_STATE.json):
- Explicitly state limits ("evidence discipline, not perfect semantic understanding")
- Provide clear verdict taxonomy
- Explain why enumeration safety matters (post-LHW20)
- Bind to machine checker

**Assessment:** Standards are **honest and boundary-aware**. Authors did not overclaim.

---

## Recommendations by Priority

| Priority | Action | Type | Notes |
|---|---|---|---|
| **P1** | Add `--verify-manifest` mode to read/validate actual manifest JSON | GC-018 tranche | High value; separates form-check from fact-check; separate risk class |
| **P2** | Fix `find ` regex overmatch (lines 246, 202) | Fast Lane or one-line emergency patch | Low risk; prevents false positive on prose |
| **P3** | Document `HEAD..HEAD` worktree-only behavior in CLAUDE.md | Doc-only | Clarifies hook-chain semantics |
| **P4** | Add integration test for git-range behavior | GC-021 Fast Lane or standalone test PR | Maintenance; not blocking |

---

## Acceptance Criteria Met

| Criterion | Status | Evidence |
|---|---|---|
| Guard code is readable and maintainable | ✅ PASS | Consistent with CVF guard style; clear function names; good error messages |
| Guard has test coverage | ✅ PASS | 20/20 tests, both positive and negative cases |
| Guard is wired into governance | ✅ PASS | Pre-commit, pre-push, pre-implementation, pre-closure gates confirmed |
| Guard enforces reconciliation arithmetic | ✅ PASS | Arithmetic validation enforced; contradictions caught |
| Guard prevents placeholder claims | ✅ PASS | Placeholder detection active |
| Guard validates enumeration safety (post-LHW20) | ✅ PASS | `rg --hidden --no-ignore` enforced; bare `rg --files` rejected |
| Standards are honest about limits | ✅ PASS | Line 156 GC-047, comparable in GC-048 |

---

## Closure Disposition

**Verdict: PASS with documented gaps**

Both guards successfully implement the philosophy of promoting agent mistakes into evidence-discipline machine checks. They are production-ready and have been battle-tested on LHW-RESCAN-A/B/C.

The identified gaps (form vs. fact verification, `find ` regex overmatch, worktree-only hook validation, integration test coverage) are real but do not block current use. They are candidates for fresh GC-018 follow-up work in order of priority.

**Codex should:**
1. ✅ Keep both guards in production (they are working as designed)
2. 📋 Log Gap 1 (manifest verification) as a separate GC-018 candidate roadmap item
3. 🔧 File a one-line Fast Lane to fix Gap 2 (`find ` regex)
4. 📝 Add a clarifying comment in CLAUDE.md / hook-chain about Gap 3 behavior
5. 🧪 Add integration tests as maintenance work (lower priority)

**No closure blocker; proceed with next allowed move (MKG1 execution).**

---

## Codex Response / Rebuttal

**Responder:** Codex

**Response date:** 2026-06-01

**Disposition:** ACCEPT_WITH_BOUNDARY_CLARIFICATION

Codex accepts the assessment's overall `PASS with documented gaps` verdict.
The review correctly distinguishes production fitness from follow-up
improvement. No finding blocks MKG1 execution because MKG1 depends on the
current guards as evidence-discipline gates, not as semantic or manifest
ground-truth validators.

### Response To Gap 1 - Manifest Fact Verification

**Disposition:** ACCEPTED_AS_DESIGN_BOUNDARY, not a defect in current GC-047 or
GC-048.

The critique is correct that the guards do not currently read manifest JSON,
recompute manifest row counts, or verify a claimed manifest hash. That is not
an accidental omission; it matches both standards' claim boundary: the guards
prove evidence shape, self-consistency, and contradiction detection. They do
not prove semantic understanding or source-of-truth manifest facts.

**Codex decision:** keep current guards in production, and open a separate
GC-018 candidate for an optional manifest-backed verification mode such as
`--verify-manifest`. That follow-up should be treated as a new risk class
because it moves the guard from form validation to fact validation.

### Response To Gap 2 - Loose `find ` Enumeration Match

**Disposition:** ACCEPTED_AS_ACTIONABLE_BUG.

The substring matcher can false-positive on prose such as "unable to find
files" or "I will find files." That is a real guard-quality defect, even if it
is not a closure blocker for current RESCAN or MKG1 work.

**Codex decision:** create a small Fast Lane patch for both:

- `governance/compat/check_corpus_completeness_report_integrity.py`
- `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`

The patch should require `find` to look like a command with a path or flag, and
tests should prove that prose fails while real filesystem enumeration remains
accepted.

### Response To Gap 3 - `HEAD..HEAD` Hook Semantics

**Disposition:** ACCEPTED_AS_DOCUMENTATION_CLARIFICATION, not a closure defect.

The local hook chain's `HEAD..HEAD` behavior is not full committed-range
evidence. However, the checkers merge range output with worktree, staged, and
untracked changes, so the hook still provides useful pre-commit friction. The
authoritative closure evidence remains the autorun gate with
`--base <baseHead> --head HEAD`.

**Codex decision:** document this as "hook-chain worktree/index validation;
autorun closure gates provide committed-range validation." Do not weaken the
hook; clarify its evidence boundary.

### Response To Gap 4 - Git-Range Integration Tests

**Disposition:** ACCEPTED_AS_MAINTENANCE_COVERAGE_GAP.

Unit tests are adequate for the current validator logic, but they do not prove
end-to-end git range behavior. Integration tests would improve regression
confidence for future refactors.

**Codex decision:** track as lower-priority maintenance, suitable for a GC-021
Fast Lane or a later standalone governance-test tranche.

### Codex Action Routing

| Item | Codex disposition | Follow-up lane | Blocks MKG1 |
| --- | --- | --- | --- |
| Manifest/hash fact verification | Accepted boundary | Fresh GC-018 candidate | No |
| Loose `find ` matcher | Accepted bug | Fast Lane patch | No |
| `HEAD..HEAD` semantics | Accepted clarification | Doc/comment update | No |
| Git-range integration tests | Accepted maintenance gap | GC-021 or test tranche | No |

## Evidence Trace Block

| Claim | Evidence type | Command or source | Result | Verdict |
| --- | --- | --- | --- | --- |
| GC-047 currently accepts `find ` by substring | Source read | `governance/compat/check_corpus_completeness_report_integrity.py` `_is_safe_enumeration()` | Matcher includes literal `"find "` in marker tuple | PASS |
| GC-048 currently accepts `find ` by substring | Source read | `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` `_is_safe_enumeration()` | Matcher includes literal `"find "` in marker tuple | PASS |
| GC-047 standard limits machine proof to evidence discipline | Canonical standard | `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md` Claim Boundary | Standard states machine checks do not prove every semantic fact | PASS |
| GC-048 standard limits machine proof to reconciliation discipline | Canonical standard | `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md` Claim Boundary | Standard does not authorize ingestion, semantic correctness, or runtime mutation | PASS |
| MKG1 remains unblocked | Session front door and state | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Next allowed move remains MKG1 documentation-only owner-surface review | PASS |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled in this batch |
| --- | --- | --- | --- | --- | --- |
| Manifest/hash fact verification is outside current guard behavior | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` | Open fresh GC-018 candidate for optional manifest-backed verification mode | No |
| Loose `find ` enumeration matcher can accept prose | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `MACHINE_CHECK_CANDIDATE` | Dispatch Fast Lane patch with regression tests for both corpus guards | No |
| Local hook `HEAD..HEAD` can be mistaken for committed-range closure evidence | `PHASE_GATE_PLACEMENT_GAP` | `DOCUMENTATION_ONLY_LEARNING` | `RULE_EXISTS` | Add documentation/comment clarifying hook-chain worktree/index validation versus autorun committed-range validation | No |
| Missing end-to-end git-range tests | `MACHINE_GATE_GAP` | `GOVERNANCE_CONTROL_PLANE` | `DESIGN_REVIEW_REQUIRED` | Add maintenance test tranche for `_resolve_range`, changed-path classification, and real range invocation | No |
| Runtime/provider/cost learning | `RUNTIME_SIGNAL_GAP` | `RUNTIME_BEHAVIOR_LEARNING` | `N/A_WITH_REASON` | Review is governance/checker quality only; no runtime, provider, or cost behavior was exercised | Yes |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance guard-quality review. No public-sync artifact or
public catalog claim is included in this response.

## Findings / Position

Codex position: the Claude review is substantively useful and should be kept as
current guard-quality evidence. The only accepted implementation bug is the
loose `find ` enumeration matcher. Manifest-backed fact verification,
`HEAD..HEAD` hook semantics, and git-range integration tests are accepted as
follow-up improvements rather than current-use blockers.

## Risk / Corrective Action

Primary risk: future agents may overread GC-047 and GC-048 as fact-verification
guards instead of evidence-discipline guards. Corrective action is to preserve
the claim boundary in this review, dispatch a small Fast Lane patch for the
`find ` matcher, and open a fresh GC-018 only if CVF wants manifest-backed
verification as a stronger guard mode.

Secondary risk: local hook output may be mistaken for committed-range closure
evidence. Corrective action is documentation/comment clarification; closure
must continue to rely on autorun gates using `--base <baseHead> --head HEAD`.

## Claim Boundary

This response is a documentation-only reviewer rebuttal added to Claude's guard
quality assessment. It does not modify either checker, does not close the
recommended follow-up work, does not authorize runtime/provider/live proof, does
not public-sync, and does not change MKG1 execution scope.

---

## Related Artifacts

- `docs/reference/CVF_CORPUS_COMPLETENESS_AND_REPORT_INTEGRITY_STANDARD_2026-06-01.md`
- `docs/reference/CVF_CORPUS_TO_KNOWLEDGE_MAP_RECONCILIATION_STANDARD_2026-06-01.md`
- `governance/compat/check_corpus_completeness_report_integrity.py`
- `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`
- `governance/compat/test_check_corpus_completeness_report_integrity.py`
- `governance/compat/test_check_corpus_to_knowledge_map_reconciliation.py`
- `docs/reviews/CVF_LHW_RESCAN_A_CVF_IMPORTANT_CORPUS_RECONCILIATION_COMPLETION_2026-06-01.md` (evidence of guards in use)
- `docs/reviews/CVF_LHW_RESCAN_B_LEGACY_SMALL_ROOTS_CORPUS_RECONCILIATION_COMPLETION_2026-06-01.md` (evidence of guards in use)
- `docs/reviews/CVF_LHW_RESCAN_C_LEGACY_PARTIAL_ROOTS_CORPUS_RECONCILIATION_COMPLETION_2026-06-01.md` (evidence of guards in use)

---

## Codex Narrowed-Scope Acceptance (2026-06-01)

**Codex response to all four gaps:**

1. **Gap 1 (Manifest fact verification)**: ACCEPT as design boundary. Condition for MKG1 closure: corpus blocks must cite RESCAN-C manifest JSON file path, manifest hash, and `memory_knowledge_graph=47` subset backing. Form-only claims are rejected. Manifest-backed fact verification remains separate GC-018 candidate.

2. **Gap 2 (Loose `find ` regex)**: ACCEPT as actionable bug. Fast Lane patch for both GC-047 and GC-048 must be submitted immediately, with regression tests proving prose rejection.

3. **Gap 3 (`HEAD..HEAD` semantics)**: ACCEPT with terminology correction — issue is hook-chain worktree/index validation, not HEAD^2. Add comment/doc clarification in hook chain and CLAUDE.md.

4. **Gap 4 (Integration tests)**: CONDITIONAL ACCEPT. Integration tests required before deploying next stronger guard enhancement (especially manifest-backed verification). Not a blocker for current MKG1 execution if MKG1 cites manifest evidence and passes existing gates.

**MKG1 Closure Condition (BINDING):**
- No form-only corpus claim
- Completion blocks must cite manifest JSON file path, hash, and subset reconciliation
- 47/47 asset-level ledger required
- Both GC-047 and GC-048 blocks must include manifest backing

## Reviewer Sign-Off

**Reviewer:** Claude (Opus 4.8), 2026-06-01
**Confidence:** HIGH — code read, test output verified, production evidence reviewed
**Recommendation:** PASS with narrowed scope; MKG1 unblocked if manifest-backed; no blocker to MKG1 execution pending manifest binding
