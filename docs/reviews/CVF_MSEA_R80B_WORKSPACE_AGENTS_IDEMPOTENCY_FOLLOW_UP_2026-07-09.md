# CVF MSEA-R80B Workspace AGENTS Idempotency Follow-Up

Memory class: governed-review

Status: CLOSED_PASS_BOUNDED

docType: review

Date: 2026-07-09

## Purpose / Decision

R80B closes the bounded product bug found during R80 local dogfood: rerunning
`New-CVF-Governed-Project.ps1` for an already-CVF-generated project can insert
a CVF merge block into `AGENTS.md` instead of refreshing the generated file in
place.

Decision: accept a narrow idempotency repair in `scripts/new-cvf-workspace.ps1`.

## Target / Source

Target surface:

- `scripts/new-cvf-workspace.ps1`

Source trigger: after R80 promoted `Policy_Local`, rerunning the project wrapper
against the same project exposed that `AGENTS.md` handling treated a generated
CVF AGENTS file like custom downstream prose.

## Scope / Methodology

R80B is a script-only follow-up. It does not add a new checker, hook, Fast Lane
rule, provider proof, public claim, or downstream project commit.

Method:

1. Remove any existing CVF merge block before deciding how to rewrite
   `AGENTS.md`.
2. If the remaining file is CVF-generated, refresh it in place with the current
   generated template.
3. If the remaining file is custom downstream content, prepend exactly one CVF
   merge block above the custom content.

## Source Verification

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| Project bootstrap generates downstream `AGENTS.md` from the CVF template. | `scripts/new-cvf-workspace.ps1` | lines 255-265 | `$agentsTemplatePath`; `$downstreamAgentsPath`; `$agentContent` | workspace bootstrap script | ACCEPT |
| Existing downstream `AGENTS.md` is now read before deciding update behavior. | `scripts/new-cvf-workspace.ps1` | lines 267-268 | `$existingContent` | workspace bootstrap script | ACCEPT |
| Old CVF merge blocks are stripped before new merge handling. | `scripts/new-cvf-workspace.ps1` | lines 269-273 | `$withoutCvfMergeBlocks` | workspace bootstrap script | ACCEPT |
| CVF-generated AGENTS files are detected and refreshed in place. | `scripts/new-cvf-workspace.ps1` | lines 274-282 | `$isCvfGeneratedAgents` | workspace bootstrap script | ACCEPT |
| Custom AGENTS files receive one new CVF merge block above the cleaned custom content. | `scripts/new-cvf-workspace.ps1` | lines 283-296 | `$mergeBlock` | workspace bootstrap script | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `Checker Source Read-Ahead Block`; `applicableCheckersRead`; `literalTokensReviewed`; `gateRunPurpose`; `claimBoundary`; `Agent Operation Trace Block`; `Deletion or rename disposition`; `Delta Execution Claim Boundary Control Block`; `Public Export Disposition` |
| gateRunPurpose | confirmation evidence after source read-ahead, not first discovery |
| claimBoundary | R80B checker read-ahead covers this bounded review packet and changed workspace script only |

## Findings / Position

| Finding | Disposition |
|---|---|
| Rerunning project bootstrap against an already-CVF-generated `AGENTS.md` should be idempotent. | Fixed by detecting generated CVF AGENTS content and overwriting it in place. |
| Rerunning bootstrap against custom downstream `AGENTS.md` should not stack repeated CVF merge blocks. | Fixed by stripping old CVF merge blocks before inserting one current block. |

## Finding-To-Governance Learning Disposition

| Field | Value |
|---|---|
| defectClass | RULE_GAP |
| learningLane | DOCUMENTATION_ONLY_LEARNING |
| disposition | STANDARD_UPDATED; N/A_WITH_REASON for runtime/provider/cost lanes because R80B makes no runtime, provider, cost, token, or latency finding |
| next action | Keep this as workspace product hardening. No new ADIF entry is needed because the reusable behavior is captured in the bootstrap script. |

## Risk / Corrective Action

Risk is bounded to downstream workspace bootstrap text generation. The fix does
not touch application source, downstream git state, checker behavior, provider
execution, or public readiness claims.

Corrective action completed:

- Existing CVF merge blocks are removed before AGENTS merge handling.
- CVF-generated AGENTS files are refreshed in place.
- Custom AGENTS files keep custom content with one CVF merge block.

## Verification

| Command | Result |
|---|---|
| PowerShell parser over `scripts/new-cvf-workspace.ps1` | PASS |
| Direct rerun against `Policy_Local` using fixed source script | PASS; `AGENTS.md` refreshed without `CVF_MERGE_BLOCK_START` residue |
| Direct `Policy_Local` project doctor after rerun | PASS WITH NOTE; existing warning remains bootstrap log ignored by `.gitignore` |

## Machine Closure Package

| Closure item | Required artifact/path | Machine-readable evidence | Final status |
|---|---|---|---|
| Work order status | R80 session-sync next move | active state named R80B idempotency follow-up as next allowed move | PASS |
| Completion or reviewer artifact | `docs/reviews/CVF_MSEA_R80B_WORKSPACE_AGENTS_IDEMPOTENCY_FOLLOW_UP_2026-07-09.md` | this packet records bounded closure evidence | PASS |
| Roadmap state | no dedicated roadmap changed | direct R80 follow-up; no roadmap status mutation | N/A with reason: no R80B roadmap file exists |
| Registry JSON | no corpus registry mutation | R80B changes one workspace bootstrap script and this review packet | BLOCKED with reason: not a corpus/search/classification closure and no registry JSON update is authorized |
| Registry Markdown | no corpus registry mutation | R80B changes one workspace bootstrap script and this review packet | BLOCKED with reason: not a corpus/search/classification closure and no registry Markdown update is authorized |
| External evidence digest | local workspace smoke output only | command output captured in this packet | N/A with reason: no durable external artifact is attached |
| System loop interlock | no runtime route or system loop changed | workspace bootstrap script only | N/A with reason: no system-loop interlock surface changed |
| Session continuity | session-sync after material commit | pending separate session-sync commit after R80B material/public-sync | PASS |

## Acceptance Receipt Assertion Matrix

| Query ID | Receipt artifact | JSON path | Required value | Observed value | Status |
|---|---|---|---|---|---|
| R80B-RECEIPT-NA | N/A with reason: R80B creates no receipt artifact | N/A | N/A | N/A | N/A with reason: no receipt-based acceptance claim |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: R80B is implemented in provenance source first. Public-sync export is a
separate next step through the sibling public-sync clone after material commit
and gate pass.

## Epistemic Process Block

EPISTEMIC_PROCESS_NA_WITH_REASON: bounded implementation closure based on local
dogfood observation and command evidence; no competing external assessment is
being compared in this packet.

## Delta Execution Claim Boundary Control Block

| Field | Disposition |
|---|---|
| claimScope | R80B `AGENTS.md` generation idempotency only |
| claimDisposition | N/A with reason: no Delta execution-control claim is made |
| receiptEvidence | N/A with reason: no runtime receipt is created or consumed |
| actionEvidence | N/A with reason: no provider or runtime action is executed |
| invocationBoundary | local PowerShell workspace bootstrap script invoked manually by operator or agent |
| interceptionBoundary | no IDE, shell, git, filesystem, provider, or network interception claim |
| claimLanguage | product hardening for workspace bootstrap idempotency |
| forbiddenExpansion | no governance checker severity change, hook edit, Fast Lane edit, live proof, production claim, or downstream project commit |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Codex reviewer/closer |
| Provider or surface | Codex local workspace |
| Session or invocation | MSEA-R80B workspace AGENTS idempotency follow-up |
| Working directory | `D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF` |
| Command or tool surface | PowerShell, git, apply_patch |
| Target paths | `docs/reviews/CVF_MSEA_R80B_WORKSPACE_AGENTS_IDEMPOTENCY_FOLLOW_UP_2026-07-09.md`; `scripts/new-cvf-workspace.ps1` |
| Allowed scope source | R80 session-sync next allowed move named R80B AGENTS bootstrap idempotency follow-up from stash `r80b-agents-idempotency` |
| Before status evidence | R80 dogfood found rerun could add a CVF merge block to already-generated downstream `AGENTS.md` |
| After status evidence | script detects generated CVF AGENTS files, strips stale CVF merge blocks, and avoids stacked merge blocks |
| Diff evidence | `git diff --name-status`; PowerShell parse; direct `Policy_Local` rerun; direct project doctor |
| Approval boundary | R80B idempotency follow-up only |
| Claim boundary | no downstream project commit, provider/live proof, production claim, checker retirement, or Fast Lane edit |
| Agent type | Codex |
| Invocation ID | r80b-workspace-agents-idempotency-follow-up-2026-07-09 |
| Expected manifest | `docs/reviews/CVF_MSEA_R80B_WORKSPACE_AGENTS_IDEMPOTENCY_FOLLOW_UP_2026-07-09.md`; `scripts/new-cvf-workspace.ps1` |
| Actual changed set | `docs/reviews/CVF_MSEA_R80B_WORKSPACE_AGENTS_IDEMPOTENCY_FOLLOW_UP_2026-07-09.md`; `scripts/new-cvf-workspace.ps1` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename in R80B |

## Claim Boundary

R80B claims only bounded workspace-local AGENTS bootstrap idempotency. It does
not claim that `Policy_Local` was committed or pushed, does not alter
governance checker semantics, and does not make runtime, provider, hosted,
public-readiness, or production-readiness claims.
