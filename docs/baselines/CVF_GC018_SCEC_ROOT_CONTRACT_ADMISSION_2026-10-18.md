# CVF GC-018 Baseline - SCEC Root Contract Admission

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY
Date: 2026-10-18

Dispatch condition: Root releases the worker only after the committed, bound pre-dispatch gate passes. This packet records approved scope; it does not claim release occurred.

Batch ID: SCEC_ROOT_CONTRACT_ADMISSION

Dispatch base head: bf838e0de68c1eb0cf47a49b4b0228ff64b43cc4

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: LOCAL

Reviewer/closer: Root Local reviewer

Worker target: one INTERNAL_AGENT source-maintenance worker

Role and phase: INTERNAL_AGENT Local dispatch author; phase DISPATCH; decision owner LOCAL

## Purpose

Record the operator-approved exact four-path SCEC owner-maintenance scope and bounded verification so Root can release one worker after the bound pre-dispatch gate. This is a fresh owner-maintenance chain, separate from the R1 product recovery chain.

Startup acknowledged: current mode=cvf_scec_root_contract_admission_dispatched; active handoff=AGENT_HANDOFF_V63_2026-09-18.md; next allowed move=release the exact work order after Root's committed bound pre-dispatch PASS; parked checkpoint=R1 product dispatch remains conditional on installed and verified admission; role=INTERNAL_AGENT Local dispatcher; phase=DISPATCH; decision owner=LOCAL.

## Scope Decision and Boundary

The operator explicitly approved the exact four SCEC paths and focused verification in reply "Cho phép scope 4 SCEC và kiểm chứng" to call_908d64c71dfc4c8d9b08f9363f4da679. The approved source is the Canonical Owner Change Proposal - Explicit Approval Required section of docs/baselines/CVF_NCR_R1_INTEGRATED_HTML_JOB_DESIGN_2026-10-18.md, raw SHA256 2ff7a70ebdc2ca929e5b3e4a59882b7214e6387b869e3b2ffd44fa8c436509ea.

This tranche changes the SCEC standard, its existing checker, one focused helper, and one focused test. It does not dispatch or implement R1 product source, run a product, call a provider, use a network, touch real data, write publicly, deploy, change a roadmap, edit the current six continuity files, or change a registry. Approval is not a claim of installed admission or product readiness.

The actual prior product-chain child is docs/reviews/CVF_NCR_HTML_DRAFT_RECOVERY_BROWSER_COMPLETION_2026-10-18.md, raw SHA256 756c64da7af786cf8c220f6d60474d7334710707c051da2f96d0375bb01eac7b. It declares requiredDisposition=ROOT_CONTRACT_REQUIRED and successorScope=NO_SUCCESSOR, with empty blockers. It is the only admissible product-chain predecessor fixture. The prospective STOP object in the pinned R1 design is historical/prospective, not an actual predecessor. This owner-maintenance work order has its own problem key and INITIAL ordinal zero; it does not carry a product rootContractAdmission pointer and does not reset or continue the R1 recovery chain.

## Approved Seven-Clause Source Contract

Implement the approved design clauses without expanding their authority:

1. Preserve cvf.semanticConvergenceControl.v1, stable problem key, SUCCESSOR ordinal-plus-one, exact predecessor SHA, normal blocker reconciliation, and all counters. Add one optional strict rootContractAdmission pointer with schema cvf.scecRootContractAdmissionPointer@1.0.0, path, SHA256, and stage DISPATCH or RETURN. All-absent retains current behavior. Partial, duplicate, malformed, or unverifiable opt-in fails closed; no counter reset. The selected empty-to-empty streak remains two at dispatch and three at return.
2. Resolve the pointer to an existing non-archive UTF-8 Markdown baseline or review no larger than 65,536 bytes with exactly one strict root-contract-admission-json object. Reject duplicate JSON keys before ordinary parsing can discard them, unsafe paths, invalid hashes, and inconsistent types. Resolve repository bytes and hash from a single byte snapshot; never trust a packet-controlled root.
3. Require exact grant fields: schemaVersion=cvf.scecRootContractAdmission@1.0.0, status=ACCEPTED_FOR_BOUNDED_SOURCE_IMPLEMENTATION, decisionOwner=LOCAL, operatorInstructionEvidence, problemKey, predecessor path/hash, sourceContract path/hash, workOrderPath, workerReturnPath, allowedArtifacts, effectCeilings, and expiresAtUtc. Grant, source contract, and work order are outside allowedArtifacts; worker return is included. Reuse check_work_order_acceptance_ledger.validate_work_order(text) and require allowedArtifacts to equal the exact union of its valid expectedArtifacts. Compare the real artifact path. Expiry uses actual UTC, not a packet clock. Reject self-reference, archive paths, traversal, symlink escape, worker-writable grant, absent source hash, or mismatched manifest.
4. Require exactly providerCalls, networkCalls, publicWrites, deployments, realDataMutations, destructiveActions, and productRuntimeStarts in effectCeilings, each a strict integer zero (booleans are invalid). Effects are source edits and isolated in-process fixture verification only. Production, provider, network, public, real-data, deployment, destructive, and product-runtime effects are excluded; no prior actor/effect budget transfers.
5. Permit DISPATCH only for the exact bound work-order path directly after the bound actual ROOT_CONTRACT_REQUIRED predecessor with empty prior and current blockers. Require the predecessor ROOT_CONTRACT_REQUIRED state and the bound child candidate INTEGRATED_ROOT_CONTRACT scope, no runtime-readiness assertion, and no INITIAL or renamed product problem. The one narrow integrated dispatch can supersede that predecessor's declared NO_SUCCESSOR only for the bound pair. It must never follow an actual STOP predecessor.
6. Permit RETURN only for the exact bound worker-return path immediately after that work order and with the same pinned admission. Preserve monotonic ordinal and counters, empty blockers, READY_WITH_EXECUTABLE_PROOF / EXECUTABLE_IMPLEMENTATION, and the existing nonempty claim-to-proof mapping. Limit readiness to actual source/fixture assertions; infer no application, provider, business acceptance, or whole-R1 exit. Worker failure may return ordinary STOP_REASSESS_ARCHITECTURE / NO_SUCCESSOR; it earns no retry or successor.
7. Exhaust admission after the exact dispatch/return pair. Reject replay or any changed path, ordinal, predecessor, grant, manifest, or blockers. Preserve historical defaults and interpretations. The prospective R1 STOP remains a declaration, not an actual chain continuation.

## SCEC Owner-Maintenance Chain

This is the fresh chain for the actual SCEC owner gap, not a reset or continuation of the product recovery key:

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "scec-root-contract-source-admission",
  "chainMode": "INITIAL",
  "chainOrdinal": 0,
  "predecessor": null,
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": ["SCEC-ROOT-ADMISSION-OWNER-GAP"],
    "reopened": [],
    "current": ["SCEC-ROOT-ADMISSION-OWNER-GAP"]
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 0,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 0
  },
  "claims": [
    {
      "claimId": "SCEC-ROOT-ADMISSION-OWNER-SCOPE",
      "claimClass": "OTHER",
      "proofClass": "NAMED_OBSERVABLE_PROOF",
      "evidenceRef": "Operator approval call_908d64c71dfc4c8d9b08f9363f4da679 and pinned design section"
    }
  ],
  "requiredDisposition": "CONTINUE_BOUNDED",
  "successorScope": "INITIAL_BOUNDED"
}
```

The source checker still enforces STOP after two non-decreasing transitions by default. Tests must prove unchanged default STOP and separately prove prospective, strictly bound product dispatch/return fixtures through the real repository identity and evidence resolvers. Fixture evaluation is declared-state verification only.

## Focused Verification Contract

| Case | Expected result |
| --- | --- |
| No admission and ordinary empty-to-empty ordinal 2 | Existing mandatory STOP remains enforced. |
| Prospective R1 bound direct ROOT dispatch and exact immediate proof return | Each candidate is evaluated with repository resolvers and real artifact_path; accepted only in declared bound scope. |
| Actual STOP predecessor, new INITIAL product key, renamed problem, narrow scope, or active blockers | Reject; no exception. |
| Missing, partial, malformed, duplicate, or wrong-stage pointer/grant | Reject visibly; never disappear to PASS0 or default acceptance. |
| Wrong raw hash/source contract/owner/manifest/real artifact path/expiry | Reject. |
| Worker-writable or self-referential grant; unsafe, oversized, non-UTF-8, traversal, or symlink-escaping path | Reject. |
| Nonzero or boolean effect ceilings, missing resolver, undocumented proof, or fake readiness | Reject. |
| Replay, second pair, changed work-order/return path, predecessor, grant, manifest, ordinal, or blockers | Reject. |
| Existing SCEC regression suite and legacy fixtures | Existing expected verdicts retained; no counter migration. |
| Old public validator calls without admission context | Backward-compatible default results retained. |

No global release gate is part of worker proof. Root owns the bound pre-dispatch gate, independent probe, final review, current continuity, and closure.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: exact four protected paths and focused verification specified in this baseline and paired work order.

Protected paths:

- docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md
- governance/compat/check_semantic_convergence_control.py
- governance/compat/semantic_convergence_root_admission.py
- governance/compat/test_semantic_convergence_root_admission.py

Operator authorization: the exact reply recorded above, call call_908d64c71dfc4c8d9b08f9363f4da679, approving the four paths and focused verification in the pinned design proposal.

Rollback boundary: only these four owner paths and focused source/test changes. No broader SCEC policy, unrelated checker, product path, registry, hook, autorun catalog, roadmap, runtime, provider, or public change is authorized.

## Root Continuity Manifest Authorization

Root owns these exact eight dispatch-material paths: paired baseline and work order plus the six active continuity paths. Root owns all six continuity edits and synchronization; they are not worker outputs.

- docs/baselines/CVF_GC018_SCEC_ROOT_CONTRACT_ADMISSION_2026-10-18.md
- docs/work_orders/CVF_AGENT_WORK_ORDER_SCEC_ROOT_CONTRACT_ADMISSION_2026-10-18.md
- AGENT_HANDOFF_V63_2026-09-18.md
- CVF_SESSION_MEMORY.md
- CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json
- CVF_SESSION/state/entries/nextAllowedMove.json
- CVF_SESSION/ACTIVE_SESSION_STATE.json
- CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json

Authorization basis: approved owner scope and existing session-sync authority. This exact-eight manifest does not authorize a roadmap change. Root binds final pair bytes and committed material before worker release.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified section/symbol | Verified path or value | Disposition |
| --- | --- | --- | --- | --- | --- |
| Exact four owner paths and seven admission clauses | AUTHORIZED_SCOPE | docs/baselines/CVF_NCR_R1_INTEGRATED_HTML_JOB_DESIGN_2026-10-18.md | Canonical Owner Change Proposal; SHA256 2ff7a70ebdc2ca929e5b3e4a59882b7214e6387b869e3b2ffd44fa8c436509ea | four paths above | ACCEPT |
| Actual product ROOT predecessor | SOURCE_STATE | docs/reviews/CVF_NCR_HTML_DRAFT_RECOVERY_BROWSER_COMPLETION_2026-10-18.md | Semantic Convergence Outcome; SHA256 756c64da7af786cf8c220f6d60474d7334710707c051da2f96d0375bb01eac7b | ROOT_CONTRACT_REQUIRED / NO_SUCCESSOR, empty blockers | ACCEPT |
| Current parser and validation seams | EXISTING_OWNER | governance/compat/check_semantic_convergence_control.py | validate_block, find_active_blocks, repository hash/evidence resolvers | 974 lines at dispatch base | ACCEPT |
| Work-order exact-output ledger validation | EXISTING_OWNER | governance/compat/check_work_order_acceptance_ledger.py | validate_work_order(text) | reuse for exact expectedArtifacts union | ACCEPT |
| Default escalation contract | GOVERNED_STANDARD | docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md | escalation invariants and ROOT/STOP clauses | actual STOP remains terminal | ACCEPT |
| Size budget and shrink requirement | GOVERNED_STANDARD | governance/toolkit/05_OPERATION/CVF_GOVERNED_FILE_SIZE_GUARD.md | python_checker threshold and near-hard guidance | 1,000 hard lines; 25-line margin | ACCEPT |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind protected-governance-path --batch-id SCEC_ROOT_CONTRACT_ADMISSION --title "SCEC Root Contract Admission" --date 2026-10-18 --base bf838e0de68c1eb0cf47a49b4b0228ff64b43cc4 --commit-mode WORKER_MUST_NOT_COMMIT --scec-problem-key scec-root-contract-source-admission --scec-chain-mode INITIAL --scec-chain-ordinal 0 --scec-required-disposition CONTINUE_BOUNDED --scec-successor-scope INITIAL_BOUNDED --stdout |
| generatedProfile | protected-governance-path plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | Added approved scope, seven-clause contract, separate owner INITIAL chain, exact worker and Root manifests, evidence contracts, read-ahead, and N/A reconciliation. |
| checkerReadAheadConfirmation | SCEC, core-guard, acceptance-ledger, gate-to-role, and ADIF checker sources read before authoring. |
| docOnlyNewFields | Exact clause mapping; dual-agent binding; Root continuity manifest; source/fixture-only proof boundary. |
| claimBoundary | Dispatch authoring and declared-state contract only; no installed helper, runtime, provider, live, public, product, or AI-governance efficacy claim. |

Generated scaffold: .cvf/runtime/scec-root-contract-admission-20261018/dispatch-scaffold.txt; actual command exited 0. Scratch is ignored and is not a worker output.

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | governance/compat/check_semantic_convergence_control.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/run_adif_defect_resolver.py; governance/compat/build_dispatch_packet_scaffold.py |
| literalTokensReviewed | rootContractAdmission; cvf.scecRootContractAdmissionPointer@1.0.0; cvf.scecRootContractAdmission@1.0.0; ACCEPTED_FOR_BOUNDED_SOURCE_IMPLEMENTATION; ROOT_CONTRACT_REQUIRED; INTEGRATED_ROOT_CONTRACT; STOP_REASSESS_ARCHITECTURE; READY_WITH_EXECUTABLE_PROOF; EXECUTABLE_IMPLEMENTATION; DISPATCH; RETURN; exact four-path scope; exact six-path worker ledger; DEFERRED_PRIVATE_ONLY; N/A corpus verdict |
| gateRunPurpose | Source, scope, and declaration-shape confirmation; not first discovery and not runtime proof. |
| claimBoundary | Read-ahead does not prove implementation, reviewer judgment, agent comprehension, or runtime/provider behavior. |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`, maxResults=100.

Actual command: `python -B governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 100 --json`. Actual exit0,27 returned, truncated=false; custodied `.cvf/runtime/scec-root-contract-admission-20261018/adif-work-order-authoring-dispatcher-pre-dispatch.json`. Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0056, ADIF-0057, ADIF-0058, ADIF-0061, ADIF-0062, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006.

Impact: exact source/output union, authority/encoding/read-ahead, bound lifecycle bases and final-byte return evidence. The earlier governance-machine-hardening filter returned0; it is not substituted for the canonical dispatcher query.

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | internal governed input (no external intake) |
| Internal source | docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md |
| Chain map route | private SCEC owner -> approved exact4 source -> bounded fixture review |
| Matching local-view guard | governance/compat/check_external_knowledge_intake_routing.py |
| Owner surface | canonical SCEC owner and approved root-admission design |
| Disposition | NOT_APPLICABLE_WITH_REASON: named internal source only |
| Claim boundary | Shared-workspace planning aide and implementation worker are INTERNAL_AGENT; Local decides. |

## Dual Agent Surface Matrix

| Surface | Role and phase | Decision owner | Disposition | Binding |
| --- | --- | --- | --- | --- |
| INTERNAL_AGENT | Local worker, implementation and source-only tests | LOCAL | ACCEPT | exact four source paths; exact six outputs; no commit |
| EXTERNAL_AGENT_CLI_MCP | no external research or repository absorption | LOCAL | N/A_WITH_REASON | Local retains private-CVF verification; no external adapter in scope |

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private governance maintenance only; no public artifact, public-sync remote, or public commit is authorized or claimed.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - selected owner paths and focused fixtures only; no corpus result is asserted.

## Knowledge System Reconciliation

- Knowledge task class: targeted source-design preparation, not corpus absorption
- Source manifest: the selected owner symbols and the exact worker manifest
- Source manifest hash: NOT_APPLICABLE_WITH_REASON - no knowledge corpus manifest selected
- Enumeration safety: filesystem-backed named owner reads; no directory enumeration selected
- Intake registry or ledger: not applicable to this internal design; no acquired knowledge files
- Authority assets: 0 - no new knowledge corpus; existing named owners retain authority
- Derived views: 0 - no knowledge view generated
- Semantic region ledger: 0 - no semantic corpus selected
- Region reconciliation: assets=0; mapped=0; deferred=0; unmapped=0
- Orphan or unmapped assets: 0
- Cross-region links: not applicable to this source design
- Drift check: named owner pins rechecked; no repository-wide freshness claim
- Rebuildability check: not applicable to a knowledge map; existing session generator used separately
- Retrieval boundary: no retrieval readiness or corpus completeness claim
- Adversarial verification: not a corpus task; canonical successor candidate evaluated separately
- Knowledge-map verdict: PARTIAL

## Text Encoding Exception

The only non-ASCII text is the single verbatim operator reply recorded above in Scope Decision and Boundary. It is retained as exact authorization evidence; all other text is ASCII.

## Claim Boundary

This baseline authorizes only the exact owner-maintenance scope after Root's bound committed pre-dispatch PASS. It records the operator's exact four-path approval. It does not prove implementation, grant R1 product dispatch, authorize product/runtime/provider/network/public/data/deploy effects, or establish governance efficacy.

rawMemoryReleased=false.

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Decision / Baseline

SOURCE_OWNER_DESIGN_ACCEPTED_BOUNDED. Explicit operator scope4 and focused verification satisfied; committed bound pre-dispatch PASS still controls worker release. Product R1 is not yet admitted.

## Evidence / Verification

Use the paired work-order ledger for existing and new focused SCEC tests, real repository-resolver fixtures, exact checker-size reduction and final-byte worker return. No app/provider proof or whole-job readiness claim.

