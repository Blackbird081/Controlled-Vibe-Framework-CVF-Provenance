# CVF GC-018 Baseline - NCR HTML B1 Print Origin Isolation R1

Memory class: governed-dispatch-baseline

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-HTML-B1-PRINT-R1

Dispatch base head: `b3c5a0aa8`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local technical reviewer; operator owns real-data and effect checkpoints.

Worker target: shared-workspace `INTERNAL_AGENT`.

## Purpose

Authorize one consolidated R1 security rework of the B1 Print candidate. The print surface must not grant printed HTML app-origin script, storage, cookie or authenticated-request authority. Preserve native print invocation and displayed-version binding with a real-browser positive/negative/mutation oracle. Worker edits six inherited paths and does not commit.

## Source / Predecessor Evidence

Local review `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_AUDIT_2026-10-01.md` (material `9cf3b9772`, SHA-256 `13a1fbba70c2e6f6a44047cd486a989053c51982f15a8f3ed619b57bf6ba30ca`) rejected R0 despite native Chromium 1/1 and structural worker-return gate PASS. The popup opened as app-origin `about:blank`, and the synthetic script executed after opener detachment. The original order `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_2026-10-01.md` targeted opener only. D058 authorizes R1 preparation; Q001/Q004 remain open. Candidate input is isolated in stash `beeaf933bf03924532eb02bea331455e2233d743` with six raw-file hashes below.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Local review requires security rework | `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_AUDIT_2026-10-01.md` | Decision / Disposition | `REWORK_REQUIRED_SECURITY_BOUNDARY` | reviewer | ACCEPT |
| Original Print contract tested opener isolation | `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_2026-10-01.md` | Implementation Contract | `window.opener` | R0 work order | ACCEPT |
| Committed panel owns Print and sandboxed preview | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `handlePrint`, preview | `window.open`, `sandbox` | Web panel | ACCEPT |
| Route escapes exported user text | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | `escapeHtml` | `escapeHtml` | export route | ACCEPT |
| D058 parks R0 and requests R1 | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D058 | B1 Print | NCR roadmap | ACCEPT |

## Decision / Baseline / Proposed Tranche

Run bound pre-implementation gate on clean released HEAD, then apply and verify the exact inherited stash. R1 must provide an executable same-origin positive control and an actual Print negative control for synthetic localStorage, cookie and an intercepted no-forward endpoint. An isolation-removal mutation must make the test fail. Preserve native print invocation, displayed build after form edit, and benign visible content. No mechanism is pre-approved: browser enforcement, not a policy string, decides. If safe behavior needs forbidden paths, worker returns blocked for a Local scope decision.

## Scope / Target / Owner Boundary

Exactly six inherited worker paths, with no new worker path: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts`; `docs/reference/CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_PROOF_2026-10-01.md`; `docs/reviews/evidence/cvf-ncr-html-b1-print-repair-worker-proof-2026-10-01.json`; `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_WORKER_RETURN_2026-10-01.md`. Stash `beeaf933bf03924532eb02bea331455e2233d743` is an execution aid only. Route, auth, config, package, ledger, engine, roadmap, continuity and governance are read-only. Local owns independent probe, review and commit.

## Inherited Candidate Fingerprint

| Path | SHA-256 before R1 edit |
|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `169cae24994dd1ead464dfe5a9d88833c5a30926144d9eb9f5bf859918451ad5` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | `d5abfcd3f91b60ae3dc5b24a29da082af3359035cd1114421c00f9c267fd04f8` |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts` | `ae60e047706afa96ae362f6439461fc36f22f74fa75f470b1dc5c473e72a6fa8` |
| `docs/reference/CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_PROOF_2026-10-01.md` | `3cd2f926a260d06f89246943954912f31e0b6ea8be06e22d83131aabde2f8f45` |
| `docs/reviews/evidence/cvf-ncr-html-b1-print-repair-worker-proof-2026-10-01.json` | `2471be54b53d2c5a35a139929aba1baa6c5efc7a657f0a1046557f2aab7efa63` |
| `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_WORKER_RETURN_2026-10-01.md` | `3d76d83e63925142059bcab8a804e85f1f1db6b529914474b9a85412fa673acd` |

## Acceptance Criteria

1. Clean bound pre-implementation PASS precedes verified stash apply; six restored raw hashes match and no extra path appears.
2. A real Chromium positive control demonstrates the synthetic payload has app-origin capability when unsandboxed; actual Print blocks storage/cookie/request authority, and an isolation-removal mutation fails the oracle.
3. Native Print invocation, displayed-version binding and benign rendered content remain proven. No fake popup/print result, real data, provider or uncontrolled network request.
4. Six exact paths contain repair, focused unit/browser test, proof JSON, bounded reference and R1 pending return; focused checks and worker-return gate recorded, no commit.
5. No physical paper/PDF, print-dialog accessibility, universal HTML safety, provider governance or durable acceptance claim. Q001/Q004 remain open.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | Print callback and browser spec | synthetic B1 origin-isolation rework only | D058 and pending R1 run | Web panel | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external interface | no ingress or mutation grant | bounded R1 packet | external adapter deferred | DEFERRED_WITH_REASON |

## Evidence / Verification

Capture clean executionBaseHead/status, stash SHA, six restored hashes, positive and negative browser observations, mutation result, native print count, version and heading, controlled endpoint hits, unexpected request count, focused tests/checks and worker-return gate. Local reruns one focused independent Chromium probe. No raw cookie/token values or real data.

## Operator Checkpoints

Q001/Q004 Profile A remains. The operator retains real-data classification, actor/account, store/writer, backup/key custody, retention, RPO/RTO, cost and pilot/live effect. No B2 durable writer or active acceptance follows from B1 Print proof.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B1-PRINT-R1 --title "NCR HTML B1 Print Origin Isolation R1" --date 2026-10-01 --base b3c5a0aa8 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id B1_PRINT_ORIGIN_AUTHORITY_GAP --prior-finding-set-digest 13a1fbba70c2e6f6a44047cd486a989053c51982f15a8f3ed619b57bf6ba30ca --stdout` |
| generatedProfile | generic-worker-dispatch and no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | source-backed R1 Print origin-isolation scope |
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
