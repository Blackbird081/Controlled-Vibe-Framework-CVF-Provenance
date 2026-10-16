# CVF GC-018 Baseline - NCR HTML Main-Entry Cache Source Correction

Memory class: governed-baseline
docType: baseline
Status: DISPATCH_READY
Date: 2026-10-17
Batch ID: CVF-NCR-HTML-MAIN-ENTRY-CACHE-SOURCE-20261017
Dispatch inspection base: 1cc2700d2d6944f2499366126855f7034434c3a9
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN
rawMemoryReleased=false

## Purpose

Correct two source defects exposed by the spent fresh BE-R01 cap2 result. `journey.cjs` preloads the same W05 entry file that Node later selects as main; its preload guard returns at `require.main !== module` and the cached record prevents main/browser execution. Separately, the HTTP evaluate observer parses an empty readiness GET body as JSON inside an asynchronous handler. Root retained `web.log` SHA256 `bbf63992aaf68602882ce5487042b1090398e78107087a8e60e462771b48762c` with GET `/api/governance/evaluate` 405 and three uncaught `Unexpected end of JSON input` exceptions. The actual failed run had no `browser.json`, `SNAPSHOT`, Chrome observation, exports or evaluates. Its exit0 is a failed result, not acceptance. This source correction does not retry BE-R01 or admit a new browser actor.

## Authority And Dependency

Consumer: `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_MAIN_ENTRY_CACHE_SOURCE_2026-10-17.md`. Accepted Windows source pair/release remain immutable: `docs/baselines/CVF_GC018_NCR_HTML_WINDOWS_SOURCE_2026-10-16.md`, `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_WINDOWS_SOURCE_2026-10-16.md`, `docs/reviews/evidence/ncr-html-windows-source-release-20261016.json` SHA256 `ab30a0de37c4f93832117833f1e7093d9a97c2f3e8d08ae7325f0047230cfc9c`. Existing source13/adjunct5 members remain fixed. Root must first close the spent r1b return with its failed actual evidence and ensure the active lane is released. The new source pair requires a separate dispatch/continuity commit and bound pre-implementation gate before any worker edit or Node fixture.

## Locked Action Contract

1. Worker may edit only existing `scripts/cvf_ncr_html_owned_profile/journey.cjs`, `scripts/cvf_ncr_html_owned_profile/journey.test.cjs`, `scripts/cvf_ncr_html_owned_profile/source_release.py`, and the exact authority assertion in `scripts/test_cvf_ncr_html_effect_driver.py`; produce exactly two return/evidence files. No new source family, product edit, driver/fence edit, runtime actor, provider, deletion, or cap1.
2. In `journey.cjs::installOwnedGuard`, require the existing `probe_cvf_w05_browser_chain.cjs` to install the base egress guard, then remove **only its resolved cache key** if `process.argv[1]` exactly identifies that future main entry. Keep journey-first/browser-fence-second preload order and every installed guard. Ordinary library import/different main must not evict. If this narrow seam fails actual Node evidence, return a blocked source result; do not substitute a new launcher.
3. Worker adds one finite RED/GREEN native Node entry-as-main regression using pinned physical Node, the actual pinned browser entry, single journey preload and new ignored custody, plus pure library-import/different-main regression. The RED observation must capture current exit0/no-main-marker behavior; GREEN must capture one guard installation and one main marker without browser/service. This isolated fixture omits the second browser-fence preload, which requires full browser binding/config/hash; accepted ordered-preload proof remains in force. Worker may not mutate the pinned browser entry or launch Chrome/Next/engine. Root independently authors one different native Node probe with its own budget/custody, consuming worker evidence without rerunning the worker suite.
4. In the same `journey.cjs::installOwnedGuard` HTTP observer, only consume actual `POST /api/governance/evaluate` requests. Preserve valid POST `evaluate-recipient` observation. Empty/malformed POST bodies must not throw from the asynchronous `end` handler or become a valid evaluate-recipient; any invalid log uses a distinct event with bounded metadata and no raw body. Add pure GET-empty, malformed-POST and valid-POST regressions in the existing journey test. No new observer owner or extra runtime.
5. `source_release.AUTHORITY` becomes exactly this new B/W pair. Worker updates only the old hard-coded authority assertion in `scripts/test_cvf_ncr_html_effect_driver.py` to the new pair, preserving test meaning and all other test content. Worker leaves `scripts/cvf_ncr_html_effect_fence.py` release constants unchanged. Old native `worker-native-budget.json` fixture opened with `x` is not reusable.
6. Root freezes accepted B/W bytes without final release/hash backedge; computes a new `SOURCE_IDENTITY_ONLY` manifest from current source13/product/entry/spec/new B/W; updates only `F.RELEASE`/`F.RELEASE_SHA`; joins source13/adjunct5 current hashes and independent probe; writes Local CP/LP and BE-S09 support roadmap disposition. A new runtime grant and fresh qualification are separate decisions. Existing cap2 controls9/26 cannot be reused against changed source until separately qualified.

## Exact Artifact And Owner Boundary

Worker exact6: the four existing source/test paths above, `docs/reviews/CVF_NCR_HTML_MAIN_ENTRY_CACHE_SOURCE_WORKER_RETURN_2026-10-17.md`, `docs/reviews/evidence/ncr-html-main-entry-cache-source-worker-20261017.json`. Root final expected material19: worker6; new release1; `scripts/cvf_ncr_html_effect_fence.py`1; B/W2; CP/LP2; roadmap1; source6. Source union18 remains fixed, selected5/other13. Worker return ledger stays exact6. Root owns all commits and release calculation; worker must not commit. No tracked source edit while prior BE-R01 worker owns its lane.

## Evidence, Cost And Stop

Finite worker budget proposal: one pure CJS test selection without inherited `CVF_NCR_ALLOWED_PORTS`/`CVF_HCR_EGRESS_LOG`; one RED and one GREEN physical Node start in new ignored worker custody, each <=10 seconds, total native <=60 seconds, retry0. Root independent probe: one physical Node start <=10 seconds, native total <=30 seconds, retry0. Pin actual Node path/hash before each start; ledger STARTING before process start and retain raw stdout/stderr/exit/duration/marker hashes. Select only named changed-seam tests; avoid the legacy one-time Windows fixture collection. A failed/ambiguous start spends its bounded slot. Worker then full bound return gate. Root consumes worker evidence under M5/M10/safety/M20, probes once, and performs independent final source identity join. No old browser grant replay or new actual runtime run belongs here.

## Parent And Claim Boundary

Parent generation9/SCECordinal2/counters2,0,2,0/two blockers/freeze/prior7/LHW24 retained unchanged. This source task can have its own initial local SCEC block but cannot reset the parent chain. BE-R01 remains failed/open until a later new-source runtime grant returns actual proof. BE-S09 is support only; BE-R02 cap1 remains deferred. Public export disposition: `DEFERRED_PRIVATE_ONLY`. No AI governance, release, production, cross-runtime determinism, provider, or business acceptance claim.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: new source-correction B/W, BE-S09 in-progress support and current6 raw authority/mode/next only at dispatch; no worker source change in this metadata commit.
Protected paths:
- `docs/baselines/CVF_GC018_NCR_HTML_MAIN_ENTRY_CACHE_SOURCE_2026-10-17.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_MAIN_ENTRY_CACHE_SOURCE_2026-10-17.md`
- `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`
- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`
Operator authorization: current Local source-only continuation after closed spent BE-R01 first result; standing root author/reviewer/steward authority.
Rollback boundary: exact listed metadata only; prior worker2/CP/LP/BW, source18/accepted Windows source B/W/releases/qualification/old grants and custody unchanged. gen9/SCECordinal2/counters2,0,2,0/blockers2/freeze/prior7 exclusions/LHW24 and R1/R2partial,R3/R4open,R5/R6deferred unchanged; old1spent/2retired and fresh r1b spent blocked retained.

## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST

Atomicity reason: new source-only authority, BE-S09 support-in-progress and source-generated current raw B/W/mode/next align in dispatch9; following actual material SHA continuity exact6.

Exact changed manifest:

- `docs/baselines/CVF_GC018_NCR_HTML_MAIN_ENTRY_CACHE_SOURCE_2026-10-17.md`
- `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_MAIN_ENTRY_CACHE_SOURCE_2026-10-17.md`
- `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`
- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Rollback boundary: listed metadata only; no production-source, old evidence, runtime or resource effect.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, maxResults=`100`.
Resolver command: `python -B governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 100 --json`.
Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0056, ADIF-0057, ADIF-0058, ADIF-0061, ADIF-0062, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006. Root actual exit0, raw .cvf/runtime/ncr-be-fresh-runtime-20261016/main-entry-source-adif.log SHA256 669a86021fd61cb8fd91fba96e39dce168ebd62345ac043d635612a531b3b687. Existing source/ownership/complete-manifest/budget/return-route/readiness/first-failure rules apply; no all-entry-body-read claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY. Private source correction only.

## Scope / Target / Owner Boundary

Worker exact6 and Local final19 per Locked Action Contract; Local owns final source identity and commits. No product runtime or old actor replay.

## Source / Predecessor Evidence

Closed failed BE-R01 Local completion and proof, accepted Windows source pair/release, and current journey/entry source are the governed predecessors. Root Refreshed Dependency Release binds actual closure commits and receipt hashes at adoption.

## Decision / Proposed Tranche

Admit the bounded existing-owner bootstrap and HTTP observer source correction; support BE-S09 remains open until real source proof and independent Local acceptance.

## Evidence / Verification

Worker RED/GREEN actual Node main-entry, selected pure observer/identity tests and frozen full return gate; Local separate one-start native probe and new source release identity join. Existing accepted controls do not prove changed-source runtime.

## Claim Boundary

Source correction only; BE-R01/R02 open, no automatic control qualification, browser runtime, provider, deletion or public claim.

## Root Refreshed Dependency Release

Actual closed failed predecessor: material `6d5ffd0a9a7fb04b99f9f594ca35f1fabbfc4504`, actual-SHA continuity `1cc2700d2d6944f2499366126855f7034434c3a9`; both exact13/6 split gate records exit0/raw-hash verified. Frozen worker2/Local CP-LP and old authority remain failed immutable evidence, not acceptance. New dispatch inspection/base HEAD `1cc2700d2d6944f2499366126855f7034434c3a9` is not worker executionBaseHead. Source18 raw before-hashes are retained in ignored adoption state. Root selected this finite source-only correction; no runtime/cap1/provider/deletion/retry. Preparation-inclusive start `2026-10-16T17:10:00Z`; worker90min hard `2026-10-16T18:40:00Z`; Local180min hard `2026-10-16T20:10:00Z`; no reset. Actual fresh dispatcher ADIF result .cvf/runtime/ncr-be-fresh-runtime-20261016/main-entry-source-adif.log SHA256 669a86021fd61cb8fd91fba96e39dce168ebd62345ac043d635612a531b3b687.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local INTERNAL_AGENT dispatcher/reviewer/steward |
| Provider or surface | private shared workspace |
| Session or invocation | ncr-main-entry-source-material-20261017 |
| Working directory | repository root |
| Command or tool surface | root-reviewed source packet derivative, git status --short, actual prior-result/dependency/ADIF metadata joins and canonical current6 generation; gates/commits separately owned by root |
| Target paths | `docs/baselines/CVF_GC018_NCR_HTML_MAIN_ENTRY_CACHE_SOURCE_2026-10-17.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_MAIN_ENTRY_CACHE_SOURCE_2026-10-17.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Allowed scope source | Local next source-correction continuation; current new exact source-only order after spent-result split closure |
| Before status evidence | HEAD 1cc2700d2d6944f2499366126855f7034434c3a9; clean worktree; git status --short empty at admission; prior blocked result13/6 split PASS consumed, source18 before-image unchanged |
| After status evidence | conditional source-only worker release, no code/test/native start or source acceptance |
| Diff evidence | exact9 material manifest |
| Approval boundary | new source exact6 worker only after committed bound authority/preimplementation; fixture budgets in W, no runtime/cap1/provider/deletion/retry |
| Claim boundary | source dispatch is not corrected source, support completion or BE-R01 outcome |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-main-entry-source-material-20261017 |
| Expected manifest | `docs/baselines/CVF_GC018_NCR_HTML_MAIN_ENTRY_CACHE_SOURCE_2026-10-17.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_MAIN_ENTRY_CACHE_SOURCE_2026-10-17.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Actual changed set | `docs/baselines/CVF_GC018_NCR_HTML_MAIN_ENTRY_CACHE_SOURCE_2026-10-17.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_MAIN_ENTRY_CACHE_SOURCE_2026-10-17.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Manifest delta | MATCH exact9 |
| Deletion or rename disposition | none; prior stage/custody/failed proof preserved |

## Preparation History Preservation

Candidate and prior adopted source/runtime packet preparation limitations remain as recorded; root must consolidate any remaining candidate defects before release. Prior failed helper/adoption/gate logs are retained, not new capability or retroactively perfect procedure. No source edit/test/native/runtime by this metadata helper. Actual prior-result split PASS is consumed; no duplicate gates/proof rerun by adoption.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python -B governance/compat/build_dispatch_packet_scaffold.py --help` |
| generatedProfile | generic-worker-dispatch; INTERNAL_AGENT; WORKER_MUST_NOT_COMMIT |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: reviewed existing passing qualification guard sections and explicit new source correction; no new helper skeleton used |
| checkerReadAheadConfirmation | named failed predicates and canonical current sections read before this consolidated repair |
| docOnlyNewFields | new source task/deadlines and finite fixture budgets, no source schema |
| claimBoundary | actual CLI help exit0; no generated skeleton or runtime proof claimed; initial packet gaps retained |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_semantic_convergence_control.py; governance/compat/route_task_governance.py; accepted Windows source work order controls |
| literalTokensReviewed | cvf.workOrderAcceptanceLedger@1.0.0; cvf.semanticConvergenceControl.v1; cvf.taskGovernanceManifest.v1; required exact worker and root paths |
| gateRunPurpose | root confirmation after consolidated source/literal review; gate evidence confirms artifact shape, no native behavior proof |
| claimBoundary | targeted read and literal reuse; no all-checker read claim |
