# Work Order - Terminal Hardening Five Option Closure

Memory class: FULL_RECORD

Status: CLOSED_TERMINAL_HARDENING_SWEEP_WITH_BOUNDARIES

docType: work_order

Worker role: Codex

Date dispatched: 2026-05-21

---

## Purpose

Execute the final five-option hardening sweep and then stop.

---

## Authority Chain

- Roadmap:
  `docs/roadmaps/CVF_TERMINAL_HARDENING_FIVE_OPTION_CLOSURE_ROADMAP_2026-05-21.md`
- GC-018:
  `docs/baselines/CVF_GC018_TERMINAL_HARDENING_FIVE_OPTION_CLOSURE_2026-05-21.md`
- Active state:
  `CVF_SESSION/ACTIVE_SESSION_STATE.json`

---

## Agent Roles

Codex performs all roles for this bounded terminal tranche:

- Orchestrator: keep the five-option sweep from becoming a new roadmap wave.
- Reviewer: reject unsupported hosted, stability, or public claims.
- Implementer: run the clean-room proof and public claim audit.
- Auditor: file evidence, update continuity, and commit.

---

## Scope / Target / Owner Boundary

Allowed scope:

- clean-room public clone/install/static proof;
- public-sync claim audit;
- provenance evidence and continuity documents.

Forbidden scope:

- app/runtime/provider source changes;
- hosted deployment configuration;
- persistence/database implementation;
- Maika child-data/photo/vision proof;
- new provider semantics;
- public maturity claim;
- freeze release.

Risk ceiling: R1.

---

## Operator Checkpoint

Checkpoint source: operator request on 2026-05-21 to process the five proposed
hardening options and stop.

---

## Write Ownership

Owned by this work order:

- `docs/roadmaps/CVF_TERMINAL_HARDENING_FIVE_OPTION_CLOSURE_ROADMAP_2026-05-21.md`
- `docs/baselines/CVF_GC018_TERMINAL_HARDENING_FIVE_OPTION_CLOSURE_2026-05-21.md`
- `docs/work_orders/CVF_WO_TERMINAL_HARDENING_FIVE_OPTION_CLOSURE_2026-05-21.md`
- `docs/reviews/CVF_TERMINAL_HARDENING_FIVE_OPTION_CLOSURE_COMPLETION_2026-05-21.md`
- `CVF_SESSION/ACTIVE_REVIEW_QUEUE.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `AGENT_HANDOFF_V11_2026-05-21.md`

---

## Required First Reads

- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `docs/reviews/CVF_RELEASE_GATE_BUILD_TIMEOUT_MAINTENANCE_COMPLETION_2026-05-21.md`
- `docs/evidence/post-phase-2b-publicization-readiness.md` in public-sync
- `docs/evidence/provider-lanes.md` in public-sync

---

## Pre-Flight Checks

- Confirm provenance working tree changes are limited to evidence and
  continuity.
- Confirm public-sync remote points to
  `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git`.
- Confirm public-sync has no local edits before any claim audit decision.
- Do not print or commit raw API keys.

---

## Execution Plan

1. Clone the public repository into `.cvf/runtime/terminal-hardening/`.
2. Retry with `core.longpaths=true` if Windows path length blocks checkout.
3. Run `npm ci` in the clean public `cvf-web` package.
4. Run `python scripts/run_cvf_static_ci_gate.py --json` in the clean public
   clone.
5. Audit public-sync claims for hosted, production, provider-stability,
   persistence, Maika, and freeze overclaims.
6. File completion and continuity.
7. Run governance checks and commit.

---

## Evidence Requirements

| Claim | Required evidence |
| --- | --- |
| Clean public clone is viable with correct Windows path handling | clean clone result and commit hash |
| Public install works | `npm ci` result in public `cvf-web` |
| Public static gate is healthy | `python scripts/run_cvf_static_ci_gate.py --json` result |
| Secrets/claim boundary is healthy | static gate secret scan and public claim audit |
| Stop boundary is retained | state/handoff updated |

---

## Acceptance Criteria

- [x] Clean-room public proof run.
- [x] Five options classified.
- [x] Completion review filed.
- [x] Continuity updated.
- [x] Governance checks PASS.
- [x] Commit created.

---

## Review Gate

Close only if:

- clean-room public proof passes or records a precise blocker;
- hosted and long-horizon lanes do not receive unsupported readiness claims;
- public claim audit finds no uncorrected overclaim;
- governance checks pass.

---

## Closure Checklist

- [x] Roadmap filed.
- [x] GC-018 filed.
- [x] Work order filed.
- [x] Clean-room proof executed.
- [x] Completion packet filed.
- [x] Queue/state/front door synced; handoff SHA sync follows commit.
- [x] Handoff SHA synced.
- [x] Commit created.

---

## Return-To-Orchestrator Conditions

Return instead of closing only if the public static gate fails in a way that
requires product-source changes or a public overclaim requires public-sync
edits.

---

## Claim Boundary

This work order closes a terminal hardening sweep only. It does not prove
external hosted SaaS readiness, public deployment readiness, broad provider
stability, persistence readiness, Maika readiness, or freeze release.
