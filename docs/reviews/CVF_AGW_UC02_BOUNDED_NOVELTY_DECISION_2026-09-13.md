# AGW UC02 Bounded Novelty Decision

Memory class: FULL_RECORD
docType: decision
Status: REVIEWED_DECISION_ONLY
Date: 2026-09-13
Review base: d8b0edb2b98f2d159102c3ca5f3987494e0180e5

## Purpose

Dispose the internal research return for the selected AGW-UC-02 comparison. Retain source-level response-masking value while rejecting the unsupported conversion of a capability difference into a required safety-policy change. Final candidate disposition: DEFER_WITH_TRIGGER. No adaptation or implementation is accepted.

## Target / Source

Authority: docs/reviews/CVF_DOMAIN_PILOT_DEFERRED_TRIGGER_TRIAGE_2026-09-13.md, Decision and Next Bounded Review Contract. The operator assigned Local orchestrator/reviewer and transported the internal worker's read-only return. The chat assignment authorized local reads and a conversational report only; no filed implementation baseline/work order was released.

The following is the bounded reviewer evidence ledger, not a mirror inventory. AGW prefix means `.private_reference/source_mirrors/agentgateway__agentgateway/`; CVF prefix means `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/`.

| ID | Evidence path | Processing status / depth | Decision-bearing region |
| --- | --- | --- | --- |
| E1 | docs/reviews/evidence/CVF_AGW_UC02_NOVELTY_RESEARCH_RETURN_2026-09-13.txt | READ / FULL_READ | Entire submitted report; candidate evidence, corrected below |
| E2 | docs/reviews/CVF_DOMAIN_PILOT_DEFERRED_TRIGGER_TRIAGE_2026-09-13.md | READ / PARTIAL_READ | Selected comparison contract and risk boundary |
| E3 | AGW crates/agentgateway/src/llm/policy/mod.rs | READ / PARTIAL_READ | evaluate_regex_response 1477-1513; evaluate_webhook_request/response 1516-1704; FailureMode and Webhook 2126-2159 |
| E4 | AGW crates/agentgateway/src/llm/policy/webhook.rs | READ / PARTIAL_READ | Payload builders, header expressions, send_request/send_response 149-283 |
| E5 | CVF app/api/execute/route.ts | READ / PARTIAL_READ | Validation/retry/terminal branches 790-930; targeted DLP/readout references |
| E6 | CVF lib/output-validator.ts | READ / PARTIAL_READ | Types/patterns 17-93; validateOutput, shouldRetry, computeDecision 97-268 |
| E7 | CVF lib/safety-workflow-chain.ts | READ / FULL_READ | LOG/STRIP/BLOCK definitions and helper behavior |

E1 is preserved as supplied. SHA-256: `ea1d3faf323ab95f4816111187c0c79eab66fe7d475bd3a176050a695952a17f`. Its abbreviated source paths are expanded by the prefix map above; statements marked NOT_OPENED or PARTIAL_READ in E1 remain so. Worker read-depth claims are not independent reviewer full-read certification.

Source identity: Local `git -C .private_reference/source_mirrors/agentgateway__agentgateway rev-parse HEAD` returned `3d5f59f8e2e17fd05e99b443e6e1bcc76daa5826`; local mirror status was clean. CVF HEAD matched the worker's base, and the initial worktree was clean. Prior intake license/freshness evidence is inherited from docs/audits/CVF_DOMAIN_PILOT_INITIAL_INTAKE_2026-09-12.json; latest upstream and subtree redistribution rights were not refreshed. No external source is CVF authority.

## Scope / Methodology

EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION. One safety/decision-boundary pass, zero worker redispatches, no per-row recreation of research. Named contradiction: the return calls missing output masking a proven requirement and proposes masking existing unsafe/governance matches instead of retry. Expected information gain: distinguish a useful mechanism from an authorized need, and verify whether existing enforcement was understated. Cost reason: targeted functions in seven evidence paths suffice for deferral; a broad source/test scan cannot establish the missing consumer policy.

No upstream or CVF application execution, live proof, network call, credential access, installation or source-code mutation. Source observations are static; no runtime safety, efficacy or latency claim is made. Governance gates validate only the review and continuity artifacts.

## Single-Pass Review Matrix

| Boundary | Review disposition |
| --- | --- |
| Contract/schema | Read-only conversational research was returned; no implementation schema or runtime contract was accepted |
| Authority/source | Exact pin/current CVF base checked; E1 retained as candidate evidence; unsupported generalizations narrowed below |
| Paths/repository | Material changes are this decision and E1 only; continuity is a separate seven-path projection |
| Safety/negative cases | Replacing unsafe/governance rejection with span masking is not established safe; retry budget, repeated issues, bypass block and vision branch constrain claims |
| Test adequacy | No runtime tests required for a decision-only deferral; no historical live receipt transfers |
| Closure range | Review base to material commit, then material commit to continuity commit; separate pre-closure checks |
| Commit plan | One material commit, one continuity commit; no worker commit or push |

Return-Time Closeability Recheck: documentation corrections are reviewer-owned and closeable in this bounded decision. No worker source repair or successor tranche is needed. Implementation remains HOLD.

## Findings / Position

| Finding | Returned claim / proposal | Reviewer disposition and evidence |
| --- | --- | --- |
| F1 | No output masking is a proven requirement; convert UNSAFE_CONTENT matches into a MASKED alternative | REJECT_AS_PROPOSED. E3 proves a response-text masking mechanism exists upstream. E5/E6 show no masking step in the reviewed validation branch, but that difference is not evidence that a CVF consumer needs partial-redaction delivery. Existing unsafe/governance expressions detect behavior, not merely PII spans. Removing matched text does not prove the remaining answer safe and can hide signals from later checks. Preserve the PII-only idea as a deferred hypothesis; do not replace current safety decisions. |
| F2 | CVF can reject only after two retries; every unsafe detection forces full regeneration | CORRECTED. E6 shouldRetry stops on repeated issues and caps attempts at MAX_RETRIES=2. E5 also checks elapsed retry budget and provider admission. The successful non-vision RETRY branch can terminate before two retries. E5 897-916 separately blocks detected output bypass with HTTP 400. The validation block is gated by !isVisionExecution; no universal response-path claim is accepted. |
| F3 | CVF always audits and enforces together; has no observe-only behavior | NARROWED. E7 has MEDIUM LOG actions with no text mutation and no block from those LOG matches. AGW's configurable per-guard audit mode may differ from that fixed classification, but the claimed absence of observation without enforcement is false. No shadow-policy consumer requirement was supplied. |
| F4 | All webhook failures share one branch; response payload is Vec<Message>; JWT claims never leave | NARROWED. E4 builds request messages and response choices separately. Forwarded headers and CEL expressions can disclose selected data from original request context; not attaching JWT extensions is not a prohibition on configured claim/header disclosure. E3 handles send/parse errors via failure_mode, but request-context evaluation can fail before that branch and action-body validation can fail afterward. Non-2xx transport behavior and outer error propagation were not traced here; no universal fail-mode guarantee is accepted. |

Additional non-load-bearing claims in E1 are not promoted: comparative regex precision without reading the upstream PII patterns, full-buffer validation being strictly more thorough in all respects, exact streaming masking/window guarantees based mainly on module documentation, and repository-wide absence of external policy consumers. These remain unverified beyond the return's declared read scope. No extra exploration is required to decide the current deferral.

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| Request-side detection/redaction/rejection | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety-workflow-chain.ts and DLP owner evidence in E2/E1 | CONFIRMED_EXISTING | Configurable upstream details do not establish new demand | NO_NEW_VALUE for the submitted request-side adaptation case only; not the upstream repository |
| Response regex PII masking | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/output-validator.ts uses PASS/WARN/RETRY; E3 produces masked replacements | NEW_FINDING | Response-text masking mechanism | DEFER_WITH_TRIGGER; potentially useful mechanism, policy need and final-response dependency closure unresolved |
| External webhook policy decisions | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts is the named consumer checked; no required external service supplied | NEW_FINDING | Outbound policy-service boundary | DEFER_WITH_TRIGGER; no HTTP integration or new authority |
| Configurable audit/custom rejection | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/safety-workflow-chain.ts contains non-mutating LOG behavior | ENRICH_EXISTING | Per-guard configuration versus fixed classification | DEFER_WITH_TRIGGER; no policy-tuning or custom-response requirement supplied |

## Decision

AGW-UC-02: DEFER_WITH_TRIGGER. Accept the bounded source comparison with the above reviewer corrections, not the proposed adaptation. Preserve response-PII masking as possible existing-owner enrichment; do not label the whole candidate or repository NO_NEW_VALUE.

Response-masking reopen trigger: a named CVF consuming workflow supplies a concrete requirement/example for returning a useful answer with specified PII categories redacted. The contract must separate redactable PII from unsafe/governance content, preserve current blocking/audit/admission behavior, and define relevant output channels and failure behavior. A subsequent source-verified design must compare reuse of the existing DLP owner with any upstream-derived logic, trace final-response/storage/audit dependencies, and define adversarial verification before implementation can be proposed. No new MASKED decision or SAF2 rewrite is selected now.

Webhook reopen trigger: a named consumer requires an identified external policy service, with explicit data categories, disclosure/header rules, failure/timeout policy, authority and operational owner. No such requirement is evidenced in this return.

Next allowed move: retain this decision and await concrete trigger evidence for a bounded re-triage. No worker dispatch follows this review automatically. DSH-UC01 remains closed; DSH-UC02, QM-UC01, AGW-UC01 and QM-UC02 retain their existing deferred triggers. No broader absorption completion is claimed.

## Risk / Corrective Action

Correct the decision record locally rather than asking the worker to reproduce research. Keep E1 intact so the provenance of the corrected assertions remains reviewable. Potential provider-call savings are a hypothesis, not measured economics or a reason to weaken safety. Current rejection and audit contracts are not modified. Source-level masking is not a semantic safety certificate.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Existing rule / action |
| --- | --- | --- | --- | --- |
| F1 | WORKER_EXECUTION_ERROR | DOCUMENTATION_ONLY_LEARNING | RULE_EXISTS | E2 requires named-consumer value and forbids manufacturing a requirement; keep mechanism, need and authorization separate |
| F2 | WORKER_EXECUTION_ERROR | DOCUMENTATION_ONLY_LEARNING | RULE_EXISTS | E2 risk boundary requires separating detection, audit, masking and rejection; use branch-specific source evidence |
| F3 | WORKER_EXECUTION_ERROR | DOCUMENTATION_ONLY_LEARNING | RULE_EXISTS | Named-owner collision review must respect LOG semantics; no global absence inference |
| F4 | WORKER_EXECUTION_ERROR | DOCUMENTATION_ONLY_LEARNING | RULE_EXISTS | E2 requires explicit timeout/failure/header/disclosure boundaries; preserve unknowns outside traced branches |

Next action: preserve the four corrections and require named demand before re-triage. Runtime/provider/cost learning: N/A_WITH_REASON - static report review, no runtime observation or measured economics.

No new checker or ADIF entry is opened for this bounded report correction; the controlling contract already states the relevant rules. The reusable distinction is recorded here in CVF, not only in provider memory.

## Epistemic Process Block

Expected Result / Prediction: response masking could offer incremental value under an existing output consumer.
Evidence Comparison: upstream has a response masking mechanism, while the reviewed CVF validation branch has different response treatment. The return supplies no concrete consumer requirement; existing route/safety behavior contradicts several global claims.
Contradiction Or Gap Disposition: reject unsafe-pattern masking as proposed, narrow branch/failure claims, and retain the PII-specific hypothesis with a demand trigger.
Claim Update: DEFER_WITH_TRIGGER; no adaptation acceptance or runtime proof.

## Corpus Completeness And Report Integrity

- Corpus task class: bounded returned-evidence review, no complete scan
- Corpus root: seven selected evidence paths E1-E7 in Target / Source
- Snapshot time: 2026-09-13 at review base d8b0edb2b98f2d159102c3ca5f3987494e0180e5
- Enumeration command: filesystem-backed Get-Content and targeted rg of named paths; Git identity/status inspection
- Manifest artifact or inline manifest: E1-E7, with AGW/CVF prefix expansion defined above
- Manifest hash: N/A with reason: inline bounded evidence list, not a new source snapshot; E1 content hash recorded separately
- Processing ledger artifact or inline ledger: E1-E7 status/depth/regions above
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=7; ledger_terminal=7; unresolved=0 within E1-E7; exclusions=0 within the named list; reviewer full-depth=2 and partial-depth=5
- Unresolved files: unvisited source regions, final-response helper dependencies, upstream transport and streaming implementation remain outside the accepted proof
- Declared exclusions: no named path excluded; the rest of either repository is outside scope
- Unreadable or unsupported files: none among E1-E7; failed discovery-path probes are not source evidence
- Aggregation check: four correction clusters and capability dispositions map to E1-E7
- Drift check: CVF base and clean mirror pin checked; no upstream freshness claim
- Output traceability: corrected claims and demand triggers derive from cited source regions and E2 authority
- Adversarial verification: absence of a capability is not proof of a consumer requirement; masking a safety signal is not proof of safe remainder
- Corpus verdict: PARTIAL

## Knowledge System Reconciliation

This is a partial capability-to-owner mapping only, not corpus absorption or a complete knowledge inventory.

- Knowledge task class: bounded comparison disposition
- Source manifest: E1-E7 in Target / Source
- Source manifest hash: N/A with reason: inline selected evidence list, not a corpus snapshot
- Enumeration safety: filesystem-backed direct file reads
- Intake registry or ledger: E1 and the accepted pilot intake cited above
- Authority assets: E2 comparison decision and named CVF source owners
- Derived views: four-row Overlap And Novelty Classification table
- Semantic region ledger: request overlap maps to existing owners; response masking, webhook and configurable audit/custom rejection remain deferred
- Region reconciliation: assets=4; mapped=1; deferred=3; unmapped=0 within the four compared capability groups
- Orphan or unmapped assets: none in these four rows; other capabilities not inventoried
- Cross-region links: response masking requires separate PII and governance-safety policies under existing DLP/output owners
- Drift check: named CVF base and mirror pin inspected; no latest-upstream claim
- Rebuildability check: follow E1-E7 and the correction/disposition tables; no generated knowledge view
- Retrieval boundary: decision evidence only; no retrieval system or readiness claim
- Adversarial verification: deferred value is retained without inventing a requirement
- Knowledge-map verdict: PARTIAL

## Mandatory Blind-Spot Control Block

NOT_APPLICABLE_WITH_REASON: targeted review with explicit partial depths and unresolved regions; no full-source or global coverage claim.

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION: pinned source comparison only. E1 is an internal research report, not accepted external code or a runtime dependency. No source import or adaptation is performed.

## External Knowledge Intake Routing

External knowledge intake routing: REQUIRED

| Field | Value |
| --- | --- |
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | external repo or copied folder |
| Chain map route | accepted intake to bounded named-consumer/owner comparison |
| Matching local-view guard | governance/compat/check_external_absorption_overlap_discipline.py; governance/compat/check_absorption_blindspot_control_presence.py |
| Owner surface | existing DLP/SAF1/SAF2 and execute-route owners; no new owner |
| Disposition | COMPARISON_ONLY_NO_ABSORPTION |
| Claim boundary | bounded comparison accepted with corrections; adaptation deferred |

## Dual Agent Surface Matrix

| Surface | Interface | Authority / risk boundary | Evidence | Adapter boundary | Disposition |
| --- | --- | --- | --- | --- | --- |
| INTERNAL_AGENT | operator-transported same-workspace research report | read-only worker; Local owns final decision and SOT | E1 and this decision | no runtime adapter | ACCEPT_WITH_BOUNDARY |
| EXTERNAL_AGENT_CLI_MCP | not invoked | no provider execution authority | zero such invocations | no adapter activation | NOT_APPLICABLE_WITH_REASON |

## Review Cost Telemetry And Stop Disposition

reviewRoundCount: 1
workerRepairTurnCount: 0
providerCallCount: 0
tokenOrQuotaUsage: NOT_AVAILABLE_WITH_REASON - cross-session token usage is not exposed
elapsedReviewMinutes: NOT_AVAILABLE_WITH_REASON - no governed wall-clock receipt was captured
valueDelta: retain response-masking value without inventing demand or weakening unsafe-content handling
reviewerWorkBoundary: EVALUATE_RETURNED_EVIDENCE_NOT_RECREATE_IMPLEMENTATION
nextRoutineReviewBoundary: safety/M20 decision boundary reached; no implementation lane
stopDisposition: DEFER_WITH_TRIGGER; no worker redispatch
plannedCommitShape: one material decision/evidence commit and one continuity commit

## Verification

Initial reviewer-fast reported two documentation-shape failures: learning next-action/N/A fields and overlap-table column labels. Both were repaired locally; no source behavior changed. Focused learning/overlap checks passed after repair; final reviewer-fast passed 68/68. The first pre-commit attempt additionally required numeric unresolved accounting and a fully shaped partial knowledge reconciliation block; these documentation fields were repaired before retry. Commit and split-range receipts record the subsequent material/continuity gates.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | governance/compat/check_markdown_structural_completeness.py; governance/compat/check_epistemic_process_packet.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_absorption_blindspot_control_presence.py; governance/compat/check_finding_to_governance_learning.py; governance/compat/check_corpus_completeness_report_integrity.py |
| literalTokensReviewed | Purpose; Target / Source; Scope / Methodology; Findings / Position; Risk / Corrective Action; Decision; Claim Boundary; WORKER_EXECUTION_ERROR; RULE_EXISTS; PARTIAL; COMPARISON_ONLY_NO_ABSORPTION |
| gateRunPurpose | Confirm documentation shape and evidence boundaries after source-read-ahead |
| claimBoundary | no runtime behavior test or full checker-source audit |

## Agent Operation Trace Block

| Field | Value |
| --- | --- |
| Actor | Local orchestrator/reviewer |
| Provider or surface | internal private provenance workspace |
| Session or invocation | AGW UC02 novelty decision 2026-09-13 |
| Working directory | repository root |
| Command or tool surface | local file reads, Git inspection, evidence copy, documentation edits and governance gates |
| Target paths | this decision and E1 |
| Allowed scope source | E2 selected-review authority and operator continuation |
| Before status evidence | clean at d8b0edb2b98f2d159102c3ca5f3987494e0180e5 |
| After status evidence | two new material paths; continuity projected separately |
| Diff evidence | git status --short --untracked-files=all and staged exact manifest |
| Approval boundary | decision and SOT only; no worker implementation release |
| Claim boundary | source comparison with corrected claims; no runtime safety proof |
| Agent type | reviewer/closer |
| Invocation ID | agw-uc02-novelty-decision-2026-09-13 |
| Expected manifest | docs/reviews/CVF_AGW_UC02_BOUNDED_NOVELTY_DECISION_2026-09-13.md; docs/reviews/evidence/CVF_AGW_UC02_NOVELTY_RESEARCH_RETURN_2026-09-13.txt |
| Actual changed set | docs/reviews/CVF_AGW_UC02_BOUNDED_NOVELTY_DECISION_2026-09-13.md; docs/reviews/evidence/CVF_AGW_UC02_NOVELTY_RESEARCH_RETURN_2026-09-13.txt |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

This is the terminal decision for the bounded comparison only. Candidate adaptation is deferred, implementation remains unopened, and no broad absorption, runtime/provider/live, public/deploy, RABA/DARA-T5/P5/P6 authority is granted. Future demand evidence permits re-triage, not automatic implementation.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private review and retained internal research evidence; no public-sync requested.
