# CVF CADP-AI-T5 External Agent Adapter Decision Assessment

Memory class: governed-decision-assessment

Status: ACCEPTED_BOUNDED_DEFERRED_MISSING_AUTHORITY

docType: baseline

Date: 2026-08-14

Batch ID: CADP-AI-T5D

executionBaseHead: `e00d1dd96911e34b2224fc17d055d2325325c3d9`

## Purpose

Decide, from current CVF-governed sources only, whether CADP T5 can now
support a bounded external-agent read/query metadata adapter, or whether it
must be rejected or deferred. This assessment produces decision evidence
only; no adapter, MCP tool, CLI command, or runtime code is created or
proposed for immediate implementation.

## Source / Predecessor Evidence

| Predecessor | Path | Disposition cited |
|---|---|---|
| CADP-AI-T4 completion review | `docs/reviews/CVF_CADP_AI_T4_AUTHORITY_BOUNDARY_MACHINE_ENFORCEMENT_COMPLETION_2026-08-14.md` | `ACCEPTED_CLOSED_PASS_BOUNDED`; Dual Agent Surface Matrix already records `EXTERNAL_AGENT_CLI_MCP: DEFERRED_NOT_AUTHORIZED` with auth, ingress, mutation, and redaction unverified |
| CADP-AI roadmap | `docs/roadmaps/CVF_CADP_FULL_KNOWLEDGE_AND_IMPLEMENTATION_ABSORPTION_ROADMAP_2026-08-13.md` | Work Plan T5 row: `optional external-agent adapter decision`, entry condition `accepted T3/T4 plus operator authorization`, status `DISPATCH_READY_DECISION_ONLY` |
| T5 GC-018 baseline | `docs/baselines/CVF_GC018_CADP_AI_T5_EXTERNAL_AGENT_ADAPTER_DECISION_2026-08-14.md` | Decision Test: positive result requires an identified owner and fail-closed contract for authentication, input validation, field allowlisting/redaction, zero mutation/activation/execution authority, deterministic error/receipt semantics, and both internal- and external-agent surfaces; any missing prerequisite requires rejection or deferral |
| Generic MCP adapter guide | `docs/guides/CVF_GENERIC_MCP_ADAPTER_INTEGRATION_GUIDE_2026-05-31.md` | advisory only; `runtimeExecutionAuthorized=false` across all INT-1 tools; no CADP-specific tool exists in this owner |
| RTAD-T5 Model Gateway MCP boundary | `docs/baselines/CVF_GC018_RTAD_T5_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY_2026-06-18.md` | Forbidden Scope: must not add or change MCP runtime tools, add provider live calls, or claim readiness; boundary-only, no CADP adapter authority |
| ASSF external-agent readout boundary roadmap | `docs/roadmaps/CVF_ASSF_EXTERNAL_AGENT_READOUT_CLI_MCP_ADAPTER_BOUNDARY_ROADMAP_2026-06-26.md` | `Status: CLOSED_PASS_BOUNDED`; T2 result: adapter remains `DEFERRED_WITH_REASON` until a separate work order; Dual Agent Surface Matrix marks `EXTERNAL_AGENT_CLI_MCP` as `DEFERRED_WITH_REASON` pending a future source-verified GC-018/work order |
| External-agent invocation-control roadmap | `docs/roadmaps/CVF_EXTERNAL_AGENT_INVOCATION_CONTROL_KNOWLEDGE_READINESS_ROADMAP_2026-07-22.md` | Roadmap Release Rules: `T5 requires a new roadmap, fresh GC-018, source-verified work order, and an explicit operator decision lifting the invocation moratorium`; Next Allowed Move: implementation and invocation-control T5 are not opened |

## Scope / Applies To

Repository-local decision audit over currently committed CADP T1/T3A/T3B/T4
interfaces and the generic MCP, RTAD, ASSF, and invocation-control owner
surfaces named above. No adapter code, MCP tool, CLI command, external-agent
process, credential, or network action is in scope.

## Existing CADP Interface Inventory

| Surface | Path | Nature |
|---|---|---|
| capability admission/distribution contract kernel | `EXTENSIONS/CVF_GUARD_CONTRACT/` CADP contract sources (T1) | internal TypeScript contract; no HTTP/CLI/MCP entry point |
| Execution Plane consumer contract | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/src/cadp.capability.consumer.contract.ts` | internal, non-executing eligibility projection only |
| Model Gateway constraint projection | `EXTENSIONS/CVF_MODEL_GATEWAY/src/cadp.constraint.projection.contract.ts` | internal, provider-neutral metadata projection only; no provider call |
| authority boundary drift checker | `governance/compat/check_cadp_authority_boundary_drift.py` | standalone static lexical checker; not wired to any hook, autorun, or CI trigger; no HTTP/CLI/MCP surface |

Focused token/path searches across `EXTENSIONS`, `governance`, and `scripts`
found no HTTP endpoint, MCP tool registration, or CLI command that reads or
serves CADP metadata to an external caller. The bounded search returned the
internal CADP surfaces above, tests, and documentation, but no CADP-named
external entry point.

## Required Decision Analysis

| Prerequisite row | Source | Observed state | Gap | Disposition |
|---|---|---|---|---|
| owner and package boundary | CADP T1-T4 sources above | CADP is owned inside Guard Contract as a composition contract; Execution Plane and Model Gateway are accepted internal consumers | no external-facing owner package or export boundary exists | MISSING_AUTHORITY |
| caller authentication and identity binding | CADP-AI-T2/T2A owner-binding grants (`governance/capability-grants/cadp-ai-t2a-owner-binding-grant.v2.json`) | owner-binding grants exist for internal repository-local callers only | no external caller identity, token, or credential binding scheme exists for a CLI/MCP consumer | MISSING_AUTHORITY |
| ingress schema and size validation | T1 strict record types and T4 fixture schema (`governance/compat/fixtures/cadp_authority_boundary_contract.v1.json`) | internal contract shapes are strictly typed and schema-validated for internal payloads | no external-request ingress schema, size limit, or transport validator has been authored | MISSING_AUTHORITY |
| exact metadata field allowlist | T4 completion review Dual Agent Surface Matrix | evidence explicitly states auth, ingress, mutation, and redaction are unverified for `EXTERNAL_AGENT_CLI_MCP` | no field-level allowlist for a read/query response has been defined for CADP | MISSING_AUTHORITY |
| secret/private-provenance redaction | T1 distribution secret and private-provenance export rejection invariants | T1 rejects secrets and private-provenance export inside its internal distribution contract | that invariant has never been exercised against an external-facing response path; no redaction contract for an external consumer exists | MISSING_AUTHORITY |
| mutation, activation, certification, execution, provider-call, credential-resolution, and external-launch denial | T4 authority boundary drift checker; RTAD-T5 Forbidden Scope; invocation-control roadmap Roadmap Release Rules | current CADP surfaces are read-only/non-executing by construction; RTAD-T5 and the invocation-control roadmap both forbid new MCP tools or lifting the invocation moratorium without a fresh GC-018 | denial is currently achieved only by the absence of any adapter, not by an enforced fail-closed gate on a live external entry point | SATISFIED_BY_ABSENCE; not sufficient alone to authorize a new entry point |
| deterministic error and receipt shape | T1 F12 deterministic canonical receipt identity | a deterministic receipt constructor exists for internal distribution use | no error/receipt contract has been defined or tested for an external read/query response | MISSING_AUTHORITY |
| replay/freshness behavior | T2/T2A owner-binding and grant expiry reconciliation | expiry/transport/resource/credential/invocation/retry reconciliation exists for internal governed work-order binding | no replay/freshness contract exists for an external stateless read/query call | MISSING_AUTHORITY |
| internal-agent and external-agent surface accounting | T4 completion review Dual Agent Surface Matrix | `INTERNAL_AGENT` row is `CONTRACT_ONLY`/local static checker; `EXTERNAL_AGENT_CLI_MCP` row is `DEFERRED_NOT_AUTHORIZED` | none beyond the already-recorded deferral; consistent across T4, ASSF, and RTAD-T5 | SATISFIED (as a deferral record, not as adapter readiness) |
| package-root/transport discoverability | T4 package-root boundary tests; generic MCP adapter guide Quick Start | internal package roots are boundary-tested; the only existing MCP server (`EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER`) exposes generic advisory tools, none CADP-specific | no CADP tool is registered on any transport; adding one is out of this decision's scope | MISSING_AUTHORITY |
| focused negative-proof plan | T4 seven-code negative corpus and reviewer 8-probe matrix | a negative-proof method exists for the internal static checker | no negative-proof plan exists yet for an external ingress/auth/redaction surface because that surface does not exist | MISSING_AUTHORITY |
| registry, hook, public, and session effects | T4 completion review; CVF_SESSION_MEMORY.md Parked Checkpoints | T4 checker is standalone and unwired to any hook/autorun/CI; session memory records CLI/MCP invocation and adapter implementation as parked | no registry/hook/public/session change is proposed by this assessment | NOT_APPLICABLE_WITH_REASON: this assessment itself makes no such change |

Prerequisite disposition counts: `SATISFIED` = 1; `SATISFIED_BY_ABSENCE` (non-
sufficient) = 1; `MISSING_AUTHORITY` = 9; `NOT_APPLICABLE_WITH_REASON` = 1;
`CONFLICT` = 0.

## Overlap And Owner Reconciliation

| Candidate value | Existing owner | Reconciliation |
|---|---|---|
| generic advisory MCP tool calls | `CVF_ECO_v2.5_MCP_SERVER` INT-1 tools | already exists and is provider-agnostic; a CADP-specific tool would be additive, not a duplicate, but requires that owner's own GC-018 to add a tool per its Protocol/Contract/Requirements section |
| CLI/MCP external-agent readout boundary decision | ASSF external-agent readout roadmap | ASSF already ran an equivalent T0-T4 decision cycle for a different domain and reached `DEFERRED_WITH_REASON`, requiring a fresh GC-018/work order before implementation; CADP T5 reaching the same class of outcome is consistent, not duplicative |
| Model Gateway MCP bridge | RTAD-T5 boundary | RTAD-T5 is explicitly boundary-only and forbids new MCP tools; a CADP adapter cannot be routed through that boundary without its own release |
| external-agent invocation authority generally | invocation-control roadmap | that roadmap holds a repository-wide moratorium on opening T5-class invocation work absent a fresh roadmap, GC-018, work order, and explicit operator decision; CADP T5 is a sub-instance of that same moratorium |

No existing owner already provides a bounded read/query metadata adapter for
CADP; none of the four related owners duplicates this decision's scope.

## Findings / Position

Current governed sources establish that CADP T1-T4 are internal, non-
executing, provider-neutral, repository-local contracts and a standalone
static checker. The named sources and bounded reviewer search expose no hook,
MCP tool, or CLI command for CADP metadata today. Nine of twelve mandatory prerequisite
rows resolve to `MISSING_AUTHORITY`: no external caller authentication or
identity binding, no ingress schema/size validator, no field allowlist, no
tested external-redaction path, no external error/receipt contract, no
replay/freshness contract, no transport registration, no external owner/package
boundary, and no negative-proof
plan for an external surface, because none of these has ever been built or
source-verified for an external consumer. The `T5 requires ... an explicit
operator decision lifting the invocation moratorium` release rule in the
invocation-control roadmap and the `DEFERRED_WITH_REASON` T2 result in the
ASSF roadmap both independently confirm that value may exist later but no
current governed source supplies the missing owners/contracts/proofs today.

## Risk / Corrective Action

| Risk | Corrective action |
|---|---|
| treating checker/internal-contract read-only-by-construction as equivalent to a tested external fail-closed gate | keep the `SATISFIED_BY_ABSENCE` row explicitly marked non-sufficient; do not count it toward `IMPLEMENTATION_READY_BOUNDED_READ_ONLY` |
| a future worker reusing this assessment as implementation authority | this assessment's Claim Boundary and the paired work order's Operator Checkpoint both state no adapter, T6, or T7 opens from this recommendation |
| duplicating the ASSF or RTAD-T5 owner surfaces in a future CADP adapter packet | any future CADP adapter work order must cite and reconcile with the ASSF and RTAD-T5 boundary contracts named above, not re-decide their scope |

## Decision / Baseline

`terminalRecommendation: DEFER_WITH_MISSING_AUTHORITY`

Rationale: current CVF-governed sources confirm CADP has real, tested,
internal, non-executing value (T1 contract kernel, T3A/T3B consumers, T4
drift checker) that could plausibly support a bounded future read/query
metadata adapter, so outright `REJECT_WITH_REASON` is not warranted. But
`IMPLEMENTATION_READY_BOUNDED_READ_ONLY` requires all mandatory prerequisite
rows to be `SATISFIED`, and nine of twelve are `MISSING_AUTHORITY` today:
no owner package/export boundary, no external caller authentication, no
ingress schema, no field allowlist, no tested redaction path, no external
error/receipt contract, no replay/freshness contract, and no transport
registration or external-surface negative-proof plan exist for an external
consumer. The invocation-control roadmap's
Roadmap Release Rules independently require a new roadmap, fresh GC-018,
source-verified work order, and an explicit operator decision lifting the
invocation moratorium before any T5-class implementation packet may open.

## Reopen / Future-Manifest Conditions

This is not an implementation authorization. A future CADP external-agent
adapter packet may reopen this decision only after all of the following are
in place, each with its own source-verified GC-018 and work order:

1. an explicit operator decision that names CADP T5 and lifts the relevant
   scope of the external-agent invocation moratorium recorded in the
   invocation-control roadmap;
2. a named owner package/export boundary for an external-facing CADP
   read/query surface, distinct from the internal T1/T3A/T3B contract
   boundary;
3. a caller authentication and identity-binding contract for an external
   CLI/MCP consumer, analogous to the existing internal owner-binding grants;
4. an ingress schema and size-validation contract for external requests;
5. an exact metadata field allowlist plus a tested redaction contract proven
   against the existing T1 secret/private-provenance rejection invariants;
6. a deterministic external error/receipt contract, extending or reusing the
   existing T1 F12 receipt identity design;
7. a replay/freshness contract for external stateless calls;
8. a focused negative-proof plan (fixtures plus adversarial probes) for the
   new external ingress/auth/redaction surface, following the T4 negative-
   corpus and reviewer-probe pattern;
9. explicit reconciliation with the ASSF external-agent readout boundary and
   RTAD-T5 Model Gateway MCP boundary so no owner surface is duplicated.

A future implementation packet, if opened, should propose (not create in
that packet) a manifest such as: one new CADP external-readout contract
module under the existing Guard Contract owner, one MCP tool registration
under `CVF_ECO_v2.5_MCP_SERVER` gated on the authentication/ingress/allowlist
contracts above, focused positive and adversarial negative tests for the new
external surface, and a standalone drift/negative-proof checker mirroring
`governance/compat/check_cadp_authority_boundary_drift.py`'s pattern. This
assessment does not create any of that; it only names the shape a future
packet should target.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | CADP Guard Contract, Execution Plane projection, Model Gateway constraint projection, authority boundary drift checker | may consume governed metadata only within existing accepted contract authority | T1/T3A/T3B/T4 sources cited above | no new internal adapter proposed by this assessment | `CONTRACT_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | candidate future read/query surface; not implemented | no mutation, execution, provider, credential, launch, or public authority exists or is proposed | nine `MISSING_AUTHORITY` prerequisite rows above | decision only; future source-verified GC-018/work order required per Reopen conditions | `DEFERRED_WITH_REASON` |

## Evidence / Verification

- Source Verification rows above cite full repository paths and section
  identifiers for every claimed item, consistent with the paired work order's
  own Source Verification Block.
- `EXTENSIONS/CVF_GUARD_CONTRACT/` CADP contract sources, `EXTENSIONS/
  CVF_EXECUTION_PLANE_FOUNDATION/src/cadp.capability.consumer.contract.ts`,
  `EXTENSIONS/CVF_MODEL_GATEWAY/src/cadp.constraint.projection.contract.ts`,
  and `governance/compat/check_cadp_authority_boundary_drift.py` were located
  by direct file-path enumeration and confirmed present at
  executionBaseHead `e00d1dd96911e34b2224fc17d055d2325325c3d9`.
- Focused token/path searches across `EXTENSIONS`, `governance`, and `scripts`
  found no external CADP-specific HTTP/CLI/MCP entry point at this HEAD; this
  is bounded absence evidence, not a full-corpus completeness claim.
- No production, test, schema, checker, hook, registry, roadmap, or session
  file was edited to produce this assessment.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_epistemic_process_packet.py`; `governance/compat/check_external_agent_absorption_table.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_delta_execution_claim_boundary.py`; `governance/compat/check_dispatch_scaffold_provenance.py` |
| literalTokensReviewed | `docs/assessments/` path maps to the `baseline` structural class requiring source/predecessor evidence, decision/baseline/proposed tranche, and evidence/verification groups; `Delta Execution Claim Boundary Control Block` field-row table shape; `External Knowledge Intake Routing` seven row-label shape; `terminalRecommendation` enum tokens |
| gateRunPurpose | confirm the assessment satisfies its own structural class before the bundled worker-return fast gate runs |
| claimBoundary | structural checker read-ahead does not itself prove the terminal recommendation is correct; the recommendation rests on the Required Decision Analysis prerequisite matrix above |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | operator-provided external comparison, critique, or recommendation |
| Chain map route | N/A with reason: no external artifact or recommendation is ingested by this assessment |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this assessment and the paired T5D work order |
| Disposition | NOT_APPLICABLE_WITH_REASON |
| Claim boundary | only CVF-governed repository sources support this decision |

## Delta Execution Claim Boundary Control Block

| Field | Value |
|---|---|
| claimScope | CADP T5 external-agent adapter decision assessment |
| claimDisposition | CLAIM_REJECTED: no execution-control, runtime-enforcement, interception, or adapter behavior is claimed |
| receiptEvidence | CLAIM_REJECTED_NO_RECEIPT: no runtime receipt is created or consumed by this assessment |
| actionEvidence | CLAIM_REJECTED_NO_ACTION: no runtime or external-agent action is executed or observed |
| invocationBoundary | local read-only inspection and governed Markdown authoring only |
| interceptionBoundary | no direct interception, wrapper/proxy enforcement, runtime gate, or agent coding control is authorized |
| claimLanguage | decision recommendation only, pending independent review |
| forbiddenExpansion | no adapter implementation, MCP/CLI invocation, external-agent launch, provider/live action, credentials, public sync, deploy, production, T6, or T7 |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance decision assessment; no public artifact or sync
action is authorized or performed.

## Claim Boundary

This assessment records a source-backed decision recommendation only. It
does not implement, authorize, or prove any adapter, MCP tool, CLI command,
external-agent invocation, authentication, redaction, receipt, replay,
transport, provider, credential, public-sync, deployment, or production
behavior. `terminalRecommendation: DEFER_WITH_MISSING_AUTHORITY` binds no
future tranche; it only names the exact reopen conditions above.
