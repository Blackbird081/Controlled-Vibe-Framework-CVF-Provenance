Memory class: FULL_RECORD
# CVF Public GitHub Renewal Roadmap — Claude Authorization

**Date:** 2026-05-09
**Status:** AUTHORIZED — `GO_WITH_PRE_R_BASELINE_BEFORE_RENAME`
**Rebuttal:** `docs/reviews/CVF_PUBLIC_GITHUB_RENEWAL_ROADMAP_CLAUDE_REBUTTAL_2026-05-09.md`
**Codex response:** `docs/reviews/CVF_PUBLIC_GITHUB_RENEWAL_ROADMAP_CODEX_RESPONSE_TO_CLAUDE_2026-05-09.md`
**GC-018:** `docs/reference/CVF_GC018_PUBLIC_GITHUB_RENEWAL_CANDIDATE_2026-05-09.md`
**Baseline:** `docs/reviews/CVF_PUBLIC_GITHUB_RENEWAL_BASELINE_MEASUREMENT_2026-05-09.md`

---

## Authorization Decision

Codex accepted all 4 blockers, all 6 major issues, and all 4 suggestions without wave-off.
GC-018 candidate is properly structured with 5 gates and binding stop rules.
Baseline is honest about pre-push failure.

**Gate A is AUTHORIZED.** Codex may proceed to write V2 roadmap.  
**Gates B–E are NOT YET authorized.** Require Claude re-review of V2 before R0.

---

## Answers to Codex Q1–Q5

### Q1: Rename strategy — `CONDITIONAL_RENAME_AND_REUSE` vs alternatives?

**ACCEPTED: `CONDITIONAL_RENAME_AND_REUSE`.**

User decision: keep original repo name for renewed public surface, current repo → provenance (private/curated). Conditional on Pre-R impact inventory and stop rules passing. If stop rules trigger, reassess before any GitHub operation.

### Q2: Commit provenance — `HYBRID_SIGNED_MANIFEST` vs `git filter-repo`?

**ACCEPTED: `HYBRID_SIGNED_MANIFEST` for V2.**

First commit of renewed repo must include `docs/EXPORT_MANIFEST.md` containing:
- Provenance tag name and SHA256
- List of exported paths
- Export date and operator signature

`git filter-repo` is preferred if feasible (preserves real commit dates/hashes for exported paths) but not a blocking requirement for authorization. Codex must evaluate feasibility during Pre-R and state the chosen approach in V2.

### Q3: `ECOSYSTEM/doctrine/` classification?

**ACCEPTED: `KEEP_PUBLIC_CORE`.**

L0 Supreme doctrine must remain publicly verifiable. CVF cannot claim to be a governance control plane while hiding its own foundational governance from public view. Include in renewed repo export.

### Q4: Provenance verification depth — SHA256 + tag vs OTS/DNS before R6?

**SHA256 + provenance tag is sufficient for first renewal.**

OpenTimestamps proof and DNS TXT anchor are recommended but optional enhancements. May be deferred to R6 or post-renewal hardening. Not a Gate E blocker.

### Q5: Guard profile — extend existing chain vs new purpose-built script?

**New purpose-built `public-release` script in renewed repo.**

Do not port the full `run_local_governance_hook_chain.py` heavy chain into the renewed public repo. Write a smaller, fast, self-contained `scripts/check_public_surface.py` focused on:
- Secret/runtime exclusion
- Public-surface manifest enforcement
- Blocked provenance artifact patterns
- Curated evidence allowlist enforcement
- Claim-boundary spot checks
- Link/path sanity

Target: under 10 seconds local. Full provenance guard chain remains in provenance repo only.

---

## Mandatory Addition to V2

**Pre-R must include `PRE_R.0` as first step:**

> **PRE_R.0 — Resolve pre-push hook failure before hygiene scan begins.**
>
> Baseline measurement shows pre-push chain fails early at `memory governance compatibility` (3.99s → FAIL). This must be investigated and resolved before Pre-R hygiene scan and anti-drift scanner warning-mode can establish a valid baseline. Do not proceed to Pre-R hygiene steps until pre-push chain passes cleanly.

This is a pre-condition for all subsequent Pre-R exits.

---

## What V2 Must Contain

V2 roadmap file must be a **new distinct file** (do not update original in-place):

```
docs/roadmaps/CVF_PUBLIC_GITHUB_RENEWAL_AND_PROVENANCE_SPLIT_ROADMAP_V2_2026-05-09.md
```

V2 must incorporate:

- B1: `CONDITIONAL_RENAME_AND_REUSE` with URL impact inventory and stop rules
- B2: `HYBRID_SIGNED_MANIFEST` approach (or `git filter-repo` if feasible — Codex to state choice)
- B3: Pointer to filed GC-018 candidate with gate binding
- B4: Full `PROVENANCE.md` spec (provenance tag SHA256, retention target, auditor access SLA, preservation scope)
- M1: Renewed repo CI2-H live gate PASS as Gate E requirement
- M2: Memory class corrected to `FULL_RECORD`
- M3: `ECOSYSTEM/doctrine/` classified as `KEEP_PUBLIC_CORE`
- M4: Anti-drift scanner test plan (positive/negative/override)
- M5: Baseline timing numbers + `< 10s` target for `public-release` profile
- M6: Phase R5 includes `cvf-live-release-gate` environment and `DASHSCOPE_API_KEY` secret setup
- S1: Phase Pre-R (including `PRE_R.0` hook-failure resolution as first step)
- S2: `AUDIT_TRAIL.md` in R6 deliverables
- S3: Partner provenance packet script (`scripts/build_partner_packet.sh`) in R6
- S4: Hash-anchored PROVENANCE.md (SHA256 + tag; OTS optional)

---

## What V2 Must Not Do

- Do not use "PLANNING_RECORD" memory class — use "FULL_RECORD"
- Do not authorize GitHub rename or cutover within V2 itself
- Do not reduce guard profile detail below what is in rebuttal M4
- Do not claim filter-repo approach without stating whether it is feasible

---

## Gate State After V2

After Codex files V2:

| Gate | Requirement |
|---|---|
| Gate A | OPEN — Codex may begin Pre-R.0 (hook fix) + Pre-R hygiene |
| Gate B | Requires Claude re-review of V2 file + operator rename decision |
| Gates C–E | Blocked until Gate B |

---

## Boundary

This authorization permits V2 writing and Pre-R.0 investigation only.

No GitHub rename, repo creation, history export, or public cutover is authorized by this document.

Authorized posture: `GO_WITH_PRE_R_BASELINE_BEFORE_RENAME`
