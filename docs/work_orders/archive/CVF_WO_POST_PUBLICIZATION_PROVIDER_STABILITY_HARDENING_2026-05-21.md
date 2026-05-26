# CVF Work Order Post Publicization Provider Stability Hardening

Memory class: FULL_RECORD

Status: CLOSED

docType: work_order

Date: 2026-05-21

---

## Purpose

Execute the bounded post-publicization provider-stability hardening roadmap.

---

## Authority Chain

- Operator instruction: 2026-05-21 "tiếp tục next roadmap".
- Active state: `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- Roadmap:
  `docs/roadmaps/CVF_POST_PUBLICIZATION_PROVIDER_STABILITY_HARDENING_ROADMAP_2026-05-21.md`
- GC-018:
  `docs/baselines/CVF_GC018_POST_PUBLICIZATION_PROVIDER_STABILITY_HARDENING_2026-05-21.md`
- Prior PBR completion:
  `docs/reviews/CVF_POST_PHASE_2B_PUBLICIZATION_READINESS_COMPLETION_2026-05-21.md`
- Active handoff: `AGENT_HANDOFF_V10_2026-05-19.md`

---

## Agent Roles

Codex performs all roles for this bounded tranche:

- Orchestrator: resolve the valid next candidate and open the tranche.
- Implementer: run the live second-window proof and public-sync delta if
  permitted.
- Reviewer: evaluate evidence and file completion.
- Auditor: run governance checks and sync session state.

---

## Scope / Target / Owner Boundary

Allowed scope:

- PSH-01 second-window provider repeatability for Alibaba and DeepSeek.
- PSH-02 mandatory release gate.
- PSH-03 bounded public evidence delta if proof passes.
- Completion review and session sync.

Forbidden scope:

- Broad provider stability claim.
- New providers, provider runtime changes, timeout/SSE/router changes, or
  provider method expansion.
- Persistence/database implementation.
- Maika child-data/photo/vision proof.
- Hosted/product readiness claim.
- Kernel-owner replacement.
- Global freeze lift.

Risk ceiling: R2.

---

## Operator Checkpoint

Checkpoint source: operator request on 2026-05-21 to continue the next
roadmap.

Interpretation: proceed with the least-risk valid candidate from active state:
bounded provider-stability hardening. Any expansion beyond this work order
requires another operator checkpoint.

---

## Write Ownership

Owned by this work order:

- `docs/roadmaps/CVF_POST_PUBLICIZATION_PROVIDER_STABILITY_HARDENING_ROADMAP_2026-05-21.md`
- `docs/baselines/CVF_GC018_POST_PUBLICIZATION_PROVIDER_STABILITY_HARDENING_2026-05-21.md`
- `docs/work_orders/CVF_WO_POST_PUBLICIZATION_PROVIDER_STABILITY_HARDENING_2026-05-21.md`
- `docs/reviews/CVF_POST_PUBLICIZATION_PROVIDER_STABILITY_HARDENING_COMPLETION_2026-05-21.md`
- public-sync evidence/catalog files if PSH-01 and PSH-02 pass
- active session continuity files

Not owned:

- provider runtime source;
- Maika app/runtime source;
- persistence/database source;
- kernel owner or freeze-release artifacts.

---

## Target / Source Under Review

Primary proof command:

```powershell
$env:CVF_POST_PHASE2B_PROVIDERS='alibaba,deepseek'; $env:CVF_POST_PHASE2B_REPEATS='3'; $env:CVF_POST_PHASE2B_PROVIDER_STABILITY_PORT='3221'; node scripts/run_post_phase2b_provider_stability_probe.mjs
```

Mandatory release gate:

```powershell
python scripts/run_cvf_release_gate_bundle.py --json
```

---

## Required First Reads

- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/reviews/CVF_POST_PHASE_2B_PUBLICIZATION_READINESS_COMPLETION_2026-05-21.md`
- `docs/roadmaps/CVF_POST_PUBLICIZATION_PROVIDER_STABILITY_HARDENING_ROADMAP_2026-05-21.md`
- `AGENTS.md`

---

## Pre-Flight Checks

Commands:

```powershell
git status --short
git remote -v
```

For public-sync:

```powershell
git remote -v
```

---

## Evidence Requirements

- `node scripts/run_post_phase2b_provider_stability_probe.mjs` with
  `CVF_POST_PHASE2B_REPEATS=3`.
- `python scripts/run_cvf_release_gate_bundle.py --json`.
- Public-sync remote verification before public push.
- Public static CI gate after public edits.
- Docs governance compatibility.
- Markdown structural completeness.
- Active session state compatibility.
- Local hook chain.

---

## Execution Plan

1. Run PSH-01 second-window repeatability proof.
2. Run PSH-02 mandatory release gate.
3. If both pass, update public-sync with a bounded second-window evidence
   delta.
4. File completion review.
5. Update active session continuity.
6. Run governance checks.
7. Commit and push provenance changes.

---

## Acceptance Criteria

- PSH-01 returns `PASS`, `6/6`, with `3` repeats per provider.
- Each journey records provider, model, decision, routing decision, receipt id,
  trace id, route id, evidence mode, and no mock fallback.
- PSH-02 release gate passes.
- PSH-03 public-sync update, if made, uses only bounded language and records
  the public commit SHA.
- No raw API key values are printed or committed.

---

## Review Gate

Required checks before provenance commit:

- JSON parse for active state and review queue.
- Active session state compatibility.
- Docs governance gate.
- Markdown structural completeness gate.
- Git whitespace check.
- Local governance hook chain.

---

## Closure Checklist

- [x] Roadmap filed.
- [x] GC-018 accepted.
- [x] Work order filed.
- [x] PSH-01 second-window proof run.
- [x] PSH-02 release gate run.
- [x] PSH-03 public-sync disposition recorded.
- [x] Completion review filed.
- [x] Active session continuity synced.

---

## Return-To-Orchestrator Conditions

Return for a new GC-018/work order before starting:

- broad provider stability;
- hosted/product readiness;
- provider runtime remediation;
- persistence/database implementation;
- Maika child-data/photo/vision proof;
- kernel-owner replacement;
- any freeze-release work.

---

## Claim Boundary

This work order can close only bounded second-window two-provider
repeatability. It does not claim broad provider stability, all-provider parity,
production/hosted readiness, persistence/database readiness, Maika proof,
kernel-owner replacement, or global freeze lift.
