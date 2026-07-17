# CVF SOT3-APP-T3 Build And Real Test Evidence

Memory class: governed-worker-evidence

Self-declared worker-return artifact: yes

Status: BLOCKED_WITH_REASON

docType: review_context

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_APP_T3_REPRODUCIBLE_BUILD_AND_REAL_TEST_HARDENING_2026-07-17.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_APP_T3_REPRODUCIBLE_BUILD_AND_REAL_TEST_HARDENING_2026-07-17.md`

executionBaseHead: `41e96d206`

## Purpose

Record the exact 19-path before/after manifest, lockfile identity, Node/pnpm
versions, dependency command receipts, test discovery and pass/fail counts,
build/typecheck results, the production-behavior failure-injection trace, and
the exact classified blocker that prevents `COMPLETE_PENDING_REVIEW`.

## Target / Source

Target: the 19 allowed external source outputs under
`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\SOT-Application`, plus the
declared generated pnpm/build side effects.

Source: the work order's Execution Plan, Fail Conditions, and Verification
Commands; direct reads of the pre-edit external manifests/configs/tests; the
accepted T2 completion review.

## Scope / Methodology

1. Captured `executionBaseHead=41e96d206` on a clean provenance worktree.
2. Ran the ADIF resolver query named by the work order; `NONE_RETURNED`.
3. Ran the mandatory pre-implementation gate
   (`--base 59eec0f02 --head HEAD`); `COMPLIANT`.
4. Confirmed environment state before any edit: `node --version` = `v22.17.0`;
   the global `pnpm` shim resolves to `10.30.3`, which does not match the
   manifest's `packageManager: pnpm@9.15.0`; `corepack pnpm@9.15.0` resolves
   the exact pinned version and was used for every pnpm command in this
   tranche instead of the ambient global `pnpm`. `pnpm-lock.yaml` was
   `ABSENT`; `node_modules` was absent; the external root has no `.git`.
5. Read all 19 allowed paths in full.
6. Repaired exactly three allowed-scope defects (see Semantic Change
   Summary): the root `test` script, the Vitest workspace project list, and
   the `apps/api`/`apps/web` TypeScript configs.
7. Added `tests/failure-injection/application-boundary-behavior.test.ts`.
8. Generated `pnpm-lock.yaml` with `pnpm install --lockfile-only` under
   pinned pnpm 9.15.0, then ran `pnpm install --frozen-lockfile`, which
   reported "Lockfile is up to date, resolution step is skipped" and
   installed 196 packages with zero resolution changes.
9. Ran `pnpm build`, `pnpm typecheck`, `pnpm test`, the exact focused Vitest
   command, and `pnpm doctor`. Diagnosed every failure directly against
   source before any repair or rerun.
10. Computed after-hashes for all 19 allowed paths.

## Findings / Position

### Semantic Change Summary

| # | Path | Change | Reason |
|---|---|---|---|
| 1 | `package.json` | root `scripts.test` changed from `pnpm -r test` to `vitest run --workspace vitest.workspace.ts` | `pnpm -r test` only invokes each package's own local `test` script, none of which point at the root `tests/` directory; it silently never discovered `tests/integration/`, `tests/failure-injection/`, `tests/unit/`, or `tests/e2e/`, which is exactly the failure class the work order names ("a root command that only runs package-local tests while silently omitting root integration tests is a failure") |
| 2 | `vitest.workspace.ts` | replaced the bare glob string `"tests/**/*.test.ts"` with an inline workspace project object (`{ test: { name: "root-tests", root: ".", include: ["tests/**/*.test.ts"] } }`) | the bare glob caused Vitest to try to load each matched `.test.ts` file itself as a project config, producing a hard `Startup Error` ("Vitest failed to access its internal state") on every real run; a bare file-glob string in `defineWorkspace` is not a valid project-selector shape for ad-hoc root-level tests, only for directory/config-file patterns |
| 3 | `apps/api/tsconfig.json` | `rootDir` changed from `"src"` to `"../.."` | `tsc -p`/`--noEmit` enforces that every file in the program (including cross-package `@sot/contracts`, `@sot/domain`, etc. source pulled in via the `paths` mapping in `tsconfig.base.json`) lies under `rootDir`; with `rootDir: "src"`, every workspace-package import failed with `TS6059`, before any application-source defect was even reachable |
| 4 | `apps/web/tsconfig.json` | added `"types": ["vite/client"]` to `compilerOptions` | `import.meta.env` in `src/api/client.ts` requires Vite's ambient `ImportMetaEnv`/`ImportMeta.env` type augmentation, which is normally supplied by a `vite-env.d.ts` reference file; no such file exists in the allowed scope, and adding one was not an allowed path, so the equivalent narrow, config-only fix (`types: ["vite/client"]`) was used instead |
| 5 | `tests/failure-injection/application-boundary-behavior.test.ts` | new file | imports the real `GovernedOutputService` and `GovernedExecutionAdapter` (not a preassigned constant or boolean), constructs a `BLOCK`-routed `ContextPackage`, asserts the thrown `SOT_ROUTE_NOT_ALLOWED` error, and asserts a real local `executionCallCount` variable, incremented only inside the fake execution port, remains `0` |

No other allowed path required a change. `pnpm-lock.yaml` was generated
(new). `packages/application/package.json`, `packages/contracts/package.json`,
`packages/cvf-bindings/package.json`, `packages/domain/package.json`,
`packages/evidence/package.json`, `packages/persistence-sqlite/package.json`,
`packages/workflows/package.json`, `pnpm-workspace.yaml`,
`tsconfig.base.json`, `apps/api/package.json`, `apps/web/package.json`,
`tests/integration/application-boundary-negative.test.ts`, and
`apps/api/src/middleware/application-boundary.middleware.test.ts` are
UNCHANGED; their current hashes below match their T2/T2-R1-accepted state.

### Exact 19-Path Before/After Hash Manifest

| # | Path | Before SHA-256 | After SHA-256 | Disposition |
|---|---|---|---|---|
| 1 | `package.json` | `981144baebb81aa64bc390f19714021a92288f08e182e516f0c0410dd03c0866` | `6bc334406dce42ddbbd85f644493a5cc0348174f6a6679e66e0abb11773e96c2` | CHANGED |
| 2 | `pnpm-lock.yaml` | ABSENT | `400117fa6b728c2b4c4ab70af0f6ece90a2f5e2d1216b32b29a0ffb034106438` | CREATED |
| 3 | `pnpm-workspace.yaml` | `08d75840c97ab0e72d1d9b5b84a17e47a2e06cb159a5fbec5ee0a6a56682dad7` | `08d75840c97ab0e72d1d9b5b84a17e47a2e06cb159a5fbec5ee0a6a56682dad7` | UNCHANGED |
| 4 | `vitest.workspace.ts` | `ccbbdcd8da005f58903265c016d170f07e8efeeb72ce14a8df3db7a685b9dc99` | `08d7f683700b53d82bcd4096edd08ca616785a094b6ad64820ddb4ea0a0de6a5` | CHANGED |
| 5 | `tsconfig.base.json` | `2b6a15abe9d9b89bd971929ad7c34b7a3e871f7548ae352444628784c8078dde` | `2b6a15abe9d9b89bd971929ad7c34b7a3e871f7548ae352444628784c8078dde` | UNCHANGED |
| 6 | `apps/api/package.json` | `bbec25909e85daa6309bae2c3fb628ed6fc300a576f4b8eb6731de59ff0af732` | `bbec25909e85daa6309bae2c3fb628ed6fc300a576f4b8eb6731de59ff0af732` | UNCHANGED |
| 7 | `apps/api/tsconfig.json` | `9bed61ee71eef1e5523a79b9a25b364ae18590d9e5e6eef052d2eb06b0036b6e` | `f9163eb499f3b039fed2c39e5e10e16f2c090256d43a49db58ba28c8063e1d88` | CHANGED |
| 8 | `apps/web/package.json` | `93a2a5d4b8a671dbfe11989c3e70a503aadc8cf6180c83eefa4054ee3a430650` | `93a2a5d4b8a671dbfe11989c3e70a503aadc8cf6180c83eefa4054ee3a430650` | UNCHANGED |
| 9 | `apps/web/tsconfig.json` | `96ec74e0aae2560c2bca868000a5b76a1788beda122410bed7cd64f8d2e77f75` | `4c258fa3843cd85958bf841687c3424aff2121cc743abecbd491ff8efc911286` | CHANGED |
| 10 | `packages/application/package.json` | `fa495c8b8a695b34d915c3cb454fc8d70b69edc2302c1f8ce69b852ccc8e18f1` | `fa495c8b8a695b34d915c3cb454fc8d70b69edc2302c1f8ce69b852ccc8e18f1` | UNCHANGED |
| 11 | `packages/contracts/package.json` | `daea100ceed271fd279b0240ef9500f7bb1918851deb125f42306ff1e72ee88c` | `daea100ceed271fd279b0240ef9500f7bb1918851deb125f42306ff1e72ee88c` | UNCHANGED |
| 12 | `packages/cvf-bindings/package.json` | `470458ba2dc0bc393c30c5e0205c31cfdc0698853cf96d40d96b1d78236d9607` | `470458ba2dc0bc393c30c5e0205c31cfdc0698853cf96d40d96b1d78236d9607` | UNCHANGED |
| 13 | `packages/domain/package.json` | `82563a7c382fe21a90757df708e197ca70da55b193bafd0cc1ece7a30d340996` | `82563a7c382fe21a90757df708e197ca70da55b193bafd0cc1ece7a30d340996` | UNCHANGED |
| 14 | `packages/evidence/package.json` | `023ebd4f1e66adcb77773fe949c597bb5262b5f04bb6ed61da5848a8adc13259` | `023ebd4f1e66adcb77773fe949c597bb5262b5f04bb6ed61da5848a8adc13259` | UNCHANGED |
| 15 | `packages/persistence-sqlite/package.json` | `51914706dffb9bdc6da90d9b89372298a834ad489ee673226b4f101145cf120a` | `51914706dffb9bdc6da90d9b89372298a834ad489ee673226b4f101145cf120a` | UNCHANGED |
| 16 | `packages/workflows/package.json` | `2835de61dd56ff96c823c4deb8f6ce4a2cc416266ec4a9109af440c6ac5bca54` | `2835de61dd56ff96c823c4deb8f6ce4a2cc416266ec4a9109af440c6ac5bca54` | UNCHANGED |
| 17 | `tests/integration/application-boundary-negative.test.ts` | `9faf4440c7cf97b891bdd9dd5f3af9d1939d02a07cf601d7c56d480d0ff22b96` | `9faf4440c7cf97b891bdd9dd5f3af9d1939d02a07cf601d7c56d480d0ff22b96` | UNCHANGED |
| 18 | `apps/api/src/middleware/application-boundary.middleware.test.ts` | `01dc7edab2d936a901bbd6dca396036ddd459e09d11fc61640d54140d281deef` | `01dc7edab2d936a901bbd6dca396036ddd459e09d11fc61640d54140d281deef` | UNCHANGED |
| 19 | `tests/failure-injection/application-boundary-behavior.test.ts` | ABSENT | `3f7139c47e2e03958e946a6d049d20b4d3c59d0572bf8b6b37e5318efc9e3efd` | CREATED |

No path outside this exact 19-path set was created, modified, or deleted.

### Environment And Dependency Evidence

| Field | Value |
|---|---|
| `node --version` | `v22.17.0` |
| ambient global `pnpm --version` | `10.30.3` (does not match manifest; not used for any command in this tranche) |
| pinned `corepack pnpm@9.15.0 --version` | `9.15.0` (used for every pnpm command; matches `packageManager` field) |
| lockfile before | ABSENT |
| lockfile after | present; SHA-256 `400117fa6b728c2b4c4ab70af0f6ece90a2f5e2d1216b32b29a0ffb034106438` |
| `node_modules` before | ABSENT |
| `node_modules` after | present; 196 packages installed by `pnpm install --frozen-lockfile` |
| `DEPENDENCY_RESOLUTION_CALL_COUNT` | 2 (`install --lockfile-only` to generate; `install --frozen-lockfile` to reproduce) |
| frozen-install reproducibility | CONFIRMED: `pnpm install --frozen-lockfile` reported "Lockfile is up to date, resolution step is skipped" |
| package-registry scope | manifest-declared dependencies only; no unrelated package addition; no credential printed |

### Command Receipts

| # | Command | Exit | Result |
|---|---|---|---|
| 1 | `corepack pnpm@9.15.0 install --lockfile-only` | 0 | lockfile generated; 292 packages resolved |
| 2 | `corepack pnpm@9.15.0 install --frozen-lockfile` | 0 | 196 packages installed; lockfile reproducible, zero resolution drift |
| 3 | `corepack pnpm@9.15.0 build` (initial, before tsconfig repair) | 1 | `apps/web` failed: `TS2339` (`ImportMeta.env`), `TS2322` (`NavLink to`) |
| 4 | `corepack pnpm@9.15.0 --filter @sot/api build` (before tsconfig repair) | 2 | `apps/api` failed: 11x `TS6059` `rootDir` violations from `@sot/contracts` cross-package imports |
| 5 | `apps/api/tsconfig.json` repair (`rootDir: "../.."`) | N/A | source change |
| 6 | `corepack pnpm@9.15.0 --filter @sot/api typecheck` (after `rootDir` repair) | 2 | ALL 11 `TS6059` errors resolved; exactly one residual error remains: `src/middleware/error.middleware.ts(6,49): error TS18046: 'error' is of type 'unknown'` |
| 7 | `corepack pnpm@9.15.0 --filter @sot/api build` (after `rootDir` repair) | 2 | same single residual `TS18046` error; build otherwise clean |
| 8 | `apps/web/tsconfig.json` repair (`types: ["vite/client"]`) | N/A | source change |
| 9 | `corepack pnpm@9.15.0 --filter @sot/web typecheck` (after `vite/client` types repair) | 2 | `TS2339 ImportMeta.env` error resolved; exactly one residual error remains: `src/layouts/application-layout.tsx(27,31): error TS2322: Type 'string \| undefined' is not assignable to type 'To'` |
| 10 | `corepack pnpm@9.15.0 typecheck` (root, both repairs applied) | 2 | fails at `apps/web` with the single residual `TS2322`; `pnpm -r` stops at the first failing package in its traversal order |
| 11 | `corepack pnpm@9.15.0 build` (root, both repairs applied) | 1 | fails at `apps/web` with the same single residual `TS2322` |
| 12 | `corepack pnpm@9.15.0 test` (after `vitest.workspace.ts` repair) | 0 | 29 test files, 42 tests, ALL PASS; `ROOT_TEST_DISCOVERY_COUNT=42` |
| 13 | `corepack pnpm@9.15.0 exec vitest run --workspace vitest.workspace.ts tests/integration/application-boundary-negative.test.ts apps/api/src/middleware/application-boundary.middleware.test.ts tests/failure-injection/application-boundary-behavior.test.ts` | 0 | 3 test files, 16 tests, ALL PASS |
| 14 | `corepack pnpm@9.15.0 doctor` (via `node_modules/.bin/tsx scripts/doctor.ts` directly, since the pnpm-wrapped invocation's stdout was not captured by the shell pipe used) | 0 | `healthy: true`; all 10 CVF binding/manifest/policy files exist and are valid JSON |

### Test Discovery And Pass/Fail Counts

- `ROOT_TEST_DISCOVERY_COUNT`: 42 (29 test files) via `pnpm test`, including:
  - the T2 integration test `tests/integration/application-boundary-negative.test.ts` (8 tests);
  - the T2 API admission test `apps/api/src/middleware/application-boundary.middleware.test.ts` (7 tests, run once under the `root-tests` project glob during the full `pnpm test` pass, and once under the `@sot/api` package project in the same pass, both green);
  - the new `tests/failure-injection/application-boundary-behavior.test.ts` (1 test);
  - all 18 pre-existing root `tests/unit/`, `tests/integration/`, `tests/e2e/`, and `tests/failure-injection/` files (each still legacy tautological constant-assertion tests except the one added by this tranche, but all pass as written).
- `PRODUCTION_BEHAVIOR_FAILURE_TEST_COUNT`: 1. The new test in `tests/failure-injection/application-boundary-behavior.test.ts` imports `GovernedOutputService` (real production class, not a mock of the service itself) and `GovernedExecutionAdapter`, constructs a `route_decision: "BLOCK"` context, and asserts both the exact thrown error token and a real local counter (`executionCallCount`, incremented only inside the fake leaf execution port) remain `0`. This is not a preassigned boolean or constant token; the assertion values are produced by executing the real `GovernedOutputService.create` control flow.

### Build And Typecheck Result

`pnpm build` and `pnpm typecheck` both fail at the `apps/web` package (the
first failing package in `pnpm -r`'s traversal order). After the two
in-scope config repairs above, exactly two application-source defects remain
unresolved system-wide, both outside the 19-path Allowed Scope:

1. `apps/api/src/middleware/error.middleware.ts(6,49)`: `TS18046: 'error' is
   of type 'unknown'`. `apps/api/src/middleware/error.middleware.ts` is not
   one of the 19 allowed paths (only its test companion,
   `apps/api/src/middleware/application-boundary.middleware.test.ts`, is
   allowed).
2. `apps/web/src/layouts/application-layout.tsx(27,31)`: `TS2322: Type
   'string | undefined' is not assignable to type 'To'`. This file is not
   one of the 19 allowed paths at all.

No allowed-scope config or manifest change can resolve either error: both
are genuine type-narrowing defects inside application source logic, not
compiler configuration gaps. `TS18046` requires either a type guard/cast
inside `error.middleware.ts` (a source edit) or a `tsconfig` compiler-option
change (`useUnknownInCatchVariables: false`) that would weaken strictness
workspace-wide, which was not attempted because it changes a public
compiler contract beyond a narrow, justified correction and was not named as
an allowed remedy by the work order. `TS2322` requires a source-level
narrowing fix inside `application-layout.tsx` (e.g., a fallback string or an
`undefined`-safe `to` prop), which is entirely outside Allowed Scope.

## Risk / Corrective Action

| Risk | Resolution |
|---|---|
| `apps/api` build/typecheck blocked by an out-of-scope `TS18046` in `error.middleware.ts` | requires a fresh, narrowly-scoped work order authorizing an edit to that exact file (or a workspace-wide `tsconfig.base.json` strictness change, which is a larger decision the operator/dispatcher should make explicitly, not this worker) |
| `apps/web` build/typecheck blocked by an out-of-scope `TS2322` in `application-layout.tsx` | requires a fresh, narrowly-scoped work order authorizing an edit to that exact file |
| `pnpm -r build`/`pnpm -r typecheck` only report the first failing package | this is inherent pnpm recursive-run behavior (`ERR_PNPM_RECURSIVE_RUN_FIRST_FAIL`), not a defect this tranche introduced; both failing packages were independently isolated and fully diagnosed with `--filter` to avoid a false "only one blocker exists" reading |
| ambient global `pnpm` (10.30.3) does not match the declared `packageManager` (9.15.0) | used `corepack pnpm@9.15.0` for every command in this tranche instead; this is an environment observation, not a manifest defect, since the manifest's `packageManager` field is itself the correct, already-accurate declaration |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_equivalence_claim_evidence.py`; `governance/compat/check_worker_return_quality_gate.py` |
| literalTokensReviewed | Status: BLOCKED_WITH_REASON; section name: Purpose; section name: Target / Source; section name: Scope / Methodology; section name: Findings / Position; section name: Risk / Corrective Action; section name: Claim Boundary |
| gateRunPurpose | confirm this evidence artifact satisfies structural completeness for a `docs/reviews/` companion before the paired worker return links it |
| claimBoundary | checker conformance does not substitute for a resolved build/typecheck; this artifact explicitly records the two unresolved out-of-scope blockers |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | delegated implementation worker |
| Provider or surface | operator sibling source plus private provenance workspace; package-registry access via corepack/pnpm for manifest-declared dependency resolution only |
| Session or invocation | SOT3-APP-T3, 2026-07-17 |
| Working directory | external `SOT-Application` root and private provenance root |
| Command or tool surface | source edits, SHA-256 hashing, `pnpm install`/`build`/`typecheck`/`test`/`doctor` via pinned `corepack pnpm@9.15.0`, `pnpm exec vitest run`, read-only `git status` in both roots |
| Target paths | 19 allowed external source outputs |
| Allowed scope source | work order Allowed Scope and paired GC-018 |
| Before status evidence | four pre-existing files changed, eleven unchanged, two created (lockfile plus new test); `node_modules` and lockfile absent before |
| After status evidence | four external files changed, eleven unchanged, two created; `node_modules` and lockfile present after; build/typecheck blocked by two out-of-scope defects |
| Diff evidence | SHA-256 before/after manifest above; provenance `git diff --name-status` reports this file as untracked/new, not a tracked modification |
| Approval boundary | bounded deterministic T3 dependency/build/test implementation evidence only |
| Claim boundary | no provider/live/public/T4/production claim; build/typecheck are BLOCKED, not PASS; test/doctor are PASS |
| Agent type | worker |
| Invocation ID | `sot3-app-t3-worker-execution-2026-07-17` |
| Expected manifest | 19 allowed external paths |
| Actual changed set | four changed, eleven unchanged, two created (see hash manifest above) |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename occurred |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | local deterministic dependency resolution, test execution, and partial build/typecheck evidence in the sibling source |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: real executed dependency install, test, and doctor commands; build/typecheck are BOUNDED_BLOCKED, not claimed as passing |
| receiptEvidence | CVF_RECEIPT_PRESENT: real command exit codes, lockfile hash, and test-run output for install/test/doctor; BLOCKED receipt for build/typecheck |
| actionEvidence | ACTION_EVIDENCE_PRESENT: four source files changed, two files created, eleven confirmed unchanged; 196 real packages installed; 42 real tests executed and passed |
| invocationBoundary | pinned `corepack pnpm@9.15.0` commands and direct `tsx` invocation only; no provider, network beyond package-registry resolution, browser, or production action |
| interceptionBoundary | application/API call-path guards exercised by real executed tests; no universal agent interception claim |
| claimLanguage | bounded downstream reproducible-dependency and real-test evidence; build/typecheck explicitly not claimed passing |
| forbiddenExpansion | provider, network beyond manifest-declared package resolution, live, browser, public, production, T4, Git initialization, credential printing, or unlisted path |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | T2 bounded closure -> T3 reproducibility hardening -> independent review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_work_order_dispatch_quality.py` |
| Owner surface | SOT3-APP roadmap and this T3 evidence artifact |
| Disposition | ADAPT_CONTRACT; no CVF Core import performed |
| Claim boundary | bounded sibling implementation evidence only; no public/product/runtime-wide claim |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- Reason: this evidence artifact performs no intake refresh and no
  source-backed reassessment of the accepted predecessor corpus; it records
  the T3 reproducible-build tranche's command receipts and hash manifest
  only.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - this artifact does not claim a fresh full corpus rescan; its
  completeness denominator is exactly the 19 allowed external paths, all
  individually accounted for in the hash manifest above.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| the root `vitest.workspace.ts`'s bare `"tests/**/*.test.ts"` glob string is not a valid ad-hoc project selector and crashes every real Vitest invocation with a `Startup Error` | RULE_GAP | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | downstream-application-owned Vitest workspace-configuration gap; repaired inside this tranche's Allowed Scope | handled in this tranche |
| `apps/api/tsconfig.json`'s `rootDir: "src"` combined with cross-package `@sot/*` source imports produces eleven `TS6059` errors the moment `tsc` is actually invoked | RULE_GAP | DOCUMENTATION_ONLY_LEARNING | N/A_WITH_REASON | downstream-application-owned TypeScript project-reference gap; repaired inside this tranche's Allowed Scope | handled in this tranche |

## Epistemic Process Block

### Expected Result / Prediction

If T3 correctly established reproducible dependency resolution, the
generated lockfile would reproduce exactly on a frozen reinstall, and real
root test discovery would surface every T2 test plus a new
non-tautological production-behavior test.

### Evidence Comparison

The frozen install reported zero resolution drift. Root test discovery went
from zero real execution to 42 passing tests across 29 files after the
in-scope script and workspace-config repairs.

### Contradiction Or Gap Disposition

No contradiction found. Build/typecheck exposed genuine defects exactly as
expected once real compilation was attempted for the first time; eleven
were resolved in-scope, two remain out-of-scope and are recorded as the
classified blocker in Findings / Position.

### Claim Update

Dependency reproducibility and real test execution are proven with
executed command receipts. Build/typecheck remain BLOCKED pending a
follow-up tranche with expanded scope covering the two identified files.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private sibling application evidence; no public-sync authorization
or public-safe artifact set exists.

## git status --short

```
?? docs/reviews/CVF_SOT3_APP_T3_BUILD_AND_REAL_TEST_EVIDENCE_2026-07-17.md
```

## Changed Files

External `SOT-Application` root only (not a Git repository; hash manifest
above is authoritative): four changed, eleven unchanged, two created,
matching the Exact 19-Path Before/After Hash Manifest table. No path outside
this set was created, modified, or deleted. Generated side effects
(`node_modules`, `pnpm-lock.yaml` is a tracked allowed output, pnpm store
cache) are disposable and not otherwise added to provenance.

## Command Evidence

See the Command Receipts table in Findings / Position above for the exact
14-command sequence, exit codes, and per-command result classification. The
material excerpts there are the authoritative record; this section confirms
the heading is present per the worker-return packet-shape contract.

Command disposition summary: pre-implementation gate PASS (recorded in the
paired worker return); dependency install PASS (reproducible, zero
resolution drift); `pnpm test`/focused Vitest/`pnpm doctor` PASS;
`pnpm build`/`pnpm typecheck` BLOCKED (two out-of-scope application-source
defects); external-root Git status N/A with reason (non-Git directory by
design).

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. Nothing was staged in the provenance
repository. HEAD remains `41e96d206`. No Git operation beyond read-only
`status`/`rev-parse` was performed in the provenance repository. The
external `SOT-Application` root remains a non-Git directory; no Git
initialization was performed there.

## Claim Boundary

This evidence artifact records source changes, a before/after hash
manifest, real dependency resolution/install evidence, real executed test
results, and command attempts against the external `SOT-Application` root.
It does NOT claim a passing `pnpm build` or `pnpm typecheck` result; both
are explicitly BLOCKED by exactly two application-source defects outside
the 19-path Allowed Scope. It does not claim any provider/live/network
beyond manifest-declared package resolution/browser/public/production
behavior.
