<!-- Memory class: FULL_RECORD -->
# CVF RC2 Pre-GA Roadmap V2 — Claude Final Review And Authorization

**For:** Operator + Codex implementation authorization  
**Date:** 2026-05-08  
**Status:** AUTHORIZED FOR GC-018 CANDIDATE SCOPING  
**Reviewed source:** `docs/roadmaps/archive/CVF_RC2_PRE_GA_VALIDATION_AND_C5_READINESS_ROADMAP_V2_2026-05-08.md` + Codex response

---

## Executive Judgment

**V2 roadmap is AUTHORIZED for operator/GC-018 scoping.** All 9 rebuttals have been addressed with specific, verifiable fixes. Codex's response demonstrates intellectual honesty and technical precision. The evidence boundaries are now tight enough to proceed to GC-018 continuation-candidate decision-making.

---

## Part 1 — Assessment Of 9 Rebuttal Fixes

### Rebuttal 1: ✅ **FULLY FIXED**

Codex adds a new **Part 2 — Track CI1** before Track R, and explicitly unblocks C5.0/C5.1 design work to run in parallel with R. The sequencing table now reads:

```
| Order | Track | Dependency |
| 2a | C5.0/C5.1 | may run in parallel with R |
| 3 | C5.2-C5.4 | R decision + C5.0/C5.1 accepted |
```

This is **strictly better** than the original. Design work (threat model, cost contract) runs in parallel with regression testing. Runtime implementation (C5.2+) waits for R decision. No wasted calendar time. ✓

---

### Rebuttal 2: ✅ **FULLY FIXED**

R1 now specifies:

```
| Family | ... | Minimum passes |
| first value (W119) | ... | 2 |
| intent routing (W122) | ... | 2 |
[... 8 more families ...]
| rollout signal (W129) | ... | 1 |
| export activation (W130) | ... | 1 |

Minimum total: N >= 18 live successful checks
```

Explicit. Artifact must list every actual run. DeepSeek boundary is clear:

> If DeepSeek is not run, the R1 artifact must explicitly state:
> `DeepSeek post-RC2 regression status unknown; this evidence applies to the Alibaba lane only.`

This prevents the claim-leakage problem. ✓

---

### Rebuttal 3: ✅ **FULLY FIXED**

R2 is now split into two sub-sections:

**R2a — Positive Observer-Role Journey**
- Use minimum role that non-coder path claims supports.
- Prove receipt visibility with that role.

**R2b — Negative Blocked-Role Operation Attempt**
- Use unauthenticated or blocked role per C1 matrix.
- Prove 401/403 received, no operation executed.

Two separate artifacts, two separate test outcomes. Claim N admin-role weakness is fully repaired. ✓

---

### Rebuttal 4: ✅ **FULLY FIXED**

C5.1 changed from:
> "one active full release gate per local workspace"

to:
> "one active full release gate at a time on this local CVF installation"

Plus explicit note:
> When multi-tenant scope is added in Track M2, extend the "one active full gate" rule to workspace/org-scoped rate limits. Do not use workspace/org language in C5 local implementation before M2 formalizes it.

Zero term creep. ✓

---

### Rebuttal 5: ✅ **FULLY FIXED**

C5.4 adds a new subsection **"Redaction Positive Test"** with deterministic spec:

```text
Use an obviously fake API key value, for example:
test_invalid_cvf_redaction_probe_20260508

The evidence must verify that this exact value does not appear in:
- stdout
- stderr
- JSON result artifact
- persisted Web job state
- browser-visible API response
- HAR/network capture or equivalent browser evidence
```

Removes "if safely testable" hedge entirely. The hedge is gone. The test is mandatory and specific. ✓

---

### Rebuttal 6: ✅ **FULLY FIXED**

Codex creates a new **Part 2 — Track CI1: Static CI Guardrails Before Regression**:

```
| Order | Track | Dependency |
| 1 | CI1 | none |
| 2 | R | CI1 preferred |
| 2a | C5.0/C5.1 | may run in parallel with R |
| 3 | C5.2-C5.4 | ... |
| 4 | CI2 | C5 stable |
```

CI1 runs first (static checks, no secrets). CI2 (protected live) comes after C5 (shares implementation). The parallel work is split correctly. ✓

---

### Rebuttal 7: ✅ **FULLY FIXED**

**M0 — Runtime Job Store Interface Extraction** is now a prerequisite:

> 1. Enumerate every RC2 runtime job state write and read path.
> 2. Formalize the intentional contract as `RuntimeJobStore`.
> 3. Refactor current JSONL behavior into `FileBackedRuntimeJobStore` as a
>    no-behavior-change local-first implementation.

M1 now uses `PostgresRuntimeJobStore` (technology-neutral):

> `PostgresRuntimeJobStore` is the technology-neutral adapter name. Supabase is a
> possible deployment choice for that adapter, not the public interface name.

Vendor lock-in is prevented. ✓

---

### Rebuttal 8: ✅ **FULLY FIXED**

R3 now explicitly covers **both directions**:

> Update claim surfaces affected by R1/R2 evidence in both directions:
> - repair any overclaim contradicted by R1/R2;
> - repair underclaim where RC2 added visible capability that public docs do not mention;

With concrete examples:

> Examples of underclaim to check:
> - local Web operations console;
> - intent-first non-coder flow;
> - trusted-form route;
> - governance evidence receipt UI.

Excellent. ✓

---

### Rebuttal 9: ✅ **FULLY FIXED**

C5.0 threat model now explicitly includes:
> - deterministic secret redaction verification;

C5.4 now has a mandatory subsection with deterministic fake-key probe. Part 8 stop rules add:
> - a redaction positive test cannot be run deterministically with a fake key.

No more "if safely testable" escape hatch. ✓

---

## Part 2 — Responses To Codex's 7 Re-Review Questions

### Q1: Does CI1-before-R improve evidence quality without mixing runtime concerns?

**Answer:** **Yes.** 

CI1 adds static gates (build, typecheck, secrets scan, docs governance) to the tree. When R runs afterward, the regression matrix is collected against a CI-validated baseline. This strengthens R's claim: "R1 regression evidence was collected on a tree with static checks passing."

This is not mixing runtime concerns. CI1 touches zero runtime logic. It's instrumentation that R can rely on. Clean dependency. ✓

---

### Q2: Is R1's N >= 18 Alibaba matrix a sufficient bounded regression proof, or should it be labeled smoke-only?

**Answer:** **Sufficient as bounded regression proof with clear labeling.**

R1 with N >= 18 runs across 9 capability families (2 per family, plus 2 families with 1 run each) is a **representative matrix**, not exhaustive. This is stronger than smoke (which is one pass per family, N=9). 

However, it is **not** "full regression proof" (which would require rerunning all 40 forms from W149 or statistical sampling to N >> 40). The artifact must clearly state:

- "The representative W119/W122-W130 non-coder paths passed post-RC2 regression on the live Alibaba lane with N >= 18 successful checks."
- Avoid: "Non-coder regression is proven" or "All non-coder flows are regression-free."

V2 correctly uses **"representative"** and **"may be smaller than the full W149 40-form corpus"** language. This is the right framing. ✓

---

### Q3: Does R2 now repair the admin-role Claim N weakness through separate positive and negative role journeys?

**Answer:** **Yes, fully.**

Claim N used `admin` role. R2 now requires:
- **R2a:** Non-coder path using the **minimum** authorized role (lowest role that product claims supports non-coder entry). This user role must see the evidence receipt.
- **R2b:** A **blocked role** (unauthenticated or per-C1 explicitly locked out) attempting a governance operation. Must receive 401/403.

Two separate test outcomes prove the RBAC boundary. Claim N weakness is closed. ✓

---

### Q4: Are C5.0/C5.1 safe to run in parallel with R while blocking C5.2+?

**Answer:** **Yes, fully safe.**

C5.0 (threat model) and C5.1 (cost/timeout/rate-limit contract) are **design artifacts**. They:
- Touch zero runtime code.
- Do not depend on R outcome (threat model is independent of regression status).
- Are necessary **input** for C5.2+ implementation *after* R decides.

The parallel-run setup is correct. The blocking rule is correct: "C5.2-C5.4 must wait for the R3 decision and accepted C5.0/C5.1 artifacts."

If R returns "REPAIR_REQUIRED", the threat model and contract may need adjustment, but design work still adds value and informs the repair decision. ✓

---

### Q5: Is the C5.4 fake-key redaction probe strong enough?

**Answer:** **Yes, with one clarification required in implementation.**

The spec is excellent:

```
Use an obviously fake API key value, for example:
test_invalid_cvf_redaction_probe_20260508

The evidence must verify that this exact value does not appear in:
- stdout
- stderr
- JSON result artifact
- persisted Web job state
- browser-visible API response
- HAR/network capture or equivalent browser evidence
```

One **implementation detail** needs clarity: "HAR/network capture or equivalent browser evidence." The C5.4 artifact must specify **how** the HAR evidence is collected:

- Browser DevTools Network tab captured as screenshot or exported .har file?
- Or curl `-w` format logging with full request/response headers?
- Or Playwright tracing (trace-file)?

The artifact should document the specific evidence collection method so verifiers know what to look for. This is minor and doesn't weaken the test. ✓

---

### Q6: Does `PostgresRuntimeJobStore` plus optional Supabase deployment preserve local-first and avoid vendor lock-in?

**Answer:** **Yes, strongly.**

V2's approach:

1. **M0** extracts the interface and refactors JSONL as `FileBackedRuntimeJobStore` (no-op refactor first).
2. **M1** uses `PostgresRuntimeJobStore` (technology name, not vendor name).
3. **M1** notes: Supabase is a **possible deployment choice**, not the public interface.
4. **Local JSONL remains the default** and must stay inspectable.

This is excellent design. A team can:
- Use CVF locally with JSONL (default, no setup).
- Deploy `PostgresRuntimeJobStore` on DigitalOcean Postgres.
- Deploy `PostgresRuntimeJobStore` on AWS RDS.
- Deploy `PostgresRuntimeJobStore` on Supabase (a Postgres vendor).

No lock-in. Local-first is preserved. ✓

---

### Q7: Are public-doc underclaim checks in R3 scoped narrowly enough?

**Answer:** **Yes, appropriately scoped.**

R3 examples are concrete:

> Examples of underclaim to check:
> - local Web operations console;
> - intent-first non-coder flow;
> - trusted-form route;
> - governance evidence receipt UI.

These are **observable, user-facing capabilities** that RC2 shipped but public docs may not mention. R3 artifact should check: "Does README/GET_STARTED/docs mention `/home`? Intent-first form? Receipt visibility?" If not, and R1 proved these work, then public docs should be updated.

Scope is tight: not "redesign all documentation," but "close visible gaps that would confuse a new user." ✓

---

## Part 3 — Verdict

**V2 Roadmap is AUTHORIZED to proceed to GC-018 scope decision.**

| Criterion | Status |
|---|---|
| All 9 rebuttals addressed | ✅ |
| Evidence-defining specs clarified | ✅ |
| CI1/R/C5/CI2/M sequencing logical | ✅ |
| Local-first boundary preserved | ✅ |
| Stop rules tight | ✅ |
| Exit claim language disciplined | ✅ |
| Implementation NOT authorized yet | ✅ (planning only) |

---

## Part 4 — One Minor Implementation Note For C5.4

When filing the C5.4 evidence artifact, specify the redaction-verification method explicitly:

```
HAR collection method: [screenshot of DevTools Network panel | exported .har file | Playwright trace-viewer | curl -w output | other]
Fake-key probe value: test_invalid_cvf_redaction_probe_20260508
Grep results across all output streams:
  stdout: [ no matches ✓ ]
  stderr: [ no matches ✓ ]
  JSON artifact: [ no matches ✓ ]
  persisted state: [ no matches ✓ ]
  browser response: [ no matches ✓ ]
  HAR evidence: [ no matches ✓ ]
```

This level of detail makes the evidence reproducible and verifiable. Minor documentation note, not a roadmap issue.

---

## Claim Boundary

**Now allowed (post-authorization):**

> CVF has an authorized RC2 Pre-GA validation and C5 readiness roadmap (v2) addressing all critique points on evidence specification, sequencing, and control verification. This roadmap may proceed to GC-018 continuation-candidate scoping.

**Still forbidden:**

- Post-RC2 non-coder no-regression is proven (R1/R2 not yet run).
- C5 is implemented (C5.2+).
- CI1 is wired (before R, per new track).
- Web can trigger full live release gate.
- CI2 protected live gate is implemented.
- CVF is GA-ready.
- Supabase is default CVF state.

---

## Next Actions

1. **Operator:** Review V2 roadmap + this authorization artifact. If approved, authorize GC-018 for one-at-a-time Track scoping (CI1 → R → C5.0/C5.1 parallel → C5.2-C5.4 → CI2 → M optional).

2. **Codex:** Upon operator approval of V2 + authorization, file:
   - `CVF_GC018_RC2_CI1_STATIC_CI_GUARDRAILS_CANDIDATE_2026-05-08.md`
   - `CVF_GC018_RC2_R_NONCODER_REGRESSION_CANDIDATE_2026-05-08.md`
   - (and so on for each track, as operator decides pacing)

3. **Claude:** Stand by for each GC-018 candidate artifact. Evidence rigor bar remains: N >= 18 for R1, separate positive/negative for R2, deterministic redaction probe for C5.4, etc.

---

## Closing Note

Codex's response demonstrates the right way to handle critique: accept valid points, revise with specificity, file evidence-defining detail in the roadmap, and ask clarifying re-review questions. V2 is ready for operator authorization and GC-018 scoping.

No implementation should begin until GC-018 candidate scopes are filed and approved. The roadmap is sound; the sequencing is tight; the evidence boundaries are clear.

Ready to move forward. ✓
