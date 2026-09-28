# CVF NCR Q001 Production Auth Profile Boundary

Memory class: governed-review

docType: review

Status: BOUNDED_SOURCE_CORRECTION_PRODUCTION_PROFILE_OPEN

Date: 2026-09-29

Text Encoding Exception: the login page retains and extends source-faithful Vietnamese product copy; source comments and this packet remain ASCII.

Decision owner: Local reviewer/closer. External Web remains advisory and was not invoked.

executionBaseHead: `25aeca738`

## Purpose

Resolve the Auth.js mock-login contradiction exposed while preparing Q001's production-like HTML export profile. Required OAuth environment variables did not prevent the known mock `owner/owner123` credentials path from creating a session. The production login page also advertised those accounts.

## Target / Source

The source owners are `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts`, `src/app/login/page.tsx`, their focused tests and `.env.example`. Prior production-like build blocker: `docs/reviews/CVF_CVF_NCR_Q001_RECEIPT_STATUS_CORRECTION_2026-09-29.md`. The earlier CADP audit `docs/audits/CVF_CADP_AI_T5_R3_EXTERNAL_AUTHENTICATION_OWNER_ADOPTION_READINESS_DECISION_2026-08-15.md` identified the mock credentials risk; the later T5-R5 invariant guarded required configuration and the legacy admin fallback, but the known mock-user branch remained reachable outside development/test. Role: shared-workspace INTERNAL_AGENT Local implementer/reviewer. Phase: bounded Q001 production-auth source correction. Final technical decision owner: Local.

## Scope / Methodology

Source inspection found that `validateAuthEnvironmentInvariants` requires `NEXTAUTH_SECRET` and both GitHub/Google client pairs outside test/development, yet `CredentialsProvider.authorize` checked `findMockUserByUsername` before any environment guard. The correction returns `null` from that provider outside test/development. The login page now shows the documented mock form/accounts only in those two environments; its production branch presents GitHub and Google sign-in controls. `.env.example` lists required Auth.js variables and the Q001 receipt-hop settings without values.

Focused Vitest 14/14, TypeScript and targeted ESLint passed. The tests assert known owner credentials are rejected in production, retained in development, and that production UI omits mock credentials while offering the configured-provider controls. The first UI test run had one assertion typo (`Enterprise Mock Accounts` omitted the rendered colon); after correcting that matcher, the focused suite passed. No provider account, OAuth callback, production credential or network login was used. No production build was reclassified as passed.

## Findings / Position

| Finding | Evidence | Disposition |
|---|---|---|
| Known mock-user branch remained usable with production `NODE_ENV` if Auth.js required values were present | Direct source trace and focused negative regression | SOURCE_DEFECT_CORRECTED_BOUNDED |
| Production login advertised demo credentials and had no visible external-provider route | Client page source and focused UI tests | PRESENTATION_CORRECTED_BOUNDED |
| Real production-like Q001 export profile | Valid OAuth client configuration, callback, real identity/role mapping, source record, and deployed latency evidence are absent from this local run | OPEN; no production or acceptance claim |

## Risk / Corrective Action

OAuth button presence and required environment documentation do not prove a working real OAuth login. The existing JWT callback maps provider users to default developer/org/team values when source-specific authority is absent; its role/identity policy requires separate review before production admission. A legitimate provider configuration and controlled test identity are needed for a production-like browser profile. The operator-owned secret store must supply values; placeholder credentials must not be used to bypass the invariant. Q001's P08 broad scan, receipt-hop deployment latency, ledger retention/backup/restore, cost and provider/live proof remain open.

## Decision / Recommendation / Disposition

Accept only the fail-closed source/test correction and configuration inventory. Keep Q001 open and P11 parked. The next admissible production-like run requires a reviewed OAuth identity/role policy plus operator-controlled real configuration and a named effect/profile scope; it cannot be inferred from this hermetic test.

## Epistemic Process Block

### Expected Result / Prediction

The existing environment invariant might have made the demo account unusable in production once OAuth values were configured.

### Evidence Comparison

The source placed the mock-user password check inside the credentials provider without an environment condition, contradicting that prediction. Focused negative and development-preservation tests passed after the guard was added; the UI test confirmed the production mock disclosure was removed.

### Contradiction Or Gap Disposition

Configuration presence alone was an incomplete auth boundary. Source correction closes this specific branch, while real OAuth authentication and identity authorization remain untested and unaccepted.

### Claim Update

The local source now fails closed for known mock credentials outside test/development. Production-like Auth.js/receipt latency proof remains open.

## Finding-To-Governance Learning Disposition

| Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|
| RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | Review external-provider identity/role mapping before any production-like Q001 browser acceptance; retain the auth negative regression. |
| RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | DESIGN_REVIEW_REQUIRED | Measure OAuth-authenticated first-export receipt latency only after a valid identity/role profile is available. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_delta_execution_claim_boundary.py` |
| literalTokensReviewed | `Target / Source`, `Scope / Methodology`, `Findings / Position`, `Risk / Corrective Action`, `Decision / Recommendation / Disposition`, `Evidence Comparison`, `Contradiction Or Gap Disposition`, `Claim Update`, `Public Export Disposition` |
| gateRunPurpose | Confirm known review structure and bounded claim before closure, not discover token requirements from a failing gate. |
| claimBoundary | Structural checker success cannot prove OAuth behavior, production readiness or artifact acceptance. |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local single agent in implementer and reviewer roles |
| Provider or surface | Private CVF workspace; local hermetic web tests |
| Session or invocation | Q001 production-auth source boundary, 2026-09-29 |
| Working directory | Private repository root and cvf-web package |
| Command or tool surface | Source audit, apply_patch, Vitest, TypeScript, ESLint and governed gates |
| Target paths | Auth.js source/test, login page/test, `.env.example`, this review and NCR roadmap |
| Allowed scope source | Operator `next` at the Q001 production-like profile checkpoint |
| Before status evidence | Clean `25aeca738`; production-like build previously blocked by missing required Auth.js configuration |
| After status evidence | Focused auth/UI negative tests 14/14, TypeScript and ESLint PASS; material commit pending |
| Diff evidence | Exact working-tree source diff and tests |
| Approval boundary | No real credentials, provider call, deployment, public sync or P11 |
| Claim boundary | Source fail-closed correction only; production-like runtime profile still open |
| Agent type | Codex (shared-workspace INTERNAL_AGENT) |
| Invocation ID | q001-production-auth-boundary-20260929 |
| Expected manifest | Auth.js source/test; login page/test; `.env.example`; this review; NCR roadmap |
| Actual changed set | Auth.js source/test; login page/test; `.env.example`; this review; NCR roadmap |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | Q001 Auth.js source and UI environment boundary |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: local negative tests and source trace only |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no new governance receipt or real provider session was produced |
| actionEvidence | ACTION_EVIDENCE_PRESENT: focused tests executed the known mock credentials rejection and UI branch |
| invocationBoundary | Hermetic local tests, no provider API or OAuth callback |
| interceptionBoundary | Vitest mocks NextAuth package integration for source-level auth tests; no production request interception claim |
| claimLanguage | Known mock credential branch rejects outside test/development; no live or deployed assertion |
| forbiddenExpansion | No artifact acceptance, production readiness, P11, public sync or provider-live inference |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

This review establishes a bounded source correction. A real OAuth identity and role policy, configuration and browser run are still required before Q001's production-like profile can be assessed.
