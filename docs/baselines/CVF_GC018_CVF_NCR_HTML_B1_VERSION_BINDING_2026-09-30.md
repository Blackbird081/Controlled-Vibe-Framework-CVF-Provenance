# CVF GC-018 Baseline - NCR HTML B1 Version Binding

Memory class: governed-dispatch-baseline

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-HTML-B1-VERSION-BINDING

Dispatch base head: `44542a063`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local technical reviewer; operator owns effect and data checkpoints.

Worker target: shared-workspace `INTERNAL_AGENT`.

## Purpose

Authorize one bounded consumer repair so an HTML review packet's visible result and governance receipt remain tied to the exact form version submitted for that generation attempt. This baseline does not authorize any Q001/R0 ledger decision or pilot effect.

## Source / Predecessor Evidence

The operator selected B1 packet authoring on 2026-09-30 after the D034/D035 roadmap reconciliation. `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` still parks Q001/R0 real-ledger decisions. The new B1 lane is separate from that checkpoint. `DESIGN.md` governs user-facing clarity.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| B1 is the next bounded HTML repair candidate | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D034, Work Plan | D034 | NCR roadmap | ACCEPT |
| Form edits retain result while generation assigns the next response directly | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | lines 258-299 | `updateRequest`, `handleGenerate` | HTML export consumer | ACCEPT |
| Copy, download and print act on the displayed result | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | lines 301-322 | `handleCopy`, `handleDownload`, `handlePrint` | HTML export consumer | ACCEPT |
| Existing focused tests mock fetch and verify candidate rendering | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx` | lines 28-94 | `ArtifactExportPanel` tests | component test owner | ACCEPT |
| The server creates HTML from multiple fields but hashes only source text | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | lines 288-362 | `POST`, `sourceHash`, `buildHtml` | export route | ACCEPT |
| Receipt helper sends only a source excerpt | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` | lines 64-94 | `fetchGovernanceReceipt` | receipt helper | ACCEPT |

External Web input is advisory; Local source verification above controls this packet. No full-corpus or runtime proof is claimed.

## Decision / Baseline / Proposed Tranche

The worker may repair the component and its focused test only. At submit, preserve the full request snapshot and a local attempt identity. Present result, receipt, preview and output actions as belonging to that submitted version. If current form fields differ, make the stale-version state explicit while preserving the previous result. A later/superseded response must not replace a newer attempt's result. A failed attempt must not silently erase a valid prior result. An `initialResult` without request provenance must not be described as matching the current form.

The implementation may choose a simple local comparison/attempt strategy. It must not imply that the server's `sourceHash` is an exact rendered-artifact hash. Do not change route, proof helper, persistence, schema, auth, acceptance, or ledger owners in B1.

## Scope / Target / Owner Boundary

Allowed worker edits: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` and `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.test.tsx`. The worker may create `docs/reviews/CVF_CVF_NCR_HTML_B1_VERSION_BINDING_WORKER_RETURN_2026-09-30.md`. All other paths are read-only. Local reviewer owns acceptance, commit and continuity. If the focused test reveals a necessary API/caller contract change, return a blocked dependency rather than widening the manifest.

## Acceptance Criteria

1. Editing title or claim boundary while source content stays identical makes the prior HTML version unmistakable; preview and actions refer to that prior version.
2. Editing any request field during a pending request cannot cause its later response or receipt to be presented as the edited form's output.
3. Superseded or out-of-order responses cannot overwrite the selected newer attempt; errors remain attached to the correct attempt.
4. Initial result provenance is explicit or conservatively unknown. Current draft and receipt language remains truthful in English and Vietnamese.
5. Focused component tests cover the cases above and copy/download/print where the relevant browser API is mockable; TypeScript and the worker-return fast gate pass without network or live calls.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | `ArtifactExportPanel` through existing Web consumer | One local UI component; no artifact acceptance authority | Component and focused test source above | No new adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | No CLI/MCP export surface in this tranche | No external ingress, raw data, receipt or mutation grant | D034 chooses existing Web route only | External adapter deferred; B1 adds none | DEFERRED_WITH_REASON |

## Evidence / Verification

Worker captures `executionBaseHead`, exact changed files, focused Vitest result, TypeScript result, and worker-return fast gate. Local reviews the behavior and performs one distinct targeted probe only if the returned evidence leaves a named contradiction. Pre-dispatch and pre-implementation gates bind the packet and execution frontier; pre-closure applies after Local commit and continuity sync. Gate PASS alone does not prove a live UI or provider behavior.

## Operator Checkpoints

Q001/R0 remains Profile A without effect. The operator retains real ledger source/copy, backup/key custody, retention, RPO/RTO, P08, cost, artifact acceptance, pilot/live, public sync and deployment decisions. B1 does not resolve those questions.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind web-ui-dashboard --batch-id CVF-NCR-HTML-B1-VERSION-BINDING --title "HTML B1 Version Binding" --date 2026-09-30 --base 44542a063 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | web-ui-dashboard and no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | source-backed B1 scope and version-binding acceptance invariants |
| checkerReadAheadConfirmation | dispatch, release, acceptance-ledger, closeability, envelope and structural checker sources |
| docOnlyNewFields | N/A with reason: no new governed field schema |
| claimBoundary | Authoring aid only; no implementation proof |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_dispatch_prompt_envelope.py` |
| literalTokensReviewed | dispatch status, source ACCEPT rows, first-section envelope, acceptance ledger, closeability graph, worker-return fast gate |
| gateRunPurpose | Confirm source-backed packet structure, not discover the HTML behavior |
| claimBoundary | Static checker read-ahead cannot grant execution or runtime proof |

## Claim Boundary

This baseline selects only the B1 component repair. It does not prove the UI after implementation, accept an artifact, or change Q001/R0 and P11.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
