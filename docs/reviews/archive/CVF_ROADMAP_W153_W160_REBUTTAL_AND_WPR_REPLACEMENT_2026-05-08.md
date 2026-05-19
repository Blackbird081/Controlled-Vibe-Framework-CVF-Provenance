# CVF Roadmap W153–W160 Rebuttal + WPR Replacement

**For:** Codex (executor)  
**Date:** 2026-05-08  
**Authority:** git log + AGENT_HANDOFF.md + README.md HEAD `99a811eb` + filesystem verification  
**Conclusion:** Proposed roadmap is invalid for execution because it duplicates
several artifacts that are already present. **Do not execute the original
W153-W160 sequence.** Execute the narrower WPR roadmap below instead.

---

## Part 1 — Why the Original Roadmap is Wrong

### 1.1 Roadmap Underweights Current State

The earlier roadmap is too generic for the actual state on `main` HEAD
`99a811eb` (2026-05-08). It does not explicitly reopen W133/W134, but it treats
several already-delivered public-readiness surfaces as if they still need to be
created from scratch:

| Wave | Codex Assumes | Reality |
|---|---|---|
| W134 (HTTP 400 pre-AI-call) | active blocker | **CLOSED** commit `22fcf5b6` |
| W135–W141 | not done | **CLOSED** — output validation, retry budget, UI matrix timeout, browser lifecycle, trusted-form disambiguation |
| W142–W147 | not done | **CLOSED** — TRUSTED_FORM_MAP expanded 8 → 40 entries |
| W149 trusted-form live value gate | not done | **CLOSED** — Alibaba direct **40/40**, browser UI **40/40**, DeepSeek **12/12** |
| W150–W152 | not done | **CLOSED** — corpus split, test split, claim sync |
| Release gate | unclear | **PASS 7/7** (2026-05-08) |
| RC packet | "W160 first" | **published 2026-04-21** (RC Truth Packet, Demo Script, Known Limitations Register, Public RC Roadmap) |
| Public claim boundary | "W156 first" | **exists** in README sections "What CVF Can Publicly Claim Today" + "What CVF is not claiming today" |
| Technical design front door | "W153 first" | **added** in HEAD `99a811eb` (section + module table) |

### 1.2 Five of Eight Waves Duplicate Existing Artifacts

| Codex Proposes | Already Exists |
|---|---|
| **W153** Public Developer Onboarding Pack | `README.md` "Developer Technical Design" + `ARCHITECTURE.md` + `START_HERE.md` + `docs/reference/CVF_ARCHITECTURE_MAP.md` + `docs/reference/CVF_ARCHITECTURE_DIAGRAMS.md` |
| **W154** One-Command Local Demo | `README.md` "Quick Run: Web UI" + `scripts/bootstrap_foundations.ps1/sh` + `scripts/new-cvf-workspace.ps1` |
| **W155** Public Non-Coder Demo Path | W149 proved 40-form trusted front door live-usable; demo path in `docs/guides/CVF_DEMO_SCRIPT_2026-04-21.md` |
| **W156** Public Evidence Pack Refresh | `CVF_RELEASE_CANDIDATE_TRUTH_PACKET_2026-04-21.md` + `CVF_LIVE_EVIDENCE_PUBLICATION_PACKET_2026-04-21.md` + `CVF_KNOWN_LIMITATIONS_REGISTER_2026-04-21.md` + `CVF_PUBLIC_NONCODER_VALUE_STATEMENT_2026-04-17.md` + `CVF_PROVIDER_LANE_READINESS_MATRIX.md` |
| **W160** Public Release Candidate Tag | RC state declared 2026-04-21 with 4 artifacts |

→ Executing 5 of 8 waves as written would likely rewrite or duplicate existing
artifacts, creating GC-022 memory overrecording risk and GC-032 governed
artifact authoring drift.

### 1.3 Conceptual Error

Codex frames this as **"public-readiness prep"**. Wrong. CVF is **already in RC state** since 2026-04-21. This is **"post-RC public-release packaging"** — different stage, different artifacts:

- **Public-readiness prep** = write basic docs, claim boundary, demo. → DONE.
- **Post-RC public-release packaging** = open contributor surface, deployment surface, exposure audit, bind tag. → REAL GAPS.

---

## Part 2 — Replacement Roadmap (WPR: Public Release)

**Code:** `WPR` (Public Release packaging), 4 waves. Each wave is a separate GC-018 candidate, not bundled.

### WPR-1 — Contributor / Extension SDK Boundary Doc

**Why:** CONTRIBUTORS.md exists but only lists attribution. No doc explains "where extension/skill/template authors add new things, what they cannot touch".

**Scope:** Create `docs/reference/CVF_EXTENSION_AUTHOR_BOUNDARY.md` (new), content:

1. How to add 1 trusted form template (path: template file → `trusted-form-corpus.ts` registration → activation test → release gate).
2. How to add 1 provider lane (canary script + readiness matrix entry + live-key handling).
3. How to add 1 skill to library (rescreen standard + GC-044 trusted subset boundary).
4. How to add 1 governance guard (`governance/toolkit/05_OPERATION/` pattern).
5. Clear "do not touch" list:
   - `ECOSYSTEM/doctrine/` (FROZEN)
   - `v1.0/`, `v1.1/` baseline layers
   - frozen test files in exception registry (EPF/CPF/LPF index.test.ts)
   - GC-018 tranche scope without explicit authorization

**Verification:**
- File ≤ 200 lines (GC-023)
- Cross-link from `CONTRIBUTORS.md` and README "Contributing" section
- Pre-commit hook PASS

**Boundary:** Doc only, no runtime changes.

---

### WPR-2 — Multi-Target Deploy Guide

**Why:** `netlify.toml` exists; deploy hints scattered across files; no canonical single deploy guide for community.

**Scope:** Create `docs/guides/CVF_DEPLOY_GUIDE.md` (new), content:

1. **Local development** (already in README, link there).
2. **Netlify** (canonical, reference `netlify.toml`; env var checklist; live key boundary — no raw key commits).
3. **Vercel** (alternative; env var mapping; build command equivalent).
4. **Docker** (if Dockerfile exists, reference it; else provide minimal template).
5. **Live key policy** (reference `docs/reference/CVF_PROVIDER_LANE_READINESS_MATRIX.md` and README "Mandatory Live Governance Proof").
6. **Release gate verification post-deploy** (`python scripts/run_cvf_release_gate_bundle.py --json`).

**Verification:**
- File ≤ 250 lines (GC-023)
- Netlify section verifiable against real `netlify.toml`
- Cross-link from README "Quick Run" and "New Machine Quick Start"

**Boundary:** No actual deployment, no credential commits, no runtime changes.

---

### WPR-3 — Public Exposure Sweep (Pre-Wide-Release Audit)

**Why:** Before wide public release, audit comprehensively to avoid leaks. `.private_reference/` already in `.gitignore:72` ✓ — but need to verify 4 additional aspects.

**Scope:** Create `docs/reviews/CVF_PUBLIC_EXPOSURE_AUDIT_2026-05-08.md` recording audit findings + open issues/fixes if discovered.

**Audit Checklist:**

1. **License headers:** Scan all `EXTENSIONS/*/package.json` + source files, verify each extension has LICENSE or inherits from root LICENSE (CC BY-NC-ND 4.0).
2. **Raw API keys in fixtures:** Grep recursively for pattern `sk-*`, `dashscope_*`, `DASHSCOPE_API_KEY=`, `ALIBABA_API_KEY=` in all tracked files (excluding `.env.example` and `docs/reference/*` documentation).
3. **Internal handoff text leak:** Verify `.private_reference/` and raw
   internal-only notes are not accidentally tracked. Canonical tracked files
   such as `AGENT_HANDOFF.md`, Claude transfer notes, and
   `docs/reviews/cvf_phase_governance/` may be `ACCEPTED_BOUNDARY` rather than
   automatic leaks when they are intentionally part of CVF's public evidence
   chain.
4. **Stale TODO/FIXME with personal info:** Grep `TODO.*@`, `FIXME.*@`, `// HACK` to find PII or internal references.
5. **Config secrets:** Verify `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/.env.local` is not tracked; only `.env.example` is tracked.

**Verification:**
- Audit report file passes GC-023 size limit
- Every finding is in one of three states: `RESOLVED`, `ACCEPTED_BOUNDARY` (with justification), `DEFERRED_TO_WPR_4`
- Release gate still PASS after audit

**Boundary:** Do not push public repository in this wave; audit only. Public-wide release is WPR-4.

---

### WPR-4 — Public RC Tag + CHANGELOG Binding

**Why:** RC packet published but no git tag binding. Community cloning repo doesn't know "which version is RC?".

**Scope:**

1. Update `CHANGELOG.md` with new entry:
   - Version: `v4.0.0-rc.1` (or per current semantic versioning from `docs/VERSIONING.md`)
   - List: W114–W152 closed, RC packet artifacts, release gate 7/7 PASS, multi-provider operability proven
   - Link to `docs/reference/CVF_RELEASE_CANDIDATE_TRUTH_PACKET_2026-04-21.md`
2. Create annotated git tag `v4.0.0-rc.1` on current HEAD.
3. Update `README.md` badge `version-4.0.0%20Runtime` to `version-4.0.0--rc.1`.
4. Create GitHub Release notes draft referring to CHANGELOG and RC packet.
   Publishing the GitHub Release itself is human/CLI-token dependent; if no
   GitHub release tool is available, prepare the release notes in-repo and leave
   publication as an operator step.
5. Update `AGENT_HANDOFF.md` state header to `RC1 TAGGED` for clear baton handoff.

**Verification:**
- `git tag -l v4.0.0-rc.1` returns tag
- CHANGELOG entry passes document naming guard
- README badge link valid
- WPR-3 audit must PASS before this wave (gate)

**Boundary:** This is **release candidate tag**, not GA. Keep `rc.1` clear so community understands this is still evidence-bounded.

---

## Part 3 — Execution Order (binding)

```
WPR-1 (contributor doc)   →  WPR-2 (deploy guide)
                          ↓
                       WPR-3 (exposure audit) ← gate for WPR-4
                          ↓
                       WPR-4 (RC tag)
```

WPR-1 and WPR-2 can run in parallel. WPR-3 must complete clean before WPR-4. Each wave closes independently with GC-018 + closure decision doc + handoff sync.

---

## Part 4 — Execution Prohibitions

Codex **must not** execute the following under any wave:

1. **Do not** rewrite "Developer Technical Design" — already in README HEAD `99a811eb`.
2. **Do not** rewrite "Public Claim Boundary" — already in README + 5 reference docs.
3. **Do not** rewrite RC packet — `CVF_RELEASE_CANDIDATE_TRUTH_PACKET_2026-04-21.md` is canonical.
4. **Do not** touch W134 — already closed commit `22fcf5b6`.
5. **Do not** touch `ECOSYSTEM/doctrine/`, `v1.0/`, `v1.1/`, frozen test files.
6. **Do not** rebuild trusted-form corpus — W149–W152 already canonical 40-form.
7. **Do not** add new provider lane in this roadmap — separate track after RC.

---

## Part 5 — Verification Commands

```bash
# Before each wave
git status
git log --oneline -5
python scripts/run_cvf_release_gate_bundle.py --json

# After each wave
python scripts/run_cvf_release_gate_bundle.py --json   # must PASS 7/7
git diff --stat                                          # review impact
```

WPR-3 audit-specific:
```powershell
git ls-files | rg -i "private|internal|\\.env\\.local"
git grep -n -E "sk-[a-zA-Z0-9]{20,}|dashscope-[a-zA-Z0-9]+"
```

Audit output must be classified, not blindly treated as failure. Expected
canonical docs may be `ACCEPTED_BOUNDARY`; raw keys or tracked `.env.local`
must be `RESOLVED` before WPR-4.

WPR-4 tag-specific:
```bash
git tag -l "v4.0.0-rc.1"           # must exist after wave
git show v4.0.0-rc.1 --stat        # verify annotated tag
```

---

## Part 6 — Summary for Operator

| Item | Status |
|---|---|
| Codex original roadmap (W153–W160) | **REJECT** — 5/8 waves duplicate existing artifacts |
| W134 blocker | closed (`22fcf5b6`) — no separate wave needed |
| Trusted-form 40-form | live-proven (W149) — no re-prove needed |
| RC packet | published 2026-04-21 — no re-create needed |
| Public claim boundary | in README + 5 reference docs |
| Replacement roadmap | **WPR-1 → WPR-2 → WPR-3 → WPR-4** (4 focused waves) |
| Total scope | ~4 new files + 1 git tag + CHANGELOG entry. No runtime changes. |
| Risk class | R0–R1 (docs + audit + tag) |

**End of rebuttal.** Codex executes WPR-1 first, one wave at a time, with standard CVF GC-018 + closure decision per tranche.

---

## Appendix: File Checklist

**To create:**
- `docs/reference/CVF_EXTENSION_AUTHOR_BOUNDARY.md` (WPR-1)
- `docs/guides/CVF_DEPLOY_GUIDE.md` (WPR-2)
- `docs/reviews/CVF_PUBLIC_EXPOSURE_AUDIT_2026-05-08.md` (WPR-3)

**To update:**
- `CHANGELOG.md` (WPR-4)
- `README.md` badge (WPR-4)
- `AGENT_HANDOFF.md` state header (WPR-4)

**To create (git):**
- Tag `v4.0.0-rc.1` (WPR-4)
- GitHub Release notes (WPR-4)

**To verify (no changes needed):**
- `.gitignore:72` still has `.private_reference/` ✓
- `netlify.toml` exists ✓
- RC packet files exist ✓
