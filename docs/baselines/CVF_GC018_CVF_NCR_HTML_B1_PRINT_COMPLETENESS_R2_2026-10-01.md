# CVF GC-018 Baseline - NCR HTML B1 Print Completeness R2

Memory class: governed-dispatch-baseline

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-HTML-B1-PRINT-R2

Dispatch base head: `796079885e45fac2b8e6e6366fe87a8fdb020318`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local technical reviewer; operator owns real-data and effect checkpoints.

Worker target: shared-workspace `INTERNAL_AGENT`.

## Purpose

R2 objective: repair D060 long-document clipping while retaining R1 origin-security obligations. The integrated contract below controls any inherited origin-only wording.

Authorize one consolidated R2 completeness rework of the B1 Print candidate. The print surface must not grant printed HTML app-origin script, storage, cookie or authenticated-request authority. Preserve native print invocation and displayed-version binding with a real-browser positive/negative/mutation oracle. Worker edits six inherited paths and does not commit.

## Source / Predecessor Evidence

Local R1 review `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_ORIGIN_ISOLATION_R1_REVIEW_2026-10-01.md` (material `df1b928a9`, raw SHA-256 `470bd4cae1f4a0d2498aba3c2553489ec91b1227acffd3fc6a4067aebe45fed9`) supports origin isolation but rejects the candidate for long-document clipping: fixed `100vh` sandbox frame prints one page through row 33 versus direct control four pages with row 120/end marker. D060 admits bounded R2 preparation after independent-root-cause adjudication. Candidate stash `42d22bbcea12ee0f555e84e0649877dabd967a4b` is execution input only. Historical R1 contract: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PRINT_ORIGIN_ISOLATION_R1_2026-10-01.md`.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Local review requires security rework | `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_ORIGIN_ISOLATION_R1_REVIEW_2026-10-01.md` | Decision / Disposition | `REWORK_REQUIRED_PRINT_COMPLETENESS` | reviewer | ACCEPT |
| Original Print contract tested opener isolation | `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_2026-10-01.md` | Implementation Contract | `window.opener` | R0 work order | ACCEPT |
| Committed panel owns Print and sandboxed preview | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `handlePrint`, preview | `window.open`, `sandbox` | Web panel | ACCEPT |
| Route escapes exported user text | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | `escapeHtml` | `escapeHtml` | export route | ACCEPT |
| D060 parks R0 and requests R2 | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D060 | B1 Print | NCR roadmap | ACCEPT |

## Decision / Baseline / Proposed Tranche

Run bound pre-implementation gate on clean released HEAD, then apply and verify the exact inherited stash. R2 must provide an executable same-origin positive control and an actual Print negative control for synthetic localStorage, cookie and an intercepted no-forward endpoint. An isolation-removal mutation must make the test fail. Preserve native print invocation, displayed build after form edit, and benign visible content. No mechanism is pre-approved: browser enforcement, not a policy string, decides. If safe behavior needs forbidden paths, worker returns blocked for a Local scope decision.

## Scope / Target / Owner Boundary

Exactly six inherited worker paths, with no new worker path: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts`; `docs/reference/CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_PROOF_2026-10-01.md`; `docs/reviews/evidence/cvf-ncr-html-b1-print-repair-worker-proof-2026-10-01.json`; `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_WORKER_RETURN_2026-10-01.md`. Stash `42d22bbcea12ee0f555e84e0649877dabd967a4b` is an execution aid only. Route, auth, config, package, ledger, engine, roadmap, continuity and governance are read-only. Local owns independent probe, review and commit.

## Inherited Candidate Fingerprint

Git blob OIDs before R2 edits; verify each restored path with `git hash-object <path>` (Git clean filters account for checkout line endings). Record raw-file SHA-256 separately; do not equate raw checkout bytes to Git blob bytes. Preserve the stash.

| Path | Git blob OID |
|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `b71d707fb221725a16c2174cb2d328d4a884fc9e` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | `cd5f4b8c8b454f439e523082d1d0924ce2994d49` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts` | `62f70d5c484770b0e23e186962246a9845b7ae7e` |
| `docs/reference/CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_PROOF_2026-10-01.md` | `5ee04e0875d03b8e74c81b514949167b1c16daac` |
| `docs/reviews/evidence/cvf-ncr-html-b1-print-repair-worker-proof-2026-10-01.json` | `7cda902481341a95efe2dac6ed05ac7184483b73` |
| `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_WORKER_RETURN_2026-10-01.md` | `57b1d1e694b2092284e2a1d6b80e5b243c4914a8` |

## R2 Independent Finding Admission And Integrated Outcome Contract

SCEC disposition is STOP_REASSESS_ARCHITECTURE / INTEGRATED_ROOT_CONTRACT. Worker must first record full architecture reassessment in the existing proof reference; implement only a coherent design meeting all integrated outcomes within scope. Otherwise return blocked design evidence. No same-problem successor is authorized.

Finding ID: D060_PRINT_120_ROW_CLIPPING. Round two is admitted because fixed-height print geometry truncates benign content even while origin-isolation controls PASS; R0/R1 origin authority and R2 pagination have distinct failure oracles. Both remain acceptance obligations; the rejected candidate does not close the origin-security blocker. This is not a reset of the repair chain. No automatic R3 dispatch.

Source authority: `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_ORIGIN_ISOLATION_R1_REVIEW_2026-10-01.md`, Findings / Position and Decision / Disposition, material `df1b928a9`. Evidence reuse is bounded: use the existing Local 120-row finding without rerunning it during authoring. Worker must acquire new implementation output proof.

Reviewer-local repair assessment: MATERIAL_DESIGN_CHANGE. The rejected empty-sandbox `height:100vh` mechanism cannot be accepted by a deterministic wording or one-line evidence repair. A printable isolation design plus output oracle must materially change; scope, effect and commit owner remain bounded to the inherited six paths and Local closure.

1. Drive the actual product Print button with synthetic short and long displayed HTML; do not validate only a hand-built equivalent shell. Retain native `print()` observation and displayed-version binding after unsaved form changes.
2. Obtain browser-generated multi-page output from the actual resulting print surface using Chromium print media/A4. Assert at least two pages, row 1, representative rows 40 and 80, row 120 and a unique end marker from a 120-row fixture. Page count alone is insufficient. Record extraction method and observed markers/counts in the existing proof JSON. Temporary PDF files belong outside tracked paths and are disposable test outputs. Use existing tooling only; no dependency/config/package changes.
3. Positive output control must include the full long document; the fixed-height clipping mutation must remove the end marker or intermediate rows and fail the completeness assertion. Also retain executable app-origin positive control, actual-button negative storage/cookie/intercepted-request oracle, and isolation-removal mutation from R1. Never regain full output by granting payload app-origin authority.
4. Cover normal short content and fail-closed popup/opener/load/print failure branches with focused unit evidence; distinguish browser-observed branches from unit-only branches. No unexpected outbound fixture request may occur.
5. Return one integrated outcome: completeness AND origin safety AND native print AND version binding. If any is unproven, return BLOCKED_WITH_REASON with the narrowest amendment; no partial success or hand-built-shell proof may close this order.

Browser-generated output is synthetic renderer proof only. It establishes no physical-printer, dialog, accessibility, every-browser or universal HTML guarantee. Q001/Q004 remain OPEN; durable B2 and P11 remain parked.

## Acceptance Criteria

- [ ] Actual-button long-document output includes row 1, 40, 80, 120 and unique end marker across multiple pages; clipping mutation fails that oracle while direct positive output succeeds.

1. Clean bound pre-implementation PASS precedes verified stash apply; six restored Git blob OIDs match and no extra path appears.
2. A real Chromium positive control demonstrates the synthetic payload has app-origin capability when unsandboxed; actual Print blocks storage/cookie/request authority, and an isolation-removal mutation fails the oracle.
3. Native Print invocation, displayed-version binding and benign rendered content remain proven. No fake popup/print result, real data, provider or uncontrolled network request.
4. Six exact paths contain repair, focused unit/browser test, proof JSON, bounded reference and R2 pending return; focused checks and worker-return gate recorded, no commit.
5. No physical paper, print-dialog accessibility, universal HTML safety, provider governance or durable acceptance claim. Q001/Q004 remain open.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | Print callback and browser spec | synthetic B1 origin-isolation rework only | D060 and pending R2 run | Web panel | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external interface | no ingress or mutation grant | bounded R2 packet | external adapter deferred | DEFERRED_WITH_REASON |

## Evidence / Verification

Capture clean executionBaseHead/status, stash SHA, six restored Git blob OIDs, positive and negative browser observations, mutation result, native print count, version and heading, controlled endpoint hits, unexpected request count, focused tests/checks and worker-return gate. Local reruns one focused independent Chromium probe. No raw cookie/token values or real data.

## Operator Checkpoints

Q001/Q004 Profile A remains. The operator retains real-data classification, actor/account, store/writer, backup/key custody, retention, RPO/RTO, cost and pilot/live effect. No B2 durable writer or active acceptance follows from B1 Print proof.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B1-PRINT-R2 --title "NCR HTML B1 Print Completeness R2" --date 2026-10-01 --base 796079885e45fac2b8e6e6366fe87a8fdb020318 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 2 --root-cause-cluster-id B1_PRINT_CONTENT_COMPLETENESS_GAP --prior-finding-set-digest 470bd4cae1f4a0d2498aba3c2553489ec91b1227acffd3fc6a4067aebe45fed9 --stdout` |
| generatedProfile | generic-worker-dispatch and no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | source-backed R2 Print origin-isolation scope |
| checkerReadAheadConfirmation | dispatch, acceptance-ledger, closeability, structural, release and high-risk local transaction checker sources |
| docOnlyNewFields | N/A with reason: no new governed field schema |
| claimBoundary | Scaffold is authoring aid only |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_high_risk_local_transaction_proof.py` |
| literalTokensReviewed | DISPATCH_READY; source ACCEPT rows; worker-return gate; exact six-path inherited scope; no durable transaction authority |
| gateRunPurpose | Confirm packet structure and authority after source review |
| claimBoundary | Static gate PASS cannot prove browser behavior |

## Claim Boundary

This baseline authorizes synthetic B1 Print origin-isolation rework only. It does not authorize route/auth/engine/storage changes, real data, provider/governance proof, durable B2 acceptance, physical printing, other browsers, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
