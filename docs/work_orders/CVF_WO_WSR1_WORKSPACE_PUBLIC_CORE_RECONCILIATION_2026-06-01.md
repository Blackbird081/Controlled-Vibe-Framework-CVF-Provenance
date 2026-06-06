# CVF Work Order - WSR1 Workspace Public-Core Reconciliation

Memory class: FULL_RECORD

Status: IMPLEMENTED_PUBLICATION_READY_PENDING_OPERATOR_REVIEW

docType: work_order

Date: 2026-06-01

## Purpose

Restore a truthful public-core workspace kit and migrate the local hidden core
without merging unrelated histories.

## Authority Chain

| Authority | Path / basis | Disposition |
| --- | --- | --- |
| Operator instruction | 2026-06-01 request to reconcile `CVF-Workspace` | ACCEPT |
| Operator continuation | 2026-06-01 request to finish README workspace onboarding and replace the long guard table with links | ACCEPT |
| WSR1 GC-018 | `docs/baselines/CVF_GC018_WSR1_WORKSPACE_PUBLIC_CORE_RECONCILIATION_2026-06-01.md` | ACCEPT |
| WSR1 roadmap | `docs/roadmaps/CVF_WSR1_WORKSPACE_PUBLIC_CORE_RECONCILIATION_ROADMAP_2026-06-01.md` | ACCEPT |

## Agent Roles

| Role | Responsibility | Boundary |
| --- | --- | --- |
| Orchestrator | patch, migrate, verify, and record result | no public push |
| Reviewer | inspect bounded public-sync diff | publication checkpoint |
| Operator | authorize public commit and push | explicit decision required |

## Scope / Target / Owner Boundary

Allowed scope:

- workspace bootstrap, doctor, bridge, ingest, hooks, foundation bootstrap,
  sample proof, and new public-core reconciler scripts;
- public-sync allowlist and mapped public root `AGENTS.md`;
- workspace isolation, setup, and W114 public evidence docs;
- README workspace onboarding and concise guard registry links;
- guard registry checker/readme-pointer policy update;
- public-surface cleanup required for static public gate readiness;
- local hidden-core backup plus fresh clone;
- local `WORKSPACE_RULES.md`;
- `.cvf/manifest.json` pin updates for bootstrapped downstream projects;
- WSR1 governance artifacts and continuity note.

Forbidden scope:

- downstream application source edits;
- public push without operator checkpoint;
- provenance push;
- destructive deletion of backup;
- live-provider proof;
- MKG6 source ownership.

## Required First Reads

- `docs/reference/CVF_WORKSPACE_RULES.md`
- `governance/toolkit/05_OPERATION/CVF_WORKSPACE_ISOLATION_GUARD.md`
- `scripts/new-cvf-workspace.ps1`
- `scripts/check_cvf_workspace_agent_enforcement.ps1`
- `scripts/cvf-public-sync.ps1`

## Pre-Flight Checks

- inspect provenance and public-sync `git status --short`;
- inspect hidden-core remote, HEAD, cleanliness, and `git merge-base`;
- verify absolute hidden-core and backup paths remain under `CVF-Workspace`.

## Write Ownership

Write only WSR1 workspace-kit scripts, related docs, WSR1 packet files, local
workspace rules, the hidden-core backup/fresh-clone path, and bootstrapped
project manifest pins.

## Source Verification Block

| Claimed item | Verification class | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Public workspace topology exists | EXISTS | `docs/reference/CVF_WORKSPACE_RULES.md` | `Required Layout` | `.Controlled-Vibe-Framework-CVF` | workspace topology | ACCEPT |
| Bootstrap script owns generated downstream artifacts | RUNTIME_BEHAVIOR | `scripts/new-cvf-workspace.ps1` | manifest, policy, AGENTS generation blocks | `cvfCoreCommit` | workspace bootstrap | ACCEPT |
| Old doctor only compared local manifest pin | RUNTIME_BEHAVIOR | `scripts/check_cvf_workspace_agent_enforcement.ps1` | pre-WSR1 check 11 | `cvfCoreCommit` | workspace doctor | ACCEPT |
| Public-sync uses explicit allowlists | RUNTIME_BEHAVIOR | `scripts/cvf-public-sync.ps1` | allowlist blocks | `ALLOWED_TREES` | public exporter | ACCEPT |
| Local hidden core points to public remote | VALUE_SET | `docs/reference/CVF_WORKSPACE_RULES.md` | `Governance Repository` | `origin` | hidden public core | ACCEPT |
| Local hidden core and current public HEAD require safe reconciliation when unrelated | RUNTIME_BEHAVIOR | `docs/reference/CVF_WORKSPACE_RULES.md` | `Update Flow` | `origin/main` | migration decision | ACCEPT |

## Roadmap-To-Work-Order Trace Matrix

| Roadmap requirement | Work order output | Verification |
| --- | --- | --- |
| bounded public kit export | `-WorkspaceKitOnly -NoCommit` plus public README/static cleanup | public-sync `git status --short` |
| public-safe root front door | `CVF_PUBLIC_CORE_AGENTS.md -> AGENTS.md` | public-sync `Test-Path AGENTS.md` |
| stale/diverged detection | doctor freshness checks | old workspace doctor expected FAIL |
| safe migration | backup plus fresh clone reconciler | backup folder plus replacement remote/HEAD |
| sample replay | migrated `qt-saigon-works` manifest and doctor | doctor PASS |

## Execution Plan

1. Patch provenance public-safe workspace kit and docs.
2. Run bounded public-sync copy with `-WorkspaceKitOnly -NoCommit`.
3. Verify public-sync contains only workspace-kit changes.
4. Verify old hidden core is clean and backup paths resolve inside workspace.
5. Run `update_cvf_workspace_public_core.ps1` with reviewed public-sync overlay
   and `-UpdateProjectManifests`.
6. Run doctor for `qt-saigon-works`.
7. Record completion review and leave public publication at operator checkpoint.

## Worker Autonomy / No-Question Rule

Proceed autonomously with non-destructive allowed-scope repair, parser checks,
bounded public-sync copy without commit, backup plus fresh clone migration,
manifest pin refresh, workspace rules refresh, and doctor reruns.

Ask before commit, push, public publication, destructive backup deletion,
live-provider proof, or downstream application source edits.

## Governance Gates Run

- PowerShell parser checks: PASS for exporter, reconciler, doctor, and bootstrap.
- pre-migration doctor: expected FAIL recorded with missing reconciler and
  `DIVERGED_OR_UNRELATED_HISTORY`.
- first migration validation: expected-safe FAIL recorded because public
  `AGENT_HANDOFF.md` was absent; failed replacement clone preserved and old
  clone restored.
- post-fix migration: PASS; old clone backed up; replacement HEAD `eb87479`.
- overlay refresh: PASS with `-AllowPendingCoreBackup`; prior pending hidden
  core preserved under `_cvf-core-backups/.Controlled-Vibe-Framework-CVF-20260601-151708`.
- post-migration doctor: `PASS WITH NOTE (16 passed, 1 warning)`; warning is
  pending public-core overlay publication.
- public-sync bounded diff: workspace kit, README/guard-entry cleanup, and
  public-surface cleanup; no MKG6 runtime file.
- public static gate: PASS.

## Evidence Requirements

- old-doctor negative proof;
- backup inventory;
- replacement remote plus HEAD equality;
- updated sample manifest;
- post-migration doctor;
- bounded public-sync changed-file review.

## Acceptance Criteria

- [x] old hidden core preserved;
- [x] replacement hidden core equals public `origin/main`;
- [x] public-safe workspace kit present;
- [x] sample doctor passes with bounded pending-overlay note;
- [x] public static gate passes;
- [x] public-sync delta contains no MKG6 runtime file.

## Review Gate

Operator reviews the pending public-sync diff before commit or push.

## Closure Checklist

- [x] local migration verified;
- [x] backup retained;
- [x] sample manifest repinned;
- [x] continuity updated;
- [ ] public commit and push authorized.

## Return Conditions

Return to orchestrator if the public diff expands beyond workspace-kit scope,
doctor freshness fails, backup restoration fails, or downstream source would
need edits.

## Operator Checkpoint

Checkpoint: authorize or defer bounded public-sync commit and push.

## Claim Boundary

This work order authorizes local reconciliation and pending public-sync
preparation only. It does not authorize commit or push.
