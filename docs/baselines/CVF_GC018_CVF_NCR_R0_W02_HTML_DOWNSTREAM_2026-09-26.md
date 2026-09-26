# CVF GC-018 Baseline - CVF-NCR-R0-W02 HTML Downstream Effect Boundary

Memory class: governed-dispatch-baseline

docType: baseline

Status: DISPATCH_READY

Batch ID: CVF-NCR-R0-W02

Dispatch base head: `7b5758c72983da3295666748d3e89ed670325cf5`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator for data, effect and expense; Local reviewer for source and technical disposition

Reviewer owner: Local orchestrator/reviewer, distinct from worker

Worker target: shared-workspace `INTERNAL_AGENT` source/profile-mapping role

## Purpose

Authorize one read-only source trace of the HTML receipt path beyond the export helper. The worker follows `/api/governance/evaluate` to the configured Governance Engine client and its downstream owner, then returns a decision-ready map of possible egress, persistence, latency and cost. W00/W01 remain accepted bounded; no pilot run occurs.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-R0-W02 --title "HTML Downstream Effect Boundary" --date 2026-09-26 --base 7b5758c72983da3295666748d3e89ed670325cf5 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | generic-worker-dispatch plus no-commit internal worker profile |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | adapted accepted W01 packet shape to W02 downstream source trace, new authority and stop rules |
| checkerReadAheadConfirmation | read dispatch quality, envelope, closeability, ADIF and governed read-ahead checker sources before authoring |
| docOnlyNewFields | second-hop egress, persistence and decision matrix |
| claimBoundary | scaffold provenance and dispatch shape only, not runtime proof |

## Authorization / Decision

The operator resumed delegation after D011 was integrated at `7b5758c72983da3295666748d3e89ed670325cf5`. Roadmap Q001 and the Local-accepted W01 return at `d9b43a6f6deff7fb19710b5a9a4f50bf2a6015b6` leave the configured destination, downstream effects and expense open. This batch is the next document-only Local scope: inspect named tracked source and produce one pending return. Operator decisions on data, route effect and cost remain separate.

## Scope

Allowed: read named tracked export helper, evaluate route, Governance Engine HTTP client and the narrowly identified downstream owner files; map authentication, destination derivation, request fields, further network calls, persistence/retention evidence, error/timeout behavior and cost uncertainty; identify exact configuration key names only, without values; create exactly one pending worker return. Stop source expansion at the first fully explained terminal effect or a named missing-owner boundary.

Forbidden: browser/UI interaction, route invocation, network/egress, provider call, raw `.env*` or credential inspection, dependency install, code/tests/owner/guide/roadmap changes, media production, public action, stage/commit, or edits to the separate 52-deferred lane. Do not search ignored/untracked configuration files or print source-content payloads. Unknown actual configuration remains `UNKNOWN`.

Maximum worker write set: `docs/reviews/CVF_CVF_NCR_R0_W02_HTML_DOWNSTREAM_WORKER_RETURN_2026-09-26.md` only. Local owns review, commit and continuity.

## Baseline Invariants

1. The operator's pilot-candidate selection is settled; do not compare candidates again.
2. W00/W01 source evidence is accepted bounded. Reuse its consumer/form/route trace and P06/P08 disposition; no repeated selection or source matrix.
3. The export route awaits `fetchGovernanceReceipt`; an absolute `NEXTAUTH_URL` can trigger a POST with a content excerpt. The evaluate route calls `governanceEvaluate`, whose client may POST to a configured Governance Engine URL. This is source-visible conditional behavior, not actual-profile proof.
4. Classify each conditional hop, authentication, failure and any storage or provider boundary separately. Do not turn a 4000ms abort setting into a measured latency bound or missing source into no retention/cost.
5. UI, route and live effect evidence remain `NOT_RUN`; the operator has not selected a data/effect/expense profile for a pilot call.
6. A source-only map may reduce Q001 unknowns but does not close P06/P08, establish L1/L2/L3 or authorize R1/R2 code change.
7. Existing AKOE-P2-R2/P3 and U1 remain closed bounded; this order does not reopen them. The 52-deferred lane is separate.
8. Guide/video D010 is a later documentation tranche and not HTML pilot evidence.

## Verification / Evidence

Dispatch evidence is the committed paired packet, synchronized active continuity and passing bound pre-dispatch gate. Worker evidence is one secret-safe two-hop source/effect trace, a terminal-effect or named-gap disposition, and exact changed-set return. Local reviewer checks decision-changing locators without recreating W00/W01. This baseline is document evidence only.

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| Candidate selection | NCR roadmap D009 at committed HEAD `7b5758c72983da3295666748d3e89ed670325cf5` | retain HTML choice, no reselection | ACCEPT |
| W00 source review | `docs/reviews/CVF_CVF_NCR_R0_W00_PILOT_SELECTION_WORKER_RETURN_2026-09-26.md`, Local disposition | reuse current consumer/route trace and open P06/P08/receipt facts | ACCEPT |
| W01 source/profile review | `docs/reviews/CVF_CVF_NCR_R0_W01_HTML_PROFILE_WORKER_RETURN_2026-09-26.md`, Local disposition at `d9b43a6f6deff7fb19710b5a9a4f50bf2a6015b6` | reuse first-hop receipt facts; trace only downstream gap | ACCEPT |
| Paired work order | `docs/work_orders/CVF_AGENT_WORK_ORDER_CVF_NCR_R0_W02_HTML_DOWNSTREAM_2026-09-26.md` | material commit plus continuity and bound pre-dispatch gate before relay | PENDING_GATE |
| Pilot effect | actual endpoint/data/retention/cost and operator choice still open | no effect in W02 | DEFER |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | paired work order and one worker return | read-only downstream source mapping; no commit or effect | roadmap Q001, W01 and exact source trace | shared-workspace file/Git evidence only | CONTRACT_ONLY |
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
| claimBoundary | static authoring and role/shape admission only; downstream source facts remain worker research and Local review |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| selected HTML and open decisions | roadmap decision | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D009, Q001, R0/R1 | HTML candidate; effect/data/cost open | operator scope | ACCEPT |
| accepted first-hop boundary | reviewer evidence | `docs/reviews/CVF_CVF_NCR_R0_W01_HTML_PROFILE_WORKER_RETURN_2026-09-26.md` | Local Reviewer Disposition, Secret-Safe Actual-Profile Matrix | W01 source/profile packet | Local reviewer | ACCEPT |
| export helper | current source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` | `fetchGovernanceReceipt`, `resolveEvaluateUrl` | conditional POST to evaluate route | cvf-web receipt helper | ACCEPT |
| evaluate route | current source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/evaluate/route.ts` | `POST`, `governanceEvaluate` | auth and downstream call | cvf-web API | ACCEPT |
| Governance Engine client | current source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/governance-engine.ts` | `getConfig`, `governanceFetch`, `governanceEvaluate` | configured URL and second POST | cvf-web HTTP client | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| New W02 artifact names | exact target paths absent before generation; worker return path absent | no prior W02 packet overwritten |
| Existing W00/W01 evidence | Local-accepted returns present; no new owner/field is declared | reuse without repeating matrices |
| New runtime symbol | none introduced | NOT_APPLICABLE_WITH_REASON: document-only downstream mapping |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local orchestrator/reviewer |
| Provider or surface | private CVF workspace |
| Session or invocation | CVF-NCR-R0-W02 dispatch authoring, 2026-09-26 |
| Working directory | repository root |
| Command or tool surface | governed reads, `rg`, Git, scaffold, local gates |
| Target paths | this baseline and paired work order |
| Allowed scope source | operator resumed internal worker delegation after D011; Q001/W01 authorize Local to scope a bounded read-only successor |
| Before status evidence | clean HEAD `7b5758c72983da3295666748d3e89ed670325cf5` |
| After status evidence | dispatch packet material commit plus continuity commit required before relay |
| Diff evidence | exact two-file dispatch material batch |
| Approval boundary | operator data/effect/budget; Local technical review |
| Claim boundary | documentation-only source mapping; no capability execution |
| Agent type | orchestrator/reviewer |
| Invocation ID | `cvf-ncr-r0-w02-dispatch-2026-09-26` |
| Expected manifest | baseline and paired work order |
| Actual changed set | checked at material commit |
| Manifest delta | pending material commit |

## Claim Boundary

This baseline authorizes one source-backed W02 downstream-effect return. Actual configuration, egress, persistence, expense, UI behavior and pilot readiness remain subject to separate evidence and operator decisions.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: this is a private provenance dispatch packet, with no public artifact or public-sync authorization.
