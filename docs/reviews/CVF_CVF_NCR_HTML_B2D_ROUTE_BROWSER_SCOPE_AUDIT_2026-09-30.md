# CVF NCR HTML B2d Route-to-Browser Scope Audit

Memory class: governed-review

docType: review

Status: REVIEW_COMPLETE_BOUNDED

Date: 2026-09-30

providerExecutionAuthority: FORBIDDEN

## Purpose

Decide the next proof boundary after B2c showed exact saved-file bytes for an intercepted synthetic export response. The question is whether a bounded browser test can consume the actual HTML export route without allowing its optional server-side governance receipt hop to run.

## Target / Source

This is a named-path audit of the export route, its receipt helper and unit test, and the route authorization helper. B2c completion, panel source and Playwright mock config are current context. The four new source paths have a targeted GC-051 entry. No complete Web corpus claim is made.

## Scope / Methodology

Startup acknowledged: current mode=`cvf_ncr_p10_closed_p11_parked`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=read-only B2d route/browser byte audit; role=Local source verifier; phase=internal audit; technical decision owner=Local; effect/data decision owner=operator. Parked checkpoint=Q001/Q004, real accepting actor/store, data, backup/key custody, retention, RPO/RTO, cost, pilot/live, P11, public sync and deployment.

Local read the named route/proof/auth/test sources at clean HEAD `336128f22`. No route, browser, provider, store or artifact operation was executed during this audit. The prior B2c browser run is accepted only for its intercepted synthetic response. A shared-workspace worker remains `INTERNAL_AGENT`; Web-agent research is advisory, not private-CVF verification.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Route authorizes request, validates fields, builds HTML and places it inside JSON | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | `POST` | `authorizeRouteGovernanceProof`, `buildHtml`, `NextResponse.json` | export route | ACCEPT |
| `sourceHash` covers `sourceContent`, not exact rendered HTML bytes | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | final `POST` block | `createHash('sha256').update(sourceContent)` | export route | ACCEPT |
| The route calls a receipt helper before returning JSON | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | final `POST` block | `fetchGovernanceReceipt` | export route | ACCEPT |
| Receipt helper returns `NOT_CONFIGURED` if no absolute URL can be resolved; `NEXTAUTH_URL` can make the evaluate URL absolute and trigger server-side fetch | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` | `resolveEvaluateUrl`, `fetchGovernanceReceipt` | `NEXTAUTH_URL`, `/api/governance/evaluate`, `fetch` | receipt helper | ACCEPT |
| Route authorization accepts a valid signed service token or verified session and emits proof | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | `authorizeRouteGovernanceProof` | `verifyServiceTokenRequest`, `verifySessionCookie` | route auth helper | ACCEPT |
| Unit tests call `POST` directly and stub server `fetch` in receipt cases | TEST_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.test.ts` | receipt cases | `vi.stubGlobal('fetch', ...)` | route unit test | ACCEPT_BOUNDED |
| B2c intercepts export with `page.route`, never reaching the real handler | TEST_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-byte-download.spec.ts` | synthetic route fulfillment | `page.route('**/api/artifacts/export')` | B2c browser spec | ACCEPT_BOUNDED |

## Findings / Position

| Boundary | Current evidence | Remaining gap |
|---|---|---|
| Route to browser | Route builds an HTML string and returns JSON; panel parses `response.json` and displays the returned string | No integrated browser/download readback of an un-intercepted route result and its exact decoded HTML bytes |
| Receipt hop | `fetchGovernanceReceipt` can make a server-side fetch if `NEXTAUTH_URL` exists | `page.route` cannot isolate this server-side hop; a B2d test must prove it is disabled or captured before invoking the real route |
| Source versus artifact identity | `sourceHash` is over source content; B2b/B2c identity is over rendered HTML bytes | Do not equate `sourceHash`, JSON wire bytes and HTML artifact bytes |
| Route unit tests | Synthetic `POST` tests validate output and stub server fetch | They do not observe a browser's saved file after the real route responds |
| B2c | Synthetic intercepted response was downloaded byte-exact in Chromium | It did not execute the real export route or prove its receipt branch safe in a browser test |

The next technically useful slice is a synthetic route-to-browser byte proof with an explicit no-hop test environment. A packet must make the receipt helper return `NOT_CONFIGURED` by construction, verify that status in the response and independently establish zero server-side evaluate/provider calls. It must use only synthetic request fields and keep the result unaccepted. If the environment cannot prove that isolation, return blocked rather than run the route. A browser-side intercept of `/api/artifacts/export` would defeat the purpose; a browser-side intercept of `/api/governance/evaluate` alone would not control the server-side helper.

This audit does not decide the exact harness or authorize its execution. It permits Local to author a separate GC-018/work order that restricts changes to test-only paths and requires a preflight isolation proof. Production route, panel, auth, receipt helper, config, store and data files remain read-only. Any proposal to edit a production seam needs a separate reviewed amendment and evidence of necessity.

## Decision / Disposition

`REVIEW_COMPLETE_BOUNDED`: B2d packet authoring may proceed for a synthetic no-hop real-route/browser saved-byte proof. The work order must fail closed if `NEXTAUTH_URL` resolution can trigger `fetchGovernanceReceipt`, and must distinguish route HTML bytes from JSON envelope and `sourceHash`. No B2d implementation, provider/live, real data, artifact acceptance or durable B2 is authorized by this audit. Q001/Q004 remain open.

## Risk / Corrective Action

Do not infer that `NEXT_PUBLIC_CVF_MOCK_AI=1` disables the receipt helper; the audited helper checks `NEXTAUTH_URL`. Do not rely on page-level network interception for a server-side fetch. Preserve the optional receipt attempt's observed status without claiming governance behavior. If no safe no-hop harness is available, keep B2d at `BLOCKED_WITH_REASON` and revisit the design; do not silently invoke the evaluate route.

## Finding-To-Governance Learning Disposition

| Defect class | Learning lane | Disposition | Next control action | Batch status |
|---|---|---|---|---|
| RUNTIME_SIGNAL_GAP: server receipt-hop isolation absent from B2c | DOCUMENTATION_ONLY_LEARNING | DESIGN_REVIEW_REQUIRED | Specify fail-closed no-hop proof in B2d packet before any real-route browser test | Packet candidate |
| Runtime/provider/cost learning | N/A_WITH_REASON | N/A_WITH_REASON: this source audit invoked no route or provider | Reassess only from separately authorized execution evidence | Parked |

## Corpus Completeness And Report Integrity

- Corpus task class: AUDIT
- Corpus root: exact four-file source list below; no complete Web corpus claim.
- Snapshot time: 2026-09-30; source read at HEAD `336128f22`.
- Enumeration command: `Get-ChildItem -LiteralPath 'EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts','EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts','EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.test.ts','EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts' -File`.
- Manifest artifact or inline manifest: four exact source paths and hashes below.
- Manifest hash: N/A with reason: a four-file partial source audit records per-file SHA-256, not a complete-corpus manifest hash.
- Processing ledger artifact or inline ledger: all four rows are READ.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=4; ledger_terminal=4; exclusions=0; unresolved=0.
- Unresolved files: 0 within this exact four-file list; broader Web coverage is outside the audit.
- Declared exclusions: other Web source files are outside this bounded list, not counted as scanned.
- Unreadable or unsupported files: none within the four-file list.
- Aggregation check: PASS, four distinct TypeScript paths.
- Drift check: PASS, per-file SHA-256 recomputed after source inspection with no intervening edit.
- Output traceability: Source Verification rows above; B2c context is cited separately.
- Adversarial verification: contrasted the B2c `page.route` intercept with the server-side receipt helper and confirmed that a page intercept cannot establish no server fetch; no network action was performed.
- Corpus verdict: PARTIAL - only four named route/proof/auth/test sources are registered; no extension-wide completeness claim.

| Path | SHA-256 | Terminal status |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | `6b988ba687b9b1478f097ca81c3e1235aa20ef819106c050279779da00781c3c` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` | `fbdcc3a434eea13842c9f692d2b54cc9955e80d8c8777d9dfaa14cace9cdfcaf` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.test.ts` | `09c64901b1fd2500806493f0db11dfb5c810cc64e63aed2891d97aa4f5835eab` | READ |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts` | `17c19ccc4e31d5e068b728304e4a0970ddc072a9711460dd62b859f3ade15b6e` | READ |

## Knowledge System Reconciliation

- Knowledge task class: named-path route/browser ownership audit.
- Source manifest: the four exact file/hash rows above.
- Source manifest hash: N/A with reason: this partial audit uses per-file SHA-256, not a complete-corpus manifest.
- Enumeration safety: exact-path filesystem reads only; no broad listing is treated as completeness evidence.
- Intake registry or ledger: `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b2d-route-browser-scope-source.json`.
- Authority assets: B2c completion, NCR roadmap D045, the four current source paths and active continuity.
- Derived views: Source Verification and Findings / Position tables in this audit.
- Semantic region ledger: route JSON output, optional receipt hop, route session authorization and route unit test.
- Region reconciliation: assets=4; mapped=4; deferred=0; unmapped=0 within the named list.
- Orphan or unmapped assets: 0 within the four-file list.
- Cross-region links: B2c browser test is a prior intercepted-response proof, not an integrated route/browser proof.
- Drift check: PASS, four per-file SHA-256 values match the source at HEAD `336128f22`.
- Rebuildability check: PASS for the four path/hash rows by rehashing those exact files; no broader map is claimed.
- Retrieval boundary: no external or vector retrieval; this audit answers only the named route/browser isolation question.
- Adversarial verification: source comparison showed that page-level intercept cannot control `proof.ts` server-side fetch.
- Knowledge-map verdict: PARTIAL

## Epistemic Process Block

### Expected Result / Prediction

If B2c already proved un-intercepted route-to-browser bytes safely, the browser spec would reach `POST` while its server receipt branch was explicitly isolated and measured.

### Evidence Comparison

B2c intercepts the export response. The route calls `fetchGovernanceReceipt`, and the helper may fetch an absolute evaluate URL based on `NEXTAUTH_URL`. The route unit test isolates `fetch` in process but no current browser test joins these boundaries.

### Contradiction Or Gap Disposition

The route/browser integration claim remains unproven. The optional server-side receipt call is a concrete execution hazard for a browser test; it is not evidence of an observed call in this audit.

### Claim Update

Authorize only design of a no-hop synthetic B2d packet. Keep execution, governance, acceptance and durable-effect claims closed.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py`; `governance/compat/check_corpus_scan_registry.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | `Corpus verdict: PARTIAL`; `Knowledge System Reconciliation`; `REVIEW_COMPLETE_BOUNDED`; exact four-path registry scope |
| gateRunPurpose | Confirm the bounded named-path audit and registry projection without whole-corpus claim |
| claimBoundary | Static gates cannot prove no-hop runtime isolation or browser transport bytes |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local source verifier |
| Agent type | INTERNAL_AGENT reviewer |
| Invocation ID | cvf-ncr-html-b2d-scope-audit-20260930 |
| Provider or surface | private CVF workspace, read-only source inspection |
| Session or invocation | B2d route/browser scope audit, 2026-09-30 |
| Working directory | private CVF repository |
| Command or tool surface | ripgrep, named reads/hashes, GC-051 generator and governance gates |
| Target paths | audit, NCR roadmap, GC-051 source entry and generated aggregate |
| Before status evidence | clean HEAD `336128f22` after B2c closure |
| After status evidence | four bounded audit material paths pending Local commit |
| Diff evidence | exact audit material set against `336128f22` |
| Allowed scope source | B2c D045 successor audit permission and delegated Local technical decision |
| Approval boundary | B2d packet authoring decision only |
| Claim boundary | no browser/route execution or Q001/Q004 exit |
| Expected manifest | `docs/reviews/CVF_CVF_NCR_HTML_B2D_ROUTE_BROWSER_SCOPE_AUDIT_2026-09-30.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b2d-route-browser-scope-source.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |
| Actual changed set | `docs/reviews/CVF_CVF_NCR_HTML_B2D_ROUTE_BROWSER_SCOPE_AUDIT_2026-09-30.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b2d-route-browser-scope-source.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Input type | internal governed input (no external intake) |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Internal source | `docs/reviews/CVF_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_COMPLETION_2026-09-30.md` |
| Chain map route | Local source-derived owner decision |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | No Web advisory is private CVF proof. |

## External/Local Coordination Binding

Role: Local source verifier; phase: read-only B2d audit; decision owner: Local.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | read-only B2d route/browser byte boundary |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: exact source inspection only |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no new governance receipt used |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no route/browser action executed |
| invocationBoundary | local source reads and hashes only |
| interceptionBoundary | no runtime interception claimed |
| claimLanguage | optional server receipt hop must be isolated before real-route synthetic browser proof |
| forbiddenExpansion | provider, real data, store, artifact acceptance, public sync, deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This audit establishes a test design constraint, not a running route/browser proof. It does not authorize provider calls, real data, accepted artifacts, durable B2, Q001/Q004 exit, P11, public sync or deployment.
