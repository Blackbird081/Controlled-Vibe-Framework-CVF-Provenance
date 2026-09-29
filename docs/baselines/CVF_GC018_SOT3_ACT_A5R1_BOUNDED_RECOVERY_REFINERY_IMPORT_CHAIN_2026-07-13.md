# CVF GC-018 Baseline - SOT3 Activation A5 Bounded Recovery - Refinery Import Chain Repair

Memory class: governed-dispatch-baseline

Status: CLOSED_PASS_BOUNDED

docType: baseline

Batch ID: SOT3-ACT-A5R1

Date: 2026-07-13

Dispatch base head: `57f1a9fda`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Operator

Reviewer owner: Codex reviewer/closer

Worker target: delegated implementation and bounded live-proof worker

## Purpose

Authorize one bounded recovery tranche that repairs the diagnosed Refinery
package-consumption defect blocking the canonical release bundle's live E2E
stage, proves both production build and Next.js development-bundler
compatibility, adds structured release-level diagnostics for failed live E2E
stages, and permits exactly one post-repair canonical live rerun only after
every local check is green and a concrete result-changing repair is recorded.

## Authority / Decision

The operator authorized A0-A5 toward `LIVE_GOVERNANCE_PROVEN_BOUNDED`. A5's
first execution attempt is blocked: material commit `f038bcb81` preserves the
blocked worker return as historical evidence, and session-sync commit
`57f1a9fda` is the current clean HEAD. This baseline releases exactly one A5
recovery packet. It does not pre-approve `LIVE_GOVERNANCE_PROVEN_BOUNDED`, an
overall release PASS, or any A5 closure claim.

## Source / Predecessor Evidence

The blocked A5 worker return
(`docs/reviews/CVF_SOT3_ACT_A5_CANONICAL_RELEASE_PROOF_WORKER_RETURN_2026-07-13.md`,
`Status: BLOCKED_WITH_REASON`) is the direct predecessor packet. It records
that the SOT3 canonical check itself PASSed (all A4 denominators satisfied,
one real Alibaba call) while the overall release `gate_result` FAILed because
`E2E Playwright Governance (live)` returned HTTP 500 HTML instead of JSON. The
retained Playwright trace and the worker return's own diagnosis identify the
concrete cause. Runtime source overrides summaries; every claim below is
independently re-verified against current source in the Source Verification
Block, not merely copied from the blocked return's prose.

## Decision

Release one no-commit A5R1 bounded recovery tranche: reproduce, diagnose-
confirm, and repair the Refinery package-consumption defect that made the
canonical release bundle's live E2E stage fail, then run exactly one
post-repair canonical live invocation.

## Baseline

A5's first execution attempt is blocked: the SOT3 canonical check itself
PASSed with every required A4 denominator, but the overall release
`gate_result` FAILed because the execute route's Refinery import chain could
not be resolved by the Next.js development bundler. That blocked evidence
(material commit `f038bcb81`) is retained, read-only, as the diagnostic
baseline for this recovery.

## Proposed Tranche

Reproduce the failure locally, apply the smallest correct Refinery-
consumption repair, prove Refinery's own ESM/typecheck/build/test contract is
preserved, prove both production build and development-bundler compatibility,
add a focused regression over the repaired import chain, add structured
release-level diagnostics for failed live E2E stages, and permit exactly one
post-repair canonical live rerun only after every local check passes and a
concrete result-changing repair is recorded.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| A5 first attempt preserved as blocked historical evidence | material commit `f038bcb81`; `docs/reviews/CVF_SOT3_ACT_A5_CANONICAL_RELEASE_PROOF_WORKER_RETURN_2026-07-13.md`; `Status: BLOCKED_WITH_REASON` | the blocked return and its evidence paths must remain unmodified by recovery work | ACCEPT |
| session continuity | session-sync commit `57f1a9fda` routes A5 bounded recovery as next allowed move | recovery packet must dispatch from this clean HEAD | ACCEPT |
| A4 closure (unaffected) | `docs/reviews/CVF_SOT3_ACT_A4_FAILURE_AND_RECOVERY_BOUNDARY_PROOF_COMPLETION_2026-07-13.md`; `Status: CLOSED_PASS_BOUNDED` | A4 remains accepted; recovery must not reopen or mutate A4 evidence | ACCEPT |

## Scope / Target / Owner Boundary

Allowed:

- source-verify and repair the Refinery package-consumption boundary that the
  execute route's knowledge-context import chain depends on
  (`EXTENSIONS/CVF_REFINERY/src/index.ts` and/or its `./deps.js` specifier,
  `EXTENSIONS/CVF_REFINERY/package.json` `main`/`exports`/`type` fields, and
  the explicitly selected Next.js development bundler in
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` and the
  Turbopack/webpack resolver configuration in
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/next.config.ts` that already
  targets `.js`-to-`.ts` resolution for sibling packages);
- select the smallest correct repair; do not rewrite Refinery's export surface
  or its consumers' import statements beyond what the diagnosed defect
  requires;
- add one zero-provider Playwright regression proving `/api/execute` can
  compile and return JSON through the Refinery import chain under the real
  explicitly selected `next dev` bundler;
- add structured release-level diagnostics (stage, class, retryability, user
  action, provider/model where applicable, HTTP status, latency, trace/
  receipt, safe message) for a failed live E2E stage in
  `scripts/run_cvf_release_gate_bundle.py`, reusing the existing live
  diagnostic vocabulary;
- execute the canonical release bundle with real Alibaba credentials exactly
  once, post-repair, only after every local check (typecheck, build, package
  test, focused regression, dry-run) is green.

Forbidden:

- overwriting, deleting, or mutating the retained blocked A5 evidence
  (`docs/reviews/CVF_SOT3_ACT_A5_CANONICAL_RELEASE_PROOF_WORKER_RETURN_2026-07-13.md`
  and its three `docs/reviews/evidence/sot3-act-a5-*-2026-07-13.json` files)
  during local repair validation; a fresh, separately dated or separately
  named result set must be produced by any new canonical run;
- blindly rewriting all Refinery imports, all sibling package `.js` import
  specifiers, or the shared Truth Kernel/Truth Flow packages, which are not
  implicated by the diagnosed defect;
- weakening or removing Refinery's ESM export contract, its own
  `tsc --noEmit` typecheck, its own `tsc` build, or its own `vitest run` test
  suite;
- changing Truth Kernel or Truth Flow source, or any A1-A4 runtime source or
  historical A1-A4 evidence;
- mock substitution for SOT3 or live governance proof;
- more than one post-repair canonical live invocation, and no invocation at
  all before local checks are fully green;
- automatic provider retry before a secret-safe diagnostic and an explicit,
  recorded, result-changing repair;
- directly invoking any `.live.test.ts` file or the Playwright live spec files
  outside the one canonical release-bundle command;
- public-sync, production deployment, universal-control, scale, certification,
  or real-user-value claims;
- worker commit or session-state mutation.

## Live Proof Boundary

Alibaba calls are operator-unmetered for this tranche's canonical command, but
exactly one post-repair canonical release-bundle invocation is planned. It may
occur only after (a) Refinery's own typecheck/build/test all pass, (b) the web
package's production build and TypeScript check pass, (c) the new focused
regression proving the Refinery import chain compiles under dev-server mode
passes, and (d) `--dry-run --json` still shows the structural shape expected
(SOT3 `SKIP`, no PASS claim). A failed, partial, empty, timed-out, or unclear
live stage must persist a diagnostic and stop; a later rerun needs a specific,
recorded, result-changing repair, and provider/quota availability is never a
sufficient reason to retry.

The final claim remains reviewer-owned. Worker success supports only
`COMPLETE_PENDING_REVIEW`.

## Acceptance Criteria

- the diagnosed Refinery-to-Next.js-development-bundler import defect no
  longer reproduces;
- Refinery's own ESM module contract, `tsc --noEmit`, `tsc` build, and
  `vitest run` all remain green and unweakened;
- the web package's production build (`npm run build`) and TypeScript check
  both pass;
- a new zero-provider Playwright regression proves `/api/execute` compiles
  and returns JSON through the Refinery import chain under the real selected
  `next dev` bundler;
- `scripts/run_cvf_release_gate_bundle.py` persists a structured diagnostic
  (stage/class/retryable/userAction/provider-model-where-applicable/
  httpStatus/latency/trace-or-receipt/safeMessage) for any failed live E2E
  stage, not only for the SOT3 check;
- the retained blocked A5 result, diagnostic, and manifest evidence remain
  byte-unchanged;
- exactly one post-repair canonical live invocation occurs, only after every
  local check is green;
- final evidence remains secret-safe and A5-recovery-bounded; no
  `LIVE_GOVERNANCE_PROVEN_BOUNDED` or overall-release-PASS claim is made by
  the worker.

## Verification / Evidence

- Refinery package: `tsc --noEmit`, `tsc` (build), `vitest run`;
- web package: TypeScript check, production build (`npm run build`);
- new focused regression proving the import chain compiles under dev-server
  mode;
- `--dry-run --json` structural proof with zero provider calls;
- exactly one planned post-repair canonical live bundle invocation;
- fresh A5-recovery release JSON, diagnostic, and manifest hash
  recomputation, dated and named distinctly from the retained blocked
  evidence;
- reviewer-fast, pre-implementation, worker-return, and commit-steward gates;
- `git diff --name-status`, `git status --short`, and unchanged worker HEAD.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind runtime-provider-live --batch-id SOT3-ACT-A5R1 --title "SOT3 Activation A5 Bounded Recovery - Refinery Import Chain Repair" --date 2026-07-13 --base 57f1a9fda --commit-mode WORKER_MUST_NOT_COMMIT --dependency "A5 blocked f038bcb81 BLOCKED_WITH_REASON_DIAGNOSED" --stdout --include-worker-return-skeleton` |
| generatedProfile | runtime-provider-live plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with verified blocked-A5 dependency evidence, current Refinery/web/Next.js source facts, exact scope reopening the Refinery-consumption boundary, diagnostics requirement, and claim boundary |
| checkerReadAheadConfirmation | `governance/compat/check_work_order_dispatch_quality.py`, `governance/compat/check_agent_handoff_boundary.py`, `governance/compat/check_machine_closure_package.py`, `governance/compat/check_finding_to_governance_learning.py`, `governance/compat/check_governed_file_size.py`, `governance/compat/run_agent_autorun_workflow_gate.py` read |
| docOnlyNewFields | declared in paired work order |
| claimBoundary | dispatch authorization only; no recovery execution or final claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`SOT3 runtime dependency resolution bounded recovery dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "SOT3 runtime dependency resolution bounded recovery dispatch" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector "refinery package consumption next.js turbopack module resolution" --risk-ceiling HIGH --max-results 30 --json`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Returned defect count | 0 |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | worker must still read ADIF-0030 and ADIF-0031 as explicit required reads; both remain binding for this recovery's live-call and writable-manifest discipline even though the semantic resolver query returned no matching entries |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/run_agent_autorun_workflow_gate.py` |
| literalTokensReviewed | Status; Dependency Release Evidence; Source Verification Block; Required Artifact Manifest; Agent Handoff Contract Control Block; Public Export Disposition |
| gateRunPurpose | dispatch authoring confirmation after source verification |
| claimBoundary | checker compliance does not prove the recovery repair works or that live proof passes |

## Current Runtime Freshness Verification

| Field | Value |
|---|---|
| runtimeClaimPresent | YES_AT_DISPATCH_SOURCE_VERIFICATION_ONLY |
| runtimeMutationAuthorized | exact Refinery package-consumption boundary, web-package development-bundler/resolver/diagnostic wiring, and evidence paths named in the paired work order's manifest |
| freshnessVerificationMode | FRESH_SOURCE_READ_AT_DISPATCH; worker must re-verify before editing |
| reason | this baseline's Source Verification Block was built from direct reads of `EXTENSIONS/CVF_REFINERY/src/index.ts`, `EXTENSIONS/CVF_REFINERY/src/deps.ts`, `EXTENSIONS/CVF_REFINERY/package.json`, `EXTENSIONS/CVF_REFINERY/tsconfig.json`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/next.config.ts`, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tsconfig.json`, and the consuming import sites at dispatch base `57f1a9fda`, not from the blocked worker return's prose alone |
| requiredFutureAction | worker re-runs the same symbol/path searches immediately before editing, since source may have moved between dispatch and execution |

## Claim Boundary

This baseline authorizes exactly one bounded A5 recovery tranche: repair of
the diagnosed Refinery import-chain defect, structured live-E2E diagnostics,
and one post-repair canonical live invocation. It does not assert
`LIVE_GOVERNANCE_PROVEN_BOUNDED`, an overall release PASS, release to users,
production readiness, public availability, scale, or user validation. The
final claim remains reserved for the independent Codex reviewer/closer after
the recovery worker return is accepted.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this recovery tranche uses operator-local Alibaba credentials and
private provenance evidence. No public-sync authority exists.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this artifact | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Work order status | paired A5 recovery work order | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SOT3_ACT_A5R1_BOUNDED_RECOVERY_REFINERY_IMPORT_CHAIN_COMPLETION_2026-07-14.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Roadmap state | activation roadmap | `Status: CLOSED_PASS_BOUNDED_LIVE_GOVERNANCE_PROVEN_BOUNDED` | PASS |
| Registry JSON | corpus registry | generated aggregate check PASS | PASS |
| Registry Markdown | corpus front door | existing front door; no change required | PASS |
| External evidence digest | A5R1 recovery manifest | result sha256 `3e65e359de66888f45c143ea9a2809f29f27e6b7097edf0a910db2c855f0ca8b`; three evidence entries; unsigned | PASS |
| System loop interlock | N/A with reason: no automated loop edge at dispatch | N/A | N/A with reason |
| Session continuity | separate post-dispatch sync | pending after packet commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

NOT_APPLICABLE_WITH_REASON: this baseline authorizes a runtime dependency-
resolution recovery, not a corpus-candidate or query-acceptance closure. It
mentions the release-evidence "result and diagnostic" receipt files
(`sot3-act-a5-*-2026-07-13.json`) only as read-only predecessor evidence and
future fresh evidence paths; it does not close, accept, or select any
candidate/query receipt requiring a required-value/observed-value/status
assertion row.
