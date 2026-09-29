# CVF NCR Q001 GitHub Local OAuth Profile

Memory class: POINTER_RECORD

Status: LOCAL_ADMIN_BINDING_CONFIGURED_GITHUB_CLIENT_PENDING

docType: reference

Date: 2026-09-29

## Purpose

Record the exact local GitHub OAuth setup for the bounded Q001 sign-in and receipt profile. This is a configuration recipe, not a completed login or governance proof. Local owns private-CVF verification and final technical disposition.

## Scope / Applies To

Applies to the operator's selected local Q001 GitHub sign-in profile and Local verification of its account binding, callback, session, and receipt. The operator selected `admin` for the comprehensive test and controls the GitHub OAuth App. Local owns the technical evidence disposition.

## Fixed Profile Inputs

| Input | Value / evidence |
|---|---|
| Provider | `github`, selected by operator |
| Browser origin and `NEXTAUTH_URL` | `http://127.0.0.1:3000`; port 3000 was not listening at preflight on 2026-09-29 |
| GitHub OAuth App homepage | `http://127.0.0.1:3000` |
| GitHub OAuth App authorization callback | `http://127.0.0.1:3000/api/auth/callback/github` |
| Public account candidate | `Blackbird081`; `https://api.github.com/users/Blackbird081` returned numeric ID `206422451` on 2026-09-29 |
| Auth.js subject representation | Installed GitHub provider converts profile `id` to string; candidate `providerAccountId` is `"206422451"` |
| CVF binding | `provider=github`, `providerAccountId="206422451"`, `userId=usr_github_206422451`, `role=admin`, `orgId=org_cvf`, `teamId=team_exec`; operator selected `admin` for the local test |
| Local config | Ignored `.env.local` has the binding, provider, URL, and a locally generated session secret; GitHub client ID/secret are absent |

The GitHub login email is not the CVF authority key. The public account lookup identifies a candidate only; control of that account must be established by a real OAuth callback.

## Operator Configuration

1. Register one GitHub OAuth App under the intended GitHub account or organization at GitHub Settings > Developer settings > OAuth apps > New OAuth App. Use the homepage and callback above. GitHub's [OAuth App registration guide](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app) describes these fields. Do not put private CVF paths or secrets in the public application name or description.
2. Put the generated client ID and client secret in the controlled local configuration as `GITHUB_ID` and `GITHUB_SECRET`. The ignored `cvf-web/.env.local` already contains the other Q001 values and a generated `NEXTAUTH_SECRET`; `git check-ignore` confirms `.env.local` is ignored. Do not send secret values through chat or commit them.
3. Keep the reviewed `CVF_OAUTH_IDENTITY_BINDINGS_JSON` keyed to subject `"206422451"`; do not substitute the username or email. The distinct CVF user ID keeps admin audit attribution separate from the seeded mock admin. `admin` can access admin API routes; owner-only actions still require `owner`.
4. Run the web package on the local browser origin above with the real configuration. If port/origin changes, update `NEXTAUTH_URL` and the OAuth App callback together. GitHub's [authorization flow and redirect rules](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps) govern the callback match.

## Bounded Verification To Collect

- Observe a successful GitHub redirect and callback, then verify `/api/auth/me` reports the bound CVF user/role/org/team. Record only safe identifiers and status; do not record codes, tokens, cookies, or headers.
- Verify an unbound account is denied if one is available, and that removing the binding invalidates subsequent use after controlled configuration propagation. Do not infer immediate revocation from source tests.
- Exercise one Work Transfer HTML export with the authenticated session and join the receipt ID to the governance ledger. Keep `DRAFT_UNACCEPTED` distinct from a receipt `ALLOW` decision. Measure first and warm export latency separately.

## Claim Boundary

Existing source tests cover the binding contract, and the ignored local file now holds an operator-selected admin binding and session secret. No GitHub OAuth App, client pair, real callback, local production-like build, or account-control proof was present when this revision was written. Provider-side documentation is advisory for registration and redirect behavior; the installed Auth.js source and CVF code are the local implementation evidence. P11, public export, deployment, artifact acceptance, and production readiness remain parked.

EPISTEMIC_PROCESS_NA_WITH_REASON: this pointer records selected inputs, source-verified callback construction, and a future verification recipe; it does not close an empirical runtime claim.
