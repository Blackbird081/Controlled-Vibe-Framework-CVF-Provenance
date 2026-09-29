# CVF GC-018 Baseline - CVF-NCR-R0-W01 HTML Pilot Profile Evidence

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Batch ID: CVF-NCR-R0-W01

Dispatch base head: `11ba9eb46`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator for data, effect and expense; Local reviewer for source and technical disposition

Reviewer owner: Local orchestrator/reviewer, distinct from worker

Worker target: shared-workspace `INTERNAL_AGENT` source/profile-mapping role

## Purpose

Authorize one documentation-only profile reconciliation after the operator selected the existing Work Transfer HTML review packet as the first internal pilot candidate. The worker checks the current source path, actual available configuration evidence and remaining P06/P08/receipt-helper/UI-walkthrough gaps, then returns one bounded read-only decision packet for Local review. No pilot run occurs.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-R0-W01 --title "NCR R0 W01 HTML Pilot Profile Evidence" --date 2026-09-26 --base 11ba9eb46 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit internal worker profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | replaced generated skeleton with bounded W01 authority, source/profile axes, owner, evidence and stop rules |
| checkerReadAheadConfirmation | read dispatch quality, envelope, closeability, ADIF and governed read-ahead checker sources before authoring |
| docOnlyNewFields | actual-profile classification, receipt-egress boundary and UI walkthrough admission |
| claimBoundary | scaffold provenance and dispatch shape only, not runtime proof |

## Authorization / Decision

The operator selected the HTML candidate and asked Local to continue as orchestrator/reviewer, with Claude as a separately relayed internal worker. NCR roadmap D009/D010 and the Local-accepted W00 return at commit `c7b7a2c721a3388a738eb2b2633fc4414cf1dff3` are the current planning basis. This baseline authorizes source/profile inspection and a pending document only. Operator effect/expense approval and any runtime/UI interaction remain separate decisions.

## Scope

Allowed: inspect named source, tests, profile documentation and secret-safe configuration metadata; classify what actual profile is known versus `UNKNOWN`; trace receipt destination/payload/timeout/retention/cost and P06/P08 depth; propose a harmless UI walkthrough protocol without executing it; create exactly one pending worker return.

Forbidden: UI pilot execution, route invocation, network/egress, provider call, credential or raw environment-variable inspection, dependency install, code/owner/guide/roadmap changes, media production, public action, stage/commit, or edits to the separate 52-deferred lane. Treat unknown active config as `NEEDS_EVIDENCE`, never infer a value.

Maximum worker write set: `docs/reviews/CVF_CVF_NCR_R0_W01_HTML_PROFILE_WORKER_RETURN_2026-09-26.md` only. Local owns review, commit and continuity.

## Baseline Invariants

1. The operator's pilot-candidate selection is settled; do not compare candidates again.
2. W00 source reading proved the Work Transfer UI/form/preview/download and route, not an actual browser walkthrough.
3. The route awaits `fetchGovernanceReceipt`; whether it sends depends on an absolute `NEXTAUTH_URL`. Do not expose configured values or source text.
4. P06/P08 remain `PARTIALLY_CONFIRMED_NEEDS_EVIDENCE`; show precise fixture/validation gaps without writing tests in this tranche.
5. Distinguish no-cost local source inspection from unmeasured potential receipt egress, latency, retention and cost.
6. Simulated agent observation, actual UI action, and machine/provider proof are distinct evidence classes.
7. Existing AKOE-P2-R2/P3 and U1 remain closed bounded; this order does not reopen them. The 52-deferred lane is separate.
8. Guide/video D010 is a later documentation tranche and not HTML pilot evidence.

## Verification / Evidence

Dispatch evidence is the committed paired packet, synchronized active continuity and passing bound pre-dispatch gate. Worker evidence is one secret-safe source/profile matrix and exact changed-set return. Local reviewer checks source locators and unresolved decisions without recreating W00. This baseline is not UI, network, runtime or usability proof.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| Candidate selection | NCR roadmap D009 at committed HEAD `11ba9eb46` | retain HTML choice, no reselection | ACCEPT |
| W00 source review | `docs/reviews/CVF_CVF_NCR_R0_W00_PILOT_SELECTION_WORKER_RETURN_2026-09-26.md`, Local disposition | reuse current consumer/route trace and open P06/P08/receipt facts | ACCEPT |
| Paired work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R0_W01_HTML_PROFILE_2026-09-26.md` | material commit plus continuity and bound pre-dispatch gate before relay | PENDING_GATE |
| Pilot effect | actual endpoint/data/retention/cost and operator choice still open | no effect in W01 | DEFER |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | paired work order and one worker return | read-only source mapping; no commit or effect | roadmap R0/W01 and exact Git/source trace | shared-workspace file/Git evidence only | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no adapter work in this batch | no external ingress, auth, receipt, raw-data or mutation authority | external advisory input already reviewed in roadmap | N/A with reason: no CLI/MCP adapter is designed or changed | N/A_WITH_REASON |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | scoped source evidence, clean two-commit dispatch binding and separate Local review remain required |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_adif_defect_registry_disclosure.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py` |
| literalTokensReviewed | dispatch status, exact Source Verification columns, envelope-first rule, gate graph columns, ADIF query and read-ahead scalar labels |
| gateRunPurpose | confirmation evidence after source/literal read, not first discovery or proof of implementation |
| claimBoundary | static authoring and role/shape admission only; actual profile remains worker research and Local review |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| HTML selection and guide split | roadmap decision | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D009/D010 and Q001 | HTML candidate selected, guide later | operator scope | ACCEPT |
| accepted W00 boundary | review evidence | `docs/reviews/CVF_CVF_NCR_R0_W00_PILOT_SELECTION_WORKER_RETURN_2026-09-26.md` | Local Reviewer Disposition | source trace accepted bounded | Local reviewer | ACCEPT |
| UI entry | source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx` | ArtifactExportPanel embedding | Work Transfer page | cvf-web UI | ACCEPT |
| route call | source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | POST / fetchGovernanceReceipt | export route | cvf-web API | ACCEPT |
| receipt helper | source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` | NEXTAUTH_URL conditional fetch | fetchGovernanceReceipt | cvf-web receipt helper | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| New W01 artifact names | exact `Test-Path` on both packet names was false before generation | no previous W01 packet overwritten |
| Existing W00 owner | Local-accepted W00 review and current source found; no new owner/field is declared | reuse without redoing selection |
| New runtime symbol | none introduced | NOT_APPLICABLE_WITH_REASON: document-only profile work |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace |
| Session or invocation | CVF-NCR-R0-W01 dispatch authoring, 2026-09-26 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, Git, scaffold, local gates |
| Target paths | this baseline and paired work order |
| Allowed scope source | operator instruction and selected roadmap D009/D010, Q001 |
| Before status evidence | clean HEAD `11ba9eb46` |
| After status evidence | dispatch packet material commit plus continuity commit required before relay |
| Diff evidence | exact two-file dispatch material batch |
| Approval boundary | operator data/effect/budget; Local technical review |
| Claim boundary | documentation-only source mapping; no capability execution |
| Agent type | orchestrator/reviewer |
| Invocation ID | `cvf-ncr-r0-w01-dispatch-2026-09-26` |
| Expected manifest | baseline and paired work order |
| Actual changed set | checked at material commit |
| Manifest delta | pending material commit |

## Claim Boundary

This baseline authorizes one source-backed W01 profile return. It does not establish actual configured destination, run the UI, send data, approve effect/cost, repair P06/P08, produce a guide/video, or claim runtime/live/public readiness.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance dispatch packet, with no public artifact or public-sync authorization.
