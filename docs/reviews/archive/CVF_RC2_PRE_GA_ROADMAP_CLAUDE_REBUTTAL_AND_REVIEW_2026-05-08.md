<!-- Memory class: FULL_RECORD -->
# CVF RC2 Pre-GA Validation and C5 Readiness Roadmap — Claude Rebuttal + Review

**For:** Codex (executor review and v2 revision authorization)  
**Date:** 2026-05-08  
**Status:** REBUTTAL PLUS STRUCTURED REVIEW — RC2 roadmap is directionally correct, but 9 specific points require clarification before authorization  
**Authority:** Independent critique of draft roadmap logic, evidence specification, and sequencing

---

## Executive Summary

Codex's Pre-GA Validation and C5 Readiness roadmap is **directionally sound**:
- Correctly refuses GA after RC1 tag.
- Right sequencing: prove post-RC2 non-coder no-regression (R) before Web-triggering full release gate (C5).
- Correct architectural boundary: Supabase optional, local-first preserved.
- Disciplined exit claim language (allowed/forbidden pairs).

However, **9 specific points are under-specified or logically flawed**:
1. R → C5 ordering blocks even C5 paperwork (threat model design) that has zero runtime risk.
2. R1 matrix scope under-specified on N (runs per capability family) and lane coverage (DeepSeek absent).
3. R2 conflates observer-role and unauthorized-role tests; likely to pass formality without closing RBAC gap.
4. C5.1 uses "per local workspace" — term smuggles in multi-tenant concept from deferred Track M.
5. C5.4 redaction test is hedged ("if safely testable") — creates way out of verification.
6. CI ordering puts CI1 after C5; should come before R to instrument regression collection.
7. Track M adapter naming and interface extraction are one step short.
8. R3 claim sync covers overclaim but skips underclaim (RC2 added capability public docs don't mention yet).
9. Stop rule on key leakage is a gate, not a verification — no positive test for redaction in this roadmap.

**Recommendation:** Codex reviews this critique + 7 Q&A answers below, revises draft into v2 addressing all 9 points, re-files as authorization artifact. Do not proceed to R/C5/CI implementation on current draft.

---

## Part 1 — Responses to Codex's 7 Review Questions

### Q1: Is Track R sufficient to prove post-RC2 non-coder no-regression without rerunning the entire historical corpus?

**Answer:** Not as currently specified. R1 says "minimum coverage" of 9 capability families, but **does not state how many runs per family**. 

- **If one run per family:** A single passing journey does not refute intermittent regression. W149 ran 40 forms; one per family is a smoke check, not a regression proof.
- **If N ≥ 2 per family:** Depends on whether we're sampling or exhaustive. Codex should specify floor (e.g., "at least 2 per family" or "statistical coverage to N=30 total runs") and update R1 artifact to list actual runs executed, not just families covered.
- **Failure mode if unspecified:** R passes formality, C5 proceeds, users discover intermittent failures in production that RC2 hardening introduced but single-run matrix missed.

**Required fix:** R1 artifact must state minimum runs per family and account for variance. If reusing some W149 runs, state explicitly which and why they remain valid post-RC2.

---

### Q2: Is R2 strong enough to repair the earlier RC2 Claim N admin-role weakness?

**Answer:** No — R2 as written conflates two separate tests.

Claim N used `admin` session to verify receipt visibility. This is a **role boundary issue**: does *lowest-authorized* role see the evidence receipt? And separately: does *unauthorized* role get blocked from governance operations?

R2 currently reads: "run at least one live browser journey under the lowest role … verify that unauthorized Web governance operations remain blocked."

This is **one test** written as two. The matrix needs:
- **Positive:** Lowest-authorized role (e.g., `viewer` or `developer` per C1 matrix) opens `/home`, submits intent-first form, receives execution and **sees governance evidence receipt**.
- **Negative:** A role explicitly locked out of governance (e.g., unauthenticated or `guest` if that tier exists) attempts to trigger a governance operation and **receives 403/401 + no receipt visibility**.

Unless both pass, Claim N weakness remains open. R2 artifact must explicitly document both test outcomes separately.

**Required fix:** R2 to itemize role matrix from C1, define observer vs operator test pair, separate positive/negative evidence.

---

### Q3: Are the C5 controls enough before allowing Web to trigger the full live release gate?

**Answer:** Controls are sound *on paper*, but **C5.4 redaction test is hedged out of testing**. 

C5.0/C5.1 define threat model and rate/timeout/cost contracts. These are architectural. But C5.4 says "missing-key or invalid-preflight behavior if **safely testable** without printing secrets" — this is a way out.

Every control that touches secrets **must be tested deterministically**:

```bash
export ALIBABA_API_KEY="test_invalid_XXXXXXXX"
python scripts/run_cvf_release_gate_bundle.py --json 2>&1 | tee full_output.log
# Assert: (a) command fails with expected error
# Assert: (b) grep "test_invalid_XXXXXXXX" full_output.log == 0 (no matches)
# Assert: (c) grep in browser DevTools network tab == 0 (no key in HTTP response)
# Assert: (d) grep in persisted job artifact == 0 (no key stored)
```

Using a *fake* value is safe (it's not a real secret). Grepping for it is testable. Omitting this leaves redaction a design claim, not a proven control.

**Required fix:** C5.4 must include deterministic redaction probe. Remove "if safely testable" hedge.

---

### Q4: Should CI integration happen before or after C5, given the need to avoid mixing runtime changes with workflow changes?

**Answer:** Split CI into two lanes with different timing:

- **CI1 (static_pr_gate):** Build, typecheck, unit tests, secrets scan, docs governance. **Land BEFORE R**, not after C5. Instrumenting the tree with CI1 during R execution strengthens R's claim ("evidence collected on CI-validated tree"). Also: zero risk of runtime regression (static checks only), zero need for secrets.
- **CI2 (protected_live_release_gate):** Share canonical command with C5.2. Reasonably comes after C5 implementation is stable. This pair is a unit (runtime code + CI orchestration).

Codex's current sequencing (C5 first, CI later) leaves R evidence unchecked by CI infrastructure. Flipping CI1 before R costs nothing and gains signal quality.

**Required fix:** Add CI1 sub-track before R. Mark CI2 as "after C5 stable" in Part 6 sequencing.

---

### Q5: Does Track M preserve the operator's local-first boundary clearly enough?

**Answer:** Boundary is clear *semantically*, but **two implementation details are one step short**:

1. **Adapter naming:** `SupabaseRuntimeJobStore` presumes a specific vendor. Better naming: `PostgresRuntimeJobStore` (technology-agnostic). Supabase = Postgres + Auth + RLS + dashboard. If we name the adapter `Supabase*`, switching to self-hosted Postgres later requires public API renaming.

2. **Interface extraction:** M0 says "introduce a storage boundary." But before polymorphism, must first **enumerate all RC2 runtime state writes** and formalize as an interface. Then ship the file-backed implementation in a no-op refactor **first**. Only then add managed adapter. Skipping the extraction step risks "Supabase adapter" designed against accidental contract of today, not intentional interface.

**Required fix:** M0 to include interface extraction as a prerequisite; rename `Postgres*` in M1.

---

### Q6: Is Supabase correctly framed as optional managed adapter rather than default CVF state?

**Answer:** Yes, correctly framed. Explicit wording in Part 1 Boundary is clear: "CVF remains local-first for developers ... Supabase/Postgres is only an optional managed-deployment adapter."

This boundary is solid. **No change needed here.**

---

### Q7: Are any claims still too strong for the evidence proposed here?

**Answer:** No overclaims detected, but **one underclaim gap** in R3:

R3 says update "claim surfaces that are affected by R1/R2 evidence." But it covers only:
- `AGENT_HANDOFF.md`
- Claude transfer note
- **public known-limits or release notes only if current public wording would overclaim**

This is tuned to prevent overclaim. But RC2 **added** Web operations UI (C3/C4) that README / GET_STARTED have not mentioned yet. Current public docs are **silent** on new capability, which is an underclaim. Users clone the repo and don't know the visual Web operations console exists.

R3 should also cover: "Update public surfaces (README, GET_STARTED) if RC2 added capability that users would reasonably expect to find documented."

**Required fix:** R3 to address underclaim case, not just overclaim.

---

## Part 2 — 9 Specific Rebuttals (Implementation Detail Level)

### Rebuttal 1: R → C5 Ordering Blocks Paperwork With Zero Runtime Risk

**Codex claim:** "Do not begin C5 until R1/R2 evidence is filed."

**Issue:** This blocks **all of C5**, including C5.0 (threat model) and C5.1 (cost/timeout/rate-limit contract). These are design artifacts, not code. They touch zero runtime paths, cannot regress anything, and are necessary inputs for R3 claim-sync decision anyway.

**Mechanic failure:** If R decides "SCOPE_REDUCED" or "REPAIR_REQUIRED", then C5 threat model and controls contract must be revised. But that revision happens **regardless** — blocked or not blocked. Blocking design now just delays the contract work that R will inform.

**Recommended fix:** Allow C5.0/C5.1 to run **in parallel** with R. Block only C5.2 (job type implementation), C5.3 (UI), C5.4 (live evidence) until R concludes. This gains 2–3 weeks of design work without runtime risk.

**Updated sequencing:**
```
R (runs in parallel with →) C5.0/C5.1 (design) → R closes → C5.2/C5.3/C5.4 (implementation)
```

---

### Rebuttal 2: R1 Matrix Scope is Under-Specified on N and Lane Coverage

**Codex claim:** R1 lists 9 capability families, says "minimum coverage: [table with 1 row per family]."

**Issue #2a (N per family):**
- W149 ran 40 forms post-RC1.
- RC2 hardening touched runtime, Web operations job persistence, RBAC.
- One run per capability family = 9 total runs.
- One run does not refute intermittent failure (statistical n=1).
- If any family is async/network-dependent, one pass ≠ stable pass.

**Failure mode:** R1 passes with N=9, C5 proceeds, production user hits race condition in evidence persistence (W142 was routing-intensive) on form #47 because RC2 hardening changed timing under load.

**Issue #2b (lane coverage):**
- W110 certified both Alibaba + DeepSeek.
- RC2 hardening may have regressed DeepSeek in ways Alibaba hides (e.g., token limit handling, latency).
- R1 explicitly says "Alibaba lane only."
- R1 forbidden claim excludes "universal provider parity" — correct.
- But there's a gap: **forbidden claim should be explicit**: "DeepSeek post-RC2 regression status unknown (Alibaba lane only)."

**Recommended fix:** 
- R1 must state minimum runs: e.g., "at least 2 passes per capability family (N ≥ 18 total runs)" or "smoke coverage N ≥ 1, statistical variance not included in regression proof."
- R1 artifact to list actual runs executed, not just families covered.
- Add forbidden claim: "DeepSeek post-RC2 regression status unknown; this evidence applies to Alibaba lane only."

---

### Rebuttal 3: R2 Conflates Observer-Role and Unauthorized-Role Tests

**Codex claim:** "verify that unauthorized Web governance operations remain blocked; verify that the non-coder path can still see the evidence receipt where the product claim says it can; record the role/auth mode explicitly."

**Issue:** One sentence = two separate tests merged into one artifact. RBAC testing requires:
1. **Positive:** Non-coder observer (lowest-authorized role) can see non-coder surfaces (form entry, intent routing, evidence receipt). Example: `viewer` role logs in, opens `/home`, enters intent-first form, sees result + receipt.
2. **Negative:** Unauthorized role (guest, unauthenticated, or a role below `viewer` threshold) attempts to access same surfaces. Result: 401/403, no receipt visible.

Unless both tests run in the R2 evidence artifact, the C1 RBAC matrix is not regression-tested; only the "happy path with some role" is tested.

**Claim N weakness:** Used `admin` role — highest permission. R2 must explicitly use the **minimum** role that the non-coder path is claimed to support.

**Recommended fix:**
- R2 artifact to enumerate C1 role matrix.
- Define observer role (minimum role that should see non-coder features).
- Define blocked role (example of role that should not).
- File two separate browser journeys with outputs:
  - Positive: observer role → sees receipt.
  - Negative: blocked role → 403 or cannot navigate to non-coder path.

---

### Rebuttal 4: C5.1 Uses "Per Local Workspace" — Smuggles Multi-Tenant Concept

**Codex claim:** "one active full release gate per local workspace; owner/admin/operator only."

**Issue:** "Workspace" is undefined in RC2 context.
- Local-first = one user, one repo clone, JSONL state in file system.
- "Per local workspace" implies a boundary between workspaces (e.g., user Alice's copy vs user Bob's copy on same machine).
- But that boundary doesn't exist until Track M2 introduces `orgId` and `workspaceId`.
- Using "workspace" before M2 is **term creep from deferred scope**.

**Mechanic failure:** If someone implements C5.1 controls using "per-workspace" namespacing, then M2 has to retrofit. Or if C5.1 is written assuming M2 semantics, RC2 local-first violates its own "no Supabase by default" rule.

**Recommended fix:** Simplify C5.1 wording:
- "one active full release gate at a time on this local CVF installation"
- Remove "workspace" until M2 formalizes org/workspace boundary.
- Add note: "When multi-tenant scope is added in Track M2, extend this to 'per workspace' with org-level rate limits."

---

### Rebuttal 5: C5.4 Redaction Test is Hedged with "If Safely Testable"

**Codex claim:** "missing-key or invalid-preflight behavior **if safely testable without printing secrets**."

**Issue:** This is a way out of testing. "If safely testable" = subjective escape hatch. But redaction is a **security control**, not a "nice-to-have" — it must be tested deterministically.

**Safe test exists:**
```bash
# Use a test key value that is obviously fake
export ALIBABA_API_KEY="test_invalid_deadbeef_12345678"

# Run the full gate
python scripts/run_cvf_release_gate_bundle.py --json > output.json 2> errors.log

# Verify:
# (a) Command fails (key is invalid)
grep -i "unauthorized\|invalid" errors.log || echo "FAIL: no error for invalid key"

# (b) Test key value NEVER appears in output
grep "test_invalid_deadbeef_12345678" output.json && echo "FAIL: key leaked in JSON" || echo "PASS: not in JSON"
grep "test_invalid_deadbeef_12345678" errors.log && echo "FAIL: key leaked in stderr" || echo "PASS: not in stderr"

# (c) Check browser DevTools / network tab does not contain key
# (recorded in evidence screenshot or HAR file)
```

Using a *fake* value is safe — it's not a real secret. This test is repeatable, verifiable, and proves redaction works.

**Recommended fix:** Remove "if safely testable" hedge. Make C5.4 mandatory:
- Add sub-item: "Redaction Verification: Run full release gate with invalid test key (e.g., `test_invalid_...`). Verify key value does not appear in stdout, stderr, JSON artifact, or browser network output."
- File the test output as part of C5.4 evidence.

---

### Rebuttal 6: CI Ordering Puts CI1 After C5; Should Come Before R

**Codex claim:** "Track CI: Release Gate Automation ... Status: Candidate track after C5 or in parallel only if implementation is strictly non-overlapping."

**Issue:** Codex conflates CI1 (static) and CI2 (protected live). But they have different dependencies:

- **CI1 (static_pr_gate):** Build, typecheck, unit tests, secrets scan, docs governance. **Zero runtime risk. Zero need for secrets.** Can land anytime.
- **CI2 (protected_live_release_gate):** Uses canonical live command. Shares implementation details with C5.2. Reasonably depends on C5.2 stable.

Current sequencing makes both wait for C5, but CI1 gains more value **before** R:
- R runs a representative matrix. Running R on a tree with CI1 gate enabled strengthens R's claim ("regression evidence collected on CI-validated tree").
- R is non-coder path regression. CI1 is static checks (build, lint, secrets). No overlap.
- CI1 lands in 2 days (wire existing checks into a PR gate). R needs 1–2 weeks (run matrix + artifact).

**Recommended fix:** 
- Create **CI1 sub-track** and place it before R in Part 6 sequencing.
- CI2 remains after C5 (shares implementation).
- Update Part 6 to show:
  ```
  CI1 (static) → R (regression matrix) → C5 design // CI1-complete → C5 implementation → CI2 (protected live)
  ```

---

### Rebuttal 7: Track M Adapter Naming and Interface Extraction Are One Step Short

**Codex claim (M1):** "Supabase is a reasonable candidate for hosted/shared CVF because it can provide: Postgres persistence; row-level security; org/workspace scoping; audit retention; managed dashboard queryability."

**Issue #7a (Naming):**
- `SupabaseRuntimeJobStore` presumes a specific vendor in the class name.
- Supabase = Postgres (database) + Auth + RLS + Dashboard (managed service).
- If we name it `Supabase*`, we couple the interface to the vendor.
- Switching to self-hosted Postgres later (DigitalOcean, AWS RDS, on-prem) requires renaming the public interface.

Better: `PostgresRuntimeJobStore` (technology-neutral). If Supabase is chosen, use Supabase as the **configuration**, not the class name. E.g., `PostgresRuntimeJobStore(backend="supabase", ...)`.

**Issue #7b (Interface extraction):**
- M0 says "Introduce a storage boundary only when needed: RuntimeJobStore → FileBackedRuntimeJobStore | SupabaseRuntimeJobStore."
- But before introducing polymorphism, must **first extract the interface** from what RC2 already does.
- RC2 writes runtime state to JSONL files. That behavior should be formalized as an interface contract, then implemented explicitly in a `FileBackedRuntimeJobStore` in a no-op refactor.
- Only *after* file-backed is explicit should managed adapter be added.

Skipping extraction risks designing the Postgres adapter against RC2's **accidental** contract, not an **intentional** interface. Then adding more adapters (CloudSQL, etc.) becomes a Frankenstein.

**Recommended fix:**
- M0 to include interface extraction as prerequisite: "Enumerate all RC2 runtime state writes. Formalize as `RuntimeJobStore` interface. Refactor file-backed code into `FileBackedRuntimeJobStore` as explicit implementation (no-op refactor first)."
- M1 to use `PostgresRuntimeJobStore` (not `SupabaseRuntimeJobStore`).
- Note: Supabase is a **deployment choice**, not an adapter name.

---

### Rebuttal 8: R3 Covers Overclaim But Skips Underclaim Gap

**Codex claim (R3):** "update claim surfaces … public known-limits or release notes only if current public wording would **overclaim**."

**Issue:** R3 is tuned to prevent overclaim (saying CVF can do things it can't). But RC2 added new capability that public docs haven't caught up with yet:

- RC2 shipped Web operations console (C3/C4): intent-first form entry, trusted-form routing, governance evidence visibility.
- README.md and docs/GET_STARTED.md don't mention `/home` endpoint, intent-first flow, or governance evidence receipt UI yet.
- This is **underclaim** (public docs are silent on capability that exists).
- Users clone repo, run `npm run dev`, and don't know the visual operations console is available.

R3 as written ("only if public wording would overclaim") would skip this. But from a product perspective, underclaim = confusing users about what they can do with CVF.

**Recommended fix:** R3 to cover both directions:
- "Update claim surfaces: (a) repair any overclaims that R1/R2 evidence contradicts; (b) **add documentation if RC2 added visible capability that public surfaces don't yet mention.** Example: document `/home` intent-first form, trusted-form path, and governance evidence receipt UI in GET_STARTED if these are live and user-facing."

---

### Rebuttal 9: Stop Rule on Key Leakage is a Gate, Not a Verification

**Codex claim (Part 7):** "Stop and ask for operator decision if ... raw API keys would appear in logs, artifacts, browser output, or CI output."

**Issue:** This is a **stop condition** (gate/blocker), not a **verification procedure** (active test). The roadmap defines:
- What to stop on (gate).
- No corresponding track item that **proves** keys don't leak.

C5.0 threat model lists "artifact integrity and redaction" as a threat. C5.4 says "output redaction verified." But no C5.x sub-item actively tests redaction by running a known-bad key and grepping output streams.

**Comparison:**
- C5.2 says "no free-form argv from browser" → this is a design constraint, should be tested (code review confirms argv not passed).
- C5.4 says "output redacted before persistence" → this **must** be tested (run with test key, verify key does not appear).

Without the positive test, the stop rule is a hope (that no one accidentally logs a key) not a proof (that the redaction path fires correctly).

**Recommended fix:** Add to C5.4:
- "Redaction Positive Test: Run full release gate with invalid test API key (e.g., `ALIBABA_API_KEY=test_invalid_xxxxx`). Verify the key value does not appear in stdout, stderr, JSON artifacts, or browser network output (inspect DevTools HAR or screenshot). File test output and redaction verification in evidence."

---

## Part 3 — Recommendation for Codex

1. **Review this critique + 7 Q&A responses** above. Identify any points where you disagree with the reasoning.

2. **File a response artifact** (e.g., `CVF_RC2_PRE_GA_ROADMAP_CODEX_RESPONSE_2026-05-08.md`) addressing:
   - Do you agree/disagree with each of the 9 rebuttals? (state reasoning if disagree)
   - How will you address the 7 Q&A points in v2 of the roadmap?

3. **Revise the draft into v2** with:
   - R → C5 unblocks design work (C5.0/C5.1 in parallel with R) — addresses rebuttal #1
   - R1 adds N-specification and DeepSeek lane status — addresses rebuttal #2
   - R2 separates positive (observer role sees receipt) and negative (blocked role gets 403) tests — addresses rebuttal #3
   - C5.1 removes "workspace" term — addresses rebuttal #4
   - C5.4 removes "if safely testable" hedge, adds deterministic redaction test — addresses rebuttal #5
   - CI1 (static) placed before R in Part 6 sequencing — addresses rebuttal #6
   - M0 includes interface extraction; M1 renames to `PostgresRuntimeJobStore` — addresses rebuttal #7
   - R3 covers underclaim doc drift (not just overclaim) — addresses rebuttal #8
   - C5.4 adds "Redaction Positive Test" sub-item — addresses rebuttal #9

4. **After v2 is filed and you confirm acceptance of addressing 9 points:** I will authorize R/C5/CI/M tracks to proceed to GC-018 candidate scope decisions.

**Do not authorize implementation on the current draft.** Points #2 (N/lane), #3 (RBAC test split), #5 (redaction determinism), #6 (CI1 reorder), and #9 (redaction probe) are **evidence-defining**. Revising them post-implementation requires re-filing evidence artifacts.

---

## Claim Boundary

Allowed after Codex files response and v2 revised roadmap:

> CVF has a revised post-RC2 Pre-GA validation and C5 readiness roadmap addressing operator critique points on evidence specification, sequencing, and control verification.

Still forbidden:

- Post-RC2 non-coder no-regression is proven (R1/R2 not yet run).
- C5 is implemented.
- Web can trigger full live release gate (C5.2+).
- CI is integrated.
- CVF is GA-ready.
- Supabase is default CVF persistence.

---

## Author Note

This rebuttal is structured to help Codex strengthen the roadmap, not to block it. All 9 points are solvable within the current tracks; none require new tracks or major resequencing. The goal is evidence rigor: if R1 passes with single-run matrix, we should know that's smoke, not regression-proof. If C5.4 claims redaction is tested, we should see the test.

Codex's local-first boundary, stop rules, and exit-claim discipline are strong. This critique sharpens the detail.
