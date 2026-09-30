# CVF NCR HTML B2e Synthetic Loopback Receipt Proof

Memory class: governed-reference

docType: reference

Status: WORKER_DRAFT_PENDING_LOCAL_REVIEW

Batch ID: CVF-NCR-HTML-B2E-SYNTHETIC-LOOPBACK

## Purpose

Define what the B2e focused test proves about the configured server-side receipt POST of the real export route and the panel's display of a fabricated failure, and what it does not. Files: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-loopback-receipt.spec.ts` and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/support/b2e-loopback-receipt-harness.cjs`. Observed values are in `docs/reviews/evidence/cvf-ncr-html-b2e-loopback-worker-proof-2026-09-30.json`. B2d proved the no-hop branch (`NOT_CONFIGURED`); B2e covers the configured branch against an inert destination.

## Scope / Applies To

One fresh local Next test server started by the mock Playwright config, one headless Chromium page, two synthetic form inputs and two fabricated stub replies (HTTP 200 with incomplete JSON, and HTTP 503). It applies to no other route, browser, environment or input.

## Scope / Target / Owner Boundary

Target: the route's `governanceReceiptStatus`, attempt ID, absent receipt and `DRAFT_UNACCEPTED` state, and the panel's failure note and attempt ID display. The export route, receipt helper, Next evaluate route, engine client, auth and panel are read-only. The worker owns only the five B2e create paths; Local owns review, independent probe, commit and continuity; the operator owns real-data, store and effect decisions.

## How The Run Is Invoked

Run `node tests/e2e/support/b2e-loopback-receipt-harness.cjs` from the cvf-web directory (`--help` prints usage; no other argument is accepted). The harness binds the stub, self-tests it, picks a free port for a fresh Next server and spawns Playwright with the mock config on the spec. It forces, in the child environment only: `NEXTAUTH_URL` to the exact stub origin, `AUTH_URL` to the fresh server origin (so browser auth does not follow the stub origin), `GOVERNANCE_ENGINE_ENABLED=false`, a dead engine URL and a synthetic service token. Credential-like variables inherited from the parent are dropped. The harness is also loaded as a `--require` preload through `NODE_OPTIONS` in every child process. Without the harness the spec is skipped and issues no export request.

## Isolation Preflight

The first test issues no export request and must pass before the export test runs (serial mode). It requires: the stub is bound to IPv4 `127.0.0.1` and the stub origin matches; three self-test requests were rejected with 404 and no run-phase request exists yet; log paths are absolute and outside the repository; `NODE_OPTIONS` names the harness; every fresh Next server context that has loaded its env reports, from inside the server, `NEXTAUTH_URL` equal to the stub origin, `AUTH_URL` equal to the server origin, engine flag `false` and the synthetic token (compared by hash, never logged); the fetch wrapper is reached; zero evaluate fetches and zero Next governance route hits; and browser login plus `/api/auth/session` succeed under the forced origin.

## What The Export Test Does

1. Logs in, opens the Artifacts page and fills Title, Source notes and Receipt reference with synthetic text; the receipt reference selects the stub's fabricated reply (`b2e-invalid-case` or `b2e-unavailable-case`).
2. Clicks Build HTML and captures the real route response passively with `waitForResponse`; the endpoint is never routed, fulfilled or mocked.
3. Requires HTTP 200, `INVALID_RESPONSE` or `UNAVAILABLE` respectively, no receipt, `DRAFT_UNACCEPTED`, and an attempt ID `artifact-proof-<reference>-<timestamp>`.
4. Requires exactly one expected POST at the stub for the case, with the same request ID as the attempt ID, the expected artifact ID and excerpt length, and the synthetic service token present.
5. Requires the panel to show the draft state, the matching absent-receipt note and the attempt ID, no receipt badge or approved/evaluated/denied note, and the preview heading equal to the built title.
6. After both cases requires distinct attempt IDs, exactly two run-phase stub requests and none unexpected, every evaluate fetch destination equal to the stub origin, and zero Next governance route hits.

## What A Pass Shows

For this synthetic input, the actual export route sent its configured receipt POST to a loopback stub that cannot forward, received fabricated failure replies, and returned the matching status and attempt ID; the panel presented them as draft with no receipt. No request reached the actual Next evaluate route, the Governance Engine or a provider in any server context that logged. The real `.env.local` service token was overridden and never sent to the stub.

## Not Proven

- That every server execution context loaded the preload; 13 server contexts were logged, but the route handler's own context is not individually identified. The stub ledger (exact request IDs) and the `evaluate_fetch` destinations are the direct evidence.
- Non-forwarding is by design and source inspection of the stub (no outbound client, constant replies), not by a network-level trace.
- Receipt validity, the `PRESENT` branch, `TIMED_OUT`, governance or engine behavior, the real Next evaluate route, provider behavior, production network transport, other browsers, durable storage, artifact acceptance, Q001/Q004 Profile A, Profile B/C, pilot/live, P11, public sync and deployment.

## Claim Boundary

Synthetic configured-hop transport and panel presentation evidence for one focused run only. A fabricated stub reply is not a governance receipt. It does not ratify a store, writer, route or acceptance, and it does not edit or approve production code.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
