# CVF WSR1 Workspace Public-Core Reconciliation Completion

Memory class: FULL_RECORD

Status: PUBLICATION_READY_PENDING_OPERATOR_COMMIT

Date: 2026-06-01

## Purpose

Record the WSR1 reconciliation result, public README/guard-entry cleanup, and
static public gate readiness without overstating export finality.

## Scope / Target / Owner Boundary

Target owners: workspace kit, workspace docs, local hidden core, local rules,
and `qt-saigon-works/.cvf/manifest.json`.

Boundary: no downstream app source, no MKG6 source, no live proof, no commit,
and no push.

## Target / Source

Source authority: current public remote `origin/main`, canonical workspace
rules, WSR1 scripts, and filesystem-backed workspace evidence.

## Scope / Methodology

Compare old local core with public HEAD, patch the bounded kit, run old-doctor
negative proof, migrate through backup plus fresh clone, overlay pending public
kit files, repin the sample manifest, and rerun doctor.

## Result

Local `CVF-Workspace` reconciliation passed. The public-sync worktree now also
passes the static public gate. Publication remains at a separate commit/push checkpoint
because the public-sync delta is pending and uncommitted.

## Delivered

- added explicit public-safe script allowlist and
  `-WorkspaceKitOnly -NoCommit` public-sync mode;
- added mapped public-safe root `AGENTS.md` and `AGENT_HANDOFF.md`;
- added backup plus fresh-clone reconciler:
  `scripts/update_cvf_workspace_public_core.ps1`;
- hardened workspace doctor to check public origin, kit completeness,
  `origin/main` freshness, pending-overlay warning, and bounded offline
  override;
- refreshed workspace docs, downstream template, and isolation guard;
- replaced the long README guard table with registry links and updated the
  guard registry checker so README stays a concise entry point;
- added README workspace bootstrap instructions for user/dev cloning;
- removed or dispositioned pre-existing public-surface residuals so the public
  static gate passes;
- migrated local hidden core from stale unrelated `dc841d33` history to fresh
  public `eb87479`;
- repinned `qt-saigon-works/.cvf/manifest.json`;
- regenerated local `CVF-Workspace/WORKSPACE_RULES.md`.

## Migration Evidence

| Check | Evidence | Result |
| --- | --- | --- |
| pre-migration doctor | missing reconciler plus `DIVERGED_OR_UNRELATED_HISTORY` | expected FAIL |
| path boundary | hidden core and backup resolved under `CVF-Workspace` | PASS |
| first validation failure | missing public-safe `AGENT_HANDOFF.md` | detected |
| failed clone handling | preserved under `_cvf-core-backups/.Controlled-Vibe-Framework-CVF-failed-20260601-142612` | PASS |
| old hidden core backup | `_cvf-core-backups/.Controlled-Vibe-Framework-CVF-20260601-142929` | PASS |
| overlay refresh backup | `_cvf-core-backups/.Controlled-Vibe-Framework-CVF-20260601-151708` | PASS |
| replacement origin | `https://github.com/Blackbird081/Controlled-Vibe-Framework-CVF.git` | PASS |
| replacement HEAD | `eb87479`; equals `origin/main` | PASS |
| sample manifest pin | `qt-saigon-works` `cvfCoreCommit=eb87479` | PASS |
| post-migration doctor | `PASS WITH NOTE (16 passed, 1 warning)` | PASS |

The remaining doctor warning is intentional: the local hidden core carries the
reviewed public workspace-kit overlay while publication is pending.

## Findings / Position

Position: local reconciliation and public-sync static readiness are accepted
with one bounded workspace-doctor warning. Public publication remains pending
a separate commit/push instruction.

## Risk / Corrective Action

Residual risk: the hidden core and public-sync clone carry a pending reviewed
overlay until publication. Corrective action: commit and push only after the
publication owner accepts the bounded public-sync diff.

## Verification

- PowerShell parser checks: PASS for exporter, reconciler, doctor, and
  bootstrap.
- Public-sync copy:
  `powershell -File scripts/cvf-public-sync.ps1 -WorkspaceKitOnly -NoCommit`
  copied the bounded workspace kit only.
- Public-sync diff review: workspace kit, README guard/workspace onboarding,
  public-surface cleanup, and one public runtime test placeholder comment; no
  MKG6 runtime file copied.
- Public static gate: `python scripts/run_cvf_static_ci_gate.py --json` PASS
  on 2026-06-01: public surface, workflow orchestration, web build,
  TypeScript, secrets scan, docs governance compatibility, and static
  governance/unit tests (`44 passed`) all PASS.
- Hidden-core refresh: reran the reconciler with
  `-AllowPendingCoreBackup`; pending overlay was preserved in backup
  `_cvf-core-backups/.Controlled-Vibe-Framework-CVF-20260601-151708`, README
  was overlaid into the local public core, and the `qt-saigon-works` doctor
  remained `PASS WITH NOTE (16 passed, 1 warning)`.
- Live-provider proof: N/A with reason; this tranche changes workspace
  bootstrap and local enforcement only.

## Static Public Gate Result

The prior public-surface residuals were resolved in the same 2026-06-01
continuation: private review/roadmap/assessment residuals were removed from
public-sync, `spec-export-portable-handoff.ts` was explicitly allowlisted as a
public runtime source, and the OpenAI test key fixture line was marked as a
`test-key` placeholder without changing validator behavior.

`python scripts/run_cvf_static_ci_gate.py --json` now returns PASS.

## Finding-To-Governance Learning Disposition

Defect class: `MACHINE_GATE_GAP`

Learning lane: `GOVERNANCE_CONTROL_PLANE`

Disposition: `MACHINE_CHECK_ADDED`

Next control action: retain public origin, kit-completeness, and freshness
checks in workspace doctor; keep README as a concise registry pointer instead
of a duplicated guard table.

Runtime/provider/cost learning: `N/A_WITH_REASON` - WSR1 changes local
workspace bootstrap and governance-control enforcement only.

| Defect class | Learning lane | Escalation state | Next control action |
| --- | --- | --- | --- |
| doctor false confidence on stale core | governance/control-plane learning | promoted to machine check | require public origin, kit, and freshness checks |
| post-split public contract drift | documentation-only learning plus governance/control-plane learning | promoted to bounded export kit | publish explicit public-safe workspace scripts and front doors |
| unrelated hidden-core history | governance/control-plane learning | promoted to migration rule | backup plus fresh clone; never merge unrelated histories |
| first migration left replacement clone after validation failure | runtime-behavior learning | repaired in reconciler | preserve failed clone and restore original backup automatically |
| README guard table bloat | documentation-only learning plus governance/control-plane learning | promoted to checker rule | README links to registry; filename completeness remains in `docs/CVF_CORE_KNOWLEDGE_BASE.md` |

## Public Export Disposition

Disposition: `BLOCKED_MISSING_PUBLIC_ARTIFACTS`

Blocker: public remote has not yet received the pending public-sync diff.
Local public-sync artifacts exist and the static public gate passes, but there
is no public commit or push evidence yet.

Next action: inspect the bounded public-sync diff, then run a separate
public-sync commit and push only after explicit instruction.

## Claim / Final / Verification Boundary

This completion proves local workspace reconciliation, public-sync static gate
readiness, and pending public export preparation. It does not claim public
publication, live-provider behavior, hosted readiness, or production readiness.
