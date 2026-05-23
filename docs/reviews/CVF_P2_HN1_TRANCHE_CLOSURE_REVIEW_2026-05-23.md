# CVF P2/HN1 Tranche Closure Review

Memory class: FULL_RECORD

Status: CLOSED_P2_HN1_P3_HELD

docType: review

Reviewer: Codex

Date: 2026-05-23

---

## Purpose

Close the two executable candidates selected from the fresh P2/P3/HN1 GC-018:

- P2 longer-horizon provider stability soak;
- HN1 template-skill linkage hygiene re-verification.

P3 hosted protected workflow proof remains on conditional hold because no
hosted target, protected workflow, auth/token posture, or pass/fail workflow
was supplied.

---

## Scope / Target / Owner Boundary

Target:

- P2 live provider soak over the existing local governed `/api/execute` route;
- HN1 template-skill linkage hygiene re-verification;
- P3 conditional-hold status.

Owner boundary:

- review/evidence closure only;
- no source-code runtime ownership;
- no provider adapter ownership;
- no public-sync ownership;
- no hosted deployment ownership.

---

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_P2_P3_HN1_NEXT_VALUE_SCREENING_2026-05-23.md`
- HN1 prior closure:
  `docs/reviews/CVF_HN1_TEMPLATE_LINKAGE_EXEMPTION_CLOSURE_REVIEW_2026-05-20.md`
- HN1 work order:
  `docs/work_orders/CVF_WO_HN1_TEMPLATE_LINKAGE_EXEMPTION_FAST_LANE_2026-05-20.md`
- P2 evidence:
  `docs/reviews/CVF_P2_PROVIDER_SOAK_EVIDENCE_2026-05-23.md`
- P2 machine-readable evidence:
  `docs/reviews/CVF_P2_PROVIDER_SOAK_EVIDENCE_2026-05-23.json`

---

## Target / Source Under Review

P2 source under review:

- `scripts/run_post_phase2b_provider_stability_probe.mjs`
- `docs/reviews/CVF_P2_PROVIDER_SOAK_EVIDENCE_2026-05-23.md`

HN1 source under review:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/data/skill-template-map.json`
- `docs/reviews/CVF_HN1_TEMPLATE_LINKAGE_EXEMPTION_CLOSURE_REVIEW_2026-05-20.md`

P3 source under review:

- `docs/roadmaps/CVF_HOSTED_PRODUCT_READINESS_PROOF_ROADMAP_2026-05-21.md`
- no concrete hosted target/workflow/auth addendum supplied in this tranche.

---

## Scope / Methodology

Method:

1. Re-ran targeted HN1 template/skill linkage tests.
2. Ran the P2 live provider soak with six repeats per provider.
3. Ran the mandatory release gate bundle after the live soak.
4. Compared results against the GC-018 candidate requirements.
5. Preserved P3 as hold because its prerequisite details remain absent.

---

## HN1 Re-Verification

HN1 was already closed on 2026-05-20 by adding explicit exemptions for the two
folder-navigation template IDs:

- `individual_skills_folder`
- `vibe_workflow_folder`

Current re-verification command:

```powershell
npx vitest run src/lib/templates/governance-enforcement.test.ts src/lib/skill-template-map.test.ts --reporter=verbose
```

Result:

- 2 test files passed;
- 22 tests passed;
- all skill-template map entries reference real template IDs;
- every mapped `skillId` exists in the active skill library;
- all form templates are present in `skill-template-map.json`;
- wizard governance wrapper checks remain passing.

HN1 disposition: `CLOSED_REVALIDATED`.

Boundary: no skill corpus expansion, no runtime routing change, no template
category expansion, no public claim that every template requires a one-to-one
skill.

---

## P2 Provider Soak

P2 command:

```powershell
$env:CVF_POST_PHASE2B_PROVIDERS='alibaba,deepseek'
$env:CVF_POST_PHASE2B_REPEATS='6'
$env:CVF_POST_PHASE2B_PROVIDER_STABILITY_PORT='3223'
node scripts/run_post_phase2b_provider_stability_probe.mjs
```

Result:

| Provider | Model | Repeats | Pass | Fail |
| --- | --- | ---: | ---: | ---: |
| Alibaba | `qwen-turbo` | 6 | 6 | 0 |
| DeepSeek | `deepseek-chat` | 6 | 6 | 0 |
| Total | mixed | 12 | 12 | 0 |

Every journey had:

- HTTP 200;
- `success=true`;
- non-mock output;
- governance receipt present;
- trace/envelope id present;
- `evidenceMode=live`;
- route id `/api/execute`;
- routing decision `ALLOW`;
- provider match;
- raw secret printed `false`.

P2 disposition: `CLOSED_BOUNDED_SOAK_PASS`.

Boundary: this is stronger than the prior two-provider 3-repeat window, but
still bounded to local governed `/api/execute`, Alibaba `qwen-turbo`, and
DeepSeek `deepseek-chat`. It is not broad provider stability, all-provider
parity, hosted readiness, production readiness, or runtime remediation.

---

## P3 Disposition

P3 remains `CONDITIONAL_HOLD`.

Reason: no hosted target URL/platform, protected workflow, auth/token path,
secret posture, or explicit pass/fail criteria were supplied for this tranche.

This closure does not implement or prove hosted protected workflow behavior.

---

## Verification

| Check | Result |
| --- | --- |
| HN1 targeted vitest | PASS, 22/22 |
| P2 live provider soak | PASS, 12/12 |
| Raw secret printed | `false` |
| Release gate bundle | PASS, 7/7 |

Release gate command:

```powershell
python scripts/run_cvf_release_gate_bundle.py --json
```

Release gate result:

- web build: PASS;
- TypeScript check: PASS;
- provider readiness: PASS, `CERTIFIED lanes: 3`;
- secrets scan: PASS;
- docs governance: PASS;
- Playwright UI mock: PASS;
- Playwright live governance: PASS.

---

## Findings / Position

Position: `CLOSED_P2_HN1_P3_HELD`.

Findings:

- HN1 remains correctly closed as explicit folder-template exemption hygiene.
- P2 passed a bounded two-provider live soak with `12/12` successful governed
  executions.
- P3 cannot be executed from the current information because no hosted target,
  protected workflow, auth/token path, or pass/fail workflow was supplied.

---

## Risk / Corrective Action

| Risk | Corrective action |
| --- | --- |
| P2 result is overread as broad provider stability | Closure and evidence limit the claim to local `/api/execute`, Alibaba `qwen-turbo`, DeepSeek `deepseek-chat`, six repeats per provider. |
| HN1 stale linkage work regenerates | Closure points to existing `exemptTemplateIds` and targeted tests. |
| P3 is accidentally treated as closed | This review keeps P3 as `CONDITIONAL_HOLD` until hosted target/workflow/auth details exist. |

---

## Decision

Decision: close the executable part of the tranche as
`CLOSED_P2_HN1_P3_HELD`.

The next allowed move is not more provider soak by default. Continue only if a
fresh operator request narrows a new value target, or if P3 receives concrete
hosted target/workflow/auth details.

---

## Claim Boundary

This review closes P2 and HN1 only. It does not close P3, does not update the
public repository, does not claim broad provider stability, does not claim
hosted readiness, and does not change CVF runtime/provider semantics.
