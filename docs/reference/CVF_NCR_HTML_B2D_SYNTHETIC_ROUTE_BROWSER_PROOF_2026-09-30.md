# CVF NCR HTML B2d Synthetic Route Browser Proof

Memory class: governed-reference

docType: reference

Status: WORKER_DRAFT_PENDING_LOCAL_REVIEW

Batch ID: CVF-NCR-HTML-B2D-SYNTHETIC-ROUTE-BROWSER

## Purpose

Define what the B2d focused test proves about the real export route feeding the existing Artifacts panel and its saved file, and what it does not. Files: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-route-byte-download.spec.ts` and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/support/b2d-no-hop-preload.cjs`. Observed values are in `docs/reviews/evidence/cvf-ncr-html-b2d-route-browser-worker-proof-2026-09-30.json`. B2c remains the intercepted-response proof; B2d removes the interception.

## Scope / Applies To

Applies to one fresh local Next test server started by the mock Playwright config with the no-hop preload and an empty `NEXTAUTH_URL`, one headless Chromium page, and two synthetic form inputs. It applies to no other route, browser, environment or input.

## Scope / Target / Owner Boundary

Target: bytes of the file saved by Download HTML after the real `/api/artifacts/export` route built HTML from synthetic input. The route, panel, `proof.ts` and B2b helper are read-only; the worker owns only the five B2d create paths; Local owns review, independent probe, corpus registry coverage, commit and continuity; the operator owns real-data, store and effect decisions.

## How The Run Is Invoked

The parent environment sets `NEXTAUTH_URL` to the empty string, `CVF_B2D_NO_HOP_LOG` to an absolute path outside the repository, `CVF_PLAYWRIGHT_PORT=3000`, `PLAYWRIGHT_BASE_URL` and `NODE_OPTIONS` with a quoted forward-slash `--require` path to the preload. Setting an empty value survives a Git Bash launch; a PowerShell assignment of an empty string would delete the variable, so the spec fails the preflight if the parent value is not exactly empty.

## No-Hop Preflight

The first test issues no export request and must pass before the browser test runs (serial mode). It requires: the parent `NEXTAUTH_URL` is `''`; the log path is absolute and outside the repository; `NODE_OPTIONS` names the preload; a Next server context (`start-server.js` or a `next-server` title) has logged a tick within 3 seconds; at least one server context reports `__NEXT_PROCESSED_ENV` true, meaning Next has loaded `.env.local`, and every such context reports `NEXTAUTH_URL` still empty; the wrapper is fetch itself or is reached through Next's patched fetch (`fetchIsWrapper` or a nonzero pass-through count); and zero attempt events. The preload throws at startup if the log path is not absolute, and it throws synchronously on any fetch whose URL contains `/api/governance/evaluate`, logging only the method and count, never headers, tokens, bodies or origin.

## What The Browser Test Does

1. Logs in through the existing helper, opens the Artifacts page and fills Title and Source notes with synthetic text. The endpoint is never routed, fulfilled or mocked; the response is captured with `waitForResponse` and read from its real body.
2. Requires HTTP 200, `success`, `governanceReceiptStatus: NOT_CONFIGURED`, no receipt, no attempt id and `DRAFT_UNACCEPTED`.
3. Reads the Preview iframe `<h1>` for the displayed title, edits the form without rebuilding, and confirms the iframe still shows the built title and no second request was sent.
4. Clicks Download HTML, awaits the real download event, saves to a disposable directory outside the repository, and compares saved bytes by length, SHA-256 and buffer equality with an independent `Buffer.from(data.html, 'utf8')` oracle taken from the decoded route result, and with the B2b identity.
5. Confirms the saved digest is neither the JSON wire digest nor the digest of the source notes, that no leading BOM exists, that a mid-text BOM and 3- and 4-byte UTF-8 sequences survive as bytes, and that the filename equals the route's `filename`.
6. Builds a second input whose title differs by same-length ASCII text. The saved files have equal length and different digests, and the two decoded HTML strings are equal once the generation time and title are masked, so the difference is the version.
7. Removes the download directory and re-checks the log: zero evaluate attempts and `NEXTAUTH_URL` empty everywhere.

## What A Pass Shows

For this synthetic input, the un-intercepted route response reached the browser with the receipt hop not configured, the panel displayed it, and the file saved by the panel is byte-identical to the route's decoded `data.html`. Same-length version substitution is discriminated. No evaluate fetch was attempted from any server context that logged.

## Not Proven

- That every server execution context loaded the preload. The preload is inherited by Next worker threads and child processes through `NODE_OPTIONS`; the log showed 10 server contexts in 8 processes, but the route handler's own context is not individually identified. The `NOT_CONFIGURED` status, which the route helper returns before any fetch when `NEXTAUTH_URL` is empty, is the independent second control.
- The preload's negative control was a plain Node one-shot: an evaluate URL was blocked synchronously and logged once without the body; a missing log path failed closed. It was not exercised inside the server because doing so would require a route that fetches.
- Production network transport, the receipt hop when configured, governance behavior, provider behavior, CRLF from form input (browser textareas normalize it), print, clipboard, other browsers, durable storage, acceptance, Q001/Q004 Profile A, Profile B/C, pilot/live, P11, public sync and deployment.
- Any connection between the panel and B2b. B2b remains an unconnected Node-side helper.

## Claim Boundary

Synthetic no-hop route-to-browser saved-file byte evidence for one focused run only. It does not ratify a store, writer, route or acceptance, and it does not edit or approve production code.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
