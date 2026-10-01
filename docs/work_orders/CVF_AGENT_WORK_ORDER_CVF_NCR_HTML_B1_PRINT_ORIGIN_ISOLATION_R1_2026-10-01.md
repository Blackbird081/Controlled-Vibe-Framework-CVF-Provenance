# CVF Agent Work Order - NCR HTML B1 Print Origin Isolation R1

Memory class: governed-worker-dispatch

docType: work_order

Status: DISPATCH_READY

providerExecutionAuthority: FORBIDDEN

Batch ID: CVF-NCR-HTML-B1-PRINT-R1

Dispatch base head: `b3c5a0aa8`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Worker: shared-workspace `INTERNAL_AGENT` implementation role

Reviewer/closer: Local reviewer/closer

Worker return path: `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_WORKER_RETURN_2026-10-01.md`

workerReturnPath: `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_WORKER_RETURN_2026-10-01.md`

## Dispatch Prompt Envelope

Role: shared-workspace INTERNAL_AGENT rework implementer; Local reviews and closes. Canonical packet: this order and paired GC-018 baseline. Commit mode: `WORKER_MUST_NOT_COMMIT`. executionBaseHead: capture released HEAD before any worker edit.

Current-time notes: R0 Print candidate was rejected by Local review `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_AUDIT_2026-10-01.md` for same-origin popup authority. Clean released HEAD has the six inherited candidate paths preserved in Git stash `beeaf933bf03924532eb02bea331455e2233d743`; they are execution input only, not CVF authority. First run bound pre-implementation PASS on clean HEAD; only then apply that exact stash, verify the six path hashes below, and perform R1 repair. Do not commit or drop the stash.

Do-not-misread notes: opener-null does not isolate origin storage or ambient cookie requests. Worker-return fast gate PASS for R0 was structural, not acceptance. A test that merely sees no script side effect without a positive executable control is insufficient. Browser print invocation is not physical output.

Required first actions: read continuity, this order, paired baseline, Local R0 review, original order and named Web owner; capture clean HEAD/status; run bound pre-implementation gate; apply verified stash only after PASS. If stash/hash/changed set conflicts, stop `BLOCKED_WITH_REASON` without guessing.

Return contract: revise only the six inherited worker paths; return `COMPLETE_PENDING_REVIEW` or `BLOCKED_WITH_REASON`, focused browser/unit/TypeScript/lint and worker-return gate evidence, no worker commit.

## Purpose

Rework the rejected B1 Print candidate so HTML placed in the print surface cannot obtain app-origin script, storage or ambient authenticated-request authority. Keep the native Print invocation and displayed-version behavior proved by R0, with a discriminating real-browser positive/negative security oracle. Q001/Q004 remain open.

## Authority Chain

| Authority | Evidence | Disposition |
|---|---|---|
| Operator delegation | Local may source-audit and issue bounded internal work orders | ACCEPT for R1 packet only |
| Current continuity | active bootstrap and handoff next move | ACCEPT for packet authoring |
| Roadmap | D058 and Q001/Q004 | ACCEPT for R1 security rework |
| Local finding set | `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_AUDIT_2026-10-01.md`; SHA-256 `13a1fbba70c2e6f6a44047cd486a989053c51982f15a8f3ed619b57bf6ba30ca` | ACCEPT, one consolidated critical finding |
| Original packet | `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_2026-10-01.md` | ACCEPT as R0 historical contract, superseded for R1 |
| Paired GC-018 | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B1_PRINT_ORIGIN_ISOLATION_R1_2026-10-01.md` | ACCEPT subject to bound release gate |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Local rejects same-origin popup candidate | GOVERNED_DECISION | `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_AUDIT_2026-10-01.md` | Findings and Decision | `REWORK_REQUIRED_SECURITY_BOUNDARY` | Local reviewer | ACCEPT |
| Initial Print order covered opener only | GOVERNED_CONTRACT | `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_2026-10-01.md` | Implementation Contract | `window.opener` | B1 Print packet | ACCEPT |
| Committed panel has Print callback and sandboxed preview | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `handlePrint` and preview | `window.open`, `sandbox` | Artifacts panel | ACCEPT |
| Committed export route escapes user text | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | `escapeHtml`, `buildHtml` | `escapeHtml` | export route | ACCEPT |
| D058 holds R0 and permits R1 preparation | GOVERNED_DECISION | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D058 | B1 Print | NCR roadmap | ACCEPT |
| GC-051 source entry registers the named browser spec | REGISTRY | `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b1-print-browser-repair-source.json` | scopePaths | `artifact-export-print-browser.spec.ts` | GC-051 | ACCEPT |

## Negative Search And Collision Discipline

At clean dispatch base `b3c5a0aa8`, exactly the six inherited candidate paths are represented by stash `beeaf933bf03924532eb02bea331455e2233d743`: two tracked Web paths revert to HEAD and four create paths are absent. Verify stash identity and six SHA-256 hashes before applying it. No other worker path is authorized. Named-path audit is not full Web coverage.

## Current Runtime Freshness Verification

Local inspected R0 diff and return, independently reran one focused Chromium case, and compared the same-origin popup finding to official browser-origin semantics at review D058. R0 showed native print invocation and version binding, but its fixture script executed with app origin. R1 packet authoring itself has not tested an isolation design.

## Task Governance Routing Manifest

```json
{"schemaVersion":"cvf.taskGovernanceManifest.v1","taskId":"CVF-NCR-HTML-B1-PRINT-R1","requestedProfile":"P3_ELEVATED","classification":{"taskKind":"STATEFUL_LOCAL_IMPLEMENTATION","authorityImpact":"ENRICHES_EXISTING_OWNER","externalEffect":"LOCAL_REVERSIBLE","dataSensitivity":"PRIVATE_REPO","reversibility":"STATEFUL_REVERSIBLE","sourceScale":"NAMED_FILES","delegation":"MULTI_ROLE_NO_COMMIT","novelty":"OWNER_COMPOSITION"},"pathFamilies":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/","docs/baselines/","docs/roadmaps/","docs/reference/","docs/reviews/"],"claims":["one-profile synthetic Print origin-isolation rework"],"requiredProof":["positive unsandboxed app-origin capability control","actual Print negative storage/cookie/request oracle","mutation discriminates lost isolation","native print invocation","displayed-version binding","no fixture outbound request","focused unit/browser/TypeScript/lint"],"operatorCheckpoints":["Q001/Q004","real actor/data/store","pilot/live","cost","public sync","deployment"],"forbiddenEffects":["worker commit","route/provider/engine/ledger/storage edit","real data","artifact acceptance","public sync","deployment"],"sourceEvidence":{"selectedFilesFullyRead":false,"corpusReceiptRef":"docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_AUDIT_2026-10-01.md","completenessClaimChanged":false}}
```

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | Internal governed input (no external intake) |
| Internal source | `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_AUDIT_2026-10-01.md` |
| Chain map route | Local source-derived R1 correction |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | Browser standards inform design; only Local private-CVF proof can accept it |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | Artifacts Print callback and focused browser oracle | synthetic local UI rework only | D058; pending R1 run | Web panel | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external interface | no ingress or mutation grant | R1 scope | deferred | DEFERRED_WITH_REASON |

## Agent Roles And Scope

One shared-workspace INTERNAL_AGENT repairs the six inherited candidate paths. Local independently probes, reviews and commits if safe. Operator retains Q001/Q004 effect choices. This is not external Web research.

Allowed: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts`; `docs/reference/CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_PROOF_2026-10-01.md`; `docs/reviews/evidence/cvf-ncr-html-b1-print-repair-worker-proof-2026-10-01.json`; `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_WORKER_RETURN_2026-10-01.md`.

Forbidden: route, auth, config, package, lock, engine, ledger, storage, README, roadmap, governance or continuity edits; real data, provider calls, worker commit, public sync and deployment. Do not create extra tracked test outputs.

## Intake Role Routing Decision

| Field | Value |
|---|---|
| intake summary | R0 callback fixes noopener/null but renders HTML in app-origin popup |
| scope classification | one consolidated R1 security rework of B1 Print |
| risk sensitivity | false isolation claim when script control is inert or network stub absent |
| selected role route | SINGLE_AGENT_MULTI_ROLE worker with distinct Local reviewer |
| role separation basis | worker cannot self-accept or authorize effect |
| escalation condition | safe design requires a route/header/auth/config change or more than six paths |

## Single-Agent Multi-Role Control Block

| Field | Disposition |
|---|---|
| Applicability | one worker performs R1 and produces pending evidence; Local reviews |
| actor | INTERNAL_AGENT worker |
| role set | implementer and evidence producer, not closer |
| Role separation ledger | pending R1 return followed by Local security disposition |
| Evidence basis independent of memory | committed R0 review, stash SHA and path hashes, Git changed set, browser receipt, Local probe |
| Stop boundary | no worker commit or effect choice |
| Gate sequence | packet release, clean pre-implementation, stash apply, focused tests, worker-return fast, Local reviewer gate |
| Self-review boundary | worker PASS does not prove safe origin boundary |
| escalation condition | origin authority cannot be excluded in authorized paths |

## Required First Reads

Read `AGENTS.md`, front door/bootstrap/active handoff, paired packet, `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_AUDIT_2026-10-01.md`, `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_2026-10-01.md`, panel and its component test, B1 sandbox browser spec, existing Print browser spec after stash apply, export route, `DESIGN.md`, guard orientation, literal gotchas and output checkers. Capture HEAD and `git status --short --untracked-files=all`.

## Worker Autonomy / No-Question Rule

Choose an outcome-preserving origin/script-isolation design within the six paths. A sandboxed printable frame, effective pre-content CSP or another mechanism may be considered, but none is pre-approved. Prove it in real Chromium with an executable positive control, blocked actual Print payload and mutation. If a safe design or browser oracle cannot be achieved, return `BLOCKED_WITH_REASON` without widening scope or claiming success.

## Pre-Flight Checks

Begin only after paired packet material commit, exact-hash continuity and bound pre-dispatch PASS. On clean HEAD, record status and run `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-implementation --head HEAD --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PRINT_ORIGIN_ISOLATION_R1_2026-10-01.md` before applying stash. Then verify `git rev-parse beeaf933bf03924532eb02bea331455e2233d743` equals the named object, apply exactly that stash without dropping it, and compare all six restored raw-file SHA-256 values to the Inherited Candidate Fingerprint table. Any mismatch or extra changed path is BLOCKED. The stash is an execution aid, not source authority.

## Write Ownership

Worker edits only the six restored candidate paths, no commit. Local owns independent browser probe, review, material commit and continuity. GC-051 already registers the browser spec; do not modify its entry. Scope expansion needs a new Local decision.

## Work-Order Fulfillment Manifest

| Path | Worker action | Handoff requirement |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | revise inherited candidate | Print implementation with browser-proven isolation |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | revise inherited candidate | unit regression for fail-closed and version behavior |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts` | revise inherited candidate | positive/negative origin-authority and native Print browser oracles |
| `docs/reference/CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_PROOF_2026-10-01.md` | revise inherited candidate | R1 bounded proof and untested contexts |
| `docs/reviews/evidence/cvf-ncr-html-b1-print-repair-worker-proof-2026-10-01.json` | revise inherited candidate | observed browser controls and counts |
| `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_WORKER_RETURN_2026-10-01.md` | revise inherited candidate | R1 return bound to this order with gate and no-commit evidence |

## Required Artifact Manifest

Six exact inherited paths are mandatory; all exist after the verified stash is applied. No seventh worker deliverable is authorized.

| Path | Required at handoff | Worker action |
|---|---|---|
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | Yes | revise inherited candidate |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | Yes | revise inherited candidate |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts` | Yes | revise inherited candidate |
| `docs/reference/CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_PROOF_2026-10-01.md` | Yes | revise inherited candidate |
| `docs/reviews/evidence/cvf-ncr-html-b1-print-repair-worker-proof-2026-10-01.json` | Yes | revise inherited candidate |
| `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_WORKER_RETURN_2026-10-01.md` | Yes | revise inherited candidate |

## Dated Owner Dependency Discovery

| Owned dated reference | Classification |
|---|---|
| `docs/reference/CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_PROOF_2026-10-01.md` | NOT_BINDING_REFERENCE_WITH_REASON: bounded synthetic R1 browser proof, not a standard |

## Work-Order Acceptance Requirement Ledger

```acceptance-ledger-json
{"schemaVersion":"cvf.workOrderAcceptanceLedger@1.0.0","requirements":[{"requirementId":"REQ-PANEL","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx","EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx"],"requiredProofIds":["PROOF-SAFE-DESIGN","PROOF-UNIT"]},{"requirementId":"REQ-BROWSER","mandatory":true,"expectedArtifacts":["EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts"],"requiredProofIds":["PROOF-POSITIVE","PROOF-NEGATIVE","PROOF-MUTATION","PROOF-PRINT","PROOF-VERSION"]},{"requirementId":"REQ-PROOF","mandatory":true,"expectedArtifacts":["docs/reviews/evidence/cvf-ncr-html-b1-print-repair-worker-proof-2026-10-01.json"],"requiredProofIds":["PROOF-OBSERVATIONS"]},{"requirementId":"REQ-CONTRACT","mandatory":true,"expectedArtifacts":["docs/reference/CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_PROOF_2026-10-01.md"],"requiredProofIds":["PROOF-BOUNDARY"]},{"requirementId":"REQ-RETURN","mandatory":true,"expectedArtifacts":["docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_WORKER_RETURN_2026-10-01.md"],"requiredProofIds":["PROOF-RETURN"]}],"proofCatalog":[{"proofId":"PROOF-SAFE-DESIGN","kind":"Print payload cannot obtain app-origin script/storage/cookie/request authority","locator":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx"},{"proofId":"PROOF-UNIT","kind":"fail-closed and displayed-result regressions","locator":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx"},{"proofId":"PROOF-POSITIVE","kind":"unsandboxed same-origin control proves synthetic payload could access seeded capabilities","locator":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts"},{"proofId":"PROOF-NEGATIVE","kind":"actual Print payload cannot read/mutate seeded app-origin storage/cookie or call controlled same-origin endpoint","locator":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts"},{"proofId":"PROOF-MUTATION","kind":"removing isolation makes negative oracle fail","locator":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts"},{"proofId":"PROOF-PRINT","kind":"native Chromium popup and print invocation, no fake successful handle","locator":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts"},{"proofId":"PROOF-VERSION","kind":"printed document bound to displayed result after unsaved edit","locator":"EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts"},{"proofId":"PROOF-OBSERVATIONS","kind":"secret-free browser/profile, control/negative/mutation, request counts and gates","locator":"docs/reviews/evidence/cvf-ncr-html-b1-print-repair-worker-proof-2026-10-01.json"},{"proofId":"PROOF-BOUNDARY","kind":"bounded R1 design and untested contexts","locator":"docs/reference/CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_PROOF_2026-10-01.md"},{"proofId":"PROOF-RETURN","kind":"R1 exact changed set, gate and no commit","locator":"docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_WORKER_RETURN_2026-10-01.md"}]}
```

## Roadmap-To-Work-Order Trace Matrix

| Roadmap decision | Worker obligation | Deferred boundary |
|---|---|---|
| D036 | preserve displayed-version binding | no builder redesign |
| D058 | remove same-origin popup authority gap with discriminating browser controls | no paper/PDF or universal HTML safety claim |
| Q001/Q004 | keep actor/store/effect parked | no durable writer or artifact acceptance |

## Implementation Contract

Apply the verified R0 candidate only after clean pre-implementation PASS. First add an actual browser positive control on a disposable same-origin context using synthetic, uniquely named localStorage and non-HttpOnly cookie sentinels plus a locally intercepted no-forward endpoint. The control must show executable HTML can observe or alter the synthetic origin state and attempt the controlled request; reset the sentinels before testing Print. Do not use real credentials or record cookie values in output. The test must distinguish script blocking from a script that never ran and must count all controlled endpoint hits and unexpected requests.

Repair the real Artifacts Print path so HTML from `result.html` cannot exercise app-origin script, storage, cookie or authenticated-request authority. Keep preview sandbox intact. Assert the actual Print payload cannot read/mutate the synthetic storage or cookie, cannot hit the controlled same-origin endpoint, and has no direct opener access. Include a mutation or negative control that removes the chosen isolation and fails the oracle. In the same Chromium profile, prove a native popup/print invocation and the displayed build after an unsaved form edit; a fabricated Window or print return is forbidden. A blank popup, silent blocked script without positive control, or CSP text without browser enforcement is insufficient.

The safe design may wrap or sandbox the print presentation, but document any rendering or byte difference from the displayed/exported HTML. Do not claim exact bytes, physical output or accessibility. Preserve copy/download/export behavior and route/auth boundaries. A test fixture may only call the controlled intercepted endpoint; any unplanned outbound request is a failure. If the design cannot meet these outcomes within six paths, return `BLOCKED_WITH_REASON` with the narrowest scope amendment.

## Execution Plan

1. Read named sources/checkers; verify clean HEAD and run bound pre-implementation gate.
2. Apply exact stash without dropping, verify six path SHA-256 fingerprints and no extras.
3. Build positive app-origin capability control, actual Print negative oracle and isolation-removal mutation; preserve R0 native print/version assertions.
4. Repair panel within scope, then run one focused Chromium case, focused unit tests, TypeScript/lint and worker-return fast gate. Write bounded proof and R1 return against this order. Local independently probes before acceptance.

## Evidence Requirements

Return executionBaseHead, clean pre-stash and post-stash status, stash SHA and six restored hashes, exact final changed set, positive control observations, actual Print negative observations, mutation failure, native print count, displayed versus printed version, popup/iframe origin or effective policy, controlled endpoint hit counts, unexpected request counts, focused unit/browser/TypeScript/lint and worker-return gate. Use one machine-readable acceptance-evidence-json join. No raw cookie values, tokens, real data or unredacted HTML.

## Acceptance Criteria

- [ ] Clean bound pre-implementation PASS precedes stash apply; six restored hashes match the packet and no extra path is changed.
- [ ] Positive browser control proves the synthetic payload can reach seeded app-origin capabilities when not isolated.
- [ ] Actual Print payload cannot read or mutate seeded localStorage/cookie or make a controlled same-origin request; isolation-removal mutation makes the oracle fail.
- [ ] Native Chromium Print invocation and displayed-version binding remain proven; preview/copy/download behavior remains intact.
- [ ] Six exact worker paths, secret-free proof, focused checks and worker-return gate evidence; no commit or scope expansion.

Fail closed on inert control, same-origin authority leakage, popup-only proof, unknown requests, stash/hash mismatch, unavailable browser, out-of-scope mutation or worker commit.

## Review Gate

Local checks the inherited candidate fingerprint, scope, positive/negative/mutation oracles, native print/version behavior, and rendering tradeoff. Independently rerun the focused Chromium case and inspect any CSP/sandbox enforcement ordering. Worker fast-gate PASS cannot override a semantic origin-authority failure. Q001/Q004 remain open.

## Independent Review Probe Admission Contract

independentProbeRequired: YES

independentProbeRiskClass: FALSE_ORIGIN_ISOLATION_OR_PRINT_PROOF

independentProbeDispositionAtDispatch: PENDING_REVIEWER_EXECUTION

probeExecutorRole: LOCAL_REVIEWER_NOT_IMPLEMENTATION_WORKER

implementationOracleSeparation: Local reruns the native Chromium positive/negative/mutation case and inspects the actual isolation mechanism independently of worker prose.

positiveControl: unsandboxed same-origin synthetic payload reaches seeded origin capabilities and intercepted no-forward endpoint.

negativeMutationClasses: actual Print reads or mutates seeded storage/cookie; controlled endpoint hit; opener reachable; native print absent; stale form version printed; isolation mutation does not fail.

expectedInformationGain: distinguish effective browser origin/script isolation from opener-only and inert-fixture claims.

rerunCostReason: one focused browser case addresses the critical D058 finding without broad duplicate suites.

reviewerDecisionOwner: LOCAL

## Review Dispatch Convergence And Invocation Budget Control

Review-Dispatch Convergence Control: REQUIRED

reviewerLocalRepairBoundary: MATERIAL_DESIGN_CHANGE
reviewerLocalRepairBasis: docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_AUDIT_2026-10-01.md demonstrates a new app-origin authority gap; Local cannot safely patch the unproven print architecture without a positive/negative browser design and mutation proof.

dispatchKind: REWORK
dispatchSurface: INTERNAL_AGENT
parentAssignmentId: CVF-NCR-HTML-B1-PRINT-REPAIR
reviewRoundCount: 1
priorFindingSetDigest: 13a1fbba70c2e6f6a44047cd486a989053c51982f15a8f3ed619b57bf6ba30ca
dependencyAuditDisposition: COMPLETE_BEFORE_FIRST_REPAIR
reworkFindingDisposition: CONSOLIDATED_ALL_DEPENDENT_FINDINGS
newIndependentCriticalEvidence: docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_BROWSER_AUDIT_2026-10-01.md D058 same-origin authority finding
regressionGuardDisposition: REQUIRED_AND_PLANNED_FOR_EACH_TARGETED_DEFECT
cumulativeExternalInvocationCount: 0
externalInvocationCeiling: 0
usageAvailability: NOT_APPLICABLE_INTERNAL_AGENT
quotaAdmissionDisposition: NOT_APPLICABLE_INTERNAL_AGENT
nextDispatchDisposition: ONE_CONSOLIDATED_REWORK
rootCauseClusterId: B1_PRINT_ORIGIN_AUTHORITY_GAP
reworkGeneration: 1
consolidatedDefectClassSweep: COMPLETE_BEFORE_REWORK_DISPATCH
successorTrancheOpened: NO
implementationAutonomyDisposition: CONTRACT_AUTHORITY_EVIDENCE_OUTCOME_ONLY
preExecutionReviewAdmission: NOT_REQUIRED_BEFORE_EXECUTION
preExecutionReviewTrigger: NONE
nextRoutineReviewBoundary: WORKER_RETURN
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION

## Gate-To-Role Closeability Contract

closeabilityContractVersion: cvf.gate-role-closeability@1.0.0

closeabilityDisposition: CLOSEABLE

implementationTopologyPolicy: EXACT_PATHS_WITH_NO_FORESEEABLE_SPLIT

foreseeableFileSplitDisposition: NOT_REQUIRED_UNDER_SIZE_BUDGET

returnTimeRecheck: REQUIRED_BEFORE_REPAIR

| gateId | mustPassBy | repairOwner | repairPhase | mutationSurface | topology | commitOwner | commitPhase | dependsOn |
|---|---|---|---|---|---|---|---|---|
| authorization_review | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet and audit | EXACT_PATHS | closer | DISPATCH_COMMIT | NONE |
| pre_dispatch_gate | PRE_DISPATCH | dispatcher | PRE_DISPATCH | paired packet | EXACT_PATHS | closer | DISPATCH_COMMIT | authorization_review |
| dispatch_continuity | IMPLEMENTATION | session-sync-steward | IMPLEMENTATION | `AGENT_HANDOFF_V63_2026-09-18.md` material-SHA marker | EXACT_PATHS | session-sync-steward | DISPATCH_CONTINUITY_COMMIT | pre_dispatch_gate |
| focused_checker_tests | WORKER_RETURN | worker | IMPLEMENTATION | panel, unit/browser specs, proof JSON and contract | EXACT_PATHS | closer | MATERIAL_COMMIT | dispatch_continuity |
| adif_integrity | WORKER_RETURN | worker | IMPLEMENTATION | worker return | EXACT_PATHS | closer | MATERIAL_COMMIT | focused_checker_tests |
| pre_implementation_autorun | WORKER_RETURN | worker | IMPLEMENTATION | exact worker manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | adif_integrity |
| worker_return_fast | REVIEW | worker | WORKER_RETURN | exact worker manifest | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_implementation_autorun |
| reviewer_fast | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted worker paths and Local probe | EXACT_PATHS | closer | MATERIAL_COMMIT | worker_return_fast |
| pre_commit | PRE_MATERIAL_COMMIT | reviewer | REVIEW | accepted material paths | EXACT_PATHS | closer | MATERIAL_COMMIT | reviewer_fast |
| terminal_completion_review | PRE_MATERIAL_COMMIT | reviewer | REVIEW | reviewer disposition | EXACT_PATHS | closer | MATERIAL_COMMIT | pre_commit |
| continuity | CONTINUITY_COMMIT | session-sync-steward | CONTINUITY_COMMIT | active continuity paths | BOUNDED_PATH_FAMILY | session-sync-steward | CONTINUITY_COMMIT | terminal_completion_review |
| committed_range_closure | POST_MATERIAL_CLOSURE | reviewer | POST_MATERIAL | split committed ranges | BOUNDED_PATH_FAMILY | closer | CORRECTIVE_MATERIAL_COMMIT | continuity |

## Semantic Convergence Outcome

```json
{"schemaVersion":"cvf.semanticConvergenceControl.v1","problemKey":"cvf-ncr-html-b1-print-browser-repair","chainMode":"SUCCESSOR","chainOrdinal":1,"predecessor":{"path":"docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PRINT_BROWSER_REPAIR_2026-10-01.md","sha256":"8ff82b29df48abd0173f7c7a9a98d85f0f2ab6e00ab0c53498799d999bf79fdc"},"blockerDelta":{"prior":[],"resolved":[],"retained":[],"new":["B1_PRINT_ORIGIN_AUTHORITY_GAP"],"reopened":[],"current":["B1_PRINT_ORIGIN_AUTHORITY_GAP"]},"resolutionEvidence":{},"counters":{"partialReadyClosures":0,"reviewerScopeExpansions":0,"sameClaimCorrections":0,"nonDecreasingBlockerTransitions":1},"claims":[],"requiredDisposition":"CONTINUE_BOUNDED","successorScope":"INITIAL_BOUNDED"}
```

## High-Risk Local Transaction Proof Applicability

High-Risk Local Transaction Proof Applicability: NOT_APPLICABLE_WITH_REASON - synthetic browser UI print rework has no authoritative write, rollback transaction, process lock, ownership or security configuration mutation

## Foundation Storage Layout Block

N/A with reason: R1 edits only the Artifacts panel and its existing six-path synthetic proof set; it does not create, split, relocate or refactor a durable governance foundation file or index.

## Architecture Readiness Admission

Architecture-Readiness Admission: NOT_APPLICABLE_INTERNAL_AGENT_WITH_REASON: synthetic internal Chromium UI rework without external invocation

## Closure Checklist

Local checks exact six paths, control/negative/mutation observations, print/version proof, no unintended requests, bounded reference/JSON/return, focused independent probe, material commit and continuity. Do not accept merely because structural gates pass. Q001/Q004 stay open.

## Worker Return Packet Shape Contract

contractProfile: WORKER_RETURN_FULL_GATE_V1
requiredGate: `python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PRINT_ORIGIN_ISOLATION_R1_2026-10-01.md`
individualCheckerSubstitution: FORBIDDEN
workerReturnSkeleton: CHECKER_SAFE_SKELETON_REQUIRED

Required terms: Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Decision / Disposition; Checker Source Read-Ahead Block; Agent Operation Trace Block; Delta Execution Claim Boundary Control Block; Public Export Disposition; executionBaseHead; git status --short; Changed Files; No-Commit Statement; Return-Time Closeability Recheck. Include one acceptance-evidence-json block joining the ledger to exact changed files.

Conditional terms: External Knowledge Intake Routing; Rescan Intelligence Hardening; Corpus Completeness And Report Integrity; Finding-To-Governance Learning Disposition; Epistemic Process Block; Machine Closure Package. State N/A with reason for each non-applicable block.

## Verification Commands

```powershell
Set-Location EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web
npx playwright test tests/e2e/artifact-export-print-browser.spec.ts --config playwright.config.mock.ts
npx vitest run src/components/ArtifactExportPanel.test.tsx
npm run check
npx eslint --max-warnings=0 src/components/ArtifactExportPanel.tsx src/components/ArtifactExportPanel.test.tsx tests/e2e/artifact-export-print-browser.spec.ts
Set-Location ../../..
git status --short --untracked-files=all
python governance/compat/run_worker_return_fast_gate.py --active-work-order docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PRINT_ORIGIN_ISOLATION_R1_2026-10-01.md
```

Use only existing safe auth-origin/port override if required by the harness; do not edit config, install dependencies or print secrets.

## Reviewer Closure Conversion

completionReviewPath: `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_ORIGIN_ISOLATION_R1_COMPLETION_2026-10-01.md`

reviewerOwnedClosurePaths: completion review if required by closure gate or security evidence; Local owns final disposition, commit and continuity.

## Agent Handoff Contract Control Block

Contract source archive-qualified exception: `docs/reference/CVF_AHB_T2_AGENT_HANDOFF_CONTRACT_RATIFICATION_2026-06-16.md`.

| Field | Value |
|---|---|
| route | SINGLE_AGENT_MULTI_ROLE with distinct Local reviewer phase |
| rolePattern | worker revises six inherited candidate paths and returns pending; Local reviews and commits |
| phase | packet release before worker implementation |
| baseHeadFor(phase) | dispatchBaseHead=`b3c5a0aa8`; executionBaseHead=worker captures after release; closureBaseHead=Local captures after return |
| changedSetScope(phase) | exact six inherited worker paths; paired packet dispatcher-owned |
| traceScope(phase, actor) | worker records restored candidate hashes, positive/negative/mutation controls, print/version, requests and exact changed set |
| commitOwner(phase) | Local closer; worker commit forbidden |
| crossBatchIsolation | Q001/Q004, real ledger, P11, external runtime, public sync, deployment parked |
| nextMoveSurfaces | packet material commit, continuity release, bound worker gate |

sharedWorktreeCoordinationMode: EXPLICIT_LANE_HANDOFF

activeLaneOwner: none until bound release PASS

laneOwnedPaths: exact six-path worker acceptance ledger after release

dispatcherMutationBoundary: NO_MUTATION_WHILE_LANE_ACTIVE

laneReleaseEvidence: pending worker return, exact changed set, focused Playwright and full worker gate

## Return-To-Orchestrator Conditions

Return `BLOCKED_WITH_REASON` if stash/hash differs, control is inert, isolation/print/version cannot all be proven, browser/auth harness is unavailable, controlled or unexpected request escapes, safe design requires forbidden paths, or worker changed set exceeds six paths. Include observed failure and narrowest requested amendment; do not silently broaden.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | first-section envelope; source ACCEPT rows; acceptance-ledger-json; closeability graph; high-risk non-applicability; worker-return gate |
| gateRunPurpose | Confirm source-backed packet shape and authority before release |
| claimBoundary | Static checks cannot prove native Print or origin isolation |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B1-PRINT-R1 --title "NCR HTML B1 Print Origin Isolation R1" --date 2026-10-01 --base b3c5a0aa8 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind REWORK --dispatch-surface INTERNAL_AGENT --review-round-count 1 --root-cause-cluster-id B1_PRINT_ORIGIN_AUTHORITY_GAP --prior-finding-set-digest 13a1fbba70c2e6f6a44047cd486a989053c51982f15a8f3ed619b57bf6ba30ca --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | source-backed R1 origin isolation contract, six-path worker manifest and operator boundary |
| checkerReadAheadConfirmation | dispatch, release, acceptance-ledger, closeability, envelope, structural and high-risk checker sources |
| docOnlyNewFields | N/A with reason: no new governed field schema |
| claimBoundary | Scaffold is authoring aid only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local dispatch author |
| Provider or surface | private CVF shared workspace |
| Session or invocation | NCR HTML B1 packet authoring, 2026-10-01 |
| Working directory | repository root |
| Command or tool surface | source reads, scaffold preview, packet gates and Git |
| Target paths | paired B1 baseline, this work order and NCR roadmap D059 |
| Allowed scope source | delegated Local dispatch; roadmap D058 and B1 Print reviewer decision |
| Before status evidence | clean worktree at `b3c5a0aa8` |
| After status evidence | paired packet and roadmap paths pending material commit; no worker edit |
| Diff evidence | exact three-path packet/roadmap set from Git status |
| Approval boundary | B1 packet only; worker follows committed release gate |
| Claim boundary | no implementation or runtime proof from packet authoring |
| Agent type | dispatcher |
| Invocation ID | cvf-ncr-html-b1-print-origin-isolation-r1-packet-20261001 |
| Expected manifest | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B1_PRINT_ORIGIN_ISOLATION_R1_2026-10-01.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PRINT_ORIGIN_ISOLATION_R1_2026-10-01.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Actual changed set | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B1_PRINT_ORIGIN_ISOLATION_R1_2026-10-01.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PRINT_ORIGIN_ISOLATION_R1_2026-10-01.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | synthetic real-browser Print origin-isolation rework packet |
| claimDisposition | CLAIM_REJECTED: no implementation or active acceptance behavior claimed before worker evidence |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: R1 worker browser observation receipt is pending |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: R1 worker browser test is pending |
| invocationBoundary | synthetic local browser/test process only |
| interceptionBoundary | no direct interception or mandatory wrapper claimed |
| claimLanguage | D058 same-origin authority gap, pending R1 worker repair and Local security review |
| forbiddenExpansion | no route, ledger, database, provider, real data, artifact acceptance or public effect |

## Claim Boundary

This R1 order authorizes synthetic B1 Print origin-isolation repair and proof only after release. It does not establish physical paper/PDF output, print dialog or accessibility, passive loads, other browsers, universal HTML safety, provider/governance behavior, durable B2 acceptance, Q001/Q004 exit, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Operator Checkpoint

Operator retains real-data classification, actor/account, artifact store/writer, backup/key custody, retention, RPO/RTO, cost and pilot/live effect. No such choice is required for this synthetic B1 rework.
