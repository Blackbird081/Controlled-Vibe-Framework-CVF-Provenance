# CVF NCR HTML Secret Refusal Recovery

Memory class: governed-reference-proof

Text Encoding Exception: Vietnamese recovery copy is quoted verbatim from the panel so the proof shows what the user sees.

docType: reference

Status: COMPLETE_PENDING_REVIEW

Batch ID: CVF-NCR-HTML-SECRET-REFUSAL-RECOVERY

executionBaseHead: `0b738c3299c7c68cfcd732a35e1e5cd1538c5df1`

## Purpose

Fix finding F-01 from the R1 source audit: the panel's plain-language secret-refusal recovery never showed for the real export route, because the route's error string differs from the one the panel matched.

## Target / Source

`ArtifactExportPanel.tsx` (`recoveryMessageFor`), its test file, and the export route read only. Hashes, old-code runs and final runs are in `docs/reviews/evidence/cvf-ncr-html-secret-refusal-recovery-worker-evidence-2026-10-02.json`.

## Scope / Methodology

The plan and pre-edit hashes were sealed in the evidence file before any edit. Five new cases were added to the test file. SR-01 and SR-02 were then run alone on the unchanged panel and each failed. Only after that was the panel changed. No route, browser, build, HTTP or provider was used.

## Behavior

The secret-refusal branch of `recoveryMessageFor` now accepts exactly two strings and nothing else:

- `Potential secret-like value detected in artifact export fields.` (what the route returns now)
- `Potential secret-like value detected in source content.` (the older string, kept for existing callers)

For either, the panel shows the existing recovery text and keeps the raw error as the secondary detail line:

- EN: This text looks like it may contain a private key or token. Remove that value and try again.
- VI: Nội dung này có vẻ chứa khóa riêng tư hoặc mã token. Hãy xóa giá trị đó rồi thử lại.

The labels were not changed. PROOF-COPY.

| Case | Checks | Old code | New code |
|---|---|---|---|
| SR-01 | current route string, English UI: recovery, raw detail, no callback, no draft state | FAIL | PASS |
| SR-02 | same, Vietnamese UI | FAIL | PASS |
| SR-03 | route.ts holds exactly one secret-like error literal and it equals the mocked string | PASS | PASS |
| SR-04 | legacy string still recovers and keeps raw detail | PASS | PASS |
| SR-05 | unrelated error mentioning secret-like and private key stays raw, no detail line | PASS | PASS |

PROOF-DRAFT: SR-01 and SR-02 assert the callback is not called and no draft-state element appears, so a refusal builds no candidate. Prior-preview and version behavior is owned by the existing attempt tests, which were kept and still pass.

PROOF-SELECTION: SR-04 and SR-05 plus the existing missing-field test show the match is exact, not a classifier. The new controls were expected green on old code and were.

PROOF-SOURCE: SR-03 reads `route.ts` as text and never imports or runs it. The route hash is unchanged before and after.

## Boundaries

PROOF-CHECKONLY and PROOF-BOUNDARY. Only the presentation matcher changed. Secret detection, route admission, auth, receipt, cancel and job behavior are untouched. The test mocks a fetch response; it does not prove the real route refuses real secrets. Send, B2, Q001/Q004 and effects are not involved and not advanced.

## Findings / Position

F-01 is fixed at the panel with exact-string matching. The real route and panel now agree, and SR-03 will fail if either side's string changes again.

## Risk / Corrective Action

SR-03 extracts the literal with a regex over route source, so a reformatted route (double quotes, template string) fails the pin loudly rather than silently. That is intended. The panel still depends on exact strings; a second route refusal wording would need its own alias.

## Decision / Disposition

COMPLETE_PENDING_REVIEW. Local reviews and commits.

## Epistemic Process Block

### Expected Result / Prediction

On unchanged code the two current-route cases fail and the legacy, fallback and source-pin cases pass; after the exact alias, all pass.

### Evidence Comparison

That is what the runs showed: SR-01 and SR-02 failed with the raw route string shown, SR-03 to SR-05 passed, and the final file passed 68 of 68.

### Contradiction Or Gap Disposition

No contradiction with the sealed plan; no deviation. The proof is mocked UI mapping only.

### Claim Update

F-01 is closed at the presentation layer, pending Local review.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Internal worker |
| Provider or surface | Shared private CVF workspace; jsdom unit tests, tsc and eslint |
| Session or invocation | NCR HTML secret refusal recovery worker, 2026-10-02 |
| Working directory | Repository root and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web` |
| Command or tool surface | pre-implementation gate; focused Vitest; tsc; eslint; worker fast gate |
| Target paths | the five paths of the work order |
| Allowed scope source | Bound work order and paired GC-018 baseline |
| Before status evidence | clean worktree at HEAD `0b738c329`; three output paths absent |
| After status evidence | two modified tracked paths and three new paths, nothing staged, no commit |
| Diff evidence | `git status --short --untracked-files=all` lists exactly the five paths |
| Approval boundary | Worker evidence only; Local owns review and commit |
| Claim boundary | Mocked panel response mapping only |
| Agent type | INTERNAL_AGENT worker |
| Invocation ID | cvf-ncr-html-secret-refusal-recovery-worker-20261002 |
| Expected manifest | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`; `docs/reference/CVF_NCR_HTML_SECRET_REFUSAL_RECOVERY_2026-10-02.md`; `docs/reviews/evidence/cvf-ncr-html-secret-refusal-recovery-worker-evidence-2026-10-02.json`; `docs/reviews/CVF_CVF_NCR_HTML_SECRET_REFUSAL_RECOVERY_WORKER_RETURN_2026-10-02.md` |
| Actual changed set | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx`; `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`; `docs/reference/CVF_NCR_HTML_SECRET_REFUSAL_RECOVERY_2026-10-02.md`; `docs/reviews/evidence/cvf-ncr-html-secret-refusal-recovery-worker-evidence-2026-10-02.json`; `docs/reviews/CVF_CVF_NCR_HTML_SECRET_REFUSAL_RECOVERY_WORKER_RETURN_2026-10-02.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

Local UI error presentation only. No claim about secret detection, route, auth, receipt, provider, cancellation, server outcome, acceptance, Q001/Q004, send or B2, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
