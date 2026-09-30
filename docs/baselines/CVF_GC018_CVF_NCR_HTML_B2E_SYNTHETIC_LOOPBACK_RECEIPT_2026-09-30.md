# CVF GC-018 Baseline - NCR HTML B2e Synthetic Loopback Receipt

Memory class: governed-dispatch-baseline

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-HTML-B2E-SYNTHETIC-LOOPBACK

Dispatch base head: `a19e59f01`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local technical reviewer; operator owns real-data and effect checkpoints.

Worker target: shared-workspace `INTERNAL_AGENT`.

## Purpose

Authorize a test-only browser proof that a configured export receipt request reaches an isolated, non-forwarding loopback stub and that the real Artifacts panel displays the synthetic failure status and attempt ID while keeping the artifact draft. No production edit, real evaluate route, Governance Engine, provider or artifact acceptance is authorized.

## Source / Predecessor Evidence

B2d is Local-accepted bounded at `7ad6994bc` for `NOT_CONFIGURED`. D048 and the B2e read-only audit at `5b8cfb588` identify the untested configured-hop boundary. The route helper builds an absolute evaluate URL from `NEXTAUTH_URL`; the actual Next evaluate route can forward to Governance Engine. Unit/jsdom tests use fabricated responses. Q001/Q004 Profile A remain open.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| D048 permits only a bounded synthetic loopback packet after source audit | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D047-D048/Q001/Q004 | B2e | NCR roadmap | ACCEPT |
| Audit identifies possible engine forwarding and an inert loopback containment candidate | `docs/reviews/CVF_CVF_NCR_HTML_B2E_CONFIGURED_RECEIPT_SCOPE_AUDIT_2026-09-30.md` | Findings and Decision | configured receipt boundary | Local audit | ACCEPT |
| Helper constructs URL and POSTs a source excerpt with IDs | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` | `resolveEvaluateUrl`, `fetchGovernanceReceipt` | `NEXTAUTH_URL`, `fetch` | receipt helper, read-only | ACCEPT |
| Actual Next evaluate route can call Governance Engine | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/evaluate/route.ts` | `POST` | `governanceEvaluate` | evaluate route, forbidden target | ACCEPT |
| Direct route tests use stubbed fetch for invalid/timeout cases | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.test.ts` | receipt cases | `fetchMock` | unit-test precedent | ACCEPT |

## Decision / Baseline / Proposed Tranche

The worker may create a focused Playwright spec and a test-only CommonJS harness that starts an inert HTTP stub on an ephemeral loopback port before starting the fresh Next test server. The harness sets `NEXTAUTH_URL` to that exact stub origin and `GOVERNANCE_ENGINE_ENABLED=false` as defense in depth. It must prove the stub is bound to loopback, never forwards, and receives only the expected `/api/governance/evaluate` POST. Unexpected requests fail closed. It records only secret-safe method/path, request/artifact IDs, excerpt length and whether a service-token header was present. No raw HTML, credential or request body is logged.

The browser calls the actual `/api/artifacts/export` route without intercepting it. The configured server-side receipt fetch terminates at the stub, which returns fabricated `INVALID_RESPONSE` and `UNAVAILABLE` outcomes. The test checks attempt IDs, draft UI text and zero actual Next evaluate/engine calls. If `NEXTAUTH_URL` interferes with browser login/auth origin or stub isolation cannot be proved, the worker returns `BLOCKED_WITH_REASON` before any export request. Production auth/config may not be edited. Browser `page.route` does not contain the server-side hop.

## Scope / Target / Owner Boundary

Exactly five create paths are allowed: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-loopback-receipt.spec.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/support/b2e-loopback-receipt-harness.cjs`; `docs/reference/CVF_NCR_HTML_B2E_SYNTHETIC_LOOPBACK_RECEIPT_PROOF_2026-09-30.md`; `docs/reviews/evidence/cvf-ncr-html-b2e-loopback-worker-proof-2026-09-30.json`; and `docs/reviews/CVF_CVF_NCR_HTML_B2E_SYNTHETIC_LOOPBACK_RECEIPT_WORKER_RETURN_2026-09-30.md`. Existing production, config, package, ledger/store, roadmap and continuity paths are worker-read-only. Local owns review, commit and continuity.

## Acceptance Criteria

1. Before export, the inert stub listens on verified loopback-only ephemeral port; fresh Next inherits its exact origin and disabled-engine flag. Uncertain preflight blocks execution.
2. Real browser uses the un-intercepted export route and synthetic fields. The stub observes the expected POST, IDs and excerpt length, never forwards, and detects any unexpected request. No actual evaluate route, engine or provider call occurs.
3. Fabricated invalid/unavailable outcomes yield `INVALID_RESPONSE`/`UNAVAILABLE`, attempt IDs, no receipt, `DRAFT_UNACCEPTED` and matching panel status text. No fabricated `ALLOW`/`PRESENT` is treated as governance proof.
4. Browser/profile, stub counts, destination, attempt IDs, status, cleanup and exact commands/results are recorded without raw HTML or credentials.
5. Only five create paths change. Focused Playwright, TypeScript/lint where applicable, worker-return fast and exact-manifest checks pass before `COMPLETE_PENDING_REVIEW`; isolation/auth failure returns `BLOCKED_WITH_REASON`.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | inert loopback harness, browser spec and proof receipt | synthetic transport/presentation only | D048, audit and pending test | test harness only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no B2e external interface | no ingress, auth, receipt, raw data or mutation grant | bounded packet scope | external adapter deferred | DEFERRED_WITH_REASON |

## Evidence / Verification

Capture executionBaseHead, initial/final status, exact changed set, preflight, destination/request metadata, route/UI statuses, browser version, cleanup, focused test and TypeScript/lint results, and worker-return fast gate. Local independently inspects the stub's non-forwarding design and runs one focused probe if the worker returns complete. Synthetic stub evidence cannot prove real governance or durable acceptance.

## Operator Checkpoints

Profile A remains. Operator retains real actor/account, source/instance and data classification, store/writer, backup/key custody, retention/deletion, RPO/RTO, cost and pilot/live effect. Actual Governance Engine or provider execution requires a separately authorized proof and live-governance gate.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B2E-SYNTHETIC-LOOPBACK --title "NCR HTML B2e Synthetic Loopback Receipt" --date 2026-09-30 --base a19e59f01 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | generic-worker-dispatch and no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | source-backed B2e inert-loopback synthetic receipt boundary |
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

This baseline authorizes a synthetic configured-hop transport/presentation test against a non-forwarding loopback stub only. It does not authorize the actual evaluate route, Governance Engine, provider, real data, authoritative store, HTML acceptance, Q001/Q004 exit, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
