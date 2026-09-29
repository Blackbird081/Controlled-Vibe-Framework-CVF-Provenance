# CVF MSEA-R80 Adopt Existing Project Workspace Hardening

Memory class: governed-review

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-07-09

## Purpose / Decision

R80 closes the product follow-up exposed by R79: a real downstream project can
be onboarded successfully but still remain hidden behind the local legacy
baseline, and the project bootstrap log can be hidden by a broad downstream
ignore pattern.

Decision: accept bounded workspace hardening for existing-project adoption.

## Target / Source

Target surfaces:

- `scripts/check_cvf_workspace_new_project_enforcement.ps1`
- `scripts/check_cvf_workspace_agent_enforcement.ps1`
- `scripts/install_cvf_workspace_root_wrappers_public.ps1`
- `scripts/new-cvf-workspace.ps1`
- `scripts/cvf-public-sync.ps1`
- `docs/reference/CVF_WORKSPACE_RULES.md`

Source trigger: R79 Policy Local dogfood found direct project doctor PASS 17/17
while workspace-wide enforcement still reported `LEGACY_EXEMPT`, and
`git check-ignore` showed the project ignored `docs/CVF_BOOTSTRAP_LOG_20260709.md`.

## Scope / Methodology

R80 adds source-backed adopt-existing-project behavior without adding a new
governance checker, hook, Fast Lane rule, provider proof, or public-sync run.

Method:

1. Add the workspace-wide enforcement gate source that already exists in the
   public workspace lane back into provenance source ownership.
2. Add `-PromoteProjectName` to that gate so a named legacy project is only
   removed from `WORKSPACE_PROJECT_ENFORCEMENT_BASELINE.json` after its doctor
   passes.
3. Update generated root wrappers so rerunning `New-CVF-Governed-Project.ps1`
   for an existing project promotes it by default, with `-KeepLegacyExemption`
   as the explicit escape hatch.
4. Add a doctor warning when a downstream project `.gitignore` hides the
   generated bootstrap log.
5. Update canonical workspace rules and generated guides.

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Workspace-wide enforcement baseline file name is already documented as the legacy-project exemption baseline. | `docs/reference/CVF_WORKSPACE_RULES.md` | `Workspace Root` and `Bootstrap Contract` sections | `WORKSPACE_PROJECT_ENFORCEMENT_BASELINE.json` | workspace rules reference | ACCEPT |
| Project doctor checks generated bootstrap logs under project `docs`. | `scripts/check_cvf_workspace_agent_enforcement.ps1` | bootstrap log check block | `CVF_BOOTSTRAP_LOG_*.md` | workspace project doctor | ACCEPT |
| Root installer generates `New-CVF-Governed-Project.ps1` and `Run-CVF-NewProject-Enforcement.ps1`. | `scripts/install_cvf_workspace_root_wrappers_public.ps1` | root wrapper heredocs | `$governedProjectWrapper`; `$workspaceGateWrapper` | public-safe workspace installer | ACCEPT |
| Public sync allowlist owns exported workspace-kit scripts. | `scripts/cvf-public-sync.ps1` | allowlist definitions | `$ALLOWED_SCRIPT_FILES`; `$WORKSPACE_KIT_FILES` | public-sync script | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `Checker Source Read-Ahead Block`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary`; `Agent Operation Trace Block`; `Deletion or rename disposition`; `Delta Execution Claim Boundary Control Block`; `RULE_GAP`; `DOCUMENTATION_ONLY_LEARNING`; `STANDARD_UPDATED`; `Public Export Disposition` |
| gateRunPurpose | confirmation evidence after source read-ahead, not first discovery |
| claimBoundary | R80 checker read-ahead covers this bounded review packet and changed workspace scripts/docs only |

## Findings / Position

| Finding | Disposition |
|---|---|
| Existing project onboarding needs a promotion path after doctor pass; otherwise the workspace gate keeps reporting a healthy project as `LEGACY_EXEMPT`. | Fixed by `-PromoteProjectName` in the workspace-wide gate and default promotion from the generated project wrapper. |
| Downstream ignore patterns can hide generated bootstrap logs from project git status while the doctor still sees the file. | Fixed by a non-blocking doctor warning with exact `git check-ignore -v` evidence. |
| The workspace-wide gate script existed in the public/local workspace lane but was absent from provenance source ownership. | Fixed by adding the script to provenance source and the public-sync allowlist. |

## Finding-To-Governance Learning Disposition

| Field | Value |
|---|---|
| defectClass | RULE_GAP |
| learningLane | DOCUMENTATION_ONLY_LEARNING |
| disposition | STANDARD_UPDATED; N/A_WITH_REASON for runtime/provider/cost lanes because R80 makes no runtime, provider, cost, token, or latency finding |
| next action | Keep this as workspace product hardening. No new ADIF entry is needed because the reusable rule is captured in the installer, canonical workspace rules, and source-owned gate script. |

## Risk / Corrective Action

Risk is bounded to workspace-local product behavior. The promotion path only
removes the named project from the local baseline after the project doctor
returns success. It does not rewrite application files, commit downstream
project changes, change CVF governance checker semantics, or publish public-sync
state.

Corrective action completed:

- Source-owned workspace-wide gate now supports named project promotion.
- Root project wrapper promotes adopted existing projects by default after
  doctor pass.
- Doctor warns when downstream ignore rules hide bootstrap logs.
- Guides and canonical workspace rules document the adoption flow.

## Verification

| Command | Result |
|---|---|
| PowerShell parser over changed scripts | PASS |
| Temp workspace promotion smoke using fake passing doctor | PASS; baseline `legacyProjects` removed `ProjectA` |
| Direct doctor on `Policy_Local` using changed doctor script | PASS WITH NOTE; warning reports `.gitignore:3:CVF_*.md` hiding `docs/CVF_BOOTSTRAP_LOG_20260709.md` |
| Temp installer generation and generated wrapper parse | PASS |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | R80 operator next-move authorization | `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` named R80 as next allowed move before this batch | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MSEA_R80_ADOPT_EXISTING_PROJECT_WORKSPACE_HARDENING_2026-07-09.md` | this packet records bounded closure evidence | PASS |
| Roadmap state | no dedicated roadmap changed | standalone next-move follow-up; no roadmap status mutation | N/A with reason: no R80 roadmap file exists |
| Registry JSON | no corpus registry mutation | R80 changed workspace scripts/docs only | BLOCKED with reason: not a corpus/search/classification closure and no registry JSON update is authorized |
| Registry Markdown | no corpus registry mutation | R80 changed workspace scripts/docs only | BLOCKED with reason: not a corpus/search/classification closure and no registry Markdown update is authorized |
| External evidence digest | local workspace smoke outputs only | command output captured in this packet; no external artifact hash is claimed | N/A with reason: no durable external artifact is attached |
| System loop interlock | no runtime route or system loop changed | `scripts/` and workspace docs only | N/A with reason: no system-loop interlock surface changed |
| Session continuity | session-sync after material commit | pending separate session-sync commit after R80 material commit | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| R80-RECEIPT-NA | N/A with reason: R80 creates no receipt artifact | N/A | N/A | N/A | N/A with reason: no receipt-based acceptance claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R80 is implemented in provenance source first. Public-sync export is a
separate next step requiring the sibling public-sync clone and remote
verification.

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: bounded implementation closure based on
direct source edits and command evidence; no competing external assessment is
being compared in this packet.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | R80 workspace wrapper and doctor hardening only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no runtime receipt is created or consumed |
| actionEvidence | N/A with reason: no provider or runtime action is executed |
| invocationBoundary | local PowerShell scripts invoked manually by operator or agent |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, or network interception claim |
| claimLanguage | product hardening for workspace adoption flow |
| forbiddenExpansion | no governance checker severity change, hook edit, Fast Lane edit, live proof, public-sync export, production claim, or downstream project commit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R80 adopt-existing-project workspace hardening |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, git, apply_patch |
| Target paths | `docs/reference/CVF_WORKSPACE_RULES.md`; `docs/reviews/CVF_MSEA_R80_ADOPT_EXISTING_PROJECT_WORKSPACE_HARDENING_2026-07-09.md`; `scripts/check_cvf_workspace_agent_enforcement.ps1`; `scripts/check_cvf_workspace_new_project_enforcement.ps1`; `scripts/cvf-public-sync.ps1`; `scripts/install_cvf_workspace_root_wrappers_public.ps1`; `scripts/new-cvf-workspace.ps1` |
| Allowed scope source | operator said `next` after R79 closed with R80 as the next allowed move |
| Before status evidence | R79 disclosed `Policy_Local` direct doctor PASS but workspace gate `LEGACY_EXEMPT`, plus ignored bootstrap log evidence |
| After status evidence | source-owned promotion gate, wrapper promotion path, doctor warning, and workspace rules/guides are present in the changed set |
| Diff evidence | `git diff --name-status`; PowerShell parse; temp promotion smoke; direct Policy_Local doctor warning smoke; temp installer generation smoke |
| Approval boundary | R80 workspace product hardening only |
| Claim boundary | no public-sync export, downstream project commit, provider/live proof, production claim, checker retirement, or Fast Lane edit |
| Agent type | Codex |
| Invocation ID | r80-adopt-existing-project-workspace-hardening-2026-07-09 |
| Expected manifest | `docs/reference/CVF_WORKSPACE_RULES.md`; `docs/reviews/CVF_MSEA_R80_ADOPT_EXISTING_PROJECT_WORKSPACE_HARDENING_2026-07-09.md`; `scripts/check_cvf_workspace_agent_enforcement.ps1`; `scripts/check_cvf_workspace_new_project_enforcement.ps1`; `scripts/cvf-public-sync.ps1`; `scripts/install_cvf_workspace_root_wrappers_public.ps1`; `scripts/new-cvf-workspace.ps1` |
| Actual changed set | `docs/reference/CVF_WORKSPACE_RULES.md`; `docs/reviews/CVF_MSEA_R80_ADOPT_EXISTING_PROJECT_WORKSPACE_HARDENING_2026-07-09.md`; `scripts/check_cvf_workspace_agent_enforcement.ps1`; `scripts/check_cvf_workspace_new_project_enforcement.ps1`; `scripts/cvf-public-sync.ps1`; `scripts/install_cvf_workspace_root_wrappers_public.ps1`; `scripts/new-cvf-workspace.ps1` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in R80 |

## Claim Boundary

R80 claims only bounded workspace-local adoption hardening. It does not claim
that `Policy_Local` was committed or pushed, does not export public-sync, does
not alter governance checker semantics, and does not make runtime, provider,
hosted, public-readiness, or production-readiness claims.
