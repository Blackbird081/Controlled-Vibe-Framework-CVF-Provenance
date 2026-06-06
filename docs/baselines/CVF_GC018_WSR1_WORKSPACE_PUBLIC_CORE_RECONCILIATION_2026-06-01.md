# CVF GC-018 - WSR1 Workspace Public-Core Reconciliation

Memory class: FULL_RECORD

Status: AUTHORIZED_IN_PROGRESS

Date: 2026-06-01

## Purpose

Reconcile the local `CVF-Workspace` topology with the post-split public CVF
repository. Restore a public-safe workspace kit, detect stale or unrelated
hidden-core histories, migrate the local hidden core through backup plus fresh
clone, and verify one existing downstream project.

## Scope / Target / Owner Boundary

Target: public-safe workspace scripts, workspace docs, local hidden core, local
workspace rules, and the `qt-saigon-works` manifest pin.

Boundary: no downstream application source, no MKG6 ownership, no live proof,
no commit, and no push.

## Source / Predecessor Evidence

Predecessors: W112/W113/W114 workspace bootstrap proof, the canonical workspace
topology, the local hidden clone, and current public `origin/main`.

## Trigger Evidence

| Evidence | Observed value | Disposition |
| --- | --- | --- |
| Local hidden core | `dc841d33`, 2026-04-30 | stale |
| Public remote `origin/main` | `eb87479d`, 2026-05-31 | current public anchor |
| History relation | no merge-base | do not merge |
| Old doctor result | `PASS 13/13` | false confidence; freshness not checked |
| Public workspace scripts | bootstrap, doctor, bridge, ingest absent | public contract gap |
| Workspace adoption | 19 app-like folders; 1 fully bootstrapped project | bounded migration target |

## Authorized Scope

- restore public-safe workspace scripts through explicit public-sync allowlist;
- publish a public-safe root `AGENTS.md` from a dedicated template;
- add a backup plus fresh-clone workspace reconciler;
- harden doctor checks for public remote, public kit completeness, freshness,
  and explicit offline override;
- refresh workspace docs and local rules;
- migrate the hidden core and `qt-saigon-works` manifest pin;
- keep public-sync pending and unpushed until operator review.

## Decision / Baseline / Proposed Tranche

Decision: authorize WSR1 as a parallel local reconciliation tranche while
MKG6 remains delegated to its worker.

## Evidence / Verification

- pre-migration doctor must reject the stale hidden core;
- reconciler must preserve the old clone;
- post-migration doctor must pass or pass with an explicit bounded note;
- public-sync delta must contain no MKG6 runtime file.

## Forbidden Scope

- provenance push;
- public push without operator review;
- destructive deletion of the old hidden core;
- merge of unrelated hidden-core and public histories;
- edits to downstream application source;
- live-provider proof;
- MKG6 implementation ownership.

## Claim Boundary

This tranche may prove local workspace reconciliation and a pending public-sync
export packet. It must not claim public publication until the public-sync
changes are committed and pushed from the verified public repository clone.
