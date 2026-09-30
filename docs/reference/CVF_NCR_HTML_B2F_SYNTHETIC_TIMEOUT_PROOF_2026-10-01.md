# CVF NCR HTML B2f Synthetic Timeout Proof

Memory class: governed-reference

docType: reference

Status: WORKER_DRAFT_PENDING_LOCAL_REVIEW

Batch ID: CVF-NCR-HTML-B2F-SYNTHETIC-TIMEOUT

## Purpose

Define what the B2f focused test proves about the actual export route's receipt POST timing out against a delayed inert loopback stub and the panel's ambiguous-outcome presentation, and what it does not. Files: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-loopback-timeout.spec.ts` and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/support/b2f-loopback-timeout-harness.cjs`. Observed values are in `docs/reviews/evidence/cvf-ncr-html-b2f-timeout-worker-proof-2026-10-01.json`. B2d proved the no-hop branch (`NOT_CONFIGURED`) and B2e the invalid/unavailable configured-hop failures; B2f covers only `TIMED_OUT`.

## Scope / Applies To

One fresh local Next test server started by the mock Playwright config, one headless Chromium page, one synthetic form input and one delayed stub that never answers within the receipt timeout. It applies to no other route, browser, environment or input.

## Scope / Target / Owner Boundary

Target: the route's `governanceReceiptStatus` of `TIMED_OUT`, the attempt ID, absent receipt and `DRAFT_UNACCEPTED` state, and the panel's timeout warning and attempt ID display. The export route, receipt helper, Next evaluate route, engine client, auth and panel are read-only. The worker owns only the five B2f create paths; Local owns review, independent probe, commit and continuity; the operator owns real-data, store and effect decisions.

## How The Run Is Invoked

Run `node tests/e2e/support/b2f-loopback-timeout-harness.cjs` from the cvf-web directory (`--help` prints usage; no other argument is accepted). The harness binds the stub on `127.0.0.1`, self-tests it, picks a free port for a fresh Next server and spawns Playwright with the mock config on the spec. It forces, in the child environment only: `NEXTAUTH_URL` to the exact stub origin, `AUTH_URL` to the fresh server origin, `GOVERNANCE_ENGINE_ENABLED=false`, a dead engine URL, a synthetic service token and `CVF_GOVERNANCE_RECEIPT_TIMEOUT_MS=1000`. Credential-like variables inherited from the parent are dropped. The harness is also loaded as a `--require` preload through `NODE_OPTIONS` in every child process. Without the harness the spec is skipped and issues no export request. The stub holds the one expected receipt POST for 3,500 ms (the 1,000 ms timeout plus a 2,500 ms margin), then only observes whether a client is still connected.

## Isolation Preflight

The first test issues no export request and must pass before the export test runs (serial mode). It requires: the stub is bound to IPv4 `127.0.0.1` and its origin matches; four self-test requests, including one carrying the expected artifact ID, were rejected with 404 and no run-phase request exists yet; log paths are absolute and outside the repository; `NODE_OPTIONS` names the harness; every fresh Next server context that has loaded its env reports, from inside the server, `NEXTAUTH_URL` equal to the stub origin, `AUTH_URL` equal to the server origin, engine flag `false`, receipt timeout `1000` and the synthetic token (compared by hash, never logged); zero evaluate fetches and zero Next governance route hits; and browser login plus `/api/auth/session` succeed under the forced origin.

## What The Export Test Does

1. Logs in, opens the Artifacts page and fills Title, Source notes and Receipt reference (`b2f-timeout-case`) with synthetic text.
2. Clicks Build HTML and captures the real route response passively with `waitForResponse`; the endpoint is never routed, fulfilled or mocked.
3. Requires HTTP 200, `TIMED_OUT`, no receipt, `DRAFT_UNACCEPTED` and an attempt ID `artifact-proof-b2f-timeout-case-<timestamp>`.
4. Requires exactly one expected POST at the stub, received before the route response, with the same request ID as the attempt ID, the expected artifact ID and excerpt length, and the synthetic service token present; requires the route to respond about one configured timeout after the stub received the POST and before the stub's planned reply, with no late reply yet recorded.
5. Requires the panel to show the draft state, the exact timeout warning that the service may still have processed the request and an operator should check the attempt ID before trying again, the same attempt ID, no receipt badge or approved/evaluated/denied note, and no safe-retry, cancel, rollback or stopped wording; requires the preview heading to equal the built title.
6. Records, without asserting as a guarantee, the client disconnect and the late-reply outcome seen by the stub, then requires one run-phase stub request with none unexpected, one evaluate fetch whose destination equals the stub origin, and zero Next governance route hits.

## What A Pass Shows

For this synthetic input, the actual export route sent its configured receipt POST to a loopback stub that cannot forward, received no reply within the configured 1,000 ms, and returned `TIMED_OUT` with the attempt ID the stub saw; the panel presented the ambiguous outcome as draft with a warning and no receipt. No request reached the actual Next evaluate route, the Governance Engine or a provider in any server context that logged. The real `.env.local` service token was overridden and never sent to the stub.

## Not Proven

- Remote cancellation, rollback, that no remote work occurred, or that retry is safe. The recorded client disconnect and the late reply finding no connected client describe the stub's view only; an abort does not prove remote work stopped, and no receipt does not imply safe retry.
- That every server execution context loaded the preload; 13 server contexts were logged, but the route handler's own context is not individually identified. The stub ledger (exact request ID) and the `evaluate_fetch` destination are the direct evidence.
- Non-forwarding is by design and source inspection of the stub (no outbound client, no reply body in the recorded run), not by a network-level trace.
- Receipt validity, the `PRESENT` branch (none is fabricated), governance or engine behavior, the real Next evaluate route, provider behavior, production network transport, other browsers, timeout values other than 1,000 ms, durable storage, artifact acceptance, Q001/Q004 Profile A, Profile B/C, pilot/live, P11, public sync and deployment.

## Claim Boundary

Synthetic configured-hop transport timeout and panel presentation evidence for one focused run only. A timed-out stub exchange is not a governance receipt and not evidence about remote state. It does not ratify a store, writer, route, retry policy or acceptance, and it does not edit or approve production code.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
