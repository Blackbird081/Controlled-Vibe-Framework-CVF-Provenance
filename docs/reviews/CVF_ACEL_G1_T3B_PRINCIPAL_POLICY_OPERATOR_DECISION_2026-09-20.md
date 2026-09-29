# CVF ACEL G1 T3B Principal And Policy Operator Decision

Memory class: governed-local-decision

docType: review

Status: OPERATOR_APPROVED_ACCOUNT_CREATION_PENDING

Date: 2026-09-20

Decision base HEAD: `617357bf1`

Decision owner: operator for principal and policy; Local orchestrator/reviewer
for exact recording, launcher implementation and later verification.

successorTrancheOpened: NO

## Purpose

Record the operator's approval of both T3B readiness recommendations and add
two password-free launchers so repeated alternate-principal PowerShell startup
does not require memorizing commands.

## Target / Source

| Source | Authority |
|---|---|
| operator instruction, 2026-09-20 | approved both the dedicated approver principal and proposed v1 policy |
| `docs/audits/CVF_ACEL_G1_T3B_GROUP2_SOURCE_READINESS_ROUTE_2026-09-20.md` | exact account recommendation, compact JCS payload and route boundary |
| `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Group 2 author/approver separation, paths, hashes and event order |

## Scope / Methodology

Local recorded the two approvals, created two simple Windows command launchers,
and ran their `--check` modes. The launchers store no password, token, key or
credential. They call Windows `runas`, which requests the selected account's
password through the operating-system prompt, open PowerShell 7 at the current
repository root, and add the existing NVM4W Node directory when present.

No account was created because the Local process is not elevated. No `runas`
authentication, alternate-user execution, Group 2 source creation, approval
event or activation occurred.

## Operator Decision

Principal decision:
`APPROVE_DEDICATED_LOCAL_STANDARD_ACCOUNT_CVF_G1_ACTIVATION_APPROVER`.

Approved account name after Local platform-compatibility correction:
`cvf-g1-approver`.

The earlier proposed literal `cvf-g1-activation-approver` was 26 characters
and therefore not representable as a Windows local SAM account name. Local
corrected this orchestrator-owned defect before provisioning; the approved
dedicated-role semantics and separation boundary are unchanged.

Policy decision: `APPROVE_RECOMMENDED_T3B_V1_POLICY_BYTES`.

The approved decoded content is exact UTF-8 compact JCS, no BOM and no trailing
newline:

```json
{"admissionRequiredLookupResult":"IDENTITY_CONFIRMED","authorityId":"ACEL_G1_DECISION_OWNER","authoritySpecSchema":"cvf.acel.g1.verificationAuthoritySpec@1","freshnessThresholdSeconds":86400,"issuerVerificationRequirement":"VERIFIED_BY_LIVE_REGISTRY_LOOKUP","receiptDomain":"cvf.verifierReceipt","receiptProfileVersion":"v1"}
```

The value `freshnessThresholdSeconds=86400` is now operator-approved policy for
the first specification version. This approval does not itself encode the
bytes into `SPEC_v1.json` or authorize an activation event.

## Launcher Artifacts

| Path | Principal | Behavior | Check result |
|---|---|---|---|
| `scripts/run_as_cvf_g1_party_a.cmd` | `LAM-RUBY\cvf-g1-party-a` | password-free launcher configuration; Windows prompts for password | READY, exit 0 |
| `scripts/run_as_cvf_g1_activation_approver.cmd` | `LAM-RUBY\cvf-g1-approver` | same launcher behavior; stops if account is absent | ACCOUNT_NOT_FOUND, exit 3, expected until provisioning |

Both scripts resolve the repository from their own location rather than
hard-code the workspace path. `--check` verifies PowerShell 7 and account
existence without opening `runas` or requesting a password. The approver
launcher additionally fails closed unless the account is enabled, carries the
Windows password-required flag, and is outside the local Administrators group.

## Findings / Position

The policy checkpoint is closed. The principal-selection checkpoint is closed
as a decision but not as operational evidence: account creation, SID capture,
enabled/password-required/non-admin checks and separation evidence remain
required before a T3B worker packet can rely on the principal.

The two launchers remove repeated command-recall friction without weakening
credential handling. Embedding a password, using `/savecred`, or automatically
approving UAC would violate the selected boundary and is intentionally absent.

## Decision / Disposition

Decision: `ACCEPT_OPERATOR_T3B_PRINCIPAL_AND_POLICY_SELECTIONS`.

Policy content: `APPROVED_EXACT_BYTES`.

Principal identity: `APPROVED_NAME_PROVISIONING_PENDING`.

T3B work order: `NOT_YET_DISPATCHABLE`; Local must first verify the created
account's exact name/SID, enabled state, password requirement and non-admin
membership. No source or activation authority opens automatically.

## Risk / Corrective Action

| Risk | Control |
|---|---|
| password is embedded for convenience | launchers use `runas` prompt only; no `/savecred` |
| launcher silently targets a missing/wrong account | `net user` preflight and explicit account constant |
| approver becomes Administrator | create as a standard local user and verify group membership before dispatch |
| account has a password but Windows leaves `PasswordRequired=False` | require explicit `net user cvf-g1-approver /passwordreq:yes` and make the launcher fail closed |
| account name is mistaken for operational proof | require Local SID and policy checks after provisioning |
| proposed name exceeds the Windows local SAM-name limit | use exact 15-character `cvf-g1-approver`; validate platform representability before operator action |
| approved policy is changed during implementation | bind exact bytes and independently recompute hashes |

## Checker Source Read-Ahead Block

| Field | Evidence |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_public_export_disposition.py` |
| literalTokensReviewed | `successorTrancheOpened: NO`; `## Findings / Position`; `## Finding-To-Governance Learning Disposition`; `## Agent Operation Trace Block`; `DEFERRED_PRIVATE_ONLY`; `## Claim Boundary` |
| gateRunPurpose | confirmation after exact decision and launcher checks |
| claimBoundary | approval record and launch convenience only; no account/source/activation claim |

## Epistemic Process Block

Epistemic Process Applicability: HIGH_EVIDENCE

Expected Result / Prediction: Party A launcher would be ready and the new
approver launcher would fail closed until its approved account exists.

Evidence Comparison: exact match; exit codes were 0 and 3 respectively.

Contradiction Or Gap Disposition: account provisioning requires an elevated
operator action; the first proposed name also exceeded Windows' local account
name limit, so Local corrected it before provisioning and will verify afterward.

Claim Update: policy bytes and principal name are approved; principal evidence,
tooling dispatch, Group 2 creation and activation remain unopened.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Disposition | Next control action | Batch status |
|---|---|---|---|---|---|
| repeated manual `runas` command recall is error-prone | OPERATOR_SCOPE_CLARITY_GAP | GOVERNANCE_CONTROL_PLANE | RULE_EXISTS | use password-free named launcher scripts while preserving OS password prompts | HANDLED_IN_THIS_BATCH |
| orchestrator proposed a non-representable Windows account name | ORCHESTRATOR_PACKET_GAP | GOVERNANCE_CONTROL_PLANE | CORRECTED_BEFORE_PROVISIONING | validate platform identity constraints before asking the operator to create a principal | HANDLED_IN_REVIEWER_CORRECTION |
| `New-LocalUser -Password` did not guarantee the separate Windows password-required account flag | OPERATIONAL_PREFLIGHT_GAP | GOVERNANCE_CONTROL_PLANE | CORRECTED_BEFORE_DISPATCH | enforce enabled/password-required/non-admin posture in the approver launcher before `runas` | HANDLED_IN_REVIEWER_CORRECTION |

Runtime/provider/cost learning: `N/A_WITH_REASON` because no provider, runtime
service, token, latency or cost behavior was exercised.

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace and read-only Windows identity checks |
| Session or invocation | `acel-g1-t3b-principal-policy-decision-launchers-20260920` |
| Working directory | repository root |
| Command or tool surface | apply_patch, cmd launcher check, whoami/admin-role check, governance gates |
| Target paths | this decision and two launcher scripts |
| Allowed scope source | operator approved both T3B recommendations and requested two batch launchers |
| Before status evidence | selections pending; no approver launcher; Local process non-admin |
| After status evidence | exact policy/principal selections recorded; two launchers present; account still absent |
| Diff evidence | exact three-path intended material manifest plus unchanged parked paths |
| Approval boundary | decision recording and password-free launcher creation only |
| Claim boundary | no account creation, alternate-user execution, source, approval event or activation |
| Agent type | Local reviewer/implementer for bounded convenience files |
| Invocation ID | `acel-g1-t3b-operator-decision-launchers-20260920` |
| Expected manifest | this decision; `scripts/run_as_cvf_g1_party_a.cmd`; `scripts/run_as_cvf_g1_activation_approver.cmd` |
| Actual changed set | exact expected three paths; thirteen parked paths unchanged |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: no deletion or rename |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: local account names and private-workspace convenience tooling remain
private provenance; no public artifact or public-sync authority exists.

## Claim Boundary

This decision proves the operator selected an account name and exact policy
bytes and that the launchers fail closed in their observed states. It does not
prove account provisioning, credentials, alternate-user execution, Group 2
source creation, approval, activation, consumer binding, candidate admission,
provider/live behavior, runtime readiness, public export or deployment.
