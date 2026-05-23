# CVF D9 Qwen3 Thinking Enable True Adapter Blocker Review

Memory class: FULL_RECORD

Status: RETURNED_BLOCKED_PROVIDER_ROUTER_RISK_POSTURE

docType: review

Reviewer: Codex

Date: 2026-05-23

---

## Purpose

Record the D9 hosted proof result after the public-safe adapter change was
pushed to the public repository.

D9 does not pass because the hosted call was denied by provider routing before
provider dispatch.

---

## Scope / Target / Owner Boundary

Target:

- hosted endpoint: `https://vibcode.netlify.app/api/execute`;
- protected workflow: signed service-token `/api/execute`;
- payload class: concrete `strategy_analysis`;
- requested provider/model: Alibaba `qwen3-235b-a22b-thinking-2507`;
- public commit: `811e59f6`;
- private commit: `0b1fc2e8`;
- proof count: one hosted call.

Owner boundary:

- evidence review only;
- no route/auth/safety/receipt/guard weakening;
- no hosted retry under D9.

---

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_D9_QWEN3_THINKING_ENABLE_TRUE_ADAPTER_2026-05-23.md`
- Work order:
  `docs/work_orders/CVF_WO_D9_QWEN3_THINKING_ENABLE_TRUE_ADAPTER_2026-05-23.md`
- Prior blocker:
  `docs/reviews/CVF_D8_QWEN3_AI_COMMIT_HOSTED_PROOF_BLOCKER_REVIEW_2026-05-23.md`

---

## Target / Source Under Review

Source under review:

- one signed service-token POST to hosted `/api/execute`;
- sanitized response facts only;
- no raw API key, service token, NextAuth secret, HMAC signature, or signed
  headers were copied into this review.

---

## Scope / Methodology

Method:

1. Pushed public-safe adapter change to the public repository at commit
   `811e59f6`.
2. Waited `120s` for Netlify deployment freshness.
3. Sent one signed hosted request with Skill Preflight and `aiCommit`.
4. Captured sanitized response facts.
5. Stopped after the non-pass result.

---

## Evidence

Sanitized hosted response facts:

| Field | Value |
| --- | --- |
| Proof | `D9_QWEN3_THINKING_ENABLE_TRUE_HOSTED_PROOF` |
| Target | `https://vibcode.netlify.app/api/execute` |
| HTTP status | `403` |
| Duration | `1830ms` |
| `success` | `false` |
| Decision | `ALLOW` |
| Routing decision | `DENY` |
| Enforcement status | `ALLOW` |
| Skill Preflight declared | `true` |
| Evidence mode | `live` |
| Provider | `alibaba` |
| Requested model | `qwen3-235b-a22b-thinking-2507` |
| Response model | `router-denied` |
| Receipt id | `rcpt-env-mpigusm2-kco50q` |
| Trace id | `env-mpigusm2-kco50q` |
| Policy snapshot id | `pol-20260523-0001` |
| Error | `No provider matches policy constraints` |
| Raw secret printed | `false` |

Local cause isolation:

- D9 payload used `cvfRiskLevel=R2`.
- `routeWebProvider()` maps Alibaba with `maxRiskLevel=R1`.
- Provider routing therefore denied before Alibaba dispatch.
- The prior D8 provider error about `enable_thinking` was not re-observed.

---

## Findings / Position

Position: `RETURNED_BLOCKED_PROVIDER_ROUTER_RISK_POSTURE`.

Findings:

- Hosted endpoint and signed auth remain reachable.
- Skill Preflight and `aiCommit` pass far enough to reach provider routing.
- The D9 call did not test the adapter against Alibaba because routing denied
  the request first.
- The next proof must use a provider-policy-compatible risk posture, not a D9
  retry.

---

## Decision

D9 is returned blocked. Do not claim D9/P3 pass from this evidence.

Any next hosted proof requires a fresh GC-018/work order and must keep the
request within Alibaba's current web-router `R1` provider boundary.

---

## Claim Boundary

This review claims only that the D9 hosted proof was router-denied before
provider dispatch because the payload used an `R2` risk posture. It does not
claim adapter failure, Qwen3 provider failure, hosted readiness, or broad
provider stability.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Mistaking router denial for adapter failure | Record that provider dispatch did not occur. |
| Retrying under D9 | Stop after one hosted call and open a new bounded tranche. |
| Weakening router policy to force a proof | Prohibited; use a compatible proof payload instead. |
| Secret leakage | Preserve sanitized facts only and `rawSecretPrinted=false`. |

---

## Evidence Trace Block

Claim: D9 hosted proof did not pass because the provider router denied the
payload before provider dispatch.

Evidence:

- public commit `811e59f6`;
- private commit `0b1fc2e8`;
- HTTP `403`;
- `success=false`;
- `decision=ALLOW`;
- `routingDecision=DENY`;
- `enforcementStatus=ALLOW`;
- `evidenceMode=live`;
- response model `router-denied`;
- receipt `rcpt-env-mpigusm2-kco50q`;
- trace `env-mpigusm2-kco50q`;
- error `No provider matches policy constraints`;
- `rawSecretPrinted=false`.

Verdict:

- D9 returned blocked. A new `R1`-compatible proof tranche is required.
