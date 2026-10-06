# NCR P06 - Bounded artifact-export body read

Memory class: FULL_RECORD

docType: baseline

Status: LOCAL_IMPLEMENTED_VERIFIED_BOUNDED

Date: 2026-10-06

executionBaseHead: `45b1a48d4f97e221adcd3e3bd21610b54d6f5f5a`

## Purpose

Continue the wider NCR backlog after the bounded INTAKE draft disposition.
Prevent artifact-export ingress from buffering an unlimited request body when
Content-Length is absent or understates the actual stream. Preserve the current
128000-byte maximum and accepted raw-text signature semantics.

## Source Verification Block

| Source | Disposition | Finding |
|---|---|---|
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts, POST | ACCEPT | Declared length checked before request.text(); actual byte limit checked only after complete buffering and authorization |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.test.ts | ACCEPT | Existing oversize fixture covers response status, not cancellation before end-of-stream |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts | ACCEPT | Receipt helper is later in the route; use test instrumentation to ensure oversized input never reaches it |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/route-governance-proof.ts, authorizeRouteGovernanceProof | ACCEPT | Signature consumes captured raw text before JSON normalization; preserve this for allowed-size input |
| docs/reviews/CVF_CVF_NCR_Q001_HTML_INGRESS_REVIEW_2026-09-28.md | ACCEPT | Existing bounded ingress repair owner; this delta is stream resource handling, not a repeat receipt/UI repair |
| docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md, P06/W02-C | ACCEPT | Reuse existing ingress-before-effect backlog; no new capability or spec-generation tranche |

## Decision / Scope

Operator request: `next tranche`, following agreement to stop the completed
spec-input sample and continue the wider CVF backlog. Local owns selection,
implementation and bounded technical disposition. Reversible local maintenance
only; no worker delegation or separate provider test is required for byte reading.

Exactly two product paths: the export route and its existing test file above.
This baseline records scope/results; the existing NCR roadmap records selection.
Preserve the prior 15-path worktree delta.
Do not change field limits, auth policy, signature verification, receipt helper,
approval state, storage, dependencies, schemas or UI. No public/deploy/effect
admission; Q001/Q004, send/B2 and P11 checkpoints remain as previously recorded.

Read request chunks up to the existing byte limit. On overflow, cancel the
reader and return the current 413 error before further processing. For accepted
input, decode UTF-8 with the same text semantics as Request.text(), including
split multibyte sequences; pass that raw text into existing authorization.
This bounds application-retained bytes, not transport/proxy buffers, per-chunk
allocation, timeout, upload bandwidth or concurrency across requests.

## Evidence / Verification Plan

Add deterministic stream regressions: an oversized producer with an unread tail
must be cancelled; a multibyte body must be limited by bytes, not characters;
an accepted signed body with split Vietnamese UTF-8 must retain its content.
Exercise absent and understated Content-Length. Run the existing route suite,
typecheck, targeted lint and applicable static gates. Test fixtures establish
local byte-reading behavior only, not AI governance, real service operation,
release readiness or production protection. Record red/green results below.

## Verification Results

The route now reads incrementally, counts incoming bytes before decoding and
cancels on overflow. Accepted text reaches the existing authorization before
JSON parsing/normalization. Original field/body post-checks remain in place.

Red: three new overflow/cancellation cases failed against the old route;
30 cases passed, including the signed split-UTF-8 control (red.log, 18.14s).
Green: initial 33/33 passed (green.log, 14.03s). Added exact-limit and producer
cancellation-failure coverage because those boundary behaviors were untested;
intermediate suite 35/35 passed (final-tests.log, 16.38s). Typecheck identified a test
fixture literal inference error for duplex; corrected to the half literal.
Source review then identified that awaiting producer cancellation could delay
413 indefinitely. Cancellation is now issued without awaiting producer cleanup;
rejection is handled and the reader lock released. Added the unresolved-producer
case to exercise this dependency. Final 36/36 passed, 18.83s in
cancellation-final-tests.log; final-typecheck.log and final-lint.log exit 0.
Seven additional cases cover this bounded class. No other product suite needed
repetition; no changes were made to the previous spec-input implementation.
Evidence directory: .cvf/runtime/ncr-p06-body-read-20261006/.

Initial preflight rejected a missing standalone Claim Boundary heading; corrected
before product edits, preflight-corrected.log PASS, 16.99s. Original failures
remain in their logs. Focused lint passed. Provider requests for this delta: zero.
These tests exercise local deterministic streaming with synthetic auth/receipt
fixtures; they are not evidence of AI governance or real downstream operation.

## Execute And Knowledge Ingress Follow-Up - 2026-10-06

Fresh operator `next` selects the remaining named P06 ingress consumers as one
bounded Local implementation/review batch. Source ACCEPT: execute/route.ts reads
request.text before JSON/auth; knowledge/ingest/route.ts reads req.text before
auth/JSON. Both currently have no application-level body bound. Prior artifact
export evidence is reusable; no new provider call is needed for byte reading.

Exact follow-up product manifest, below
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src: lib/bounded-request-body.ts and
its test; app/api/execute/route.ts and its existing test; app/api/knowledge/ingest/
route.ts and its existing test. This local utility is not a service/runtime or
new schema/checker. Preserve artifact export's existing 128000-byte implementation
and all prior delta. This section supersedes the initial two-path scope only for
the fresh follow-up. Roadmap selection paragraph and this baseline are metadata.

Local design choice: execute ceiling 16 MiB (allow image-bearing requests),
knowledge-ingest ceiling 4 MiB. These are new application limits, not inferred
existing guarantees; larger clients get 413 and need a smaller request. No claim
that every previous unbounded payload remains compatible. Count actual stream
bytes, preserve raw UTF-8/signature text, cancel overflow without awaiting
producer cleanup; declared oversized length can reject before reading. Existing
auth, parse, validation, provider admission and knowledge-store ownership remain.
No upload deadline, proxy, concurrency, persistence or full P06 closure claim.

Verify helper exact boundary/split UTF-8/cancellation and both real route handlers
with oversized streams and signed accepted inputs. Fixtures assert local request
handling only; no mocked AI governance claim. Typecheck/lint and existing static
autorun apply. Role=Local; phase=implementation/verification; decision owner=Local;
parked checkpoints retained. No delegation, provider, commit, public or deploy.

Follow-up verification: pre-edit static autorun PASS 85/85, 8.52s (preflight.log).
ADIF resolver returned zero candidates, no truncation (adif.json). Focused helper
and both route suites PASS 75/75, 18.07s (tests.log); thirteen new cases cover
exact bytes, split UTF-8/BOM text semantics, declared and actual oversize,
unread-tail cancellation, cleanup rejection/pending producer, and signed accepted
inputs reaching existing route/provider-mock/store boundaries. Existing route
auth/validation/output controls remain collected. No real provider invocation;
all execute tests use the existing mocked adapter and cleared provider keys.
TypeScript exit 0; targeted ESLint exit 0 with no warnings/errors (typecheck.log,
lint.log), git diff --check PASS. Evidence is in ignored
.cvf/runtime/ncr-p06-ingress-20261006/. Final static confirmation is final-static.log.
No claim of full Web/runtime,
governance behavior or closing P06 across unexamined routes.

Follow-up expected/actual manifest: six product paths listed above, this baseline
and two replaced roadmap lines; prior worktree delta retained. No other paths
are admitted by this batch. Historical initial two-path trace below remains
evidence of the earlier artifact-only repair, superseded for current scope.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_markdown_structural_completeness.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_public_export_disposition.py |
| literalTokensReviewed | baseline Source/Decision/Evidence headings; four read-ahead fields; trace labels; Resolver query; Returned defects; Public Export Disposition |
| gateRunPurpose | Confirm the authored bounded scope and resulting evidence; not first discovery of literals |
| claimBoundary | Packet/static confirmation only; no live governance proof |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Worker execution`, role=`worker`, lifecyclePhase=`pre-implementation`

Returned defects: NONE_RETURNED. Resolver returned zero candidates, no truncation.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local implementer/reviewer |
| Provider or surface | Local workspace |
| Session or invocation | NCR-P06 bounded body read, 2026-10-06 |
| Working directory | D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF |
| Command or tool surface | Source reads, apply_patch, focused Vitest, TypeScript, ESLint, static autorun |
| Target paths | Two product paths listed in Source Verification Block and this baseline |
| Allowed scope source | Operator next-tranche request and existing NCR P06 backlog |
| Before status evidence | Fifteen existing modified/untracked material paths; route/test initially clean |
| After status evidence | Route/test delta implemented; 36/36 focused cases, typecheck and lint pass; applicable static confirmation retained in final-static.log |
| Diff evidence | git diff for the two product paths; baseline remains untracked |
| Approval boundary | Local reversible source maintenance; other effects not admitted |
| Claim boundary | Application body-read resource bound, not end-to-end protection |
| Agent type | Local implementer/reviewer |
| Invocation ID | NCR-P06-BODY-20261006 |
| Expected manifest | Two product paths, this baseline, existing NCR roadmap selection paragraph |
| Actual changed set | These four tranche paths; prior material delta retained |
| Manifest delta | Existing roadmap paragraph replaced without increasing file length; no other tranche paths |

## Claim Boundary

This delta addresses application-level input buffering for one existing route.
It does not establish AI governance behavior, deployment resource protection,
profile readiness or authority for subsequent effects.
Local byte-reader repair is complete within this manifest; this is not a release
or committed tranche closure. Material changes remain uncommitted. Next roadmap
selection returns to the wider backlog; no automatic effect/worker successor.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY - local source maintenance and bounded test evidence.
