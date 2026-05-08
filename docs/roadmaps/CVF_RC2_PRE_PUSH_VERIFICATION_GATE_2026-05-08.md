<!-- Memory class: FULL_RECORD -->
# CVF RC2 Pre-Push Verification Gate

**Date:** 2026-05-08  
**For:** Codex (executor)  
**Authority:** Operator decision; standing rule on live governance proof  
**Posture:** BLOCKING — `git push origin main` is **not authorized** until all four blockers below are cleared on top of HEAD `78c92362`.

---

## State

RC2 Track A (A0–A2) + Track B (B0–B3) + Track C (C0–C4) are CLOSED on local `main`. There are 13 commits ahead of `origin/main` and **none have been pushed**. Each wave's closure decision records targeted Vitest results only, not the full release gate. The standing rule still applies: *all governance behavior claims must use live provider API calls. The operator has provided live Alibaba and DeepSeek API keys for this verification.*

RC2 cannot be declared closed until the four blockers below are addressed and committed on top of `78c92362`.

---

## Blocker 1 — Full Release Gate Has Not Been Run for RC2

Each RC2 wave (A0–C4) closure decision records only **targeted Vitest results**, never `python scripts/run_cvf_release_gate_bundle.py --json`. The pattern from W141 / W149 / WPR-1..WPR-4 was: end every wave with full release gate `7/7 PASS`. RC2 broke this pattern across 12 consecutive waves.

**Required action:**

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

Must return `7/7 PASS` (web build, TypeScript check, provider readiness, secrets scan, docs governance, UI mock Playwright, **live governance Playwright**). If any check fails, do not push; fix and re-run.

---

## Blocker 2 — C3 / C4 Governance Code Has No Live Provider Proof

C3 introduced an allowlisted job runner; C4 added a UI that triggers governance jobs through that runner. Both touch governance behavior (audit trail, RBAC enforcement, redaction, secret-safe output). Per the standing rule, governance behavior must be proven against a real provider, not unit tests + UI mock alone.

**Required live evidence specs:**

1. **Live RBAC enforcement proof:** with a real Alibaba / DeepSeek key configured, trigger a `provider_check` job through the C4 UI as `viewer` (must be blocked), `operator` (must succeed and audit), `admin` (must succeed and audit). Store the audit JSONL excerpt as evidence.
2. **Live redaction proof:** trigger `provider_check alibaba` and `provider_check deepseek` through the C4 UI; verify the recorded `stdoutSummary` / `stderrSummary` contain no key fragment, no full key, no `sk-...` pattern. Confirm with grep against the audit JSONL.
3. **Live timeout proof:** force a job timeout (low `timeoutMs` override or unreachable provider) and confirm `status=timed_out`, lifecycle correct, no orphaned subprocess.
4. **Live release-gate dry readiness:** trigger `release_gate_dry_readiness` once through the C4 UI with a real key; confirm output is dry-readiness only and that this path does not actually fire the full live gate from Web.

**Evidence file:** `docs/reviews/CVF_RC2_C3_C4_LIVE_GOVERNANCE_EVIDENCE_2026-05-08.md` — include audit JSONL excerpts (key-redacted), role classification per request, and result class per scenario.

---

## Blocker 3 — Two Public Maturity Claims Need Bounded Live Evidence

Before CVF can publicly state "good enough for non-coders" or "good enough for developers" past RC1, each claim requires bounded live evidence on top of the existing W149 / W114 corpus. These are **RC2 spot-checks**, not new W-tranches.

### Claim N — Non-coder maturity

A non-coder using `v4.0.0-rc.1` can reach a useful governed output within the documented setup time, with evidence visible in the UI.

- **Required:** 1 live end-to-end run on Alibaba lane through the trusted-form web front door, captured screen + receipt, visible governance evidence panel populated.
- **Boundary:** RC2 noncoder spot-check only; do not re-open W122–W129 noncoder adoption tranches.
- **Evidence file:** `docs/reviews/CVF_RC2_NONCODER_LIVE_SPOT_CHECK_2026-05-08.md`.

### Claim D — Developer maturity

A developer can clone `v4.0.0-rc.1`, run `cvf_doctor.py`, run `cvf_provider_check.py --provider alibaba` (and `--provider deepseek`), run `cvf_setup.py`, reach the Web health page, see the runtime module registry, see the governance evidence readout, and trigger a non-destructive job through the C4 UI — all on a real local clone with a real key.

- **Required:** capture the doctor JSON, provider check JSON for both lanes, screenshot of B1 health UI / B2 module registry / B3 evidence panel / C4 operations UI, and one audit JSONL job record.
- **Boundary:** Windows only (per A2 commitment). macOS / Linux remain `DEFERRED_PLATFORM`.
- **Evidence file:** `docs/reviews/CVF_RC2_DEVELOPER_LIVE_SPOT_CHECK_2026-05-08.md`.

---

## Blocker 4 — Pre-Existing Typecheck Drift Decision

Every RC2 closure note repeats: *"full `npx tsc --noEmit` remains blocked by pre-existing test typing drift recorded in B1."* This has been carried across 6+ closures without resolution. Before RC2 push, choose one:

- **Resolve:** fix the drift (preferred if scoped < ~30 min).
- **Accept and bound:** record an explicit `ACCEPTED_BOUNDARY` entry in the closest applicable governance compatibility registry, listing the affected files and the reason. Cite the entry from the next handoff.
- **Defer with named owner:** open a tracked follow-up entry with a target wave (e.g. `RC2-T-typecheck`) and an explicit responsible party. No more silent carry-forward across closures.

---

## Push Authorization

`git push origin main` is **not authorized** until Blockers 1, 2, 3, and 4 are addressed in commits on top of HEAD `78c92362`. After the four evidence/decision artifacts exist and the release gate passes, push and update the handoff state to `RC2 Foundation CLOSED — pushed`.

---

## Standing Rule Reaffirmed

The operator has provided live Alibaba and DeepSeek API keys for this verification. Mock mode is **not acceptable** for these blockers. Do not propose mock substitutes. Do not propose deferring live proof. The whole point of CVF claiming governance is that the claim can be proven live, repeatedly, with real providers.
