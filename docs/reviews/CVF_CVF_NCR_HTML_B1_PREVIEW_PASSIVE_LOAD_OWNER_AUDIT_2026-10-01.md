# CVF NCR HTML B1 Preview Passive Loads - Local Owner Audit

Memory class: governed-review

docType: review

Status: REVIEW_COMPLETE_NO_DISPATCH

Date: 2026-10-01

providerExecutionAuthority: FORBIDDEN

## Purpose

Resolve PREVIEW_PASSIVE_RESOURCE_LOADS to its existing source owner, current reachability and next packet boundary. Audit only; no source implementation, browser rerun, provider invocation or worker release.

## Target / Source

Clean audit base `abcf1f1679ba57e68455790c63b3a4ae2a2e79d9`. Next allowed move from active continuity is READ_ONLY_PREVIEW_PASSIVE_LOAD_OWNER_AUDIT. Prior decision: `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_COMPLETENESS_R2_COMPLETION_2026-10-01.md`, material `6251ca305`; current R2 proof is reused without recreating its browser run.

## Scope / Methodology

Startup acknowledged: mode=cvf_ncr_p10_closed_p11_parked; active handoff=AGENT_HANDOFF_V63_2026-09-18.md; next=preview passive-load owner audit; role=Local orchestrator/reviewer; phase=read-only audit; decision owner=Local; effect owner=operator; parked=Q001/Q004, durable B2, P11, real actor/data/store/effect, public sync and deployment. Shared-workspace workers are INTERNAL_AGENT; external research remains advisory and none was opened.

Read selected sections of the eight inline-manifest paths below, trace response-to-iframe input and current consumer invocations, and compare the existing synthetic script/origin spec and accepted Print binding. Source-read work is bounded to this owner question. No repository-wide inventory, absence or all-files-read claim.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Preview sink and input seams | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | ArtifactExportPanelProps; handleGenerate; Preview iframe | result.html -> srcDoc; initialResult/exportEndpoint | ArtifactExportPanel | ACCEPT |
| Default HTML producer | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | escapeHtml; renderInline/renderMarkdownLite; buildHtml; POST | escaped fields and inline CSS; returned html | export route | ACCEPT |
| Artifacts consumer | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/artifacts/page.tsx` | ArtifactExportPanel invocation | initialRequest only | Artifacts page | ACCEPT |
| Work-transfer consumer | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx` | ArtifactExportPanel invocation | initialRequest only | Work-transfer page | ACCEPT |
| Named configured response headers | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/next.config.ts` | securityHeaders; headers | no Content-Security-Policy entry in inspected array | Next config | ACCEPT |
| Existing synthetic script/origin proof | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts` | FIXTURE_HTML; control and actual frame assertions | fixture has script, no passive resource reference | B1 preview spec | ACCEPT |
| Current Print coupling | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts` | displayedHtml; printedPayloadEqualsDisplayed | raw Preview srcdoc equals printed payload assertion | Print regression | ACCEPT |
| Observed preview resource requests | `docs/reviews/evidence/cvf-ncr-html-b1-print-r2-local-probe-2026-10-01.json` | observations.print.previewEndpointHits; endpointHits | previewEndpointHits; endpointHits | Local bounded evidence | ACCEPT |

## Findings / Position

1. Existing owner is the Preview iframe in ArtifactExportPanel. It renders result.html directly as srcDoc with sandbox empty and no Preview-specific resource policy in the inspected component. The response JSON is admitted on success/data presence, then displayed. initialResult and exportEndpoint are component input seams, not newly authorized external integrations.
2. Current default route escapes all dynamic field text and uses escape-first inline/Markdown-lite rendering; its fixed HTML template supplies inline CSS. The two observed production component invocations supply initialRequest only and use that default endpoint. Thus the synthetic HTML response demonstrates sink behavior, not raw user-source markup injection through the current default producer. No actual production data exposure is established.
3. Existing Local Chromium evidence observed one intercepted image and one intercepted stylesheet request before Print. The printed surface later recorded zero such endpoint hits with its own CSP. Sandbox script/origin isolation and passive resource prohibition are different guarantees; the former does not close this finding. Cookie transmission, production endpoint authorization effects, external destination behavior and production proxy headers were not measured by this audit.
4. The old Preview spec contains no resource-bearing fixture. It proves a harmless script executes in its control and is blocked in the actual sandbox; it cannot prove that a passive-resource policy exists. The inspected Next header array contains no CSP entry; this is a statement about that named source, not all deployments or header producers.
5. Print and Preview must remain separate render contexts. Print's test currently equates printed payload to raw Preview srcdoc. A Preview policy wrapper may change render bytes while canonical result.html must remain the source for copy, download and Print. A future packet must own this dependency and bind displayed content/version to canonical result provenance; it must not simply remove or weaken the stale-version assertion.

## Owner / Overlap Disposition

ADAPT_EXISTING_OWNER: harden the Preview renderer boundary inside ArtifactExportPanel rather than create a new framework, global sanitizer or durable acceptance owner. The intended outcome is an isolated, self-contained preview that denies passive network resources before payload parsing, keeps inline presentation/benign content, and preserves accepted script/origin isolation. No implementation mechanism is approved by this audit.

Default route escaping is existing mitigation, not a substitute for a sink-level contract across component input seams. A route-only change would leave the renderer contract conditional on every producer; a global CSP/config change would widen the affected app surface. Both are outside the proposed narrow lane.

## Decision / Disposition

REVIEW_COMPLETE_NO_DISPATCH. Local may next AUTHOR a distinct bounded Preview passive-resource packet under existing owners. This is a separate Preview concern, not a successor of the stopped Print problem chain. No worker execution is authorized until paired GC-018/work order, manifest/closeability, material/continuity binding and release gates pass.

The packet must cover the complete known dependency set in one assignment:

- actual Preview before any Print click, with executable resource-positive control, zero negative resource hits, and policy-removal mutation that restores hits;
- both same-origin controlled endpoints and intercepted off-origin synthetic destinations, including image, stylesheet/CSS import/font and nested-frame/resource paths relevant to the selected policy; no real outbound forwarding;
- opaque origin, empty sandbox, blocked payload script and benign inline rendering; define permitted data resources explicitly and prove any claimed support;
- preservation of canonical result.html for copy/download/Print and displayed-version binding after unsaved edits, latest-response supersession and initialResult provenance;
- focused existing Preview and Print specs plus unit/type/lint evidence, with distinct Local reviewer probe and no blanket same-origin request exemption;
- zero changes to route/auth/config/package/ledger/storage/governance/continuity by worker; no credentials, provider/live, real data, public sync or deployment.

The prospective manifest must include ArtifactExportPanel, its unit test, the existing Preview spec AND the existing Print spec, together with task-specific proof/return outputs. Reuse registered browser paths and plan all proof-artifact ownership before dispatch. Do not overwrite historical accepted sandbox or Print proof artifacts. If a coherent policy requires forbidden paths, return the design conflict to Local instead of expanding scope.

## Risk / Corrective Action

A policy injected after untrusted markup parses cannot undo earlier loads; deny-before-payload ordering is a required future observable outcome. A transformed Preview render document must be distinguished from the canonical HTML result without changing downloadable/source bytes or falsely displaying a newer form version. Merely adding a policy string, passing jsdom attributes or counting zero requests with an inert positive control is insufficient.

No incident, universal HTML safety or real governance assurance is claimed. Q001/Q004 and durable B2 remain open. Print R2 acceptance and its 700px/renderer-only limits remain intact.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | Preview owner and future bounded packet | source-only owner decision, no execution grant | named source/evidence above | existing Web component | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | no interface opened | no ingress/credential/mutation grant | internal-only audit | adapter deferred | DEFERRED_WITH_REASON |

## Corpus Completeness And Report Integrity

- Corpus task class: AUDIT, eight named paths with selected-section read depth.
- Corpus root: private CVF repository at audit base.
- Snapshot time: 2026-10-01, audit source HEAD above.
- Enumeration command: filesystem-backed Python Path.is_file/Path.read_bytes on the eight explicit paths; SHA-256, no whole-repo enumeration.
- Manifest artifact or inline manifest: inline JSON below; processing ledger uses terminalStatus plus explicit readDepth/sections.
- Manifest hash: `c24ae59b5f9f4e7dae2d5cea4e59a3130e7e22545b363237c559bd130e3ca0ad` (compact sorted-key UTF-8 JSON).
- Processing ledger artifact or inline ledger: inline manifest terminalStatus/readDepth/sections fields.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE. All eight rows READ at SELECTED_SECTIONS depth.
- Reconciliation: manifest=8; ledger_terminal=8; exclusions=0; unresolved=0. Counts cover the eight explicit paths only.
- Unresolved files: no missing named source; unexamined regions remain outside semantic claim.
- Declared exclusions: other paths, unselected sections, production headers/endpoints/data, runtime experiments and physical-output contexts.
- Unreadable or unsupported files: none in named byte-hash manifest.
- Aggregation check: manifest length and unique path count both 8; every row has SHA-256 and section ledger.
- Drift check: sources hashed at clean audit base; only review and roadmap authored; product sources not changed.
- Output traceability: Source Verification, Findings and Decision above.
- Adversarial verification: existing executable controls and mutations consumed within their limits; new resource classes require future packet proof.
- Corpus verdict: PARTIAL

```json
[{"path":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx","sha256":"4b90fa59d4ba6d5c28f51e963d1d183e8f2b93c6b16d134b2bc4e7ffbb715f9a","terminalStatus":"READ","readDepth":"SELECTED_SECTIONS","sections":"ArtifactExportPanelProps; handleGenerate; Preview iframe"},{"path":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts","sha256":"6b988ba687b9b1478f097ca81c3e1235aa20ef819106c050279779da00781c3c","terminalStatus":"READ","readDepth":"SELECTED_SECTIONS","sections":"escapeHtml; renderInline/renderMarkdownLite; buildHtml; POST"},{"path":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/artifacts/page.tsx","sha256":"651652d7ce7757503ca3126bba03889e9286152d4e788e181970a56dfe18b0ec","terminalStatus":"READ","readDepth":"SELECTED_SECTIONS","sections":"ArtifactExportPanel invocation"},{"path":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx","sha256":"a6c6f6ef3738538f982833bc282275be845905b5cabadd3011feddc6890e56a8","terminalStatus":"READ","readDepth":"SELECTED_SECTIONS","sections":"ArtifactExportPanel invocation"},{"path":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/next.config.ts","sha256":"9eb210167c1cb82f5320823f94735691e68fd42cc8b0c60a429610c00bbca992","terminalStatus":"READ","readDepth":"SELECTED_SECTIONS","sections":"securityHeaders; headers"},{"path":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts","sha256":"1ad62af6a0e8dee386ffee7f1b4ec1518f582c3cf08eb033d2bca511fa093651","terminalStatus":"READ","readDepth":"SELECTED_SECTIONS","sections":"FIXTURE_HTML; control and actual frame assertions"},{"path":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts","sha256":"78f9c5e52af274f97f0731147050d9c6a677167ac00693999ecf5f4a70b17731","terminalStatus":"READ","readDepth":"SELECTED_SECTIONS","sections":"displayedHtml; printedPayloadEqualsDisplayed"},{"path":"docs/reviews/evidence/cvf-ncr-html-b1-print-r2-local-probe-2026-10-01.json","sha256":"03a715ba5ec03869cb1b6e09acfae7f508b9811e377f833e6ef5527615b9361f","terminalStatus":"READ","readDepth":"SELECTED_SECTIONS","sections":"observations.print.previewEndpointHits; endpointHits"}]
```

## Knowledge System Reconciliation

- Knowledge task class: bounded source owner audit.
- Source manifest: eight-row inline JSON in Corpus Completeness And Report Integrity.
- Source manifest hash: c24ae59b5f9f4e7dae2d5cea4e59a3130e7e22545b363237c559bd130e3ca0ad.
- Enumeration safety: filesystem-backed Python Path.is_file/Path.read_bytes on eight explicit paths.
- Intake registry or ledger: inline terminalStatus/readDepth/sections ledger.
- Authority assets: existing Preview component, producer, two consumers, config, two specs and prior Local evidence.
- Derived views: this audit and roadmap D063; source-audited candidate only.
- Semantic region ledger: eight named selected regions mapped to Source Verification and Findings; unselected sections outside claim.
- Region reconciliation: assets=8; mapped=8; deferred=0; unmapped=0.
- Orphan or unmapped assets: none within explicit manifest; no wider coverage claim.
- Cross-region links: producer/consumer reachability to Preview sink and browser evidence; Print identity dependency.
- Drift check: byte hashes at audit base; product sources unchanged.
- Rebuildability check: named paths, section ledger and source hashes permit reconstruction of bounded audit.
- Retrieval boundary: eight explicit paths and selected sections; no whole-repository semantic coverage.
- Adversarial verification: prior synthetic request observations consumed; future policy needs independent controls and mutation proof.
- Knowledge-map verdict: PARTIAL

## Finding-To-Governance Learning Disposition

| Defect class | Learning lane | Disposition | Next control action | Batch status |
|---|---|---|---|---|
| RUNTIME_SIGNAL_GAP: Preview passive loads outside script/origin proof | RUNTIME_BEHAVIOR_LEARNING | DESIGN_REVIEW_REQUIRED | one owner-bound deny-before-payload policy and resource-positive/negative/mutation proof packet | packet authoring candidate |
| ORCHESTRATOR_PACKET_GAP: future Preview wrapping affects Print comparison | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | include both existing browser specs and canonical-versus-rendered identity in one closeable manifest | required before dispatch |

## Epistemic Process Block

### Expected Result / Prediction
The observed requests should map to the existing Preview renderer independently of Print, with current route escaping narrowing production reachability.

### Evidence Comparison
Direct Preview srcdoc and existing intercepted pre-Print hits support the sink finding; route escape-first rendering and current default consumers support the narrower reachability statement.

### Contradiction Or Gap Disposition
No production incident is inferred. Future resource policy must preserve canonical identity and accepted Print behavior; implementation stays unopened.

### Claim Update
Source-audited ADAPT_EXISTING_OWNER candidate ready for bounded packet AUTHORING only.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`reviewer_return_review`, role=`reviewer`, lifecyclePhase=`review`.
Command: `python governance/compat/run_adif_defect_resolver.py --task-class reviewer_return_review --role reviewer --lifecycle-phase review --json`; 0 items, truncated=false.
Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` |
| literalTokensReviewed | review headings; Source Verification ACCEPT rows; selected-depth PARTIAL corpus verdict; complete trace fields; Public Export Disposition |
| gateRunPurpose | Confirm pre-read source audit structure and scope; not first discovery of checker requirements |
| claimBoundary | no browser rerun, production incident or worker implementation proof |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace |
| Session or invocation | Preview passive-load owner audit, 2026-10-01 |
| Working directory | repository root |
| Command or tool surface | named source/evidence reads, scoped rg, byte hashes, review/roadmap authoring, Git/gates |
| Target paths | this audit and NCR roadmap D063 |
| Allowed scope source | active nextAllowedMove; operator next move; bounded Local owner decision |
| Before status evidence | clean HEAD `abcf1f1679ba57e68455790c63b3a4ae2a2e79d9` |
| After status evidence | two material docs pending commit; product unchanged |
| Diff evidence | git status --short --untracked-files=all; exact two-path batch |
| Approval boundary | owner decision/next packet authoring only; no worker release |
| Claim boundary | no provider/governance/runtime implementation, data/effect or public claim |
| Agent type | INTERNAL_AGENT reviewer |
| Invocation ID | cvf-ncr-preview-passive-owner-audit-20261001 |
| Expected manifest | `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_LOAD_OWNER_AUDIT_2026-10-01.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Actual changed set | `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_LOAD_OWNER_AUDIT_2026-10-01.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

A source-only owner audit using prior synthetic observations. It does not prove production exploitability, a new Preview resource policy, all HTML safety, provider behavior, artifact acceptance, Q001/Q004 exit, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
