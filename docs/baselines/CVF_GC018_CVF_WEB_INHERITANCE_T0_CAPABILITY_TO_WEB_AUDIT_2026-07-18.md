# CVF GC-018 - CVF-WEB-INHERITANCE-T0 Capability-To-Web Audit

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: gc018

Date: 2026-07-18

Batch ID: CVF-WEB-INHERITANCE-T0

## Purpose

Authorize one read-only audit of how recent CVF capability families are or are
not inherited by `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`.

## Proposed Tranche / Decision

Release T0 inventory only. The worker creates one terminal inheritance ledger
and one no-commit worker return. No Web implementation, test edit, registry
edit, provider call, browser run, public action, or production action is
authorized.

## Scope / Target / Owner Boundary

Primary target: current cvf-web package dependencies, backend integration,
runtime-module registry, page inventory, and README.

Comparison owners: current SOT3 and MAO package roots plus accepted governed
reviews for the sibling SOT application and Four-Surface adaptation.

Worker outputs:

- `docs/reviews/CVF_WEB_INHERITANCE_T0_CAPABILITY_TO_WEB_LEDGER_2026-07-18.md`
- `docs/reviews/CVF_WEB_INHERITANCE_T0_WORKER_RETURN_2026-07-18.md`

Commit mode: `WORKER_MUST_NOT_COMMIT`.

## Capability Family Seed Manifest

| ID | Capability family | Required comparison surfaces |
|---|---|---|
| WEB-01 | SOT3 package dependency | cvf-web `package.json`; three SOT3 package roots |
| WEB-02 | SOT3 backend activation | adapter, knowledge-context route, execute route, evidence store, focused tests |
| WEB-03 | SOT3 operator visibility | all current `page.tsx` files and navigation owners |
| WEB-04 | runtime-module registry truth | `runtime-modules.ts` and focused registry tests |
| WEB-05 | MAO execution-plane inheritance | cvf-web dependencies/imports; execution-plane MAO root export |
| WEB-06 | MAO control-plane inheritance | cvf-web dependencies/imports; control-plane MAO root export |
| WEB-07 | MAO operator readout | all current pages and runtime-module registry |
| WEB-08 | Controlled Quotation service chain | accepted SOT3-APP T4/T5 reviews; cvf-web dependency/import/page search |
| WEB-09 | freeze and impact/recall projection | accepted SOT3-APP reviews; cvf-web source/page search |
| WEB-10 | Four-Surface control-boundary projection | accepted adaptation completion; cvf-web source/page search |
| WEB-11 | cvf-web README/version freshness | cvf-web README and package version |
| WEB-12 | design and QA readiness | `DESIGN.md`, current scripts, test/build owners, changed-file size risks |

The denominator is exactly 12 capability-family rows. Each must be terminal.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| SOT3 package dependencies exist in cvf-web | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | dependency rows 27-29 | `cvf-refinery`; `cvf-truth-flow`; `cvf-truth-kernel` | npm dependency map | ACCEPT |
| SOT3 real owner chain is composed | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/sot3-knowledge-adapter.ts` | imports 14-18; lifecycle function 543 onward | `evaluateSot3KnowledgeActivation` | SOT3 knowledge adapter | ACCEPT |
| execute route consumes SOT3 result and fails closed | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | knowledge activation block around 686-735 | `resolveKnowledgeContext`; `sot3.terminalOutcome` | execute route | ACCEPT |
| current page inventory and main navigation have zero audited capability terms | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/Sidebar.tsx` | main navigation groups plus repository enumeration of 41 `page.tsx` files; zero term hits at dispatch audit | `Sidebar` | main Web navigation plus enumerated app pages | ACCEPT |
| runtime registry marks Execution Plane not exposed | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts` | Execution Plane entry around 103-110 | `execution-plane-foundation`; `NOT_EXPOSED` | `MODULES` | ACCEPT |
| runtime registry marks Control and Learning partially inherited | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/runtime-modules.ts` | entries around 93-130 | `control-plane-foundation`; `learning-plane-foundation`; `PARTIAL_INHERITED` | `MODULES` | ACCEPT |
| MAO execution-plane root export exists | EXISTS | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/index.ts` | root export near 1418 | `export * from "./mao"` | execution-plane package root | ACCEPT |
| MAO control-plane root export exists | EXISTS | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/index.ts` | line 12 | `./control.plane.mao.barrel` | control-plane package root | ACCEPT |
| MAO execution package is not a cvf-web dependency | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | complete dependency map | `dependencies` | npm dependency map whose current values exclude the execution-plane package | ACCEPT |
| sibling Controlled Quotation flow is accepted | EXISTS | `docs/reviews/CVF_SOT3_APP_T5_COMPLETION_REVIEW_2026-07-18.md` | final accepted downstream application posture | `SOT3-APP-T5` | governed completion review | ACCEPT |
| Four-Surface adaptation is accepted | EXISTS | `docs/reviews/CVF_FSCB_ADAPT_T0_COMPLETION_2026-07-15.md` | final disposition | `FSCB-ADAPT-T0` | governed completion review | ACCEPT |
| cvf-web README is dated before current work | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/README.md` | version badge, quality snapshot, changelog | `1.6.0`; `2026-02-22`; `2026-02-07` | developer README | ACCEPT |
| visual implementation must follow CVF design contract | LITERAL_INVARIANT | CANONICAL_CONTRACT: root `DESIGN.md` | sections 4, 8, 9, 14 | `DESIGN.md` | canonical UI/UX contract | ACCEPT |

## New Doc-Only Fields

| Field | Allowed values |
|---|---|
| `dependencyState` | `PRESENT`; `ABSENT`; `N/A_WITH_REASON` |
| `backendWiringState` | `WIRED`; `PARTIAL`; `ABSENT`; `SIBLING_ONLY`; `N/A_WITH_REASON` |
| `registryProjectionState` | `CURRENT`; `STALE`; `MISSING`; `N/A_WITH_REASON` |
| `operatorSurfaceState` | `VISIBLE`; `PARTIAL`; `ABSENT`; `N/A_WITH_REASON` |
| `inheritanceDisposition` | `INHERITED_RUNNABLE`; `INHERITED_HIDDEN`; `PARTIAL_INHERITANCE`; `NOT_INHERITED`; `SIBLING_ADOPTION_DECISION_REQUIRED`; `DEFER_WITH_REASON` |
| `targetTranche` | `T1`; `T2`; `T3`; `T4`; `T5`; `NONE_WITH_REASON` |

## Verification / Evidence

The ledger must cite direct source path plus symbol/section for each row, state
all five evidence dimensions, reconcile exact counts to 12, distinguish
source-proven absence from search-limited absence, and name any near-threshold
files that later implementation must split or avoid expanding.

## Acceptance Criteria

- AC-01: 12/12 seed families are terminal.
- AC-02: every row reports dependency, backend, registry, operator, and final
  inheritance disposition separately.
- AC-03: SOT3 backend wiring is not erased by absent operator UI.
- AC-04: MAO package existence is not promoted into Web inheritance.
- AC-05: sibling application behavior is not cited as cvf-web runtime source.
- AC-06: T1-T5 routing is exact and reconciled.
- AC-07: no source, test, UI, package, registry, browser, or provider mutation.
- AC-08: the worker returns exactly two unstaged, uncommitted files.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | current Web and package source | read-only audit | terminal ledger | fresh implementation packet required | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | none changed | no ingress, auth, approval, receipt, mutation, or public behavior | no adapter output | parked | `N/A_WITH_REASON` |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`frontend`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class frontend --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --risk-ceiling HIGH --max-results 20 --json`

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | Status; Purpose; Proposed Tranche / Decision; Scope / Target / Owner Boundary; Capability Family Seed Manifest; Source Verification Block; New Doc-Only Fields; Verification / Evidence; Acceptance Criteria; Dual Agent Surface Matrix; ADIF Defect Registry Disclosure; Public Export Disposition; Claim Boundary |
| gateRunPurpose | confirmation after source and checker read-ahead |
| claimBoundary | dispatch evidence only; final inheritance decisions remain reviewer-owned |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-WEB-INHERITANCE-T0 --title "Capability To Web Audit" --date 2026-07-18 --base 36041a985 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | completed exact seed, source, evidence, and boundary contracts |
| checkerReadAheadConfirmation | checker paths and literal families recorded above |
| docOnlyNewFields | inheritance ledger fields named above |
| claimBoundary | dispatch-authoring provenance only |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance audit packet; no public-sync action authorized.

## Claim Boundary

This baseline authorizes one two-output read-only audit. It does not authorize
cvf-web source, test, package, UI, registry, documentation, runtime, provider,
live, browser, public-sync, push, or production mutation.
