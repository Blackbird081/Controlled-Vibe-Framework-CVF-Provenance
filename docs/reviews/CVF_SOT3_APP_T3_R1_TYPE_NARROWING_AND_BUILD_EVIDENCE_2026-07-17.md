# CVF SOT3-APP-T3-R1 Type Narrowing And Build Evidence

Memory class: governed-worker-evidence

Self-declared worker-return artifact: yes

Status: ACCEPTED_BY_REVIEWER_WITH_REPAIR

docType: review_context

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_APP_T3_R1_SOURCE_LOCAL_TYPE_NARROWING_AND_BUILD_CLOSURE_2026-07-17.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_APP_T3_R1_SOURCE_LOCAL_TYPE_NARROWING_AND_BUILD_CLOSURE_2026-07-17.md`

executionBaseHead: `4f513f324`

## Reviewer Repair Overlay

Independent review accepted the worker's source-local type narrowing and
build/test repair, then found and repaired one additional application
boundary defect before closure: raw thrown values were redacted from the HTTP
response but still passed to the application logger. The reviewer repaired
that defect within the already authorized API middleware/test scope by
exporting a safe `sanitizeError(error: unknown)` projection and using it for
both logging and response creation.

Final reviewer-recomputed hashes:

- `apps/api/src/middleware/error.middleware.ts`:
  `7A49558F9AE2DFC044DC000C4CDE0C69C8AC0A6BB4766D364EDD646D2EA6E38D`
- `apps/api/src/middleware/application-boundary.middleware.test.ts`:
  `2A99B6CD895ED2DDD48D4006C9E94EDD972F076937A622CB32A99CFF512AAE22`
- `apps/web/src/layouts/application-layout.tsx`:
  `03F3736A5D63D2237900835E9373387399C1FD672994DBE9D5E4E93F71E96F1B`
- `apps/web/src/layouts/application-layout.test.tsx`:
  `A8B33B6F4C99BAB26EC89A453C1BD012736573E3ECC1DEFBB0DDE7AAC61E70F3`

Final reviewer-recomputed commands: isolated API/web typecheck and build
PASS; root typecheck/build PASS; root tests 30 files and 45 tests PASS;
focused tests 2 files and 10 tests PASS; doctor `healthy: true`.

## Purpose

Record the exact four-path before/after hash manifest, isolated and root
compiler results, focused and full test receipts, navigation-preservation
proof, and doctor output for the SOT3-APP-T3-R1 source-local type-narrowing
and build-closure tranche.

## Target / Source

Target: the four allowed external source/test outputs under
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application`, listed in the
work order's Allowed Scope.

Source: the work order's Execution Plan, Fail Conditions, and Verification
Commands; the accepted T3 blocked-return review
(`docs/reviews/CVF_SOT3_APP_T3_BLOCKED_RETURN_REVIEW_2026-07-17.md`); direct
reads of the pre-edit external source files.

## Scope / Methodology

1. Captured `executionBaseHead=4f513f324` on a clean provenance worktree.
2. Confirmed the mandatory pre-implementation gate
   (`--base 7e347cae0 --head HEAD`); `COMPLIANT`.
3. Computed SHA-256 before-hashes for all four allowed paths; the web layout
   test path was `ABSENT`.
4. Reproduced both isolated compiler errors before any edit:
   `apps/api` typecheck failed with `TS18046` at
   `error.middleware.ts(6,49)`; `apps/web` typecheck failed with `TS2322` at
   `application-layout.tsx(27,31)`.
5. Repaired both defects at their exact source location (see Semantic
   Change Summary), without touching any `tsconfig*`, manifest, lockfile,
   or workspace-configuration path.
6. Added two regression tests: one non-Error thrown-value case in the
   existing API test file, and one new web layout test verifying all
   thirteen navigation targets render correctly.
7. Reran isolated API/web typecheck and build, then root typecheck, build,
   test, the exact focused Vitest command, and doctor.
8. Computed after-hashes for all four allowed paths.

## Findings / Position

### Semantic Change Summary

| # | Path | Change | Reason |
|---|---|---|---|
| 1 | `apps/api/src/middleware/error.middleware.ts` | added a local `extractErrorMessage(error: unknown): string` helper that narrows via `error instanceof Error` (returns `error.message`) or `typeof error === "string"` (returns the string), else returns `""`; the existing `SOT_[A-Z0-9_]+` token-extraction regex now runs against this helper's return value instead of directly against `error.message` | `error` in a Fastify `setErrorHandler` callback is typed `unknown`/not narrowed by default under `strict`; dereferencing `.message` directly failed `TS18046`. The narrowing preserves the exact existing token-extraction and redaction behavior for every `Error`-typed value (including `SOT_*`-prefixed messages and their raw-suffix stripping) and additionally handles non-`Error` thrown values (objects, strings) without ever exposing their raw content, since a non-matching value produces `""`, which never matches the `SOT_` regex and falls to the existing generic `"An internal error occurred."` / `SOT_INTERNAL_ERROR` fallback |
| 2 | `apps/api/src/middleware/application-boundary.middleware.test.ts` | added one new test, "redacts a non-Error thrown value and never dereferences it as a message," which throws a plain object containing a sentinel key/value from the injected boundary and asserts a `500` response with `SOT_INTERNAL_ERROR`, the fixed safe message, and confirms the sentinel value is absent from the full JSON response body | proves the new `extractErrorMessage` narrowing handles the non-`Error` case the work order specifically requires regression coverage for, using the real production `registerErrorMiddleware` and `buildApp`, not a mock |
| 3 | `apps/web/src/layouts/application-layout.tsx` | replaced the untyped `const links = [["path", "label"], ...]` array (inferred as `(string \| undefined)[][]` at the destructured element level under `noUncheckedIndexedAccess`) with `interface NavLinkEntry { to: string; label: string }` and `const links: NavLinkEntry[] = [{ to: "...", label: "..." }, ...]`; the render call changed from `links.map(([to, label]) => ...)` to `links.map(({ to, label }) => ...)` | the prior array-of-tuples shape let TypeScript widen each destructured element to `string \| undefined` because `noUncheckedIndexedAccess` treats array element access (including array destructuring) as possibly out-of-bounds; an explicit named-field interface has no such ambiguity, so `to` is provably `string` everywhere, which is what `NavLink`'s `to: To` prop requires. All thirteen path/label pairs and their order MATCH the pre-edit array exactly (verified by direct visual diff during editing), only the literal shape changed from `[path, label]` tuples to `{ to: path, label }` objects |
| 4 | `apps/web/src/layouts/application-layout.test.tsx` | new file | renders `<ApplicationLayout>` inside a `MemoryRouter`/`Routes`/`Route` tree using `renderToStaticMarkup` from `react-dom/server` (no `jsdom`/`happy-dom`/`@testing-library/react` dependency was added, since none is installed and adding one is forbidden by this work order's Forbidden Scope), then asserts the resulting HTML string contains an `href` attribute matching each path immediately followed by the corresponding label text, for all thirteen expected pairs, and asserts no `href="undefined"` or `href="null"` appears anywhere in the output |

No other allowed path required a change. No `tsconfig*`, manifest, lockfile,
or workspace-configuration path was modified; their current hashes were
independently reconfirmed unchanged (see Non-Allowed-Path Verification
below).

### Exact Four-Path Before/After Hash Manifest

| # | Path | Before SHA-256 | After SHA-256 | Disposition |
|---|---|---|---|---|
| 1 | `apps/api/src/middleware/error.middleware.ts` | `f71d1010386f531fc159c8b5412961ba5478d9234fe0f0dab5df062c1723f965` | `e32940be54de93b5327b54e62d0769922462d98df6fdd2e2de2c0b45aad1132e` | CHANGED |
| 2 | `apps/api/src/middleware/application-boundary.middleware.test.ts` | `01dc7edab2d936a901bbd6dca396036ddd459e09d11fc61640d54140d281deef` | `b9c81cb5867158a28aee6b0ced249bd2777f7d4830cfb5f23b2a7c12f7aec0d0` | CHANGED |
| 3 | `apps/web/src/layouts/application-layout.tsx` | `f64722c15fd5283265ca9e13da36c1074b6e30bb19e7bebdb94e0264fd55c2ac` | `03f3736a5d63d2237900835e9373387399c1fd672994dbe9d5e4e93f71e96f1b` | CHANGED |
| 4 | `apps/web/src/layouts/application-layout.test.tsx` | ABSENT | `a8b33b6f4c99bab26ec89a453c1bd012736573e3ecc1defbb0dde7aac61e70f3` | CREATED |

No path outside this exact four-path set was created, modified, or deleted.

### Non-Allowed-Path Verification

To prove no forbidden path drifted, the following SHA-256 hashes were
recomputed after all edits and confirmed identical to their T3-accepted
values:

| Path | Hash | Disposition |
|---|---|---|
| `apps/api/tsconfig.json` | `f9163eb499f3b039fed2c39e5e10e16f2c090256d43a49db58ba28c8063e1d88` | UNCHANGED (matches T3 evidence) |
| `apps/web/tsconfig.json` | `4c258fa3843cd85958bf841687c3424aff2121cc743abecbd491ff8efc911286` | UNCHANGED (matches T3 evidence) |
| `package.json` | `6bc334406dce42ddbbd85f644493a5cc0348174f6a6679e66e0abb11773e96c2` | UNCHANGED (matches T3 evidence) |
| `pnpm-lock.yaml` | `400117fa6b728c2b4c4ab70af0f6ece90a2f5e2d1216b32b29a0ffb034106438` | UNCHANGED (matches T3 evidence) |
| `tsconfig.base.json` | `2b6a15abe9d9b89bd971929ad7c34b7a3e871f7548ae352444628784c8078dde` | UNCHANGED (matches T3 evidence) |
| `vitest.workspace.ts` | `08d7f683700b53d82bcd4096edd08ca616785a094b6ad64820ddb4ea0a0de6a5` | UNCHANGED (matches T3 evidence) |

No compiler option, dependency version, or workspace configuration was
touched.

### Command Receipts

| # | Command | Exit | Result |
|---|---|---|---|
| 1 | `corepack pnpm@9.15.0 --filter @sot/api typecheck` (before edit) | 2 | `TS18046` reproduced at `error.middleware.ts(6,49)` |
| 2 | `corepack pnpm@9.15.0 --filter @sot/web typecheck` (before edit) | 2 | `TS2322` reproduced at `application-layout.tsx(27,31)` |
| 3 | `corepack pnpm@9.15.0 --filter @sot/api typecheck` (after repair) | 0 | clean, no output; `API_TYPE_ERROR_COUNT=0` |
| 4 | `corepack pnpm@9.15.0 --filter @sot/api build` (after repair) | 0 | clean, no output |
| 5 | `corepack pnpm@9.15.0 --filter @sot/web typecheck` (after repair) | 0 | clean, no output; `WEB_TYPE_ERROR_COUNT=0` |
| 6 | `corepack pnpm@9.15.0 --filter @sot/web build` (after repair) | 0 | `tsc -b` clean; `vite build` succeeded: 56 modules transformed, `dist/index.html`, `dist/assets/index-C6TzOG-E.css`, `dist/assets/index-5tzf_3QC.js` emitted |
| 7 | `corepack pnpm@9.15.0 typecheck` (root) | 0 | 9 of 10 workspace projects; `apps/web typecheck: Done`; `apps/api typecheck: Done` |
| 8 | `corepack pnpm@9.15.0 build` (root) | 0 | 9 of 10 workspace projects; `apps/web build: Done`; `apps/api build: Done` |
| 9 | `corepack pnpm@9.15.0 test` (root) | 0 | 30 test files, 44 tests, ALL PASS (up from T3's 29 files / 42 tests) |
| 10 | `corepack pnpm@9.15.0 exec vitest run --workspace vitest.workspace.ts apps/api/src/middleware/application-boundary.middleware.test.ts apps/web/src/layouts/application-layout.test.tsx` | 0 | 2 test files, 9 tests, ALL PASS |
| 11 | `node_modules/.bin/tsx scripts/doctor.ts` (direct invocation, matching the T3 evidence's documented reason for bypassing the pnpm-wrapped stdout capture) | 0 | `healthy: true`; all 10 CVF bindings present and valid |

### Test Discovery And Pass/Fail Counts

- `pnpm test` (root): 30 test files, 44 tests, all passing. This is the
  prior T3 evidence's 29 files / 42 tests plus exactly two new tests: the
  API non-Error regression case and the new web layout navigation test.
- Focused Vitest command: 2 test files, 9 tests, all passing (7 pre-existing
  API middleware tests + 1 new API regression test + 1 new web layout
  test).
- `API_TYPE_ERROR_COUNT`: 0 (isolated `apps/api` typecheck, after repair).
- `WEB_TYPE_ERROR_COUNT`: 0 (isolated `apps/web` typecheck, after repair).

### Redaction And Navigation Preservation Proof

- No raw internal error detail is ever returned by the API, for any thrown
  value shape. The pre-existing tests (raw `Error` message, `SOT_*`-prefixed
  `Error` with a raw suffix) continue to pass unchanged. The new regression
  test proves a non-`Error` thrown object (containing the sentinel key
  `TEST_SENTINEL_SECRET_VALUE`) also never reaches the HTTP response: the
  response is `500`/`SOT_INTERNAL_ERROR`/`"An internal error occurred."`,
  and `JSON.stringify(body)` does not contain the sentinel value.
- All thirteen navigation path/label pairs are byte-identical to the
  pre-edit source, in the same order, only the container shape changed from
  `[path, label]` tuples to `{ to, label }` objects. The new
  `application-layout.test.tsx` test independently re-declares the expected
  thirteen pairs from the work order's own Source Verification Block
  citation (lines 3-17 of the pre-edit file) and asserts each one renders
  with a real `href` attribute and label text in the static-rendered HTML,
  and that no `href="undefined"` or `href="null"` appears anywhere.

## Risk / Corrective Action

| Risk | Resolution |
|---|---|
| adding a DOM-testing dependency (`jsdom`, `@testing-library/react`) would have been the more conventional way to test the rendered layout | not available in the installed dependency set and forbidden by this work order's Forbidden Scope ("any new dependency"); used `react-dom/server`'s `renderToStaticMarkup`, which requires no DOM shim and is already available via the installed `react-dom` package, to get equivalent real-render proof |
| narrowing `unknown` in a catch/error handler can silently swallow real error information if done incorrectly | the new `extractErrorMessage` helper is exhaustively tested: `Error` instances (both plain and `SOT_*`-prefixed with a raw suffix), and non-`Error` thrown values, all produce the exact same redaction behavior as before for `Error` cases, and a safe empty-string fallback (routed to the existing generic-error path) for anything else |
| an interface-typed navigation array could accidentally drop or reorder a target during the shape change | the Semantic Change Summary and this evidence explicitly re-list and cross-check all thirteen pairs against the pre-edit source; the new test independently asserts each one renders |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_equivalence_claim_evidence.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Status: COMPLETE_PENDING_REVIEW; section name: Purpose; section name: Target / Source; section name: Scope / Methodology; section name: Findings / Position; section name: Risk / Corrective Action; section name: Claim Boundary |
| gateRunPurpose | confirm this evidence artifact satisfies structural completeness for a `docs/reviews/` companion before the paired worker return links it |
| claimBoundary | checker conformance confirms structural shape only; does not substitute for the reviewer's own independent command reruns |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated implementation worker |
| Provider or surface | operator sibling source plus private provenance workspace |
| Session or invocation | SOT3-APP-T3-R1, 2026-07-17 |
| Working directory | external `SOT-Application` root and private provenance root |
| Command or tool surface | source edits, SHA-256 hashing, `corepack pnpm@9.15.0` typecheck/build/test/doctor, `pnpm exec vitest run`, direct `tsx` invocation, read-only `git status` in both roots |
| Target paths | four allowed external paths |
| Allowed scope source | work order Allowed Scope and paired GC-018 |
| Before status evidence | two pre-existing files to change, one new test file to create, one pre-existing test file to extend; both isolated compiler errors reproduced |
| After status evidence | two files changed, one file extended, one file created; isolated and root typecheck/build both clean; 44/44 tests pass; doctor healthy |
| Diff evidence | SHA-256 before/after manifest above; provenance `git diff --name-status` reports the two new provenance files as untracked, not tracked modifications |
| Approval boundary | bounded deterministic SOT3-APP-T3-R1 implementation only |
| Claim boundary | no provider/live/public/T4/production claim; no compiler-option, dependency, or workspace-config change |
| Agent type | worker |
| Invocation ID | `sot3-app-t3-r1-worker-execution-2026-07-17` |
| Expected manifest | four allowed external paths |
| Actual changed set | four allowed external paths (see hash manifest above) |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | local deterministic type-narrowing repair and real executed test evidence in the sibling source |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: real executed isolated/root typecheck, build, and test commands, all passing |
| receiptEvidence | CVF_RECEIPT_PRESENT: real command exit codes and full test-run output for every listed command |
| actionEvidence | ACTION_EVIDENCE_PRESENT: two source files changed, one test file extended, one test file created; 44 real tests executed and passed |
| invocationBoundary | pinned `corepack pnpm@9.15.0` commands and direct `tsx` invocation only; no dependency installation or network resolution was performed |
| interceptionBoundary | application/API call-path guards exercised by real executed tests, including a real HTTP request/response cycle via Fastify's `.inject()`; no universal agent interception claim |
| claimLanguage | bounded downstream source-local type-narrowing and real test/build evidence |
| forbiddenExpansion | provider, network, live, browser, public, production, T4, Git initialization, compiler-option change, dependency change, workspace-config change, or unlisted path |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private sibling application evidence; no public-sync authorization
or public-safe artifact set exists.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | accepted T3 block -> T3-R1 repair -> independent review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_work_order_dispatch_quality.py` |
| Owner surface | SOT3-APP roadmap and this T3-R1 evidence artifact |
| Disposition | ADAPT_CONTRACT; no CVF Core import performed |
| Claim boundary | bounded sibling implementation evidence only; no public/product/runtime-wide claim |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- Reason: this evidence artifact performs no intake refresh and no
  source-backed reassessment of the accepted predecessor corpus; it records
  the T3-R1 source-local repair's command receipts and hash manifest only.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - this is an exact four-path
  repair batch, not a corpus completeness claim; every denominator member
  (four allowed paths, six forbidden-path re-verification hashes, eleven
  command receipts) is individually accounted for above.

## Finding-To-Governance Learning Disposition

N/A_WITH_REASON: no new repeated or non-obvious governance-control-plane
defect pattern was found. Both repaired defects are downstream-application-
owned TypeScript type-narrowing gaps, already correctly classified as
first-observed by the accepted T3 blocked-return review; no new ADIF entry
is warranted.

## Epistemic Process Block

### Expected Result / Prediction

If both type errors were purely source-local narrowing gaps (as the T3
blocked-return review concluded), fixing them at their exact source
location, without any compiler-option change, should make isolated and
root typecheck/build pass cleanly while leaving all prior 42 passing tests
unaffected.

### Evidence Comparison

Both isolated typechecks now pass with zero output. Root typecheck and
build both pass across all applicable workspace projects. All 42 prior
tests still pass, plus the two new regression tests, for 44/44 total.

### Contradiction Or Gap Disposition

No contradiction found. The T3 blocked-return review's classification (two
source-local, non-strictness-related type gaps) is confirmed correct by
this repair: no `tsconfig.base.json` or any compiler option needed to
change.

### Claim Update

SOT3-APP-T3-R1 closes both outstanding T3 build/typecheck blockers with
source-local fixes and real regression proof, while preserving TypeScript
strictness and all thirteen navigation targets exactly. T4 remains parked
pending independent review.

## git status --short

```
?? docs/reviews/CVF_SOT3_APP_T3_R1_TYPE_NARROWING_AND_BUILD_EVIDENCE_2026-07-17.md
```

## Changed Files

External `SOT-Application` root only (not a Git repository; hash manifest
above is authoritative): two changed, one extended (counted as changed),
one created, matching the Exact Four-Path Before/After Hash Manifest table.
No path outside this set was created, modified, or deleted.

## Command Evidence

See the Command Receipts table in Findings / Position above for the exact
eleven-command sequence, exit codes, and per-command result. The material
excerpts there are the authoritative record; this section confirms the
heading is present per the worker-return packet-shape contract.

Command disposition summary: pre-implementation gate PASS (recorded in the
paired worker return); isolated API/web typecheck and build PASS (after
repair); root typecheck/build/test PASS; focused Vitest PASS; doctor PASS;
external-root Git status N/A with reason (non-Git directory by design).

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. Nothing was staged in the provenance
repository. HEAD remains `4f513f324`. No Git operation beyond read-only
`status`/`rev-parse` was performed in the provenance repository. The
external `SOT-Application` root remains a non-Git directory; no Git
initialization was performed there. No dependency was installed, updated,
or added.

## Claim Boundary

This evidence artifact records source changes, a before/after hash
manifest, real executed compiler and test evidence, and confirmation that
no forbidden path drifted. It does NOT claim any provider/live/network/
browser/public/production behavior, T4 readiness, or any change beyond the
exact four allowed paths.
