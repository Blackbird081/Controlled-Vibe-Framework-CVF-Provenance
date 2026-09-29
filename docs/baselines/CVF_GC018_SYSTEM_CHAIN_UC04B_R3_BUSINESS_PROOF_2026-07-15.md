# CVF GC-018 System Chain UC-04B R3 Business Proof

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: baseline

Date: 2026-07-15

GC-018 ID: `SCLP-UC04B-R3-GC018`

dispatchBaseHead: `4c8a8231f`

## Purpose

Authorize one bounded, provider-free Web Operations business proof after the
developer/anonymous auth-projection dependency was accepted in R2R1.

## Proposed Tranche / Decision

Dispatch one no-commit worker to execute the retained, byte-frozen
`docs_governance_check` two-case Playwright spec under one canonical localhost
origin. The positive case may submit the allowlisted job once and execute its
fixed docs checker once. The negative reviewer case may submit once and must be
blocked before runner execution.

## Design Control Gate

- `DESIGN.md` was read because the proof asserts a current UI readout.
- No UI, runtime, config, auth, job, route, test, or checker owner may change.
- The retained UI and proof source are evidence consumers only.
- This tranche tests existing behavior; it does not redesign the surface.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| selected business job exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts` | lines 154-160 | `docs_governance_check` | Web governance job definition | VALUE_SET | ACCEPT |
| selected job uses fixed checker argv | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts` | lines 157-159 | `buildArgv` | Web governance job definition | LITERAL_INVARIANT | ACCEPT |
| reviewer is read-only | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts` | lines 211-234 | `canTrigger` | Web authorization policy | RUNTIME_BEHAVIOR | ACCEPT |
| blocked request returns before runner | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts` | lines 449-521 | `submitGovernanceJob` | Web job execution owner | RUNTIME_BEHAVIOR | ACCEPT |
| selected job avoids live-provider cost preflight | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts` | lines 415-443 | `liveEstimateJobTypes` | provider/cost boundary | VALUE_SET | ACCEPT |
| API maps developer to operator | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/system/jobs/route.ts` | lines 37-58 | `POST` | system jobs API | RUNTIME_BEHAVIOR | ACCEPT |
| API returns 403 on policy block | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/system/jobs/route.ts` | lines 60-65 | `POST` | system jobs API | RUNTIME_BEHAVIOR | ACCEPT |
| UI offers and submits selected job | canonical-contract:cvf-web-operations-page-source | lines 62-105 and 165-185 in the freshly read page source | `JOBS`; `runJob` | Operations page | RUNTIME_BEHAVIOR | ACCEPT |
| UI exposes latest job and audit readout | canonical-contract:cvf-web-operations-page-source | lines 314-367 in the freshly read page source | `latest`; `jobs` | Operations page | RUNTIME_BEHAVIOR | ACCEPT |
| credentials resolve developer and reviewer roles | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | lines 42-78 | `authorize` | Auth.js credentials owner | RUNTIME_BEHAVIOR | ACCEPT |
| retained proof contains two stable cases | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-web-operations-readout.spec.ts` | lines 71-135 | `positive_developer_docs_check`; `negative_reviewer_docs_check` | Playwright proof | EXISTS | ACCEPT |
| retained proof hash | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-web-operations-readout.spec.ts` | SHA-256 recomputation | `89aaf5a078c7c90bb01265d5f982110f6a077343641bff09e245eb5cff271d49` | Playwright proof | LITERAL_INVARIANT | ACCEPT |
| canonical origin override controls relative paths | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.ts` | `use.baseURL` | `PLAYWRIGHT_BASE_URL` | Playwright config | VALUE_SET | ACCEPT |
| R2R1 released business packet authoring | `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R2R1_LOCALHOST_NORMALIZED_RECOVERY_COMPLETION_2026-07-15.md` | Decision and Risk / Corrective Action | `Decision` | reviewer closure | VALUE_SET | ACCEPT |

## Current Runtime Freshness Verification

The worker must re-read every ACCEPT source at execution base, recompute the
proof hash, require a clean worktree, and stop on any contradiction. Existing
owners are not repairable under this packet.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition |
|---|---|---|---|
| bounded auth projection | `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R2R1_LOCALHOST_NORMALIZED_RECOVERY_COMPLETION_2026-07-15.md` | `37942fb38` | SATISFIED |
| session route | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `4c8a8231f` | SATISFIED |
| retained proof owner | cited committed spec | `4c8a8231f` execution ancestry | SATISFIED |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Packet control | Evidence target | Status |
|---|---|---|---|
| real Web business path | retained real Playwright config | positive UI submission | READY |
| visible outcome | UI job ID/status/audit assertions | receipt | READY |
| meaningful deny case | reviewer POST | 403 plus blocked audit | READY |
| bounded cost | docs-only job | zero provider calls | READY |
| no unified inventory claim | explicit boundary | worker return | READY |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Live runtime or provider proof`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cvf-web`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Live runtime or provider proof" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --max-results 20 --json`

Returned defects: ADIF-0033; ADIF-0034; ADIF-0035

Directly applicable governed defects: `CVF_ADIF-0033`; `CVF_ADIF-0034`;
`CVF_ADIF-0035`.

The direct resolver returned zero JSON items. Changed-range applicability and
the retained failure history require protected-call authorization, immutable
invocation accounting, and canonical-host normalization in this packet.

## Cost And Retry Control

Exactly one Playwright invocation, two Web submissions, one selected docs
checker execution, zero retries, and zero provider calls. Governance gates and
focused unit tests are control-plane verification, not selected business-job
checker executions. Any unclear or failed Playwright result consumes the
invocation and stops the worker.

## Acceptance Criteria

- Focused owner/auth preflight passes 32/32.
- Frozen business proof hash matches the declared SHA-256.
- One invocation uses `http://localhost:3001` and runs both cases serially.
- Developer UI submission succeeds and exposes matching job/audit evidence.
- Reviewer submission returns 403 and emits no runner/final event.
- Counters equal 1/2/1/0/0 for invocation/submission/checker/retry/provider.
- No retained owner changes and worker HEAD stays unchanged.

## Evidence / Verification

Worker produces an immutable invocation ledger, reconciled two-case receipt,
conditional diagnostic on non-PASS, and no-commit worker return. Reviewer owns
closure, reverse projection, material commit, and session sync.

## Fail Conditions

Dirty start, source/hash drift, focused failure, proof edit, wrong host, second
invocation, case skip/fail, wrong counters, provider use, missing UI/audit
evidence, secret leak, retained-owner mutation, staged path, commit, or broader
claim blocks the packet without retry.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance business-proof dispatch; no public-sync authority.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Source Verification Block`; `Dependency Release Evidence`; `Roadmap-To-Work-Order Trace Matrix`; `Public Export Disposition` |
| gateRunPurpose | confirm current business, auth, UI, proof, and cost contracts before dispatch |
| claimBoundary | dispatch authorization only; no business invocation in authoring batch |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id SCLP-UC04B-R3 --title "System Chain UC-04B R3 Business Proof" --date 2026-07-15 --base 4c8a8231f --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | Web/UI no-commit live business proof |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source verification, retained-proof hash, ledger, counters, cost, and closure controls |
| checkerReadAheadConfirmation | applicable checker sources and literal gotchas read |
| docOnlyNewFields | R3 dated ledger and receipt fields only |
| claimBoundary | packet authorization only |

## Claim Boundary

This baseline authorizes one provider-free local business proof for one
allowlisted docs job and one reviewer denial. It does not prove unified checker
inventory, other jobs/roles, provider governance, public, production, scale,
certification, or user value.
