# CVF NCR HTML B1 Print Origin Isolation R1 Reviewer Decision

Memory class: governed-review

docType: review

Status: REVIEW_COMPLETE_REWORK_REQUIRED

Date: 2026-10-01

providerExecutionAuthority: FORBIDDEN

## Purpose

Decide whether the six-path R1 Print candidate can be accepted after the Local browser probe and return gate.

## Target / Source

R1 work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PRINT_ORIGIN_ISOLATION_R1_2026-10-01.md`. Worker return and its six-path implementation are preserved in stash `42d22bbcea12ee0f555e84e0649877dabd967a4b`, since they are not accepted repository artifacts. Execution base: `243ed6665064a491bc2f2c31d168850253246d44`.

## Scope / Methodology

Startup acknowledged: current mode=`cvf_ncr_p10_closed_p11_parked`; active handoff=`AGENT_HANDOFF_V63_2026-09-18.md`; next allowed move=review R1 Print; parked=Q001/Q004 and real actor/data/store/effect decisions. Role=Local reviewer; phase=worker-return review; technical decision owner=Local; effect decision owner=operator. The shared-workspace worker is INTERNAL_AGENT; external research is advisory only.

Local inspected the exact six-path candidate and its bounded proof, reran the actual Print security case once in Chromium, and ran the worker-return fast gate. The disclosed fixed-height frame raised one independent functional contradiction, so Local also ran a minimal Chromium print-renderer comparison using the production shell's empty-sandbox `iframe` and `height:100vh` style against direct-document printing. This is a targeted safety probe, not a duplicate implementation test or a paper-output claim.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Committed panel owns the Print callback and sandboxed preview; R1 candidate geometry is retained in the named stash | SOURCE_BOUNDARY | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `handlePrint` and preview | `handlePrint`, `sandbox` | Artifacts panel | ACCEPT for committed owner only |
| R1 packet requires a Local independent probe and review of rendering tradeoff | GOVERNED_CONTRACT | `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_HTML_B1_PRINT_ORIGIN_ISOLATION_R1_2026-10-01.md` | Reviewer Closure Conversion | B1 Print | R1 order | ACCEPT |
| R1 requires native print, displayed version and benign visible content | GOVERNED_CONTRACT | `docs/baselines/CVF_GC018_CVF_NCR_HTML_B1_PRINT_ORIGIN_ISOLATION_R1_2026-10-01.md` | Acceptance Criteria | B1 Print | GC-018 | ACCEPT |

## Findings / Position

The focused actual-button Chromium rerun passed 1/1. The executable unsandboxed control reached the synthetic origin state and local endpoint; the real Print payload had opaque origin, did not run its script, and did not touch those sentinels. One native `print()` call and displayed-version binding were observed. The worker's security repair is therefore supported within that one-profile synthetic claim.

The print surface loses document content. In a separate Chromium 145 headless probe, a 120-row synthetic document inside the same empty-sandbox, `100vh` frame produced a one-page PDF containing rows through 33 and no end marker. The direct-document control produced four pages, row 120 and the end marker. The probe used Playwright `page.pdf({format:'A4', printBackground:true})` and extracted text with PyMuPDF; no real data, provider call or network route was involved. It reproduces the production frame geometry, while the existing UI test does not assert printed pages. This is evidence of a functional clipping risk in that design, not proof of a physical printer result or of every browser's behavior.

Local reran `run_worker_return_fast_gate.py` against the bound R1 order: exit 0, COMPLIANT; 69 reviewer-fast hooks passed. Its quality checker accepted a worker prose line saying the gate "requires PASS evidence" because the regex matches `run_worker_return_fast_gate.py` and `PASS` on the same line. Thus the structural PASS does not independently validate the worker's originally reported exit 1, and it cannot override the pagination finding. No checker or worker-return edit is needed to record Local's actual result here.

## Decision / Disposition

`REWORK_REQUIRED_PRINT_COMPLETENESS`. Do not commit the six worker paths as a completed Print repair. The exact six-path R1 candidate is isolated in stash `42d22bbcea12ee0f555e84e0649877dabd967a4b`; original R0 stash `beeaf933bf03924532eb02bea331455e2233d743` remains intact. Keep the committed product Print behavior unchanged. A follow-up design must retain the observed origin isolation, native Print and displayed-version binding while proving that a long document's final marker appears in the browser-generated print output across pages. The next packet must distinguish a genuine independent functional root cause from the R0/R1 origin-authority cluster before any round-two dispatch; round-three automatic re-dispatch is forbidden. Q001/Q004 remain OPEN.

## Risk / Corrective Action

Review the full Print dependency graph before rework: executable origin control, actual Print negative oracle, isolation-removal mutation, normal short content, long multi-page content, and failure paths. A page-count-only test is insufficient; require the end marker and representative intermediate rows in the output. Passive loads, other browsers, popup-blocked and opener-detach-failure real-browser branches, dialog, paper, accessibility and real-data effects remain outside this bounded decision.

## Review Gate

Actual-button Chromium security case: PASS 1/1. Local worker-return fast gate: PASS, exit 0. Minimal Chromium PDF pagination control: direct 4 pages with row 120 and end marker; sandboxed `100vh` frame 1 page, max row 33 and no end marker. Semantic acceptance: FAIL on print completeness.

## Finding-To-Governance Learning Disposition

| Defect class | Learning lane | Disposition | Next control action | Batch status |
|---|---|---|---|---|
| RUNTIME_SIGNAL_GAP: fixed-height iframe print truncation | RUNTIME_BEHAVIOR_LEARNING | DESIGN_REVIEW_REQUIRED | Add multi-page output oracle without losing origin isolation | Open |
| Worker-return gate self-reference match | GOVERNANCE_CONTROL_PLANE | MACHINE_CHECK_CANDIDATE | Record actual Local run separately; do not treat prose regex as execution proof | Open, no checker change in this review |

## Epistemic Process Block

### Expected Result / Prediction

An origin-isolated print shell should preserve all benign document content across browser-generated pages, including the final row of a long document.

### Evidence Comparison

The actual-button security case passed. The isolated renderer probe output one page through row 33, while a direct-document control output four pages through row 120 and the final marker.

### Contradiction Or Gap Disposition

Security isolation and native print invocation do not establish complete print output. Hold R1 and add a content-completeness oracle to the next bounded design.

### Claim Update

R1 has bounded origin-isolation evidence but is not an accepted Print repair.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_work_order_acceptance_ledger.py` |
| literalTokensReviewed | `Status:`, `docType: review`, Source Verification ACCEPT rows, `Agent Operation Trace Block`, `Public Export Disposition`; reviewer gate PASS is structural |
| gateRunPurpose | Confirm the pre-read review evidence shape and preserve the semantic boundary separately from the worker packet gate; not first discovery of checker requirements |
| claimBoundary | No physical-output, universal browser, passive-load or artifact-acceptance claim |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local reviewer |
| Provider or surface | private CVF workspace; one local headless Chromium |
| Session or invocation | NCR HTML B1 Print R1 review, 2026-10-01 |
| Working directory | repository root and cvf-web package |
| Command or tool surface | exact source/return inspection, focused Playwright, isolated Chromium PDF probe, worker-return gate, Git |
| Target paths | this review and NCR roadmap D060 |
| Allowed scope source | delegated Local technical review under R1 work order |
| Before status evidence | HEAD `243ed6665`; exactly six pending worker paths, no staged path |
| After status evidence | six worker paths isolated in stash `42d22bbcea12ee0f555e84e0649877dabd967a4b`; only review and roadmap remain changed |
| Diff evidence | `git status --short --untracked-files=all` shows only review and roadmap; candidate stash is retained |
| Approval boundary | no acceptance, real-data, pilot/live, public or deployment effect |
| Claim boundary | Chromium print-renderer result on synthetic fixed-height shell; actual product paper output not measured |
| Agent type | reviewer |
| Invocation ID | cvf-ncr-html-b1-print-r1-review-20261001 |
| Expected manifest | `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_ORIGIN_ISOLATION_R1_REVIEW_2026-10-01.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Actual changed set | `docs/reviews/CVF_CVF_NCR_HTML_B1_PRINT_ORIGIN_ISOLATION_R1_REVIEW_2026-10-01.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` |
| Manifest delta | MATCH after candidate isolation |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

The R1 security oracle is accepted only as bounded synthetic evidence. The Print implementation is not accepted because the fixed-height shell loses long-document content in the independent Chromium print-renderer probe. No Q001/Q004 exit, artifact acceptance, public export or deployment follows.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
