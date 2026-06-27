# CVF Agent Work Order: DSCP-T6 Scan Descriptor Runtime

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-06-08

Worker: Claude

Reviewer: Codex

Commit mode: WORKER_MUST_NOT_COMMIT

dispatchBaseHead: `10b02a79`

executionBaseHead: `10b02a79`

closureBaseHead: `8a01da2b`

---

## Purpose

Dispatch Claude to implement `buildGovernedArtifactDescriptor()` — the
scan-side builder for the DSCP governed pipeline — inside
`CVF_CONTROL_PLANE_FOUNDATION`. This completes the scan → pack → receipt
cycle started in DSCP-T3 and DSCP-T4.

## Authority Chain

Operator instruction 2026-06-08 → GC-018:
`docs/baselines/CVF_GC018_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_2026-06-08.md`
→ this work order.

Predecessor: DSCP-T5 `CLOSED_PASS_BOUNDED` at `1f140042`.

## Agent Roles

| Role | Agent | Responsibility |
|---|---|---|
| Worker | Claude | Implement runtime + tests; author worker return; stage artifacts |
| Reviewer | Codex | Review worker return; run governance gates; commit if PASS |
| Operator | Human | Authorized T6 dispatch; owns session sync and registry updates |

## Scope / Target / Owner Boundary

**Allowed scope:**
- Create `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts`
- Create `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.artifact.descriptor.test.ts`
- Create `docs/reviews/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_WORKER_RETURN_2026-06-08.md`
- Reviewer closure update to `docs/reviews/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_COMPLETION_2026-06-08.md`
- Reviewer closure update to `docs/roadmaps/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_ROADMAP_2026-06-08.md`
- Reviewer closure update to `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md`
- Reviewer closure sync to `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Reviewer closure sync to `CVF_SESSION_MEMORY.md`
- Reviewer closure sync to `AGENT_HANDOFF_V17_2026-06-07.md`

**Forbidden scope:** see Source Verification and Forbidden Scope sections below.

## Roadmap-To-Work-Order Trace Matrix

| Roadmap section | Work order section | Status |
|---|---|---|
| Goal: implement `buildGovernedArtifactDescriptor()` | Section 6B: Implementation Contract | TRACED |
| Scope: new source + test files only | Scope / Target / Owner Boundary | TRACED |
| Non-goals: no provider call, no existing file modification | Section 6C: Forbidden Scope | TRACED |
| Acceptance criteria: tsc + vitest + gates PASS | Acceptance Criteria | TRACED |
| Verification commands | Evidence Requirements | TRACED |

## Worker Autonomy / No-Question Rule

Worker-Autonomy / No-Question Rule: any governance gate failure that is
within the allowed implementation scope (tsc errors, vitest failures,
markdown structural violations) must be repaired and rerun by the worker
without escalating to the operator. Only forbidden-scope boundary violations
or missing source facts require escalation.

## Required Artifact Manifest

| Artifact | Type | Required path | Proof literal |
|---|---|---|---|
| Runtime implementation | new TypeScript source | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts` | `tsc --noEmit` 0 errors |
| Test suite | new TypeScript test | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.artifact.descriptor.test.ts` | `npx vitest run` N/N PASS |
| Worker return | new Markdown review | `docs/reviews/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_WORKER_RETURN_2026-06-08.md` | all 4 governance gates COMPLIANT |

## Required First Reads

| File | Purpose |
|---|---|
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | Verify `GovernedArtifactDescriptor` and `GovernanceGateSet` exact interfaces |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts` | Reference gate enforcement pattern from T3 |
| `docs/baselines/CVF_GC018_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_2026-06-08.md` | Confirm authorized scope |
| `docs/roadmaps/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_ROADMAP_2026-06-08.md` | Confirm acceptance criteria |

## Pre-Flight Checks

| Check | Command | Required result |
|---|---|---|
| Clean working tree | `git status --short` | no unexpected modified files |
| Base HEAD confirmed | `git rev-parse --short HEAD` | capture as `executionBaseHead` |
| Predecessor source files exist | `Get-ChildItem EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | FILE FOUND |
| T6 source file does not yet exist | `Get-ChildItem EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts` | NOT FOUND (new file) |

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function | Disposition |
|---|---|---|---|---|---|
| `GovernedArtifactDescriptor` interface | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | lines 31-51 | `export interface GovernedArtifactDescriptor` | `dscp.governed.context.contract.ts` | ACCEPT |
| `GovernanceGateSet` interface | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | lines 13-26 | `export interface GovernanceGateSet` | `dscp.governed.context.contract.ts` | ACCEPT |
| `GovernedArtifactDescriptor.artifactRole` values | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | line 39 | `"corpus_candidate" \| "reference" \| "template" \| "operational"` | `GovernedArtifactDescriptor` | ACCEPT |
| `GovernanceGateSet.classificationGate` values | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | line 18 | `"PASS" \| "BLOCKED" \| "CONDITIONAL" \| "UNKNOWN"` | `GovernanceGateSet` | ACCEPT |
| `GovernanceGateSet.freshnessGate` values | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.contract.ts` | line 15 | `"PASS" \| "BLOCKED" \| "NOT_APPLICABLE" \| "UNKNOWN"` | `GovernanceGateSet` | ACCEPT |
| T3 gate enforcement pattern | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.context.packer.ts` | lines 1-96 | `GovernedContextPackerContract.pack()` | `dscp.governed.context.packer.ts` | ACCEPT |

## Section 6A: Source Verification Table (Legacy Label)

See `## Source Verification` table above. Kept for cross-reference.

## Section 6B: Implementation Contract

### New file: `dscp.governed.artifact.descriptor.ts`

**Imports:**
```typescript
import type {
  GovernedArtifactDescriptor,
  GovernanceGateSet,
} from "./dscp.governed.context.contract";
```

**Input type (export):**
```typescript
export interface GovernedArtifactDescriptorInput {
  artifactId: string;
  sourceHash: string;
  artifactRole: GovernedArtifactDescriptor["artifactRole"];
  contentClass: string;
  governanceGates: GovernanceGateSet;
  metadata?: Record<string, string>;
}
```

**Result type (export):**
```typescript
export interface GovernedArtifactDescriptorResult {
  descriptor: GovernedArtifactDescriptor | null;
  blocked: boolean;
  blockReason?: string;
}
```

**Function (export):**
```typescript
export function buildGovernedArtifactDescriptor(
  input: GovernedArtifactDescriptorInput
): GovernedArtifactDescriptorResult
```

**Gate enforcement rules:**
1. If `input.governanceGates.classificationGate === "BLOCKED"`:
   return `{ descriptor: null, blocked: true, blockReason: "classificationGate=BLOCKED for artifact <id>" }`
2. If `input.governanceGates.freshnessGate === "BLOCKED"`:
   return `{ descriptor: null, blocked: true, blockReason: "freshnessGate=BLOCKED for artifact <id>" }`
3. All other gate values (PASS, CONDITIONAL, NOT_APPLICABLE, UNKNOWN): build descriptor.

**Descriptor construction:**
- `artifactId` ← `input.artifactId`
- `sourceHash` ← `input.sourceHash`
- `artifactRole` ← `input.artifactRole`
- `contentClass` ← `input.contentClass`
- `governanceGates` ← `input.governanceGates`
- `metadata` ← `input.metadata ?? {}`

Return `{ descriptor, blocked: false }`.

**Governance note:** `GovernedArtifactDescriptor` is a scan-layer metadata
descriptor. It does NOT carry a `rawContentReleased` lock (that lock lives
on `GovernedContextPackageEvidence`). The descriptor's `governanceGates`
field records gate outcomes for audit; gate enforcement is done before
building, not after.

### New file: `dscp.governed.artifact.descriptor.test.ts`

Deterministic vitest test file. Required test cases:

1. **PASS path** — PASS classificationGate + PASS freshnessGate → returns non-null descriptor with correct fields.
2. **Blocked classificationGate** — `classificationGate: "BLOCKED"` → `blocked: true`, `descriptor: null`, `blockReason` contains artifact ID.
3. **Blocked freshnessGate** — `freshnessGate: "BLOCKED"` → `blocked: true`, `descriptor: null`, `blockReason` contains artifact ID.
4. **CONDITIONAL classificationGate** — passes through, descriptor returned.
5. **UNKNOWN freshnessGate** — passes through, descriptor returned.
6. **metadata default** — omitting `metadata` → descriptor has `metadata: {}`.
7. **metadata provided** — provided metadata object → descriptor preserves it.
8. **customGates preserved** — `governanceGates.customGates` → preserved in descriptor.
9. **corpus_candidate role** — correct `artifactRole` field.
10. **reference role** — correct `artifactRole` field.
11. **template role** — correct `artifactRole` field.
12. **operational role** — correct `artifactRole` field.

## Write Ownership

| Path | Ownership | Note |
|---|---|---|
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts` | Worker-created | new file |
| `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.artifact.descriptor.test.ts` | Worker-created | new file |
| `docs/reviews/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_WORKER_RETURN_2026-06-08.md` | Worker-created | new file |
| `docs/reviews/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_COMPLETION_2026-06-08.md` | Reviewer-created | closure review |
| `docs/roadmaps/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_ROADMAP_2026-06-08.md` | Reviewer-updated | closure status |
| `docs/roadmaps/CVF_DSCP_DOMAIN_AGNOSTIC_SCAN_CONTEXT_PACK_READINESS_ROADMAP_2026-06-07.md` | Reviewer-updated | parent status |
| `CVF_SESSION/ACTIVE_SESSION_STATE.json` | Reviewer-updated | session continuity |
| `CVF_SESSION_MEMORY.md` | Reviewer-updated | session continuity |
| `AGENT_HANDOFF_V17_2026-06-07.md` | Reviewer-updated | session continuity |
| All other existing files | FORBIDDEN | no modification |

## Execution Plan

1. Capture `executionBaseHead` via `git rev-parse --short HEAD`.
2. Confirm pre-flight checks PASS.
3. Implement `dscp.governed.artifact.descriptor.ts` per Section 6B contract.
4. Implement `dscp.governed.artifact.descriptor.test.ts` with all 12 required test cases.
5. Run `npx tsc --noEmit` — confirm 0 errors.
6. Run focused vitest — confirm all tests PASS.
7. Stage all new files.
8. Run all 4 governance gates against `10b02a79..HEAD`.
9. Author and stage worker return packet.
10. Return staged, uncommitted artifacts to reviewer.

## Work-Order Fulfillment Manifest

Worker-Autonomy / No-Question Rule: allowed-scope gate failures must be
repaired and rerun by the worker without escalating to the operator.

| Artifact | Type | Path | Proof required |
|---|---|---|---|
| Runtime implementation | new TypeScript source | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/dscp.governed.artifact.descriptor.ts` | `tsc --noEmit` PASS |
| Test suite | new TypeScript test | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/tests/dscp.governed.artifact.descriptor.test.ts` | vitest all PASS |
| Worker return | new Markdown review | `docs/reviews/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_WORKER_RETURN_2026-06-08.md` | all 4 gates COMPLIANT |

Forbidden paths (must NOT appear in `git diff --name-status`):
- Any `*.ts` file not listed above
- Any `.test.ts` file not listed above
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION_MEMORY.md`
- `AGENT_HANDOFF_V17_2026-06-07.md`
- Any public-sync or provenance-boundary file

## Evidence Requirements

| Evidence | Command | Format |
|---|---|---|
| TypeScript clean | `npx tsc --noEmit` | 0 errors |
| Vitest result | `npx vitest run tests/dscp.governed.artifact.descriptor.test.ts` | N/N PASS |
| Git diff scope | `git diff --name-status HEAD` | only worker-owned new files |
| 4 governance gates | gate runner commands in Section 6E | all COMPLIANT |

## Acceptance Criteria

| Criterion | Required result |
|---|---|
| `buildGovernedArtifactDescriptor()` exported and compiles | `tsc --noEmit` PASS |
| PASS-gate path returns populated non-null descriptor | vitest PASS |
| `classificationGate=BLOCKED` returns `blocked: true`, `descriptor: null` | vitest PASS |
| `freshnessGate=BLOCKED` returns `blocked: true`, `descriptor: null` | vitest PASS |
| CONDITIONAL gate passes through | vitest PASS |
| `metadata` defaults to `{}` when omitted | vitest PASS |
| All 4 `artifactRole` values accepted | vitest PASS |
| No existing file modified | `git diff --name-status` shows only new files |
| All 4 governance gates COMPLIANT | gate runner |

## Fail Conditions

| Condition | Action |
|---|---|
| `tsc --noEmit` emits errors | fix before returning |
| Any vitest test FAIL | fix before returning |
| Any governance gate VIOLATION | fix before returning |
| Any existing `.ts` file appears in diff | STOP — escalate to operator |
| Session, handoff, or registry file modified | STOP — escalate to operator |

## Section 6C: Forbidden Scope

| Forbidden action | Reason |
|---|---|
| Modify `dscp.governed.context.contract.ts` | existing source; T6 creates new files only |
| Modify `dscp.governed.context.packer.ts` | existing source; no modification authorized |
| Modify `dscp.governed.retrieval.receipt.ts` | existing source; no modification authorized |
| Make provider/LLM/API call | deterministic local only |
| Corpus ingestion, OCR, chunking | out of scope |
| Authorize PolicyLocal T12 | separately forbidden |
| Public-sync, production readiness | out of scope |
| Commit or push | WORKER_MUST_NOT_COMMIT |

## Section 6D: Required Artifact Manifest (Legacy Label)

See `## Work-Order Fulfillment Manifest` above.

## Review Gate

Reviewer must confirm before committing:
1. All vitest tests PASS (count matches expected).
2. `tsc --noEmit` 0 errors.
3. All 4 governance gates COMPLIANT.
4. `git diff --name-status` shows only worker-owned new files.
5. No session, handoff, registry, or existing TypeScript file modified.
6. Worker return packet contains all required evidence.

## Closure Checklist

- [x] Worker return packet reviewed and accepted
- [x] `tsc --noEmit` PASS confirmed
- [x] vitest all PASS confirmed (12/12)
- [x] All governance gates COMPLIANT confirmed
- [x] `git diff --name-status` scope confirmed
- [x] Reviewer commits material artifacts
- [x] Reviewer updates `CVF_SESSION/ACTIVE_SESSION_STATE.json` to `dscp_t6_closed_pass_bounded`
- [x] Reviewer updates `CVF_SESSION_MEMORY.md` and active handoff
- [x] Completion review packet authored by reviewer

## Return-To-Orchestrator Conditions

Worker returns to orchestrator (Codex reviewer) when all of the following are true:
- All new source files staged and uncommitted
- `tsc --noEmit` PASS confirmed
- All vitest tests PASS
- All 4 governance gates COMPLIANT
- Worker return packet complete and staged

Worker must NOT return if:
- Any gate has a VIOLATION
- Any existing file was modified
- Any vitest test FAIL remains unresolved

## Acceptance Receipt Assertion Matrix

DSCP-T6 produces no retrieval receipt. This matrix records pre-return
evidence for the scan descriptor builder.

| Required value | Observed value | Status |
|---|---|---|
| `buildGovernedArtifactDescriptor()` compiles | `tsc --noEmit` PASS; 0 errors | PASS |
| BLOCKED gate enforcement works | 12/12 vitest PASS | PASS |
| No provider call | no live/provider route in implementation | N/A with reason: deterministic local only |
| No corpus ingestion | scan descriptor is metadata only | N/A with reason: no corpus mutation |
| No T12 authorization | T6 does not authorize T12 | N/A with reason: T12 requires separate authorization |
| No existing file modified outside reviewer closure scope | `git diff --name-status` | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | this file | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_COMPLETION_2026-06-08.md` | reviewer completion authored | PASS |
| Roadmap state | `docs/roadmaps/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_ROADMAP_2026-06-08.md` | `Status: CLOSED_PASS_BOUNDED` | PASS |
| Registry JSON | `CVF_SESSION/ACTIVE_SESSION_STATE.json` | reviewer session sync in closure batch | PASS |
| Registry Markdown | `CVF_SESSION_MEMORY.md` and active handoff | reviewer session sync in closure batch | PASS |
| External evidence digest | external artifact | no external artifact authorized | N/A with reason: local deterministic only |
| System loop interlock | no system-loop mutation | new local function only | N/A with reason: helper function only |
| Session continuity | active session front door and handoff | reviewer-owned sync in closure batch | PASS |

## Operator Checkpoint

operator.checkpoint.waiver: operator authorized T6 dispatch via explicit
chat instruction 2026-06-08; no additional checkpoint needed before
Claude implements per this work order.

## Section 6F: Reviewer Closure Conversion

```yaml
completionReviewPath: docs/reviews/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_COMPLETION_2026-06-08.md
reviewerOwnedClosurePaths:
  - CVF_SESSION/ACTIVE_SESSION_STATE.json
  - CVF_SESSION_MEMORY.md
  - AGENT_HANDOFF_V17_2026-06-07.md
  - docs/roadmaps/CVF_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_ROADMAP_2026-06-08.md
  - docs/work_orders/CVF_AGENT_WORK_ORDER_DSCP_T6_SCAN_DESCRIPTOR_RUNTIME_FOR_CLAUDE_2026-06-08.md
closedStatusTokens:
  - CLOSED_PASS_BOUNDED
reviewerClosureCompleted: true
forbiddenClosedEquivalentResidue: []
```

---

## Claim Boundary

This work order claims: implementation contract, source verification, and
gate requirements for DSCP-T6. It does not claim: runtime provider behavior,
live proof, corpus ingestion, public readiness, production readiness,
T12 authorization, or public-sync.

---

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance work order; not public-synced and no public-facing
artifact or public catalog claim is made in this batch.
