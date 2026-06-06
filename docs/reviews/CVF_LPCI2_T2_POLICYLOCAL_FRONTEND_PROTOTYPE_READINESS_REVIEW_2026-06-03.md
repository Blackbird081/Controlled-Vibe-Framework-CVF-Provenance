# CVF LPCI2-T2 PolicyLocal Frontend Prototype Readiness Review

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-06-03

executionBaseHead: `e4bc4b23`

## Purpose

Evaluate the PolicyLocal frontend prototype added under the local workspace and
decide how it should feed the LPCI2 productization plan.

The review protects a useful design artifact from becoming an accidental
runtime contract with schema drift.

## Target / Source

Reviewed local workspace:

`D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\PolicyLocal`

Primary reviewed files:

| Source | Role |
| --- | --- |
| `landing.html` | Public landing prototype |
| `app.html` | Static prototype shell |
| `app.jsx` | Static React application routing |
| `components\ui.jsx` | Shared badges and UI primitives |
| `components\screens_chat.jsx` | Chat and receipt prototype |
| `components\screens2.jsx` | Search and document browsing prototype |
| `data\mock.js` | Mock corpus, queries, reports, receipts |
| `CLAUDE_BUILD_HANDOFF.md` | Original frontend build handoff |
| `CVF_POLICYLOCAL_BUILD_CONTROL_PACKET_2026-06-03.md` | CVF build-control packet copy |

## Scope / Methodology

Method:

- filesystem inventory of the PolicyLocal workspace;
- targeted symbol search for answer classes, citation fields, source hashes,
  normalized paths, provider markers, and receipts;
- source inspection of app shell, landing page, UI helpers, chat/search screens,
  and mock data;
- comparison against the LPCI2-T1 build-control packet.

No browser automation, provider call, corpus ingestion, Next.js build, or legal
answer test was run in this review.

## Findings

Verdict: `ACCEPT_AS_VISUAL_PROTOTYPE_WITH_BLOCKING_RUNTIME_GAPS`.

The frontend prototype is valuable. The landing and dashboard screenshots match
the product direction: local-first legal/policy lookup, citation-first answers,
freshness warnings, abstain behavior, receipts, reports, and Vietnamese-first
copy. It is good product clay.

It is not ready to become the runtime scaffold without a schema cleanup tranche.

| ID | Finding | Evidence | Disposition |
| --- | --- | --- | --- |
| F1 | Visual/product direction is strong | `landing.html`, `app.jsx`, `components\screens_chat.jsx`, screenshots supplied by operator | ACCEPT |
| F2 | Answer class vocabulary is non-canonical in prototype data and UI | `data\mock.js` uses `direct_cited`, `summary`, `procedural`, `abstain`; `components\ui.jsx` maps those same short values; `landing.html` shows `DIRECT_CITED` | FIX_BEFORE_SCAFFOLD |
| F3 | Mock corpus and receipt evidence are below CVF citation minimum | `data\mock.js` corpus records lack `sourcePath`, `normalizedPath`, `sourceHash`, `jurisdiction`, `authorityLevel`, and evidence pointer fields; sample receipt citations lack source hash and excerpt | FIX_BEFORE_SCAFFOLD |
| F4 | Prototype is static UMD/Babel with remote CDN dependencies | `app.html` loads React, ReactDOM, Babel, and fonts through external URLs | ACCEPT_AS_PROTOTYPE_ONLY |
| F5 | Chat/provider behavior is simulated and must not be mistaken for live proof | `components\screens_chat.jsx` uses mock receipt and provider copy; `data\mock.js` has `providerUsed` hardcoded | ACCEPT_WITH_BOUNDARY |
| F6 | Negative search/abstain concept exists but negative-evidence receipt is not complete | `components\screens2.jsx` has no-result handling; receipt fields do not yet prove selected and rejected candidates | FIX_BEFORE_CHAT |

## Risk / Corrective Action

Risk: if a future app builder copies the prototype data model directly, the
runtime may store and emit non-canonical answer classes and incomplete citation
evidence. That would bypass LPCI1/LPCI2 rules while making the UI look governed.

Corrective action before scaffold:

1. Normalize runtime/API/database answer classes to:
   `DIRECT_CITED_ANSWER`, `SUMMARY_WITH_SOURCE`, `PROCEDURAL_GUIDANCE`,
   `ESCALATE_OR_ABSTAIN`.
2. Add a compatibility UI mapper only at the display layer if short labels are
   desired.
3. Expand mock corpus and receipts to carry `sourcePath`, `normalizedPath`,
   `sourceHash`, `fileName`, `excerpt`, `documentType`, `freshnessStatus`,
   `authorityLevel`, and `effectiveDate`.
4. Make receipt examples include selected context, excluded/rejected candidates,
   provider/model boundary, and answer-boundary reason.
5. Treat `app.html` and `landing.html` as design prototypes only; production
   scaffold must use local package dependencies, no runtime CDN reliance.

## Decision / Disposition

LPCI2-T2 is closed as `CLOSED_PASS_BOUNDED`.

The prototype is accepted for:

- visual direction;
- product navigation;
- dashboard/reporting concepts;
- local-first copy direction;
- citation/freshness/receipt/abstain UI concepts.

The prototype is not accepted for:

- runtime schema;
- storage contract;
- API response contract;
- receipt contract;
- production dependency model;
- legal answer quality;
- live provider proof.

Next allowed move: open a bounded schema-cleanup/scaffold-readiness tranche or
proceed to LPCI2-T3 production-corpus pilot planning. Broad chat runtime remains
blocked until import, search, citation, and receipt gates pass.

## Evidence Trace Block

| Evidence | Result |
| --- | --- |
| `rg` for answer class values in PolicyLocal | Found short classes in `data\mock.js`, `components\ui.jsx`, `components\screens2.jsx`, `components\screens_chat.jsx`, and `CLAUDE_BUILD_HANDOFF.md` |
| `rg` for `sourceHash`, `normalizedPath`, `sourcePath`, `authorityLevel`, `jurisdiction` | Fields are present in handoff/control docs but not in prototype mock corpus records |
| Source inspection of chat receipt | Receipt UI exists; sample receipt lacks source hash, excerpt, normalized path, and answer-boundary fields |
| Source inspection of `app.html` | Static prototype loads external UMD/Babel dependencies |
| Operator screenshots | UI is polished and aligned with local-first PolicyLocal direction |

## Verification Evidence

| Check | Result |
| --- | --- |
| Startup front door resolved | PASS |
| Active handoff identified | PASS |
| PolicyLocal workspace reviewed | PASS |
| Runtime implementation performed | N/A with reason: review-only tranche |
| Provider proof performed | N/A with reason: no runtime governance behavior claimed |
| Public export performed | N/A with reason: private workspace review only |

## Claim Boundary

Claim boundary: this review is a readiness and quality assessment of an external
workspace prototype.

Final boundary: no app code in the CVF repo was implemented, no production
corpus was ingested, no provider call was made, no legal answer was certified,
and no public export is claimed.

Verification boundary: evidence is filesystem and source-inspection based,
plus operator screenshots. Browser/runtime automation was not run.

## Finding-To-Governance Learning Disposition

Defect class: `RULE_GAP`

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Disposition: `MACHINE_CHECK_CANDIDATE`

Next control action: future PolicyLocal scaffold work should add a local schema
or fixture check that fails if API/mock/runtime answer classes use
`direct_cited`, `summary`, `procedural`, or `abstain` as stored values instead
of CVF canonical answer classes.

Runtime/provider/cost learning: `N/A_WITH_REASON`

Reason: this review does not execute runtime, provider, or cost-bearing paths.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: the reviewed prototype sits in a private local workspace and cites
internal CVF/LPCI control artifacts. A sanitized public product note may be
prepared later as a separate public-sync batch.
