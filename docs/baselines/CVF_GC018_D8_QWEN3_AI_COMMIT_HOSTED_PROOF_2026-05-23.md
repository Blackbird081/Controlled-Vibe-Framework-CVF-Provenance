# CVF GC-018 D8 Qwen3 AI Commit Hosted Proof

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

## Purpose

Authorize one narrow continuation after D7 proved Skill Preflight declaration
is accepted but the hosted guard runtime blocked the BUILD-class proof payload
because `aiCommit` metadata was absent.

## Scope / Target / Owner Boundary

In scope:

- add explicit `aiCommit` metadata to the D7 Skill Preflight-compliant hosted
  proof payload;
- run local safety, enforcement, and guard-runtime preflight;
- run exactly one signed hosted call for `qwen3-235b-a22b-thinking-2507`;
- file completion or blocker review;
- commit private provenance and public-sync public-safe updates.

Out of scope:

- route/auth/safety/receipt/guard weakening;
- hosted retry loops under D8;
- changing hosted environment variable values;
- claiming broad provider stability or hosted readiness.

## Source / Predecessor Evidence

Source evidence is D7: Skill Preflight declaration was accepted, but the
hosted guard runtime blocked the request because `aiCommit` metadata was
missing.

## Decision / Baseline / Proposed Tranche

Decision: authorize D8.

Baseline: Skill Preflight payload gate passes; `aiCommit` is the next missing
pre-provider guard field.

Proposed tranche: add `aiCommit` metadata and run one hosted proof.

## Depth Audit

| Candidate | Type | Score | Decision | Rationale |
| --- | --- | ---: | --- | --- |
| Add `aiCommit` metadata and run one hosted proof | VALIDATION_TEST | 9/10 | CONTINUE | D7 isolated the block to a machine-readable guard-runtime requirement. Local guard simulation passes with `aiCommit`. |
| Reuse D7 payload without `aiCommit` | RETRY_LOOP | 0/10 | REJECT | D7 already proved that payload blocks. |
| Disable guard runtime | GOVERNANCE_SEMANTIC_CHANGE | 0/10 | REJECT | Guard runtime must remain authoritative. |

## Acceptance Criteria

D8 may close PASS only if:

- local safety preflight PASS;
- local enforcement preflight PASS with Skill Preflight declared;
- local guard-runtime preflight PASS with `aiCommit`;
- hosted HTTP 200;
- hosted `success=true`;
- decision, routing decision, and enforcement status are `ALLOW`;
- evidence mode is `live`;
- provider is `alibaba`;
- response model is `qwen3-235b-a22b-thinking-2507`;
- receipt and trace ids are present;
- raw secret printed flag is false.

If any hosted criterion fails, D8 returns blocked and no second hosted call is
allowed under D8.

## Evidence / Verification

Verification requires local safety/enforcement/guard preflight, one hosted
proof result, a completion/blocker review, and governance hook evidence.

## Claim Boundary

D8 can claim only the one corrected-model hosted proof result and public-safe
sync status. It cannot claim broad Qwen3 stability, hosted SaaS readiness,
production readiness, provider account coverage beyond the observed model,
Maika proof, persistence readiness, or freeze release.
