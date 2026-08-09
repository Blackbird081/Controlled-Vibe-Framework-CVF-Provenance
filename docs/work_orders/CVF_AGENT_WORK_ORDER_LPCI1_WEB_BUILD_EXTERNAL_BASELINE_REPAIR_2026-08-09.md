# CVF Agent Work Order - LPCI1 Web Build External Baseline Repair

Date: 2026-08-09
Work order: LPCI1-WEB-BR1
Status: DISPATCH_READY
Memory class: POINTER_RECORD
Authority: `AUTHORIZE_LPCI1_WEB_BUILD_EXTERNAL_BASELINE_REPAIR`; bounded waivers `AUTHORIZE_BOUNDED_WAIVER_SYSTEM_CHAIN_FRESHNESS_FOR_LPCI_BR1` and `AUTHORIZE_BOUNDED_WAIVER_AS_BUILT_CATALOG_DRIFT_FOR_LPCI_BR1`
Dispatch base: `d9497c5db`
Branch: `codex/lpci1-web-br1`
Route: `MULTI_AGENT_MULTI_ROLE`
Commit mode: WORKER_MUST_NOT_COMMIT

## Dispatch Prompt Envelope

Role: no-commit implementation worker for LPCI1-WEB-BR1.

Canonical packet:
`docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_BUILD_EXTERNAL_BASELINE_REPAIR_2026-08-09.md`

Paired baseline:
`docs/baselines/CVF_GC018_LPCI1_WEB_BUILD_EXTERNAL_BASELINE_REPAIR_2026-08-09.md`

Commit mode: WORKER_MUST_NOT_COMMIT.

executionBaseHead: WORKER_MUST_CAPTURE_COMMITTED_DISPATCH_HEAD_AT_START.

Current-time notes: date is 2026-08-09; dispatch source base is `d9497c5db`;
the packet remains untracked and uncommitted. Both canonical pre-dispatch
blockers - system-chain map freshness and as-built catalog/gap-index drift -
are released within their bounded scopes by the two operator waivers named
in Authority above. The packet is not yet committed; the worker still
requires the reviewer to commit and hand off the exact committed base
before pre-implementation.

Required first actions: the two operator bounded waivers
`AUTHORIZE_BOUNDED_WAIVER_SYSTEM_CHAIN_FRESHNESS_FOR_LPCI_BR1` and
`AUTHORIZE_BOUNDED_WAIVER_AS_BUILT_CATALOG_DRIFT_FOR_LPCI_BR1` have waived
both canonical pre-dispatch failures within this packet's exact scope -
after the reviewer commits this packet and hands off the exact committed
base, read the packet and baseline completely; capture base, branch, and
clean status; verify the exact manifest and local runner; rerun ADIF; run
pre-implementation; then edit only worker-owned paths.

Return contract: change only the exact ten repair paths, create exactly the
one worker return, leave all changes unstaged and uncommitted, and return
one exact terminal disposition.

Prepared implementation instructions only. Do not execute them until the
reviewer has committed this packet and handed off the exact committed base.
After reviewer packet commit and exact-base handoff, implement only the
ten-file baseline repair defined here in the isolated clean worktree, run
the required local non-live checks, write exactly the worker-return
artifact, and stop without staging or committing.

Do-not-misread notes:

- `external baseline` means external to the LPCI1-WEB-B1 feature manifest, not
  external repository/provider/network authority;
- the reviewer chat result is a human checkpoint, not canonical source;
- the pending B1 worker return in another dirty workspace is not an input file
  to this isolated worker;
- the fourteen B1 dirty paths are integration exemptions and forbidden here;
- failing test stack traces through route/gateway production code do not grant
  permission to edit production route/gateway logic;
- local pnpm means the already available package-owned runner only; no `npx`,
  install, registry access, network, provider, or live execution.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id LPCI1-WEB-BR1 --title "LPCI1 Web Build External Baseline Repair" --date 2026-08-09 --base d9497c5db --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | generic no-commit local source/test repair dispatch |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | Current template and precedent were specialized for the exact ten-file repair and dirty-set integration controls |
| checkerReadAheadConfirmation | applicable dispatch, source, handoff, trace, worker-return, closure, and file-size checker sources reviewed |
| docOnlyNewFields | packet-local routing vocabulary isolated in New Doc-Only Fields |
| claimBoundary | scaffold provenance only; no implementation or integration claim |

## Purpose

Remove four deterministic execute-suite failures caused by three reset audit
mocks returning no event identifier, and remove ten lint errors across seven
files by replacing explicit `any` with exact local types. Preserve all runtime
route/gateway logic and the separate B1 feature diff.

## Authority Chain

1. Operator authority: `AUTHORIZE_LPCI1_WEB_BUILD_EXTERNAL_BASELINE_REPAIR`.
2. GC-018 baseline named in Scaffold Provenance.
3. This work order.
4. One no-commit implementation worker.
5. One reviewer/closer who owns acceptance, integration, closure evidence, and
   authorized local dispatch/repair/integration/closure/session-sync commits.

The original repair token alone authorizes only this exact repair and local
non-live proof and excludes commit authority. The two later bounded waivers
grant Codex reviewer-only local dispatch, repair, integration, closure, and
session-sync commits. They do not authorize route/gateway production changes,
provider/live/network, package/configuration changes, public sync, release, or
any worker commit.

## Agent Roles

| Role | Owner | Responsibility |
|---|---|---|
| Dispatcher/reviewer | Primary reviewer | Source/packet control, dispatch, review |
| Implementation worker | One assigned worker | Exact ten-file repair, verification, worker return, no commit |
| Reviewer/integration closer | Primary reviewer | Diff acceptance, combined B1 integration, closure proof, and authorized local commits |

## Scope / Target / Owner Boundary

Target: three execute test mocks and ten lint errors in seven files.

The worker owns only the ten listed source/test paths and the exact worker
return. The reviewer owns the completion packet, integration action, any
authorized continuity update, staging, and commit.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| Operator authority | Exact token above | SATISFIED |
| Clean isolated base | `d9497c5db`, `codex/lpci1-web-br1`, initially empty status | SATISFIED |
| Canonical pre-dispatch | `check_system_chain_map_freshness.py` returned `SOURCE_DRIFT` with 10 fingerprint mismatches; unconditional and no changed-range exclusion | WAIVED_BOUNDED - operator waiver applies only to LPCI1-WEB-BR1; gate remains NON-COMPLIANT and not PASS |
| As-built catalog/gap-index freshness | `check_as_built_system_catalog_drift.py` returned aggregate and gap-index drift in the canonical pre-dispatch run | WAIVED_BOUNDED - released by operator waiver `AUTHORIZE_BOUNDED_WAIVER_AS_BUILT_CATALOG_DRIFT_FOR_LPCI_BR1`; catalog/gap-index remain NON-COMPLIANT and are not represented as PASS |
| B1 bounded-source review | Reviewer communicated `PASS_FOR_BOUNDED_SOURCE` in chat | HUMAN_CHECKPOINT_ONLY_NOT_SOURCE_AUTHORITY |
| B1 worker return | Pending uncommitted external artifact at `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD_WORKER_RETURN_2026-08-09.md` in the separate B1 workspace | PENDING_EXTERNAL_INTEGRATION_EVIDENCE |
| Failure evidence | Direct source audit and independent local non-live reproduction at clean base | SATISFIED |

The worker must not cite chat or the pending B1 artifact as repository source.
The reviewer must revalidate the actual dirty B1 diff during integration.

## Canonical Pre-Dispatch Failure Evidence

The canonical pre-dispatch run on 2026-08-09 passed all packet-local gates but
failed `governance/compat/check_system_chain_map_freshness.py` with
`Freshness state: SOURCE_DRIFT` and 10 fingerprint mismatches. The failing gate
is unconditional in the canonical workflow and has no changed-range exclusion.

The same canonical run failed
`governance/compat/check_as_built_system_catalog_drift.py` for the as-built
catalog aggregate and gap index. That separate failure was not covered by
the system-chain waiver alone; it is released below by its own operator
waiver.

## Operator Bounded Waiver - AUTHORIZE_BOUNDED_WAIVER_SYSTEM_CHAIN_FRESHNESS_FOR_LPCI_BR1

The operator issued an explicit bounded waiver on 2026-08-09 for this exact
failure. The waiver is recorded verbatim by field:

| Field | Operator-recorded value |
|---|---|
| Authorization token | `AUTHORIZE_BOUNDED_WAIVER_SYSTEM_CHAIN_FRESHNESS_FOR_LPCI_BR1` |
| Failed gate named | `governance/compat/check_system_chain_map_freshness.py` (system chain map freshness) |
| Reason | LPCI BR1 is blocked by 10 pre-existing MSEA-R90 SOURCE_DRIFT findings outside its manifests. Independent review confirms a mixture of CRLF/LF byte drift and genuine documentation deltas; updating fingerprints now could create platform-specific or semantically unreviewed evidence. |
| Bounded scope | permit only LPCI1-WEB-BR1 packet dispatch, its exact 10-file external-baseline repair, integration with the existing reviewed 14-path LPCI B1 diff, and deterministic non-live closure checks. |
| Accepted risk | system-chain freshness remains NON-COMPLIANT and must not be represented as PASS, waived globally, or used as release/live/public evidence. |
| Follow-up owner | Codex reviewer must open a separate governed cross-platform fingerprint and MSEA-R90 semantic reconciliation batch. |
| Separate parked finding | as-built catalog aggregate and gap-index drift require their own governed reconciliation batch and are not covered by this waiver. |
| Commit authority | Codex reviewer may create local governed dispatch, repair, integration, closure, and session-sync commits. Workers must not commit. |
| Forbidden under this waiver | checker weakening, fingerprint rewriting, runtime gateway changes, provider/live/network, persistence, vector/RAG, corpus mutation, public-sync, push, or deployment. |

The system-chain dependency is `WAIVED_BOUNDED` within the exact scope
above. The waiver does not certify
`governance/compat/check_system_chain_map_freshness.py` as passing and does
not apply to any other packet, checker, fingerprint, runtime, provider, or
public-facing surface. A fresh canonical pre-dispatch run against this
packet after 2026-08-09 is still expected to report `Freshness state:
SOURCE_DRIFT` for the same 10 fingerprints; that expected, disclosed, and
waived failure is not a new blocking condition.

## Operator Bounded Waiver - AUTHORIZE_BOUNDED_WAIVER_AS_BUILT_CATALOG_DRIFT_FOR_LPCI_BR1

The operator issued a second explicit bounded waiver on 2026-08-09 for the
as-built catalog/gap-index drift failure. The waiver is recorded verbatim
by field:

| Field | Operator-recorded value |
|---|---|
| Authorization token | `AUTHORIZE_BOUNDED_WAIVER_AS_BUILT_CATALOG_DRIFT_FOR_LPCI_BR1` |
| Failed gate named | `governance/compat/check_as_built_system_catalog_drift.py` (as-built system catalog drift) |
| Reason | pre-existing generated aggregate and gap-index drift are outside LPCI BR1 manifests. |
| Bounded scope | LPCI BR1 dispatch, exact 10-file baseline repair, integration with the reviewed 14-path B1 diff, and deterministic non-live closure. |
| Accepted risk | catalog aggregate and gap index remain non-compliant and must not be claimed as PASS, release evidence, or public evidence. |
| Follow-up owner | Codex reviewer must open a separate governed as-built catalog reconciliation batch. |
| Commit authority | Codex reviewer may perform local governed commits; workers must not commit. |

This waiver releases the as-built catalog/gap-index drift dependency for
LPCI1-WEB-BR1 within the bounded scope above. With both waivers recorded,
worker dispatch and pre-implementation are released for this packet's exact
ten-file repair, pending only the reviewer's packet commit and exact-base
handoff. Neither waiver certifies its named gate as passing, extends to any
other packet or batch, or authorizes checker weakening, aggregate/index
rewriting outside a proper regeneration command, runtime gateway changes,
provider/live/network, persistence, vector/RAG, corpus mutation,
public-sync, push, or deployment.

Canonical autorun isolation rule: because the bundled pre-dispatch workflow can
silently regenerate
`docs/reference/system_architecture_catalog/CVF_AS_BUILT_SYSTEM_CATALOG_AGGREGATE.json`
and `docs/reference/system_chain/gaps/CVF_SYSTEM_CHAIN_GAP_INDEX.json` as a
side effect, run canonical autorun only in a disposable clean verification
worktree at the committed dispatch HEAD. Record the expected two waived
NON-COMPLIANT failures there, verify any dirty paths are limited to those known
generated side effects, and remove the verified disposable worktree. Do not run
that mutating bundle in the exact worker execution lane; its status and content
must remain unchanged before worker handoff.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intakeSummary | bounded LPCI1-Web external-baseline source/test repair |
| scopeClassification | three deterministic execute tests and seven TypeScript/TSX lint files |
| riskSensitivity | R1 local test/type repair; production route/gateway and external surfaces forbidden |
| selectedRouteMode | MULTI_AGENT_MULTI_ROLE |
| roleSeparationBasis | dispatcher/reviewer; one no-commit implementation worker; reviewer/integration closer |
| escalationCondition | wrong/dirty base, missing runner, stale source, extra path, production/config need, B1 collision, or gate failure outside scope |

## Required First Reads

1. `AGENTS.md`;
2. `CVF_SESSION_MEMORY.md`;
3. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`;
4. `CVF_SESSION/ACTIVE_SESSION_STATE.json` and its named active handoff;
5. `docs/reference/guard_orientation/README.md`;
6. `docs/reference/CVF_AGENT_WORK_ORDER_TEMPLATE_2026-05-19.md`;
7. `docs/reference/CVF_GOVERNED_ARTIFACT_LITERAL_FORMAT_GOTCHAS_2026-06-25.md`;
8. `docs/reference/CVF_AGENT_AUTORUN_WORKFLOW_CONTROL_STANDARD_2026-05-28.md`;
9. `docs/reference/CVF_AGENT_COMMIT_STEWARD_PROTOCOL_STANDARD_2026-06-15.md`;
10. `docs/reference/CVF_WORK_ORDER_CLOSURE_QUALITY_GATE_STANDARD_2026-05-28.md`;
11. the baseline, Source Verification Block, exact manifests, and all ten writable files;
12. the canonical AHB contract cited by exception in its control block.

## Pre-Flight Checks

Only after reviewer packet commit and exact-base handoff, before editing, the worker must:

1. record `git rev-parse --short HEAD`, branch, and full status;
2. verify the worktree is the isolated BR1 lane and the fourteen B1 paths are absent;
3. verify exact ten source/test paths plus one worker return as writable;
4. rerun the worker ADIF query and disclose all returned defect IDs;
5. run canonical `pre-implementation` against a real changed input range;
6. confirm an existing local pnpm/package dependency environment without install;
7. if unavailable, return `BLOCKED_LOCAL_RUNNER_UNAVAILABLE` without broadening scope.

## ADIF Defect Registry Disclosure

Dispatcher query:
`python governance/compat/run_adif_defect_resolver.py --task-class "baseline repair" --role dispatcher --lifecycle-phase pre-dispatch --json`

Resolver query: taskClass=`baseline repair`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

Worker query:
`python governance/compat/run_adif_defect_resolver.py --task-class "baseline repair" --role worker --lifecycle-phase pre-implementation --json`

Returned defects: NONE_RETURNED

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Diagnostics suite declares the owned audit mock | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.diagnostics.test.ts` | line 10 | `appendAuditEventMock` | diagnostics test mock | ACCEPT |
| Governance-trace suite declares the owned audit mock | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.governance-trace.test.ts` | line 7 | `appendAuditEventMock` | governance-trace test mock | ACCEPT |
| VI5 suite declares the owned audit mock | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.vi5-t1-language-state.test.ts` | line 10 | `appendAuditEventMock` | VI5 test mock | ACCEPT |
| Stable execute suite declares the same audit mock symbol | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts` | line 10 | `appendAuditEventMock` | execute route test mock | ACCEPT |
| Home browse production icon prop is explicit `any` | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/home/HomeBrowseExperience.tsx` | line 40, `HomeBrowseExperienceProps` | `icon` | `HomeBrowseExperienceProps` | ACCEPT |
| Existing local component contract uses concrete Lucide type | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/sidebar/SidebarNavItem.tsx` | lines 5 and 20 | `LucideIcon` | `SidebarNavItemProps` | ACCEPT |
| Package scripts own lint, check, and non-live test execution | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json` | lines 5-16, `scripts` | `scripts` | package scripts | ACCEPT |

## Current Runtime Freshness Verification

Independent local focused execution produced three failing files, four failing
tests, and one passing candidate file. The exact owned failures are diagnostics
(two), governance-trace (one), and VI5 language-state (one). Every failure
stacks through `evaluateRouteMandatoryGateway` reading an undefined event
identifier. Actor-gate passed and is not writable.

Independent lint execution produced ten errors in the exact seven lint files.
The five dashboard test facts are recorded in the diagnostic ledger below
rather than as parenthesized Source Verification paths, while their current
source lines were directly inspected.

## Clean-Base Diagnostic Ledger

| Path | Current defect | Bounded repair |
|---|---|---|
| `src/app/api/execute/route.diagnostics.test.ts` | reset mock returns undefined; two failures | deterministic nonempty audit event ID |
| `src/app/api/execute/route.governance-trace.test.ts` | reset mock returns undefined; one failure | deterministic nonempty audit event ID |
| `src/app/api/execute/route.vi5-t1-language-state.test.ts` | reset mock returns undefined; one failure | deterministic nonempty audit event ID |
| `src/app/(dashboard)/artifacts/page.test.tsx` | line 9 explicit `any` | exact `currentStep` prop type |
| `src/app/(dashboard)/governance/knowledge/page.test.tsx` | line 9 explicit `any` | exact `currentStep` prop type |
| `src/app/(dashboard)/help/page.test.tsx` | lines 10 and 16 explicit `any` | exact title/subtitle and currentStep prop types |
| `src/app/(dashboard)/knowledge/intake/page.test.tsx` | line 9 explicit `any` | exact `currentStep` prop type |
| `src/app/(dashboard)/work-transfer/page.test.tsx` | line 9 explicit `any` | exact `currentStep` prop type |
| `src/components/home/HomeBrowseExperience.test.tsx` | lines 9, 13, and 14 explicit `any` | exact mock prop types sourced from rendered values |
| `src/components/home/HomeBrowseExperience.tsx` | line 40 explicit `any` | `LucideIcon` or source-backed concrete equivalent |

Warnings outside these ten errors are not owned and must not be opportunistically
edited.

## Negative Search And Collision Discipline

- Search the changed set for `eslint-disable`, `@ts-ignore`, `@ts-expect-error`,
  ` as ` casts added by this tranche, and new explicit `any`.
- Search Git diff for package/config/lockfile changes and fail if found.
- Search Git status for any path outside the exact fulfillment manifest.
- Do not invent a shared helper or widen a public production contract to avoid
  a small local test-prop type.

## New Doc-Only Fields

| Field | Meaning |
|---|---|
| `LPCI1-WEB-BR1` | Packet-local repair batch identifier |
| `HUMAN_CHECKPOINT_ONLY_NOT_SOURCE_AUTHORITY` | Non-canonical chat checkpoint |
| `PENDING_EXTERNAL_INTEGRATION_EVIDENCE` | Artifact pending in another dirty workspace |
| `BLOCKED_LOCAL_RUNNER_UNAVAILABLE` | Existing local runner/dependency tree cannot execute and install is forbidden |

No row in this table is an existing runtime field or implementation request.

## Protocol / Contract / Requirements

### Execute Test Repair

For each of the three owned execute suites, preserve all existing test purpose,
inputs, assertions, environment cleanup, and production imports. After reset,
configure `appendAuditEventMock` to resolve an object containing a stable,
suite-local, nonempty `id`. Do not randomize or use clock/process-derived IDs.
Do not edit the route, gateway, audit store, or production contracts.

### Lint Repair

Replace only the ten explicit-`any` errors with exact local prop shapes. Prefer
the narrowest inline object type where a test mock only renders one or two
fields. For `statCards.icon`, import and use `LucideIcon` or an equally concrete
type verified from existing source. Do not cast, suppress, weaken ESLint, or
change configuration.

### Integration Contract

The isolated worker must see none of the fourteen dirty B1 paths. The reviewer
must later prove the BR1 diff is exactly the ten repair paths, integrate without
editing/reverting the B1 set, and rerun both BR1 proof and the original B1
seven-suite/99-test proof on the combined state. A collision, unexplained path,
or changed test count returns to reviewer; it is not worker autonomy.

## Roadmap-To-Work-Order Trace Matrix

| Baseline requirement | Worker instruction | Required evidence |
|---|---|---|
| Three execute suites | deterministic nonempty mock IDs only | focused suite output; exact diff |
| Seven lint files | exact local/concrete types | full lint; negative searches |
| No production logic | route/gateway forbidden | name-status and zero diff for forbidden paths |
| Preserve B1 | isolated execution and reviewer-owned integration | fourteen-path before/after preservation evidence |
| Local-only verification | package-owned pnpm, no install/network/live | command transcript and secret-safe environment statement |
| No worker commit | stop after worker return | status showing unstaged/uncommitted worker output |

## Worker Autonomy / No-Question Rule

Repair packet-local implementation and verification issues autonomously while
remaining inside the exact manifest. Return to reviewer only for a forbidden
path requirement, source contradiction, missing local runner, dirty isolated
input, integration collision, or gate failure that cannot be repaired without
scope expansion.

## Write Ownership

### Worker-Owned Writable Paths

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.diagnostics.test.ts`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.governance-trace.test.ts`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.vi5-t1-language-state.test.ts`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/artifacts/page.test.tsx`
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/knowledge/page.test.tsx`
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/help/page.test.tsx`
7. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/knowledge/intake/page.test.tsx`
8. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.test.tsx`
9. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/home/HomeBrowseExperience.test.tsx`
10. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/home/HomeBrowseExperience.tsx`
11. `docs/reviews/CVF_LPCI1_WEB_BUILD_EXTERNAL_BASELINE_REPAIR_WORKER_RETURN_2026-08-09.md`

### Reviewer-Owned Closure Paths

- `docs/reviews/CVF_LPCI1_WEB_BUILD_EXTERNAL_BASELINE_REPAIR_COMPLETION_2026-08-09.md`
- accepted implementation paths, staging, integration, commit, and separately
  authorized continuity updates.

## Work-Order Fulfillment Manifest

Worker output must be exactly the ten source/test files when changed plus:

`docs/reviews/CVF_LPCI1_WEB_BUILD_EXTERNAL_BASELINE_REPAIR_WORKER_RETURN_2026-08-09.md`

No other file is a valid worker fulfillment artifact.

## Required Artifact Manifest

| Artifact | Owner | Required state |
|---|---|---|
| ten repair files | Worker | bounded diff only |
| worker return | Worker | complete, unstaged, uncommitted |
| completion review | Reviewer/closer | created only after source review and integration proof |
| work-order closure conversion | Reviewer/closer | reviewer-owned |

## Forbidden Path Manifest

- every path outside Worker-Owned Writable Paths;
- production `src/app/api/execute/route.ts`;
- production `src/lib/route-guard-gateway.ts`;
- package.json, lockfiles, configs, dependency manifests, provider adapters;
- route/LPCI production logic, corpus/registry/grants/persistence/vector/RAG;
- session, roadmap, spec, baseline, dispatch, completion, and public-sync files
  by the worker;
- real key/config files, generated output, release bundles.

## Pre-Existing Dirty Exemptions And Do-Not-Edit Manifest

These fourteen original-main B1 paths must be absent in the isolated lane and
preserved unchanged by BR1 integration:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.tsx`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.governance.test.ts`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.test.ts`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/lpci/query/route.ts`
5. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/audit-receipt.test.ts`
6. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/audit-receipt.ts`
7. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.test.ts`
8. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/filter-pipeline.ts`
9. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/retrieval.test.ts`
10. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts`
11. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/lpci/page.test.tsx`
12. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/query-conformance.test.ts`
13. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/query-conformance.ts`
14. `docs/reviews/CVF_LPCI1_WEB_GROUNDING_AND_CLEARANCE_CONFORMANCE_BUILD_WORKER_RETURN_2026-08-09.md`

No stash, reset, clean, checkout overwrite, staging, or ownership claim is
permitted for these paths.

## Forbidden Filesystem State At Dispatch

- any pre-existing implementation change in the isolated lane;
- any B1 dirty path present in isolated status;
- any path outside the two dispatch docs before worker execution;
- any real key or provider config copied into this worktree.

## Required Proof Manifest

1. base/branch/status capture;
2. exact path manifest and forbidden-path negative proof;
3. three-suite focused test pass;
4. full lint pass with zero errors;
5. full non-live test pass excluding live `.ts` and `.tsx` tests;
6. TypeScript check pass;
7. negative cast/suppression/config/package search;
8. GC-023 enforce pass;
9. worker-fast pass;
10. worker return with no-stage/no-commit evidence;
11. reviewer diff acceptance and canonical pre-closure on real changed range;
12. post-integration B1 99-focused-test pass plus repeated full gates.

## Execution Plan

After reviewer packet commit and exact-base handoff only:

1. Validate clean isolated input, exact manifest, local runner, ADIF, and pre-implementation.
2. Add deterministic nonempty audit-event IDs in only the three test resets.
3. Replace the ten explicit-`any` lint errors with exact local/concrete types.
4. Run targeted tests, lint, check, full non-live tests, negative searches, GC-023, worker-fast.
5. Inspect diff/status against the exact manifest.
6. Write the exact worker return and stop unstaged/uncommitted.
7. Reviewer inspects source, integrates with B1, reruns all combined gates, and
   owns authorized local repair/integration/closure/session-sync commits.

## Evidence Requirements

The worker return must include commands, exit codes, test-file/test counts,
lint error count, exact changed paths, before/after line counts, negative search
results, local-only/no-network/no-provider statement, AOT, Source Verification
refresh, and unresolved conditions. Do not claim a gate that was not run.

If local dependencies are unavailable, record the exact missing runner evidence
and return `BLOCKED_LOCAL_RUNNER_UNAVAILABLE`; do not install or use `npx`.

## Epistemic Process Block

### Expected Result / Prediction

The three deterministic mock IDs remove four failures without production
changes. Exact mock prop/icon types remove ten lint errors without behavior
changes. Existing warnings may remain outside scope.

### Evidence Comparison

Compare focused failures before/after, full lint before/after, exact diff, full
non-live suite, and integration reruns. Separate worker proof from combined B1
proof.

### Contradiction Or Gap Disposition

Any new failure outside the ten paths is evidence for reviewer triage, not
permission to expand. Any route/gateway behavior need is a source contradiction
and stops implementation.

### Claim Update

Only fresh command output may update the claim from dispatched repair to
reviewer-accepted repair. Chat and pending external artifacts cannot do so.

## Acceptance Criteria

1. Exact ten source/test paths plus worker return, no extra worker path.
2. Three stable, nonempty audit-event mock IDs; no production route/gateway diff.
3. Ten lint errors removed with exact types; no casts or suppressions.
4. No package/config/dependency/install/registry/network/provider/live action.
5. Focused three suites pass with four repaired tests and no regression.
6. Full lint, full non-live tests, check, GC-023, worker-fast pass.
7. Worker return is complete and worker makes no commit.
8. Reviewer preserves all fourteen B1 paths and proves exact non-overlap.
9. Combined-state original B1 focused command passes exactly 99 tests.
10. Reviewer runs canonical pre-closure on a real changed range before closure.

## Review Gate

Reviewer must inspect every changed line, verify each type is source-justified,
verify IDs are deterministic/nonempty, reject any production or configuration
change, compare exact manifests, and independently rerun required checks.

## Closure Diff Gate

Compare baseline requirements, this work order, worker return, final ten-file
diff, B1 fourteen-path preservation evidence, completion claims, and command
outputs. Every checklist item must be checked, `N/A with reason`, or `BLOCKED`
with a return action. No open checkbox or stale dispatch status may remain in a
closed-equivalent packet.

## Closure Checklist

- [ ] Exact ten-file repair manifest verified.
- [ ] Exact worker return verified.
- [ ] Route/gateway production diff absent.
- [ ] Cast/suppression/config/package diff absent.
- [ ] Targeted, lint, full non-live, check, GC-023, worker-fast pass.
- [ ] Fourteen B1 dirty paths preserved.
- [ ] Original B1 seven suites pass exactly 99 tests after integration.
- [ ] Canonical pre-closure passes on a real changed range.
- [ ] Reviewer alone owns staging and local dispatch/repair/integration/closure/session-sync commits; worker makes no commit.

## Return-To-Orchestrator Conditions

- `BLOCKED_LOCAL_RUNNER_UNAVAILABLE`;
- dirty or wrong isolated base;
- required edit outside the exact manifest;
- production route/gateway change appears necessary;
- cast/suppression/config/package/dependency change appears necessary;
- B1 integration collision or unexplained dirty path;
- test count differs from the stated combined B1 expectation;
- `governance/compat/check_system_chain_map_freshness.py` reports a mismatch
  outside the exact 10 waived fingerprints or the requested action exceeds the
  waiver's named reason, scope, accepted risk, or follow-up;
- any other canonical checker family fails;
- canonical gate failure cannot be repaired inside assigned ownership.

## Terminal Disposition Enum

Worker may return exactly one:

- `COMPLETE_PENDING_REVIEW`
- `BLOCKED_LOCAL_RUNNER_UNAVAILABLE`
- `BLOCKED_SOURCE_CONTRADICTION`
- `BLOCKED_SCOPE_EXPANSION_REQUIRED`
- `BLOCKED_GATE_FAILURE`

## Worker Return Packet Shape Contract

Return path:
`docs/reviews/CVF_LPCI1_WEB_BUILD_EXTERNAL_BASELINE_REPAIR_WORKER_RETURN_2026-08-09.md`

```text
contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: python governance/compat/run_worker_return_fast_gate.py
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED
requiredEvidenceTerms: executionBaseHead; git status --short
requiredSections: Summary; Purpose; Scope / Methodology; Findings / Position; Risk / Corrective Action; Authority And Base; Source Verification Refresh; Exact Changed Manifest; Repair Evidence; Verification Commands And Results; Negative Scope Proof; B1 Isolation Statement; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; External Knowledge Intake Routing; Closure Checklist State; Claim Boundary; Public Export Disposition; Terminal Disposition; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package
conditionalDispositionRule: Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; and Machine Closure Package must each contain applicable evidence or N/A with reason
```

Required headings: Summary; Purpose; Scope / Methodology; Findings / Position;
Risk / Corrective Action; Authority And Base; Source Verification Refresh; Exact
Changed Manifest; Repair Evidence; Verification Commands And Results; Negative
Scope Proof; B1 Isolation Statement; Agent Operation Trace Block; Delta Execution
Claim Boundary Control Block; External Knowledge Intake Routing; Closure Checklist
State; Claim Boundary; Public Export Disposition; Terminal Disposition; Rescan
Intelligence Hardening; Corpus Completeness And Report Integrity;
Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine
Closure Package.

The conditional sections Rescan Intelligence Hardening, Corpus Completeness And
Report Integrity, Finding-To-Governance Learning Disposition, Epistemic Process
Block, and Machine Closure Package must each contain applicable evidence or the
literal `N/A with reason`.

## Verification Commands

Run from repository root unless the command changes directory:

```powershell
git rev-parse --short HEAD
git branch --show-current
git status --short --untracked-files=all
git diff --name-status
git diff --check
Push-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
pnpm run test:run -- --exclude "src/**/*.live.test.tsx" src/app/api/execute/route.diagnostics.test.ts src/app/api/execute/route.governance-trace.test.ts src/app/api/execute/route.vi5-t1-language-state.test.ts
pnpm run lint
pnpm run check
pnpm run test:run -- --exclude "src/**/*.live.test.tsx"
Pop-Location
python governance/compat/check_governed_file_size.py --enforce
python governance/compat/run_worker_return_fast_gate.py
```

After reviewer integration with B1, rerun all commands above and this original
B1 focused command, which must report exactly 7 passed files and 99 passed tests:

```powershell
Push-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
pnpm run test:run -- --exclude "src/**/*.live.test.tsx" src/lib/lpci/query-conformance.test.ts src/lib/lpci/filter-pipeline.test.ts src/lib/lpci/retrieval.test.ts src/lib/lpci/audit-receipt.test.ts src/app/api/lpci/query/route.test.ts src/app/api/lpci/query/route.governance.test.ts "src/app/(dashboard)/lpci/page.test.tsx"
Pop-Location
```

The package script already excludes live `.test.ts`; the explicit extra exclude
covers live `.test.tsx`. Use only existing local pnpm and package-owned runners.
No `npx`, registry/install/update, browser, real key, provider, network, live
test, release bundle, deploy, or public-sync command is permitted.

Reviewer pre-closure must use a real accepted changed range:

```powershell
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base <accepted-base-head> --head HEAD
```

## Maintainability And File-Size Plan

Record before/after line counts for all ten files. No new shared module is
authorized. If an owned file crosses or approaches a hard guard limit and
cannot be repaired by a small local change, return scope expansion rather than
compressing or editing outside the manifest.

## Dual Agent Surface Matrix

| Surface | Worker | Reviewer/closer |
|---|---|---|
| ten repair files | edit and prove | inspect and accept/reject |
| worker return | author | inspect |
| B1 dirty paths | do not touch | preserve and integrate around |
| completion review | no write | author |
| staging/commit | forbidden | reviewer-owned; no commit has occurred yet, pending reviewer packet commit |
| continuity/public/release | forbidden | only with separate authority |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | runtime/provider/mcp/readiness claim |
| Chain map route | N/A with reason: no external knowledge input is consumed; filename-triggered classification only |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this work order and paired GC-018 baseline |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | local repository source/test repair only; no external source absorption or authority promotion |

## External Absorption Core

External absorption core: REQUIRED because the governed batch filename contains
the guard trigger `EXTERNAL`; the substantive disposition remains no external
input authorized or consumed.

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | local clean worktree `D:\UNG DUNG AI\TOOL AI 2026\CVF-LPCI-BR1`; no external corpus |
| Enumeration command | `git status --short --untracked-files=all` plus exact local source `rg` inspection |
| Manifest artifact or inline manifest | inline manifest below: one classification record, zero external source items |
| Processing ledger artifact or inline ledger | inline ledger below: filename trigger classified `NO_NEW_VALUE` for absorption |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | inline: local repair -> this work order; integration -> reviewer completion path |
| Unresolved items | zero external-input items; local implementation remains pending worker review |
| Completion claim boundary | dispatch classification only; no corpus, provider, runtime readiness, package, release, or public claim |

| Manifest item | Source class | Count | Disposition |
|---|---|---:|---|
| filename-trigger classification | local governed packet | 1 | NO_NEW_VALUE for external absorption |
| external source items | none authorized or supplied | 0 | REJECT from scope |

| Ledger item | Status | Owner | Evidence |
|---|---|---|---|
| filename-trigger classification | NO_NEW_VALUE | dispatcher/reviewer | operator token means B1-external baseline, not external repository/input |

## Corpus Completeness And Report Integrity

- Corpus task class: NO_EXTERNAL_CORPUS_FILENAME_TRIGGER_ONLY
- Corpus root: local clean BR1 worktree; no external corpus authorized
- Snapshot time: 2026-08-09 dispatch source audit
- Enumeration command: `rg --files --hidden --no-ignore` limited to the clean local worktree; no external root is enumerated
- Manifest artifact or inline manifest: inline two-row manifest in External Absorption Core
- Manifest hash: N/A with reason: no external corpus bytes exist
- Processing ledger artifact or inline ledger: inline one-row ledger in External Absorption Core
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE
- Reconciliation: manifest=1; ledger_terminal=1; exclusions=0; unresolved=0
- Unresolved files: 0
- Declared exclusions: all external repositories, copied folders, provider payloads, and network inputs are forbidden
- Unreadable or unsupported files: none because no external files are in scope
- Aggregation check: zero external source items plus one filename-trigger classification record
- Drift check: integration reviewer must recompute local Git state; no external rescan exists
- Output traceability: local ten-file repair maps to this work order and worker return only
- Adversarial verification: do not reinterpret `external baseline` as external-input authority
- Corpus verdict: PARTIAL - filename-trigger classification only; no external corpus completeness claim is made

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| local operator token | bounded repair authority only | DOCTRINE_ADAPTED | this work order | preserve exact authority boundary | documentation routing only |
| absent external package input | no package value | PACKAGE_CANDIDATE | future separately governed packet | remain forbidden unless fresh authority and source exist | no package activation |
| absent provider/runtime input | no runtime value | RUNTIME_CANDIDATE | future separately governed packet | remain forbidden unless fresh authority and source exist | no runtime/provider change |
| filename-trigger behavior | checker compatibility fact | CHECKER_CANDIDATE | future governance-maintenance packet | record only if reviewer finds a repeated defect | no checker edit here |
| any direct external import | none authorized | REJECT_DIRECT_IMPORT | this work order claim boundary | reject | no import |
| external absorption lane | zero source items | NO_PACKAGE_OR_RUNTIME_VALUE | inline classification ledger | no action | local repair only |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| filename-triggered external classification | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` and this work order | CONFIRMED_EXISTING | no external source value; only local baseline-repair meaning | retain NOT_APPLICABLE boundary and perform no absorption |

## Evidence Reuse And Encoding Plan

Reuse only command output and repository source verified in this execution.
Chat evidence remains labeled human-only. Pending B1 evidence remains external
and uncommitted until reviewer integration. Author new governed prose in ASCII;
preserve existing localized-source encoding exceptions without broad rewrite.

## Agent Handoff Contract Control Block

Contract source archive-qualified checker exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`

| Field | Binding value |
|---|---|
| canonicalRoute | `MULTI_AGENT_MULTI_ROLE` |
| rolePattern | dispatcher/reviewer -> one no-commit worker -> reviewer/integration closer |
| phase | DISPATCH_AUTHORING, EXECUTION, CLOSURE, INTEGRATION |
| baseHeadFor(phase) | dispatchBaseHead=d9497c5db; executionBaseHead=N/A until reviewer commits this packet, then worker captures the exact committed dispatch HEAD; closureBaseHead=N/A until authorized execution exists |
| changedSetScope(phase) | dispatch=paired packet; execution=exact ten repair paths plus worker return; closure=accepted repair plus completion; integration=accepted ten-file diff against preserved B1 state |
| traceScope(phase, actor) | every actor records its phase, commands, expected/actual manifest, and delta |
| commitOwner(phase) | reviewer is authorized for local dispatch, repair, integration, closure, and session-sync commits under both operator waivers; no commit has occurred yet; worker remains `WORKER_MUST_NOT_COMMIT` |
| crossBatchIsolation | Fourteen B1 dirty paths absent/forbidden in worker lane and preserved at integration |
| nextMoveSurfaces | Reviewer/closer only, and only when separately authorized |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_LPCI1_WEB_BUILD_EXTERNAL_BASELINE_REPAIR_COMPLETION_2026-08-09.md` |
| reviewerOwnedClosurePaths | completion review, work-order closure conversion, and authorized local commits under both operator waivers |
| workerReturnPath | `docs/reviews/CVF_LPCI1_WEB_BUILD_EXTERNAL_BASELINE_REPAIR_WORKER_RETURN_2026-08-09.md` |
| integrationOwner | Reviewer/closer |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_governed_file_size.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/run_agent_autorun_workflow_gate.py` |
| literalTokensReviewed | DISPATCH_READY; WAIVED_BOUNDED; NON-COMPLIANT; WORKER_MUST_NOT_COMMIT; MULTI_AGENT_MULTI_ROLE; Source Verification columns; New Doc-Only Fields; exact manifests; completionReviewPath; reviewerOwnedClosurePaths |
| gateRunPurpose | Checker runs provide confirmation evidence after source verification and packet authoring, not first discovery |
| repairPolicy | Assigned agent repairs allowed-scope gate failures and reruns before handoff |
| claimBoundary | gate compliance does not prove implementation, integration, live governance, or release |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatch author/reviewer |
| Provider or surface | local governed workspace |
| Session or invocation | LPCI1-WEB-BR1 worker-return packet-shape and continuity repair, 2026-08-09 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\CVF-LPCI-BR1` |
| Command or tool surface | governed reads, `apply_patch`, local governance checkers, and Git evidence |
| Target paths | BR1 work order packet-shape contract only; active handoff continuity is committed separately by the session-sync steward |
| Allowed scope source | reviewer repair instruction after dispatch commit `fa75aeea4` under the two bounded operator waivers |
| Before status evidence | HEAD `fa75aeea4`; branch `codex/lpci1-web-br1`; clean worktree; packet-shape and active-continuity blockers reported |
| After status evidence | work-order packet-shape repair is checker-clean; active handoff continuity remains a separately owned session-sync change |
| Diff evidence | `git status --short`; `git diff --name-status`; `git diff --check` |
| Approval boundary | worker-return packet-shape correction only in this material commit; worker may not commit |
| Claim boundary | no implementation, generated-state edit, provider/live/network action, release, deployment, or public-sync claim |
| Agent type | reviewer and session-sync steward |
| Invocation ID | `lpci1-web-br1-packet-shape-continuity-2026-08-09` |
| Expected manifest | `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_BUILD_EXTERNAL_BASELINE_REPAIR_2026-08-09.md` |
| Actual changed set | `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI1_WEB_BUILD_EXTERNAL_BASELINE_REPAIR_2026-08-09.md` |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | bounded LPCI1-WEB-BR1 no-commit implementation dispatch |
| claimDisposition | CLAIM_REJECTED - packet authoring is not runtime execution |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT |
| actionEvidence | ACTION_EVIDENCE_PRESENT - current source reads, local non-live reproduction, and packet gates only |
| invocationBoundary | repository-local dispatch and later isolated worker workflow |
| interceptionBoundary | no provider, browser, live, network, or runtime interception claim |
| claimLanguage | no worker is released and no commit has occurred yet; after reviewer commits, the reviewer may hand off the exact committed base to the worker |
| forbiddenExpansion | no B1 acceptance, combined-state green claim, live/release proof, provider/config, corpus/public/deployment/readiness, or worker commit |

## Foundation Storage Layout Block

- N/A with reason: this work order does not create, split, relocate, or refactor durable governance foundation files or indexes; it changes only the exact ten existing app test/type files and one worker return.

## Public Export Disposition

`DEFERRED_PRIVATE_ONLY`

This is a private provenance repair packet with no public-sync artifact or
authority.

## Operator Checkpoint

The operator has supplied three bounded authority tokens: the original
`AUTHORIZE_LPCI1_WEB_BUILD_EXTERNAL_BASELINE_REPAIR`, the system-chain
freshness release waiver `AUTHORIZE_BOUNDED_WAIVER_SYSTEM_CHAIN_FRESHNESS_FOR_LPCI_BR1`,
and the as-built catalog drift release waiver
`AUTHORIZE_BOUNDED_WAIVER_AS_BUILT_CATALOG_DRIFT_FOR_LPCI_BR1`. No further
operator choice is inferred beyond their plain, bounded meaning. Both named
canonical pre-dispatch failures are waived for this packet only, within
each waiver's named scope. Scope expansion, production logic change,
install/network need, integration collision, or any violation outside the
exact waived findings still returns to the reviewer/orchestrator.

## Claim Boundary

Dispatch authoring reaches `DISPATCH_READY`. The operator's two bounded
waivers together cover both named canonical pre-dispatch failures - system
chain map freshness and as-built catalog/gap-index drift - for this
packet's exact scope: LPCI1-WEB-BR1 packet dispatch, its ten-file
external-baseline repair, integration with the existing reviewed
fourteen-path B1 diff, and deterministic non-live closure checks. The
packet remains untracked and uncommitted; the worker remains
`WORKER_MUST_NOT_COMMIT`. The reviewer may now commit this packet and hand
off the exact committed dispatch HEAD; only then may the worker run
pre-implementation and the ten-file repair, then return
`COMPLETE_PENDING_REVIEW` after exact evidence. Neither waiver certifies
its named gate as passing, extends to any other packet or checker family,
or authorizes checker weakening, fingerprint rewriting, aggregate/index
rewriting outside a proper regeneration command, runtime gateway changes,
provider/live/network action, persistence, vector/RAG, corpus mutation,
public-sync, push, or deployment. Any commit (dispatch, repair,
integration, closure, or session-sync) is reserved to Codex reviewer under
both waivers' Commit Authority fields, not the worker.
