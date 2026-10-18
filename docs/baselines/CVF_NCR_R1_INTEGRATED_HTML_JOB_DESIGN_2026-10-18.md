# NCR R1 Integrated HTML Job - Design And Source Packet

Memory class: governed-source-design
docType: baseline
Status: DESIGN_COMPLETE_EXECUTION_HELD
Date: 2026-10-18
Batch ID: CVF-NCR-R1-INTEGRATED-DESIGN-20261018

## Purpose

Lock one concrete artifacts-domain design for the existing Work Transfer consumer: goal/job and exact HTML version join, local Stop, unknown Save reconciliation and explicit person review. This is the finite PLAN outcome requested by the current roadmap. It is not a released implementation work order.

## Scope / Target / Owner Boundary

Role=INTERNAL_AGENT Local dispatcher/reviewer; phase=PLAN; decision owner=LOCAL. The operator's next and standing autonomous roadmap instruction admit this design. Two internal read-only aides supplied source design and progression advice; Local selected the disposition below. No product source, test, running app, browser, provider, real-data or public effect is released here.

The payload owner remains the existing artifacts domain. Keep the immutable DraftSnapshot v1 format and its CLIENT_SUBMITTED_UNVERIFIED/DRAFT_UNACCEPTED labels. Store only small metadata sidecars beside it; do not add another raw HTML store, generic job engine, dispatcher or parallel approval page. R1/R2 remain partial, R3/R4 open and R5/R6 deferred. Parent gen9/SCEC2/counters2,0,2,0/blockers2/freeze/prior7/LHW24 and spent actors remain intact.

## Source / Predecessor Evidence

Source base: 1e1e004c7db9acce879341ec5acbaf6269885be2; clean start. Root planning owner: docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md, R1 Integrated HTML Job Contract, material c49e0682cc7b771847ef46e4402ed011a8c1cbbd. Existing browser recovery evidence is limited to its recorded source revisions and joined assertions; both original overall browser tests remain FAIL. No new clean browser PASS is inferred.

Targeted symbol reads, including the internal source aide; no corpus census or all-files-read claim. File pins are pre-implementation raw SHA256:

| Concern | Current owner / symbol | Raw SHA256 |
| --- | --- | --- |
| selected source | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx` - recordToExportRequest; selectedRecord | 469bab1358bb65eef69e730a2203404ac6eddb8ffcbfad57edde750d35d23b0d |
| frozen displayed build | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx` - DisplayedResult; handleGenerate; inFlightRequests | c3e0b768f444fc452c6cd72815ef13b27ca8ac24e1506698123732a71152f625 |
| pending Save | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlDraftRecovery.tsx` - knownSave; save; reconcile; restore | 8bb93c9f037a6893083b8715495994d6523ee09366e47a9bd258f69a2c3e9964 |
| snapshot identity | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-draft-recovery-contract.ts` - parseDraftInput; requestIdentity; validateSnapshot | 89782c054e3e242b0d398ef37c1d4887f0763a97d730734cd45f05270c9185f0 |
| artifacts storage | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-snapshot-store.ts` - HtmlDraftSnapshotStore; directory; save; get | 9d7bbc8f73418d64520485d06cf5f5861d1663d7d6b85817c34f9b690e943b3b |
| normal session boundary | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-recovery-api.ts` - normalPrincipal; draftRouteHandlers | c5399e838b6c195423912f7ae33da4f352f94c66958c8aeccb29fe3bdeaf4d88 |
| profile owner | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-synthetic-profile.ts` - resolveHtmlDraftSyntheticProfile | dcb8cdd8a98f49f345b53c9ea9d824b11785f0a12854023b545cc34cdfe3a23b |
| export and egress | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts` - POST; fetchGovernanceReceipt | a17ddd57882be1e58a86fb1d86bea8a2693f1169f5ba0c8b6da2af75d7f024ae |
| receipt destination | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts` - resolveEvaluateUrl; fetchGovernanceReceipt | fbdcc3a434eea13842c9f692d2b54cc9955e80d8c8777d9dfaa14cace9cdfcaf |
| pure identity reference | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-artifact-acceptance-candidate.ts` - createHtmlArtifactCandidate; computeHtmlBytesIdentity | 95372cfb6b21e27e5dd76e7a24c135474299a022bd67cdc4b062fc2cca90ce0f |
| separate SPEC acceptance | `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-spec-acceptance.ts` - prepareIntentSpecAcceptance | b4c452663440bf74cc11833462e3c10ea43e29a2fe156b3d3c9cdef00fc79c12 |

## Current Runtime Freshness Verification

Fresh source inspection is pinned to 1e1e004c7db9acce879341ec5acbaf6269885be2 and the named raw hashes above. The observed absence concerns only those selected source interfaces; no app/provider run or current-revision executable behavior proof was performed. Historical recovery assertions and both overall FAILs retain their original source/evidence scope. New fields and paths are DOC_ONLY_NEW.

## Decision / Baseline

DESIGN_COMPLETE_EXECUTION_HELD. The source design below is locked for future admission. Canonical feasibility supports only a STOP/NO_SUCCESSOR same-problem candidate. Do not issue an implementation worker or promote a documentary check to an execution grant. A new INITIAL key, renamed objective or Review Cost continuation declaration cannot reset the recovery chain.

Local reassessment: the existing renderer and immutable snapshot repository are suitable for their bounded payload roles. The missing responsibility is the cross-action job/version/decision join. Metadata sidecars within that domain are the chosen smallest extension. The remaining admission conflict is canonical progression, not evidence that another payload backend or broader runtime is necessary. Do not reopen completed six-path maintenance or repeat this design merely to accumulate tranches.

## Requirements / Job And Version Model

All following names and DTOs are DOC_ONLY_NEW. UUIDs use the existing canonical UUID predicate; source records use SOURCE_ID and the server's ncr-synthetic- prefix. Reject unknown keys, invalid Unicode, secret-like values and over-limit bodies. JSON requests are at most280000 bytes; persisted metadata is at most16384 bytes. Hashes are lowercase64-hex, timestamps canonical UTC ISO.

1. Create an immutable job before Build. The client assigns jobId once, before POST, so a lost acknowledgement can be reconciled by GET without a duplicate create. Job input is jobId, sourceRecordId, goal (1..2000chars), criteria (1..8 exact objects {criterionId,text}; unique criterionId matches ^[a-z0-9][a-z0-9_-]{0,31}$; text1..500chars), expectedOutput=HTML, allowedEffects (the fixed ordered set LOCAL_HTML_BUILD, LOCAL_DRAFT_SAVE, LOCAL_SYNTHETIC_REVIEW), and the frozen existing seven-field request. Server validates the request and stores its requestSha256, not a duplicate source payload. No client actor, owner, timestamp or hash is accepted.
2. Job record exact fields: schema=cvf.htmlJob.v1, jobId, owner (server userId/orgId/teamId), sourceRecordId, goal, criteria, expectedOutput, allowedEffects, requestSha256, createdAt, expiresAt. Synthetic expiry is createdAt+24h; it is not production retention. Editing request, source, goal or criteria invalidates the local current job and requires a new explicit job target. It never mutates an old job.
3. A successful Build freezes its job reference with the existing submitted request and result. A Save uses that displayed pair; current form values never rewrite it. An old version can be reviewed only by explicitly reopening its original job and criteria. It must not appear accepted for the edited current goal. Server can validate immutable job/version identity; it cannot observe unsent form edits and must not claim a global latest version.
4. Version-link input: jobId, sourceRecordId, versionId. The server reads the owner-bound unexpired job and snapshot, recomputes snapshot hashes and requires snapshot.requestSha256=job.requestSha256. Record exact fields: schema=cvf.htmlJobVersion.v1, jobId, owner, sourceRecordId, versionId, requestSha256, htmlSha256, createdAt, expiresAt=min(job expiry,snapshot expiry). No supplied hash, receipt or source-text hash replaces these checks.
5. Save acknowledgement loss retains the same versionId. Recovery first GETs the exact snapshot; a successful read permits linking the same saved version. Link loss is reconciled by exact-link GET; a confirmed absent link may be explicitly created with the same pair, never a new Save or export. There is no cross-file transaction or exactly-once job-execution claim.

## Requirements / Separate Person Decision

Acceptance input exact fields: decisionId (client UUID fixed before send), jobId, sourceRecordId, versionId, requestSha256, htmlSha256, criteriaReview (one exact row per job criterion: criterionId, passed=true and reviewNote1..1000chars), reviewedVersionConfirmed=true. These are explicit review attestations and expected identities, not trusted technical provenance. Unknown fields, owner, acceptance state or timestamp supplied by a client are rejected. Review notes are inspectable person assertions, not independently verified evidence. Identity evidence pointers are server-derived from the joined job, version link, snapshot and complete criteria-review rows.

Server requires the existing normal unexpired admin session with complete owner IDs, allowBreakGlass=false, no impersonation, same origin and the separate selected synthetic writer profile. Only the authenticated owning user may record the review in this slice; no new RBAC role or delegate is inferred. Read the job, version link and saved snapshot again; validate all owner/record/version joins and both expected hashes; require every criterion exactly once and explicit reviewed-version confirmation. Revalidate original snapshot integrity and expiry at the decision boundary.

Decision record exact fields: schema=cvf.htmlJobDecision.v1, decisionId, jobId, owner, actor (server userId/orgId/teamId), sourceRecordId, versionId, requestSha256, htmlSha256, criteriaReview, evidence (jobId/versionId plus validated request and HTML hashes), decision=ACCEPT_FOR_LOCAL_SYNTHETIC_REVIEW, decidedAt (server), expiresAt=min(job,link,snapshot expiry). This records a person's synthetic review for an exact version. It does not verify generation provenance, satisfy production business acceptance, trust receipt ALLOW or promote client-submitted bytes to trusted governance evidence.

Only one positive decision record per job/version is selected; no revocation or overwrite API in this slice. A duplicate or conflicting write returns409, followed by exact decision GET. Unknown write outcome never displays accepted or creates a fresh decisionId. UI displays a decision only after successful server commit/readback or a matching authenticated GET. The original draft stays unverified/unaccepted; render its trust label next to the separate synthetic review result.

## Requirements / Storage And API

Extend HtmlDraftSnapshotStore at its existing validated owner namespace; keep directory private and share its root/symlink/owner guards. Use job-<jobId>.json, version-<versionId>-job.json and job-<jobId>-decision-<versionId>.json. The version-keyed exclusive link permits exactly one job association per saved version; body jobId must match every GET and decision. A saved version cannot be silently reattached to a different goal. Existing draft listing ignores these non-UUID filenames. Use exclusive wx creation, bounded strict read/validation and exact readback. Every read checks filename-to-body identity, owner, schema, limits, joins and expiry. No update, delete, overwrite or scan-based accepted-state inference. A failed/partial write consumes its ID and stays unconfirmed; do not overwrite it. No host-crash durability claim follows from file fsync alone.

Use one /api/artifacts/jobs GET/POST route with a small server factory; avoid three route families for this finite consumer. POST is a strict discriminated union:

| action | Body in addition to action | Success |
|---|---|---|
| CREATE_JOB | immutable job input above | 201 with read-back job |
| LINK_VERSION | jobId/sourceRecordId/versionId | 201 with read-back version link |
| ACCEPT_VERSION | exact acceptance input above | 201 with read-back decision |

Authenticated GET kind=capabilities accepts only that one query key and returns the selected synthetic writer/effect boundary, or503 when disabled; no source payload or configuration secret. The existing page keeps its current non-job flow when that profile is unavailable; job controls appear only after explicit server capability admission. GET query kind=job requires jobId+sourceRecordId; kind=version adds versionId; kind=decision adds versionId+decisionId. Reject extras/duplicate keys. Authenticated wrong owner, absent/expired/mismatched object returns404; invalid input422, origin/session refusal403, unsupported content415, too large413, collision409, disabled/unavailable/unconfirmed503. All replies and forwarded auth responses are no-store. Do not return an empty successful result for an unavailable decision read.

Job writes require resolveHtmlDraftSyntheticProfile plus the additional server flag CVF_NCR_HTML_JOB_PROFILE=LOCAL_SYNTHETIC. Extend the internal profile type with explicit jobDecisions=true; default existing draft profile cannot invoke new metadata writer methods. NODE_ENV=production always refuses. No request field, query or header can enable the profile. Reuse the validated absolute non-root/non-UNC fixture root and marker; require synthetic source prefix at every action. This explicit source profile is not a grant to launch or spend an old actor.

The export route must detect the selected server job profile and return NOT_CONFIGURED/DRAFT_UNACCEPTED without calling fetchGovernanceReceipt or reading CVF_SERVICE_TOKEN. Outside that selected profile, preserve the current export behavior. A client header cannot suppress a required receipt. UI describes local synthetic Build, zero receipt hop in that profile and local Stop's unknown remote/cost boundary; general configured egress remains outside this slice's effect authority.

## Requirements / Stop And Recovery UI

Extract the Build attempt controller from ArtifactExportPanel (944lines at the source pin) into useHtmlBuildAttempts; leave the edited panel below975lines and target a net shrink. Own one AbortController and publication token per exact attempt, including asynchronous job creation. Stop synchronously invalidates that token and marks locally stopped before abort; late success/error/onGenerated must not publish. finally only clears matching attempt state. Keep the duplicate-request lock until that fetch settles locally; settlement is not remote completion. During async job creation, Stop may leave an unlinked job or unknown create; it must prevent export after its token is invalidated. An identical frozen request stays blocked in this component session after a stopped export with unknown remote outcome; there is no explicit override in this slice. A changed request can start a fresh explicit Build/job target with the earlier unknown outcome disclosed. Reload does not prove remote completion and is never offered as a retry workaround. No automatic retry, late old-result publication or whole-job cancellation claim. Dispose on unmount/selection/session change. Do not import Node crypto into a client runtime.

HtmlJobControls composes the existing panel and recovery companion; no separate dashboard. Display goal, criteria, scoped job/version IDs and separate operation, persistence and decision states. Save and review target the frozen displayed version or an explicitly restored saved version. Keep stale/unsaved/unknown visibly distinct. The acceptance action names local synthetic review and requires explicit criterion confirmation; never a generic completed badge.

Use sessionStorage only for a bounded same-tab pending-ID journal: schema, owner IDs, sourceRecordId, jobId, versionId, optional decisionId and operation; no HTML, source text, cookies or tokens. Journal before a write; do not overwrite an unresolved operation with another write or a new ID. Storage failure holds that write; malformed or wrong-scope journal is discarded without effect. Session/owner/record changes clear visible data and invalidate async epochs; expired sessions prohibit reads/writes. A reloaded journal is untrusted: authenticate and GET the exact server objects before display or review; it cannot trigger POST, Build or automatic acceptance. A lost journal honestly loses unknown-write recovery; manual IDs can only cause GET. Session storage is not durable whole-job resume or an access-control boundary.

## Proposed Source Manifest - Unreleased

The following exact11 source paths are the chosen future candidate, not current write permission. Existing snapshot schema and separate SPEC acceptance owner are excluded from mutation.

| Path (all under cvf-web/src) | Disposition | Required change |
| --- | --- | --- |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/page.tsx | existing | render the integrated controls for the selected audit source |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx | existing | extract attempt controller; freeze optional job reference with submitted result; Stop control |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/useHtmlBuildAttempts.ts | new | exact-attempt AbortController and publication-token lifecycle |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlDraftRecovery.tsx | existing | scoped pending-ID journal and GET reconciliation; attach exact saved version to its job |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlJobControls.tsx | new | goal/criteria, create-job pre-Build callback and explicit saved-version review companion |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-job-contract.ts | new | bounded DTOs and server-side exact record validation; type-only client imports |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-snapshot-store.ts | existing | same artifacts namespace: immutable job, version-link and decision sidecars; snapshot schema intact |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-job-api.ts | new | strict action DTOs; session, origin, profile, identity and criteria enforcement |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-job-synthetic-profile.ts | new | additional explicit synthetic job-writer opt-in over existing validated draft root |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/jobs/route.ts | new | thin GET/POST exports resolving server profile |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts | existing | selected synthetic job profile bypasses receipt hop before token access; no client-selected bypass |

## Proposed Proof And Registry Manifest - Unreleased

No tests are added or executed by this design task. These exact9 focused test paths are the candidate proof dependencies for a later explicitly admitted verification scope:

- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.job.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlDraftRecovery.job.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlJobControls.test.tsx`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-job-contract.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-snapshot-store.job.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-job-api.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-job-synthetic-profile.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/job-profile.test.ts`
- `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/(dashboard)/work-transfer/job.test.tsx`

Dispatcher-owned future requirement/proof mapping: JOIN (job/request/version/edit/owner), STOP (late success/error/unmount and unknown remote), SAVE (lost acknowledgement/reload/journal unavailable, no duplicate POST), DECISION (foreign/stale/mismatched hashes/incomplete criteria/unknown write), PROFILE (default/production OFF, no request opt-in and no receipt/token hop), TRUST (ALLOW/download/Save without person decision remains unaccepted), RETURN (exact manifest, type/scoped lint, original outcomes and final-byte machine evidence). Positive claims require actual evidence at the implemented source revision; no source review substitutes for executable behavior proof.

Candidate registry dependencies, if a new proof artifact is later registered: docs/corpus-intelligence/registry/entries/cvf-ncr-r1-integrated-html-job-test.json and its generated docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json and docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md. Change source item then regenerate; never hand-edit the aggregates. No registry is changed by this documentary task.

Candidate worker return/proof: docs/reviews/CVF_NCR_R1_INTEGRATED_HTML_JOB_WORKER_RETURN_2026-10-18.md and docs/reviews/evidence/ncr-r1-integrated-html-job-worker-20261018.json. A future work order must enumerate these with the source/test/registry union and the dispatcher-owned acceptance ledger. Root owns admission baseline/work order, roadmap and current6 separately. A real-app/browser harness is not included: it needs its own finite future scope, fresh source pins, effect ceiling, isolation/teardown and independent oracle. Existing spent actor budgets are not transferable.

## Prospective Canonical Progression - Not An Execution Release

This single active object is the actual candidate evaluated by the canonical checker, not an example or a new INITIAL chain. Its predecessor is the hash-bound accepted completion. It evaluates the proposed next same-problem transition only; the historical child remains ordinal1/ROOT_CONTRACT_REQUIRED/NO_SUCCESSOR and its bytes are untouched. Prior=[] means every possible current blocker set is non-decreasing; the streak necessarily becomes2. STOP_REASSESS_ARCHITECTURE/NO_SUCCESSOR is the feasible documentary disposition, not source readiness. No READY_WITH_EXECUTABLE_PROOF assertion is made.

```json
{
  "schemaVersion": "cvf.semanticConvergenceControl.v1",
  "problemKey": "ncr-html-draft-refresh-recovery",
  "chainMode": "SUCCESSOR",
  "chainOrdinal": 2,
  "predecessor": {
    "path": "docs/reviews/CVF_NCR_HTML_DRAFT_RECOVERY_BROWSER_COMPLETION_2026-10-18.md",
    "sha256": "756c64da7af786cf8c220f6d60474d7334710707c051da2f96d0375bb01eac7b"
  },
  "blockerDelta": {
    "prior": [],
    "resolved": [],
    "retained": [],
    "new": [],
    "reopened": [],
    "current": []
  },
  "resolutionEvidence": {},
  "counters": {
    "partialReadyClosures": 0,
    "reviewerScopeExpansions": 1,
    "sameClaimCorrections": 0,
    "nonDecreasingBlockerTransitions": 2
  },
  "claims": [],
  "requiredDisposition": "STOP_REASSESS_ARCHITECTURE",
  "successorScope": "NO_SUCCESSOR"
}
```

## Evidence / Verification

Run diagnose_file on this exact baseline using governance/compat/check_semantic_convergence_control.py repository hash/block/evidence resolvers; retain .cvf/runtime/ncr-r1-integrated-design-20261018/feasibility.json. Observed: diagnose_file evaluated this single baseline object; STOP candidate valid, non-stop candidate rejected with MISSING_STOP_REASSESS_ESCALATION and PREDECESSOR_ESCALATION_DROPPED. The normal changed-range checker also evaluated1 active object and passed. These are declaration checks, not implementation admission. Also run the normal changed-range checker so an evaluated-object count of1 is visible. Compare the same candidate with CONTINUE_BOUNDED and INTEGRATED_ROOT_CONTRACT as a diagnostic negative candidate; it must fail the mandatory stop. This is declared-state verification, not a product test, provider proof, consent or implementation grant.

The final internal semantic review found two holes: many-to-many job linking and criterion attestations without an inspectable basis. Local consolidated both into this version-keyed exclusive link and bounded review-note design; Stop during job-create and default-flow capability admission were clarified together. No implementation or product-proof claim follows. Consume valid historical source/evidence and the two internal source reviews. No duplicate browser run or per-row evidence recreation. Before any release, Local must resolve an admissible canonical architecture disposition at the existing SCEC owner; do not rerun this packet, reset counters or open a renamed recovery child. The finite design outcome ends with the actual feasibility result and current continuity synchronized. Initial reviewer-fast failed two documentary checks: missing named source-freshness section and handoff Current Mode literal. Local corrected both together; original reviewer-fast.log remains FAIL. No product proof was rerun. The initial commit shape plan also refused the mixed batch because authorization lacked the exact manifest and rollback labels; Local corrected the labels within the granted exact8 scope. Initial material-plan.log remains FAIL. The first normal commit was refused by corpus and knowledge-block literal shape; Local supplied the exact N/A verdict syntax and zero-asset reconciliation. Original material-commit-initial.log remains FAIL; product proof was not replayed.

## Canonical Owner Change Proposal - Explicit Approval Required

Disposition: PREPARED_PENDING_OPERATOR_SCOPE; proposal date2026-10-18, source HEAD 4228c115ac1110c6bb7951c47a8976ef236cfb83. This section resolves the next Local owner decision as far as current authority permits. The existing source design and its exact11 source/exact9 test candidates are complete; do not repeat them. No canonical rule, checker, helper, test, product source or active effect has been changed by preparing this proposal.

### Why this decision requires the operator

The current SCEC rule intentionally requires STOP after two non-decreasing transitions, including empty-to-empty, and forbids successors after an actual STOP. Its current owner supplies no opt-in admission for a completed root reassessment. Neither another documentary acceptance nor the Review Cost continuation declaration changes this. Local cannot repair the absence by resetting counters, using a new INITIAL key or pretending that the integrated recovery problem is unrelated.

GC-049, governance/toolkit/05_OPERATION/CVF_CORE_GUARD_SELF_PROTECTION_GUARD.md, Rule and Final Clause, freezes protected machinery by default and requires an explicit, bounded, reviewable authorization before it is touched. The operator's autonomous roadmap/PLAN direction permits this proposal and documentary continuity; it does not explicitly approve changing the escalation invariant. The completed six-path Review Cost maintenance is a different scope and stays closed. The source and canonical-progression aides independently reviewed this boundary; final decision owner=LOCAL.

### Exact proposed four-path owner scope

- `docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md`
- `governance/compat/check_semantic_convergence_control.py`
- `governance/compat/semantic_convergence_root_admission.py`
- `governance/compat/test_semantic_convergence_root_admission.py`

| Path role | Concrete change after approval |
|---|---|
| SCEC standard | Add a versioned, forward-only root-contract admission exception to invariant6 and explain its interaction with ROOT_CONTRACT_REQUIRED/NO_SUCCESSOR. Preserve the absolute actual-STOP predecessor prohibition. |
| Existing checker | Thread actual artifact path and existing repository evidence resolvers through a narrowly declared opt-in; preserve all ordinary chain/hash/blocker/counter/proof checks. Extract its current escalation function into the helper so the edited974line checker shrinks by at least50lines and stays below975. Preserve its public validation entrypoints and default results. |
| New helper | Validate only the strict hash-bound admission contract and shared escalation predicates; no runtime, dispatcher, new SCEC chain mode or general authorization framework. |
| New focused test | Cover positive bounded dispatch/return and negative/default/forgery/replay cases below. Existing SCEC tests are consumed and rerun under the approved focused verification scope; their source is outside the write manifest. |

No hook, autorun catalog, scaffold producer, Review Cost owner/checker, threshold, old fixture, old artifact or retired actor is changed. The guard-maintenance tranche ends with its owner/test result, current continuity and committed-range closure; it does not itself execute the R1 product package.

### Concrete admission rule to implement after approval

1. Keep schema cvf.semanticConvergenceControl.v1, stable problemKey, SUCCESSOR, ordinal+1, exact predecessor SHA, normal blocker reconciliation and all counters. Add one optional strict rootContractAdmission pointer with schemaVersion=cvf.scecRootContractAdmissionPointer@1.0.0, path, sha256 and stage (DISPATCH or RETURN). All absent preserves current behavior. A present partial/duplicate/malformed/unverifiable pointer fails closed and never falls back to ordinary mode. No counter is reset; the selected empty-to-empty streaks remain2 at dispatch and3 at return.
2. Pointer path names an existing non-archive UTF8 Markdown baseline or review outside worker write scope, at most65536bytes, with exactly one strict root-contract-admission-json object. Reject duplicate JSON keys, unsafe paths, invalid hashes and inconsistent types. Resolve bytes/hash from the repository, not packet-controlled roots; retain one byte snapshot for hash and object parsing. A parser PASS establishes declared bindings only; Local still verifies actual operator authority and semantic truth.
3. Admission object exact fields: schemaVersion=cvf.scecRootContractAdmission@1.0.0, status=ACCEPTED_FOR_BOUNDED_SOURCE_IMPLEMENTATION, decisionOwner=LOCAL, operatorInstructionEvidence, problemKey, predecessor (path/sha256), sourceContract (path/sha256), workOrderPath, workerReturnPath, allowedArtifacts, effectCeilings and expiresAtUtc. The source contract and grant are outside allowedArtifacts; workOrderPath and workerReturnPath are distinct normalized governed paths. allowedArtifacts is the exact union of the future work order's valid acceptance-ledger expectedArtifacts. Compare real artifact paths, not a self-declared filename. Expiry uses current UTC; no packet clock. No self-reference, archive, traversal, symlink escape, worker-writable grant or missing source hash passes.
4. effectCeilings has exactly providerCalls, networkCalls, publicWrites, deployments, realDataMutations, destructiveActions and productRuntimeStarts, all strict integer0. Source and isolated in-process fixture verification are the only admissible effects. Production is excluded. Old actor/effect budgets cannot be reused; normal work-order role/budget/source/gate checks still control. A future running-app/browser/provider tranche requires its own authority and cannot use this admission.
5. DISPATCH is allowed only at the bound workOrderPath, directly after the bound actual ROOT_CONTRACT_REQUIRED predecessor with empty prior/current blockers. The declared source contract must include the consolidated root reassessment. Require ROOT_CONTRACT_REQUIRED/INTEGRATED_ROOT_CONTRACT, no runtime-readiness assertion and no INITIAL or renamed problem. The narrow exception permits that one integrated source dispatch despite the unchanged non-decreasing streak; it explicitly supersedes that predecessor's documentary NO_SUCCESSOR only for the bound pair. It never follows an actual STOP_REASSESS_ARCHITECTURE predecessor.
6. RETURN is allowed only at the bound workerReturnPath, immediately after that bound work order and the same pinned admission. Keep ordinal and counters monotonic, empty blockers, and require READY_WITH_EXECUTABLE_PROOF/EXECUTABLE_IMPLEMENTATION with the existing nonempty claim-to-proof mapping and no documentation-only readiness. Scope readiness to actual source/fixture assertions; no app/provider/business acceptance or whole-R1 exit is inferred. An unsuccessful worker can return the ordinary STOP_REASSESS_ARCHITECTURE/NO_SUCCESSOR disposition without the opt-in; failure does not acquire a fresh attempt or successor budget.
7. This admission is exhausted by that exact dispatch/return pair. A new path, another ordinal, a different predecessor/grant/manifest, active blockers, unbound reassessment, or any actual STOP predecessor cannot reuse it. Existing defaults and historical blocks retain their original interpretation. Existing STOP candidates in this design remain prospective historical declarations; the new source work order would bind the actual ordinal1 child rather than pretending that an actual STOP chain continued.

### Required focused verification after approval

| Case | Required result |
|---|---|
| No admission; ordinary empty-to-empty ordinal2 | Existing mandatory STOP remains enforced. |
| Bound direct ROOT dispatch then exact immediate proof return | Accepted declared scope, preserved problem/ordinals/counters; no pre-proof READY. |
| Actual STOP predecessor, new INITIAL, narrow scope or active blockers | Reject; no exception. |
| Missing/malformed/partial/duplicate/wrong-stage pointer or grant | Reject; no fallback. |
| Wrong raw hash/source contract/owner/manifest/real artifact path/expiry | Reject. |
| Worker-writable/self-referential/unsafe/oversized/non-UTF8 grant | Reject. |
| Nonzero/bool effects, undocumented proof or fake readiness | Reject. |
| Reuse after the bound pair or different work-order/return path | Reject. |
| Existing SCEC regression suite and untouched legacy artifacts | Existing expected verdicts retained; no historical counter migration. |
| Actual R1 prospective dispatch/return objects | Evaluate both objects with canonical repository resolvers before product dispatch; zero evaluated objects is not admission. |

No tests for the proposed machinery have been added or run before approval. No evidence claims the proposed exception is already installed or proven. A forward-only source patch and its focused regression result are deliverables of the requested owner-maintenance scope, conditional on approval.

### Approval and continuation boundary

Requested decision: authorize these exact four owner paths and their focused verification as one tranche. This is the only new permission request: it changes the mechanism judging agents. After approval, Local authors/releases the exact owner work order, delegates one internal worker, reviews the result, closes it and then continues the already-requested bounded R1 source packet if its actual candidate passes. No new permission is requested for each work-order, check, repair or commit within those granted scopes. Real data, provider/live, running product, production, public and deploy remain parked.

Until a real operator answer arrives, keep all four owner paths untouched. Elapsed time, standing next messages and a written authorization-shaped block are not substitutes for that answer. This is a prepared scope request, not an approval, active source work order or executable successor.

Documentary validation history for this proposal: initial reviewer-fast flagged an approval-related proximity match in the trace and missing LHW24 continuity text. Local clarified that owner changes are outside the admitted scope and retained explicit parent/freeze continuity; original reviewer-fast.log stays FAIL. No protected owner change or proposed-rule verification was performed.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality_core.py; governance/compat/check_active_session_state.py; governance/compat/check_semantic_convergence_control.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_governed_artifact_checker_read_ahead.py; governance/compat/check_agent_packet_authority_and_encoding.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_core_guard_self_protection.py; governance/compat/check_next_move_freshness.py; governance/compat/check_public_export_disposition.py |
| literalTokensReviewed | baseline structural sections; one unchanged prospective SCEC STOP candidate; pending exact4 protected owner scope; exact7/6 documentary continuity; no source/authority claim |
| gateRunPurpose | confirmation of source design, actual candidate and current continuity; not first discovery or runtime proof |
| claimBoundary | checker validates declarations and source hashes; Local decides source semantics; no claim of agent comprehension |

## External/Local Coordination

INTERNAL_AGENT source-design and progression aides operate in the shared private workspace. Phase=PLAN, decision owner=LOCAL. External relay/funnel methods were read; no remote research, repository absorption or external dispatch occurs. Public absence is not used as private absence. Advisory results do not override the current roadmap or canonical checker.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - selected current source and owner symbols only; no corpus result is asserted.

## Knowledge System Reconciliation

- Knowledge task class: targeted source-design preparation, not corpus absorption
- Source manifest: the selected eleven owner-symbol rows in Source / Predecessor Evidence
- Source manifest hash: 7089ea00bed2c5599b3da3cac306ff017e5d08cdbc57865070616e5860faf580
- Enumeration safety: filesystem-backed named-path reads; no directory enumeration selected
- Intake registry or ledger: not applicable to this internal design; no acquired knowledge files
- Authority assets: 0 - no new knowledge corpus; existing named owners retain authority
- Derived views: 0 - no knowledge view generated
- Semantic region ledger: 0 - no semantic corpus selected
- Region reconciliation: assets=0; mapped=0; deferred=0; unmapped=0
- Orphan or unmapped assets: 0
- Cross-region links: not applicable to this source design
- Drift check: PASS for the eleven recorded source pins; no repository-wide freshness claim
- Rebuildability check: not applicable to a knowledge map; existing session generator used separately
- Retrieval boundary: no retrieval readiness or corpus completeness claim
- Adversarial verification: not a corpus task; canonical successor candidate evaluated separately
- Knowledge-map verdict: PARTIAL

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private design/admission record; no public-sync remote/commit/artifact claim.

## Core Guard Self-Protection Authorization

Authorized guard-maintenance scope: current exact7 documentary proposal/continuity and separate exact6 actual-material binding only; four canonical owner code/rule paths listed in the proposal are NOT_AUTHORIZED_PENDING_OPERATOR.

Protected paths:
- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Operator authorization: go through the tranche under standing autonomous roadmap authority; record the mandatory GC-049 decision without touching judgment machinery.
Rollback boundary: exact7 then exact6; no canonical owner/source/evidence mutation.

## Mixed Protected-Path Atomicity Authorization

Disposition: AUTHORIZED_EXACT_MANIFEST

Atomicity reason: one existing design owner and current6 record the same mandatory operator decision; no guard machinery or product source in the batch.

Exact changed manifest:
- `docs/baselines/CVF_NCR_R1_INTEGRATED_HTML_JOB_DESIGN_2026-10-18.md`
- `AGENT_HANDOFF_V63_2026-09-18.md`
- `CVF_SESSION_MEMORY.md`
- `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`
- `CVF_SESSION/state/entries/nextAllowedMove.json`
- `CVF_SESSION/ACTIVE_SESSION_STATE.json`
- `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`

Rollback boundary: exact7 documentary material, then separate exact6 continuity binding.

Separate continuity authorization: AUTHORIZED_EXACT_MANIFEST exact6, limited to current6 actual-material binding.

Preserved historical authorization: AUTHORIZED_EXACT_MANIFEST exact8 at 4e5feb17660412b7c2b34039d182f839df8c0f8c, limited to: `docs/baselines/CVF_NCR_R1_INTEGRATED_HTML_JOB_DESIGN_2026-10-18.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json`.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | Local INTERNAL_AGENT orchestrator/reviewer; decision owner=LOCAL |
| Provider or surface | private shared workspace |
| Session or invocation | ncr-scec-owner-admission-proposal-20261018 |
| Working directory | repository root |
| Command or tool surface | targeted owner/source reads, one internal advisory review, concrete scope proposal and documentary continuity checks |
| Target paths | `docs/baselines/CVF_NCR_R1_INTEGRATED_HTML_JOB_DESIGN_2026-10-18.md`; `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Allowed scope source | operator go-through-tranche instruction; current PLAN owner-disposition action |
| Before status evidence | 4228c115ac1110c6bb7951c47a8976ef236cfb83; clean worktree |
| After status evidence | concrete exact4 guard-maintenance scope prepared; operator permission pending; no guard/product mutation |
| Diff evidence | git diff --name-status; git diff --check; exact7 documentary manifest |
| Approval boundary | proposal/current6 only; four canonical owner paths remain frozen until explicit scope consent |
| Claim boundary | no installed root-admission route, proof of proposed rules or R1 source execution |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-scec-owner-admission-proposal-20261018 |
| Expected manifest | `docs/baselines/CVF_NCR_R1_INTEGRATED_HTML_JOB_DESIGN_2026-10-18.md`; `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Actual changed set | `docs/baselines/CVF_NCR_R1_INTEGRATED_HTML_JOB_DESIGN_2026-10-18.md`; `AGENT_HANDOFF_V63_2026-09-18.md`; `CVF_SESSION_MEMORY.md`; `CVF_SESSION/state/ACTIVE_SESSION_STATE_CORE.json`; `CVF_SESSION/state/entries/nextAllowedMove.json`; `CVF_SESSION/ACTIVE_SESSION_STATE.json`; `CVF_SESSION/ACTIVE_SESSION_BOOTSTRAP_READ_MODEL.json` |
| Manifest delta | MATCH exact7 |
| Deletion or rename disposition | none; original child and all four proposed owner paths untouched |

## Epistemic Process Block

Expected Result / Prediction: one concrete schema/API/manifest and actual successor evaluation removes implementation ambiguity before dispatch. Evidence Comparison: current source supplies snapshot identity/recovery but lacks a job-bound decision writer and HTML Stop; canonical progression requires the stop at ordinal2. Contradiction Or Gap Disposition: finish the design, hold source release and route the architecture disposition to the existing owner. Claim Update: design complete, execution not admitted; no whole-job, accepted product, overhead-effectiveness or R1 exit proof.

## Claim Boundary

Design and declared-state feasibility only. No implementation, tests, running application, browser, provider/live, real-data writer, production, public or deployment claim. No new generic governance mechanism, counter reset or machine-gate semantics is introduced.
