# CVF NCR Work Transfer Recent Order

Memory class: POINTER_RECORD

Status: LOCAL_UI_ORDER_CORRECTED_PENDING_REVIEW

docType: reference

Date: 2026-10-02

## Purpose

Record what changed on the Work Transfer page for finding WT-F03, how it was proved, and where the change stops. The page titled its history "Recent transfers" but kept the first eight records of a list that the shared store sorts ascending, so it showed the eight oldest. The page now orders a copy of the response newest first and caps at eight afterwards. Nothing about who may read the history, what counts as a transfer, or what the export carries was changed.

## Scope / Applies To

One existing page, `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx`, and its existing test file in the same folder. The endpoint, session and role admission, loading, error and empty handling, selection and deselection, `recordToExportRequest`, and the Vietnamese and English copy are unchanged. The store sort in `control-plane-events.ts` is unchanged and still ascending; its ascending order is asserted by its own test and is the contract this page now accounts for.

## The Change

One statement in the successful-response branch. Before: `setRecords(payload.data.slice(0, 8))`. After: `setRecords([...payload.data].sort((a, b) => b.timestamp.localeCompare(a.timestamp)).slice(0, 8))`, with a two-line comment. Properties:

- Order before cap: the whole response is ordered, then the first eight are kept, so the cap can no longer discard the newest records.
- Copy, not mutation: the spread makes a new array, so the response array and its record objects are untouched.
- Same comparator as the store, reversed: the store orders by `timestamp.localeCompare`; the page uses the same comparison descending, so the two agree on what "newer" means for the canonical ISO timestamps the store holds.
- Stable ties: `Array.prototype.sort` is stable, and the comparator returns 0 for equal timestamps, so records with equal timestamps keep the order the store gave them.
- Identity preserved: the same record objects are rendered, so each export button still opens the export request of its own record by id.

## Proof

Local, mocked UI tests only. Each test renders the real page with a synthetic mocked GET response and reads the rendered order from the `export-record-<id>` test ids. Expected sequences are literal ids; they are not computed by a second copy of the comparator. The export panel is a mock that exposes the `initialRequest` it received.

| Case | Oracle | Old page | New page |
|---|---|---|---|
| 12 records, ascending input | literal newest eight, newest first; four oldest absent | FAIL, rendered evt-01 to evt-08 | PASS |
| 12 records, shuffled input | same literal sequence | FAIL, rendered the first eight of the input order | PASS |
| equal timestamps, 10 records | q1, q2, p1, p2, a6, a5, a4, a3; a1 and a2 absent | FAIL, rendered a1 to a6, p1, p2 | PASS |
| non-mutation | frozen array and records, unchanged snapshot, no throw | FAIL (same test also asserts the corrected order) | PASS |
| three records, exactly eight, empty, unsuccessful payload, rejected fetch | order for three and eight; empty and error states | FAIL on order for three records | PASS |
| English title with corrected order | title present, newest first | FAIL, first row evt-01 | PASS |
| selection by identity | clicking the first displayed record gives its literal export request; clicking another switches; clicking again removes the panel | FAIL, the newest record is not rendered | PASS |
| the three existing tests | unchanged assertions | PASS | PASS |

Old page: 7 failed, 3 passed (exit 1), each failing on the intended order or limit assertion. New page: 10 passed (exit 0). Type check and lint of the two files exit 0. Three wrong implementations were also tried against the new tests and each was caught: sorting after the cap (6 failures), sorting the response in place (1 failure, the non-mutation test, because the frozen array makes it throw into the error state), and reversing an ascending list (4 failures, including ties). The page was restored to its exact final bytes after each trial.

## Boundary And What Is Not Claimed

- Timestamps: the comparator assumes a string timestamp on every record, as the store does. Malformed/non-string timestamps may make timestamp.localeCompare throw for comparisons that use such a value as the receiver; behavior depends on array size and comparisons. No guarantee that every malformed record throws or that the store always prevents it reaching this page. Source inference only, untested; schema/fallback policy outside scope. Malformed, legacy and non-canonical timestamp policy is outside this change and no fallback was invented.
- Missing fields, role and data scope, the definition of a transfer record, the producer, export provenance, the store order and the "oldest eight" behavior of any other consumer are untouched. WT-F01, WT-F02 and WT-F04 to WT-F10 remain as recorded in the source audit.
- Not shown: real HTTP, a real store, a real browser, the real export panel, role bindings or any production behavior. Fixtures are synthetic and prove local rendering order and selection only.

## Claim Boundary

A page-local, mocked-UI proof that the displayed list is the latest eight records, newest first, and that selection maps a displayed record to its own export request. It is not a policy or access proof, an acceptance of Work Transfer as a transfer system, or a Q001, Q004, B2, P11, public or deployment claim.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Local Review Qualification

Controlling review: `docs/reviews/CVF_CVF_NCR_WORK_TRANSFER_RECENT_ORDER_COMPLETION_2026-10-02.md`. Timestamp failure inference is conditional and untested; not a guarantee of store rejection. Worker pre-edit seal remains unchanged. Original document/evidence/return digests recorded in the review; no Local code/test repair or duplicate executable suite.
