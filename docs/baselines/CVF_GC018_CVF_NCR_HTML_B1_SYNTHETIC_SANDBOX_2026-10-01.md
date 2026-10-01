# CVF GC-018 Baseline - NCR HTML B1 Synthetic Sandbox

Memory class: governed-dispatch-baseline

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-HTML-B1-SANDBOX

Dispatch base head: `e09430475`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local technical reviewer; operator owns real-data and effect checkpoints.

Worker target: shared-workspace `INTERNAL_AGENT`.

## Purpose

Authorize one test-only Chromium proof of the existing Artifacts preview iframe sandbox using fully synthetic HTML. The worker creates evidence in four new paths and does not change production code, invoke a provider, or claim HTML safety beyond the tested iframe behavior.

## Source / Predecessor Evidence

Local audit at `docs/reviews/CVF_CVF_NCR_HTML_B1_SANDBOX_SCOPE_AUDIT_2026-10-01.md` (material audit `000017f22`) identified a specific browser oracle gap. Roadmap D053 permits packet authoring; B1 version binding and B2a-B2f remain bounded. The panel has `srcDoc={result.html}` and `sandbox=""`, while the named tests check the attribute or rendered content, not executable-control behavior. Q001/Q004 remain open.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| D053 permits a B1 browser-sandbox packet | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D053 | B1 sandbox | NCR roadmap | ACCEPT |
| Local audit isolates the browser-enforcement gap | `docs/reviews/CVF_CVF_NCR_HTML_B1_SANDBOX_SCOPE_AUDIT_2026-10-01.md` | Findings and Decision | sandbox control | Local audit | ACCEPT |
| Panel preview has srcDoc and empty sandbox | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | preview iframe | `srcDoc`, `sandbox` | Web panel | ACCEPT |
| Existing browser spec uses intercepted synthetic export and reads preview | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-panel.spec.ts` | HTML export case | `page.route`, preview | Playwright precedent | ACCEPT |
| Mock Playwright config starts a local Web server | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.mock.ts` | `webServer` | mock flag | test harness | ACCEPT |

## Decision / Baseline / Proposed Tranche

Use a harmless inline script that only attempts to set an in-memory parent-page sentinel. First demonstrate it runs in an unsandboxed same-origin `srcdoc` control frame on a disposable test page. Then intercept `/api/artifacts/export` with synthetic HTML in the real Artifacts panel and assert the actual preview iframe retains an empty sandbox token list, renders a benign heading, does not set the sentinel, and has an opaque origin in the tested Chromium profile. Keep the control separate from the app and make no outbound fixture request. Record observed values and browser/profile in secret-free proof JSON.

A failed assertion or unavailable browser is `BLOCKED_WITH_REASON`; the worker must not repair the panel under this packet. The result can prove only this fixture/profile's browser behavior. Print, screen-reader announcement, passive resource loading, downloaded HTML, other browsers, sanitization, provider governance and durable B2 acceptance remain untested.

## Scope / Target / Owner Boundary

Exactly four new worker paths: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts`; `docs/reference/CVF_NCR_HTML_B1_SYNTHETIC_SANDBOX_PROOF_2026-10-01.md`; `docs/reviews/evidence/cvf-ncr-html-b1-sandbox-worker-proof-2026-10-01.json`; `docs/reviews/CVF_CVF_NCR_HTML_B1_SYNTHETIC_SANDBOX_WORKER_RETURN_2026-10-01.md`. Existing panel, route, auth, mock config, package files, roadmap and continuity are read-only for the worker. Local owns independent probe, review and commit.

## Acceptance Criteria

1. A real Chromium run shows the harmless sentinel executes in an unsandboxed same-origin `srcdoc` control frame and does not execute in the actual panel iframe with `sandbox=""`.
2. The panel still renders a benign synthetic heading and its iframe has an opaque origin. The export response is intercepted; no fixture network call, provider or real export handler is used.
3. The spec checks both control and panel in one focused run, reports browser/profile and observed control/panel values, and fails closed if the control cannot demonstrate executability.
4. Four exact new paths contain test, secret-free proof JSON, bounded reference and pending return. Focused Playwright, TypeScript, targeted lint and worker-return fast gate results are recorded without production edit or worker commit.
5. Passing evidence does not imply universal HTML safety or artifact acceptance. Q001/Q004 remain open.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | Playwright sandbox test and proof receipt | synthetic browser UI proof only | D053 and pending browser result | test harness only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no B1 external interface | no ingress, auth or mutation grant | bounded packet | external adapter deferred | DEFERRED_WITH_REASON |

## Evidence / Verification

Capture executionBaseHead, initial/final status, exact changed set, focused Playwright command/count/exit, browser version/profile, positive-control sentinel, panel sentinel and origin, benign heading, intercepted route count, unexpected request disposition, TypeScript/lint and worker-return fast gate. Local reruns one focused independent probe before acceptance. A passing mocked UI test cannot assert AI governance or broad HTML safety.

## Operator Checkpoints

Q001/Q004 Profile A remains. The operator retains real-data classification, actor/account, store/writer, backup/key custody, retention, RPO/RTO, cost and pilot/live effect. No B2 durable writer or active acceptance follows from B1 sandbox proof.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B1-SANDBOX --title "NCR HTML B1 Synthetic Sandbox" --date 2026-10-01 --base e09430475 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | generic-worker-dispatch and no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | source-backed B1 synthetic preview sandbox scope |
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

This baseline authorizes only the test-only B1 preview sandbox proof. It does not authorize production panel repair, route changes, downloaded-file safety, printing or screen-reader claims, real data, provider/governance proof, durable B2 acceptance, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
