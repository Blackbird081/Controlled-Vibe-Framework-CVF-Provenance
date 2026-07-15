# CVF Agent Work Order - System Chain UC-04B R2R1 Localhost-Normalized Recovery

Memory class: FULL_RECORD

Status: DISPATCH_READY

Work Order ID: SCLP-UC04B-R2R1

Date: 2026-07-15

dispatchBaseHead: `2feb62046`

Execution mode: WORKER_MUST_NOT_COMMIT

Commit mode: `WORKER_MUST_NOT_COMMIT`

## Dispatch Prompt Envelope

```text
Role: worker/proof executor. Codex is reviewer/closer.
Canonical packet: docs/work_orders/CVF_AGENT_WORK_ORDER_SYSTEM_CHAIN_UC04B_R2R1_LOCALHOST_NORMALIZED_RECOVERY_2026-07-15.md.
Commit mode: WORKER_MUST_NOT_COMMIT.
Base: capture executionBaseHead and require a clean worktree.
Current-time notes: committed runtime repair and proof spec are read-only; set PLAYWRIGHT_BASE_URL=http://localhost:3001 for the sole Playwright command.
Do-not-misread notes: this is not an R2 retry and not a UC-04B business proof. Do not edit next.config.ts, playwright config, proof source, runtime, tests, or application owners.
Required first actions: read startup/guard sources, paired GC-018, R2 closure, ADIF-0034/0035, retained proof and config, then run pre-implementation and focused preflight.
Return contract: COMPLETE_PENDING_REVIEW only with two PASS cases and reconciled evidence; otherwise BLOCKED_WITH_REASON with one diagnostic. Never rerun or commit.
```

## Purpose

Prove the committed R2 request-bound auth repair using a single canonical
localhost origin without changing any source or consuming business/provider
proof budget.

## Objective

Run the retained two-case auth projection regression once with
`PLAYWRIGHT_BASE_URL=http://localhost:3001`, proving developer agreement across
session, auth-me, and Operations plus the anonymous negative boundary.

## Authority Chain

Operator continuation -> R2 blocked closure `545628ca4` -> session route
`2feb62046` -> paired R2R1 GC-018 -> this work order. Current committed source
and machine gates control.

## Agent Roles

| Role | Ownership |
|---|---|
| dispatcher | source verification, canonical-origin and cost controls |
| worker | read-only preflight, one invocation, evidence, no-commit return |
| reviewer/closer | independent review, closure, reverse projection, commits |

## Scope

All runtime, config, test, proof, page, route, registry, roadmap, and session
owners are read-only. Worker may create only the three dated R2R1 evidence
files and one worker return. Disposable Playwright outputs are not governed
deliverables and must not be staged.

## Required First Reads

1. Startup front doors, active handoff, guard orientation, literal gotchas.
2. Paired R2R1 GC-018, this work order, R2 completion, ADIF-0034, ADIF-0035.
3. Live Run Diagnostic Standard, Playwright config, retained R2 proof spec,
   auth adapter/tests, auth-me route, and Operations page.

## Pre-Flight Checks

- Capture `executionBaseHead`; require empty `git status --short`.
- Refresh every Source Verification ACCEPT fact.
- Run pre-implementation autorun.
- Confirm no `PLAYWRIGHT_BASE_URL` is inherited, then set it only for the sole
  command to `http://localhost:3001`; record presence and resolved host without
  exposing any unrelated environment value.
- Run focused 12-test suite and typecheck before ledger creation.
- Compute SHA-256 of the committed retained spec and verify `git diff` is empty.
- Capture tracked `test-results/.last-run.json` baseline for restoration.

## Write Ownership

Worker owns only the dated ledger, receipt, conditional diagnostic, and worker
return listed in the manifest. All source/config/test/proof files, build state,
cookies, traces, screenshots, videos, environment files, runtime audits, and
tracked `.last-run.json` are read-only or disposable. Reviewer owns closure,
reverse projection, session updates, and commits.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| base URL has explicit environment override | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.ts` | use config | `PLAYWRIGHT_BASE_URL` | Playwright configuration | VALUE_SET | ACCEPT |
| web server port defaults to 3001 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.ts` | port constant | `PLAYWRIGHT_PORT` | Playwright configuration | VALUE_SET | ACCEPT |
| proof paths resolve through configured base URL | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-auth-projection-regression.spec.ts` | auth helper and navigation calls | `OPERATIONS_URL` | retained R2 proof | RUNTIME_BEHAVIOR | ACCEPT |
| positive and negative case IDs are stable | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-auth-projection-regression.spec.ts` | serial tests | `positive_developer_auth_projection`; `negative_anonymous_auth_projection` | retained R2 proof | EXISTS | ACCEPT |
| request-bound adapter uses request token | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | request resolver | `resolveBaseSessionFromRequest` | Web auth adapter | RUNTIME_BEHAVIOR | ACCEPT |
| focused tests cover request and ambient behavior | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.test.ts` | verifySessionCookie describes | `verifySessionCookie` | auth test owner | EXISTS | ACCEPT |
| R2 reviewer accepted unit repair and corrected blocker | `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R2_WEB_AUTH_PROJECTION_REPAIR_COMPLETION_2026-07-14.md` | Decision and Findings | `CLOSED_BLOCKED_BOUNDED` | reviewer closure | VALUE_SET | ACCEPT |
| canonical-host learning is governed | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0035.md` | Remediation | `ADIF-0035` | ADIF registry | VALUE_SET | ACCEPT |

## Current Runtime Freshness Verification

Refresh all accepted facts before ledger start. Any committed-source drift,
failed preflight, unexpected inherited origin, or need to edit a read-only file
returns `BLOCKED_WITH_REASON` before Playwright.

## Execution Plan

1. Capture clean execution base, required reads, and source refresh.
2. Run pre-implementation gate, focused 12-test suite, and typecheck.
3. Confirm retained proof source and all owners remain unchanged. Compute and
   record the proof SHA-256.
4. Create the invocation ledger with ceiling 1, canonical origin
   `http://localhost:3001`, frozen hash, both case IDs, and zero counters.
5. Immediately before spawn, set `invocationStarted=1`. Run exactly:
   `$env:PLAYWRIGHT_BASE_URL='http://localhost:3001'; npx playwright test tests/e2e/system-chain-uc04b-auth-projection-regression.spec.ts --config playwright.config.ts --workers=1`.
6. Never execute a second Playwright command and never edit proof source after
   ledger start. On failure, write one diagnostic and stop.
7. On PASS, record both cases, direct/API/page projections, and a trace-derived
   observed-host inventory proving no `127.0.0.1:3001` request occurred.
8. Restore tracked runtime artifacts, write receipt/return, run return gates,
   and leave HEAD unchanged with nothing staged.

## Planned Worker Fulfillment Manifest

| Path | Ownership | Required disposition |
|---|---|---|
| `docs/reviews/evidence/system-chain-uc04b-r2r1-localhost-invocation-ledger-2026-07-15.json` | worker | monotonic one-invocation ledger |
| `docs/reviews/evidence/system-chain-uc04b-r2r1-localhost-regression-2026-07-15.json` | worker | reconciled two-case receipt |
| `docs/reviews/evidence/system-chain-uc04b-r2r1-localhost-diagnostic-2026-07-15.json` | worker conditional | required only on non-PASS |
| `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R2R1_LOCALHOST_NORMALIZED_RECOVERY_WORKER_RETURN_2026-07-15.md` | worker | no-commit return |

## Invocation Ledger Contract

The ledger exists before Playwright and records execution base, command
fingerprint, proof path/hash, canonical origin, invocation ceiling/start,
timestamps, both case IDs, result, observed hosts, and business/checker/retry/
provider counters. Set start to one before spawn; never reset it. Receipt,
diagnostic, trace, and prose must reconcile.

## Evidence Requirements

Record clean base, source refresh, focused preflight, inherited-origin check,
canonical origin, frozen hash, ledger, command fingerprint, both cases,
direct/API/page projections, observed host set, exact 1/0/0/0/0 counters,
conditional diagnostic, secret scan, diff/status/stage evidence, tracked
artifact restoration, and unchanged HEAD. Never retain credentials or cookies.

## Acceptance Criteria

- AC-01: source refresh, 12/12 focused tests, and typecheck pass before ledger.
- AC-02: proof hash matches committed source, ledger, and receipt.
- AC-03: canonical origin is exactly `http://localhost:3001`.
- AC-04: exactly one Playwright command runs both stable cases.
- AC-05: developer session, auth-me, and Operations operator projections agree.
- AC-06: anonymous auth-me 401 and Operations anonymous projection agree.
- AC-07: observed host set excludes `127.0.0.1:3001`.
- AC-08: business/checker/retry/provider counters all equal zero.
- AC-09: only manifest evidence paths change; nothing staged.
- AC-10: worker HEAD remains execution base and worker makes no commit.

## Fail Conditions

Dirty start, source drift, failed preflight, proof edit, wrong origin, ledger
reset, second command, case skip/fail, any 127 host request, projection mismatch,
nonzero cost counter, secret leak, unexpected governed path, staged change,
commit, or stronger claim stops with `BLOCKED_WITH_REASON`.

## Return-To-Orchestrator Conditions

Return `COMPLETE_PENDING_REVIEW` only if all ACs are evidenced. Otherwise
return `BLOCKED_WITH_REASON`, one secret-safe diagnostic, retryability false,
and the smallest source-backed reviewer action. Never request a rerun.

## Operator Checkpoint

No checkpoint is parked. Canonical local mock credentials may be used. No
provider key, business execution, or source edit is authorized.

## Closure Checklist

| Item | Disposition |
|---|---|
| clean base and source refresh | worker evidence required |
| focused preflight | worker evidence required |
| canonical origin and frozen hash | worker evidence required |
| one command and two PASS cases | worker evidence required |
| no 127 host request | worker evidence required |
| exact zero cost counters | worker evidence required |
| exact changed set and unchanged HEAD | worker evidence required |
| GAP/coverage/roadmap decision | reviewer-owned |

## Worker Autonomy / No-Question Rule

Proceed inside the manifest. Focused preflight may be rerun before ledger start.
After ledger start, no source edit or Playwright rerun is authorized. Any
read-only-owner need or unclear result stops.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work-order control | Evidence | Status |
|---|---|---|---|
| canonical-host recovery | explicit localhost environment | ledger/trace | READY |
| accepted repair remains fixed | all owners read-only | empty source diff | READY |
| projection proof | retained two-case spec | receipt | READY |
| bounded cost | immutable ledger | 1/0/0/0/0 | READY |
| no business overclaim | business spec forbidden | reviewer decision | READY |

## Cost And Retry Control

Authorized totals: Playwright invocations 1; business submissions 0; checker
executions 0; retries 0; provider/API/MCP calls 0. Auth and page GET/credential
callback requests inside the retained cases are allowed and are not business
submissions.

## Agent Handoff Contract Control Block

Contract stable front door: `docs/reference/agent_handoff/README.md`.

Contract source archive-qualified exception:
`docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | SINGLE_AGENT_SINGLE_ROLE |
| rolePattern | one no-commit proof worker, then reviewer/closer |
| phase | R2R1 localhost-normalized regression, receipt, return |
| baseHeadFor(phase) | dispatchBaseHead=`2feb62046`; executionBaseHead=`WORKER_MUST_CAPTURE_AT_START`; closureBaseHead=`REVIEWER_TO_SET` |
| changedSetScope(phase) | exact Planned Worker Fulfillment Manifest |
| traceScope(phase, actor) | worker records preflight/hash/origin/ledger/invocation/cases/hosts/counters/diff/HEAD; reviewer owns closure |
| commitOwner(phase) | WORKER_MUST_NOT_COMMIT; reviewer owns material commit |
| crossBatchIsolation | CLEAN_WORKTREE_CONFIRMED at dispatch; all non-manifest surfaces read-only |
| nextMoveSurfaces | reviewer updates closure, reverse projection, and session only after review |

## Reviewer Closure Conversion

| Field | Value |
|---|---|
| completionReviewPath | `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R2R1_LOCALHOST_NORMALIZED_RECOVERY_COMPLETION_2026-07-15.md` |
| reviewerOwnedClosurePaths | completion; paired baseline/work order; GAP/coverage/roadmap; active session sources |
| closureOwner | reviewer/closer |
| workerCommitPermission | FORBIDDEN |

## Worker Output Checker Read-Ahead Mandate

Before writing evidence/return, read checker source for each path family and
derive exact review headings, trace labels, delta fields, and no-commit shape.
Do not list heading-shaped checklist literals before real sections.

## Worker Return Packet Shape Contract

workerReturnPath: `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R2R1_LOCALHOST_NORMALIZED_RECOVERY_WORKER_RETURN_2026-07-15.md`

contractProfile: WORKER_RETURN_FULL_GATE_V1

requiredGate: `python governance/compat/run_worker_return_fast_gate.py`

individualCheckerSubstitution: FORBIDDEN

workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Skeleton command: `python governance/compat/run_worker_return_scaffold.py --write docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R2R1_LOCALHOST_NORMALIZED_RECOVERY_WORKER_RETURN_2026-07-15.md --title "CVF System Chain UC-04B R2R1 Localhost-Normalized Recovery Worker Return" --profile WORKER_RETURN_FULL_GATE_V1`

## Intake Role Routing Decision

| Field | Disposition |
|---|---|
| Intake route | operator continuation of reviewer-closed R2 blocker |
| canonical route mode | SINGLE_AGENT_SINGLE_ROLE |
| Selected role route | dispatcher -> no-commit worker -> reviewer/closer |
| scope classification | bounded local Web auth recovery proof |
| risk sensitivity | R1 provider-free development runtime |
| escalation condition | any fail condition |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Runtime/provider/MCP/readiness claim |
| Chain map route | current committed source plus bounded localhost Web regression |
| Matching local-view guard | `governance/compat/check_work_order_dispatch_quality.py` |
| Owner surface | Web auth adapter and system-chain GAP |
| Disposition | BLOCKED_UNTIL_CVF_PROOF |
| Claim boundary | R2 unit proof and diagnosis are not R2R1 browser proof |

## Legacy Absorption Coverage Index Disposition

NOT_APPLICABLE_WITH_REASON: internal Web regression; no legacy corpus intake.

## Evidence Reuse And Encoding Plan

verificationMode: RECOMPUTE_REQUIRED

recomputeReason: R2 browser proof failed under mixed host evidence

priorVerificationArtifact: `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R2_WEB_AUTH_PROJECTION_REPAIR_COMPLETION_2026-07-14.md`

priorVerificationAnchor: accepted runtime repair and blocker only; no browser PASS reuse

freshRecomputeRequired: yes, under fresh R2R1 authority

unicodePathHandling: literal repository paths and explicit UTF-8 readers; new governed prose is ASCII

extractedTextAuthority: N/A with reason: no OCR or external extraction input

## Provider Memory Authority Boundary

Provider memory and chat are not authority. Refresh all executable facts from
governed source and retained reviewer evidence.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | one localhost-normalized local Web auth projection regression |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT only through R2R1 ledger and receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT only if both retained cases pass |
| invocationBoundary | one Playwright command; zero business/checker/retry/provider calls |
| interceptionBoundary | no IDE, shell, git, provider, MCP, public, production, or universal interception claim |
| claimLanguage | selected local auth projections agreed under one canonical origin |
| forbiddenExpansion | no UC-04B business, all-auth, provider, production, public, scale, certification, or user-value claim |

## Verification Commands

```text
python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base <executionBaseHead> --head HEAD
cd EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npx vitest run src/lib/middleware-auth.test.ts src/app/api/auth/me/route.test.ts --reporter=verbose
npx tsc --noEmit -p tsconfig.json
$env:PLAYWRIGHT_BASE_URL='http://localhost:3001'; npx playwright test tests/e2e/system-chain-uc04b-auth-projection-regression.spec.ts --config playwright.config.ts --workers=1
cd ../../../..
python governance/compat/run_worker_return_fast_gate.py
python governance/compat/run_agent_commit_steward_preflight.py --mode reviewer-return --base <executionBaseHead> --head HEAD --enforce
git diff --check
git status --short
```

The Playwright line is the sole live invocation. Never repeat it.

## Review Gate

Reviewer checks committed-source immutability, focused preflight, proof hash,
canonical origin, ledger monotonicity, one invocation, both cases, host set,
projection agreement, exact counters, diagnostic accuracy, changed set,
tracked runtime hygiene, and unchanged worker HEAD.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Live runtime or provider proof`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cvf-web`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Live runtime or provider proof" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --max-results 20 --json`

Returned defects: ADIF-0033; ADIF-0035

Directly applicable governed defects: `CVF_ADIF-0034`; `CVF_ADIF-0035`.

The direct resolver execution returned zero JSON items. The changed-range ADIF
gate additionally required ADIF-0035 because the packet governs the canonical
host defect. These governed controls are explicitly applied because this packet
uses a protected retained proof and one live call.

## Commit Prompt Readiness

| Field | Value |
|---|---|
| workerCommitPrompt | FORBIDDEN |
| reviewerMaterialCommit | only after accepted review |
| sessionSyncCommit | separate after material decision |
| changedSetEvidence | exact manifest plus diff/status/stage evidence |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id SCLP-UC04B-R2R1 --title "System Chain UC-04B R2R1 Localhost-Normalized Recovery" --date 2026-07-15 --base 2feb62046 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | Web/UI plus no-commit recovery |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | canonical-host, immutable-ledger, exact manifest, cost, and closure controls |
| checkerReadAheadConfirmation | applicable checker sources and literal gotchas read |
| docOnlyNewFields | canonicalOrigin and observedHosts in dated evidence |
| claimBoundary | dispatch packet only |

## Foundation Storage Layout Block

Committed Web auth owners and proof spec remain read-only. New dated evidence
stays under reviews. No stable API, schema, config, provider, MCP, public, or
production surface is added.

## UI / Web Design Control Block

| Field | Value |
|---|---|
| canonicalDesignSource | `DESIGN.md` |
| designMutation | FORBIDDEN |
| visualProofScope | existing Operations active-role readout only |
| accessibilityInteraction | visible role text assertions |
| responsiveOrBrandClaim | N/A with reason: no redesign or viewport claim |
| evidenceBoundary | auth projection behavior only |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `WORKER_MUST_NOT_COMMIT`; `Source Verification Block`; `Planned Worker Fulfillment Manifest`; `Agent Handoff Contract Control Block`; `Public Export Disposition` |
| gateRunPurpose | confirmation after complete source and evidence inventory |
| claimBoundary | no-commit provider-free localhost recovery proof |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance recovery packet; no public-sync authority.

## Claim Boundary

A PASS proves only the selected local auth projections under one canonical
development origin in one evidence window. It does not prove UC-04B business
operation, all auth paths, provider governance, production, public readiness,
scale, certification, or user value.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | dispatcher/reviewer |
| Provider or surface | private provenance repository |
| Session or invocation | SCLP-UC04B-R2R1 packet authoring, 2026-07-15 |
| Working directory | repository root |
| Command or tool surface | governed reads, source search, apply_patch, resolver, dispatch gates |
| Target paths | paired R2R1 baseline and work order |
| Allowed scope source | active nextAllowedMove at `2feb62046` |
| Before status evidence | clean worktree at `2feb62046` |
| After status evidence | source-verified localhost recovery dispatch packet |
| Diff evidence | two-file dispatch diff before commit |
| Approval boundary | packet authoring and one later no-commit worker |
| Claim boundary | no Playwright, business, checker, provider, public, or source mutation in authoring batch |
| Agent type | dispatcher/reviewer |
| Invocation ID | `system-chain-uc04b-r2r1-dispatch-2026-07-15` |
| Expected manifest | paired R2R1 baseline and work order |
| Actual changed set | paired R2R1 baseline and work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |
