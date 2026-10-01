# CVF NCR HTML B1 Preview Passive Resource Worker Return

Memory class: worker-return-evidence

docType: review

Status: COMPLETE_PENDING_REVIEW

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_2026-10-01.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_2026-10-01.md`

executionBaseHead: `7548ac66b114bb5b79bbb602bab1681dd4802ad2`

contractProfile: WORKER_RETURN_FULL_GATE_V1

## Rework Convergence Self-Proof

rootCauseClusterId: B1_PREVIEW_PASSIVE_RESOURCE_GAP
recurrenceDisposition: INITIAL_DISPATCH_GENERATION_ZERO
priorRelatedFinding: `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_LOAD_OWNER_AUDIT_2026-10-01.md`
operatorNoticeDisposition: NOT_APPLICABLE_WITH_REASON - no operator decision is involved
successorFreezeDisposition: NO_SUCCESSOR_OPENED - none opened
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES
productionBindingEvidence: the `iframe[title="Preview"]` in `ArtifactExportPanel.tsx` is the production sink exercised by the real Build button in the Chromium spec; the policy-only mutation edited that real path's srcdoc and was not a source change
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
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-ncr-html-b1-preview-passive-resource-policy","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["B1_PREVIEW_PASSIVE_RESOURCE_GAP"],"reopened":[],"current":["B1_PREVIEW_PASSIVE_RESOURCE_GAP"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

Blocker resolution is claimed by the worker as evidence only; Local decides the blocker delta at review.

## Purpose

Return the bounded Preview passive-resource policy: the sandboxed Preview now denies same-origin and off-origin passive network resources and data/blob resources while keeping empty sandbox, opaque origin, blocked script, benign inline rendering and the canonical `result.html` used by Copy, Download and Print. Worker evidence for Local, not artifact acceptance.

## Target / Source

Bound work order, paired GC-018 baseline, owner audit `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_LOAD_OWNER_AUDIT_2026-10-01.md` and the accepted Print R2 baseline. Read: panel (Preview, `handleGenerate`, Copy/Download/Print), panel unit test, both Playwright specs, `playwright.config.mock.ts`, `tests/e2e/utils.ts`; the export route was not needed beyond the packet's description and was not modified. Revised exactly the four existing source paths and created three task outputs.

## Scope / Methodology

Startup acknowledged: mode `cvf_ncr_p10_closed_p11_parked`; handoff `AGENT_HANDOFF_V63_2026-09-18.md`; next move: execute the bound Preview seven-path packet; role INTERNAL_AGENT worker; decision owner Local.

Order of work: clean HEAD `7548ac66b`, three output paths absent, no stash applied, bound pre-implementation gate COMPLIANT before any edit. Design chosen: a Preview-only derived `srcdoc` with a CSP meta placed first (after a plain leading doctype, otherwise prepended), sandbox unchanged. A nested-frame wrapper was rejected because four other specs outside the seven paths read the Preview frame's `h1` directly and a nested frame would break them. Then units, the Preview spec (control, two negative fixtures, policy-only mutation), the Print spec canonical comparison, type/lint, proof reference, evidence JSON and this return.

## Findings / Position

Positive control (disposable context, `sandbox=""`, no resource policy, no script reliance): all 20 expected hits observed, 10 classes on the app origin and the same 10 on an intercepted off origin (image, srcset, link stylesheet, CSS import, CSS background, font, nested frame, frame image, object, object image); a data image decoded (width 1).

Actual Preview before any Print click, two fixtures (passive markup before the doctype and any head with duplicate heads and a permissive payload CSP meta; plain doctype with head inline style): counters reset before Build, zero controlled hits, zero unexpected sub-frame requests, `sandbox=""`, origin `null`, payload script not run, heading color `rgb(1, 2, 3)` and paragraph background `rgb(4, 5, 6)` from inline CSS applied, benign text visible, data image blocked (width 0), derived srcdoc differs from canonical and carries the policy before the first resource markup.

Policy-only mutation on the real product path: stripping only the Preview policy meta from the iframe srcdoc (sandbox kept) restored all 20 hits and the decoded data image; the same oracle failed with passive-resource and data-image violations only, sandbox/origin/script isolation unchanged.

Canonical identity: units (55 passed, 45 existing plus 10 added) assert Copy, Download and Print deliver exact `result.html` while Preview shows a different derived document, for current build, unsaved edit, latest-response supersession, failed newer build keeping the prior result and `initialResult` unknown provenance. The Print spec now compares the printed srcdoc to the canonical response fixture and asserts the Preview is a distinct derived document with zero controlled hits before Print. All Print R2 assertions retained: 5 passed (short 1 page, long 3 pages with 120 rows and end marker, isolation mutation, clipping mutation 44 rows). Preview and Print specs together: 10 passed, Chromium 145.0.7632.6.

## Risk / Corrective Action

Tradeoffs for Local: Preview shows text and inline-styled layout only; embedded `data:`/`blob:` images and fonts do not display in Preview (Print still allows `data:` images). A payload without a plain leading doctype gets the policy first, which can change compatibility mode versus its original. CSP does not govern navigation, so meta refresh and link navigation are untested. Other browsers, headed mode, real exported packets and paper/dialog output are untested. The policy is presentation isolation, not sanitization, and production exploitability of the original gap is unproven.

Environment: the login helper redirects to port 3000 because of `.env.local`; runtime override `NEXTAUTH_URL=http://localhost:3001 AUTH_URL=http://localhost:3001` and `CVF_PDFTOTEXT_PATH` pointing at the existing system poppler were used. No config edit, no dependency install. Tracked `test-results` state is unchanged in status. A first spec revision missed `same:css-bg` because both stylesheets styled one class and the later rule won; distinct per-origin classes fixed the control and mutation, found by the oracle itself.

## Decision / Disposition

Disposition: COMPLETE_PENDING_REVIEW. The worker claims that, for synthetic input in one Chromium profile, the real Artifacts Preview denies same-origin and off-origin passive resources before payload parsing (including early markup and a permissive payload policy), keeps benign inline rendering and script/origin isolation, a policy-only removal restores the hits and fails the same oracle, and canonical Copy/Download/Print bytes and accepted Print R2 behavior are unchanged. Acceptance and the independent false-denial probe remain with Local; operator decisions remain with the operator.

## Work-Order Acceptance Evidence

```acceptance-evidence-json
{
  "schemaVersion": "cvf.workOrderAcceptanceEvidence@1.0.0",
  "executionBaseHead": "7548ac66b",
  "results": [
    {"requirementId":"REQ-1","actualArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx"],"proofRefs":["PROOF-DENY-BEFORE-PARSE"],"status":"PASS"},
    {"requirementId":"REQ-2","actualArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx"],"proofRefs":["PROOF-UNIT","PROOF-CANONICAL"],"status":"PASS"},
    {"requirementId":"REQ-3","actualArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts"],"proofRefs":["PROOF-POSITIVE","PROOF-NEGATIVE","PROOF-MUTATION","PROOF-SANDBOX"],"status":"PASS"},
    {"requirementId":"REQ-4","actualArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts"],"proofRefs":["PROOF-PRINT-REGRESSION"],"status":"PASS"},
    {"requirementId":"REQ-5","actualArtifacts":["docs/reference/CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_PROOF_2026-10-01.md"],"proofRefs":["PROOF-BOUNDARY"],"status":"PASS"},
    {"requirementId":"REQ-6","actualArtifacts":["docs/reviews/evidence/cvf-ncr-html-b1-preview-passive-resource-worker-proof-2026-10-01.json"],"proofRefs":["PROOF-OBSERVATIONS"],"status":"PASS"},
    {"requirementId":"REQ-7","actualArtifacts":["docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_WORKER_RETURN_2026-10-01.md"],"proofRefs":["PROOF-RETURN"],"status":"PASS"}
  ],
  "parkedCheckpoints": ["real GitHub-ledger cutover","real accepting actor and account","artifact store location and writer model","backup location and key custody","retention and deletion schedule","RPO and RTO","cost budget","P08","artifact acceptance","pilot or live effect","P11","deployment","Q001 and Q004 exit"]
}
```

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_worker_experience_retrospective.py` (field values follow the accepted Print R2 return, which passed the same gate) |
| literalTokensReviewed | `COMPLETE_PENDING_REVIEW`; `acceptance-evidence-json`; `WORKER_MUST_NOT_COMMIT honored`; `run_worker_return_fast_gate.py`; `git diff --name-status`; `PENDING_REVIEWER_EXECUTION` |
| gateRunPurpose | Confirm the exact seven-path ledger join and reviewer-pending status |
| claimBoundary | Structural gates cannot substitute for the Local reviewer-owned probe or prove behavior beyond the synthetic input. |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Internal worker |
| Provider or surface | Shared private CVF workspace; local Next dev server and one headless Chromium; synthetic fixture |
| Session or invocation | NCR HTML B1 Preview passive resource worker, 2026-10-01 |
| Working directory | Repository root and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` |
| Command or tool surface | bound pre-implementation gate; Playwright; Vitest; tsc; eslint; worker fast gate |
| Target paths | Exact seven-path worker acceptance ledger |
| Allowed scope source | Bound B1 Preview work order and paired GC-018 baseline |
| Before status evidence | `git status --short --untracked-files=all` empty at HEAD `7548ac66b` before any edit; three output paths absent |
| After status evidence | Four modified tracked paths and three untracked worker paths, no staged path, no worker commit |
| Diff evidence | `git diff --name-status` lists the four modified paths; the three new paths appear as untracked in `git status --short --untracked-files=all` |
| Approval boundary | Worker evidence only; Local reviewer owns the independent probe, acceptance and commit |
| Claim boundary | Synthetic one-profile Chromium Preview observation; no acceptance, Q001 or Q004 closure, universal HTML safety or live assertion |
| Agent type | INTERNAL_AGENT worker |
| Invocation ID | cvf-ncr-html-b1-preview-passive-resource-worker-20261001 |
| Expected manifest | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts`; `docs/reference/CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_PROOF_2026-10-01.md`; `docs/reviews/evidence/cvf-ncr-html-b1-preview-passive-resource-worker-proof-2026-10-01.json`; `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_WORKER_RETURN_2026-10-01.md` |
| Actual changed set | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts`; `docs/reference/CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_PROOF_2026-10-01.md`; `docs/reviews/evidence/cvf-ncr-html-b1-preview-passive-resource-worker-proof-2026-10-01.json`; `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_WORKER_RETURN_2026-10-01.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | Synthetic one-profile real-browser Preview passive-resource isolation and canonical identity proof |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: observed in one Chromium run; reviewer pending |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no governance receipt is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: positive control, actual-Preview negatives, policy-only mutation and Print regression in the proof JSON |
| invocationBoundary | local Next dev server and headless browser; synthetic intercepted export |
| interceptionBoundary | context routes fulfill the probe endpoints locally on both origins, no forwarding; the export request is fulfilled by `page.route`; no production wrapper is claimed |
| claimLanguage | Observed denial of passive resources by the Preview policy before payload parsing, reviewer pending |
| forbiddenExpansion | No route, ledger, database, provider, real data, artifact acceptance, public sync or deployment |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Input type | internal governed input (no external intake) |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Internal source | `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_LOAD_OWNER_AUDIT_2026-10-01.md` |
| Chain map route | Local source-derived Preview adaptation |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | No external advisory is private CVF proof. |

## External/Local Coordination Binding

Role: shared-workspace `INTERNAL_AGENT`. Phase: bounded B1 Preview worker. Decision owner: Local.

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
| Defect class | RUNTIME_SIGNAL_GAP: a script sandbox does not deny passive loads; the gap only shows with a counter on the intercepted endpoint and a no-policy positive control, and a control whose two stylesheets styled the same class silently under-reported one hit |
| Learning lane | RUNTIME_BEHAVIOR_LEARNING |
| Finding | A resource-denial proof needs distinct per-origin selectors in the control, a derived-document ordering check, a policy-only mutation on the real product path and byte-identity checks for canonical outputs |
| Disposition | RUNTIME_LEARNING_CANDIDATE: Local decides whether to keep the control and mutation as review-probe material |
| Next control action | Local reviewer runs one distinct early-resource fixture in the actual Preview before Print for false-denial risk |

## Epistemic Process Block

### Expected Result / Prediction

An empty sandbox without a resource policy loads passive resources; a CSP meta placed first in the derived Preview document stops them for early markup, duplicate heads and a permissive payload policy without changing canonical outputs.

### Evidence Comparison

The prediction held: the control produced 20 of 20 hits, the actual Preview produced 0 for both fixtures, and removing only the policy restored 20 of 20 and failed the same oracle. The first control run produced 19 and exposed a fixture selector collision, fixed in scope.

### Contradiction Or Gap Disposition

Remaining gaps are disclosed above (navigation, other browsers, rendering mode, real packets). The Local independent probe remains pending.

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
observedStep: the auth helper redirects to port 3000 under the 3001 mock config, requiring the documented runtime override, and a two-stylesheet control collided on one class
preventiveControlCandidate: HELPER_DIAGNOSTIC

## Claim Boundary

The worker return is `COMPLETE_PENDING_REVIEW`; it is not acceptance, artifact approval, a durable store, an operator decision, universal HTML safety, navigation safety, other-browser behavior, paper or dialog output, Q001 or Q004 exit, P11 release or a public claim. Undecided operator checkpoints remain: real accepting actor, real data and store profile, store location and writer model, backup and key custody, retention, RPO and RTO, cost, P08 scope, artifact acceptance, pilot or live effect, P11 and deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## git status --short

Four modified tracked Web files and three untracked worker-owned files, zero staged files. Exact path list follows.

## Changed Files

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts`
- `docs/reference/CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_PROOF_2026-10-01.md`
- `docs/reviews/evidence/cvf-ncr-html-b1-preview-passive-resource-worker-proof-2026-10-01.json`
- `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_WORKER_RETURN_2026-10-01.md`

## Command Evidence

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_2026-10-01.md`: COMPLIANT (exit 0) on the clean worktree at `7548ac66b` before any edit.
- `npx playwright test tests/e2e/artifact-export-preview-sandbox.spec.ts tests/e2e/artifact-export-print-browser.spec.ts --config playwright.config.mock.ts` with the port override: first Preview-only runs showed the control and mutation at 19 of 20 hits (fixture selector collision), fixed; final combined run PASS, 10 passed, exit 0.
- `npx vitest run src/components/ArtifactExportPanel.test.tsx`: PASS, 55 passed.
- `npm run check` (`tsc --noEmit`): PASS, exit 0.
- `npx eslint --max-warnings=0` on the four code paths: PASS, exit 0.
- `git status --short --untracked-files=all` before the return files: four modified paths only.
- `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_2026-10-01.md`: PASS (exit 0, 69/69 hook checks) on the final seven-path state. Earlier worker runs before the return was complete failed on missing return sections (review cost sweep value, operation trace and epistemic blocks in the proof reference); those were repaired in scope and the gate rerun.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`worker_execution`, role=`worker`, lifecyclePhase=`worker-return`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class worker_execution --role worker --lifecycle-phase worker-return --json`; not rerun by the worker; the dispatch-time query returned 0 items.

Returned defects: NONE_RETURNED

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. All seven worker outputs are uncommitted, and the distinct Local reviewer owns acceptance and material commit.
