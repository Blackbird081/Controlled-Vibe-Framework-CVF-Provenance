# CVF External Source Mirror Index

Memory class: PRIVATE_REFERENCE_CONTROL_PLANE

Status: ACTIVE_INDEX

docType: private_reference_index

Date: 2026-06-29

INDEX type: private external source mirror registry

Source authority: pinned upstream repository clone or upstream URL/commit record; external-agent packs are secondary artifacts only

Human-reviewable: yes

Claim boundary: local reference index only; no cloned source payload is tracked, executed, installed, activated, published, or promoted by this index

Public Export Disposition: DEFERRED_PRIVATE_ONLY

## Purpose

Track which upstream repositories have or need local source mirrors for
high-value external absorption.

This index links a source mirror to any derived external-agent pack so future
work can distinguish upstream source facts from secondary interpretation.

## Mirror Ledger

| Mirror ID | Upstream repository | Local mirror path | Pinned commit | Mirror status | Verified date | Tracked file count | Related external-agent pack or folder | Current CVF absorption surface | Source authority disposition | Runtime boundary |
|---|---|---|---|---|---|---:|---|---|---|---|
| `addyosmani__agent-skills` | `https://github.com/addyosmani/agent-skills.git` | `.private_reference/source_mirrors/addyosmani__agent-skills/` | `aba7c4e9695c363e65cb59effe926c7f1d1abe3d` | `CLONED_PINNED` | 2026-06-29 | 96 | `.private_reference/legacy/CVF 28.06/CVF_Agent_Skills_Governance_Absorption_Pack/` | AGSK-R2 package backfill candidate; existing ASSF candidate registry entries under `docs/reference/agent_system_skills/registry/entries/` | upstream source mirror must be preferred for skill/package facts; absorption pack is secondary comparison material | no install, hook execution, runtime activation, package activation, provider/live proof, public-sync, or direct import |

## Update Rule

When a source mirror is cloned or refreshed:

1. Record the exact commit SHA in `Pinned commit`.
2. Change `Mirror status` to `CLONED_PINNED`.
3. Record or update the linked absorption lane.
4. Keep the cloned repository payload ignored by git.
5. Do not claim absorption completion from clone presence alone.

## Selection Rule

Before a full-value external repo absorption starts, the reviewer must check
this index:

- if a high-value upstream repo is available but only a derived external-agent
  pack exists locally, create or request a source mirror before closeout;
- if a mirror exists, use it as source-verification authority for upstream
  facts;
- if cloning is blocked, record `BLOCKED_SOURCE_MIRROR_WITH_REASON` in the
  absorption artifact and keep the derived pack as secondary evidence only.

## Claim Boundary

This index records reference-source availability. It does not authorize
runtime, package activation, checker wiring, dependency installation, hook
execution, provider calls, public export, or production readiness.
