# CVF NCR HTML Work Transfer Source Record Reachability

Memory class: POINTER_RECORD

Status: SOURCE_AUDIT_PENDING_REVIEW

docType: reference

Date: 2026-10-02

## Purpose

Record, from source only, what the Work Transfer page actually consumes, who can produce those records, who can read them, and what is lost on the way into the HTML export. The prior Docker walkthrough reached the export panel only after an admin seeded a synthetic audit record, so it did not show that a normal user can produce a transfer record. This audit answers that question for the declared source graph. It is documentation only: nothing was executed, imported, requested or changed, and every behavior statement is a reading of source.

## Scope / Applies To

Consumer: `src/app/(dashboard)/work-transfer/page.tsx` in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`, followed through the admin audit route, admin session admission, enterprise roles, the control-plane event store and storage adapter, the session and middleware layers, the sidebar entry, and the export panel and route. Producer search scope: the Web package `src` tree plus the package-root `middleware.ts`, found during the search. Excluded: runtime stores, `.env` files, credentials, `node_modules`, build output, other extensions, and any execution. All locators were verified against the file bytes at executionBaseHead `4dd5276feda0a01e8b2479d7cae95cc184df862f`; per-file SHA-256 values are in the paired evidence JSON.

Independence: this is not a B2 successor. It proposes no store, schema, receipt, acceptance contract, witness or lock. B2 remains terminal, and no recommendation below depends on B2 durable acceptance.

## 1. Source Graph From Consumer To Store

| Step | What the source does | Locator |
|---|---|---|
| Form and check | The page keeps from, to, status and summary in local React state and computes `validateHandoff(...)` with `useMemo`. Nothing is sent anywhere | `page.tsx` line 136; state at lines 125-130 |
| Only network call | `fetch('/api/admin/audit')`, a GET with no options | `page.tsx` line 145 |
| Response handling | `success` true with an array sets state ready and keeps `data.slice(0, 8)`; anything else, or a rejected fetch, sets state error | `page.tsx` lines 149-158 (slice at 150, error at 153 and 157) |
| Empty and populated states | empty text when the array is empty; otherwise a list with one Export HTML button per row | `page.tsx` lines 247-279 |
| Selection | clicking toggles one selected row; the selected row renders `ArtifactExportPanel` with `initialRequest` | `page.tsx` lines 162-164, 273 |
| Request mapping | `recordToExportRequest` builds title, sourcePath, sourceContent, memoryClass, status, claimBoundary and receiptAnchor from seven record fields | `page.tsx` lines 98-118 |
| Route admission | `requireAdminApiSession(request, '/api/admin/audit')`; a non-session or non-admin caller is refused | `audit/route.ts` line 9; `admin-session.ts` lines 245-267 |
| Read | `readAuditEvents()` with no query parameter, no actor, organization or team filter | `audit/route.ts` line 14 |
| Filter and order | the whole control-plane list is sorted ascending by timestamp, then filtered to `kind === 'audit'` | `control-plane-events.ts` lines 111-114, 167-170 |
| Store | one adapter (file by default, SQLite or Redis by environment) at one store path from an environment variable or a default under the working directory | `control-plane-events.ts` lines 62, 101-105; `storage-adapter.ts` lines 62, 515-522 |

The record type the page expects is `AuditRecord` with `id`, `timestamp`, `action`, `actorId`, `actorRole`, `targetResource`, `outcome` (`page.tsx` lines 77-85). The page never reads `eventType`, `riskLevel`, `phase`, `payload` or `evidenceClass`. Nothing constrains the event kind beyond `audit`, and nothing constrains `eventType` or `action` to a transfer meaning.

## 2. Producer Families

The symbol search matched 24 non-test source files for `appendAuditEvent` or `appendControlPlaneEvent`. Twenty-two call it, one is the definition file `control-plane-events.ts`, and one is the unrelated envelope helper `web-governance-envelope.ts`. The package-root middleware, outside `src`, also posts to the audit route. They fall into families. None emits an event whose meaning is a work transfer.

| Family | Files | Event types and actions seen | Trigger and reachability | Classification |
|---|---|---|---|---|
| Admin access denial | `admin-session.ts` lines 192-203 | `ADMIN_ACCESS_DENIED`, `CALL_ADMIN_API` or `READ_ADMIN_ROUTE` | any authenticated non-admin calling an admin API or admin server page, including `GET /api/admin/audit` itself | DENIAL, production-reachable by non-admins |
| Break-glass | `admin-session.ts` lines 90-184 | `BREAK_GLASS_USED`, `BREAK_GLASS_DENIED`, `EMERGENCY_ACCESS` | request with the break-glass header and the configured token | ADMIN_INTERNAL |
| Middleware denial | `middleware.ts` lines 36-58 | `ADMIN_ACCESS_DENIED`, `READ_ADMIN_ROUTE`, outcome `REDIRECTED`, posted through the internal-secret branch of the audit route | an authenticated non-admin opening an `/admin` page, only when the internal audit secret is configured | DENIAL via internal POST |
| Admin configuration | admin routes for tool-registry policy and knowledge scope, quota policy and override, DLP policy, SIEM, impersonation start and end | `TOOL_POLICY_UPDATED`, `QUOTA_*`, `DLP_POLICY_UPDATED`, `SIEM_CONFIG_UPDATED`, `IMPERSONATION_*` | admin sessions only | ADMIN_INTERNAL |
| Approvals | `api/approvals/route.ts`, `api/approvals/[id]/route.ts`, and the resume branch in the execute route | `APPROVAL_EXPIRED`, `APPROVAL_DECIDED`, `APPROVAL_CONSUMED` | approval flows | PRODUCTION, not transfer |
| Execute path | `api/execute/route.ts`, `route-final-response.ts`, `route-knowledge-context.ts`, `execute-telemetry.ts`, `execute-role-permission-gate.ts`, `execute-route-guards` consumers | `DLP_REDACTION_APPLIED`, `QUOTA_HARD_CAP_BLOCKED`, `ACTOR_ROLE_GATE_REJECTED`, `OUTPUT_SAFETY_TRIGGERED`, `WORKFLOW_BINDING_EXECUTED`, and, in `execute-telemetry.ts` line 111, action `EXECUTE_AI_TEMPLATE`, among others | any authenticated user calling the execute API | PRODUCTION by normal users, not transfer |
| Mandatory gateway | `route-guard-gateway.ts` lines 49-69, called from the execute route | `MANDATORY_GATEWAY_EVALUATED` with `action` from `resolveGuardAction(rawBody)`, which returns the request body's own `action` string when present | the same authenticated execute call | PRODUCTION, with a user-influenced action label |
| Governance feedback | `api/governance/false-positive-report/route.ts` | `FALSE_POSITIVE_REPORTED` | user report route | PRODUCTION, not transfer |
| Memory and LPCI | `aif-memory-reinjection-route.ts`, `lpci/release-audit.ts` | `AUDIT_MEMORY_RECEIPT_CAPTURED`, `LPCI_QUERY_TERMINAL` | their routes | PRODUCTION, not transfer |
| Policy events | `policy-events.ts` through `appendControlPlaneEvent` | policy event kinds | admin | filtered out of the audit read because the kind is not `audit` |
| Direct admin POST | `audit/route.ts` lines 18-45 | any `eventType` and `action` from the body; `actorId` and `actorRole` come from the body first and the session second (lines 32-33) | an admin session, or the internal-secret header | ADMIN_SEED_POSSIBLE: an admin can write any actor and action, so a seeded row is indistinguishable by its fields |
| Tests and mocks | many `*.test.*` files and `page.test.tsx` | mocks of `appendAuditEvent` | test runs | TEST_ONLY, not reachability |

The one handoff-named symbol found in an audit-producing file is `buildExecutionContinuityHandoffReadout` in `route-final-response.ts` (lines 13, 443-512). It builds a readout object inside the execute response and is not an audit append. The page's own check function `validateHandoff` has two callers outside its own file: the page, which persists nothing, and `mlw-runtime-chain-readouts.ts` line 148, which was seen only as a call building a readout and was not traced further.

Unresolved indirect edges, stated and not assumed away: any producer that builds its `eventType` or payload dynamically beyond the literals searched; callers of `lpci/release-audit.ts` and `aif-memory-reinjection-route.ts`; whatever else posts to the audit route from outside the searched tree; and the runtime event contents of any real store. The absence conclusion applies only to the searched graph and patterns in the evidence JSON, not to the repository.

## 3. Does Normal Work Transfer Create A Transfer Record

In the declared graph it does not. The page validates locally and never writes. The only data the history shows is whatever audit events already exist, produced by unrelated families above. A user can do the full check, change the status, edit the summary and press nothing that persists. The word "transfer" appears only in the page copy and in the mapping that titles an exported record `Work Transfer`; no event type, action or filter makes an event a transfer.

## 4. Role And Data Scope

- Page entry: `middleware.ts` requires only an authenticated session for `/work-transfer` (lines 23-34); its admin check covers paths under `/admin` only (line 36). The sidebar shows the Work Transfer link to every role except viewer (`Sidebar.tsx` lines 202-205).
- History read: admission is `canAccessAdmin(role)` for roles `owner` and `admin` (`enterprise-access.ts` lines 3-4, 11-14), or a break-glass session (`admin-session.ts` lines 206-216). A developer or reviewer reaches the page, receives 403 (401 without a session) and the page shows its error state (`page.tsx` lines 149-158). A viewer has no link but can open the URL and gets the same result.
- Denial write effect: a refused API read appends an `ADMIN_ACCESS_DENIED` event before responding (`admin-session.ts` lines 259-265, 186-203). A read-only worker task does not authorize making that request, and none was made. For an unauthenticated browser, the middleware redirects `/api/*` to login first, so that event appears only for authenticated non-admins.
- Actor derivation on read: server session only. On the admin POST the body wins: `actorId` and `actorRole` come from the body before the session (`audit/route.ts` lines 32-33). The internal-secret branch has no session at all.
- Session defaults: when a token lacks fields, role defaults to `developer`, organization `org_cvf`, team `team_eng` (`middleware-auth.ts` lines 101-109). In non-development builds a session without an OAuth identity binding is null (lines 97-99). Real account, role and workspace configuration is UNKNOWN.
- Data scope: store-wide. The read has no organization, team, workspace or actor filter, and audit events carry no organization or team field. Any admin sees every audit event of every actor in the one store.
- Order and selection: the store sorts ascending (`control-plane-events.ts` line 113, asserted as intended by `control-plane-events.durable.test.ts` line 167) and the page keeps the first eight (`page.tsx` line 150). The section title says recent. With the file and SQLite adapters there is no retention trim (`retentionSeconds` null), so once more than eight audit events exist the page shows the eight oldest and never a newer one; Redis trims at 30 days. This is a reading of source; the actual event count is RUNTIME_UNKNOWN.

## 5. Record Fields And Export Mapping

| Consumer field | Source | Retained in export | Notes |
|---|---|---|---|
| `id` | event id | yes, as `receiptAnchor` = `transfer-<id>` | a rendering anchor, not a link back to the store |
| `timestamp` | event time | yes, in source text | |
| `action` | event | yes, in title and source text | for gateway events this can come from the user's request body |
| `actorId`, `actorRole` | event | yes, in source text | the admin POST path lets these be arbitrary |
| `targetResource` | event | yes, as `sourcePath` | an empty or missing value makes the export route answer 400 (`export/route.ts` line 295) |
| `outcome` | event | yes, as `status` | |
| `eventType`, `riskLevel`, `phase`, `payload`, `evidenceClass` | event | lost | the payload carries break-glass and impersonation markers, so the real-actor distinction is dropped |
| organization, team | not in audit events | not available | |

After the mapping, every field is user-editable in the panel, including the source text (`ArtifactExportPanel.tsx` line 712 and the other `updateRequest` fields), and the export route accepts any well-formed body. Nothing binds the exported content to the selected event, so the exported "Work Transfer Record" proves only what the user typed or left in the form. The route still labels it a draft and not governance proof.

## 6. Journey Matrix

Each row is a reading of source. RUNTIME_UNKNOWN means source does not decide it. The negative plans in the evidence JSON are all NOT_EXECUTED_PLANNED.

| ID | Journey | Source-derived outcome | Class |
|---|---|---|---|
| J01 | admin opens the page with an empty store | empty text, no export button, no panel | SOURCE_DERIVED |
| J02 | admin, store holds only unrelated audit events (denial or execute; non-audit policy events are filtered out) | a list of those events labelled as transfers; Export HTML titles them "Work Transfer" | SOURCE_DERIVED |
| J03 | ordinary non-admin (developer or reviewer) | page loads; read refused; error text; an `ADMIN_ACCESS_DENIED` event is appended | SOURCE_DERIVED, real role binding RUNTIME_UNKNOWN |
| J04 | unauthenticated | initial page navigation redirects to login before the page mounts; a later session loss during the audit fetch is a separate, unexecuted journey | SOURCE_DERIVED |
| J05 | validation success or failure | local computation only; no record, no request | SOURCE_DERIVED |
| J06 | event with a missing or empty field | an undefined `sourcePath` overrides the panel default through the object spread (`ArtifactExportPanel.tsx` line 328), the request would be sent without it, and the route's required-field check (`export/route.ts` line 295) would refuse it; the panel's own handling was not traced, so this is not decided by source | UNRESOLVED_SOURCE_EDGE |
| J07 | loading and error | three states exist; a non-success body or rejected fetch gives error; no retry | SOURCE_DERIVED |
| J08 | select and deselect | one row at a time; the panel mounts inline | SOURCE_DERIVED |
| J09 | more than eight events | the eight oldest are shown | SOURCE_DERIVED, event volume RUNTIME_UNKNOWN |
| J10 | denial-produced event | the denied read of J03 becomes a row an admin later sees and can export as a "transfer" | SOURCE_DERIVED |
| J11 | admin seed or test fixture | the walkthrough seeded an admin audit record; `page.test.tsx` mocks an empty list and the panel; neither is production reachability | SEED_AND_TEST_ONLY |
| J12 | break-glass session | admitted as owner-like; reads like an admin | SOURCE_DERIVED |
| J13 | export of a selected event | panel with every field editable; build calls the export route | SOURCE_DERIVED |
| J14 | admin impersonating a non-admin | the effective role is the non-admin's, so the read is refused | SOURCE_DERIVED |

## 7. Findings

Implementation-shaped observations (candidates for a fix, none approved) are separated from operator policy and from unknowns.

| ID | Kind | Statement |
|---|---|---|
| WT-F01 | source gap | no dedicated transfer-record producer exists in the declared graph; the page only exposes existing audit events |
| WT-F02 | source gap | the history has no filter that makes an event a transfer, so unrelated events appear under "Recent transfers" and export as "Work Transfer Record" |
| WT-F03 | implementation defect candidate | ascending store order with the page's first-eight slice shows the oldest eight events, contradicting the section title |
| WT-F04 | operator policy | which roles may see transfer history, versus the page and the sidebar being open to nearly every role, and whether a denied read should write an event |
| WT-F05 | operator policy | the read is store-wide with no organization, team or actor scope |
| WT-F06 | implementation observation | export provenance is lost: event type and payload are dropped and the content is client-editable, with nothing tying it to the selected event |
| WT-F07 | evidence limit | admin POST lets the body set actor fields, so a seeded row is not distinguishable from a real producer by its fields |
| WT-F08 | observation | gateway events carry a request-body-influenced `action`, so a normal user can influence one visible label |
| WT-F09 | test gap | the inspected page test does not cover populated history, order/first-eight, selection or record mapping; generic non-admin refusal/audit-event coverage exists in admin-session.test.ts, but page integration coverage is unverified |
| WT-F10 | unresolved edge | behavior for events with missing fields, and the unsearched dynamic and outside-the-tree producers |

## 8. Verdict

For the declared graph: the normal-user path from Work Transfer to an exportable history record is not source-reachable as a transfer. The page is reachable by most roles, the history is reachable only by owner or admin, the history shows unrelated audit events, and no producer in the searched graph records a transfer. The missing pieces are a named producer, a filter or kind that defines a transfer record, and a role and data-scope contract. This is a source finding, not a runtime result: real roles, workspace mapping, store contents and configuration are UNKNOWN, and the Docker walkthrough is consumed only for its stated limit (seeded history).

## 9. Overlap, Freshness And Independence

| Item | Disposition |
|---|---|
| Docker walkthrough, 2026-09-29 | consumed for its limit that the record was seeded; not repeated; warm receipt and ledger join untouched |
| B1 Preview, Print and transport evidence | read-only context; unchanged by this audit |
| Stopped B2 chain | untouched; no durable acceptance, store, witness or lock content here, and no recommendation requires them |
| Existing owners | page, audit route, admin session, enterprise roles, control-plane events and the export panel are all reused as described; nothing new is proposed as a second framework |
| Freshness | all file hashes were taken at the execution base; the search patterns and counts are in the evidence JSON and can be rerun |

## 10. Ranked Next Recommendation

One recommendation, smallest first. It is a proposal and is not approved by this audit.

Rank 1: a Local and operator decision, then one bounded implementation packet on the existing owners. Decision first, because the code shape depends on two policy facts that source cannot decide: what counts as a transfer record, and which roles may see which records. Candidate shapes are (a) relabel and correct the page as an admin audit view, or (b) add a transfer producer that appends an audit event when an authenticated user confirms a transfer, with a scoped read. Owners and consumers: `work-transfer/page.tsx`, `control-plane-events.ts` (read order and filter), the audit route or a sibling route under `src/app/api` (proposed, not existing), and the export mapping. Evidence gap closed: WT-F01, WT-F02, WT-F03, WT-F06.

Future acceptance oracles, all unexecuted:

- an unseeded user flow validates, records and lists a transfer, then exports it, without an admin seed;
- a non-admin sees only the records the chosen scope allows, and an admin sees the chosen wider scope;
- the list is newest first and excludes unrelated event types;
- a refused read is not shown as a transfer;
- the export carries the event type and payload provenance and a server-checkable link to the selected event;
- a record with a missing field is handled without an unhandled 400.

Required authority: Local dispatch, and operator choice of record definition and role scope. Parked and not authorized: real data, accounts or workspaces, provider or pilot effects, Q001 and Q004 exit, P11, public sync and deployment. Ranked after it, not proposed together: Rank 2, fix only the ordering and the "Recent" label (WT-F03) if the operator wants no producer yet; Rank 3, add the missing page and route tests (WT-F09) as a documentation-and-test-only packet.

## Claim Boundary

rawMemoryReleased=false: the memory and reinjection producer files were read only as source and listed by name; no memory content, raw memory, reinjection payload or retrieval result was read, produced or released.

Source-derived reachability and permission and data-scope observations only. There is no observed production user journey, real account or role mapping, runtime policy enforcement, governance success, durable acceptance, Q001, Q004 or B2 closure, or public or deployment readiness. The static checks behind this audit are `PASS_STATIC_ONLY`: they confirm that cited locators exist and that the document and evidence agree, not that any behavior holds.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Local Review Qualification

Local source-audit review at `docs/reviews/CVF_CVF_NCR_HTML_WORK_TRANSFER_SOURCE_RECORD_REACHABILITY_COMPLETION_2026-10-02.md` controls accepted scope. Original worker output digests are preserved there. J04 separates initial navigation from session loss after mount; J02 excludes non-audit policy events; WT-F09 is restricted to inspected page tests. S1-S6 are equivalent query descriptions, not exact executed rg receipts: worker reports a Python scanner, whose executable source was not supplied. S4 repository-wide search is excluded from accepted scope. Producer-family classification is advisory where entry points/dynamic edges remain untraced; accept no repository-wide absence or complete producer proof.
