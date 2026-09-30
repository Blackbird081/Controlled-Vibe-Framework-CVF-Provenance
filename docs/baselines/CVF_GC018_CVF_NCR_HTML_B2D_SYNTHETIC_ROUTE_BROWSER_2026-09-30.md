# CVF GC-018 Baseline - NCR HTML B2d Synthetic Route Browser

Memory class: governed-dispatch-baseline

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-HTML-B2D-SYNTHETIC-ROUTE-BROWSER

Dispatch base head: `205a76790`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local technical reviewer; operator owns real-data and effect checkpoints.

Worker target: shared-workspace `INTERNAL_AGENT`.

## Purpose

Authorize a test-only, real-browser proof of the existing export route's synthetic HTML reaching the Artifacts panel and a disposable downloaded file byte-exact. The route is called without browser interception. A test-only Node preload blocks any server-side governance-evaluate fetch before it can leave the process; the route must report `NOT_CONFIGURED`. This packet does not wire B2b into production, change the route or panel, call a provider, or accept an artifact.

## Source / Predecessor Evidence

The operator delegated Local work-order decisions after source audit. B2c is Local-accepted bounded at `f8f1cc7e8`; D046 and the B2d scope audit at `e1cb0bdb4` identify the remaining route-to-browser gap and optional server-side receipt hop. Profile A and Q001/Q004 remain open. B2c proved saved-file bytes only for an intercepted export response.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| D046 permits a synthetic route/browser packet after source audit | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D045-D046, Q001/Q004 | B2d | NCR roadmap | ACCEPT |
| Local audit identifies the route receipt hop and no-hop requirement | `docs/reviews/CVF_CVF_NCR_HTML_B2D_ROUTE_BROWSER_SCOPE_AUDIT_2026-09-30.md` | Findings and Decision | route/browser boundary | Local audit | ACCEPT |
| Receipt helper returns `NOT_CONFIGURED` before fetch when `NEXTAUTH_URL` is empty | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` | `resolveEvaluateUrl`, `fetchGovernanceReceipt` | `NEXTAUTH_URL`, `fetch` | receipt helper, read-only | ACCEPT |
| Route returns rendered HTML in JSON and hashes source content separately | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | `POST` | `data.html`, `sourceHash` | export route, read-only | ACCEPT |
| Panel constructs Blob from displayed HTML and immediately revokes object URL | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `downloadHtml`, `handleDownload` | `Blob`, `anchor.click`, `revokeObjectURL` | Web panel, read-only target | ACCEPT |
| Existing browser spec intercepts export with a synthetic JSON fixture | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-panel.spec.ts` | first Artifacts case | `page.route`, preview | Playwright test precedent | ACCEPT |
| Mock Playwright config launches Web with mock-AI flag | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.mock.ts` | `webServer` | `NEXT_PUBLIC_CVF_MOCK_AI` | test harness | ACCEPT |
| B2b owns a Node-side exact UTF-8 byte identity, unconnected to panel | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-byte-handoff.ts` | `createHtmlByteHandoff`, `verifyHtmlByteHandoff` | B2b identity | isolated helper | ACCEPT |

## Decision / Baseline / Proposed Tranche

B2d's target is an un-intercepted local export route response consumed by a real browser, followed by a saved-file byte readback. A test-only `.cjs` preload wraps Node `fetch` at process startup and blocks/logs any attempted `/api/governance/evaluate` request before network dispatch. The invocation sets `NEXTAUTH_URL` to the empty string before Playwright starts its server; the worker verifies environment inheritance and the preload startup marker before invoking the export route. If either preflight fails, no route call is allowed. The browser test passively captures the actual route JSON, requires `governanceReceiptStatus: NOT_CONFIGURED`, and checks that the preload recorded zero attempted evaluate calls. The saved file must match an independent `Buffer.from(data.html, 'utf8')` length/SHA-256 oracle and the B2b Node-side identity. `sourceHash` is over source content, not these HTML bytes or JSON wire bytes. A same-length title change must produce a different saved digest, and a form change without rebuild must preserve the displayed/downloaded version.

The proof receipt records server/preload preflight, zero-hop observation, route status, browser/profile, synthetic input identity, downloaded filename, observed file-byte length/digest, equality verdict, cleanup and any failed attempt. Raw HTML and downloaded files are not committed. A preflight failure, non-`NOT_CONFIGURED` status, attempted evaluate call, missing download or digest mismatch is `BLOCKED_WITH_REASON`. The worker may not repair production code in this packet.

## Scope / Target / Owner Boundary

Exactly five create paths are allowed: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-route-byte-download.spec.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/support/b2d-no-hop-preload.cjs`; `docs/reference/CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_PROOF_2026-09-30.md`; `docs/reviews/evidence/cvf-ncr-html-b2d-route-browser-worker-proof-2026-09-30.json`; and `docs/reviews/CVF_CVF_NCR_HTML_B2D_SYNTHETIC_ROUTE_BROWSER_WORKER_RETURN_2026-09-30.md`. The existing panel, route, B2b helper, package/config, auth, roadmap, and continuity are read-only. Local owns review, commit and continuity.

## Acceptance Criteria

1. Before the first route call, a fresh local server inherits empty `NEXTAUTH_URL` and the test-only Node preload. The preload fails closed on any attempted evaluate fetch, logs startup and attempts outside the repository, and cannot be bypassed by a browser-level route intercept.
2. A real browser drives the existing panel with synthetic inputs and the un-intercepted export route. Passive response capture observes `NOT_CONFIGURED`; the preload records zero attempted evaluate calls. No provider or AI governance behavior is claimed.
3. The browser emits a download; saved bytes match an independent UTF-8 oracle from the route's decoded `data.html`, plus B2b identity. A same-length title change yields a different digest; a form edit without rebuild preserves the displayed/downloaded version.
4. The worker records browser version/profile, route status, preload evidence, exact commands/results, file cleanup and machine-readable proof. Any isolation or byte failure returns `BLOCKED_WITH_REASON`.
5. Only five create paths change. Focused Playwright, TypeScript, lint where applicable, worker-return fast gate and exact-manifest checks pass before `COMPLETE_PENDING_REVIEW`.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | no-hop preload, Playwright test and proof receipt | synthetic route/browser saved-byte evidence only | D046, audit and pending browser test | test harness only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no B2d external interface | no ingress, auth, receipt, raw data or mutation grant | bounded packet scope | external adapter deferred | DEFERRED_WITH_REASON |

## Evidence / Verification

Capture executionBaseHead, initial/final status, exact changed set, no-hop preflight/attempt log, actual route status, focused Playwright command, TypeScript/lint results, file-byte hashes, browser version, cleanup result and worker-return fast gate. Local independently recomputes actual saved-file bytes from a reviewer-owned run before acceptance. Passing synthetic route/browser behavior is local transport/file proof only, not production governance or durable acceptance.

## Operator Checkpoints

Profile A remains. Operator retains designation of actual accepting actor/account, source/instance and classification of real data, store location, writer/fencing model, backup/key custody, retention/deletion, RPO/RTO, cost and pilot/live effect. A separate work order is required for route/store wiring or active acceptance.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B2D-SYNTHETIC-ROUTE-BROWSER --title "NCR HTML B2d Synthetic Route Browser" --date 2026-09-30 --base 205a76790 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | generic-worker-dispatch and no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | source-backed B2d real-browser synthetic download scope |
| checkerReadAheadConfirmation | dispatch, acceptance-ledger, closeability, structural, release and high-risk local transaction checker sources |
| docOnlyNewFields | N/A with reason: no new governed field schema |
| claimBoundary | Scaffold is authoring aid only |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_high_risk_local_transaction_proof.py` |
| literalTokensReviewed | DISPATCH_READY; source ACCEPT rows; worker-return gate; exact five-path scope; no durable transaction authority |
| gateRunPurpose | Confirm packet structure and authority after source review |
| claimBoundary | Static gate PASS cannot prove browser behavior |

## Claim Boundary

This baseline authorizes a no-hop synthetic route/browser download test and evidence receipt only. It does not accept HTML, persist an artifact in an authoritative store, grant writer rights, close Q001/Q004, or authorize real data, provider/live governance proof, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
