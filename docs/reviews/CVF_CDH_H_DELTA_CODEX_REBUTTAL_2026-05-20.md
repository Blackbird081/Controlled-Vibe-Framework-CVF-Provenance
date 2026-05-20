# CVF CDH-H Delta Codex Rebuttal

Memory class: FULL_RECORD

Status: REBUTTAL_FILED_NON_BLOCKING_WITH_READOUT_SCOPE

Reviewer: Codex

Date: 2026-05-20

---

## Purpose

File the reviewer-only rebuttal for CDH-H in the CDH delta meta-roadmap.

This rebuttal decides whether the remaining memory-governance delta can move
forward. It does not authorize implementation, GC-018 execution, new memory
tiers, memory reinjection, persistent/archive memory, or provider-side memory
behavior.

---

## Scope / Target / Owner Boundary

In scope:

- `docs/roadmaps/CVF_CDH_DELTA_META_ROADMAP_2026-05-20.md`
- `docs/work_orders/CVF_WO_CDH_H_DELTA_REBUTTAL_2026-05-20.md`
- `docs/reviews/CVF_H2_AUDIT_MEMORY_POLICY_REFINEMENT_COMPLETION_2026-05-19.md`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/audit-memory-receipt.test.ts`

Out of scope:

- memory reinjection;
- persistent/archive memory enablement;
- new memory tier semantics;
- provider-side memory;
- route expansion beyond an explicit future GC-018;
- using `reinjectionAllowed` as a memory-capture write gate.

---

## Target / Source Under Review

Queue item:

- `cdh-h-delta`

Expected response path:

- `docs/reviews/CVF_CDH_H_DELTA_CODEX_REBUTTAL_2026-05-20.md`

Prior closure evidence:

- `docs/reviews/CVF_H2_AUDIT_MEMORY_POLICY_REFINEMENT_COMPLETION_2026-05-19.md`

---

## Scope / Methodology

Method:

1. Reviewed the H2 closure packet and its explicit claim boundary.
2. Re-read the audit-memory source and tests for write-gate and reinjection
   invariants.
3. Compared the remaining CDH-H delta against what is already closed.
4. Classified only the residual work that may proceed after a fresh
   slice-specific GC-018.

No live governance proof was run for this rebuttal. This is a reviewer packet,
not a runtime closure packet.

---

## Findings / Position

Position: **NON_BLOCKING_WITH_READOUT_SCOPE**.

Findings:

1. H2 already closed the core policy-field surfacing delta. The
   `AuditMemoryReceipt` type and returned object include
   `writesRequireReceipt` and `privacyFilters`.
2. The no-reinjection invariant is preserved. Source review confirms the
   capture call still passes `canReinject: false`.
3. `reinjectionAllowed` is not present in
   `audit-memory-receipt.ts`; it is not being used as a write gate.
4. The remaining useful CDH-H continuation is a narrow readout/proof delta:
   make the policy metadata and degraded-capture reason easier to observe in
   audit/readout evidence, then prove the existing route with a live governed
   call if a future GC-018 asks for that proof.
5. CDH-H must not be converted into broader memory-product work. The rebuttal
   accepts only audit-memory policy/readout hardening around the already
   existing session-memory path.

---

## Risk / Defect / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Reviewer treats H2 as runtime memory expansion | Keep the claim boundary at audit-memory receipt/readout only |
| Future work uses `reinjectionAllowed` as a write gate | Preserve `canReinject=false`; add/retain tests proving no `reinjectionAllowed` write gate |
| Readout evidence is hard to inspect from route-level audit output | A future GC-018 may add readout fields for `writesRequireReceipt`, `privacyFilters`, receipt decision, and degraded reason |
| Local tests are mistaken for live route proof | Any future runtime claim must use a real provider/API path and file a separate closure packet |

---

## Decision / Recommendation / Disposition

Disposition: **NON_BLOCKING_WITH_READOUT_SCOPE**.

CDH-H may proceed only as a fresh slice-specific GC-018 and work order for
audit-memory policy/readout proof. Acceptable future work is limited to:

- surfacing or preserving the existing policy fields in route-level readout or
  audit evidence;
- proving `writesRequireReceipt=true` and privacy-filter visibility on the
  existing session-memory receipt path;
- proving degraded-capture behavior without enabling reinjection;
- proving `canReinject=false` remains binding.

CDH-H is not authorized to add memory reinjection, new memory classes,
persistent/archive memory, provider memory, or new capture semantics.

---

## Claim Boundary

This rebuttal may be cited as:

> CDH-H is non-blocking only for narrow audit-memory readout/proof hardening.
> H2 already preserves `canReinject=false` and does not use
> `reinjectionAllowed` as a write gate.

This rebuttal must not be cited as:

> CVF has implemented memory reinjection, persistent memory, archive memory,
> provider memory, or a new memory governance runtime.

