# CVF P2 Provider Soak Evidence

Memory class: FULL_RECORD

Status: PASS

docType: evidence

Date: 2026-05-23

---

## Purpose

Record the bounded P2 longer-horizon provider stability soak authorized by
`docs/baselines/CVF_GC018_P2_P3_HN1_NEXT_VALUE_SCREENING_2026-05-23.md`.

This is live evidence only. It does not change provider runtime semantics,
router behavior, prompt/model/token-budget settings, or public claims.

---

## Scope / Target / Owner Boundary

Target:

- existing local governed `/api/execute` route;
- Alibaba `qwen-turbo`;
- DeepSeek `deepseek-chat`;
- six live repeats per provider.

Owner boundary:

- evidence capture only;
- no runtime/provider implementation ownership;
- no public-sync publication ownership;
- no hosted target ownership.

---

## Target / Source Under Review

Source under review:

- `scripts/run_post_phase2b_provider_stability_probe.mjs`

Predecessor evidence:

- `docs/reviews/CVF_POST_PUBLICIZATION_PROVIDER_STABILITY_HARDENING_COMPLETION_2026-05-21.md`
- `docs/baselines/CVF_GC018_P2_P3_HN1_NEXT_VALUE_SCREENING_2026-05-23.md`

---

## Scope / Methodology

Method:

1. Load approved local provider keys through process environment.
2. Start the local CVF web app.
3. Sign in through the real login UI.
4. Submit repeated governed `/api/execute` calls for each provider lane.
5. Require HTTP 200, success, non-mock output, live evidence mode, receipt,
   trace, routed-provider match, routing `ALLOW`, and no mock fallback.
6. Reject any evidence object that contains a raw provider secret.

---

## Command

```powershell
$env:CVF_POST_PHASE2B_PROVIDERS='alibaba,deepseek'
$env:CVF_POST_PHASE2B_REPEATS='6'
$env:CVF_POST_PHASE2B_PROVIDER_STABILITY_PORT='3223'
node scripts/run_post_phase2b_provider_stability_probe.mjs
```

The runner loads approved local environment files, starts the local CVF web
app, signs in through the real login UI, and executes repeated governed
`/api/execute` calls. Raw provider keys are not printed.

---

## Summary

| Metric | Result |
| --- | --- |
| Schema | `post-phase2b-provider-stability-result-1` |
| Status | `PASS` |
| Claim class | `narrow_two_provider_repeatability` |
| Providers requested | `alibaba`, `deepseek` |
| Repeats per provider | `6` |
| Pass count | `12` |
| Fail count | `0` |
| Governed route required | `/api/execute` |
| Live evidence required | `true` |
| Receipt required | `true` |
| Mock fallback rejected | `true` |
| Raw secret printed | `false` |

Runtime coherence anchor:

- completion: `docs/reviews/CVF_PHASE_2B_RUNTIME_COHERENCE_COMPLETION_2026-05-21.md`
- graph schema version: `phase2b-runtime-coherence-graph-1`
- adapter inventory checksum: `fnv1a32:5d3d2dac`

---

## Journey Results

| Provider | Model | Journey | HTTP | Decision | Routing | Evidence | Receipt | Trace | Latency | Result |
| --- | --- | ---: | ---: | --- | --- | --- | --- | --- | ---: | --- |
| Alibaba | `qwen-turbo` | 1 | 200 | `ALLOW` | `ALLOW` | `live` | `rcpt-env-mpi13lwm-f0w7qb` | `env-mpi13lwm-f0w7qb` | 12305ms | PASS |
| Alibaba | `qwen-turbo` | 2 | 200 | `ALLOW` | `ALLOW` | `live` | `rcpt-env-mpi13v5t-oq0cic` | `env-mpi13v5t-oq0cic` | 11986ms | PASS |
| Alibaba | `qwen-turbo` | 3 | 200 | `ALLOW` | `ALLOW` | `live` | `rcpt-env-mpi144ex-kyd14l` | `env-mpi144ex-kyd14l` | 12066ms | PASS |
| Alibaba | `qwen-turbo` | 4 | 200 | `ALLOW` | `ALLOW` | `live` | `rcpt-env-mpi14dqb-c2pbj2` | `env-mpi14dqb-c2pbj2` | 13626ms | PASS |
| Alibaba | `qwen-turbo` | 5 | 200 | `ALLOW` | `ALLOW` | `live` | `rcpt-env-mpi14o8k-e8bo17` | `env-mpi14o8k-e8bo17` | 13973ms | PASS |
| Alibaba | `qwen-turbo` | 6 | 200 | `ALLOW` | `ALLOW` | `live` | `rcpt-env-mpi14z0h-9bvzq9` | `env-mpi14z0h-9bvzq9` | 14191ms | PASS |
| DeepSeek | `deepseek-chat` | 1 | 200 | `ALLOW` | `ALLOW` | `live` | `rcpt-env-mpi159yu-zlcppk` | `env-mpi159yu-zlcppk` | 20381ms | PASS |
| DeepSeek | `deepseek-chat` | 2 | 200 | `ALLOW` | `ALLOW` | `live` | `rcpt-env-mpi15pp1-4kb09k` | `env-mpi15pp1-4kb09k` | 21491ms | PASS |
| DeepSeek | `deepseek-chat` | 3 | 200 | `ALLOW` | `ALLOW` | `live` | `rcpt-env-mpi166a7-25x2is` | `env-mpi166a7-25x2is` | 16789ms | PASS |
| DeepSeek | `deepseek-chat` | 4 | 200 | `ALLOW` | `ALLOW` | `live` | `rcpt-env-mpi16j8o-4afi9x` | `env-mpi16j8o-4afi9x` | 21710ms | PASS |
| DeepSeek | `deepseek-chat` | 5 | 200 | `ALLOW` | `ALLOW` | `live` | `rcpt-env-mpi16zzp-hazf8r` | `env-mpi16zzp-hazf8r` | 18324ms | PASS |
| DeepSeek | `deepseek-chat` | 6 | 200 | `ALLOW` | `ALLOW` | `live` | `rcpt-env-mpi17e4r-e46wkl` | `env-mpi17e4r-e46wkl` | 19555ms | PASS |

All journeys passed the runner assertions:

- HTTP status is 200;
- `success=true`;
- output is non-mock;
- governance receipt exists;
- governance envelope evidence mode is `live`;
- route id is `/api/execute`;
- routed provider matches requested provider;
- routing decision is `ALLOW`;
- no mock fallback marker appears.

---

## Findings / Position

Position: `PASS`.

The bounded P2 soak strengthens the previous narrow two-provider repeatability
evidence from three repeats per provider to six repeats per provider in one
live local session. No provider/runtime change was needed.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| Readers overinterpret `12/12` as broad provider stability | Claim boundary limits the result to local governed `/api/execute`, two named providers, and two named model lanes. |
| Raw API key leakage | Runner asserts no raw secret is present in the proof object and records `rawSecretPrinted=false`. |
| Hosted readiness overclaim | P3 remains held; this evidence uses only local route proof. |

---

## Decision / Recommendation / Disposition

Disposition: `CLOSED_BOUNDED_SOAK_PASS`.

Recommendation: do not continue provider soak by default. Any broader provider
claim needs a fresh GC-018 with a larger matrix, schedule, and explicit claim
ceiling.

---

## Claim Boundary

This evidence supports only a bounded P2 longer-horizon soak on the existing
local governed `/api/execute` path, across Alibaba `qwen-turbo` and DeepSeek
`deepseek-chat`, with six repeats per provider in one live session.

It does not prove broad provider stability, all-provider parity, hosted
readiness, production readiness, SSE/runtime lifecycle remediation, public
deployment readiness, Maika proof, or any freeze release.
