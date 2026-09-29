# CVF WP-ARCH-003 RABA F01-F02 Root Evidence Reassessment

Memory class: governed-assessment

Status: COMPLETE_PENDING_REVIEW

docType: assessment

Date: 2026-09-08

Batch ID: WP-ARCH-003-RABA-F01-F02-ROOT-EVIDENCE-REASSESSMENT

Responds to work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_WP_ARCH_003_RABA_F01_F02_ROOT_EVIDENCE_REASSESSMENT_2026-09-08.md`

providerExecutionAuthority: FORBIDDEN

executionBaseHead: `e69bcc5b11273639a619976a190f383496825ee5`

## Purpose

Resolve reviewer findings `WP-ARCH-003-RABA-T0-R1-01` and
`WP-ARCH-003-RABA-T0-R1-02`. Classify the four omitted current candidate
families (Web approval, provider execution grant, delegation, mutating-profile
approval) against RABA-Q01 through RABA-Q06, then restate the six-question root
decision from complete current-source evidence. This assessment produces an
evidence and owner decision only; it designs and implements nothing.

## Authority Boundary

Governed by the RABA-F01-F02 work order, its paired GC-018 baseline, and the
RABA-F01-F02 roadmap. Provider-local files are `NOT_CVF_SOURCE` and are never
cited here as authority. The RABA-T0 completion review is accepted only for its
two finding statements and terminal park boundary; the rejected RABA-T0 and AR1
worker artifacts are historical evidence and are not reused as current
authority. Every claim below was re-verified against repository source read at
`executionBaseHead`.

## Source And Predecessor Evidence

Every source file named in the work order Source Verification Block was read at
`executionBaseHead`, including the four candidate families the RABA-T0 return
omitted. Non-test call sites were located with bounded `rg` queries scoped to
`EXTENSIONS`. The predecessor completion review
(`docs/reviews/CVF_WP_ARCH_003_RABA_T0_ROOT_AUTHORITY_SOURCE_VERIFICATION_COMPLETION_2026-09-08.md`)
was reconfirmed byte-identical at SHA-256
`dc413723dd6a2b06f77e714577b1be1b412b5f3561fee7ea6c6a5814f421ed9f`, matching the
value the work order cites. The RABA-F01-F02 roadmap was read at SHA-256
`efeeb25457c6276d60935212e15601ffac42efcd578388951acf09006f314b94`.

## Target / Source

| Artifact | Role |
|---|---|
| `docs/work_orders/CVF_AGENT_WORK_ORDER_WP_ARCH_003_RABA_F01_F02_ROOT_EVIDENCE_REASSESSMENT_2026-09-08.md` | governing work order |
| `docs/baselines/CVF_GC018_WP_ARCH_003_RABA_F01_F02_ROOT_EVIDENCE_REASSESSMENT_2026-09-08.md` | paired dispatch baseline |
| `docs/roadmaps/CVF_WP_ARCH_003_RABA_F01_F02_ROOT_EVIDENCE_REASSESSMENT_ROADMAP_2026-09-08.md` | fresh bounded parent, two-finding contract |
| `docs/reviews/CVF_WP_ARCH_003_RABA_T0_ROOT_AUTHORITY_SOURCE_VERIFICATION_COMPLETION_2026-09-08.md` | two-finding predecessor authority |
| named `EXTENSIONS/` MAO, Control Plane, Guard Contract, Execution Plane, MCP and Web source files | current-source evidence base |

## Scope / Methodology

Bounded named-source read plus targeted non-test `rg` call-site search across
`EXTENSIONS`. No repository-wide or corpus-completeness claim is made. No
source, test, runtime, provider, live, public-sync or deploy action was taken.

## Four-Family Reconciliation Table

This table discharges `WP-ARCH-003-RABA-T0-R1-01`. Every family the RABA-T0
return omitted is classified here with producer, verifier, current non-test
consumer, broken edges and one evidence disposition.

| Family | Producer (CURRENT) | Verifier (CURRENT) | Non-test consumer (CURRENT) | Broken edges against the RABA chain | Disposition |
|---|---|---|---|---|---|
| Web approval | `PATCH` in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/[id]/route.ts` lines 57-118; issuer identity from `verifySessionCookie` (`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/middleware-auth.ts` line 118) gated by `canAccessAdmin` (`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/enterprise-access.ts` line 11); `reviewedBy` set from the verified session at line 93 | approval-resume block in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` lines 185-269: existence, `requestHash` presence, actor-binding presence, `approvalRecordMatchesActor`, hash equality, `expiresAt`, `status === 'approved'` | same `execute` route lines 498-514: on `NEEDS_APPROVAL` with an approved record it emits `APPROVAL_CONSUMED` and calls `getApprovalStore().delete(...)`, then execution proceeds past the approval gate | does not bind MAO parent authority, `taskGraphId`, `taskId`, per-task `fileScope` or a numeric budget into the approved receipt; approval scope is template/intent/provider/model, not authority-delta or file scope | PARTIAL_TRUSTED_CHAIN_WRONG_SUBJECT |
| provider execution grant | none authenticated; the grant object is `JSON.parse`-d from caller-controlled environment `CVF_PROVIDER_EXECUTION_GRANT_JSON` by `parseProviderExecutionGrant` (`EXTENSIONS/CVF_MODEL_GATEWAY/scripts/run-p4b-b-live-proof.ts` lines 132-137, 428-430; same pattern at `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/scripts/run-mao-live-provider-value-pilot.ts` lines 126-131, 148) | `evaluateProviderExecutionAuthority` (`EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` lines 57-91): authority, `authorizedBy === "ORCHESTRATOR"`, grant-id match, subject match, delegation match, allowed-provider, call budget, expiry | `EXTENSIONS/CVF_MODEL_GATEWAY/src/p4b-b-live-proof-harness.ts` line 168; `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/live.provider.value.pilot.ts` line 245 | the `authorizedBy: "ORCHESTRATOR"` literal is a field inside the same caller-supplied JSON; comparing it to a constant authenticates nothing. No signature, session, or server-side issuer record exists. Subject/delegation ids are likewise env-supplied (`CVF_AGENT_ID`, `CVF_DELEGATION_ID`) | REJECT_SELF_ATTESTED_ISSUER |
| delegation | no source-proven trusted producer: no non-test code constructs a `DelegationContract`; only the interface, its own validators and a barrel re-export exist (`EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` line 16; `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/control.plane.coordination.barrel.ts` lines 151-155) | `validateWriteScope` (`delegation.contract.ts` lines 155-193) and `validateDelegationContract` (lines 229-310) | none outside the defining module: `validateWriteScope` is called only by `validateClosureReport` in the same file (line 217) and re-exported by the barrel (line 152) | carries exactly the fields RABA-Q04 wants (`parentTaskId`, `workerAgentId`, `ownership.ownedFiles`, `ownedModules`, `forbiddenPaths`) but has no trusted producer and no runtime consumer; the producer edge and the consumer edge are both absent | REJECT_NO_PRODUCER_NO_CONSUMER |
| mutating-profile approval | `buildMutatingProfileApprovalRecord` (`EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/mutating-profile-approval.ts` lines 58-79); `approvedBy` is a plain input string on the record (line 24) | `JsonMutatingProfileApprovalPolicy.evaluate` (lines 88-136): fixed target, fixed profile, `actionHash` match, optional `bindingHash` match, timestamp validity, future-dated rejection, expiry | real: `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts` line 85 constructs the policy and passes it to `launchGovernedCommand`, evaluated at `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` line 460 | `approvedBy` is never authenticated; the record is read from a local JSON store with no issuer proof. The launcher's own comment (lines 337-346) states it is a composition root and not an authority source, and the canonical `build_authority` guard denies the mutating write at the `preflightGovernanceAction` step (lines 347-369) before the approval policy at line 460 is reached | REJECT_UNAUTHENTICATED_APPROVER_AND_EARLIER_DENIAL |

Reconciliation outcome: the RABA-T0 statements `NO_ISSUER_FOUND`,
`NO_PRINCIPAL_FIELD_EXISTS` and `NONE_CURRENT` were broader than the evidence
supported. One current family (Web approval) does contain an authenticated
issuer and a complete verifier-to-consumer chain. It nonetheless fails the RABA
root because its approved subject is an AI execution request, not an authority
delta bound to MAO parent authority, task graph, task and file scope.

## Exact Source Ledger

| Q# | Path | Symbol | Producer | Verifier | Consumer | Disposition |
|---|---|---|---|---|---|---|
| RABA-Q01 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/[id]/route.ts` | `PATCH` (line 57) | authenticated admin session via `verifySessionCookie` plus `canAccessAdmin` (lines 61-63); `reviewedBy` from session (line 93) | server-side role check, not caller input | `store.set(id, updatedRecord)` (line 101) plus `APPROVAL_DECIDED` audit event (lines 103-116) | AUTHENTICATED_ISSUER_EXISTS_WRONG_SUBJECT |
| RABA-Q01 | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` | `ProviderExecutionGrant.authorizedBy` (line 8) | caller-controlled env JSON | literal comparison only (line 64) | live-proof harnesses only | REJECT_NOT_AN_ISSUER |
| RABA-Q01 | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | `MaoApprovalCheckpoint` (line 25) | caller-supplied `approvalCheckpoints` (line 46) | folded into `computeAuthorityHash` (line 134) | `compileTaskGraph` (line 343) | REJECT_NO_ISSUER_INTEGRITY_ONLY |
| RABA-Q02 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.ts` | `buildApprovalRequestSnapshot` (line 201); `computeApprovalRequestHash` (line 232) | server-side snapshot over template, intent, provider, model, inputs, phase, risk and actor fields | SHA-256 over the projected snapshot (lines 232-237) | `execute` route line 183 | BOUND_DELTA_PRESENT_BUT_NOT_AUTHORITY_SCOPED |
| RABA-Q02 | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` | `ProviderExecutionGrant` (lines 5-14) | env JSON | `evaluateProviderExecutionAuthority` (line 57) | live-proof harnesses | PARTIAL_BUDGET_AND_EXPIRY_NO_PARENT_AUTHORITY |
| RABA-Q03 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | approval-resume block (lines 185-269) | n/a | actor match (line 219), hash match (line 230), expiry (line 241), status (line 256), missing-binding rejection (lines 197, 208) | single-use `delete` (line 514) | COMPLETE_VERIFIER_FOR_ITS_OWN_SUBJECT |
| RABA-Q03 | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/mutating-profile-approval.ts` | `buildMutatingProfileApprovalRecord` (line 58) | n/a | `evaluate` (line 88): target, profile, action hash, binding hash, timestamp, future, expiry | `governed-command-launcher.ts` line 460 | VERIFIER_PRESENT_ISSUER_UNAUTHENTICATED |
| RABA-Q04 | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` | `DelegationContract` (line 16) - fields `parentTaskId`, `workerAgentId`, `ownership.ownedFiles`, `ownedModules`, `forbiddenPaths` | none: no non-test constructor exists | `validateWriteScope` (line 155) | `validateClosureReport` (line 217) same module only | FIELDS_EXIST_NO_TRUSTED_PRODUCER |
| RABA-Q04 | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/role.resolver.contract.ts` | `MaoRoleResolutionReceipt` (line 55) | `resolveRole` (line 191), pure over caller-supplied graph | none for principal identity | `orchestration.composition.contract.ts` line 71 | NO_PRINCIPAL_FIELD_ON_RECEIPT |
| RABA-Q04 | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` | `GuardRequestContext.agentId` (line 98) | caller/tool-argument input | presence-only check in `audit-trail.guard.ts` (lines 31-32) | guard pipeline | SELF_ATTESTED_PRESENCE_ONLY |
| RABA-Q05 | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | approval consumption (lines 498-514) | verifier block above | execution proceeds past the `NEEDS_APPROVAL` gate to the guard composition at line 578 | REAL_NON_TEST_CONSUMER_EXISTS |
| RABA-Q05 | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` | `buildContext` (line 71), `cvf_evaluate_full` (line 398) | `agentId` accepted as `z.string().optional()` (line 406), forwarded unverified (line 417) | `engine.evaluate(context)` (line 423) via `createGuardEngine` (`EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` line 394) | REAL_CONSUMER_UNVERIFIED_INPUT |
| RABA-Q05 | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts` | `JsonMutatingProfileApprovalPolicy` construction (line 85) | policy evaluate (launcher line 460) | `launchGovernedCommand` (line 72) then `dependencies.runner.run` (launcher line 484) | REAL_CONSUMER_BEHIND_EARLIER_DENIAL |
| RABA-Q06 | `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts` | `bindCommittedCapabilityOwnerGrant` (line 121) reads committed repository HEAD, not caller input | `reconcileGrantWithObservation` (line 195): field match, trace/receipt linkage, validity window | `evaluateCadpCapabilityConsumer` (`EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/cadp.capability.consumer.contract.ts` line 194) | TRUSTED_PATTERN_NARROW_SCOPE |

Negative finding: `evaluateAuthorityExpansionApproval`, `verifiedFileScope` and
`PrincipalScopeIdentityGuard` return zero matches under `EXTENSIONS` at
`executionBaseHead`. They exist only as prose in rejected predecessor
documents and are labeled `PROPOSED`, never `CURRENT`.

## Root Authority Candidate Matrix

| Candidate | Approver identity | Envelope integrity | Circular or requester-issued? | Disposition |
|---|---|---|---|---|
| Web approval `PATCH` decision | REAL: Auth.js JWT-decoded session (`verifySessionCookie`, `middleware-auth.ts` line 118) plus server-side `canAccessAdmin` role gate; the request body cannot set `reviewedBy` | `computeApprovalRequestHash` binds the request snapshot; `approvalRecordMatchesActor` binds the consumer to the submitter | PARTIAL: the approver is authenticated, but `approvalRecordMatchesScope` does not require `reviewedBy` to differ from `submittedByActorId`; an admin requester may approve a same-scope own request | ACCEPT_AS_AUTHENTICATED_APPROVAL_PATH_NO_SEPARATION_OF_DUTY |
| `ProviderExecutionGrant.authorizedBy` | NONE: a string literal inside caller-supplied `CVF_PROVIDER_EXECUTION_GRANT_JSON` | grant-id, subject, delegation, provider, budget and expiry checks | YES: the same environment that requests provider execution supplies the grant claiming to authorize it | REJECT_AS_APPROVAL_ISSUER |
| `MutatingProfileApprovalRecord.approvedBy` | NONE: plain input string on the record builder (line 24) | `actionHash`, optional `bindingHash`, timestamp and expiry checks | YES: whoever writes the local JSON store also names the approver | REJECT_AS_APPROVAL_ISSUER |
| `MaoApprovalCheckpoint` list plus `authorityHash` | NONE: category enum populated by the envelope constructor | `verifyAuthorityEnvelope` detects post-hoc content change only | YES: the same caller supplies the checkpoint list and the content it hashes | REJECT_AS_APPROVAL_ISSUER |
| `MaoRoleResolutionReceipt.decision` | NONE: pure function of the caller-supplied graph | structural admission checks only | YES: admission is computed from data the requester already supplied | REJECT_AS_APPROVAL_ISSUER |
| `bindCommittedCapabilityOwnerGrant` committed grant | REAL: values read from git-committed state the live requester cannot rewrite in the same call | exact-match reconciliation plus validity window and invocation accounting | NO | ACCEPT_AS_NARROW_PRECEDENT_CADP_ONLY |

Corrected RABA-Q01 position: an authenticated approval issuer does exist in
current source (the Web admin approval route), and the RABA-T0 claim that none
exists is withdrawn. It is not, however, an issuer for authority expansion: it
approves a bounded AI execution request, holds no relation to MAO parent
authority, and never states that the approver's authority is strictly above a
requested delta.

## Principal Scope Binding Matrix

| Field | Current producer | Trusted or self-attested | Evidence |
|---|---|---|---|
| principal ID | `ApprovalActorBinding.actorId` from the verified session (`approval-binding.ts` lines 175-186) | TRUSTED for the Web approval subject: derived from the session cookie, not the request body | `approval-binding.ts` line 181; `middleware-auth.ts` lines 101-109 |
| principal ID (MCP/guard path) | `GuardRequestContext.agentId` | SELF_ATTESTED: optional caller field forwarded unchanged | `EXTENSIONS/CVF_GUARD_CONTRACT/src/types.ts` line 98; `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/index.ts` lines 76, 87, 406, 417 |
| principal ID (delegation path) | `DelegationContract.workerAgentId` | NO_PRODUCER: no non-test code constructs the contract | `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` line 18 |
| task graph ID | `MaoTaskGraph.taskGraphId` | DERIVED_NOT_VERIFIED: deterministic hash of caller-supplied content | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` lines 261-269 |
| task ID | `MaoTaskDefinition.taskId`; `DelegationContract.parentTaskId` | SELF_ATTESTED and NO_PRODUCER respectively | `task.graph.contract.ts` lines 53-59; `delegation.contract.ts` line 17 |
| file scope | `MaoTaskDefinition.fileScope`; `DelegationContract.ownership.ownedFiles` | SELF_ATTESTED and NO_PRODUCER; neither reaches a guard decision through a verified receipt | `task.graph.contract.ts` line 57; `delegation.contract.ts` lines 20-25 |
| action/resource scope | Web approval snapshot (template, intent, provider, model, inputs) | TRUSTED but WRONG_SUBJECT: binds an execution request, not a file/authority scope | `approval-binding.ts` lines 49-63, 201-230 |
| receipt identity | `ApprovalRequestRecord.id` plus `requestHash`; `MaoRoleResolutionReceipt.receiptId`; `MutatingProfileApprovalRecord.approvalId` | TRUSTED for Web approval; DERIVED_NOT_VERIFIED for MAO; UNAUTHENTICATED_ISSUER for mutating profile | `execute/route.ts` lines 230, 514; `role.resolver.contract.ts` lines 135-137; `mutating-profile-approval.ts` line 18 |
| provenance | Web: Auth.js session. Provider grant: environment JSON. Mutating profile: local JSON store. Delegation: none. | mixed, as above | as cited above |

Corrected RABA-Q04 position: a trusted, non-self-attested principal producer
does exist for the Web approval subject. No current producer binds a trusted
principal to a task graph, a task and a file scope as one artifact. The
delegation contract carries exactly those fields but has neither a producer nor
a consumer, so the binding cannot be sourced end to end.

## Runtime Chain Map

Chain A - Web approval (CURRENT, complete for its own subject):

`authenticated admin session (verifySessionCookie, middleware-auth.ts:118)`
-> `canAccessAdmin role gate (approvals/[id]/route.ts:62)`
-> `approval decision record with reviewedBy (approvals/[id]/route.ts:93-101)`
-> `verifier block: actor, hash, expiry, status (execute/route.ts:185-269)`
-> `single-use consumption and delete (execute/route.ts:498-514)`
-> `execution proceeds past the NEEDS_APPROVAL gate to guard composition (execute/route.ts:578)`.

Every edge of this chain is present in current non-test source. Its defect for
RABA is subject scope, not a broken edge: nothing in the approved record names
MAO parent authority, `taskGraphId`, `taskId`, per-task `fileScope` or an
authority-delta budget.

Chain B - MCP guard evaluation (CURRENT, real consumer, untrusted input):

`z.string().optional() agentId tool argument (mcp/index.ts:406)`
-> `buildContext (mcp/index.ts:71-92)`
-> `GuardRequestContext (guard types.ts:93-112)`
-> `engine.evaluate via createGuardEngine (guard index.ts:394-408)`
-> `ALLOW / BLOCK / ESCALATE`.

Composition root is exact and real; every upstream edge carries unverified
caller data.

Chain C - mutating-profile governed exec (CURRENT, consumer behind an earlier denial):

`buildMutatingProfileApprovalRecord with unauthenticated approvedBy (mutating-profile-approval.ts:58-79)`
-> `JsonMutatingProfileApprovalPolicy.evaluate (mutating-profile-approval.ts:88-136)`
-> `governed-exec.ts:85 composition`
-> `launchGovernedCommand (governed-command-launcher.ts)`
-> `preflightGovernanceAction canonical build_authority denial (launcher:347-369)`
-> approval policy at `launcher:460` is only reached if preflight already allowed.

The launcher's own source comment (lines 337-346) records that it is a
composition root and not an authority source, and that the canonical
`build_authority` guard fails the mutating write closed before the approval
check. So this family cannot be the authority root either.

Chain D - delegation (CURRENT, both ends broken):

`no non-test producer` -> `DelegationContract (delegation.contract.ts:16)`
-> `validateWriteScope (delegation.contract.ts:155)`
-> `validateClosureReport same module (delegation.contract.ts:217)` -> `no runtime consumer`.

Chain E - CADP committed grant (CURRENT, trusted, narrow):

`git-committed capability grant`
-> `bindCommittedCapabilityOwnerGrant (capability-owner-binding.contract.ts:121)`
-> `reconcileGrantWithObservation (capability-owner-binding.contract.ts:195)`
-> `evaluateCadpCapabilityConsumer (cadp.capability.consumer.contract.ts:194)`.

This is the accepted `ARCH-ABS-021` correction, reused without re-review.

No single current chain carries
`strictly higher authority -> bound authority delta -> authentic fresh receipt -> principal/task-graph/task/file binding -> guard composition -> action decision`.
Chain A supplies authenticated issuance, freshness and single-use consumption
but not the authority-delta or scope binding. Chain E supplies committed-source
trust but only for CADP capability grants.

## Authenticity, Omission, Expiry, Replay, Forgery And Mismatch Cases

| Case | Chain A (Web approval) | Chain B (MCP guard) | Chain C (mutating profile) | Chain D (delegation) |
|---|---|---|---|---|
| authenticity | session-verified admin issuer; requester cannot set `reviewedBy` | none: any `agentId` string accepted | none: `approvedBy` unauthenticated | not reachable |
| omission | omitting `approvalId` does not bypass: the `NEEDS_APPROVAL` branch (line 498) creates a pending record and returns HTTP 409 | omission produces a guidance message only; no scope denial | omission returns `APPROVAL_POLICY_MISSING` (launcher line 442) | not reachable |
| mismatch | `requestHash !== approvalRequestHash` denies with HTTP 409 (line 230); actor mismatch denies with HTTP 403 (line 219) | no comparison exists | `APPROVAL_TARGET_MISMATCH`, `APPROVAL_PROFILE_MISMATCH`, action-hash mismatch | `validateWriteScope` denies outside ownership, but nothing calls it at runtime |
| expiry / sequence | `expiresAt` checked and record marked `expired` (lines 241-254) | not modeled on `MaoAuthorityEnvelope` | `APPROVAL_EXPIRED` plus `APPROVAL_FROM_FUTURE` (lines 122-127) | not modeled |
| replay | single-use: `getApprovalStore().delete(...)` after consumption (line 514) | pure content hash re-verifies on replay; no single-use | `bindingHash` ties the record to one receipt consumption; marker write uses `flag: 'wx'` | not modeled |
| forgery | requires forging an Auth.js session | trivial: any string | requires only local JSON store write access | not reachable |

Chain A is the only current family whose denial matrix is fail-closed across
all six cases. That strengthens it as a precedent and still does not make it
the RABA authority root, because the artifact it protects is not an authority
expansion. The six-case matrix also does not prove separation of duty or a
strictly higher-authority relation between submitter and approver.

## Owner Candidate Matrix

| Responsibility | Canonical current owner | Rejected alternatives | Rationale |
|---|---|---|---|
| authenticated approval issuance (execution requests) | `PATCH` in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/[id]/route.ts` | provider grant `authorizedBy`; mutating-profile `approvedBy`; `MaoApprovalCheckpoint` | only this one authenticates the approver server-side rather than reading an approver name out of caller-supplied data |
| approval request binding and hashing | `buildApprovalRequestSnapshot` / `computeApprovalRequestHash` in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/approvals/approval-binding.ts` | `computeAuthorityHash` in `task.graph.contract.ts` | both hash content; only the approval binding also carries a server-derived actor identity into the hashed projection |
| approval verification and single-use consumption | approval-resume block in `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | `JsonMutatingProfileApprovalPolicy` | the mutating-profile policy has no single-use deletion and sits behind an earlier canonical denial |
| authority-envelope integrity | `buildAuthorityEnvelope` / `verifyAuthorityEnvelope` in `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/mao/task.graph.contract.ts` | none competing | sole implementation with five non-test consumers |
| role/admission decision | `resolveRole` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/role.resolver.contract.ts` | none | sole exported resolver, one non-test caller |
| universal guard evaluation | `createGuardEngine` in `EXTENSIONS/CVF_GUARD_CONTRACT/src/index.ts` | none: `types.ts` line 3 declares itself the single source of truth for guard types | explicit in-source single-source declaration |
| delegated write-scope evaluation | `validateWriteScope` in `EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/delegation.contract.ts` | `evaluateDelegatedWriteBoundary` in `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/delegation.boundary.guard.contract.ts` | DUPLICATE_BEHAVIOR_ACROSS_PACKAGES: two independent evaluators implement the same owned-file/owned-module/forbidden-path algorithm; neither has a runtime consumer, so uniqueness cannot be resolved from current source |
| committed-authority capability binding | `bindCommittedCapabilityOwnerGrant` / `reconcileGrantWithObservation` in `EXTENSIONS/CVF_GUARD_CONTRACT/src/contracts/capability-owner-binding.contract.ts` | none | accepted `ARCH-ABS-021` owner, reused without re-review |
| authority-expansion approval issuance | NONE_CURRENT | Web approval route (wrong subject); provider grant, mutating profile, MAO checkpoints (unauthenticated) | no current symbol issues an approval whose subject is an authority delta |
| trusted principal/task/file-scope binding consumed by a guard | NONE_CURRENT | `DelegationContract` (no producer, no consumer); `MaoRoleResolutionReceipt` (no principal field); `GuardRequestContext.agentId` (self-attested) | no current chain carries a verified binding into a guard decision |

New owner finding not present in the RABA-T0 return: delegated write-scope
evaluation has a genuine duplicate-owner problem. `validateWriteScope`
(`delegation.contract.ts` lines 155-193) and `evaluateDelegatedWriteBoundary`
(`delegation.boundary.guard.contract.ts` lines 12-50) implement the same
normalize/forbidden/owned-file/owned-module algorithm in two packages, with
neither holding a runtime consumer. Per RABA-Q06 this is `PARK_AMBIGUOUS_OWNER`
for that responsibility.

## Current Versus Proposed Labels

Every locator above marked with a path and line number is `CURRENT`, read at
`executionBaseHead`, and has at least one cited definition or call site.
`NONE_CURRENT` rows are absent-evidence findings, not citations. The tokens
`evaluateAuthorityExpansionApproval`, `PrincipalScopeIdentityGuard` and
`verifiedFileScope` are `PROPOSED` only, confirmed absent from `EXTENSIONS` by
the negative searches recorded below, and are never treated as current
authority anywhere in this assessment.

## ARCH-ABS-021 Reuse

The accepted bounded correction from the AR1 R1 completion review (Reviewer
Dependency Matrix row for the `ARCH-ABS-021` current consumer, `PASS_BOUNDED`,
citing `evaluateCadpCapabilityConsumer`) is reused directly as Chain E without
re-review. Current source at `executionBaseHead` confirms the same call path
with no contradiction; no duplicate review was performed beyond confirming the
cited symbols still exist and still call each other.

## Exact Future Manifest

Not produced. The terminal decision below is `PARK_NO_TRUTHFUL_AUTHORITY_ROOT`,
so no proceed decision is supported and the future-manifest-union requirement
does not apply. A future manifest is deferred to a separately authorized RABA-T1
tranche.

## Negative Search And Collision Discipline

| Check | Exact command | Result | Disposition |
|---|---|---|---|
| target path pre-existence | direct file-existence check on both RABA-F01-F02 output paths before authoring | both absent | PASS_NO_COLLISION |
| batch token | `rg -n "WP-ARCH-003-RABA-F01-F02-ROOT-EVIDENCE-REASSESSMENT" docs CVF_SESSION -l` | two files: the committed work order and baseline of this same packet | PASS_NO_COLLISION |
| proposed approval evaluator | `rg -n "evaluateAuthorityExpansionApproval" EXTENSIONS` | zero matches | PASS_CONFIRMS_PROPOSED_ONLY |
| proposed scope guard and field | `rg -n "verifiedFileScope\|PrincipalScopeIdentityGuard" EXTENSIONS docs` | zero matches under `EXTENSIONS`; matches only in rejected predecessor documents under `docs` | PASS_CONFIRMS_PROPOSED_ONLY |
| `validateWriteScope` non-test consumers | `rg -n "validateWriteScope" EXTENSIONS --type ts -g "!*.test.ts" -g "!*.spec.ts"` | three hits: definition line 155, same-module call line 217, barrel re-export line 152 | CLASSIFIED_NO_EXTERNAL_CONSUMER |
| `evaluateProviderExecutionAuthority` non-test consumers | `rg -n "evaluateProviderExecutionAuthority" EXTENSIONS --type ts -g "!*.test.ts" -g "!*.spec.ts"` | definition, barrel export, and live-proof harness/script call sites in `CVF_MODEL_GATEWAY` and `CVF_EXECUTION_PLANE_FOUNDATION` | CLASSIFIED_LIVE_PROOF_HARNESS_CONSUMERS |
| `DelegationContract` non-test producers | `rg -n "DelegationContract" EXTENSIONS --type ts -g "!*.test.ts" -g "!*.spec.ts"` | interface declaration, two validator parameter positions, barrel export; no constructor | CLASSIFIED_NO_PRODUCER |
| `ProviderExecutionGrant` provenance | `rg -n "ProviderExecutionGrant" EXTENSIONS --type ts -g "!*.test.ts" -g "!*.spec.ts"` plus `parseProviderExecutionGrant` reads | every construction is `JSON.parse` of `CVF_PROVIDER_EXECUTION_GRANT_JSON` | CLASSIFIED_ENV_SUPPLIED_NOT_AUTHENTICATED |
| approval-route session provenance | direct read of `verifySessionCookie` (`middleware-auth.ts` lines 118-156) and `canAccessAdmin` (`enterprise-access.ts` lines 11-14) | identity resolved from an Auth.js JWT-decoded session, not request body fields | CLASSIFIED_CURRENT_AUTHENTICATED_ISSUER |
| `agentId` same-token collisions | `rg -n "agentId:" EXTENSIONS --type ts -g "!*.test.ts" -g "!*.spec.ts"` | unrelated `agentId` fields in `CVF_ECO_v2.0_AGENT_GUARD_SDK`, `CVF_AGENT_LEDGER`, `CVF_ECO_v2.3_AGENT_IDENTITY`, `CVF_PLANE_FACADES` | CLASSIFIED_DIFFERENT_MEANING_NOT_CURRENT_CONSUMER |

Absent-versus-collision disposition: every negative result above is a genuine
absence of a current symbol or edge, not a same-token collision mistaken for
non-authority. No documentation-only or test-only occurrence was promoted to a
runtime producer.

## Findings / Position

### RABA-F01-F02-01 - An authenticated approval issuer exists, for the wrong subject

The RABA-T0 claim `NO_ISSUER_FOUND` is corrected. The Web approval `PATCH`
route authenticates the approver through an Auth.js session and a server-side
admin role gate, and records `reviewedBy` from that verified session. The
request body cannot supply the approver identity, but no source check requires
that identity to differ from `submittedByActorId`; an admin may therefore
approve a same-scope own request. This is a real, current, non-test
authenticated approval path with a complete verifier and single-use consumer,
not proof of a distinct or strictly higher-authority issuer. It is nevertheless
not the RABA authority root: its approved subject is an AI
execution request bound to template, intent, provider, model and inputs, with
no MAO parent authority, task graph, task, file scope or authority-delta budget
in the approved receipt.

### RABA-F01-F02-02 - Provider grant and mutating-profile approvals are self-attested

`ProviderExecutionGrant.authorizedBy === "ORCHESTRATOR"` is a literal compared
against a constant, inside a JSON object parsed from a caller-controlled
environment variable. `MutatingProfileApprovalRecord.approvedBy` is an
unvalidated input string on the record builder. Both families have real
verifiers with budget, expiry and mismatch checks, and neither authenticates
who approved. Additionally, the governed launcher's own source states that the
canonical `build_authority` guard denies the mutating write before the approval
policy is consulted, so that approval cannot function as an authority root.

### RABA-F01-F02-03 - The delegation contract has the right fields and no chain

`DelegationContract` carries `parentTaskId`, `workerAgentId` and explicit
owned-file/owned-module/forbidden-path scope, which is closer to the RABA-Q04
shape than anything else in current source. No non-test code constructs it, and
`validateWriteScope` has no consumer outside its own module and a barrel
re-export. Both the producer edge and the consumer edge are absent.

### RABA-F01-F02-04 - Delegated write-scope evaluation has duplicate owners

`validateWriteScope` and `evaluateDelegatedWriteBoundary` implement the same
path-ownership algorithm in two different packages, neither with a runtime
consumer. Under RABA-Q06 this is an unresolved ownership ambiguity, and it is a
new finding not present in the RABA-T0 return.

### RABA-F01-F02-05 - Machine-parseable trace and truthful gate attribution

This tranche's operation trace lists both new output paths as literal
repository-relative strings in both `Expected manifest` and `Actual changed
set`, with no pronoun or shorthand, discharging the trace half of
`WP-ARCH-003-RABA-T0-R1-02`. The worker view at `executionBaseHead` began
clean, so no cross-artifact contamination confound exists and no exclusive-cause
claim about an unrelated artifact is made. Actual per-command exit evidence is
recorded in the paired worker return.

## Finding-To-Governance Learning Disposition

| Finding | Defect class | Learning lane | Existing owner | Disposition | Next control action |
|---|---|---|---|---|---|
| RABA-F01-F02-01 authenticated issuer exists but approves the wrong subject | `RULE_GAP` | `GOVERNANCE_CONTROL_PLANE` | RABA roadmap RABA-Q01/RABA-Q02 | `RULE_EXISTS` | a future root design should evaluate extending the Web approval issuer pattern to an authority-delta subject rather than inventing a new issuer |
| RABA-F01-F02-02 provider grant and mutating-profile approvers are unauthenticated | `RULE_GAP` | `GOVERNANCE_CONTROL_PLANE` | RABA roadmap RABA-Q01/RABA-Q03 | `RULE_EXISTS` | no future design may treat an approver-name field inside caller-supplied data as issuer proof |
| RABA-F01-F02-03 delegation contract has no producer and no consumer | `RULE_GAP` | `GOVERNANCE_CONTROL_PLANE` | RABA roadmap RABA-Q04/RABA-Q05 | `RULE_EXISTS` | a future design must name a trusted producer and a real consumer before adopting the delegation fields as the scope carrier |
| RABA-F01-F02-04 duplicate write-scope evaluators across packages | `RULE_GAP` | `GOVERNANCE_CONTROL_PLANE` | RABA roadmap RABA-Q06 | `MACHINE_CHECK_CANDIDATE` | resolve one canonical write-scope evaluator before either is wired to a runtime consumer |

Runtime/provider/cost learning lane: N/A_WITH_REASON - all findings are static
source-architecture findings over current TypeScript contracts; this assessment
made no provider call, no live runtime execution, and recorded no token or cost
sample.

## RABA Root Question Contract Outcome

| ID | Outcome | Fail-closed assessment result |
|---|---|---|
| RABA-Q01 | an authenticated issuer exists for execution requests (Web approval `PATCH`), but no current symbol issues an approval whose subject is an authority expansion, and no strictly-higher-authority relation is expressed anywhere | `PARK_NO_TRUTHFUL_APPROVAL_ISSUER` |
| RABA-Q02 | the Web approval record binds subject, action/resource and decision with a hash, but never parent authority, requested authority delta, file scope or an authority budget | `PARK_UNBOUND_APPROVAL` |
| RABA-Q03 | Chain A verifies authenticity, mismatch, expiry, status and single use; the MAO envelope path has no expiry, sequence or replay defense at all | evidence complete; Chain A passes for its own subject, MAO does not |
| RABA-Q04 | a trusted principal producer exists for the Web approval actor, but no current producer binds a trusted principal to task graph, task and file scope as one artifact; the contract that has those fields has no producer | `PARK_SELF_ATTESTED_SCOPE` |
| RABA-Q05 | three real non-test consumers exist (Web execute, MCP guard evaluation, governed exec), but none consumes a binding that satisfies RABA-Q01, RABA-Q02 and RABA-Q04 together | evidence complete; consumers exist, the binding does not |
| RABA-Q06 | one canonical owner is selected per responsibility that has one, and delegated write-scope evaluation has an unresolved duplicate owner across two packages | `PARK_AMBIGUOUS_OWNER` |

Per the work order, any fail-closed row forces the overall terminal decision to
`PARK_NO_TRUTHFUL_AUTHORITY_ROOT`. RABA-Q01, RABA-Q02, RABA-Q04 and RABA-Q06
are fail-closed from current source.

## Evidence / Verification

Evidence is the four-family reconciliation table, exact source ledger, root
authority candidate matrix, principal scope binding matrix, runtime chain map
and case table above, each citing a repository-relative path and line number
read directly at `executionBaseHead`. Verification consists of those direct file
reads, the bounded `rg` call-site searches recorded in the Negative Search And
Collision Discipline table, and the SHA-256 recomputation of the predecessor
completion review and parent roadmap. No governance gate is treated as first
discovery of this evidence; gates were run as confirmation after the source
reads were complete.

## Risk / Corrective Action

Do not treat the Web approval route as the RABA authority root: adopting it
without changing its approved subject would authorize AI execution requests
while claiming to govern authority expansion. Do not treat
`ProviderExecutionGrant.authorizedBy` or `MutatingProfileApprovalRecord.approvedBy`
as issuer proof. Do not wire either write-scope evaluator to a runtime consumer
before the duplicate-owner ambiguity is resolved. Do not begin implementation or
a RABA-T1 design from this assessment alone; RABA-T1 requires a separate
operator decision after reviewer closure.

## Decision / Disposition

Terminal decision: `PARK_NO_TRUTHFUL_AUTHORITY_ROOT`

This is the same terminal token as the predecessor tranche, now supported by
complete four-family candidate coverage rather than by an over-broad absence
claim. This assessment is non-authoritative pending evidence; only an
independent reviewer-authored completion review may accept it.

## Epistemic Process Block

### Expected Result / Prediction

Including the four omitted candidate families would either expose a defensible
authority root that the RABA-T0 return had missed, or narrow the over-broad
absence claims while still proving that the integrated chain cannot be sourced.

### Evidence Comparison

The second outcome held, with one substantive correction. The Web approval
family is materially stronger than the RABA-T0 return implied: it has a real
authenticated issuer, a complete six-case denial matrix and single-use
consumption. The provider grant and mutating-profile families are as weak as
the reviewer described. The delegation family has the right fields and no
chain. A previously unreported duplicate-owner defect was found for delegated
write-scope evaluation.

### Contradiction Or Gap Disposition

The contradiction against the RABA-T0 assessment is confirmed and resolved
here: `NO_ISSUER_FOUND` and `NONE_CURRENT` were too broad. The remaining gap is
subject scope rather than missing machinery. CVF already builds authenticated,
hash-bound, expiring, single-use approvals; none of them approves an authority
delta bound to a principal, task graph, task and file scope.

### Claim Update

The claim that CVF has no authenticated approval issuer is withdrawn. The
supported claim is narrower and stronger: CVF has one authenticated approval
issuer whose subject is an execution request, one trusted committed-source
grant binder scoped to CADP, and no current artifact that binds an authority
delta to a verified principal and scope for a guard decision.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_public_export_disposition.py`; `governance/compat/check_finding_to_governance_learning.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_rescan_intelligence_hardening.py`; `governance/compat/check_agent_packet_authority_and_encoding.py`; `governance/compat/check_review_cost_control.py` |
| literalTokensReviewed | assessment structural heading groups including source/predecessor evidence and evidence/verification, Finding-To-Governance defect-class enum plus the runtime lane escape token, ASCII-only encoding rule, SCEC required top fields, trace path literals, private export token |
| gateRunPurpose | confirmation of this assessment's shape against known checker constants after the source reads, not discovery |
| claimBoundary | checker success cannot select an issuer, prove a trusted principal binding, resolve the duplicate write-scope owner, or open RABA-T1 |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | committed packet and reviewer-owned completion | source-verification review only; no implementation | this assessment, its four-family table and the paired worker return | N/A with reason: internal review has no runtime adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | operator-relayed external worker | one invocation, exact-two outputs, no commit | execution base, trace, hashes, commands and return recorded in the paired worker return | CLI transports evidence only; it is not the authority runtime chain under review | CONTRACT_ONLY |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | committed RABA-F01-F02 packet -> explicit operator relay -> exact-two pending evidence -> independent reviewer disposition |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_worker_return_quality_gate.py` |
| Owner surface | RABA-F01-F02 work order and reviewer-owned completion review |
| Disposition | this assessment is evidence input and remains unaccepted until independent review |
| Claim boundary | no external repository absorption, worker self-acceptance or runtime authority |

## External Repository Absorption Entry Control

COMPARISON_ONLY_NO_ABSORPTION: no external repository, copied folder, mirror or
outside corpus is absorbed. All evidence is local CVF-governed source read at
`executionBaseHead`.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - this assessment makes no
  complete-scan, inventory, or all-files-read claim. Its evidence is a bounded
  named-source cluster plus targeted non-test call-site searches, sufficient
  only to answer RABA-Q01 through RABA-Q06 and the two reviewer findings.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance source-verification evidence; no public-sync
authority is claimed or exercised by this assessment.

## Claim Boundary

This assessment records current-source evidence, four-family candidate
coverage, one owner decision per responsibility and one terminal RABA-F01-F02
decision. It does not accept itself, does not design or implement an integrated
root contract, does not repair AR1 or RABA-T0, does not edit source or tests,
does not open RABA-T1 or DARA-T5, does not mutate MFRP, does not call a
provider, does not expose credentials, and does not publish, push, deploy or
claim runtime or production readiness. Only an independent reviewer-authored
completion review over the returned bytes may accept this decision.
