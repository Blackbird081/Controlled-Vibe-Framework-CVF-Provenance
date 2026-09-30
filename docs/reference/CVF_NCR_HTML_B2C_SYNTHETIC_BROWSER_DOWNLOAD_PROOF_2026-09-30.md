# CVF NCR HTML B2c Synthetic Browser Download Proof

Memory class: governed-reference

docType: reference

Status: WORKER_DRAFT_PENDING_LOCAL_REVIEW

Batch ID: CVF-NCR-HTML-B2C-SYNTHETIC-BROWSER-DOWNLOAD

## Purpose

Define what the B2c focused browser test proves about the existing Artifacts panel download, and what it does not. The test is `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-byte-download.spec.ts`. Observed values are in `docs/reviews/evidence/cvf-ncr-html-b2c-browser-download-worker-proof-2026-09-30.json`.

## Scope / Applies To

Applies to the one focused spec named above, run against the existing Artifacts panel through the mock Playwright config, for two synthetic HTML fixtures. It applies to no other route, page, browser or fixture.

## Scope / Target / Owner Boundary

Target: the saved file produced by the panel's Download HTML action. Owners: the panel and B2b helper are read-only sources; the worker owns only the four B2c create paths; Local owns review, commit, corpus registry coverage and continuity; the operator owns real-data, store and effect decisions.

## What The Test Does

1. Starts the mock Web server through `playwright.config.mock.ts` and drives one real headless Chromium page through the real Artifacts panel.
2. Intercepts `POST **/api/artifacts/export` with `page.route` and fulfills a synthetic JSON envelope keyed by the requested title. The real export handler, any provider and any real data are never reached; the test records which titles reached the intercept.
3. Builds fixture A and reads the `<h1>` inside the Preview iframe to confirm the displayed version. It then edits the Title field without rebuilding, confirms the version notice is no longer `current`, and confirms the iframe `<h1>` still shows A and not the edited form text.
4. Clicks Download HTML, awaits Playwright's real `download` event and saves the file to a disposable directory outside the repository. It reads the saved file as bytes and compares length and SHA-256 with an independent oracle (Node `Buffer` plus `node:crypto`) and with the B2b Node-side identity (`createHtmlByteHandoff`, `verifyHtmlByteHandoff`), imported only inside the test process.
5. Builds fixture B, whose title differs from A by same-length ASCII substitution, confirms the iframe `<h1>` now shows B, downloads, and repeats the comparison. Lengths must be equal and digests must differ.
6. Asserts BOM (`EF BB BF`), CRLF (`0D 0A`), a lone LF, and 3- and 4-byte UTF-8 sequences as byte values, and asserts the suggested filename.
7. Removes the disposable directory and asserts it is gone.

## What A Pass Shows

For these two synthetic fixtures, in the recorded browser profile, the file the panel saves is byte-identical to the HTML string of the displayed result, which the Preview iframe was directly observed to render. It is not the JSON envelope, not a re-encoded or newline-normalized copy, and not a result of a later form edit. Same-length version substitution is discriminated by digest. Immediate object-URL revocation in the panel did not prevent the observed download for these fixtures.

## Not Proven

- Production network transport, the real export route, `sourceHash`, provider or governance behavior. Mock mode cannot show AI governance behavior.
- Print, clipboard, other browsers, headed mode, other operating systems, large files, or interrupted downloads.
- Any connection between the panel and B2b. B2b remains an unconnected Node-side helper.
- Durable storage, accepting-actor authority, artifact acceptance, retention or recovery. Every artifact stays `DRAFT_UNACCEPTED`.
- Q001/Q004 Profile A, Profile B/C, pilot/live, P11, public sync and deployment remain open or parked.

## Run Note

The test needs the Web server on the port named by `AUTH_URL` in the local environment file (3000). The mock config defaults to 3001, so the run sets `CVF_PLAYWRIGHT_PORT=3000`; no config was edited.

## Claim Boundary

Synthetic real-browser saved-file byte evidence for one focused test only. It does not ratify a store, writer, route or acceptance, and it does not edit or approve `ArtifactExportPanel.tsx`.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
