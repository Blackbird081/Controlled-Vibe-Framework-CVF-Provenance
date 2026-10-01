# CVF GC-018 Baseline - NCR HTML B1 Print Browser Repair

Memory class: governed-dispatch-baseline

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-HTML-B1-PRINT-REPAIR

Dispatch base head: `0cb7d7b2a`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local technical reviewer; operator owns real-data and effect checkpoints.

Worker target: shared-workspace `INTERNAL_AGENT`.

## Purpose

Authorize one bounded B1 Print repair in the Artifacts panel after real Chromium reproduces the current failure. The worker may edit the panel and focused tests within six named paths, with no provider, real data, durable store, artifact acceptance or worker commit.

## Source / Predecessor Evidence

Local audit `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_SCOPE_AUDIT_2026-10-01.md` (material `8ad689b48`) identified a source/browser gap. Roadmap D056 permits packet authoring. The Print callback uses `_blank` plus `noopener,noreferrer`, then returns on a null `window.open` result. The HTML Standard specifies this null return; an isolated Chromium probe observed it. Existing jsdom test supplies a non-null fake; the app button has not yet been tested in real browser and must be reproduced by the worker. Q001/Q004 remain open.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| D056 permits Print packet | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D056 | B1 Print | NCR roadmap | ACCEPT |
| Local audit bounds evidence | `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_SCOPE_AUDIT_2026-10-01.md` | Findings/Decision | null-return probe | Local audit | ACCEPT |
| Print callback opens with noopener and returns on null | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | Print callback | `window.open`, `result.html` | Web panel | ACCEPT |
| jsdom test fakes non-null popup | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | Print test | `window.open` mock | panel test | ACCEPT |
| Browser spec supports intercepted synthetic export | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-panel.spec.ts` | HTML case | `page.route(` | test harness | ACCEPT |
| Mock config starts local Web server | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.mock.ts` | `webServer` | `webServer` | test harness | ACCEPT |

## Decision / Baseline / Proposed Tranche

Worker first observes the actual Artifacts Print button failing on unmodified panel in one Chromium profile with an intercepted synthetic export. Then worker repairs the callback to invoke print on the displayed result while detaching the opener before HTML write. A real-browser negative oracle must show a synthetic script cannot reach the app through `window.opener`; a version oracle must show form edits without rebuild do not alter printed HTML. Blank popup or fabricated `window.open` object is not sufficient.

If the app failure is not reproduced or safe browser proof is impossible in scope, return `BLOCKED_WITH_REASON`. No physical printer, print-dialog accessibility, passive load, downloaded HTML, other browsers, provider governance or durable B2 acceptance is claimed.

## Scope / Target / Owner Boundary

Exactly six worker paths: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts`; `docs/reference/CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_PROOF_2026-10-01.md`; `docs/reviews/evidence/cvf-ncr-html-b1-print-repair-worker-proof-2026-10-01.json`; `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_WORKER_RETURN_2026-10-01.md`. Panel and component test are modify paths; remaining four are create paths. Route, auth, config, package, engine, ledger, storage, roadmap and continuity are read-only. Local owns independent probe, registry repair, review and commit.

## Acceptance Criteria

1. Native Chromium reproduces actual Artifacts Print button failure before production edit; retain the observation.
2. Repaired button opens a native popup and invokes print on the current displayed result, including after a form edit without rebuild.
3. Opener is detached before any synthetic HTML write; popup script cannot access app through opener; no fixture outbound request.
4. Six exact paths contain repair, focused unit/browser tests, proof JSON, bounded reference and pending return. Focused tests, TypeScript/lint and worker-return gate are recorded without worker commit.
5. Q001/Q004 and real actor/store/effect decisions stay open.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | panel Print callback and browser spec | synthetic B1 browser UI proof only | D056 and pending run | Web panel | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no B1 external interface | no ingress or mutation grant | bounded packet | external adapter deferred | DEFERRED_WITH_REASON |

## Evidence / Verification

Capture executionBaseHead, initial/final status, exact six-path changed set, pre-repair actual-button failure, focused Chromium command/result/profile, native popup and print oracle, opener state before HTML write, synthetic script result, displayed-version binding, export interception and unexpected request count, focused unit/TypeScript/lint and worker-return gate. Local reruns one focused independent probe. Synthetic UI proof does not establish AI governance.

## Operator Checkpoints

Q001/Q004 Profile A remains. The operator retains real-data classification, actor/account, store/writer, backup/key custody, retention, RPO/RTO, cost and pilot/live effect. No B2 durable writer or active acceptance follows from B1 Print proof.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B1-PRINT-REPAIR --title "NCR HTML B1 Print Browser Repair" --date 2026-10-01 --base 0cb7d7b2a --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | generic-worker-dispatch and no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | source-backed B1 Print browser repro/repair scope |
| checkerReadAheadConfirmation | dispatch, acceptance-ledger, closeability, structural, release and high-risk local transaction checker sources |
| docOnlyNewFields | N/A with reason: no new governed field schema |
| claimBoundary | Scaffold is authoring aid only |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_high_risk_local_transaction_proof.py` |
| literalTokensReviewed | DISPATCH_READY; source ACCEPT rows; worker-return gate; exact six-path scope; no durable transaction authority |
| gateRunPurpose | Confirm packet structure and authority after source review |
| claimBoundary | Static gate PASS cannot prove browser behavior |

## Claim Boundary

This baseline authorizes only synthetic B1 Print browser repro/repair. It does not authorize route changes, real data, provider/governance proof, durable B2 acceptance, physical printing, accessibility, passive load, downloaded HTML, other browsers, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
