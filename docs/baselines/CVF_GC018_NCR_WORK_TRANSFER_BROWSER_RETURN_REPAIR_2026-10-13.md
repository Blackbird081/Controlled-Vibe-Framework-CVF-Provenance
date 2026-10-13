# CVF GC-018 Baseline - NCR Work Transfer Browser Return Repair

Memory class: governed-dispatch-baseline
docType: baseline
Status: DISPATCH_READY
Date: 2026-10-13
Batch ID: CVF-NCR-WORK-TRANSFER-BROWSER-RETURN-REPAIR-20261013
Dispatch inspection base: 8050a3631770ec902758da1691c627345db48b4c
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN

## Purpose

Repair the rejected primary Work Transfer browser-test harness and complete its original four synthetic draft proof requirements. Local retained the primary exact bytes and partial real-route response; this conditional packet authorizes one same-scope test correction, not a product change or a new milestone.

## Decision / Proposed Tranche

Primary quality is QUALITY_REJECTED_WITH_CONSOLIDATED_FINDINGS in `docs/reviews/CVF_NCR_WORK_TRANSFER_BROWSER_PRIMARY_QUALITY_REVIEW_2026-10-13.md`; frozen custody is `docs/reviews/evidence/ncr-work-transfer-browser-primary-quality-20261013.json` (raw SHA-256 `27d73f14a1d09b785a4acdebc2233259f8ae3b9eb4ed7672e22b5fdd84826d3c`). One user-authorized INTERNAL_AGENT conditional implementation BUILD may modify the existing test and create two fresh proof/return artifacts after Local commits this pair, dedicated continuity and a bound pre-dispatch PASS. Local owns independent review, commits and final disposition. No successor is automatic.

## Evidence

The primary test/proof/return raw SHA-256 are `7eee3f58bd71ec9c38f661527812b1dff96dc2cc01f82495b22b9fc93cdcd446`, `2cc16e758cb590a6971db2cc885619a6d245ee6e42efed6f4bb81be7854db712`, and `f2494fbdd9bc32e4e81da1d9ee5a3e23fa3dc193af20124a6c1efb2da79d0732`. The failed five candidates and raw partial response remain in immutable Local custody. Their unmocked route POST 200 and draft labels are partial positives; download, stale, toggle/reload and complete no-hop-after-journey remain unproved. GC-051 source coverage was Root-owned, committed before this packet; scan status is NOT_STARTED, not a scan claim.

## Scope / Target / Owner Boundary

Conditional exact three outputs: modify `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/ncr-work-transfer-browser.spec.ts`; create `docs/reviews/evidence/ncr-work-transfer-browser-conditional-worker-20261013.json`; create `docs/reviews/CVF_NCR_WORK_TRANSFER_BROWSER_CONDITIONAL_RETURN_2026-10-13.md`. Test <=700 lines, proof <=128000 bytes, return <=450 lines/64000 bytes. One BUILD <=45 minutes including worker reads, writes, focused run, type/lint and final gates. Original primary proof/return, frozen custody, production page/panel/routes, config/preload, registry and active continuity are worker read-only. Local alone cleans any verified Next-generated tsconfig include/format diff from captured preimage. No stage/commit, nested agents, provider/live, real data, public/deploy or extra tracked path.

## Design Control Gate

The only browser API interception allowed is `GET /api/admin/audit`, returning named synthetic records in the real response shape. Do not intercept, fulfill, mock or replace `/api/artifacts/export`, the Work Transfer page or `ArtifactExportPanel`. Use `playwright.config.mock.ts` only for UI-safe local configuration; it is not governance proof. Before any export, prove the existing no-hop preload reached the fresh Next server process after environment loading, `NEXTAUTH_URL` is empty in parent and server, and the evaluate-hop attempt counter is zero. Keep `AUTH_URL` at the chosen loopback origin. Clear provider credential aliases from the child environment without reading or printing values; `.env.local` loading remains a risk addressed by the server-side no-hop preflight. Log only safe state/counters.

Use isolated port 3021, `NEXT_DIST_DIR=.next-ncr-work-transfer-browser`, separate disposable file-adapter audit/snapshot paths under `.cvf/runtime/ncr-work-transfer-browser-conditional-20261013` and an absolute no-hop log in the external temporary directory with a conditional-only basename. The modified test MUST set `EVIDENCE_DIRECTORY` to `.cvf/runtime/ncr-work-transfer-browser-conditional-20261013`, with `ROUTE_RESPONSE_PATH` and `DOWNLOADED_HTML_PATH` derived from it; private decoded HTML and test-owned logs use that same fresh directory; no primary private file may be reused or overwritten. Stop the owned server and remove only owned disposable paths. The separate canonical Alibaba release diagnostic already completed with bounded 9/9 PASS; it is not part of this conditional browser BUILD. No server or browser runs during dispatch authoring.

## Acceptance Criteria

REQ-PREFLIGHT: serial fresh server-side no-hop wrapper before any export; `CVF_PLAYWRIGHT_PORT=3021`, loopback AUTH_URL, empty parent/server NEXTAUTH_URL, distinct dist/file-adapter paths, external absolute log, no credential alias values inspected, zero evaluate attempts both before and after journey. Quote the Windows preload path in NODE_OPTIONS so Node starts with it.

REQ-JOURNEY: real Chromium `/work-transfer` selects named synthetic audit fixture, edits title/source, builds through unmocked export route, observes NOT_CONFIGURED/DRAFT_UNACCEPTED and iframe preview, then honestly checks deselection, reselect and reload; only audit GET is intercepted. Disambiguate navigation/main and preview heading locators from actual DOM.

REQ-VERSION-BYTES: retain actual response JSON and decoded HTML bytes plus saved downloaded HTML bytes under `.cvf/runtime/ncr-work-transfer-browser-conditional-20261013`; compare raw UTF-8 bytes and SHA-256; edit after build, assert stale result/retained prior preview/download and no implicit POST. Distinguish source hash from JSON-wire and HTML hashes.

REQ-RETURN: exact three conditional outputs, fresh actual commands/exits/pins/logs/cleanup/clock and four proof IDs; focused browser, type/lint, worker fast and acceptance ledger PASS for COMPLETE_PENDING_REVIEW; otherwise truthful consolidated BLOCKED_WITH_REASON. Original primary failures remain unchanged.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| EXISTS: Local primary rejection and five failed candidates | `docs/reviews/CVF_NCR_WORK_TRANSFER_BROWSER_PRIMARY_QUALITY_REVIEW_2026-10-13.md` | Findings / Position | NCR-BROWSER-HARNESS, LOCATOR, PROOF, READ-BUDGET | Local quality review | ACCEPT |
| EXISTS: frozen primary raw custody | `docs/reviews/evidence/ncr-work-transfer-browser-primary-quality-20261013.json` | exact embedded primary and partial wire | raw SHA-256 `27d73f14a1d09b785a4acdebc2233259f8ae3b9eb4ed7672e22b5fdd84826d3c` | Local custody | ACCEPT |
| EXISTS: committed GC-051 test coverage source | `docs/corpus-intelligence/registry/entries/cvf-ncr-work-transfer-browser-test.json` | scopePaths, NOT_STARTED | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/ncr-work-transfer-browser.spec.ts` | Local registry owner | ACCEPT |
| EXISTS: Work Transfer selects audit fixture into panel | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx` | recordToExportRequest and inline panel | /work-transfer | Web page | ACCEPT |
| EXISTS: mock port name and default | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.mock.ts` | CVF_PLAYWRIGHT_PORT | port 3001 default | Playwright config | ACCEPT |
| EXISTS: route/preview/download owners | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | POST/buildHtml | /api/artifacts/export | export route | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/build_dispatch_packet_scaffold.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_independent_review_probe_admission.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_changed_corpus_registry_coverage.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | DISPATCH_READY; WORKER_MUST_NOT_COMMIT; acceptance-ledger-json; REQUIRED_GATE_IDS; REQUIRED_FIELDS; TRACE_REQUIRED_LABELS; DEFERRED_PRIVATE_ONLY |
| gateRunPurpose | confirmation/evidence of source-informed packet preparation, not first discovery; Local reviewer runs active-binding pre-dispatch after continuity release |
| claimBoundary | targeted constants and literal requirements, not all checker branches |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python -B governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-WORK-TRANSFER-BROWSER-RETURN-REPAIR-20261013 --title "NCR Work Transfer Browser Return Repair" --date 2026-10-13 --base 8050a3631770ec902758da1691c627345db48b4c --commit-mode WORKER_MUST_NOT_COMMIT --dependency docs/reviews/CVF_NCR_WORK_TRANSFER_BROWSER_PRIMARY_QUALITY_REVIEW_2026-10-13.md --include-worker-return-skeleton --no-evidence-readiness-applicable --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id NCR_WORK_TRANSFER_BROWSER_HARNESS_LOCATOR_PROOF --prior-finding-set-digest 27d73f14a1d09b785a4acdebc2233259f8ae3b9eb4ed7672e22b5fdd84826d3c --scec-problem-key ncr-work-transfer-browser --scec-chain-mode SUCCESSOR --scec-chain-ordinal 1 --scec-predecessor-path docs/reviews/CVF_NCR_WORK_TRANSFER_BROWSER_WORKER_RETURN_2026-10-13.md --scec-predecessor-sha256 f2494fbdd9bc32e4e81da1d9ee5a3e23fa3dc193af20124a6c1efb2da79d0732 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope NO_SUCCESSOR --stdout` |
| generatedProfile | web-ui-dashboard; INTERNAL_AGENT REWORK, no commit |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | ADAPTED_WITH_REASON: frozen primary custody, exact3 conditional manifest, original four requirements and GC-051 preflight |
| checkerReadAheadConfirmation | current REWORK, ledger, source-coverage and literal dispatch checks read before authoring |
| docOnlyNewFields | finding digest, frozen byte lineage and one45-minute conditional worker budget |
| claimBoundary | scaffold is structure only; no conditional BUILD or browser result |

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
| Session or invocation | ncr-work-transfer-browser-return-repair-dispatch-20261013 |
| Working directory | repository root |
| Command or tool surface | targeted source/quality/checker reads, scaffold, raw/HEAD pins and exact3 packet authoring |
| Target paths | `docs/baselines/CVF_GC018_NCR_WORK_TRANSFER_BROWSER_RETURN_REPAIR_2026-10-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_WORK_TRANSFER_BROWSER_RETURN_REPAIR_2026-10-13.md`; `docs/reviews/evidence/ncr-work-transfer-browser-return-repair-dispatch-20261013.json` |
| Allowed scope source | operator2026-10-13 NCR continuation and Root explicit conditional authoring release |
| Before status evidence | HEAD `8050a3631770ec902758da1691c627345db48b4c`; clean worktree and empty staged index before conditional authoring |
| After status evidence | exact three dispatch drafts; conditional BUILD pending |
| Diff evidence | Local reviewer checks manifest, diff, full gates and bound pre-dispatch |
| Approval boundary | private synthetic browser repair only |
| Claim boundary | authoring only; no browser or provider observation |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-work-transfer-browser-return-repair-dispatch-20261013 |
| Expected manifest | `docs/baselines/CVF_GC018_NCR_WORK_TRANSFER_BROWSER_RETURN_REPAIR_2026-10-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_WORK_TRANSFER_BROWSER_RETURN_REPAIR_2026-10-13.md`; `docs/reviews/evidence/ncr-work-transfer-browser-return-repair-dispatch-20261013.json` |
| Actual changed set | `docs/baselines/CVF_GC018_NCR_WORK_TRANSFER_BROWSER_RETURN_REPAIR_2026-10-13.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_WORK_TRANSFER_BROWSER_RETURN_REPAIR_2026-10-13.md`; `docs/reviews/evidence/ncr-work-transfer-browser-return-repair-dispatch-20261013.json` |
| Manifest delta | MATCH required |
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
| Internal source | `docs/reviews/evidence/ncr-work-transfer-browser-return-repair-dispatch-20261013.json` |
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
| INTERNAL_AGENT | local Work Transfer Web source and internal worker | existing test modified plus two fresh docs, no production edit or commit | pinned sources and returned browser proof pending | shared workspace | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | no selected external consumer | no external execution grant | no remote return | no adapter selected | DEFERRED_WITH_REASON |

## Claim Boundary

Synthetic browser draft and byte transport only. No AI governance efficacy, artifact acceptance, durable draft, real-data, W05/R3/R4 exit, provider, public, deployment or production claim.
