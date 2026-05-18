# CVF Phase E — Governed Execution Chain Roadmap

Memory class: FULL_RECORD
Status: PROPOSED — pending operator approval and GC-018 before any implementation

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

```
grep getRolePermissionProfile / isOutputAllowedForRole / WorkflowTransition
/ ToolActionClass / OrchestratorDelegation / MemoryReinjection
→ EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/**
→ 0 results (excluding tests)
```

Every Phase D contract is isolated — defined but not called in any live
execution path. The web app's `route.ts` reads `session?.role` as a raw
string but never passes it through `getRolePermissionProfile()`, never
checks `isOutputAllowedForRole()`, and never emits a receipt tied to a
`WorkflowTransition.receiptRequired` rule.

This means CVF currently has:

- Governance Infrastructure ✓
- Contract definitions ✓
- **Governed Capability System ✗** — the chain from user intent to
  governed output does not fire

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

```
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

For each step, record:

| Step | Contract available | Called in flow | Gap type |
|---|---|---|---|
| Role permission check | `role-permission.contract.ts` | NO | Wiring gap |
| Output class enforcement | `RolePermissionOutputClass` | NO | Wiring gap |
| Orchestrator delegation check | `orchestrator.contract.ts` | NO | Wiring gap |
| Memory write restriction | `memory-continuity.contract.ts` | NO | Wiring gap |
| Workflow transition receipt | `runtime-workflow.contract.ts` | NO | Wiring gap |
| Per-agent receipt binding | not implemented | N/A | Implementation gap |

**Output artifact:**
`docs/reviews/CVF_PHASE_E_EXECUTION_CHAIN_AUDIT_2026-05-18.md`

This audit is the acceptance criteria for the entire Phase E. Every
subsequent tranche closes specific rows in this table. Phase E is done
when every row in the table is either "wired" or "explicitly deferred
with reason."

**GC-018 required:** No — this is documentation only.

**Acceptance criteria:** Audit table is complete, every gap is typed as
"wiring gap" (contract exists, not called) or "implementation gap"
(contract does not exist). No implementation work in this tranche.

---

### Tranche E.2 — Role Permission Gate in Execute Path

**Purpose:** Wire `role-permission.contract.ts` into `route.ts` so that
every governed execution call checks the caller's allowed output classes
before the provider call fires.

**What changes:**

`route.ts` currently reads `session?.role` as a raw string for logging.
After this tranche, it calls `getRolePermissionProfile(role)` and checks
`isOutputAllowedForRole(role, resolvedOutputClass)` before dispatching.

If the role is not allowed to produce the requested output class, the
route returns a policy-denied response with a structured receipt — not a
500 or a silent fallback.

**Files changed:**
- `cvf-web/src/app/api/execute/route.ts` — add role permission check
  after AuthN, before provider dispatch
- `cvf-web/src/lib/execute-route-guards.ts` — add
  `checkRoleOutputPermission(role, outputClass)` helper
- `cvf-web/src/app/api/execute/route.test.ts` — add tests: OBSERVER role
  denied for `code_patch` output, BUILDER role allowed

**Live proof required:** No — deterministic tests cover the gate.
The existing Alibaba live proof (Phase 2.C) must still PASS after wiring.

**GC-018 required:** Yes — this changes live execute path behavior.

**Acceptance criteria:**
- `getRolePermissionProfile` is called for every authenticated request
- Policy-denied response is returned when role is not in allowed output classes
- Existing golden path (BUILDER role + `artifact` output class) still passes
- No regression in existing 63 web tests

---

### Tranche E.3 — Workflow Binding Contract

**Purpose:** Implement the `workflow.binding.json` schema that the legacy
17.05 spec designed (`CVF_CAPABILITY_WORKFLOW_COMPOSITION.md`) and that
CVF has never implemented.

This is the missing layer between "user asks for something" and "CVF
dispatches a governed sequence of steps." Without it, every request is
a single unstructured provider call with no composed governance.

**What this adds:**

```
workflow.product.create_product_brief.v1
  → step 1: intake validation (role: BUILDER, output: recommendation)
  → step 2: knowledge retrieval (role: BUILDER, output: analysis)
  → step 3: provider call (role: BUILDER, output: artifact)
  → step 4: review gate (role: REVIEWER, output: review_finding)
  → step 5: receipt emit (role: BUILDER, receiptRequired: true)
```

Each step is typed with: `CVFRole`, `RolePermissionOutputClass`,
`WorkflowTransition`, `receiptRequired`.

**Files to create:**
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/workflow-binding.contract.ts`
  — `WorkflowBinding`, `WorkflowStep`, `WorkflowStepRole`; validator
  `validateWorkflowBinding(binding)`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/contracts.phaseE-workflow-binding.test.ts`
  — tests: step sequence is valid, roles are in CVFRole vocabulary,
  output classes are in allowed vocabulary, receipt steps are typed
- One concrete binding file as proof:
  `cvf-web/src/lib/workflows/workflow.product.create_product_brief.v1.json`
  — wires the existing Phase 2.C golden path into a typed workflow binding

**GC-018 required:** Yes.

**Acceptance criteria:**
- `WorkflowBinding` type is exported from guard contract
- `validateWorkflowBinding` returns errors for invalid role/output combos
- Concrete `create_product_brief` binding file validates clean
- Tests pass
- No runtime behavior change yet (binding is defined, not yet enforced
  in route — that is E.4)

---

### Tranche E.4 — Wire Workflow Binding into Execute Path

**Purpose:** Make `route.ts` dispatch against a `WorkflowBinding` when
one is available for the requested skill/template, instead of dispatching
a raw unstructured provider call.

**What changes:**

When a request maps to a known workflow binding (by skill ID or template
ID), the execute path:

1. Loads the binding
2. Validates the caller's role against each step's required role
3. Fires each step in sequence, respecting `receiptRequired` per step
4. Returns a structured response that names the workflow, the steps
   executed, and the receipts emitted

When no binding exists for the request, the path falls back to the
current unstructured flow (backwards compatible).

**Files changed:**
- `cvf-web/src/lib/workflows/workflow-resolver.ts` — new; looks up
  binding by skill ID or template ID
- `cvf-web/src/app/api/execute/route.ts` — add binding lookup after AuthN;
  if binding found, use governed step dispatch; else use existing path
- `cvf-web/src/app/api/execute/route.test.ts` — add: bound request fires
  all steps; unbound request uses fallback path; receipt is emitted for
  steps with `receiptRequired: true`

**Live proof required:** YES. After this tranche, a `Create Product Brief`
request must:
- Resolve the `workflow.product.create_product_brief.v1` binding
- Fire all steps in sequence
- Emit at least one receipt tied to `receiptRequired: true`
- Return a response that includes `workflowId` and step receipts

Run with Alibaba API key. Record result in completion packet.

**GC-018 required:** Yes.

**Acceptance criteria:**
- Bound workflow request resolves correct binding
- All steps fire in order
- Receipt is emitted for `receiptRequired` steps
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

**Files to create or extend:**
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/receipt-binding.contract.ts`
  — `StepReceiptObligation`: maps `(CVFRole, ToolActionClass)` →
  `receiptRequired: boolean`; `buildStepReceipt(role, actionClass, stepId)`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/contracts.phaseE-receipt-binding.test.ts`
  — tests: BUILDER + `code_patch` requires receipt; OBSERVER + `observation`
  does not; receipt shape has required fields
- `cvf-web/src/app/api/execute/route.ts` — after step execution in E.4
  dispatch, call `emitStepReceipt` when obligation fires

**Live proof required:** Deterministic tests are sufficient. The E.4
live proof already exercises the receipt emit path.

**GC-018 required:** Yes.

**Acceptance criteria:**
- `StepReceiptObligation` covers all current `CVFRole` × `ToolActionClass` combinations
- Enforcement fires in E.4 workflow dispatch
- `row 8.2` in `CVF_LEGACY_CONCEPT_AXIS_MATRIX_2026-05-18.md` updated from
  `needs_gc018` to `partially_absorbed`

---

### Tranche E.6 — Phase E Closure and Chain Verification

**Purpose:** Verify the complete governed execution chain fires end-to-end
and close Phase E.

**Verification test:** Run one `Create Product Brief` request and confirm:

```
1. AuthN resolves caller → CVFRole (BUILDER)
2. getRolePermissionProfile(BUILDER) called → profile loaded
3. isOutputAllowedForRole(BUILDER, 'artifact') → true
4. Workflow binding resolved: workflow.product.create_product_brief.v1
5. Steps dispatched in order: intake → retrieval → provider → review → receipt
6. Provider call: Alibaba Qwen → governed receipt emitted
7. Step receipt emitted: BUILDER + artifact + step-3 → receipt persisted
8. Response includes: workflowId, stepReceipts[], governanceEnvelope
9. Audit event includes: role permission check result
10. All Phase D contracts called at least once in this flow
```

Every row in the E.1 audit table must show "wired" or "explicitly deferred."

**Output artifact:**
`docs/reviews/CVF_PHASE_E_CLOSURE_2026-05-18.md`

Update `CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`:
- "Role and agent governance": evidence link updated to include
  execution chain proof
- "Knowledge-backed execution": update evidence to cite E.4 workflow binding
- Run `Test-Path` on all catalog paths in public-sync before committing

---

## Tranche Dependency Order

```
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
|---|---|
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

- E.1 audit table exists and is fully populated
- E.2: role permission gate fires on every authenticated request
- E.3: `WorkflowBinding` type exported; `create_product_brief` binding validates
- E.4: bound workflow dispatches all steps; live Alibaba proof PASS; receipts emitted
- E.5: per-agent receipt obligation table covers all role × action combinations
- E.6: closure audit shows all 10 chain checkpoints firing in one real request
- No `needs_gc018` row in concept-axis matrix without deferral note
- Public catalog updated with chain proof evidence — Test-Path 100% in public-sync
- `system_reconvergence_stop` posture unchanged

## Work Plan

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
python governance/compat/check_governed_file_size_compat.py --base HEAD --head HEAD --enforce
python governance/compat/check_agent_handoff_guard_compat.py --base HEAD~1 --head HEAD --enforce
```

For tranches requiring live proof (E.4):

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

Phase E chain verification (E.6 only): run one live `Create Product
Brief` request and confirm all 10 checkpoints fire as listed in the
Tranche E.6 section.

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
