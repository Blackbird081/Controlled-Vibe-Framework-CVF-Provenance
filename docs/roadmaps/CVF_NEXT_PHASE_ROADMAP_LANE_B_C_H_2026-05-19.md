# CVF Next Phase Roadmap — Lane B + C + H

Memory class: FULL_RECORD
Status: OPERATOR_APPROVED — 2026-05-19

## Authorization / Decision

Authority: `docs/reviews/CVF_MULTI_AGENT_DECISION_PACK_REVIEW_CVF_NEXT_PHASE_2026-05-18.md`
Session lift: `CVF_SESSION/ACTIVE_SESSION_STATE.json` mode `operator_lane_selection_active`
Implementer: Codex (PROPOSER)
Reviewer: Claude (REVIEWER)
Protocol: GC-018 per lane, GC-046 evidence-traced

Operator instruction (2026-05-19): implement all three lanes B + C + H.
Gate 0 was accepted by both agents on 2026-05-19. This roadmap is the
implementation authority for all three lanes.

## Purpose

This roadmap defines the three implementation lanes approved by the
operator after Gate 0 closure. Each lane has a GC-018 scope, exact
demand gate, acceptance criteria, and a boundary — what Codex must NOT
do in that lane.

Codex reads this roadmap, files a GC-018 for Lane B, implements it,
gets Claude review, then proceeds to Lane C, then Lane H. No lane may
be skipped or parallelized without operator instruction.

---

## Scope

Three lanes authorized in execution order: B (Workflow Packaging) →
C (Execution Gateway) → H (Memory Runtime Wiring). Each lane requires
its own GC-018 before implementation. Scope per lane is defined in the
lane sections below.

## Non-Goals

- Implementing Lane D (provider method parity) — demand-gated, no use case named
- Implementing Lane E (benchmark reorientation) — Phase F candidate, deferred
- Implementing Lane F (noncoder UX) — product design decision, needs operator direction
- Implementing Lane G (runtime actor enforcement) — requires H to exist first
- Globally lifting `system_reconvergence_stop` — stop is lifted per-lane only
- Adding new governance semantics beyond lane scope definitions
- Changing public claims without evidence receipts

## Read Before Starting

Before filing any GC-018, Codex must:

1. Read `CVF_SESSION_MEMORY.md` and confirm mode is `operator_lane_selection_active`.
2. Read `AGENT_HANDOFF_V9_2026-05-18.md` — especially "Active Boundary —
   Gate 0 Decision Pack" and "Claim Boundary" sections.
3. Read `docs/reviews/CVF_MULTI_AGENT_DECISION_PACK_REVIEW_CVF_NEXT_PHASE_2026-05-18.md`
   — especially §4 Canonical Ownership Map and §6 Next Recommended Tranche.
4. Read `docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md`
   — corrected problem map; know what already exists before building.

Anti-duplication rule: Before writing any new file, grep for existing
equivalents in `EXTENSIONS/`. Building from zero when a foundation exists
is the N-1 failure mode.

---

## Lane B — Workflow Packaging

### GC-018 Scope

Add governed capability pack specs alongside 3 existing templates. This
turns existing templates into documented governed capability packs. No
runtime changes. No new execution semantics. Purely additive
documentation and schema.

### Demand Gate (already met by operator instruction)

Templates selected by operator default:

1. `app_builder_complete` (EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/templates.ts)
2. One business template — `business` category, highest-value template
3. One content template — `content` category, highest-value template

Codex must locate exact template IDs from `templates.ts` before filing GC-018.

### What Codex Must Build

For each of the 3 selected templates, create 3 files alongside (or in a
`governance/` subfolder next to the template definition):

**File 1: `workflow.spec.md`**

```text
# Workflow Spec — <Template Name>

Template ID: <exact id from templates.ts>
Role binding: BUILDER (or as defined in template)
Governed by: CVF v4.0.0 GA

## Intake
- Input fields: <list from template inputs>
- Role check: resolveExecutionCVFRole() must return BUILDER or above
- DLP gate: applied before provider dispatch

## Workflow Steps
1. intake — validate inputs against template schema
2. retrieval — knowledge retrieval (if template uses knowledge)
3. provider_call — dispatch to certified provider lane
4. receipt_emission — emit governance receipt

## Output
- Deliverable: <what the template produces>
- Receipt: GovernanceReceiptV1 with step traces

## Evidence
- Execution path: EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts
- Provider lane: docs/evidence/provider-lanes.md
```

**File 2: `execution.policy.json`**

```json
{
  "templateId": "<exact id>",
  "requiredRole": "BUILDER",
  "minimumPermission": "output.product_brief",
  "dlpEnabled": true,
  "quotaEnabled": true,
  "providerLane": "certified",
  "receiptRequired": true,
  "guardPolicyRef": "CVF_GUARD_CONTRACT"
}
```

**File 3: `receipt.schema.json`**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12",
  "title": "<Template Name> Receipt",
  "description": "Governance receipt envelope for <template id>",
  "type": "object",
  "properties": {
    "templateId": { "type": "string", "const": "<exact id>" },
    "role": { "type": "string" },
    "stepTraces": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "step": { "type": "string" },
          "status": { "type": "string" },
          "durationMs": { "type": "number" }
        }
      }
    },
    "providerLane": { "type": "string" },
    "dlpResult": { "type": "string" },
    "quotaResult": { "type": "string" },
    "issuedAt": { "type": "string", "format": "date-time" }
  },
  "required": ["templateId", "role", "stepTraces", "issuedAt"]
}
```

### File Placement

Option A (preferred): Create `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governed-packs/<template-id>/` with the 3 files.

Option B: Create `docs/reference/governed-packs/<template-id>/` if Codex judges the lib location inappropriate.

Codex chooses and justifies the placement in its GC-018.

### GC-018 Template to File

Use `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md`.

GC-018 must include:
- Scope/Target/Owner Boundary
- Source/Predecessor Evidence (cite templates.ts paths, existing execute route)
- Decision/Baseline/Proposed Tranche
- Acceptance Criteria (exact checkboxes)
- Tranche Closure Checklist (mandatory per GC-018 template)
- Evidence/Verification (Test-Path for all new paths before commit)

GC-018 Risk: R0.

### Acceptance Criteria

- [ ] 3 templates have `workflow.spec.md` describing intake → steps → receipt
- [ ] 3 templates have `execution.policy.json` with role/permission binding
- [ ] 3 templates have `receipt.schema.json` defining governance envelope
- [ ] No runtime code added or modified
- [ ] No new public capability claim added without evidence
- [ ] All new file paths pass Test-Path in governance repo before commit
- [ ] Public catalog updated: add "Workflow capability packs" row to Key Extensions or note in Delivery History (catalog update rule — mandatory)
- [ ] GC-020 handoff Current HEAD updated after commit

### Boundary — What Codex Must NOT Do in Lane B

- Do NOT wire packs to runtime (`execute/route.ts` untouched)
- Do NOT add `receiptRequired: true` to runtime config without Phase E validation
- Do NOT create new governance semantics or new role definitions
- Do NOT claim governed pack is "live proven" — claim is "schema defined, awaiting runtime binding"
- Do NOT add W-series names or internal governance references to the pack files

---

## Lane C — Execution Gateway

### GC-018 Scope

Implement `cvf execute` as a CLI command that invokes the governed execute
path (`/api/execute` route) for a named template + role combination, and
returns the governance receipt with step traces. This is the developer
surface that lets a terminal user trigger the same governed flow as the
web UI.

### Demand Gate (met by operator instruction)

Use case: **Developer triggers `cvf execute` from terminal to run a
governed product brief and receive governance receipt.**

No new governance logic. The CLI is a thin caller of the existing route.

### Prior Art Inventory (Codex must read before filing GC-018)

```
EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/   — existing cvf-guard CLI (evaluate/audit/session/report)
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts  — the governed execute route
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.test.ts
ARCHITECTURE.md (public-sync)  — CLI surface description
```

Codex must answer these in the GC-018 before implementation:

1. **Invocation model**: Does the CLI call a running web server (HTTP) or
   import the execute module directly (Node)? Recommend: HTTP call to
   `localhost:3000/api/execute` — simplest, reuses all existing middleware.
2. **Auth/session model**: The web route uses NextAuth session. For CLI,
   use a `--api-key` flag or a local `.cvf-token` file. Document the
   choice. Do NOT store secrets in plain text without warning.
3. **Env/key loading**: Provider keys (`DASHSCOPE_API_KEY` etc.) must be
   loaded from `.env` or environment — never hardcoded or printed to stdout.
4. **Input schema**: CLI accepts `--template <id> --role <role>` plus
   optional `--input <json>`. Must validate against the execute route's
   input schema.
5. **Receipt output**: Print governance receipt as JSON to stdout. Print
   step traces to stderr or with `--verbose` flag.
6. **Error/timeout**: Graceful error messages. Timeout default 30s.

### What Codex Must Build

**New extension or file location:**

Option A (preferred): Add `cvf-execute.ts` (or `cvf-execute.js`) to
`EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/` alongside existing
`cvf-guard` commands.

Option B: Create `EXTENSIONS/CVF_CLI_EXECUTE/` as a new minimal extension
if Codex judges the execute surface warrants separation from the guard CLI.

Codex chooses and justifies in GC-018.

**Minimum viable implementation:**

```typescript
// cvf-execute.ts (pseudocode — Codex fills exact implementation)
import { Command } from 'commander';

const program = new Command();

program
  .name('cvf execute')
  .description('Execute a governed CVF template and return receipt')
  .requiredOption('--template <id>', 'Template ID')
  .requiredOption('--role <role>', 'CVF role (BUILDER, REVIEWER, etc.)')
  .option('--input <json>', 'Input payload as JSON string', '{}')
  .option('--endpoint <url>', 'CVF web endpoint', 'http://localhost:3000')
  .option('--verbose', 'Print step traces to stderr')
  .action(async (opts) => {
    // 1. Load provider env (from process.env or .env file)
    // 2. Build execute request matching route.ts input schema
    // 3. POST to <endpoint>/api/execute with auth header
    // 4. Print receipt JSON to stdout
    // 5. If --verbose, print step traces to stderr
  });

program.parse();
```

**Tests required:**

- Unit test: mock HTTP call returns mock receipt — CLI outputs valid JSON
- Unit test: missing `--template` flag → exits with code 1 + usage message
- Integration test (optional if live call is gated): describe as
  `describe.skip('live — requires running CVF server')` — do NOT run in CI
  without provider key gate

### GC-018 Template to File

Risk: R1.

GC-018 must resolve the 6 inventory questions above before implementation
section. Each answer must cite the specific file or decision.

### Acceptance Criteria

- [ ] `cvf execute --template product_brief --role BUILDER` returns governance receipt JSON to stdout when CVF web server is running
- [ ] Receipt includes `stepTraces` array with at minimum `intake`, `provider_call`, `receipt_emission` steps
- [ ] Auth model documented and implemented (no secret printed to stdout)
- [ ] Error on missing required flags with usage message
- [ ] Unit tests pass in CI (no live provider call in CI path)
- [ ] `cvf execute --help` shows correct usage
- [ ] Extends `cvf-guard` CLI or documents why separate extension was chosen
- [ ] Public catalog updated: governance CLI row updated to include `cvf execute` (catalog update rule — mandatory)
- [ ] GC-020 handoff updated after commit

### Boundary — What Codex Must NOT Do in Lane C

- Do NOT modify `execute/route.ts` — the CLI calls it, does not change it
- Do NOT add new governance middleware to the execute path
- Do NOT create a new auth system — use existing NextAuth or a simple token
- Do NOT implement `cvf trace`, `cvf run`, `cvf debug` in this tranche —
  one command only (`cvf execute`) for MVP
- Do NOT add live provider call to CI without provider key gate check
- Do NOT claim the CLI as a "runtime entry point" replacing the web route —
  it is a developer convenience surface

---

## Lane H — Memory Runtime Wiring

### GC-018 Scope

Wire `MemoryReinjectionPolicy` and `MemoryTierOwner` from
`CVF_LEARNING_PLANE_FOUNDATION` and `CVF_GUARD_CONTRACT` into the live
execute path for one memory-writing flow: **governance audit event
persistence** (the session audit log written after each governed execution).

This is the most narrowly scoped memory-writing event that already exists
in the execute path — governance audit output is already produced by the
execute route; the gap is that it is not passed through the memory tier
contracts.

### Demand Gate (met by operator instruction)

Flow selected: **governance audit event persistence** — when the execute
route emits a governance audit event (already happens), route it through
`MemoryTierOwner` to determine the correct audit tier, apply
`MemoryReinjectionPolicy` checks, and emit a memory receipt alongside the
governance receipt.

### Prior Art Inventory (Codex must read before filing GC-018)

```
EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts
EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/tests/
EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/  — MemoryTierOwner, MemoryReinjectionPolicy
EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts
  — specifically: where audit event is currently emitted (search for 'audit', 'receipt', 'log')
docs/evidence/cvf-16-5-runtime-absorption.md  — prior memory work evidence
```

Codex must answer these in the GC-018 before implementation:

1. **Audit event location**: Find the exact line(s) in `route.ts` where the
   audit event or governance receipt is currently emitted. Paste the line
   reference in the GC-018.
2. **Storage owner**: Which `MemoryTierOwner` tier owns audit events?
   Expected: `audit` tier (5-tier model from Phase 1.M).
3. **Persistence boundary**: Does the audit event persist to JSONL file,
   in-memory, or elsewhere? Document the current behavior before changing it.
4. **Retention policy**: What retention policy applies to audit events?
   Cite the existing policy contract or note that one must be defined.
5. **Contamination boundary**: Audit events must not be reinjected into
   subsequent provider calls. Confirm reinjection is not triggered for this
   event type.
6. **Receipt shape**: What does the memory receipt look like for an audit
   event? Define the schema before wiring.
7. **Live proof requirement**: Does wiring this memory path change provider
   output? If yes, live Alibaba proof required. If no (audit is post-response),
   unit test + integration test are sufficient.

### What Codex Must Build

**Step 1 — Inventory (in GC-018, not in code)**

Answer the 7 questions above with file:line citations. Do not write code
until these are answered.

**Step 2 — Memory receipt schema**

Define `AuditMemoryReceipt` type in the appropriate contract file:

```typescript
// In CVF_GUARD_CONTRACT or CVF_LEARNING_PLANE_FOUNDATION
export interface AuditMemoryReceipt {
  eventType: 'governance_audit';
  sessionId: string;
  templateId: string;
  role: string;
  tier: 'audit';           // MemoryTierOwner classification
  retentionPolicy: string; // policy ID applied
  reinjectionAllowed: false; // hard false for audit tier
  persistedAt: string;     // ISO timestamp
  storageRef?: string;     // path or key where audit is stored
}
```

**Step 3 — Wire into execute route (minimal, post-response only)**

In `route.ts`, after the governance receipt is built and before the
response is returned:

```typescript
// After receipt is built — pseudocode, Codex fills exact implementation
const memoryTier = MemoryTierOwner.classify('governance_audit');
const reinjectionCheck = MemoryReinjectionPolicy.check(memoryTier, context);
if (reinjectionCheck.allowed === false) {
  // audit events never reinjected — expected
}
const auditMemoryReceipt = emitAuditMemoryReceipt({
  sessionId, templateId, role, tier: memoryTier,
  retentionPolicy: reinjectionCheck.retentionPolicyId,
  persistedAt: new Date().toISOString()
});
// Attach to response or log separately — do NOT include in provider prompt
```

**Step 4 — Tests**

- Unit test: `MemoryTierOwner.classify('governance_audit')` returns `'audit'`
- Unit test: `MemoryReinjectionPolicy.check('audit', ctx)` returns `{allowed: false}`
- Unit test: `emitAuditMemoryReceipt(...)` returns valid `AuditMemoryReceipt`
- Integration test: Full execute flow emits `auditMemoryReceipt` in response
  payload or side log — verify field presence (not value)

### GC-018 Template to File

Risk: R1. The 7-question inventory must be answered in the GC-018 before
any code section.

### Acceptance Criteria

- [ ] `MemoryTierOwner.classify('governance_audit')` returns `'audit'` tier
- [ ] `MemoryReinjectionPolicy.check('audit', ...)` returns `{ allowed: false }`
- [ ] Execute route emits `AuditMemoryReceipt` after each governed execution
- [ ] `AuditMemoryReceipt` does not appear in the provider prompt (contamination boundary confirmed)
- [ ] All 4 unit/integration tests pass
- [ ] Live Alibaba proof: if audit wiring does not change provider output, integration test with mock provider is sufficient; if it does change output, live proof required
- [ ] `route.ts` diff is additive only — no existing governance logic modified
- [ ] Public catalog updated: "Memory and continuity contracts" row status upgraded from `partially absorbed` to `partially proven` with evidence path (catalog update rule — mandatory)
- [ ] GC-020 handoff updated after commit

### Boundary — What Codex Must NOT Do in Lane H

- Do NOT wire memory reinjection into the provider prompt — audit events
  are post-response only
- Do NOT implement multi-flow memory (skill evolution, session continuity)
  in this tranche — one flow only
- Do NOT change MemoryTierOwner or MemoryReinjectionPolicy contract
  signatures if existing tests rely on them — additive only
- Do NOT claim "full memory governance" — claim is "governance audit event
  persistence wired for selected flow"
- Do NOT delete or replace the existing audit log mechanism — extend it

---

## Execution Order and Review Gates

```
Lane B ──→ Codex GC-018 ──→ Codex implements ──→ Claude reviews ──→ CLOSE Lane B
    │
    └── After Lane B closes ──→ Lane C ──→ Codex GC-018 ──→ implement ──→ Claude reviews ──→ CLOSE Lane C
                                    │
                                    └── After Lane C closes ──→ Lane H ──→ Codex GC-018 ──→ implement ──→ Claude reviews ──→ CLOSE Lane H
```

**No lane may begin implementation before its GC-018 is filed and Claude
has not raised a blocking objection within one review cycle.**

If Codex raises a GC-018 and Claude is silent for the session, Codex may
proceed. If Claude raises a blocking objection (not wording — structural),
Codex pauses and resolves before implementing.

---

## Work Plan

Execution order is B → C → H. Each lane follows this sequence:

1. Codex reads prior art inventory listed in the lane section
2. Codex files GC-018 (answers inventory questions, states acceptance criteria)
3. Claude reviews GC-018 — no blocking objection → Codex proceeds
4. Codex implements the lane scope
5. Claude reviews implementation and evidence
6. Tranche Closure Checklist completed (catalog update, Test-Path, GC-020)
7. Lane closed — proceed to next lane

No lane begins step 2 before the previous lane's step 6 is complete.

## Acceptance Criteria

**Lane B complete when:**

- 3 template packs (workflow.spec.md + execution.policy.json + receipt.schema.json) committed
- No runtime code modified
- Public catalog updated

**Lane C complete when:**

- `cvf execute --template product_brief --role BUILDER` returns receipt JSON
- Unit tests pass in CI without live provider call
- Public catalog governance CLI row updated

**Lane H complete when:**

- `AuditMemoryReceipt` emitted after each governed execution
- `MemoryTierOwner` and `MemoryReinjectionPolicy` fire for `governance_audit` event
- All 4 tests pass; route.ts diff additive only
- Public catalog memory row upgraded to `partially proven`

## Verification / Evidence

Each lane must produce:

- GC-018 baseline file in `docs/baselines/`
- Completion evidence file in `docs/reviews/` or `docs/evidence/`
- Test-Path verification for all new paths in public-sync clone
- GC-046 Evidence Trace Block for any capability claim

## Related Artifacts

- `docs/reviews/CVF_MULTI_AGENT_DECISION_PACK_REVIEW_CVF_NEXT_PHASE_2026-05-18.md` — Gate 0 authority
- `docs/reviews/CVF_REVIEW_CVF_ASSESSMENT_AND_DIRECTION_2026-05-18.md` — corrected problem map
- `CVF_SESSION/ACTIVE_SESSION_STATE.json` — mode `operator_lane_selection_active`
- `AGENT_HANDOFF_V9_2026-05-18.md` — active session state
- `docs/reference/CVF_GC018_CONTINUATION_CANDIDATE_TEMPLATE.md` — GC-018 template
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` — Lane C + H target
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/` — Lane C base
- `EXTENSIONS/CVF_LEARNING_PLANE_FOUNDATION/src/index.ts` — Lane H base
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/` — Lane H contracts

## Claim Boundary

This roadmap authorizes implementation of Lane B, C, and H only. It does not:

- authorize Lane D, E, F, or G
- globally lift `system_reconvergence_stop` — stop is lifted per-lane only
- authorize new governance semantics beyond what each lane scope defines
- authorize public capability claims without evidence receipts and live proof
- authorize changes to existing tests, contracts, or governance logic outside each lane's additive scope
