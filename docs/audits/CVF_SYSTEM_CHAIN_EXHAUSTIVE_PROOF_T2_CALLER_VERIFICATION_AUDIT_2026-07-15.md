# CVF System Chain Exhaustive Proof T2 Caller Verification Audit

Memory class: FULL_RECORD

Status: COMPLETE_PENDING_REVIEW

docType: audit

Date: 2026-07-15

Responds to work order:
`docs/work_orders/CVF_AGENT_WORK_ORDER_SYSTEM_CHAIN_EXHAUSTIVE_E2E_PROOF_T2_CALLER_VERIFICATION_2026-07-15.md`

## Purpose

Human-readable companion to the machine JSON at
`docs/reference/system_chain/CVF_SYSTEM_CHAIN_EXHAUSTIVE_PROOF_T2_CALLER_VERIFICATION.json`.
Records the repository-wide, read-only caller-existence search performed for
the two accepted T1 targets - GC-009 (`MandatoryGateway` /
`createMandatoryGateway`) and GC-010 (`AgentExecutionRuntime`) - and both
terminal target decisions.

## Target / Source

Target is `SCLP-X-T2` at `executionBaseHead` `9e3a672e6`, a clean worktree
verified before any output file was created. Direct authority is the accepted
T1 value-selection JSON and completion review, the current guard-contract
runtime source files, and fresh repository-wide filesystem search evidence
gathered in this tranche.

## Hash Verification

Both accepted T1 inputs were recomputed independently with SHA-256 via
Python's `hashlib` before any search began.

| Input | Claimed | Actual | Char length | Result |
|---|---|---|---|---|
| T1 value-selection JSON | `ab7797912c35ff6a29173b956678f1af2ce47b8e69b5b2f8940713e1259863ae` | identical | 64 / 64 | MATCH |
| T1 completion review | `c429881283632af0f2ecb2f3b90ebd8c24bca423c3f4df3d0e53244ec1417a39` | identical | 64 / 64 | MATCH |

The work order flagged a possible transcription quirk carried over from the
same pattern the T1 worker hit against its own T0 inputs (a claimed hash
string that reads as one hex character longer than the standard length).
Independent recomputation here shows both strings are exactly 64 hex
characters (the standard SHA-256 length) and character-for-character
identical to the claimed values. No drift materialized. The hash-drift stop
condition did not trigger.

## Scope / Methodology

Scope is repository-wide, read-only caller-existence verification for exactly
two accepted T1 targets. No live, provider, browser, business CLI, runtime,
test, build, typecheck, or CI action occurred. The 11-step Required Search
Method from the work order was followed exactly.

1. **Filesystem enumeration.** `rg --files --hidden --no-ignore` excluding
   only `.git`, `node_modules` (including nested), `.next` (including
   nested), and `.cvf` (including nested), plus a check that no build-output
   directory (`dist`, `build`, `coverage` as a bare segment) exists outside
   those already-excluded trees. Result: **22026 files** enumerated. The
   sorted, forward-slash-normalized path list hashes to
   `47e2c963495f5a5c85b74d019736df38bc306b27b0d1334affe750fd9f973101`.
2. **Full collision scan**, five terms: `MandatoryGateway` (128 raw hits),
   `createMandatoryGateway` (48), `AgentExecutionRuntime` (127),
   `mandatory-gateway` (86), `agent-execution-runtime` (61).
3. **Constructor/factory-call scan**: `new\s+MandatoryGateway` (14),
   `createMandatoryGateway\(` (7), `new\s+AgentExecutionRuntime\s*\(` (8).
4. **Import / re-export / dynamic-import / module-path scans**, eight
   queries covering `from.*mandatory-gateway`, `require\(.*mandatory-gateway`,
   `import\(.*mandatory-gateway`, `export.*MandatoryGateway`, and the
   equivalent four for `agent-execution-runtime` / `AgentExecutionRuntime`.
   Combined raw hits: 21 (`require(` and dynamic `import(` forms returned
   zero for both targets).
5. Every unique path/line occurrence across all 16 queries was recorded as
   one terminal match-ledger row, including tests, generated coverage
   output, historical documents, and one private external evidence source -
   nothing was silently discarded.
6. Exact path/line overlaps across multiple queries were merged into a single
   row that retains every contributing query ID; two different lines in the
   same file were never collapsed into one row.
7. Both targets received exactly one `callerVerificationDisposition`.
8. Not applicable for either target: no non-test production caller was found
   for GC-009 or GC-010, so step 8's "found a caller" branch does not apply.
9. Both targets satisfy step 9: zero unresolved/ambiguous matches, so both
   received `ADD_GAP_ENTRY_PROPOSED`.
10. Not applicable: no indirect reference for either target remained
    unresolved after source reading, so `RETURN_TO_ORCHESTRATOR` was not
    needed for either target.
11. The GC-009 catalog edge (T1-DEC-03 in the accepted T1 JSON) was
    reverse-projected as evidence only inside this T2 output, per the work
    order's instruction; it is not treated as a third target.

## Findings / Position

Both accepted T1 input hashes matched exactly (64 hex characters, no drift).
The repository-wide search enumerated 22026 files, ran 16 queries for 500 raw
hits, and deduplicated to 329 unique path/line rows with zero
`AMBIGUOUS_REFERENCE` rows and zero `NON_TEST_PRODUCTION_CALL` rows for
either target. Both `MandatoryGateway`/`createMandatoryGateway` (GC-009) and
`AgentExecutionRuntime` (GC-010) are implemented, tested, and defined only
inside their own module; no non-test production caller exists anywhere in
the current repository. This position is corroborated by fresh package
surface evidence (both helpers omitted from `package.json` exports/files and
from the `src/index.ts` barrel) gathered directly in this tranche, and by
the independently-closed `MSEA-R94-T1B` gateway-helper-ownership tranche
reaching the same conclusion on 2026-07-11.

## Match Reconciliation Summary

| Metric | Value |
|---|---|
| Raw hits across all 16 queries | 500 |
| Unique (path, line) ledger rows after dedupe | 329 |
| Rows merged as exact query-overlap duplicates | 171 (every merged row retains all contributing query IDs) |
| Rows classified `AMBIGUOUS_REFERENCE` | 0 |
| Rows classified `NON_TEST_PRODUCTION_CALL` | 0 (for either target) |

### Match classification distribution (329 unique rows)

| `matchClassification` | Count |
|---|---|
| `HISTORICAL_DOCUMENT` | 265 |
| `TEST_ONLY` | 26 |
| `GENERATED_COVERAGE` | 22 |
| `PRIVATE_EXTERNAL_EVIDENCE` | 4 |
| `COMMENT_ONLY` | 4 |
| `TYPE_ONLY_IMPORT` | 2 |
| `DEFINITION` | 5 |
| `SELF_CONSTRUCTION` | 1 |
| `NON_TEST_PRODUCTION_CALL` | 0 |
| `AMBIGUOUS_REFERENCE` | 0 |

Sum check: 265+26+22+4+4+2+5+1 = 329, matching the unique row count exactly.

### Authority class distribution (329 unique rows)

| `authorityClass` | Count |
|---|---|
| `HISTORICAL_NON_AUTHORITY` | 265 |
| `TEST_SOURCE` | 26 |
| `GENERATED_NON_AUTHORITY` | 22 |
| `CURRENT_RUNTIME_SOURCE` | 12 |
| `PRIVATE_INPUT_NON_AUTHORITY` | 4 |

Sum check: 265+26+22+12+4 = 329, matching the unique row count exactly.

## Authority Classification Rationale

**Why 265 `HISTORICAL_DOCUMENT` rows are rejected as production callers.**
These rows span governance/audit/baseline/work-order/review/roadmap prose
under `docs/audits`, `docs/baselines`, `docs/work_orders`, `docs/reviews`,
`docs/roadmaps`, `docs/reference` (governance control matrix, architecture
catalog entries, system chain map and inventory JSON files), the corpus
intelligence registry, incremental test-run logs, and active session-state
routing files (`CVF_SESSION_MEMORY.md`, `CVF_SESSION/ACTIVE_SESSION_STATE.json`,
its bootstrap read model, and the `nextAllowedMove` state entry - all three of
which cite this exact T2 tranche's own dispatch prose). None of these files
are TypeScript/JavaScript runtime source; they describe, audit, or route work
about the two targets without constructing or invoking either class. Every
archived file (any path containing an `archive` segment) and every file
under `ECOSYSTEM/strategy/archive/` was classified the same way regardless of
original authorship date, because a document's prose claim about a class's
capability is not runtime invocation evidence.

One archived lineage deserves explicit note: three files under
`docs/reviews/cvf_phase_governance/archive/` dated 2026-03-10 through
2026-03-12 (an independent expert review, its postfix review, and an earlier
roadmap-fixes note) explicitly document that the `/api/execute` Web route
bypassed `AgentExecutionRuntime` entirely as of that date - the opposite
framing of the same gap this T2 search independently reconfirms today. This
is recorded as corroborating historical evidence in the JSON's
`additionalHistoricalCorroboration` field for GC-010. It was not used to
widen the search: `/api/execute`'s current wiring is outside the two named
symbol/module targets and the 16 authorized queries, so re-verifying it here
would have been scope expansion beyond the work order's Required Search
Method.

**Why 26 `TEST_ONLY` rows are rejected as production callers.** All 26 rows
are inside `.test.ts` files: `mandatory-gateway.test.ts` (10 rows, seven
distinct `new MandatoryGateway(...)` constructor calls plus import/describe
lines), `agent-execution-runtime.test.ts` (9 rows), and the two provider
test files `gemini-provider.test.ts` / `alibaba-dashscope-provider.test.ts`
(4 and 3 rows respectively, each importing and constructing
`AgentExecutionRuntime` directly for their own test scenarios). Every row
was individually read, not inferred from the `.test.ts` filename alone; each
one is a genuine test-scope import, `describe()` block, or constructor call
with no production entry point involved.

**Why 22 `GENERATED_COVERAGE` rows are rejected as production callers.**
These rows are Istanbul/Vitest coverage output - `coverage/clover.xml`,
`coverage/coverage-final.json`, and per-file `coverage/src/runtime/*.ts.html`
pages - that mirror the exact same source and test lines already counted
under `DEFINITION`, `SELF_CONSTRUCTION`, and `TEST_ONLY`. They are build
artifacts, not authored source, and are explicitly excluded from caller
authority per the corpus completeness standard's generated-output handling.

**Why 4 `PRIVATE_EXTERNAL_EVIDENCE` rows are rejected as production
callers.** All four rows are inside a single file,
`.private_reference/external_reviews/system_chain_gap_closure_2026-07-10/cvf_scout_report.json`
- a third-party AST declaration inventory that lists `MandatoryGateway` and
`AgentExecutionRuntime` as declared classes in their defining files. It is a
declaration listing produced by an external tool, not a repository-native
caller reference, and per the work order's Evidence Reuse plan private
external material is not source authority for a production-caller claim.

**Why 4 `COMMENT_ONLY` and 2 `TYPE_ONLY_IMPORT` rows are rejected as
production callers.** The two non-test provider source files
(`gemini-provider.ts`, `alibaba-dashscope-provider.ts`) each contain one
JSDoc comment mentioning `AgentExecutionRuntime` by name and one
`import type { ExecutionProvider } from '../agent-execution-runtime'`
statement - a TypeScript type-only import that is erased at compile time and
creates no runtime dependency edge, let alone a construction or invocation.
The remaining `COMMENT_ONLY` rows are the two target files' own internal
JSDoc module-path headers, not external callers.

**Why the 5 `DEFINITION` and 1 `SELF_CONSTRUCTION` rows do not establish a
caller.** These six rows are `MandatoryGateway` (class, line 66),
`createMandatoryGateway` (factory, line 219), and `AgentExecutionRuntime`
(class, line 130) declaring themselves; two same-module declaration-signature
type references at lines 185 and 222; plus `createMandatoryGateway`'s own
factory body constructing `new MandatoryGateway(engine, config)` at line 223.
A module defining and self-constructing its own export is the definitional
minimum every implemented class exhibits; it is not evidence of an external
caller.

## Fresh Corroborating Evidence Beyond Reuse

Two additional checks were performed directly in this tranche, not reused
from T1 or the earlier R94-T1B gateway-helper-ownership tranche:

- `EXTENSIONS/CVF_GUARD_CONTRACT/package.json` `exports` and `files` fields
  were read in full. Both fields explicitly list `runtime/agent-handoff` and
  `runtime/agent-coordination` as public package surfaces, but omit
  `runtime/mandatory-gateway` and `runtime/agent-execution-runtime` entirely.
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` (the package barrel) was
  grep-searched for both symbols and both module paths - zero matches. The
  barrel re-exports neither helper.

Both checks corroborate, with fresh independent evidence gathered at
`executionBaseHead` `9e3a672e6`, the same conclusion reached by the accepted
T1 record and by the earlier `MSEA-R94-T1B` gateway-helper-ownership tranche
(`docs/baselines/CVF_GC018_MSEA_R94_T1B_GATEWAY_HELPER_OWNERSHIP_DISPOSITION_2026-07-11.md`,
closed 2026-07-11): neither helper has an active production owner reachable
through the package's public surface.

## Target Decisions

### GC-009 - MandatoryGateway / createMandatoryGateway

- `callerVerificationDisposition`: `NO_NON_TEST_PRODUCTION_CALLER_FOUND`
- `architectureRecommendation`: `ADD_GAP_ENTRY_PROPOSED`

Zero rows classified `NON_TEST_PRODUCTION_CALL` and zero rows classified
`AMBIGUOUS_REFERENCE` among the 24 ledger rows tied to
`mandatory-gateway.ts`, `mandatory-gateway.test.ts`, and their generated
coverage mirror. The class is defined and self-constructed only inside its
own module; its only external construction sites are the ten test rows in
its co-located test file; the package surface and barrel omit it. This
satisfies the work order's zero-unresolved requirement for a no-caller
disposition. The proposal-only recommendation is a formal GC-009
no-non-test-production-caller architecture GAP entry for reviewer
consideration; this worker performs no owner or GAP mutation.

### GC-010 - AgentExecutionRuntime

- `callerVerificationDisposition`: `NO_NON_TEST_PRODUCTION_CALLER_FOUND`
- `architectureRecommendation`: `ADD_GAP_ENTRY_PROPOSED`

Zero rows classified `NON_TEST_PRODUCTION_CALL` and zero rows classified
`AMBIGUOUS_REFERENCE` among the 30 ledger rows tied to
`agent-execution-runtime.ts`, its test file, the two provider source/test
file pairs, and their generated coverage mirrors. The class is defined only
at its own declaration; every `new AgentExecutionRuntime(...)` construction
site is inside a `.test.ts` file; the two non-test provider files import
only the `ExecutionProvider` type, never the class. The package surface and
barrel omit this module identically to GC-009. This satisfies the
zero-unresolved requirement for a no-caller disposition. The proposal-only
recommendation is a formal GC-010 no-non-test-production-caller architecture
GAP entry for reviewer consideration, potentially grouped with GC-009 per
the accepted T1 record's `OWNER-GAP-01` framing; this worker performs no
owner or GAP mutation.

## GC-009 Catalog Edge Reverse Projection (Evidence Only)

Per work order step 11, the GC-009 result above is reverse-projected onto its
related T1 catalog-edge claim `T1-DEC-03`
(`cvf.asc.edge.gc009_gateway_no_caller.v1`) as evidence only. This is not a
third target - exactly two `targetDecisions` exist in the paired JSON. The
catalog entity's own claim boundary already self-limits it as sampled-only
and forbids treating it as full-matrix proof; this T2 evidence answers its
open question as a byproduct without changing that self-limitation, exactly
as `T1-DEC-01`'s recommended next action anticipated.

## Risk / Corrective Action

Reviewer repair corrected `ROW-0057` and `ROW-0059` from
`TYPE_ONLY_IMPORT` to `DEFINITION`. Both rows are same-module type references
inside class/factory declaration signatures, not import statements. The
classification distribution changed from 3/4 to 5/2 for
`DEFINITION`/`TYPE_ONLY_IMPORT`; the 329-row total, authority counts, raw query
counts, target decisions, and no-caller conclusion are unchanged.

No corrective action is required inside this tranche's scope: both targets
received a clean terminal disposition with zero unresolved rows, so no
repair to search method, classification, or hashing was needed. The residual
governance risk this audit surfaces is architectural, not evidentiary -
GC-009 and GC-010 remain `IMPLEMENTED_NOT_INVOCATION_PROVEN` in the current
repository, and this worker proposes (without authorizing) a formal GAP
entry for reviewer consideration rather than performing any owner or GAP
mutation itself.

## Stop Conditions Checked

| Stop condition | Result |
|---|---|
| Either accepted T1 hash drifts | NOT TRIGGERED |
| A file in the search universe is unreadable | NOT TRIGGERED |
| A target cannot receive a terminal disposition from source reading | NOT TRIGGERED |
| An indirect reference remains ambiguous | NOT TRIGGERED |
| A required correction would touch a fourth path | NOT TRIGGERED |

## Bounded Completeness Verdict

`corpusVerdict`: `COMPLETE_VERIFIED`. Manifest (22026 files) and terminal
ledger (329 unique rows, zero unresolved, zero `AMBIGUOUS_REFERENCE`)
reconcile with zero undeclared exclusions. `knowledgeMapVerdict`:
`RECONCILED_VERIFIED`. Both authority assets (the two T1-selected targets)
are mapped with zero deferred and zero unmapped.

## Claim Boundary

This audit and its paired JSON record only caller-EXISTENCE verification for
two named targets across a filesystem-backed repository-wide search. They do
not prove or claim runtime invocation, do not authorize any live, provider,
browser, business-CLI, runtime, test, build, typecheck, or CI action, do not
mutate any owner or GAP record, and do not promote a third target beyond the
two authorized by the accepted T1 record. Both `architectureRecommendation`
values are proposals for a separate reviewer/closer to consider, not
authorizations.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance caller-verification audit; no public-sync
authorization.
