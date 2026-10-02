# CVF NCR R1 HTML UX Support Audit

Memory class: governed-reference-audit

docType: reference

Status: COMPLETE_PENDING_REVIEW

Batch ID: CVF-NCR-R1-HTML-UX-SUPPORT-AUDIT

executionBaseHead: `cddd1040dcca144833788d430a11ddcf5a9480de`

Claim level: PASS_STATIC_ONLY. Source reading only; nothing was executed.

Text Encoding Exception: Vietnamese user-facing copy is quoted verbatim from the audited panel so the audit shows what the user sees.

## Purpose

Map the existing HTML review page against the NCR-R1 meanings of goal and input, pending, error, recovery and cancel. Accepted B1 and B2F evidence is consumed at its original level. The audit adds no feature, no cancel contract and no duplicate test.

## Target / Source

Owners: the Artifacts page, `ArtifactExportPanel.tsx` and its test file, plus the export route and receipt helper read only to explain what the user sees. Hashes, locators and the cross-check script are in `docs/reviews/evidence/cvf-ncr-r1-html-ux-support-audit-2026-10-02.json`. Prior proof: `docs/reviews/CVF_CVF_NCR_HTML_B1_VERSION_BINDING_COMPLETION_2026-09-30.md` and `docs/reviews/CVF_CVF_NCR_HTML_B2F_SYNTHETIC_TIMEOUT_COMPLETION_2026-10-01.md`.

## Scope / Methodology

Named files only. No complete repository scan and no absence claim outside the named files. Excluded: node_modules, builds, environment files, runtime stores, credentials. The existing test names below were read, not run.

Classes: IMPLEMENTED_SOURCE_ONLY, ACCEPTED_BOUNDED_EVIDENCE, UNSUPPORTED_BY_CURRENT_OWNER, UNKNOWN, OUT_OF_SCOPE_STOPPED_ROOT.

## Owner Graph

PROOF-OWNER. The page composes one owner: `<ArtifactExportPanel initialRequest={starterRequest} />` (page L121, starter at L42). The panel posts to `/api/artifacts/export`, which builds the HTML, then makes one receipt call through `fetchGovernanceReceipt` and returns the result with a receipt status.

| Row | Meaning | Class | User-visible copy (EN / VI) | Existing test names |
|---|---|---|---|---|
| S01 | Goal and input: seven editable fields under "Review Packet Export" | IMPLEMENTED_SOURCE_ONLY | "Build a self-contained HTML review packet..." / "Tạo gói HTML tự chứa..." | renders the English HTML export surface; renders Vietnamese labels |
| S02 | Build button is disabled only when source notes or receipt reference are blank; other blanks go to the route and return the missing-field recovery | IMPLEMENTED_SOURCE_ONLY | "Some required fields are empty..." / "Một số trường bắt buộc còn trống..." | maps the missing-field rejection to plain-language recovery |
| S03 | Data-egress disclosure before the Build button | IMPLEMENTED_SOURCE_ONLY | "Building this packet may send a short excerpt..." / "Việc tạo gói này có thể gửi..." | shows the pre-generate disclosure (EN and VI) |

## Request And Outcome Authority

PROOF-AUTHORITY. Every successful build is labelled draft and unaccepted (`draftNote`). A receipt never becomes artifact approval: ALLOW, APPROVED, DENY and absent receipts each have separate copy, and the approved badge reads "Final artifact acceptance is still required".

| Row | Meaning | Class | Copy | Tests |
|---|---|---|---|---|
| S04 | Pending: button shows "Generating" / "Đang tạo" with a spinner and `aria-busy`; it is not disabled | ACCEPTED_BOUNDED_EVIDENCE (B1) | "Generating" / "Đang tạo" | does not let a superseded attempt dismiss the busy state of the newer attempt |
| S09 | Success shows preview, checks, receipt reference and the draft note | ACCEPTED_BOUNDED_EVIDENCE (B1) | "DRAFT / UNACCEPTED..." / "BẢN NHÁP / CHƯA ĐƯỢC CHẤP NHẬN..." | posts the artifact source and renders the returned candidate; shows DENY as draft...; shows an ALLOW evaluation as evidence... |
| S10 | Receipt outcomes: timed out, unavailable, invalid, not configured, absent | ACCEPTED_BOUNDED_EVIDENCE (B2F, timeout only) | "The review check timed out... may still have processed the request" / "Kiểm tra rà soát đã hết thời gian chờ..." | shows the timeout and attempt ID without offering an approval badge |
| S13 | Retry | UNSUPPORTED_BY_CURRENT_OWNER | none beyond "check the attempt ID before trying again" | none |

S10 note: unavailable, invalid-response and not-configured copy exists in source. The panel suite has no case by name for them; the B2e browser spec covers invalid-response and unavailable per the receipt-branch audit. This is not a gap and is not reopened.

S13: there is no automatic retry. Pressing Build again starts a new numbered build. The timed-out and unavailable notes tell the user to check the attempt ID first, but nothing enforces that.

## Input To Displayed Candidate

PROOF-IDENTITY. Each build snapshots all seven fields. The displayed result, receipt, checks, Copy, Download and Print stay bound to that snapshot; editing the form only changes the version notice.

| Row | Meaning | Class | Copy | Tests |
|---|---|---|---|---|
| S05 | Version state current, stale or unknown | ACCEPTED_BOUNDED_EVIDENCE (B1) | "Earlier version (build #n)..." / "Phiên bản cũ (lần tạo #n)..." | snapshots all seven request fields at submit; returns to current when the form is edited back |
| S06 | A newer build replaces an older pending one | ACCEPTED_BOUNDED_EVIDENCE (B1) | "Build #n was replaced by a newer build. Its response, if one arrives, will not be shown or used." | records a replaced pending attempt separately...; shows superseded-attempt copy in Vietnamese without retry advice |
| S07 | Stale response is ignored | ACCEPTED_BOUNDED_EVIDENCE (B1) | superseded success copy names the returned ID or says none was carried | lets the latest attempt win when an older attempt succeeds late; ignores a superseded attempt error... |
| S08 | Identical in-flight snapshot is not resent | ACCEPTED_BOUNDED_EVIDENCE (B1) | none | does not create a second request when Build is pressed twice...; Local probe: A to B to A... |
| S11 | Latest-build failure keeps the earlier preview and names the build | ACCEPTED_BOUNDED_EVIDENCE (B1) | "Export failed", "Build #n", "The preview still shows build #n, not this build." | labels a newer failure with its build number...; does not erase a valid earlier result... |
| S16 | Copy, Download, Print use the displayed version | ACCEPTED_BOUNDED_EVIDENCE (B1) | version notice stays visible | copies, downloads and prints the displayed older version... |

B1 limits still apply: the status list and in-flight guard exist for the mounted component only, and no real iframe, print or screen-reader behavior was tested.

## Recovery And Cancel

PROOF-RECOVERY. The page has no Cancel control. Six different things could be meant by "cancel", and the current owner supports only the first three as local presentation:

| Row | Meaning | Class | Basis |
|---|---|---|---|
| S12 | Secret-refusal recovery mapping exists, but current route literal does not match it (F-01) | IMPLEMENTED_SOURCE_ONLY | Existing mock test uses the old source-content literal; real-route recovery remains unproven and source coupling is contradictory. |
| S14a | Change the input | IMPLEMENTED_SOURCE_ONLY | Editing never touches a request in flight; it only changes the version notice. |
| S14b | Start a newer build | ACCEPTED_BOUNDED_EVIDENCE (B1) | The older build is labelled replaced; copy does not say the server stopped. |
| S14c | Suppress a stale response | ACCEPTED_BOUNDED_EVIDENCE (B1) | `isLatest()` check at L506; the old response is recorded, never shown. |
| S14d | Abort the client request | UNSUPPORTED_BY_CURRENT_OWNER | The panel's `fetch` has no signal and the file has no abort, effect cleanup or `beforeunload`. The only `AbortController` is on the server receipt hop (proof.ts L75-76) and is a timeout, not a user cancel. |
| S14e | Confirmed server cancellation | UNSUPPORTED_BY_CURRENT_OWNER | No cancel endpoint or job is established in the named page/panel/export-route graph; no repository-wide absence is claimed. B2F saw a client disconnect and a late timer on the stub and states that this is not remote cancellation. |
| S14f | Unknown server outcome | UNKNOWN | Superseded, timed-out and unavailable copy refuses to assert an outcome. For a transport failure of the latest build the panel shows "Export failed" and the raw message and says nothing about whether the server acted (see O-3). |
| S15 | Unmount, refresh, navigation while pending | UNKNOWN | No cleanup or warning in source. State and refs are lost on remount or refresh. Whether the server finished is UNKNOWN and no test covers it. |

Absence of a cancel control is an unsupported capability, not a defect. A failed fetch does not show that server work did not happen.

## Independent Findings

### F-01 Secret-refusal recovery copy is unreachable through the real route

Source-proven contradiction, narrow, not critical.

- The panel maps the recovery text only when the error equals `Potential secret-like value detected in source content.` (panel L384).
- The route returns `Potential secret-like value detected in artifact export fields.` (route L323).
- The two strings differ, so a user whose text is refused sees only the raw English route string. The plain-language "remove that value and try again" copy (EN L158, VI L214) never shows. The missing-field literal does match (route L295, panel L387).
- Neither test pins the pair. The panel test mocks the old string (test L254). The route test only checks `/secret-like/i` (route test L101).
- History: the panel mapping was added in 5e99eb209 (2026-09-26) when the route said "source content". The route string changed in bc6e8b010 (2026-09-28).
- This is a route-to-panel string coupling that B1, B2e and B2F never exercised, so it does not reopen a closed defect.

Future oracle J-01 (NOT_EXECUTED_PLANNED): drive the panel with the exact string the route produces and assert the recovery copy in both languages. It fails at the current bytes.

### Observations, not ranked

- O-2: if build B settles while superseded build A is still in flight and the form is edited back to A, pressing Build does nothing and the button looks idle. B1 accepted this guard on purpose and the superseded notice explains it. No oracle was run. Case J-02.
- O-3: a latest-build network or parse failure shows the raw English message in both languages. It makes no false claim. Cases J-05, J-06.

## Independence And Boundaries

| Row | Meaning | Class | Basis |
|---|---|---|---|
| S17 | Send, B2 durable acceptance, artifact acceptance, store and witness | OUT_OF_SCOPE_STOPPED_ROOT | Excluded; no successor, finality or effect authority. |

PROOF-BOUNDARY. Send identity and scope, B2 durable acceptance, finality, storage and witness remain stopped roots (row S17, OUT_OF_SCOPE_STOPPED_ROOT). Nothing here depends on them, and nothing here selects a successor for them. D087 policy direction is retained unchanged.

Follow-up gate for F-01, status UNAPPROVED_PENDING_LOCAL_ADMISSION:

| Gate | Result |
|---|---|
| Owner | ArtifactExportPanel |
| Paths | `ArtifactExportPanel.tsx` and `ArtifactExportPanel.test.tsx` |
| Source-proven trigger | panel L384 against route L323 |
| Acceptance oracle | J-01 |
| Information gain | first check coupling the route literal to the panel literal |
| Overlap | none with send, B2, durable acceptance, storage or witness; adds no endpoint, AbortController or job contract |

This is the only ranked item. It is not dispatched.

## Static Cross-Check

The script is stored in the evidence JSON so it can be rerun:

```
python -c "import json;d=json.load(open('docs/reviews/evidence/cvf-ncr-r1-html-ux-support-audit-2026-10-02.json',encoding='utf-8'));exec(d['staticCrossCheck']['script'])"
```

It checks the 13 declared source hashes, 30 line locators, row-to-locator joins, the five reference proof IDs, that the panel has no abort or cleanup, that the F-01 strings differ while the missing-field strings match, English and Vietnamese label key parity, and that the working tree holds exactly the three output paths. Result PASS_STATIC_ONLY means source and document consistency only.

## Risk / Corrective Action

Line locators are bound to the hashes recorded in the JSON and break if the sources change. Nothing here proves browser, route, provider, cancellation or server-outcome behavior. F-01 is real at the source level but unexecuted. No source was changed.

## Decision / Disposition

COMPLETE_PENDING_REVIEW with one narrow independent finding (F-01) and two unranked observations. No critical gap. Cancel is unsupported by the current owner, which is not a defect. Local decides whether to admit the F-01 follow-up.

## Epistemic Process Block

### Expected Result / Prediction

The panel already carries attempt, version and timeout protections, so mapping it would find those covered and would find cancel unsupported rather than broken.

### Evidence Comparison

The prediction held for pending, version, supersede, stale-response and timeout rows. Comparing the route's error strings with the panel's mapping found one string the panel cannot match (F-01).

### Contradiction Or Gap Disposition

F-01 is a narrow source-proven contradiction in a recovery claim, unexecuted. No contradiction was found in the accepted B1 or B2F claims.

### Claim Update

Complete source-derived mapping plus one narrow finding, reviewer pending. Nothing is accepted and Q001/Q004 stay open.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Internal worker |
| Provider or surface | Shared private CVF workspace; source reading and Git only |
| Session or invocation | NCR R1 HTML UX support audit worker, 2026-10-02 |
| Working directory | Repository root |
| Command or tool surface | bound pre-implementation gate; file reads; hash and line checks; static cross-check |
| Target paths | the three worker outputs of the work order |
| Allowed scope source | Bound work order and paired GC-018 baseline |
| Before status evidence | clean worktree at HEAD `cddd1040d`; three output paths absent |
| After status evidence | three untracked worker paths, nothing staged, no commit |
| Diff evidence | `git status --short --untracked-files=all` lists exactly the three paths |
| Approval boundary | Worker evidence only; Local owns review and commit |
| Claim boundary | Source and document consistency only |
| Agent type | INTERNAL_AGENT worker |
| Invocation ID | cvf-ncr-r1-html-ux-support-audit-worker-20261002 |
| Expected manifest | `docs/reference/CVF_NCR_R1_HTML_UX_SUPPORT_AUDIT_2026-10-02.md`; `docs/reviews/evidence/cvf-ncr-r1-html-ux-support-audit-2026-10-02.json`; `docs/reviews/CVF_CVF_NCR_R1_HTML_UX_SUPPORT_AUDIT_WORKER_RETURN_2026-10-02.md` |
| Actual changed set | `docs/reference/CVF_NCR_R1_HTML_UX_SUPPORT_AUDIT_2026-10-02.md`; `docs/reviews/evidence/cvf-ncr-r1-html-ux-support-audit-2026-10-02.json`; `docs/reviews/CVF_CVF_NCR_R1_HTML_UX_SUPPORT_AUDIT_WORKER_RETURN_2026-10-02.md` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## Claim Boundary

Static source audit only. It makes no claim about runtime behavior, cancellation, server outcome, artifact acceptance, Q001/Q004, send or B2 closure, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Local Reviewer Qualification

D089 controlling completion review records the original worker digests and these bounded corrections: 13 declared source hashes; S12/S17 surfaced from the existing JSON; cancel/job absence scoped to named graph. The static script describes the original three-untracked-path pre-review snapshot, not a perpetual closure-state check: roadmap/source-ledger hashes must be compared to the recorded execution base after Local closure changes. No runtime proof or new product mutation.
