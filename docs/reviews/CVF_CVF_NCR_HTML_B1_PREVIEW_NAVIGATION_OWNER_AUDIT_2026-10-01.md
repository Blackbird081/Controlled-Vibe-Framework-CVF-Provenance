# CVF NCR HTML B1 Preview Navigation - Local Owner Audit

Memory class: governed-review

docType: review

Status: REVIEW_COMPLETE_NO_DISPATCH

Date: 2026-10-01

providerExecutionAuthority: FORBIDDEN

## Purpose

Resolve NAVIGATION_AFTER_PREVIEW_POLICY_ESCAPE to the existing owner, current reachability, known proof boundary and next packet route. Read-only source/evidence audit; no product edit, browser rerun or worker release.

## Target / Source

Clean audit base `1e22f1b4a52f1ac47da70b736d13e957c9eefcde`. Active next move READ_ONLY_PREVIEW_NAVIGATION_OWNER_AUDIT. Initial Preview accepted bounded at f00658021 in `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_COMPLETION_2026-10-01.md`; reuse distinct Local link-click evidence in `docs/reviews/evidence/cvf-ncr-html-b1-preview-passive-resource-local-probe-2026-10-01.json`.

## Scope / Methodology

Startup acknowledged: mode=cvf_ncr_p10_closed_p11_parked; active handoff=AGENT_HANDOFF_V63_2026-09-18.md; next=read-only Preview navigation owner audit; role=Local orchestrator/reviewer; phase=audit; decision owner=Local; effect owner=operator; parked=Q001/Q004, durable B2, P11, actor/data/store/effect, public sync/deployment. Worker INTERNAL_AGENT regardless of provider; no external research or MCP authorization opened.

Read selected regions of six explicit paths below. Trace derived initial document versus navigated destination; check source producer and current test oracle scope. Consume existing independent observations; no duplicate browser experiment and no repository-wide coverage claim.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Existing render owner/policy | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | buildPreviewDocument; Preview iframe | buildPreviewDocument; PREVIEW_FRAME_POLICY; sandbox | ArtifactExportPanel | ACCEPT |
| Default producer escapes text | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | escapeHtml; renderInline/renderMarkdownLite; buildHtml | escapeHtml; renderInline; buildHtml | export route | ACCEPT |
| Current resource oracle is pre-navigation | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts` | previewViolations; previewCases | previewViolations | Preview spec | ACCEPT |
| Explicit click/destination observation | `docs/reviews/evidence/cvf-ncr-html-b1-preview-passive-resource-local-probe-2026-10-01.json` | observations.navigation; oracleSource | navigation; after-navigation | Local probe | ACCEPT |
| Accepted boundary excludes navigation | `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_COMPLETION_2026-10-01.md` | Findings; Decision | initial derived srcdoc | Local reviewer | ACCEPT |
| Prior packet covers initial rendering | `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_2026-10-01.md` | Implementation Contract | Preview before any Print click | Local packet | ACCEPT |

## Findings / Position

1. Owner remains the Preview iframe and buildPreviewDocument in ArtifactExportPanel. The component injects a CSP meta into a derived srcdoc, keeps sandbox empty, and uses unchanged canonical result.html for Copy/Download/Print. It does not implement a navigation containment layer in the inspected render path. The source comment explicitly discloses navigation outside CSP coverage.
2. Existing Local observation: initial derived Preview produced no controlled hits; a direct click on an off-origin anchor replaced its document. The locally fulfilled destination then requested an image: two controlled hits, parent URL remained /artifacts. This proves the initial policy does not persist across that observed self-navigation; it does not prove production authorization effects, cookie delivery, exfiltration or top-level escape. Post-navigation origin/script/storage capabilities were not measured; do not infer them from the pre-click observation.
3. Automatic meta refresh in the same synthetic profile produced zero hits within its observation window. This is not a proof for every refresh syntax, browser or timing. Self, parent/top, named/blank targets, keyboard activation, alternate click, fragment navigation, SVG links, download-like actions, malformed HTML and redirect chains have not all been proved by the current evidence.
4. Default route renderInline escapes source text then adds only code/strong; renderMarkdownLite produces escaped headings/list/paragraphs. The inspected fixed buildHtml template contains no anchor navigation markup. The shown escaped source text does not become a raw link under that producer. Synthetic result.html/component input demonstrates renderer behavior, not user-source injection or a production incident. No app-wide absence claim.
5. Current Preview browser oracle observes initial passive resources, script/origin and benign rendering, with policy-only mutation. It does not activate navigation links. Passing it cannot certify a navigated destination. Initial resource acceptance stays intact and bounded. Navigation is a distinct user-interaction concern, not a reset or successor of the stopped Print chain.

## Owner / Overlap Disposition

ADAPT_EXISTING_OWNER. A prospective navigation assignment belongs to Preview-derived presentation and its existing tests; no global sanitizer, route/auth/header policy, external-navigation service or durable acceptance owner is authorized. Keep Copy/Download/Print canonical and retain accepted initial passive-resource/script/origin behavior.

Prospective product posture: external/document-replacing navigation is inactive in the Preview presentation; text, inline layout, reading/scrolling and canonical actions remain usable. Define the treatment of same-document fragment links explicitly and prove any supported behavior without network or document replacement. This technical posture is a candidate for the next bounded packet, not an implemented behavior or an approved mechanism.

## Decision / Disposition

REVIEW_COMPLETE_NO_DISPATCH. Next AUTHOR one distinct Preview navigation containment packet with paired GC-018, integrated design admission, exact paths, role closeability and discriminating browser evidence. No implementation begins before bound release; no specific interception, parser transformation, browser directive or inert wrapper is approved by this audit.

The authoring contract must address known dependencies as one assignment:

- Before choosing a mechanism, evaluate navigation triggers, payload parsing, policy ordering, sandbox/opaque-origin constraints, canonical provenance, usability and initial resource regression. A mechanism that only restores the original srcdoc after a destination request is too late to prove zero navigation requests.
- Build an executable safe synthetic navigation positive control using existing empty sandbox, and actual-product negative/mutation oracles. Intercept navigation destinations and their secondary resources on all relevant frames/pages before payload; count attempted destination requests, not only final URL. Reuse observed explicit self-link proof; do not reproduce it during authoring.
- Declare a bounded navigation matrix covering same/off-origin absolute and relative links, self/parent/top/blank targets, mouse/keyboard activation, refresh, base/SVG/other navigation markup relevant to the selected mechanism, data/blob destinations, fragment behavior and malformed inputs. Unimplemented classes must be fail-closed or explicitly excluded from claim; no blanket all-HTML navigation assertion.
- Preserve readable/selectable text, scrolling and inline styles. State rendering/interaction losses and prove any retained fragment behavior. Disabling every interaction or hiding payload cannot satisfy benign presentation without a demonstrated usability disposition.
- Preserve canonical result.html and displayed-version/provenance across Copy/Download/Print, supersession, failure and initialResult. Include panel/unit and existing Preview AND Print specs in the prospective manifest; retain initial resource controls and R2 Print assertions. Mechanism selection may need an integrated design artifact before execution, with all output paths declared before release.
- No route/auth/config/dependency/package/governance/storage edits by worker. Historical proof outputs remain read-only. If coherent containment cannot fit existing authority, return blocked design evidence to Local rather than claim a policy directive or expand scope.

Q001/Q004 remain OPEN; durable B2/P11 and real actor/data/store/effects/public/deploy parked. No automatic repair dispatch or same-problem Print successor.

## Risk / Corrective Action

Empty sandbox with opaque origin means parent-side listeners cannot simply inspect/cancel child navigation; no unproved event-interception guarantee is accepted. A late load/reset observation may expose destination requests before it reacts. A future design must show effective outcomes, not just a restored heading or unchanged parent URL. This audit makes no browser specification guarantee beyond observed/source-owned evidence.

Data/blob images and font loss, non-plain-doctype mode changes and other initial rendering limits remain accepted only within previous boundary. Do not conflate presentation derivation with general sanitization or change downloadable/source bytes.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | Preview owner and future bounded packet | navigation source audit only, no execution grant | six named sources/evidence above | existing Web component | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | no interface opened | no ingress/credential/mutation grant | internal-only audit | adapter deferred | DEFERRED_WITH_REASON |

## Corpus Completeness And Report Integrity

- Corpus task class: AUDIT, six named paths with selected-section read depth.
- Corpus root: private CVF repository at audit base.
- Snapshot time: 2026-10-01, audit source HEAD above.
- Enumeration command: filesystem-backed Python Path.is_file/Path.read_bytes on the six explicit paths; SHA-256, no whole-repo enumeration.
- Manifest artifact or inline manifest: inline JSON below; processing ledger uses terminalStatus plus explicit readDepth/sections.
- Manifest hash: `eeb20e93b3b3de7c81442b68410c4a73d1a637acc6fb58d160d14f182bc9ff6b` (compact sorted-key UTF-8 JSON).
- Processing ledger artifact or inline ledger: inline manifest terminalStatus/readDepth/sections fields.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE. All six rows READ at SELECTED_SECTIONS depth.
- Reconciliation: manifest=6; ledger_terminal=6; exclusions=0; unresolved=0. Counts cover the six explicit paths only.
- Unresolved files: no missing named source; unexamined regions remain outside semantic claim.
- Declared exclusions: other paths, unselected sections, production headers/endpoints/data, runtime experiments and physical-output contexts.
- Unreadable or unsupported files: none in named byte-hash manifest.
- Aggregation check: manifest length and unique path count both 6; every row has SHA-256 and section ledger.
- Drift check: sources hashed at clean audit base; only review and roadmap authored; product sources not changed.
- Output traceability: Source Verification, Findings and Decision above.
- Adversarial verification: existing executable controls and mutations consumed within their limits; new resource classes require future packet proof.
- Corpus verdict: PARTIAL

```json
[{"path":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx","sha256":"9d3561680b860915ac729e44bd6096b7e11fad75d1eeb93452bbe97d16e5a809","terminalStatus":"READ","readDepth":"SELECTED_SECTIONS","sections":"buildPreviewDocument; PREVIEW_FRAME_POLICY; Preview iframe; canonical callbacks"},{"path":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts","sha256":"6b988ba687b9b1478f097ca81c3e1235aa20ef819106c050279779da00781c3c","terminalStatus":"READ","readDepth":"SELECTED_SECTIONS","sections":"escapeHtml; renderInline/renderMarkdownLite; buildHtml"},{"path":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts","sha256":"6d800cd5bdbe69160387832c3b0ff83cd442e64e2d64b1e7772ff7ae9f223f7f","terminalStatus":"READ","readDepth":"SELECTED_SECTIONS","sections":"previewViolations; previewCases; resource mutation"},{"path":"docs/reviews/evidence/cvf-ncr-html-b1-preview-passive-resource-local-probe-2026-10-01.json","sha256":"7ccedf209c4f363969a6d14bb2dadb058fcf5d56ad3cfa7961d5a10562a86530","terminalStatus":"READ","readDepth":"SELECTED_SECTIONS","sections":"oracleSource; observations.negative/navigation"},{"path":"docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_COMPLETION_2026-10-01.md","sha256":"e8c0ae9d5142e8381160d794bfd6a480491940c886c60b2362d1201c703c4a3f","terminalStatus":"READ","readDepth":"SELECTED_SECTIONS","sections":"Findings; Decision; initial-document claim boundary"},{"path":"docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_2026-10-01.md","sha256":"328085ae4c19a89e14857ace76e6bdcfd1fd6b4bb9379208e054ead965562db0","terminalStatus":"READ","readDepth":"SELECTED_SECTIONS","sections":"Implementation Contract; initial before-Print scope"}]
```

## Knowledge System Reconciliation

- Knowledge task class: bounded source owner audit.
- Source manifest: six-row inline JSON in Corpus Completeness And Report Integrity.
- Source manifest hash: eeb20e93b3b3de7c81442b68410c4a73d1a637acc6fb58d160d14f182bc9ff6b.
- Enumeration safety: filesystem-backed Python Path.is_file/Path.read_bytes on six explicit paths.
- Intake registry or ledger: inline terminalStatus/readDepth/sections ledger.
- Authority assets: Preview component, producer, existing Preview spec, prior Local evidence, completion and work order.
- Derived views: this audit and roadmap D066; source-audited candidate only.
- Semantic region ledger: six named selected regions mapped to Source Verification and Findings; unselected sections outside claim.
- Region reconciliation: assets=6; mapped=6; deferred=0; unmapped=0.
- Orphan or unmapped assets: none within explicit manifest; no wider coverage claim.
- Cross-region links: producer reachability, initial versus navigated Preview evidence and canonical-action dependency.
- Drift check: byte hashes at audit base; product sources unchanged.
- Rebuildability check: named paths, section ledger and source hashes permit reconstruction of bounded audit.
- Retrieval boundary: six explicit paths and selected sections; no whole-repository semantic coverage.
- Adversarial verification: prior synthetic request observations consumed; future policy needs independent controls and mutation proof.
- Knowledge-map verdict: PARTIAL

## Finding-To-Governance Learning Disposition

| Defect class | Learning lane | Disposition | Next control action | Batch status |
|---|---|---|---|---|
| RUNTIME_SIGNAL_GAP: navigated destination loses initial policy | RUNTIME_BEHAVIOR_LEARNING | DESIGN_REVIEW_REQUIRED | one integrated owner-bound navigation design/outcome packet | authoring candidate |
| ORCHESTRATOR_PACKET_GAP: URL/heading restoration is weaker than request denial | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | require destination and secondary-resource request oracle before release | planned, no dispatch |

## Epistemic Process Block

### Expected Result / Prediction
Navigation concern should belong to existing Preview presentation and remain distinct from canonical export/Print.

### Evidence Comparison
Derived srcdoc plus observed explicit click/destination requests support the owner gap. Escaped default producer narrows the reachability claim. Initial passive-resource proof does not test active link navigation.

### Contradiction Or Gap Disposition
No production incident or universal navigation behavior inferred. Mechanism, usability and broader trigger matrix require next packet design/evidence.

### Claim Update
ADAPT_EXISTING_OWNER; packet AUTHORING only. Initial Preview acceptance and operator checkpoints unchanged.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`reviewer_return_review`, role=`reviewer`, lifecyclePhase=`review`.
Command: `python governance/compat/run_adif_defect_resolver.py --task-class reviewer_return_review --role reviewer --lifecycle-phase review --json`; 0 items, truncated=false.
Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_corpus_completeness_report_integrity.py`; `governance/compat/check_corpus_to_knowledge_map_reconciliation.py` |
| literalTokensReviewed | review headings; Source Verification ACCEPT rows; six-source selected-depth PARTIAL verdict; complete trace fields; Public Export Disposition |
| gateRunPurpose | Confirm pre-read navigation source-audit structure and scope; not first discovery of checker requirements |
| claimBoundary | no browser rerun, production incident or worker implementation proof |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace |
| Session or invocation | Preview navigation owner audit, 2026-10-01 |
| Working directory | repository root |
| Command or tool surface | named source/evidence reads, scoped rg, byte hashes, review/roadmap authoring, Git/gates |
| Target paths | this audit and NCR roadmap D066 |
| Allowed scope source | active nextAllowedMove; operator next move; bounded Local navigation owner decision |
| Before status evidence | clean HEAD `1e22f1b4a52f1ac47da70b736d13e957c9eefcde` |
| After status evidence | two material docs pending commit; product unchanged |
| Diff evidence | git status --short --untracked-files=all; exact two-path batch |
| Approval boundary | owner decision/next packet authoring only; no worker release |
| Claim boundary | no provider/governance/runtime implementation, data/effect or public claim |
| Agent type | INTERNAL_AGENT reviewer |
| Invocation ID | cvf-ncr-preview-navigation-owner-audit-20261001 |
| Expected manifest | `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_OWNER_AUDIT_2026-10-01.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Actual changed set | `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_OWNER_AUDIT_2026-10-01.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

Source-only navigation owner audit consuming prior synthetic evidence. No new implementation, browser rerun, production incident, universal navigation containment, provider/governance proof, durable acceptance, Q001/Q004 exit, public sync/deployment or worker release.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
