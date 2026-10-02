# CVF NCR HTML B1 Preview Navigation Containment Proof

Memory class: bounded-proof-reference

docType: reference

Status: WORKER_RETURNED_PENDING_REVIEW

## Purpose

Record the integrated design, and later the bounded synthetic browser proof, for containing document-replacing navigation in the existing Artifacts Preview presentation. The Preview already has an empty sandbox, an opaque origin, blocked scripts and an initial passive-resource policy. It does not stop a user-activated self-navigation, so a link inside the derived Preview document can replace that document (and its policy) with a destination and load that destination's own resources. Worker evidence for Local review, not acceptance.

## Scope / Applies To

Owner: the Preview iframe and `buildPreviewDocument` in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`. The proof applies to that component, its jsdom units in `ArtifactExportPanel.test.tsx`, the browser matrix in `tests/e2e/artifact-export-preview-sandbox.spec.ts` and the retained Print regression in `tests/e2e/artifact-export-print-browser.spec.ts`. No route, auth, config, package, lock, ledger, storage or governance file is changed.

## Pre-Edit Integrated Design

This section was written and its structured snapshot hashed before any product source edit. The hash, the four product-source hashes at seal time and the seal time are in the worker proof JSON under `preEditDesign`.

### Observed Baseline (non-product experiments, one headless Chromium profile)

An experiment page outside the repository served an app-like parent that sets a sandbox-empty iframe `srcdoc` from the current product construction (policy meta first, payload after) and intercepted every request locally. Real mouse and keyboard activation of each construct gave:

- Document-replacing destination plus secondary resource (the destination page's own image): absolute same-origin and off-origin anchors, relative anchors, Enter on an anchor, `target=_self`, download-attribute anchors, `area` links by mouse and by keyboard, SVG `a` with `href` and with `xlink:href`, base plus relative anchor, uppercase and whitespace-padded `href`, duplicate `href` attributes, declarative-shadow-root anchors, `noscript` anchors, a redirect chain first hop, and SVG `set` or `animate` that gives an `a` element an `href` without any script.
- Extra page opened plus destination hits: middle click, Ctrl click and Shift click on an anchor.
- Document replaced with no network request: `data:` anchors, `about:blank` anchors, and a same-document-looking fragment anchor (the srcdoc base URL is the app page, so the fragment link navigates the frame to the app document: an app-document request and a nested app).
- No effect in the baseline (sandbox or policy regression only): `target` top, parent, blank and named, form submit by click, Ctrl click and implicit Enter, `formaction`, `input type=image`, `javascript:` anchors, `mailto:` anchors, blob anchors, meta refresh (absolute, relative, self), nested `iframe srcdoc` links and `object` data documents. Meta refresh does navigate in an unsandboxed or `allow-scripts` frame, so its inertness here is the empty sandbox.

### Chosen Mechanism

Containment is applied to the derived Preview document before it reaches the iframe, so no destination request can exist.

1. `containPreviewNavigation(html)` parses the canonical HTML with `DOMParser` in the parent (inert: no scripts, no resource loads). It walks every element, including the contents of every `template` element at any depth (a declarative shadow root is attached by the iframe parser but not by `DOMParser`, so template contents must be neutralized explicitly).
2. It removes every attribute whose local name is `href` (any namespace, so `xlink:href`) from `a` and `area` elements in any namespace and from any MathML element. It removes SVG `animate` and `set` elements, because they can create an `href` on an `a` element without script. It removes meta refresh elements and `base` elements. Everything else stays: element, text, inline style, `class`, `id`, `target`, `download`, `ping` (without `href` none can activate), and `use`/internal references.
3. It serializes the document (`<!doctype html>` only when the parsed document is in standards or limited-quirks mode, otherwise no doctype so quirks mode is kept) and verifies the result by parsing it again. The result is accepted only when a verification parse finds nothing left to remove; up to four rounds are allowed, after which it returns null.
4. When it returns null, or when `DOMParser` is unavailable (server render), the panel shows an inert localized "preview unavailable" document instead of any payload text. This fails closed and never shows an un-neutralized payload.
5. `buildPreviewDocument` is unchanged and still places the resource policy meta first (after a plain leading doctype, otherwise prepended) on the neutralized string. The empty sandbox, opaque origin and blocked scripts are unchanged. `result.html` is never altered: Copy, Download and Print consume it verbatim.

Link labels stay visible and selectable because the element remains; it is simply not a link any more. Fragment links are intentionally inactive in this read-only presentation (disclosed; they were already broken, because the srcdoc base URL sends them to the app page).

### Candidate Comparison

| Row | DOM neutralization before the iframe (chosen) | Embedder frame-src in a nested wrapper frame | CSP navigate-to | iframe csp attribute | Parent-side observer or late reset | Inert or pointer-events on content | Pattern rewrite of the HTML string |
|---|---|---|---|---|---|---|---|
| Triggers and timing | No link, area, SVG href or refresh exists when the frame loads; no request is possible | Blocks self-navigation before the request, but not new-page dispositions (middle, Ctrl, Shift opened a page and hit the network in the experiment) | Not a supported policy directive in the shipped browser (unsupported policy string) | Enforced on the destination response after the request is made | Request already made; a restored heading does not prove denial | Keyboard, Enter and modified clicks bypass pointer-events; inert removes selection | Same timing as chosen but parse-differential prone |
| Parsing and normalization | `DOMParser` plus serialize plus verifying re-parse; template contents walked; scripting-disabled parse matches the no-script frame | Not applicable | Not applicable | Not applicable | Not applicable | Not applicable | Cannot see shadow-root, namespace, case, whitespace or duplicate-attribute forms reliably |
| Inherited resource CSP ordering | Policy meta stays first through the unchanged `buildPreviewDocument` | A wrapper policy would be inherited by the inner document and must be re-derived | Not applicable | Not applicable | Not applicable | Not applicable | Same as chosen |
| Sandbox and opaque origin | Unchanged (empty sandbox, origin null, no scripts) | Adds a second nested frame and sandbox | Unchanged | Unchanged | Unchanged | Unchanged | Unchanged |
| Canonical bytes and provenance | `result.html` untouched; Preview alone is derived | Same | Same | Same | Same | Same | Same |
| Readable, selectable, scrollable inline presentation | Preserved (labels, inline style, selection, scroll) | Blocked navigation replaces the frame with an error page, so content is lost | Not applicable | Not applicable | Content restored late, flicker | Selection removed on inert content | Preserved when it works |
| Browser test discrimination | Control keeps every other layer and drops only this one, so hits return | Would work for self-navigation only | Cannot be observed | Request still observable but too late | Cannot pass the zero-attempt oracle | Cannot pass usability | Mutation hard to express |
| Exact paths | Seven owned paths suffice | More surface in the same file | Not feasible | Not feasible | Not feasible | Not feasible | Fewer lines, weaker |

Rejected: nested wrapper frame-src (loses content on any blocked navigation and misses new-page dispositions; kept only as a documented defense-in-depth candidate that was not adopted), navigate-to, the csp iframe attribute, late reset, parent-only observers, inert or pointer-events, string rewriting, any added sandbox token, and hiding or removing text. No route, config, dependency or new file outside the seven paths is needed.

### Declared Navigation Matrix

Layer-attributable classes (the control, which keeps the empty sandbox and the resource policy but not this layer, must show an effect; the actual product must show none; the navigation-only mutation must bring the effect back). Effects are: attempted destination request, secondary resource request, extra page, or a document replaced in the same frame.

| Id | Construct and real trigger | Control effect expected |
|---|---|---|
| L01 | absolute same-origin anchor, mouse click | destination and secondary |
| L02 | absolute off-origin anchor, mouse click | destination and secondary |
| L03 | relative anchor, mouse click (resolves against the app URL) | destination and secondary |
| L04 | anchor, keyboard Enter | destination and secondary |
| L05 | `target=_self` anchor, mouse click | destination and secondary |
| L06 | anchor, middle click | extra page, destination and secondary |
| L07 | anchor, Ctrl click | extra page, destination and secondary |
| L08 | anchor, Shift click | extra page, destination and secondary |
| L09 | anchor with `download`, mouse click | destination and secondary |
| L10 | image-map `area`, mouse click | destination and secondary |
| L11 | image-map `area`, keyboard Tab then Enter | destination and secondary |
| L12 | SVG `a` with `href`, mouse click | destination and secondary |
| L13 | SVG `a` with `xlink:href`, mouse click | destination and secondary |
| L14 | `base` plus relative anchor, mouse click | destination and secondary |
| L15 | anchor whose destination redirects, mouse click | attempted first hop |
| L16 | `data:` anchor, mouse click | document replaced, no request |
| L17 | `about:blank` anchor, mouse click | document replaced, no request |
| L18 | fragment anchor, mouse click | document replaced, app-document request |
| L19 | SVG `set` giving an `a` an `href`, mouse click | destination and secondary |
| L20 | SVG `animate` of `xlink:href` on an `a`, mouse click | destination and secondary |
| L21 | declarative-shadow-root anchor, mouse click | destination and secondary |
| L22 | `noscript` anchor, mouse click | destination and secondary |
| L23 | uppercase tag and attribute with padded `href`, mouse click | destination and secondary |
| L24 | duplicate `href` attributes (first wins), mouse click | destination and secondary |

Sandbox or policy regression classes (the control shows no effect in this browser; they are observed in the control and in the actual product and are not credited to the new layer): `target` top, parent, blank and named; form submit by click, by Ctrl click and by implicit Enter; `formaction`; `input type=image`; `javascript:` anchor; `mailto:` anchor; blob anchor; meta refresh absolute, relative and self; nested `iframe srcdoc` link; `object` data document. They are executed as one grouped control and one grouped product observation because no effect means the document survives.

Outside the claim: browsers other than the one headless profile, a user reload of the parent, assistive-technology link navigation, MathML `href` (no navigation support in the tested engine; unit proof only), compatibility-mode differences for limited-quirks doctypes, U+0000 handling, scripts (blocked by the unchanged sandbox) and resource hints on `link` elements (the resource lane).

### Proof Route

Interception is installed at browser-context level before login, navigation, Build and payload insertion; destination, secondary, redirect and extra-page requests are fulfilled locally and never forwarded; unknown sub-frame or new-page requests are unexpected and fail the oracle with no same-origin exemption. Counters are reset before Build. Each trigger uses real input (mouse, keyboard, modifiers). The document replaced check uses a window marker set in the frame before the trigger plus the policy meta and heading afterwards, so an unchanged URL or a restored heading cannot pass. The control disposes its own context. The mutation patches only the layer's attribute and element removals in the real product path (a counter proves it applied) and keeps the policy and sandbox, so the same oracle fails with restored requests, pages or transitions. Usability uses real mouse selection and wheel and keyboard scrolling, computed inline style, and semantic inspection of the intentionally inactive labels. Canonical identity uses the existing unit byte checks and a link-bearing Print fixture whose printed `srcdoc` must equal the canonical response including its links.

### Oracle Authorship Disclosure

Authored by the worker and not mapped to an external authority line: the class list and construct fixtures, the destination and secondary probe pages, the marker-based replaced-document check, the mutation patch and its applied counter, the usability thresholds, and the unit fixtures. Mapped to an authority line: the paired work order (zero attempted destination requests, zero secondary hits, zero unexpected requests, no page transition, policy and content retained, mutation retains policy and sandbox) and the accepted initial resource and Print assertions, which are retained unchanged in meaning.

### Feasibility Conclusion

Every mandatory outcome has an in-scope design and proof route inside the seven paths: navigation containment before any request, initial resource and script isolation unchanged, a readable selectable scrollable inline-styled Preview, canonical and version identity unchanged, and the Print regression retained. No blocked return is needed at this point.

## Post-Implementation Proof

All values are in `docs/reviews/evidence/cvf-ncr-html-b1-preview-navigation-worker-proof-2026-10-02.json`. One headless Chromium 145.0.7632.6 profile, mock config, synthetic intercepted export; the combined Preview and Print run gave 88 passed, exit 0.

- Layer classes: 25 (the sealed 24 plus mailto, see the deviation below). For each, the control (empty sandbox and resource policy, no layer) showed its declared effect; the actual product showed zero attempted destinations, zero secondary hits, zero unexpected requests, one page, parent unchanged, the in-frame marker, the policy meta and the benign content retained, with the derived `srcdoc` free of any navigation construct and different from the pre-layer construction; the navigation-only mutation (element walk blinded on the real product path, applied counter at least 1, `srcdoc` equal to the pre-layer construction, sandbox and policy kept) restored the declared effects and failed the same oracle.
- Sandbox regression group (S01 to S16): control zero effects, actual product zero effects. Not credited to the layer.
- Usability in the actual Preview: heading, stylesheet, style attribute and nested span computed styles correct; real triple click and double click selected text; wheel and End key scrolled a long document; the two inactive labels stayed visible, had no `href` and did not match `:any-link`; clicking them changed neither scroll position nor document and caused no request; the real Download button delivered bytes equal to the canonical fixture, which still has its fragment link.
- Resource regression: the three existing Preview resource tests (control 20 hits, two actual-Preview negatives, policy-only mutation 20 hits) pass unchanged in meaning; the two-parse containment pass caused no controlled hit.
- Print regression: all accepted R2 assertions pass (native print, opener detach, isolation, one-page short output, three-page 120-row output, isolation and clipping mutations). The fixture now carries an anchor and an SVG link: the Preview drops both targets and the printed `srcdoc` equals the canonical response including them.
- Units: 63 passed (9 added) covering removal forms, template and noscript contents, SMIL, refresh and base removal, byte-identity for clean documents, idempotence, doctype handling, parser-unavailable and non-convergent fail-closed paths and the localized unavailable document; TypeScript and ESLint clean.

## Post-Seal Deviations

Recorded after the design snapshot was sealed; the sealed snapshot is unchanged. (1) A `mailto:` click in the control produced an attempted external-protocol request, so mailto moved from the sandbox group to layer class L25 with an attempt effect (the group is now S01 to S16). (2) The usability drag selection stalled the harness, so a real double click replaced it. (3) A CSP-blocked image request is reported as a request by the harness, so the image-map fixtures use a `data:` image. (4) Popup requests have no frame at event time, so the main-frame check tolerates that. (5) The unavailable document gained minimal inline typography. None changes the mechanism or the matrix outcomes.

## Tradeoffs And Limits

Link activation and fragment jumps are absent from the read-only Preview (labels remain); canonical exports keep every link. SVG `animate` and `set` elements, meta refresh and `base` are removed from the Preview only. Containment re-serializes a document only when it had something to remove; a clean document is byte-identical before the policy meta. Limited-quirks doctypes become standards mode and document-level comments are dropped when re-serialized. Nested `iframe srcdoc` and `object` documents are covered by the unchanged policy and sandbox, not by this layer. Untested: other browsers and versions, reload of the parent, assistive technology, MathML in a browser, real packets, much larger documents, paper and dialog output.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Internal worker |
| Provider or surface | Shared private CVF workspace; local Next dev server and one headless Chromium; synthetic fixture |
| Session or invocation | NCR HTML B1 Preview navigation worker, 2026-10-02 |
| Working directory | Repository root and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` |
| Command or tool surface | bound pre-implementation gate; Playwright; Vitest; tsc; eslint; worker fast gate |
| Target paths | Exact seven-path worker acceptance ledger |
| Allowed scope source | Bound Preview navigation work order and paired GC-018 baseline |
| Before status evidence | `git status --short --untracked-files=all` empty at HEAD `d9d2366a8` before any edit; three output paths absent |
| After status evidence | Four modified tracked paths and three untracked worker paths, no staged path, no worker commit |
| Diff evidence | `git diff --name-status` lists the four modified paths; the three new paths appear as untracked in `git status --short --untracked-files=all` |
| Approval boundary | Worker evidence only; Local reviewer owns the independent probe, acceptance and commit |
| Claim boundary | Synthetic one-profile Chromium Preview observation; no acceptance or universal safety claim |
| Agent type | INTERNAL_AGENT worker |
| Invocation ID | cvf-ncr-html-b1-preview-navigation-worker-20261002 |
| Expected manifest | the seven paths in the paired work order |
| Actual changed set | the same seven paths |
| Manifest delta | MATCH |

## Epistemic Process Block

### Expected Result / Prediction

Removing activatable navigation constructs from the derived Preview before the frame exists prevents every self-navigation, new-page and replaced-document effect that the control shows, without losing readable, selectable, scrollable inline presentation or canonical output.

### Evidence Comparison

The prediction held for all 25 layer classes: control effect, zero in the product, effect restored by the layer-only mutation. The first full run exposed harness defects (popup frame access, a blocked-image request counted as unexpected, a stalled drag) and one classification error (mailto), all fixed in scope.

### Contradiction Or Gap Disposition

Gaps are listed under Tradeoffs And Limits. The Local distinct-fixture probe remains pending.

### Claim Update

Observed one-profile Chromium result, reviewer acceptance pending. Q001 and Q004 remain open.

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | synthetic Preview navigation presentation design |
| claimDisposition | CLAIM_REJECTED: design record only; behavior is proven by the browser matrix recorded after implementation |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no receipt exists at design time |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no product edit existed when this section was sealed |
| invocationBoundary | local synthetic browser and test process |
| interceptionBoundary | local fixture fulfillment, no forwarding |
| claimLanguage | navigation containment design, pending integrated proof |
| forbiddenExpansion | no route, auth, storage, provider, real data or public effects |

## Claim Boundary

Synthetic Preview navigation presentation design in one headless profile only. Not a production incident, universal sanitizer, all-navigation or all-HTML claim, real packet or data claim, other-browser, paper, dialog or accessibility claim, durable acceptance, Q001 or Q004 exit, public sync or deployment. Link activation and fragment jumps are intentionally absent from the read-only Preview; canonical exports keep them.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
