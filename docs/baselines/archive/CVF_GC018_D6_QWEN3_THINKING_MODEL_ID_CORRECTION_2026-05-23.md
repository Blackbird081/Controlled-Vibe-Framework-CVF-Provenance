# CVF GC-018 D6 Qwen3 Thinking Model ID Correction

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_READY_FOR_IMPLEMENTATION

Date: 2026-05-23

## Purpose

Authorize a narrow correction after D5 proved that the hosted path can execute
`qwen3-32b`, but the second model id `qwen3-235b-a22b-thinking` returned
`success=false` because the model does not exist or the hosted account lacks
access.

Alibaba Cloud Model Studio documentation lists the current Qwen3 235B thinking
text model id as `qwen3-235b-a22b-thinking-2507`. D6 corrects the local
capability registry and focused tests to this model id, then runs exactly one
hosted proof call for the corrected model.

## Scope

In scope:

- update the Alibaba Model Gateway capability registry entry from
  `qwen3-235b-a22b-thinking` to `qwen3-235b-a22b-thinking-2507`;
- update Alibaba `capability.json` with the corrected model id;
- update Model Gateway registry tests for the corrected model id;
- update `cvf-web` provider adapter tests so the D4 `enable_thinking=false`
  assertion covers the corrected model id;
- run focused Model Gateway and `cvf-web` verification;
- push private provenance if needed so hosted deploy can receive the corrected
  model id metadata/test state;
- run exactly one hosted proof call for
  `qwen3-235b-a22b-thinking-2507`;
- file completion or blocker review with sanitized evidence.

Out of scope:

- changing `/api/execute`, auth, service-token signing, safety filters, DLP,
  receipt schema, governance envelope, or route evidence logic;
- changing the D4 adapter behavior beyond test coverage;
- adding broad Qwen3 soak, provider tuning, streaming/json-mode adapter work,
  vision/reasoning contract changes, public-sync, persistence, Maika proof, or
  freeze release;
- retrying the old `qwen3-235b-a22b-thinking` id.

## Source / Predecessor Evidence

- D5 blocker:
  `docs/reviews/CVF_D5_QWEN3_HOSTED_SAFE_PAYLOAD_RERUN_BLOCKER_REVIEW_2026-05-23.md`
- D4 adapter blocker:
  `docs/reviews/CVF_D4_QWEN3_ENABLE_THINKING_ADAPTER_BLOCKER_REVIEW_2026-05-23.md`
- D3 provider registry predecessor:
  `docs/reviews/CVF_D3_QWEN3_PROVIDER_EXPANSION_BLOCKER_REVIEW_2026-05-23.md`
- Official model reference: Alibaba Cloud Model Studio supported models page,
  text Qwen3 International section, model
  `qwen3-235b-a22b-thinking-2507`.

## GC-018 Candidate Screening

| Candidate | Class | Score | Decision | Rationale |
| --- | ---: | ---: | --- | --- |
| Correct model id to `qwen3-235b-a22b-thinking-2507` and run one hosted proof | BUG_FIX / VALIDATION_TEST | 9/10 | CONTINUE | D5 isolated the failure to model id/access after `qwen3-32b` passed. Official docs identify the `-2507` suffix model id. |
| Retry old `qwen3-235b-a22b-thinking` | RETRY_LOOP | 0/10 | REJECT | D5 stop rule forbids retrying the same unavailable id. |
| Switch to unrelated Qwen3 thinking model | SCOPE_CHANGE | 3/10 | DEFER | Could prove another model but would not close the intended 235B target. |
| Hosted account provisioning | OPERATOR_INFRA | 5/10 | DEFER | Only needed if corrected model id still returns access denial. |

## Depth Audit

Candidate: `D6_QWEN3_THINKING_MODEL_ID_CORRECTION`

- Risk reduction: 2 (tests the likely root cause identified by official docs)
- Decision value: 2 (can close or precisely reclassify the remaining D5 block)
- Machine enforceability: 2 (registry/test diff plus one hosted proof)
- Operational efficiency: 2 (small metadata/test correction; no route change)
- Portfolio priority: 1 (time-bounded by Qwen3 quota window)
- Total: 9
- Decision: CONTINUE

## Authorization Boundary

- Authorized now: YES
- Tranche name: `D6_QWEN3_THINKING_MODEL_ID_CORRECTION`
- Blocked-work override required: NO
- Expected enforcement class: PROVIDER_MODEL_ID_CORRECTION
- Required evidence:
  - Model Gateway registry/capability entries use
    `qwen3-235b-a22b-thinking-2507`;
  - focused Model Gateway tests PASS;
  - focused `cvf-web` provider adapter tests PASS;
  - `cvf-web` check PASS;
  - one hosted proof call for `qwen3-235b-a22b-thinking-2507` returns HTTP
    `200`, `success=true`, `ALLOW`, `evidenceMode=live`, provider `alibaba`,
    matching model, receipt/trace present, and `rawSecretPrinted=false`;
  - completion or blocker review filed with sanitized facts.

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED.

Baseline: D5 proved hosted `qwen3-32b` with live ALLOW receipt evidence, but
the old 235B thinking id returned `success=false`. D6 corrects only that model
identifier and validates once.

Proposed tranche: `D6_QWEN3_THINKING_MODEL_ID_CORRECTION`.

## Evidence / Verification

Required before closure:

- targeted Model Gateway registry tests;
- targeted `cvf-web` provider tests;
- `cvf-web` check;
- one sanitized hosted proof result;
- local governance hook chain PASS.

## Claim Boundary

D6 can only prove the corrected one-model hosted path for
`qwen3-235b-a22b-thinking-2507`, combined with prior D5 evidence for
`qwen3-32b`. It does not claim broad Qwen3 stability, all-provider parity,
hosted SaaS readiness, production readiness, public deployment readiness,
thinking-mode governance completeness, persistence, Maika proof, public-sync,
or freeze release.
