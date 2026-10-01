# CVF GC-018 Baseline - NCR HTML B1 Preview Passive Resource Policy

Memory class: governed-dispatch-baseline

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-HTML-B1-PREVIEW-RESOURCES

Dispatch base head: `86dae9fa218a34048ba1420e9644497e3be87bdc`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local reviewer; effect owner: operator.

## Purpose

Authorize distinct initial Preview resource policy under existing owner, with sandbox/inline content/canonical bytes/version preserved; no Print successor.

## Source / Predecessor Evidence

Owner audit `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_LOAD_OWNER_AUDIT_2026-10-01.md` at `9512b71c7` selects ADAPT_EXISTING_OWNER; default producer escapes text, synthetic hits not production incident. Accepted Print R2 at `6251ca305` remains regression baseline.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Distinct owner decision | GOVERNED_DECISION | `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_LOAD_OWNER_AUDIT_2026-10-01.md` | Decision / Disposition | ADAPT_EXISTING_OWNER | Local reviewer | ACCEPT |
| Direct Preview sink and input seams | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | Preview; handleGenerate | srcDoc; initialResult; setDisplayed | ArtifactExportPanel | ACCEPT |
| Canonical actions | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | handleCopy; handleDownload; handlePrint | handleCopy; handleDownload; handlePrint | ArtifactExportPanel | ACCEPT |
| Producer escapes text | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | escapeHtml; buildHtml | escapeHtml | export route | ACCEPT |
| Existing script/origin control | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts` | FIXTURE_HTML | FIXTURE_HTML | Preview spec | ACCEPT |
| Print coupling | SOURCE_BEHAVIOR | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts` | displayedHtml; observation validation | printedPayloadEqualsDisplayed | Print spec | ACCEPT |
| Preview registration | REGISTRY | `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b1-synthetic-sandbox-source.json` | scopePaths | artifact-export-preview-sandbox.spec.ts | GC-051 | ACCEPT |
| Print registration | REGISTRY | `docs/corpus-intelligence/registry/entries/cvf-ncr-html-b1-print-browser-repair-source.json` | scopePaths | artifact-export-print-browser.spec.ts | GC-051 | ACCEPT |
| Packet admission | GOVERNED_DECISION | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D063 | ADAPT_EXISTING_OWNER | NCR roadmap | ACCEPT |

## Decision / Baseline / Proposed Tranche

Release after material commit, exact-hash continuity and bound pre-dispatch PASS. Clean released HEAD, no stash, worker pending/no commit. Independent INITIAL Preview problem; Print stop history retained.

## Scope / Target / Owner Boundary

Exactly seven worker paths:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-preview-sandbox.spec.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tests/e2e/artifact-export-print-browser.spec.ts`
- `docs/reference/CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_POLICY_PROOF_2026-10-01.md`
- `docs/reviews/evidence/cvf-ncr-html-b1-preview-passive-resource-worker-proof-2026-10-01.json`
- `docs/reviews/CVF_CVF_NCR_HTML_B1_PREVIEW_PASSIVE_RESOURCE_WORKER_RETURN_2026-10-01.md`

Route/auth/config/package/ledger/storage/governance/continuity and historical proofs read-only. Local release/review/commit; operator effects. No foreseeable split within budgets.

## Implementation Contract

Harden only the existing Preview renderer. No mechanism is pre-approved. Establish effective resource denial before any payload parsing/loading, including early resource markup before a head, duplicate heads and payload-supplied permissive policy. Preserve canonical result.html unchanged. A Preview-only derived render document may differ; distinguish it from canonical source rather than replacing exported bytes with the wrapper.

Retain empty sandbox, opaque origin, blocked payload script and existing form/top-navigation/opener restrictions. Preserve visible benign text/headings and inline CSS from the default producer. Deny same-origin and off-origin passive network resources: images/srcset, link stylesheets, CSS @import/background/font and nested iframe/object/embed resource paths relevant to the selected policy. Declare data/blob behavior and rendering losses explicitly; prove any allowed data image with real decode/visibility assertions, otherwise state blocked/unproven. Payload meta/CSS cannot reopen network authority. This is presentation isolation, not universal sanitization or durable acceptance.

Positive control: a disposable context with the existing empty sandbox and no resource-denial policy must generate passive hits without scripts. Include same-origin controlled endpoints and an intercepted off-origin synthetic destination. Install interception before payload insertion; fulfill/abort locally, never forward fixture traffic. Positive image/CSS/font fixtures must actually load enough to trigger downstream dependencies. Record expected/observed hit classes. Reset counters, drive actual product Preview before any Print click, and require zero controlled hits plus visible benign text and inline style. Mutation removes only the chosen resource policy while retaining script sandbox; restored passive hits must fail the same negative oracle. Observe all pages/frames. No blanket same-origin exemption; normal Next/auth harness exceptions must be exact route/purpose bounded. Unknown fixture requests fail.

Keep Copy, Download and Print bound to displayed.result.html and its submitted snapshot. Assert exact copied/downloaded/printed HTML equals known canonical response fixture even when Preview srcdoc differs; do not remove or weaken stale-version assertions. Cover unsaved edits, latest-response supersession, failure preserving previous result and initialResult unknown provenance in focused units, with actual browser displayed-version/Print binding. Retain all existing Print R2 native invocation, isolation, short/120-row completeness and mutation assertions. No Print sizing/CSP/lifecycle redesign or new Print successor.

If a coherent design or oracle requires forbidden paths, return BLOCKED_WITH_REASON with narrowest design conflict; no automatic scope extension.

## Acceptance Criteria

- [ ] Bound clean pre-implementation PASS before edits; exact seven paths; no worker commit.
- [ ] Executable empty-sandbox resource-positive control records same/off-origin image/style/CSS import/font/nested-resource hits; counters reset before actual Preview.
- [ ] Actual Preview before Print has zero controlled/unexplained hits, effective deny-before-payload under early-markup adversary, empty sandbox/opaque origin/blocked script and visible benign inline content/style.
- [ ] Policy-only removal mutation retains sandbox and makes negative oracle fail with passive hits.
- [ ] Canonical Copy/Download/Print bytes/version remain correct; derived Preview is distinguished; unsaved edits/superseded responses/prior-result failure/initialResult provenance covered.
- [ ] Existing Preview/Print and unit/type/lint checks PASS with all accepted R2 regressions retained; new proof/return disclose policy/resource choices, rendering limits and untested contexts.
- [ ] Full worker-return gate PASS with acceptance-evidence-json join and exact changed set including new return; no historical proof overwrite or effects.

Fail closed on inert control, post-parse policy, actual Preview request, ineffective mutation, missing benign render, stale/corrupted canonical output, weakened Print proof, unknown request or unauthorized path.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | Preview component/specs | synthetic UI only | owner audit, pending proof | existing Web panel | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | none | no ingress/mutation grant | internal-only packet | deferred | DEFERRED_WITH_REASON |

## Evidence / Verification

Exact seven-path diff, clean executionBaseHead, actual Preview resource positive/negative/mutation before Print, canonical/sandbox/version, retained Print, secret-safe proof/reference/return and full return gate. One admitted Local probe, no broad duplicate suites.

## Operator Checkpoints

Q001/Q004 OPEN; durable B2/P11, actor/data/store/effects/cost/public/deploy parked.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B1-PREVIEW-RESOURCES --title "NCR HTML B1 Preview Passive Resource Policy" --date 2026-10-01 --base 86dae9fa218a34048ba1420e9644497e3be87bdc --commit-mode WORKER_MUST_NOT_COMMIT --scec-problem-key cvf-ncr-html-b1-preview-passive-resource-policy --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | Preview resource outcomes, seven-path manifest and canonical identity |
| checkerReadAheadConfirmation | dispatch, release, acceptance-ledger, closeability, envelope, structural and high-risk checker sources |
| docOnlyNewFields | N/A with reason: no new governed field schema |
| claimBoundary | Scaffold is authoring aid only |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_high_risk_local_transaction_proof.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_semantic_convergence_control.py` |
| literalTokensReviewed | first-section envelope; source ACCEPT rows; acceptance-ledger-json; closeability graph; high-risk non-applicability; worker-return gate |
| gateRunPurpose | Confirm source-backed packet shape and authority before release |
| claimBoundary | Static checks cannot prove Preview resource enforcement |

## Claim Boundary

Synthetic Preview denial and canonical identity only after release/review. No production incident, universal safety/all resource-browser support, paper/dialog/accessibility, provider governance, durable acceptance, Q001/Q004 exit, public sync or deployment. Print R2 limits retained.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

