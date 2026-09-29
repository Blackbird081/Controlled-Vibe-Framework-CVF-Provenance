# CVF GC010 SCR-R2-T1F Pending Agent Execution Approval Snapshot Durable Compatibility Correction Decision

Memory class: governed-assessment

docType: assessment

Status: REVIEWER_ACCEPTED_CLOSED_PASS_BOUNDED

Batch ID: GC010-SCR-R2-T1F

Date: 2026-08-31

executionBaseHead: `68682362839c9bcdbfc569e2aac9393902626663`

Selected terminal token: `CANONICAL_APPROVAL_REQUEST_HASH_FAIL_CLOSED_REISSUE_READY_FOR_BOUNDED_IMPLEMENTATION`

successorTrancheOpened: NO

## Purpose

Select the smallest source-owned correction contract for the T1E approval
snapshot/hash versus durable-persistence contradiction. This assessment is a
decision artifact only; it changes no source, test, record, route, or runtime.

## Target / Source

The target is the contract among approval snapshot construction, approval
request identity, SQLite canonical payload serialization, pending claim drift
checks, and execute-route fail-closed behavior. Evidence is limited to the
fourteen paths named by the governing work order and current local Git/search
receipts.

## Scope / Methodology

At fresh HEAD `68682362839c9bcdbfc569e2aac9393902626663`, the worker confirmed a clean
worktree and absent output paths, ran the 82-command pre-implementation gate,
read the named source/evidence paths, classified current hash/version/caller
matches, and applied one common rubric to all four families: owner fit, stable
identity, fail-closed safety, issued-approval compatibility, persisted-pending
compatibility, migration/rollback safety, changed-set width, proof cost, and
proportionality.

Observed source facts, deductions, and proposed future contract terms are kept
separate below.

## Source Verification And Processing Ledger

| Source | Fresh symbol or line evidence | Processing status | Disposition |
| --- | --- | --- | --- |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.ts` | `sortStringRecord` lines 34-43 uses `localeCompare`; `buildApprovalRequestSnapshot` lines 71-92 emits optional own properties with `undefined`; `computeApprovalRequestHash` lines 95-98 hashes `JSON.stringify(snapshot)` | READ | ACCEPT_READ_ONLY |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.ts` | `ApprovalRequestSnapshot` lines 21-35; file load/persist lines 69-103 uses JSON parse/stringify with no hash version | READ | ACCEPT_READ_ONLY |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/route.ts` | POST builds snapshot lines 63-77, stores it lines 78-100, and computes `requestHash` line 101 | READ | ACCEPT_READ_ONLY |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | current snapshot/hash lines 177-182; missing hash reissue 196-204; hash mismatch 229-237 returns 409 | READ | ACCEPT_READ_ONLY |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.ts` | canonical object keys sort ordinal and reject `undefined` lines 149-169; create verifies hash lines 660-670; claim drift rows 879-883 fail closed | READ | ACCEPT_READ_ONLY |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.ts` | `encodeRecordToRow` line 256 persists `payload_json` through `canonicalizeToJson`; decode lines 350-414 parses, validates, and rejects corruption without rewrite | READ | ACCEPT_READ_ONLY |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approvals.c4.test.ts` | approval POST regression lines 195-244 verifies request hash and actor-bound snapshot | READ | ACCEPT_READ_ONLY |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/store.test.ts` | lines 9-39 prove file-backed persist/reload but do not recompute hash compatibility | READ | ACCEPT_READ_ONLY |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts` | matching resume lines 801-852 and changed-payload 409 mismatch lines 854-895 | READ | ACCEPT_READ_ONLY |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution.test.ts` | create-time mismatch lines 459-461; claim request-hash/current-snapshot drift regressions lines 653-680 | READ | ACCEPT_READ_ONLY |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/pending-agent-execution-sqlite-store.test.ts` | create/readback lines 161-174; restart survival lines 567-588; schema-version checks lines 828-847 | READ | ACCEPT_READ_ONLY |
| `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/pending-agent-execution-local-harness.test.ts` | versions 0/1/2/3 lines 144-196; reopen lines 198-210; stringify/parse-masked builder contradiction lines 264-287 | READ | ACCEPT_READ_ONLY |
| `docs/reviews/CVF_GC010_SCR_R2_T1E_PENDING_AGENT_EXECUTION_LOCAL_HARNESS_NON_PRODUCTION_IMPLEMENTATION_WORKER_RETURN_2026-08-31.md` | lines 60-88 records exact mismatch and separately authorized correction need | READ | ACCEPT_READ_ONLY |
| `docs/reviews/CVF_GC010_SCR_R2_T1E_PENDING_AGENT_EXECUTION_LOCAL_HARNESS_NON_PRODUCTION_IMPLEMENTATION_COMPLETION_2026-08-31.md` | lines 40-66 independently accepts the blocker and keeps T1E parked | READ | ACCEPT_READ_ONLY |

Reconciliation: manifest=14; ledger terminal=14 READ; deferred=0;
blocked/unreadable=0; unresolved=0.

## Negative Search And Collision Receipt

| Query | Result | Classification |
| --- | --- | --- |
| exact two worker output paths via `Test-Path -LiteralPath` | both absent before writing | NO_COLLISION |
| T1F token search under `docs` and `CVF_SESSION` | committed dispatch/continuity self-matches only | EXPECTED_AUTHORITY_MATCHES |
| `computeApprovalRequestHash|buildApprovalRequestSnapshot|approvalRequestHash` under cvf-web source | approval binding, two route callers, pending core, and focused tests | CURRENT_OWNER_AND_CONSUMER_MATCHES |
| `hashVersion|approvalHashVersion|preimageVersion|migrat` under cvf-web source | no approval-hash/preimage version owner; unrelated migration text only | NO_CURRENT_APPROVAL_HASH_VERSION_OWNER |
| `buildPendingAgentExecutionRuntime|AgentExecutionRuntime` under named roots | T1C/T1E tests/composition, one manual API-key script, and guard-contract test/source matches | NO_NEW_PRODUCTION_PENDING_CALLER |

## Observed Contract Contradiction

1. The approval owner constructs an object in a fixed but non-canonical root
   insertion order and retains own optional properties whose value is
   `undefined`.
2. Its hash is the SHA-256 of order-sensitive `JSON.stringify` bytes.
3. T1A canonical validation rejects own `undefined`; T1C persists the containing
   payload with ordinal-key canonical JSON.
4. The current T1E regression first removes `undefined` by stringify/parse,
   then demonstrates that durable readback changes root insertion order and
   claim recomputation returns `APPROVAL_SNAPSHOT_HASH_MISMATCH`, version 1
   `STALE`.

## Four-Family Decision Matrix

| Family | Owner fit | Stable identity and fail-closed safety | Legacy/migration and rollback | Changed set and proof | Proportional disposition |
| --- | --- | --- | --- | --- | --- |
| A - canonical approval-request hash plus reissue | STRONG: approval identity remains at `approval-binding.ts` | STRONG: schema projection, ordinal ordering, omitted optional values, no dual acceptance | BOUNDED: old unversioned records reject/reissue; rollback remains fail-closed | one source owner, one new focused test, two existing regression tests | SELECT |
| B - preserve SQLite byte order | WEAK: persistence would own approval semantics | WEAK: weakens accepted canonical persistence and couples store bytes to caller insertion order | HIGH: special subtree serializer or global persistence regression | store/source regressions plus wider integrity proof | REJECT_EXISTING_OWNER_CONTRACT_CONFLICT |
| C - pending-core semantic equivalence | WEAK: duplicates approval identity in pending claim | WEAK: leaves builder `undefined` and execute-route order-sensitive hash unresolved | AMBIGUOUS: may accept semantics whose stored hash no longer proves its exact preimage | pending core/tests plus separate route/builder correction still needed | REJECT_INCOMPLETE_AND_WRONG_OWNER |
| D - versioned hash/preimage migration | VALID only when compatibility continuity is required | STRONG with explicit version admission | HIGHEST: version fields, dual-read window, migration and rollback matrix | multi-owner schema/store/route/pending changes | DEFER_DISPROPORTIONATE_UNTIL_TRIGGER |

## Findings / Position

Family A is selected. Canonical approval-request identity belongs to the
approval binding owner because both approval issuance and execution already
call its builder/hash API, while T1A consumes that identity and T1C must remain
an identity-neutral canonical store.

The future contract is schema-specific, not a generic object-equivalence rule:

- accepted root keys are exactly `actorAuthMode`, `actorId`, `actorOrgId`,
  `actorTeamId`, `cvfPhase`, `cvfRiskLevel`, `inputs`, `intent`,
  `knowledgeCollectionId`, `model`, `provider`, `templateId`, and
  `templateName`;
- root keys and `inputs` keys use ordinal UTF-16 comparison (`a < b`), never
  locale-dependent ordering;
- `templateId`, `templateName`, and `intent` remain required string values;
- the builder omits every optional property whose normalized value is
  `undefined`; defined nullable fields retain explicit `null`;
- the hash boundary rejects unknown own keys, present own `undefined`, symbol,
  accessor, non-plain, or type-invalid values instead of silently dropping
  them;
- the preimage is UTF-8 `JSON.stringify` of the schema projection inserted in
  the ordinal key order above, with nested `inputs` projected in ordinal key
  order and no whitespace; SHA-256 lowercase hex remains the digest format.

This byte contract matches the canonical persisted snapshot order without
making the SQLite store an approval-aware serializer.

## Mandatory Decision Questions

1. **Owner:** `approval-binding.ts`; it already defines builder and hash used by
   both issue and execute callers.
2. **Preimage:** the exact recognized projection and ordinal rules above,
   serialized once with UTF-8 `JSON.stringify` and hashed SHA-256.
3. **Optional `undefined`:** omitted by the builder and rejected if explicitly
   present at the hash boundary.
4. **Missing pre-binding hash:** execute route retains 409 with the existing
   `predates request binding and must be re-issued` receipt; a malformed pending
   payload remains fail-closed/corrupt rather than synthesized.
5. **Old order-sensitive approval hash:** in-memory and file-reloaded records
   retain their old digest; current canonical recomputation differs and the
   execute route returns 409 `Approval request does not match the current
   execution payload.` The approval ID cannot authorize execution and must be
   reissued. No rewrite occurs.
6. **Old SQLite schema-version-1 pending row:** a CREATED row whose payload
   carries the old hash fails recomputation and transitions to `STALE` with
   `STALE_APPROVAL_SNAPSHOT_HASH_MISMATCH`; an already-CLAIMED row is not
   reclaimable and receives no new grant. Neither path rewrites hash/snapshot.
7. **Dual acceptance:** forbidden. There is no implicit old-hash fallback or
   time window.
8. **Fail-closed:** preserved by existing route comparison, create validation,
   claim drift ordering, CAS stale transition, and corrupt-row rejection.
9. **Future files:** exactly the four-path manifest below; unchanged T1A/T1C
   tests run as regressions but are not edited.
10. **Raw-builder proof:** pass the direct return value of
    `buildApprovalRequestSnapshot` into approval and pending fixtures, without
    stringify/parse, then observe versions 0/1/2/3 plus close/reopen equality.
11. **Route receipt:** a manually seeded legacy order-sensitive hash with the
    same semantic request receives 409 mismatch and zero provider invocation;
    a newly issued canonical hash resumes only the exact matching payload.
12. **Wider-migration trigger:** any requirement to preserve already-issued
    approval availability, silently transform records, support a mixed-version
    dual-read window, or migrate hashes opens Family D instead of A.
13. **Deploy/rollback:** forward deploy rejects old-contract records. Rollback
    safely validates new persisted snapshots when their canonical insertion
    order remains intact, while a rebuilt old-order route request may reject
    and require reissue. If uninterrupted bidirectional availability rather
    than fail-closed rejection is required, stop and select Family D.
14. **Rollback:** revert only the four-path implementation tranche. Do not
    rewrite records or relax comparisons. Records not validated by the rolled
    back hash owner fail closed/reissue; any demand to accept both algorithms
    is the stop-to-Family-D condition.

## Exact Future Implementation Manifest

Only a separately authorized bounded implementation may change:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.ts`
2. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.test.ts`
3. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts`
4. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/pending-agent-execution-local-harness.test.ts`

The implementation must not edit the approval route/store, pending core,
SQLite store/composition/harness source, package/barrel, provider, audit,
configuration, workflow, or production surfaces. It must run the existing
approval/store, T1A, and T1C suites unchanged as regressions.

## Future Proof And Reopen Contract

T1E remains blocked until all of these pass under separately committed
authority:

- focused approval binding tests prove raw builder output has no own
  `undefined`, root and input order are ordinal, semantic key-order variants
  hash identically, unknown/invalid shapes reject, and a legacy old-order hash
  is not dual-accepted;
- execute-route tests prove new exact-match resume and legacy same-semantics
  hash 409/reissue with zero provider call;
- the T1E harness test removes its stringify/parse mask and proves direct raw
  builder create/claim/begin/terminal versions `0/1/2/3`, durable reopen, and
  caller identity;
- unchanged T1A/T1C/approval/store regressions and TypeScript pass;
- no package export, production caller, provider/live, or wider migration claim
  is inferred.

## Evidence / Verification

Verification is the fourteen-row source ledger, the bounded negative-search
receipt, the four-family common-rubric matrix, and the mandatory-question
answers above. Runtime/product tests are N/A with reason: T1F is decision-only
and authorizes no source implementation.

## Risk / Corrective Action

The bounded correction intentionally trades legacy approval availability for
fail-closed reissue. That is safe only while the operator accepts the reissue
window and no mixed-version continuity requirement exists. Otherwise this
decision stops before implementation and Family D requires a new decision
packet.

## Decision / Recommendation / Disposition

Terminal decision:
`CANONICAL_APPROVAL_REQUEST_HASH_FAIL_CLOSED_REISSUE_READY_FOR_BOUNDED_IMPLEMENTATION`

No implementation tranche is opened by this assessment.

## Corpus Completeness And Report Integrity

- Corpus task class: COMPARISON
- Corpus root: exact fourteen named paths in the Source Verification And Processing Ledger
- Snapshot time: 2026-08-31 at execution base `68682362839c9bcdbfc569e2aac9393902626663`
- Enumeration command: bounded `rg --files --hidden --no-ignore` plus exact-path `Test-Path` and direct reads
- Manifest artifact or inline manifest: Source Verification And Processing Ledger
- Manifest hash: N/A with reason: bounded inline manifest, no generated corpus artifact
- Processing ledger artifact or inline ledger: Source Verification And Processing Ledger
- Allowed terminal statuses: READ, SKIPPED_WITH_REASON, DEFERRED, BLOCKED_UNREADABLE
- Reconciliation: manifest=14; ledger_terminal=14; exclusions=full-repository-and-unrelated-corpus; unresolved=0
- Unresolved files: 0
- Declared exclusions: full repository, unrelated CVF surfaces, external repositories, provider/browser/MCP/public-sync inputs
- Unreadable or unsupported files: none
- Aggregation check: N/A with reason: no corpus aggregate produced
- Drift check: PASS: HEAD remained at the captured execution base during assessment authoring
- Output traceability: every decision claim maps to the named source/symbol ledger
- Adversarial verification: independent reviewer must recheck owner, legacy, rollback, and exact manifest
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## Knowledge System Reconciliation

- Knowledge task class: OTHER - bounded cross-owner contract decision
- Source manifest: fourteen-row inline ledger
- Source manifest hash: N/A with reason: bounded inline source ledger, no generated manifest artifact
- Enumeration safety: `rg --files --hidden --no-ignore` over bounded roots, exact-path `Test-Path`, direct reads, and targeted `rg -n`
- Intake registry or ledger: Source Verification And Processing Ledger
- Authority assets: approval binding/store/routes, pending core/SQLite, focused tests, and T1E governed evidence
- Derived views: four-family matrix, selected contract, future manifest, and reopen proof
- Semantic region ledger: inline mapping of approval identity, persistence, pending validation, and route compatibility owners
- Region reconciliation: assets=14; mapped=14; deferred=0; unmapped=0
- Orphan or unmapped assets: none
- Cross-region links: approval preimage -> persisted snapshot -> pending drift -> route mismatch/reissue
- Drift check: PASS
- Rebuildability check: PASS from named paths and commands
- Retrieval boundary: targeted current-owner evidence only
- Adversarial verification: independent reviewer rechecked builder, hash, persistence, pending claim, legacy and rollback consequences
- Knowledge-map verdict: RECONCILED_VERIFIED

## Finding-To-Governance Learning Disposition

Defect class: RUNTIME_SIGNAL_GAP

Learning lane: RUNTIME_BEHAVIOR_LEARNING

Disposition: DESIGN_REVIEW_REQUIRED

T1E already retained the first cross-owner runtime signal. T1F converts it into
an owner/compatibility contract; it adds no checker or broader governance rule.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private documentation decision; no accepted repair or public artifact.

## Claim Boundary

This assessment selects a bounded future correction contract only. It does not
repair source, accept T1E, migrate or issue records, add dual acceptance, change
route/provider/audit behavior, call an external service, synchronize public
artifacts, deploy, open production, or authorize an automatic successor.

## Independent Reviewer Addendum

Reviewer disposition: `REVIEWER_ACCEPTED_WITH_BOUNDED_DOCUMENTATION_REPAIR`.

Independent review confirmed the selected approval owner, ordinal schema
projection, omission/rejection boundary for `undefined`, no-dual-acceptance
policy, legacy 409/stale behavior, rollback reissue boundary and exact four-
path future manifest. Family A remains proportional because no production
pending caller or issued-record continuity requirement is present; any such
requirement stops implementation and reopens Family D.

Bounded repair completed the machine-required corpus/knowledge reconciliation
fields only. It does not change the selected terminal, correction semantics or
future manifest. No product source or test was edited or executed.
