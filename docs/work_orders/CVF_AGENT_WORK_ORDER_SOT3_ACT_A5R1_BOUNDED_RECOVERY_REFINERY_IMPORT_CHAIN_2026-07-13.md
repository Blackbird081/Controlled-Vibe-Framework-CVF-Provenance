# CVF Agent Work Order - SOT3 Activation A5 Bounded Recovery - Refinery Import Chain Repair

Memory class: governed-worker-dispatch

Status: DISPATCH_READY

docType: work_order

Batch ID: SOT3-ACT-A5R1

## Dispatch Prompt Envelope

Role: delegated SOT3-ACT-A5 bounded recovery implementation and live-proof
worker.

Canonical packet: this work order and its paired GC-018 baseline
`docs/baselines/CVF_GC018_SOT3_ACT_A5R1_BOUNDED_RECOVERY_REFINERY_IMPORT_CHAIN_2026-07-13.md`.

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_AT_START.

Current-time notes: use the actual clean post-dispatch HEAD, current source,
the actual execution date, and operator-local key bootstrap. Fresh A5R1
execution artifacts use `2026-07-14`; retained predecessor artifacts keep
their original `2026-07-13` names.

Do-not-misread notes: this is a bounded recovery repair for the diagnosed A5
runtime integration defect, not a fresh A5 tranche, not A5 closure, not final
`LIVE_GOVERNANCE_PROVEN_BOUNDED`, not public-sync, and not production or scale
work.

Required first actions: read startup front doors, guard orientation, literal
gotchas, this packet, the paired baseline, the blocked A5 worker return, the
original A5 work order, ADIF-0030, ADIF-0031, every source path in the Source
Verification Block, and every checker named in the Checker Source Read-Ahead
Block. Capture a clean executionBaseHead before edits and run pre-
implementation with a real range.

Return contract: implement the exact manifest, keep the retained blocked A5
evidence byte-unchanged, run local Refinery and web-package checks before any
live call, permit exactly one post-repair canonical live invocation only after
every local check is green and a concrete result-changing repair is recorded,
create the worker return, run all required gates, leave changes uncommitted,
and return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`.

Date: 2026-07-13

dispatchBaseHead: `57f1a9fda`

executionBaseHead: `WORKER_MUST_CAPTURE_AT_START`

closureBaseHead: `REVIEWER_TO_SET`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: delegated implementation and bounded live-proof worker

Reviewer/closer: Codex reviewer/closer

Worker return path: `docs/reviews/CVF_SOT3_ACT_A5R1_BOUNDED_RECOVERY_REFINERY_IMPORT_CHAIN_WORKER_RETURN_2026-07-14.md`

## Purpose

Repair the diagnosed Refinery package-consumption defect that made the
canonical release bundle's live E2E stage return HTTP 500 HTML instead of
JSON, prove both production build and Next.js development-bundler
compatibility for the repaired import chain, add structured release-level
diagnostics for failed live E2E stages, and produce one fresh, correlated
post-repair canonical release result for independent review.

## Authority Chain

Operator A0-A5 authorization -> activation roadmap A5 release ->
blocked A5 material commit `f038bcb81` (retained diagnosed evidence) ->
session-sync commit `57f1a9fda` -> this recovery GC-018 baseline -> this work
order -> no-commit worker return -> Codex reviewer/closer decision. Runtime
source and canonical contracts override chat, provider-local memory, and the
blocked return's own prose (which must still be independently re-verified,
not merely trusted).

## Agent Roles

The delegated worker owns implementation, tests, the one planned post-repair
canonical live run, evidence, diagnostics, and the no-commit return. Codex
owns review, bounded repair, closure conversion, commit, roadmap transition,
and session synchronization. The operator retains final decision authority.

## Required First Reads

1. `CVF_SESSION_MEMORY.md`, active session state registry, and active handoff;
2. `docs/reference/guard_orientation/README.md` and literal gotchas;
3. paired GC-018 baseline `docs/baselines/CVF_GC018_SOT3_ACT_A5R1_BOUNDED_RECOVERY_REFINERY_IMPORT_CHAIN_2026-07-13.md`;
4. the blocked A5 worker return `docs/reviews/CVF_SOT3_ACT_A5_CANONICAL_RELEASE_PROOF_WORKER_RETURN_2026-07-13.md` (read fully; independently re-verify its diagnosis against current source, do not merely trust its prose);
5. the original A5 work order `docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A5_CANONICAL_RELEASE_PROOF_2026-07-13.md` (context for what A5 already wired; this recovery does not redo it);
6. `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0030.md`;
7. `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0031.md`;
8. current Refinery, web-package, Next.js config, and release-bundle sources
   named below.

## Pre-Flight Checks

- clean worktree and captured executionBaseHead;
- exact manifest confirmed and the three retained blocked-A5 evidence paths
  plus the blocked worker return are unchanged before and after;
- pre-implementation autorun PASS on a real range;
- local key bootstrap checked without printing values;
- re-run every Source Verification search below against current source before
  editing, since source may have moved since this packet was authored.

## Write Ownership

The worker may write only the Work-Order Fulfillment Manifest paths below.
The three retained blocked-A5 evidence JSON files, the blocked A5 worker
return, all A1-A4 runtime source and evidence, roadmaps, baselines, other work
orders, session state, handoffs, public-sync, and all other runtime paths are
read-only to the worker.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| A5 blocked-with-diagnosis predecessor | `docs/reviews/CVF_SOT3_ACT_A5_CANONICAL_RELEASE_PROOF_WORKER_RETURN_2026-07-13.md`; `Status: BLOCKED_WITH_REASON`; material commit `f038bcb81` | recovery packet must not overwrite this evidence | ACCEPT |
| session continuity | session-sync commit `57f1a9fda` names bounded A5 recovery as the next allowed move | recovery packet dispatches from this clean HEAD | ACCEPT |
| A4 closure (unaffected) | `docs/reviews/CVF_SOT3_ACT_A4_FAILURE_AND_RECOVERY_BOUNDARY_PROOF_COMPLETION_2026-07-13.md`; `Status: CLOSED_PASS_BOUNDED` | must remain unmodified | ACCEPT |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Refinery re-exports from a `./deps.js` specifier pointing at TypeScript source | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_REFINERY/src/index.ts` | lines 1-2 | `Clock`, `IdFactory`, `DeterministicClock`, `SequentialIdFactory` | Refinery package entrypoint | ACCEPT |
| the referenced `deps.ts` file exists (specifier is a `.js`-extension convention over real `.ts` source, per Node16/bundler `moduleResolution`) | EXISTS | `EXTENSIONS/CVF_REFINERY/src/deps.ts` | full file | `DeterministicClock`, `SequentialIdFactory` | Refinery deterministic-services module | ACCEPT |
| Refinery package maps `main`/`types`/`exports` directly at TypeScript source, no build/dist step is consumed by the web app | EXISTS | `EXTENSIONS/CVF_REFINERY/package.json` | `main`, `types`, `exports` fields | `main` | Refinery package manifest | ACCEPT |
| Refinery `tsconfig.json` uses `moduleResolution: "bundler"` | EXISTS | `EXTENSIONS/CVF_REFINERY/tsconfig.json` | `compilerOptions.moduleResolution` | `moduleResolution` | Refinery TypeScript config | ACCEPT |
| Truth Kernel and Truth Flow use the identical `./deps.js`-to-`deps.ts` and `main`-at-source pattern as Refinery | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_TRUTH_KERNEL/src/index.ts`; `EXTENSIONS/CVF_TRUTH_FLOW/src/index.ts`; `EXTENSIONS/CVF_TRUTH_KERNEL/package.json`; `EXTENSIONS/CVF_TRUTH_FLOW/package.json` | lines 1-2 of each `index.ts`; `main`/`exports` of both package manifests | `DeterministicClock`, `SequentialIdFactory` | Truth Kernel and Truth Flow package entrypoints | ACCEPT |
| the web app links all three sibling packages through `file:` dependencies | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package-lock.json` | dependency block; matching `node_modules/cvf-*` lock entries with `link: true` | `cvf-refinery` | web package dependency and lock manifests | ACCEPT |
| the execute route's knowledge-context chain imports directly from `cvf-refinery` | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route-knowledge-context.ts` | line 37 | `DeterministicClock`, `SequentialIdFactory` | execute route knowledge-context helper | ACCEPT |
| the SOT3 product adapter also imports Refinery, Truth Kernel, and Truth Flow symbols directly | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-knowledge-adapter.ts` | lines 14-20 | `RefineryEngine`, `TruthKernel`, `DistributionEngine` | SOT3 product adapter | ACCEPT |
| Next.js config declares sibling-package transpilation, Turbopack extension ordering, and webpack `.js` extension aliases, including `cvf-refinery` | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/next.config.ts` | `transpilePackages` array; `turbopack.resolveExtensions`; `webpack(config)` `resolve.extensionAlias` | `transpilePackages` | Next.js configuration | ACCEPT |
| the existing Next.js resolver declaration prevents the observed Refinery failure under `next dev` | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/next.config.ts`; `docs/reviews/CVF_SOT3_ACT_A5_CANONICAL_RELEASE_PROOF_WORKER_RETURN_2026-07-13.md` | current resolver configuration; diagnosed E2E failure section | `turbopack.resolveExtensions` | Next.js development bundling boundary | REJECT |
| web package TypeScript config also uses `moduleResolution: "bundler"` | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tsconfig.json` | `compilerOptions.moduleResolution` | `moduleResolution` | web package TypeScript config | ACCEPT |
| web package development script invokes `next dev` without an explicit bundler while production build explicitly selects webpack | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | `scripts.dev`; `scripts.build` | `dev` | web package scripts | ACCEPT |
| installed Next.js development CLI supports explicit `--webpack` and `--turbopack` selectors | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/node_modules/next/dist/bin/next` | `next dev --help` option registration | `--webpack` | installed Next.js CLI | ACCEPT |
| `check_e2e` currently has no structured per-stage diagnostic; failure detail is a flat `list[str]` of raw log lines | RUNTIME_BEHAVIOR | `scripts/run_cvf_release_gate_bundle.py` | lines 254-290; lines 107-112 | `check_e2e`, `CheckResult` | release gate bundle | REJECT |
| the release bundle's live diagnostic vocabulary already exists and is reused elsewhere in this lineage | EXISTS | `docs/reference/archive/CVF_LIVE_RUN_DIAGNOSTIC_STANDARD_2026-05-24.md`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/execution-diagnostics.ts` | `ExecutionDiagnosticStage`, `ExecutionDiagnosticUserAction`, `safeMessage` field shapes | `ExecutionDiagnosticStage` | execution diagnostic contract | ACCEPT |
| the retained blocked A5 evidence paths are the exact three JSON files plus the worker return | EXISTS | `docs/reviews/evidence/sot3-act-a5-release-gate-result-2026-07-13.json`; `docs/reviews/evidence/sot3-act-a5-release-gate-manifest-2026-07-13.json`; `docs/reviews/evidence/sot3-act-a5-release-sot3-diagnostic-2026-07-13.json`; `docs/reviews/CVF_SOT3_ACT_A5_CANONICAL_RELEASE_PROOF_WORKER_RETURN_2026-07-13.md` | full files at material commit `f038bcb81` | `gate_result`, `evidence`, `diagnostic`, `Status` | blocked A5 evidence set | ACCEPT |
| release bundle CLI has no existing flag for a structured E2E diagnostic output path | RUNTIME_BEHAVIOR | `scripts/run_cvf_release_gate_bundle.py` | lines 515-544 | `add_argument` | release gate bundle CLI | REJECT |

Rejected-row explanations: the Next.js runtime-effect row is REJECT because
the existing resolver declaration does not prevent the diagnosed failure for
the Refinery-triggered chain and must be corrected or supplemented, not
assumed sufficient. The declaration itself is ACCEPTed as a current source
fact. The `check_e2e`/`CheckResult` row is
REJECT because no `stage`/`class`/`retryable`/`userAction`/`safeMessage`
fields exist for a failed E2E stage today. The release-bundle-CLI row is
REJECT because the `--e2e-diagnostic-output` flag this recovery requires does
not exist yet and must be added.

Corrected source facts: the diagnosed defect is not that Refinery lacks
`.js`-extension resolution support in this repository's Next.js
configuration in principle -- Truth Kernel and Truth Flow use the identical
pattern and are already covered by the same `transpilePackages` array. The
recovery worker must determine, from live source and a reproduction, exactly
why the Refinery-triggered chain specifically fails where the Kernel/Flow
chain does not (candidates include, but are not limited to: Turbopack
resolution-order or caching behavior specific to being the first package in
an import chain to hit the `.js`-to-`.ts` alias, a stale `.next`/Turbopack
cache, or a Refinery-specific export/specifier difference not shared by
Kernel/Flow) rather than assuming the fix is identical to an existing
Kernel/Flow pattern that already appears in configuration but did not prevent
the failure.

## New Doc-Only Fields

| Field | Purpose | Runtime status |
|---|---|---|
| `e2eDiagnostic` | structured secret-safe diagnostic object for a failed live E2E `check_e2e` stage, mirroring the existing execution-diagnostic vocabulary (`stage`, `class`, `retryable`, `userAction`, `safeMessage`, optional `provider`/`model`/`httpStatus`/`latencyMs`/`traceOrReceipt`) | DOC_ONLY_NEW |
| `repairAction` | one-sentence record of the concrete, result-changing repair made before the one permitted post-repair canonical live rerun | DOC_ONLY_NEW |
| `refineryImportChainRepaired` | boolean recovery-evidence field confirming the diagnosed defect no longer reproduces | DOC_ONLY_NEW |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id SOT3-ACT-A5R1 --title "SOT3 Activation A5 Bounded Recovery - Refinery Import Chain Repair" --date 2026-07-13 --base 57f1a9fda --commit-mode WORKER_MUST_NOT_COMMIT --dependency "A5 blocked f038bcb81 BLOCKED_WITH_REASON_DIAGNOSED" --stdout --include-worker-return-skeleton` |
| generatedProfile | runtime-provider-live plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with the verified blocked-A5 dependency evidence, current Refinery/web/Next.js source facts, the exact four-file repair-surface allowance, the 19-row-unaffected/unchanged-scope boundary, structured diagnostic requirement, call budget, and claim boundary |
| checkerReadAheadConfirmation | dispatch quality, handoff, worker-return, machine-closure, finding-learning, file-size, ADIF-disclosure, checker-read-ahead, markdown-structural-completeness, dispatch-scaffold-provenance, dispatch-prompt-envelope, and autorun checker sources read |
| docOnlyNewFields | declared in New Doc-Only Fields |
| claimBoundary | dispatch authoring provenance only; no recovery execution or final claim at dispatch |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`SOT3 runtime dependency resolution bounded recovery dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "SOT3 runtime dependency resolution bounded recovery dispatch" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector "refinery package consumption next.js turbopack module resolution" --risk-ceiling HIGH --max-results 30 --json`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | exact query above |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | worker must still read ADIF-0030 and ADIF-0031 as explicit required reads; both remain binding for this recovery's live-call and writable-manifest discipline even though the semantic resolver query returned no matching entries |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/run_agent_autorun_workflow_gate.py` |
| literalTokensReviewed | Status; exact manifest; Source Verification dispositions; Required Artifact Manifest; Agent Handoff Contract Control Block; Reviewer Closure Conversion; Public Export Disposition; Decision/Baseline/Proposed Tranche heading triplet; Dispatch Prompt Envelope read-first line limit |
| gateRunPurpose | confirmation and evidence after source-backed authoring; not first discovery |
| claimBoundary | gate PASS proves packet shape only, not a working repair or a live SOT3/E2E result |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| A5R1 packet paths | `Test-Path` on all Work-Order Fulfillment Manifest evidence paths returned false before authoring | ACCEPT |
| A5R1 artifact token | `rg -n "SOT3-ACT-A5R1|A5 Bounded Recovery"` against `docs` and `CVF_SESSION` returned no prior artifact before this packet was authored | ACCEPT |
| retained blocked evidence | the three `sot3-act-a5-*-2026-07-13.json` paths and the A5 worker return exist and are read-only inputs; recovery evidence must use new dated/named paths, never overwrite these | ACCEPT |
| collision decision | create only A5R1-specific evidence and return paths; never touch the retained blocked-A5 evidence set | ACCEPT |

## Design Control Gate

### Required implementation design

1. Reproduce the diagnosed failure locally first (the current default
   development-server compilation of the execute route's Refinery import chain) before
   changing anything, to confirm the exact failing resolution step.
2. Select the smallest correct repair to the Refinery package-consumption
   boundary. Candidate repair surfaces, in order of preference (smallest
   blast radius first): (a) explicitly select the already-supported webpack
   development bundler in the web package `dev` script if reproduction proves
   the existing webpack `extensionAlias` resolves the route while Turbopack
   does not; (b) a targeted Next.js resolver correction if Turbopack can be
   made compatible without weakening package semantics; (c) a
   Refinery-specific `package.json` export-map correction only if direct
   reproduction proves that package metadata is the fault. Do not prescribe
   explicit `.ts` imports or any source-specifier rewrite unless independent
   typecheck, emitted-JavaScript ESM execution, package tests, and both web
   bundlers prove the resulting package contract remains valid.
3. Do not rewrite Refinery's public export surface, add new exports, or
   change any consumer's import statements beyond what the proven repair
   requires.
4. Preserve Refinery's own `tsc --noEmit`, `tsc` build, and `vitest run`
   green and unweakened; these are the package's own contract and must not
   regress.
5. Add one focused Playwright regression that starts the real `next dev`
   server through `playwright.config.mock.ts`, posts a deliberately invalid
   request to `/api/execute`, and proves the route compiles through the
   Refinery import chain by receiving a JSON 4xx response rather than the
   prior HTML 500 compilation page. This regression must use zero provider
   calls. It must record whether webpack or Turbopack is the selected
   development bundler. A Vitest-only route import is insufficient because it
   does not exercise the failed Next.js development-server path.
6. Prove production build compatibility separately (`npm run build` in the
   web package) so the repair does not regress the existing production
   bundling path while fixing the development-bundler path.
7. Add a structured `e2eDiagnostic` to `check_e2e`'s failure path in
   `scripts/run_cvf_release_gate_bundle.py`, reusing the existing diagnostic
   vocabulary shape (stage/class/retryable/userAction/safeMessage, optional
   provider/model/httpStatus/latencyMs/traceOrReceipt), and wire a new
   `--e2e-diagnostic-output` CLI flag (mirroring the existing
   `--sot3-diagnostic-output` pattern at lines 532-536) that persists this
   diagnostic to a caller-provided JSON path on failure. On success, persist
   `null` for symmetry with the existing SOT3 diagnostic behavior. Never
   persist raw provider body, raw HTML response body beyond a short safe
   excerpt classification, API keys, or bearer headers.
8. Do not modify `check_sot3`, the SOT3 A5 adapter, the A4 runner, or any
   A1-A4 source; this recovery's scope is the E2E/Refinery-chain defect and
   its diagnostic gap only.

### Non-goals

No CVF Truth Kernel or Truth Flow source mutation, no A1-A4 evidence
overwrite, no rewrite of Refinery's export surface beyond the proven minimal
fix, no prompt/model tuning, no public-sync, no release deployment, and no
generalized provider wrapper.

## Execution Plan

1. Capture clean `executionBaseHead` and run pre-implementation.
2. Reproduce the diagnosed failure locally; record the exact reproduction
   command and observed error.
3. Implement the smallest correct Refinery-consumption repair per the Design
   Control Gate's preference order; re-run Refinery's own
   `tsc --noEmit`/`tsc`/`vitest run` after each change.
4. Add the focused regression proving `/api/execute` compiles and responds
   through the Refinery import chain under dev-server mode.
5. Run the web package's production build and TypeScript check.
6. Implement the structured `e2eDiagnostic` and `--e2e-diagnostic-output`
   wiring in the release bundle; add or extend release-bundle unit coverage
   if an existing test file in scope already covers `check_e2e`/CLI wiring,
   otherwise add assertions to the new regression file only -- do not create
   a second new Python test file beyond what the manifest allows.
7. Run `--dry-run --json` and confirm structural shape is unchanged (SOT3
   still SKIP, overall still cannot claim PASS).
8. Confirm operator key bootstrap without printing values.
9. Invoke the canonical release command exactly once, using fresh,
   A5R1-specific dated evidence paths (never the retained blocked-A5 paths):

   ```
   python scripts/run_cvf_release_gate_bundle.py --json --output docs/reviews/evidence/sot3-act-a5r1-recovery-release-gate-result-2026-07-14.json --manifest-output docs/reviews/evidence/sot3-act-a5r1-recovery-release-gate-manifest-2026-07-14.json --sot3-diagnostic-output docs/reviews/evidence/sot3-act-a5r1-recovery-release-sot3-diagnostic-2026-07-14.json --e2e-diagnostic-output docs/reviews/evidence/sot3-act-a5r1-recovery-release-e2e-diagnostic-2026-07-14.json
   ```

10. On failure, preserve result and diagnostics, classify the stage, and
    stop. Do not rerun unless a further concrete repair changes the expected
    result, and record that repair explicitly before any second attempt.
11. Confirm the three retained blocked-A5 evidence paths and the blocked
    worker return remain byte-identical to their state at dispatch.
12. Write the no-commit worker return, run worker-return gates and steward
    preflight, and leave HEAD unchanged.

## Work-Order Fulfillment Manifest

| Artifact | Required worker action |
|---|---|
| Refinery package-consumption boundary (exact path determined by the proven smallest repair: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/next.config.ts`, `EXTENSIONS/CVF_REFINERY/package.json`, and/or `EXTENSIONS/CVF_REFINERY/src/index.ts`) | apply the smallest correct repair per the Design Control Gate preference order; do not touch paths not implicated by the proven defect |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/refinery-import-chain-dev.spec.ts` | new zero-provider Playwright regression proving `/api/execute` compiles through the Refinery import chain under the explicitly selected real `next dev` bundler and returns JSON rather than an HTML compilation error |
| `scripts/run_cvf_release_gate_bundle.py` | add structured `e2eDiagnostic` on `check_e2e` failure and a new `--e2e-diagnostic-output` CLI flag; no other behavior change |
| `docs/reviews/evidence/sot3-act-a5r1-recovery-release-gate-result-2026-07-14.json` | fresh post-repair canonical release JSON |
| `docs/reviews/evidence/sot3-act-a5r1-recovery-release-gate-manifest-2026-07-14.json` | hash manifest over the A5R1 recovery evidence set |
| `docs/reviews/evidence/sot3-act-a5r1-recovery-release-sot3-diagnostic-2026-07-14.json` | fresh SOT3 diagnostic from the post-repair run |
| `docs/reviews/evidence/sot3-act-a5r1-recovery-release-e2e-diagnostic-2026-07-14.json` | new structured E2E diagnostic (present as `null` on success) |
| `docs/reviews/CVF_SOT3_ACT_A5R1_BOUNDED_RECOVERY_REFINERY_IMPORT_CHAIN_WORKER_RETURN_2026-07-14.md` | checker-safe no-commit worker return |

If the proven repair requires touching a source path not selected in the
first manifest row, the worker may edit only
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`,
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/next.config.ts`,
`EXTENSIONS/CVF_REFINERY/package.json`, and
`EXTENSIONS/CVF_REFINERY/src/index.ts` -- no other Refinery or web-package
source file. If the required correction needs any path outside these four
plus the explicitly named artifacts above,
return `BLOCKED_WITH_REASON` with source evidence; do not repeat the A4
manifest-omission defect (ADIF-0031) by improvising an out-of-manifest edit.

## Evidence Requirements

Evidence must record the exact reproduction command and observed failure
before repair, the exact repair applied and why it is the smallest correct
fix, Refinery's own typecheck/build/test results after repair, the web
package's production build and typecheck results, the new regression's
result, the structured E2E diagnostic shape, the one post-repair canonical
live invocation's full per-check result table (mirroring the blocked
return's own table format), SOT3 admission fields for the new run,
provider-call accounting for the new run, evidence hashes, secret-safety
scan results, exact changed set, unchanged worker HEAD, and explicit
confirmation the three retained blocked-A5 evidence paths plus the blocked
worker return are byte-unchanged.

## Acceptance Criteria

- the diagnosed Refinery-to-Next.js-development-bundler import defect no
  longer reproduces, proven by the new focused regression;
- Refinery's own ESM contract, `tsc --noEmit`, `tsc` build, and `vitest run`
  remain green and unweakened;
- the web package's production build and TypeScript check both pass;
- `scripts/run_cvf_release_gate_bundle.py` persists a structured
  `e2eDiagnostic` for any failed live E2E stage via a new
  `--e2e-diagnostic-output` flag, using the existing diagnostic vocabulary
  shape;
- the retained blocked A5 evidence set (three JSON files plus the worker
  return) is byte-unchanged;
- exactly one post-repair canonical live invocation occurs, only after every
  local check is green, using fresh A5R1-dated evidence paths;
- `LIVE_GOVERNANCE_PROVEN_BOUNDED` and any overall-release-PASS claim remain
  reserved for the independent reviewer;
- no secret, raw provider/prompt/output content, or raw response body beyond
  a short safe-classified excerpt is persisted;
- exact manifest only, HEAD unchanged, no worker commit.

## Worker Autonomy / No-Question Rule

Resolve allowed-scope test/repair details from verified source. Repair any
allowed-scope gate or test-shape defect directly. Stop only for: a current-
source contradiction with this packet's Source Verification Block; a need to
touch a path outside the Work-Order Fulfillment Manifest and its named
four-file repair-surface allowance; a secret-safety failure; or a live
failure whose diagnostic does not justify a result-changing rerun. Do not ask
the operator whether to fix an allowed-scope failure. Provider availability
alone is never a reason to retry the canonical command.

## Roadmap-to-Work-Order Trace Matrix

| Roadmap requirement | Work-order instruction | Evidence owner |
|---|---|---|
| SOT3 required in canonical gate (already closed by A5) | unchanged; this recovery does not touch `check_sot3` | prior A5 material and this recovery's unchanged-path confirmation |
| canonical command passes overall | reproduce, repair, and prove the Refinery import-chain defect before any rerun | new focused regression and post-repair canonical result |
| structured diagnostics for failed live stages | new `e2eDiagnostic` and `--e2e-diagnostic-output` | release bundle source and new diagnostic evidence file |
| retained historical evidence preserved | explicit read-only boundary on the three blocked-A5 JSON files and the blocked worker return | before/after byte-comparison in the worker return |
| exactly one post-repair canonical invocation | Call Budget And Rerun Protocol below | worker return invocation and per-stage provider-call accounting |
| final exact claim | reviewer-owned only | future A5R1 completion review |

## Call Budget And Rerun Protocol

| Control | Required behavior |
|---|---|
| local-first | Refinery typecheck/build/test, web build/typecheck, and the new regression must all be green before any live-triggering command runs |
| planned live invocation | exactly one canonical `python scripts/run_cvf_release_gate_bundle.py --json ...` command, using fresh A5R1-dated evidence paths |
| provider-call accounting | the canonical invocation may contain multiple provider calls across the live Playwright stage and SOT3 stage; record the actual call count per stage and the call-level versus event-level denominators without converting them into a one-call claim |
| direct live-test invocation | forbidden; do not invoke any `.live.test.ts` file or Playwright live spec directly (ADIF-0030) |
| default retry | forbidden |
| diagnostic-gated retry | permitted only after a complete, secret-safe diagnostic is captured and a further concrete, recorded, result-changing repair is made; provider/quota availability alone never justifies a retry |
| hard ceiling | one post-repair canonical invocation for A5R1; a need for a second live-triggering command returns to the operator/reviewer |

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one implementation/bounded-live-proof worker, then independent reviewer/closer |
| phase | recovery implementation and worker return |
| baseHeadFor(phase) | dispatchBaseHead=`57f1a9fda`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| changedSetScope(phase) | exact Work-Order Fulfillment Manifest, plus the four explicitly named Refinery/web repair-surface paths if and only if implicated by the proven defect |
| traceScope(phase, actor) | worker records reproduction, repair rationale, tests, the one canonical invocation, actual provider-call count by stage, diagnostics, evidence, diff, and HEAD; reviewer owns closure conversion |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer/closer owns material commit |
| crossBatchIsolation | retained blocked-A5 evidence and A1-A4 evidence are read-only; unrelated and session paths forbidden |
| nextMoveSurfaces | reviewer updates roadmap, session state, handoff, and memory only following the accepted material closure commit |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SOT3_ACT_A5R1_BOUNDED_RECOVERY_REFINERY_IMPORT_CHAIN_COMPLETION_2026-07-14.md` |
| reviewerOwnedClosurePaths | completion review; paired baseline/work-order status; activation roadmap; active session state sources; active handoff; session memory |
| closureOwner | Codex reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_SOT3_ACT_A5R1_BOUNDED_RECOVERY_REFINERY_IMPORT_CHAIN_WORKER_RETURN_2026-07-14.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Skeleton command:
`python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_SOT3_ACT_A5R1_BOUNDED_RECOVERY_REFINERY_IMPORT_CHAIN_WORKER_RETURN_2026-07-14.md --title "CVF SOT3 ACT A5R1 Bounded Recovery Refinery Import Chain Worker Return" --profile WORKER_RETURN_FULL_GATE_V1`

The return must include execution base, exact changed set, reproduction
evidence, repair rationale, command evidence, call-level provider accounting,
diagnostic disposition, result/manifest hashes, retained-evidence
byte-unchanged confirmation, Roadmap trace, Finding-To-Governance
disposition, Epistemic Process Block, Public Export Disposition, claim
boundary, and explicit no-commit statement.

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake route | operator-directed SOT3 A5 bounded recovery dispatch |
| canonical route mode | `SINGLE_AGENT_SINGLE_ROLE` |
| selected role route | dispatcher -> no-commit implementation/bounded-live-proof worker -> reviewer/closer |
| scope classification | bounded runtime dependency-resolution repair plus one bounded live recovery run |
| risk sensitivity | R2 runtime and real-provider proof |
| escalation condition | stop for forbidden paths, authority movement, secret risk, unresolved local repair, unjustified live rerun, A5 closure claim, public-sync, or scope expansion |
| Dispatcher role | external dispatch author; independently reviewed by Codex before dispatch |
| Worker route | `WORKER_MUST_NOT_COMMIT` |
| Reviewer/closer route | Codex reviewer/closer after accepted worker return |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: A5R1 repairs an already-diagnosed runtime
integration defect within the already-absorbed SOT3 runtime roadmap and does
not scan, classify, or absorb a legacy corpus. No coverage index row is owned
by this tranche.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current runtime proof, bounded live proof, and work-order source verification |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py` plus this work order's own Source Verification Block |
| Owner surface | current governed CVF Refinery/web-package/release-bundle source and the retained blocked A5 evidence |
| Disposition | BLOCKED_UNTIL_CVF_PROOF at dispatch; reviewer may accept only fresh A5R1 evidence |
| Claim boundary | provider-local memory, the blocked return's own prose, and external material are not source authority; only current source and fresh evidence are |

## Verification Commands

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 57f1a9fda --head HEAD
cd EXTENSIONS/CVF_REFINERY
npx tsc --noEmit
npx tsc
npx vitest run
cd ../../..
cd EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npx playwright test tests/e2e/refinery-import-chain-dev.spec.ts --config=playwright.config.mock.ts --reporter=line
npm run check
npm run build
cd ../../..
python scripts/run_cvf_release_gate_bundle.py --dry-run --json
python scripts/run_cvf_release_gate_bundle.py --json --output docs/reviews/evidence/sot3-act-a5r1-recovery-release-gate-result-2026-07-14.json --manifest-output docs/reviews/evidence/sot3-act-a5r1-recovery-release-gate-manifest-2026-07-14.json --sot3-diagnostic-output docs/reviews/evidence/sot3-act-a5r1-recovery-release-sot3-diagnostic-2026-07-14.json --e2e-diagnostic-output docs/reviews/evidence/sot3-act-a5r1-recovery-release-e2e-diagnostic-2026-07-14.json
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_commit_steward_preflight.py --base 57f1a9fda --head HEAD
git diff --check
git status --short
```

If the actual post-dispatch HEAD differs, substitute the captured
executionBaseHead for `57f1a9fda` in worker-range commands. Verify the exact
commit-steward preflight flag name via `--help` before relying on it, since a
prior tranche found the work-order-literal flag name did not match the real
CLI.

Do not run the canonical release bundle more than once. Do not invoke any
`.live.test.ts` file or Playwright live spec file directly.

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES_AT_WORKER_EXECUTION_ONLY |
| runtimeMutationAuthorized | exact Refinery/web development-bundler and package-consumption repair surface plus release-bundle diagnostic wiring named in the manifest |
| freshnessVerificationMode | fresh local reproduction, fresh repair, fresh local proof, then fresh live recovery |
| priorVerificationArtifact | the blocked A5 worker return is prerequisite diagnostic evidence only, independently re-verified, not trusted as-is |
| requiredFutureAction | worker reproduces, repairs, proves locally, and returns uncommitted A5R1 evidence |

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

priorVerificationArtifact: `docs/reviews/CVF_SOT3_ACT_A5_CANONICAL_RELEASE_PROOF_WORKER_RETURN_2026-07-13.md`

priorVerificationAnchor: material commit `f038bcb81`

freshRecomputeRequired: yes; the blocked A5 evidence proves diagnosis only, not
a repaired or passing result

unicodePathHandling: use literal repository paths and UTF-8-safe readers;
author new prose and source in ASCII

extractedTextAuthority: N/A with reason: no external extraction or OCR input

## Review Gate

The independent reviewer must reproduce the local Refinery and web-package
checks, inspect the repair's minimality against the Source Verification
Block, confirm the retained blocked-A5 evidence is byte-unchanged, recompute
the new evidence hashes, verify the one canonical invocation's actual
provider-call accounting by stage and diagnostic
disposition, and refuse any claim beyond
`SOT3_A5_RECOVERY_LOCAL_AND_LIVE_PROVEN_BOUNDED` for this recovery alone;
`LIVE_GOVERNANCE_PROVEN_BOUNDED` and any overall roadmap-final claim remain
reserved for a separate reviewer decision after this recovery closes.

## Closure Checklist

- [ ] Exact manifest only; no historical A1-A4 or retained blocked-A5 evidence
  mutation.
- [ ] Reproduction, repair rationale, and minimality evidence recorded.
- [ ] Refinery own typecheck/build/test green and unweakened.
- [ ] Web package production build and typecheck pass.
- [ ] New Refinery-import-chain regression passes.
- [ ] Structured `e2eDiagnostic` and `--e2e-diagnostic-output` implemented.
- [ ] Local checks green before the one post-repair canonical live call.
- [ ] Post-repair canonical live call is fully accounted, one call only.
- [ ] Worker-return fast gate and steward preflight pass.
- [ ] HEAD remains unchanged and worker made no commit.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only when every checklist item is evidenced.
Return `BLOCKED_WITH_REASON` for a source contradiction, forbidden-path need,
unresolved local repair, unsafe evidence, or a live failure whose diagnostic
does not justify the one permitted rerun. Do not return a partial PASS.

## Operator Checkpoint

No operator checkpoint is parked before the one planned post-repair canonical
run. Stop and return to the operator/reviewer if the next action after a live
failure would require a second live-triggering command, a change outside the
named repair surface, or any authority beyond this recovery's bounded scope.

## Stop Conditions

- current source contradicts a verified claim in this packet;
- implementation requires a path outside the exact manifest and its named
  four-file repair-surface allowance;
- the repair cannot be made without weakening Refinery's own ESM/typecheck/
  build/test contract;
- local checks are not fully green before a live-triggering command;
- live output is failed/partial/unclear without a complete diagnostic;
- a proposed rerun has no result-changing action;
- raw content, a secret, or an unclassified raw response body would need to
  be persisted;
- work expands into A5 closure claims, public-sync, prompt tuning, or
  provider comparison.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | external dispatch author; Codex independent dispatch reviewer |
| Provider or surface | private provenance workspace; Alibaba only during the worker's one bounded post-repair recovery call |
| Session or invocation | SOT3-ACT-A5R1 authoring on 2026-07-13 and independent dispatch review on 2026-07-14 |
| Working directory | repository root |
| Command or tool surface | governed reads, source verification, scaffold helper, ADIF resolver, Write/Edit, dispatch gates |
| Target paths | paired A5R1 baseline and this work order now; exact worker manifest during execution |
| Allowed scope source | operator authority, blocked A5 diagnosed evidence, session-sync routing |
| Before status evidence | clean `57f1a9fda`; A5R1 packet paths absent before authoring |
| After status evidence | source-verified A5R1 packet ready for worker |
| Diff evidence | `git diff --name-status` before any commit |
| Approval boundary | A5R1 recovery only |
| Claim boundary | no recovery execution or final claim at dispatch |
| Agent type | dispatcher |
| Invocation ID | `sot3-act-a5r1-dispatch-review-2026-07-14` |
| Expected manifest | paired baseline and this work order |
| Actual changed set | paired baseline and this work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | dispatch authorization and future bounded A5R1 repair-and-recovery proof |
| claimDisposition | CLAIM_REJECTED: no repair, recompilation, or live result is claimed at dispatch |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: future fresh A5R1 evidence required |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: future reproduction, repair, local proof, and one canonical live invocation with measured provider-call accounting required |
| invocationBoundary | one explicit post-repair canonical release-bundle invocation |
| interceptionBoundary | release-orchestration and Refinery-consumption-boundary repair only; no universal provider wrapper |
| claimLanguage | future PASS may claim only `SOT3_A5_RECOVERY_LOCAL_AND_LIVE_PROVEN_BOUNDED` |
| forbiddenExpansion | no `LIVE_GOVERNANCE_PROVEN_BOUNDED`, overall-release-PASS claim beyond this recovery's own result, A5 closure, final, production, public, universal, or user-value claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private runtime/evidence recovery tranche using operator-local
credentials; no public-sync authority exists.

## Machine Closure Package

NOT_APPLICABLE_WITH_REASON: this is a dispatch-ready work order, not a
closure artifact. Reviewer closure conversion owns the final machine package.

## Claim Boundary

This work order authorizes exactly one bounded A5R1 recovery tranche. Even a
complete worker return remains pending independent review and may support
only `SOT3_A5_RECOVERY_LOCAL_AND_LIVE_PROVEN_BOUNDED` for this recovery's own
result. It does not itself close A5, and it does not establish
`LIVE_GOVERNANCE_PROVEN_BOUNDED`, which remains reserved for a separate
reviewer decision after this recovery is accepted and any further required
A5 evidence is complete.
