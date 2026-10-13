# CVF GC-018 Baseline - NCR Work Transfer Browser HTML Draft Journey

Memory class: governed-dispatch-baseline
docType: baseline
Status: DISPATCH_READY
Date: 2026-10-13
Batch ID: CVF-NCR-WORK-TRANSFER-BROWSER-20261013
Dispatch inspection base: 8accf591da4223fe0a88fc6c63b2062cce733ee1
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN

## Purpose

Select one finite browser proof of the existing Work Transfer HTML draft path. A synthetic audit record is selected on `/work-transfer`; the real `ArtifactExportPanel` sends one request to the real `/api/artifacts/export` route; the browser shows its draft receipt, preview and saved HTML. Existing B2d proves route bytes from the separate artifacts page. This package fills the Work Transfer composition gap without product changes.

## Decision / Proposed Tranche

Select one internal test-only worker with the exact three outputs in the paired work order. Local reviewer/closer retains final technical disposition, material commit and session sync. Dispatch is pending the bound Local gate and continuity release; this baseline is no worker execution receipt.

## Evidence

`docs/reviews/evidence/ncr-work-transfer-browser-dispatch-20261013.json` carries the clean inspection base, ten raw/HEAD source pins and the named composition gap. Current Work Transfer unit tests stub the panel; existing B2d proves the separate artifacts-page real route bytes. Browser outcome evidence will be returned by the worker and reviewed independently.

## Scope / Target / Owner Boundary

The worker creates exactly three paths: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/ncr-work-transfer-browser.spec.ts`; `docs/reviews/evidence/ncr-work-transfer-browser-worker-20261013.json`; `docs/reviews/CVF_NCR_WORK_TRANSFER_BROWSER_WORKER_RETURN_2026-10-13.md`. Existing page, panel, routes, B2d test/preload, Playwright config, auth utilities and all production files are read-only. Test <=700 lines, proof <=128000 bytes, return <=450 lines and <=64000 bytes. One BUILD <=60 minutes including reads, writes, tests and gates; any preceding read-only intake is recorded separately. No nested agents, extra tracked helper, dependency, real data, provider invocation, public effect or deployment. The Local reviewer/closer owns review, gate disposition, material commit and continuity.

## Design Control Gate

The only browser API interception allowed is `GET /api/admin/audit`, returning named synthetic records in the real response shape. Do not intercept, fulfill, mock or replace `/api/artifacts/export`, the Work Transfer page or `ArtifactExportPanel`. Use `playwright.config.mock.ts` only for UI-safe local configuration; it is not governance proof. Before any export, prove the existing no-hop preload reached the fresh Next server process after environment loading, `NEXTAUTH_URL` is empty in parent and server, and the evaluate-hop attempt counter is zero. Keep `AUTH_URL` at the chosen loopback origin. Clear provider credential aliases from the child environment without reading or printing values; `.env.local` loading remains a risk addressed by the server-side no-hop preflight. Log only safe state/counters.

Use isolated port 3021, `NEXT_DIST_DIR=.next-ncr-work-transfer-browser`, separate disposable file-adapter audit/snapshot paths and an absolute no-hop log in the external temporary directory. Stop the owned server and remove only owned disposable paths. The Local release diagnostic on ports 3011/3012 and its dist directories is separate and may run concurrently. No server or browser runs during dispatch authoring.

## Acceptance Criteria

REQ-PREFLIGHT: a serial test with no export request proves server-side no-hop wrapper after Next environment loading, parent and server empty `NEXTAUTH_URL`, external absolute log, zero evaluate attempts and isolated run configuration before the journey case.

REQ-JOURNEY: one real Chromium `/work-transfer` path receives only a named synthetic audit fixture, selects a record, verifies populated draft fields, edits title/source, builds via the unmocked route, and observes `NOT_CONFIGURED`, `DRAFT_UNACCEPTED`, draft UI state, and iframe HTML preview. Deselect/reselect switches clear the selected panel/result; reload/reselect derives a fresh draft from the fixture, without claiming durable draft restore.

REQ-VERSION-BYTES: capture the actual export response bytes, decode its `data.html`, compare downloaded raw UTF-8 bytes and SHA-256 to that HTML with no normalization, then edit a field without rebuilding. Assert stale version labeling, retained prior preview/download identity, and no second export until an explicit build. Distinguish source hash, JSON wire hash and artifact hash.

REQ-RETURN: exact three worker artifacts and a truthful ledger join; source/raw-HEAD pins, setup, browser response/download/preflight log observations, commands/exits, cleanup, timing and failures are recorded. Focused test, type/lint as applicable, worker fast gate and acceptance-ledger gate must pass before `COMPLETE_PENDING_REVIEW`.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: selected Work Transfer record becomes export request | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx` | `recordToExportRequest`, `handleSelectRecord`, inline panel | `recordToExportRequest`; `ArtifactExportPanel initialRequest` | Work Transfer page | ACCEPT |
| EXISTS: current unit test stubs panel | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.test.tsx` | top-level `vi.mock` for panel | `ArtifactExportPanel` | Work Transfer unit test | ACCEPT |
| EXISTS: real route returns HTML draft with optional receipt hop | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | `buildHtml`, `POST` | `/api/artifacts/export` | export route | ACCEPT |
| EXISTS: existing server no-hop guard and B2d byte test | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-route-byte-download.spec.ts` | serial preflight and saved-byte case | `summarizeIsolation`; route response body | B2d test | ACCEPT |
| EXISTS: no-hop preload records processed environment and blocks evaluate fetch | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/support/b2d-no-hop-preload.cjs` | `b2dNoHopFetch`, `stateEntry` | `/api/governance/evaluate` | B2d preload | ACCEPT |
| EXISTS: W05 retained browser composition limit | `docs/reviews/CVF_NCR_W05_SELECTED_CHAIN_READINESS_2026-10-07.md` | Consolidated Milestone Disposition | Work Transfer browser consumer and whole-UX qualification | Local W05 review | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | DISPATCH_READY; WORKER_MUST_NOT_COMMIT; acceptance-ledger-json; REQUIRED_GATE_IDS; REQUIRED_FIELDS; TRACE_REQUIRED_LABELS; DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | confirmation/evidence of source-informed packet preparation, not first discovery; Local reviewer runs active-binding pre-dispatch after continuity release |
| claimBoundary | targeted constants and literal requirements, not all checker branches |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python -B governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-WORK-TRANSFER-BROWSER-20261013 --title "NCR Work Transfer Browser HTML Draft Journey" --date 2026-10-13 --base 8accf591da4223fe0a88fc6c63b2062cce733ee1 --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_NCR_W05_SELECTED_CHAIN_READINESS_2026-10-07.md --include-worker-return-skeleton --no-evidence-readiness-applicable --scec-problem-key ncr-work-transfer-browser --scec-successor-scope NO_SUCCESSOR --stdout` |
| generatedProfile | web-ui-dashboard; internal no-commit |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: existing Work Transfer route, mock config and no-hop evidence define a browser-specific test contract |
| checkerReadAheadConfirmation | current constants and required markers read before authoring |
| docOnlyNewFields | synthetic browser scope, distinct port/dist and exact raw byte oracle |
| claimBoundary | scaffold generated outside repository; packet content remains Local-authored and pending review |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work-order`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`
Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class work-order --role dispatcher --lifecycle-phase pre-dispatch`
Returned defects: NONE_RETURNED
Actual result: 0 candidates, 0 returned, not truncated.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local INTERNAL_AGENT dispatch author |
| Provider or surface | private shared workspace |
| Session or invocation | ncr-work-transfer-browser-dispatch-20261013 |
| Working directory | repository root |
| Command or tool surface | targeted reads, scaffold, ADIF resolver and raw/HEAD source pins |
| Target paths | `docs/baselines/CVF_GC018_NCR_WORK_TRANSFER_BROWSER_2026-10-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_WORK_TRANSFER_BROWSER_2026-10-13.md`; `docs/reviews/evidence/ncr-work-transfer-browser-dispatch-20261013.json` |
| Allowed scope source | 2026-10-13 operator NCR continuation and Local dispatch/review split |
| Before status evidence | inspection base `8accf591da4223fe0a88fc6c63b2062cce733ee1`; clean worktree and empty staged index (`git status --short` empty) before dispatch authoring |
| After status evidence | three dispatch drafts; worker BUILD pending |
| Diff evidence | Local reviewer checks exact manifest and bound pre-dispatch gate |
| Approval boundary | test-only internal assignment |
| Claim boundary | no worker/browser/provider observation in this trace |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-work-transfer-browser-dispatch-20261013 |
| Expected manifest | `docs/baselines/CVF_GC018_NCR_WORK_TRANSFER_BROWSER_2026-10-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_WORK_TRANSFER_BROWSER_2026-10-13.md`; `docs/reviews/evidence/ncr-work-transfer-browser-dispatch-20261013.json` |
| Actual changed set | `docs/baselines/CVF_GC018_NCR_WORK_TRANSFER_BROWSER_2026-10-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_WORK_TRANSFER_BROWSER_2026-10-13.md`; `docs/reviews/evidence/ncr-work-transfer-browser-dispatch-20261013.json` |
| Manifest delta | MATCH: exactly the three dispatch artifacts above |
| Deletion or rename disposition | N/A with reason: none |

## Epistemic Process Block

Expected Result / Prediction: selected audit fixture drives editable request; the real route response drives draft preview and exact download; post-build edit marks the old result stale.
Evidence Comparison: B2d already tests export-route bytes from `/artifacts`; Work Transfer unit tests stub the panel. Selected browser composition is not yet observed.
Contradiction Or Gap Disposition: add one finite test, consume accepted evidence, preserve any source failure as a blocker.
Claim Update: dispatch plan only; no browser result or approval claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Reason: private dispatch and synthetic test scope.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: Local closer may update named active continuity after reviewed dispatch material and after later worker closure. Worker has no protected-path write grant.
Protected paths:
- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Operator authorization: 2026-10-13 NCR continuation with Local review/closure and selected internal worker.
Rollback boundary: this dispatch packet and dedicated Local continuity updates only; prior accepted evidence remains retained.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Internal source | `docs/reviews/evidence/ncr-work-transfer-browser-dispatch-20261013.json` |
| Chain map route | Local selection -> internal worker -> Local verification and disposition |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | existing NCR W05 roadmap and Work Transfer/browser owners |
| Disposition | internal test-only execution; no remote research |
| Claim boundary | Local private verification is final decision |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named sources and test only; no complete corpus scan.

## Knowledge System Applicability

NOT_APPLICABLE_WITH_REASON: no knowledge-map or repository scan claim.

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: named browser proof, no rescan.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | local Work Transfer Web source and internal worker | exact three new outputs, no production edit or commit | pinned sources and returned browser proof pending | shared workspace | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | no selected external consumer | no external execution grant | no remote return | no adapter selected | DEFERRED_WITH_REASON |

## Claim Boundary

Synthetic browser draft and byte transport only. No AI governance efficacy, artifact acceptance, durable draft, real-data, W05/R3/R4 exit, provider, public, deployment or production claim.
