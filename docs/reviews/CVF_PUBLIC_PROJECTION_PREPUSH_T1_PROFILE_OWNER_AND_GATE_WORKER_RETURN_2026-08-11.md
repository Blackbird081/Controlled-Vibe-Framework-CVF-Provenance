# CVF Public Projection Pre-Push T1 Profile Owner And Gate Worker Return

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

docType: review

Self-declared worker-return artifact: yes

Responds to work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_AMENDMENT_2_2026-08-12.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_AMENDMENT_2_2026-08-12.md`

Batch ID: PUBLIC-PROJECTION-PREPUSH-T1-AMENDMENT-2

executionBaseHead: `6d403d72d531d500cf424d71920b4c14c5d9b377`

closureBaseHead: same as executionBaseHead (worker did not commit)

Commit mode: WORKER_MUST_NOT_COMMIT

## Amendment 1 Continuation Record

This return is a continuation of the same Amendment 1 worker turn, not a
fresh dispatch, per orchestrator disposition `BLOCKER_REJECTED_AS_PREMATURE`
/ `CONTINUE_SAME_AMENDMENT_1`. The prior version of this file recorded
`BLOCKED_WITH_REASON` / `BLOCKED_CONTRACT_CONTRADICTION` for
`external_command:cvf_web_next_build`, plus a dependency-isolation design
(`_isolate_dependencies` junctioning third-party entries directly from the
real public root's installed `node_modules`) that did not conform to
Amendment 1 AC-03. Both are corrected below.

**Retraction of the prior return's premature conclusions**, per the
orchestrator's rejection findings:

- Retracted: the claim that resolving `next build --webpack` required
  editing the public candidate's `next.config.ts`. It did not. The actual
  defect was that `_isolate_dependencies` never gave `next` a genuinely
  junction-free path inside the sandbox; a full physical copy of `next`
  directly into the sandbox's own `node_modules` (no junction anywhere in
  its path) resolves the failure entirely inside this worker's existing
  five-path authority.
- Retracted: the claim that a full-copy isolation strategy "requires a
  separately authorized decision." Amendment 1 already authorizes
  junctions/symlinks/copies sourced from existing local dependency stores;
  disk cost from a full copy is not a contract contradiction requiring new
  authority.
- Retracted: the classification of the `next build` failure as a fresh
  `BLOCKED_CONTRACT_CONTRADICTION`. It was a dependency-isolation
  implementation gap, not an irreconcilable command requirement. Corrected
  disposition below: `PREMATURE_BLOCKER` /
  `DEPENDENCY_ISOLATION_IMPLEMENTATION_GAP`.
- Disclosed: the prior return's `_isolate_dependencies` design did not
  conform to Amendment 1 AC-03 even though no public mutation was ever
  observed. AC-03 requires real repositories (public root and Core) to be
  read-only copy sources only, never live dependency-link targets. The
  prior design junctioned/hard-linked every third-party `node_modules`
  entry directly from the real public root's installed store, and its
  `_assert_inside` check verified only the link's own placement inside the
  sandbox, never the link's resolved target - so a link whose target
  resolved into the real public root would have passed that check
  undetected. No such escape was ever exercised by any command this
  profile actually ran (every command's I/O stayed inside the sandbox,
  confirmed by `public_root_invariant_check` PASS on every run), but the
  isolation design itself was contract-nonconforming, independent of
  whether a mutation ever occurred in practice.

## Amendment 2 Continuation Record

This return is further amended in place for
PUBLIC-PROJECTION-PREPUSH-T1-AMENDMENT-2, a maintainability-only structural
refactor. Amendment 1 was `FUNCTIONALLY_ACCEPTED` (independent reviewer
reproduction: 58/58 tests, real-candidate sandboxed run exit 0,
`compliant: true`, zero gate failures, exact evidence reconciliation, public
clone unchanged) but `CLOSURE_REJECTED_SIZE_GUARD`:
`run_public_projection_pre_push_gate.py` at 1380 lines exceeded the
`python_cli_orchestrator` hard threshold of 800 lines, and
`test_run_public_projection_pre_push_gate.py` at 1279 lines exceeded the
`python_test` hard threshold of 1200 lines, both under
`governance/compat/check_python_automation_size.py` - a gate entirely
separate from this profile's own `governed_python_automation_size`
inherited-debt family (which pins an unrelated file).

Amendment 2 authorizes structural extraction only, not semantic reopening:
cohesive non-CLI implementation (sandbox lifecycle, dependency-isolation
utilities, the four inherited-debt family checkers, command-output
evidence extraction) was relocated - disposition NOT_LITERAL_WITH_REASON:
verbatim in logic, not a byte-identical file move, since module location
and import statements changed - into a new library helper,
`governance/compat/public_projection_pre_push_gate_lib.py`, with zero
change to any validation, fail-closed condition, or evidence-reconciliation
behavior.

**Repair record (orchestrator `REVIEW_REJECTED_REPAIR_REQUIRED`, blocking
finding: an out-of-manifest test-sibling file).** An earlier pass of this
Amendment 2 work created a second new test file,
`governance/compat/test_public_projection_pre_push_gate_lib.py`, outside
the committed exact-seven Amendment 2 manifest, to bring the existing test
file under its own size threshold. The orchestrator rejected this and
required either removing that path while preserving coverage inside the
authorized seven paths, or returning `BLOCKED_WITH_REASON` for a fresh
narrower authorization. Route 1 was chosen: the sibling file's content was
merged back into `test_run_public_projection_pre_push_gate.py` (no test
deleted, only relocated back), and non-load-bearing docstring prose was
tightened - not test logic, fixtures, or assertions - to bring the single
merged file to 1191 physical lines, under the 1200-line hard threshold.
`governance/compat/test_public_projection_pre_push_gate_lib.py` no longer
exists. The seeded exception-registry entry for the test file was
re-ratcheted from the earlier (incorrect) 570 down-then-up to 1191, which
remains a strictly downward ratchet relative to the committed baseline's
seeded 1279 - `_is_authorized_ratchet_down` compares against the committed
`HEAD` baseline, not against any of this worker's own intermediate values.
Every other manifest claim in this file that referenced the sibling file
or its now-superseded line counts is corrected below.

## Purpose

Implement the disposable-sandbox strategy authorized by Amendment 1 inside
the exact same five T1 worker-owned paths, resolving the read-only-vs-build
conflict by relocating mutating package execution rather than weakening any
required command, and record truthful updated evidence in this same worker
return. Amendment 2 extends this purpose with a structural-only refactor
that preserves every behavioral invariant Amendment 1 proved, satisfying
the closure-hook governed Python automation size guard.

## Target / Source

Target (worker-owned, exact seven paths under Amendment 2 - six inherited
paths from Amendment 1's five plus one new library helper, plus the
size-exception registry):

- `docs/reference/CVF_PUBLIC_PROJECTION_PRE_PUSH_PROFILE_STANDARD_2026-08-11.md`
- `governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json`
- `governance/compat/run_public_projection_pre_push_gate.py`
- `governance/compat/public_projection_pre_push_gate_lib.py` (new this
  amendment)
- `governance/compat/test_run_public_projection_pre_push_gate.py`
- this worker return
- `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`

Exactly these seven paths, and no other, exist in this pass's final state.
No sibling test file exists; the earlier pass's out-of-manifest
`test_public_projection_pre_push_gate_lib.py` was removed and its content
merged back into `test_run_public_projection_pre_push_gate.py` per the
repair described in the Amendment 2 Continuation Record above.

Source: the committed Amendment 1 work order, GC-018 baseline, and source
verification (SHA-256 `674d3cbb28...`, `df3a61f192...`, `1cd6bb1fb3...`
respectively); the committed Amendment 2 work order, GC-018 baseline, and
source verification (authority commit
`8bbbd86226880ab952932d9b1aca8ddab20d310c`); this file's own prior version
as the Amendment 2 preimage (matched exactly at the Amendment 2 preflight
check before any edit in this pass); direct execution of the pinned public
candidate's package.json scripts, generator scripts, and the real
ESLint/vitest/Next.js toolchain inside the disposable sandbox, reproduced
against the post-refactor code.

## Scope / Methodology (This Continuation Pass)

1. Verified the continuation checkpoint in full before any edit: Core
   `HEAD` exactly `ddd54cbebb550af83db6ac8dbb7d96f5795768aa`; exact five-path
   dirty set; all five pinned SHA-256 preimages matched exactly against the
   continuation dispatch; staged content zero; public clone clean at
   `021f8b852afc245a6383177dd69bf56caf488b02` on `lpci1-ref-staging`.
2. Repaired `_isolate_dependencies` (R-02): removed every live dependency
   link whose source was the real public root or Core directly. Every
   third-party `node_modules` entry is now first physically copied
   (`_copy_dependency_entry`, `shutil.copytree`/`shutil.copy2`) from the
   real public root's installed store into a dedicated
   `dependency-store` subtree of the sandbox's own disposable temporary
   support directory, and only then linked (junction for a directory, hard
   link with copy fallback for a file) from that support-owned copy into
   the sandbox - never linked directly from either real repository. Added
   `_assert_target_inside` calls (resolved-target boundary, not just
   link-placement boundary) on every dependency link, branched correctly
   for directory-vs-file link types (a junction's resolved target is the
   support-store copy; a hard-linked file's resolved path is its own
   on-disk location, already inside the sandbox).
3. Implemented `next` as a documented full-copy exception
   (`FULL_COPY_DEPENDENCY_ENTRIES = frozenset({"next"})`): physically
   copied directly into the sandbox's own `node_modules` with zero
   junctions anywhere in its path, plus an independent second physical
   copy into the support store's own `node_modules` (required because
   `eslint-config-next`, itself a store-resident package, resolves
   `require("next/...")` relative to its own location in the store -
   Node's module resolution walks up from the requiring module's own path,
   so a copy that exists only in the sandbox is invisible to a package
   that itself lives in the store; discovered via the real-candidate
   `cvf_web_lint` run, see Findings).
4. Removed all `os.link()` calls that aliased real-repository files
   directly; the only remaining hard links are between two independently
   support/sandbox-owned copies, never between a sandbox path and a real
   repository path.
5. Fixed evidence-count reconciliation (R-03): `_run_external_command` now
   compares `observedEvidence` against `expectedEvidence` whenever the
   latter is configured, and returns `GATE` on any mismatch (including
   extraction failure, which now produces `None` rather than a silently
   omitted key) - a zero exit code alone is no longer sufficient evidence
   when `expectedEvidence` is configured. Also fixed the output-capture
   evidence dict to include `stdoutTail`/`stderrTail` on any non-clean-PASS
   outcome (previously only nonzero exit populated them, hiding the
   diagnostic output needed to explain an exit-0 count mismatch).
6. Fixed `_extract_observed_counts` against real tool output, found only by
   running the actual pinned candidate's real vitest/Next.js commands
   inside the sandbox (see Findings): added ANSI escape-code stripping
   before regex matching (real vitest output interleaves ANSI color codes
   between "Test Files" and the count, which a bare `\s+` pattern does not
   span); widened the static-page regex to tolerate the real Next.js 16
   "Generating static pages using N workers (X/Y)" phrasing and its
   repeated progress lines (the prior regex assumed the count immediately
   followed "static pages").
7. Raised `cvf_web_lint`'s `timeoutSeconds` from 120 to 300 in the policy,
   with an inline citation explaining why: a disposable sandbox has zero
   warm ESLint/TypeScript-parser caches on every run by design, and direct
   measurement of this exact scoped command inside the sandbox showed
   ~117s elapsed - too little margin at 120s to distinguish a real hang
   from ordinary cold-cache latency.
8. Added 12 new fail-closed and positive tests (58 total, up from 46):
   physical-copy-not-junction proof for `next`; resolved-target-stays-
   inside-sandbox proof for `next`; proof that no dependency link resolves
   into the real public root or Core specifically (not merely "outside the
   sandbox" in the abstract); proof that mutating a sandbox-copied
   dependency file never changes the real repository's own copy (no
   hard-link aliasing); proof that mutating the real repository's
   dependency store after isolation never changes the sandbox's
   independently-copied entry; a configured live-target-into-real-
   repository regression case fails closed via `_assert_target_inside`;
   dependency-copy failure and partial/silent-copy-failure both fail
   closed; expected-evidence count mismatch gates; expected-evidence
   extraction failure gates; expected-evidence exact match passes; and a
   regression test reproducing the exact real ANSI/progress-line output
   formats that broke the original regexes.
9. Ran the repaired runner against the real, read-only public candidate
   four times in this continuation pass, iteratively repairing what each
   real run surfaced that the fixture tests could not (see Findings): a
   dependency-link target-boundary bug for hard-linked file entries
   (fixed by branching the boundary assertion on directory-vs-file link
   type); the `eslint-config-next` cross-package resolution gap (fixed by
   the support-store peer copy); the ANSI/progress-line regex gaps; the
   `cvf_web_lint` cold-cache timeout margin.
10. Confirmed the real public clone's `HEAD` and full `git status --short`
    were compared before and after every real-candidate run in this
    continuation pass (disposition: MATCH every time), and confirmed no
    sandbox or support directory was left behind after any run.

## Scope / Methodology (Amendment 2 Structural Refactor)

1. Verified the Amendment 2 preflight in full before any edit: Core `HEAD`
   exactly `6d403d72d531d500cf424d71920b4c14c5d9b377` (`executionBaseHead`);
   exactly five inherited implementation paths untracked; all five SHA-256
   preimages matched the Preimage Authority Matrix exactly; staged content
   zero; `public_projection_pre_push_gate_lib.py` did not yet exist; public
   clone clean at `021f8b852afc245a6383177dd69bf56caf488b02`.
2. Ran the worker's own ADIF pre-implementation resolver query
   (`taskClass="PUBLIC-PROJECTION-PREPUSH-T1 Amendment 2 size-guard refactor
   dispatch", role=worker, lifecyclePhase=pre-implementation`) -
   `NONE_RETURNED`. Ran the pre-dispatch autorun gate - `COMPLIANT`.
3. Read the full 1380-line runner and 1279-line test file to identify
   cohesive non-CLI logic boundaries, then created
   `governance/compat/public_projection_pre_push_gate_lib.py` (753 lines)
   containing, moved (disposition NOT_LITERAL_WITH_REASON: verbatim in
   logic, module location and import statements changed):
   `GateFailClosed`/`CheckResult` (the shared types);
   `capture_public_root_invariants`/`diff_public_root_invariants`; the full
   sandbox lifecycle (`SandboxError`, `_assert_inside`,
   `_assert_target_inside`, `materialize_sandbox`,
   `verify_sandbox_materialization`, `is_junction`, `create_junction`,
   `create_link`, `copy_dependency_entry`, `isolate_dependencies`,
   `_find_sandbox_extensions_dir_for_sibling`, `teardown_sandbox`,
   `FULL_COPY_DEPENDENCY_ENTRIES`); the four inherited-debt family checkers
   (`check_governed_file_size`, `check_governed_python_automation_size`,
   `check_guard_registry_compatibility`, `check_pre_public_p3_readiness`,
   `count_lines`, `FAMILY_CHECKERS`); and command-output normalization/
   evidence extraction (`truncate`, `resolve_command_executable`,
   `ANSI_ESCAPE_RE`, `extract_observed_counts`).
4. Updated the runner (now 724 lines) to import every relocated symbol from
   the helper via the same `sys.path`-insertion-then-bare-import pattern
   `check_python_automation_size.py` already uses for `policy_baseline`
   (`COMPAT_DIR` inserted at module load, then `from
   public_projection_pre_push_gate_lib import ...`), aliasing every symbol
   back to its original private name (e.g. `materialize_sandbox as
   _materialize_sandbox`) so every call site inside `run_gate` and
   `_run_external_command` needed zero further changes. The runner retains:
   argument parsing, policy loading/top-level Git-level validation
   (`_load_policy`, `_validate_pins`, `_run_git`, `_resolve_public_root`,
   `_validate_remote`/`_validate_branch`/`_validate_clean`/`_validate_head`/
   `_validate_range_and_manifest`), `_run_external_command` (orchestration:
   builds `CheckResult`s from real subprocess execution, using the helper's
   `resolve_command_executable`/`truncate`/`extract_observed_counts` as
   pure utilities), `_validate_external_commands`, `_resolve_policy_checks`,
   `_reconcile_check_registry`, `run_gate` (full orchestration), and
   `_print_report`/`main` (output/exit-code mapping).
5. Ran the existing 58 focused tests unchanged against the new import
   layout - all 58 passed with zero test-file edits, confirming the
   extraction changed no observable behavior.
6. Found the test file, still 1279 lines (unchanged, since no test edit was
   needed), remained over its own 1200-line hard threshold. First attempted
   a split into a new sibling file
   (`test_public_projection_pre_push_gate_lib.py`); the orchestrator
   rejected this as an out-of-manifest path (see Repair record above).
7. Repair: deleted `test_public_projection_pre_push_gate_lib.py` entirely
   and merged its full content back into
   `test_run_public_projection_pre_push_gate.py` (every test restored, none
   deleted), then tightened non-load-bearing multi-line docstring prose
   across both the restored and pre-existing tests (summarizing "why" text
   to a single line per test, never touching an assertion, fixture call, or
   test body) to bring the single merged file to exactly 1191 physical
   lines - under the 1200-line hard threshold, with headroom.
8. Added the required no-circular-import test
   (`test_no_circular_import_between_runner_and_helper`, now inside the
   single authorized test file): imports the helper the same way the
   runner does (bare module name via the runner's own `sys.path`
   insertion, not the `governance.compat.` dotted path this test module
   otherwise uses), confirms the helper has no reference to
   `run_public_projection_pre_push_gate` anywhere in its own namespace, and
   confirms every relocated symbol the runner exposes really does
   originate from the helper module
   (`__module__ == "public_projection_pre_push_gate_lib"`) rather than a
   duplicate redefinition. 59 tests now pass total (58 pre-existing plus
   this one), all inside the single, authorized test file.
9. Ratcheted `approvedMaxLines` downward on both seeded exception-registry
   entries: 724 for the runner (unchanged from the first pass), and 1191
   for the test file (corrected from the first pass's incorrect 570, which
   reflected the now-deleted split, not the merged file's real size) -
   disposition MATCH: every other field on both entries (`status`,
   `rationale`, `requiredFollowup`, `seedAuthorization`, `path`,
   `fileClass`) left unchanged from the committed baseline, and both new
   caps remain strictly below the committed baseline's seeded values (1380,
   1279), satisfying `_is_authorized_ratchet_down`.
10. Ran `governance/compat/check_python_automation_size.py --enforce`:
    `COMPLIANT`, 0 violations, exit 0. The new helper (753 lines, soft-
    threshold advisory only, well under its 900 hard limit) and the single
    merged test file (1191 lines, under its 1200 hard limit) both register
    with no violation. No sibling test file exists to report on.
11. Ran the real, repaired-import, repaired-manifest runner against the
    real, read-only public candidate: `compliant: true`, zero gate
    failures, all seven external command categories PASS, with
    `observedEvidence` exactly matching Amendment 1's proof on every
    `expectedEvidence`-bearing command (Model Gateway 30 files/231 tests;
    cvf-web 15 files/218 tests; Next build 121 static pages). Confirmed the
    public clone's `HEAD` and full `git status --short` matched before and
    after, and no sandbox or support directory was left behind.

## Findings / Position

**Repaired: the out-of-manifest test-sibling file is resolved, not
disclosed-and-carried.** The prior pass of this Amendment 2 worker return
created `governance/compat/test_public_projection_pre_push_gate_lib.py`, a
path beyond the committed exact-seven manifest, to bring the existing test
file under its own 1200-line hard threshold after a split rather than an
in-place fix. The orchestrator issued `REVIEW_REJECTED_REPAIR_REQUIRED`
naming this the blocking finding and required either removing the path
while preserving coverage inside the authorized seven paths, or returning
`BLOCKED_WITH_REASON` pending a fresh, narrower authorization explicitly
adding the sibling path. Route 1 (remove and repair) was chosen: creating
an out-of-manifest path was this worker's own repair-time judgment call in
the prior pass, not a pre-existing blocker requiring new external
authority, so it is this worker's to correct without waiting on a fresh
dispatch. The sibling file's full content (every test, fixture, and
assertion, none deleted) was merged back into
`test_run_public_projection_pre_push_gate.py`, and non-load-bearing
multi-line docstring prose (the "why" explanation text, never an
assertion, fixture call, or test body) was tightened to single lines
across both the restored and several pre-existing tests, bringing the
single merged file to exactly 1191 physical lines - under the 1200-line
hard threshold. The file now exists at exactly the seven paths the work
order authorized, no more.

**D-01 through D-04 and the sandbox lifecycle mechanics (materialization,
hash verification, invariant capture, teardown) remain repaired and
unaffected by this continuation.**

**All seven proof-envelope command categories now genuinely pass inside the
disposable, copy-isolated sandbox against the real pinned public candidate.**
Against `lpci1-ref-staging@021f8b852afc245a6383177dd69bf56caf488b02`, base
`2103a38fda01ee827e9fc6c3be38a824fa5d54ad`, the final real-candidate run in
this continuation pass returned `compliant: true`, zero gate failures:

- `sandbox_materialization`: PASS.
- `external_command:model_gateway_test`: PASS, exit 0, `observedEvidence`
  `{"files": 30, "tests": 231}` - exact match to the Pinned Command
  Manifest's expected `{"files": 30, "tests": 231}`. (The prior return's
  claim that this count mismatch was "benign" is retracted; the real cause
  was the ANSI-stripping regex gap in item 6 above, now fixed and
  evidenced with an exact match, not excused.)
- `external_command:model_gateway_check`: PASS, exit 0.
- `external_command:cvf_web_check`: PASS, exit 0.
- `external_command:cvf_web_lint`: PASS, exit 0, scoped to exactly
  `src/app/api/lpci/query/route.governance.test.ts` per the pinned
  manifest.
- `external_command:cvf_web_test`: PASS, exit 0, `observedEvidence`
  `{"files": 15, "tests": 218}` - exact match to the pinned expectation.
- `external_command:cvf_web_build`: PASS, exit 0 (risk-model generator).
- `external_command:cvf_web_build_skill_index`: PASS, exit 0 (skill-index
  generator).
- `external_command:cvf_web_next_build`: PASS, exit 0, `observedEvidence`
  `{"staticPages": 121}` - exact match to the pinned expectation of 121
  static pages. This is the command the prior return's version of this
  file reported as a fresh `BLOCKED_CONTRACT_CONTRADICTION`; per the
  Retraction section above, that was a dependency-isolation implementation
  gap, corrected by giving `next` a genuinely junction-free path inside
  the sandbox, not a webpack/candidate defect requiring public-candidate
  edits.
- `public_root_invariant_check`: PASS on every run in this continuation
  pass - disposition MATCH: the real public clone's `HEAD`, branch, full
  status, and staged/unstaged diff, compared immediately before sandbox
  materialization against immediately after the last sandbox's teardown,
  every time, including the runs that ended in a `GATE`.
- `sandbox_teardown`: PASS on every run.

**Root cause of the corrected `next build` result.** The prior return
correctly observed that webpack's default `resolve.symlinks: true`
realpaths a junctioned `node_modules/next` back to its real-repository
absolute path during module resolution. It incorrectly concluded the only
fixes were public-candidate edits or "a separately authorized decision."
The actual fix, entirely inside this worker's existing authority: give
`next` a path with zero junctions anywhere in it. `next` is now copied
physically, twice, independently - once directly into the sandbox's own
`node_modules` (so the application's own build never crosses a junction to
resolve it) and once into the support store's own `node_modules` (so
`eslint-config-next`, which itself lives in the support store, can resolve
its own `require("next/...")` without crossing back into the sandbox or
the real repository). Both copies were confirmed non-junction,
non-symlink, and resolved-target-inside-boundary by dedicated tests.

**Evidence-extraction defects found only by running the real candidate.**
Two of the four gate failures observed mid-continuation
(`model_gateway_test`, `cvf_web_next_build` count mismatches) were not
sandbox or isolation defects at all - they were regex gaps in
`_extract_observed_counts` against real tool output formats that no
fixture test reproduced (real vitest interleaves ANSI escape codes; real
Next.js repeats the static-page progress line with extra "using N
workers" text). Both are fixed and now covered by a dedicated regression
test using the exact captured real output strings.

**The structural refactor changed zero observable behavior.** All 58
pre-existing focused tests pass unchanged against the new import layout
(no test-file edit was required to keep them passing), and the real-
candidate proof envelope reproduces `compliant: true`, zero gate failures,
and exact evidence-count matches identical to Amendment 1's own proof on
every command. This confirms the extraction is genuinely behavior-
preserving, not merely believed to be.

**Both size-guard violations are resolved with zero exception growth and no
extra path.** `run_public_projection_pre_push_gate.py` dropped from 1380 to
724 lines (under the 800 hard threshold with no exception needed in
principle, though the seeded exception entry is retained and ratcheted per
the work order's literal instruction rather than removed, since removing
it is explicitly forbidden scope); `test_run_public_projection_pre_push_gate.py`
dropped from 1279 to 1191 lines (under the 1200 hard threshold, achieved by
docstring-only tightening after the sibling-file split was rejected and
repaired, not by any test deletion). The new helper (753 lines, under 900
hard) registers advisory-only, never a violation, under
`check_python_automation_size.py --enforce`. Exactly seven paths exist;
no sibling test file remains.

## Risk / Corrective Action

Corrective action already taken this pass, per the reviewer's
`REVIEW_REJECTED_REPAIR_REQUIRED`: the out-of-manifest test-sibling file
was deleted and its content merged back into the single authorized test
file (see Findings / Position and Amendment 2 Continuation Record). No
further corrective action is outstanding. All seven proof-envelope command
categories pass with exact evidence-count reconciliation; the public root
and Core were never live link targets in the final isolation design (AC-03
conforming); the public clone was confirmed byte-identical before and
after every run; every sandbox and support directory was confirmed fully
removed after every run. The governed Python automation size guard reports
`COMPLIANT` with 0 violations across the three Python implementation files
this amendment touches or creates (the runner, the new helper, and the
single test file - no fourth or eighth file).

The `guard_registry_compatibility` and `pre_public_p3_readiness` families
still compare presence/marker state rather than re-deriving a full
classification registry, unchanged from the prior return; carried forward,
not re-litigated here.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_corpus_scan_registry.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_equivalence_claim_evidence.py`; `governance/compat/check_python_automation_size.py`; `governance/compat/policy_baseline.py` |
| literalTokensReviewed | `WORKER_RETURN_FULL_GATE_V1` required heading set; exact `- Rescan intelligence verdict:` / `- Corpus verdict:` bullet-line formats; `EXTERNAL_INPUT_CANONICAL` phrase requirement; `STATUS_MARKERS` accepting `COMPLETE_PENDING_REVIEW`; corpus-scan-registry `EXTENSIONS/` path-mention scanning; Core Guard Self-Protection required tokens; equivalence-claim disposition-token adjacency for "exact match"/"MATCH" phrasing; `_is_authorized_ratchet_down`'s exact-match-except-`approvedMaxLines` requirement; `DEFAULT_CLASS_THRESHOLDS` category hard/soft values |
| gateRunPurpose | confirm this repaired return's shape, including its `COMPLETE_PENDING_REVIEW` disposition, the sandbox-lifecycle evidence tables, and the Amendment 2 structural-refactor evidence, against the same checker sources already read for the prior repair cycles |
| claimBoundary | structural and literal-shape confirmation only; no semantic self-grading claim |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | delegated implementation worker |
| Provider or surface | local private Core plus read-only public-sync clone plus disposable temporary sandboxes |
| Session or invocation | `public-projection-prepush-t1-amendment-2-worker-20260812` |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | local file reads/edits, Git read-only inspection (`git diff --name-status`, `git status --short`), Python, pytest, `git archive`/Python `tarfile` extraction, PowerShell junction creation, `subprocess.run` package-command execution inside disposable sandboxes, `governance/compat/check_python_automation_size.py`, governance gates |
| Target paths | the seven paths named in Target above (disposition MATCH against the Amendment 2 preflight and against the final repaired state; no scope expansion) |
| Allowed scope source | committed Amendment 2 execution authority (`8bbbd86226880ab952932d9b1aca8ddab20d310c`); Amendment 2 preflight passed in full before any edit; orchestrator `REVIEW_REJECTED_REPAIR_REQUIRED` repair instruction for the out-of-manifest path, resolved by this worker's own in-scope repair (Route 1: remove and preserve coverage), not by a fresh authorization |
| Before status evidence | Core `HEAD` `6d403d72d531d500cf424d71920b4c14c5d9b377`; exact five-path dirty set with all five pinned SHA-256 preimages matched; staged zero; helper file absent; public clone clean at `021f8b852` |
| After status evidence | exactly seven owner paths amended/created in place, no eighth path (disposition MATCH); public clone still clean at `021f8b852afc245a6383177dd69bf56caf488b02` (disposition MATCH), `HEAD` unchanged, before/after comparison disposition MATCH for the real-candidate run in this pass |
| Diff evidence | Core `git status --short` partitions into exactly six untracked Amendment-2 implementation paths (five amended, one new helper file) plus one tracked-and-modified registry amendment (`CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`, part of committed `HEAD`); `git diff --name-status` against `HEAD` shows the same set with no other Core path touched and no sibling test path; no unexpected path |
| Approval boundary | worker-owned local repair only; reviewer/closer owns commit |
| Claim boundary | no push, deploy, provider/store, secret, network install, or public-clone mutation at any point |
| Agent type | delegated implementation worker |
| Invocation ID | `public-projection-prepush-t1-amendment-2-worker-20260812` |
| Expected manifest | six implementation owner paths (including this worker return) plus the registry amendment - exactly seven, no eighth |
| Actual changed set | six implementation owner paths (including this worker return) plus the registry amendment - exactly seven, no eighth |
| Manifest delta | MATCH |
| Deletion or rename disposition | one path deleted this repair pass: `governance/compat/test_public_projection_pre_push_gate_lib.py` (the out-of-manifest sibling the orchestrator's blocking finding named), its full content merged back into `test_run_public_projection_pre_push_gate.py`; one new path created within authorized scope (`public_projection_pre_push_gate_lib.py`); no other deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
| --- | --- |
| claimScope | local maintainability-only structural refactor (runner/helper extraction, plus repair of an earlier out-of-manifest test-file split back into the single authorized test file), exception-registry ratchet, and one real-candidate read-only evaluation run against the pinned public candidate reproducing Amendment 1's proof exactly |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT: JSON receipt captured for the post-repair Amendment 2 real-candidate run (`compliant: true`, 18 checks, 0 gate failures, 4 inherited-debt reports, evidence counts identical to Amendment 1's proof) |
| actionEvidence | ACTION_EVIDENCE_PRESENT: 59 focused pytest cases passed (58 pre-existing plus 1 new no-circular-import test, all inside the single authorized test file); `check_python_automation_size.py --enforce` COMPLIANT, 0 violations; one post-repair real-candidate sandboxed run; worker-return fast gate run; `git diff --check` run |
| invocationBoundary | exactly the seven worker-owned local paths, no eighth; public clone read-only for evaluation only; every mutating command confined to a disposable sandbox outside both repository roots; zero behavioral change to the AC-03-conforming dependency isolation this amendment did not touch |
| interceptionBoundary | no IDE, provider, browser, network, or remote mutation claim |
| claimLanguage | no-commit structural refactor complete; terminal disposition is `COMPLETE_PENDING_REVIEW` because every required command and invariant passes with exact evidence-count reconciliation identical to Amendment 1, size guard is COMPLIANT, and the manifest deviation the orchestrator flagged is repaired, not merely disclosed |
| forbiddenExpansion | generic gate weakening, public mutation, push, deploy, secrets, provider/store, production, command-category omission, size-exception field mutation beyond the authorized downward ratchet, threshold editing, out-of-manifest path retention - none occurred; all seven commands remain configured exactly per the Pinned Command Manifest, none silently dropped or reclassified |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this worker return and its four owned artifacts are private
provenance governance-control-plane work. No public artifact is created,
and the public clone is evaluated read-only only.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Public/simple CVF vocabulary |
| Chain map route | N/A with reason: the orchestrator's `BLOCKER_REJECTED_AS_PREMATURE` continuation dispatch is operator-provided external comparison, critique, or recommendation, absorbed directly as continuation authority rather than routed through external-knowledge intake; no other external knowledge intake occurred |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | the four T1/Amendment-1 implementation owner paths and this worker return |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | all source material is CVF-governed (T1/Amendment 1 baseline, work order, source verification, this continuation dispatch) or direct repository/checker-source/candidate reads; no external authority admitted |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

N/A with reason: this is a bounded in-place repair and continuation of an
existing worker return under committed Amendment 1 authority; it is not a
corpus scan or a knowledge-absorption refresh cycle, so no predecessor scan
ledger governs this scope.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - this tranche amends four
  named artifacts against a named 41-path candidate manifest; it is not a
  corpus inventory, extraction, migration, or completeness claim over a
  folder tree.

## Finding-To-Governance Learning Disposition

| Finding or lesson | Disposition | Learning lane | Next action |
| --- | --- | --- | --- |
| A dependency-isolation design that junctions/hard-links third-party entries directly from a real repository's installed store, verified only by a link-placement check (not a resolved-target check), can pass every test while still being contract-nonconforming under an AC-03-style "real repositories are read-only copy sources, never live link targets" requirement | RULE_GAP_CLOSED | GOVERNANCE_CONTROL_PLANE | require every dependency-isolation implementation to copy into a disposable support store first, then link only from that copy, with a resolved-target (not just link-location) assertion on every link |
| Webpack's default `resolve.symlinks: true` realpaths a junctioned dependency back to its real-repository absolute path during build; the general fix is not editing the consuming project's build config, it is eliminating the junction for that specific dependency (a full physical copy) - a fix available entirely within a sandbox-authoring worker's own scope | RULE_EXISTS | GOVERNANCE_CONTROL_PLANE | keep a documented, explicit `full_copy_entries` mechanism for any dependency a build tool resolves via realpath-following symlink/junction traversal, rather than assuming the only fix is consumer-side configuration |
| A package that itself lives in a dependency-store copy (not the sandbox) can `require()` another dependency that was only copied into the sandbox and fail, because Node's module resolution walks up from the requiring module's own location, not from some shared root | RULE_GAP_CLOSED | GOVERNANCE_CONTROL_PLANE | when a `full_copy_entries` dependency is also required by another package living in a separate store/copy location, place an independent copy of it in every location from which it is required, not just the sandbox |
| Command output evidence-extraction regexes must be validated against a real captured sample of the actual tool's output before being trusted as a fail-closed signal; a fixture using synthetic/simplified output can pass every test while the regex fails against real ANSI-colored or multi-line-progress output | RULE_GAP_CLOSED | GOVERNANCE_CONTROL_PLANE | strip ANSI escape codes before matching tool output, and validate extraction regexes against a real captured sample, not only a synthetic fixture string |
| A disposable sandbox's cold dependency/tool caches (no `.eslintcache`, no warm TypeScript parser state) can make a command that is fast against a warm real clone take materially longer against a fresh sandbox on every single run, by design | RULE_EXISTS | GOVERNANCE_CONTROL_PLANE | size `timeoutSeconds` for any sandboxed command against a directly-measured cold-sandbox run, not against typical warm-clone latency |

## Epistemic Process Block

### Expected Result / Prediction

Prediction (this continuation, per orchestrator R-01/R-02/R-03 findings):
repairing the dependency-isolation design to be AC-03 conforming (copy into
a disposable support store, then link only from that copy; give `next` a
genuinely junction-free path) will resolve the `next build` failure without
requiring any public-candidate edit, and enforcing real expected/observed
evidence-count reconciliation will surface any remaining evidence gaps
honestly rather than accepting a bare zero exit code.

### Evidence Comparison

Confirmed exactly. After the AC-03 repair, `next build` passes with exact
evidence (`{"staticPages": 121}` matching expected `121`) with no
public-candidate edit. Enforcing evidence-count reconciliation surfaced two
further, previously-hidden defects that a bare-exit-code check would have
missed entirely: the ANSI-stripping gap and the static-page progress-line
regex gap, both in `_extract_observed_counts` itself, not in the sandbox or
isolation logic. All three were fixed and are now independently covered by
tests using the real captured output format, not only synthetic fixture
strings.

### Contradiction Or Gap Disposition

Gap closed, not contradiction. The prior return's classification of
`next build` as a fresh `BLOCKED_CONTRACT_CONTRADICTION` requiring
public-candidate edits is retracted: it was a `PREMATURE_BLOCKER` caused by
`DEPENDENCY_ISOLATION_IMPLEMENTATION_GAP` (an under-scoped `full_copy_entries`
mechanism, not yet implemented in that pass), not a genuine irreconcilable
requirement. The orchestrator's R-01 finding ("full copy was already
authorized... disk cost is not a contract contradiction") is confirmed
correct by this continuation's evidence.

### Claim Update

Claim REVISED (fully resolved): the disposable-sandbox strategy, once made
AC-03 conforming and once `next` is given a genuinely junction-free sandbox
path, resolves all seven previously-blocked or previously-untestable
command categories against the real pinned candidate, with zero public
mutation and exact evidence-count reconciliation. No further amendment or
public-candidate edit is required for this profile's proof envelope.

### Amendment 2 Addendum

Prediction (Amendment 2, per the baseline's Required Semantic Delta):
relocating cohesive non-CLI implementation into a new library helper, with
zero logic change, will bring both the CLI runner and the test file under
their applicable hard size thresholds while reproducing an identical
real-candidate proof envelope to Amendment 1's own independently reviewed
result.

Evidence comparison: confirmed exactly on the functional axis - the
post-refactor real-candidate run reproduces `compliant: true`, zero gate
failures, and every `expectedEvidence` count identical to Amendment 1's
proof, with zero test-file logic edits required for the runner/helper
extraction. Initially contradicted on the manifest axis: the prediction
did not anticipate that the test file, unedited, would remain over its own
hard threshold even after the extraction (since the extraction changed
only import wiring, not test-file line count), and the first repair
attempt (a test-file split into a second new file) exceeded the work
order's exact-seven manifest without authorization - the orchestrator
correctly rejected this. Repaired: the split was reverted (content merged
back, nothing deleted) and the size threshold met instead through
docstring-only compression inside the single authorized test file. Claim
REVISED (fully resolved): the structural-refactor strategy is functionally
proven sound and complete, and the manifest-exactness dimension is now
also satisfied exactly, with no path beyond the seven the work order
authorized.

## Machine Closure Package

| Closure item | Evidence | Status |
| --- | --- | --- |
| Amendment 1 work order | committed authority `ddd54cbebb550af83db6ac8dbb7d96f5795768aa` | PASS |
| Amendment 2 work order | committed authority `8bbbd86226880ab952932d9b1aca8ddab20d310c` | PASS |
| Worker return | this file, amended in place | PASS |
| Size guard | `check_python_automation_size.py --enforce` | PASS: COMPLIANT, 0 violations |
| Deterministic proof | 59 focused tests; real-candidate sandboxed run | PASS: 7/7 proof-envelope categories PASS with exact evidence-count reconciliation identical to Amendment 1 |
| Public clone invariant | HEAD/status identical before/after the Amendment 2 real-candidate run | PASS |
| Sandbox teardown | fully removed after the Amendment 2 real-candidate run | PASS |
| Manifest exactness | exactly seven authorized paths, no eighth | PASS: out-of-manifest path repaired, not carried |
| Local commits | reviewer-owned next action; worker did not commit | N/A with reason |
| Push/deploy | separately controlled; not attempted | N/A with reason |

## Claim Boundary

This worker return documents an in-place continuation repair of the
committed Amendment 1 disposable-sandbox strategy (AC-03 dependency-
isolation conformance, evidence-extraction correctness, timeout
calibration), its expanded focused tests, and four iterative real-candidate
read-only evaluation runs against the actual pinned public candidate, each
confirmed to leave the real public clone byte-identical before and after.
It does not authorize push, deploy, Netlify or any provider/browser/store
action, public clone mutation, secret access, network installs, or any
change to the generic private pre-push catalog. Terminal disposition is
`COMPLETE_PENDING_REVIEW`: every required command and invariant passes,
with exact expected/observed evidence-count reconciliation for every
command that configures `expectedEvidence`. Independent orchestrator review
remains required before this lane can proceed to commit or any
further-authorized action.

## git status --short

```text
 M governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json
?? docs/reference/CVF_PUBLIC_PROJECTION_PRE_PUSH_PROFILE_STANDARD_2026-08-11.md
?? docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md
?? governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json
?? governance/compat/public_projection_pre_push_gate_lib.py
?? governance/compat/run_public_projection_pre_push_gate.py
?? governance/compat/test_run_public_projection_pre_push_gate.py
```

(The independent reviewer's own rejected completion review,
`docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_AMENDMENT_2_COMPLETION_2026-08-12.md`,
is also untracked in the live working tree at repair time; it is
reviewer-owned, not a worker path, and this worker return neither created,
edits, nor claims it as part of its own manifest.)

Note: this is disposition MATCH: exactly seven paths, no eighth. The
sibling test file that previously appeared here
(`governance/compat/test_public_projection_pre_push_gate_lib.py`) no
longer exists - deleted and merged back into
`test_run_public_projection_pre_push_gate.py` per this repair. The five
inherited implementation paths (standard, policy, runner, test file,
worker return) plus the one newly created file (helper) are all untracked
at this repaired Amendment 2 pass, matching the dispatch's own statement
that they are "untracked intentionally" so authority commits can be
reviewed independently. The size-exception registry shows as
tracked-and-modified (`M`) since it is committed as part of the Amendment
2 authority batch at `HEAD` and this pass amends only its
`approvedMaxLines` ratchet in the working tree. No file was staged with
content and no commit was made at any point. The three Amendment 2
authority files
(`docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_AMENDMENT_2_SOURCE_VERIFICATION_2026-08-12.md`,
`docs/baselines/CVF_GC018_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_AMENDMENT_2_2026-08-12.md`,
`docs/work_orders/CVF_AGENT_WORK_ORDER_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_AMENDMENT_2_2026-08-12.md`)
are already committed as part of Core `HEAD`
(`6d403d72d531d500cf424d71920b4c14c5d9b377`) and therefore do not appear in
this working-tree status, alongside the three Amendment 1 authority files
committed earlier at `ddd54cbebb550af83db6ac8dbb7d96f5795768aa`.

## Changed Files

- `docs/reference/CVF_PUBLIC_PROJECTION_PRE_PUSH_PROFILE_STANDARD_2026-08-11.md` (unchanged this pass; last amended in the Amendment 1 continuation pass)
- `governance/compat/CVF_PUBLIC_PROJECTION_PRE_PUSH_POLICY.json` (unchanged this pass; last amended in the Amendment 1 continuation pass)
- `governance/compat/run_public_projection_pre_push_gate.py` (amended this pass: reduced from 1380 to 724 lines via structural extraction into the new library helper; all relocated logic imported back under its original private name, zero call-site or behavioral change; unaffected by the test-file repair)
- `governance/compat/public_projection_pre_push_gate_lib.py` (created this pass: 753 lines; sandbox lifecycle, dependency-isolation utilities, the four inherited-debt family checkers, and command-output evidence extraction, disposition NOT_LITERAL_WITH_REASON: moved verbatim in logic, module location changed, from the runner)
- `governance/compat/test_run_public_projection_pre_push_gate.py` (repaired this pass: reduced from 1279 to 1191 lines - not via the rejected split, but by merging the deleted sibling file's full content back in, then tightening non-load-bearing docstring prose only; 59 test functions, zero deleted, zero duplicated)
- `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json` (amended this pass: the runner entry's `approvedMaxLines` ratcheted to 724 (unchanged from the first pass); the test-file entry's `approvedMaxLines` corrected to 1191 (superseding the first pass's incorrect 570, which reflected the now-deleted split); disposition MATCH: every other field on both entries verified unchanged from the committed baseline, and both new caps remain strictly below the seeded baseline values (1380, 1279))
- `docs/reviews/CVF_PUBLIC_PROJECTION_PREPUSH_T1_PROFILE_OWNER_AND_GATE_WORKER_RETURN_2026-08-11.md` (rewritten in place, this file, repairing every manifest claim that referenced the now-deleted sibling file)

Deleted this pass: `governance/compat/test_public_projection_pre_push_gate_lib.py` (the out-of-manifest path the reviewer's F-01 finding named; its content is fully preserved, merged into `test_run_public_projection_pre_push_gate.py`, not lost).

## Worker Experience Retrospective

The costliest defects in this continuation pass were, again, only
discoverable by running the real candidate: the hard-linked-file resolved-
target boundary bug (a directory junction and a hard-linked file have
different "resolved target" semantics, and the assertion needed to branch
on which one it was); the `eslint-config-next` cross-package resolution gap
(only surfaced because `eslint-config-next` genuinely lives in a different
physical location than `next` once the two are isolated independently);
and both evidence-extraction regex gaps (only surfaced against real ANSI-
colored, multi-line-progress tool output, never reproduced by the
simplified fixture format). Each was fixed and re-verified against the real
candidate before moving to the next, exactly as the orchestrator's
"Real-Candidate Verification" instruction required.

WORKER_EXPERIENCE_RETRO:
frictionLevel: MEDIUM
frictionType: HELPER_GAP
observedStep: fixture-test coverage of the sandbox lifecycle and evidence extraction did not surface any of the four real-candidate-only defects (hard-link target-boundary branch, eslint-config-next cross-store resolution, ANSI stripping, static-page regex) until real-candidate runs were performed; each is now covered by a dedicated regression test using the real captured output/topology, closing the specific gap for future changes
preventiveControlCandidate: HELPER_DIAGNOSTIC

## Command Evidence

| Command | Working directory | Result | Exit code |
| --- | --- | --- | --- |
| Amendment 2 preflight verification (HEAD equals executionBaseHead, exact five-path dirty set, five SHA-256 preimages, helper-file absence, staged count, public clone state) | Core root | all conditions matched exactly | n/a |
| `python governance/compat/run_adif_defect_resolver.py --task-class "PUBLIC-PROJECTION-PREPUSH-T1 Amendment 2 size-guard refactor dispatch" --role worker --lifecycle-phase pre-implementation` | Core root | `Returned defects: NONE_RETURNED` | 0 |
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-dispatch` | Core root | `COMPLIANT` | 0 |
| `python -c "import governance.compat.run_public_projection_pre_push_gate"` / `python -c "import public_projection_pre_push_gate_lib"` (both import paths) | Core root | both import cleanly; every re-exported symbol resolves to the helper module | 0 |
| Repair: deleted `governance/compat/test_public_projection_pre_push_gate_lib.py`; merged its full content back into `governance/compat/test_run_public_projection_pre_push_gate.py`; tightened non-load-bearing docstring prose only | Core root | single merged test file: 1191 physical lines (under the 1200 hard threshold); 59 test functions, zero duplicates, zero deletions | n/a |
| `python -m pytest governance/compat/test_run_public_projection_pre_push_gate.py -q` (final, post-repair, single file) | Core root | `59 passed in ~66s` | 0 |
| `python governance/compat/check_python_automation_size.py --enforce` | Core root | `COMPLIANT`, 0 violations, 11 advisories (none constitute a violation for the three files this amendment touches/creates) | 0 |
| `python governance/compat/run_public_projection_pre_push_gate.py --public-root "D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync" --base 2103a38fda01ee827e9fc6c3be38a824fa5d54ad --head 021f8b852afc245a6383177dd69bf56caf488b02 --json` (Amendment 2, real candidate, real sandbox, post-repair code) | Core root | 18 checks; all seven `external_command:*` PASS with `observedEvidence` disposition MATCH against `expectedEvidence` for `model_gateway_test` (`{"files": 30, "tests": 231}`), `cvf_web_test` (`{"files": 15, "tests": 218}`), `cvf_web_next_build` (`{"staticPages": 121}`) - identical to Amendment 1's proof; `public_root_invariant_check` PASS; `sandbox_teardown` PASS; 4 inherited-debt REPORT rows; `compliant: true` | 0 |
| `git status --short` / `git rev-parse HEAD` (public clone, before and after the post-repair Amendment 2 real-candidate run) | public-sync clone root | empty / `021f8b852afc245a6383177dd69bf56caf488b02`; before/after disposition MATCH | 0 |
| sandbox/support-directory residue check (OS temp root, after the post-repair real-candidate run) | n/a | no `cvf-pp-sandbox-*` directories remain | n/a |
| `git diff --name-status HEAD` (Core, this pass) | Core root | six untracked implementation paths plus one tracked-and-modified registry amendment, no other path, no sibling test path | 0 |
| `git diff --check` | Core root | no whitespace errors (only autocrlf LF/CRLF warnings) | 0 |

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: extend the same isolated
public-projection implementation surface under `governance/compat/` that
T1 and Amendment 1 already authorized, by relocating cohesive non-CLI
logic out of the existing runner into exactly one new, equally isolated
library helper file, while using the GC-018-seeded registry mechanism only
to admit the already-proven runner and test preimages into governed commit
flow; no growth or semantic weakening is authorized. No existing checker,
hook catalog, or guard semantics are changed.

Protected paths:

- `governance/compat/run_public_projection_pre_push_gate.py`
- `governance/compat/public_projection_pre_push_gate_lib.py`
- `governance/compat/test_run_public_projection_pre_push_gate.py`
- `governance/compat/CVF_PYTHON_AUTOMATION_SIZE_EXCEPTION_REGISTRY.json`

Operator authorization: committed Amendment 2 execution authority
(`8bbbd86226880ab952932d9b1aca8ddab20d310c`), carried forward from the
committed work order's own Core Guard Self-Protection Authorization
section.

Rollback boundary: revert exactly the six Amendment 2 implementation paths
to their pre-Amendment-2 (Amendment-1-accepted, five-path) state if
rejected, with the new helper file removed and the two freshly seeded
registry entries removed as one authorized rollback; do not revert
candidate commits `492e11eab`, `021f8b852`, or any session-sync or prior
Amendment authority commit. (The out-of-manifest test-sibling file the
reviewer's F-01 finding named has already been removed as part of this
repair, its content merged back into the authorized test file; no
further rollback action is needed for that path.)

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. No `git add` with staged content and no
`git commit` was executed at any point in this session, including during
this Amendment 2 pass. The six untracked implementation paths and this
worker return remain uncommitted; the size-exception registry amendment is
an unstaged working-tree change against its committed `HEAD` content. The
public-sync clone was never written to, staged, or committed by this
runner or by this worker at any point; it was confirmed clean at
`021f8b852afc245a6383177dd69bf56caf488b02`, `HEAD` and full status
byte-identical, before and after the Amendment 2 real-candidate run, and
the disposable sandbox and its support directory were fully removed after
the run.

## Terminal Disposition

COMPLETE_PENDING_REVIEW

This is a repaired return responding to the independent reviewer's
`REVIEW_REJECTED_REPAIR_REQUIRED` (blocking finding F-01: an unauthorized
eighth implementation path; F-02: contradictory manifest claims in this
same file). Both are repaired, not merely disclosed: the out-of-manifest
`governance/compat/test_public_projection_pre_push_gate_lib.py` has been
deleted, its full content (every test, fixture, and assertion) merged
back into the single authorized `test_run_public_projection_pre_push_gate.py`,
which now stands at exactly 1191 physical lines - under the 1200-line
`python_test` hard threshold, achieved by tightening non-load-bearing
docstring prose only, never by deleting or weakening coverage. Every
manifest claim throughout this file (Target / Source, Findings /
Position, Agent Operation Trace, Machine Closure Package, Command
Evidence, git status, Changed Files, Core Guard Self-Protection) has been
corrected to state consistently: exactly seven authorized paths exist,
no eighth.

Amendment 2's structural refactor is complete with zero observable
behavioral change: `run_public_projection_pre_push_gate.py` reduced from
1380 to 724 lines (under the 800-line `python_cli_orchestrator` hard
threshold); `public_projection_pre_push_gate_lib.py` created at 753 lines
(under the 900-line `python_library_helper` hard threshold);
`test_run_public_projection_pre_push_gate.py` reduced from 1279 to 1191
lines (under the 1200-line `python_test` hard threshold).
`governance/compat/check_python_automation_size.py --enforce` reports
`COMPLIANT`, 0 violations. Both seeded exception-registry entries carry
`approvedMaxLines` values (724, 1191) strictly below the committed
baseline's seeded values (1380, 1279), with every other field on both
entries unchanged, satisfying `_is_authorized_ratchet_down`. 59 focused
tests pass (58 pre-existing, zero deleted, plus 1 new no-circular-import
test), all inside the single authorized test file. The post-repair
real-candidate proof envelope reproduces Amendment 1's result exactly:
`compliant: true`, zero gate failures, all seven external command
categories PASS, with `observedEvidence` exactly matching Amendment 1's
proof on every `expectedEvidence`-bearing command. The public clone
remained disposition MATCH (byte-identical) before and after the run; the
sandbox and support directory were fully removed. Core `HEAD` remains
`6d403d72d531d500cf424d71920b4c14c5d9b377`; staged content is zero. No
commit, push, deploy, or public mutation occurred at any point.
