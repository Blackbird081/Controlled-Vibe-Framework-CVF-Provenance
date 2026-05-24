# CVF Post-AIF Claim Graduation Roadmap

Memory class: SUMMARY_RECORD

Status: ACTIVE_C1_CLOSED_C2_C5_NEXT_TRANCHE_REQUIRED

docType: roadmap

Date: 2026-05-24

---

## Purpose

Convert the remaining Post-AIF non-claims into explicit claim-graduation
conditions. Complete any claim that can be closed immediately and move the rest
into fresh tranches rather than leaving ambiguous blockers.

---

## Authorization / Decision

Operator directed on 2026-05-24: complete the conditions needed for the listed
claims if feasible, otherwise move them to a new tranche.

Decision:

- C1 public runtime availability for the preview harness is feasible now and is
  CLOSED_PASS.
- C2 live memory reinjection, C3 graph authority, C4 broad provider stability,
  and C5 hosted/production readiness are not safe to claim from the current
  evidence and must proceed through fresh GC-018 work orders.

---

## Owner / Source

Owner: Codex multi-role execution.

Sources:

- `docs/reference/CVF_POST_AIF_OPERATIONAL_READINESS_MATRIX_2026-05-24.md`
- `docs/roadmaps/CVF_POST_AIF_OPERATIONALIZATION_ROADMAP_2026-05-24.md`
- `docs/reviews/CVF_C1_PUBLIC_AIF_PREVIEW_RUNTIME_AVAILABILITY_COMPLETION_2026-05-24.md`

---

## Scope / Target / Owner Boundary

In scope:

- Claim-gate the five operator-named claim families.
- Close C1 through public-sync code availability and tests.
- Define exact pass conditions for C2-C5.

Out of scope until their own fresh GC-018:

- live `/api/execute` memory reinjection;
- graph-governed approval authority;
- broad provider stability certification;
- hosted SaaS readiness;
- production readiness.

---

## Non-Goals

This roadmap does not use documentation alone to convert a non-claim into a
claim. Runtime and ops claims require live proof.

---

## Role Execution Model

| Role | Responsibility | Disposition |
| --- | --- | --- |
| Planner | Split feasible public code availability from runtime/ops claims. | CLOSED for C1, staged for C2-C5. |
| Governance Reviewer | Preserve no-overclaim boundaries. | CLOSED for C1. |
| Implementer | Publish C1 public-sync code. | CLOSED_PASS. |
| QA | Verify C1 public-sync LPF tests and TypeScript. | CLOSED_PASS. |
| Release Manager | Commit public-sync and record provenance. | CLOSED_PASS. |

---

## Work Plan

| Tranche | Claim target | Status | Required pass condition |
| --- | --- | --- | --- |
| C1 | Public runtime availability for preview harness | `CLOSED_PASS` | Public-sync code, exports, targeted test, TypeScript check, full LPF suite, public-safe catalog/evidence. |
| C2 | Live memory reinjection | `NEXT_TRANCHE_REQUIRED` | Fresh GC-018; route-level opt-in; policy gate; summary-only prompt injection; receipt field proving injected memory ids; live provider E2E; negative tests for unauthorized/secret/disputed memory. |
| C3 | Graph authority | `NEXT_TRANCHE_REQUIRED` | Fresh GC-018; authority model separating advisory graph evidence from governance decision; scoring thresholds; audit receipts; deny/allow tests; proof graph cannot bypass policy. |
| C4 | Broad provider stability | `NEXT_TRANCHE_REQUIRED` | Fresh GC-018; preregistered tri-provider matrix; minimum sample window and cooldown; live receipts across Alibaba, DeepSeek, OpenAI; failure classification; release-gate PASS. |
| C5 | Hosted/production readiness | `NEXT_TRANCHE_REQUIRED` | Fresh GC-018; hosted environment checklist; secrets/keys/observability; live hosted smoke; rollback and incident packet; security/release gate; public claim packet. |

---

## Acceptance Criteria

- [x] C1: public-sync remote checked.
- [x] C1: preview harness and dependencies published in public-sync.
- [x] C1: targeted preview test passed.
- [x] C1: public-sync LPF TypeScript check passed.
- [x] C1: public-sync full LPF suite passed.
- [x] C1: public-sync catalog/evidence updated and committed.
- [x] C2-C5: pass conditions explicitly defined instead of silently claimed.

---

## Progress Tracker

| Tranche | Status | Evidence |
| --- | --- | --- |
| C1 | `CLOSED_PASS` | `docs/reviews/CVF_C1_PUBLIC_AIF_PREVIEW_RUNTIME_AVAILABILITY_COMPLETION_2026-05-24.md`; public commit `ea889a46` |
| C2 | `NEXT_TRANCHE_REQUIRED` | Fresh GC-018 required before implementation. |
| C3 | `NEXT_TRANCHE_REQUIRED` | Fresh GC-018 required before implementation. |
| C4 | `NEXT_TRANCHE_REQUIRED` | Fresh GC-018 required before live soak. |
| C5 | `NEXT_TRANCHE_REQUIRED` | Fresh GC-018 required before hosted/production claim. |

---

## Verification / Evidence

C1 public-sync verification:

- Targeted preview test: PASS, 1 file / 4 tests.
- LPF TypeScript check: PASS.
- Full LPF public-sync suite: PASS, 48 files / 1516 tests.
- Public-sync commit:
  `ea889a46 feat(lpf): publish aif context preview harness`.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| C1 is mistaken for live route integration. | Evidence says local summary-only harness; no provider prompt injection. |
| C2 is rushed and leaks raw memory into prompts. | Require summary-only packaging, privacy filters, negative tests, and live receipt evidence. |
| C3 turns graph evidence into policy bypass. | Require authority model and tests proving policy remains dominant. |
| C4 overclaims after a small sample. | Require preregistered sample window and provider-specific failure taxonomy. |
| C5 confuses one hosted proof with production readiness. | Require hosted checklist, observability, rollback, security, and public claim packet. |

---

## Related Artifacts

- `docs/baselines/CVF_GC018_C1_PUBLIC_AIF_PREVIEW_RUNTIME_AVAILABILITY_2026-05-24.md`
- `docs/work_orders/CVF_WO_C1_PUBLIC_AIF_PREVIEW_RUNTIME_AVAILABILITY_2026-05-24.md`
- `docs/reviews/CVF_C1_PUBLIC_AIF_PREVIEW_RUNTIME_AVAILABILITY_COMPLETION_2026-05-24.md`
- `docs/reference/CVF_POST_AIF_OPERATIONAL_READINESS_MATRIX_2026-05-24.md`

---

## Decision / Recommendation / Disposition

Disposition: C1 CLOSED_PASS; C2-C5 moved to explicit next-tranche gates.

Recommended next execution order:

1. C4 bounded tri-provider stability window, because it can improve evidence
   without changing runtime semantics.
2. C2 live memory reinjection, only after a narrow opt-in route design is
   accepted.
3. C3 graph authority, only after C2 and a policy-dominance model exist.
4. C5 hosted/production readiness, after runtime claims and provider stability
   are stronger.

---

## Claim Boundary

Allowed after C1: public-sync runtime availability of the local, summary-only
AIF operational context preview harness.

Still not allowed: live memory reinjection, graph authority, broad provider
stability, hosted readiness, production readiness, or freeze release.
