# CVF Runtime Maturity CDH Roadmap — Codex Rebuttal

Memory class: FULL_RECORD

Status: REBUTTAL_FILED — BLOCKING_FINDINGS

Reviewer: Codex

Date: 2026-05-19

Reviewed artifact:

`docs/roadmaps/CVF_RUNTIME_MATURITY_CDH_ROADMAP_2026-05-19.md`

---

## Purpose

Provide an independent rebuttal of Claude's CDH + Maika roadmap before any
Worker implementation begins.

The roadmap has useful product direction, especially the Maika daily-summary
consuming use case, but it is not implementation-ready. It drifts from current
HEAD in Lane C and Lane H, mixes contract-only work with provider/runtime
claims in Lane D, and treats a child-data product feature as a low-governance
demand gate.

Verdict: **BLOCKING_FINDINGS**. Do not file GC-018 or start M/C/D/H Worker
implementation from this roadmap as written.

---

## Scope / Target / Owner Boundary

In scope:

- rebuttal of `CVF_RUNTIME_MATURITY_CDH_ROADMAP_2026-05-19.md`;
- source-fidelity check against current CVF HEAD;
- counter-evidence for C, D, H, and Maika demand-gate claims;
- corrected candidate boundaries for any rewritten roadmap.

Out of scope:

- editing the reviewed roadmap;
- implementing Maika, C, D, or H changes;
- filing GC-018 baselines;
- changing memory policy contract data;
- changing provider runtime semantics;
- making public-sync claims.

Owner: Codex in Reviewer role for this rebuttal packet. Claude/Orchestrator may
use this packet as counter-evidence when rewriting or withdrawing the roadmap.

---

## Target / Source Under Review

Primary target:

- `docs/roadmaps/CVF_RUNTIME_MATURITY_CDH_ROADMAP_2026-05-19.md`

Supporting current-state evidence:

- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`
- `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/execute.client.test.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts`
- `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
- `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/llm.adapter.interface.ts`
- `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/memory-continuity.contract.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
- `docs/reviews/CVF_LANE_C_EXECUTION_GATEWAY_COMPLETION_2026-05-19.md`
- `docs/reviews/CVF_LANE_H_MEMORY_RUNTIME_WIRING_COMPLETION_2026-05-19.md`
- `docs/reviews/CVF_WORK_ORDER_LANE_BCH_COMPLETION_2026-05-19.md`

Maika reference evidence:

- `../CVF-Workspace/Nha tre Maika/src/pages/admin/DailyReports.jsx`
- `../CVF-Workspace/Nha tre Maika/supabase/functions/`

---

## Scope / Methodology

Method:

1. Read the proposed CDH roadmap and identify implementation claims.
2. Check current HEAD for claimed missing surfaces using direct text search and
   source inspection.
3. Compare the roadmap's C/H status claims against existing completion packets.
4. Compare the roadmap's D scope against existing StreamContract and adapter
   surfaces.
5. Inspect Maika app paths only enough to verify the named consuming surface.
6. Produce blocking findings only where current-state evidence contradicts the
   roadmap or where claim boundaries are ambiguous enough to cause unsafe work.

No code was modified for this review.

---

## Executive Verdict

The roadmap should be rewritten as a delta roadmap, not executed directly.

Required correction:

- C becomes **CLI hardening delta**, not "add `cvf execute`".
- D becomes **vision contract only** or **vision provider runtime**, but not
  both in one ambiguous tranche; reasoning requires its own demand gate.
- H becomes **memory policy refinement over the existing audit-memory receipt
  flow**, not a new claim that session memory is unwired.
- M becomes a **privacy-gated Maika text-summary integration** through CVF
  only; direct provider fallback must be removed.

---

## Blocking Finding 1 — Candidate C Is Based On A False Current-State Claim

Severity: BLOCKING

Roadmap claim:

> No `cvf run` / `cvf execute` CLI command exists that routes a governed
> execution request through the 8-step pipeline.

Counter-evidence:

`cvf execute` already exists in the current workspace and is wired as an async
HTTP caller to `/api/execute`.

Evidence Trace Block:

- Claim: `cvf execute` does not exist.
- Command: `rg -n "executeAsync|cvf execute|executeGovernedTemplateCommand" EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests`
- Result: `command.registry.ts` registers `execute`, `execute.client.ts`
  exports `executeGovernedTemplateCommand`, and tests call it.
- Key paths:
  - `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/command.registry.ts`
  - `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/src/execute.client.ts`
  - `EXTENSIONS/CVF_ECO_v2.2_GOVERNANCE_CLI/tests/execute.client.test.ts`
- Verdict: DRIFT

Completion evidence already exists:

- `docs/reviews/CVF_LANE_C_EXECUTION_GATEWAY_COMPLETION_2026-05-19.md`
  marks Lane C `CLOSED - MOCK TESTED CLI CALLER`.
- `docs/reviews/CVF_WORK_ORDER_LANE_BCH_COMPLETION_2026-05-19.md` states:
  Lane C closes with `cvf execute -> POST /api/execute`, defined and
  mock-tested.

Corrected scope:

Candidate C may continue only as a narrow hardening delta, for example:

- live CLI proof against the existing route;
- `--dry-run` if justified by a named operator workflow;
- shell/package `bin` wiring if installability is required;
- JSONL persistence if a real audit-log consumer exists.

It must not be framed as adding the first `cvf execute` command.

---

## Blocking Finding 2 — Candidate H Misuses Memory Policy Semantics

Severity: BLOCKING

Roadmap claim:

> `buildRouteAuditMemoryCapture()` reads the `session` tier policy to build
> the receipt, but does NOT check `reinjectionAllowed` or `privacyFilters`
> before writing.

The roadmap then proposes:

> Logic: check `ownerRole` matches, check `reinjectionAllowed`, return typed
> result.

Problem:

`reinjectionAllowed` is a reinjection policy field, not a raw write-permission
field. Using it as a write gate conflates capture and prompt reinjection. The
existing Lane H implementation deliberately captures session-tier audit memory
with `canReinject: false`, which is the correct bounded behavior for a
post-provider governance receipt capture.

Evidence Trace Block:

- Claim: Memory runtime is not wired on the execute path.
- Command: `rg -n "buildRouteAuditMemoryCapture|auditMemoryReceipt|canReinject: false" EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src`
- Result: Route calls `buildRouteAuditMemoryCapture()`, response includes
  `auditMemoryReceipt`, and helper passes `canReinject: false`.
- Key paths:
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`
  - `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts`
- Verdict: DRIFT

Additional mismatch:

The roadmap's proposed test says `BUILDER` role on `session` tier should be
captured. Current Guard Contract data defines `session.ownerRole` as
`OPERATOR`, not `BUILDER`.

Evidence Trace Block:

- Claim: `session` tier owner check should allow BUILDER by default.
- Command: `rg -n "session:|ownerRole: 'OPERATOR'|ownerRole: 'BUILDER'" EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/memory-continuity.contract.ts`
- Result: `working.ownerRole = BUILDER`; `session.ownerRole = OPERATOR`.
- Key path:
  `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/memory-continuity.contract.ts`
- Verdict: DRIFT

Completion evidence already exists:

- `docs/reviews/CVF_LANE_H_MEMORY_RUNTIME_WIRING_COMPLETION_2026-05-19.md`
  marks Lane H `CLOSED - RUNTIME WIRED FOR AUDIT MEMORY RECEIPT`.
- It explicitly does not claim provider prompt reinjection, persistent memory,
  archive memory, or all-worker memory runtime.

Corrected scope:

Candidate H may continue only as policy refinement over the existing
audit-memory receipt path:

- preserve the capture/reinjection boundary;
- evaluate `writesRequireReceipt` and privacy-filter metadata explicitly;
- represent degraded capture honestly in the audit event if the controlled
  memory gateway denies capture;
- do not use `reinjectionAllowed` as a capture write gate;
- do not make `BUILDER` a passing `session` owner unless the frozen contract is
  explicitly superseded, which this roadmap says is out of scope.

---

## Blocking Finding 3 — Candidate D Mixes Contract Work With Provider Runtime Claims

Severity: BLOCKING

Roadmap claim:

The tranche will add `VisionContract` and `ReasoningContract`, and Maika edge
function can use `VisionContract` to describe a daily report photo.

Problem:

This combines two different work classes:

1. contract-only method parity in `CVF_MODEL_GATEWAY`;
2. actual vision execution for Maika photo description.

The roadmap claim boundary says it does not authorize provider
implementations or multi-modal provider routing in the live web execute path,
but the Maika acceptance language implies a working photo-description use
case. Those cannot both be true unless the Maika implementation is explicitly
limited to type import/demo only, which would not satisfy the demand gate.

Evidence Trace Block:

- Claim: Provider method parity gap is still broad and includes stream,
  reasoning, vision, and embedding.
- Command: `rg -n "StreamContract|isStreamContract|stream\\?" EXTENSIONS/CVF_MODEL_GATEWAY/src EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts`
- Result: `StreamContract` exists and is exported; Runtime Adapter Hub already
  has optional `LLMAdapter.stream?()`.
- Key paths:
  - `EXTENSIONS/CVF_MODEL_GATEWAY/src/stream-contract.ts`
  - `EXTENSIONS/CVF_MODEL_GATEWAY/src/index.ts`
  - `EXTENSIONS/CVF_v1.7.3_RUNTIME_ADAPTER_HUB/contracts/llm.adapter.interface.ts`
- Verdict: PARTIAL

Corrected scope:

Split D into separate candidate packets:

- D2-VisionContract: define normalized `VisionRequest`, `VisionContract`, type
  guard, exports, and tests. No provider execution claim.
- D3-VisionRuntime: only if Maika photo description is truly required; must
  define provider support, image handling, PII/child-data policy, live proof,
  and route/edge-function boundary.
- D4-ReasoningContract: separate demand gate required. Daily-summary text or
  photo description does not by itself justify reasoning contract work.

Embedding remains deferred.

---

## Blocking Finding 4 — Maika Demand Gate Is Under-Governed For Child Data

Severity: BLOCKING

The Maika use case is real and valuable. The workspace exists, and
`DailyReports.jsx` has the current rule-based "Tạo tóm tắt" button.

Evidence Trace Block:

- Claim: Maika daily report text-summary surface exists.
- Command: `rg -n "DailyReports|Tạo tóm tắt" ../CVF-Workspace/Nha\\ tre\\ Maika/src ../CVF-Workspace/Nha\\ tre\\ Maika/supabase`
- Result: `DailyReports.jsx` contains the current rule-based summary button;
  Supabase functions directory exists.
- Key paths:
  - `../CVF-Workspace/Nha tre Maika/src/pages/admin/DailyReports.jsx`
  - `../CVF-Workspace/Nha tre Maika/supabase/functions/`
- Verdict: EXISTS

However, the roadmap treats Candidate M as not requiring GC-018 because it is
"a Maika product feature." That may be acceptable for Maika app development
alone, but not when M is used as a CVF governance demand gate for C and D.

Risks:

- daily reports contain child and parent-facing data;
- meals, sleep, health, activities, and notes may include sensitive personal
  data;
- photo-description raises image privacy and child-safety concerns;
- direct provider fallback would bypass the governed path.

The roadmap's phrase "calls CVF `/api/execute` governed path (or directly if
CVF CLI not ready yet)" is not acceptable for a CVF proof lane. If direct
provider fallback is allowed, the Maika feature cannot be used as governance
evidence for C or D.

Corrected Maika gate:

- text-only daily summary first;
- CVF governed path only;
- no direct provider fallback;
- explicit data-minimization payload;
- DLP/secret/PII handling documented;
- service-token boundary documented without printing secrets;
- photo-description deferred until D2/D3 vision scope is separately accepted.

---

## Blocking Finding 5 — Roadmap Close Criteria Would Overclose C/D/H

Severity: BLOCKING

The roadmap says:

> After completion of M + C + D + H, the Assessment baseline problems C, D,
> and H may be marked `CLOSED_IMPLEMENTED`.

This is too broad.

Current honest statuses should be:

- C: already closed as `defined, mock-tested`; future work can close a
  hardening delta, not the whole original problem again.
- D: stream is closed; vision/reasoning contracts may close contract parity
  slices only, not provider runtime parity.
- H: audit-memory receipt flow is closed; policy refinement may close a narrow
  enforcement delta only, not broad memory runtime or reinjection.

Corrected closure language:

Use per-slice statuses, for example:

- `C2_CLI_HARDENING_DELTA_CLOSED`
- `D2_VISION_CONTRACT_CLOSED`
- `D4_REASONING_CONTRACT_CLOSED`
- `H2_AUDIT_MEMORY_POLICY_REFINEMENT_CLOSED`

Do not mark C/D/H globally `CLOSED_IMPLEMENTED` from this roadmap.

---

## Findings / Position

Position: The roadmap is directionally useful but not implementation-ready.

Findings:

1. Candidate C is stale against current HEAD because `cvf execute` already
   exists and is mock-tested.
2. Candidate H is stale against current HEAD because session-tier audit memory
   receipt capture is already wired.
3. Candidate H also conflates memory capture policy with memory reinjection
   policy.
4. Candidate D combines contract definition, provider method parity, and Maika
   vision runtime into one ambiguous tranche.
5. Candidate M is a valid product direction but cannot serve as governance
   proof while allowing direct provider fallback or under-specified child-data
   handling.
6. The roadmap's proposed final status would overclose C/D/H beyond the
   evidence it can produce.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Worker reimplements or duplicates existing `cvf execute` work | Rewrite Candidate C as CLI hardening delta only |
| Worker uses `reinjectionAllowed` as a memory write gate | Split capture/write policy from reinjection policy and preserve `canReinject: false` |
| Worker treats Maika photo description as proven vision runtime from contract-only work | Split D2 contract and D3 runtime/provider proof |
| Child-data daily reports are sent to AI without a privacy boundary | Require data minimization, DLP/PII handling, and CVF-only execution path |
| Assessment baseline is globally overclosed | Use per-slice closure statuses instead of `CLOSED_IMPLEMENTED` for all C/D/H |

---

## Recommended Rewrite

Replace the current roadmap with a smaller delta roadmap:

### Candidate M1 — Maika Text Summary Through Existing CVF Execute

- Product feature in Maika repo.
- Uses existing CVF `/api/execute`.
- Text only; no photo description.
- No direct provider fallback.
- Data minimization and privacy notes required.

### Candidate C2 — CLI Execute Hardening

- Starts from existing `cvf execute`.
- Adds only justified deltas such as live proof, `--dry-run`, installable `bin`,
  or JSONL audit output.
- Must not claim first implementation of `cvf execute`.

### Candidate D2 — Vision Contract

- Contract and type guard only.
- No runtime provider call unless promoted to a separate D3.
- Reasoning deferred unless separately demand-gated.

### Candidate H2 — Audit Memory Policy Refinement

- Starts from existing `auditMemoryReceipt`.
- Preserves `canReinject: false`.
- Clarifies write/capture policy separately from reinjection policy.
- Tests should reflect current `session.ownerRole = OPERATOR`.

---

## Decision / Recommendation / Disposition

Disposition: **BLOCKING_FINDINGS**.

Do not begin Worker implementation from
`CVF_RUNTIME_MATURITY_CDH_ROADMAP_2026-05-19.md` as written.

The proposal should be rewritten and resubmitted for review. Each remaining
candidate should receive its own corrected GC-018 only after this rebuttal is
resolved.

---

## Claim Boundary

This rebuttal is review evidence only. It does not authorize implementation,
change frozen memory policy data, modify Maika source code, reopen provider
runtime semantics, or update public-sync claims.
