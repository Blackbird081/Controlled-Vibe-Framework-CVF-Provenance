# CVF GC-018 Baseline - QM Operational Recovery T1
Memory class: governed-dispatch-baseline
docType: baseline
Status: APPROVED_FOR_EXECUTION
Date: 2026-09-15
Batch ID: QM-OPERATIONAL-RECOVERY-T1
Commit mode: WORKER_MUST_NOT_COMMIT
dispatchBaseHead: d4a81699788a053391625ed2ec88e120b56d4c32

## Purpose

Project the already-implemented QM-derived service-token replay control and its two real Web consumers into the machine-readable as-built catalog, and record the QM-derived known-value redaction feature as value-parked because no truthful non-test value supplier exists. This tranche adds no runtime code and must not manufacture a consumer.

## Decision / Baseline

Replay deduplication is runtime-present and invoked by two non-test routes, bounded to one process. Known-value redaction remains a valid opt-in foundation but has no lawful production activation path. Paired work order: `docs/work_orders/CVF_AGENT_WORK_ORDER_QM_OPERATIONAL_RECOVERY_T1_2026-09-15.md`.

## Scope / Target / Owner Boundary

Worker owns only the compact catalog/gap records, their generated aggregates, narrowly necessary family summaries, and the worker return named by the paired work order. Runtime source is read-only. Local owns review, acceptance, commits, continuity, and every successor decision.

## Source Verification Block

| Fact | Source file | Verified section | Disposition |
| --- | --- | --- | --- |
| Process-local replay ledger and exact-replay rejection | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/service-token-auth.ts` | lines 38-49 and 117-142 | ACCEPT |
| Execute route invokes verifier | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts` | import line 25; invocation line 117 | ACCEPT |
| QBS clarification route invokes verifier | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/qbs/front-door-clarification/route.ts` | import line 5; invocation line 26 | ACCEPT |
| Known-value input is trusted in-process dependency only | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-command-launcher.ts` | dependency contract lines 176-192; snapshot line 329 | ACCEPT |
| Sole non-test launcher caller supplies no known values | `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/src/cli/governed-exec.ts` | launcher call lines 72-89 | ACCEPT |
| Recovery decision and owner correction | `docs/reviews/CVF_THREE_REPO_PILOT_FINAL_ASSESSMENT_AND_RECOVERY_2026-09-15.md` | Three-repository operational state and Risk / Corrective Action | ACCEPT |
| Compact-entry and generated-view topology | `docs/reference/system_architecture_catalog/README.md` | Family Contents and Relationship To The R91 System-Chain Map | ACCEPT |

## Acceptance Criteria

The catalog can retrieve the replay control, its Web consumer edge, exact owner paths, process-local limitation, accepted evidence, and freshness inputs. The GAP ledger can retrieve the redaction no-consumer blocker and a source-checkable reopen condition. Generated outputs match compact sources; runtime files remain byte-identical; no live/provider/secret/public action occurs.

## Evidence / Verification

Require schema validation through the existing catalog drift checker, deterministic regeneration, focused existing replay tests, exact changed-set evidence, and a no-commit worker return. Existing accepted evidence is reused; no broad rerun or live proof is required.

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_as_built_system_catalog_drift.py`; `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_agent_operation_trace.py` |
| literalTokensReviewed | dispatch-ready status; exact gate graph columns; compact source entries; generated aggregate; External Knowledge Intake Routing; Work-Order Fulfillment Manifest |
| gateRunPurpose | Confirm dispatch shape and machine projection boundaries, not discover source semantics |
| claimBoundary | No runtime implementation, live behavior, or absorption completion is certified by checker read-ahead |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`architecture catalog system chain projection`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class "architecture catalog system chain projection" --role dispatcher --lifecycle-phase pre-dispatch --risk-ceiling MEDIUM --json`. Returned defects: NONE_RETURNED; items=[], totalCandidates=0, truncated=false.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Local dispatcher |
| Provider or surface | internal workspace |
| Session or invocation | QM-OPERATIONAL-RECOVERY-T1 dispatch |
| Working directory | repository root |
| Command or tool surface | bounded source reads, rg, apply_patch, source verification and pre-dispatch gates |
| Target paths | this baseline and paired work order |
| Allowed scope source | operator direction on 2026-09-15 and final three-repository recovery assessment |
| Before status evidence | clean HEAD d4a81699788a053391625ed2ec88e120b56d4c32 |
| After status evidence | paired dispatch documents only before continuity projection |
| Diff evidence | `git diff --name-status` |
| Approval boundary | machine projection of existing runtime plus truthful parked GAP; no runtime mutation |
| Claim boundary | dispatch only, no worker result or three-repository closure |
| Agent type | dispatcher |
| Invocation ID | qm-operational-recovery-t1-dispatch-2026-09-15 |
| Expected manifest | this baseline and paired work order |
| Actual changed set | this baseline and paired work order |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: none |

## External/Local Coordination Binding

```json
{
  "contractId": "cvf.external-local-absorption-coordination@1",
  "invariants": {
    "externalRole": "ADVISORY_RESEARCH_AND_PATTERN_MAPPING",
    "externalContext": "PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ",
    "localRole": "SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION",
    "finalDecisionOwner": "LOCAL",
    "localCoverageBasis": "SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST",
    "externalEvidenceAuthority": "INPUT_NOT_PRIVATE_CVF_PROOF"
  },
  "contractSha256": "92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c",
  "parentArtifact": "docs/reviews/CVF_THREE_REPO_PILOT_FINAL_ASSESSMENT_AND_RECOVERY_2026-09-15.md"
}
```

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external-agent returned output |
| Chain map route | retained external evidence -> Local source/runtime verification -> bounded private machine projection |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | as-built catalog and system-chain GAP compact sources |
| Disposition | `ADAPT` replay evidence and `DEFER` redaction activation behind truthful reopen conditions |
| Claim boundary | external evidence is advisory input; Local owns private-CVF truth and final disposition |

## Claim Boundary

Authorizes private, machine-readable architecture projection of already-accepted bounded facts only. It does not authorize changes to runtime, secrets, environment, CLI/MCP schemas, persistence, distributed replay, provider/live execution, public sync, deployment, or program closure.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private provenance recovery dispatch; no public artifact or public-sync action.
