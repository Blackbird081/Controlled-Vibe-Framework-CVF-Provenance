# CVF GC-018 System Chain UC-04B R3R1 Negative Locator Recovery

Memory class: FULL_RECORD

Status: CLOSED_BLOCKED_BOUNDED

docType: baseline

Date: 2026-07-15

GC-018 ID: `SCLP-UC04B-R3R1-GC018`

dispatchBaseHead: `a41660892`

## Purpose

Authorize the smallest recovery that can close the remaining UC-04B reviewer
browser-denial GAP without repeating the already accepted developer business
path.

## Proposed Tranche / Decision

Dispatch one no-commit worker to replace exactly one ambiguous negative-case
locator in the retained Playwright proof, verify that Playwright selects only
the negative case, and run that case once under the canonical localhost origin.

## Design Control Gate

- Root `DESIGN.md` was read because the proof observes the current UI.
- No UI, runtime, auth, route, job, checker, config, or design change is allowed.
- The proof spec may change only at its negative pre-submission role assertion.
- The developer positive case is retained from R3 and must not run again.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Source fact type | Disposition |
|---|---|---|---|---|---|---|
| negative case exists independently | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-web-operations-readout.spec.ts` | lines 109-135 | `negative_reviewer_docs_check` | Playwright proof | EXISTS | ACCEPT |
| ambiguous assertion precedes POST | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-web-operations-readout.spec.ts` | lines 113-119 | `page.getByText('reviewer')` | negative proof case | LITERAL_INVARIANT | ACCEPT |
| Active role and role value share one local container | canonical-contract:cvf-web-operations-page-source | lines 210-214 in the freshly read page source | `Active role` | Operations page header card | EXISTS | ACCEPT |
| selected run button has stable test ID | canonical-contract:cvf-web-operations-page-source | lines 224-270 in the freshly read page source | `governance-job-run-` | Operations job card | EXISTS | ACCEPT |
| reviewer is denied selected job | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/web-governance-jobs.ts` | `canTrigger`; `submitGovernanceJob` | `read_only_role_cannot_trigger` | Web job authorization | RUNTIME_BEHAVIOR | ACCEPT |
| API returns policy block as 403 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/system/jobs/route.ts` | `POST` policy-block branch | `POST` | system jobs API | RUNTIME_BEHAVIOR | ACCEPT |
| canonical origin override exists | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.ts` | `use.baseURL` | `PLAYWRIGHT_BASE_URL` | Playwright config | VALUE_SET | ACCEPT |
| R3 positive result is retained and negative is pending | `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R3_BUSINESS_PROOF_COMPLETION_2026-07-15.md` | Decision; Risk / Corrective Action | `SCLP-UC04B-R3` | reviewer closure | VALUE_SET | ACCEPT |
| locator GAP requires negative-only recovery | `docs/reference/system_chain/gaps/entries/web_reviewer_denial_proof_locator_ambiguity.json` | `closeCondition`; `actionOwner` | `cvf.asc.gap.web_reviewer_denial_proof_locator_ambiguity.v1` | system-chain GAP registry | VALUE_SET | ACCEPT |

## New Implementation Item

| Item | Exact authorized shape | Existing-source claim |
|---|---|---|
| scoped negative role locator | `page.getByText('Active role', { exact: true }).locator('..').getByText('reviewer', { exact: true })` | DOC_ONLY_NEW implementation instruction; not claimed to exist before worker edit |

## Current Runtime Freshness Verification

At execution base, re-read the proof spec, Operations page source, Web job
owner, API route, and Playwright config. Recompute the pre-edit proof hash and
stop if the named case, locator, role card, denial reason, or canonical-origin
control no longer matches this packet. No capability-absence claim is made.

## Dependency Release Evidence

| Dependency | Artifact | Commit | Disposition |
|---|---|---|---|
| R3 bounded closure | `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R3_BUSINESS_PROOF_COMPLETION_2026-07-15.md` | `e1ce6dc18` | SATISFIED |
| locator learning | `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0036.md` | `e1ce6dc18` | SATISFIED |
| active session route | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` | `a41660892` | SATISFIED |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Packet control | Evidence target | Status |
|---|---|---|---|
| close reviewer browser-denial edge | negative-only grep | 403 and blocked audit receipt | READY |
| avoid duplicate positive work | positive case excluded | list output and invocation command | READY |
| repair proof harness only | one exact locator change | tracked diff | READY |
| preserve zero provider cost | reviewer rejection before runner | exact 1/1/0/0/0 counters | READY |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Web UI/dashboard`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, surfaceSelector=`cvf-web`

Query: `python governance/compat/run_adif_defect_resolver.py --task-class "Web UI/dashboard" --role dispatcher --lifecycle-phase pre-dispatch --surface-selector cvf-web --max-results 20 --json`

Returned defects: NONE_RETURNED

Changed-range applicability: `ADIF-0034`; `ADIF-0035`; `ADIF-0036`. R3R1
uses one invocation, one canonical origin, a scoped pre-action locator, and no
same-packet retry.

## Cost And Retry Control

Exactly one Playwright invocation, one reviewer Web submission, zero selected
checker executions, zero retries, and zero provider calls. Playwright `--list`,
focused tests, and governance gates do not count as business invocations.

## Acceptance Criteria

- The proof diff changes exactly one locator expression.
- Focused owner/auth tests remain 32/32 PASS.
- Playwright list selects exactly the negative stable case.
- One negative invocation uses `http://localhost:3001`.
- Reviewer POST returns 403 with `blocked_by_policy` and
  `read_only_role_cannot_trigger`.
- Audit events equal requested then blocked_by_policy, with no runner event.
- Exact counters equal 1/1/0/0/0.
- Positive case does not run and no provider call occurs.

## Evidence / Verification

Worker returns the changed proof spec, immutable invocation ledger, negative
receipt, conditional diagnostic, and no-commit worker return. Reviewer owns
closure, GAP projection, material commit, and session sync.

## Fail Conditions

Dirty start, source contradiction, wider proof/UI/runtime diff, positive-case
execution, more than one selected test, focused failure, wrong host, second
invocation, missing denial/audit evidence, runner/checker event, retry, provider
call, secret leak, staging, commit, or broader claim blocks without retry.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | local worker using Playwright and repository source | exact five-path manifest; no commit | ledger, receipt, return | internal local test surface only | `IMPLEMENTED` |
| `EXTERNAL_AGENT_CLI_MCP` | no external adapter owner | no ingress, authentication, action, receipt, or mutation authority | no external execution authorized | separate source-verified adapter required | `DEFERRED_WITH_REASON` |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance recovery dispatch; no public-sync authority.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Status: DISPATCH_READY`; `Source Verification Block`; `Dependency Release Evidence`; `Roadmap-To-Work-Order Trace Matrix`; `Dual Agent Surface Matrix`; `Public Export Disposition` |
| gateRunPurpose | confirm negative-case isolation, locator owner, runtime denial route, and exact cost boundary before dispatch |
| claimBoundary | packet authorization only; no browser invocation in authoring batch |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id SCLP-UC04B-R3R1 --title "System Chain UC-04B R3R1 Negative Locator Recovery" --date 2026-07-15 --base a41660892 --commit-mode WORKER_MUST_NOT_COMMIT --stdout` |
| generatedProfile | Web/UI no-commit negative-only recovery |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | source verification, exact locator, grep isolation, ledger, counters, and closure controls |
| checkerReadAheadConfirmation | applicable checker sources and literal gotchas read |
| docOnlyNewFields | R3R1 dated evidence fields and exact locator instruction only |
| claimBoundary | dispatch authorization only |

## Claim Boundary

This baseline authorizes one negative-only local reviewer-denial recovery. It
does not re-prove the positive path or prove unified inventory, other jobs or
roles, provider governance, public or production readiness, scale,
certification, or user value.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | SCLP-UC04B-R3R1 | `CLOSED_BLOCKED_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R3R1_NEGATIVE_LOCATOR_RECOVERY_COMPLETION_2026-07-15.md` | `CLOSED_BLOCKED_BOUNDED` | PASS |
| Registry JSON | coverage and generated GAP index | reviewer projection reopened | PASS |
| Registry Markdown | system-chain and GAP front doors | R3R2 route | PASS |
| System loop interlock | exact worker ledger | 1/0/0/0/0 | PASS |
| Roadmap state | system-chain roadmap | R3R2 packet next | PASS |
| External evidence digest | N/A with reason: repository/runtime evidence only | no external input | N/A with reason |
| Session continuity | active session | separate post-material sync | N/A with reason |
| Public export | this baseline | `DEFERRED_PRIVATE_ONLY` | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required | Observed | Status |
|---|---|---|---|
| Playwright invocation | 1 | 1 | PASS |
| reviewer denial | PASS | pre-POST projection FAIL | BLOCKED |
| Web submissions | 1 | 0 | BLOCKED_DIAGNOSED |
| checker executions | 0 | 0 | PASS |
| retries | 0 | 0 | PASS |
| provider calls | 0 | 0 | PASS |
