# CVF GC-018 D3 Qwen3 Provider Expansion

Memory class: SUMMARY_RECORD

Status: AUTHORIZED_READY_FOR_IMPLEMENTATION

Date: 2026-05-23

## Purpose

Authorize a bounded expansion of the Alibaba provider entry in
`PROVIDER_CAPABILITY_REGISTRY` to include two Qwen3 models
(`qwen3-32b` and `qwen3-235b-a22b-thinking`), plus one live hosted
proof call per model against `https://vibcode.netlify.app/api/execute`
using the P3 pass/fail matrix.

The goal is to capture evidence that CVF's governed execution path
handles Qwen3 models correctly before their free-tier quota expires
on 2026-06-02.

## Scope

In scope:

- add `qwen3-32b` and `qwen3-235b-a22b-thinking` to
  `PROVIDER_CAPABILITY_REGISTRY` under `providerId: "alibaba"`;
- add corresponding entries to
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/providers/alibaba/capability.json`;
- update `PROVIDER_CAPABILITY_REGISTRY` tests to assert new models;
- run two live hosted proof calls (one per model) against
  `https://vibcode.netlify.app/api/execute` using the P3 pass/fail
  matrix;
- file a completion review with sanitized receipt facts per model.

Out of scope:

- stream adapter or json_mode adapter for Qwen3 (add to registry only);
- any change to `vision-contract.ts` or `reasoning-contract.ts`;
- any change to `/api/execute` route logic, receipt envelopes, or
  auth semantics;
- any new memory tier, persistence, or database work;
- any public-sync update;
- any freeze release or kernel-owner replacement;
- claiming broad provider stability, all-provider parity, or
  production readiness.

## Source / Predecessor Evidence

- D2 closure: `docs/baselines/archive/CVF_GC018_D2_PROVIDER_CAPABILITY_MATRIX_2026-05-22.md`
- P3 hosted proof: `docs/baselines/CVF_GC018_P3_HOSTED_PROTECTED_WORKFLOW_PROOF_RERUN_2026-05-23.md`
- P3 pass/fail matrix: HTTP 200, success=true, decision ALLOW,
  evidenceMode=live, receipt present, trace present, rawSecretPrinted=false
- Free-tier expiry: Alibaba Qwen3 free quota expires 2026-06-02

## GC-018 Candidate Screening

| Candidate | Class | Score | Decision | Rationale |
| --- | ---: | ---: | --- | --- |
| qwen3-32b registry + hosted proof | VALIDATION_TEST / REALIZATION | 8/10 | CONTINUE | Free quota expires 2026-06-02; D2 structure ready; P3 hosted target proven; bounded registry-only change. |
| qwen3-235b-a22b-thinking registry + hosted proof | VALIDATION_TEST | 7/10 | CONTINUE | Same rationale; thinking-mode reasoning chain adds governance signal value. |
| stream/json_mode adapters for Qwen3 | IMPLEMENTATION | 4/10 | DEFER | Registry entry is sufficient for this tranche; adapters require separate work order. |
| Broader Qwen3 model sweep (all 8 models) | BROAD_TEST | 3/10 | DEFER | Two models bounded by pass/fail matrix is sufficient for this tranche. |

## Depth Audit

Candidate: `D3_QWEN3_PROVIDER_EXPANSION`

- Risk reduction: 2 (free-tier expiry creates time pressure)
- Decision value: 2 (extends provider matrix with proven hosted target)
- Machine enforceability: 2 (registry type-checked; tests assert models)
- Operational efficiency: 2 (D2 structure requires minimal code delta)
- Portfolio priority: 1 (not P0 critical but time-bounded)
- Total: 9
- Decision: CONTINUE

## Authorization Boundary

- Authorized now: YES
- Tranche name: `D3_QWEN3_PROVIDER_EXPANSION`
- Blocked-work override required: NO
- Active-path impact: ADDITIVE ONLY — no existing model or route changed
- Expected enforcement class: PROVIDER_REGISTRY_EXTENSION
- Required evidence:
  - `PROVIDER_CAPABILITY_REGISTRY` updated with two new Alibaba models;
  - `capability.json` updated;
  - `npm test` PASS in `CVF_MODEL_GATEWAY`;
  - two hosted proof calls, each returning HTTP 200, success=true,
    decision ALLOW, evidenceMode=live, receipt id present,
    rawSecretPrinted=false;
  - completion review filed with sanitized receipt facts.

## Decision / Baseline / Proposed Tranche

Decision: AUTHORIZED.

Baseline: D2 provider capability matrix is closed. P3 hosted proof is
closed with receipt `rcpt-env-mpi55je6-hiddxq`. The hosted target
`https://vibcode.netlify.app` is confirmed reachable and governed.

Proposed tranche: `D3_QWEN3_PROVIDER_EXPANSION` — additive registry
extension only. No existing model entries are modified. No route, receipt,
or auth change.

## Evidence / Verification

Required evidence before closure:

- `PROVIDER_CAPABILITY_REGISTRY` updated with `qwen3-32b` and
  `qwen3-235b-a22b-thinking` under `"alibaba"`;
- `npm test` PASS in `CVF_MODEL_GATEWAY` (all existing + new assertions);
- two hosted proof calls passing the P3 pass/fail matrix (HTTP 200,
  success=true, ALLOW, evidenceMode=live, receipt present,
  rawSecretPrinted=false);
- completion review filed with sanitized receipt facts only.

## Claim Boundary

This GC-018 authorizes a bounded provider registry extension and two
hosted proof calls only. It does not claim broad Qwen3 stability,
production readiness, hosted SaaS readiness, thinking-mode governance
completeness, or any capability beyond the two named models executing
one governed call each.
