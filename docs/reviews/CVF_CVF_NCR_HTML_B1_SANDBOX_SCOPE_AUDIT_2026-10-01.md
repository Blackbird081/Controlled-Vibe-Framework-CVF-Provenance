# CVF NCR HTML B1 Preview Sandbox Scope Audit

Memory class: governed-review

docType: review

Status: REVIEW_COMPLETE_BOUNDED

Date: 2026-10-01

providerExecutionAuthority: FORBIDDEN

## Purpose

Select the next decision-changing no-effect HTML slice after B2f. Compare the remaining B1 preview/browser gap with the already bounded B2a-B2f transport evidence and the B2 actor/store checkpoint. This is a Local read-only audit, not browser execution or worker authority.

## Target / Source

At clean HEAD `c8bc60b5f`, Local read four exact Web source/test paths and the governed B1, B2 owner/storage, B2c and B2f reviews. GC-051 entry `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b1-sandbox-scope-source.json` records only those four Web paths. This is a named-path partial audit; no full Web coverage, browser run, real data or provider call is claimed. [The HTML Standard](https://html.spec.whatwg.org/dev/iframe-embed-object.html) supplies external browser-semantics context, not CVF source authority or a substitute for the proposed runtime probe.

## Scope / Methodology

Startup acknowledged: current mode=`cvf_ncr_p10_closed_p11_parked`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=read-only post-B2f roadmap triage; role=Local source verifier; phase=internal audit; technical decision owner=Local; effect/data decision owner=operator. Parked checkpoint=Q001/Q004 Profile A, real accepting actor/store, backup/key custody, retention, RPO/RTO, cost, pilot/live, P11, public sync and deployment.

Local inspected the panel's `srcDoc`/`sandbox` markup, its adjacent jsdom preview assertions, and two Playwright Artifacts specs. The existing browser tests observe a rendered heading and downloaded bytes but contain no named assertion that active content in the preview is blocked. The B2 owner/storage audit remains controlling for durable acceptance: exact bytes and a receipt do not decide actor, writer, store or recovery. The shared-workspace worker would be `INTERNAL_AGENT`; remote Web advice remains advisory. No test was executed in this audit.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| The preview uses `srcDoc={result.html}` and an empty `sandbox` attribute | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | preview iframe, lines 700-707 | `srcDoc`, `sandbox` | Artifacts panel | ACCEPT |
| B1 jsdom tests compare iframe `srcdoc` across displayed versions | TEST_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | `iframeHtml` and version cases | `getAttribute('srcdoc')` | panel component tests | ACCEPT_BOUNDED |
| B2c browser test reads preview heading and saved-file bytes from an intercepted synthetic response | TEST_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-byte-download.spec.ts` | `openArtifactsWithSyntheticExport`, `buildAndDownload` | `page.route`, `frameLocator`, `download` | B2c browser proof | ACCEPT_BOUNDED |
| Existing Artifacts browser test uses an intercepted synthetic export and checks visible preview | TEST_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-panel.spec.ts` | English HTML packet case | `page.route`, `getByTitle('Preview')` | Artifacts browser smoke | ACCEPT_BOUNDED |

## Findings / Position

| Boundary | Evidence | Decision consequence |
|---|---|---|
| Preview sandbox | The component specifies an empty sandbox token list on the `srcDoc` iframe. The HTML Standard describes restrictions on scripts and origin unless opt-in tokens re-enable them. | Markup intent is source-backed; actual browser enforcement for this panel has not been observed by the named tests. |
| Existing browser proof | B2c validates displayed version and downloaded bytes; Artifacts smoke validates visible output. Jsdom reads a string attribute. | None is an oracle for script execution or origin isolation in a real browser. |
| Meaningful negative control | A harmless inline script can set only an in-memory parent-page sentinel when run in an unsandboxed, same-origin `srcDoc` control frame. | A focused test should first show the sentinel flips in that control, then show it remains unset in the panel sandbox while benign heading content still renders. No network endpoint, credential or real artifact is involved. |
| Scope limit | An empty sandbox does not by itself prove all content is harmless; the HTML renderer, downloaded file and print window are different contexts. | The candidate claims only script blocking and opaque-origin behavior for one synthetic preview in tested Chromium; no global HTML safety, exfiltration, print/download or acceptance assertion. |
| B2 readiness | D037-D052 establish pure byte identity, synthetic download/route transport and receipt failure/timeout presentation, but no actor/store/writer/recovery authority. | Another fabricated `PRESENT` or synthetic ledger/store demonstration would not resolve the operator checkpoint. Durable B2 remains parked. |

## Decision / Disposition

`REVIEW_COMPLETE_BOUNDED`: Local may author a B1 browser-sandbox packet limited to one new focused Playwright spec, a secret-free proof JSON, a reference boundary and worker return. The browser test may intercept `/api/artifacts/export` with synthetic HTML containing benign content plus a harmless inline script sentinel; it must include an unsandboxed control proving the sentinel is executable and then verify that the actual panel iframe retains `sandbox=""`, renders benign content, does not execute that script and has an opaque origin in the tested Chromium profile. The test must forbid outgoing requests from the fixture and make no provider/governance claim. This audit does not authorize worker execution; a committed GC-018/work order and bound gate are required.

Do not open another B2 synthetic receipt success fixture, durable writer or acceptance route from this decision. Q001/Q004 and operator actor/store/effect choices remain open. Real print and screen-reader status announcement stay separate gaps and are not silently covered by sandbox proof.

## Risk / Corrective Action

The control frame must be isolated to an in-memory test page, removed after the assertion and incapable of sending network requests. A missing sandbox or script execution in the panel is a finding; worker must not edit production UI under this test-only packet. A successful test in one Chromium profile cannot certify other browsers, all iframe capabilities, sanitized export output, downloaded HTML execution, print-window behavior or accessibility. If the test fails, Local decides a separate repair work order.

## Finding-To-Governance Learning Disposition

| Defect class | Learning lane | Disposition | Next control action | Batch status |
|---|---|---|---|---|
| RUNTIME_SIGNAL_GAP: sandbox markup without a browser enforcement oracle | RUNTIME_BEHAVIOR_LEARNING | DESIGN_REVIEW_REQUIRED | Bound one synthetic Playwright proof with executable negative control | packet candidate |
| Durable B2 actor/store gap | DOCUMENTATION_ONLY_LEARNING | DEFER_WITH_REASON: D037/D038/Q001/Q004 require operator profile before effect | No synthetic receipt or writer successor by default | parked |

## Corpus Completeness And Report Integrity

- Corpus task class: AUDIT.
- Corpus root: four exact Web paths in the manifest below, not the whole Web package.
- Snapshot time: 2026-10-01; source read at HEAD `c8bc60b5f`.
- Enumeration command: `Get-ChildItem -LiteralPath <four exact Source Verification paths> -File`; `Get-FileHash -Algorithm SHA256` applied to each exact path.
- Manifest artifact or inline manifest: the four path/hash rows below.
- Manifest hash: N/A with reason: partial named-path audit uses per-file hashes, not a full-corpus manifest.
- Processing ledger artifact or inline ledger: all four rows below are READ.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=4; ledger_terminal=4; exclusions=0; unresolved=0 within these named paths.
- Unresolved files: 0 within exact list; broader Web paths are outside scope.
- Declared exclusions: all other Web paths and historical review context are not counted as scanned Web source.
- Unreadable or unsupported files: none within exact list.
- Aggregation check: PASS, four distinct paths.
- Drift check: PASS, hashes recomputed after source inspection with no intervening source edit.
- Output traceability: Source Verification, Findings and Decision tables above.
- Adversarial verification: contrasted attribute presence with browser execution and B2 transport evidence with acceptance authority.
- Corpus verdict: PARTIAL

| Path | SHA-256 | Terminal status |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `8602daf187444423c2575dee14898db19508e575224148c896dd235cd587451a` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | `7e3db63aa9744fbc63af0e22272c6ece6e0acea3adea73d8775145ba4416996e` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-byte-download.spec.ts` | `5034b443f0655f0a8e47e1a3f6b1aec0ef4718c6423825618bea87ad2a887b23` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-panel.spec.ts` | `7e8fc4cdd088a2142960fbfb7df4133d30956db325b5fdfc70c718a80aa9c0f3` | READ |

## Knowledge System Reconciliation

- Knowledge task class: named-path B1 preview sandbox gap audit.
- Source manifest: the four exact file/hash rows above.
- Source manifest hash: N/A with reason: partial named-path manifest uses per-file hashes.
- Enumeration safety: filesystem-backed `Get-ChildItem -LiteralPath` on the four exact paths; no broad listing is completeness evidence.
- Intake registry or ledger: `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b1-sandbox-scope-source.json`.
- Authority assets: four Web paths and governed B1/B2 reviews.
- Derived views: Source Verification, Findings and Decision in this audit.
- Semantic region ledger: component markup, jsdom preview, B2c browser preview and Artifacts smoke.
- Region reconciliation: assets=4; mapped=4; deferred=0; unmapped=0.
- Orphan or unmapped assets: 0 within exact scope.
- Cross-region links: B1 version binding and B2c content/bytes do not prove sandbox execution; D037-D052 do not supply B2 acceptance authority.
- Drift check: PASS, four hashes match source at HEAD `c8bc60b5f`.
- Rebuildability check: PASS by rehashing four named paths; no broader map claimed.
- Retrieval boundary: exact local source reads and official browser-standard context, no vector or external repository retrieval.
- Adversarial verification: a visible heading can coexist with a broken sandbox, and B2 transport can coexist with absent acceptance authority.
- Knowledge-map verdict: PARTIAL

## Epistemic Process Block

### Expected Result / Prediction

If browser sandbox enforcement had already been proven, a named Playwright spec would pair an executable control with a sandboxed panel frame and assert the script signal and origin behavior.

### Evidence Comparison

The inspected tests check preview content or string attributes and do not make that paired assertion. Component markup specifies an empty sandbox, while B2 actor/store decisions remain open.

### Contradiction Or Gap Disposition

No contradiction to the bounded markup claim. Browser enforcement is unproved in this named scope; a separate focused packet can resolve it without active governance or storage effects.

### Claim Update

Permit B1 sandbox packet authoring only. Keep durable B2, real actor/store/effect, `PRESENT` governance and Q001/Q004 exit parked.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Input type | internal governed input (no external intake) |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Internal source | `docs/reviews/CVF_CVF_NCR_HTML_B1_VERSION_BINDING_COMPLETION_2026-09-30.md` |
| Chain map route | Local source-derived owner comparison |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | External browser standard is not private CVF runtime proof |

## External/Local Coordination Binding

Role: Local source verifier. Phase: internal read-only audit. Decision owner: Local; effect owner: operator.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | `Corpus verdict: PARTIAL`; `Knowledge-map verdict: PARTIAL`; source ACCEPT rows; exact four-path manifest |
| gateRunPurpose | Confirm source-backed evidence after checker read-ahead; gates are not first discovery of browser behavior |
| claimBoundary | Static checks do not prove sandbox execution or select B2 acceptance authority |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local source verifier |
| Agent type | INTERNAL_AGENT reviewer |
| Invocation ID | cvf-ncr-html-b1-sandbox-scope-audit-20261001 |
| Provider or surface | private CVF source and official browser-standard read only |
| Session or invocation | B1 preview sandbox triage, 2026-10-01 |
| Working directory | repository root |
| Command or tool surface | exact source reads, `rg`, Git status and file hashing; no browser invocation |
| Target paths | this review, NCR roadmap D053, GC-051 entry/aggregate |
| Before status evidence | clean worktree at `c8bc60b5f` |
| After status evidence | exact four-path audit material set pending commit |
| Diff evidence | four-path source/registry/roadmap change set |
| Allowed scope source | active read-only post-B2f roadmap triage; Local technical decision delegation |
| Approval boundary | audit and packet-authoring recommendation only |
| Claim boundary | no browser proof yet, no B2 effect, provider/live, public sync or deployment |
| Expected manifest | `docs/reviews/CVF_CVF_NCR_HTML_B1_SANDBOX_SCOPE_AUDIT_2026-10-01.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b1-sandbox-scope-source.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |
| Actual changed set | `docs/reviews/CVF_CVF_NCR_HTML_B1_SANDBOX_SCOPE_AUDIT_2026-10-01.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b1-sandbox-scope-source.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | B1 preview sandbox source gap and no-effect packet candidate |
| claimDisposition | CLAIM_REJECTED: no browser sandbox behavior claimed before test |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no receipt created or inspected here |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no browser, route or provider action in audit |
| invocationBoundary | named source reads and official browser-standard context only |
| interceptionBoundary | proposed worker fixture may intercept export only; none in this audit |
| claimLanguage | markup intent and browser-test gap; B2 authority checkpoint persists |
| forbiddenExpansion | no actual evaluate/engine/provider, B2 writer, real data, artifact acceptance, public sync or deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This audit supports only a browser-sandbox proof packet candidate. It does not establish runtime enforcement, universal HTML safety, receipt validity, accessible announcement, print behavior, accepted artifact storage, Q001/Q004 exit or live effect.
