# CVF GC-018 Baseline - NCR HTML B2b Synthetic Byte Boundary

Memory class: governed-dispatch-baseline

docType: gc018

Status: DISPATCH_READY

Batch ID: CVF-NCR-HTML-B2B-SYNTHETIC-BYTE-BOUNDARY

Dispatch base head: `e9395fb68`

Commit mode: `WORKER_MUST_NOT_COMMIT`

Decision owner: Local technical reviewer; operator owns real-data and effect checkpoints.

Worker target: shared-workspace `INTERNAL_AGENT`.

## Purpose

Authorize an isolated synthetic handoff from a decoded HTML string to owned UTF-8 bytes, using the B2a identity algorithm. This does not connect to the export route, browser UI or a durable artifact store.

## Source / Predecessor Evidence

The operator approved synthetic proof first with Profile A retained. B2a was Local-accepted bounded at `ea90e0e2a`. D040 and the Local byte-transport audit at `49495b2b9` identify the missing string-to-byte custody boundary; the Q001/Q004 effect and store decisions remain open.

| Claimed item | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|
| D040 allows synthetic B2b packet, not an active acceptance path | `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md` | D039-D040, Q001, Q004 | B2b | NCR roadmap | ACCEPT |
| Export route returns transient HTML and sourceHash covers source text only | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` | buildHtml and POST | html, sourceHash | HTML export route | ACCEPT |
| Panel parses JSON and makes a Blob from displayed HTML string | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` | `handleGenerate`, `downloadHtml` | `response.json`, `Blob([html])` | Web consumer, read-only context | ACCEPT |
| B2a already hashes UTF-8 bytes of a supplied string and rejects lone surrogates | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.ts` | `utf8Bytes`, `computeHtmlBytesIdentity` | B2a identity | pure helper | ACCEPT |
| Local audit separates JSON wire bytes from the decoded HTML artifact bytes | `docs/reviews/CVF_CVF_NCR_HTML_B2_BYTE_TRANSPORT_AUDIT_2026-09-30.md` | Findings and Decision | B2 transport boundary | Local audit | ACCEPT |

## Decision / Baseline / Proposed Tranche

B2b is a pure, unconnected byte-handoff module. Its input is the exact decoded HTML string. It must reject invalid Unicode rather than replace it, encode without trimming, newline conversion, BOM insertion or removal, or Unicode normalization, make a defensive owned byte copy, and bind length/digest using the existing B2a identity. Verification must compare the actual handed-off byte array with the declared identity and fail closed on length or hash mismatch. No new identity algorithm, acceptance state or receipt interpretation is introduced.

The reference contract must name the byte owner, encode-once and copy-on-transfer rules, and distinguish JSON envelope bytes, decoded HTML string, candidate bytes, Blob bytes and rendered DOM. It may refer to the B2a future store proposal but must not ratify or repeat its undecided store policy.

## Scope / Target / Owner Boundary

Allowed worker paths: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-byte-handoff.ts`; its adjacent `html-artifact-byte-handoff.test.ts`; `docs/reference/CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_2026-09-30.md`; and `docs/reviews/CVF_CVF_NCR_HTML_B2B_SYNTHETIC_BYTE_BOUNDARY_WORKER_RETURN_2026-09-30.md`. All are create paths. The module may import the existing B2a helper but no route, page or production composition root may import B2b. Local owns review, commits and continuity.

## Acceptance Criteria

1. A decoded synthetic HTML string produces a defensively owned UTF-8 byte array; its digest and byte length agree with B2a identity and an independently computed test oracle.
2. JSON serialize/parse and an in-memory Blob roundtrip preserve the expected artifact bytes under tests, while JSON envelope bytes are explicitly excluded from identity.
3. Same-byte-length mutation, Unicode normalization difference, CRLF/LF change, BOM insertion, malformed Unicode and post-handoff byte mutation are discriminating negative cases.
4. Verification consumes actual bytes and rejects mismatch without silently re-encoding from a source string. State remains `DRAFT_UNACCEPTED` if a candidate is included.
5. Only four allowed paths change; focused tests, TypeScript and worker-return fast gate pass without route, database, provider, network or real data access.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| `INTERNAL_AGENT` | isolated B2b handoff helper and reference contract | synthetic byte boundary only; no active accept effect | source rows above and pending tests | no active adapter | CONTRACT_ONLY |
| `EXTERNAL_AGENT_CLI_MCP` | no external B2b interface | no ingress, auth, raw data, receipt or mutation grant | NCR D040 and bounded packet scope | external adapter deferred | DEFERRED_WITH_REASON |

## Evidence / Verification

Capture executionBaseHead, initial/final status, exact changed set, focused Vitest, TypeScript and worker-return fast gate. Reviewer verifies no active B2b import and independently checks one same-length byte mutation against the handed-off array. Tests prove only an in-memory handoff, not network wire bytes, saved file, disk durability, browser UI or live governance behavior.

## Operator Checkpoints

Profile A remains. Operator retains designation of the actual accepting actor/account, source/instance and classification of real data, store location, writer/fencing model, backup location and key custody, retention/deletion, RPO/RTO, cost and pilot/live effect. A separate work order is required for durable store or active acceptance.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`work_order_authoring`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Command: `python governance/compat/run_adif_defect_resolver.py --task-class work_order_authoring --role dispatcher --lifecycle-phase pre-dispatch --json`; 0 items, `truncated=false`.

Returned defects: NONE_RETURNED

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B2B-SYNTHETIC-BYTE-BOUNDARY --title "NCR HTML B2b Synthetic Byte Boundary" --date 2026-09-30 --base e9395fb68 --commit-mode WORKER_MUST_NOT_COMMIT --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --stdout` |
| generatedProfile | generic-worker-dispatch and no-commit worker profile, previewed to stdout |
| generatedSkeletonStatus | GENERATED_BUT_REPLACED |
| manualEditsAfterScaffold | source-backed B2b byte handoff and synthetic-only scope |
| checkerReadAheadConfirmation | dispatch, acceptance-ledger, closeability, structural, release and high-risk local transaction checker sources |
| docOnlyNewFields | N/A with reason: no new governed field schema |
| claimBoundary | Scaffold is authoring aid only |

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_work_order_acceptance_ledger.py`; `governance/compat/check_dispatch_release_readiness.py`; `governance/compat/check_gate_to_role_closeability.py`; `governance/compat/check_governed_artifact_checker_read_ahead.py`; `governance/compat/check_high_risk_local_transaction_proof.py` |
| literalTokensReviewed | DISPATCH_READY; source ACCEPT rows; worker-return gate; exact four-path scope; no durable transaction authority |
| gateRunPurpose | Confirm packet structure and authority after source review |
| claimBoundary | Static gate PASS cannot prove B2 runtime behavior |

## Claim Boundary

This baseline authorizes an isolated synthetic byte handoff and contract only. It does not accept HTML, persist bytes, grant production writer rights, close Q001/Q004, or authorize real data, provider/live, public sync or deployment.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
