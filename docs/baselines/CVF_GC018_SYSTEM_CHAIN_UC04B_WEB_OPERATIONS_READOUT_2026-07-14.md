# CVF GC-018 System Chain UC-04B Web Operations Readout

Memory class: FULL_RECORD

Status: CLOSED_BLOCKED_BOUNDED

docType: gc018_baseline

Date: 2026-07-14

Risk classification: R1

## Purpose

Authorize one bounded, provider-free proof that the existing CVF Web Operations
surface can trigger one real allowlisted governance checker, expose its result
to an authenticated operator, and reject the same trigger from a read-only
role before command execution.

## Authorization / Decision

The accepted UC-04A closure and active system-chain roadmap make UC-04B packet
authoring the current allowed move. Fresh source verification selects
`docs_governance_check` because the current Web job owner maps it to the real
docs compatibility checker, presents it in the existing Operations page, and
does not classify it as a live-provider or cost-quota job.

Authorize `SCLP-UC04B-T4` for one no-commit proof worker. The worker may add one
proof-only Playwright specification, one structured proof receipt, one
conditional diagnostic, and one worker return. The Playwright command may be
invoked exactly once. It may submit exactly one authorized developer request
and one expected-blocked reviewer request. Only the authorized request may
start the checker subprocess. No retry and no provider call are authorized.

## Proposed Tranche

`SCLP-UC04B-T4` is one no-commit proof tranche. It creates only a proof-only
Playwright consumer, dated evidence, an optional failure diagnostic, and a
worker return. Reviewer/closer retains all closure and reverse-projection
ownership.

## Scope / Target / Owner Boundary

Target: the current development Web Operations page, API route, allowlisted
job runner, audit trail, and `docs_governance_check` only. Existing Web source,
API, auth, job runner, checker, tests, roadmap, coverage, Catalog/GAP, session,
provider, public, and production owners are read-only during worker execution.

## Design Control Gate

| Control | Decision |
|---|---|
| visual contract | root `DESIGN.md`; no UI change is authorized |
| positive actor | authenticated `developer`, mapped to Web `operator` |
| positive job | `docs_governance_check` |
| positive execution | one real POST through Next route and one real checker subprocess |
| positive readout | page message, Latest Job, and Audit Trail show the selected job and final status |
| negative actor | authenticated `reviewer` |
| negative boundary | same job POST returns policy block with `read_only_role_cannot_trigger`; zero subprocess execution |
| audit evidence | new job IDs and matching JSONL events are reconciled without committing runtime audit state |
| harness ceiling | one Playwright command |
| Web submissions | two: one allowed and one blocked |
| checker executions | exactly one |
| retry ceiling | zero |
| provider boundary | zero provider/API/MCP calls |
| closure owner | reviewer/closer only |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Web job vocabulary includes the selected job | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts` | lines 16-21 | `GovernanceJobType` | Web governance job contract | EXISTS | ACCEPT |
| selected job invokes the current docs checker with fixed arguments | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts` | lines 154-160 | `docs_governance_check` | allowlisted job definition | VALUE_SET | ACCEPT |
| reviewer and viewer roles are denied | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts` | lines 211-234 | `canTrigger` | Web job authorization policy | RUNTIME_BEHAVIOR | ACCEPT |
| denied submissions emit requested and blocked audit events and return policy status | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts` | lines 449-495 | `submitGovernanceJob` | Web job execution owner | RUNTIME_BEHAVIOR | ACCEPT |
| allowed submissions emit running and final events around a fixed Python subprocess | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts` | lines 498-559 | `submitGovernanceJob` | Web job execution owner | RUNTIME_BEHAVIOR | ACCEPT |
| only provider check and full live gate enter live cost preflight | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts` | lines 415-443 | `liveEstimateJobTypes` | Web provider/cost boundary | VALUE_SET | ACCEPT |
| Operations page exposes Docs Governance Check | canonical-contract:cvf-web-operations-page-source | lines 62-95 in the freshly read page source | `JOBS` | Web Operations UI | VALUE_SET | ACCEPT |
| developer maps to operator and reviewer remains read-only | canonical-contract:cvf-web-operations-page-source | lines 97-112 in the freshly read page source | `mapRole`; `canTrigger`; `disabledReason` | Web Operations UI authorization view | RUNTIME_BEHAVIOR | ACCEPT |
| page submits through the real API and reloads audit jobs | canonical-contract:cvf-web-operations-page-source | lines 141-185 in the freshly read page source | `loadJobs`; `runJob` | Web Operations UI | RUNTIME_BEHAVIOR | ACCEPT |
| page renders final status, job ID, type, decision, and audit summary | canonical-contract:cvf-web-operations-page-source | lines 314-363 in the freshly read page source | `latest`; `jobs` | Web Operations readout | RUNTIME_BEHAVIOR | ACCEPT |
| API maps developer to operator and returns 403 for policy blocks | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/system/jobs/route.ts` | lines 28-57 | `POST` | Next API route | RUNTIME_BEHAVIOR | ACCEPT |
| current E2E helper authenticates through NextAuth credentials | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/utils.ts` | lines 20-66 | `signInViaNextAuth`; `loginAs` | Playwright E2E helper | RUNTIME_BEHAVIOR | ACCEPT |
| live Playwright config starts a real Next development server | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.ts` | lines 20-42 | `webServer` | Playwright runtime config | VALUE_SET | ACCEPT |
| roadmap selects real development runtime and selected job execution | `docs/roadmaps/CVF_SYSTEM_CHAIN_LIVE_PROOF_USE_CASE_ROADMAP_2026-07-14.md` | tranche T4 / UC-04B | `T4 / UC-04B` | system-chain roadmap | VALUE_SET | ACCEPT |
| coverage ledger retains Web as the missing half of UC-04 | `docs/reference/system_chain/CVF_SYSTEM_CHAIN_LIVE_PROOF_COVERAGE.json` | UC-04 and Evidence-to-Operator entries | `UC-04-EVIDENCE-TO-OPERATOR-SURFACE` | live-proof coverage ledger | VALUE_SET | ACCEPT |

## Current Runtime Freshness Verification

Fresh reads at dispatch base `17d69ec1c` verified the selected job mapping,
authorization policy, audit event behavior, UI submission/readout, Next API
route, credential helper, and real development-server Playwright config. The
worker must recompute these facts at execution base. Any contradiction returns
`BLOCKED_WITH_REASON` before proof artifacts are created.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Dispatch control | Evidence requirement | Disposition |
|---|---|---|---|
| real development runtime | live Playwright config only | server startup plus real page/API evidence | READY |
| selected job execution | `docs_governance_check` only | job ID, fixed handler, exit, and audit reconciliation | READY |
| visible outcome | page message, Latest Job, Audit Trail | screenshot or DOM assertion plus receipt | READY |
| meaningful policy boundary | reviewer submits same job | 403, reason, blocked audit events, zero runner event | READY |
| no unified inventory claim | one job only | exact claim boundary | READY |
| provider conditional | selected job is local docs checker | provider call count zero | READY |
| preserve CLI evidence | UC-04A paths read-only | exact changed-set review | READY |
| reverse-project learning | reviewer-owned after acceptance | coverage, roadmap, Catalog/GAP, and ADIF decision | READY |

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| UC-04A accepted | material commit `b335c0e4c` | SATISFIED |
| session routes UC-04B packet authoring | session commit `17d69ec1c` | SATISFIED |
| roadmap separates CLI and Web | current T3/T4 split | SATISFIED |
| Web job and readout source-verified | Source Verification Block above | SATISFIED |
| dispatch worktree clean | empty `git status --short` at `17d69ec1c` | SATISFIED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`system-chain-live-proof`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cvf-web`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class system-chain-live-proof --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --max-results 20 --json`

Returned defects: NONE_RETURNED

## Cost And Retry Control

One Playwright command, two Web submissions, one underlying checker execution,
zero retries, and zero provider calls. A failed, partial, timed-out, or unclear
result is classified once under the Live Run Diagnostic Standard and stops.

## Acceptance Criteria

- Current source still proves the selected Web/API/job ownership.
- Focused static or mocked owner tests pass before the one live Web command.
- Developer runs `docs_governance_check` once through the real page/API.
- The real checker succeeds and the UI exposes its job type, ID, status, and
  audit summary.
- Reviewer submission of the same job returns HTTP 403 with
  `read_only_role_cannot_trigger` and produces no running event.
- Receipt reconciles two distinct case IDs, two submissions, one command
  execution, zero retries, and zero provider calls.
- Worker changes only declared proof and return paths, leaves HEAD unchanged,
  stages nothing, and does not commit.

## Evidence / Verification

Evidence must include execution base, source refresh, focused preflight tests,
one Playwright command, positive and negative stable case IDs, new job IDs,
HTTP statuses, UI assertions, audit-event sequence, checker exit/readout,
command/submission/retry/provider counts, secret scan, exact changed set, and
unchanged HEAD. Runtime JSONL is evidence input only; the receipt must retain a
secret-safe digest and the JSONL itself must not be committed.

## Fail Conditions

Source drift, unrelated dirty start, owner mutation, mock Web proof, second
Playwright command, submission count other than two, checker execution count
other than one, retry, provider call, positive failure, negative allow, missing
403/reason, missing UI readout, unmatched audit events, secret leakage,
unexpected path, or stronger claim stops the tranche.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance proof packet; no public-sync scope.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Source Verification Block`; `Roadmap-To-Work-Order Trace Matrix`; `Dependency Release Evidence`; `ADIF Defect Registry Disclosure`; `Cost And Retry Control`; `Public Export Disposition` |
| gateRunPurpose | confirmation after complete Web-owner and output inventory; not first discovery |
| claimBoundary | dispatch authorization only; no UC-04B proof execution in this batch |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --help` |
| generatedProfile | GC-018 dispatch baseline |
| generatedSkeletonStatus | NOT_USED_WITH_REASON |
| manualEditsAfterScaffold | source-verified authoring from the accepted system-chain dispatch pattern |
| checkerReadAheadConfirmation | applicable checker sources and literal-format gotchas read before authoring |
| docOnlyNewFields | N/A with reason: baseline introduces no runtime or canonical schema field |
| claimBoundary | packet authorization only |

## Claim Boundary

A PASS may prove only that the existing development Web Operations surface ran
the selected docs checker once for an authorized developer/operator, exposed
the retained result, and rejected one reviewer request in one local evidence
window. It does not prove a unified checker inventory, all Web jobs, provider
governance, production, public readiness, scale, certification, or user value.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | this baseline | `CLOSED_BLOCKED_BOUNDED` | PASS |
| Work order status | paired SCLP-UC04B-T4 work order | `CLOSED_BLOCKED_BOUNDED` | PASS |
| Completion or reviewer artifact | declared completion path | reviewer blocker closure | PASS |
| Roadmap state | system-chain roadmap | recovery packet next | PASS |
| Registry JSON | coverage ledger and GC-051 | Web blocked; proof test registered | PASS |
| Registry Markdown | system-chain and ADIF front doors | blocker/learning recorded | PASS |
| External evidence digest | N/A with reason: no external evidence consumed | repository evidence only | N/A with reason |
| System loop interlock | corrected proof receipt | FAIL retained; no PASS promotion | PASS |
| Session continuity | active session | separate sync after material commit | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Assertion | Required value | Observed value | Status |
|---|---|---|---|
| Playwright invocation | 1 | 2 | BLOCKED |
| Web submissions | 2 | 0 | BLOCKED |
| checker executions | 1 | 0 | BLOCKED |
| retry count | 0 | 1 | BLOCKED |
| provider calls | 0 | 0 | PASS |
