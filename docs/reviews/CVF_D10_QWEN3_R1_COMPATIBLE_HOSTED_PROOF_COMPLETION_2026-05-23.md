# CVF D10 Qwen3 R1 Compatible Hosted Proof Completion

Memory class: FULL_RECORD

Status: CLOSED_D10_QWEN3_R1_COMPATIBLE_HOSTED_PROOF_PASS

docType: review

Reviewer: Codex

Date: 2026-05-23

---

## Purpose

Record the successful D10 hosted proof for
`qwen3-235b-a22b-thinking-2507` after D9 isolated the remaining blocker to
provider-router risk posture.

---

## Scope / Target / Owner Boundary

Target:

- hosted endpoint: `https://vibcode.netlify.app/api/execute`;
- protected workflow: signed service-token `/api/execute`;
- payload class: concrete `strategy_analysis`;
- risk posture: `cvfRiskLevel=R1`;
- provider/model: Alibaba `qwen3-235b-a22b-thinking-2507`;
- public commit carrying adapter fix: `811e59f6`;
- proof count: one hosted call.

Owner boundary:

- proof and evidence review only;
- no route/auth/safety/receipt/guard weakening;
- no provider-router policy relaxation;
- no broad provider stability claim.

---

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_D10_QWEN3_R1_COMPATIBLE_HOSTED_PROOF_2026-05-23.md`
- Work order:
  `docs/work_orders/CVF_WO_D10_QWEN3_R1_COMPATIBLE_HOSTED_PROOF_2026-05-23.md`
- D9 blocker:
  `docs/reviews/CVF_D9_QWEN3_THINKING_ENABLE_TRUE_ADAPTER_BLOCKER_REVIEW_2026-05-23.md`

---

## Target / Source Under Review

Source under review:

- focused provider unit test output;
- `cvf-web` TypeScript check output;
- local `routeWebProvider()` preflight;
- one signed service-token POST to hosted `/api/execute`;
- sanitized response facts only.

No raw API key, service token, NextAuth secret, HMAC signature, or signed
headers were copied into this review.

---

## Scope / Methodology

Method:

1. Retained the public adapter fix from commit `811e59f6`.
2. Re-ran focused provider tests.
3. Re-ran `cvf-web` check.
4. Ran local provider-router preflight for Alibaba `R1`.
5. Sent one hosted request with `cvfRiskLevel=R1`, Skill Preflight, and
   `aiCommit`.
6. Captured only sanitized response facts.

No D10 retry loop was performed.

---

## Evidence

Local verification:

| Check | Result |
| --- | --- |
| `npm run test:run -- src/lib/ai/providers.test.ts` | PASS, 1 file / 42 tests |
| `npm run check` in `cvf-web` | PASS |
| Local router preflight | `decision=ALLOW`, `selectedProvider=alibaba`, `requestRiskLevel=R1`, `policyRiskCeiling=R2` |

Sanitized hosted response facts:

| Field | Value |
| --- | --- |
| Proof | `D10_QWEN3_R1_COMPATIBLE_HOSTED_PROOF` |
| Target | `https://vibcode.netlify.app/api/execute` |
| HTTP status | `200` |
| Duration | `28349ms` |
| `success` | `true` |
| Decision | `ALLOW` |
| Routing decision | `ALLOW` |
| Enforcement status | `ALLOW` |
| Skill Preflight declared | `true` |
| Evidence mode | `live` |
| Provider | `alibaba` |
| Requested model | `qwen3-235b-a22b-thinking-2507` |
| Response model | `qwen3-235b-a22b-thinking-2507` |
| Receipt id | `rcpt-env-mpigxtmn-pml5ky` |
| Trace id | `env-mpigxtmn-pml5ky` |
| Policy snapshot id | `pol-20260523-0002` |
| Output length | `4057` |
| Error | null |
| Raw secret printed | `false` |

---

## Findings / Position

Position: `CLOSED_D10_QWEN3_R1_COMPATIBLE_HOSTED_PROOF_PASS`.

Findings:

- Public-hosted `/api/execute` accepted the signed service-token request.
- Skill Preflight and `aiCommit` both passed.
- Provider routing allowed Alibaba under the `R1` proof posture.
- Hosted runtime dispatched to Alibaba and returned live governed evidence.
- The corrected Qwen3 thinking model returned `success=true` with the requested
  model id, which proves the `enable_thinking=true` adapter path for this
  bounded hosted proof.

---

## Decision

D10 closes as pass.

The D9 blocker remains valid historical evidence for an `R2` payload denied by
the current provider router. D10 supersedes it only for the bounded `R1`
compatible Qwen3 hosted proof status.

---

## Claim Boundary

This completion claims only one successful hosted signed service-token proof for
Alibaba `qwen3-235b-a22b-thinking-2507` under the current `R1` provider-router
boundary. It does not claim Alibaba `R2` routing, broad Qwen3 stability, hosted
SaaS readiness, production readiness, public release readiness, or freeze
release.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Overclaiming one hosted proof as broad Qwen3 stability | Keep claim to one bounded hosted proof. |
| Treating `R1` proof as an `R2` router release | Preserve Alibaba `R1` boundary; no router policy change was made. |
| Assuming hosted SaaS readiness | Do not claim production readiness from one proof call. |
| Secret leakage into evidence | Record sanitized facts only and `rawSecretPrinted=false`. |

---

## Evidence Trace Block

Claim: the hosted protected route can execute Alibaba
`qwen3-235b-a22b-thinking-2507` under the current `R1` provider-router
boundary and return live governed `ALLOW` evidence.

Evidence:

- public commit `811e59f6`;
- focused provider tests PASS `42/42`;
- `cvf-web` check PASS;
- local router preflight `ALLOW`;
- HTTP `200`;
- `success=true`;
- `decision=ALLOW`;
- `routingDecision=ALLOW`;
- `enforcementStatus=ALLOW`;
- `evidenceMode=live`;
- provider `alibaba`;
- model `qwen3-235b-a22b-thinking-2507`;
- receipt `rcpt-env-mpigxtmn-pml5ky`;
- trace `env-mpigxtmn-pml5ky`;
- output length `4057`;
- `rawSecretPrinted=false`.

Verdict:

- D10 hosted proof passes for this bounded proof scope.
