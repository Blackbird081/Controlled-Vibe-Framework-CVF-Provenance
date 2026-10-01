# CVF NCR HTML B1 Print Scope Audit

Memory class: governed-review

docType: review

Status: REVIEW_COMPLETE_BOUNDED

Date: 2026-10-01

providerExecutionAuthority: FORBIDDEN

## Purpose

Select the next decision-changing B1 slice after the preview sandbox proof. Inspect the Print action's real browser semantics and current tests without changing product code or asserting governance behavior.

## Target / Source

At clean HEAD `5d594dfe2`, Local inspected four exact Web paths. The GC-051 entry `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b1-print-scope-source.json` names only those paths. [The HTML Standard](https://html.spec.whatwg.org/multipage/nav-history-apis.html) is external browser-semantics context, not private CVF authority. The controlled code path remains the panel source; no full Web scan is claimed.

## Scope / Methodology

Startup acknowledged: current mode=`cvf_ncr_p10_closed_p11_parked`; handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=read-only post-B1 sandbox triage; role=Local source verifier; phase=internal audit; technical decision owner=Local; effect/data decision owner=operator. Parked checkpoint=Q001/Q004 Profile A, real actor/data/store, artifact acceptance, pilot/live, P11, public sync and deployment.

Local compared the real Print callback, the jsdom mock, existing browser test, and export route's escaping. The HTML Standard says `window.open` with `noopener` and `_blank` returns `null`. A separate in-memory Chromium 145 probe installed a click listener on a disposable page and observed `window.open('', '_blank', 'noopener,noreferrer') === null`; it made no app request or repository mutation. That probe confirms native semantics in one Chromium profile but is not an Artifacts-panel run. Other B1 gaps (passive loads and accessibility) were considered but do not explain the Print callback's early return.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Print opens `_blank` with `noopener,noreferrer`, returns if handle is null, then writes HTML and calls print | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `handlePrint`, lines 435-443 | `window.open`, `if (!printWindow) return`, `document.write`, `print` | Artifacts panel | ACCEPT |
| Component test substitutes an object for `window.open` before checking write/print | TEST_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | print test, lines 490-534 | `mockReturnValue(printWindow)` | panel jsdom test | ACCEPT |
| Existing Artifacts browser spec has no named native Print invocation assertion | TEST_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-panel.spec.ts` | synthetic export cases | preview/export checks | Playwright precedent | ACCEPT |
| Route escapes user text before HTML rendering | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | `escapeHtml`, `renderInline`, `buildHtml` | escaped fields/body | HTML export route | ACCEPT_BOUNDED |

## Findings / Position

| Boundary | Evidence | Decision consequence |
|---|---|
| Native `window.open` return | HTML Standard returns `null` for `_blank` with `noopener`; isolated Chromium click probe returned `NULL` | The panel's `if (!printWindow) return` is reached on that tested native path, before `document.write` or `print`. |
| Test masking | jsdom test forces a non-null fake window | Its passing write/print assertions do not establish actual browser Print behavior. |
| UI/runtime scope | Panel uses the displayed `result.html`; B1 version binding is already bounded by jsdom tests | Browser test should verify the displayed version is printed after form edits, not current unsaved form input. |
| Security boundary | The Print path opens a top-level document and writes HTML; it does not inherit preview iframe sandbox | A repair must preserve opener isolation and avoid treating the preview sandbox proof as print-window safety. Route escaping is source-backed for the normal route, but intercepted HTML is only a synthetic test fixture. |
| Alternative gaps | Passive loads and screen-reader announcement remain untested | They require separate outcome-specific work and should not be folded into this Print repair. |

## Decision / Disposition

`REVIEW_COMPLETE_BOUNDED`: Local may author a B1 Print repair packet. The worker should first reproduce the actual panel Print failure with a real Chromium browser and synthetic intercepted export, then implement the smallest correction within the panel and its tests, preserving no-opener behavior before any HTML is written. The browser acceptance must distinguish a successful print invocation from merely opening a blank popup and verify the printed displayed result after form edits. If a browser-safe, no-opener design cannot be proven within scope, the worker returns `BLOCKED_WITH_REASON`; do not weaken the boundary just to make the button respond. This audit itself does not authorize worker execution.

Q001/Q004, durable B2 actor/store/writer/recovery, passive-load, accessibility, provider/live governance, public sync and deployment remain parked. No actual printed paper, print-dialog accessibility or other-browser behavior is claimed.

## Risk / Corrective Action

Removing `noopener` alone can expose the app to printed HTML via `window.opener`; a repair must prevent that before writing the document and include a negative synthetic script/opener oracle. Native `window.open` may create a popup while returning `null`, so a popup count alone is not proof of printing. A browser test that stubs `window.open` with an object would repeat the jsdom blind spot. The Local reviewer should independently inspect ordering and rerun one focused browser case.

## Finding-To-Governance Learning Disposition

| Defect class | Learning lane | Disposition | Next control action | Batch status |
|---|---|---|---|---|
| RUNTIME_SIGNAL_GAP: fake `window.open` bypasses native noopener return | RUNTIME_BEHAVIOR_LEARNING | DESIGN_REVIEW_REQUIRED | native browser repro and bounded Print repair packet | packet candidate |
| B2 durable owner/store gap | DOCUMENTATION_ONLY_LEARNING | DEFER_WITH_REASON: Q001/Q004 require operator choices | no writer or acceptance successor | parked |

## Corpus Completeness And Report Integrity

- Corpus task class: AUDIT.
- Corpus root: four exact Web paths below, not the Web package.
- Snapshot time: 2026-10-01 at HEAD `5d594dfe2`.
- Enumeration command: `Get-ChildItem -LiteralPath <four Source Verification paths> -File`; hashes via `Get-FileHash -Algorithm SHA256` on each exact path.
- Manifest artifact or inline manifest: four path/hash rows below.
- Manifest hash: N/A with reason: partial named-path audit uses per-file hashes.
- Processing ledger artifact or inline ledger: all four rows below are READ.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=4; ledger_terminal=4; exclusions=0; unresolved=0 within named scope.
- Unresolved files: 0 within named scope; broader Web source is outside scope.
- Declared exclusions: all other Web paths are not counted as scanned Web source.
- Unreadable or unsupported files: none within named scope.
- Aggregation check: PASS, four distinct paths.
- Drift check: PASS, hashes recomputed after source inspection with no source edit.
- Output traceability: Source Verification, Findings and Decision above.
- Adversarial verification: separated native `window.open` return from mocked object and popup creation from actual print invocation.
- Corpus verdict: PARTIAL

| Path | SHA-256 | Terminal status |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `8602daf187444423c2575dee14898db19508e575224148c896dd235cd587451a` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | `7e3db63aa9744fbc63af0e22272c6ece6e0acea3adea73d8775145ba4416996e` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-panel.spec.ts` | `7e8fc4cdd088a2142960fbfb7df4133d30956db325b5fdfc70c718a80aa9c0f3` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | `6b988ba687b9b1478f097ca81c3e1235aa20ef819106c050279779da00781c3c` | READ |

## Knowledge System Reconciliation

- Knowledge task class: named-path B1 Print gap audit.
- Source manifest: four exact file/hash rows above.
- Source manifest hash: N/A with reason: partial named-path manifest uses per-file hashes.
- Enumeration safety: filesystem-backed exact `Get-ChildItem -LiteralPath`; no broad listing is completeness evidence.
- Intake registry or ledger: `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b1-print-scope-source.json`.
- Authority assets: four Web paths; external HTML Standard is browser context only.
- Derived views: Source Verification, Findings and Decision here.
- Semantic region ledger: panel Print callback, jsdom mock, browser-test gap, route escaping.
- Region reconciliation: assets=4; mapped=4; deferred=0; unmapped=0.
- Orphan or unmapped assets: 0 within named scope.
- Cross-region links: B1 preview sandbox does not carry to Print; route escaping does not make null WindowProxy printable.
- Drift check: PASS for four hashes at HEAD `5d594dfe2`.
- Rebuildability check: PASS by rehashing four named paths.
- Retrieval boundary: exact local source and official browser standard; no outside-repo ingestion.
- Adversarial verification: a popup may exist even though the callback receives `null` and never writes/prints.
- Knowledge-map verdict: PARTIAL

## Epistemic Process Block

### Expected Result / Prediction

If the Print callback were browser-proven, a native browser test would verify actual print invocation despite `noopener` and check opener isolation.

### Evidence Comparison

The named jsdom test forces a non-null return, while the HTML Standard and isolated Chromium probe return `null` for the exact `window.open` arguments.

### Contradiction Or Gap Disposition

The mock and native semantics disagree on the branch that controls Print. Actual panel click remains untested and is the first acceptance step of a repair packet.

### Claim Update

Permit bounded Print repair packet authoring. Do not claim printed output or broader HTML security before real browser proof.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Input type | internal governed input (no external intake) |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Internal source | `docs/reviews/CVF_CVF_NCR_HTML_B1_SYNTHETIC_SANDBOX_COMPLETION_2026-10-01.md` |
| Chain map route | Local source-derived browser owner comparison |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | Artifacts panel Print callback |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | HTML Standard informs semantics, not CVF runtime proof |

## External/Local Coordination Binding

Role: Local source verifier. Phase: internal read-only audit. Decision owner: Local; effect owner: operator.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `Corpus verdict: PARTIAL`; `Knowledge-map verdict: PARTIAL`; exact four-path manifest; source ACCEPT rows |
| gateRunPurpose | Confirm bounded source evidence after read-ahead, not discover browser behavior |
| claimBoundary | Static gate PASS does not prove the Artifacts Print button or a repair |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local source verifier |
| Agent type | INTERNAL_AGENT reviewer |
| Invocation ID | cvf-ncr-html-b1-print-scope-audit-20261001 |
| Provider or surface | private CVF source and official browser-standard context |
| Session or invocation | post-B1 Print triage, 2026-10-01 |
| Working directory | repository root and Web package |
| Command or tool surface | exact source reads, Git status, file hashes, official standard, disposable Chromium probe |
| Target paths | this review, NCR roadmap D056, GC-051 entry/aggregate |
| Before status evidence | clean worktree at `5d594dfe2` |
| After status evidence | exact four-path audit material set pending commit |
| Diff evidence | four-path source/roadmap/registry change set |
| Allowed scope source | active read-only post-B1 triage; delegated Local technical decisions |
| Approval boundary | audit and packet-authoring recommendation only |
| Claim boundary | no Artifacts Print browser test or production repair yet |
| Expected manifest | `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_SCOPE_AUDIT_2026-10-01.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b1-print-scope-source.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |
| Actual changed set | `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_SCOPE_AUDIT_2026-10-01.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b1-print-scope-source.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | B1 Print source/native return gap and bounded repair-packet candidate |
| claimDisposition | CLAIM_REJECTED: no actual Artifacts Print success or failure is asserted before app browser test |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no governance receipt created or inspected |
| actionEvidence | ACTION_EVIDENCE_PRESENT: isolated disposable Chromium click probe only |
| invocationBoundary | local source reads and isolated browser semantics probe |
| interceptionBoundary | no app export interception or wrapper in this audit |
| claimLanguage | source path reaches early return under standard/native semantics; panel browser proof pending |
| forbiddenExpansion | no route, provider, real data, durable store, artifact acceptance, public sync or deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This audit supports only authoring a bounded B1 Print repair packet. It does not prove paper output, popup lifetime, app Print behavior, universal HTML safety, preview sandbox transfer, governance behavior, Q001/Q004 exit or production readiness.
