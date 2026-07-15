# CVF GC-018 System Chain UC-04B R3R3 Reviewer Negative Proof

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: baseline

Date: 2026-07-15

GC-018 ID: `SCLP-UC04B-R3R3-GC018`

dispatchBaseHead: `ae9607022`

## Purpose

Authorize one negative-only canonical-origin browser proof against the accepted
R3R2 reviewer projection repair. The selected reviewer request must reach the
policy owner, return the expected denial, and stop before checker/provider work.

## Proposed Tranche / Decision

Dispatch one no-commit worker for evidence execution only. The retained proof
spec, UI, auth, API, job runtime, checker, provider, roadmap, GAP, and session
owners are read-only. One Playwright invocation is authorized; no retry is.

## Scope / Target / Owner Boundary

The target is only `negative_reviewer_docs_check` in the committed UC-04B proof
spec. The positive developer case is excluded. Worker writes are limited to a
new invocation ledger, proof receipt, conditional failure diagnostic, and
worker return. Disposable Playwright output and runtime audit data are evidence
inputs and must not be staged.

Risk ceiling: R1 local browser proof with a policy rejection before checker or
provider execution.

## Authorization / Dependency Release Evidence

| Dependency | Artifact | Commit | Final disposition |
|---|---|---|---|
| R3R2 local repair | `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R3R2_REVIEWER_AUTH_PROJECTION_REPAIR_COMPLETION_2026-07-15.md` | `52efec528` | ACCEPT; deterministic precondition satisfied |
| active route | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `ae9607022` | ACCEPT; R3R3 packet authoring released |
| proof source | committed proof spec | `52efec528` ancestry | ACCEPT; read-only negative case exists |
| architecture GAP | projection GAP entry | `52efec528` | ACCEPT; fresh negative browser proof is the close condition remainder |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| negative case is independently selectable | EXISTS | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-web-operations-readout.spec.ts` | lines 109-135 | `negative_reviewer_docs_check` | Playwright proof spec | ACCEPT |
| reviewer projection uses scoped exact locator | LITERAL_INVARIANT | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-web-operations-readout.spec.ts` | line 113 | `Active role` | negative proof precondition | ACCEPT |
| negative request uses jobs POST | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-web-operations-readout.spec.ts` | lines 119-126 | `negative_reviewer_docs_check` | negative proof action | ACCEPT |
| proof expects HTTP 403 and policy reason | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-web-operations-readout.spec.ts` | lines 128-130 | `read_only_role_cannot_trigger` | negative proof assertions | ACCEPT |
| proof expects requested then blocked events | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-web-operations-readout.spec.ts` | lines 132-134 | `blocked_by_policy` | audit assertion | ACCEPT |
| server wrapper supplies ambient role/user | RUNTIME_BEHAVIOR | `canonical-contract:cvf-web-operations-page-source` | lines 4-6 in current page source | `GovernanceOperationsPage` | Operations server entry | ACCEPT |
| client accepts reviewer props and retains auth refresh | RUNTIME_BEHAVIOR | `canonical-contract:cvf-web-operations-client-source` | lines 127-160 in current client source | `OperationsClient` | Operations client | ACCEPT |
| ambient session verifier exists | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | `verifySessionCookie` | `verifySessionCookie` | session adapter | ACCEPT |
| reviewer role is rejected before runner | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts` | `canTrigger`; blocked branch | `read_only_role_cannot_trigger` | Web job policy | ACCEPT |
| blocked result maps to HTTP 403 | RUNTIME_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/system/jobs/route.ts` | `POST` response status | `POST` | jobs API route | ACCEPT |
| canonical localhost can be selected | VALUE_SET | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.ts` | `use.baseURL` | `PLAYWRIGHT_BASE_URL` | Playwright config | ACCEPT |
| R3R2 releases exactly one negative proof | VALUE_SET | `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R3R2_REVIEWER_AUTH_PROJECTION_REPAIR_COMPLETION_2026-07-15.md` | Risk / Corrective Action | `SCLP-UC04B-R3R2` | reviewer closure | ACCEPT |

## New Doc-Only Fields

| Field | Owner | Disposition |
|---|---|---|
| `invocationStarted` | R3R3 ledger | DOC_ONLY_NEW |
| `positiveCaseExcluded` | R3R3 ledger and receipt | DOC_ONLY_NEW |
| `exactCounters` | R3R3 ledger and receipt | DOC_ONLY_NEW |
| `proofSourceHash` | R3R3 ledger and receipt | DOC_ONLY_NEW |

## Current Runtime Freshness Verification

The dispatcher recomputed proof SHA-256 as
`6568f0463feaa0b2680365e89bcd31c49c4245648cd3de12d409ed37e713f0ec`
at `ae9607022`, re-read the R3R2 owners, and found no source contradiction.
The worker must recompute the same hash before invocation and stop on mismatch.

## Design Control Gate

`DESIGN.md` was read. No visual, copy, layout, interaction, accessibility,
responsive, token, route, or component change is authorized. The proof observes
the existing role card and disabled action only.

## Cost And Retry Control

| Counter | Ceiling |
|---|---|
| Playwright browser invocations | 1 |
| reviewer Web submissions | 1 |
| selected checker executions | 0 |
| retries | 0 |
| provider calls | 0 |

The zero-provider requirement is material evidence: the reviewer request must
be rejected before checker/provider execution. A provider call would contradict
the selected denial path and block this tranche.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Packet control | Evidence target | Status |
|---|---|---|---|
| fresh reviewer browser denial | negative-only grep and one invocation | denial receipt | READY |
| retain positive evidence | positive case excluded | selection ledger | READY |
| prove repaired projection | scoped reviewer locator | browser observation | READY |
| reach policy POST | one direct browser-context request | HTTP 403 and job ID | READY |
| stop before checker/provider | audit/counter reconciliation | exact 1/1/0/0/0 | READY |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Web UI/dashboard`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cvf-web`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Web UI/dashboard" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --max-results 20 --json`

Returned defects: NONE_RETURNED

Applicable changed-range defects: `ADIF-0034`; `ADIF-0035`; `ADIF-0036`;
`ADIF-0037`. This packet uses one canonical origin, verifies client projection,
isolates the negative case, records a pre-spawn ledger, and forbids retry.

## Acceptance Criteria

- Proof source hash matches the declared committed hash.
- Focused five-file tests pass 34/34 and typecheck passes before invocation.
- Playwright list contains exactly the negative case and excludes positive.
- Exactly one canonical-localhost invocation runs.
- Reviewer role is visible and its Run control is disabled.
- Exactly one reviewer POST returns HTTP 403, `blocked_by_policy`, and
  `read_only_role_cannot_trigger`.
- Audit events equal requested then blocked_by_policy, with no runner/final.
- Counters equal 1/1/0/0/0; no retry or provider call occurs.
- Worker return is unstaged, uncommitted, and manifest-exact.

## Evidence / Verification

Worker evidence must include immutable pre-spawn ledger, reconciled proof
receipt, conditional secret-safe diagnostic on non-PASS, test/list/typecheck
output, audit baseline/finality, exact counters, secret scan, status/diff, and
unchanged HEAD.

## Fail Conditions

Dirty start, hash/source drift, proof/runtime edit, positive execution, wrong
host, more than one selected test, failed local preflight, second invocation,
missing reviewer projection, missing or incorrect denial, checker/runner event,
retry, provider call, secret leakage, staging, commit, or broader claim blocks
the worker without rerun.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance browser-proof dispatch; no public-sync authority.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Source Verification Block`; `Dependency Release Evidence`; `Roadmap-To-Work-Order Trace Matrix`; `Public Export Disposition` |
| gateRunPurpose | confirm current negative proof, policy boundary, exact ceilings, and dependency release before dispatch |
| claimBoundary | packet authorization only; no browser action in authoring batch |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id SCLP-UC04B-R3R3 --title "System Chain UC-04B R3R3 Reviewer Negative Proof" --date 2026-07-15 --base ae9607022 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | Web/UI no-commit negative-only proof |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source verification, immutable ledger, negative selection, exact counter, diagnostic, and no-retry controls |
| checkerReadAheadConfirmation | applicable checker sources and literal gotchas read |
| docOnlyNewFields | R3R3 dated ledger/receipt fields only |
| claimBoundary | dispatch authoring provenance only |

## Claim Boundary

This baseline authorizes one local negative reviewer proof. It does not prove
the retained positive path again, full UC-04B, unified checker inventory,
provider governance, public or production readiness, scale, certification, or
real-user value.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | R3R3 work order | `CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | R3R3 completion review | reviewer acceptance | PASS |
| Roadmap state | system-chain roadmap | T5 final projection next | PASS |
| Registry JSON | coverage and generated GAP index | selected pair projected | PASS |
| Registry Markdown | system-chain front door | R3R3 accepted | PASS |
| External evidence digest | N/A with reason: repository evidence only | no external input | N/A with reason |
| System loop interlock | receipt and isolated audit sequence | exact 1/1/0/0/0 | PASS |
| Session continuity | active session surfaces | separate post-material sync | N/A with reason |

## Acceptance Receipt Assertion Matrix

| Criterion | Required value | Observed value | Status |
|---|---|---|---|
| reviewer projection | reviewer | reviewer | PASS |
| policy outcome | HTTP 403 blocked | HTTP 403 `blocked_by_policy` | PASS |
| audit sequence | requested then blocked | requested then blocked | PASS |
| counters | 1/1/0/0/0 | 1/1/0/0/0 | PASS |
