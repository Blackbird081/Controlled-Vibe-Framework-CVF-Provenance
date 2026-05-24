# CVF Work Order: P2 - Non-Coder Step 0 API-Key Setup

Memory class: SUMMARY_RECORD

Status: SUPERSEDED_BY_R3

docType: work_order

Date: 2026-05-24

Tranche: P2

Roadmap: `docs/roadmaps/CVF_R1_R2_P2_POST_M1_GAP_CLOSURE_ROADMAP_2026-05-24.md`

---

## STOP - Demand Gate

Do not claim P2 closed until the setup guide is public-safe, secret-free, and
verified from the public-sync clone if it changes public onboarding claims.

R3 supersedes this P2 label on 2026-05-24:

`docs/baselines/CVF_GC018_R3_NONCODER_STEP0_API_KEY_SETUP_2026-05-24.md`

R3 closed pass on 2026-05-24:

`docs/reviews/CVF_R3_NONCODER_STEP0_API_KEY_SETUP_COMPLETION_2026-05-24.md`

---

## Purpose

Close the P1 Step 0 gap. P1 proved a first-receipt path after provider keys
were already configured, but a non-coder/small-team operator still needs
plain-language instructions for obtaining and configuring the first provider
key.

---

## Authority Chain

- Roadmap: `docs/roadmaps/CVF_R1_R2_P2_POST_M1_GAP_CLOSURE_ROADMAP_2026-05-24.md`
- P1 completion review:
  `docs/reviews/CVF_P1_PRODUCTION_READINESS_SMALL_TEAM_COMPLETION_2026-05-24.md`
- Public repository boundary in root `AGENTS.md`.

---

## Scope / Target / Owner Boundary

Target:

- `docs/guides/CVF_NON_CODER_SETUP_GUIDE_2026-05-24.md`
- Optional new guide under `docs/guides/`.
- Public-sync guide/catalog update if a public onboarding claim changes.

Owner: CVF public onboarding and operator setup documentation.

Boundary: P2 is documentation and setup validation only. It does not claim
provider procurement support, enterprise credential management, hosted
secret-vault operations, or universal provider availability.

---

## Agent Roles

| Role | Responsibility |
| --- | --- |
| Planner | Define Step 0 provider-key path and public/private split. |
| Implementer | Write the non-coder setup guide and link it from first-receipt docs. |
| QA | Run secret hygiene and public-sync path checks. |
| Governance Reviewer | Confirm no public claim overreach. |
| Release Manager | Commit provenance and public-sync updates if needed. |

---

## Required First Reads

- `docs/reviews/CVF_P1_PRODUCTION_READINESS_SMALL_TEAM_COMPLETION_2026-05-24.md`
- `docs/guides/CVF_NON_CODER_SETUP_GUIDE_2026-05-24.md`
- Root `AGENTS.md` public repository boundary.
- Public-sync guide/catalog files if public docs are updated.

---

## Write Ownership

- `docs/guides/` setup guide files.
- Public-sync `docs/guides/` and catalog files if public claims change.
- Completion review and roadmap status updates.

---

## Pre-Flight Checks

- Confirm public-sync clone and remote before public-facing updates.
- Confirm no raw API key, service token, signed header, or real secret is
  present in documentation.
- Confirm Step 0 does not imply automated hosted onboarding.

---

## Required Content

The guide must tell a non-coder/small-team operator:

- which provider lane is the recommended first lane;
- which environment variable name to set;
- where to place it locally without committing it;
- how to verify CVF sees the key without printing the value;
- how to run one first-receipt proof;
- what to do if no key is available.

---

## Execution Plan

1. Decide recommended first provider lane and fallback wording.
2. Write Step 0 guide in non-coder language.
3. Link Step 0 from the first-receipt guide.
4. Update public-sync guide/catalog if the public claim changes.
5. Run secret hygiene scan and Test-Path checks.
6. File completion review and update roadmap.

---

## Evidence Requirements

- Guide is readable without TypeScript knowledge.
- No raw key, token, signed header, or secret-like placeholder is committed.
- Verification command uses masked or boolean output only.
- Public-sync Test-Path verification if public docs are updated.

---

## Acceptance Criteria

- [x] Step 0 setup guide filed by R3.
- [x] Existing first-receipt guide links to Step 0 by R3.
- [x] Secret hygiene check PASS by R3.
- [x] Public-sync guide/catalog update complete by R3.
- [x] Completion review filed by R3.

---

## Review Gate

The completion review must confirm guide readability, secret hygiene, public
repository boundary compliance, and any public-sync verification.

---

## Operator Checkpoint

P2 is registered from the Claude audit but remains gated until the operator
confirms the public/onboarding claim update should be executed.

---

## Closure Checklist

- [x] Step 0 guide filed by R3.
- [x] First-receipt guide linked by R3.
- [x] Secret hygiene PASS by R3.
- [x] Public-sync update complete by R3.
- [x] Completion review filed by R3.

---

## Return-To-Orchestrator Conditions

Return blocked if public-sync remote cannot be verified, secret hygiene fails,
or the guide would require real key values or provider-account promises.

---

## Claim Boundary

P2 may support a bounded claim that a small-team operator has a documented
provider-key setup path. It does not prove automated onboarding, hosted
credential management, or full non-coder self-service deployment.
