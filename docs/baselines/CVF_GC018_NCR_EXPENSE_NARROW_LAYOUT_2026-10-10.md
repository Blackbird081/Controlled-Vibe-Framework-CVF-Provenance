# CVF GC-018 Baseline - NCR Expense Narrow Layout
Memory class: governed-dispatch-baseline
Status: DISPATCH_READY
Date: 2026-10-10
Batch ID: CVF-NCR-EXPENSE-LAYOUT-20261010
Dispatch base head: c202cc73ff97cdeb1fe57358d1438afbc623b566
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN
rawMemoryReleased=false

## Purpose

Correct the retained320px long-label table content overflow in the actual ExpenseList component. Preserve target44 and filter/date/notice semantics. This is responsive UI maintenance backed by Local F5 measurement, not a benchmark-only assignment, new source-R2 chain or general guard promotion.

## Scope / Target / Owner Boundary

Standing autonomous isolated UI/test authority covers bounded existing table/cell style correction, one new direct-source browser proof and three metadata outputs. Only component presentation styles may change; business/date/filter code, exports/props/row order/Vietnamese labels/synthetic notice/input44 remain fixed. Existing unit and prior scripts/receipts are read-only. Local owns independent acceptance and worker-only longitudinal evaluation.

## Authority Chain

| Source | Disposition |
|---|---|
| Operator2026-10-10 collect/classify/evaluate for later worker configuration; Haiku/Sonnet workers only; continue; standing isolated tests/manual transfer | ACCEPT |
| Paired baseline docs/baselines/CVF_GC018_NCR_EXPENSE_NARROW_LAYOUT_2026-10-10.md | ACCEPT |
| Retained Local320 defect and current pins docs/reviews/evidence/cvf-expense-layout-dispatch-inputs-2026-10-10.json | ACCEPT |
| SourceR2 and effect holds | ACCEPT; retained |

## Implementation Contract

1. Modify only presentation style declarations for the existing table/header/cells in EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.tsx; existing input44/border-box remains unchanged. No business/filter/date/props/export/notice/label/row-order changes, DOM replacement or data truncation. Keep semantic table headers and native input. Worker chooses bounded CSS solution; no prescribed algorithm. Test content must fit visible section inner content box at320,390 and1280. Wrapping dates is permitted; preserving a single date line is NOT a requirement. No hidden overflow, ellipsis, deleted text, scaling, page/table horizontal scroll or font-size reduction to disguise overflow. All synthetic labels/dates/amounts must remain fully readable.
2. New scripts/test_cvf_expense_narrow_layout_browser.cjs bundles ACTUAL current tracked component with installed Vite/React/ReactDOM, configFile:false/envFile:false/write:false/production NODE_ENV, one IIFE/escaped closing script. Do not import worker/prior test assertions or use lookalike filter. Own literal rows/expectations. Prior touch script is read-only method reference, not rerun or edited. Check raw source SHA before/build/after every case.
3. Exactly five own synthetic rows: two Feb2026/two Mar2026 plus invalid05/03/2026. Include March label 'Independent row', a March unbroken80-character alphanumeric label and an amount260000; February short labels. Preserve all literal text. March oracle exact IDs/order, invalid excluded. Page fixture margin0, padding16 and system-ui16px; no wrapper table/td/th style overrides, nowrap, width/overflow/min-height or scaling remedies. Only page tokens/container and focus-visible2px outline allowed. All layout repairs must live in component styles.
4. Three default-dark profiles:320x844,390x844,1280x800. DESIGN dark tokens; consume prior synthetic light/accent proof within its historical source scope, no current-source all-theme certification. March state: table rectangle and every rendered cell/text range contained in section content box with1px tolerance; section content box computed from real rect minus borders/padding. Input/note/table in viewport; no document or section/table horizontal overflow; for label/date/amount Range.getClientRects each visible line inside its cell inner bounds, with full text equality. The unbroken label must wrap or otherwise remain fully contained without lost characters. Record boxes/text expectations/scroll metrics; assertions must fail on offscreen/clipped text, not just width100 style. Input44 outer remains >=44; focused Tab input has visible2px accent outline; row/notice computed colors retain tokens and targeted contrast>=4.5. Not full WCAG.
5. One March -> April -> clear flow at320 with exact IDs, invalid absent, empty state/table absent, restored valid rows and layout assertions after clear. Other profiles March layout/geometry/focus/contrast only. Block/count every non-file request; page/console errors/timeouts/skips fail; close browser/contexts in finally. No server/network/install/sleep readiness. Screenshot March320 and390 with raw hashes, each<=3MiB; HTML<=2MiB and total runtime30MiB.
6. One layout mutation: save exact admitted component preimage628862... to ignored runtime BEFORE editing; bundle that source independently as an ignored mutant against SAME long-label320 oracle, with input44 intact. The existing presentation must be rejected by a meaningful content-box/text containment ASSERTION. No compilation/harness failure counted; baseline corrected source PASS before and restored corrected source PASS after. If admitted preimage does not yield intended assertion failure, return one consolidated blocker instead of inventing kill. Existing44 and date/calendar mutations consumed, not rerun. Tracked source never temporarily mutated.
7. Exact existing unit suite rerun because component changed; unit/config read-only. Use uppercase-drive web cwd and node node_modules/vitest/vitest.mjs run src/expenses/ExpenseList.test.tsx --reporter=verbose. Node--check new CJS. No global tsc/lint, old browser duplicate or app-wide suite. Caps component250/script300/guide100/evidence350/return450 physical lines; count blank lines correctly. Guide explains current layout command and prior proofs remain source-version scoped.
8. ONE90-minute total timer: first awaited timer-only command CAPTURES AND PERSISTS UTC/monotonic BEFORE CVF reads. Record exact required reads; omissions are deviations even if all gates pass. Full bound draft gate then freeze five raw files; a distinct full bound B confirms frozen return, hashes unchanged. End UTC/monotonic/elapsed written only to ignored final-confirmation.json AFTER B and hash verification; no tracked rewrite/backdate. Bill/token/currency null with reason when unexposed; capture Local/worker/metadata repair groups and gate attempts separately, no inferred model pricing.

## Acceptance Criteria

Five admitted worker paths; actual component style-only correction; three profiles fully contain complete labels/dates/amounts within section content box, input44 retained; meaningful preimage layout ASSERTION kill/restoration; exact unit regression PASS; two hashed screenshots; zero network/page errors; original semantics/readonly pins; full bound frozen B confirmation and honest complete timer/read evidence. Pure UI, not AI-governance proof.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Retained320 inner overflow | docs/reviews/CVF_NCR_EXPENSE_TOUCH_TARGET_COMPLETION_2026-10-10.md | F5 ADDITIONAL_320_CONTENT_LIMITATION_RETAINED | docs/reviews/CVF_NCR_EXPENSE_TOUCH_TARGET_COMPLETION_2026-10-10.md | F5 ADDITIONAL_320_CONTENT_LIMITATION_RETAINED | ACCEPT |
| Independent320 measurement | docs/reviews/evidence/cvf-expense-touch-local-review-2026-10-10.json | independentProbe.actual.clipped | docs/reviews/evidence/cvf-expense-touch-local-review-2026-10-10.json | independentProbe.actual.clipped | ACCEPT |
| Admitted current source | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.tsx | ExpenseList table and cellStyle | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.tsx | ExpenseList table and cellStyle | ACCEPT |
| Read-only unit regression | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.test.tsx | describe and FIXTURE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.test.tsx | describe and FIXTURE | ACCEPT |
| Canonical mobile UI contract | canonical UI contract DESIGN.md | sections2,6,7,8 | DESIGN.md | sections2,6,7,8 | ACCEPT |
| Illustrative intent | docs/reference/CVF_NCR_GENERAL_VIDEO_DESIGN_2026-10-02.md | S05 and S06 | docs/reference/CVF_NCR_GENERAL_VIDEO_DESIGN_2026-10-02.md | S05 and S06 | ACCEPT |
| Compiler/browser method reference | scripts/test_cvf_expense_touch_target_browser.cjs | bundle and probe | scripts/test_cvf_expense_touch_target_browser.cjs | bundle and probe | ACCEPT |
| Worker-only classification | docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json | evaluationScope and workerTaskClassification | docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json | evaluationScope and workerTaskClassification | ACCEPT |
| Forward learning | docs/reviews/learnings/CVF_ORCHESTRATOR_PREAPPROVAL_FEASIBILITY_LEARNING_2026-10-08.md | Actual Dispatch Application Observation | docs/reviews/learnings/CVF_ORCHESTRATOR_PREAPPROVAL_FEASIBILITY_LEARNING_2026-10-08.md | Actual Dispatch Application Observation | ACCEPT |
| Installed dependencies | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json | react; @playwright/test; vitest | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json | react; @playwright/test; vitest | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_dispatch_release_readiness.py; governance/compat/check_task_governance_route.py |
| literalTokensReviewed | WORKER_MUST_NOT_COMMIT; acceptance-ledger-json; Source Verification Block; COMPLETE_PENDING_REVIEW; CLOSEABLE; gateId; mutationSurface; Returned defects: NONE_RETURNED |
| gateRunPurpose | confirmation of source-verified packet structure, not first discovery |
| claimBoundary | no worker implementation or media execution proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`expense-narrow-layout`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | python governance/compat/run_adif_defect_resolver.py --task-class expense-narrow-layout --role dispatcher --lifecycle-phase pre-dispatch |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no returned registry defect; substantive STOP still retained |

## Negative Search And Collision Discipline

Named Local F5 and actual320 measurement establish retained content-box overflow, not repository-wide absence. Four new worker paths/four packet paths absent. Existing component628862 is exact mutable preimage; old test/HTML/receipt source scope preserved. Separate responsive-table defect outcome, not touch-target replay/sourceR2 reset.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private operator handoff and isolated preparation only.


## Claim Boundary

Private synthetic responsive table correction only. Default dark/Chromium at selected widths; no complete WCAG, current-source light/accent, app/real-data/AI-governance/media/provider/public/deploy/P11 claim. Input44 and filter remain fixed. Models are operator-reported worker-only observations; no orchestrator/reviewer assignment, price advantage or automatic router.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-EXPENSE-LAYOUT-20261010 --title "NCR Expense Narrow Layout" --date 2026-10-10 --base c202cc73ff97cdeb1fe57358d1438afbc623b566 --commit-mode WORKER_MUST_NOT_COMMIT --no-evidence-readiness-applicable --stdout |
| generatedProfile | web-ui-dashboard/no-commit worker |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | bounded task fields adapted from accepted existing order; scaffold retained ignored |
| checkerReadAheadConfirmation | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_independent_review_probe_admission.py |
| docOnlyNewFields | N/A with reason: fields adapted under existing owners, no new runtime contract |
| claimBoundary | authoring aid, not task execution or closure proof |

## Decision

Admit bounded existing table/cell presentation correction after clean committed bound release; no worker execution by dispatcher. Model evaluation remains worker-only, no configuration effect.

## Evidence / Verification

Named Local320 finding/pinned source/design; installed compiler/browser capability reused, exact feasibility and full authoring/release gates; own330 review probe awaits return. Full closure after actual-SHA sync.
