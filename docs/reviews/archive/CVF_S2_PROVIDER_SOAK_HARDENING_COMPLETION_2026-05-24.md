# CVF S2 Provider Soak Hardening Completion

Memory class: FULL_RECORD

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-05-24

---

## Scope

S2 reran the authorized provider soak after improving the probe diagnostic
surface. The rerun used live governed `/api/execute` calls across Alibaba,
DeepSeek, and OpenAI.

## Purpose

Close the S2 provider soak hardening tranche with a bounded, diagnosable
tri-provider repeatability window after the earlier DeepSeek transient blocker.

## Target / Source

Target:

- `scripts/run_post_phase2b_provider_stability_probe.mjs`
- `scripts/run_cvf_s2_provider_soak_probe.mjs`
- `docs/roadmaps/CVF_S1_S2_S3_NEXT_VALUE_ROADMAP_2026-05-24.md`
- `docs/work_orders/CVF_WO_S2_PROVIDER_SOAK_HARDENING_2026-05-24.md`

Source authority:

- `docs/baselines/CVF_GC018_S2_PROVIDER_SOAK_HARDENING_2026-05-24.md`
- operator instruction on 2026-05-24 to clean the DeepSeek blocker before
  moving to a value-screened next tranche

Command:

```bash
node scripts/run_cvf_s2_provider_soak_probe.mjs
```

Bounded runtime setting:

- `CVF_AI_PROVIDER_TIMEOUT_MS=120000`
- `CVF_POST_PHASE2B_REPEATS=5`
- `CVF_POST_PHASE2B_INTER_JOURNEY_DELAY_MS=1500`

## Diagnostic Fix

The prior blocker review recorded DeepSeek `execute_failure` but the probe did
not retain the route response `error` field. S2 now records a redacted
diagnostic error and classifies provider timeout, rate-limit, balance/quota, and
auth cases separately.

No route, provider adapter, governance receipt, memory, or kernel behavior was
changed.

## Result

Overall: `PASS`

| Provider | Model | Result |
| --- | --- | --- |
| Alibaba | `qwen-turbo` | `5/5 PASS` |
| DeepSeek | `deepseek-chat` | `5/5 PASS` |
| OpenAI | `gpt-4o` | `5/5 PASS` |

Total: `15/15 PASS`

All journeys returned:

- HTTP `200`
- `success=true`
- `decision=ALLOW`
- `routingDecision=ALLOW`
- `evidenceMode=live`
- route `/api/execute`
- `rawSecretPrinted=false`

## Findings / Position

Finding 1: The prior DeepSeek failure was not reproduced after diagnostic
hardening and bounded timeout increase.

Finding 2: All three provider lanes passed the authorized five-journey window.

Finding 3: The diagnostic probe now preserves enough redacted error information
to classify future failures without printing secrets.

Position: S2 is closed pass bounded. The earlier blocker is superseded, not
deleted.

## Receipt Evidence

Alibaba receipts:

- `rcpt-env-mpjh5ilf-f8zzgj`
- `rcpt-env-mpjh5s20-zbmfva`
- `rcpt-env-mpjh61ql-i0xw7f`
- `rcpt-env-mpjh6cjk-eycqle`
- `rcpt-env-mpjh6m4x-zrtjik`

DeepSeek receipts:

- `rcpt-env-mpjh6xej-1vseeg`
- `rcpt-env-mpjh7a1i-c6hvd1`
- `rcpt-env-mpjh7r0g-f17n37`
- `rcpt-env-mpjh82pp-zhhu32`
- `rcpt-env-mpjh8e0k-qzz82l`

OpenAI receipts:

- `rcpt-env-mpjh8sxo-pemwld`
- `rcpt-env-mpjh8z26-w2lgoy`
- `rcpt-env-mpjh942a-1duwib`
- `rcpt-env-mpjh9alw-25q5ef`
- `rcpt-env-mpjh9gry-tqf1jx`

## Prior Blocker Disposition

The earlier DeepSeek `0/5` blocker is retained as historical evidence of a
transient timeout/execute-failure window. It is superseded for S2 closure by
this diagnostic rerun.

This completion does not prove universal provider stability or SLA-level
availability. It proves only the bounded 15-call repeatability window above.

## Operator Top-Up Rerun Addendum - 2026-05-24

After the operator topped up the DeepSeek account, Codex reran only the
DeepSeek lane to avoid spending unrelated provider quota.

Command:

```bash
CVF_POST_PHASE2B_PROVIDERS=deepseek CVF_POST_PHASE2B_REPEATS=5 node scripts/run_cvf_s2_provider_soak_probe.mjs
```

Result: `PASS 5/5`.

| Journey | Receipt | Trace | Status | Latency |
| --- | --- | --- | --- | --- |
| 1 | `rcpt-env-mpju5p4n-vz21an` | `env-mpju5p4n-vz21an` | PASS | 15650 ms |
| 2 | `rcpt-env-mpju629l-193w3g` | `env-mpju629l-193w3g` | PASS | 20081 ms |
| 3 | `rcpt-env-mpju6ixe-3htqmx` | `env-mpju6ixe-3htqmx` | PASS | 17993 ms |
| 4 | `rcpt-env-mpju6xz6-59w5jr` | `env-mpju6xz6-59w5jr` | PASS | 18179 ms |
| 5 | `rcpt-env-mpju7d61-69skn2` | `env-mpju7d61-69skn2` | PASS | 16501 ms |

All five calls returned HTTP `200`, `success=true`, `decision=ALLOW`,
`routingDecision=ALLOW`, `evidenceMode=live`, route `/api/execute`, and
`rawSecretPrinted=false`. No failure class was emitted.

## Risk / Corrective Action

Risk: The superseding `15/15` result could be overstated as broad provider
stability.

Corrective action: Claim language is restricted to the exact bounded window.
The next-value roadmap explicitly holds further provider soaking unless a
specific product or public claim requires it.

## Public Catalog

Public catalog update: N/A.

Reason: S2 adds no new public capability surface. It only supersedes a private
provider-soak blocker with a bounded diagnostic repeatability window.

## Claim Boundary

S2 may claim:

- bounded tri-provider repeatability window: `15/15`
- Alibaba `5/5`, DeepSeek `5/5`, OpenAI `5/5`
- live governed `/api/execute` receipts for every journey

S2 must not claim:

- universal provider stability
- SLA or uptime guarantee
- enterprise production readiness
- hosted SaaS/GA readiness
- provider procurement/account robustness
- freeze release
