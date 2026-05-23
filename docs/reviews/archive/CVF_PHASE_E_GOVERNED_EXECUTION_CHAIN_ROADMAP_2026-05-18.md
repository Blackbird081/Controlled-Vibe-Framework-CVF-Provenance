# CVF Phase E — Governed Execution Chain Roadmap

Memory class: FULL_RECORD
Status: PROPOSED_V2 — revised after Codex rebuttal; pending operator approval and GC-018 before any implementation
Rebuttal source: `docs/reviews/CVF_PHASE_E_GOVERNED_EXECUTION_CHAIN_CODEX_REBUTTAL_TO_CLAUDE_2026-05-18.md`
Revision: Claude Round 2, 2026-05-18

## Authorization Required

This roadmap is PROPOSED, not authorized. No implementation may begin
until the operator approves this document and a fresh GC-018 is filed
for each tranche.

Parent review: `.private_reference/legacy/CVF 17.05/Review CVF.md`

## Purpose

Wire the Phase D contracts into the live execution path and implement the
Workflow Composition layer so that CVF has a Governed Capability System,
not just a Control System. Phase E converts isolated contract definitions
into a chain that fires on every real governed request.

## Problem Statement

Phase A–D delivered correct, well-governed contracts. However a complete
audit of the live execution path reveals:

```text
grep getRolePermissionProfile / isOutputAllowedForRole / WorkflowTransition
/ ToolActionClass / OrchestratorDelegation / MemoryReinjection
→ EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/**
→ 0 results (excluding tests)
```

Every Phase D contract is isolated — defined but not called in any live
execution path. The web app's `route.ts` already has a governed execution
route (AuthN, DLP, quota, guard runtime, provider routing, output
validation, governance receipt, audit event). However, the route does not
consume the Phase D contract layer: `session?.role` is read as a raw RBAC
string and never normalized to `CVFRole`, `getRolePermissionProfile()` is
never called, `isOutputAllowedForRole()` is never checked, and no receipt
is tied to a `WorkflowTransition.receiptRequired` rule.

The more precise claim:

> CVF has a governed execution route, but the route does not yet consume
> the Phase D contract layer as an enforced Governed Capability System.

This means CVF currently has:

- Governance Infrastructure ✓
- Contract definitions ✓
- Governed execution route ✓
- **Phase D contract chain ✗** — existing governance surfaces do not
  consume the Phase D typed contracts

The `Review CVF.md` audit (2026-05-17) named this precisely:
> "CVF có Control System nhưng chưa có Governed Capability System"

## Scope

In scope:

- Wire Phase D contracts into the live execute path (no new contracts)
- Implement one end-to-end Governed Workflow for the existing golden path
  (`Create Product Brief` — already has live Alibaba proof)
- Build the Workflow Composition layer that the legacy spec already
  designed (`CVF_CAPABILITY_WORKFLOW_COMPOSITION.md`)
- Receipt binding: tie role + action class + receipt obligation into one
  enforced chain
- Acceptance test: a governed task run must show every checkpoint firing,
  not just the output being correct

Out of scope:

- New AI providers or provider methods (Tranche 4 remains demand-gated)
- Noncoder UX redesign (separate product initiative)
- cvf-cli runtime entry point (separate tranche, lower dependency)
- Skill Certification System for external repos (Phase F, after chain exists)
- Agent OS claim expansion
- Lifting `system_reconvergence_stop`

## Non-Goals

This roadmap does not add more contracts, does not expand governance
concepts, and does not absorb additional legacy folders. The goal is
convergence of what already exists, not growth.

## Root Cause of the Wiring Gap

Phase A–D used **concept-first** execution: each tranche added one
contract type per legacy concept axis. Correct as governance artifacts.
But no tranche asked: "does the live execution path call this?"

Phase E uses **flow-first** execution: start from a real user request,
trace every step, identify every broken wire, fix only what the flow needs.

## Work Plan

### Tranche E.1 — Execution Chain Audit (no code)

**Purpose:** Before writing a single line, produce a verified map of
every wiring gap in the `Create Product Brief` golden path.

**Method:** Trace the live request flow step by step:

```text
POST /api/execute
  → AuthN (verifySessionCookie / service token)       ← already wired
  → Role resolution (session.role → CVFRole)          ← raw string, NOT through getRolePermissionProfile()
  → Output class check (allowedOutputClasses)         ← NOT checked
  → Budget / quota gate                               ← already wired
  → Guard pipeline (buildWebGuardContext)             ← wired, but Phase D contracts not in pipeline
  → Knowledge context injection                       ← already wired
  → Provider call (routeWebProvider)                  ← already wired
  → Output validation (validateOutput)                ← wired, but output CLASS not checked against role profile
  → DLP filter                                        ← already wired
  → Governance receipt (buildGovernanceEnvelope)      ← wired, but NOT tied to WorkflowTransition rules
  → Audit event (appendAuditEvent)                    ← wired, but role permission result NOT included
  → Response                                          ← already wired
```

For each step, record using the five allowed states:

- `wired` — contract/surface already enforced in live path
- `wiring_gap` — contract exists but not called in live path
- `implementation_gap` — contract does not exist yet
- `not_applicable_to_selected_flow` — contract exists but the selected
  flow (`Create Product Brief`) does not exercise this capability
- `deferred_with_reason` — known gap, not in Phase E scope; reason stated

| Checkpoint | Current surface | Phase D contract | Selected-flow relevance | Current state | Required close condition |
| --- | --- | --- | --- | --- | --- |
| AuthN | `verifySessionCookie` / service token | existing route guard | relevant | wired | keep regression tests passing |
| CVF role resolution | `session?.role` raw string | `role-permission.contract.ts` | relevant | wiring_gap | normalized `CVFRole` trace emitted |
| Output class gate | none | `RolePermissionOutputClass` | relevant | wiring_gap | output class resolved and checked before provider call |
| DLP filter | `applyDLPFilter` | existing route guard | relevant | wired | audit event remains emitted on redaction |
| Quota gate | `checkTeamQuota` | existing route guard | relevant | wired | quota block still returns structured response |
| Guard pipeline | `buildWebGuardContext` | guard runtime | relevant | wired | Phase D role/action context included after E.2 |
| Workflow transition | none | `runtime-workflow.contract.ts` | relevant | wiring_gap | transition trace includes receipt obligation |
| Provider call | `executeAI` via routed provider | `ToolActionClass.provider_call` | relevant | wiring_gap | provider call is a typed workflow step |
| Output validation | `validateOutput` | role output class + validator | relevant | partial | validation result tied to workflow step |
| Governance receipt | `buildEvidenceReceipt` | receipt binding | relevant | partial | receipt references step/action/role obligation |
| ORCHESTRATOR delegation | none in product brief path | `orchestrator.contract.ts` | not applicable — no worker used | not_applicable_to_selected_flow | defer to worker-backed workflow |
| Memory write restriction | no write in product brief path | `memory-continuity.contract.ts` | not applicable — no memory write | not_applicable_to_selected_flow | defer to memory-writing workflow |

**Output artifact:**
`docs/reviews/CVF_PHASE_E_EXECUTION_CHAIN_AUDIT_2026-05-18.md`

This audit is the acceptance criteria for the entire Phase E. Every
subsequent tranche closes specific rows in this table. Phase E is done
when every row is either `wired` or has an explicit state with reason.

**GC-018 required:** No — this is documentation only.

**Acceptance criteria:** Audit table is complete with five-state
taxonomy. Every row populated. No implementation work in this tranche.

---

### Tranche E.2 — Role Permission Gate in Execute Path

**Purpose:** Wire `role-permission.contract.ts` into `route.ts` so that
every governed execution call checks the caller's allowed output classes
before the provider call fires.

**Design preconditions (must be implemented before `getRolePermissionProfile` call):**

`session?.role` is an RBAC text string from NextAuth (`"owner"`, `"admin"`,
`"developer"`, etc.). `getRolePermissionProfile()` requires a `CVFRole` enum
value. A normalization layer is required between them.

Two resolvers must be added:

1. `resolveExecutionCVFRole(session, isServiceAllowed)` — maps RBAC role to
   `CVFRole`:
   - service token present → `CVFRole.SERVICE_AGENT`
   - `"owner"` | `"admin"` → `CVFRole.OPERATOR`
   - `"developer"` → `CVFRole.BUILDER`
   - `"reviewer"` → `CVFRole.REVIEWER`
   - `"viewer"` → `CVFRole.OBSERVER`
   - `undefined` / unknown → deny (must not silently widen authority)

2. `resolveExecutionOutputClass(templateId, templateCategory, mode)` — maps
   request context to `RolePermissionOutputClass`:
   - `templateCategory: "product_brief"` + any mode → `OutputClass.artifact`
   - Additional mappings demand-gated until a consuming slice is selected.

**What changes:**

`route.ts` currently reads `session?.role` as a raw string for logging.
After this tranche:

1. `resolveExecutionCVFRole()` runs first to normalize the session role;
2. `resolveExecutionOutputClass()` resolves the output class from request context;
3. `getRolePermissionProfile(cvfRole)` is called with the normalized role;
4. `isOutputAllowedForRole(cvfRole, resolvedOutputClass)` is checked before
   provider dispatch.

If the role is not allowed to produce the requested output class, the
route returns a policy-denied response with a structured receipt — not a
500 or a silent fallback.

**Files changed:**

- `cvf-web/src/lib/execute-role-resolver.ts` — new; exports
  `resolveExecutionCVFRole()` and `resolveExecutionOutputClass()`
- `cvf-web/src/app/api/execute/route.ts` — add role permission check
  after AuthN, before provider dispatch; call both resolvers
- `cvf-web/src/lib/execute-route-guards.ts` — add
  `checkRoleOutputPermission(cvfRole, outputClass)` helper
- `cvf-web/src/lib/execute-role-resolver.test.ts` — tests:
  - service token → `SERVICE_AGENT`
  - `"owner"` → `OPERATOR`
  - unknown role → deny (not widened)
  - `app_builder_complete` template → `artifact` output class
- `cvf-web/src/app/api/execute/route.test.ts` — add tests: OBSERVER role
  denied for `code_patch` output, BUILDER role allowed for `artifact`

**Live proof required:** No — deterministic tests cover the gate.
The existing Alibaba live proof (Phase 2.C) must still PASS after wiring.

**GC-018 required:** Yes — this changes live execute path behavior.

**Acceptance criteria:**

- `resolveExecutionCVFRole` runs for every authenticated or service-token request
- Unknown/unsupported roles do not silently widen authority (explicit deny)
- `resolveExecutionOutputClass` maps `app_builder_complete` to `artifact`
- `getRolePermissionProfile` is called with resolved `CVFRole`
- `isOutputAllowedForRole` gates before provider dispatch
- Policy-denied response returned when role is not in allowed output classes
- Existing golden path (BUILDER role + `artifact` output class) still passes
- No regression in existing web tests

---

### Tranche E.3 — Workflow Binding Contract

**Purpose:** Implement the `workflow.binding.json` schema that the legacy
17.05 spec designed (`CVF_CAPABILITY_WORKFLOW_COMPOSITION.md`) and that
CVF has never implemented.

This is the missing layer between "user asks for something" and "CVF
dispatches a governed sequence of steps." Without it, the execute route
handles each request without a typed, composed governance sequence.

**What this adds:**

```text
workflow.product.create_product_brief.v1
  → step 1: intake validation   (role: BUILDER,   output: recommendation, status: active)
  → step 2: knowledge retrieval (role: BUILDER,   output: analysis,       status: active)
  → step 3: provider call       (role: BUILDER,   output: artifact,       status: active)
  → step 4: review gate         (role: REVIEWER,  output: review_finding, status: deferred_until_reviewer_surface)
  → step 5: receipt emit        (role: BUILDER,   receiptRequired: true,  status: active)
```

Each step is typed with: `CVFRole`, `RolePermissionOutputClass`,
`WorkflowTransition`, `receiptRequired`, `status`.

Step 4 (REVIEWER) is declared in the binding but marked
`status: "deferred_until_reviewer_surface"` — no real reviewer actor or
deterministic validator exists today. E.4 live proof covers only steps
1–3 and 5. Step 4 must not be force-fired to create artificial proof.

Each step also carries a `WorkflowStepExecutionTrace` shape:
`{ stepId, preconditionChecked, decision, receiptId, source }` — a step
is only counted as fired when all four fields are observable in the
response or audit event.

**Files to create:**

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/workflow-binding.contract.ts`
  — `WorkflowBinding`, `WorkflowStep`, `WorkflowStepRole`,
  `WorkflowStepExecutionTrace`; validator `validateWorkflowBinding(binding)`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/contracts.phaseE-workflow-binding.test.ts`
  — tests: step sequence is valid, roles are in CVFRole vocabulary,
  output classes are in allowed vocabulary, receipt steps are typed,
  deferred steps are valid binding members
- One concrete binding file as proof:
  `cvf-web/src/lib/workflows/workflow.product.create_product_brief.v1.json`
  — wires the existing Phase 2.C golden path into a typed workflow binding

**GC-018 required:** Yes.

**Acceptance criteria:**

- `WorkflowBinding` type is exported from guard contract
- `WorkflowStepExecutionTrace` type is exported from guard contract
- `validateWorkflowBinding` returns errors for invalid role/output combos
- Concrete `create_product_brief` binding file validates clean with step 4
  marked `deferred_until_reviewer_surface`
- Tests pass
- No runtime behavior change yet (binding is defined, not yet enforced
  in route — that is E.4)

---

### Tranche E.4 — Wire Workflow Binding into Execute Path

**Purpose:** Make `route.ts` dispatch against a `WorkflowBinding` when
one is available for the requested skill/template, so the execute path
uses a governed step sequence instead of a direct provider call.

**Observable proof rule:** A step is only counted as fired when
`WorkflowStepExecutionTrace { stepId, preconditionChecked, decision,
receiptId, source }` is observable in both the response body and the
audit event. Bookkeeping that records a step without checking its
precondition does not count.

**What changes:**

When a request maps to a known workflow binding (by skill ID or template
ID), the execute path:

1. Loads the binding
2. Validates the caller's resolved `CVFRole` against each active step's
   required role
3. Fires each active step in sequence, skipping `deferred_*` steps
4. Emits a `WorkflowStepExecutionTrace` per step into the audit event
5. Returns a structured response that includes `workflowId`,
   `stepTraces[]`, and `receipts[]`

When no binding exists for the request, the path falls back to the
existing governed route (backwards compatible).

**Files changed:**

- `cvf-web/src/lib/workflows/workflow-resolver.ts` — new; looks up
  binding by skill ID or template ID
- `cvf-web/src/app/api/execute/route.ts` — add binding lookup after AuthN;
  if binding found, use governed step dispatch; else use existing path
- `cvf-web/src/app/api/execute/route.test.ts` — add: bound request fires
  all active steps with observable traces; unbound request uses fallback
  path; receipt emitted for `receiptRequired: true` steps; deferred steps
  are not fired

**Live proof required:** YES. After this tranche, a `Create Product Brief`
request must:

- Resolve the `workflow.product.create_product_brief.v1` binding
- Fire all active steps (1, 2, 3, 5) in sequence with observable traces
- Skip step 4 (deferred REVIEWER step)
- Emit at least one receipt tied to `receiptRequired: true`
- Return a response that includes `workflowId`, `stepTraces[]`, and receipts
- Both the audit event and the response contain the step trace data

Run with Alibaba API key via `scripts/run_cvf_release_gate_bundle.py --json`
plus a targeted route live test. Record both in completion packet.

**GC-018 required:** Yes.

**Acceptance criteria:**

- Bound workflow request resolves correct binding
- Each active step emits a `WorkflowStepExecutionTrace` with all four fields
- Deferred steps are not fired (not counted, not faked)
- Receipt is emitted for `receiptRequired` steps; receipt ID in trace
- Both audit event and response body contain step trace data
- Live Alibaba proof PASS
- Existing unbound requests are unaffected (fallback path)

---

### Tranche E.5 — Per-Agent Receipt Binding (row 8.2 closure)

**Purpose:** Close the row 8.2 implementation gap: bind role + action
class + receipt obligation into one enforced chain.

This is the tranche that was deferred from Phase D. After E.4 exists,
this tranche has a concrete flow to plug into.

**What this adds:**

`runtime-workflow.contract.ts` already has `WorkflowTransition` with
`receiptRequired`. This tranche adds the enforcement: when a step
completes and `receiptRequired` is true, the execute path calls
`emitStepReceipt(role, actionClass, stepId)` and the receipt is
persisted in the audit log.

**Scope boundary:** E.5 covers only the role/action pairs used by the
bound `Create Product Brief` workflow (active steps 1, 2, 3, 5). The
full `CVFRole × ToolActionClass` matrix is broader than the golden path
and is deferred with reason: no consuming slice selected for the
remaining combinations.

**Files to create or extend:**

- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts`
  — `StepReceiptObligation`: maps `(CVFRole, ToolActionClass)` →
  `receiptRequired: boolean`; `buildStepReceipt(role, actionClass, stepId)`;
  initial table covers only pairs used by the selected workflow
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/contracts.phaseE-receipt-binding.test.ts`
  — tests: `BUILDER` + `provider_call` requires receipt;
  `BUILDER` + `intake_validation` does not; receipt shape has required fields;
  full-matrix coverage deferred note present in contract
- `cvf-web/src/app/api/execute/route.ts` — after step execution in E.4
  dispatch, call `emitStepReceipt` when obligation fires

**Live proof required:** Deterministic tests are sufficient. The E.4
live proof already exercises the receipt emit path.

**GC-018 required:** Yes.

**Acceptance criteria:**

- `StepReceiptObligation` covers role/action pairs used by the selected workflow
- Full `CVFRole × ToolActionClass` matrix explicitly deferred with reason in contract
- Enforcement fires in E.4 workflow dispatch
- `row 8.2` in `CVF_LEGACY_CONCEPT_AXIS_MATRIX_2026-05-18.md` updated from
  `needs_gc018` to `partially_absorbed`

---

### Tranche E.6 — Phase E Closure and Chain Verification

**Purpose:** Verify the complete governed execution chain fires end-to-end
and close Phase E.

**Verification test:** Run one `Create Product Brief` request and confirm:

```text
1.  AuthN resolves caller → CVFRole (BUILDER via resolveExecutionCVFRole)
2.  getRolePermissionProfile(BUILDER) called → profile loaded
3.  isOutputAllowedForRole(BUILDER, 'artifact') → true
4.  Workflow binding resolved: workflow.product.create_product_brief.v1
5.  Active steps dispatched in order: intake(1) → retrieval(2) → provider(3) → receipt(5)
6.  Step 4 (REVIEWER) skipped — status: deferred_until_reviewer_surface
7.  Provider call: Alibaba Qwen → governed receipt emitted
8.  Step receipt emitted: BUILDER + provider_call + step-3 → receipt persisted
9.  Response includes: workflowId, stepTraces[], receipts[], governanceEnvelope
10. Audit event includes: role permission check result + stepTraces[]
```

Phase D contract applicability for selected flow — each must be either
enforced or explicitly documented as not applicable:

| Phase D contract | Selected-flow verdict | Required action |
| --- | --- | --- |
| `role-permission.contract.ts` | relevant | must be enforced (E.2) |
| `runtime-workflow.contract.ts` | relevant | must be enforced (E.4) |
| `orchestrator.contract.ts` | not_applicable_to_selected_flow | document in closure packet |
| `memory-continuity.contract.ts` | not_applicable_to_selected_flow | document in closure packet |

Every row in the E.1 audit table must show `wired`, `not_applicable_to_selected_flow`,
or `deferred_with_reason` — no row may be left as `wiring_gap` or
`implementation_gap` at closure.

**Output artifact:**
`docs/reviews/CVF_PHASE_E_CLOSURE_2026-05-18.md`

Update `CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`:

- "Role and agent governance": evidence link updated to include
  execution chain proof
- "Knowledge-backed execution": update evidence to cite E.4 workflow binding
- Run `Test-Path` on all catalog paths in public-sync before committing

**Public-sync boundary (mandatory):** All public catalog edits must be
performed only in the `Controlled-Vibe-Framework-CVF-public-sync` clone.
Before committing any catalog change, record `git remote -v` output in
the E.6 closure packet to prove the edit targets the correct remote.
Never edit the public catalog from this private governance repo.

---

## Tranche Dependency Order

```text
E.1 Execution Chain Audit (no GC-018, no code)
    ↓
E.2 Role Permission Gate  ← GC-018 required
    ↓
E.3 Workflow Binding Contract  ← GC-018 required
    ↓
E.4 Wire Binding into Execute Path  ← GC-018 required; live proof required
    ↓
E.5 Per-Agent Receipt Binding  ← GC-018 required (closes row 8.2)
    ↓
E.6 Phase E Closure
```

E.3 and E.2 may run in parallel if separate GC-018s are filed. E.4
depends on both E.2 and E.3 being complete.

---

## Forbidden Moves

- Do NOT add more governance concepts or contract types beyond what the
  flow needs
- Do NOT redesign the noncoder UX in this phase — that is a product
  decision, not a chain wiring decision
- Do NOT claim "governed execution" in the public catalog before E.4
  live proof PASS
- Do NOT absorb additional legacy folders
- Do NOT implement provider method expansion (Tranche 4 remains
  demand-gated)
- Do NOT use `--no-verify` on any commit

---

## What Phase E Does NOT Fix

These items are real but out of scope for Phase E:

| Item | Why deferred |
| --- | --- |
| cvf-cli runtime | Separate tranche; no consumer identified yet |
| Noncoder outcome UX (`[Create PRD]` buttons) | Product/design decision, not chain wiring |
| Operational benchmark suite (Problem E) | Requires E.4 to exist first; Phase F candidate |
| Skill Certification System for external repos | Requires chain to exist first; Phase F |
| Provider method parity (Problem D remaining) | Demand-gated; no consuming slice |

---

## Why This Avoids the "DONE but broken chain" Pattern

Phase A–D acceptance criteria: "contract X exists" → agent declares DONE.
Phase E acceptance criteria: "checkpoint X fires in a real request" →
agent declares DONE.

If a contract is not called in E.1 chain audit, it cannot be counted as
wired. The audit table is the source of truth, not the contract file list.

---

## Acceptance Criteria (Phase E complete)

- E.1 audit table exists and is fully populated with five-state taxonomy
- E.2: `resolveExecutionCVFRole` and `resolveExecutionOutputClass` run on every request; unknown roles denied; role permission gate fires before provider dispatch
- E.3: `WorkflowBinding` and `WorkflowStepExecutionTrace` types exported; `create_product_brief` binding validates with step 4 marked deferred
- E.4: bound workflow dispatches all active steps with observable `WorkflowStepExecutionTrace`; live Alibaba proof PASS; receipts emitted; deferred steps skipped
- E.5: per-agent receipt obligation covers role/action pairs used by selected workflow; full matrix deferred with reason
- E.6: closure verifies selected-flow checkpoints; non-applicable Phase D contracts explicitly documented; `git remote -v` proof in closure packet
- No `needs_gc018` row in concept-axis matrix without deferral note
- Public catalog updated with chain proof evidence from public-sync clone only — `Test-Path` 100%
- `system_reconvergence_stop` posture unchanged

## Work Plan Summary

See the six tranche sections above (E.1 through E.6) as the complete
work plan.

## Verification

Minimum verification per tranche:

```bash
cd EXTENSIONS/CVF_GUARD_CONTRACT && npm run check
npm run test -- --run src/contracts/contracts.phaseE-<tranche>.test.ts
python governance/compat/check_active_session_state.py --enforce
python governance/compat/check_docs_governance_compat.py --base HEAD --head HEAD --enforce
python governance/compat/check_markdown_structural_completeness.py --base HEAD --head HEAD --enforce
python governance/compat/check_governed_file_size.py --base HEAD --head HEAD --enforce
python governance/compat/check_agent_handoff_guard_compat.py --base HEAD~1 --head HEAD --enforce
```

For tranches requiring live proof (E.4):

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

Phase E chain verification (E.6 only): run one live `Create Product
Brief` request and confirm all chain checkpoints fire as listed in the
Tranche E.6 verification table. Non-applicable contracts must be
explicitly documented, not forced.

## Claim Boundary

This roadmap may support updating catalog rows for "Role and agent
governance" and "Knowledge-backed execution" after E.4 live proof PASS.

It does not authorize:

- complete Agent OS claim
- universal provider parity claim
- full legacy absorption claim
- any claim beyond what E.4 live proof demonstrates

## Related Artifacts

- `.private_reference/legacy/CVF 17.05/Review CVF.md` — original pain point audit
- `.private_reference/legacy/CVF 17.05/CVF_EXTERNAL_CAPABILITY_INTAKE/CVF_CAPABILITY_WORKFLOW_COMPOSITION.md` — workflow binding schema origin
- `docs/reviews/CVF_LEGACY_PHASE_D_FULL_CLOSURE_2026-05-18.md`
- `docs/reviews/CVF_LEGACY_CONCEPT_AXIS_MATRIX_2026-05-18.md`
- `docs/reviews/CVF_17_05_LEGACY_ABSORPTION_GAP_LEDGER_2026-05-18.md`
- `AGENT_HANDOFF_V9_2026-05-18.md`
