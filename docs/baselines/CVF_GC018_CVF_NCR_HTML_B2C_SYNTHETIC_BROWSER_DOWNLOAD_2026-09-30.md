# CVF GC-018 Baseline - NCR HTML B2c Synthetic Browser Download

Memory class: governed-dispatch-baseline

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-HTML-B2C-SYNTHETIC-BROWSER-DOWNLOAD

Dispatch base head: `7be703a4d`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local technical reviewer; operator owns real-data and effect checkpoints.

Worker target: shared-workspace `INTERNAL_AGENT`.

## Purpose

Authorize a test-only, real-browser synthetic proof that the existing Artifacts panel downloads the exact UTF-8 bytes of the displayed HTML version to a disposable file. This packet does not wire B2b into production, change the panel, call the export route or provider, or accept an artifact.

## Source / Predecessor Evidence

The operator delegated Local work-order decisions after source audit. B2b is Local-accepted bounded at `8f2db40fa`; D043 and the B2c scope audit at `6224b74d4` identify the missing saved-file-byte proof. Profile A and Q001/Q004 remain open. The existing mock Playwright Artifacts spec intercepts the export endpoint and checks preview text but not a download event or file bytes.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| D043 permits authoring a synthetic browser-download proof packet | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D042-D043, Q001/Q004 | B2c | NCR roadmap | ACCEPT |
| Local audit separates current browser tests from saved-file proof | `docs/reviews/CVF_CVF_NCR_HTML_B2C_BROWSER_FILE_PROOF_SCOPE_AUDIT_2026-09-30.md` | Findings and Decision | browser-file boundary | Local audit | ACCEPT |
| Panel constructs Blob from displayed HTML and immediately revokes object URL | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `downloadHtml`, `handleDownload` | `Blob`, `anchor.click`, `revokeObjectURL` | Web panel, read-only target | ACCEPT |
| Existing browser spec intercepts export with a synthetic JSON fixture | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-panel.spec.ts` | first Artifacts case | `page.route`, preview | Playwright test precedent | ACCEPT |
| Mock Playwright config launches Web with mock-AI flag | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.mock.ts` | `webServer` | `NEXT_PUBLIC_CVF_MOCK_AI` | test harness | ACCEPT |
| B2b owns a Node-side exact UTF-8 byte identity, unconnected to panel | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-byte-handoff.ts` | `createHtmlByteHandoff`, `verifyHtmlByteHandoff` | B2b identity | isolated helper | ACCEPT |

## Decision / Baseline / Proposed Tranche

B2c's target is an observed browser download and saved-file readback for intercepted synthetic HTML. The worker creates a focused Playwright spec that uses the real Artifacts panel and a synthetic intercepted export response, waits for the download event, saves to a disposable test location, reads the bytes, and compares exact length and SHA-256 to an independent fixture oracle and the B2b identity in the Node-side test process. The test must discriminate a same-byte-length version change and include BOM, CRLF/LF and non-ASCII content so text-only readback cannot masquerade as byte proof. It must prove the downloaded file corresponds to the displayed result when the form has changed, respecting B1 version binding.

The proof receipt records browser/profile, fixture identity, downloaded filename, observed file-byte length/digest, equality verdict, cleanup and any failed attempt. The raw HTML fixture and downloaded file are not committed. An exact missing-download or digest mismatch is a `BLOCKED_WITH_REASON` return. The worker may not repair `ArtifactExportPanel.tsx` in this initial packet; Local will decide a separate R1 repair if the browser test exposes a defect. Immediate object-URL revocation is a hypothesis to test, not an assumed failure.

## Scope / Target / Owner Boundary

Exactly four create paths are allowed: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-byte-download.spec.ts`; `docs/reference/CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_PROOF_2026-09-30.md`; `docs/reviews/evidence/cvf-ncr-html-b2c-browser-download-worker-proof-2026-09-30.json`; and `docs/reviews/CVF_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_WORKER_RETURN_2026-09-30.md`. The existing panel, route, B2b helper, package/config, auth, roadmap, and continuity are read-only. Local owns review, commit and continuity.

## Acceptance Criteria

1. A real browser drives the existing panel with an intercepted synthetic export response; the test does not call a provider or assert AI governance behavior from mock mode.
2. The browser emits a download; bytes read from a disposable saved file match an independently computed fixture SHA-256 and length, and the Node-side B2b identity for the exact fixture string.
3. A same-length different rendered title yields a different digest; the downloaded version matches the displayed result even when the form changes. BOM, newline and non-ASCII cases are tested as byte values, not text-only readback.
4. The worker records browser version/profile, exact commands/results, file cleanup and a machine-readable proof receipt. Missing browser, blocked download, byte mismatch or cleanup failure is reported as `BLOCKED_WITH_REASON`, not silently skipped.
5. Only four create paths change. Required focused Playwright, TypeScript, lint where applicable, worker-return fast gate and exact-manifest checks pass before `COMPLETE_PENDING_REVIEW`.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | Playwright test and proof receipt for existing panel | synthetic browser saved-byte evidence only | D043, audit and pending browser test | test harness only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no B2c external interface | no ingress, auth, receipt, raw data or mutation grant | bounded packet scope | external adapter deferred | DEFERRED_WITH_REASON |

## Evidence / Verification

Capture executionBaseHead, initial/final status, exact changed set, focused Playwright command, TypeScript/lint results, file-byte hashes, browser version, cleanup result and worker-return fast gate. Local independently chooses a distinct synthetic fixture or recomputes actual saved-file bytes from a reviewer-owned run before acceptance. Passing mock browser behavior is UI/file proof for this fixture only, not production governance or durable acceptance.

## Operator Checkpoints

Profile A remains. Operator retains designation of actual accepting actor/account, source/instance and classification of real data, store location, writer/fencing model, backup/key custody, retention/deletion, RPO/RTO, cost and pilot/live effect. A separate work order is required for route/store wiring or active acceptance.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B2C-SYNTHETIC-BROWSER-DOWNLOAD --title "NCR HTML B2c Synthetic Browser Download" --date 2026-09-30 --base 7be703a4d --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | generic-worker-dispatch and no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | source-backed B2c real-browser synthetic download scope |
| checkerReadAheadConfirmation | dispatch, acceptance-ledger, closeability, structural, release and high-risk local transaction checker sources |
| docOnlyNewFields | N/A with reason: no new governed field schema |
| claimBoundary | Scaffold is authoring aid only |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_high_risk_local_transaction_proof.py` |
| literalTokensReviewed | DISPATCH_READY; source ACCEPT rows; worker-return gate; exact four-path scope; no durable transaction authority |
| gateRunPurpose | Confirm packet structure and authority after source review |
| claimBoundary | Static gate PASS cannot prove browser behavior |

## Claim Boundary

This baseline authorizes a synthetic real-browser download test and evidence receipt only. It does not accept HTML, persist an artifact in an authoritative store, grant writer rights, close Q001/Q004, or authorize real data, provider/live governance proof, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
