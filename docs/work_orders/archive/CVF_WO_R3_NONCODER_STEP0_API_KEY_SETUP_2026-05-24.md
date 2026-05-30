# CVF Work Order: R3 - Non-Coder Step 0 API-Key Setup

Memory class: SUMMARY_RECORD

Status: CLOSED_PASS

docType: work_order

Date: 2026-05-24

Tranche: R3

Roadmap: `docs/roadmaps/CVF_R1_R2_P2_POST_M1_GAP_CLOSURE_ROADMAP_2026-05-24.md`

---

## Purpose

Close the P1 Step 0 gap with a public-safe provider-key setup guide for
non-coders, solo operators, and small teams.

---

## Authority Chain

- GC-018: `docs/baselines/CVF_GC018_R3_NONCODER_STEP0_API_KEY_SETUP_2026-05-24.md`
- P1 completion:
  `docs/reviews/CVF_P1_PRODUCTION_READINESS_SMALL_TEAM_COMPLETION_2026-05-24.md`
- Superseded P2 work order:
  `docs/work_orders/CVF_WO_P2_NONCODER_STEP0_API_KEY_SETUP_2026-05-24.md`

---

## Scope / Target / Owner Boundary

Target:

- `docs/guides/CVF_NON_CODER_STEP0_API_KEY_SETUP_2026-05-24.md`
- `docs/guides/CVF_NON_CODER_SETUP_GUIDE_2026-05-24.md`
- Public-sync guide/catalog copies if public-facing claims change.

Owner: CVF onboarding and public-safe documentation.

Boundary: docs only; no provider procurement, hosted secret vault, enterprise
credential management, or universal provider availability claim.

---

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Planner | Map Step 0 setup path and public/private split. |
| Implementer | Write/update guides. |
| QA | Run secret hygiene and path checks. |
| Governance Reviewer | Confirm claim boundary and public repo compliance. |
| Release Manager | Commit private and public-sync artifacts if needed. |

---

## Required First Reads

- `docs/reviews/CVF_P1_PRODUCTION_READINESS_SMALL_TEAM_COMPLETION_2026-05-24.md`
- `docs/guides/CVF_NON_CODER_SETUP_GUIDE_2026-05-24.md`
- Root `AGENTS.md` public repository boundary.
- Public-sync `docs/guides/` and catalog files.

---

## Write Ownership

- Private `docs/guides/` Step 0 and first-receipt guides.
- Public-sync `docs/guides/` and catalog files if public-safe claim changes.
- R3 completion review and roadmap status updates.

---

## Pre-Flight Checks

- Verify public-sync remote before any public update.
- Confirm docs contain no real key/token/signed header.
- Confirm guide does not imply hosted/enterprise credential management.

---

## Execution Plan

1. Write Step 0 provider-key setup guide.
2. Link the first-receipt guide to Step 0.
3. Mirror public-safe guide changes to public-sync.
4. Update public catalog evidence path if needed.
5. Run secret hygiene and Test-Path checks.
6. File completion review and update roadmap.

---

## Evidence Requirements

- Step 0 guide path.
- Secret hygiene scan PASS.
- Public-sync remote verification and Test-Path PASS.
- Completion review filed.

---

## Acceptance Criteria

- [x] Step 0 setup guide filed.
- [x] Existing first-receipt guide links to Step 0.
- [x] Secret hygiene PASS.
- [x] Public-sync update complete if public claim changes.
- [x] Completion review filed.

---

## Review Gate

The completion review must confirm guide readability, secret hygiene, public
repository boundary compliance, and public-sync verification.

---

## Operator Checkpoint

Operator authorized R2/R3 on 2026-05-24 under prior workflow rules.

---

## Closure Checklist

- [x] Step 0 guide filed.
- [x] First-receipt guide linked.
- [x] Secret hygiene PASS.
- [x] Public-sync update complete.
- [x] Completion review filed.

---

## Return-To-Orchestrator Conditions

Return blocked if public-sync remote cannot be verified, secret hygiene fails,
or the guide would require committing real key values.

---

## Claim Boundary

R3 may claim a documented provider-key setup path for small teams. It does not
claim provider account availability, automated onboarding, hosted credential
management, or enterprise production readiness.
