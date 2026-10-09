# CVF GC-018 Baseline - NCR Expense Filter Fixture
Memory class: governed-dispatch-baseline
Status: DISPATCH_READY
Date: 2026-10-09
Batch ID: CVF-NCR-EXPENSE-FIXTURE-20261009
Dispatch base head: d46cd676a367666bfe3abffbf25c54e327522fc0
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN
rawMemoryReleased=false

## Purpose

Implement the four expense-filter UI behaviors explicitly described in storyboard S05-S06 as a standalone React fixture and meaningful tests. No app wiring, API, model call, video asset or storyboard revision. The named value gap is that the expense behavior has no implementation/test in the inspected source regions; the accepted offline storyboard was presentation-only.

## Scope / Target / Owner Boundary

Operator standing autonomous isolated-test/continuation and manual worker transfer authority applies to this finite UI fixture. Exactly two implementation paths plus three guide/proof/return paths. Local owns technical acceptance; source R2 and effect holds remain untouched. No product route integration, HTML export change or source storyboard content acceptance is inferred.

## Authority Chain

| Source | Disposition |
|---|---|
| Operator2026-10-09: continue; manual transfer to Claude; Local orchestrator/reviewer | ACCEPT |
| Paired GC-018 baseline docs/baselines/CVF_GC018_NCR_EXPENSE_FILTER_FIXTURE_2026-10-09.md | ACCEPT |
| Accepted behavior design and pinned unit config/setup docs/reviews/evidence/cvf-expense-filter-dispatch-inputs-2026-10-09.json | ACCEPT |
| Source R2 terminal restrictions | ACCEPT; retained boundary |

## Implementation Contract

1. Named export ExpenseList in EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/expenses/ExpenseList.tsx; props expenses are readonly records with id:string, date:string, label:string, amount:number. Optional exported pure filter helper stays in this file. No production mount/import elsewhere.
2. Native month input with accessible Vietnamese label, visible list/table and no-expenses message. Empty month shows all valid rows; YYYY-MM month filters by exact year/month. Invalid dates are always excluded without crashing. Preserve supplied order/IDs; do not mutate props.
3. Dates accepted only as actual Gregorian YYYY-MM-DD calendar dates. Reject malformed text, unpadded fields and nonexistent days; no locale parser or host timezone month inference. Leap-year behavior must be tested. No persistence, requests or new dependencies.
4. Primary fixture has exactly five manually authored synthetic rows: two February2026, two March2026, one invalid date. March shows two, April empty, cleared filter four valid rows, invalid row never crashes or appears. Additional negative cases transform this same fixture; record this interpretation of all/invalid, not a change to source wording.
5. Actual React rendering tests use existing Vitest/jsdom and testing-library, not only a helper or snapshots. Show synthetic/private fixture notice; use DESIGN.md tokens for simple accessible markup. Unit tests assert behavior/content/accessibility only; no browser/responsive or AI-governance claim.
6. Source caps component200, tests350, guide100, evidence300, return450 physical lines. No extra source split foreseeable; a sixth tracked path requires dispatcher amendment. Do not modify the accepted storyboard narration, badges or source claim status.

## Acceptance Criteria

Deliver all five outputs with concrete source-backed component, four render cases, date/year/leap negatives, no props mutation and at least two killed in-memory/disposable-source mutants: removed month filtering and accepting invalid dates. Every mutant starts from the passing unchanged baseline; keep worker source hashes unchanged after sweep. A finite NOT_EXECUTED test class is not PASS.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Four behaviors and source boundaries | docs/reference/CVF_NCR_GENERAL_VIDEO_DESIGN_2026-10-02.md | S05 and S06; Claim Boundary | docs/reference/CVF_NCR_GENERAL_VIDEO_DESIGN_2026-10-02.md | S05 and S06; Claim Boundary | ACCEPT |
| Prior UI lacks expense proof | docs/reviews/CVF_NCR_OFFLINE_PREVIEW_DELIVERY_COMPLETION_2026-10-09.md | Scope / Methodology; Claim Boundary | docs/reviews/CVF_NCR_OFFLINE_PREVIEW_DELIVERY_COMPLETION_2026-10-09.md | Scope / Methodology; Claim Boundary | ACCEPT |
| Existing unit tooling | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts | test environment/setup/include | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts | test environment/setup/include | ACCEPT |
| Source/effect isolation | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts | provider-execution fetch guard; secret-safe environment setup | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts | provider-execution fetch guard; secret-safe environment setup | ACCEPT |
| UI contract | canonical UI contract DESIGN.md | theme and tokens | DESIGN.md | theme and tokens | ACCEPT |
| Forward control | docs/reviews/learnings/CVF_ORCHESTRATOR_PREAPPROVAL_FEASIBILITY_LEARNING_2026-10-08.md | Actual Dispatch Application Observation; parentFindingId | docs/reviews/learnings/CVF_ORCHESTRATOR_PREAPPROVAL_FEASIBILITY_LEARNING_2026-10-08.md | Actual Dispatch Application Observation; parentFindingId | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_dispatch_release_readiness.py; governance/compat/check_task_governance_route.py |
| literalTokensReviewed | WORKER_MUST_NOT_COMMIT; acceptance-ledger-json; Source Verification Block; COMPLETE_PENDING_REVIEW; CLOSEABLE; gateId; mutationSurface; Returned defects: NONE_RETURNED |
| gateRunPurpose | confirmation of source-verified packet structure, not first discovery |
| claimBoundary | no worker implementation or media execution proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`expense-filter-fixture`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | python governance/compat/run_adif_defect_resolver.py --task-class expense-filter-fixture --role dispatcher --lifecycle-phase pre-dispatch |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE_RETURNED |
| Dispatch impact | no returned registry defect; substantive STOP still retained |

## Negative Search And Collision Discipline

Targeted filename search in EXTENSIONS/scripts/review evidence found no ExpenseList/expense demo fixture. This is not corpus absence/completeness proof. All exact new packet/worker paths checked absent. Existing Print/navigation E2E tests inspected; no duplicate rerun selected. Independent storyboard unit-fixture identity; source-R2 STOP is not renamed or reset.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private operator handoff and isolated preparation only.


## Claim Boundary

Private standalone unit UI fixture only; two implementation paths and three metadata artifacts, not an actual two-file-only governance run. No app integration, E2E workflow, CVF AI-governance behavior, real ledger, browser/print/paper, media/live/public claim. Source R2/counters and native/provider/media holds unchanged. Tokens/bill unknown; no Haiku-versus-Sonnet superiority or savings claim.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-EXPENSE-FIXTURE-20261009 --title "NCR Expense Filter Fixture" --date 2026-10-09 --base d46cd676a367666bfe3abffbf25c54e327522fc0 --commit-mode WORKER_MUST_NOT_COMMIT --no-evidence-readiness-applicable --stdout |
| generatedProfile | web-ui-dashboard/no-commit worker |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | reuse verified prior packet role/closeability contracts; replace all task-specific scope, ledger, source and fixture sections |
| checkerReadAheadConfirmation | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_independent_review_probe_admission.py |
| docOnlyNewFields | NONE |
| claimBoundary | authoring provenance only |

## Decision

Release the five-output fixture after committed bound pre-dispatch and continuity. Existing isolated testing/manual worker-transfer authority covers this reversible unit development; no repeat operator approval. No implication of source/native/demo/media release.

## Evidence / Verification

Pinned inputs; installed tooling availability; actual-order binding positive/missing-plan negative; explicit canonical feasibility and authoring/release gates. Dispatcher creates no implementation fixture.
