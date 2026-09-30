# CVF GC-018 Baseline - NCR HTML B2f Synthetic Timeout

Memory class: governed-dispatch-baseline

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-HTML-B2F-SYNTHETIC-TIMEOUT

Dispatch base head: `b882d5d59`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local technical reviewer; operator owns real-data and effect checkpoints.

Worker target: shared-workspace `INTERNAL_AGENT`.

## Purpose

Authorize a test-only browser proof that one configured export receipt request reaches a delayed, non-forwarding loopback stub, times out at the client, and leaves the real Artifacts panel draft with the same attempt ID and an ambiguous-outcome warning. No production edit, real evaluate route, Governance Engine, provider, retry or artifact acceptance is authorized.

## Source / Predecessor Evidence

B2e is Local-accepted bounded at `ec283760d` for `INVALID_RESPONSE`/`UNAVAILABLE`. D050 and the B2f read-only audit at `7db74ca69` identify the controlled real-browser `TIMED_OUT` gap. Unit/jsdom tests cover timeout by fabrication; Q001 cold-development observation did not bind a controlled timeout status and attempt ID. A fabricated `PRESENT` fixture is excluded because it could overstate governance evidence. Q001/Q004 Profile A remain open.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| D050 permits timeout-only packet authoring after source audit | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D050/Q001/Q004 | B2f | NCR roadmap | ACCEPT |
| Audit separates the timeout gap from fake `PRESENT` overclaim | `docs/reviews/CVF_CVF_NCR_HTML_B2F_RECEIPT_BRANCH_GAP_AUDIT_2026-10-01.md` | Findings and Decision | `TIMED_OUT` | Local audit | ACCEPT |
| Helper bounds timeout, aborts fetch, and returns status plus request ID with no receipt | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` | `proofTimeoutMs`, `fetchGovernanceReceipt` | `controller.abort`, `TIMED_OUT` | receipt helper, read-only | ACCEPT |
| Panel warns remote processing may have happened and displays attempt ID | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | output receipt block | `receiptTimedOutNote`, `governance-receipt-attempt-id` | panel, read-only | ACCEPT |
| Direct route test aborts a stubbed fetch after 1,000 ms | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.test.ts` | timeout case | `CVF_GOVERNANCE_RECEIPT_TIMEOUT_MS` | unit precedent | ACCEPT |

## Decision / Baseline / Proposed Tranche

The worker may create a focused Playwright spec and test-only CommonJS harness, using the reviewed B2e design as read-only precedent. The harness binds an inert delayed HTTP stub to ephemeral IPv4 loopback before starting fresh Next, forces `NEXTAUTH_URL` to the stub origin, `AUTH_URL` to the Next origin, `GOVERNANCE_ENGINE_ENABLED=false`, a dead engine URL and a synthetic service token. It sets `CVF_GOVERNANCE_RECEIPT_TIMEOUT_MS=1000` in the child and verifies these values from inside the server before export. The stub accepts only one expected `/api/governance/evaluate` POST, records secret-safe method/path and request/artifact IDs, waits long enough to cross the client timeout, and never forwards. Unexpected requests fail closed. No raw HTML, credential, request body or token value is logged.

The browser calls the actual `/api/artifacts/export` route without intercepting it. It checks HTTP 200, `TIMED_OUT`, absent receipt, matching attempt/stub request ID, `DRAFT_UNACCEPTED`, and the panel warning that the service may still have processed the request. Stub receive time precedes route timeout observation; late response, disconnect and cleanup are recorded without assuming remote rollback or safe retry. The harness must fail closed before export if origin, auth, isolation, timeout inheritance or synthetic-token preflight is uncertain. No fabricated `PRESENT` or real evaluate/engine/provider path is allowed.

## Scope / Target / Owner Boundary

Exactly five create paths are allowed: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-loopback-timeout.spec.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/support/b2f-loopback-timeout-harness.cjs`; `docs/reference/CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_PROOF_2026-10-01.md`; `docs/reviews/evidence/cvf-ncr-html-b2f-timeout-worker-proof-2026-10-01.json`; and `docs/reviews/CVF_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_WORKER_RETURN_2026-10-01.md`. Existing production, config, package, ledger/store, roadmap and continuity paths are worker-read-only. Local owns review, commit and continuity.

## Acceptance Criteria

1. Before export, the inert stub listens on verified loopback-only ephemeral port; fresh Next inherits its exact origin and disabled-engine flag. Uncertain preflight blocks execution.
2. Real browser uses the un-intercepted export route and synthetic fields. The stub observes the expected POST, IDs and excerpt length, never forwards, and detects any unexpected request. No actual evaluate route, engine or provider call occurs.
3. One delayed synthetic request yields `TIMED_OUT`, matching attempt/stub request ID, no receipt, `DRAFT_UNACCEPTED` and the panel's explicit ambiguous-outcome text. Abort does not imply remote cancellation or retry safety.
4. Browser/profile, preflight, timeout configuration, request/abort/late-response observations, cleanup and exact commands/results are recorded without raw HTML or credentials.
5. Only five create paths change. Focused Playwright, TypeScript/lint where applicable, worker-return fast and exact-manifest checks pass before `COMPLETE_PENDING_REVIEW`; isolation/auth failure returns `BLOCKED_WITH_REASON`.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | delayed inert loopback harness, browser spec and proof receipt | synthetic timeout transport/presentation only | D050, audit and pending test | test harness only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no B2f external interface | no ingress, auth, receipt, raw data or mutation grant | bounded packet scope | external adapter deferred | DEFERRED_WITH_REASON |

## Evidence / Verification

Capture executionBaseHead, initial/final status, exact changed set, preflight, secret-safe request/timing metadata, route/UI status and warning, browser version, cleanup, focused test and TypeScript/lint results, and worker-return fast gate. Local inspects the delayed stub's non-forwarding design and runs one focused probe if the worker returns complete. Synthetic timeout evidence cannot prove remote rollback, retry safety, real governance or durable acceptance.

## Operator Checkpoints

Profile A remains. Operator retains real actor/account, source/instance and data classification, store/writer, backup/key custody, retention/deletion, RPO/RTO, cost and pilot/live effect. Actual Governance Engine or provider execution requires a separately authorized proof and live-governance gate.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B2F-SYNTHETIC-TIMEOUT --title "NCR HTML B2f Synthetic Timeout" --date 2026-10-01 --base b882d5d59 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | generic-worker-dispatch and no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | source-backed B2f delayed-loopback timeout and ambiguous-outcome boundary |
| checkerReadAheadConfirmation | dispatch, acceptance-ledger, closeability, structural, release and high-risk local transaction checker sources |
| docOnlyNewFields | N/A with reason: no new governed field schema |
| claimBoundary | Scaffold is authoring aid only |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_high_risk_local_transaction_proof.py` |
| literalTokensReviewed | DISPATCH_READY; source ACCEPT rows; worker-return gate; exact five-path scope; no durable transaction authority |
| gateRunPurpose | Confirm packet structure and authority after source review; not first discovery |
| claimBoundary | Static gate PASS cannot prove stub isolation or browser behavior |

## Claim Boundary

This baseline authorizes one synthetic configured-hop timeout/presentation test against a delayed non-forwarding loopback stub only. It does not authorize a fabricated `PRESENT` claim, remote-cancellation or retry-safety assertion, the actual evaluate route, Governance Engine, provider, real data, authoritative store, HTML acceptance, Q001/Q004 exit, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
