# CVF NCR Q001 Single OAuth Identity Binding

Memory class: governed-review

docType: review

Status: BOUNDED_SOURCE_CONTRACT_PRODUCTION_PROFILE_OPEN

Date: 2026-09-29

Text Encoding Exception: the moved login client retains source-faithful Vietnamese product copy; its existing local source note applies. This packet is ASCII.

Decision owner: Local reviewer/closer. External Web remains advisory and was not invoked.

executionBaseHead: `6f5dd1715`

## Purpose

Prepare Q001 for one real OAuth provider without granting a newly authenticated provider user a default CVF role. The preceding Q001 review blocked a production-like profile because Auth.js required both GitHub and Google client pairs, while its session callbacks assigned absent OAuth authority the default developer/org/team values.

## Target / Source

Owners: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/auth.ts`, `src/lib/middleware-auth.ts`, the login page/client, focused tests, `.env.example`, and `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`. Earlier disposition: `docs/reviews/CVF_CVF_NCR_Q001_PRODUCTION_AUTH_PROFILE_BOUNDARY_2026-09-29.md`. Role: shared-workspace INTERNAL_AGENT Local implementer/reviewer. Phase: Q001 local identity/profile contract. Final technical decision owner: Local.

## Scope / Methodology

Outside test/development, `CVF_OAUTH_PROVIDER` now selects exactly `github` or `google`; the environment invariant requires only that provider's client pair, `NEXTAUTH_SECRET`, `NEXTAUTH_URL`, and at least one exact CVF binding. `CVF_OAUTH_IDENTITY_BINDINGS_JSON` contains strict entries keyed by provider and exact provider account ID, with explicit CVF `userId`, `role`, `orgId`, and `teamId`. Malformed entries, unknown roles, duplicate subjects, empty selected-provider coverage, unknown subjects, and revoked bindings fail closed. The production Auth.js provider list contains only the selected provider; the mock credentials provider remains local-only. The login route is a dynamic server wrapper that passes provider selection to its client UI without exposing server configuration through a public environment variable.

The Auth.js sign-in/JWT callbacks require a binding before creating an OAuth session, tag the token as bound, and re-resolve that binding on later JWT callbacks. Request-bound and ambient session readers reject old or unbound production tokens and derive role/org/team from the current binding rather than caller claims. This includes removal of a binding from the running configuration; actual configuration propagation and revocation timing in a deployment remain unmeasured. Test/development mock behavior remains available for the existing Q001 Docker profile.

Focused Vitest passed 36/36 across Auth.js invariants/callbacks, strict binding parsing, session reader and login UI. Three adjacent export/admin/route-governance suites passed 41/41. TypeScript and targeted ESLint passed. All identities and client strings in these tests are synthetic; no OAuth authorization URL, callback, provider account, credential, production build or external API was used.

## Findings / Position

| Finding | Evidence | Disposition |
|---|---|---|
| Both OAuth client pairs were mandatory for a one-provider Q001 profile | Source invariant and new GitHub-only/Google-only tests | SOURCE_CONTRACT_CORRECTED_BOUNDED |
| OAuth user/session previously inherited default developer/org/team values | Auth.js and request/ambient session source; negative and claim-override tests | SOURCE_AUTHORITY_GAP_CORRECTED_BOUNDED |
| Actual OAuth identity, role decision and latency | No operator-selected provider, provider subject, real client configuration or callback run | OPEN; no live/deployment/acceptance claim |

## Risk / Corrective Action

The operator must still select a provider and approve an exact subject-to-CVF identity/role/org/team binding. A binding can grant a privileged role, so its provenance and change control require review before a real sign-in. The configured JSON is not an automatically discovered user directory. A running process may retain old environment configuration until restart; revocation timing must be measured in the later profile. This change does not prove callback correctness, session persistence, real Work Transfer access, receipt latency, P08 broad secret scan, ledger retention/backup, deployment cost, provider governance or HTML artifact acceptance.

## Decision / Recommendation / Disposition

Accept the provider-selection and explicit identity-binding source contract with hermetic evidence only. Keep Q001 and P11 at their existing boundaries. The next operator checkpoint should select GitHub or Google and a test subject/role after Local source review; place credentials and binding in controlled configuration, then authorize one bounded OAuth login/profile run. No secret should be sent in chat.

## Epistemic Process Block

### Expected Result / Prediction

One selected OAuth provider should suffice to initialize the profile, and an unbound or revoked provider subject should never acquire CVF's default developer authority.

### Evidence Comparison

GitHub-only and Google-only invariant tests passed. Callback tests denied unknown subjects and removed bindings. Session tests rejected unbound production tokens and ignored forged role/org/team claims in favor of the current binding. Login tests showed only the selected provider control.

### Contradiction Or Gap Disposition

The source contract matches the prediction in hermetic tests, but no real provider or production build was exercised. Runtime callback, configuration propagation and receipt latency remain separate evidence requirements.

### Claim Update

Q001 can be configured for one explicitly selected OAuth provider with no automatic CVF role assignment. Production-like end-to-end evidence is still absent.

## Finding-To-Governance Learning Disposition

| Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|
| RULE_GAP | GOVERNANCE_CONTROL_PLANE | DESIGN_REVIEW_REQUIRED | Review and approve the exact provider-subject-to-CVF-role binding before live sign-in. |
| RUNTIME_SIGNAL_GAP | RUNTIME_BEHAVIOR_LEARNING | DESIGN_REVIEW_REQUIRED | Measure callback, session, revocation and first-export latency in a bounded configured profile. |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_agent_packet_authority_and_encoding.py` |
| literalTokensReviewed | `Target / Source`, `Scope / Methodology`, `Findings / Position`, `Risk / Corrective Action`, `Decision / Recommendation / Disposition`, `Evidence Comparison`, `Contradiction Or Gap Disposition`, `Claim Update`, `Public Export Disposition`, `Text Encoding Exception` |
| gateRunPurpose | Confirm the bounded source/test packet shape before closure; checker pass is not first discovery of evidence requirements. |
| claimBoundary | Gates do not prove OAuth callback, real subject control or production latency. |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local single agent in implementer and reviewer roles |
| Provider or surface | Private CVF workspace and local hermetic tests |
| Session or invocation | Q001 single OAuth identity binding, 2026-09-29 |
| Working directory | Private repository root and cvf-web package |
| Command or tool surface | Source audit, apply_patch, Vitest, TypeScript, ESLint and governed gates |
| Target paths | Auth.js, session reader, OAuth binding module, login route/client, tests, `.env.example`, this review and NCR roadmap |
| Allowed scope source | Operator `ok. vay tiep tuc` following the Q001 OAuth checkpoint explanation |
| Before status evidence | Clean `6f5dd1715`; source required both OAuth pairs and defaulted external identities to developer/org/team |
| After status evidence | 36/36 focused, 41/41 adjacent route/auth suites, TypeScript and ESLint PASS; material commit pending |
| Diff evidence | Exact working-tree diff and focused test results |
| Approval boundary | No real credential, OAuth callback, provider call, deployment, public sync or P11 |
| Claim boundary | Provider selection and identity-binding source contract only |
| Agent type | Codex (shared-workspace INTERNAL_AGENT) |
| Invocation ID | q001-single-oauth-binding-20260929 |
| Expected manifest | ten web source/test/config paths; this review; NCR roadmap |
| Actual changed set | ten web source/test/config paths; this review; NCR roadmap |
| Manifest delta | MATCH |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | Q001 one-provider OAuth source contract |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: local tests and source trace only |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no real OAuth or new governance receipt was produced |
| actionEvidence | ACTION_EVIDENCE_PRESENT: focused tests exercised provider selection, exact binding, denial and revocation paths |
| invocationBoundary | Hermetic local test runner; no provider or deployment |
| interceptionBoundary | Tests mock NextAuth package integration while exercising real callback/source functions; no live interception claim |
| claimLanguage | Explicit binding contract in source; real sign-in and production readiness unclaimed |
| forbiddenExpansion | No artifact acceptance, provider-live proof, P11, public sync or deployment inference |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Claim Boundary

No provider subject, client credential or real OAuth callback was available. A user and role binding must be separately reviewed and a real sign-in must be observed before Q001's production-like profile advances.
