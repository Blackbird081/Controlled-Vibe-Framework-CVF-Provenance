# CVF NCR HTML B1 Preview Navigation Worker Return

Memory class: worker-return-evidence

docType: review

Status: COMPLETE_PENDING_REVIEW

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_CONTAINMENT_2026-10-02.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_CONTAINMENT_2026-10-02.md`

executionBaseHead: `d9d2366a82d6284eee57ab92f8a190aa365d1065`

contractProfile: WORKER_RETURN_FULL_GATE_V1

## Rework Convergence Self-Proof

rootCauseClusterId: B1_PREVIEW_NAVIGATION_POLICY_ESCAPE
recurrenceDisposition: INITIAL_DISPATCH_GENERATION_ZERO
priorRelatedFinding: `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_OWNER_AUDIT_2026-10-01.md`
operatorNoticeDisposition: NOT_APPLICABLE_WITH_REASON - no operator decision is involved
successorFreezeDisposition: NO_SUCCESSOR_OPENED - none opened
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES
productionBindingEvidence: the `iframe[title="Preview"]` in `ArtifactExportPanel.tsx` is the production sink exercised by the real Build button; the navigation-only mutation blinded the layer's element walk on that real path and was not a source change
adversarialRegressionDisposition: PASS_TARGETED_DEFECT_CLASS
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
internalAgentInvocationCount: 1
externalAgentInvocationCount: 0
providerCallCount: 0
tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON: local agent usage meter was not exposed to this worker
terminalReadinessVerdict: READY_FOR_REVIEW

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-ncr-html-b1-preview-navigation-containment","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["B1_PREVIEW_NAVIGATION_POLICY_ESCAPE"],"reopened":[],"current":["B1_PREVIEW_NAVIGATION_POLICY_ESCAPE"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

Blocker resolution is claimed by the worker as evidence only; Local decides the blocker delta at review.

## Purpose

Return the bounded Preview navigation containment: the derived Preview document no longer carries any activatable link, image-map area, SVG link target, script-less SVG target animation, meta refresh or base element, so a user action cannot replace the policy-bearing Preview document, open a page or request a destination. Empty sandbox, opaque origin, blocked scripts, initial passive-resource denial, readable selectable scrollable inline presentation, canonical `result.html` for Copy, Download and Print, and the accepted Print R2 behavior are retained. Worker evidence for Local, not artifact acceptance.

## Target / Source

Bound work order, paired GC-018 baseline, owner audit `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_OWNER_AUDIT_2026-10-01.md`, the accepted initial Preview and Print R2 baselines. Read: panel, panel unit test, both Playwright specs, `playwright.config.mock.ts`, `tests/e2e/utils.ts`, DESIGN.md error and empty state rules, guard orientation and the gate lessons. Revised the four existing source paths and created three task outputs.

## Scope / Methodology

Startup acknowledged: mode `cvf_ncr_p10_closed_p11_parked`; handoff `AGENT_HANDOFF_V63_2026-09-18.md`; next move: execute the bound Preview navigation packet; role INTERNAL_AGENT worker; decision owner Local.

Order of work: clean HEAD `d9d2366a8` (two commits after the dispatch base, both continuity and packet only), three output paths absent, bound pre-implementation gate COMPLIANT before any edit. Non-product experiments in one headless Chromium profile measured every trigger class against the current construction. The integrated design was then sealed in the proof reference with its snapshot hash and the four product-source hashes in the proof JSON before any product edit. Chosen mechanism: parse the canonical HTML with DOMParser in the parent, walk all elements including template contents, remove href attributes from links and areas and from MathML elements, remove SVG animate and set, meta refresh and base, serialize and verify by re-parse, and fail closed to an inert localized document; the unchanged policy builder then places the resource policy first. A nested frame-src wrapper was rejected by measurement (blocked navigation replaces the content and middle, Ctrl and Shift clicks still open a page). Then units, the 25-class browser matrix with control, negative and mutation, the sandbox group, usability, the Print fixture comparison, proof reference, evidence JSON and this return.

## Findings / Position

Baseline measurement showed real escapes in the current Preview: anchors of every URL form, Enter, target self, download anchors, area links, SVG links, base plus relative anchors, redirecting links, duplicate and padded href, declarative-shadow-root and noscript anchors, SVG set and animate adding a target without script, and middle, Ctrl and Shift clicks opening a page. data and about:blank links and the fragment link replaced the document without a destination (the fragment link loaded the app page itself because of the srcdoc base URL).

Actual product after the change, 25 layer classes: control effect observed for each, zero attempted destinations, secondary hits and unexpected requests, one page, parent unchanged, marker, policy meta and benign content retained, derived srcdoc free of navigation constructs; layer-only mutation restored every declared effect and failed the same oracle with sandbox, policy and srcdoc-equals-pre-layer verified. Sandbox regression group (targets top, parent, blank, named, forms, formaction, image input, javascript, blob, meta refresh, nested frame, object): control and product both zero effects, not credited to the layer.

Usability: computed inline styles correct, real triple and double click selection, wheel and End key scrolling, inactive labels readable with no href, no request from clicking them, Download bytes equal to the canonical fixture. Existing initial resource tests (20-hit control, two negatives, policy-only mutation) and all Print R2 assertions pass unchanged; the Print fixture now proves the Preview drops link targets while the printed srcdoc keeps them verbatim. Final combined run: 88 passed, exit 0, Chromium 145.0.7632.6. Units 63 passed, tsc and eslint clean.

## Risk / Corrective Action

Tradeoffs for Local: links and fragment jumps are inactive in the Preview, canonical exports keep them; SVG animate and set, meta refresh and base are removed from the Preview only; limited-quirks doctypes become standards mode when a document is re-serialized; clean documents stay byte-identical. Oracle authorship: the class list, fixtures, probe pages, marker check, mutation patch, usability thresholds and unit fixtures are worker-authored, mapped only to the work order oracle rows; the Local probe should use a distinct fixture. Post-seal deviations are listed in the proof reference (mailto reclassified to a layer class, harness fixes). Untested: other browsers, parent reload, assistive technology, MathML in a browser, real packets, larger documents, paper and dialog output.

Environment: runtime override `NEXTAUTH_URL=http://localhost:3001 AUTH_URL=http://localhost:3001` and `CVF_PDFTOTEXT_PATH` used; no config edit, no dependency install. The incidental tracked `test-results/.last-run.json` was restored. The file size guard flagged the unit file near its hard limit during work and it was reduced to 1165 lines.

## Decision / Disposition

Disposition: COMPLETE_PENDING_REVIEW. The worker claims that, for synthetic input in one Chromium profile, the real Artifacts Preview contains document-replacing navigation before any destination request, keeps isolation and benign presentation, the layer-only mutation restores the effects and fails the same oracle, and canonical bytes and Print R2 behavior are unchanged. Acceptance and the independent probe remain with Local; operator decisions remain with the operator.

## Work-Order Acceptance Evidence

```acceptance-evidence-json
{
  "schemaVersion": "cvf.workOrderAcceptanceEvidence@1.0.0",
  "executionBaseHead": "d9d2366a8",
  "results": [
    {"requirementId":"REQ-1","actualArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx"],"proofRefs":["PROOF-NAV-LAYER"],"status":"PASS"},
    {"requirementId":"REQ-2","actualArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx"],"proofRefs":["PROOF-UNIT"],"status":"PASS"},
    {"requirementId":"REQ-3","actualArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts"],"proofRefs":["PROOF-NAV-POSITIVE","PROOF-NAV-NEGATIVE","PROOF-NAV-MUTATION","PROOF-USABILITY","PROOF-RESOURCE-REGRESSION"],"status":"PASS"},
    {"requirementId":"REQ-4","actualArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts"],"proofRefs":["PROOF-PRINT-REGRESSION"],"status":"PASS"},
    {"requirementId":"REQ-5","actualArtifacts":["docs/reference/CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_CONTAINMENT_PROOF_2026-10-02.md"],"proofRefs":["PROOF-NAV-DESIGN","PROOF-BOUNDARY"],"status":"PASS"},
    {"requirementId":"REQ-6","actualArtifacts":["docs/reviews/evidence/cvf-ncr-html-b1-preview-navigation-worker-proof-2026-10-02.json"],"proofRefs":["PROOF-OBSERVATIONS"],"status":"PASS"},
    {"requirementId":"REQ-7","actualArtifacts":["docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_WORKER_RETURN_2026-10-02.md"],"proofRefs":["PROOF-RETURN"],"status":"PASS"}
  ],
  "parkedCheckpoints": ["real GitHub-ledger cutover","real accepting actor and account","artifact store location and writer model","backup location and key custody","retention and deletion schedule","RPO and RTO","cost budget","P08","artifact acceptance","pilot or live effect","P11","deployment","Q001 and Q004 exit"]
}
```

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_experience_retrospective.py` (field values follow the accepted prior Preview return, which passed the same gate) |
| literalTokensReviewed | `COMPLETE_PENDING_REVIEW`; `acceptance-evidence-json`; `WORKER_MUST_NOT_COMMIT honored`; `run_worker_return_fast_gate.py`; `git diff --name-status`; `PENDING_REVIEWER_EXECUTION` |
| gateRunPurpose | Confirm the exact seven-path ledger join and reviewer-pending status |
| claimBoundary | Structural gates cannot substitute for the Local reviewer-owned probe or prove behavior beyond the synthetic input. |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Internal worker |
| Provider or surface | Shared private CVF workspace; local Next dev server and one headless Chromium; synthetic fixture |
| Session or invocation | NCR HTML B1 Preview navigation worker, 2026-10-02 |
| Working directory | Repository root and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` |
| Command or tool surface | bound pre-implementation gate; Playwright; Vitest; tsc; eslint; worker fast gate |
| Target paths | Exact seven-path worker acceptance ledger |
| Allowed scope source | Bound Preview navigation work order and paired GC-018 baseline |
| Before status evidence | `git status --short --untracked-files=all` empty at HEAD `d9d2366a8` before any edit; three output paths absent |
| After status evidence | Four modified tracked paths and three untracked worker paths, no staged path, no worker commit |
| Diff evidence | `git diff --name-status` lists the four modified paths; the three new paths appear as untracked in `git status --short --untracked-files=all` |
| Approval boundary | Worker evidence only; Local reviewer owns the independent probe, acceptance and commit |
| Claim boundary | Synthetic one-profile Chromium Preview observation; no acceptance, Q001 or Q004 closure, universal HTML safety or live assertion |
| Agent type | INTERNAL_AGENT worker |
| Invocation ID | cvf-ncr-html-b1-preview-navigation-worker-20261002 |
| Expected manifest | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts`; `docs/reference/CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_CONTAINMENT_PROOF_2026-10-02.md`; `docs/reviews/evidence/cvf-ncr-html-b1-preview-navigation-worker-proof-2026-10-02.json`; `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_WORKER_RETURN_2026-10-02.md` |
| Actual changed set | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts`; `docs/reference/CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_CONTAINMENT_PROOF_2026-10-02.md`; `docs/reviews/evidence/cvf-ncr-html-b1-preview-navigation-worker-proof-2026-10-02.json`; `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_WORKER_RETURN_2026-10-02.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | Synthetic one-profile real-browser Preview navigation containment and canonical identity proof |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: observed in one Chromium run; reviewer pending |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no governance receipt is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: controls, actual-Preview negatives, layer-only mutations, usability and Print regression in the proof JSON |
| invocationBoundary | local Next dev server and headless browser; synthetic intercepted export |
| interceptionBoundary | context routes fulfill destination, secondary, redirect and unknown navigation requests locally, no forwarding; the export request is fulfilled by `page.route`; no production wrapper is claimed |
| claimLanguage | Observed containment of Preview navigation before any destination request, reviewer pending |
| forbiddenExpansion | No route, ledger, database, provider, real data, artifact acceptance, public sync or deployment |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Input type | internal governed input (no external intake) |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Internal source | `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_OWNER_AUDIT_2026-10-01.md` |
| Chain map route | Local source-derived Preview navigation adaptation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | No external advisory is private CVF proof. |

## External/Local Coordination Binding

Role: shared-workspace `INTERNAL_AGENT`. Phase: bounded B1 Preview navigation worker. Decision owner: Local.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: named source files were read directly; no external-source rescan occurred.

## Corpus Completeness And Report Integrity

N/A with reason: seven exact worker outputs are the bounded set; no all-files inventory is claimed.

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - the tranche makes no corpus completeness claim.

## Finding-To-Governance Learning Disposition

| Field | Value |
|---|---|
| Defect class | RUNTIME_SIGNAL_GAP: a script sandbox and a resource policy do not stop user-activated self-navigation, and a verification step inside the mechanism can turn a naive mutation into a safe fail-closed result instead of the escape it was meant to restore |
| Learning lane | RUNTIME_BEHAVIOR_LEARNING |
| Finding | A navigation proof needs real input per trigger, a replaced-document marker rather than a final URL, a control that keeps every other layer, and a mutation that blinds only the layer walk so the product's own verification cannot mask it |
| Disposition | RUNTIME_LEARNING_CANDIDATE: Local decides whether to keep the control and mutation as review-probe material |
| Next control action | Local reviewer runs one distinct-fixture click, request and usability probe in the actual Preview |

## Epistemic Process Block

### Expected Result / Prediction

Removing activatable navigation constructs from the derived Preview before the frame exists prevents every self-navigation, new-page and replaced-document effect the control shows, without losing readable, selectable, scrollable inline presentation or canonical output.

### Evidence Comparison

The prediction held for all 25 layer classes: control effect, zero in the product, effect restored by the layer-only mutation. The first full run exposed harness defects and one classification error, fixed in scope.

### Contradiction Or Gap Disposition

Remaining gaps are disclosed above. The Local independent probe remains pending.

### Claim Update

The worker claims an observed one-profile Chromium result, reviewer acceptance pending. Q001 and Q004 remain open and nothing is accepted.

## Return-Time Closeability Recheck

closeabilityDisposition: CLOSEABLE
outsideAuthorityBlockers: NONE
nextRepairRoute: NONE
workerRedispatchAllowed: NO

The seven-path worker manifest is complete and no forbidden path was edited. GC-051 entries for both specs are already committed and were not modified.

independentProbeDisposition: PENDING_REVIEWER_EXECUTION
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:
frictionLevel: LOW
frictionType: HELPER_GAP
observedStep: the first matrix run failed on harness defects (popup frame access, blocked-image request counted, stalled drag) and the file size guard needed the unit file trimmed
preventiveControlCandidate: HELPER_DIAGNOSTIC

## Claim Boundary

The worker return is `COMPLETE_PENDING_REVIEW`; it is not acceptance, artifact approval, a durable store, an operator decision, universal HTML safety, all-navigation support, other-browser behavior, paper or dialog output, Q001 or Q004 exit, P11 release or a public claim. Undecided operator checkpoints remain: real accepting actor, real data and store profile, store location and writer model, backup and key custody, retention, RPO and RTO, cost, P08 scope, artifact acceptance, pilot or live effect, P11 and deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## git status --short

Four modified tracked Web files and three untracked worker-owned files, zero staged files. Exact path list follows.

## Changed Files

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts`
- `docs/reference/CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_CONTAINMENT_PROOF_2026-10-02.md`
- `docs/reviews/evidence/cvf-ncr-html-b1-preview-navigation-worker-proof-2026-10-02.json`
- `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_WORKER_RETURN_2026-10-02.md`

## Command Evidence

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_CONTAINMENT_2026-10-02.md`: COMPLIANT (exit 0) on the clean worktree at `d9d2366a8` before any edit.
- `npx playwright test tests/e2e/artifact-export-preview-sandbox.spec.ts tests/e2e/artifact-export-print-browser.spec.ts --config playwright.config.mock.ts` with the port override: earlier runs failed on harness defects and one classification error, fixed; final run PASS, 88 passed, exit 0.
- `npx vitest run src/components/ArtifactExportPanel.test.tsx`: PASS, 63 passed.
- `npm run check` (`tsc --noEmit`): PASS, exit 0.
- `npx eslint --max-warnings=0` on the four code paths: PASS, exit 0.
- `python governance/compat/check_governed_file_size.py --enforce` after trimming the unit file to 1165 lines: no violation in the changed files.
- `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_CONTAINMENT_2026-10-02.md`: PASS (exit 0, 69/69 hook checks) on the final seven-path state. Earlier runs failed on the operation trace changed-set row (paths must be listed) and on the missing PASS evidence line in this return; both were repaired in scope and the gate rerun.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`worker_execution`, role=`worker`, lifecyclePhase=`worker-return`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class worker_execution --role worker --lifecycle-phase worker-return --json`; run by the worker at return time: 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. All seven worker outputs are uncommitted, and the distinct Local reviewer owns acceptance and material commit.
