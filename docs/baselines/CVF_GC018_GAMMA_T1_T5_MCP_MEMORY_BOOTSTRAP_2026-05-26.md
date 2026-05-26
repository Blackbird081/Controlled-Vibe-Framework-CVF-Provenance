# CVF GC-018 Gamma-T1-T5 MCP Memory Bootstrap

Memory class: BASELINE_RECORD

docType: baseline

Date: 2026-05-26

Status: AUTHORIZED_BY_OPERATOR_FOR_FULL_GAMMA_IMPLEMENTATION

## Purpose

Authorize bounded implementation of Gamma after Gamma-T0 selected reuse of
`EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER` as the substrate.

## Source / Predecessor

- `docs/roadmaps/CVF_CROSS_AGENT_MEMORY_PROGRESSION_ROADMAP_2026-05-26.md`
- `docs/reviews/CVF_GAMMA_T0_MCP_SERVER_READINESS_AUDIT_COMPLETION_2026-05-26.md`
- Existing MCP package:
  `EXTENSIONS/CVF_ECO_v2.5_MCP_SERVER/`
- Current official MCP TypeScript SDK docs checked before implementation:
  `https://modelcontextprotocol.io/docs/sdk`,
  `https://modelcontextprotocol.io/docs/develop/build-server`, and
  `https://ts.sdk.modelcontextprotocol.io/documents/server.html`.

## Decision / Baseline

The operator requested continuing through the full Gamma sequence and will
perform operator/client testing after completion.

This GC-018 authorizes a single bounded Gamma implementation packet covering:

- T1/T2: read-only MCP memory bootstrap tools;
- T3: read-only governance rule/action tools;
- T4: local setup guide;
- T5: local SDK-client stdio verification.

## Knowledge Absorption Blind-Spot Control Block

Verdict: CLEAR_FOR_BOUNDED_GAMMA_IMPLEMENTATION.

1. Standard read: WC-4 remains binding because this tranche touches memory,
   tool, MCP, and governance-startup surfaces.
2. Source inventory:
   - existing MCP package and README;
   - Gamma-T0 audit;
   - cross-agent memory progression roadmap;
   - active session state and handoff;
   - official MCP TypeScript SDK/build-server docs;
   - W3 tool/MCP/database taxonomy boundary.
3. Prior evidence resolved:
   - Alpha/Beta remain soft startup-accountability bridges;
   - Gamma-T0 selected reuse/adaptation rather than new server tree;
   - W3 did not authorize arbitrary MCP execution.
4. Accepted value:
   - stdio MCP server remains the transport;
   - existing seven guard tools remain;
   - new tools read repo state and rules with secret redaction;
   - audit records Gamma MCP tool-call metadata.
5. Deferred:
   - third-party client auto-start proof by operator;
   - persistent audit storage;
   - Alpha/Beta retirement;
   - public package publication;
   - hosted/production hardening.
6. Rejected:
   - provider/API route changes;
   - remote MCP transport;
   - write/mutation MCP tools;
   - raw secret output.
7. Adversarial role review:
   - Implementer: reuse server.tool pattern already used by package.
   - Auditor: verify through SDK client, not only unit tests.
   - Product/operator advocate: startup ack and state tools reduce agent
     memory loss.
   - Boundary owner: keep claims local and private.
8. Blind-spot delta: external client-specific config remains operator-tested
   because this shell can run local SDK-client verification but not every
   operator UI client.

## Scope

In scope:

- Add read-only startup memory tools.
- Add read-only governance rule/action tools.
- Add secret-safe MCP tool-call audit for Gamma tools.
- Add local setup guide.
- Add local SDK-client verification script.
- Update roadmap/session/handoff.

Out of scope:

- Provider/API-key calls.
- `/api/execute` changes.
- Remote MCP transport.
- Public-sync.
- Persistent audit database.
- External GUI client proof.
- Hosted readiness, production readiness, or freeze release.

## Evidence / Verification

Required:

- MCP package build PASS.
- MCP package tests PASS.
- Local SDK-client stdio verification PASS.
- Governance docs/session gates PASS.

## Claim Boundary

This GC-018 can close only local Gamma MCP memory bootstrap. It cannot claim
universal client auto-start, hosted availability, public readiness, production
readiness, provider behavior, route behavior, Alpha/Beta retirement, or freeze
release.
