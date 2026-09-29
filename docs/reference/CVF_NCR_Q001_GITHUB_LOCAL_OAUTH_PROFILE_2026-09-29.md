# CVF NCR Q001 GitHub Local OAuth Profile

Memory class: POINTER_RECORD

Status: OPERATOR_CONFIGURATION_PENDING

docType: reference

Date: 2026-09-29

## Purpose

Record the exact local GitHub OAuth setup for the bounded Q001 sign-in and receipt profile. This is a configuration recipe, not a completed login or governance proof. Local owns private-CVF verification and final technical disposition.

## Scope / Applies To

Applies to the operator's selected local Q001 GitHub sign-in profile and Local verification of its account binding, callback, session, and receipt. The operator controls the GitHub OAuth App and CVF role decision; Local owns the technical evidence disposition.

## Fixed Profile Inputs

| Input | Value / evidence |
|---|---|
| Provider | `github`, selected by operator |
| Browser origin and `NEXTAUTH_URL` | `http://127.0.0.1:3000`; port 3000 was not listening at preflight on 2026-09-29 |
| GitHub OAuth App homepage | `http://127.0.0.1:3000` |
| GitHub OAuth App authorization callback | `http://127.0.0.1:3000/api/auth/callback/github` |
| Public account candidate | `Blackbird081`; `https://api.github.com/users/Blackbird081` returned numeric ID `206422451` on 2026-09-29 |
| Auth.js subject representation | Installed GitHub provider converts profile `id` to string; candidate `providerAccountId` is `"206422451"` |
| CVF role/org/team | PENDING_OPERATOR_ROLE_DECISION; no active binding is recorded by this document |

The GitHub login email is not the CVF authority key. The public account lookup identifies a candidate only; control of that account must be established by a real OAuth callback.

## Operator Configuration

1. Register one GitHub OAuth App under the intended GitHub account or organization at GitHub Settings > Developer settings > OAuth apps > New OAuth App. Use the homepage and callback above. GitHub's [OAuth App registration guide](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app) describes these fields. Do not put private CVF paths or secrets in the public application name or description.
2. Put the generated client ID and client secret in the controlled local configuration as `GITHUB_ID` and `GITHUB_SECRET`. Generate a separate `NEXTAUTH_SECRET`. Use the ignored `cvf-web/.env.local` or another controlled secret store; `git check-ignore` confirms `.env.local` is ignored. Do not send secret values through chat or commit them.
3. After the operator selects the CVF role, Local will review one binding of provider `github`, subject `"206422451"`, explicit CVF `userId`, `role`, `orgId`, and `teamId` for `CVF_OAUTH_IDENTITY_BINDINGS_JSON`. Do not substitute the username or email for the provider account ID.
4. Run the web package on the local browser origin above with the real configuration. If port/origin changes, update `NEXTAUTH_URL` and the OAuth App callback together. GitHub's [authorization flow and redirect rules](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps) govern the callback match.

## Bounded Verification To Collect

- Observe a successful GitHub redirect and callback, then verify `/api/auth/me` reports the bound CVF user/role/org/team. Record only safe identifiers and status; do not record codes, tokens, cookies, or headers.
- Verify an unbound account is denied if one is available, and that removing the binding invalidates subsequent use after controlled configuration propagation. Do not infer immediate revocation from source tests.
- Exercise one Work Transfer HTML export with the authenticated session and join the receipt ID to the governance ledger. Keep `DRAFT_UNACCEPTED` distinct from a receipt `ALLOW` decision. Measure first and warm export latency separately.

## Claim Boundary

Existing source tests cover the binding contract, but no GitHub OAuth App, real client secret, callback, local production-like build, or account-control proof was present when this profile was written. Provider-side documentation is advisory for registration and redirect behavior; the installed Auth.js source and CVF code are the local implementation evidence. P11, public export, deployment, artifact acceptance, and production readiness remain parked.

EPISTEMIC_PROCESS_NA_WITH_REASON: this pointer records selected inputs, source-verified callback construction, and a future verification recipe; it does not close an empirical runtime claim.
