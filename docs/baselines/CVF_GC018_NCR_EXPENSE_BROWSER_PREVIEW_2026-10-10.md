# CVF GC-018 Baseline - NCR Expense Browser Preview
Memory class: governed-dispatch-baseline
Status: DISPATCH_READY
Date: 2026-10-10
Batch ID: CVF-NCR-EXPENSE-BROWSER-20261010
Dispatch base head: 665da5b2df3e1d2b81553a5c9567c7babb364459
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN
rawMemoryReleased=false

## Purpose

Deliver a reusable offline browser preview of the accepted ExpenseList component and real Chromium interaction proof. Named gap: accepted unit fixture has no real-browser behavior/layout evidence or runnable preview. Reuse the unchanged component; do not recreate its filter, mount production routes or revise the storyboard. The useful outcome is an inspectable synthetic UI preview plus discriminating browser tests, not a model benchmark alone.

## Scope / Target / Owner Boundary

Standing operator autonomous isolated-test/continuation authority and manual worker transfer cover this finite private browser preview. Exactly two implementation scripts plus three metadata outputs. Accepted component/tests remain read-only; Local owns technical acceptance. Launch only installed headless Chromium against generated self-contained HTML, no server or external requests. No application-route, storyboard or AI-governance claim change.

## Authority Chain

| Source | Disposition |
|---|---|
| Operator2026-10-10 continue; prior autonomous isolated tests/manual transfer and Local reviewer role | ACCEPT |
| Paired GC-018 baseline docs/baselines/CVF_GC018_NCR_EXPENSE_BROWSER_PREVIEW_2026-10-10.md | ACCEPT |
| Accepted unit and browser capability pins docs/reviews/evidence/cvf-expense-browser-dispatch-inputs-2026-10-10.json | ACCEPT |
| Source R2 and all effect holds | ACCEPT; retained |

## Implementation Contract

1. Builder scripts/cvf_expense_fixture_preview.cjs is a Node CommonJS CLI plus importable bounded helper. CLI: `node scripts/cvf_expense_fixture_preview.cjs --output .cvf/runtime/cvf-expense-browser-worker-20261010/expense-preview.html`. Resolve installed Vite/React/react-dom from the existing web node_modules, use browser IIFE bundling with configFile:false, envFile:false, write:false and production NODE_ENV literal. No install, app config/env load or server. Use a runtime-owned entry and existing JSX transform, no handwritten replacement of ExpenseList.
2. Bundle actual read-only EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.tsx; its raw SHA is pinned in dispatch inputs. Browser root renders this named component with exactly five manually synthetic rows: two Feb2026, two Mar2026, one 05/03/2026 invalid row. Existing test fixture may inform data shape but must not be imported into browser oracle. Preserve displayed IDs/order; primary browser row expectations authored in test script.
3. Produce one standalone HTML with all runtime JS/CSS inline, no CDN/font/image/source-map imports or links. Escape closing script sequences in inline bundles. Use DESIGN.md token values for a small wrapper, system fonts, no invented success/governance badge. Existing component notice remains. Add concise Vietnamese text that this is private synthetic browser UI, not AI governance/application integration. Keep accepted storyboard and its historical badge/narration untouched.
4. Optional build helper arguments fixtureVariant=primary|calendar and sourceTextOverride are for test-only runtime negatives, not app features. Calendar variant transforms the same five rows to include a wrong-year March row and an impossible March32 row. Override must operate in memory or ignored copies, never change accepted tracked source. Ordinary CLI refuses source-pin drift before replacing existing output; failure preserves a preexisting output sentinel.
5. Browser test scripts/test_cvf_expense_fixture_preview_browser.cjs launches only installed Playwright Chromium, loads generated HTML with page.setContent or local file URL, and closes context/browser in finally. Block/report every external request; distinguish main file load from subresources. No HTTP listener. Treat page errors/console errors, skipped cases, missing readiness and timeout as failures, never PASS. Desktop1280x800 and mobile390x844 are the only profiles; use explicit waits for rendered rows, no timing sleeps as readiness proof.
6. Browser assertions: March2026 two exact rows; April empty message/table absent; clear filter four valid rows; malformed row absent/no errors; native input has Vietnamese accessible label and existing note. Calendar variant excludes wrong-year same-month and impossible date; preserve order/identity. Inspect input/note/table within viewport, no horizontal clipping at both profiles. Screenshots desktop/mobile primary March view for Local visual review, not media/storyboard assets.
7. Two browser mutants from pinned source: remove exact month predicate; bypass actual calendar-day validity. Browser assertions must fail for the corresponding behavior, not bundling/harness setup. Each starts from unchanged baseline; record tests collected/completed and assertion failure, exclude harness-invalid runs. Keep all accepted source hashes unchanged and restore ordinary passing preview after mutations.
8. Caps builder250/test350/guide100/evidence350/return450 physical lines. Generated primary HTML2MiB max. No extra tracked fixture/split, storage, real data, provider or runtime integration. Before coding inspect existing package/build API and checker shape; routine internal choices remain worker-owned.

## Acceptance Criteria

Five artifacts, unchanged accepted source pins, self-contained actual-component preview, concrete desktop/mobile browser interactions and calendar negatives, two genuine assertion-level browser mutant kills, no external requests or leaks, source-drift refusal preserving output sentinel, and full bound frozen-return confirmation. New browser proof is supplementary to accepted unit evidence; do not rerun the unit suite or claim application/AI-governance execution.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Accepted component | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.tsx | ExpenseList; filterExpensesByMonth | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.tsx | ExpenseList; filterExpensesByMonth | ACCEPT |
| Read-only existing test fixture | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.test.tsx | FIXTURE; render cases | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.test.tsx | FIXTURE; render cases | ACCEPT |
| Accepted unit result and limitations | docs/reviews/CVF_NCR_EXPENSE_FILTER_FIXTURE_COMPLETION_2026-10-09.md | Findings / Position; Claim Boundary | docs/reviews/CVF_NCR_EXPENSE_FILTER_FIXTURE_COMPLETION_2026-10-09.md | Findings / Position; Claim Boundary | ACCEPT |
| Behavior intent | docs/reference/CVF_NCR_GENERAL_VIDEO_DESIGN_2026-10-02.md | S05 and S06 | docs/reference/CVF_NCR_GENERAL_VIDEO_DESIGN_2026-10-02.md | S05 and S06 | ACCEPT |
| UI contract | canonical UI contract DESIGN.md | theme and tokens | DESIGN.md | theme and tokens | ACCEPT |
| Existing browser method | scripts/test_cvf_storyboard_preview_browser.cjs | withPage; Chromium; screenshot | scripts/test_cvf_storyboard_preview_browser.cjs | withPage; Chromium; screenshot | ACCEPT |
| Forward learning | docs/reviews/learnings/CVF_ORCHESTRATOR_PREAPPROVAL_FEASIBILITY_LEARNING_2026-10-08.md | Actual Dispatch Application Observation; parentFindingId | docs/reviews/learnings/CVF_ORCHESTRATOR_PREAPPROVAL_FEASIBILITY_LEARNING_2026-10-08.md | Actual Dispatch Application Observation; parentFindingId | ACCEPT |
| Existing dependencies | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json | react; @playwright/test; vitest | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json | react; @playwright/test; vitest | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_dispatch_release_readiness.py; governance/compat/check_task_governance_route.py |
| literalTokensReviewed | WORKER_MUST_NOT_COMMIT; acceptance-ledger-json; Source Verification Block; COMPLETE_PENDING_REVIEW; CLOSEABLE; gateId; mutationSurface; Returned defects: NONE_RETURNED |
| gateRunPurpose | confirmation of source-verified packet structure, not first discovery |
| claimBoundary | no worker implementation or media execution proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`expense-browser-preview`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | python governance/compat/run_adif_defect_resolver.py --task-class expense-browser-preview --role dispatcher --lifecycle-phase pre-dispatch |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no returned registry defect; substantive STOP still retained |

## Negative Search And Collision Discipline

Targeted rg in scripts and accepted expenses directory found only the new accepted unit fixture, no actual-component browser preview/helper. Prior storyboard browser suite covers a different static projection; no duplicate rerun selected. This is not repository-wide absence/completeness proof. Exact nine packet/worker paths checked absent. Existing source-R2 key and STOP unchanged; new finite UI outcome has a separate INITIAL identity.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private operator handoff and isolated preparation only.


## Claim Boundary

Private actual-component browser UI preview only; two new scripts plus three metadata files, not a two-file-only governed execution. No application-route integration, AI-governance behavior, actual ledger/provider, media, production readiness, source-R2 recovery/public/deploy/P11 claim. Original unit timing/process deviations retained. Next worker preference is operator-reported Haiku5.5/Max metadata, not normative or a savings claim.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-EXPENSE-BROWSER-20261010 --title "NCR Expense Browser Preview" --date 2026-10-10 --base 665da5b2df3e1d2b81553a5c9567c7babb364459 --commit-mode WORKER_MUST_NOT_COMMIT --no-evidence-readiness-applicable --stdout |
| generatedProfile | web-ui-dashboard/no-commit worker |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | verified prior packet boilerplate reused; all task-specific scope/source/ledger/probe/timing/browser contracts replaced |
| checkerReadAheadConfirmation | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_independent_review_probe_admission.py |
| docOnlyNewFields | NONE |
| claimBoundary | authoring only |

## Decision

Admit five-output browser preview after actual clean committed bound release and continuity. Standing isolated-test/manual worker authority applies. No source/media/app/provider/public effect admission.

## Evidence / Verification

Frozen component/design pins; installed generic build capability; current-order learning binding; explicit canonical feasibility; authoring gate then committed release. No worker preview produced by dispatcher.
