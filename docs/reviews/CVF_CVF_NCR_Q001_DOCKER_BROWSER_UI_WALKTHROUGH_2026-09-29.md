# CVF NCR Q001 Docker Browser UI Walkthrough

Memory class: governed-review

docType: review

Status: BOUNDED_LOCAL_UI_OBSERVED

Date: 2026-09-29

Text Encoding Exception: source-faithful Vietnamese UI labels are retained to identify the browser controls observed; this file is UTF-8.

Decision owner: Local reviewer/closer under the operator's instruction to continue Q001. External Web remains advisory and was not invoked.

executionBaseHead: `b61de9fa4`

## Purpose

Check the actual Work Transfer UI path after the HTTP-only Docker receipts in `docs/reviews/CVF_CVF_NCR_Q001_DOCKER_LEDGER_ENFORCEMENT_REPAIR_2026-09-29.md`. Establish what a browser user can see and what remains unproved. This packet does not accept the HTML artifact, close Q001, or prove provider governance.

## Target / Source

The selected path is `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx`, `src/components/ArtifactExportPanel.tsx`, `src/app/api/artifacts/export/route.ts` and `proof.ts`, backed by the current Governance Engine. The NCR roadmap is the decision owner surface. Role: shared-workspace INTERNAL_AGENT Local implementer/reviewer. Phase: bounded Q001 Docker browser profile. Final technical decision owner: Local. No external repository or runtime was absorbed.

## Scope / Methodology

The two existing Q001 services ran in their internal Docker network with no host port. A third temporary container used Alpine Chromium 136 and the web container's network namespace, so the browser used the configured `http://127.0.0.1:3000` origin. The sandbox web container alone received `allowedDevOrigins: ['127.0.0.1']` in its `next.config.ts` to permit Next.js development resources; repository source and the committed web image were not changed. A browser diagnostic confirmed the login submit became enabled and no page errors followed that sandbox fix. An external Google Fonts request could not resolve in the internal network; no application request depended on it.

Playwright drove the browser through the visible login form with the documented development mock owner, dismissed the welcome modal through its Skip button, and used the authenticated admin API to seed one synthetic audit record in the sandbox. The Work Transfer UI otherwise has no inline export panel when history is empty. The browser selected the synthetic record's Xuất HTML action, filled synthetic source text and a unique receipt anchor, and clicked Tạo HTML. The script observed the actual export response and DOM state; it did not intercept or replace the browser's fetch. The image is `docs/reviews/evidence/CVF_NCR_Q001_DOCKER_UI_2026-09-29/work-transfer-draft-receipt.png`, SHA-256 `954a25469f0452d5bc6d2ee90bb2997430c06d9cff552a987a532c6e4dffb74d`. It contains synthetic UI data and mock account display only.

## Findings / Position

| Finding | Observation | Disposition |
|---|---|---|
| Cold development request | First clicked export returned HTTP 200 and a draft HTML result without a governance receipt. Its internal evaluate hop exceeded `proof.ts`'s 4-second timeout while the Next.js route compiled; sandbox logs showed the late evaluate request body could not be parsed. The UI displayed its no-receipt/draft state and did not show approval. | PROFILE_LATENCY_GAP_OPEN; not evidence that a production build would behave the same |
| Warm browser path | A later browser run returned export HTTP 200, `success=true`, route auth mode `session`, receipt decision `ALLOW`, matching anchor, `DRAFT_UNACCEPTED`, visible draft notice, no approval badge and no UI error. The UI displayed 8/8 readiness checks and a review-not-approved note. | LOCAL_UI_AND_RECEIPT_OBSERVED_BOUNDED |
| Ledger join | Final browser receipt ID `artifact-proof-q001-ui-1790616877047-1790616877510` matched the last Governance Engine volume block's request ID. Four-block chain validated; final hash `449674d89a909b7075c5f16cff16aef6f4493d457f2d034d107d26140ebf693f`. | LOCAL_LEDGER_JOIN_OBSERVED |

The browser image digest was `sha256:e07cc6d055ac9fdeeb86dce71c1a59b69945a26b88472ff4ef648077a967b425`. The screenshot is a visual record of the final warm browser state; it is not an artifact acceptance receipt. Repeated synthetic admin records and ledger blocks are confined to the sandbox containers/volume.

## Risk / Corrective Action

The 4-second hop timeout and dev cold compile must be evaluated with a production-like local build and a bounded latency/retry profile before relying on first-attempt receipt behavior. Current fallback produces a draft packet without receipt, visibly labelled as such. The UI export path needs an audit record to expose the panel; this walkthrough seeded one through an authenticated sandbox admin endpoint and did not prove a real transfer-record producer. Docker volume survival does not settle backup/restore or RPO/RTO. No hosted Netlify UI, provider API call, production authentication, P08 broad secret scan, cost distribution or artifact acceptance was tested. Q001/R0 exit and P11 remain parked.

## Decision / Recommendation / Disposition

Accept only the observed local browser interaction, session-auth receipt and draft-state presentation. Keep Q001 open for a production-like first-attempt profile, retention, P08, deployment constraints and separately authorized effect/live proof. Do not promote the receipt or the 8/8 presentation checks to HTML acceptance.

## Epistemic Process Block

### Expected Result / Prediction

A mock-authenticated user could open Work Transfer, select a source record and build HTML whose visible draft state and receipt matched the engine ledger.

### Evidence Comparison

The browser needed a sandbox dev-origin setting and a synthetic audit record. The cold run gave draft output without receipt; the warm run gave the expected receipt and valid ledger join. Both kept the UI in a draft/unaccepted state.

### Contradiction Or Gap Disposition

The actual browser route is now observed, but cold-hop latency, real record production and production-like profile remain open. The synthetic mock flow cannot establish hosted or provider-live behavior.

### Claim Update

Q001 has a bounded real-browser local UI walkthrough with a warm receipt. Artifact acceptance, deployment durability, provider governance and R0 exit remain unproved.

## Finding-To-Governance Learning Disposition

| Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|
| RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | DESIGN_REVIEW_REQUIRED | Profile first-attempt receipt latency in a production-like local build; make timeout/retry and explicit no-receipt draft behavior part of the Q001 acceptance contract. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | `Target / Source`, `Scope / Methodology`, `Findings / Position`, `Risk / Corrective Action`, `Decision / Recommendation / Disposition`, `Evidence Comparison`, `Contradiction Or Gap Disposition`, `Claim Update`, `Public Export Disposition` |
| gateRunPurpose | Confirm the browser packet shape and bounded observation after source read-ahead. |
| claimBoundary | Checker compliance does not promote a synthetic browser run to provider-live or artifact-acceptance proof. |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local single agent in implementer and reviewer roles |
| Provider or surface | Private CVF workspace and local Docker Desktop/Chromium |
| Session or invocation | Q001 Docker browser UI walkthrough, 2026-09-29 |
| Working directory | Repository root and isolated Windows Temp/Docker sandbox |
| Command or tool surface | Docker build/run/exec, Playwright Chromium browser, Python ledger validation, screenshot visual inspection |
| Target paths | Work Transfer UI, export route, current engine; this review, screenshot and NCR roadmap |
| Allowed scope source | Operator instruction to continue the bounded Q001 profile |
| Before status evidence | clean `b61de9fa4`; real browser walkthrough still open |
| After status evidence | browser session receipt and ledger join; review, screenshot and roadmap pending material commit |
| Diff evidence | Working-tree Git diff, screenshot hash and Docker/browser evidence above |
| Approval boundary | synthetic local browser only; no provider/live, public write, deployment or pilot acceptance |
| Claim boundary | bounded UI presentation and session receipt, with cold timeout gap |
| Agent type | Codex (shared-workspace INTERNAL_AGENT) |
| Invocation ID | q001-docker-browser-ui-20260929 |
| Expected manifest | this review; screenshot; NCR roadmap |
| Actual changed set | this review; screenshot; NCR roadmap |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | Q001 local Docker browser UI |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: actual headless browser and synthetic session-auth HTTP |
| receiptEvidence | CVF_RECEIPT_PRESENT: warm browser receipt ID equals the final sandbox ledger event request ID; first cold attempt had no receipt |
| actionEvidence | ACTION_EVIDENCE_PRESENT: UI click generated draft HTML and engine appended a matching, hash-valid block |
| invocationBoundary | internal Docker network, development mock owner, synthetic audit/content and no external provider |
| interceptionBoundary | browser route fetch was not intercepted; temp dev-origin setting and seeded audit record are declared |
| claimLanguage | local warm UI/receipt observed; approval, acceptance and live governance unclaimed |
| forbiddenExpansion | no P11, external runtime, Netlify, public sync, production readiness or live-provider inference |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This private packet records a browser-observed draft. Neither the Work Transfer `ALLOW` summary nor engine `ALLOW` receipt approves the HTML artifact.
