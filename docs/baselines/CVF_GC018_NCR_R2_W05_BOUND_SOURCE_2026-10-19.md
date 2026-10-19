# NCR R2 W05 Bound Receipt Offline Source - GC-018 Baseline

Memory class: governed-baseline
docType: baseline
Status: DISPATCH_READY
Date: 2026-10-19
Batch ID: CVF-NCR-R2-W05-BOUND-SOURCE-20261019
Inspection base: fcf6ad46150748c54938cbfe040461de6e4c7552
Commit mode: WORKER_MUST_NOT_COMMIT
providerExecutionAuthority: FORBIDDEN
rawMemoryReleased=false
Decision owner: LOCAL

## Purpose

GC-018 admission for one integrated offline bound-effect source assignment after activation design. All mandatory source/proof/consumer/measured-store joins are fixed before BUILD; source is not implemented or accepted here.

## Scope / Target / Owner Boundary

Root material6 pair/roadmap/registry3, dedicatedcurrent6; future workerexact36 source/test/vector/returnEP; no Root worker invocation. One manually transferred INTERNAL_AGENT, Local independent acceptance/commit. Runtime/effect controls remain OFF.

## Locked Protocol And Mechanism

Finite outcome: implement the complete D01-D12/P01-P07 bound-receipt composition in production modules with offline/in-memory transports, fresh synthetic local stores and focused proof. Runtime resolvers and both mounted dedicated endpoints remain DENY without a typed in-process fixture context; no environment, client, body/header or dependency-default value can mint it. An injected context is fixture execution authority only, not a real-network/provider grant. Implement both hops, store/proof join and truthful consumer disclosure together; do not return an HTTP wrapper with deferred known dependencies.

BC01 - Schema and keys. New schema cvf.artifactsBoundReceiptOperation.v1, effect BOUND_ENGINE_RECEIPT, fixture disclosure OFFLINE_BOUND_RECEIPT_NOT_ACTIVATED. Preserve v1 contract/source byte-for-byte. Combined codec C3 dispatches strictly by exact schema/effect to v1 parser or C1; unknown/cross-schema data denies. Each lifecycle record carries its schema. New key SHA256 of fixed-order [newSchema,userId,orgId,teamId,sourceRecordId,recomputedRequestSha256,newEffect]; exclude job/version/config/HTML from key and bind them in the immutable envelope. New operations use a separate bound-operations child namespace in the SAME artifacts store owner; no copied parallel store, key migration, v1 authority conversion or new generic dispatcher. Keep 256 consumed keys/owner/effect namespace,16KiB/record,monotonic reservations and no expiry/GC/replay. Valid synthetic source prefix remains required for this offline profile. Existing draft/job types, Save/version/person acceptance and v1 fixtures remain strict.

BC02 - Types. C1 mirrors v1 immutable envelope/output/request fields but fixes the new schema/effect/disclosure and config identityTrust=AUTHENTICATED_DEPLOYMENT_BINDING, production=false. Config body exact keys: schemaRevision,policyRevision,transformRevision,endpointId,storeId,authReference,authScope,identityTrust,production,webOrigin,proxyPath,engineOrigin,engineChallengePath,engineEvaluatePath,instanceId,storeBindingId,timeoutMs,maxRequestBytes,maxResponseBytes,configDigest. endpointId/storeId are nonsecret ASCII labels (1..100); instanceId UUID, storeBindingId lowercase SHA256. Origins must be absolute http(s) origins only, no userinfo/query/fragment/path/default destination; fixture URLs use reserved .invalid or loopback names without DNS/network. Paths are fixed below. maxRequestBytes=16384,maxResponseBytes=32768,timeout integer1000..30000. configDigest is SHA256 canonical body without configDigest. No environment-based factory constructs this config. New bound receipt exact keys: receiptId,decision,evaluatedAt,riskLevel,engineRiskLevel,bindingDigest,ledgerReference. riskLevel=R1 means requested effect class only; engineRiskLevel records actual engine report R0..R4, never overwritten to R1. ledgerReference exact {requestId,blockHash}; receiptId=request attempt; bindingDigest joins envelope/config/instance/store/owner/payload. Existing v1 receipt parser is unchanged.

BC03 - Canonical bytes. Protocol object keys are fixed ASCII; unknown keys, nonfinite/fractional/unsafe integers, invalid UTF8, duplicate JSON object keys and oversized bodies deny before effects. canonicalAscii(value) recursively sorts object keys ordinal ASCII, keeps array order, uses compact JSON separators, standard JSON control escapes, escapes every non-ASCII UTF16 code unit and DEL as lowercase \uXXXX (including surrogate pairs), no BOM or newline. Python equivalent is json.dumps(sort_keys=True,separators=(',',':'),ensure_ascii=True,allow_nan=False), with integer range limited to JS safe integers. The exact canonical ASCII UTF8 bytes are signed/hashed; receiver requires canonical equality to reject alternate encodings. Preserve JS sourceContent.slice(0,500), including boundary/lone-surrogate cases via escaped JSON; Python counts UTF16 units using surrogatepass. The shared C5 fixture MUST bind empty/ASCII/VI/astral/lone-surrogate/control/key-order/malformed duplicate-key cases to exact canonical hex, SHA256 and HMAC expected values, consumed independently by TS and Python tests.

BC04 - Signatures. Dedicated Web path /api/governance/artifact-receipts accepts POST only, action CHALLENGE or EVALUATE. Engine paths POST /api/v1/artifact-receipts/challenge and /api/v1/artifact-receipts/evaluate. HMAC-SHA256 preimage canonicalAscii(["cvf.boundReceiptAuth.v1",hop,kind,"POST",path,timestampMs,nonce,configDigest,sha256(rawCanonicalBody)]). hop EXPORT_PROXY or PROXY_ENGINE; kind REQUEST or RESPONSE; nonce64lowercasehex. Dedicated key references/scopes per hop, secret only in fixture context; never browser, environment default, receipt or log. Headers x-cvf-bound-hop/kind/timestamp/nonce/config/signature hold bounded ASCII scalars. Timestamp integer in [now-30000,now+1000]; no duplicate/conflicting headers. Replay key covers keyReference/hop/kind/nonce/config; bounded1024entries/context, expired request never accepted, capacity-full denies. Invalid/missing signature has no session, token-equality, legacy or generic-evaluate fallback. Response body includes requestNonce and every signed request join; a request signature cannot authenticate a response or other hop/path.

BC05 - Wire bodies. Both request kinds share exact {schema,kind,owner,operationKey,attemptId,configDigest,challengeNonce}, schema=cvf.boundReceiptWire.v1. CHALLENGE has just these keys. EVALUATE additionally carries requestSha256,artifactId,payloadSha256,envelopeSha256,phase,riskLevel,instanceId,storeBindingId,evaluate. evaluate is the exact existing five-field ControlledEvaluateRequest: request_id,artifact_id,payload:{content},cvf_phase=REVIEW,cvf_risk_level=R1. phase/riskLevel repeat REVIEW/R1 and must join it. owner comes from export normal session, not browser selectors. payloadSha256 hashes canonical five-field request; envelopeSha256 hashes exact new envelope. Browser body remains seven fields, headers remain two untrusted job selectors. CHALLENGE_RESULT exact {schema,kind,requestNonce,challengeNonce,configDigest,instanceId,storeBindingId,backend,policyRevision,expiresAtMs}; backend SQLITE; expiresAtMs<=issuedAt+5000 and within overall deadline. EVALUATE_RESULT exact {schema,kind,requestNonce,operationKey,attemptId,artifactId,payloadSha256,envelopeSha256,owner,configDigest,instanceId,storeBindingId,declaredRisk,engineRiskLevel,ledgerReference,report,executionRecord}; declaredRisk R1. The report/execution fields use the current engine report shape and must agree on request/artifact/decision/action/risk/ledger. Validate each body signature and exact expected join, not merely echoed labels.

BC06 - Measured store. E3 constructs a private process/thread-owned bound subclass of existing SqliteLedger with one pinned native SQLite connection and a close-safe per-call facade for inherited read_chain/append_event; explicit close_binding closes the physical handle in finally. No change to existing SqliteLedger schema/append algorithm. Construct only over an explicitly owned fresh test root (test peers may reopen that same approved disposable database); never generic server _ledger or an active path. Measure the opened connection PRAGMA database_list canonical realpath plus primary-file stat dev/ino (decimal strings), backend and a factory-generated connection nonce; bind storeBindingId=SHA256(canonicalAscii(["cvf.boundReceiptStore.v1",instanceBootUUID,"SQLITE",privateCanonicalPath,devString,inoString,connectionNonce])). instanceBootUUID and nonce are factory-generated, not caller-supplied claims. Private path never exported. Reject symlink/reparse/foreign namespace and changed path/object/closed connection/PID/thread/config before execution, and verify again before signing response. Actual pinned connection ensures a path swap cannot redirect this operation to a new database. OS-hostile root owners and compromised interpreter/kernel are outside this fixture claim; no ACL-hardening or OS-confinement assertion. Orchestrator.ledger must be the exact factory-issued object. Bind evaluation context to that instance once; append wrapper attaches operation/envelope/owner/config/store/instance/payload metadata to the existing ledger event before calling inherited append. Exact lookup_request_id after commit must return the committed same-context block before signing; read-by-id is internal response verification only, not a public reconcile-A endpoint. Failure/closed connection consumes authority, no retry/reopen using the same logical operation. The process owns one writer; explicit peer tests challenge the same production mutation path without activating an app service.

BC07 - Engine policy and results. New handlers validate signed context and REVIEW/R1 before orchestrator entry. Derive actor_id from authenticated owner digest in server-created payload; reject caller actor override. Preserve excerpt as content; do not imply the full HTML was evaluated. Use existing CoreOrchestrator and SqliteLedger, do not rewrite generic policy/auth APIs or manufacture engine risk. Report actual computed risk separately; requested R1 is an admission envelope, not proof of global engine phase policy. Verify ledger event context and report decision/action consistency; valid remote DENY => DENIED, valid other current decisions => RECEIPT_VERIFIED with explicit policy limits. No assertion of actual AI-governance quality or release readiness from offline fixture tests.

BC08 - Attempts/unknown. Existing trusted opaque admission/start/grant/outcome authorities work across the typed schema dispatch with exact schema/owner/key/envelope/invoker binding; cross-schema, fake/copy/spent/restarted authority denies0. Snapshot request and config before first await. One invocation may perform one signed challenge plus one signed evaluate through Web and engine: distinguish invoker count, proxy requests, challenge requests, engine evaluate calls and ledger append count. One evaluate max/logical operation, zero automatic retries/redirects/fallbacks; preflight count<=1/operation. All steps share one absolute monotonic deadline, not four full timeouts. Any error/ambiguity after invoker entry, including bad challenge, typed/thrown NOT_CONFIGURED, response loss, body cap, wrong ID/store/signature/boot or Stop => OUTCOME_UNKNOWN with no later send or response upgrade. Mechanical abort before invoke may be FAILED_BEFORE_SEND, still consumed. Exact verified target/config reuse0; different job/version/config/HTML => reference-only409, never prior receipt with new HTML. Stop only fences local publish/waits, not remote cancellation/billing. Presence B stays diagnostic; no UNKNOWN release or read-by-id recovery grant.

BC09 - Composition and held activation. S3 exposes only a typed fixture profile factory with private issued identity; production, absent/disabled/invalid/unsupported mode always DENY. Mounted Web route has no active context by default; tests inject handler factory context. E4 mounts the dedicated engine router with context resolver returning no activation; env values cannot activate it. Generic routes/health/ledger and legacy helper behavior remain outside this bound path and unmodified. Actual export POST selects the bound fixture only through mocked typed resolver in offline tests, preserves auth/job/hash binding and renders the exact envelope; it cannot accept injected browser permit/config/URL. Job capability J1 may expose a nonsecret bound-disclosure object only from its explicitly injected context, never from untrusted query/body. All normal runtime resolvers remain held; no credential access or destination discovery is implemented.

BC10 - Consumer disclosure. HtmlJobControls consumes a strictly validated capability discriminator BOUND_ENGINE_RECEIPT and nonsecret disclosure only in the injected fixture case. Render U2 before the existing Build control in the same flow; no need to modify the911-line ArtifactExportPanel. Include EN/VI configured destination, excerpt/identity sent, access/retention, attempt limit1 and cost status UNKNOWN_NOT_AUTHORIZED, Stop/unknown/no-retry and requested R1 versus computed engine risk. Missing/malformed capability never labels this as LOCAL_SYNTHETIC or authorizes it. No real-effect capability is emitted by defaults. Preserve old job/Save/version/person decision APIs and stale-scope/late-capability fences. The bound output projects engineRiskLevel honestly to the existing UI risk field, while retaining requested risk in a separate verification detail. No business/person acceptance implied by a receipt.

BC11 - Transaction proof. Because real disposable SQLite append/rollback and held connection failure paths are exercised, apply the full local transaction contract below. Real second process invokes E2/E3 and inherited append_event with deterministic READY/START_ATTEMPT/ATTEMPTING/PARENT_RELEASE/ENTERED/COMPLETE events; elapsed sleeps never prove exclusion. Inject failure after acquisition before mutation; next peer acquires, records roll back exactly and resources close. Read actual scratch-file owner/protection/inheritance and complete ACE tuple before/after via read-only Windows security inspection. Adversarial copies of those actual tuples with EXTRA_ALLOW/DENY/INHERITED/WRONG_OWNER must fail semantic equality; retain multiplicity. No security mutation or claim of repairing a changed ACL is authorized. SQL rollback must leave relevant bytes/record/existence and observed security semantics equal to captured pre-state. If any required field or real peer proof is unavailable, return consolidated BLOCKED with logs, not a weakened oracle.

BC12 - Offline proof only. Use invented fixtures, per-task disposable roots, injected Node transport and in-process ASGI clients, no listener/TCP/real HTTP/DNS/browser/provider. Stub only the AI/business-decision seam where needed; do not stub the auth/store/operation path claimed as proof. An actual engine execution fixture may prove invocation/metadata/ledger joins only, not actual AI governance behavior. Do not run the release live bundle in this work order. D01-D12/P01-P07 and BC01-BC12 are the locked contract; ordinary code layout and assertion implementation stay with the worker within exact36/size/budget.

## Locked Cross-Language And Key-Lifetime Clarifications

The v1 controlledRequestSha256 export and v1 canonicalJson behavior remain compatible. The new schema uses C1 canonicalAscii for payload/envelope/config/wire digests; store/proof choose the digest function from the already validated envelope schema, never from an untrusted caller flag. Do not hash a new-schema non-ASCII request with the v1 serializer. Tests cover both request digests and cross-schema denial.

authReference identifies a versioned immutable two-hop key-reference bundle. Factory input holds distinct EXPORT_PROXY and PROXY_ENGINE references/keys; clone key bytes and all manifest/config data before any await, keep them private, and reject unknown scope/bundle/key replacement. A rotation requires a new bundle/manifest revision and cannot revive an old operation. Responses never export raw key bytes or private filesystem paths. API default resolvers cannot construct a bundle from environment.

At least one final fixture must execute actual TS export/store/proof -> actual Web handler factory -> actual Python dedicated handler -> actual bound SQLite owner, with valid signed canonical bytes and a commit-response-loss or wrong-store adversary, not mocked endpoint success bodies. Reuse E8's approved helper in an explicit pipe-bridge mode: one owned Python process holds its context/native connection on its own thread, receives canonical frames on stdin and returns bounded canonical responses on stdout. Invoke the same E2 handler with an in-process ASGI client; no sockets/listener. The test reads measured instance/store challenge metadata before constructing its fixture manifest. One shared bridge per test-run avoids spending a child per case; include it in the24Python-start cap and join/close it. Cross-language shared-vector tests remain separate oracle assertions. Test-only clocks are explicit and shared; default handler clock is real time.

Read-only security inspection and pure tuple adversaries in BC11 establish security invariance across SQL rollback. They do not establish restoration after a real OS ACL mutation, which remains forbidden. Record that limit in the return; all required actual owner/protection/inheritance/ACE fields and rollback content/existence comparisons still apply. Connection/app factories in in-process ASGI tests must create/use/close their SQLite binding on the same owning thread, not silently bypass the thread check.

Rollback content oracle: compare canonical committed block/event bytes from read_chain, the expected request-ID set, and relevant pre-existing database/root existence plus the actual security tuple. Capture SQLite journal/WAL operational state separately; its internal page bytes are not the committed-chain equality oracle. This fixes the content boundary before tests and does not relax any committed-record, extra-entry or missing-record adversary.

## Design Control Gate

| Producer/owner | Carrier/export/registration | Consumer | Positive/hostile proof | Disposition |
| --- | --- | --- | --- | --- |
| C1 newprotocol + C3codec | S1existingstore + P1proof | P3branch/P4actualexport | C2/C4/S2/P2/P5 | CREATE_NEW_AND_EXTEND_EXISTING |
| S3typedprofile/S5transport | S7factory/S8dedicatedWebroute | E1contract/E2router | S4/S6/S9 + E5/E6 shared C5vectors | CREATE_NEW_HELD_RUNTIME |
| E3openedSqliteowner subclass | E2router/E4actualmount(defaultDENY) | existingCoreOrchestrator ledger same object | E7/E8 realpeer, wrongstore/closed/failure/rollback | REUSE_EXISTING_LEDGER_NO_SCHEMA_MIGRATION |
| J1capability from injectedcontext | U1controls/U2disclosure | existing panel Build and job/version flow | J2/U3/U4 stale/malformed ENVI | EXTEND_EXISTING_CONSUMER_ONLY |

All8modified sources well below their GC-023 hard thresholds; exact34source/test/vector split planned upfront. Newtest maxima650; no expansion of the684-line operation test or911-line panel. READ-ONLY configuration and no new dependency/package. Registry new exact34planned product paths and named config/source dependencies registration NOT_STARTED; no corpus-complete claim. Source artifacts/exports/registrations are named before implementation; no runtime daemon or dispatcher.

## Required Artifact Manifest

| ID | Path | Action | Max lines | Requirement |
| --- | --- | --- | --- | --- |
| C1 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/artifacts-bound-receipt-contract.ts | ADD | 550 | REQ-CONTRACT |
| C2 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/artifacts-bound-receipt-contract.test.ts | ADD | 650 | REQ-CONTRACT |
| C3 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/receipt-operation-schema.ts | ADD | 450 | REQ-STORE |
| C4 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/receipt-operation-schema.test.ts | ADD | 650 | REQ-STORE |
| C5 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/fixtures/artifact-bound-receipt-v1.json | ADD | 350 | REQ-CONTRACT |
| S1 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-snapshot-store.ts | MODIFY | 650 | REQ-STORE |
| S2 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-snapshot-store.bound.test.ts | ADD | 650 | REQ-STORE |
| S3 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/bound-receipt-profile.ts | ADD | 350 | REQ-WEB |
| S4 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/bound-receipt-profile.test.ts | ADD | 650 | REQ-WEB |
| S5 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/bound-receipt-transport.ts | ADD | 450 | REQ-WEB |
| S6 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/bound-receipt-transport.test.ts | ADD | 650 | REQ-WEB |
| S7 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/bound-receipt-api.ts | ADD | 450 | REQ-WEB |
| S8 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/artifact-receipts/route.ts | ADD | 120 | REQ-WEB |
| S9 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/artifact-receipts/route.test.ts | ADD | 650 | REQ-WEB |
| S10 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/receipt-operation-profile.ts | MODIFY | 350 | REQ-WEB |
| P1 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts | MODIFY | 600 | REQ-STORE |
| P2 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.bound.test.ts | ADD | 650 | REQ-STORE |
| P3 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/operation-branch.ts | MODIFY | 350 | REQ-CONSUMER |
| P4 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts | MODIFY | 550 | REQ-CONSUMER |
| P5 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/bound.operation.test.ts | ADD | 650 | REQ-CONSUMER |
| J1 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-job-api.ts | MODIFY | 250 | REQ-CONSUMER |
| J2 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-job-api.bound.test.ts | ADD | 650 | REQ-CONSUMER |
| U1 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlJobControls.tsx | MODIFY | 450 | REQ-CONSUMER |
| U2 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ReceiptEffectDisclosure.tsx | ADD | 220 | REQ-CONSUMER |
| U3 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ReceiptEffectDisclosure.test.tsx | ADD | 450 | REQ-CONSUMER |
| U4 | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlJobControls.bound.test.tsx | ADD | 650 | REQ-CONSUMER |
| E1 | EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/api/artifact_receipt_contract.py | ADD | 500 | REQ-ENGINE |
| E2 | EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/api/artifact_receipts.py | ADD | 500 | REQ-ENGINE |
| E3 | EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/ledger_layer/artifact_receipt_binding.py | ADD | 400 | REQ-ENGINE |
| E4 | EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/api/server.py | MODIFY | 400 | REQ-ENGINE |
| E5 | EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/tests/test_artifact_receipt_contract.py | ADD | 650 | REQ-ENGINE |
| E6 | EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/tests/test_artifact_receipts.py | ADD | 650 | REQ-ENGINE |
| E7 | EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/tests/test_artifact_receipt_binding.py | ADD | 650 | REQ-TRANSACTION |
| E8 | EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/tests/artifact_receipt_peer.py | ADD | 250 | REQ-TRANSACTION |
| R | docs/reviews/CVF_NCR_R2_W05_BOUND_SOURCE_WORKER_RETURN_2026-10-19.md | ADD | 500 | REQ-RETURN |
| EP | docs/reviews/evidence/ncr-r2-w05-bound-source-worker-20261019.json | ADD | not line-capped; <=256KiB | REQ-RETURN |

## Evidence / Planned Verification

| Requirement | Required final evidence |
| --- | --- |
| REQ-CONTRACT | shared exact vectors independently asserted in TS/Python, schema/effect/key/config discrimination; Unicode/surrogate/duplicate JSON boundaries |
| REQ-STORE | opaque authority cross-schema/fake/copy/spent/store/restart; exact request TOCTOU; capacity/no replay; new records under distinct namespace |
| REQ-WEB | both signed hops/path/kind/response nonce; redirect/oversize/expiry/replay/capacity/config/body mutations; no default activation; counters per stage |
| REQ-CONSUMER | actual export/auth/job/hash/HTML path and capabilities; wrongowner/latecapability0; ENVI disclosure before Build, missing/malformed fallback; engine risk label distinction |
| REQ-ENGINE | actual opened-ledger measurement; object/path/config/boot mismatch0; strict context policy labels and actor; committed metadata join; no real AI-governance assertion |
| REQ-TRANSACTION | real OS peer production mutation/barrier/failure cleanup; rollback content+complete actual security tuple; negative tuple comparison adversaries; handle teardown |
| REQ-RETURN | exact36 + source/static/fullgate/raw custody, mandatory preparation chronology, SCEC1, pending distinct Local probe; all tool and resource counts |

One INTERNAL_AGENT assignment,<=300min; Vitest<=2 runs600s each, pytest<=2 runs300s each, tsc<=2 runs240s each, changed TS/TSX ESLint<=2 runs300s each; mandatory final fullgate<=3 runs180s each. No broad whole-repo test/lint or browser. No ad hoc executable diagnostic reruns to evade counters. Collection-only one pytest --collect-only and one Vitest --list allowed before product runs (no execution); record process-start failures distinctly, not hidden retries.

Exact baseline rule/message fingerprints for HtmlJobControls: react-hooks/exhaustive-deps; useEffect missing active,owner,sourceRecordId,still with the existing useReducer/setPending suggestion; useCallback missing owner,still. Current source preimage is pinned; historical raw log `.cvf/runtime/ncr-r1-goal-focus-repair-20261019/worker/lint1.out.log` documents the complete messages and the unrelated HtmlDraftRecovery third warning (read-only, not on this lint list). A nonzero lint exit accepted by this narrow exception must stay nonzero in the return and cannot be labeled ESLint exit0.

Changed lint includes HtmlJobControls with exactly the two existing react-hooks/exhaustive-deps fingerprints at its current useEffect [scope] and useCallback dependencies; original controls preimage is pinned. Baseline inventory records no new errors/warnings; lint exit may be1 only when JSON contains those exact same rule/message/source lines and0errors. Any new fingerprint blocks; no suppress comments/rule downgrade or blanket warning budget. Existing read-only hook warning/panel4 exception remains scoped; panel/whole11 not required. Do not fix unrelated baseline warnings.

Worker scratch `.cvf/runtime/ncr-r2-w05-bound-source-20261019/worker` <=32768files/128MiB, fresh roots only. Peer<=4concurrent/24Pythonstarts total; read-only PowerShell ACL captures<=12starts (total subprocesses<=40 across product fixtures). Store capacity cases retained but reuse fixtures where assertions stay meaningful. Keep raw logs/vectors/roots, no recursive delete/move. Every PID-own child must be joined and terminated only by its owner on deadlock bound; no global process kill. Retain no credentials or active data. No old test/scratch/parent budget refill.

From `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web`: installed tools only.

`node node_modules/vitest/vitest.mjs run src/lib/artifacts-bound-receipt-contract.test.ts src/lib/receipt-operation-schema.test.ts src/lib/server/html-draft-snapshot-store.bound.test.ts src/lib/server/bound-receipt-profile.test.ts src/lib/server/bound-receipt-transport.test.ts src/app/api/governance/artifact-receipts/route.test.ts src/app/api/artifacts/export/proof.bound.test.ts src/app/api/artifacts/export/bound.operation.test.ts src/lib/server/html-job-api.bound.test.ts src/components/ReceiptEffectDisclosure.test.tsx src/components/HtmlJobControls.bound.test.tsx src/lib/artifacts-receipt-operation-contract.test.ts src/lib/server/html-draft-snapshot-store.operation.test.ts src/app/api/artifacts/export/proof.operation.test.ts src/app/api/artifacts/export/operation.test.ts src/app/api/artifacts/export/route.test.ts src/app/api/artifacts/export/job-profile.test.ts src/lib/server/html-draft-snapshot-store.test.ts`

`node node_modules/typescript/bin/tsc --noEmit --incremental false`

`node node_modules/eslint/bin/eslint.js src/lib/artifacts-bound-receipt-contract.ts src/lib/artifacts-bound-receipt-contract.test.ts src/lib/receipt-operation-schema.ts src/lib/receipt-operation-schema.test.ts src/lib/server/html-draft-snapshot-store.ts src/lib/server/html-draft-snapshot-store.bound.test.ts src/lib/server/bound-receipt-profile.ts src/lib/server/bound-receipt-profile.test.ts src/lib/server/bound-receipt-transport.ts src/lib/server/bound-receipt-transport.test.ts src/lib/server/bound-receipt-api.ts src/app/api/governance/artifact-receipts/route.ts src/app/api/governance/artifact-receipts/route.test.ts src/lib/server/receipt-operation-profile.ts src/app/api/artifacts/export/proof.ts src/app/api/artifacts/export/proof.bound.test.ts src/app/api/artifacts/export/operation-branch.ts src/app/api/artifacts/export/route.ts src/app/api/artifacts/export/bound.operation.test.ts src/lib/server/html-job-api.ts src/lib/server/html-job-api.bound.test.ts src/components/HtmlJobControls.tsx src/components/ReceiptEffectDisclosure.tsx src/components/ReceiptEffectDisclosure.test.tsx src/components/HtmlJobControls.bound.test.tsx --format json --max-warnings=0`

From `EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core`: `python -m pytest tests/test_artifact_receipt_contract.py tests/test_artifact_receipts.py tests/test_artifact_receipt_binding.py -q`. Every import of api.server must first isolate CVF_GOVERNANCE_LEDGER_PATH to this task fresh root within the child environment and restore it; no .env read or active default initialization. In-process ASGI calls only; block socket/network calls. Dependencies pytest/fastapi/httpx/pydantic are already discoverable in the current Python interpreter; no install permitted.

From repository root, final requiredGate below. Do not use a shell pipeline that hides exit status. Capture actual source hashes at each product check and final return. Report initial failures and final byte coverage honestly.

## Decision / Baseline

Admit the exact36 offline source proposal for manual transfer only after actual boundrelease. No unresolved technical choice remains in this scope. BC01-BC12 supplement the frozen D01-D12 design; no old fixture contract/history changed. All later actual effects remain held.

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| v1 immutable fixture contract | SOURCE_VERIFIED | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/artifacts-receipt-operation-contract.ts | schema/config/envelope codec | parseEnvelope | v1 contract | ACCEPT |
| opaque operation owner | SOURCE_VERIFIED | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-snapshot-store.ts | admit/start/consume/outcome | HtmlDraftSnapshotStore | artifacts store | ACCEPT |
| proof request snapshot | SOURCE_VERIFIED | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts | prepare/invoke/run | runControlledReceipt | export proof | ACCEPT |
| default posture | SOURCE_VERIFIED | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/receipt-operation-profile.ts | resolver/route decision | resolveReceiptOperation | server profile | ACCEPT |
| job capability owner | SOURCE_VERIFIED | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-job-api.ts | handlers GET | jobRouteHandlers | job API | ACCEPT |
| current consumer | SOURCE_VERIFIED | EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlJobControls.tsx | capability/prepareJob/disclosure render | HtmlJobControls | job controls | ACCEPT |
| existing SQLite transaction | SOURCE_VERIFIED | EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/ledger_layer/sqlite_ledger.py | connection/read/append/exact lookup | SqliteLedger | engine ledger | ACCEPT |
| engine registration | SOURCE_VERIFIED | EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/api/server.py | app/_ledger/evaluate | evaluate | engine API | ACCEPT |
| accepted design | SOURCE_VERIFIED | docs/baselines/CVF_NCR_R2_W05_ACTIVATION_DESIGN_2026-10-19.md | D01-D12/P01-P07 | Selected Integrated Design | Local design | ACCEPT |
| new symbols and wire fields | DOC_ONLY_NEW | docs/baselines/CVF_GC018_NCR_R2_W05_BOUND_SOURCE_2026-10-19.md | BC01-BC12 | Locked Protocol And Mechanism | DOC_ONLY_NEW spec before implementation | ACCEPT |


## Source Preimage And Dependency Pins

| Path | SHA256 | Lines / action |
| --- | --- | --- |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/artifacts-bound-receipt-contract.ts | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/artifacts-bound-receipt-contract.test.ts | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/receipt-operation-schema.ts | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/receipt-operation-schema.test.ts | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/fixtures/artifact-bound-receipt-v1.json | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-snapshot-store.ts | 828afbd9d7b8f4d75156e8b7414349fbc6492afb54e4b35563547851d5d44f88 | 472 / MODIFY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-snapshot-store.bound.test.ts | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/bound-receipt-profile.ts | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/bound-receipt-profile.test.ts | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/bound-receipt-transport.ts | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/bound-receipt-transport.test.ts | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/bound-receipt-api.ts | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/artifact-receipts/route.ts | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/governance/artifact-receipts/route.test.ts | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/receipt-operation-profile.ts | bdddaeadb77dd7e9e1560243cbe3c87bc2ea920e65ab597753df28aba85fca58 | 104 / MODIFY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.ts | 34d98083c66accd4cb6b29d507a45ac719c9a5f411da9372b0ac5002ba99fd5a | 345 / MODIFY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/proof.bound.test.ts | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/operation-branch.ts | 8478e8673a2c95ebea0b7b6155fab33101d703d62c0d5737824b8fb3b6692bb7 | 97 / MODIFY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/route.ts | e9266d4ecd7f3c46dcda7a53eca4a576838af18bf9fc7663a5e8196c1e944fbb | 419 / MODIFY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/artifacts/export/bound.operation.test.ts | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-job-api.ts | bfb68c9d15afe0083d5c4d28e4ffdaf1835ae9bcb9ac11b4d77d5b2312cae9a2 | 111 / MODIFY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-job-api.bound.test.ts | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlJobControls.tsx | 36a03380619cc5bbca540cabfbe2b7a96b9ff4f656265a2f3ea8390c1cb30b45 | 301 / MODIFY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ReceiptEffectDisclosure.tsx | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ReceiptEffectDisclosure.test.tsx | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/HtmlJobControls.bound.test.tsx | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/api/artifact_receipt_contract.py | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/api/artifact_receipts.py | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/ledger_layer/artifact_receipt_binding.py | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/api/server.py | b557d28703c22353c74de170e5eb9151e73fa216a44fb3af39935b92da055bd6 | 295 / MODIFY |
| EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/tests/test_artifact_receipt_contract.py | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/tests/test_artifact_receipts.py | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/tests/test_artifact_receipt_binding.py | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/tests/artifact_receipt_peer.py | ABSENT_NEW_FILE | 0 / ADD |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/artifacts-receipt-operation-contract.ts | 7cc84663af56bbf682afc2aadac13ccabd6d45777f5a2ff9229d26ce12a05094 | READ_ONLY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/artifacts-receipt-operation-contract.test.ts | 1ba44d1f5e68bc0d72aa6668d6680c3918d5c50dc2369c66013031288bd82713 | READ_ONLY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-job-contract.ts | ceb0b7308c39d1a172ab47d86580039168ead52811f339ec2c9b8c9146d70550 | READ_ONLY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/html-draft-recovery-contract.ts | 89782c054e3e242b0d398ef37c1d4887f0763a97d730734cd45f05270c9185f0 | READ_ONLY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-job-synthetic-profile.ts | 9d87baee877031fb3839deb7caa2a0cfe431a273c166036c768e85c64da8aca8 | READ_ONLY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/server/html-draft-recovery-api.ts | c5399e838b6c195423912f7ae33da4f352f94c66958c8aeccb29fe3bdeaf4d88 | READ_ONLY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/ArtifactExportPanel.tsx | d4f2c2d8ec50de9aeb31e2c850ba311f7facbabf02bec9a667d12daf10caaa8c | READ_ONLY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/components/useHtmlBuildAttempts.ts | 00cb76dc36ae8efacaafffe3c1ec5086b1707baa8412afd4760ec1c9eb70fcfd | READ_ONLY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/test/setup.ts | bc573b2a6133b07404c42f797bce43fe73464711e0281f29da8234bf2fed6b27 | READ_ONLY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/package.json | f03fc2c2700e904dc88e10395d0856983b9b0f9e6f27150713fa402f9e9fe24b | READ_ONLY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/tsconfig.json | d4af4823c8a2919796c5faa29805cd152217fbc25d6021c2da57541a685ea0f6 | READ_ONLY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/vitest.config.ts | 9a4a65976b5b7a5d038f9cb412a90d417f804108cf1dd33bae4421989a863420 | READ_ONLY |
| EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/eslint.config.mjs | d0ccd1757c31535cdd7762fcfbfa1677a97fef2543b61e2e09322ade86797ffb | READ_ONLY |
| EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/ledger_layer/sqlite_ledger.py | df353a92b3adead1ed5cf00d7128ba9039c573e0441b819118094ec77c4c4ce5 | READ_ONLY |
| EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/core_orchestrator.py | 9d35ed87fafeb5a21814f94dbdd7db8e2e96ab430eb300f5f2a1ae77faa85a69 | READ_ONLY |
| EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/requirements.txt | 7adfeccb5eef259406a1a64993b4b205f1f3c2d153bb3c1d21d27993edaaa0f5 | READ_ONLY |
| EXTENSIONS/CVF_v1.6.1_GOVERNANCE_ENGINE/ai_governance_core/api/__init__.py | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | READ_ONLY |
| docs/baselines/CVF_NCR_R2_W05_ACTIVATION_DESIGN_2026-10-19.md | b38bd2345432e5c0ebacb85e652c9af45ae6854314b797eb4dc5369be8bf40de | READ_ONLY |
| docs/reviews/CVF_NCR_R2_W05_BINDING_REPAIR_LOCAL_COMPLETION_REVIEW_2026-10-19.md | a48dec3bc0ff8f30c45bb17c41a2267fc9bbc1ce38e3a2ca959d466a9f47d8b8 | READ_ONLY |

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperPath | governance/compat/build_dispatch_packet_scaffold.py |
| scaffoldHelperCommand | python -B governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-R2-W05-BOUND-SOURCE-20261019 --title "NCR R2 W05 integrated bound receipt offline source" --date 2026-10-19 --base fcf6ad46150748c54938cbfe040461de6e4c7552 --commit-mode WORKER_MUST_NOT_COMMIT --stdout --dispatch-kind INITIAL --dispatch-surface INTERNAL_AGENT --review-round-count 0 --root-cause-cluster-id NOT_APPLICABLE_INITIAL_DISPATCH --scec-problem-key ncr-r2-w05-bound-receipt-offline-source --no-evidence-readiness-applicable |
| scaffoldOutputSha256 | a8ad326feee2493bd1e26b7ddba9514cad599788fae9fe10012004d7adffc452 |
| scaffoldGeneratedBeforeManualAuthoring | YES |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| claimBoundary | Scaffold provenance only; no runtime or provider behavior claim |
| manualEditsAfterScaffold | locked protocol/manifest/graph/transaction/requirements/commands and source pins |
| checkerReadAheadConfirmation | dispatch/source/ledger/role/transaction/size/architecture constants and prior checker-safe owner blocks read |
| docOnlyNewFields | BC01-BC12 protocol and new real-effect schema declarations; source implementation absent at dispatch |

## Checker Source Read-Ahead Block

| Field | Evidence |
| --- | --- |
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality_source.py; governance/compat/check_work_order_dispatch_quality_architecture_schema.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_review_cost_control.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_high_risk_local_transaction_proof.py; governance/compat/check_governed_file_size.py; governance/compat/check_python_automation_size.py |
| literalTokensReviewed | exact36/7requirements; source columns; INITIAL0 neweffect not oldS5 reset; internal architecture exemption plus physical graph; REQUIRED nine-field transaction; final required gate raw bytes; closure ordering |
| gateRunPurpose | confirmation/evidence before final release, not product execution |
| claimBoundary | shape and source identity only; independent acceptance and behavior not proven by a packet |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.

Actual command: `python -B governance/compat/run_adif_defect_resolver.py --task-class "Work-order authoring / dispatch" --role dispatcher --lifecycle-phase pre-dispatch --max-results 100 --json`. IDs: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0056, ADIF-0057, ADIF-0058, ADIF-0061, ADIF-0062, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006. Raw `.cvf/runtime/ncr-r2-w05-bound-source-20261019/root/adif.json` SHA256 `669a86021fd61cb8fd91fba96e39dce168ebd62345ac043d635612a531b3b687`. Apply complete graph/authority/size/closeability/finality before dispatch; no historical worker read cure.

## Epistemic Process Block

Expected Result / Prediction: new bound-effect codec plus measured SQLite/signed two-hop context can preserve accepted one-send invariants without activating runtime. Evidence Comparison: current v1 is fixture-only; accepted199/10 proofs are prior evidence, not new-bound-schema evidence. Contradiction Or Gap Disposition: BC01-BC12 lock all foreseeable joins and new effect proof; actual deployments/cost remain held. Claim Update: reviewed source packet may be manually assigned after actual release, no source acceptance yet.

## Agent Operation Trace Block

| Field | Evidence |
| --- | --- |
| Actor | INTERNAL_AGENT Local dispatcher/reviewer; decision owner=LOCAL |
| Provider or surface | private shared checkout |
| Session or invocation | ncr-r2-w05-bound-source-dispatch-20261019 |
| Working directory | repository root |
| Command or tool surface | scaffold, named source/dependency/size pins, governed packet/registry/gates |
| Target paths | `docs/baselines/CVF_GC018_NCR_R2_W05_BOUND_SOURCE_2026-10-19.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R2_W05_BOUND_SOURCE_2026-10-19.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/corpus-intelligence/registry/entries/ncr-r2-w05-bound-source.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` |
| Allowed scope source | operator next plus activationdesign D01-D12 and standing roadmap; manualtransfer retained |
| Before status evidence | fcf6ad46150748c54938cbfe040461de6e4c7552; clean worktree; empty stage |
| After status evidence | material6 pair/roadmap/registry then dedicatedcurrent6; Rootproductsource/test/worker0 |
| Diff evidence | git diff --name-status; exact6; source preimage pins |
| Approval boundary | offline source assignment only after actualboundrelease; all real effects held |
| Claim boundary | prospective exact36 packet, no implemented or runtime readiness |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-r2-w05-bound-source-dispatch-20261019 |
| Expected manifest | `docs/baselines/CVF_GC018_NCR_R2_W05_BOUND_SOURCE_2026-10-19.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R2_W05_BOUND_SOURCE_2026-10-19.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/corpus-intelligence/registry/entries/ncr-r2-w05-bound-source.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` |
| Actual changed set | `docs/baselines/CVF_GC018_NCR_R2_W05_BOUND_SOURCE_2026-10-19.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_R2_W05_BOUND_SOURCE_2026-10-19.md`; `docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md`; `docs/corpus-intelligence/registry/entries/ncr-r2-w05-bound-source.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.json`; `docs/corpus-intelligence/CVF_CORPUS_SCAN_REGISTRY.md` |
| Manifest delta | MATCH exact6 |
| Deletion or rename disposition | none |

## Claim Boundary

Exact36 offline implementation and focused synthetic proof only after released assignment; all actual network/provider/data/production/public/deployOFF. No governing AI behavior/release/human acceptance claim. R1prelive/R2partial/R3R4open/R5R6deferred. FixtureLocalS5current0/counters0,1,0,1; parentgen9/SCEC2/counters2,0,2,0/blockers2/freeze/prior7/LHW24 and older chains fixed. NewboundeffectINITIAL0 does not reset their counters.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | internal governed input (no external intake) |
| Internal source | docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md |
| Chain map route | NOT_APPLICABLE_WITH_REASON: current private source composition |
| Matching local-view guard | governance/compat/check_external_knowledge_intake_routing.py |
| Owner surface | this source admission pair |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | Local verifies private CVF; no external source promotion |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named source/dependency reads only, no all-files claim.

## Knowledge System Reconciliation

- Knowledge task class: NON_KNOWLEDGE_SOURCE_IMPLEMENTATION
- Source manifest: exact36 implementation/evidence manifest and named read-only owners; no corpus enumeration
- Source manifest hash: NOT_APPLICABLE; no corpus manifest or map produced
- Enumeration safety: filesystem-backed explicit named-file reads
- Intake registry or ledger: no knowledge intake selected
- Authority assets: immutable accepted source, Local review, design and current continuity
- Derived views: no knowledge view produced
- Semantic region ledger: no mapping regions
- Region reconciliation: assets=0; mapped=0; deferred=0; unmapped=0
- Orphan or unmapped assets: NONE within zero-asset scope
- Cross-region links: NONE
- Drift check: read-only oracle pins and final changed source identities
- Rebuildability check: Git/source manifest and named commands
- Retrieval boundary: no retrieval-readiness assertion
- Adversarial verification: no map verification selected
- Knowledge-map verdict: PARTIAL

## Rescan Intelligence Hardening

- Rescan intelligence verdict: NOT_APPLICABLE_WITH_REASON
- Reason: bounded implementation dependencies, not a corpus scan; existing path-scope registry coverage verified without an inventory assertion.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: private source packet; public catalog/export remains deferred until separately admitted.


## Current Runtime Freshness Verification

Source-only dispatch design: no new bound endpoints/modules exist at inspection. Exact26new/8modified product paths were reconciled before authoring; preimages and19read-only pins above bind current fcf6ad46150748c54938cbfe040461de6e4c7552. Installed tool entrypoints and Python module discovery are recorded in the workorder; no product import/test/active runtime/ledger/env value was inspected.
