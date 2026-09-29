# CVF GC-018 Baseline - ACEL G1 T3A-C1 Principal-Bound Key Ceremony Tooling

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-09-18

Batch ID: ACEL-G1-T3A-C1-PRINCIPAL-BOUND-KEY-CEREMONY-TOOLING

Dispatch base HEAD: `40f6a8b514dcd507723cd919561656fecf87b126`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: operator authorized the separate local principal and Local selected the bounded tooling tranche.

Reviewer/closer: Local orchestrator/reviewer.

Worker: one shared-workspace `INTERNAL_AGENT`.

## Purpose

Build and hermetically test a Windows-local Ed25519 ceremony tool that can
later be invoked interactively by the operator while logged on as the exact
Party A principal. This tranche must not generate, access, or promote the real
Party A key and must not create the Group 1 registry.

## Scope / Owner Boundary

The worker may create one PowerShell ceremony wrapper, one JavaScript key
generator helper, and one worker return. Tests use only ephemeral keys under
the current worker user's temporary directory and must remove them. The worker
must not run as `cvf-g1-party-a`, request or receive its password, access any
Party A profile, touch local account configuration, execute the actual
ceremony, create registry/lifecycle source files, stage, or commit.

Local owns review and commit. The operator alone may later invoke the accepted
tool under `cvf-g1-party-a`; that invocation is a separate checkpoint.

## Decision / Baseline / Proposed Tranche

Windows source inspection establishes principal `cvf-g1-party-a`, SID
`S-1-5-21-1644666849-912006174-747199667-1006`, enabled, password required,
not a local Administrator, and expiring 2026-10-18. Node v22.17.0 generated
and verified an ephemeral Ed25519 key in memory. The proposal is tooling plus
hermetic self-test only. `successorTrancheOpened: NO` for ceremony execution,
registry creation, verifier wiring, candidate admission, or runtime use.

## Dependency Release Evidence

| Dependency | Evidence | Release condition | Disposition |
|---|---|---|---|
| separate local principal | Windows `Get-LocalUser` and local Administrators membership checks on 2026-09-18 | exact SID, enabled, password required, non-admin | ACCEPT |
| operator authorization | operator approved account creation and reported completion; Local independently verified Windows state | tooling design and hermetic tests only | ACCEPT_BOUNDED |
| key route | `docs/audits/CVF_ACEL_G1_T3A_KEY_CEREMONY_ROUTE_READINESS_2026-09-18.md`, Decision / Disposition | new Ed25519 key, private material outside repo | ACCEPT |
| source contract | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md`, Source Group 1 | preserve schema/status boundary | ACCEPT |
| actual ceremony and Group 1 source | no executed Party A logon or principal-bound key exists | separate operator checkpoint following Local tooling acceptance | PARKED_NO_EXECUTION_AUTHORITY |

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | three exact worker outputs | tooling and ephemeral self-test only; no principal credentials or real ceremony | committed dispatch plus Windows/Node preflight | shared workspace; no external adapter | `TOOLING_ONLY` |
| `EXTERNAL_AGENT_CLI_MCP` | no interface | no credential ingress, account operation, ceremony, registry or mutation | no external execution claimed | CLI/MCP adapter deferred | `DEFERRED_WITH_REASON` |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Group 1 requires Ed25519 public-key row and lifecycle evidence | ACCEPTED_CONTRACT | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Source Group 1 | `publicKeyBytesBase64`; `keyId`; lifecycle receipt | Group 1 source contract | ACCEPT |
| T3A requires principal and ceremony authorization | ACCEPTED_ORDER | `docs/audits/CVF_ACEL_G1_T2F_OPERATIONAL_SOURCE_ESTABLISHMENT_CONTRACT_2026-09-18.md` | Proposed Implementation Order | Future T3A | implementation ordering | ACCEPT |
| private material stays outside repository | ACCEPTED_ROUTE | `docs/audits/CVF_ACEL_G1_T3A_KEY_CEREMONY_ROUTE_READINESS_2026-09-18.md` | Decision / Disposition | new-key route | T3A route decision | ACCEPT |
| current local test key is non-operational | CURRENT_BOUNDARY | `docs/audits/CVF_ACEL_G1_T3A_KEY_CEREMONY_ROUTE_READINESS_2026-09-18.md` | Post-Decision Local Test Custody Evidence | `TEST_ONLY_NON_OPERATIONAL` | Local custody evidence | ACCEPT |

## Negative Search And Collision Discipline

Literal `Test-Path` probes returned false for the paired T3A-C1 dispatch files,
both tooling paths and the return before authoring. The exact batch-ID search
over governed Markdown/JSON/Python/PowerShell/JavaScript roots returned no
prior packet. This is bounded collision evidence, not a complete corpus scan.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_review_cost_control.py`; `governance/compat/check_semantic_convergence_control.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_worker_return_quality_gate.py`; `governance/compat/check_markdown_structural_completeness.py` |
| literalTokensReviewed | DISPATCH_READY; Source Verification columns; no-commit return profile; closeability phases; trace and export labels |
| gateRunPurpose | confirm packet shape after source inspection, not prove Party A key custody |
| claimBoundary | machine PASS cannot authorize or execute the real ceremony |

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id ACEL-G1-T3A-C1-PRINCIPAL-BOUND-KEY-CEREMONY-TOOLING --title "ACEL G1 T3A-C1 Principal-Bound Key Ceremony Tooling" --date 2026-09-18 --base 40f6a8b514dcd507723cd919561656fecf87b126 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --no-evidence-readiness-applicable --stdout` |
| generatedProfile | generic worker dispatch; internal INITIAL; no-commit |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | principal, secret boundary, three outputs and hermetic evidence requirements |
| checkerReadAheadConfirmation | dispatch, convergence, closeability, structural and return checker sources |
| docOnlyNewFields | no operational schema field; tool metadata remains pre-source |
| claimBoundary | scaffold use does not prove custody or execute ceremony |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`CODE_CHANGE`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`

Resolver command: `python governance/compat/run_adif_defect_resolver.py --task-class CODE_CHANGE --role dispatcher --lifecycle-phase pre-dispatch`

Returned defects: NONE_RETURNED

Returned defect count: 0

Dispatch impact: no matched entry; explicit secret and principal boundaries remain binding.

## Corpus Completeness And Report Integrity

- Corpus task class: N/A with reason - bounded named-file dispatch, not a corpus inventory.
- Corpus root: N/A with reason - no corpus root was authorized.
- Snapshot time: 2026-09-18 dispatch authoring.
- Enumeration command: filesystem-backed direct file reads plus `rg --files --hidden --no-ignore` for bounded path existence, and targeted `rg -n` source lookups.
- Manifest artifact or inline manifest: Source Verification Block.
- Manifest hash: N/A with reason - no generated corpus manifest.
- Processing ledger artifact or inline ledger: Source Verification Block rows.
- Allowed terminal statuses: READ | SKIPPED_WITH_REASON | DEFERRED | BLOCKED_UNREADABLE.
- Reconciliation: manifest=inline; ledger_terminal=READ; exclusions=full-corpus inventory; unresolved=0.
- Unresolved files: 0
- Declared exclusions: full corpus inventory, external repository intake and generated aggregate mutation.
- Unreadable or unsupported files: none
- Aggregation check: N/A with reason - no aggregate produced.
- Drift check: N/A with reason - no aggregate edited.
- Output traceability: paired baseline and work order identify all inputs and outputs.
- Adversarial verification: negative path and collision probes were run before authoring.
- Corpus verdict: COMPLETE_WITH_DECLARED_EXCLUSIONS

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | internal governed input (no external intake) |
| Chain map route | operator authorization plus Local Windows verification -> INTERNAL_AGENT tooling -> Local review |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py` |
| Owner surface | this baseline and paired work order |
| Internal source | `docs/audits/CVF_ACEL_G1_T3A_KEY_CEREMONY_ROUTE_READINESS_2026-09-18.md` |
| Disposition | `NOT_APPLICABLE_INTERNAL_ONLY_WITH_REASON`: no external source admitted |
| Claim boundary | Local remains final private-CVF technical decision owner |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Mandatory Blind-Spot Control Block

`NOT_APPLICABLE_WITH_REASON`

Reason: internal first-party tooling dispatch; no external or legacy absorption.

## External Repository Absorption Entry Control

`NOT_APPLICABLE_WITH_REASON`

Reason: no external repository input or source-mirror intake.

## Evidence / Verification Boundary

The worker must prove exact-user/SID fail-closed checks, output-path exclusion
from the repository, exclusive-create behavior, DPAPI CurrentUser protection,
public metadata derivation, sign/verify roundtrip and cleanup using ephemeral
test data only. No self-test may claim that Party A performed a ceremony.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private Windows-principal ceremony tooling with no public authorization.

## Claim Boundary

This baseline authorizes tooling and hermetic tests only. It does not authorize
password access, alternate-user execution, a real key, registry/lifecycle
source creation, key promotion, receipt issuance, verifier wiring, admission,
provider use, public sync or deployment.
