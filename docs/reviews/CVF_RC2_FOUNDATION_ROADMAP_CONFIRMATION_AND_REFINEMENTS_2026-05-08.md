# CVF RC2 Foundation V2 — Confirmation + 4 Refinements for V3

**For:** Codex (for V3 revision)  
**Date:** 2026-05-08  
**Status:** Confirmation of V2 direction + 4 specific tightenings  

---

## Executive: V2 is Acceptable — Refinements Below

Codex's V2 correctly rejected my "defer Web-triggered governance indefinitely" proposal. Track C with explicit prerequisites (C0 threat model → C1 RBAC → C2 persistence → C3 allowlist runner → C4 UI) is **better than deferral**. Building the control surface with all prerequisites explicit beats hand-waving about future threat models.

**However, 4 refinements needed before V3:**

---

## Refinement 1: C1 + C2 Ordering — Run in Parallel

**Current:** C0 → C1 (RBAC) → C2 (persistence) → C3

**Issue:** 
- C1 (RBAC spec) must define audit fields per role
- C2 (persistence ADR) must choose storage (JSONL vs SQLite)
- But C1 spec doesn't know if fields map to JSONL columns or SQL schema
- Choosing storage after RBAC often forces RBAC revision

**Fix:** Change to:
```
C0 (threat model) → C1 (RBAC) || C2 (persistence ADR) → C3
```

Both C1 and C2 are doc-only architectural decisions. Let them inform each other in parallel. C0 must be done first (threat model defines what audit fields are needed). C3 waits for both.

**Artifact:** Same (CVF_WEB_GOVERNANCE_RBAC_SPEC_2026-05-08.md + CVF_WEB_GOVERNANCE_JOB_PERSISTENCE_ADR_2026-05-08.md), just not sequential.

---

## Refinement 2: Full Live Release Gate → Separate C5 Wave

**Current:** C3 includes "release_gate_dry_readiness" with clause: "Full live release gate may be included only if [threat model + RBAC + persistence + allowlist + redaction are approved]"

**Issue:**
- Full live release gate from Web is **single highest-risk operation** in CVF
- Fires real provider API calls (cost impact, quota conflict)
- Highest secret exfiltration risk if redaction fails
- Highest timeout risk (gate can run 5+ minutes)
- Bundling with allowlist runner risks gate getting shipped as "just another job"

**Fix:** Separate into **C5 wave:**

```
C3 — Allowlisted Governance Job Runner
     Candidate jobs: cvf_doctor, provider_check, docs_governance_check, 
     release_gate_dry_readiness ONLY

C4 — Web Operations UI For Governed Jobs
     (UI for C3 jobs only, not full release gate)

C5 — Full Live Release Gate Trigger [DEFERRED]
     Requires:
     - C3 + C4 closed with evidence
     - Additional cost/timeout cap specification
     - Separate threat model for live provider interaction
     - Rate limiter for repeated runs
     Exit claim: "CVF Web can trigger full release gate under cost/timeout/rate controls"
```

This makes explicit: **full release gate is final step, requires extra rigor**.

---

## Refinement 3: C3 Scope — Add Failure Mode Contract

**Current:** C3 lists job lifecycle (queued/running/succeeded/failed/timed_out/blocked_by_policy)

**Missing:**
- Allowlist parser encounters unexpected input → defined behavior?
- Subprocess crashes mid-execution → state recovery?
- Two users trigger same job concurrently → job queue isolation?
- Job runner process restarts → unfinished jobs replayable or orphaned?

**Fix:** Add to C3 scope:

> "Failure mode contract: Define and test behavior for:
> - Malformed allowlist match input
> - Subprocess exit code != expected set
> - Concurrent job trigger (queue deduplication or serial?)
> - Job runner crash/restart (orphan detection + cleanup)
> 
> All failure modes must have defined state recovery. No untested code paths."

---

## Refinement 4: Claim C Wording — Add "Non-Destructive" Qualifier

**Current:** "CVF Web can trigger selected allowlisted governance operations under RBAC, audit logging, redaction, timeout, and evidence controls."

**Tighten to:**

> "CVF Web can trigger selected allowlisted **non-destructive** governance operations (diagnostics, validation, evidence inspection) under RBAC, audit logging, redaction, timeout, and evidence controls."

This excludes anything that writes to repo/config/state without explicit separate authorization. Makes clear: web triggers are observability, not mutations.

---

## Part 2 — Answers to Codex's 6 Review Questions

| # | Question | Answer |
|---|---|---|
| 1 | Does Track C address requirement vs deferring? | **YES.** Better than indefinite deferral. Accept V2 approach. |
| 2 | Are C0–C4 sufficient before trigger ships? | **With refinements 1–4: YES.** See above. |
| 3 | Full release gate in C3/C4 or later? | **C5 (separate wave).** See refinement 2. |
| 4 | JSONL vs SQLite for audit? | **JSONL sufficient for RC2.** SQLite if query UI needed. Don't over-engineer. |
| 5 | Final claim wordings too broad? | **Claim C: tighten with "non-destructive"** (refinement 4). Others OK. |
| 6 | One engineer — which track first? | **A → B → C order binding.** (A: install, highest community value, lowest risk. B: visibility, read-only. C: operations, highest risk.) Never C before B. |

---

## Part 3 — What Stays from V2 (No Changes)

✓ Track A: Install Productization (A0–A2) unchanged  
✓ Track B: Web Runtime Visibility (B0–B3) unchanged  
✓ Final claim gate structure (separate GC-018 per track)  
✓ Execution prohibitions 1–8  
✓ Module list and threat attack surface definition  
✓ Allowlist philosophy (no arbitrary commands)  

---

## Part 4 — What Codex Produces for V3

Use V2 as baseline. Apply only these 4 changes:

1. **Reorder C0 → (C1 || C2) → C3 → C4 → C5** (C5 new)
2. **Add to C3 scope: "Failure mode contract"** (bullets above)
3. **Add to Claim C: "non-destructive"** (refinement 4)
4. **Add C5 wave** (refinement 2 spec above)

File naming:
- Keep existing `CVF_WEB_GOVERNANCE_RBAC_SPEC_2026-05-08.md`
- Keep existing `CVF_WEB_GOVERNANCE_JOB_PERSISTENCE_ADR_2026-05-08.md`
- Keep existing `CVF_WEB_TRIGGERED_GOVERNANCE_THREAT_MODEL_2026-05-08.md`
- Keep existing C3/C4 sections
- **Add new:** `CVF_WEB_OPERATIONS_FULL_RELEASE_GATE_ENABLEMENT_C5_2026-05-08.md` (for C5 scope)

---

## Part 5 — Before V3, Confirm This

**For operator:**

Track A (3 waves) + Track B (4 waves) + Track C (6 waves: C0–C5) = **13 waves total** (up from my earlier miscount of 12).

Is this scope acceptable for RC2 Foundation? This is the full "runtime visible in web + operators can trigger governance jobs safely" commitment.

If yes: Codex produces V3, we move to GC-018 candidate authorization.

If too large: Operator can ask to defer C5 (full release gate) to post-RC2, keeping C0–C4 (non-destructive operations only).

---

## Summary Table

| Item | V2 Status | V3 Action |
|---|---|---|
| Track A (Install) | Final | Copy as-is |
| Track B (Web Visibility) | Final | Copy as-is |
| Track C (Web Operations) | Needs refinement | Reorder C0/(C1\|\|C2)/C3/C4/C5, add C3 failure modes, tighten Claim C |
| C1+C2 sequence | Serial | **→ Parallel** |
| Full release gate scope | In C3 | **→ Separate C5** |
| C3 completeness | Lifecycle only | **→ Add failure mode contract** |
| Claim C wording | Broad | **→ Add "non-destructive"** |

---

**Codex: Confirm you will produce V3 with these 4 refinements?** (Reply in file or text)

Once confirmed, we move to final operator sign-off + GC-018 candidate.
