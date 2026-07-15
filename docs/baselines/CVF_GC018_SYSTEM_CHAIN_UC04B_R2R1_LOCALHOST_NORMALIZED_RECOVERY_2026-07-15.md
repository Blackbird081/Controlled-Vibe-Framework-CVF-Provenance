# CVF GC-018 System Chain UC-04B R2R1 Localhost-Normalized Recovery

Memory class: FULL_RECORD

Status: DISPATCH_READY

docType: gc018_baseline

Date: 2026-07-15

Risk classification: R1

## Purpose

Authorize one fresh provider-free regression invocation for the accepted R2
request-bound auth repair, using one explicit canonical localhost origin. This
is an auth-projection recovery only, not a UC-04B business-chain proof.

## Proposed Tranche / Decision

Authorize `SCLP-UC04B-R2R1` for one no-commit worker. Runtime, test, config,
proof source, and application owners are read-only. The worker may run focused
preflight, freeze the committed proof hash, set the Playwright base URL to
`http://localhost:3001`, invoke the retained spec exactly once, and return
dated evidence.

## Design Control Gate

| Control | Decision |
|---|---|
| repaired owner | committed R2 request-bound auth adapter, read-only |
| proof source | committed R2 two-case spec, read-only |
| canonical origin | `http://localhost:3001` for API request context, callback, and browser navigation |
| positive case | developer session, auth-me, and Operations operator projection |
| negative case | anonymous auth-me 401 and Operations anonymous projection |
| live ceiling | one Playwright command |
| cost ceiling | zero business submissions/checkers/retries/providers |

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| Playwright base URL accepts an environment override | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.ts` | use config | `PLAYWRIGHT_BASE_URL` | Playwright configuration | VALUE_SET | ACCEPT |
| Playwright port defaults to 3001 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.ts` | port constant | `PLAYWRIGHT_PORT` | Playwright configuration | VALUE_SET | ACCEPT |
| retained proof uses relative auth API and page paths | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-auth-projection-regression.spec.ts` | auth helper and both cases | `OPERATIONS_URL` | R2 proof spec | RUNTIME_BEHAVIOR | ACCEPT |
| retained proof has stable positive and negative cases | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-auth-projection-regression.spec.ts` | serial describe block | `positive_developer_auth_projection`; `negative_anonymous_auth_projection` | R2 proof spec | EXISTS | ACCEPT |
| request-bound adapter repair is committed | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | request resolver | `resolveBaseSessionFromRequest` | Web auth adapter | EXISTS | ACCEPT |
| R2 closure accepts repair but blocks browser proof | `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R2_WEB_AUTH_PROJECTION_REPAIR_COMPLETION_2026-07-14.md` | Decision and Evidence Reconciliation | `CLOSED_BLOCKED_BOUNDED` | reviewer closure | VALUE_SET | ACCEPT |
| canonical-host learning requires one origin | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0035.md` | Remediation | `ADIF-0035` | ADIF registry | VALUE_SET | ACCEPT |

## Current Runtime Freshness Verification

Fresh reads at dispatch base `2feb62046` confirm the committed repair, proof
spec, and environment override. The worker must refresh all facts and run the
focused tests before ledger creation. Any source change or failed preflight
blocks before Playwright.

## Dependency Release Evidence

| Dependency | Evidence | Disposition |
|---|---|---|
| R2 blocker is reviewer-closed | material commit `545628ca4` | SATISFIED |
| current session routes recovery packet | session commit `2feb62046` | SATISFIED |
| runtime repair is committed and test-proven | R2 completion plus material diff | SATISFIED |
| host-drift learning is governed | `CVF_ADIF-0035` | SATISFIED |
| dispatch start clean | empty status at `2feb62046` | SATISFIED |

## Roadmap-To-Work-Order Trace Matrix

| Requirement | R2R1 control | Evidence | Disposition |
|---|---|---|---|
| normalize proof environment | explicit localhost base URL | ledger and trace | READY |
| retain repair source | all owners read-only | clean diff | READY |
| prove both projections | retained serial two-case spec | receipt | READY |
| bound cost | one immutable ledger | exact 1/0/0/0/0 | READY |
| prevent business overclaim | retained business spec forbidden | reviewer closure | READY |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Live runtime or provider proof`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cvf-web`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Live runtime or provider proof" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --max-results 20 --json`

Returned defects: ADIF-0033; ADIF-0035

Directly applicable governed defects: `CVF_ADIF-0034`; `CVF_ADIF-0035`.

The direct resolver execution returned zero JSON items. The changed-range ADIF
gate additionally required ADIF-0035 because the packet governs the canonical
host defect; protected proof-path and immutable-ledger controls remain directly
applicable from governed entries.

## Cost And Retry Control

Exactly one Playwright command; zero business submissions, checker executions,
retries, and provider calls. On failure, create one diagnostic and stop.

## Acceptance Criteria

- Focused 12-test suite and typecheck pass before ledger start.
- Ledger records canonical origin `http://localhost:3001` and frozen spec hash.
- Exactly one command runs both stable cases successfully.
- Trace contains no `127.0.0.1:3001` request.
- Positive and anonymous projections match expected results.
- Business, checker, retry, and provider counters remain zero.
- No tracked source, config, proof, or runtime owner changes.

## Evidence / Verification

Required evidence includes clean base, source refresh, focused preflight,
frozen hash, canonical origin, monotonic ledger, command fingerprint, both
cases, host inventory, exact counters, conditional diagnostic, diff/status,
tracked runtime hygiene, and unchanged worker HEAD.

## Fail Conditions

Dirty start, source drift, focused failure, proof edit, ledger reset, second
command, any `127.0.0.1:3001` request, missing case, wrong projection, nonzero
cost counter, secret leak, staged change, commit, or stronger claim blocks.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance recovery packet; no public-sync scope.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Source Verification Block`; `Dependency Release Evidence`; `Public Export Disposition` |
| gateRunPurpose | confirmation after source and evidence inventory |
| claimBoundary | dispatch authorization only; no Playwright invocation in authoring batch |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id SCLP-UC04B-R2R1 --title "System Chain UC-04B R2R1 Localhost-Normalized Recovery" --date 2026-07-15 --base 2feb62046 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | Web/UI plus no-commit recovery |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source verification, canonical-host ledger, exact cost and closure controls |
| checkerReadAheadConfirmation | applicable checker sources and literal gotchas read |
| docOnlyNewFields | canonicalOrigin and observedHosts in dated evidence only |
| claimBoundary | packet authorization only |

## Claim Boundary

This baseline authorizes one local auth-projection regression under one
canonical host. It does not prove UC-04B business operation, all auth paths,
provider governance, production, public readiness, scale, certification, or
user value.
