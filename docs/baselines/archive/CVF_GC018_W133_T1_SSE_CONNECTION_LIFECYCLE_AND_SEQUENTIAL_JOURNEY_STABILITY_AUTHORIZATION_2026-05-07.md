<!-- Memory class: SUMMARY_RECORD -->

# CVF GC-018 — W133-T1 Authorization

> Type: TRANCHE AUTHORIZATION
> Tranche: W133-T1 — SSE Connection Lifecycle And Sequential Journey Stability
> Date: 2026-05-07
> Predecessor closure: W132-T1 CLOSED WITH CLASSIFIED BLOCKER `sequential_journey_failure_server_side_connection`
> Operator: CVF core team

---

## 1. Authorization Decision

**AUTHORIZED.** W133-T1 may begin immediately.

W133 is authorized because W132 measured a consistent, cross-provider failure
pattern across 3 independent runs: Journey 1 always succeeds, Journeys 2+ always
timeout at ~93s regardless of model tier (qwen-turbo, qwen-plus) or provider
(Alibaba, DeepSeek). The root cause was classified as
`sequential_journey_failure_server_side_connection` — the server-side SSE or
streaming connection on `/api/execute` is likely not fully released after J1
completes, blocking J2+ requests.

This authorization approves:

- server-side SSE/streaming connection lifecycle investigation and fix
- inter-journey delay as a controlled fallback
- `user_persona` intent router routing coverage fix
- re-run of the full stability matrix to verify acceptance targets

This authorization does not approve new product features, provider parity claims,
or new governance behavior.

---

## 2. Predecessor Evidence

| Artifact | Role |
|---|---|
| `docs/roadmaps/CVF_W132_T1_PROVIDER_RUNTIME_STABILITY_AND_BROWSER_SESSION_HARDENING_ROADMAP_2026-04-30.md` | W132 roadmap — CLOSED WITH CLASSIFIED BLOCKER |
| `docs/reviews/CVF_W132_CONTINUATION_DECISION_2026-04-30.md` | CP6 continuation decision — root cause `sequential_journey_failure_server_side_connection` |
| `docs/reviews/CVF_W132_RUNTIME_STABILITY_ALIBABA_EVIDENCE_2026-04-30.md` | Alibaba evidence — qwen-plus run, 1/12 accepted (8.3%) |
| `docs/reviews/CVF_W132_RUNTIME_STABILITY_DEEPSEEK_EVIDENCE_2026-04-30.md` | DeepSeek confirmatory — 1/6 accepted (16.7%) |

W132 measured (3-run summary):

| Run | Date | Model | Alibaba accepted | DeepSeek accepted | Pattern |
|---|---|---|---|---|---|
| 1 | 2026-04-30 | qwen-turbo | 1/12 (8.3%) | 1/6 (16.7%) | J1 pass, J2+ fail at ~95s |
| 2 | 2026-05-07 | qwen-turbo | 1/12 (8.3%) | 1/6 (16.7%) | J1 pass, J2+ fail at ~93s |
| 3 | 2026-05-07 | qwen-plus | 1/12 (8.3%) | 1/6 (16.7%) | J1 pass, J2+ fail at ~93s |

Key observations ruling out alternative hypotheses:

- Same form type (J9 `documentation`) fails even though J1 `documentation` passes — rules out form type
- DeepSeek shows identical pattern — rules out Alibaba-specific issue
- `qwen-plus` (higher RPM tier) shows identical result — rules out provider RPM

---

## 3. Proposed Tranche

**W133-T1 — SSE Connection Lifecycle And Sequential Journey Stability**

Roadmap: `docs/roadmaps/CVF_W133_T1_SSE_CONNECTION_LIFECYCLE_AND_SEQUENTIAL_JOURNEY_STABILITY_ROADMAP_2026-05-07.md`

---

## 4. GC-018 Continuation Candidate Packet

```
GC-018 Continuation Candidate
- Candidate ID: CVF-W133-SSE-LIFECYCLE-2026-05-07
- Date: 2026-05-07
- Parent roadmap / wave: W132-T1 CLOSED WITH CLASSIFIED BLOCKER b957fbc3
- Proposed scope: Fix server-side SSE/streaming connection lifecycle between sequential noncoder journeys; fix user_persona routing gap; re-run stability matrix
- Continuation class: REALIZATION
- Active quality assessment: docs/reviews/CVF_W132_CONTINUATION_DECISION_2026-04-30.md
- Assessment date: 2026-05-07
- Weighted total: 4.0/10 (post-W132 measured state — sequential failure rate 91%)
- Lowest dimension: Runtime Stability (1.5/10) — J2+ failure rate 91% across 3 runs
- Quality-first decision: REMEDIATE_FIRST
- Remediation target if not expanding: Fix sequential_journey_failure_server_side_connection before any new feature expansion
- Why now: W132 classified the exact blocker with 3-run cross-provider evidence. The root cause (SSE connection not released between journeys) is narrow and addressable. user_persona routing gap is a deterministic intent-router fix. Both fixes are required before noncoder throughput can improve.
- Active-path impact: MATERIAL — current noncoder acceptance rate 8.3%/16.7%; J2+ always fail
- Risk if deferred: Noncoder path remains effectively single-journey only; CVF cannot claim stable multi-step noncoder execution
- Lateral alternative considered: YES
- Why not lateral shift: Lateral would be to add long inter-journey delays (60s+) as a workaround. Rejected as primary fix because it does not address root cause and would make the test suite impractical. Acceptable as a short-term fallback only.
- Real decision boundary improved: YES — resolves the cross-provider sequential failure that makes current noncoder throughput unmeasurable
- Expected enforcement class:
  - RUNTIME_GUARD
- Required evidence if approved:
  - SSE/streaming connection investigation note (code-level finding)
  - Connection lifecycle fix committed to /api/execute route
  - user_persona routing fix with intent router coverage
  - Re-run: ≥12 Alibaba journeys, ≥8 accepted-with-receipt OR new classified blocker
  - Re-run: ≥6 DeepSeek journeys, ≥3 accepted OR new classified blocker
  - Release gate PASS post-fix
```

---

## 5. Depth Audit

| Dimension | Score | Note |
|---|---|---|
| Risk reduction | 3 | High — removes the primary single-journey constraint |
| Decision value | 2 | Proves or disproves SSE connection hypothesis |
| Machine enforceability | 2 | Narrow code-level fix, unit + E2E proof possible |
| Operational efficiency | 2 | Unblocks all noncoder journeys beyond J1 |
| Portfolio priority | 2 | Required before any new noncoder feature |
| **Total** | **11** | **CONTINUE** |

Decision: AUTHORIZED. Blocking fix for the only path to stable noncoder throughput.

---

## 6. Exit Criteria

W133 can close when:

- SSE/streaming connection lifecycle is investigated and a root cause code finding is published
- A fix (or classified reason for no fix) is committed to `/api/execute`
- `user_persona` form type routes to the correct template with ≥80% confidence
- Alibaba re-run achieves ≥8/12 accepted-with-receipt OR publishes a new classified blocker
- DeepSeek re-run achieves ≥3/6 accepted-with-receipt OR publishes a new classified blocker
- Release gate PASS
- Continuation decision published

---

## 7. Execution Locks

1. Do not add new user-facing capability.
2. Do not claim noncoder parity or provider parity.
3. Do not count mock output as governance proof.
4. Do not close W133 from unit tests alone.
5. Do not print raw provider keys.
6. Keep W133 claims narrower than the measured evidence.
