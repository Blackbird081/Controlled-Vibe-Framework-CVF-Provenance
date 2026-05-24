# CVF WC: Workflow Chain Proof and Pain Point Return Roadmap

Memory class: FULL_RECORD

Status: ACTIVE — WC-1/WC-2 CLOSED_PASS_BOUNDED; WC-3 CLOSED_MAPPING_ONLY; WC-4 CLOSED_CONTROL_ONLY; W1/W2 CLOSED_PASS_BOUNDED; W-series CONTINUES DEMAND_GATED

Date: 2026-05-24

---

## Purpose

Define the next implementation cycle following V1/V2/V3 closure. Three work
tracks are governed in execution order:

1. **WC-2** — Mock fallback elimination (truthful-only journey)
2. **WC-1** — End-to-end workflow chain proof (no new production surfaces;
   connect what exists with live evidence)
3. **WC-3** — Legacy harvest scan (combined mapping, not isolated audit
   tranches)
4. **WC-4** — Mandatory knowledge-absorption blind-spot prevention standard
   before any W-series implementation

This roadmap also records the operator's stated philosophy on legacy absorption
as binding guidance for all future implementation work.

---

## Authorization / Decision Basis

### Core Diagnosis (Operator-Stated 2026-05-24)

The recurring blind spot in CVF implementation is not unread specs — it is the
absence of end-to-end workflow chain execution. Surfaces get read, noted, and
partially absorbed, but never connected into a running loop with live evidence.

> "dù là 2 folder tưởng chừng đã audit rất kỹ như CVF 16.5, CVF ADD, thì vẫn
> bị bỏ sót, chỉ đọc xong rồi quên, hoàn toàn không được ghi nhận ở đâu để xử
> lý runtime đầy đủ, hoặc có ghi nhận thì cũng không có implement, KHÔNG CÓ
> CHẠY END TO END, TẠO WORKFLOW CHAIN."

Reading without running is not absorption. The gap is a closed loop: user input
→ memory read → governed execution → result written back → next turn builds on
it. CVF has never demonstrated this loop end-to-end with live evidence.

### Legacy Absorption Philosophy (Operator-Stated 2026-05-24)

> "scan qua các folder CVF 16.5, CVF ADD, CVF Edit kết hợp với những painpoint
> còn tồn từ review CVF --> lấy cho hết các kiến thức đã được code sẵn, thậm
> chí là từng file rất chi tiết, dung nạp vào CVF. Vừa nhanh, vừa hiệu quả
> hơn là tự audit, tự đi đào sâu giá trị từng tranche"

Rather than running isolated audit tranches that re-discover specs, perform a
combined scan of legacy folders + open Review CVF pain points to harvest all
pre-existing knowledge at once, then absorb it directly into CVF
implementation.

### On CVF_Important and CVF_Restructure

Operator confirmed 2026-05-24: these two folders are the architectural origin
of CVF's current structure. They are already absorbed into the existing
architecture. Re-auditing them for implementation value would be low-value
distraction. Skip unless the operator explicitly re-opens them.

### On V1/V2/V3 Closure (Context)

V1 (ProcessingScreen hardening), V2 (evidence packaging), and V3 (execution
diagnostic contract) are all `CLOSED_PASS_BOUNDED`. V1 left one open item:
mock fallback is still active for network-level failures where `executeReal()`
returns `false` without a parseable response. This is the input to WC-2.

---

## Scope

Owner: Operator (authorization); Codex (implementation, per-track GC-018).

Scope:

- WC-2: `src/components/ProcessingScreen.tsx` and
  `src/components/ProcessingScreen.test.tsx`
- WC-1: no new production runtime surfaces; a live proof script and a GC-018
  baseline document are expected evidence artifacts
- WC-3: documentation mapping exercise only; no source code changes
- WC-4: documentation/process control only; no source code changes

Out of scope for this roadmap:

- New provider behavior, new receipt-envelope fields, new memory tiers
- Hosted/cloud memory persistence
- Enterprise SaaS/GA readiness
- Global freeze lift
- Universal provider stability claims
- `canReinject=true`
- CVF_Important or CVF_Restructure re-audit

---

## Non-Goals

- No new governance surfaces or contract types
- No isolated per-folder audit tranches (operator-rejected pattern)
- No `canReinject=true`, no autonomous reinjection, no raw-memory prompt
  injection
- No hosted/cloud memory persistence claim
- No enterprise SaaS/GA readiness claim
- No broad production readiness claim
- No global freeze lift
- No universal provider stability claim
- No Maika child-data/photo/vision proof
- No CVF_Important or CVF_Restructure re-audit

---

## Work Plan

### WC-2: Mock Fallback Elimination (Truthful-Only Journey)

**Gate:** CLOSED_PASS_BOUNDED — Fast Lane localized corrective, no new
surface.

**Gap from V1:** V1 blocked mock fallback when a classified diagnostic exists.
But `executeReal()` returning `false` (network-level failures without a
parseable response) still triggers `generateMockOutput()` at
`src/components/ProcessingScreen.tsx:759`.

**Target behavior:** If a live call fails at any level, the user sees the
failure — not fabricated output.

Completed steps:

1. In `ProcessingScreen.tsx`: removed the mock fallback trigger in the
   `executeReal().then(success => { if (!success) { ... runMockExecution() } })`
   path; replaced it with a generic unclassified failure state when no diagnostic
   is available.
2. In `ProcessingScreen.test.tsx`: added assertion that no mock output is
   produced when `executeReal()` returns `false` after a live call attempt.
3. Focused ProcessingScreen tests PASS `23/23`.
4. Typecheck PASS.
5. Release gate PASS 7/7.

### WC-1: Workflow Chain Proof

**Gate:** CLOSED_PASS_BOUNDED.

**Existing surfaces to wire (no new runtime surface expected):**

| Surface | Status | Location |
| --- | --- | --- |
| M1 durable memory read | CLOSED_PASS | `durable-memory-route.ts` |
| S1 durable memory write | CLOSED_PASS | `evaluateDurableMemoryWrite()` |
| `/api/execute` route | LIVE | `src/app/api/execute/route.ts` |
| V3 execution diagnostics | CLOSED_PASS | `execution-diagnostics.ts` |
| Receipt envelope | LIVE | `GovernanceEvidenceReceipt` |

Completed steps:

1. Wrote a live probe script that sends two sequential calls:
   - Call 1: standard skill execution with `durableMemoryWrite.enabled=true`
   - Call 2: reads prior session context, references call 1 receipt
2. Verified: call 1 receipt includes `durableMemoryWriteReceipt`
3. Verified: call 2 durable-memory read receipt shows allowed read with
   `memoryIds` and summary-only context injection. Model output may be
   supportive evidence, but it is not sufficient by itself.
4. Confirmed `rawMemoryReleased=false`, `canReinject=false`, `evidenceMode=live`,
   `rawSecretPrinted=false`
5. Filed completion review under `docs/reviews/`

### WC-3: Legacy Harvest Scan

**Gate:** CLOSED_MAPPING_ONLY — operator authorized after DeepSeek rerun.

**Method:** Single combined mapping exercise across:

1. `.private_reference/legacy/CVF 16.5/` — all files
2. `.private_reference/legacy/CVF ADD/` — all files
3. `.private_reference/legacy/CVF Edit/` — Review CVF 1 through 5,
   Failure Simulation, De_xuat

**Cross-reference:** open pain points from Review CVF.md that remain
unaddressed or partially addressed.

**Output:** One mapping document listing:

- Pre-existing knowledge per file (implemented vs. not implemented)
- Pain point mapping per legacy file
- Ranked absorption candidates (highest value first)

Completed output:

- `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md`
- `docs/reviews/CVF_WC3_LEGACY_HARVEST_SCAN_COMPLETION_2026-05-24.md`

No new implementation work was opened during the scan itself. Scan output
becomes the input to future work orders.

### W-Series: Return to Real User Pain Points

**Gate:** DEMAND_GATED — depends on WC-3 scan output for prioritization.
Pre-condition: WC-1 must be closed first and WC-4 blind-spot control must be
applied to any knowledge-absorption or legacy-adjacent implementation scope.

**Method:** W-series work orders drawn from WC-3 mapping output, not from
new audits. Each W-series work order must include the Knowledge Absorption
Blind-Spot Control Block from
`docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`.

#### W1: Workflow State-Machine Enforcement

**Gate:** CLOSED_PASS_BOUNDED.

Completed output:

- `docs/baselines/CVF_GC018_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_2026-05-24.md`
- `docs/work_orders/CVF_WO_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_2026-05-24.md`
- `docs/reviews/CVF_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_COMPLETION_2026-05-24.md`

Result:

- added `cvf.workflowStateMachineProjection.v1` to the existing Product Brief
  workflow execution projection;
- Product Brief now ends at `review_pending` when reviewer gate step 4 is
  deferred;
- step 5 receipt emission is also deferred because its `freeze_ready` state is
  unreachable;
- only completed reachable steps emit workflow step receipts;
- route audit event includes `stateMachine`.

Verification:

- focused resolver/route tests PASS `34/34`;
- `cvf-web` TypeScript check PASS;
- live Phase E workflow-binding spec PASS with receipt
  `rcpt-env-mpjx22ch-aee3y6` and workflow audit event
  `c8d04faa-8474-4d02-beae-2c5519d179d2`;
- mandatory release gate PASS `7/7`.

Next ranked candidate:

- Candidate 2 from the WC-3 map: memory event hooks plus context packager
  hardening. It remains demand-gated and requires a fresh GC-018/work order
  with the Knowledge Absorption Blind-Spot Control Block. Preserve
  `canReinject=false`; do not open raw reinjection.

#### W2: Memory Event Hooks + Context Packager Hardening

**Gate:** CLOSED_PASS_BOUNDED.

Authorization:

- `docs/baselines/CVF_GC018_W2_MEMORY_EVENT_HOOKS_CONTEXT_PACKAGER_2026-05-24.md`
- `docs/work_orders/CVF_WO_W2_MEMORY_EVENT_HOOKS_CONTEXT_PACKAGER_2026-05-24.md`
- `docs/reviews/CVF_W2_MEMORY_EVENT_HOOKS_CONTEXT_PACKAGER_COMPLETION_2026-05-24.md`

Bounded target:

- local Learning Plane Foundation memory event-hook classification;
- summary-only context package evidence metadata;
- focused LPF tests and exports.

Boundary:

- no `/api/execute`, provider behavior, governance evidence receipt envelope,
  auth/RBAC, durable/cloud persistence, MCP/tool hooks, public-sync,
  production readiness, freeze release, raw memory prompt injection, or
  `canReinject=true`.

Verification:

- focused LPF tests PASS `11/11`;
- LPF TypeScript check PASS;
- governed file size guard PASS.

Next ranked candidate:

- Candidate 3 from WC-3: tool/MCP/database action governance map. It remains
  demand-gated and should start as read-only taxonomy only.

### WC-4: Knowledge Absorption Blind-Spot Standard

**Gate:** CLOSED_CONTROL_ONLY — doc/process control, no runtime surface.

**Reason:** The first post-WC3 step is to prevent future agents from skipping
detailed legacy source files or treating WC-3's map as implementation
authorization.

Completed output:

- `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md`
- `docs/baselines/CVF_GC018_WC4_KNOWLEDGE_ABSORPTION_BLINDSPOT_STANDARD_2026-05-24.md`
- `docs/work_orders/CVF_WO_WC4_KNOWLEDGE_ABSORPTION_BLINDSPOT_STANDARD_2026-05-24.md`
- `docs/reviews/CVF_WC4_KNOWLEDGE_ABSORPTION_BLINDSPOT_STANDARD_COMPLETION_2026-05-24.md`

Binding result:

- future knowledge-absorption and legacy-adjacent tranches must complete source
  inventory, prior absorption resolution, file-level value extraction,
  owner-surface normalization, accept/defer/reject disposition, adversarial
  role review, and thin proof/closure delta before implementation.

---

## Acceptance Criteria

### WC-2

- [x] `generateMockOutput()` is never called when `executeReal()` returns
      `false` after a live call attempt
- [x] Failure state renders a user-visible message instead of fabricated output
- [x] Existing success path and V1 diagnostic panel remain intact
- [x] Focused ProcessingScreen tests PASS `23/23`
- [x] Typecheck PASS
- [x] Release gate PASS 7/7

### WC-1

- [x] Live receipt from turn 1 includes `durableMemoryWriteReceipt`
- [x] Live receipt from turn 2 confirms prior session context retrieval through
      durable-memory read evidence (`memoryIds`, summary-only, injected context)
- [x] `rawMemoryReleased=false` in both receipts
- [x] `canReinject=false` preserved (compile-time literal unchanged)
- [x] `evidenceMode=live` on both calls
- [x] `rawSecretPrinted=false`
- [x] Completion review filed under `docs/reviews/`

### WC-3

- [x] Mapping document covers all files in CVF 16.5, CVF ADD, CVF Edit
- [x] Each source family states implemented / not implemented / partial
- [x] Pain point cross-reference complete
- [x] No source code changes committed during scan

### WC-4

- [x] Binding anti-blindspot standard created
- [x] GC-018 template updated with Knowledge Absorption Blind-Spot Control Block
- [x] AGENTS updated with mandatory rule
- [x] W-series precondition updated
- [x] No runtime/source-code behavior changed

---

## Verification / Evidence

| Track | Evidence | Location |
| --- | --- | --- |
| WC-2 | Focused test run + release gate | `docs/reviews/CVF_WC2_MOCK_FALLBACK_ELIMINATION_COMPLETION_2026-05-24.md` |
| WC-1 | Live probe script + two receipts | `docs/reviews/CVF_WC1_WORKFLOW_CHAIN_PROOF_COMPLETION_2026-05-24.md` |
| WC-3 | Mapping document | `docs/reference/CVF_LEGACY_HARVEST_SCAN_MAP_2026-05-24.md` |
| WC-4 | Binding anti-blindspot standard | `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md` |
| W1 | Product Brief workflow state-machine projection + live proof | `docs/reviews/CVF_W1_WORKFLOW_STATE_MACHINE_ENFORCEMENT_COMPLETION_2026-05-24.md` |
| W2 | Memory event hooks + context packager hardening | `docs/reviews/CVF_W2_MEMORY_EVENT_HOOKS_CONTEXT_PACKAGER_COMPLETION_2026-05-24.md` |

---

## Sequencing

```text
WC-2 (mock fallback elimination)  <- Fast Lane, can start now
  |
WC-1 (workflow chain proof)       <- Closed pass bounded
  |
WC-3 (legacy harvest scan)        <- Closed mapping only
  |
WC-4 (blind-spot control law)     <- Closed control only
  |
W1 (workflow state projection)    <- Closed pass bounded
  |
W2 (memory hook/context package)   <- Closed pass bounded
  |
W-series next candidates          <- Demand-gated; fresh GC-018 required
```

---

## Related Artifacts

| Document | Purpose |
| --- | --- |
| `docs/reviews/CVF_V1_NONCODER_FIRST_VALUE_JOURNEY_HARDENING_COMPLETION_2026-05-24.md` | V1 closure — source of WC-2 gap |
| `docs/reviews/CVF_V3_EXECUTION_DIAGNOSTIC_CONTRACT_COMPLETION_2026-05-24.md` | V3 closure — diagnostic foundation for WC-1 |
| `docs/reviews/CVF_S1_DURABLE_MEMORY_WRITE_ROUTE_COMPLETION_2026-05-24.md` | S1 closure — memory write surface for WC-1 |
| `docs/audits/CVF_LEGACY_SPEC_ABSORPTION_BLINDSPOT_AUDIT_2026-05-23.md` | Original blindspot audit — context for WC-3 |
| `docs/reference/CVF_LEGACY_SPEC_ABSORPTION_REGISTRY_2026-05-23.md` | Full registry — WC-3 scan starting point |
| `docs/reference/CVF_KNOWLEDGE_ABSORPTION_BLINDSPOT_PREVENTION_STANDARD_2026-05-24.md` | Mandatory anti-blindspot law for future absorption |
| Memory: `project_operator_absorption_philosophy_2026-05-24.md` | Operator philosophy — decision basis for this roadmap |

---

## Claim Boundary

WC-2 claims truthful failure recovery for implemented execution paths only. It
does not claim universal provider stability, hosted readiness, production
readiness, or new governance authority.

WC-1 claims a single end-to-end workflow chain proof using existing surfaces
only. It does not claim cross-session memory persistence, hosted/cloud
persistence, autonomous reinjection, or broad production readiness.

WC-3 claims a mapping document. It does not claim implementation of any
absorbed knowledge, nor does it open new tranches.

WC-4 claims a mandatory process control for future knowledge absorption. It
does not claim implementation of any absorbed knowledge, source-code runtime
change, public capability, or production readiness.

W1 claims only one selected Product Brief workflow state-machine projection. It
does not claim route-level invalid-transition blocking, a broad workflow
engine, reviewer UI, recovery orchestration, provider behavior, auth/RBAC,
receipt-envelope semantics, public capability, hosted readiness, production
readiness, or freeze release.

No track in this roadmap claims `canReinject=true`, global freeze lift,
enterprise SaaS readiness, or universal provider parity.
