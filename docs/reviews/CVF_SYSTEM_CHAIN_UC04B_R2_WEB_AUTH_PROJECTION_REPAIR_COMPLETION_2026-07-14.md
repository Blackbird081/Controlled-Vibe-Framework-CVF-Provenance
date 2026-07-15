# CVF System Chain UC-04B R2 Web Auth Projection Repair Completion

Memory class: FULL_RECORD

Status: CLOSED_BLOCKED_BOUNDED

docType: review

Date: 2026-07-15

rawMemoryReleased=false

Responds to work order:
`CVF_AGENT_WORK_ORDER_SYSTEM_CHAIN_UC04B_R2_WEB_AUTH_PROJECTION_REPAIR_2026-07-14.md`

## Purpose

Accept the bounded request-auth repair, correct the live-failure diagnosis,
and close the consumed R2 invocation without rerun or Web-coverage promotion.

## Scope / Target / Owner Boundary

Reviewer scope is the returned runtime/test/proof diff, ledger, receipt,
diagnostic, trace, worker return, GC-051 entry/aggregate, paired dispatch
status, architecture GAP, coverage/readout surfaces, and learning registry.
No new Playwright, business, checker, or provider invocation is performed.

## Target / Source

Targets are current auth owners/tests, Auth.js dependency contract, R2 evidence,
the retained trace, Playwright config, paired dispatch, system-chain roadmap,
coverage ledger, GAP entry/index/front door, and ADIF registry.

## Scope / Methodology

The reviewer ran worker-return fast checks, independently reran the focused
12-test suite and TypeScript check, inspected the trace network and action
streams, compared API-request and browser-navigation rows, and reconciled exact
counters and changed paths. Playwright was not rerun.

## Decision

`SCLP-UC04B-R2` is `CLOSED_BLOCKED_BOUNDED`. The request-bound adapter repair
is accepted as locally unit-proven. The E2E proof is not accepted; the sole
invocation is consumed and R2 must not be rerun.

## Findings / Position

The runtime diff is source-aligned: supplied requests use `getToken` with the
shared secret; ambient `auth()` and impersonation remain covered. Reviewer
verification is 12/12 focused PASS plus clean typecheck.

The worker correctly detected mixed `127.0.0.1`/`localhost` evidence but
overstated the failure stage. The trace proves:

- Auth.js callback handling inside `page.request` redirected from
  `127.0.0.1` to `localhost`.
- The later browser `page.goto` actually requested `127.0.0.1` and carried the
  Auth.js session cookie.
- After page load, the browser emitted neither `/api/auth/me` nor
  `/api/system/jobs`; the role therefore remained its initial anonymous value.
- Dev-client HMR reported origin-related failures.

Therefore `cookie not sent on browser navigation` is rejected. The bounded
accepted diagnosis is `CANONICAL_DEV_HOST_AND_CLIENT_HYDRATION_MISMATCH`.

## Risk / Corrective Action

Do not modify `next.config.ts` based on the rejected cookie-loss claim. The
smallest recovery is proof-environment normalization: run the retained spec
under one explicit `http://localhost:<port>` Playwright base URL in a fresh
one-invocation packet. If that still fails, diagnose the newly observed stage
without retry.

## Evidence Reconciliation

| Question | Evidence | Reviewer disposition |
|---|---|---|
| runtime repair | source diff; 12/12 focused; typecheck | ACCEPT_BOUNDED |
| proof hash | ledger, receipt, retained spec | ACCEPT |
| Playwright invocations | 1 | ACCEPT |
| positive case | FAIL | BLOCKED |
| negative case | DID_NOT_RUN | BLOCKED |
| business/checker/retry/provider | 0/0/0/0 | ACCEPT |
| browser navigation host | `127.0.0.1` with session cookie | worker cookie-loss claim REJECTED |
| callback redirect host | `localhost` inside API request context | ACCEPT host drift |
| client auth/jobs requests | none after browser page load | ACCEPT hydration-stage blocker |
| worker commit | none; HEAD unchanged at return | ACCEPT |
| GC-051 delta | one source entry plus generated aggregate | ACCEPT as mandatory governed coverage |

## Closure Diff Gate

| Requirement | Final evidence | Result |
|---|---|---|
| request-bound implementation | accepted source diff | PASS_BOUNDED |
| focused tests and typecheck | reviewer 12/12 plus clean typecheck | PASS |
| one immutable invocation | ledger and trace | PASS |
| positive/negative E2E | FAIL/DID_NOT_RUN | BLOCKED |
| exact zero cost counters | 0/0/0/0 | PASS |
| no retry/provider/business run | trace and ledger | PASS |
| diagnosis accuracy | reviewer trace correction | PASS after correction |

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Learning disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| mixed host aliases and request-context confusion produced a false cookie-loss diagnosis | RULE_GAP | GOVERNANCE_CONTROL_PLANE | RULE_ADDED | ADIF-0035 plus canonical-host recovery | handled |
| request-bound auth adapter passed focused tests but browser projection remains unproven | RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | RUNTIME_LEARNING_CANDIDATE | one fresh localhost-normalized regression | deferred |

## Catalog / GAP Reverse Projection

The existing auth-projection GAP remains open but is narrowed: the adapter
owner is repaired and unit-proven; browser projection remains E2E-unproven due
to the dev-host/hydration blocker. UC-04B Web coverage remains unproven.

## Verification / Evidence

- Worker-return fast gate: PASS, including reviewer-fast 62/62.
- Reviewer focused suite: 12/12 PASS.
- Reviewer `tsc --noEmit`: PASS.
- Playwright invocations added by reviewer: zero.
- Retained worker counters: one invocation; zero business submissions,
  checker executions, retries, and provider calls.

## Epistemic Process Block

### Expected Result / Prediction

If cookie loss caused the page failure, the actual browser navigation request
would omit the Auth.js session cookie.

### Evidence Comparison

It did not: the browser request to `127.0.0.1` included the session cookie.
The cross-host redirect occurred earlier inside the API request context, and
no client auth/jobs request followed browser page load.

### Contradiction Or Gap Disposition

Reject cookie-loss attribution, retain canonical host/hydration mismatch as
the bounded blocker, and require a fresh localhost-normalized proof.

### Claim Update

R2 proves a local adapter repair through focused tests only. It does not prove
browser projection agreement or UC-04B Web operation.

## Acceptance Criteria

- [x] Runtime diff source-reviewed.
- [x] Focused tests and typecheck independently pass.
- [x] One invocation and zero retry reconciled.
- [x] Zero business/checker/provider counters retained.
- [x] Worker diagnosis corrected against trace evidence.
- [x] ADIF learning made cross-session discoverable.
- [x] No E2E, UC-04B, or stronger PASS claim made.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private blocked-proof closure and repair evidence; no public scope.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_adif_entry_integrity.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_machine_closure_package.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Status: CLOSED_BLOCKED_BOUNDED`; `Closure Diff Gate`; `Catalog / GAP Reverse Projection`; `Acceptance Receipt Assertion Matrix`; `Public Export Disposition` |
| gateRunPurpose | reviewer confirmation after source and trace reconciliation |
| claimBoundary | blocker closure only; no recovery invocation |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Baseline status | paired R2 GC-018 | `CLOSED_BLOCKED_BOUNDED` | PASS |
| Work order status | SCLP-UC04B-R2 | `CLOSED_BLOCKED_BOUNDED` | PASS |
| Completion or reviewer artifact | this review | `CLOSED_BLOCKED_BOUNDED` | PASS |
| Worker return | declared R2 return | `BLOCKED_WITH_REASON` | PASS |
| Runtime repair | auth owners and tests | 12/12 plus typecheck PASS | PASS_BOUNDED |
| Proof and ledger | R2 JSON evidence | FAIL; exact 1/0/0/0/0 | PASS for blocker closure |
| Architecture learning | GAP plus ADIF-0035 | narrowed blocker | PASS |
| Roadmap state | system-chain use-case roadmap | localhost-normalized recovery next | PASS |
| Registry JSON | coverage, GAP index, and corpus aggregate | R2 blocked and GAP open | PASS |
| Registry Markdown | system-chain, GAP, and ADIF front doors | corrected blocker route | PASS |
| External evidence digest | N/A with reason: repository/runtime evidence only | no external input | N/A with reason |
| System loop interlock | R2 ledger and receipt | FAIL retained; no Web promotion | PASS |
| Session continuity | active session | separate post-material sync | N/A with reason |
| Public export | this review | `DEFERRED_PRIVATE_ONLY` | PASS |

## Acceptance Receipt Assertion Matrix

| Assertion | Required | Observed | Status |
|---|---|---|---|
| Playwright invocation | 1 | 1 | PASS |
| positive projection | PASS | FAIL before client auth fetch | BLOCKED |
| negative projection | PASS | DID_NOT_RUN | BLOCKED |
| business submissions | 0 | 0 | PASS |
| checker executions | 0 | 0 | PASS |
| retries | 0 | 0 | PASS |
| provider calls | 0 | 0 | PASS |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | reviewer/closer |
| Provider or surface | private repository; no provider call |
| Session or invocation | SCLP-UC04B-R2 closure, 2026-07-15 |
| Working directory | repository root |
| Command or tool surface | evidence/source reads, zip trace inspection, Vitest, typecheck, apply_patch, reviewer gates |
| Target paths | returned R2 set, completion, paired status, GC-051, GAP/coverage/readout, ADIF |
| Allowed scope source | Reviewer Closure Conversion in SCLP-UC04B-R2 |
| Before status evidence | BLOCKED worker return at HEAD `9a1043404` |
| After status evidence | accepted bounded runtime repair; corrected blocker; recovery packet eligible |
| Diff evidence | `git diff --name-status` and status before commit |
| Approval boundary | closure/reverse projection/learning; no live retry |
| Claim boundary | UC-04B remains unproven |
| Agent type | reviewer/closer |
| Invocation ID | system-chain-uc04b-r2-blocked-closure-2026-07-15 |
| Expected manifest | returned R2 paths plus reviewer completion/status/GAP/coverage/ADIF paths |
| Actual changed set | reviewer material closure set |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This closure proves only the request-bound adapter repair through focused local
tests and one coherently stopped browser proof. It does not prove browser
projection agreement, UC-04B Web operation, unified inventory, provider
governance, public, production, scale, certification, or user value.
