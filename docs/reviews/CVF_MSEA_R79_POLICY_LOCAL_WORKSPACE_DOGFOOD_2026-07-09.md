# CVF MSEA-R79 Policy Local Workspace Dogfood

Memory class: governed-review

Status: CLOSED_PASS_BOUNDED_WITH_PRODUCT_FOLLOW_UPS

docType: review

Date: 2026-07-09

Execution base head: 6648a7874

## Purpose

Record a bounded dogfood run using the real local project `Policy_Local` in the
operator workspace.

The goal is to test whether CVF workspace onboarding and `paid-user-safe`
profile selection help an existing, dirty downstream project without mutating
public-sync, changing checkers, or treating the project as production-ready.

## Target / Source

| Item | Source |
| --- | --- |
| Provenance repository | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Local workspace | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace` |
| Dogfood project | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local` |
| Workspace wrapper | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\New-CVF-Governed-Project.ps1` |
| Workspace rule-pack wrapper | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Update-CVF-Workspace-RulePack.ps1` |
| Workspace gate wrapper | `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Run-CVF-NewProject-Enforcement.ps1` |

## Scope / Methodology

Allowed:

- inspect `Policy_Local` before onboarding;
- run the existing workspace bootstrap wrapper against the existing project;
- run the project doctor directly on `Policy_Local`;
- temporarily switch the workspace to the `paid-user-safe` profile;
- verify the paid-user-safe pack has no private/provenance-only token hits;
- restore the actual workspace to `operator-local`;
- record product friction and follow-up recommendations.

Not performed:

- no public-sync mutation;
- no public push;
- no `Policy_Local` commit or push;
- no revert of the existing `Policy_Local` dirty worktree;
- no checker deletion, disablement, hook edit, or Fast Lane standard edit;
- no runtime/provider/live proof;
- no hosted, production, Memory/RAG, retrieval, vectorization, P3 reopen, or
  legal workflow claim.

## Source Verification Block

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- |
| Existing project bootstrap writes `.cvf`, `.vscode`, `AGENTS.md`, `knowledge/`, workspace file, and bootstrap log | `scripts/new-cvf-workspace.ps1` | existing project and generated artifact sections | `ProjectName`; `manifestObj`; `policyObj`; `downstreamAgentsPath` | workspace bootstrap script | ACCEPT |
| Workspace installer creates or preserves the legacy-project baseline file | `scripts/install_cvf_workspace_root_wrappers_public.ps1` | workspace baseline artifact section | `WORKSPACE_PROJECT_ENFORCEMENT_BASELINE.json`; `Set-WorkspaceArtifactIfMissing` | public-safe workspace root installer | ACCEPT |
| Project doctor validates downstream agent-enforcement readiness | `scripts/check_cvf_workspace_agent_enforcement.ps1` | required check list | `.cvf/manifest.json`; `.cvf/policy.json`; `AGENTS.md` | workspace doctor | ACCEPT |
| Rule-pack sync supports paid-user-safe and operator-local profile switching | `scripts/sync_cvf_workspace_rule_pack.ps1` | parameter block and manifest write | `ProfileName`; `AllowProvenanceContinuity`; `ACTIVE_RULE_PACK.json` | rule-pack sync script | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_machine_closure_package.py` |
| literalTokensReviewed | `Purpose`; `Target / Source`; `Scope / Methodology`; `Findings / Position`; `Risk / Corrective Action`; `Decision / Disposition`; `Machine Closure Package`; `Public Export Disposition`; `Agent Operation Trace Block`; `Delta Execution Claim Boundary Control Block`; `Claim Boundary` |
| gateRunPurpose | Confirmation after local dogfood execution. Gates are verification evidence, not first discovery. |
| claimBoundary | Review-shape read-ahead only; dogfood claims are backed by local PowerShell, git, and ripgrep evidence. |

## Findings / Position

The existing `Policy_Local` project can be onboarded without touching the CVF
core or public-sync:

- before onboarding, the project was a separate git repository on
  `master...origin/master [ahead 8]` with many pre-existing modified and
  untracked application files;
- the bootstrap wrapper created only missing CVF project scaffolding:
  `.cvf/`, `.vscode/settings.json`, `AGENTS.md`, `knowledge/README.md`,
  `docs/CVF_BOOTSTRAP_LOG_20260709.md`, and
  `Policy_Local.code-workspace`;
- direct project doctor passed 17 of 17 checks after onboarding;
- switching the workspace to `paid-user-safe` succeeded with 11 copied
  artifacts and 2 workspace-root files;
- while `paid-user-safe` was active, direct project doctor still passed 17 of
  17 checks;
- the sensitive-token scan over the generated `paid-user-safe` pack returned no
  hits;
- the workspace was restored to `operator-local` with 27 artifacts and 2
  workspace-root files, and direct project doctor still passed.

Two product follow-ups surfaced:

- `Policy_Local` remains listed in
  `WORKSPACE_PROJECT_ENFORCEMENT_BASELINE.json`, so the workspace-wide gate
  reports it as `LEGACY_EXEMPT` even after it passes direct doctor. This is
  safe but weak: adopted legacy projects need an explicit, reversible
  "promote from legacy exemption to enforced" flow.
- `Policy_Local/.gitignore` contains `CVF_*.md`, and `git check-ignore -v`
  confirms it hides `docs/CVF_BOOTSTRAP_LOG_20260709.md`. This is a real
  downstream-product friction point: the bootstrap log is doctor-visible but
  not naturally commit-visible in this project.

## Risk / Corrective Action

| Risk | Disposition | Corrective action |
| --- | --- | --- |
| Existing dirty project worktree could be overwritten | AVOIDED | Precheck confirmed target scaffold files were missing before bootstrap; no existing project file was replaced except new `.vscode/settings.json` was created because no settings file existed. |
| Project is doctor-ready but still legacy-exempt in workspace gate | FOLLOW_UP_REQUIRED | Add a bounded adopt-existing-project flow that removes a project from baseline only after direct doctor PASS and operator confirmation. |
| Bootstrap log is ignored by downstream project `.gitignore` | FOLLOW_UP_REQUIRED | Add downstream `.gitignore` guidance or bootstrap warning for required CVF evidence files hidden by project ignore patterns. |
| Workspace could be left on `paid-user-safe` instead of operator-local | REPAIRED | `operator-local` was restored with explicit provenance continuity allowance after proof capture. |
| Dogfood could be misread as app correctness or production readiness | BOUNDED | This artifact proves workspace onboarding and rule-pack usability only; it does not validate `Policy_Local` app behavior. |

## Decision / Disposition

R79 is `CLOSED_PASS_BOUNDED_WITH_PRODUCT_FOLLOW_UPS`.

`Policy_Local` is now locally CVF-onboarded and direct doctor-ready. The
workspace product direction remains valuable, but the next product work should
be targeted: adopt-existing-project promotion and downstream ignore-pattern
handling, not broader governance refactor.

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
| --- | --- | --- | --- |
| Work order status | N/A with reason: direct operator-authorized dogfood, no separate work order opened | this closure status is `CLOSED_PASS_BOUNDED_WITH_PRODUCT_FOLLOW_UPS` | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MSEA_R79_POLICY_LOCAL_WORKSPACE_DOGFOOD_2026-07-09.md` | this artifact records scope, command evidence, and bounded decision | PASS |
| Roadmap state | N/A with reason: no separate R79 roadmap file opened | no roadmap status changed | PASS |
| Registry JSON | N/A with reason: no registry JSON changed by this dogfood run | no registry JSON path in changed set | PASS |
| Registry Markdown | N/A with reason: no registry Markdown changed by this dogfood run | no registry Markdown path in changed set | PASS |
| External evidence digest | N/A with reason: no external evidence artifact consumed; evidence is local command output | no external file path promoted as closure evidence | N/A with reason |
| System loop interlock | N/A with reason: no loop-interlock registry or checker behavior changed | no system loop interlock mutation | N/A with reason |
| Session continuity | `CVF_SESSION_MEMORY.md`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `AGENT_HANDOFF_V39_2026-07-08.md` | session-sync pending after material acceptance | PASS |

## Command Evidence

| Command | Result |
| --- | --- |
| `git status --short --branch` in provenance | PASS: `## main...origin/main` before dogfood material artifact authoring |
| `git -C "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local" status --short --branch` before onboarding | PASS: project was `master...origin/master [ahead 8]` with pre-existing dirty application changes |
| `powershell -ExecutionPolicy Bypass -File "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\.Controlled-Vibe-Framework-CVF\scripts\check_cvf_workspace_agent_enforcement.ps1" -ProjectPath "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local"` before onboarding | EXPECTED_FAIL: 2/8 checks passed; missing `.cvf`, `AGENTS.md`, bootstrap log, and manifest-linked workspace rules |
| `powershell -ExecutionPolicy Bypass -File "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\New-CVF-Governed-Project.ps1" -ProjectName "Policy_Local"` | PASS: created missing CVF scaffold; direct doctor PASS 17/17; workspace gate PASS with `Policy_Local` still `LEGACY_EXEMPT` |
| `powershell -ExecutionPolicy Bypass -File "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Update-CVF-Workspace-RulePack.ps1" -ProfileName "paid-user-safe"` | PASS: applied profile with 11 artifacts and 2 workspace-root files |
| `powershell -ExecutionPolicy Bypass -File "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\.Controlled-Vibe-Framework-CVF\scripts\check_cvf_workspace_agent_enforcement.ps1" -ProjectPath "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local"` while `paid-user-safe` active | PASS: 17/17 checks passed |
| `powershell -ExecutionPolicy Bypass -File "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Run-CVF-NewProject-Enforcement.ps1"` while `paid-user-safe` active | PASS: all new/non-exempt projects passed; `Policy_Local` remained `LEGACY_EXEMPT` |
| `rg -n "CVF_SESSION\|provenance-local\|workspace-provenance-local\|\.private_reference\|Gop y CVF\|private/generated MinerU" "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\CVF_RULE_PACKS\paid-user-safe"` | PASS: no hits |
| `powershell -ExecutionPolicy Bypass -File "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Update-CVF-Workspace-RulePack.ps1" -ProfileName "operator-local" -AllowProvenanceContinuity` | PASS: restored operator-local with 27 artifacts and 2 workspace-root files |
| `git -C "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local" check-ignore -v "docs/CVF_BOOTSTRAP_LOG_20260709.md"` | PASS: confirmed `.gitignore:3:CVF_*.md` ignores the bootstrap log |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
| --- | --- | --- | --- | --- | --- |
| R79-NO-RECEIPT-001 | N/A with reason: this dogfood uses local command evidence, not runtime receipts | N/A with reason | N/A with reason | N/A with reason | PASS |

## Epistemic Process Block

### Expected Result / Prediction

If the workspace product flow is useful beyond a newly created proof project,
then `Policy_Local` should be adoptable as an existing project, pass direct
doctor, tolerate `paid-user-safe` profile switching, and return safely to
`operator-local`.

### Evidence Comparison

Observed evidence mostly matched the prediction:

- direct doctor failed before onboarding for missing CVF scaffold, as expected
  for a legacy project;
- bootstrap created missing scaffold and direct doctor passed 17/17;
- profile switch to `paid-user-safe` succeeded and direct doctor still passed;
- private-token scan over `paid-user-safe` returned no hits;
- operator-local restore succeeded.

The two gaps were practical product gaps rather than governance failures:
legacy baseline exemption was not automatically lifted, and the bootstrap log
was hidden by the downstream project's existing ignore pattern.

### Contradiction Or Gap Disposition

No contradiction was observed in the bounded onboarding claim. The open gaps
need small product follow-ups before this feels smooth for repeated paid-user
workspace adoption.

### Claim Update

Claim updated from "paid-user-safe has a new-project proof" to
"paid-user-safe and the existing bootstrap flow can onboard a real dirty
downstream project, but legacy-exemption promotion and ignore-pattern handling
need product hardening."

## Finding-To-Governance Learning Disposition

| Field | Disposition |
| --- | --- |
| Defect class | N/A_WITH_REASON |
| Learning lane | PRODUCT_WORKSPACE_DOGFOOD |
| Disposition | N/A_WITH_REASON |
| Reason | Findings are product follow-ups for workspace adoption, not recurring governance checker defects. |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance dogfood record for the operator's local
`Policy_Local` project and local workspace. It does not mutate public-sync or
change public-facing CVF source.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
| --- | --- |
| claimScope | R79 local workspace dogfood on `Policy_Local`. |
| claimDisposition | BOUNDED_CLAIM_WITH_EVIDENCE: existing-project onboarding, direct doctor, profile switch, sensitive-token scan, and operator-local restore only. |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed; local command output is the evidence. |
| actionEvidence | ACTION_EVIDENCE_PRESENT: local downstream project CVF scaffold creation and workspace rule-pack profile switching. |
| invocationBoundary | Local provenance workspace, local `CVF-Workspace`, and local `Policy_Local` project only. |
| interceptionBoundary | No IDE, shell, git, filesystem, provider, wrapper, proxy, public repository, checker, hook, or product-package interception claim. |
| claimLanguage | Local workspace adoption usability proof only. |
| forbiddenExpansion | No public-sync mutation, public push, checker retirement, hook edit, Fast Lane standard edit, runtime/provider/live proof, hosted/public/production claim, Memory/RAG, retrieval, vectorization, P3 reopen, or legal workflow. |

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Codex reviewer/closer and local dogfood executor |
| Provider or surface | Codex local workspace |
| Session or invocation | R79 Policy Local workspace dogfood, 2026-07-09 |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, git, rg, apply_patch |
| Target paths | `docs/reviews/CVF_MSEA_R79_POLICY_LOCAL_WORKSPACE_DOGFOOD_2026-07-09.md`; local workspace `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace`; local project `D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local` |
| Allowed scope source | operator selected R79 real-project dogfood and specified `Policy_Local` |
| Before status evidence | provenance was clean/current; `Policy_Local` was a dirty downstream git repository missing CVF scaffold and direct doctor failed 2/8 |
| After status evidence | `Policy_Local` direct doctor PASS 17/17; `paid-user-safe` profile PASS; operator-local restored; product follow-ups recorded |
| Diff evidence | `git status --short --branch`; `git -C "D:\UNG DUNG AI\TOOL AI 2026\CVF-Workspace\Policy_Local" status --short --branch`; command evidence table |
| Approval boundary | local dogfood and provenance evidence record only |
| Claim boundary | local workspace adoption evidence only; no app correctness, production readiness, public release, provider/live behavior, or legal workflow claim |
| Agent type | Codex |
| Invocation ID | r79-policy-local-workspace-dogfood-2026-07-09 |
| Expected manifest | `docs/reviews/CVF_MSEA_R79_POLICY_LOCAL_WORKSPACE_DOGFOOD_2026-07-09.md` |
| Actual changed set | `docs/reviews/CVF_MSEA_R79_POLICY_LOCAL_WORKSPACE_DOGFOOD_2026-07-09.md`; local downstream project scaffold files outside provenance |
| Manifest delta | MATCH_WITH_LOCAL_WORKSPACE_OUTPUT_DISCLOSED |
| Deletion or rename disposition | N/A with reason: no deletion or rename in provenance; local dogfood created scaffold files only |

## Claim Boundary

This artifact records a bounded local workspace dogfood result. It does not
claim `Policy_Local` app correctness, legal adequacy, release readiness, hosted
operation, public CVF readiness, provider behavior, or production governance.

The useful next product move is a bounded adopt-existing-project hardening
tranche: promote a doctor-passing legacy project out of baseline exemption and
detect or advise on `.gitignore` patterns that hide required CVF evidence.
