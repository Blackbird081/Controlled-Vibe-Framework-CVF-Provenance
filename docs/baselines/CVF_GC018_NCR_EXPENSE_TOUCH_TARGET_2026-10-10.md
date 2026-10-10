# CVF GC-018 Baseline - NCR Expense Touch Target
Memory class: governed-dispatch-baseline
Status: DISPATCH_READY
Date: 2026-10-10
Batch ID: CVF-NCR-EXPENSE-TOUCH-20261010
Dispatch base head: 638aae00c3615aff772ef0702e943fbc51ea3a9e
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN
rawMemoryReleased=false

## Purpose

Correct the inherited month-input touch target in ExpenseList: accepted mobile DOM outer height38 is below DESIGN.md44. Add focused browser protection and controlled light/alternate-accent fixture coverage. Existing filter behavior and identity/order stay fixed. This is useful component maintenance, not a benchmark-only assignment or source-R2 successor.

## Scope / Target / Owner Boundary

Standing autonomous isolated UI/test and manual-transfer authority covers this bounded correction of a reviewed inherited design defect. Component input sizing only; one new browser proof script and three metadata paths. Existing unit tests, old builder/browser artifacts, dispatch pins and historical returns are read-only. Local owns independent review and subsequent model report. No app routing or real-data work.

## Authority Chain

| Source | Disposition |
|---|---|
| Operator2026-10-10 next; standing autonomous isolated tests/manual transfer; Local orchestrator/reviewer | ACCEPT |
| Paired baseline docs/baselines/CVF_GC018_NCR_EXPENSE_TOUCH_TARGET_2026-10-10.md | ACCEPT |
| Reviewed inherited defect/current tool/source pins docs/reviews/evidence/cvf-expense-touch-dispatch-inputs-2026-10-10.json | ACCEPT |
| Source R2 and effect holds | ACCEPT; retained |

## Implementation Contract

1. Modify only the month input style in EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.tsx: set height44 and boxSizing:'border-box', producing an outer target at least44px on all selected profiles. Keep date validation, filter, exports, props, source row/order, Vietnamese labels and synthetic notice intact. No padding-area trick, transform scale or wrapper min-height substitute. Preserve component smallness; changing input style does not authorize adjacent refactors.
2. New scripts/test_cvf_expense_touch_target_browser.cjs bundles the actual current component with installed Vite8/React/ReactDOM using configFile:false, envFile:false, write:false, production NODE_ENV literal, one IIFE and escaped closing-script text. Import actual tracked component path; never a rewritten filter/lookalike or frozen old component. Check its raw post-change SHA before and after every proof and record it. Test-only mutant source may be an ignored copy rebuilt separately; never mutate tracked component for mutation testing. Previous builder/browser scripts are read-only method references, not the new-source proof command.
3. Exactly five manually synthetic rows (two Feb2026, two Mar2026, invalid05/03/2026) and literal browser oracle, not imported unit expectations. New offline HTML artifacts stay ignored, <=2MiB each. System fonts/inline CSS only. Private synthetic note, existing role=note notice and native accessible Vietnamese month label retained. No app/server or external requests.
4. Four profiles: dark desktop1280x800, dark mobile390x844, light mobile390x844 and light alternate-accent mobile390x844. Dark values use DESIGN core tokens. Light fixture overrides: page#f8fafc, surface#ffffff, primary#0f172a, secondary#334155, muted#475569, border rgba(15,23,42,.12), strong border rgba(15,23,42,.24), warning#92400e. Default accent#5b5cf6; alternate#0f766e. These are explicit synthetic light/accent fixtures, not a newly claimed production light palette. One primary accent per profile; color-scheme matches theme.
5. At each profile assert actual DOM input outer height>=44 and width>=44; input/note/table within viewport with no horizontal clipping. Tab from a nonfocused page to input, verify focused element and visible focus outline using active accent token, not color alone. A small wrapper :focus-visible outline (2px accent, offset2px) is admitted; it must not change control geometry. Assert computed input foreground/background and note color resolve to selected fixture tokens. Check rendered row text foreground against actual surface and notice foreground against actual surface with local sRGB WCAG ratio>=4.5 for normal-size text. This is a targeted contrast check, not a full accessibility certification. Capture March screenshots dark/light/alternate mobile with byte hashes.
6. One ordinary March/April/clear browser flow on dark mobile asserts exact IDs, empty state/table absent, invalid row absent and no errors. Other profiles need March state/geometry/focus/token/contrast checks, not broad repeat of historical calendar suite. Block/count every nonlocal request; page/console errors, missing DOM, timeout/skipped cases fail. Installed Playwright Chromium only; contexts/browser closed in finally; no sleep as readiness or server.
7. One sizing mutant: revert input height44 to36 in an ignored source copy, keep boxSizing, rerun the same geometry assertion; fail must be an assertion for target<44, not compilation/harness. Passing baseline before and after, source hashes match each boundary. Record collected/completed/killed counts; invalid harness run counts zero. Existing date/calendar mutants are consumed from accepted evidence, not rerun.
8. Rerun the existing exact ExpenseList.test.tsx suite because the component changed; tests/config stay read-only. Preserve uppercase drive-letter cwd string used by passing prior run to avoid duplicate Vitest module identity. No full app suite/global tsc/lint. Node --check for new CJS. Caps component250/script300/guide100/evidence350/return450 lines. Guide explains new command and why the historical builder now refuses changed source; preserve old HTML/receipts and frozen pins.
9. Budget one90-minute total; timer captures UTC and monotonic before reads in its own awaited command, end AFTER separate frozen full bound confirmation and raw hash verification. Frozen tracked return/evidence must already name ignored `final-confirmation.json`; write end/elapsed/raw hashes there only. Exposed bill/tokens recorded with currency/basis; unavailable is null plus reason, never zero or an effort-based price inference.

## Acceptance Criteria

Five-path change: input outer target>=44; actual current component browser proof in four controlled token profiles; focused keyboard/token/normal-text contrast checks; valid sizing mutant kill/restoration; exact existing unit suite PASS; three hashed mobile screenshots; no external requests/errors; original filter/notice retained; full bound frozen return plus separate confirmation and complete timer provenance. Pure UI only.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Inherited target defect | docs/reviews/CVF_NCR_EXPENSE_BROWSER_PREVIEW_COMPLETION_2026-10-10.md | Findings / Position | docs/reviews/CVF_NCR_EXPENSE_BROWSER_PREVIEW_COMPLETION_2026-10-10.md | Findings / Position | ACCEPT |
| Measured input38px | docs/reviews/evidence/cvf-expense-browser-local-review-2026-10-10.json | independentProbe.monthInputHeightPx | docs/reviews/evidence/cvf-expense-browser-local-review-2026-10-10.json | independentProbe.monthInputHeightPx | ACCEPT |
| Admitted input style preimage | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.tsx | ExpenseList input style | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.tsx | ExpenseList input style | ACCEPT |
| Read-only unit regression | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.test.tsx | describe and FIXTURE | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.test.tsx | describe and FIXTURE | ACCEPT |
| Touch and theme requirements | canonical UI contract DESIGN.md | sections2,6,7,8 | DESIGN.md | sections2,6,7,8 | ACCEPT |
| Illustrative behavior intent | docs/reference/CVF_NCR_GENERAL_VIDEO_DESIGN_2026-10-02.md | S05 and S06 | docs/reference/CVF_NCR_GENERAL_VIDEO_DESIGN_2026-10-02.md | S05 and S06 | ACCEPT |
| Existing compiler method | scripts/cvf_expense_fixture_preview.cjs | bundle and buildPreview | scripts/cvf_expense_fixture_preview.cjs | bundle and buildPreview | ACCEPT |
| Worker evaluation ledger | docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json | rows and reporting | docs/reviews/evidence/cvf-worker-model-tranche-evaluation-2026-10-10.json | rows and reporting | ACCEPT |
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

Resolver query: taskClass=`expense-touch-target`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | python governance/compat/run_adif_defect_resolver.py --task-class expense-touch-target --role dispatcher --lifecycle-phase pre-dispatch |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no returned registry defect; substantive STOP still retained |

## Negative Search And Collision Discipline

Targeted named-source review establishes input38<44 defect and absent light/accent proof, not repository-wide absence. Existing original browser/helper intentionally remain historically pinned. Four new worker paths and four packet paths checked absent; existing component is exact admitted preimage. Separate mobile-touch outcome, not a source-R2 successor/counter reset.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private operator handoff and isolated preparation only.


## Claim Boundary

Private synthetic component touch correction and controlled fixture theme checks only. No production light/accent palette or complete WCAG, app/AI-governance/real-data/media/public/deploy/P11 readiness. Filter contract and historical pins/returns remain. Haiku5.5/Max preference is operator-reported metadata, not normative worker identity or cost saving. Third reviewed sample triggers preliminary report, not automatic model routing.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-EXPENSE-TOUCH-20261010 --title "NCR Expense Touch Target" --date 2026-10-10 --base 638aae00c3615aff772ef0702e943fbc51ea3a9e --commit-mode WORKER_MUST_NOT_COMMIT --no-evidence-readiness-applicable --stdout |
| generatedProfile | web-ui-dashboard/no-commit worker |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | task fields replaced using accepted prior packet structure; actual scaffold output retained in ignored dispatch runtime |
| checkerReadAheadConfirmation | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_independent_review_probe_admission.py |
| docOnlyNewFields | N/A with reason: task-specific fields adapted under existing owners, no new runtime contract |
| claimBoundary | scaffold is authoring aid, not task or closure proof |

## Decision

Admit bounded input44 correction and synthetic theme proof after clean committed bound release. Existing component preimage is admitted modified; old proof/pins remain historical. No worker execution by dispatcher.

## Evidence / Verification

Named defect/source/design reads; current dependency hash reuse, exact canonical feasibility and full authoring/release gates. Closure SHA finality explicitly follows material commit and actual-SHA sync.
