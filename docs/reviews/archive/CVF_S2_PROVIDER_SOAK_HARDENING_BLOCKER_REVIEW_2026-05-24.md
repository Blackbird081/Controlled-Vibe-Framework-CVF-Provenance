# CVF S2 Provider Soak Hardening Blocker Review

Memory class: FULL_RECORD

Status: SUPERSEDED_BY_S2_COMPLETION

docType: review

Date: 2026-05-24

---

## Scope

S2 attempted the authorized provider soak: 5 governed `/api/execute` journeys
per provider across Alibaba, DeepSeek, and OpenAI.

Command:

```bash
node scripts/run_cvf_s2_provider_soak_probe.mjs
```

## Purpose

Determine whether the authorized S2 longer soak can support a bounded
three-provider repeatability claim, or must return blocked with failure
classification.

## Target / Source

Target:

- `scripts/run_cvf_s2_provider_soak_probe.mjs`
- `scripts/run_post_phase2b_provider_stability_probe.mjs`

Source authority:

- `docs/baselines/CVF_GC018_S2_PROVIDER_SOAK_HARDENING_2026-05-24.md`
- `docs/work_orders/CVF_WO_S2_PROVIDER_SOAK_HARDENING_2026-05-24.md`

## Result

Overall: `FAIL` / partial provider stability evidence.

| Provider | Result | Notes |
| --- | --- | --- |
| Alibaba `qwen-turbo` | `5/5 PASS` | All live receipts, route `/api/execute`, `ALLOW`. |
| DeepSeek `deepseek-chat` | `0/5 FAIL` | All returned HTTP 200 with live receipts/routing `ALLOW`, but `success=false`, output length `0`, about 60s latency each. |
| OpenAI `gpt-4o` | `5/5 PASS` | All live receipts, route `/api/execute`, `ALLOW`. |

DeepSeek receipt ids:

- `rcpt-env-mpjfo0wq-dxb77g`
- `rcpt-env-mpjfpckr-lisfa6`
- `rcpt-env-mpjfqoag-6etwwl`
- `rcpt-env-mpjfrzzy-87p5gi`
- `rcpt-env-mpjftbqo-1t18nt`

Failure class: `execute_failure` for all DeepSeek journeys.

## Findings / Position

Finding 1: PASS for Alibaba. The lane passed `5/5` live journeys.

Finding 2: BLOCKING for DeepSeek. The lane failed `0/5`; all attempts had live
ALLOW receipts but `success=false` and empty output.

Finding 3: PASS for OpenAI. The lane passed `5/5` live journeys.

Position: S2 cannot close pass because one provider failed all journeys.

## Risk / Corrective Action

Risk: partial evidence could be overstated as 3-provider stability.
Corrective action: roadmap and work order status are set to
`RETURNED_BLOCKED_DEEPSEEK_EXECUTE_FAILURE`; only Alibaba/OpenAI `5/5` positive
evidence is retained.

## Disposition

`RETURNED_BLOCKED_DEEPSEEK_EXECUTE_FAILURE`.

Per work order return-to-orchestrator rules, S2 cannot close pass because all
journeys for one provider failed. Do not claim 3-provider soak hardening or
broad provider stability from this evidence.

Superseded 2026-05-24:

- Superseding completion review:
  `docs/reviews/CVF_S2_PROVIDER_SOAK_HARDENING_COMPLETION_2026-05-24.md`
- Superseding result: Alibaba `5/5`, DeepSeek `5/5`, OpenAI `5/5`;
  total `15/15 PASS` with bounded provider timeout `120000ms`.

This blocker review remains historical evidence of the earlier DeepSeek
timeout/execute-failure window. It is no longer the current S2 status.

## Claim Boundary

Bounded positive evidence retained: Alibaba and OpenAI each passed `5/5` in
this window with live receipts and `rawSecretPrinted=false`.
