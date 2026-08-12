# CVF GC-018 Baseline - Local Retention Artifact T2 V041 Candidate Terminal Disposition

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

Batch ID: LRA-T2

Dispatch base head: `b8acef1a8258e16f0803cb675f21907152b30cca`

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: operator

Reviewer owner: independent reviewer/closer

Worker target: delegated no-commit source-intake worker

Source intake decision packet: REQUIRED

External absorption core: REQUIRED

External knowledge intake routing: REQUIRED

## Purpose

Authorize one bounded read-only value and owner reconciliation for the 18 V041
archive artifacts left deferred by accepted LRA-T0. T2 must give every one of
the 18 a source-backed terminal disposition so the retention roadmap can move
to T4 without importing an unowned runtime, package, CLI, MCP, provider, or
production claim.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind source-intake --batch-id LRA-T2 --title "Local Retention V041 Candidate Terminal Disposition" --date 2026-08-12 --base b8acef1a8258e16f0803cb675f21907152b30cca --commit-mode WORKER_MUST_NOT_COMMIT --dependency "LRA-T0 reviewer acceptance at a4c7a0a840643f7d669ec2b91752d4cd9ff7771d" --stdout --include-worker-return-skeleton` |
| generatedProfile | source-intake plus no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced placeholders with the exact 18-entry corpus, terminal-disposition objective, seven-path worker manifest, runtime boundary, dual-agent accounting, and source-backed T0 dependency |
| checkerReadAheadConfirmation | dispatch, source-intake, external-intake/core/value/overlap, corpus, workspace-runtime, operation-trace, and closure checker sources read before authoring |
| docOnlyNewFields | no new schema or checker field; batch-specific values only |
| claimBoundary | dispatch-authoring provenance only; no source admission or runtime behavior claim |

## Dependency Release Evidence

| Dependency | Current evidence | Release rule | Disposition |
|---|---|---|---|
| LRA-T0 reviewer acceptance | `docs/reviews/CVF_LOCAL_RETENTION_ARTIFACT_T0_INVENTORY_AND_AUTHORITY_AUDIT_COMPLETION_2026-08-12.md` at material commit `a4c7a0a840643f7d669ec2b91752d4cd9ff7771d` | operator explicitly releases T2 and fresh GC-018 binds exactly the 18 deferred rows | RELEASED_FOR_T2_DISPATCH |

## Scope / Target / Owner Boundary

Allowed scope:

- read the immutable ZIP and the exact 18 manifest rows currently marked
  `DEFER_REQUIRES_NEW_AUTHORITY`;
- compare each source item with current CVF owners using complete hidden and
  ignored-file searches;
- update only the T2 audit, manifest dispositions, local-retention registry
  entry and aggregates, existing findings packet, and worker return;
- assign each of the 18 a terminal evidence-backed disposition.

Forbidden scope:

- no copy or extraction of archive content into Core or `EXTENSIONS`;
- no new runtime, package, skill, CLI, MCP, IDE, provider, production, or
  public owner surface;
- no source, test, script, checker, session, roadmap, baseline, or work-order
  mutation by the worker;
- no execution of archived Python, shell, PowerShell, MCP, CLI, or tests;
- no ZIP mutation or deletion, staging, commit, push, deploy, secrets, network,
  live call, public-sync, or production claim.

Risk ceiling: R1 documentation and registry metadata only.

## Baseline / Decision

T2 is released as a no-commit, documentation-and-registry-only source-intake
tranche. The authorized outcome is a terminal disposition ledger for exactly
18 entries. No direct source import, new owner surface, executable behavior, or
archive deletion is authorized.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`source intake candidate disposition`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Returned defects: NONE_RETURNED

| Field | Value |
|---|---|
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "source intake candidate disposition" --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling MEDIUM --json` |
| Returned defect count | 0 |
| Returned defects | NONE_RETURNED |
| Disclosed defectIds | NONE |
| Dispatch impact | no additional defect-specific constraint; normal source-intake and no-commit guards remain binding |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_dispatch_quality_range.py`; `governance/compat/check_source_intake_decision_packet_preflight.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_core.py`; `governance/compat/check_external_absorption_value_conversion.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_agent_workspace_runtime_boundary.py` |
| literalTokensReviewed | real section headings, source-verification columns, intake fields, external-core fields, value-conversion lanes, overlap dispositions, runtime mode, and no-commit lifecycle fields |
| gateRunPurpose | confirm a complete fail-closed dispatch shape before the worker receives the packet |
| claimBoundary | structural compliance does not decide semantic value or admit any archive item |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| T0 accepted 129 entries with 18 deferred candidates | predecessor closure fact | `docs/reviews/CVF_LOCAL_RETENTION_ARTIFACT_T0_INVENTORY_AND_AUTHORITY_AUDIT_COMPLETION_2026-08-12.md` | Decision / Disposition; Findings / Position | 111 terminal; 18 deferred | LRA-T0 completion review | ACCEPT |
| exact candidate corpus is machine-readable | manifest fact | `docs/corpus-intelligence/manifests/local-retention-artifacts-20260812.json` | entries array | disposition equals `DEFER_REQUIRES_NEW_AUTHORITY` for exactly 18 rows | local-retention manifest | ACCEPT |
| T2 is the only candidate branch and needs fresh authority | roadmap fact | `docs/roadmaps/CVF_LOCAL_RETENTION_ARTIFACT_DISPOSITION_AND_SELECTIVE_ABSORPTION_ROADMAP_2026-08-12.md` | Work Plan; Next Allowed Move | T2 | LRA roadmap | ACCEPT |
| runtime expansion is not authorized by a foundation packet | boundary fact | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` | Runtime Expansion Boundary; Work Order Requirement | `QUEUE_SKELETON_ONLY` | workspace runtime readiness contract | ACCEPT |
| external material must be classified before governed mutation | routing fact | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` | Mandatory Chain | classify, map owner, disposition, then fresh work order for mutation | external knowledge chain map | ACCEPT |
| both internal and external agent consumers require explicit disposition | architecture fact | `docs/reference/CVF_DUAL_AGENT_SURFACE_ACCOUNTING_STANDARD_2026-06-23.md` | Core Rule; Mandatory Dual Agent Surface Matrix | `INTERNAL_AGENT`; `EXTERNAL_AGENT_CLI_MCP` | dual-agent accounting standard | ACCEPT |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
|---|---|---|
| T2 governed path existence | `Test-Path` returned false for the baseline, work order, and worker return before authoring | ACCEPT_NEW_PACKET |
| batch token search | `rg -n --fixed-strings "LRA-T2" docs CVF_SESSION` returned no pre-existing packet hit | ACCEPT_NO_COLLISION |
| candidate owner posture | accepted T0 manifest contains per-row `rg` owner searches and `OWNER_NOT_FOUND`; T2 must rerun `rg --files --hidden --no-ignore` and content searches before final disposition | RECOMPUTE_REQUIRED |
| collision decision | use the existing LRA roadmap and registry owner; do not create a second workspace foundation or runtime | ACCEPT_EXISTING_OWNER |

## Source Intake Decision Packet

| Field | Value |
|---|---|
| Decision packet standard | `docs/reference/external_agent_review/CVF_KIOD_R8_SOURCE_INTAKE_DECISION_PACKET_STANDARD.md` |
| Input root or repository | immutable `CVF_LOCAL_RETENTION_20260812.zip` pinned by SHA-256 `09e0e6f0b9de305b4cc3ce34f7cc2f0ebe0b82aa8e4b98774dd4ff0b2192493a` |
| Bounded scope | exactly 18 manifest rows currently deferred; no other ZIP entry or repository lane |
| Enumeration authority | structured ZIP central-directory lookup keyed by the accepted manifest, plus `rg --files --hidden --no-ignore` for current owners |
| Owner-surface taxonomy | `docs/reference/external_agent_review/CVF_KIOD_R1_OWNER_SURFACE_TAXONOMY.md`; selected class is existing LRA evidence owner, with current capability owner search required per row |
| Pre-scan packet source | `docs/reference/external_agent_review/CVF_KIOD_R2_PRE_SCAN_PACKET_STANDARD.md`; accepted T0 manifest and completion review form the bounded pre-scan packet |
| Overlap routing matrix | `docs/reference/external_agent_review/CVF_KIOD_R3_OVERLAP_ROUTING_MATRIX_STANDARD.md`; worker must choose evidence-backed existing-owner, direct-reject, or no-new-value routes per row |
| Negative-search evidence | T0 owner searches are prior evidence; T2 reruns complete hidden/no-ignore path and content searches and records every command in the audit |
| Core disposition | terminal `REJECT`, `NO_NEW_VALUE`, or evidence-only `ADAPT`; `DEFER` and `BLOCK` are not successful T2 closure outcomes |
| Value conversion requirement | evaluate doctrine, package, runtime, checker, direct-import rejection, and no-package/runtime lanes without activating any candidate |
| Overlap classification requirement | compare every item and finish with `CONFIRMED_EXISTING`, `REJECT_DIRECT_IMPORT`, or `NO_NEW_VALUE`; missing owners must be resolved by terminal rejection, not a new surface |
| Worker output path | seven paths in the paired work-order fulfillment manifest |
| Forbidden scope | runtime/source/test/checker/session/roadmap/baseline/work-order mutation, source copy, execution, deletion, live/provider/public scope |
| Claim boundary | pre-dispatch authority for terminal documentation/registry disposition only; no item is admitted by this packet |

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | corpus scan or extraction intake |
| Chain map route | accepted T0 corpus -> 18-row T2 value/owner reconciliation -> terminal manifest and registry disposition -> independent review -> T4 retention closeout |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_source_intake_decision_packet_preflight.py` |
| Owner surface | LRA roadmap, manifest, registry entry, audit, findings, and completion review chain |
| Disposition | ADAPT evidence into terminal CVF-owned disposition metadata; REJECT_DIRECT_IMPORT for archive payloads |
| Claim boundary | routing does not import source or create runtime, package, CLI/MCP, provider, or public authority |

## External Absorption Core

| Field | Value |
|---|---|
| Standard | `docs/reference/external_agent_review/CVF_EXTERNAL_ABSORPTION_CORE_STANDARD.md` |
| Input root or repository | exact 18-row subset of the immutable local-retention ZIP |
| Enumeration command | structured ZIP entry lookup from the accepted manifest and `rg --files --hidden --no-ignore` owner searches |
| Manifest artifact or inline manifest | `docs/corpus-intelligence/manifests/local-retention-artifacts-20260812.json` |
| Processing ledger artifact or inline ledger | the same manifest entries plus the T2 audit per-item table |
| Ledger terminal statuses | READ, ADAPTED, DEFERRED, REJECTED, NO_NEW_VALUE, BLOCKED_UNREADABLE |
| Disposition taxonomy | ABSORB, ADAPT, DEFER, REJECT, BLOCK, NO_NEW_VALUE |
| Owner-surface map | T2 audit inline owner/value matrix and existing CVF paths found by complete search |
| Unresolved items | 18 at dispatch; successful T2 closure requires 0 |
| Completion claim boundary | only the 18-row terminal value/owner disposition; no runtime/provider/public/production expansion |

## External Absorption Value Conversion Matrix

| Source item | Value extracted | Conversion lane | CVF target surface | Next governed action | Runtime/package boundary |
|---|---|---|---|---|---|
| security and hardening documents | default-deny and secret-boundary concepts to compare | DOCTRINE_ADAPTED | existing governance and workspace-runtime contracts | retain only non-duplicate evidence in T2 audit | documentation evidence only |
| IDE and MCP templates | client configuration pattern to evaluate | PACKAGE_CANDIDATE | pending owner evaluated by T2 audit | terminally reject if no current CVF owner and executable module exist | no package activation or install |
| CLI binding and launcher scripts | adapter and launcher pattern to evaluate | RUNTIME_CANDIDATE | workspace runtime readiness contract | terminally reject direct import absent current runtime owner and proof | no execution or runtime wiring |
| guardrail test and checklist | negative-case pattern to compare | CHECKER_CANDIDATE | current workspace and governance checker owners | retain only if a concrete missing invariant is proven; otherwise close no-new-value | no test/checker mutation |
| provider-specific and install artifacts | direct-copy risk and stale paths | REJECT_DIRECT_IMPORT | LRA evidence owner | record terminal rejection reason | no provider or installer claim |
| thin agent instruction duplicates | proposal/receipt wording already governed elsewhere | NO_PACKAGE_OR_RUNTIME_VALUE | existing agent/workspace governance | close as duplicate or evidence-only | no package/runtime value claim |

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
|---|---|---|---|---|
| all 18 deferred rows | existing governed workspace, CLI/MCP, security, runtime-readiness, agent instruction, and checker surfaces found by complete search | OWNER_SURFACE_NOT_FOUND at dispatch; final row must use a terminal allowed disposition | T0 proved missing same-name owners but did not decide semantic value | rerun negative searches and route each row to terminal close action in the T2 audit |

Next governed action for the dispatch-time missing-owner state: execute the
paired LRA-T2 work order, record complete negative-search evidence, and close
each row without opening a new owner surface.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | existing CVF workspace/governance owners and T2 evidence packet | read-only archive comparison; no action authority | accepted T0 manifest and current repository searches | N/A with reason: T2 creates no internal runtime adapter | N/A_WITH_REASON |
| `EXTERNAL_AGENT_CLI_MCP` | no current adapter owner admitted by this tranche | no CLI/MCP ingress, authentication, approval, receipt, mutation, or public claim | archive templates reference absent modules; current owner must be source-verified | deferred adapter owner is rejected for direct import in T2 | DEFERRED_WITH_REASON |

## Runtime Expansion Control Block

| Field | Value |
|---|---|
| runtimeMode | `QUEUE_SKELETON_ONLY` |
| contractSource | `docs/reference/agent_workspace/CVF_AGENT_WORKSPACE_RUNTIME_EXPANSION_READINESS_CONTRACT.md` |
| frontDoor | `docs/reference/agent_workspace/README.md` |
| stateSourceOfTruth | existing generated workspace state; unchanged by T2 |
| queueBoundary | queue skeleton only; no executable record or scheduler |
| operatorViewBoundary | read-model plan unchanged; no UI implementation |
| providerBoundary | no provider or live call |
| publicBoundary | private-only; no public-sync |
| guardOwner | `governance/compat/check_agent_workspace_runtime_boundary.py` |

## Acceptance Criteria

- exactly 18 input rows reconcile to the accepted manifest and ZIP hashes;
- all 18 contents are read without executing or importing them;
- each row records current-owner searches, semantic value, direct-import risk,
  and one terminal disposition;
- zero `DEFER_REQUIRES_NEW_AUTHORITY` rows remain after successful T2;
- the manifest arithmetic becomes 129 terminal, zero deferred;
- no new package/runtime/checker/CLI/MCP/provider/public owner is created;
- all seven worker outputs exist, required gates pass, HEAD is unchanged, and
  nothing is staged or committed by the worker.

## Required Evidence / Verification

- pinned ZIP SHA-256 and exact 18-entry path/hash reconciliation;
- complete per-item content-read and current-owner search ledger;
- explicit terminal rationale for all 18 and arithmetic showing 129 terminal,
  zero deferred;
- exact seven-path changed-set evidence and forbidden-path non-mutation;
- GC-047, GC-048, GC-050, GC-051, worker-return-fast, and diff-hygiene PASS;
- HEAD unchanged with no staging or worker commit.

## Corpus Completeness And Report Integrity

- Corpus task class: ABSORPTION
- Corpus root: exact 18-entry subset of immutable ZIP SHA-256 `09e0e6f0b9de305b4cc3ce34f7cc2f0ebe0b82aa8e4b98774dd4ff0b2192493a`
- Snapshot time: 2026-08-12 accepted T0 manifest
- Enumeration command: structured complete API lookup of all 18 manifest paths in the ZIP
- Manifest artifact or inline manifest: `docs/corpus-intelligence/manifests/local-retention-artifacts-20260812.json`
- Manifest hash: `e36acc3a2dea6abcafd878564294ec72b65268a5460048020780e7ac771a9fb9`
- Processing ledger artifact or inline ledger: T2 audit per-item matrix and updated manifest rows
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE
- Reconciliation: manifest=18; ledger_terminal=0; exclusions=0; unresolved=18 at dispatch
- Unresolved files: 18 at dispatch
- Declared exclusions: none
- Unreadable or unsupported files: none established at dispatch
- Aggregation check: accepted T0 count and hash set define the bounded subset
- Drift check: RECOMPUTE_REQUIRED by worker
- Output traceability: T2 audit, manifest, registry entry/aggregates, findings, and worker return
- Adversarial verification: reviewer must recompute all 18 ZIP hashes and audit terminal-value decisions
- Corpus verdict: PARTIAL - dispatch defines the complete subset but does not claim T2 processing completion

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private retained-source disposition only; no public-safe artifact or
public-sync authority exists in T2.

## Claim Boundary

This baseline authorizes a terminal documentation/registry disposition for
exactly 18 retained archive items. It does not admit their content, create an
owner, implement or execute anything, delete the ZIP, or authorize T4 before
independent reviewer acceptance.
