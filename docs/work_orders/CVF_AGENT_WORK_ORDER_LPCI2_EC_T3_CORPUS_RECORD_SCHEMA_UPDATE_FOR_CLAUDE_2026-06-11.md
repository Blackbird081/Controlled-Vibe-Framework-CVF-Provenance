# CVF Agent Work Order: LPCI2 EC-T3 Corpus Record Schema Update

docType: work_order

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

dispatchBaseHead: `b357b519`

executionBaseHead: `9b3bc72c`

closureBaseHead: `a895dc03`

Commit mode: `WORKER_MUST_NOT_COMMIT`

completionReviewPath: `docs/reviews/CVF_LPCI2_EC_T3_CORPUS_RECORD_SCHEMA_UPDATE_COMPLETION_2026-06-11.md`

reviewerOwnedClosurePaths:

- `docs/reviews/CVF_LPCI2_EC_T3_CORPUS_RECORD_SCHEMA_UPDATE_COMPLETION_2026-06-11.md`
- `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V17_2026-06-07.md`

Date: 2026-06-11

Assigned to: Claude (WORKER_MUST_NOT_COMMIT)

---

## Purpose

Deliver a TypeScript-only schema update that adds the EC-02 lifecycle fields
(`DocumentStatus` type alias, `documentStatus`, `promulgationDate`) to the
corpus record interfaces in `types.ts`, and adds `supportsDocumentStatus` to
`DscpDomainProfile`. Adds unit tests. Produces two source files + one test
update as uncommitted artifacts.

EC-T3 does NOT change runtime gate logic, DSCP profile JSON values, corpus
data files, or any public-facing contract. WORKER_MUST_NOT_COMMIT.

---

## Authority Chain

- GC-018: `docs/baselines/CVF_GC018_LPCI2_EC_T3_CORPUS_RECORD_SCHEMA_UPDATE_2026-06-11.md`
  Status: CLOSED_PASS_BOUNDED
- EC-T2 closure: `docs/baselines/CVF_GC018_LPCI2_EC_T2_CONTRACT_AMENDMENT_AND_MACHINE_SEMANTICS_2026-06-11.md`
  Status: CLOSED_PASS_BOUNDED commit `cb026168`
- EC-T1 GC-018 decisions D-01 through D-04:
  `docs/baselines/CVF_GC018_LPCI2_EC_T1_REGULATORY_DATE_MODEL_GOVERNANCE_DECISION_2026-06-11.md`
  commit `5e184d00`
- Roadmap:
  `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md`
  Part B, EC-T3 row

---

## Agent Roles

| Role | Agent | Constraint |
| --- | --- | --- |
| Worker | Claude | WORKER_MUST_NOT_COMMIT; creates and stages artifacts only |
| Reviewer | Codex | Reviews staged artifacts; runs pre-closure gate; commits if PASS |
| Closer | Codex | Updates GC-018 and work order Status to CLOSED_PASS_BOUNDED |

---

## Pre-Flight Checks

Before starting implementation, worker must confirm:

1. GC-018 `Status` has been set to `DISPATCHED` by Codex.
2. `dispatchBaseHead` matches current `git rev-parse HEAD` (or worker notes
   any HEAD drift and confirms scope is unaffected).
3. Files listed in Write Ownership section exist at expected paths.
4. No in-flight edits exist on the write-owned files.

If any pre-flight check fails, worker must stop and notify Codex.

---

## Required First Reads

Before starting implementation, worker must read:

1. `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts`
   -- current `LpciIndexRecord`, `ManifestEntry`, `IntakeRecord`, `RecordStatus`
2. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts`
   -- current `DscpDomainProfile` interface
3. `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.contract.test.ts`
   -- company-docs fixture at line 70 (collision check)
4. Existing unit tests for `types.ts` (glob for `lpci/*.test.ts`)
5. `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json`
   -- canonical `documentStatusEnum` values

---

## Write Ownership

Worker owns writes to:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts`
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts`
- Tests: one of `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/*.test.ts`
  or a new `types.ec02.test.ts` -- worker must check existing test files first.
- `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.contract.test.ts`
  ONLY if the `supportsDocumentStatus` addition breaks the existing company-docs
  fixture tests.

All other files are read-only. No corpus JSON data files. No DSCP profile JSON
files. No checker files. No public-sync.

---

## Source Verification Table

| Symbol / path | File | Verified line |
| --- | --- | --- |
| `LpciIndexRecord` interface | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/lpci/types.ts` | line 29 |
| `effectiveDate?: string` (LpciIndexRecord) | same | line 36 |
| `status: RecordStatus` (LpciIndexRecord) | same | line 37 |
| `RecordStatus` type | same | lines 9-16 |
| `ManifestEntry` interface | same | line 106 |
| `effectiveDate?: string` (ManifestEntry) | same | line 113 |
| `IntakeRecord extends LpciIndexRecord` | same | line 124 |
| `DscpDomainProfile` | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.domain.profile.contract.ts` | line 23 |
| `domainFacetFields: Record<string, string>` | same | line 38 |
| `boundaryRules: Record<string, string>` | same | line 46 |
| `supportsDocumentStatus` -- ABSENT | grep above file | ABSENT (new field) |
| `promulgationDate` -- ABSENT in types.ts | grep types.ts | ABSENT (new field) |
| `DocumentStatus` type alias -- ABSENT | grep types.ts | ABSENT (new export) |
| company-docs fixture collision | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.domain.profile.contract.test.ts` | line 70 |
| EC-02 enum values | `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | `documentStatusEnum` field |

---

## Execution Plan

### Step 1: Add `DocumentStatus` type alias to `types.ts`

Insert near `RecordStatus` (line 9-16):

```typescript
export type DocumentStatus = 'PROMULGATED' | 'IN_FORCE' | 'STATUS_UNKNOWN';
```

### Step 2: Add EC-02 fields to `LpciIndexRecord`

In `LpciIndexRecord` (after line 36, `effectiveDate?: string`), add:

```typescript
promulgationDate?: string;
documentStatus?: DocumentStatus;
```

### Step 3: Add EC-02 fields to `ManifestEntry`

In `ManifestEntry` (after line 113, `effectiveDate?: string`), add:

```typescript
promulgationDate?: string;
documentStatus?: DocumentStatus;
```

Note: `IntakeRecord` at line 124 `extends LpciIndexRecord` -- it inherits
`promulgationDate` and `documentStatus` automatically. No change needed.

### Step 4: Add `supportsDocumentStatus` to `DscpDomainProfile`

In `DscpDomainProfile` interface (after `boundaryRules` line 46), add:

```typescript
supportsDocumentStatus?: boolean;
```

### Step 5: Run existing tests, check for regressions

Run: `cd EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web && npm run test:run`
Run: `cd EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION && npm run check`

If the company-docs test fixture at line 70 fails, first confirm the failure is
caused by EC-T3. `supportsDocumentStatus` must be optional in EC-T3; absent or
undefined is the default false posture for later EC-T5 runtime work. Add
`supportsDocumentStatus: false` to the company-docs profile object only if a
focused test needs explicit fixture coverage.

### Step 6: Add unit tests

Add a test file `types.ec02.test.ts` (or append to an existing types test)
covering:

- `DocumentStatus` type accepts `'PROMULGATED'`, `'IN_FORCE'`, `'STATUS_UNKNOWN'`
  and no other value (TypeScript compile check via `satisfies` or const).
- `LpciIndexRecord` with `documentStatus: 'PROMULGATED'` is valid.
- `LpciIndexRecord` with `documentStatus: 'IN_FORCE'` AND a non-null
  `effectiveDate` is valid.
- Invariant test name: `'documentStatus IN_FORCE requires operator-supplied effectiveDate (migration rule EC-T3)'` --
  document the invariant without claiming runtime enforcement. EC-T3 must not
  claim that optional TypeScript fields enforce the date rule.
- `supportsDocumentStatus: true` on a mock `DscpDomainProfile` is accepted.
- `supportsDocumentStatus: false` on a mock `DscpDomainProfile` is accepted.
- `DscpDomainProfile` without `supportsDocumentStatus` (undefined) is also accepted
  (the field is optional).

### Step 7: Stage all changed files

`git add` the changed files (do NOT commit).

---

## Negative Search And Collision Discipline

Verified at baseHead `b357b519`:

| Token | Disposition |
| --- | --- |
| `DocumentStatus` | ABSENT as type export in EXTENSIONS. One string occurrence in company-docs test fixture at line 70 as `domainFacetFields` key -- different semantic context; no type-level collision. New export is a TypeScript type alias only. |
| `promulgationDate` | ABSENT from all EXTENSIONS source files. Non-authoritative occurrence in planning/baseline docs only. |
| `supportsDocumentStatus` | ABSENT from all EXTENSIONS source files. New field. |

Machine-gate failures inside this work order's scope must be resolved before
returning the packet to Codex. If a failure is outside this work order's scope
(e.g., a pre-existing test failure unrelated to EC-T3), worker must surface it
as a finding and NOT attempt to fix it unilaterally.

---

## Evidence Requirements

Worker packet must include:

1. Diff summary: which lines added/changed in each file.
2. Test results: `npm run test:run` output (or failure detail if any test
   fails that is NOT pre-existing).
3. Type check result: `npm run check` in `CVF_CONTROL_PLANE_FOUNDATION` (or
   equivalent `npx tsc --noEmit`).
4. Confirmation that `RecordStatus` type and `status` field are unchanged.
5. Confirmation that no corpus JSON data files were changed.
6. Confirmation that no DSCP profile JSON values were changed.
7. Line counts for modified files.

---

## Acceptance Criteria

1. `DocumentStatus` type alias exported from `types.ts`:
   `'PROMULGATED' | 'IN_FORCE' | 'STATUS_UNKNOWN'`
2. `documentStatus?: DocumentStatus` and `promulgationDate?: string` present
   in `LpciIndexRecord` and `ManifestEntry`.
3. `supportsDocumentStatus?: boolean` present in `DscpDomainProfile`.
4. All existing tests pass. New tests cover new fields (at minimum: valid
   type acceptance tests + migration invariant name). The migration invariant
   is documentation/test evidence only until EC-T5 runtime enforcement.
5. `RecordStatus` and `status` field are unchanged.
6. No corpus JSON data files changed.
7. No DSCP profile JSON values changed.
8. GC-023 file size limits respected (check line counts before staging):
   - `types.ts` current 133L -- addition of ~5L is within safe range.
   - `dscp.domain.profile.contract.ts` -- worker must check current line
     count; addition of ~2L expected to be within limits.
9. Reviewer-fast PASS:
   `python governance/compat/run_local_governance_hook_chain.py --hook reviewer-fast --serial`
10. Pre-closure autorun gate PASS:
    `python governance/compat/run_agent_autorun_workflow_gate.py --phase pre-closure --base b357b519 --head HEAD`

---

## Review Gate

Codex reviewer must:

1. Confirm all acceptance criteria met.
2. Run pre-closure autorun gate.
3. Run reviewer-fast.
4. Confirm no out-of-scope changes (corpus data, DSCP profiles, gate logic).
5. Update GC-018 Status from PROPOSED to DISPATCHED before dispatch; from
   DISPATCHED to CLOSED_PASS_BOUNDED after review passes.
6. Commit with a message referencing EC-T3 closure.

---

## Closure Checklist

- [x] `DocumentStatus` type alias exported from `types.ts`
- [x] `documentStatus?` and `promulgationDate?` added to `LpciIndexRecord`
- [x] `documentStatus?` and `promulgationDate?` added to `ManifestEntry`
- [x] `supportsDocumentStatus?` added to `DscpDomainProfile`
- [x] New unit tests added and passing
- [x] `RecordStatus` and `status` field unchanged
- [x] No corpus data or DSCP profile JSON changes
- [x] Reviewer-fast PASS
- [x] Pre-closure autorun gate PASS except expected active-session sync after material commit
- [x] GC-018 Status updated to CLOSED_PASS_BOUNDED
- [x] Roadmap EC-T3 row updated to CLOSED_PASS_BOUNDED

---

## Return-To-Orchestrator Conditions

Worker returns uncommitted packet to Codex when:

- All source file edits are complete and staged.
- `npm run test:run` completes (PASS or documented FAIL with pre-existing
  status confirmed).
- Type check completes (PASS or documented FAIL with scope assessment).
- Evidence requirements above are satisfied.

Worker must NOT return early with partial edits. Worker must NOT commit.

---

## Operator Checkpoint

No operator checkpoint required before EC-T3 execution. However:

- If any test failure is found that is ambiguous in scope (may or may not
  be pre-existing), worker must surface it and STOP -- do not attempt to
  fix out-of-scope failures.
- If `supportsDocumentStatus` being optional vs required creates ambiguity
  in the company-docs fixture, worker must surface both options and default
  to `optional` (i.e., `supportsDocumentStatus?: boolean`) unless the fixture
  break is clearly attributable to EC-T3.

---

## Claim Boundary

This work order authorizes TypeScript type additions only. Completion of EC-T3
does not claim runtime gate correctness, legal correctness, retrieval quality,
EC-02 enforcement efficacy, production readiness, or any guarantee beyond
the schema change itself.

EC-02 hard boundary 2026-07-01 remains in force after EC-T3 closes. No record
may carry `documentStatus: 'IN_FORCE'` before 2026-07-01.

---

## Machine Closure Package

This work order is closed as `CLOSED_PASS_BOUNDED`. Registry JSON and Registry
Markdown remain unchanged because EC-T3 scope is TypeScript type additions only.

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | `docs/work_orders/CVF_AGENT_WORK_ORDER_LPCI2_EC_T3_CORPUS_RECORD_SCHEMA_UPDATE_FOR_CLAUDE_2026-06-11.md` | Status field set to CLOSED_PASS_BOUNDED by Codex at closure | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_LPCI2_EC_T3_CORPUS_RECORD_SCHEMA_UPDATE_COMPLETION_2026-06-11.md` | File existence + PASS disposition line | PASS |
| Roadmap state | `docs/roadmaps/CVF_LPCI2_EXTRACTION_AND_EC02_REFINEMENT_ROADMAP_2026-06-10.md` | Part B EC-T3 row updated to CLOSED_PASS_BOUNDED | PASS |
| Registry JSON | `docs/reference/CVF_EC02_GATE_SEMANTICS_2026-06-11.json` | Schema version field present; file at commit `cb026168` | PASS |
| Registry Markdown | `docs/reference/CVF_LPCI_RESPONSE_BOUNDARY_ENFORCEMENT_CONTRACT_2026-06-11.md` | contractVersion field; file at commit `cb026168` | PASS |
| External evidence digest | N/A with reason -- EC-T3 is TypeScript type additions only; no external corpus, provider, or non-git artifact is consumed | No external path artifacts in scope | N/A with reason |
| System loop interlock | GC-052 system loop interlock: no looping worker pattern in this work order; Claude executes once and returns | Single-pass execution pattern; no loop | N/A with reason |
| Session continuity | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | nextAllowedMove updated after EC-T3 closure; handoff sync follows closure commit | PASS |

---

## Roadmap-To-Work-Order Trace Matrix

| Roadmap row | This WO section |
| --- | --- |
| EC-T3: Corpus record schema update | Execution Plan Steps 1-7 |
| D-01 documentStatus name ACCEPTED | Step 1: `DocumentStatus` type alias |
| D-03 non-regulatory omit + supportsDocumentStatus | Step 4 |
| D-04 boundary unchanged | Acceptance Criteria item 7 + Forbidden Scope |

---

## Intake Role Routing Decision

Intake summary: operator requested EC-T3 continuation after EC-T2 closure,
bounded to corpus record schema update for EC-02 lifecycle fields.

Scope classification: TypeScript schema and focused test update only; no corpus
data migration, runtime gate logic, public-sync, provider/live proof, secrets,
or production/readiness claim.

Risk sensitivity: legal/current-law sensitive concepts are present, but EC-T3
does not resolve legal status, actual dates, jurisdiction, or current-law
truth. EC-02 hard boundary through 2026-07-01 remains active. No API keys,
public repository, or live provider route are in scope.

Selected route mode: `MULTI_AGENT_MULTI_ROLE`.

Selected role route: Claude acts as no-commit worker; Codex acts as
orchestrator/reviewer/closer after worker return.

Role separation basis: source edits are delegated to a worker under
`WORKER_MUST_NOT_COMMIT`; Codex independently checks staged artifacts, gates,
scope boundary, and closure evidence before any commit.

Escalation condition: stop and return to Codex if implementation requires
runtime gate logic, corpus JSON data migration, DSCP profile JSON value changes,
public-sync, provider/API-key use, legal/current-law assertion, line-count
threshold remediation outside owned files, or ambiguous pre-existing test
failures.

---

## Reviewer Closure Conversion Block

When Codex confirms PASS:

1. Edit GC-018 `Status: DISPATCHED` -> `Status: CLOSED_PASS_BOUNDED`
2. Edit this work order `Status: DISPATCHED` -> `Status: CLOSED_PASS_BOUNDED`
3. Update roadmap Part B EC-T3 row status.
4. Commit all three changes together with the source artifacts.

---

## Worker Autonomy / No-Question Rule

Worker proceeds without asking questions if:

- The task is within the written scope above.
- The type fields are optional (default).
- The company-docs fixture fix is needed and is bounded to adding
  `supportsDocumentStatus: false` to one test object.

Worker STOPS and returns to Codex if:

- A pre-existing test failure of unknown scope is encountered.
- Any step requires changing DSCP profile JSON values, corpus data files,
  or runtime gate logic.
- Line count of any modified file would exceed its GC-023 hard limit.
