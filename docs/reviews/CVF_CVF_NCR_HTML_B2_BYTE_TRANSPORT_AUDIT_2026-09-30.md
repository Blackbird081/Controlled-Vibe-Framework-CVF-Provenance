# CVF NCR HTML B2 Byte Transport Audit

Memory class: governed-review

docType: review

Status: REVIEW_COMPLETE_BOUNDED

Date: 2026-09-30

providerExecutionAuthority: FORBIDDEN

## Purpose

Locate the exact-byte boundary between the HTML export route, browser consumer, and the isolated B2a identity helper before proposing any durable artifact acceptance.

## Target / Source

This Local source audit inspects the export route and route test, `ArtifactExportPanel` and its test, the isolated B2a helper, and its governed reference contract. The NCR roadmap D037-D039 and B2a completion establish the current scope. It is a named-path audit, not a complete repository inventory.

## Scope / Methodology

Startup acknowledged: current mode=`cvf_ncr_p10_closed_p11_parked`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=read-only HTML B2 byte-transport audit; role=Local source verifier; phase=internal source audit; technical decision owner=Local; effect decision owner=operator. Parked checkpoint: Q001/Q004 real data, accepting actor/store, backup/retention/RPO/RTO/cost, pilot/live, P11, public sync and deployment.

Local traced the value from request JSON through `buildHtml` and `NextResponse.json`, through browser `response.json`, then preview, clipboard, Blob download and print. The audit did not invoke a browser, provider, route, store or real artifact. Existing tests are interpreted at their actual mock/jsdom boundary. No network-wire or saved-file byte claim is inferred from source or a text roundtrip.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Route constructs HTML as a string and returns it inside JSON | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | `buildHtml`, `POST` return | `html`, `NextResponse.json` | export route | ACCEPT |
| Route `sourceHash` covers sourceContent, not rendered HTML | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | `POST` final block | `createHash('sha256').update(sourceContent)` | export route | ACCEPT |
| Consumer sends JSON, parses JSON and retains the returned HTML string in displayed result | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `handleGenerate` | `JSON.stringify`, `response.json`, `displayed` | browser panel | ACCEPT |
| Preview takes the string through sandboxed `srcDoc`; print writes it to a new document | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | output actions and preview | `srcDoc`, `document.write`, `print` | browser panel | ACCEPT |
| Copy passes the string to clipboard text API or legacy textarea; download creates a UTF-8-labelled Blob from the string | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `writeText`, `downloadHtml` | clipboard, `Blob([html])` | browser panel | ACCEPT |
| Existing panel test checks the same displayed string, Blob read-as-text, and mocked print calls | TEST_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | older-version output test | clipboard, `FileReader.readAsText`, mock `document.write` | jsdom test | ACCEPT_BOUNDED |
| Route test parses JSON and inspects HTML content, without a returned HTML byte digest | TEST_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.test.ts` | self-contained candidate test | `response.json`, `payload.data.html` | route test | ACCEPT_BOUNDED |
| B2a hashes UTF-8 bytes of the exact string supplied to it, and rejects lone surrogates | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.ts` | `utf8Bytes`, `computeHtmlBytesIdentity`, `verifyHtmlArtifactCandidate` | `Buffer.from(html, 'utf8')` | isolated B2a helper | ACCEPT |
| B2a is unconnected; future store protocol is proposal only | CONTRACT_BOUNDARY | `docs/reference/CVF_NCR_HTML_B2A_SYNTHETIC_ACCEPTANCE_CONTRACT_2026-09-30.md` | Parts 1 and 2 | synthetic identity and proposed store | B2a contract | ACCEPT |

## Findings / Position

| Boundary | Observed guarantee | Missing proof or owner |
|---|---|---|
| Route to browser | Route returns an HTML string in JSON; browser parses a string from JSON | No identity over the route's HTML value is emitted and independently verified after parsing. JSON wire bytes are an envelope, not the proposed artifact bytes. |
| Browser display | One `result.html` string feeds preview and actions; B1 version binding prevents an older result being silently presented as the edited form | `srcDoc` and print render a DOM; they are presentation paths, not byte-preserving artifact custody. Browser rendering has not been independently exercised here. |
| Clipboard | The selected string is passed to text clipboard methods | No byte-level verification of what an external paste destination stores. Clipboard is not an acceptance store. |
| Download | A Blob is constructed from the selected string with `text/html;charset=utf-8`; test reads Blob as text | No exact byte array/hash comparison or saved-file readback on a real browser. The MIME charset label alone is not proof of persisted bytes. |
| Candidate identity | B2a can hash and verify the UTF-8 bytes of a supplied, well-formed string | No caller binds the helper to route output, browser received value, Blob bytes, or a durable record. `sourceHash`, attempt ID and receipt ID cannot substitute for that binding. |

There are two distinct byte questions. The JSON HTTP response has transport bytes which may encode or escape the HTML string; those bytes are not the proposed HTML artifact identity. The proposed artifact identity is SHA-256 over UTF-8 bytes of the exact decoded HTML string chosen for custody. A future boundary must name where that string becomes bytes, carry an explicit byte length and digest, and verify the bytes actually handed to any writer. It must reject silent normalization, lone-surrogate substitution and re-rendering under the same identity.

## Decision / Disposition

`REVIEW_COMPLETE_BOUNDED`: B2a remains accepted only as a pure synthetic identity helper. This audit does not authorize route changes or durable acceptance. Local may prepare a separate, synthetic-only B2b work order for an in-memory string/byte handoff contract and deterministic JSON/Blob roundtrip tests, with a precise source-string versus byte-array owner and fail-closed mismatch checks. That packet may not claim actual network, clipboard, browser download, saved file, provider or durable-store proof. Integration of an accepting writer, real data, and any accept effect still requires the Q001/Q004 operator decisions.

## Risk / Corrective Action

Do not hash the JSON envelope, `sourceHash`, DOM serialization, or a regenerated packet and call it accepted HTML. A B2b test should compare the decoded result string's `TextEncoder` bytes to a separately held byte array and digest, include Unicode/newline and same-length mutation cases, and keep all state `DRAFT_UNACCEPTED`. Real-browser saved-file verification is a later bounded proof, distinct from synthetic transport tests and from durable acceptance.

## Finding-To-Governance Learning Disposition

| Defect class | Learning lane | Disposition | Next control action | Batch status |
|---|---|---|---|---|
| OPERATOR_SCOPE_CLARITY_GAP | DOCUMENTATION_ONLY_LEARNING | DESIGN_REVIEW_REQUIRED: B2 transport custody is undefined across the inspected route/browser path | Specify the first byte owner in a synthetic B2b contract before any durable writer packet | B2b design candidate only |
| Runtime/provider/cost learning | N/A_WITH_REASON | N/A_WITH_REASON: no runtime, provider or cost effect was exercised in this source audit | Reassess under a separately authorized proof plan | Parked |

## Epistemic Process Block

### Expected Result / Prediction

If the present path owned exact HTML bytes, a producer and consumer would compare an HTML-byte digest across their boundary and the tests would verify the handed-off bytes.

### Evidence Comparison

The route and browser exchange a JSON field of type string. The candidate helper is never called on that path. Existing tests check contents or text equality, with no independent byte digest or saved-byte readback.

### Contradiction Or Gap Disposition

No contradiction in the named source set. The missing join is an unimplemented boundary, not evidence that JSON necessarily changes the decoded string. Source inspection cannot establish real browser/network byte behavior.

### Claim Update

The next technically useful work is a synthetic byte-boundary contract, while durable B2 and Q001/Q004 effect remain parked.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `Purpose`; `Target / Source`; `Scope / Methodology`; `Findings / Position`; `Risk / Corrective Action`; `Claim Boundary`; `Agent Operation Trace Block`; `Public Export Disposition` |
| gateRunPurpose | Confirm this source-backed audit and its governed document shape; not first discovery |
| claimBoundary | Static gates do not prove transport or acceptance behavior |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local source verifier |
| Agent type | INTERNAL_AGENT reviewer |
| Invocation ID | cvf-ncr-html-b2-byte-transport-audit-20260930 |
| Provider or surface | private CVF repository, source inspection |
| Session or invocation | HTML B2 byte transport audit, 2026-09-30 |
| Working directory | repository root |
| Command or tool surface | `rg`, file reads and Git status |
| Target paths | this review and NCR roadmap decision D040 |
| Before status evidence | clean worktree at `5f3984ea4` |
| After status evidence | this review and roadmap decision pending material commit |
| Diff evidence | exact two-path audit material set |
| Allowed scope source | active B2a closure continuity explicitly allows read-only byte-transport audit |
| Approval boundary | source audit and next synthetic design only; operator retains data/effect choices |
| Claim boundary | no route mutation, store, provider/live, real data or accepted artifact |
| Expected manifest | `docs/reviews/CVF_CVF_NCR_HTML_B2_BYTE_TRANSPORT_AUDIT_2026-09-30.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Actual changed set | `docs/reviews/CVF_CVF_NCR_HTML_B2_BYTE_TRANSPORT_AUDIT_2026-09-30.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Input type | internal governed input (no external intake) |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Internal source | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Chain map route | Local source-derived owner correction |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | No external advisory is private CVF proof. |

## External/Local Coordination Binding

Role: Local source verifier; phase: internal B2 audit after external research ended; decision owner: Local for technical routing, operator for data and effect.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | bounded byte-transport source audit only |
| claimDisposition | CLAIM_REJECTED: no B2 runtime or acceptance behavior claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no receipt generated or inspected |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no route, browser, provider, store or artifact action occurred |
| invocationBoundary | source reads only |
| interceptionBoundary | no runtime gate claimed |
| claimLanguage | inspected path has no exact-byte handoff binding to B2a |
| forbiddenExpansion | no durable B2, Q001/R0 exit, Profile B/C, pilot/live, public sync or deployment |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This audit maps named source paths and identifies a synthetic next step. It does not prove network or saved-file bytes, establish an acceptance owner, accept an HTML artifact, close Q001/Q004, or authorize real data, provider/live, public sync or deployment.
