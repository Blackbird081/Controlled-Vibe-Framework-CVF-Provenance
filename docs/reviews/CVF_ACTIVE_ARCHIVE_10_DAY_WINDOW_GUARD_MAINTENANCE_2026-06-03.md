# CVF Active Archive 10-Day Window Guard Maintenance

Memory class: FULL_RECORD

Status: AUTHORIZED

docType: review

Date: 2026-06-03

## Purpose

Authorize a bounded guard-maintenance change that increases the active archive
age window from 5 days to 10 days. The goal is to reduce premature archive
moves while recent roadmap, review, and work-order links are still actively
used by agents.

## Scope

Allowed changed paths:

- `governance/compat/check_active_archive_hygiene.py`
- `scripts/cvf_active_archive.py`

Forbidden scope: archive execution, file moves, retention-registry rewrites,
reference-link rewriting, public-sync, runtime code, and unrelated governance
checker edits.

## Target / Source

Target: active archive age threshold used by the archive script and hook-safe
hygiene checker.

Source: operator instruction on 2026-06-03 to increase the archive file age
window from 5 days to 10 days because active links are still pointing to files
that were moved into archive too quickly.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: update the active archive hygiene checker
threshold constant from 5 to 10 days and keep the archive execution script in
sync with the same age threshold.

Protected paths:

- `governance/compat/check_active_archive_hygiene.py`

Non-protected companion path:

- `scripts/cvf_active_archive.py`

This authorization does not permit changes to any other guard, hook-chain
phase, runtime source, public-sync surface, or archive baseline.

Operator authorization: operator direction on 2026-06-03 to increase the
active archive age window from 5 days to 10 days because active operational
links still point to recent files.

Rollback boundary: revert the guard-maintenance commit to restore the previous
5-day active archive age window.

## Evidence Trace Block

| Evidence | Value |
| --- | --- |
| Changed threshold | `AGE_THRESHOLD_DAYS: 5 -> 10` |
| Guard path | `governance/compat/check_active_archive_hygiene.py` |
| Script path | `scripts/cvf_active_archive.py` |
| Verification | focused archive tests and active archive hygiene gate |
| Boundary | no archive execution or file movement |

## Findings / Position

Position: APPROVE bounded guard-maintenance change.

Finding: a 5-day age threshold can archive still-active operational documents
too early, causing active links and worker context paths to resolve through
archive folders sooner than intended.

## Risk / Corrective Action

Risk: low. The change delays archive candidacy and does not move files,
rewrite links, or weaken reference-impact screening.

Corrective action: if active docs accumulate too much stale backlog, lower the
threshold through a separate guarded maintenance change or run the archive
script after confirming link impact.

## Final Boundary

This authorization is final for the 10-day active archive window maintenance
change only. It does not authorize archive execution or any CI2/CI3 tranche
work.

## Verification Boundary

Verification is local and structural: focused unit tests plus the active
archive hygiene checker. No live/provider proof is required or claimed.

## Finding-To-Governance Learning Disposition

N/A_WITH_REASON — bounded operator-requested guard-maintenance update with no
provider calls, no runtime behavior change, and no new unresolved finding.

| Finding | Defect class | Learning lane | Disposition | Next action |
| --- | --- | --- | --- | --- |
| 5-day archive age window too aggressive for active operational links | RULE_GAP | GOVERNANCE_CONTROL_PLANE | RULE_UPDATED | Increase active archive age threshold to 10 days in checker and script |

## Claim Boundary

This document authorizes only the active archive age threshold update listed in
Scope. It does not claim archive health beyond the local gate result and does
not modify active-window registry semantics.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance guard-maintenance authorization; no public-facing
artifact is exported.
