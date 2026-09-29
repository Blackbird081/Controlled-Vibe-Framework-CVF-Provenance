# CVF GC-018 Baseline - MCP-KAR-T1 MCP 2026-07-28 Normative Invariant Profile

Memory class: governed-dispatch-baseline

Status: DISPATCH_READY

docType: baseline

Date: 2026-08-23

Batch ID: MCP-KAR-T1

Dispatch base head: 6490b36143256c1b4835af97ede4af03c41cabb6

Commit mode: WORKER_MUST_NOT_COMMIT

Decision owner: CVF operator

Reviewer owner: CVF reviewer/closer

Worker target: current CVF agent in a bounded no-commit implementation role

## Purpose

Authorize one CVF-native, provider-free contract profile for selected normative
MCP `2026-07-28` invariants and focused negative conformance tests. Convert the
T0 findings into an existing-owner enrichment without importing or activating
an MCP client, server, transport, package, or provider path.

## Scaffold Provenance Block

| Field | Value |
| --- | --- |
| scaffoldHelperCommand | `python governance/compat/build_dispatch_packet_scaffold.py --packet-kind mcp-cli-adapter --batch-id MCP-KAR-T1 --title "MCP 2026-07-28 Normative Invariant Profile And Negative Conformance" --date 2026-08-23 --base 6490b36143256c1b4835af97ede4af03c41cabb6 --commit-mode WORKER_MUST_NOT_COMMIT --include-worker-return-skeleton --stdout` |
| generatedProfile | mcp-cli-adapter plus WORKER_MUST_NOT_COMMIT no-commit worker profile |
| generatedSkeletonStatus | USED_AS_STARTING_POINT |
| manualEditsAfterScaffold | replaced stubs with the T0 decision, pinned normative sources, current owner boundary, exact local outputs, negative cases, and no-runtime prohibitions |
| checkerReadAheadConfirmation | dispatch quality, structural completeness, prompt envelope, operation trace, scaffold provenance, task routing, public export, and worker-return checker sources reviewed |
| docOnlyNewFields | `normativeInvariantSet`; `negativeConformanceSet`; `pureDecisionBoundary` |
| claimBoundary | dispatch provenance and bounded local implementation authority only; no runtime, provider, live, public, package, deployment, or production claim |

## ADIF Defect Registry Disclosure

Resolver query: taskClass=`pure-local-implementation`, role=`dispatcher`, lifecyclePhase=`dispatch`.

Returned defects: NONE_RETURNED.

| Field | Value |
| --- | --- |
| Resolver command | `python governance/compat/run_adif_defect_resolver.py --task-class "pure-local-implementation" --role dispatcher --lifecycle-phase dispatch --risk-ceiling HIGH --max-results 20 --json` |
| Returned defect count | 0 |
| Returned defects | none |
| Disclosed defectIds | none |
| Dispatch impact | no registered ADIF defect changes this bounded route |

## Checker Source Read-Ahead Block

| Field | Value |
| --- | --- |
| applicableCheckersRead | `governance/compat/check_work_order_dispatch_quality.py`; `governance/compat/check_markdown_structural_completeness.py`; `governance/compat/check_agent_operation_trace.py`; `governance/compat/check_dispatch_scaffold_provenance.py`; `governance/compat/check_dispatch_prompt_envelope.py`; `governance/compat/check_task_governance_route.py` |
| literalTokensReviewed | Source Verification Block; Negative Search And Collision Discipline; MCP/CLI Adapter Boundary; Public Export Disposition |
| gateRunPurpose | confirm authored evidence and exact packet shape, not discover requirements after dispatch |
| claimBoundary | read-ahead covers dispatch and local artifact shape, not runtime behavior or protocol certification |

## Source Verification Block

| Claimed item | Claim type | Source file | Verified line/section | Verified path or symbol | Owning interface/function/schema | Disposition |
| --- | --- | --- | --- | --- | --- | --- |
| per-request version and capabilities | normative protocol fact | `.private_reference/source_mirrors/modelcontextprotocol__modelcontextprotocol/docs/specification/2026-07-28/basic/index.mdx` | `_meta`; Per-request protocol fields | `io.modelcontextprotocol/protocolVersion`; `io.modelcontextprotocol/clientCapabilities` | MCP request metadata | ACCEPT |
| version and extension negotiation | normative protocol fact | `.private_reference/source_mirrors/modelcontextprotocol__modelcontextprotocol/docs/specification/2026-07-28/basic/versioning.mdx` | Protocol Version Negotiation; Extension Negotiation | supported versions; capability extension identifiers | MCP versioning contract | ACCEPT |
| subscription acknowledgment and correlation | normative protocol fact | `.private_reference/source_mirrors/modelcontextprotocol__modelcontextprotocol/docs/specification/2026-07-28/basic/patterns/subscriptions.mdx` | Acknowledgment; Receiving Notifications | `io.modelcontextprotocol/subscriptionId` | MCP subscription pattern | ACCEPT |
| input-required is an incomplete continuation | normative protocol fact | `.private_reference/source_mirrors/modelcontextprotocol__modelcontextprotocol/docs/specification/2026-07-28/basic/patterns/mrtr.mdx` | InputRequiredResult; Basic Workflow | `InputRequiredResult.resultType` | MCP MRTR pattern | ACCEPT |
| header/body mismatch fails closed | normative transport fact | `.private_reference/source_mirrors/modelcontextprotocol__modelcontextprotocol/docs/specification/2026-07-28/basic/transports/streamable-http.mdx` | Request Metadata; Header Validation | `HeaderMismatch`; `MCP-Protocol-Version` | MCP Streamable HTTP contract | ACCEPT |
| discovery identity is self-reported | normative trust fact | `.private_reference/source_mirrors/modelcontextprotocol__modelcontextprotocol/docs/specification/2026-07-28/server/discover.mdx` | Data Types / DiscoverResult note | `serverInfo` | MCP discovery result | ACCEPT |
| cache hints do not authorize access | normative cache/security fact | `.private_reference/source_mirrors/modelcontextprotocol__modelcontextprotocol/docs/specification/2026-07-28/server/utilities/caching.mdx` | Cacheable Model; Security Considerations | `ttlMs`; `cacheScope` | MCP caching hints | ACCEPT |
| token audience must bind to the target server | normative authorization fact | `.private_reference/source_mirrors/modelcontextprotocol__modelcontextprotocol/docs/specification/2026-07-28/basic/authorization/index.mdx` | Resource Parameter Implementation; Token Handling | RFC 8707 `resource`; intended audience | MCP authorization contract | ACCEPT |
| current CVF owner parks executable runtime | CVF owner fact | `docs/reference/mcp_gateway/CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY.md` | Bridge Readiness Ruling; Claim Boundary | `Bridge Readiness Ruling` | MCP gateway reference owner | ACCEPT |

## External Repository Absorption Entry Control

NOT_APPLICABLE_WITH_REASON: this tranche does not open or rescan an external
repository. It consumes only the selected, pinned cluster already inventoried,
classified, and reviewer-accepted by MCP-KAR-T0.

## Mandatory Blind-Spot Control Block

T0 counts and external-agent prose are not implementation evidence. Every T1
rule must cite the pinned normative section, map to a current CVF owner, and be
proved by a negative semantic assertion; unselected corpus material grants no
scope.

## Corpus Completeness And Report Integrity

- Corpus verdict: NOT_APPLICABLE_WITH_REASON - no new corpus scan or completeness
claim occurs in T1; the immutable T0 receipt is referenced only as predecessor
evidence and the selected files are read directly.

## Overlap And Novelty Classification

| Source item or group | Existing CVF owner surface checked | Overlap disposition | Novelty / delta | Action |
| --- | --- | --- | --- | --- |
| protocol and transport invariants | `docs/reference/mcp_gateway/` | ENRICH_EXISTING | pinned normative rule profile | ADAPT |
| deterministic admission decisions | `EXTENSIONS/CVF_EXECUTION_PLANE_FOUNDATION/` | ENRICH_EXISTING | typed fail-closed local interface | ADAPT |
| executable MCP client/server behavior | `docs/reference/mcp_gateway/CVF_MODEL_GATEWAY_MCP_RUNTIME_BRIDGE_BOUNDARY.md` | CONFIRMED_EXISTING | no runtime delta in T1 | DEFER |

## External Knowledge Intake Routing

| Field | Value |
| --- | --- |
| Chain map | `docs/reference/external_agent_review/CVF_EXTERNAL_KNOWLEDGE_ABSORPTION_CHAIN_MAP.md` |
| Input type | external repo or copied folder |
| Chain map route | T0 receipt and semantic audit to operator-selected T1 to current CVF owners |
| Matching local-view guard | `governance/compat/check_external_knowledge_intake_routing.py`; `governance/compat/check_external_absorption_overlap_discipline.py`; `governance/compat/check_absorption_blindspot_control_presence.py` |
| Owner surface | paired MCP-KAR-T1 baseline and work order |
| Disposition | ADAPT selected normative delta; no direct import |
| Claim boundary | no new corpus intake, runtime, package, provider, public, or production claim |

## Negative Search And Collision Discipline

| Check | Evidence | Disposition |
| --- | --- | --- |
| path existence | all six proposed MCP-KAR-T1 artifact paths returned `False` before authoring | PASS |
| token search | `rg -n "MCP-KAR-T1|MCP_KAR_T1|MCP 2026-07-28 Normative Invariant Profile" docs CVF_SESSION EXTENSIONS` returned no prior lane | PASS |
| collision decision | enrich `docs/reference/mcp_gateway/` and execution-plane contract ownership; create no parallel runtime owner | ACCEPT |

## Source / Predecessor Evidence

T0 closed selectively at material commit `79e588b0912ea6e8731140f21b90baebf3b7c099`.
Its audit identified these invariants as retained value and demonstrated that
the external redesign schemas accepted invalid cross-field states. The operator
then selected this separate T1 at continuity commit `6490b36143256c1b4835af97ede4af03c41cabb6`.

## Decision / Proposed Tranche

Implement a pure deterministic validation profile under the existing
execution-plane owner, document its normative mapping under the existing MCP
gateway reference owner, and prove rejection behavior with local tests.

## Evidence Requirements

- Each implemented rule maps to a pinned upstream section and a stable CVF rule ID.
- Negative tests cover missing metadata, unsupported versions/capabilities,
  unnegotiated extensions, subscription ordering/correlation, MRTR state,
  unsafe cache hints, token audience mismatch, and HTTP header/body mismatch.
- Type checking and the focused Vitest file pass without network or provider use.
- No code path opens sockets, performs I/O, registers tools, or activates MCP.

## MCP/CLI Adapter Boundary

| Field | Value |
| --- | --- |
| Adapter scope | pure data types and deterministic decisions only; no transport or executable adapter |
| No-runtime-overclaim | This packet does not claim the profile executes, intercepts, wraps, connects to, or certifies an MCP runtime. |

## Claim Boundary

This baseline authorizes the exact private, local profile, reference, test, and
review outputs named by the paired work order. It does not authorize runtime or
provider calls, MCP client/server activation, dependency installation, package
publication, public sync, deployment, production, or changes to repository
boundaries.

## Public Export Disposition

DEFERRED_PRIVATE_ONLY

Reason: MCP-KAR-T1 is a private provenance implementation and review tranche;
no public-sync batch is authorized.
