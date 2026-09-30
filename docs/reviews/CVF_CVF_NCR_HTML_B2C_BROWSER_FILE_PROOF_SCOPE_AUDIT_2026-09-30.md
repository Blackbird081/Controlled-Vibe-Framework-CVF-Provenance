# CVF NCR HTML B2c Browser/File Proof Scope Audit

Memory class: governed-review

docType: review

Status: REVIEW_COMPLETE_BOUNDED

Date: 2026-09-30

providerExecutionAuthority: FORBIDDEN

## Purpose

Decide whether a separately governed, synthetic real-browser download test can close the next byte boundary after the isolated B2b helper, without implying HTML artifact acceptance or a durable writer.

## Target / Source

This is a named-path Local audit of `ArtifactExportPanel.tsx`, its jsdom test, the existing Playwright Artifacts spec and mock config, the export route, and B2b's helper/reference/completion. It is not a complete Web-source inventory. The active next move allows source inspection only; this audit did not open a browser, download or read a file.

## Scope / Methodology

Startup acknowledged: current mode=`cvf_ncr_p10_closed_p11_parked`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=read-only B2c browser/file proof scope audit; role=Local source verifier; phase=internal audit; technical decision owner=Local; effect/data decision owner=operator. Parked checkpoint=Q001/Q004, real accepting actor/store, backup/key custody, retention, RPO/RTO, cost, pilot/live, P11, external runtime, public sync and deployment.

Local read the named source, test and contract paths at clean HEAD `a23090edb`. No code, browser, route, provider, store or artifact operation was executed. Existing tests are treated as evidence only for the surfaces they actually exercise. The two Playwright source paths receive a targeted, partial corpus-registry entry; this does not claim complete scan coverage. Web-agent research is advisory and not used as private-CVF proof; the shared-workspace worker remains an `INTERNAL_AGENT` for any later work order.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| The route places generated HTML in a JSON response; `sourceHash` hashes source content | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | `POST` final block | `sourceHash`, `html`, `NextResponse.json` | export route | ACCEPT |
| The panel stores the parsed result and B1 binds actions to its displayed version | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `handleGenerate`, `handleDownload`, preview | `setDisplayed`, `result.html`, `srcDoc` | browser panel | ACCEPT |
| Download constructs `Blob([html])`, clicks an anchor, and immediately revokes the object URL | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `downloadHtml` | `Blob`, `createObjectURL`, `anchor.click`, `revokeObjectURL` | browser download action | ACCEPT |
| Current panel test spies on Blob creation and anchor click, then reads Blob as text | TEST_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | older-version copy/download/print case | `createObjectURL`, `FileReader` | jsdom test | ACCEPT_BOUNDED |
| Current Playwright Artifacts spec intercepts export with a synthetic JSON fixture and checks preview/receipt text | TEST_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-panel.spec.ts` | English HTML review packet case | `page.route`, `login`, preview | browser test | ACCEPT_BOUNDED |
| Mock Playwright config launches the Web dev server with mock-AI flag | TEST_CONFIGURATION | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.mock.ts` | `webServer` | `NEXT_PUBLIC_CVF_MOCK_AI` | test harness | ACCEPT_BOUNDED |
| B2b hashes owned UTF-8 bytes in an unconnected Node helper | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-byte-handoff.ts` | `createHtmlByteHandoff`, `verifyHtmlByteHandoff` | `copyBytes`, `verifyHtmlByteHandoff` | B2b helper | ACCEPT |
| B2b Local review does not claim browser, saved-file or route binding | CONTRACT_BOUNDARY | `docs/reviews/CVF_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_COMPLETION_2026-09-30.md` | Findings, Claim Boundary | `ACCEPTED_BOUNDED` | B2b completion | ACCEPT |

## Findings / Position

| Boundary | Current evidence | Missing proof or decision |
|---|---|---|
| Version selected for download | B1 panel actions use `result.html` from the displayed result, including a stale-form notice in jsdom tests | No real-browser saved-file bytes for the displayed version |
| String to Blob | Component creates a UTF-8-labelled Blob from the displayed string | A mock Blob and `FileReader.readAsText` cannot prove downloaded file bytes, BOM fidelity or save completion |
| Browser download lifecycle | Existing Playwright spec drives the Artifacts page with a synthetic intercepted response | It does not await a download event, save/read the file or compare a digest; immediate object-URL revocation is an untested browser behavior, not an observed defect |
| Byte identity | B2b computes SHA-256 and length over in-memory owned bytes | The helper is Node-only and not imported by the panel; there is no production handoff or persisted acceptance identity |
| Preview, print, clipboard | Preview uses sandboxed `srcDoc`; print writes a DOM document; clipboard writes text | These are separate presentation/text boundaries and cannot be closed by a download-file test |

The first useful B2c proof is a synthetic browser download from the existing panel. A later packet can intercept the export endpoint with an exact synthetic HTML fixture, choose a known displayed version, wait for the real browser download, read back the saved bytes in a disposable test location, and compare length and SHA-256 to an independently computed oracle and the B2b identity for that fixture. Include a same-length changed-title fixture and BOM/newline/Unicode cases so text roundtrips cannot hide a byte difference. The browser test should make zero provider calls and assert no governance decision behavior; the fixture's receipt fields are display inputs only. Any route, panel or download-lifecycle repair requires a named, bounded allowance and a failing browser observation first.

This proof would establish only the browser's saved bytes for synthetic fixture output on the tested browser/profile. It would not establish production network transport, user-selected file destination durability, all browsers, printing, clipboard, store authority, or accepted artifact status. The current panel's `Blob([html])` and the Node-only B2b helper must not be described as already integrated.

## Decision / Disposition

`REVIEW_COMPLETE_BOUNDED`: a separate B2c synthetic browser-download proof packet is technically justified. Authoring may use the existing Playwright Artifacts spec and mock config as the test harness, with a new focused spec or an exact bounded addition. No browser/file execution or UI edit is authorized by this audit itself. The work order must keep provider and governance-behavior claims out of mock mode, define disposable file custody and cleanup, and require Local independent review of the actual saved-byte digest. Q001/Q004 remain open and no durable B2 or artifact acceptance follows.

## Risk / Corrective Action

Treat a missing download, a mismatched digest, or a wrong version as a finding, not as a reason to weaken the oracle or switch to text readback. The packet should permit only a focused, evidence-triggered repair of the panel download action if the browser proves the existing implementation fails. Keep print/clipboard, real route/proxy bytes, production data, accepting actor/store, backup and cost outside that packet. Do not infer `sourceHash` authenticates HTML bytes.

## Finding-To-Governance Learning Disposition

| Defect class | Learning lane | Disposition | Next control action | Batch status |
|---|---|---|---|---|
| RUNTIME_SIGNAL_GAP: browser-saved byte proof absent | DOCUMENTATION_ONLY_LEARNING | DESIGN_REVIEW_REQUIRED: current tests stop at mock Blob text or preview | Bound a synthetic Playwright download-file probe in a separate packet | Packet candidate |
| Runtime/provider/cost learning | N/A_WITH_REASON | N/A_WITH_REASON: this source audit executed no browser, provider or cost effect | Reassess from future measured test evidence | Parked |

## Corpus Completeness And Report Integrity

- Corpus task class: AUDIT
- Corpus root: explicit bounded list of the two Playwright files in the inline manifest below; no complete Web corpus claim.
- Snapshot time: 2026-09-30 13:06:25 UTC
- Enumeration command: `Get-ChildItem -LiteralPath 'EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.mock.ts','EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-panel.spec.ts' -File`
- Manifest artifact or inline manifest: the two file rows below.
- Manifest hash: N/A with reason: this is a two-file partial source audit; per-file SHA-256 values are recorded inline and no complete-corpus manifest is asserted.
- Processing ledger artifact or inline ledger: the two READ rows below.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=2; ledger_terminal=2; exclusions=0; unresolved=0
- Unresolved files: 0 within this exact two-file list; broader Web source coverage is outside this audit.
- Declared exclusions: none within the exact two-file list; other Web files are outside the bounded list, not silently counted.
- Unreadable or unsupported files: none within the exact two-file list.
- Aggregation check: PASS, one mock config plus one spec equals two TypeScript files.
- Drift check: PASS, both per-file hashes recomputed after source inspection with no intervening file edit.
- Output traceability: Source Verification Block rows for mock config and existing Artifacts Playwright spec.
- Adversarial verification: independently compared the existing spec's assertions to its absence of download event/file-byte assertions; no real browser execution.
- Corpus verdict: PARTIAL - only the named Playwright files were registered; no extension-wide completeness claim.

| Exact file | SHA-256 | Ledger status |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/playwright.config.mock.ts` | `704c9b4fcfa8a248a9e4fb82b49af184ee6840ccf60b44909d142fc7f61ff712` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-panel.spec.ts` | `7e8fc4cdd088a2142960fbfb7df4133d30956db325b5fdfc70c718a80aa9c0f3` | READ |

## Epistemic Process Block

### Expected Result / Prediction

If the current test evidence proved browser-saved bytes, a real-browser test would capture a download and compare the saved byte array with an independent digest for the displayed HTML version.

### Evidence Comparison

The jsdom case reads Blob as text and mocks anchor click. The Playwright case checks preview and receipt text but not download bytes. B2b is an unconnected Node helper. Thus the named evidence does not meet the saved-byte prediction.

### Contradiction Or Gap Disposition

No observed browser failure is claimed. The immediate URL revocation is a target for a future discriminating test. The gap is missing proof, and any implementation repair must follow a failing browser observation within a separately bounded packet.

### Claim Update

Authorize packet authoring for synthetic browser-file proof only. Preserve B2b's in-memory claim and all open effect decisions.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `Purpose`; `Target / Source`; `Scope / Methodology`; `Source Verification Block`; `Findings / Position`; `Risk / Corrective Action`; `Claim Boundary`; `Agent Operation Trace Block`; `Public Export Disposition` |
| gateRunPurpose | Confirm this source-backed named-path audit and governed document shape after semantic review; not first discovery |
| claimBoundary | Static gates do not prove real-browser saved bytes or acceptance behavior |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local source verifier |
| Agent type | INTERNAL_AGENT reviewer |
| Invocation ID | cvf-ncr-html-b2c-scope-audit-20260930 |
| Provider or surface | private CVF repository, source inspection |
| Session or invocation | HTML B2c scope audit, 2026-09-30 |
| Working directory | repository root |
| Command or tool surface | `rg`, named file reads and Git status |
| Target paths | this audit, NCR roadmap D043, the targeted corpus-registry source entry and generated aggregate |
| Before status evidence | clean worktree at `a23090edb` |
| After status evidence | audit, roadmap, registry source and generated aggregate pending material commit |
| Diff evidence | exact four-path audit material set |
| Allowed scope source | active B2b completion continuity permits read-only B2c scope audit |
| Approval boundary | source audit and packet-authoring decision only; operator retains real data/effect choices |
| Claim boundary | no browser/file action, route/UI/store mutation, provider/live or artifact acceptance |
| Expected manifest | `docs/reviews/CVF_CVF_NCR_HTML_B2C_BROWSER_FILE_PROOF_SCOPE_AUDIT_2026-09-30.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b2c-browser-proof-scope-source.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |
| Actual changed set | `docs/reviews/CVF_CVF_NCR_HTML_B2C_BROWSER_FILE_PROOF_SCOPE_AUDIT_2026-09-30.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b2c-browser-proof-scope-source.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Input type | internal governed input (no external intake) |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Internal source | `docs/reviews/CVF_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_COMPLETION_2026-09-30.md` |
| Chain map route | Local source-derived owner correction |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | No Web-agent advisory is private CVF proof. |

## External/Local Coordination Binding

Role: Local source verifier; phase: internal B2c scope audit; decision owner: Local for technical routing, operator for data and effect.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | named-path B2c browser-file proof scope audit only |
| claimDisposition | CLAIM_REJECTED: no browser-file runtime behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no receipt was generated or validated |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no browser, file, route, provider or store action occurred |
| invocationBoundary | source reads only |
| interceptionBoundary | no runtime gate claimed |
| claimLanguage | existing tests do not prove saved download bytes |
| forbiddenExpansion | no durable B2, Q001/Q004 exit, Profile B/C, pilot/live, public sync or deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This audit supports authoring a separate synthetic browser-file proof packet. It does not prove downloaded bytes, establish an accepting actor/store, accept an HTML artifact, close Q001/Q004, or authorize real data, provider/live, public sync or deployment.
