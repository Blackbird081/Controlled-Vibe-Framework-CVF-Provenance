# CVF GC-018 Baseline - NCR HTML B1 Preview Navigation Containment

Memory class: governed-dispatch-baseline

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-HTML-B1-PREVIEW-NAVIGATION

Dispatch base head: `35ee0c2f1703682f21a55e0120ef9c18e7c27075`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local reviewer; effect owner: operator.

## Purpose

Authorize one distinct initial navigation assignment at the existing Preview-derived presentation owner. Integrated pre-edit design admission, request-based containment, benign usability, canonical identity and accepted initial-resource/Print regressions are one outcome. No specific mechanism approved.

## Source / Predecessor Evidence

`docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_OWNER_AUDIT_2026-10-01.md` at 1b9a74559 admits ADAPT_EXISTING_OWNER. Prior Local clicked link produced locally fulfilled destination plus image; initial policy not persistent. Default producer escapes text; no production leak demonstrated. Initial Preview accepted f00658021 and Print R2 accepted 6251ca305 remain bounded regressions.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Existing navigation owner | GOVERNED_DECISION | `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_OWNER_AUDIT_2026-10-01.md` | Owner / Overlap Disposition; Decision | ADAPT_EXISTING_OWNER | Local reviewer | ACCEPT |
| Derived Preview policy and sandbox | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | buildPreviewDocument; Preview iframe | buildPreviewDocument; PREVIEW_FRAME_POLICY; sandbox | panel | ACCEPT |
| Canonical actions | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | handleCopy; handleDownload; handlePrint | handleCopy; handleDownload; handlePrint | panel | ACCEPT |
| Observed link destination plus secondary resource | OBSERVATION | `docs/reviews/evidence/cvf-ncr-html-b1-preview-passive-resource-local-probe-2026-10-01.json` | observations.navigation | navigation; after-navigation | Local JSON | ACCEPT |
| Initial resource oracle | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts` | previewViolations; resource mutation | previewViolations | Preview spec | ACCEPT |
| Print canonical comparison | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts` | printBehaviorViolations | printedPayloadEqualsCanonical | Print spec | ACCEPT |
| Registered Preview path | REGISTRY | `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b1-synthetic-sandbox-source.json` | scopePaths | artifact-export-preview-sandbox.spec.ts | GC-051 | ACCEPT |
| Registered Print path | REGISTRY | `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b1-print-browser-repair-source.json` | scopePaths | artifact-export-print-browser.spec.ts | GC-051 | ACCEPT |
| D066 authoring boundary | GOVERNED_DECISION | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D066 | ADAPT_EXISTING_OWNER | NCR roadmap | ACCEPT |

## Decision / Baseline / Proposed Tranche

Only after committed paired packet, exact-hash continuity and bound pre-dispatch PASS: clean pre-implementation gate, then integrated pre-edit design record. Implement inside seven paths only if every mandatory outcome has coherent feasible design/proof; otherwise blocked design return. No worker self-acceptance, commit or automatic successor.

## Scope / Target / Owner Boundary

Exactly seven worker paths:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts`
- `docs/reference/CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_CONTAINMENT_PROOF_2026-10-02.md`
- `docs/reviews/evidence/cvf-ncr-html-b1-preview-navigation-worker-proof-2026-10-02.json`
- `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_WORKER_RETURN_2026-10-02.md`

Route/auth/config/package/dependency/engine/ledger/storage/governance/continuity and prior accepted proof artifacts read-only. Local release/review/commit; operator effects. No foreseeable split within enforced size budget, blocked return for eighth path need.

## Integrated Design Admission

Before product code edits, create the design record in `docs/reference/CVF_NCR_HTML_B1_PREVIEW_NAVIGATION_CONTAINMENT_PROOF_2026-10-02.md`; retain a compact pre-edit snapshot and its SHA-256 in `docs/reviews/evidence/cvf-ncr-html-b1-preview-navigation-worker-proof-2026-10-02.json`. This is a same-assignment outcome admission, not a worker authority expansion or a separate approval workflow. Compare candidate mechanisms against each row: navigation triggers and timing, parsing/normalization, inherited resource CSP ordering, sandbox/opaque origin, canonical bytes/provenance, readable/selectable/scrollable inline presentation, browser test discrimination and exact paths. State chosen mechanism, alternatives rejected, limitations, matrix and feasible proof route.

All mandatory outcomes must be feasible inside the exact manifest before implementation. Reject late iframe reset, parent-only observer assumptions, an unsupported policy string, weakening sandbox/scripts, modifying canonical HTML, hiding/inerting content without required usability, and new route/config/dependency authority. If no coherent in-scope design is found, stop with blocked design evidence; do not patch one trigger and claim integrated success.

## Implementation Contract

The existing Preview-derived presentation must not activate document-replacing navigation. Copy/Download/Print continue using canonical result.html verbatim. Keep current empty sandbox, opaque origin, blocked scripts, effective initial passive-resource denial and accepted rendering losses. No mechanism is pre-approved; this is bounded presentation containment, not general sanitization.

Declare a navigation matrix before code edits: same/off-origin absolute and relative HTML anchors, self/parent/top/blank/named targets, primary click and keyboard Enter, alternate click, download-like anchors/area links, refresh, base/SVG href variants, data/blob destinations, same-document fragments and malformed/duplicate markup relevant to the selected mechanism. Every named class must have a safe declared outcome and executable observation. Classes already blocked by existing sandbox must be labeled sandbox regression, not credited to the new layer. External/document-replacing variants cannot be excluded merely because implementation is inconvenient. Any broader unsupported HTML class must be fail-closed or declared outside the claim, with reason and no all-HTML assertion.

Fragment links may be inactive in this read-only presentation; preserve their visible labels and disclose that choice. If supported, prove same-document behavior without network, document replacement, opening another page or losing policy. This ordinary technical choice does not change canonical exports. Do not require interaction with disabled controls as a fake negative oracle; use actual mouse/keyboard where activation is meaningful and inspect rendered semantics for intentionally inactive labels.

Install context-level interception before fixture insertion for all destination and secondary-resource paths, including same-origin, intercepted off-origin, redirect chains and new pages. Fulfill/abort locally; never forward fixture traffic. Positive control retains empty sandbox and existing resource CSP but removes only navigation containment: actual self-link activation must request a controlled destination and its secondary resource. Baseline already-blocked targets/refresh are recorded separately. Reset counters and exercise actual product Build/Preview with the same meaningful triggers. Require zero attempted destination requests, zero secondary hits, zero unexpected fixture requests, no parent navigation/new page and original policy-bearing document/content retained. Unchanged final URL or a restored heading after a request does not pass. Data/blob cases require document/page transition checks as well as network counters.

Mutation removes only the chosen navigation layer while retaining initial resource policy and sandbox. The same navigation negative oracle must fail for restored self-navigation/destination/secondary hits; do not drop sandbox/CSP to make it fail. A positive that never activates and a mutation that merely changes policy text are insufficient. Reset synthetic state and counters between classes; no blanket same-origin exemption or uncontrolled popup/destination.

Prove benign usability in the actual Preview: visible text/headings, inline style, user text selection and scrolling a long document while contained; labels remain readable. Keep exact canonical copied/downloaded/printed bytes and displayed-version behavior under unsaved edits, latest response, failed newer build and initialResult unknown provenance, reusing focused unit evidence where unchanged. Retain current initial resource positive/negative/mutation and Print R2 native invocation/origin/short-120-row/mutation assertions in both existing browser specs. Do not redesign Print or claim paper/dialog/other-browser behavior.

Return one integrated outcome: navigation containment AND initial resource/script isolation AND usable read-only presentation AND canonical/version identity AND Print regression. If any mandatory outcome is unproven, return BLOCKED_WITH_REASON with evidence and smallest Local amendment; no partial-success closure, implicit scope extension or automatic successor.

## Acceptance Criteria

- [ ] Clean bound pre-implementation PASS and pre-product-edit integrated design snapshot; exact seven-path scope, no worker commit.
- [ ] Declared bounded trigger matrix distinguishes new-layer denial from sandbox-only behavior; fragments/data/blob/usability choices explicit.
- [ ] Executable empty-sandbox/resource-policy-preserving positive self-navigation produces destination and secondary hits; actual-product same triggers have zero attempted navigation/secondary/unexpected hits, retain document/policy and parent/page count.
- [ ] Navigation-only removal mutation retains resource CSP/sandbox and fails the same oracle with restored destination/secondary requests.
- [ ] Actual Preview remains visible, inline styled, selectable and scrollable; fragment behavior proved if supported.
- [ ] Canonical bytes/version/provenance, initial resource controls and all accepted Print R2 assertions preserved; existing both specs/unit/type/lint PASS.
- [ ] New design/proof reference, secret-safe JSON and pending return with acceptance-evidence join, full worker gate PASS and exact scope; no historical proof overwrite or effects.

Fail closed on inert control, late reset, already-made destination request, navigation/secondary hit, unexpected popup, policy/sandbox weakening, corrupted canonical version, unusable hidden/inert text, weakened regression or unauthorized path.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | Preview component/specs | synthetic UI only | owner audit, pending proof | existing Web panel | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | none | no ingress/mutation grant | internal-only packet | deferred | DEFERRED_WITH_REASON |

## Evidence / Verification

Design snapshot/hash before product edits; safe attempted-request positive/negative/navigation-only mutation, explicit trigger matrix, actual text selection/scroll/style, canonical/version and current resource/Print regression, secret-safe JSON/proof/return and full worker gate. One Local independent navigation/usability probe, no broad duplicate suite.

## Operator Checkpoints

Q001/Q004 OPEN; durable B2/P11, actor/data/store/effects/cost/public/deployment parked. No operator technical choice required inside this synthetic lane.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B1-PREVIEW-NAVIGATION --title "NCR HTML B1 Preview Navigation Containment" --date 2026-10-02 --base 35ee0c2f1703682f21a55e0120ef9c18e7c27075 --commit-mode WORKER_MUST_NOT_COMMIT --scec-problem-key cvf-ncr-html-b1-preview-navigation-containment --stdout` |
| generatedProfile | generic-worker-dispatch no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | navigation outcome/matrix, pre-edit design admission, usability and regression obligations; seven exact paths |
| checkerReadAheadConfirmation | dispatch, release, acceptance-ledger, closeability, envelope, high-risk and semantic checker literals read |
| docOnlyNewFields | N/A with reason: existing schemas; task proof IDs only |
| claimBoundary | authoring only, no runtime proof |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_semantic_convergence_control.py` |
| literalTokensReviewed | first-section envelope; source ACCEPT rows; acceptance-ledger-json; closeability graph; high-risk non-applicability; worker-return gate |
| gateRunPurpose | Confirm source-backed packet shape and authority before release |
| claimBoundary | Static checks cannot prove Preview resource enforcement |

## Claim Boundary

Bounded synthetic Preview navigation presentation only after release/review; no production incident, universal sanitizer/all-navigation support, real packet/data, every browser, paper/dialog/accessibility, provider governance, durable acceptance, Q001/Q004 exit or public/deployment claim. Initial resource and Print acceptance remain bounded.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
