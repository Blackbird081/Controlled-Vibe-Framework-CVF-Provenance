# CVF NCR HTML B1 Print Browser Reviewer Decision

Memory class: governed-review

docType: review

Status: REVIEW_COMPLETE_REWORK_REQUIRED

Date: 2026-10-01

providerExecutionAuthority: FORBIDDEN

## Purpose

Decide whether the six-path B1 Print worker return is safe to accept after the Local GC-051 repair and an independent focused Chromium run.

## Target / Source

Worker return: `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_WORKER_RETURN_2026-10-01.md` at execution base `6390d5300`. Governed order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_2026-10-01.md`. Local registry repair: `7d96cde92`; handoff marker sync: `c3158d423`. [HTML Standard origin creation](https://html.spec.whatwg.org/multipage/document-sequences.html) and [MDN's inherited-origin explanation](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy) are browser-semantics references, not CVF authority.

## Scope / Methodology

Startup acknowledged: current mode=`cvf_ncr_p10_closed_p11_parked`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=review returned B1 Print evidence; role=Local reviewer; phase=worker-return review; technical decision owner=Local; effect decision owner=operator; parked=Q001/Q004, durable acceptance, pilot/live, P11, public sync and deployment.

Local inspected the exact six worker paths and their diff, committed the separately owned GC-051 entry and aggregate, then aligned the worker acceptance comparison base after the marker sync. The focused Playwright case was independently rerun once with the existing mock auth-origin override; Chromium 145.0.7632.6 reported 1/1 PASS. The worker-return fast gate subsequently passed. This was a named critical security contradiction review, not a broad implementation rerun.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Print opens same-origin initial blank popup, detaches opener, then writes HTML | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `handlePrint` worker diff | `window.open`, `opener`, `document.write` | Artifacts panel | ACCEPT |
| Browser fixture contains executable script and print oracle | TEST_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts` | `FIXTURE_SCRIPT`, focused case | `window.opener`, `print` | Playwright proof | ACCEPT |
| Worker discloses same-origin residual | RETURN_EVIDENCE | `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_WORKER_RETURN_2026-10-01.md` | Risk / Corrective Action | storage/cookies | worker return | ACCEPT |
| B1 preview is sandboxed while Print is top-level | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | preview and `handlePrint` | `sandbox`, popup | Artifacts panel | ACCEPT |
| D056 permitted browser repair while preserving opener isolation | GOVERNED_DECISION | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D056-D057 | B1 Print | NCR roadmap | ACCEPT |

## Findings / Position

The worker correctly reproduced the former dead button and made the real Chromium button reach one native `print()` invocation. Local rerun observed one popup, one write, one print call, displayed nonce `N1` after an unsaved form edit, and zero unexpected fixture requests. The detached opener negative oracle is discriminating for direct window access.

That oracle does not cover origin privileges. The popup starts as `about:blank` created by the app and inherits its origin. The fixture's inline script executed in that popup; its `opener-null` result demonstrates only that the opener reference was removed. Same-origin script can still reach origin-scoped storage and can issue same-origin requests with ambient browser credentials. Thus the candidate removes the iframe sandbox boundary for the printed HTML and has a material security gap even though the work order's narrow opener and print assertions pass. This is an inference from the native browser observation plus the cited origin rules; no real credential or storage read was attempted.

## Decision / Disposition

`REWORK_REQUIRED_SECURITY_BOUNDARY`. Do not accept or commit the two production/test modifications or the four pending worker paths as a completed B1 Print repair. Keep the six worker paths uncommitted and intact for corrective planning. The GC-051 registry repair is separately committed; its registration does not confer acceptance. Gate PASS means the returned packet has valid structure and bounded proof, not that printed HTML is isolated.

The corrective design must prevent printed HTML from obtaining app-origin script/storage/cookie authority, while still proving the native print invocation and displayed-version binding in Chromium. A new browser negative oracle must seed synthetic app-origin storage and show the printed payload cannot read or mutate it or invoke same-origin authenticated endpoints; it must also catch a mutation that removes the isolation. The test must distinguish a browser-enforced block from an inert payload. The worker may compare a sandboxed printable frame, effective CSP, or another design, but no mechanism is pre-approved. If a safe design cannot be shown in the authorized path set, return blocked and request a source-audited scope amendment. Do not soften the security criterion merely to obtain a passing print call.

## Risk / Corrective Action

This is a new independent security finding, not a repeat of the original noopener/null bug. The Local reviewer will author a consolidated R1 work order after preserving this disposition and resolving the inherited six-path worktree boundary. Physical paper/PDF output, headed dialog, popup-blocked branch, other browsers, passive loads and accessibility remain outside this decision. Q001/Q004 and actual data/store/effect choices remain parked.

## Review Gate

GC-051 registry generation/check PASS. Independent focused Chromium case PASS 1/1. Worker-return fast gate PASS after Local registry and comparison-base repair. Reviewer semantic security verdict FAIL; no material acceptance commit for worker paths.

## Finding-To-Governance Learning Disposition

| Defect class | Learning lane | Disposition | Next control action | Batch status |
|---|---|---|---|---|
| RUNTIME_SIGNAL_GAP: same-origin popup authority | RUNTIME_BEHAVIOR_LEARNING | RUNTIME_LEARNING_CANDIDATE; DESIGN_REVIEW_REQUIRED | add origin-privilege negative oracle and safe Print design | open R1 |
| ORCHESTRATOR_PACKET_GAP: GC-051 worker-path registration | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS: Local registry owner was declared by the packet | entry/aggregate committed `7d96cde92` | closed |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Input type | internal governed input (no external intake) |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Internal source | `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_2026-10-01.md` |
| Chain map route | Local source-derived security review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | Artifacts panel Print callback |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | Browser standard explains origin; Local source and run decide CVF status |

## External/Local Coordination Binding

Role: Local reviewer of a shared-workspace INTERNAL_AGENT return. Phase: B1 Print review. Decision owner: Local; effect owner: operator.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_work_order_acceptance_ledger.py` |
| literalTokensReviewed | `Status:`, `docType: review`, source-path ACCEPT rows, trace and Public Export Disposition |
| gateRunPurpose | Confirm the pre-read review packet requirements and record checker evidence separately from semantic security disposition |
| claimBoundary | Checker PASS cannot make same-origin popup safe |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local reviewer |
| Provider or surface | private CVF shared workspace |
| Session or invocation | B1 Print reviewer decision, 2026-10-01 |
| Working directory | repository root and cvf-web package |
| Command or tool surface | exact source/diff review, GC-051 generator/checker, focused Playwright, worker-return fast gate, Git |
| Target paths | this review and NCR roadmap D058 |
| Allowed scope source | Local reviewer role under B1 Print work order; operator delegated technical decisions |
| Before status evidence | six worker paths pending at `c3158d423` after Local registry/marker commits |
| After status evidence | six worker paths remain uncommitted; this review and roadmap decision pending material commit |
| Diff evidence | review and roadmap material set plus six preserved uncommitted worker paths in the shared worktree |
| Approval boundary | no production acceptance or effect approval |
| Claim boundary | security finding is source/browser-semantics inference; no credential or storage access attempted |
| Agent type | reviewer |
| Invocation ID | cvf-ncr-html-b1-print-review-20261001 |
| Expected manifest | `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_AUDIT_2026-10-01.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts`; `docs/reference/CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_PROOF_2026-10-01.md`; `docs/reviews/evidence/cvf-ncr-html-b1-print-repair-worker-proof-2026-10-01.json`; `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_WORKER_RETURN_2026-10-01.md` |
| Actual changed set | `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_AUDIT_2026-10-01.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts`; `docs/reference/CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_PROOF_2026-10-01.md`; `docs/reviews/evidence/cvf-ncr-html-b1-print-repair-worker-proof-2026-10-01.json`; `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_WORKER_RETURN_2026-10-01.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

The observed one-profile native print call and version binding are accepted as bounded evidence, not as an acceptable production Print implementation. No universal HTML safety, origin isolation proof, paper/PDF output, accessibility, provider governance, durable artifact acceptance, Q001/Q004 exit, public sync or deployment follows.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
