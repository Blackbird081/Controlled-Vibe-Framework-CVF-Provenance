# CVF NCR HTML B2c Synthetic Browser Download Worker Return

Memory class: worker-return-evidence

docType: review

Status: COMPLETE_PENDING_REVIEW

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_2026-09-30.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_2026-09-30.md`

executionBaseHead: `60c7e81b4d7a7aa6020631a4eddbcc1dc1e8bb5b`

contractProfile: WORKER_RETURN_FULL_GATE_V1

## Rework Convergence Self-Proof

rootCauseClusterId: NOT_APPLICABLE_INITIAL_DISPATCH
recurrenceDisposition: FIRST_OCCURRENCE
priorRelatedFinding: NOT_APPLICABLE_WITH_REASON - initial dispatch
operatorNoticeDisposition: NOT_APPLICABLE_WITH_REASON - no operator decision is involved
successorFreezeDisposition: NOT_APPLICABLE_WITH_REASON - no successor tranche is opened
reworkGeneration: 0
consolidatedDefectClassSweep: COMPLETE_ALL_KNOWN_DEPENDENCIES
productionBindingEvidence: NOT_APPLICABLE_WITH_REASON - test-only; no production file was edited or imported
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
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-ncr-html-b2c-synthetic-browser-download","chainMode":"INITIAL","chainOrdinal":0,"predecessor":null,"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":[],"reopened":[],"current":[]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":0},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## Purpose

Return the B2c synthetic real-browser download proof: a focused Playwright spec that drives the existing Artifacts panel with an intercepted synthetic export response, observes a real download event, and compares the saved-file bytes with an independent oracle and the B2b identity. Worker evidence for Local, not artifact acceptance.

## Target / Source

Bound work order `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_2026-09-30.md` (sha256 `c6d38a4602ac38d58bb4f78ba39d3544f15cfa150aa4933909d98212c957a093`) and paired baseline `docs/baselines/CVF_GC018_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_2026-09-30.md` (sha256 `d3fcca8cb84d92eb8211650eea041ca9422ed98b461e69e35c7e880881eef3af`). Read and unmodified: `ArtifactExportPanel.tsx`, `artifact-export-panel.spec.ts`, `playwright.config.mock.ts`, `tests/e2e/utils.ts`, `html-artifact-byte-handoff.ts`. Created: the four manifest paths below.

## Scope / Methodology

Startup acknowledged: current mode=`cvf_ncr_p10_closed_p11_parked`; active handoff `AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move: execute the bound B2c worker packet; role INTERNAL_AGENT worker; decision owner Local. At clean HEAD `60c7e81b4` the four create paths were absent and the bound pre-implementation gate passed before any edit.

The spec intercepts the export endpoint with `page.route`, keyed by requested title, and fulfills a synthetic JSON envelope. Fixture A and B are well-formed HTML strings with a BOM, CRLF and lone LF, Vietnamese, CJK and an astral emoji; titles differ by a same-length ASCII word. The oracle is Node `Buffer` plus `node:crypto`; B2b is imported only in the test process. Per build the test reads the Preview iframe `<h1>`, then for A edits the form without rebuilding and re-reads the iframe (still Alpha, not the edited text), downloads through the real download event, saves to a disposable directory outside the repository, and reads bytes back. Bytes are checked by length, SHA-256, buffer equality, B2b `verifyHtmlByteHandoff`, and explicit BOM, CRLF, LF and multi-byte sequences. B builds after A, iframe shows Bravo, and lengths equal while digests differ. Cleanup is asserted in the test.

## Findings / Position

Focused Playwright: 1 test, 1 passed, exit 0, Chromium 145.0.7632.6 headless, `CVF_PLAYWRIGHT_PORT=3000`, `--output` pointing to a temp directory outside the repository. Saved Alpha: 231 bytes, sha256 `e9bb9c459fc48e0cdb8852f2ea630ec1461cfda2703a1c75f1324c3f43086ed0`, equal to oracle and B2b. Saved Bravo: 231 bytes, sha256 `8b8c24305e417e3c557a8e2e0966141ffa1f761d9136044516e2a2c23a49f1ef`, equal to oracle and B2b. Same length, different digest. The intercept saw only the two titles; the edited form title never reached it. The disposable download directory was removed and confirmed gone. No panel defect was observed: the download worked despite immediate object-URL revocation for these fixtures.

The first run failed for an environment reason: the default mock port 3001 disagrees with the local `AUTH_URL` port 3000, so login got `ECONNREFUSED ::1:3000` before the panel was reached. No config was edited; the port is set through the existing environment variable. Reviewer note: that failed run also modified the tracked `test-results/.last-run.json`, which Local restored; the passing run used `--output` outside the repository and left no repository artifact.

## Risk / Corrective Action

The proof covers two synthetic fixtures in one Chromium profile only. The Preview iframe check reads the sandboxed iframe through Playwright's frame locator, which observes the rendered `<h1>` but is not a byte-level view of what the iframe received. The test depends on port 3000 because of the local auth environment; a different local `AUTH_URL` would need the port variable changed. The run recorded fixture digests in the proof JSON but no raw HTML. Print, clipboard, other browsers, production network and durable acceptance remain unproven, as the reference states.

## Decision / Disposition

Disposition: COMPLETE_PENDING_REVIEW. The original worker gate was blocked by two Local-owned surfaces; Local repaired them in `26f24a817` and synchronized the handoff marker in `84c3f14c8`. The required worker-return fast gate then passed, including reviewer-fast 69/69. The worker claims that, for these fixtures in this browser profile, the panel saves bytes identical to the displayed result, with same-length version discrimination. Acceptance, panel wiring to B2b, any store, and the open operator decisions remain with Local and the operator. Local's distinct probe is still pending.

## Open Gate Items For Local

`python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_2026-09-30.md` exited 1. Of 69 reviewer-fast checks, two fail for reasons outside the four worker paths: (1) `changed corpus registry coverage`: the new spec is not covered by `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json` scopePaths, and the registry is outside the worker manifest; (2) `session mode consistency`: `AGENT_HANDOFF_V63_2026-09-18.md` has no `startup current mode=` token (its startup line reads `Startup acknowledged: mode=...`), the same continuity token drift Local repaired for B2b. A third item, the worker-return quality gate, only reports that this return lacks PASS evidence for the fast gate, which follows from the two failures. All other checks passed after the worker repaired its own findings (non-ASCII escapes in the spec, structural sections in the reference, retrospective enums, review-cost sweep token, and trace changed-set paths). Narrowest amendment: Local adds the spec to the corpus registry and restores the handoff token, then reruns the gate; no worker redispatch is needed.

Local resolution: a new exact one-path GC-051 source entry and generated aggregate were committed with the handoff startup-token repair at `26f24a817`; the GC-020 marker was synchronized at `84c3f14c8`. No worker output was included in either Local commit. The required fast gate passed on the exact four worker paths after this repair. The original `executionBaseHead` above and in the proof JSON remains `60c7e81b4`; only the acceptance-evidence JSON comparison anchor below is the post-repair `84c3f14c8` HEAD. This separates the original execution chronology from the machine's four-path Git comparison; it does not claim the worker began at the later commit.

## Work-Order Acceptance Evidence

```acceptance-evidence-json
{
  "schemaVersion": "cvf.workOrderAcceptanceEvidence@1.0.0",
  "executionBaseHead": "84c3f14c88c0f12b74f23027221d52bd88dfc231",
  "results": [
    {"requirementId":"REQ-BROWSER","actualArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-byte-download.spec.ts"],"proofRefs":["PROOF-DOWNLOAD","PROOF-VERSION"],"status":"PASS"},
    {"requirementId":"REQ-PROOF","actualArtifacts":["docs/reviews/evidence/cvf-ncr-html-b2c-browser-download-worker-proof-2026-09-30.json"],"proofRefs":["PROOF-BYTES","PROOF-CLEANUP"],"status":"PASS"},
    {"requirementId":"REQ-CONTRACT","actualArtifacts":["docs/reference/CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_PROOF_2026-09-30.md"],"proofRefs":["PROOF-BOUNDARY"],"status":"PASS"},
    {"requirementId":"REQ-RETURN","actualArtifacts":["docs/reviews/CVF_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_WORKER_RETURN_2026-09-30.md"],"proofRefs":["PROOF-RETURN"],"status":"PASS"}
  ],
  "parkedCheckpoints": ["real GitHub-ledger cutover","real accepting actor and account","artifact store location and writer model","backup location and key custody","retention and deletion schedule","RPO and RTO","cost budget","P08","artifact acceptance","pilot or live effect","P11","deployment","Q001 and Q004 exit"]
}
```

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py` was not read by this worker; the B2b accepted return was used as the shape template |
| literalTokensReviewed | `COMPLETE_PENDING_REVIEW`; `acceptance-evidence-json`; `WORKER_MUST_NOT_COMMIT honored`; `run_worker_return_fast_gate.py`; `git diff --name-status`; `PENDING_REVIEWER_EXECUTION` |
| gateRunPurpose | Confirm the exact four-path ledger join and reviewer-pending status |
| claimBoundary | Structural gates cannot substitute for the Local reviewer-owned browser probe or prove behavior beyond the synthetic fixtures. |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Internal worker |
| Provider or surface | Shared private CVF workspace; one local headless Chromium, synthetic intercepted response |
| Session or invocation | NCR HTML B2c synthetic browser download worker, 2026-09-30 |
| Working directory | Repository root and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` |
| Command or tool surface | bound pre-implementation gate; Playwright; tsc; eslint; worker fast gate |
| Target paths | Exact four-path worker acceptance ledger |
| Allowed scope source | Bound B2c work order and paired GC-018 baseline |
| Before status evidence | `git status --short --untracked-files=all` had only a modified `AGENT_HANDOFF_V63_2026-09-18.md` at session start; Local later reported it clean; four create paths absent at HEAD `60c7e81b4` |
| After status evidence | Four untracked worker paths, no modified tracked path, no staged path, no worker commit |
| Diff evidence | every worker path is new, so `git diff --name-status` prints nothing; `git status --short --untracked-files=all` lists the four paths as untracked |
| Approval boundary | Worker evidence only; Local reviewer owns the independent probe, acceptance and commit |
| Claim boundary | Synthetic browser saved-file bytes only; no acceptance, Q001 or Q004 closure, or live assertion |
| Agent type | INTERNAL_AGENT worker |
| Invocation ID | cvf-ncr-html-b2c-synthetic-worker-20260930 |
| Expected manifest | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-byte-download.spec.ts`; `docs/reference/CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_PROOF_2026-09-30.md`; `docs/reviews/evidence/cvf-ncr-html-b2c-browser-download-worker-proof-2026-09-30.json`; `docs/reviews/CVF_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_WORKER_RETURN_2026-09-30.md` |
| Actual changed set | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-byte-download.spec.ts`; `docs/reference/CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_PROOF_2026-09-30.md`; `docs/reviews/evidence/cvf-ncr-html-b2c-browser-download-worker-proof-2026-09-30.json`; `docs/reviews/CVF_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_WORKER_RETURN_2026-09-30.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | Synthetic real-browser saved-file byte proof for two fixtures |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: observed in one Chromium run; reviewer pending |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no governance receipt is created or consumed |
| actionEvidence | ACTION_EVIDENCE_PRESENT: Playwright pass and saved-byte receipt in the proof JSON |
| invocationBoundary | local headless browser, intercepted export response, disposable temp download directory |
| interceptionBoundary | no proxy, wrapper or runtime gate is claimed |
| claimLanguage | Observed saved-file bytes equal the displayed synthetic fixture bytes, reviewer pending |
| forbiddenExpansion | No route, ledger, database, provider, real data, artifact acceptance, public sync or deployment |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Input type | internal governed input (no external intake) |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Internal source | `docs/reviews/CVF_CVF_NCR_HTML_B2C_BROWSER_FILE_PROOF_SCOPE_AUDIT_2026-09-30.md` |
| Chain map route | Local source-derived owner correction |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | No external advisory is private CVF proof. |

## External/Local Coordination Binding

Role: shared-workspace `INTERNAL_AGENT`. Phase: bounded B2c synthetic worker. Decision owner: Local.

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON

Reason: named source files were read directly; no external-source rescan occurred.

## Corpus Completeness And Report Integrity

N/A with reason: four exact worker outputs are the bounded set; no all-files inventory is claimed.

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - the tranche makes no corpus completeness claim.

## Finding-To-Governance Learning Disposition

| Field | Value |
|---|---|
| Defect class | WORKER_EXECUTION_ERROR: my first spec version only asserted that the Preview iframe was visible, which does not show which version is displayed; Local review caught it |
| Learning lane | RUNTIME_BEHAVIOR_LEARNING |
| Finding | A "displayed version" claim needs a direct read of the rendered content, not just element visibility; an environment port mismatch can fail a run before it reaches the unit under test |
| Disposition | RUNTIME_LEARNING_CANDIDATE: Local decides whether to keep the iframe content read and the port note as review-probe material |
| Next control action | Local reviewer runs its own distinct fixture through a reviewer-owned browser run |

## Epistemic Process Block

### Expected Result / Prediction

The saved file for each displayed build equals that build's fixture bytes; a form edit without rebuild does not change the displayed or downloaded version; same-length titles give equal length and different digests.

### Evidence Comparison

The single run that reached the panel matched every prediction: iframe headings read Alpha, Alpha after form edit, then Bravo; both saved digests equal oracle and B2b; lengths equal at 231 and digests differ.

### Contradiction Or Gap Disposition

No prediction failed. The earlier run failed on a port mismatch before the panel loaded, which is an environment gap, not a contradiction. The suspected immediate object-URL revocation risk did not materialize for these fixtures. The Local independent probe remains pending.

### Claim Update

The worker claims observed saved-file byte identity for two synthetic displayed results in one Chromium profile, reviewer acceptance pending. Q001 and Q004 remain open and nothing is accepted.

## Return-Time Closeability Recheck

closeabilityDisposition: CLOSEABLE
outsideAuthorityBlockers: NONE
nextRepairRoute: NONE
workerRedispatchAllowed: NO

The four-path worker manifest is complete and no forbidden path was edited.

independentProbeDisposition: PENDING_REVIEWER_EXECUTION
probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

## Worker Experience Retrospective

WORKER_EXPERIENCE_RETRO:
frictionLevel: MEDIUM
frictionType: GATE_SURPRISE
observedStep: the mock config port differs from the local auth URL port; the file-writing tool turned unicode escapes into raw characters that the encoding gate rejected; a new spec needs a corpus registry entry; a transient permission-classifier outage blocked tools for a while
preventiveControlCandidate: WORK_ORDER_TEMPLATE

## Claim Boundary

The worker return is `COMPLETE_PENDING_REVIEW`; the originally disclosed Local-owned gate items are resolved and the Local independent probe remains pending. This is not acceptance, artifact approval, a durable store, an operator decision, proof of production network, print, clipboard, other-browser or live behavior, provider proof, Q001 or Q004 exit, P11 release or a public claim. Undecided operator checkpoints remain: real accepting actor, real data and store profile, store location and writer model, backup and key custody, retention, RPO and RTO, cost, P08 scope, artifact acceptance, pilot or live effect, P11 and deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## git status --short

Four untracked worker-owned files, no modified tracked file, zero staged files. Exact path list follows.

## Changed Files

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-byte-download.spec.ts`
- `docs/reference/CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_PROOF_2026-09-30.md`
- `docs/reviews/evidence/cvf-ncr-html-b2c-browser-download-worker-proof-2026-09-30.json`
- `docs/reviews/CVF_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_WORKER_RETURN_2026-09-30.md`

## Command Evidence

- `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_2026-09-30.md`: PASS (exit 0) before any worker edit.
- `CVF_PLAYWRIGHT_PORT=3000 npx playwright test tests/e2e/artifact-export-byte-download.spec.ts --config playwright.config.mock.ts --output <temp outside repo>`: PASS, 1 passed, exit 0. An earlier run on the default port failed with ECONNREFUSED before reaching the panel.
- `npm run check` (`tsc --noEmit`): PASS, exit 0.
- `npx eslint --max-warnings=0 tests/e2e/artifact-export-byte-download.spec.ts`: PASS, exit 0.
- `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B2C_SYNTHETIC_BROWSER_DOWNLOAD_2026-09-30.md`: original exit 1 on two Local-owned surfaces named above; after Local repair and handoff sync, PASS exit 0 with reviewer-fast 69/69.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`worker_execution`, role=`worker`, lifecyclePhase=`worker-return`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class worker_execution --role worker --lifecycle-phase worker-return --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. All four worker outputs are uncommitted, and the distinct Local reviewer owns acceptance and material commit.
