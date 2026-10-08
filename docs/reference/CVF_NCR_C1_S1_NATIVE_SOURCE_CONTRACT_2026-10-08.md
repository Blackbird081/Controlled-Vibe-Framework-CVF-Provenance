# NCR C1 Integrated S1 Native Source Contract
Memory class: governed-reference
docType: reference
Status: ACCEPTED_SOURCE_SPECIFICATION_RUNTIME_NOT_ADMITTED
Date: 2026-10-08
Batch ID: CVF-NCR-C1-OFFLINE-PRODUCTION-READINESS-20261008
providerExecutionAuthority: FORBIDDEN

## Purpose

Specify one integrated source candidate from already-approved14-path scope and Local architectural reassessment. Preserve caller-parameterized data/state validation and author a guarded native Job Object candidate without executing it. Documentation resolves API design inputs,not OS enforcement.

## Scope / Target / Owner Boundary

New root D:/UNG DUNG AI/TOOL AI 2026/CVF-NCR-C1-CONTROL-SOURCE-S1-20261008;exact14 paths in the paired order;Windows x64 ABI candidate,host compatibility unmeasured. Old two source roots/returns remain frozen. Stage S1 SOURCE_ONLY: no candidate import,compile,eval,literal_eval,fixture/native launch or host probe. Source may contain future guarded calls;no such call is exercised in S1.

## Target / Source

docs/reference/CVF_NCR_S05_SUPERVISOR_SOURCE_CONTRACT_R1_2026-10-03.md remains the pure-data/state/fixture contract except the explicit native-source augmentation below. docs/reference/CVF_NCR_C1_S1_NATIVE_ABI_SOURCE_BINDINGS_2026-10-08.json binds20 actual primary Microsoft responses and their runtime raw-body hashes. Read envelope spent20/20,1170342 B,12.781s;worker may read the named local snapshots and this derived contract but makes0 network requests. Each snapshot hash must match before use;missing snapshots are BLOCKED evidence,not permission for replay.

## Native ABI And Lifecycle Contract

### S1-N1 - Binding and ABI

Keep imports/instantiation effect-free. Import ctypes and load kernel32 only inside an explicitly guarded future S2 entrypoint;never at module/class/default initialization. Default available=false/status=NO_GO;Boolean flags or artifact hashes cannot admit native effects. Refuse unsupported host/ABI before loading. No host/ABI measurement in S1.

Use Windows LLP64 types: BOOL signed32,DWORD/UINT unsigned32,WORD unsigned16,ULONGLONG unsigned64,LARGE_INTEGER signed64;HANDLE and LPVOID pointer-sized;SIZE_T/ULONG_PTR unsigned pointer-sized. Strings are UTF-16 pointers;CreateProcessW command buffer is mutable. Use natural ABI alignment,not packed structures. Derived Windows-x64 layout targets: basic limit64 B,IO_COUNTERS48 B,extended limit144 B,accounting48 B,STARTUPINFOW104 B,PROCESS_INFORMATION24 B,process-ID-list header8 B plus8 B per pointer-sized ID. These are documentary derivations,not executed sizeof/host proof. Actual layout assertions belong to admitted S2;incorrect layout refuses entry.

| API | Source binding shape | Document |
| --- | --- | --- |
| CreateJobObjectW | HANDLE(NULL security attributes,NULL name) | MS-02 |
| SetInformationJobObject | BOOL(HANDLE,32-bit info class,LPVOID,DWORD) | MS-03 |
| AssignProcessToJobObject | BOOL(HANDLE job,HANDLE process) | MS-04 |
| QueryInformationJobObject | BOOL(HANDLE,32-bit info class,LPVOID,DWORD,LPDWORD) | MS-05 |
| IsProcessInJob | BOOL(HANDLE process,HANDLE job,PBOOL result) | MS-06 |
| TerminateJobObject | BOOL(HANDLE,UINT exit code) | MS-07 |
| CloseHandle | BOOL(HANDLE) | MS-08 |
| CreateProcessW | BOOL(application pointer,mutable command pointer,security NULL,NULL,BOOL inherit,DWORD flags,environment pointer,current-directory pointer,STARTUPINFOW pointer,PROCESS_INFORMATION pointer) | MS-09 |
| ResumeThread | DWORD(HANDLE thread) | MS-10 |
| TerminateProcess | BOOL(HANDLE process,UINT exit code) | MS-18 |
| WaitForSingleObject | DWORD(HANDLE,DWORD finite milliseconds) | MS-19 |


Set argtypes/restype for every native function before use;use last-error capture only after failed return,not stale successful-call error values. A NULL CreateJobObjectW handle is failure;check every BOOL. ResumeThread failure is0xFFFFFFFF,not0. Require suspended count exactly1 before treating a resume as successful;unexpected count records unsafe state/cancel,not ready. WaitForSingleObject success0,timeout0x102,failure0xFFFFFFFF;no INFINITE wait. Worker must preserve the exact field order of MS-11..MS-17/MS-20,including every nested structure/pointer and reserved slot;no omitted fields or plain Python int replacing a pointer argument.

### S1-N2 - Owned lifecycle and limit ordering

Eight existing backend methods remain addressable: create_suspended_job,bind_child,resume,cancel,close,query_membership,query_committed_bytes,query_working_set_bytes. Explicit internal helpers may be added inside the same windows_job.py file. Keep typed per-instance references;reject arbitrary caller handles,foreign owner/repeated terminal-state use. No public shape flag authorizes an OS call.

Future native plan: create an unnamed,non-inherited Job;set and read back its limits before CreateProcessW. Extended class9 uses required kill-on-last-job-handle-close0x2000 and caller-provided positive finite job committed-memory limit flag0x200. Apply caller active-process cap flag0x8 only when explicitly supplied;no hidden C1/P1/preset defaults. Never set breakaway/silent-breakaway flags. Query readback must confirm enforced requested limits;unverified mismatch blocks launch. Job handles must not be duplicated/inherited/exported,otherwise kill-on-last-close is not a supervisor-death guarantee. All such guarantees remain unproved in S1.

CreateProcessW must use explicit absolute application path,mutable quoted command data,bInheritHandles=false and CREATE_SUSPENDED0x4;no shell or search-path fallback. Explicit Unicode environment uses CREATE_UNICODE_ENVIRONMENT0x400;unknown environment/input policy blocks. Caller absolute current directory and finite deadline must already be admitted. No resume on job creation,limit setting,process creation,assignment or membership failure. Bind process with AssignProcessToJobObject,then require successful IsProcessInJob call AND output true for that same job/process before ResumeThread. False API return and false output are distinct failure reasons. Nested-job/outer-job failure is NO_GO,never breakaway fallback.

### S1-N3 - Memory and membership observations

Extended limit JobMemoryLimit specifies job-wide commit ceiling;PeakJobMemoryUsed is PEAK,not a current committed-byte observation. Working set is a different metric. Neither may be relabelled as the other or used to claim strict RAM proof. query_committed_bytes and query_working_set_bytes must fail closed with named NOT_ADMITTED/UNKNOWN when a documented matching current sample is unavailable;do not return0,limit,peak or caller counters as measured data. A separately named peak observation may be returned as PEAK_ONLY. Source completeness includes these honest unavailable seams,not a fabricated metric implementation.

Basic accounting class1 exposes ActiveProcesses,not membership of a specific process. Process-ID-list class3 has two DWORD counts followed by ULONG_PTR IDs;bounded caller-sized allocation,return length/count reconciliation and overflow rejection required. No unlimited growth loop. IsProcessInJob is the pre-resume membership check;native active-count/PID sampling cannot prove exactly-once ordering or absence of escaped grandchildren. Those need future owned S2 probes.

### S1-N4 - Cancellation,cleanup and custody

Use finite monotonic deadlines and explicit attempt-versus-success records. Count attempted operations before calls;no hidden retries. Pending child remains suspended on every pre-resume failure. If unassigned process exists,TerminateProcess plus finite wait is required before declaring cleanup;TerminateJobObject cannot kill a process never assigned to the job. After assignment use TerminateJobObject and bounded wait/accounting confirmation. Failure/timeout retains CLEANUP_INCOMPLETE and owned references for later admitted remediation;closing a handle alone is not termination evidence.

Close owned thread/process/job handles once after the appropriate confirmed terminal condition. Capture CloseHandle failure;do not mark a failed close completed or double-close. Keep original failure and cleanup failure separately. Do not leak child handles through inherited descriptor configuration. Handle ownership/death/no-orphan/native availability remain planned/unverified. Supervision state cannot become RUNNING/BOUND/TERMINATED merely because a caller supplied those words.

### S1-N5 - Unimplemented production boundaries

Strict aggregate disk,egress DNS/TCP/UDP and caller privilege/security policy remain UNKNOWN/unimplemented. Preserve fail-closed BoundaryAdmission: source plan allowed does not allow launch. Polling/overshoot is not a hard allocation cap;timeout is not a network deny rule.10GiB disk/8GiB RAM selection is retained separately as production policy,not hardcoded as independent source defaults. P1/HaiDang are assumptions,host/Docker REPORTED_UNBOUND. Runtime overall NO_GO.

### S1-N6 - Data/state invariants and fixtures

Retain R1 F-01..F-07 strict tree/type/finite guards,fullmatch digest,exact output-hash join,NEW-before-assignment,seal revalidation,lexical path refusals and whole-value UNKNOWN sentinel. Strengthen immutable sealed plan as private normalized state with defensive copies;do not expose a mutable accepted envelope or silently claim adversarial private-attribute protection. No absolute import fallback or eager native import. All six fixture builders remain inert sources,with positive/negative and expected evidence contracts from existing fixture design;FX-D1/M1/T1/B1/N1/L1 remain NOT_EXECUTED_PLANNED.

### S1-N7 - Static acceptance and future obligations

Worker desk reading/AST evidence proves source correspondence only. Distinct Local reviewer performs one bounded actual-source hash/AST inspection and independent AST-only mutations for wrong ABI type/field order,missing limit/assignment/membership-before-resume,missing unbound-child cleanup,wrong peak/current label,eager native load,missing finite wait and false cleanup success. Never import/compile/evaluate candidate or AST copies. Predecessor review-completion resolution applies only to old R1 review;new source needs its own review and creation-custody evidence before acceptance. Preserve three retained historical source/custody blockers;do not declare them resolved because files exist or source syntax parses.

### S1-N8 - Exact write and event evidence

One fresh root with exclusive directory creation,exact14 files with create-exclusive xb/CREATE_NEW;no overwrite,append,retry,delete or reuse. Prepare and precheck all finalized source/return payloads in memory with trusted checker APIs before the first write;candidate bytes only undergo read/hash/AST parse. Existing path,drifted seed,reparse/owner ambiguity or partial failure stops the dependent attempt with actual created-path identities. No extra source logs/tests/cache/pyc files. Record resolved target,before-state,actual primitive,actor,command/tool identity,result,bytes/raw SHA and event timestamp for all16 file writes. Mode/time remains reported tool evidence,not independent OS attestation.

Write source-manifest.json last among source files;hash the other13,never itself. Neither sibling WORKER_RETURN.md nor manifest may contain cyclic final-manifest/self hashes. Final CVF Markdown return is finalized before CVF JSON;JSON PROOF-RETURN binds actual Markdown raw hash. The JSON self-hash/final write event is emitted after creation in tool output and retained outside its own contents. Full worker-return gate output must be written to the exact ignored receipt path declared by the order,with command/exit/time/raw hash retained after the gate. Planned self descriptions are never final write/gate evidence. Historical R1 deviations and partial relay remain unchanged.

## Claim Boundary

Source-only candidate contract. No source or fixtures executed,no native binding loaded,no executable ABI/layout/cleanup/containment proof. Successful docs reads are documentation evidence only. Old source closure remains withheld;no metadata STOP resolution or production/S2 admission.

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| Retained exact source approval | GOVERNED_AUTHORITY | docs/reference/CVF_NCR_C1_S1_APPROVAL_DISPATCH_DISPOSITION_2026-10-08.md | Approval Record | operatorAuthority approval recorded | existing Local admission | ACCEPT |
| Present review-completion resolution | ACCEPTED_LOCAL_REVIEW | docs/reference/CVF_NCR_C1_S1_ARCHITECTURAL_REASSESSMENT_2026-10-08.md | S1-R1-STATIC-REVIEW-COMPLETION-ACCEPTED-20261008 | SOURCE_STATIC_REVIEW_PENDING | Local reviewer | ACCEPT |
| Pure source data/state baseline | GOVERNED_PROJECT_CONTRACT | docs/reference/CVF_NCR_S05_SUPERVISOR_SOURCE_CONTRACT_R1_2026-10-03.md | Protocol / Contract / Requirements | validate_envelope;SupervisorPlan;BoundaryAdmission | local-supervisor-source@0.2.0 | ACCEPT |
| Native source/ABI constraints | GOVERNED_PROJECT_CONTRACT | docs/reference/CVF_NCR_C1_S1_NATIVE_SOURCE_CONTRACT_2026-10-08.md | Native ABI And Lifecycle Contract | WindowsJobBackend;S1-N1..S1-N8 | new source candidate contract | ACCEPT |
| Observed Microsoft documentation | LOCAL_VERIFIED_SOURCE_JOIN | docs/reference/CVF_NCR_C1_S1_NATIVE_ABI_SOURCE_BINDINGS_2026-10-08.json | documents | documents;remainingRequests | cvf.ncrC1S1NativeAbiBindings.v1 | ACCEPT |
| Same-chain invariants | GOVERNED_STANDARD | docs/reference/semantic_convergence_control/CVF_SEMANTIC_CONVERGENCE_AND_ESCALATION_CONTROL_STANDARD.md | Enforcement Invariants | hash/locator;stable key;ordinal/counters | SCEC | ACCEPT |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | governance/compat/check_work_order_dispatch_quality.py;governance/compat/check_gate_to_role_closeability.py;governance/compat/check_governed_artifact_checker_read_ahead.py;governance/compat/check_review_cost_control.py;governance/compat/check_agent_operation_trace.py;governance/compat/check_semantic_convergence_control.py;governance/compat/check_preapproval_feasibility.py;governance/compat/check_work_order_acceptance_ledger.py;governance/compat/check_markdown_structural_completeness.py;governance/compat/check_dispatch_prompt_envelope.py;governance/compat/check_dispatch_release_readiness.py;governance/compat/check_independent_review_probe_admission.py |
| literalTokensReviewed | READY;CLOSEABLE;WORKER_MUST_NOT_COMMIT;COMPLETE_PENDING_REVIEW;acceptance-ledger-json;ACCEPTED_REVIEW;hash/unique locator;exact same-chain progression;trace labels |
| gateRunPurpose | confirm integrated source packet before committed bound release;not native proof |
| claimBoundary | prospective source-only admission and documentary evidence only |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`video-production-readiness`,role=`dispatcher`,lifecyclePhase=`design`.
Returned defects: NONE_RETURNED
Actual resolver returned0 of0 candidates,truncatedfalse.

## Agent Operation Trace Block

| Field | Value |
| --- | --- |
| Actor | Local INTERNAL_AGENT dispatcher |
| Provider or surface | private shared workspace |
| Session or invocation | ncr-c1-s1-integrated-source-dispatch-20261008 |
| Working directory | D:\UNG DUNG AI\TOOL AI 2026\Controlled-Vibe-Framework-CVF |
| Command or tool surface | governed reads;bounded Microsoft GETs;scaffold;ADIF resolver;documentary packet writes;canonical gates |
| Target paths | `docs/baselines/CVF_GC018_NCR_C1_S1_INTEGRATED_SOURCE_2026-10-08.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_C1_S1_INTEGRATED_SOURCE_2026-10-08.md`; `docs/reference/CVF_NCR_C1_S1_NATIVE_SOURCE_CONTRACT_2026-10-08.md`; `docs/reference/CVF_NCR_C1_S1_NATIVE_ABI_SOURCE_BINDINGS_2026-10-08.json`; `docs/reviews/evidence/cvf-ncr-c1-s1-dispatch-design-2026-10-08.json`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_C1_S1_INTEGRATED_SOURCE_2026-10-08.json`; `docs/reference/CVF_NCR_C1_S1_MICROSOFT_DOCS_EXECUTION_CONTRACT_2026-10-08.json`; `docs/reference/CVF_NCR_C1_S1_MICROSOFT_DOCS_READ_RESULT_2026-10-08.json`; `docs/reference/CVF_NCR_C1_S1_MICROSOFT_DOCS_ABI_QUEUE_2026-10-08.json`; `docs/reference/CVF_NCR_C1_S1_MICROSOFT_DOCS_ABI_RESULT_2026-10-08.json` |
| Allowed scope source | docs/reference/CVF_NCR_C1_S1_APPROVAL_DISPATCH_DISPOSITION_2026-10-08.md Approval Record;docs/reference/CVF_NCR_C1_S1_ARCHITECTURAL_REASSESSMENT_2026-10-08.md Architecture And Progression;operator continuation |
| Before status evidence | clean at a134e4d14d817a20bd1f5f9637ce6c77d8b0b490;new source root absent |
| After status evidence | ten dispatcher documents;20 actual documentation reads;source root NOT_CREATED |
| Diff evidence | git status --short --untracked-files=all;git diff --check;hash-bound queue/results |
| Approval boundary | retained one source-only attempt;source effects await committed bound release;docs envelope spent,no further reads |
| Claim boundary | dispatch/source contract and documentary ABI only,no OS/containment/runtime proof |
| Agent type | INTERNAL_AGENT |
| Invocation ID | ncr-c1-s1-integrated-source-dispatch-20261008 |
| Expected manifest | `docs/baselines/CVF_GC018_NCR_C1_S1_INTEGRATED_SOURCE_2026-10-08.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_C1_S1_INTEGRATED_SOURCE_2026-10-08.md`; `docs/reference/CVF_NCR_C1_S1_NATIVE_SOURCE_CONTRACT_2026-10-08.md`; `docs/reference/CVF_NCR_C1_S1_NATIVE_ABI_SOURCE_BINDINGS_2026-10-08.json`; `docs/reviews/evidence/cvf-ncr-c1-s1-dispatch-design-2026-10-08.json`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_C1_S1_INTEGRATED_SOURCE_2026-10-08.json`; `docs/reference/CVF_NCR_C1_S1_MICROSOFT_DOCS_EXECUTION_CONTRACT_2026-10-08.json`; `docs/reference/CVF_NCR_C1_S1_MICROSOFT_DOCS_READ_RESULT_2026-10-08.json`; `docs/reference/CVF_NCR_C1_S1_MICROSOFT_DOCS_ABI_QUEUE_2026-10-08.json`; `docs/reference/CVF_NCR_C1_S1_MICROSOFT_DOCS_ABI_RESULT_2026-10-08.json` |
| Actual changed set | `docs/baselines/CVF_GC018_NCR_C1_S1_INTEGRATED_SOURCE_2026-10-08.md`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_C1_S1_INTEGRATED_SOURCE_2026-10-08.md`; `docs/reference/CVF_NCR_C1_S1_NATIVE_SOURCE_CONTRACT_2026-10-08.md`; `docs/reference/CVF_NCR_C1_S1_NATIVE_ABI_SOURCE_BINDINGS_2026-10-08.json`; `docs/reviews/evidence/cvf-ncr-c1-s1-dispatch-design-2026-10-08.json`; `docs/work_orders/CVF_AGENT_WORK_ORDER_NCR_C1_S1_INTEGRATED_SOURCE_2026-10-08.json`; `docs/reference/CVF_NCR_C1_S1_MICROSOFT_DOCS_EXECUTION_CONTRACT_2026-10-08.json`; `docs/reference/CVF_NCR_C1_S1_MICROSOFT_DOCS_READ_RESULT_2026-10-08.json`; `docs/reference/CVF_NCR_C1_S1_MICROSOFT_DOCS_ABI_QUEUE_2026-10-08.json`; `docs/reference/CVF_NCR_C1_S1_MICROSOFT_DOCS_ABI_RESULT_2026-10-08.json` |
| Manifest delta | MATCH |
| Deletion or rename disposition | N/A with reason: ten new dispatcher documentary files |

## External/Local Coordination Binding

```json
{"contractId":"cvf.external-local-absorption-coordination@1","invariants":{"externalRole":"ADVISORY_RESEARCH_AND_PATTERN_MAPPING","externalContext":"PUBLIC_GITHUB_AND_REFRESHED_EXTERNAL_AGENT_READ","localRole":"SOURCE_RUNTIME_VALUE_AND_PRIVATE_CVF_VERIFICATION","finalDecisionOwner":"LOCAL","localCoverageBasis":"SOURCE_DERIVED_NOT_EXTERNAL_SHORTLIST","externalEvidenceAuthority":"INPUT_NOT_PRIVATE_CVF_PROOF"},"contractSha256":"92df8a7c9492e8c3cedf624cfaa79b8185ca31442ecaf96107fd88dfcb81800c","parentArtifact":null}
```

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md |
| Input type | corpus scan or extraction intake |
| Input source | docs/reference/CVF_NCR_C1_S1_NATIVE_ABI_SOURCE_BINDINGS_2026-10-08.json;docs/reference/CVF_NCR_C1_S1_MICROSOFT_DOCS_READ_RESULT_2026-10-08.json;docs/reference/CVF_NCR_C1_S1_MICROSOFT_DOCS_ABI_RESULT_2026-10-08.json |
| Chain map route | approved bounded documentation read -> Local ABI/source specification -> exact source-only work order |
| Matching local-view guard | governance/compat/check_external_knowledge_intake_routing.py |
| Owner surface | docs/reference/CVF_NCR_S05_SUPERVISOR_SOURCE_CONTRACT_R1_2026-10-03.md;docs/reference/CVF_NCR_C1_S1_NATIVE_SOURCE_CONTRACT_2026-10-08.md |
| Disposition | Local source-derived contract;documentary facts only,not native behaviour |
| Claim boundary | no external agent or repository absorption;no source execution |

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON -20 exact documentation responses and named governed sources;no complete upstream/repository scan.

## Epistemic Process Block

Expected Result / Prediction: documentation-derived signatures and explicit review-completion resolution permit an exact source-only contract.
Evidence Comparison:20 actual HTTP200 responses,1170342 decoded B,12.781s;three retained source/custody blockers remain;canonical candidate requires real predecessor and resolution joins.
Contradiction Or Gap Disposition: current commit/working-set samples,strict disk/egress/runtime assurance remain unavailable;fail closed,do not fabricate readiness or spend more requests.
Claim Update: candidate source may be authored only after bound release;no native/source execution accepted.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY
Private provenance source packet;no public export.

## Final Post-Write Event Receipt

Explicit additional ignored trusted receipt: .cvf/runtime/ncr-c1-s1-worker/post-write-custody.json. This is within the2MiB evidence ceiling and does not add a source/repo deliverable. After actual final JSON creation and full gate completion,create this receipt exclusively with observed16 target/raw hashes,actual command/tool identities,write/gate start and end UTC,event classification,exit status and final raw gate-log SHA-256. Emit the receipt raw hash in final tool output/operator relay.

Final Markdown/JSON are immutable pre-final-event snapshots:mark their own final JSON write/gate records PLANNED_UNTIL_POST_WRITE_TOOL_EVENT,never predeclare observed final PASS/time/hash. Their S1-RETURN-GATE reference points to this post-write receipt;Local accepts completion only after the actual receipt/log bytes and hashes join. The final receipt is current tool-reported evidence,not independent OS attestation or historical R1 proof. Do not start another self-custody relay cycle for the generated receipt or modify the frozen returned files to insert their own hashes.
