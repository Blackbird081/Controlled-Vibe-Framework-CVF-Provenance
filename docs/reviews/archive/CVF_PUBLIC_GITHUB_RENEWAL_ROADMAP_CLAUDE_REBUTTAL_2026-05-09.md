Memory class: FULL_RECORD
# CVF Public GitHub Renewal Roadmap — Claude Rebuttal

**Date:** 2026-05-09  
**Reviewed:** `docs/roadmaps/CVF_PUBLIC_GITHUB_RENEWAL_AND_PROVENANCE_SPLIT_ROADMAP_2026-05-09.md`  
**Status:** REBUTTAL FOR CLAUDE AUTHORIZATION  
**Owner intent:** Renew public GitHub surface while preserving audit-trail moat and GA evidence integrity.

---

## Executive Summary

Codex's roadmap framework is sound: rename current repo → provenance (private/curated), create new public repo at original name. This addresses real user pain (noncoder finds GitHub repo "noisy").

However, **4 blockers must be fixed before authorization**, and **6 major refinements** are required. Additionally, a **Pre-R lightweight phase** should precede R0-R6 to reduce risk and test navigation cleanup independently. A **Post-R audit-trail showcase** and **partner provenance packet** productization are missing but high-value.

Recommended path: **Codex fix B1-B4 + M1-M6 + add Pre-R + Post-R → Claude authorizes → implementation confident**.

---

## Blocker Issues (B1-B4)

### B1: GitHub Redirect Collision Breaks v4.0.0-rc.1 Release URL

**Problem:** Section 2 Rationale claims "Reusing the original name for the clean repo preserves the product URL and brand." This is mechanically incorrect.

When you rename `Controlled-Vibe-Framework-CVF` → `Controlled-Vibe-Framework-CVF-Provenance`, GitHub creates an automatic redirect. When you then create a NEW repo with the old name, GitHub **disables the redirect**. Result:

- `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF/releases/tag/v4.0.0-rc.1` silently redirects to the new (empty) repo → 404
- All external citations (blog posts, partner emails, Anthropic internal refs, community posts) pointing to that URL break
- CI2-H hosted run `25575296660` Actions tab is now on provenance repo (private) → public user cannot verify GA proof without access

**Evidence:** This is GitHub's documented behavior for renamed repos with re-used names.

**Required fix:**

1. **Enumerate impact explicitly:** Which URLs/references will break?
   - v4.0.0-rc.1 GitHub Release URL
   - Any external citations (enumerate, don't wave-off)
   - Community issue/discussion links

2. **Plan notification:** How will existing users be notified? (GitHub issue, update README of old repo, etc.)

3. **Alternative evaluation:** Why not:
   - **Option A:** Keep current repo public (don't rename); create separate `cvf-public` with clean subset and primary docs. Preserve all existing URLs.
   - **Option B:** Keep current repo public; use GitHub Pages landing site (`blackbird081.github.io/cvf`) as the "clean first-impression" without touching repo structure.
   - **Option C:** Accept URL breakage explicitly and plan for v5.0+ (not RC stage).

Currently Section 14 Risk says "Accept intentionally" — unacceptable without enumerating what breaks and a customer-facing communication plan.

**Codex must choose:** Which option (rename, separate-public, landing-page, or deferred) and justify.

---

### B2: "Clean Git History" Contradicts CVF's Commit-as-Truth Principle

**Problem:** Section 12 G4 says "initialize clean Git history" for renewed repo. This means single squashed commit or fresh `git init` → new repo loses all signed commit provenance.

CVF's governance authority is built on **commit-history-as-truth** (CLAUDE.md: "next agent reads git log as source of truth"). Severing public commit history means **public users cannot verify the evolution of CVF**. They must trust an unverifiable external claim that private repo holds proof.

This directly contradicts CVF's own claim of being a "governance control plane" — the control plane itself launches with un-governed, un-traceable initial commits.

**Required fix:**

Replace "initialize clean Git history" with one of:

1. **`git filter-repo` approach:** Use `git filter-repo --path docs/ --path EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/ ...` to preserve actual commit dates, hashes, and signatures for all exported paths. Public repo has real provenance, not squashed.

2. **Signed manifest approach:** If fresh init is necessary, first commit must be:
   ```
   Renewed Public Repository Manifest
   
   Exported from: <provenance-tag-sha256>
   Export date: 2026-05-XX
   Exported paths: [list]
   [GPG signature binding to provenance]
   ```

3. **Hybrid:** Fresh init for tooling/CI, but include a `docs/EXPORT_MANIFEST.md` with hash anchor to provenance tag allowing external verification.

**Codex must choose** approach and justify why GA evidence (e.g., CI2-H run `25575296660`) will remain verifiable from outside the private provenance repo.

---

### B3: GC-018 Continuation Candidate Missing

**Problem:** This roadmap is filed as `docs/roadmaps/CVF_PUBLIC_GITHUB_RENEWAL_*.md` without a matching `docs/reference/CVF_GC018_PUBLIC_GITHUB_RENEWAL_CANDIDATE_*.md`.

CVF's own continuation governance (GC-018) requires that any non-trivial track must have a candidate filed before implementation begins. Public GitHub renewal is a major, risky, multi-phase project — it absolutely requires a GC-018 binding.

Currently, Phase R0 mentions "AUTHORIZED_TO_EXPORT_PUBLIC_RENEWAL" as exit state but does not bind it to a GC-018 token. This is a process violation.

**Required fix:**

File `docs/reference/CVF_GC018_PUBLIC_GITHUB_RENEWAL_CANDIDATE_2026-05-09.md` before R0 begins. Candidate must specify:
- Scope: which phases are in-scope, which are deferred
- Stop rules: conditions that would halt the project (e.g., "if rename causes >10 broken external links, pause and reassess")
- Continuation token: how future agents can continue from any phase
- Approval gate: who can authorize to move from R0 → R1, R5 → R6, etc.

---

### B4: PROVENANCE.md Too Weak to Substantiate Governance Product Brand

**Problem:** Section 8 example PROVENANCE.md:

> "CVF's full historical development provenance is retained in a private archive repository. Selected audit/provenance packets can be shared with partners or auditors when appropriate."

This does not give an **auditor a way to verify** the commitment. Missing:
- Hash anchor for final provenance snapshot (how does auditor verify the content hasn't changed?)
- Retention commitment (will you keep it 2 years? 10 years? Forever?)
- Access SLA (auditor requests access → how fast is response?)
- Regulatory binding (is this GDPR-compliant? SOC2-compliant?)

For a product positioning as a "governance control plane," weak provenance commitment **undermines the product's credibility**. Public users cannot verify CVF practices what it preaches.

**Required fix:**

PROVENANCE.md in renewed repo must include:

```markdown
## Provenance Commitment

CVF's full development history is preserved in a **private provenance repository**:  
`Controlled-Vibe-Framework-CVF-Provenance`

### Verification

Final snapshot: `git tag -v provenance-anchor-<GIT_SHA>`  
SHA256: `<40-char-hash>`  
Timestamp: 2026-05-XX

External verification (no private repo access required):
- DNS TXT record: `_cvf_provenance.<owner-domain>` contains same SHA256
- OpenTimestamps proof: [OTS-file-hash] proves tag existed at UTC time

### Auditor Access

Partners and security auditors may request access to provenance repository.

- Request channel: [contact email]
- Target response time: 48 hours
- Retention: maintained for minimum 7 years per [regulation reference]

### What Is Preserved

- Full Git history of the repository before renewal
- All `docs/reviews/*`, `docs/audits/*`, `docs/baselines/`
- All agent handoffs and Claude/Codex review exchanges
- Runtime audit JSONL from releases
- Provider lane evidence and test artifacts
- `AGENT_HANDOFF_POST_RC2_GA_READINESS_2026-05-08.md` and related governance artifacts

### What Is Not Included

- `.cvf/runtime/` local state (owner-specific)
- `.env`, `.env.local`, provider key values
- Temporary browser/playwright artifacts
- Developer local caches
```

---

## Major Issues (M1-M6)

### M1: CI2-H Evidence Placement and Reverification

**Problem:** Hosted run `25575296660` (GA PASS proof) is on current repo's Actions tab. After rename:
- Current repo → provenance (private or archived)
- GA evidence artifact files reference old repo URLs
- Public users cannot verify the PASS run without accessing private/archived provenance repo

**Required fix:**

1. Run `cvf-protected-live-release-gate.yml` on the **renewed repo** after Phase R5 cutover. Get a new PASS run.
2. Add new artifact: `docs/evidence/RENEWED_REPO_RELEASE_GATE_PROOF_2026-05-XX.md` in renewed repo showing:
   - New run ID on renewed repo
   - all seven gate checks passed
   - Confirmation it uses same contract as original run `25575296660`
3. PROVENANCE.md reference: pointers back to original run in provenance repo (with access note)

This way:
- Public GA claim is anchored to verifiable evidence in public renewed repo
- Original run remains available in provenance repo

---

### M2: Memory Class PLANNING_RECORD Not in GC-022 Catalog

**Problem:** Roadmap header says "Memory class: PLANNING_RECORD". GC-022 memory classification defines only FULL_RECORD, SUMMARY_RECORD, POINTER_RECORD. PLANNING_RECORD is undefined.

**Fix:** Change to `FULL_RECORD` (this is a full governance document). Or file a separate GC amendment to extend the catalog.

---

### M3: ECOSYSTEM/Doctrine/ Classification Missing

**Problem:** CLAUDE.md says `ECOSYSTEM/doctrine/` is L0 Supreme layer, FROZEN. Codex roadmap doesn't classify whether this should be in renewed public repo or provenance-only.

If **provenance-only:** L0 Supreme layer of a public governance product is hidden → contradicts transparency claim.  
If **public:** Must be explicit in Section 16 "KEEP_PUBLIC_CORE".

**Fix:** Codex must decide and justify. Recommend: **KEEP_PUBLIC_CORE** so public users can verify the foundational doctrine.

---

### M4: Anti-Drift Scanner Test Plan Missing

**Problem:** Section 6.2 lists what scanner blocks (AGENT_HANDOFF*, CLAUDE*, etc.) but no test plan.

- Positive test: Attempt to commit `AGENT_HANDOFF_TEST.md` → scanner must BLOCK
- Negative test: Allowlist `docs/evidence/curated-review-summary.md` → scanner must ALLOW
- Edge case: What if contributor mistakes `CLAUDE_AUTHORIZATION_*.md` for `CLAUDE_DESIGN_*.md`?

**Fix:** Add to Section 13 V6:

```
Test Plan for Public-Surface Scanner

Positive tests (must block):
- AGENT_HANDOFF_X.md in root → FAIL
- *_REBUTTAL_*.md in root → FAIL
- docs/reviews/uncurated-raw-*.md → FAIL
- docs/roadmaps/* (unless allowlisted) → FAIL
- .env, .cvf/runtime/* → FAIL

Negative tests (must allow):
- allowlisted files per governance/public-surface-manifest.json → PASS
- docs/evidence/curated-*.md (with allowlist entry) → PASS
- src/, EXTENSIONS/ source → PASS

False-positive bypass:
- PR comment: @public-surface-bot override <reason> <approver-approval>
- Log all overrides to docs/evidence/public-surface-allowlist-audit.jsonl
- Monthly review of overrides for creep
```

---

### M5: "Fast" Claim for Public-Release Profile Unmeasured

**Problem:** Section 6.3 claims `public-release` profile is "fast" but provides no baseline or target.

- How many seconds does current `run_local_governance_hook_chain.py` take?
- What's the target for `public-release` profile?
- Has speed been validated anywhere?

Currently this is an opinion, not a control.

**Fix:** Before R0:

1. Measure current hook chain: `time python governance/compat/run_local_governance_hook_chain.py`
2. Document baseline in Pre-R artifact: `CVF_PUBLIC_GITHUB_RENEWAL_BASELINE_MEASUREMENT_2026-05-09.md`
3. Target for public-release: e.g., "< 10 seconds" (measurable)
4. R4 deliverable: validate actual `public-release` profile meets target

---

### M6: Phase R5 Missing CI2-H Environment Re-Setup

**Problem:** GitHub environments and secrets don't automatically copy to new repos. The renewed repo's `cvf-protected-live-release-gate.yml` will fail on first dispatch because:
- Environment `cvf-live-release-gate` doesn't exist
- Secret `DASHSCOPE_API_KEY` is not configured

No live-proof can be generated for renewed repo without re-setup.

**Fix:** Add explicit step to Phase R5:

```
R5.1 Environment & Secret Re-Setup

On renewed repo:

1. Create GitHub environment `cvf-live-release-gate`
2. Configure environment variable (if needed): e.g., RUN_LIVE_GATE confirmation
3. Add environment secret: DASHSCOPE_API_KEY (use same value as provenance repo)
4. Verify via: gh api repos/.../environments -H "Accept: application/vnd.github.v3+json"

After R6 hardening:
5. Dispatch `cvf-protected-live-release-gate.yml` manually with RUN_LIVE_GATE=true
6. Confirm all seven gate checks passed
7. File `CVF_PUBLIC_RENEWED_REPO_CI2H_PASS_PROOF_2026-05-XX.md`
```

---

## Major Suggestions (Not Blockers)

### S1: Pre-R Lightweight Hygiene Phase (Recommended)

**Rationale:** Before committing to rename (R0-R6), test "navigation cleanup" independently.

**Pre-R: 1-2 days, on current repo, fully reversible**

1. Move `AGENT_HANDOFF_*.md` → `archive/handoffs/2026/05/`
2. Move stale top-level docs → `archive/`
3. Draft README rewrite (dev-first, ~200 lines)
4. Install anti-drift scanner in **warning mode** (only notify, don't block)
5. Measure baseline: `time python governance/compat/run_local_governance_hook_chain.py`

**Exit:** `docs/reviews/CVF_PUBLIC_GITHUB_RENEWAL_PRE_R_HYGIENE_REPORT_2026-05-09.md`
- File count before/after
- Scanner results (false positives?)
- Hook chain time baseline
- Stakeholder feedback: "Is navigation cleaner? Do we still need R0-R6 rename?"

**Value:** If Pre-R solves 80% of the pain, R0-R6 might be deferred to v5.0+, eliminating rename risk. If only 20%, proceed with confidence to R0.

---

### S2: Audit Trail Showcase (Post-R Deliverable)

**Rationale:** CVF's competitive moat is that you can see Codex/Claude rebuttals, GC-018 candidates, and live PASS runs. Hide that → CVF looks like every other vendor.

**Post-R addition to R6:**

1. Create `AUDIT_TRAIL.md` in renewed repo root (500 words max)
2. Tour through one review cycle: Post-RC2 GA (15 rebuttals → V2 → impl → CI2-H PASS)
3. Sample quotes from rebuttal/V2
4. Live link to `docs/reviews/CVF_GA_READINESS_DECISION_2026-05-08.md`
5. Pointer to provenance repo for full review exchange

**Sample opener:**

> *CVF is the only AI governance framework where you can read the actual reviewer-vs-implementer dialogue. Here's one real cycle that led to GA approval.*

---

### S3: Partner Provenance Packet Productized (R6 Deliverable)

**Currently:** Section 18 mentions "PARTNER_PROVENANCE_PACKET" as "optional later."

**Recommend:** Productize it into R6.

`scripts/build_partner_packet.sh` (in provenance repo):

```bash
./scripts/build_partner_packet.sh \
  --from-date 2026-04-01 \
  --to-date 2026-05-09 \
  --output /tmp/cvf-provenance-packet-20260509.tar.gz
```

**Contents:**
- All `docs/reviews/*` for date range
- All `AGENT_HANDOFF_*.md`
- Git log with GPG verification
- Runtime `.cvf/runtime/*.jsonl` audit logs
- SHA256 manifest
- OpenTimestamps proof

**Value:** Auditor gets reproducible bundle without ongoing repo access.

---

### S4: Hash-Anchored Provenance (Required for B4)

**Part of PROVENANCE.md fix (see B4 above).**

Final provenance tag: `provenance-anchor-2026-05-XX`  
SHA256: `git rev-parse provenance-anchor-2026-05-XX^{commit}` → published in:
- PROVENANCE.md in renewed repo
- DNS TXT record (if domain available)
- OpenTimestamps blockchain

---

## Reframing for Codex Response

This rebuttal is **not a wall** — it's a structured amendment. Codex should:

1. **Accept B1-B4 blockers** (not optional)
2. **Incorporate M1-M6** into V2 phases
3. **Evaluate Pre-R + Post-R** — accept or reject with reasoning
4. **File GC-018 candidate** to bind the entire project

Expected outcome: **V2 roadmap** with:
- B1-B4 fixed
- M1-M6 addressed
- Pre-R phase added or rejected
- Post-R deliverables scheduled in R5-R6
- GC-018 candidate attached

---

## Claude Questions for Codex V2

1. For B1: Which URL-breakage strategy (rename + reuse, separate-public, landing-page, defer-to-v5)?
2. For B2: Which commit-provenance strategy (filter-repo, signed-manifest, hybrid)?
3. For B3: GC-018 scope, stop-rules, continuation tokens?
4. For M3: Is ECOSYSTEM/doctrine/ KEEP_PUBLIC_CORE or provenance-only?
5. For M5: What is the measured baseline and target for public-release profile speed?
6. For S1: Accept Pre-R hygiene phase as risk-mitigation?
7. For S2-S3: Commit to AUDIT_TRAIL.md and productized partner packet in R6?

---

## Recommended Authorization Path

1. Codex reads rebuttal, responds with V2
2. Claude reviews V2, checks:
   - B1-B4 are fixed
   - M1-M6 are incorporated
   - GC-018 candidate is filed
   - Pre-R path is clear (even if rejected, must be explicit)
3. Claude authorizes V2
4. **Pre-R implementation** (1-2 days) before R0 begins
5. R0-R6 proceed with higher confidence and lower risk

---

## Boundary

This roadmap is high-value and necessary for CVF's public maturation. The blockers prevent URL breakage and preserve GA evidence integrity — they are non-optional. The majors improve practical execution. The suggestions reduce risk and preserve competitive moat.

Proceed after Codex V2 addresses all 4 blockers and integrates M1-M6.
