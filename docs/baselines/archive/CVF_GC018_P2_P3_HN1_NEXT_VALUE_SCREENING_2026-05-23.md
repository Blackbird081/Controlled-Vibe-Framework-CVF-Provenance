# CVF GC-018 P2 P3 HN1 Next-Value Screening

Memory class: SUMMARY_RECORD

Status: CLOSED_P2_HN1_P3_CONDITIONAL_HOLD

Date: 2026-05-23

## Purpose

Open the fresh GC-018 requested by the operator for the remaining post-P1
next-value candidates:

- `P2_LONGER_HORIZON_PROVIDER_STABILITY_SOAK`
- `P3_HOSTED_PROTECTED_WORKFLOW_PROOF`
- `HN1_TEMPLATE_SKILL_LINKAGE_HYGIENE`

The goal is to prevent the next agent from treating these as equal or already
implemented work. This packet records what is authorized, what is conditional,
and what remains blocked until a narrower work order exists.

## Scope

In scope:

- screen P2, P3, and HN1 against the current private baseline;
- rank the three candidates by value, risk, and evidence readiness;
- define the smallest acceptable proof/evidence shape for each candidate;
- keep public repository and hosted-readiness boundaries explicit;
- preserve the F-1 diminishing-returns stop rule and all post-A2 closure
  boundaries.

Out of scope:

- provider adapter changes, router changes, prompt/model tuning, token-cap
  tuning, or SSE/runtime lifecycle remediation;
- public npm release, hosted deployment, or public deployment claim;
- public-sync changes unless a later selected tranche explicitly requires
  public-safe evidence publication from the sibling public-sync clone;
- new governance semantics, new receipt envelope fields, new role taxonomy,
  durable persistence/database work, Maika proof, or freeze release.

## Source / Predecessor Evidence

Predecessors:

- `AGENT_HANDOFF_V11_2026-05-21.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/baselines/archive/CVF_GC018_POST_A2_PUBLIC_READINESS_AND_NEXT_VALUE_SCREENING_2026-05-22.md`
- `docs/baselines/archive/CVF_GC018_PUBLIC_DEPENDENCY_AUDIT_TRIAGE_2026-05-22.md`
- `docs/reviews/archive/CVF_A2_COHERENCE_EQUIVALENCE_AUDIT_COMPLETION_2026-05-22.md`
- `docs/reviews/archive/CVF_POST_PUBLICIZATION_PROVIDER_STABILITY_HARDENING_COMPLETION_2026-05-21.md`
- `docs/roadmaps/archive/CVF_HOSTED_PRODUCT_READINESS_PROOF_ROADMAP_2026-05-21.md`
- `docs/roadmaps/archive/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md`

Current closed baseline:

- Review-CVF G1/D2/E2/H2/F2/A2 is closed for the current private baseline.
- P0 public release-gate evidence refresh is closed.
- P1 public developer onboarding proof is closed.
- The P1 public dependency-audit residual is closed.
- Public-sync is clean at public commit
  `27e0ee63 fix(web): close public dependency audit residual`.

Operator request:

```text
Open a fresh GC-018 for P2 provider soak, P3 hosted protected workflow proof,
and HN1 hygiene.
```

## GC-018 Candidate Screening

| Candidate | Class | Score | Decision | Rationale |
|---|---:|---:|---|---|
| P2 longer-horizon provider stability soak | VALIDATION_TEST / LIVE_EVIDENCE | 8/10 | AUTHORIZE_AS_NEXT_SUBSTANTIVE_CANDIDATE | It directly tests the highest remaining evidence gap after two narrow provider windows. It must stay route/provider/model bounded and must use real provider calls. |
| HN1 template-skill linkage hygiene | PACKAGING_ONLY / CATALOG_HYGIENE | 7/10 | AUTHORIZE_AS_LOW_RISK_HYGIENE_CANDIDATE | It is small, data-backed, and can retire a stale linkage question. It should classify the two known unmapped template IDs without widening the skill corpus. |
| P3 hosted protected workflow proof | VALIDATION_TEST / HOSTED_EVIDENCE | 6/10 | CONDITIONAL_HOLD | Valuable, but not executable until a concrete hosted target, auth/token posture, protected workflow, and allowed environment are named. Local production proof is already closed. |

## Depth Audit

Scoring scale: each dimension is 0-2.

| Candidate | Risk Reduction | Decision Value | Machine Enforceability | Operational Efficiency | Portfolio Priority | Total | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| P2 provider soak | 2 | 2 | 2 | 1 | 1 | 8 | Continue only as a bounded live soak work order. |
| HN1 hygiene | 1 | 1 | 2 | 2 | 1 | 7 | Continue as small catalog hygiene if the operator wants fast cleanup. |
| P3 hosted proof | 2 | 2 | 1 | 0 | 1 | 6 | Hold until hosted target and protected workflow are concrete. |

## Candidate Requirements

### P2 Longer-Horizon Provider Stability Soak

Authorized shape:

- use existing governed `/api/execute` path only;
- use existing stable provider/model lanes unless a later work order narrows a
  different lane explicitly;
- run live provider calls only, never mock;
- record HTTP status, success flag, provider, model, decision, evidence mode,
  receipt id, trace id, pass/fail count, and raw-secret-print status;
- run the mandatory release gate before any public-safe evidence update.

Minimum boundary:

- no provider runtime changes;
- no provider tuning;
- no prompt/template/model/token-budget tuning;
- no broad provider stability, all-provider parity, hosted-readiness, or
  production-readiness claim.

### P3 Hosted Protected Workflow Proof

Conditional requirements before execution:

- hosted target URL or platform named by the operator;
- protected workflow and expected auth/token path named;
- secret handling posture confirmed without printing or committing secrets;
- explicit pass/fail criteria for one protected live workflow;
- fallback rule if hosted target is unavailable.

Minimum boundary:

- no public SaaS readiness claim;
- no public deployment readiness claim;
- no multi-tenant readiness claim;
- no private provenance material copied into the public repo.

### HN1 Template-Skill Linkage Hygiene

Authorized shape:

- re-check the current template and skill-linkage inventory before editing;
- classify only the known linkage gap class: `map`, `exempt`, or `retire`;
- if mapping, target skills must already exist in
  `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/public/data/skills-index.json`;
- if exempting, record an explicit reason so future agents do not regenerate
  false dead-reference work;
- keep public claims unchanged unless a separate public-sync update is
  explicitly authorized.

Minimum boundary:

- no new skill corpus;
- no runtime routing change;
- no template category expansion;
- no claim that every template requires a one-to-one skill.

## Decision / Recommended Sequencing

Decision: GC-018 is opened for all three candidates, but implementation is not
bundled.

Recommended sequence:

1. Run HN1 first if the operator wants fast, low-risk cleanup.
2. Run P2 first if the operator wants stronger live evidence and accepts the
   time/key cost of a bounded provider soak.
3. Keep P3 on hold until the operator supplies a hosted target and protected
   workflow.

This packet is enough to open a narrow work order for HN1 or P2. P3 still
requires a concrete hosted-target addendum before execution.

## 2026-05-23 Execution Disposition

Operator follow-up authorized doing both executable candidates to close the
tranche.

Execution disposition:

- P2 longer-horizon provider stability soak: `CLOSED_BOUNDED_SOAK_PASS`.
- HN1 template-skill linkage hygiene: `CLOSED_REVALIDATED`.
- P3 hosted protected workflow proof: `CONDITIONAL_HOLD`.

Evidence:

- P2 evidence:
  `docs/reviews/CVF_P2_PROVIDER_SOAK_EVIDENCE_2026-05-23.md`
- P2 machine-readable evidence:
  `docs/reviews/CVF_P2_PROVIDER_SOAK_EVIDENCE_2026-05-23.json`
- P2/HN1 closure review:
  `docs/reviews/CVF_P2_HN1_TRANCHE_CLOSURE_REVIEW_2026-05-23.md`

P2 result:

- command:
  `$env:CVF_POST_PHASE2B_PROVIDERS='alibaba,deepseek'; $env:CVF_POST_PHASE2B_REPEATS='6'; $env:CVF_POST_PHASE2B_PROVIDER_STABILITY_PORT='3223'; node scripts/run_post_phase2b_provider_stability_probe.mjs`
- live governed `/api/execute` pass count: `12/12`;
- Alibaba `qwen-turbo`: `6/6`;
- DeepSeek `deepseek-chat`: `6/6`;
- every journey had HTTP 200, `success=true`, live evidence mode, route id
  `/api/execute`, receipt id, trace id, routing `ALLOW`, provider match, and
  raw secret printed `false`.

HN1 result:

- current exemption block for `individual_skills_folder` and
  `vibe_workflow_folder` remains valid;
- targeted verification:
  `npx vitest run src/lib/templates/governance-enforcement.test.ts src/lib/skill-template-map.test.ts --reporter=verbose`;
- result: `2` files passed, `22/22` tests passed.

P3 remains held because the required hosted target URL/platform, protected
workflow, auth/token path, and pass/fail criteria were not supplied.

## Evidence Trace Block

Claim: P2, P3, and HN1 are the only remaining review-required candidates named
after P1 and dependency-audit closure.

Evidence:

- `AGENT_HANDOFF_V11_2026-05-21.md`
- `docs/baselines/archive/CVF_GC018_POST_A2_PUBLIC_READINESS_AND_NEXT_VALUE_SCREENING_2026-05-22.md`

Verdict: EXISTS.

Claim: P2 must use live provider proof if it asserts provider behavior.

Evidence:

- `AGENTS.md` mandatory live governance proof rule
- `docs/reviews/archive/CVF_POST_PUBLICIZATION_PROVIDER_STABILITY_HARDENING_COMPLETION_2026-05-21.md`

Verdict: EXISTS.

Claim: P3 is not executable without a hosted target.

Evidence:

- `docs/roadmaps/archive/CVF_HOSTED_PRODUCT_READINESS_PROOF_ROADMAP_2026-05-21.md`
- prior handoff boundary retaining hosted readiness as unproven

Verdict: EXISTS.

Claim: HN1 is a small linkage hygiene question, not a dead-reference emergency.

Evidence:

- `docs/roadmaps/archive/CVF_POST_PAIN_POINT_CLOSURE_HARDENING_ROADMAP_2026-05-20.md`

Verdict: EXISTS.

Counter-evidence: none found in the current session.

## Claim Boundary

This GC-018 opens screening and authorization boundaries only. It does not
complete P2, P3, or HN1; does not change runtime behavior; does not update
public-sync; does not claim broad provider stability; does not claim hosted or
public deployment readiness; and does not lift any governance-kernel freeze.
