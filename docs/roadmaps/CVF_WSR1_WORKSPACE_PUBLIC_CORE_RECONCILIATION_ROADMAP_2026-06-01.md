# CVF WSR1 Workspace Public-Core Reconciliation Roadmap

Memory class: FULL_RECORD

Status: PUBLICATION_READY_PENDING_OPERATOR_COMMIT

Date: 2026-06-01

## Objective

Make `CVF-Workspace` a truthful public-core workspace again after the
public/provenance split.

## Purpose / Why

The prior hidden clone passed the old doctor while remaining stale and
unrelated to the current public history. The public export also omitted the
scripts required by its own workspace docs.

## Scope / Target / Owner Boundary

Owners: public-safe workspace scripts, workspace docs, public-sync bounded
export, local hidden core, local workspace rules, and one bootstrapped sample.

## Scope

- restore the bounded public workspace kit;
- harden doctor freshness checks;
- migrate by backup plus fresh clone;
- replay the doctor against `qt-saigon-works`.

## Non-Goals

- downstream application source changes;
- MKG6 runtime changes;
- live-provider proof;
- public commit or push before operator review.

## Authorization / Decision

WSR1 is authorized by its GC-018 packet as a parallel local reconciliation
tranche.

## Authority Chain

- GC-018:
  `docs/baselines/CVF_GC018_WSR1_WORKSPACE_PUBLIC_CORE_RECONCILIATION_2026-06-01.md`
- Canonical topology:
  `docs/reference/CVF_WORKSPACE_RULES.md`
- Isolation guard:
  `governance/toolkit/05_OPERATION/CVF_WORKSPACE_ISOLATION_GUARD.md`

## Work Tranches

| Tranche | Deliverable | Status |
| --- | --- | --- |
| WSR1-T1 | explicit public-safe script allowlist, mapped public root `AGENTS.md`, bounded `-WorkspaceKitOnly -NoCommit` export | IMPLEMENTED_PENDING_REVIEW |
| WSR1-T2 | doctor hardening for public remote, kit completeness, freshness, offline override | IMPLEMENTED_PENDING_REVIEW |
| WSR1-T3 | backup plus fresh-clone reconciler with optional project manifest pin update | IMPLEMENTED_PENDING_REVIEW |
| WSR1-T4 | local hidden-core migration, workspace rules refresh, `qt-saigon-works` doctor proof | PASS_WITH_NOTE |
| WSR1-T5 | public-sync review, commit, push, fresh public-clone replay | READY_OPERATOR_PUBLICATION_CHECKPOINT |
| WSR1-T6 | README workspace onboarding, concise guard registry links, static public-surface cleanup | PASS |

## Work Plan

Execute T1 through T4 locally, use T6 to finish public README/static-gate
readiness, preserve T5 as the operator publication checkpoint, and keep the
public-sync delta bounded to workspace-kit plus public-readiness cleanup.

## Acceptance Criteria

- old hidden core is preserved under `_cvf-core-backups/`;
- replacement hidden core has public remote `origin`;
- replacement hidden core HEAD equals public `origin/main`;
- public workspace kit exists in the replacement hidden core;
- doctor rejects the pre-migration hidden core;
- doctor passes for `qt-saigon-works` after manifest pin migration;
- public-sync contains the bounded workspace-kit, README/guard-entry, and
  public-surface cleanup delta;
- no MKG6 runtime file is copied into the public-sync delta.

## Verification / Evidence

- PowerShell parser checks;
- pre- and post-migration doctor output;
- backup directory inventory;
- hidden-core `git remote`, local HEAD, and `origin/main`;
- public-sync changed-file review;
- public static CI gate PASS.

## Public Export Disposition

Disposition: `BLOCKED_MISSING_PUBLIC_ARTIFACTS`

Blocker: workspace-kit and public README/guard-surface cleanup files are
pending in the public-sync worktree but have not been committed or pushed.
The public static gate now passes locally.

Next action: review the bounded public-sync diff, then open the operator
publication checkpoint for commit and push.

## Claim / Final / Verification Boundary

Local reconciliation and public-sync static readiness can close before public
publication. Public export remains blocked until public-sync commit and push
evidence exist.
