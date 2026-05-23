# CVF GC-018 D7 Qwen3 Skill Preflight Hosted Proof

Memory class: SUMMARY_RECORD

Status: AUTHORIZED

## Purpose

Authorize one narrow continuation after D6 corrected the local Qwen3 thinking
model id but the hosted proof stopped at the Skill Preflight gate.

D7 is limited to using a Skill Preflight-compliant hosted proof payload for
`qwen3-235b-a22b-thinking-2507`, then publishing public-safe metadata/code
changes through the public-sync clone if the evidence packet is complete.

## Scope / Target / Owner Boundary

In scope:

- build one hosted proof payload that explicitly declares Skill Preflight;
- run local safety and enforcement preflight against that payload;
- run exactly one signed hosted `/api/execute` call for
  `qwen3-235b-a22b-thinking-2507`;
- file completion or blocker review with sanitized facts;
- commit and push private provenance;
- mirror public-safe Qwen3 metadata/test/docs updates through
  `d:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF-public-sync`.

Out of scope:

- route, auth, safety, receipt-schema, or provider-adapter weakening;
- retry loops after the single hosted call;
- changing hosted environment variable values;
- claiming broad Qwen3 stability or hosted SaaS readiness;
- pushing from the private provenance workspace to the public repository.

## Authority Chain

- D6 blocker:
  `docs/reviews/CVF_D6_QWEN3_THINKING_MODEL_ID_CORRECTION_BLOCKER_REVIEW_2026-05-23.md`
- D5 proof:
  `docs/reviews/CVF_D5_QWEN3_HOSTED_SAFE_PAYLOAD_RERUN_BLOCKER_REVIEW_2026-05-23.md`
- Hosted target: `https://vibcode.netlify.app/api/execute`
- Public-sync boundary: root `AGENTS.md`, Critical Repository Boundary.

## Source / Predecessor Evidence

Source evidence is D6: local model id correction succeeded, but hosted proof
blocked at Skill Preflight before provider dispatch.

## Decision / Baseline / Proposed Tranche

Decision: authorize D7.

Baseline: corrected model id exists locally; Skill Preflight declaration is
missing from the hosted proof payload.

Proposed tranche: add Skill Preflight declaration to one hosted proof payload.

## Depth Audit

| Candidate | Type | Score | Decision | Rationale |
| --- | --- | ---: | --- | --- |
| Skill Preflight-compliant hosted proof for corrected Qwen3 model | VALIDATION_TEST | 9/10 | CONTINUE | D6 failed before provider dispatch due a missing payload field, not due provider execution. The route contract is machine-readable and already tested. |
| Retry D6 payload unchanged | RETRY_LOOP | 0/10 | REJECT | D6 already proved missing Skill Preflight blocks the route. |
| Weaken Skill Preflight gate | GOVERNANCE_SEMANTIC_CHANGE | 0/10 | REJECT | The gate is intentional and must not be bypassed for proof convenience. |

## Acceptance Criteria

D7 may close as PASS only if:

- local safety preflight returns `blocked=false`;
- local enforcement preflight returns `ALLOW` with Skill Preflight declared;
- hosted call returns HTTP 200;
- hosted response has `success=true`;
- decision, routing decision, and enforcement status are `ALLOW`;
- evidence mode is `live`;
- provider is `alibaba`;
- response model is `qwen3-235b-a22b-thinking-2507`;
- receipt and trace ids are present;
- raw secret printed flag is false;
- governance hooks pass;
- public-sync push is performed only from the public-sync clone after
  confirming its remote is `Controlled-Vibe-Framework-CVF.git`.

## Evidence / Verification

Verification requires local safety/enforcement preflight, one hosted proof
result, a completion/blocker review, and governance hook evidence.

If any required hosted criterion fails, D7 returns blocked and no second hosted
attempt is allowed under this authorization.

## Claim Boundary

D7 can claim only the corrected model's single hosted proof result and the
public-safe sync status. It cannot claim broad Qwen3 stability, hosted SaaS
readiness, production readiness, provider account coverage beyond the observed
model, Maika proof, persistence readiness, or freeze release.
