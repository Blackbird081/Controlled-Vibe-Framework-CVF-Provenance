# NCR HTML B-E Adjunct Source-Only Envelope

Memory class: governed-baseline
docType: baseline
Status: ACTIVE
Date: 2026-10-16
Batch ID: CVF-NCR-HTML-B-E-ADJUNCT-SOURCE-20261016
Dispatch base head: f9ca6a26ef281ae14035ab5fb1d83cfc6658b000
providerExecutionAuthority: FORBIDDEN
Role: INTERNAL_AGENT Local dispatcher/reviewer
Phase: source-only implementation dispatch preparation

## Purpose

Admit bounded implementation of the locked five-file source-only adjunct and distinct Local fake probes under the current operator roadmap grant. This paired baseline/order requires committed exact6 dispatch continuity and bound pre-dispatch PASS before worker execution. No runtime or provider effect is admitted.

## Source / Predecessor Evidence

Accepted design: docs/assessments/CVF_NCR_HTML_B_E_EFFECT_DRIVER_LOCAL_DESIGN_2026-10-16.md
Design raw SHA-256: e9f08174249b61bda99964e1339e2bb2cd06984d622de112fca8aa201f9bbdd9
Design evidence: docs/reviews/evidence/ncr-html-b-e-effect-design-local-20261016.json
Design evidence raw SHA-256: 113d8b99770a76c45f955b5211dcd74d478422c2898f02df9ee71ab82def8b85
Design source head: 7ce762f9e504e7f7efc91a5e572804409956cfe4
Entry source head for this dispatch packet: f9ca6a26ef281ae14035ab5fb1d83cfc6658b000

Root-owned resolver output consumed without rerunning:
.cvf/runtime/ncr-be-adjunct-source-20261016/adif-dispatch.json
Raw SHA-256: 669a86021fd61cb8fd91fba96e39dce168ebd62345ac043d635612a531b3b687
Root-owned independent-probe expectation metadata:
.cvf/runtime/ncr-be-adjunct-source-20261016/local-expectations.json
Raw SHA-256: 9264d071f5b488d626b34a18af7da91bcb8a5fc72a7376bd3317d55a32259c15
This expectation file is preparation metadata only; it records two future Local fake-program predicates and is not observed proof, a worker assertion source, or runtime authority.

Current active parent checkpoints remain unchanged: accepted design only; actual B-E, Native, browser, container, provider, credentials, disposal, parent and public/deploy effects remain parked pending a separately admitted runtime packet.

## Decision / Baseline

SOURCE_ADJUNCT_IMPLEMENTATION_AND_BOUNDED_REVIEW_ADMITTED. Preserve the accepted source13, production7, oracle6, generation9, original source release and source-authority/control proofs byte-for-byte. Add a separate five-file adjunct source family; do not repin the original release or rerun old source13 control/native matrices. The future adjunct release is SOURCE_ADJUNCT_ONLY and cannot itself grant runtime effects.

Dispatch pair:
- docs/baselines/CVF_GC018_NCR_HTML_B_E_ADJUNCT_SOURCE_2026-10-16.md
- docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_B_E_ADJUNCT_SOURCE_2026-10-16.md

Local adopts this pair after one consolidated pre-gate review. After the pair commit, the session-sync steward must bind the active handoff marker to the actual paired material commit and update the authorized exact6 continuity surfaces. The bound pre-dispatch release gate is required before worker release. If the accepted parent marker already satisfies the applicable SOP step, do not add a handoff-only dispatch commit.

## Evidence / Verification

Root clean entry pre-implementation PASS12.54s. Accepted design/source13 evidence is reused at its stated scope; new five-source fake proofs and distinct Local probes remain required. Actual author/dispatch/worker/closure gate results are recorded when run, not inferred from this baseline.

## Scope / Target / Owner Boundary

Worker exact7:
1. scripts/cvf_ncr_html_effect_fence.py
2. scripts/run_cvf_ncr_html_effect_driver.py
3. scripts/test_cvf_ncr_html_effect_driver.py
4. scripts/cvf_ncr_html_browser_fence.cjs
5. scripts/cvf_ncr_html_browser_fence.test.cjs
6. docs/reviews/CVF_NCR_HTML_B_E_ADJUNCT_SOURCE_WORKER_RETURN_2026-10-16.md
7. docs/reviews/evidence/ncr-html-b-e-adjunct-source-worker-20261016.json

Each of the five source/test files must remain strictly below 350 readable lines. If the locked interface cannot fit, the worker returns one consolidated scope blocker; do not compress the design, add files, or edit the original source13.

Local owns the independent probes, Local completion/proof, SOURCE_ADJUNCT_ONLY release, roadmap update, closed-order disposition and final review. The session-sync steward owns exact6 continuity. The worker cannot stage or commit.

## Allowed Scope

The worker may create or modify only the exact worker7 listed above. The five source/test files are new and must be checked individually for current existence before work. Evidence and fixtures stay in current ignored task custody and are retained for Local review.

Local closure material is planned as the exact18 set: worker7; the closed work order; docs/reviews/CVF_NCR_HTML_B_E_ADJUNCT_SOURCE_COMPLETION_2026-10-16.md; docs/reviews/evidence/ncr-html-b-e-adjunct-source-local-20261016.json; docs/reviews/evidence/ncr-html-b-e-adjunct-source-release-20261016.json; docs/roadmaps/CVF_NONCODER_CONTROLLED_CAPABILITY_RUNTIME_ROADMAP_2026-09-26.md; and the six authorized continuity paths listed in the work order. A later handoff-only sync binds the actual final material SHA. The baseline is the earlier dispatch authority and is outside that final18 closure set.

## Forbidden Scope

No edits to source13, production7, oracle6, original source release, source-control authority/proofs, old matrices, product sources, governance checkers/hooks, dependencies, journey source, release/runtime pins, roadmap, session state, handoff or any path outside worker7. No real Native or Job action, Popen child, Node child, browser, network, container, provider, credential, real-data mutation, stage operation, deletion, public write, deployment, hook wiring, admission fixture for actual use, or populated runtime pins/manifest/admission/marker. No runtime authorization follows from this source packet.

## Source Interface Bindings

This section is the frozen prospective public API/schema contract for the implementation worker. These names and exact data shapes are locked before implementation dispatch and must be implemented before worker return; they are DOC_ONLY_NEW and are not claims about existing code. Internal IO/dependency adapter method names remain worker implementation details unless explicitly fixed below.

### Python public API

Module scripts/cvf_ncr_html_effect_fence.py:

- StartLedger.charge(op, *, native, collector, frame)
- StartLedger.snapshot()
- installed_fences(policy, pins, persist_attempt, *, api_factory=None, popen=None), a context manager that restores every original binding in finally, including on invalid pins, constructor errors, runner errors or verification failure.
- snapshot returns exactly the semantic record {workUsed: int, cleanupUsed: int, attempts: list}. Each attempt row carries seq:int, opId:int, kind:str, cleanup:bool, partition:'work'|'cleanup', ordinal:int.
- Only the exact registered DISPATCHED operation and active Native/Collector/Protocol frame can be charged. Work and cleanup are separate partitions, with limits 56 and 8. Work attempt 57 and cleanup attempt 9 refuse before Popen and do not charge. Invalid identity/capacity refusal does not charge. A valid failed, ambiguous, or persistence-expired start remains charged. No partition borrowing, refund or reset.
- The operation's own op.cleanup determines the partition, including after ordinary work closure. Utility frames use Collector.current_op(); direct spawn frames use only the successful original Protocol.grant for the active spawn frame. Preserve the original runner, Native implementation, assignment/readback, identity, persistence, fresh check, resume and cleanup/finalizer order. Do not substitute a grant, queue, clock or finalizer.
- Charge before the original Popen. Persist using persist_attempt(snapshot) with the snapshot as the sole positional argument; persisted content is secret-safe and contains no argv or environment. Serialize precharge and persistence with the counter lock to prevent out-of-order snapshots; release it before fresh protocol validation and Popen. Never hold the parent protocol lock across IO. Persistence failure refuses Popen while the charged slot remains spent.
- The counter is process-local and invocation-local. It does not claim a cross-process or descendant-start ledger.

Module scripts/run_cvf_ncr_html_effect_driver.py exports:

- validate_admission(document, pins, *, inputs)
- load_admission(path, expected_sha256, *, io=None)
- consume_run(admission, pins, *, io=None)
- execute(path, expected_sha256, *, inputs, io=None, runner=None, api_factory=None, popen=None)

Production defaults call the original owned-profile run and original adapters. Injected runner/API/Popen dependencies are test-only. A direct script invocation without the separately admitted runtime admission must refuse with no effect; no additional CLI schema is required, and --help is optional. Existing validate_inputs is applied before computing inputsSha256. Hash UTF-8 JSON with sorted keys, compact separators, ensure_ascii=False, no newline, and no normalization after original validation.

Original owned-profile run returns output containing ok and terminal. Its finalizer's terminal record carries evidence/evidenceSha256/evidenceBytes/acknowledgment{write,readBack,error}/accepted, with terminal evidence at custody/terminal-evidence.json; frozen terminal bytes exclude ACK. execute returns a shallow copy of the original output plus effectFence={ledger:snapshot,browserVerification:observation|null,joinsAccepted:boolean}. It never modifies terminal and never turns original ok=false into success. Effective wrapper ok can be true only when original ok is true and every required original-terminal join is accepted. For original ok=true, compare terminal raw-byte hash and length with its declared evidence hash/length; require terminal.accepted=true; require acknowledgment write=ACKNOWLEDGED and readBack=MATCH; require the original terminal's four positive ABSENT queries and child-confirmed predicate; and require a browser-fence observation matching runId, actor, cap, config, preload and Chrome binding. Missing/mismatched join data rejects wrapper success. An original failure before helper installation may have no browser observation and remains failed. The adjunct performs no new action or persistence after terminal; a later caller captures return separately under its runtime watchdog. Source-only tests stub runner/IO and join model data; they prove no actual terminal or ACK.

Admission JSON and pin JSON may contain formatting whitespace but recursive duplicate-key rejection is mandatory. Admission file bytes must match the independently supplied lowercase SHA-256. Exact closed admission keys:
schemaVersion, scope, decisionOwner, disposition, authority, sourceRelease, invocation, controls, pins, limits, effects, readiness, predecessor.
No unknown keys or bool-as-int acceptance. The exact admission contract:

- schemaVersion=cvf.ncrHtmlBEEffectAdmission@1; scope=OWNED_SYNTHETIC_B_E; decisionOwner=LOCAL; disposition=RUNTIME_EFFECT_ADMITTED.
- authority has exactly baselinePath/baselineSha256, dispatchWorkOrderPath/dispatchWorkOrderSha256, adjunctAcceptancePath/adjunctAcceptanceSha256; repository-local canonical paths and lowercase 64-hex hashes.
- sourceRelease has exactly path/sha256 and binds the frozen original SOURCE_IDENTITY_ONLY release; the adjunct release is never substituted.
- invocation has exactly runId/ordinal/actor/cap/namespace/inputsSha256. runId matches [A-Za-z0-9][A-Za-z0-9_-]{0,63}; ordinal is 1 or 2; ordinal 1 actor=IMPLEMENTATION_WORKER/cap=2; ordinal 2 actor=LOCAL_REVIEWER/cap=1. Namespace is fresh, absolute and outside provenance.
- controls has exactly path/canonicalDigest and binds an existing actor/cap receipt admitted by the original source owner.
- pins has exactly manifestPath/sha256 and binds the independently frozen pin manifest.
- limits has exactly workSeconds=900, cleanupSeconds=120, workStarts=56, cleanupStarts=8, readiness={engine:4,web:6,route:2,total:12}.
- effects has exactly job=1, container=1, web=1, browserSession=1, exports=cap, evaluates=cap, providerStarts=0, stageDeletion=0.
- readiness has disposition=READY and a nonempty array of distinct {path,sha256} current accepted canonical proofs.
- predecessor is null for ordinal 1; for ordinal 2 it has exactly runId/terminalPath/terminalSha256/acceptancePath/acceptanceSha256, each matching a Local-accepted first run.

Pins are a separate closed document. Top-level keys are exactly schemaVersion, scope, adjunctSources, sourceRelease, tools, modules, helpers, docker, chrome, custodyRoot. schemaVersion=cvf.ncrHtmlBEEffectPins@1 and scope=RUNTIME_INVOCATION_PINS. adjunctSources maps exactly the five new source/test paths to lowercase SHA-256. sourceRelease is {path,sha256} for the unchanged original source13 release. tools contains exactly python, node, docker, git, cmd, taskkill, tasklist and netstat, each {path,sha256}; resolve bare utility names to these pinned paths before Popen and never trust a shadow PATH alias. modules is {path}. helpers contains entry and journey, each {path,sha256}. docker is exactly {context,endpoint,image,os,architecture}, with context=desktop-linux, endpoint=npipe:////./pipe/dockerDesktopLinuxEngine, image=sha256:a0725d62d5cfa8fc47b5e30be04bc08ea714a9cdd72c259595526f691db95294, os=linux, architecture=amd64. chrome is {path,sha256}, fixed to C:\Users\DELL\AppData\Local\ms-playwright\chromium-1208\chrome-win64\chrome.exe and ff0c99fc5bb2301cad77930aa76e5354cf2a5fefb7efdcf3b3bc10ba0550c015. Headless Shell is not qualified. custodyRoot is an absolute existing Local-owned path outside the run namespace.

consume_run uses an ordinary exclusive marker at custodyRoot/<runId>.spent.json before the first namespace effect. Create with exclusive xb; bytes are canonical UTF-8 JSON (sorted keys, compact separators, ensure_ascii=False, no newline) with exactly admissionSha256, runId, ordinal, actor, namespace. Flush and close. Any partial write or error leaves the occupied name; no delete/refund/reuse. This seam is fake-only in this tranche and proves no cross-process uniqueness/global transaction property.

### JavaScript helper binding and activation

Module scripts/cvf_ncr_html_browser_fence.cjs exports verifyBinding(bytes, expectedDigest, deps) and installFence(binding, deps). Plain import with no binding environment performs no installation. The environment names are CVF_NCR_BROWSER_BINDING_PATH and CVF_NCR_BROWSER_BINDING_SHA256: refuse either ambient key before discovery, set both only for the exact pinned helper argv, and refuse one-key or conflicting combinations.

Binding top-level keys are exactly schemaVersion, runId, actor, cap, entry, modulesPath, journey, preload, config, profilePath, observationPath, chrome. schemaVersion=cvf.ncrHtmlBrowserBinding@1. entry/journey/preload/config/chrome each have exactly path/sha256; the other paths are canonical absolute paths. Serialize recursively with sorted keys, compact separators, ensure_ascii=False, UTF-8 and no newline. Reject BOM, invalid UTF-8, duplicate keys, unknown fields, noncanonical bytes, digest mismatch and malformed values. Python validates duplicate keys recursively. JavaScript compares input bytes to the canonical reserialization, which also refuses duplicate/noncanonical JSON.

The config is the exact parent-generated bytes and binds actor/cap/profile/inputs. observationPath is owned custody. The module directory equals the runner's qualified dependency directory. The synchronous deps seam covers file/hash/no-reparse checks, module load, observation persistence and existing journey authority; workers may choose private method names but must test the production public API and behavior. No broad module loader or child-process interception.

The helper verifies argv/config and binding, requires the exact Playwright module used by the journey, patches that same cached Chromium object's original launchPersistentContext before entry, and preserves its original this. It charges the single browser call before verification; verifies profile, headless true, absence of a channel property even when its value is an empty string, absence of conflicting executablePath, and finite numeric timeout >0 (booleans invalid). It verifies the qualified Chrome file/path/hash synchronously, persists a secret-safe verification observation, then calls existing journey.authority with the same frozen config and incoming timeout. Final allowance check is fresh; delegate once with only the smaller timeout and explicit executablePath. No await or persistence follows that final allowance check. Refusal or failure spends the slot. No retry or timeout-zero fallback.

Test contract: browser verification observation is the exact closed record {schemaVersion:"cvf.ncrHtmlBrowserFenceObservation@1",runId,actor,cap,bindingSha256,configSha256,preloadSha256,chrome:{path,sha256},verified:true,invocations:1}. It records successful verification before the final authority check and delegate; it must never claim launched=true. The parent joins its identity to the admitted invocation/helper binding and original terminal record. The observation alone is not a launch or success receipt.

Reject ambient NODE_OPTIONS, NODE_PATH, PWDEBUG, PLAYWRIGHT_* and npm_config_/npm_package_config_ equivalents plus Docker host/context overrides before discovery. Require exact Docker context before context inspection; exact endpoint before daemon query; exact inspected image ID and linux/amd64 before container creation. No switch/start/install/pull/build/fallback.

## Native Counter And Preservation Contract

Use one scoped invocation guard. FencedNative._spawn establishes a thread-local frame and calls original Native._spawn exactly once. Do not carry the Native algorithm into the adjunct. A valid charge occurs under the counter lock before original Popen; snapshots are copied/secret-safe and file persistence does not hold that lock. Fresh protocol check occurs after persistence and before original delegation. Preserve the original runner's staging, protocol, finalizer and ACK. Job32 is a separate concurrent membership cap; the root counter is cumulative controlled Native Popen attempts per invocation and does not count browser/Next descendants or in-container processes.

## Source-Only Acceptance / Test Budget

Use only fake API/Popen/Chromium/filesystem objects and synthetic retained fixtures. No actual admission, pins, marker, Native, Job, Popen or Node child, browser, network, container, server, provider, credentials or deletion is authorized. Test programs cannot import worker test assertions as root expectations.

Worker may use at most six fake-only source test program attempts, each with a 90-second outer bound. Expected RED, failure, ambiguity or timeout consumes one slot; no refund and no retry after the cap. The two required final commands are:
- python -B -m pytest scripts/test_cvf_ncr_html_effect_driver.py -q -p no:cacheprovider
- node scripts/cvf_ncr_html_browser_fence.test.cjs
Use plain node invocation, not node --test. No subprocess/fork/Native children inside a proof program. Test interpreter launchers, gates, Git/hash metadata and commit internals are separate from the fake-program slots; do not assert equality with total Git events. Retain all ignored fixtures and outputs; do not remove them in this phase.

Worker source/manual Git activity limit is 64 operations. Root limit is 128 from task entry. Worker maximum elapsed is 180 minutes and root maximum elapsed is 240 minutes, inclusive from conservative task entry 2026-10-16T06:54:00Z; target deadlines are 09:54Z and 10:54Z UTC. Gates and commit internals are not separately instrumented in these manual counts. Any failure/ambiguity spends its test slot; one consolidated blocker is returned. Local may authorize a specific repair within remaining allowance.

## Local Probe and Closure Plan

Root expectation metadata is fixed at .cvf/runtime/ncr-be-adjunct-source-20261016/local-expectations.json SHA-256 9264d071f5b488d626b34a18af7da91bcb8a5fc72a7376bd3317d55a32259c15. It defines at most two independent focused fake programs, each <=90 seconds: a Python fake program and a JavaScript fake program. Expected predicates are the recorded positive and negative boundary groups: charged work/cleanup boundaries and preserved grant/order; refusal before dependent Docker work on endpoint mismatch; marker spent before runner and retained after failure/second-use refusal; exception restoration; qualified cached Chromium object/original receiver/explicit executable path and shortened timeout; no delegation after deadline-consuming verification; binding identity/canonical-byte refusal; no installation on plain import or partial binding environment. This file is Local-owned test guidance only; no worker test helper/assertion import and no live effects.

Worker first completes only the five new source/test files and reports WAIT_ROOT_PROBE with the exact source hashes; tracked worker bytes remain frozen while Local runs the two probes. After Local accepts or authorizes one bounded repair, worker finishes the exact return/evidence pair and runs both required fake commands plus the mandatory worker fast gate. Root evaluates returned evidence, does not recreate implementation, and writes its distinct Local proof. Root may spend the two probe slots once each; a failed/ambiguous program consumes its slot.

Root closure is acyclic: Local proof binds the dispatch-work-order preimage, exact five source files and worker return/proof; the closed work order references that Local proof; the SOURCE_ADJUNCT_ONLY release binds the closed authority, five source hashes and accepted Local proof; completion links the closed work order, root proof and release. Do not repin source13.

Final material18 is worker7 + closed work order + Local completion + Local proof + release + roadmap + exact6 continuity. After the atomic final material commit, handoff-only actual-material-SHA sync follows. Preserve all six continuity paths through final closure. The exact18 path authorization belongs in the Local completion's Mixed Protected-Path Atomicity Authorization.

## SCEC And Prior Evidence Retention

Root SCEC problem key: NCR_HTML_CONFIGURED_RECEIPT_CONTROL_PROOF. Retain root generation9, ordinal2, counters [2,0,2,0], blockers2 and freeze. Preserve the prior7 P4 exclusions. No reset, new transition, independentCriticalEvidence, or normal-collector change. This adjunct is an INITIAL source-only dispatch outside source13 and leaves root SCEC unchanged. No normal suite or prior source13 matrix rerun. Root may request a named narrow repair only after a contradiction and bounded value/cost reason.

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`Work-order authoring / dispatch`, role=`dispatcher`, lifecyclePhase=`pre-dispatch`.
Returned defects: ADIF-0001, ADIF-0002, ADIF-0014, ADIF-0015, ADIF-0020, ADIF-0021, ADIF-0028, ADIF-0029, ADIF-0033, ADIF-0044, ADIF-0045, ADIF-0051, ADIF-0052, ADIF-0056, ADIF-0057, ADIF-0058, ADIF-0061, ADIF-0062, ADIF-0007, ADIF-0016, ADIF-0017, ADIF-0024, ADIF-0031, ADIF-0039, ADIF-0043, ADIF-0049, ADIF-0006.
Root actual max-results100 query returned27/truncated=false; raw output and hash retained in current ignored custody. Draft helper consumed it without rerun. No claim all entry bodies were read.

## Checker Source Read-Ahead Block

| Field | Value |
|---|---|
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py; governance/compat/check_adif_defect_registry_disclosure.py; governance/compat/check_work_order_acceptance_ledger.py; governance/compat/check_gate_to_role_closeability.py; governance/compat/check_independent_review_probe_admission.py; governance/compat/run_worker_return_scaffold.py; governance/compat/run_worker_return_fast_gate.py; governance/compat/check_worker_return_quality_gate.py; governance/compat/check_agent_operation_trace.py; governance/compat/check_external_knowledge_intake_routing.py; governance/compat/check_public_export_disposition.py; governance/compat/check_markdown_structural_completeness.py; governance/compat/check_dispatch_release_readiness.py; governance/compat/check_governed_artifact_checker_read_ahead.py |
| literalTokensReviewed | exact worker7; acceptance-ledger-json/evidence; workerReturnPath; WORKER_RETURN_FULL_GATE_V1; required fast gate; closeability gate IDs and direct dependency edges; Local reviewer role token; dispatch continuity literal; public export and corpus verdict; source symbol/DOC_ONLY_NEW distinction; fake program limits and root SCEC retention |
| gateRunPurpose | confirmatory evidence validation after Local consolidated source/schema/path/authority/acceptance/closure review; no first-discovery gate |
| claimBoundary | source/design/schema contract only; declarations and synthetic expectations do not prove implementation, runtime admission, B-E, AI or provider behavior |

## Source Verification Block

| Claimed item | Source fact type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
|---|---|---|---|---|---|---|
| Accepted bounded effect-driver design and its five new owners | EXISTING_SOURCE | docs/assessments/CVF_NCR_HTML_B_E_EFFECT_DRIVER_LOCAL_DESIGN_2026-10-16.md | Decision / Baseline and Source-Only Dispatch Acceptance Requirements | Decision / Baseline | Local accepted design | ACCEPT |
| Original runner owns staging/protocol/finalizer | EXISTING_SOURCE | scripts/cvf_ncr_html_owned_profile/__init__.py | run | run | existing owned-profile entry | ACCEPT |
| Original terminal and ACK contract | EXISTING_SOURCE | scripts/cvf_ncr_html_owned_profile/execution.py | finalize | finalize | original evidence, terminal and ACK owner | ACCEPT |
| Utility operation identity and active operation | EXISTING_SOURCE | scripts/cvf_ncr_html_owned_profile/execution.py | Collector.command/current_op | Collector.current_op | original operation source | ACCEPT |
| Direct launch frame and original spawn | EXISTING_SOURCE | scripts/cvf_ncr_html_owned_profile/lifecycle.py | Native._spawn | _spawn | original Native implementation | ACCEPT |
| Grant/check and cleanup class | EXISTING_SOURCE | scripts/cvf_ncr_html_owned_profile/protocol.py | Op/Protocol.grant/check | grant | original protocol source | ACCEPT |
| Existing environment/discovery owner | EXISTING_SOURCE | scripts/cvf_ncr_html_owned_profile/profile.py | prerequisites | prerequisites | original profile owner | ACCEPT |
| Journey launch and authority allowance | EXISTING_SOURCE | scripts/cvf_ncr_html_owned_profile/journey.cjs | run/authority | authority | original journey contract | ACCEPT |
| New Python public API signatures and closed data shapes | DOC_ONLY_NEW | docs/baselines/CVF_GC018_NCR_HTML_B_E_ADJUNCT_SOURCE_2026-10-16.md | Source Interface Bindings | StartLedger.charge; installed_fences; validate_admission; load_admission; consume_run; execute | prospective source interface locked here, not existing behavior | ACCEPT |
| New JS helper API and byte-canonical binding | DOC_ONLY_NEW | docs/baselines/CVF_GC018_NCR_HTML_B_E_ADJUNCT_SOURCE_2026-10-16.md | JavaScript helper binding and activation | verifyBinding; installFence | prospective source interface locked here, not existing behavior | ACCEPT |
| Browser verification-only observation | DOC_ONLY_NEW | docs/baselines/CVF_GC018_NCR_HTML_B_E_ADJUNCT_SOURCE_2026-10-16.md | JavaScript helper binding and activation | JavaScript helper binding and activation | verification observation joined by parent; never launch proof | ACCEPT |
| Shallow effectFence wrapper and original terminal joins | DOC_ONLY_NEW | docs/baselines/CVF_GC018_NCR_HTML_B_E_ADJUNCT_SOURCE_2026-10-16.md | Source Interface Bindings | execute; effectFence.joinsAccepted | prospective returned-output contract around original run; terminal stays unchanged | ACCEPT |
| Root independent fake predicates | DOC_ONLY_NEW | docs/baselines/CVF_GC018_NCR_HTML_B_E_ADJUNCT_SOURCE_2026-10-16.md | Local Probe and Closure Plan | Local Probe and Closure Plan | prospective Local predicates, not executed proof | ACCEPT |
| Learning obligation binding | EXISTING_SOURCE | governance/compat/learning_application_binding.py | validate_changed | validate_changed | existing learning application binding | ACCEPT |

## Negative Search And Collision Discipline

No corpus or repository-wide absence claim. Before these drafts, both canonical destination paths were absent and each of the five prospective source/test paths was individually absent. Scoped exact-name search in docs, CVF_SESSION and current ignored task custody found only the accepted design/evidence references; no conflicting output owner. The five future paths must be checked again at worker start; that observation does not claim they remain absent later.

## Dual Agent Surface Matrix

| Consumer class | Interface or owner surface | Authority and risk boundary | Evidence | Adapter boundary | Disposition |
|---|---|---|---|---|---|
| INTERNAL_AGENT | source-only Python driver and helper APIs defined above | Local owns eventual runtime admission; this draft authorizes no runtime | accepted Local design and future source-only tests | internal controller; fake seams used only by tests | CONTRACT_ONLY |
| EXTERNAL_AGENT_CLI_MCP | no external interface selected | external ingress, authority and runtime effects are outside this source family | accepted design and this Local-owned scope | no external adapter is admitted here | DEFERRED_WITH_REASON |

## Intake Role Routing Decision

Current role is INTERNAL_AGENT advisory packet drafter; phase is accepted-design source-only packet drafting; decision owner is Local. External agents provide advisory public research/pattern mapping only; Local owns private CVF source verification and final technical disposition. No external research or repository absorption is performed in this packet.

## External Knowledge Intake Routing

| Field | Value |
|---|---|
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | internal governed input (no external intake) |
| Internal source | docs/assessments/CVF_NCR_HTML_B_E_EFFECT_DRIVER_LOCAL_DESIGN_2026-10-16.md |
| Chain map route | accepted Local design -> internal source-only implementation -> Local review and disposition |
| Matching local-view guard | governance/compat/check_external_knowledge_intake_routing.py |
| Owner surface | docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_B_E_ADJUNCT_SOURCE_2026-10-16.md |
| Disposition | INTERNAL_ONLY_NO_EXTERNAL_PROMOTION |
| Claim boundary | no external research return, external shortlist or public evidence is used as private-CVF proof |

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
  "parentArtifact": null
}
```

## Current Runtime Freshness Verification

NOT_APPLICABLE_WITH_REASON - this packet defines prospective source interfaces only. No current runtime admission, pins, actor receipt, namespace, browser binding or effect is populated or checked. Any later execution needs its own fresh runtime work order and exact source/runtime authority.

## High-Risk Local Transaction Proof Applicability

NOT_APPLICABLE_WITH_REASON - ordinary marker persistence is exercised only through fake IO in this source-only tranche; this is not a live transaction proof.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Reason: this is private provenance source design and worker evidence. Public-sync is outside this packet.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - named design and source-interface owners only; no corpus scan or completeness claim.

## Claim Boundary

Source-only implementation/test grant after committed bound release; no current implementation, executed refusal, runtime or live AI proof. Actual admission/pins/run identity/namespace/Job/browser/container/provider/disposal/public/deploy remain outside this packet. Original source13 and historical controls remain immutable.

## Scaffold Provenance Block

| Field | Value |
|---|---|
| scaffoldHelperCommand | python governance/compat/build_dispatch_packet_scaffold.py --packet-kind generic-worker-dispatch --batch-id CVF-NCR-HTML-B-E-ADJUNCT-SOURCE-20261016 --title "NCR HTML B-E adjunct source" --date 2026-10-16 --base f9ca6a26ef281ae14035ab5fb1d83cfc6658b000 --commit-mode WORKER_MUST_NOT_COMMIT --stdout |
| generatedProfile | generic-worker-dispatch plus WORKER_MUST_NOT_COMMIT |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | accepted design, exact five-file public API and schema bindings, Local probes and closure dependency map |
| checkerReadAheadConfirmation | selected checker sources/functions only; no all-checker-body claim |
| docOnlyNewFields | all prospective APIs, pin/helper/admission records and fake IO seams are DOC_ONLY_NEW until implementation and review |
| claimBoundary | scaffold metadata only; not an implementation or effect grant |

## Agent Operation Trace Block

| Field | Evidence |
|---|---|
| Actor | Local INTERNAL_AGENT dispatcher/reviewer |
| Provider or surface | private shared workspace; completed internal advisory drafter |
| Session or invocation | ncr-be-adjunct-source-dispatch-20261016 |
| Working directory | repository root |
| Command or tool surface | mapped reads; actual root resolver/entry gate; advisory scaffold/drafts; Local consolidated adoption/corrections and canonical author gates |
| Target paths | canonical paired baseline/work order; exact6 dispatch continuity later |
| Allowed scope source | operator full Local roadmap handling and committed five-file design |
| Before status evidence | clean worktree f9ca6a26ef281ae14035ab5fb1d83cfc6658b000; git status --short empty; entry gate PASS12.54s |
| After status evidence | canonical pair only; no implementation/source or runtime effect |
| Diff evidence | exact paired staged manifest before material commit |
| Approval boundary | bound pair/continuity/pre-dispatch precede implementation release; runtime excluded |
| Claim boundary | source-only prospective contract, not executed source or runtime proof |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-be-adjunct-source-dispatch-20261016 |
| Expected manifest | `docs/baselines/CVF_GC018_NCR_HTML_B_E_ADJUNCT_SOURCE_2026-10-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_B_E_ADJUNCT_SOURCE_2026-10-16.md` |
| Actual changed set | `docs/baselines/CVF_GC018_NCR_HTML_B_E_ADJUNCT_SOURCE_2026-10-16.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_HTML_B_E_ADJUNCT_SOURCE_2026-10-16.md` |
| Manifest delta | MATCH exact pair |
| Deletion or rename disposition | none; all prior source/proof/custody retained |
