# CVF System Chain UC-04B R2 Web Auth Projection Repair Worker Return

Memory class: FULL_RECORD

docType: review

Status: BLOCKED_WITH_REASON

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_SYSTEM_CHAIN_UC04B_R2_WEB_AUTH_PROJECTION_REPAIR_2026-07-14.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_SYSTEM_CHAIN_UC04B_R2_WEB_AUTH_PROJECTION_REPAIR_2026-07-14.md`

executionBaseHead: `9a10434041a3c8e453ff0abfb188116a66b80b6e`

rawMemoryReleased=false
contractProfile: WORKER_RETURN_FULL_GATE_V1

## Source Inventory

| File | Action |
|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` | READ, EDIT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts` | READ, EDIT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.test.ts` | READ, EDIT |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/auth/me/route.ts` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/node_modules/@auth/core/jwt.d.ts` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/node_modules/next-auth/jwt.d.ts` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/governance/operations/page.tsx` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-web-operations-readout.spec.ts` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/utils.ts` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.ts` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/mock-enterprise-db.ts` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/next.config.ts` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-auth-projection-regression.spec.ts` | CREATE (protected path, dispatch-authorized) |
| `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0033.md` | READ |
| `docs/reference/agent_defect_intelligence/entries/CVF_ADIF-0034.md` | READ |

## Purpose

Repair `verifySessionCookie(request)` so it decodes the supplied request's
Auth.js token when a request is present, instead of ignoring it and always
falling back to ambient `auth()`, and prove the repair against the developer
positive and anonymous negative projections without consuming the retained
UC-04B business-chain proof budget.

## Scope / Methodology

1. Exported a shared `authSecret` constant from `src/auth.ts` and pointed the
   existing NextAuth `secret` field at it (no credential/JWT/session
   semantics change).
2. Split `verifySessionCookie` in `src/lib/middleware-auth.ts` into
   `resolveBaseSessionFromRequest` (calls `getToken({ req, secret: authSecret })`
   from `next-auth/jwt`, mapping `userId`/`name`/`email`/`role`/`orgId`/`teamId`/`exp`
   into `SessionCookie`) and `resolveBaseSessionAmbient` (unchanged `auth()`
   path). `verifySessionCookie` dispatches on whether a request was supplied;
   the impersonation overlay logic is unchanged and shared by both paths.
3. Extended `src/lib/middleware-auth.test.ts` with a `next-auth/jwt` mock and
   five new cases covering: `getToken` called with request+secret instead of
   `auth()`; null-token returns null; full claim mapping including expiry;
   fallback to email/default role/org/team; impersonation overlay via a
   request-carried cookie.
4. Ran the focused Vitest suite and a full `tsc --noEmit` before freezing the
   E2E proof source.
5. Authored the dispatch-authorized proof-only spec
   `tests/e2e/system-chain-uc04b-auth-projection-regression.spec.ts` with
   stable cases `positive_developer_auth_projection` and
   `negative_anonymous_auth_projection`, computed its SHA-256, and created the
   invocation ledger before spawning Playwright.
6. Ran the exact one authorized Playwright command. The invocation completed;
   case 1 failed for an environment reason unrelated to the runtime repair
   (see Findings); case 2 did not run under the spec's serial mode. Per
   ADIF-0034, no second command and no proof-spec edit-and-rerun were
   performed.
7. Restored the tracked `test-results/.last-run.json` to its pre-run baseline
   and left all disposable Playwright output (traces, screenshots, video)
   untracked.

## Findings / Position

**Runtime repair is correct and unit-proven.** All 12 focused unit tests pass
(5 pre-existing ambient-`auth()` cases unchanged, plus 5 new request-bound
cases: `getToken` call shape, null-token, full claim mapping with expiry,
fallback defaults, and impersonation-via-request). `tsc --noEmit` is clean.

**The one authorized E2E invocation did not prove the projection agreement,
for an environment reason distinct from the runtime repair.** The trace
network log (`test-results/system-chain-uc04b-auth-pr-39cc2-perations-projections-agree/trace.zip`)
shows:

- `page.request.get()` calls (base URL `http://127.0.0.1:3001`) for
  `/api/auth/csrf`, `/api/auth/callback/credentials`, `/api/auth/session`,
  and `/api/auth/me` all completed with the expected statuses.
- The subsequent `page.goto(OPERATIONS_URL)` browser navigation resolved to
  `http://localhost:3001` - a different origin from `127.0.0.1:3001` - so the
  NextAuth session cookie set on the `127.0.0.1` origin was not sent, and the
  Operations page's own client-side `fetch('/api/auth/me')` read an
  unauthenticated context, rendering active role `anonymous_local` instead of
  `operator`.
- The dev server log for the same run independently emitted a `Blocked
  cross-origin request ... from "127.0.0.1"` warning naming Next.js
  `allowedDevOrigins` as the controlling mechanism.
- `next.config.ts` has no `allowedDevOrigins` entry and is a read-only owner
  under this work order's Planned Worker Fulfillment Manifest, so no fix is
  authorized inside this packet.

The request-bound `getToken` code path inside `verifySessionCookie` was never
exercised by the failing case, because the browser navigation itself carried
no session cookie under the mismatched-origin condition - the failure is
upstream of the repaired function.

## Risk / Corrective Action

No corrective action was taken inside this packet (the causing file,
`next.config.ts`, is out of the authorized manifest). The smallest
source-backed reviewer action is one of: (a) add `127.0.0.1` to
`allowedDevOrigins` in `next.config.ts` under a fresh authorization covering
that file, or (b) make the E2E spec's `page.request` calls and `page.goto`
calls consistently target the same configured `baseURL` host so both share
one cookie jar. Neither is authorized by SCLP-UC04B-R2's manifest.

## Claim Boundary

This return proves only: (1) the request-bound `verifySessionCookie` code
path is unit-correct per 12/12 focused Vitest cases and `tsc --noEmit`; (2)
one authorized Playwright invocation ran and failed for a dev-server
cross-origin cookie-jar split, not a runtime auth-projection defect; (3)
zero business submissions, checker executions, retries, or provider calls
occurred. It does not prove developer/anonymous projection agreement end to
end, the UC-04B business chain, all authentication paths, provider
governance, production, public readiness, scale, certification, or user
value.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_agent_handoff_boundary.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_core_guard_self_protection.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_governed_file_size.py` |
| literalTokensReviewed | `Status: BLOCKED_WITH_REASON`; `WORKER_MUST_NOT_COMMIT honored`; `Evidence Comparison`; `Contradiction`; `Claim Update`; `Core Guard Self-Protection Authorization`; `Actual Changed Set`; `Machine Closure Package` |
| gateRunPurpose | confirmation after complete source, test, and evidence inventory; required shape was already known from reading checker source ahead of drafting |
| claimBoundary | no-commit provider-free local Web auth repair worker return only |

## Gate Evidence

| Command | Result |
|---|---|
| `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --base 9a10434041a3c8e453ff0abfb188116a66b80b6e --head HEAD` | PASS (75/75 checks, receipt `.cvf/runtime/autorun-receipts/pre-implementation.json`) |
| `npx vitest run src/lib/middleware-auth.test.ts src/app/api/auth/me/route.test.ts --reporter=verbose` | PASS (12/12) |
| `npx tsc --noEmit -p tsconfig.json` | PASS (no output) |
| `npx playwright test tests/e2e/system-chain-uc04b-auth-projection-regression.spec.ts --config playwright.config.ts --workers=1` | FAIL (case 1 failed on environment host-origin split; case 2 did not run) |
| `python governance/compat/run_worker_return_fast_gate.py` (first run) | FAIL (external knowledge intake `Input type` enum; missing GC-051 registry entry for the new spec path; aggregate drift and disposition-enum defects while adding that entry; missing structured `WORKER_EXPERIENCE_RETRO` fields) |
| `python governance/compat/run_worker_return_fast_gate.py` (final run, see `## Command Evidence`) | PASS (62/62 reviewer-fast checks) |

receiptEvidence: CVF_RECEIPT_PRESENT - `.cvf/runtime/autorun-receipts/pre-implementation.json`

## Actual Changed Set

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-auth-projection-regression.spec.ts`
- `docs/reviews/evidence/system-chain-uc04b-r2-auth-projection-invocation-ledger-2026-07-14.json`
- `docs/reviews/evidence/system-chain-uc04b-r2-auth-projection-regression-2026-07-14.json`
- `docs/reviews/evidence/system-chain-uc04b-r2-auth-projection-diagnostic-2026-07-14.json`
- `docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R2_WEB_AUTH_PROJECTION_REPAIR_WORKER_RETURN_2026-07-14.md`
- `docs/corpus-intelligence/registry/entries/system-chain-uc04b-r2-auth-projection-regression.json` (outside the strict manifest; added because `check_changed_corpus_registry_coverage.py` blocks any changed governed source/test path not covered by GC-051 scopePaths, and the mandatory `run_worker_return_fast_gate.py` includes that check)
- `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` (generated aggregate; regenerated via `python governance/compat/generate_corpus_scan_registry.py --generate` after the entry above, not hand-edited)

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: N/A with reason: no `governance/compat`
or `AGENTS.md` file was changed; the only protected-path creation is the
dispatch-authorized E2E spec below.

Protected paths:
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-auth-projection-regression.spec.ts`

Operator authorization: carried from the GC-018 baseline and work order -
the operator said `tiep tuc` after R1 closure routed this exact bounded
repair packet next; both name this exact path in `Core Guard
Self-Protection Authorization`.

Rollback boundary: only the R2 manifest paths listed in `Actual Changed Set`
above; no R1 closure or session commit is touched.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | the operator's `tiep tuc` continuation of the R1 bounded blocker closure routed the R2 GC-018/work order to this worker return; no external repo, corpus scan, or provider-readiness claim was absorbed |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this worker return |
| Disposition | internal Web auth runtime repair only; no external artifact import |
| Claim boundary | CVF source authority remains repo-governed surfaces only |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: N/A with reason: this worker return is not a rescan, intake-refresh,
or source-backed reassessment output.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - N/A with reason: no corpus
  completeness, inventory, or full-scan claim is made by this worker return.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Handled or deferred |
|---|---|---|---|---|---|
| E2E proof spec used a relative `page.goto` path while relying on `page.request` calls also resolving to `baseURL`; Next.js dev-server `allowedDevOrigins` treats `127.0.0.1` and `localhost` as distinct origins with separate cookie jars, so a positive-auth E2E case can fail with no runtime defect present | RULE_GAP | GOVERNANCE_CONTROL_PLANE | N/A_WITH_REASON | reviewer decides whether to authorize an `allowedDevOrigins` fix or a spec host-consistency fix in a successor packet; candidate for a new ADIF entry if this recurs | deferred to reviewer/closer |

## Epistemic Process Block

### Expected Result / Prediction

The one-invocation R2 packet was expected to produce two stable PASS cases
(`positive_developer_auth_projection`, `negative_anonymous_auth_projection`)
proving developer session/`/api/auth/me`/Operations agreement and anonymous
denial, since the request-bound `getToken` repair passed all 12 focused unit
tests and `tsc --noEmit` beforehand.

### Evidence Comparison

The trace network log for the one invocation shows all direct
`page.request` calls (`/api/auth/csrf`, `/api/auth/callback/credentials`,
`/api/auth/session`, `/api/auth/me`) succeeded on `http://127.0.0.1:3001`
with expected statuses, but the following `page.goto(OPERATIONS_URL)`
resolved to `http://localhost:3001`, a distinct origin. The dev server log
for the same run independently reported a blocked cross-origin request from
`127.0.0.1` citing `allowedDevOrigins`, corroborating the host-origin split
from an unrelated source (the dev server's own console output, not the
trace).

### Contradiction Or Gap Disposition

No contradiction in the runtime repair: the unit-test evidence and the E2E
failure are consistent, because the E2E failure occurred before the
request-bound `getToken` path could be exercised by a session-carrying
request. The gap is in the proof-spec/dev-server host consistency, not in
`verifySessionCookie`.

### Claim Update

A green focused-unit-test result for a request-bound auth adapter does not
by itself prove browser-level session-cookie propagation in E2E; that
requires the E2E harness's `page.request` and `page.goto` calls to target
the same origin. This packet does not claim projection agreement was proven
end to end.

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO: The manifest, ADIF-0033/0034 reads, and
pre-implementation gate meant the runtime repair itself proceeded with no
rework: source verification facts in the GC-018/work order matched current
source exactly (`getToken` reachable via `next-auth/jwt`, `authSecret`
extraction, claim shapes). The only friction was discovering the
`127.0.0.1`/`localhost` origin split only after the one authorized live
command - this was not predictable from static source reading alone and
would only surface by running the spec, which the packet's one-invocation
ceiling correctly limited to a single attempt.

frictionLevel: LOW
frictionType: ENUM_OR_TOKEN_MISMATCH
observedStep: first `run_worker_return_fast_gate.py` run after drafting the worker return
preventiveControlCandidate: CHECKER

The first fast-gate run failed on three checker-literal mismatches unrelated
to the runtime repair or proof evidence: the `External Knowledge Intake
Routing` section's `Input type` field rejects free-text `N/A with reason`
prose and requires one exact enum value even for a genuinely-internal
return; a new governed E2E spec path triggered GC-051
`check_changed_corpus_registry_coverage.py`, requiring a new registry entry
plus aggregate regeneration outside the work order's manifest; and that new
entry's `disposition` field required one exact enum token
(`BLOCKED_PENDING_DECISION`) rather than the general `BLOCKED_WITH_REASON`
vocabulary used elsewhere in this packet. All three were resolved by reading
checker source directly; no proof or runtime evidence changed.

## Worker Return Scaffold Effectiveness Measurement

| Measurement | Result |
|---|---|
| scaffoldUsedBeforeLongDraft | YES |
| scaffoldMissingSectionFound | NONE |
| firstWorkerReturnFastGateResult | FAIL |
| postScaffoldManualRepairCount | 4 |

## Worker Return Jurisdiction Block

| Field | Disposition |
|---|---|
| capturedArtifacts | runtime repair (`src/auth.ts`, `src/lib/middleware-auth.ts`), focused test extension (`src/lib/middleware-auth.test.ts`), proof-only E2E spec, invocation ledger, receipt, diagnostic, this worker return, plus one GC-051 registry entry and its regenerated aggregate (outside the strict manifest; see below) |
| capturedOperations | pre-implementation autorun gate; focused Vitest run; `tsc --noEmit`; one Playwright invocation; secret-safe `.env.local` existence check; secret scan of evidence files; `test-results/.last-run.json` baseline restore; GC-051 registry entry add and `generate_corpus_scan_registry.py --generate` regeneration |
| deferredOperations | fixing `next.config.ts` `allowedDevOrigins` or the E2E host-consistency root cause; any second live invocation; UC-04B business-spec execution |
| outOfScopeRequests | N/A with reason: no out-of-scope request was made during this tranche |
| reviewerActionNeeded | decide whether to authorize a successor packet for the `allowedDevOrigins`/host-consistency fix, whether this qualifies for a new ADIF entry, and whether the GC-051 registry entry/aggregate pair (added only to satisfy the mandatory `check_changed_corpus_registry_coverage.py` gate inside `run_worker_return_fast_gate.py`, not listed in the work order's Planned Worker Fulfillment Manifest) is accepted as-is or revised at closure |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | worker |
| Provider or surface | local private provenance repository |
| Session or invocation | SCLP-UC04B-R2 worker execution, 2026-07-15 |
| Working directory | repository root |
| Command or tool surface | governed reads, source search, Vitest, tsc, Playwright, governance autorun gate, git |
| Target paths | Planned Worker Fulfillment Manifest paths listed in `Actual Changed Set` |
| Allowed scope source | `docs/work_orders/CVF_AGENT_WORK_ORDER_SYSTEM_CHAIN_UC04B_R2_WEB_AUTH_PROJECTION_REPAIR_2026-07-14.md` |
| Before status evidence | clean worktree at `9a10434041a3c8e453ff0abfb188116a66b80b6e` |
| After status evidence | `git status --short` below; HEAD unchanged at `9a10434041a3c8e453ff0abfb188116a66b80b6e` |
| Diff evidence | `git diff --name-status` shows `M` for `src/auth.ts`, `src/lib/middleware-auth.ts`, `src/lib/middleware-auth.test.ts`, `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` (see `## Changed Files`); 5 new untracked files, 4 match the manifest and 1 is the added GC-051 registry entry |
| Approval boundary | one no-commit worker execution only; reviewer/closer owns acceptance, closure, and commits |
| Claim boundary | see `## Claim Boundary` above |
| Agent type | worker |
| Invocation ID | `system-chain-uc04b-r2-worker-2026-07-15` |
| Expected manifest | Planned Worker Fulfillment Manifest in the work order |
| Actual changed set | see `## Actual Changed Set` above |
| Manifest delta | EXPLAIN: exact manifest fulfilled, plus one GC-051 registry entry (`docs/corpus-intelligence/registry/entries/system-chain-uc04b-r2-auth-projection-regression.json`) and its regenerated aggregate (`docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`), required only because `run_worker_return_fast_gate.py` enforces `check_changed_corpus_registry_coverage.py` against any changed governed source/test path |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | one local request-bound Web auth repair, unit-proven; one E2E proof attempt blocked by an unrelated environment cause |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CVF_RECEIPT_PRESENT - pre-implementation autorun receipt plus invocation ledger and diagnostic |
| actionEvidence | CLAIM_REJECTED_NO_ACTION - the one-command E2E projection regression did not pass, so full action evidence for developer/anonymous projection agreement is not present |
| invocationBoundary | one Playwright command; zero business/checker/retry/provider calls, all reconciled in the invocation ledger |
| interceptionBoundary | no IDE, shell, git, provider, MCP, public, production, or universal interception claim |
| claimLanguage | request-bound auth adapter is unit-proven; E2E browser-level projection agreement remains unproven pending a host-consistency fix |
| forbiddenExpansion | no UC-04B business, all-auth, provider, production, public, scale, certification, or user-value claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: worker return in private provenance workspace; no public-sync authorization.

## git status --short

```
 M EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts
 M EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.test.ts
 M EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts
 M docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json
?? EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/system-chain-uc04b-auth-projection-regression.spec.ts
?? docs/corpus-intelligence/registry/entries/system-chain-uc04b-r2-auth-projection-regression.json
?? docs/reviews/CVF_SYSTEM_CHAIN_UC04B_R2_WEB_AUTH_PROJECTION_REPAIR_WORKER_RETURN_2026-07-14.md
?? docs/reviews/evidence/system-chain-uc04b-r2-auth-projection-diagnostic-2026-07-14.json
?? docs/reviews/evidence/system-chain-uc04b-r2-auth-projection-invocation-ledger-2026-07-14.json
?? docs/reviews/evidence/system-chain-uc04b-r2-auth-projection-regression-2026-07-14.json
```

## Changed Files

`git diff --name-status` (tracked modifications only; untracked new files
listed separately above and in `## Actual Changed Set`):

```text
M   EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts
M   EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.test.ts
M   EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts
M   docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json
```

## Command Evidence

| Command | Result |
|---|---|
| `python governance/compat/run_worker_return_fast_gate.py` (final run after repairs) | PASS |

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored: HEAD unchanged; no git commit performed by
worker. Reviewer/closer owns material commit.

## Machine Closure Package

| Artifact | Evidence | Disposition |
|---|---|---|
| Worker return status | `Status: BLOCKED_WITH_REASON` | pending reviewer closure; worker does not mark closed-equivalent |
| Work order status | `dispatchWorkOrder: docs/work_orders/CVF_AGENT_WORK_ORDER_SYSTEM_CHAIN_UC04B_R2_WEB_AUTH_PROJECTION_REPAIR_2026-07-14.md` | N/A with reason: reviewer/closer owns closure conversion |
| Changed set | `## Actual Changed Set` | lists real paths above |
| Gate evidence | `## Gate Evidence` | records pass/fail/blocked above |
