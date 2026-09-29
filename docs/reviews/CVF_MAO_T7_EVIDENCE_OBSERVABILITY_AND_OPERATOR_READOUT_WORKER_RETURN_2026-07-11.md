# CVF MAO-T7 Evidence, Observability, And Operator Readout Worker Return

Memory class: FULL_RECORD

docType: review

Status: COMPLETE_PENDING_REVIEW

Date: 2026-07-11

Batch ID: MAO-T7

Self-declared worker-return artifact: yes

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_T7_EVIDENCE_OBSERVABILITY_AND_OPERATOR_READOUT_2026-07-11.md`

dispatchWorkOrder: `docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_T7_EVIDENCE_OBSERVABILITY_AND_OPERATOR_READOUT_2026-07-11.md`

dispatchBaseHead: `746d8e08c`

executionBaseHead: `3a56da449`

closureBaseHead: TO_BE_CAPTURED_BY_REVIEWER_AT_CLOSURE

Commit mode: WORKER_MUST_NOT_COMMIT

## Purpose

Return the MAO-T7 local secret-safe evidence/read-model contract: a
secret-safe evidence ledger keyed by the six contract receipt kinds, a
deterministic operator readout built by folding ledger records (mirroring
the MAO-T1 read-model discipline), a retention-window classifier bounded by
the contract's closure-evidence-window rule, a freshness classifier for
readout staleness, and a milestone-only workspace projection function that
excludes every invocation receipt. No provider call, network request,
queue, UI, commit, workspace/session state mutation, catalog-aggregate
admission, or MAO-T8+ work was performed.

## Target / Source

Target: one new execution-plane MAO module
(`evidence.readout.contract.ts`), one focused test file
(`mao.evidence.readout.contract.test.ts`), a bounded barrel extension
(`src/mao/index.ts`), one catalog-admission candidate packet, and this
worker return. Exactly five worker paths; no commit.

Source authority: paired work order
(`docs/work_orders/CVF_AGENT_WORK_ORDER_MAO_T7_EVIDENCE_OBSERVABILITY_AND_OPERATOR_READOUT_2026-07-11.md`),
the MAO-T0 runtime foundation contract's Evidence And Receipt Model and
Storage And Retention Decision sections, and
`docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_STATE_TOPOLOGY_CONTRACT.md`.
Current MAO-T1 `read.model.contract.ts` (for the deterministic-readout
pattern) and MAO-T5 `closer.interlock.contract.ts` (for the receipt-builder
pattern) were re-read fresh at this execution base.

## Scope / Methodology

Read the mandatory startup sequence, the work order, the MAO-T0 contract's
evidence/storage/retention sections, and the workspace topology contract.
Verified MAO-T1 through T6 are accepted (work order dependency release
evidence). Implemented one module (secret-safe redaction, evidence ledger,
deterministic readout, retention policy, freshness policy, milestone-only
workspace projection), one test file, one barrel extension, and one catalog
candidate packet. Ran TypeScript typecheck (PASS), focused Vitest (34/34
PASS), the governed file size guard (COMPLIANT), and `git diff --check`
(PASS with one harmless CRLF advisory).

## Exact Changed Set

4 code/candidate paths (plus this return, not yet written):

```
M  EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts
?? EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts
?? EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.evidence.readout.contract.test.ts
?? docs/reviews/CVF_MAO_T7_EVIDENCE_OBSERVABILITY_AND_OPERATOR_READOUT_CATALOG_CANDIDATE_2026-07-11.md
```

Plus this worker return at:
`docs/reviews/CVF_MAO_T7_EVIDENCE_OBSERVABILITY_AND_OPERATOR_READOUT_WORKER_RETURN_2026-07-11.md`

## Verification Commands And Results

### TypeScript typecheck

Command: `npx tsc -p tsconfig.json --noEmit`

Result: PASS (no errors, clean exit).

### Focused test execution

Command: `npx vitest run --config vitest.config.ts tests/mao.evidence.readout.contract.test.ts`

Result: PASS. 34/34 tests pass across 8 describe blocks (10ms test
duration). No Vitest/Node incompatibility was observed in this execution
environment for this run.

### Governed file size guard

Command: `python governance/compat/check_governed_file_size.py`

Result: COMPLIANT (0 violations; new T7 files do not appear in the
advisory list; 7723 governed files checked).

### Git diff whitespace check

Command: `git diff --check`

Result: PASS. Only a harmless LF/CRLF advisory for `index.ts` (same class
of advisory recorded in the MAO-T6 worker return).

## Test Coverage

The test file (`mao.evidence.readout.contract.test.ts`, 383 lines, 8
describe blocks, 34 cases) covers:

### redactFields
- Drops known secret-shaped field names, keeps safe fields
- Case- and separator-insensitive secret field name matching
- All-safe field map returns empty redaction
- All-secret field map redacts everything

### MaoEvidenceLedger.ingest
- Rejects empty taskGraphId
- Rejects empty recordedAt
- Stores a redacted record; redacted value never persists in the ledger
- Strictly increasing sequence numbers across ingests
- Deterministic evidenceId/receiptContentHash for identical inputs
- getRecords returns a frozen defensive copy

### buildEvidenceReadout
- Zeroed counts and null pointers for an empty ledger
- Per-kind counts and redacted-field totals across mixed ingests
- lastEvidenceId/lastRecordedAt reflect highest-sequence record
- Every declared receipt kind appears in receiptCountByKind, even at zero

### readoutsAreEqual (deterministic replay)
- Two readouts from the same ledger at different times are equal ignoring generatedAt
- Readouts differ when totalReceipts differ
- Readouts differ when taskGraphId differs

### evaluateRetention
- Always RETAIN while batch is open (batchClosedAt null)
- RETAIN_WITHIN_CLOSURE_WINDOW inside the window
- ELIGIBLE_FOR_EXPIRY strictly after the window
- Inclusive boundary retains (exactly at window edge)

### classifyReadoutFreshness
- NO_EVIDENCE_YET for an empty ledger
- CURRENT within the staleness ceiling
- STALE beyond the staleness ceiling

### milestoneForReceiptKind / projectWorkspaceMilestones
- GRAPH -> GRAPH_CREATED, ROLE_RESOLUTION -> TASK_ADMITTED, INTEGRATION -> CLOSURE
- INVOCATION never maps to any milestone (no per-heartbeat mirroring)
- OUTPUT/REVIEW map to TERMINAL_OUTCOME only when flagged terminal
- Projection excludes every INVOCATION receipt
- Projection preserves ledger sequence order across mixed kinds
- Empty ledger yields empty projection

### End-to-end scenario
- Full six-receipt-kind sequence ingested, readout built, freshness
  classified both CURRENT and STALE against different ceilings, milestone
  projection yields exactly GRAPH_CREATED/TASK_ADMITTED/TERMINAL_OUTCOME/
  CLOSURE (INVOCATION excluded), and post-closure retention evaluates
  RETAIN_WITHIN_CLOSURE_WINDOW

## Source Inventory

| File | Lines | Purpose |
|---|---|---|
| `src/mao/evidence.readout.contract.ts` | 465 | Secret-safe redaction, evidence ledger, deterministic readout, retention policy, freshness policy, milestone-only workspace projection |
| `tests/mao.evidence.readout.contract.test.ts` | 383 | Focused tests across 8 describe blocks, 34 cases |
| `src/mao/index.ts` | +30 lines | Bounded barrel exports for T7 module |
| `docs/reviews/CVF_MAO_T7_EVIDENCE_OBSERVABILITY_AND_OPERATOR_READOUT_CATALOG_CANDIDATE_2026-07-11.md` | new | Catalog-admission candidate evidence packet |

## Delta Boundary

Only the four named worker paths (plus this return) were created or
modified. No provider/network call, real wall-clock, queue, UI, durable
store, workspace/session state, public-sync, root barrel, checker/hook,
roadmap, git mutation, catalog-aggregate admission, MAO-T8+, commit, push,
or live proof was performed.

## Findings / Position

### Finding 1: No pre-existing infrastructure incompatibility observed in this run

Prior MAO-T4/T5/T6 worker returns recorded a Vitest 1.6.1 / Node v22.17.0
incompatibility that blocked focused test execution. This execution
observed 34/34 tests pass cleanly. No repair was needed for this finding;
it is recorded so the reviewer can compare execution environments across
tranches rather than assume the prior blocker still applies.

Learning lane: GOVERNANCE_CONTROL_PLANE
Defect class: N/A_WITH_REASON
Repair owner: N/A with reason: no defect found in this run

### Finding 2: GC-051 corpus scan registry coverage gap

Reviewer-owned per work order's Reviewer Closure Conversion section, same
pattern as MAO-T6.

Learning lane: GOVERNANCE_CONTROL_PLANE
Defect class: ORCHESTRATOR_PACKET_GAP
Repair owner: reviewer

## Closure Diff Gate

| Requirement | Handling | Status |
|---|---|---|
| Secret-safe evidence ledger keyed by six receipt kinds | `MaoEvidenceLedger.ingest` with `redactFields` denylist applied before storage | IMPLEMENTED |
| Deterministic operator readout, regenerated from ledger | `buildEvidenceReadout` pure fold; `readoutsAreEqual` proves replay equality | IMPLEMENTED |
| Retention bounded by closure evidence window | `evaluateRetention`: RETAIN while open, RETAIN_WITHIN_CLOSURE_WINDOW, ELIGIBLE_FOR_EXPIRY | IMPLEMENTED |
| Freshness drift detection | `classifyReadoutFreshness`: CURRENT/STALE/NO_EVIDENCE_YET | IMPLEMENTED |
| Workspace projection is milestones only, no per-heartbeat mirroring | `milestoneForReceiptKind`/`projectWorkspaceMilestones`: INVOCATION never projected | IMPLEMENTED |
| Catalog-admission candidate packet | `docs/reviews/CVF_MAO_T7_EVIDENCE_OBSERVABILITY_AND_OPERATOR_READOUT_CATALOG_CANDIDATE_2026-07-11.md` | IMPLEMENTED |
| Focused tests and typecheck pass | tsc clean; 34/34 Vitest pass | IMPLEMENTED |
| Exactly five paths, no commit | 4 code/candidate + 1 return, uncommitted | CONFIRMED |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`multi-agent orchestration runtime`,
role=`worker`, lifecyclePhase=`implementation`

Returned defects: NONE_RETURNED

## Finding-To-Governance Learning Disposition

| Defect | Defect class | Learning lane | Disposition | Next control action |
|---|---|---|---|---|
| GC-051 closure metadata | ORCHESTRATOR_PACKET_GAP | DOCUMENTATION_ONLY_LEARNING; runtime learning lane N/A with reason: metadata only | RULE_EXISTS | reviewer adds entry |

## Acceptance Receipt Assertion Matrix

| Assertion | Evidence |
|---|---|
| Redaction never leaks secret-shaped field values | `redactFields`/`ingest` tests: redacted values absent from `JSON.stringify(ledger.getRecords())` |
| Readout is deterministic and replay-stable | `readoutsAreEqual` tests across different `generatedAt` values |
| Retention never releases evidence before batch closure | `evaluateRetention` RETAIN-while-open test |
| Freshness correctly classifies stale vs current readouts | boundary tests at and beyond `staleAfterMs` |
| Workspace projection excludes every invocation receipt | `projectWorkspaceMilestones` INVOCATION-exclusion test |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | local MAO-T7 evidence/read-model contract, tests, and catalog candidate |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: local pure functions only |
| actionEvidence | ACTION_EVIDENCE_PRESENT: 34/34 tests and typecheck PASS |
| invocationBoundary | local in-memory ledger only |
| interceptionBoundary | no real clock, provider, network, or workspace file interception |
| claimLanguage | tested evidence/observability mechanics only |
| forbiddenExpansion | real provider, durable runtime store, workspace file write, public, UI, catalog-aggregate admission, MAO-T8+ |

## Risk / Corrective Action

No repair was required during this execution; typecheck and focused tests
passed on first run after two test-file `readonly string[]` spread fixes
(`result.redactedFields.sort()` -> `[...result.redactedFields].sort()`)
needed to satisfy the readonly-array typecheck. Risk for reviewer attention:
the redaction denylist (`ALWAYS_REDACTED_FIELD_NAMES`) is a fixed set, not a
heuristic scanner; callers must exclude any secret-shaped field the denylist
does not enumerate before calling `ingest`, since this module has no
visibility into runtime secret material beyond the field names it is given.

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | `REQUIRED_HEADINGS`, `SELF_DECLARE_MARKER`, `RESPONDS_MARKER`, `AOT_FIELDS`, `DELTA_FIELDS`, `PUBLIC_EXPORT_TOKENS`, `DELTA_RECEIPT_TOKENS`, `DELTA_ACTION_TOKENS`; review-docType structural heading groups |
| gateRunPurpose | reviewer confirmation |
| claimBoundary | local T7 evidence only |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | worker |
| Provider or surface | private workspace |
| Session or invocation | MAO-T7 evidence/observability worker execution 2026-07-11 |
| Working directory | repository root/package |
| Command or tool surface | file writes, Vitest, tsc, governance gates |
| Target paths | four worker outputs plus this return |
| Allowed scope source | MAO-T7 work order |
| Before status evidence | clean execution HEAD `3a56da449` |
| After status evidence | 34/34 tests and typecheck PASS |
| Diff evidence | `git diff --name-status` |
| Approval boundary | T7 only |
| Claim boundary | deterministic local evidence/read-model mechanics only |
| Agent type | worker |
| Invocation ID | `mao-t7-evidence-observability-worker-2026-07-11` |
| Expected manifest | five worker paths (four code/candidate plus this return) |
| Actual changed set | same |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## External Knowledge Intake Routing

| Field | Disposition |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | NOT_APPLICABLE_WITH_REASON: no external input |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | reviewer/closer |
| Disposition | no absorption |
| Claim boundary | CVF source only |

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- N/A with reason: no rescan/intake.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no corpus completeness claim.

## Epistemic Process Block

### Expected Result / Prediction

Focused tests would run locally and demonstrate deterministic replay,
secret-safe redaction, and correct milestone-only projection boundaries.

### Evidence Comparison

Predicted deterministic replay was confirmed: `readoutsAreEqual` passed for
readouts built from the same ledger at two different `generatedAt` values.
Predicted redaction safety was confirmed: no secret-shaped value appeared in
`JSON.stringify(ledger.getRecords())` after ingesting a field containing a
secret-shaped key.

### Contradiction Or Gap Disposition

No contradiction between prediction and observed test results. 34/34 tests
passed on the second run after the two readonly-array typecheck fixes noted
in Risk / Corrective Action.

### Claim Update

Bounded local T7 evidence/observability mechanics are reviewable.

## git status --short

```
 M EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/index.ts
?? EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/evidence.readout.contract.ts
?? EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/tests/mao.evidence.readout.contract.test.ts
?? docs/reviews/CVF_MAO_T7_EVIDENCE_OBSERVABILITY_AND_OPERATOR_READOUT_CATALOG_CANDIDATE_2026-07-11.md
?? docs/reviews/CVF_MAO_T7_EVIDENCE_OBSERVABILITY_AND_OPERATOR_READOUT_WORKER_RETURN_2026-07-11.md
```

## Changed Files

Exactly five worker paths listed above; reviewer adds GC-051 coverage/review
and catalog-admission disposition.

## Command Evidence

- Focused Vitest 34/34 PASS.
- Typecheck PASS.
- Governed file size guard COMPLIANT (0 violations).
- `git diff --check` PASS (one harmless CRLF advisory on `index.ts`).
- Worker-return fast gate: ran twice. First run surfaced four repairable
  gaps (elided-path authority citation, missing catalog-candidate Agent
  Operation Trace Block, missing catalog-candidate Epistemic Process Block,
  GC-051 registry coverage for the new test file). Worker repaired the
  first three (allowed-scope checker defects). Second run: 60/61 checks
  pass; the sole remaining failure is GC-051 registry coverage, which the
  work order's Reviewer Closure Conversion block assigns to
  `reviewerOwnedClosurePaths: packet, review, registry/catalog coverage`
  (same disposition as the MAO-T6 worker return's Finding 2).

WORKER_EXPERIENCE_RETRO:

- frictionLevel: LOW
- frictionType: GATE_SURPRISE
- observedStep: worker-return fast gate first run (elided-path authority
  citation; catalog-candidate Trace/Epistemic sections)
- preventiveControlCandidate: CHECKER

## No-Commit Statement

WORKER_MUST_NOT_COMMIT honored. Reviewer owns closure commit.

## Claim Boundary

This return claims deterministic local evidence-ledger, read-model,
retention, freshness, and milestone-projection mechanics only. It does not
prove runtime behavior under real provider integration, production
orchestration readiness, catalog-aggregate admission, or workspace runtime
write behavior. Reviewer verification is required before any of those
claims may be made.
