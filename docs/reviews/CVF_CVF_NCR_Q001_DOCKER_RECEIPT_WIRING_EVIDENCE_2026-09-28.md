# CVF NCR Q001 Docker Receipt Wiring Evidence

Memory class: governed-review

docType: review

Status: BOUNDED_LOCAL_INTEGRATION_OBSERVED

Date: 2026-09-28

Decision owner: Local reviewer/closer; direct operator authorization for the Q001 Docker receipt check. External Web is advisory and was not invoked.

executionBaseHead: `6158b042c752147cd927befe411679f0fbfc7033`

## Purpose

Record what a real two-service Docker Desktop run proves about the selected Q001 HTML export receipt path, the two contradictions it exposed, and the narrow source repair. This is a local integration observation with synthetic content and development-mode mock login. It does not close Q001, accept the HTML artifact, or assert live provider governance.

## Target / Source

The selected route and current source are `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts`, `proof.ts`, `src/app/api/governance/evaluate/route.ts`, `src/lib/governance-engine.ts`, and `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/api/server.py`, `core_orchestrator.py`, `ledger_layer/immutable_ledger.py`. Accepted source maps: `docs/reviews/CVF_CVF_NCR_R0_W01_HTML_PROFILE_WORKER_RETURN_2026-09-26.md` and `docs/reviews/CVF_CVF_NCR_R0_W02_HTML_DOWNSTREAM_WORKER_RETURN_2026-09-26.md`. Current Q001 source-repair review: `docs/reviews/CVF_CVF_NCR_Q001_HTML_INGRESS_REVIEW_2026-09-28.md`.

Role: shared-workspace INTERNAL_AGENT Local implementer/reviewer. Phase: operator-selected Docker profile and receipt wiring check. Final technical decision owner: Local. No external repository or runtime was absorbed.

## Scope / Methodology

Docker Desktop 29.7.2 with Compose 5.5.1 was available. A temporary build context under the Windows user Temp directory was made with `git archive HEAD` for the web app, its eight local `file:` packages, and Governance Engine. The ignored `.env.netlify`, host `node_modules`, and other untracked files were absent. The engine used `python:3.11-slim-trixie`; web used `node:22.14.0-alpine3.21` and `npm ci`. Both containers used one Docker network with `internal=true`; no host port was published. A generated synthetic service token was supplied only to the container environment and was not printed. Web ran the Next development command directly, using tracked generated risk/skill files; `predev` needs additional canonical corpora outside this bounded build context.

The HTTP probe logged in with a documented development mock user, signed an exact synthetic export body with the configured service token, and called the real `/api/artifacts/export` route. The export helper then called the real `/api/governance/evaluate` route, which called the real Governance Engine `/api/v1/evaluate`; no fetch was intercepted. The Python engine appended a block to its sandbox ledger. The probe compared the returned receipt ID to the last ledger event request ID and checked the complete local ledger hash chain. Probe content was synthetic and contained no user document or provider credential.

## Findings / Position

| Finding | Observation and correction | Disposition |
|---|---|---|
| Tracked `ledger_chain.json` has an object shape while this engine's `ImmutableLedger.append_event` expects a list | First Docker image reached the engine but `/api/v1/evaluate` returned 500 and the export remained `DRAFT_UNACCEPTED` without receipt. The sandbox image excluded only that tracked ledger data file; server initialization then created a fresh empty list. Source ledger data and repository file were untouched. | SANDBOX_PROFILE_CORRECTED; packaging/retention owner remains open |
| Export helper expected `report.status/risk_level` and `execution_record.request_id/timestamp`, which the current engine does not return | A real evaluate call returned `request_summary`, `decision_analysis`, `report_metadata`, `cvf_risk_level`, `integrity`, and an execution record containing `final_decision`/`ledger_attached`. `proof.ts` now joins exact request and artifact IDs, matching decision, attached ledger signal, metadata time, and bounded risk before returning a receipt. The older explicit approval envelope remains supported. | SOURCE_BRIDGE_REPAIRED_BOUNDED |
| Engine returned `final_decision=ALLOW` with `cvf_enforcement.action=LOG_ONLY` for the synthetic REVIEW request | The new receipt reports raw decision `ALLOW`; the export state remains `DRAFT_UNACCEPTED`. This is evidence of evaluation and ledger wiring, not approval or artifact acceptance. | NO_AUTHORITY_PROMOTION |

Final rebuilt web image: `sha256:9b7bd254f58022e6353d4750b130287c9b70231e5f2d1283555f0ca22c6d5845`. Fresh-ledger engine image: `sha256:edeb72b39338804c46628c8632cde7ebf3e249099f68aacb305d6f3fb1023461`. The final HTTP probe returned `200`, `success=true`, `routeAuthMode=service_token`, `receiptDecision=ALLOW`, `receiptRisk=R0`, `verification=8/8`, and `governanceState=DRAFT_UNACCEPTED`. Its receipt ID was `artifact-proof-q001-docker-1790614327928-1790614329419`; the final sandbox ledger block carried exactly that `request_id`, `final_decision=ALLOW`, and SHA-256 block hash `d250be1b3e658885a30c5185873adca1435e5ddfd760fcdb7a37049467765528`. All four sandbox block hashes and previous-hash links verified. The measured request elapsed time was 1,758 ms in this one development-mode run, not a latency bound.

Focused route/component tests passed 40/40; TypeScript and targeted ESLint passed. Tests cover the current engine shape and mismatched request ID, artifact ID, decision, and missing ledger attachment. `git diff --check` passed. The earlier seeded-ledger failure also demonstrated the export remains draft when the downstream evaluation fails, but it was not a planned negative-test matrix.

## Risk / Corrective Action

The source of the tracked object-shaped ledger file must be reconciled with the running engine's list-based storage contract before a packaged durable deployment; excluding it was an explicit sandbox-only profile choice. The runtime ledger lived inside an ephemeral container, so this run does not establish retention, backup or recovery. The engine's `LOG_ONLY` enforcement despite `ALLOW` decision is a separate owner-contract issue; no approval is inferred. No real UI walkthrough, hosted Netlify call, real provider API call, production authentication, broad secret-scan proof, cost budget, latency distribution, or RPO/RTO measurement occurred. Q001 and R0 exit remain open; P11 and external runtimes remain parked.

## Decision / Recommendation / Disposition

Accept only the observed **local Docker receipt wiring** and the narrow response-shape source repair as bounded evidence. Keep the HTML result draft and unaccepted. Next Q001 work should settle the ledger packaging/retention contract and enforcement semantics, then run an authorized UI/effect profile and applicable live-provider release proof separately. No automatic public sync, deployment or pilot closure follows this packet.

## Epistemic Process Block

### Expected Result / Prediction

Two real local services with an absolute receipt URL and aligned engine URL would return a Q001 receipt joined to a ledger event.

### Evidence Comparison

The first image failed on seeded ledger shape. After a fresh sandbox ledger, the engine returned 200 and appended a block but the helper still omitted the receipt because its assumed response fields were absent. The narrow bridge repair produced a receipt whose ID matched the final ledger event, with a valid local hash chain.

### Contradiction Or Gap Disposition

The response-shape contradiction is repaired in web source and tested. The packaged ledger shape, enforcement interpretation and durable/live profile remain open, named above.

### Claim Update

Q001 has bounded real local receipt wiring evidence. It has no artifact-acceptance, provider-live, hosted or production-readiness proof from this run.

## Finding-To-Governance Learning Disposition

| Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|
| RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | DESIGN_REVIEW_REQUIRED | Bind the engine response shape, enforcement decision and ledger packaging in the existing Q001 owner contract before deployment-profile promotion. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | `Target / Source`, `Scope / Methodology`, `Findings / Position`, `Risk / Corrective Action`, `Decision / Recommendation / Disposition`, `Evidence Comparison`, `Contradiction Or Gap Disposition`, `Claim Update`, `Public Export Disposition` |
| gateRunPurpose | Confirmation of the packet shape and local evidence after source read-ahead, not first discovery of checker requirements. |
| claimBoundary | Checker compliance cannot turn local synthetic integration evidence into live/provider or artifact-acceptance proof. |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local single agent in implementer and reviewer roles |
| Provider or surface | Private CVF workspace and local Docker Desktop |
| Session or invocation | Q001 Docker receipt check, 2026-09-28 |
| Working directory | Repository root and isolated Windows Temp build context |
| Command or tool surface | `git archive`, Docker build/run/exec, Node HTTP probe, Python ledger hash verification, Vitest, TypeScript, ESLint |
| Target paths | `proof.ts`, `route.test.ts`, this review; temporary image context outside repository |
| Allowed scope source | Operator instruction to run the Q001 Docker receipt proof |
| Before status evidence | clean `6158b042c` worktree; Q001 source repair accepted bounded |
| After status evidence | two source/test files and this review pending; 40/40 focused tests and Docker receipt/ledger join |
| Diff evidence | working-tree Git diff and local Docker image digests above |
| Approval boundary | synthetic local service path only; no provider/live, public write, deployment or pilot acceptance |
| Claim boundary | bounded receipt transport and sandbox ledger append only |
| Agent type | Codex (shared-workspace INTERNAL_AGENT) |
| Invocation ID | q001-docker-receipt-20260928 |
| Expected manifest | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.test.ts`; `docs/reviews/CVF_CVF_NCR_Q001_DOCKER_RECEIPT_WIRING_EVIDENCE_2026-09-28.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Actual changed set | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.test.ts`; `docs/reviews/CVF_CVF_NCR_Q001_DOCKER_RECEIPT_WIRING_EVIDENCE_2026-09-28.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | Q001 local two-service receipt wiring |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: real local HTTP and ledger event only |
| receiptEvidence | CVF_RECEIPT_PRESENT: response receipt ID equals the final sandbox ledger event request ID |
| actionEvidence | ACTION_EVIDENCE_PRESENT: one matching ledger append with valid local hash-chain links |
| invocationBoundary | two isolated Docker containers, development mock login, synthetic request and no external provider |
| interceptionBoundary | no HTTP fetch interception in final Docker probe; focused Vitest fixtures are separate |
| claimLanguage | local receipt/effect integration observed; approval, acceptance and live governance unclaimed |
| forbiddenExpansion | no P11, external runtime, Netlify, public sync, production readiness or live-provider inference |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This private packet records an observed local integration result. A source-produced `ALLOW` decision with `LOG_ONLY` enforcement is not artifact approval, and the HTML packet remains draft and unaccepted.
