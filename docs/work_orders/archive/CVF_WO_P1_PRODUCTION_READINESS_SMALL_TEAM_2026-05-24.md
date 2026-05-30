# CVF Work Order: P1 — Production Readiness for Small Team / Non-Coder

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: work_order

Date: 2026-05-24

Tranche: P1

Roadmap: `docs/roadmaps/CVF_M1_M2_P1_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Purpose

Assess and improve the non-coder/small-team production path so CVF can make a
bounded, honest production readiness claim for that persona. Close the
end-to-end gap: non-coder user → template selection → governed execution →
receipt in hand.

This tranche runs in parallel with M2 and M1. No dependency on either.

---

## Authority Chain

- GC-018: `docs/baselines/CVF_GC018_P1_PRODUCTION_READINESS_SMALL_TEAM_2026-05-24.md`
- Roadmap: `docs/roadmaps/CVF_M1_M2_P1_NEXT_VALUE_ROADMAP_2026-05-24.md`
- C5 hosted smoke (prior evidence):
  `docs/reviews/CVF_C2_C5_POST_AIF_CLAIM_GRADUATION_COMPLETION_2026-05-24.md`
- Post-AIF operational readiness matrix:
  `docs/reference/CVF_POST_AIF_OPERATIONAL_READINESS_MATRIX_2026-05-24.md`

---

## Scope / Target / Owner Boundary

Target surfaces:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/` — web UI onboarding path.
- `docs/guides/` — minimum setup documentation.
- Public catalog (public-sync): `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
- Public-safe guide/evidence page in public-sync:
  `docs/guides/CVF_NON_CODER_SETUP_GUIDE_2026-05-24.md`

Out of scope:

- Enterprise SaaS readiness.
- Multi-tenant hosted GA.
- Broad provider stability.
- Runtime changes to governance engine.
- Any kernel surface modification.

---

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Planner | Map non-coder persona journey; identify friction points. |
| Implementer | Write minimum setup doc; close top-3 friction points. |
| QA | Run end-to-end proof; capture live receipt. |
| Governance Reviewer | Confirm claim is bounded to proven persona path only. |
| Release Manager | Update public catalog; file completion review; commit. |

---

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/reference/CVF_POST_AIF_OPERATIONAL_READINESS_MATRIX_2026-05-24.md`
- `docs/reviews/CVF_C2_C5_POST_AIF_CLAIM_GRADUATION_COMPLETION_2026-05-24.md`
- `docs/guides/` — scan existing guides for what is already documented.
- Web UI landing page and template selection flow.
- `docs/roadmaps/CVF_M1_M2_P1_NEXT_VALUE_ROADMAP_2026-05-24.md`

---

## Write Ownership

- `docs/guides/CVF_NON_CODER_SETUP_GUIDE_2026-05-24.md` — minimum setup doc.
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/` — friction point fixes (if
  code changes needed).
- Public catalog (public-sync clone):
  `docs/reference/CVF_TECHNICAL_PRODUCT_CATALOG_2026-05-18.md`
- `docs/reviews/CVF_P1_PRODUCTION_READINESS_SMALL_TEAM_COMPLETION_2026-05-24.md`
- `docs/roadmaps/CVF_M1_M2_P1_NEXT_VALUE_ROADMAP_2026-05-24.md` — update P1
  row status to `CLOSED_PASS`.

---

## Pre-Flight Checks

- Confirm live provider key is available (Alibaba or DeepSeek) for end-to-end
  proof. Do not print key value.
- Confirm web UI dev server can be started.
- Confirm public catalog is accessible in public-sync clone for final update.
- Check GC-023 line counts on any guide file before adding content.

---

## Allowed / Forbidden Scope

Allowed:

- Onboarding journey assessment (prose analysis, no code required).
- Minimum setup documentation (single-page guide for non-coders).
- Top-3 friction point identification and closure.
- End-to-end proof call: non-coder persona → template → `/api/execute` →
  receipt, using approved local provider keys.
- Public catalog row update: small-team production readiness claim with
  verified public-safe guide/evidence path.

Forbidden:

- Enterprise SaaS or multi-tenant hosted GA claim.
- Broad provider stability claim.
- Publishing secrets, service tokens, or signed headers.
- Any governance engine or kernel surface modification.
- Public-sync of `docs/baselines/`, `docs/reviews/`, or `docs/roadmaps/`
  (internal provenance artifacts).

---

## Execution Plan

1. Read required first reads.
2. Map the non-coder persona journey:
   a. What does a non-coder need to have set up?
   b. What is the minimum path from zero to first receipt?
   c. What are the top-3 friction points on that path?
3. Write minimum setup doc at `docs/guides/CVF_NON_CODER_SETUP_GUIDE_2026-05-24.md`.
4. Close top-3 friction points (code fix, doc fix, or explicit deferral with
   reason for each).
5. Run end-to-end proof: use web UI or equivalent to submit a governed template
   execution via `/api/execute`. Capture live receipt.
   - Provider: Alibaba `qwen-turbo` preferred (lowest friction for non-coder path).
   - No raw key printed.
   - `rawSecretPrinted=false` enforced.
6. Update public catalog in public-sync clone:
   a. Add or update row for small-team production readiness claim.
   b. Evidence path must point to a public-safe guide/evidence artifact in
      public-sync, not to private `docs/reviews/`, `docs/baselines/`, or
      `docs/roadmaps/` artifacts.
   c. Run Test-Path on every new or modified path from public-sync clone.
7. File completion review at:
   `docs/reviews/CVF_P1_PRODUCTION_READINESS_SMALL_TEAM_COMPLETION_2026-05-24.md`
8. Commit all artifacts (governance repo first, then public-sync update).

---

## Non-Coder Persona Definition

The target user:

- Has no software engineering background.
- Wants to use AI to help with a business task (e.g., write a strategy brief,
  summarize a meeting, build a landing page).
- Can follow a step-by-step guide but cannot read TypeScript source code.
- Has an internet connection and can use a web browser.
- Is willing to get an API key for one AI provider (Alibaba or similar).

The proof must work for this persona.

---

## Evidence Requirements

- Minimum setup doc: filed at `docs/guides/CVF_NON_CODER_SETUP_GUIDE_2026-05-24.md`.
- Friction point analysis: listed in completion review with close status.
- End-to-end proof: live receipt, HTTP 200, `success=true`, `evidenceMode=live`,
  `rawSecretPrinted=false`.
- Public catalog: updated row with verified evidence path.
- Public evidence path: verified in public-sync and contains no internal
  receipt payload, service-token header, or private review content.
- Completion review: filed.

---

## Acceptance Criteria

- [ ] Persona journey mapped.
- [ ] Minimum setup doc filed.
- [ ] Top-3 friction points identified and each has a close/defer decision.
- [ ] End-to-end proof receipt captured.
- [ ] Public catalog updated with bounded claim and verified evidence path.
- [ ] Completion review filed.
- [ ] No raw secret in any artifact.

---

## Review Gate

The completion review must confirm:

- Non-coder persona journey was assessed and documented.
- Minimum setup doc is readable without code knowledge.
- Each of the top-3 friction points has an explicit close or defer decision.
- Live proof receipt is present with HTTP 200, `success=true`, `evidenceMode=live`,
  and `rawSecretPrinted=false`.
- Public catalog row evidence path was verified via Test-Path from public-sync
  clone before commit.
- No raw API key or signed header appears in any committed artifact.

---

## Operator Checkpoint

Operator authorized P1 on 2026-05-24, to run in parallel with M2/M1.
Target audience: non-coders, solo developers, small teams.
CVF does not compete with enterprise frameworks — bounded small-team claim
is the correct scope.

Codex must self-execute and return the final result after tranche completion.

---

## Closure Checklist

- [ ] Persona journey assessment complete.
- [ ] Minimum setup doc filed and readable by non-coder.
- [ ] Friction points closed or deferred with reason.
- [ ] Live proof receipt filed.
- [ ] Public catalog updated.
- [ ] Completion review filed and committed.
- [ ] No raw secret in any committed artifact.

---

## Return-To-Orchestrator Conditions

Return blocked if: live proof fails, public catalog update fails Test-Path
verification, or friction point analysis cannot identify a viable non-coder path.

---

## Tasks

| Task | Status | Output |
| --- | --- | --- |
| Persona journey map | DONE | Analysis in completion review. |
| Minimum setup doc | DONE | `docs/guides/CVF_NON_CODER_SETUP_GUIDE_2026-05-24.md` |
| Friction point analysis | DONE | Top-3 with close/defer status. |
| End-to-end proof | DONE | Live receipt `rcpt-env-mpjb7f0k-ruyeo3`, `rawSecretPrinted=false`. |
| Public catalog update | DONE | Bounded row with verified public-safe guide path. |
| Completion review | DONE | `docs/reviews/CVF_P1_PRODUCTION_READINESS_SMALL_TEAM_COMPLETION_2026-05-24.md` |

---

## Claim Boundary

P1 claims production readiness for the non-coder/small-team persona only,
with a proven end-to-end path and live receipt evidence. It does not claim
enterprise SaaS readiness, multi-tenant hosted GA, broad provider stability,
or broad production stability beyond the narrow proven path.
