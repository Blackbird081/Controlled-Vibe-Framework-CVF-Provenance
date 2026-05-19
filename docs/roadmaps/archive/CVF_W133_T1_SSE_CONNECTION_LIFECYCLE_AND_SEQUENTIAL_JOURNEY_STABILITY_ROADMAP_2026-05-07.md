<!-- Memory class: SUMMARY_RECORD -->

# CVF W133-T1 SSE Connection Lifecycle And Sequential Journey Stability Roadmap

> Date: 2026-05-07
> Status: AUTHORIZED — NOT YET DELIVERED
> Authorization: `docs/baselines/CVF_GC018_W133_T1_SSE_CONNECTION_LIFECYCLE_AND_SEQUENTIAL_JOURNEY_STABILITY_AUTHORIZATION_2026-05-07.md`
> Predecessor: W132-T1 CLOSED WITH CLASSIFIED BLOCKER `sequential_journey_failure_server_side_connection`
> Wave ID: W133

---

## 0. Why This Is Next

W132 classified a consistent cross-provider failure:

- Journey 1 always succeeds (~15–33s)
- Journeys 2+ always timeout at ~93s
- 3 independent runs (qwen-turbo ×2, qwen-plus ×1), both Alibaba and DeepSeek
- Acceptance rate: 8.3% Alibaba / 16.7% DeepSeek — effectively single-journey only

Root cause classification: `sequential_journey_failure_server_side_connection` — the
server-side SSE or streaming connection on `/api/execute` is likely not fully
released after J1 completes, blocking J2+ requests.

W133 must:

1. Confirm and fix the connection lifecycle issue at the code level
2. Add `user_persona` intent router routing (secondary blocker)
3. Prove the fix restores multi-journey acceptance rates

---

## 1. Product Claim Target

W133 should make this bounded claim true:

> CVF's noncoder path can complete at least 8 of 12 sequential Alibaba journeys
> and 3 of 6 DeepSeek journeys with evidence receipts, measured in isolated
> per-journey browser contexts.

This is not a claim of 100% reliability, provider parity, or production readiness.

---

## 2. Non-Goals

- No new noncoder feature
- No new template or routing corpus expansion beyond `user_persona` fix
- No provider parity claim
- No mock-mode substitution for governance proof
- No raw key printing or storage
- No claim of SSE fix beyond what live evidence supports

---

## 3. Checkpoints

### CP0 — Authorization Verification

Verify:

- GC-018 `CVF_GC018_W133_T1_*` exists and is committed
- W132 classified blocker is recorded in `docs/reviews/CVF_W132_CONTINUATION_DECISION_2026-04-30.md`
- Working tree is clean

**Acceptance:** all gates clear.

### CP1 — SSE Connection Lifecycle Investigation

Investigate the `/api/execute` route to determine why J2+ requests block or
timeout after J1 completes.

**Investigate:**

- How `/api/execute` streams the AI response (SSE, chunked transfer, or plain JSON)
- Whether the Next.js server keeps any per-route state across requests
- Whether the server-side streaming connection is explicitly closed/aborted after response
- Whether there is a connection pool, queue, or concurrency limit that a long J1 response exhausts
- Whether adding an explicit `AbortController` or response cleanup after J1 would unblock J2

**Deliver:**

- `docs/reviews/CVF_W133_SSE_INVESTIGATION_2026-05-07.md` — code-level finding with file:line citations

**Acceptance:**

- Root cause confirmed OR alternative hypothesis recorded with evidence
- Finding is code-level (not a guess)
- No live provider call required for investigation

### CP2 — Connection Lifecycle Fix

Apply the narrowest fix justified by CP1.

Candidate fixes (in order of preference):

1. Add explicit stream termination / abort on the `/api/execute` response after
   the AI response is complete — prevent the server from holding a half-open
   connection
2. Add a short configurable inter-journey delay (2–5s) to the E2E spec as a
   workaround if root cause cannot be fixed at the route level
3. Both if the investigation reveals both issues

**Acceptance:**

- Fix is scoped to the current governed execution path
- No new provider behavior is introduced
- Unit or route-level test coverage added if fix changes `/api/execute` behavior

### CP3 — user_persona Routing Fix

Extend the intent router to recognize `user_persona` form-type prompts and route
them with ≥80% confidence to the `user_persona` template.

**Investigate:**

- Current intent router logic for form-type → template routing
- Why `user_persona` produces `route_miss` (fast failure at ~17s, no timeout)
- Whether the router uses form-type label directly or relies on prompt text matching

**Fix:**

- Add `user_persona` as a recognized intent with a confident template binding
- Add a unit test covering `user_persona` → correct template route

**Acceptance:**

- `user_persona` form type routes without `route_miss` in targeted unit test
- No regression on existing routing coverage

### CP4 — Alibaba Re-Run

Re-run the isolated-session live spec on Alibaba `qwen-plus` with all noncoder
flags enabled.

**Acceptance:**

- At least 12 attempted browser UI journeys
- At least 8 accepted-with-receipt OR a new classified blocker
- Zero cascade failures from browser context collapse
- Evidence written to `docs/reviews/CVF_W133_RUNTIME_STABILITY_ALIBABA_EVIDENCE_2026-05-07.md`

### CP5 — DeepSeek Confirmatory Re-Run

Re-run on DeepSeek `deepseek-chat`.

**Acceptance:**

- At least 6 attempted browser UI journeys
- At least 3 accepted-with-receipt OR a new classified blocker
- Evidence written to `docs/reviews/CVF_W133_RUNTIME_STABILITY_DEEPSEEK_EVIDENCE_2026-05-07.md`

### CP6 — Continuation Decision

Publish `docs/reviews/CVF_W133_CONTINUATION_DECISION_2026-05-07.md`.

Decision rules:

- If acceptance rate meets targets → claim W133 delivered, open W134 or close the stability tranche
- If new classified blocker emerges → record root cause and decide next tranche
- If user_persona fix works but connection lifecycle remains unresolved → classify separately

**Acceptance:**

- W134 or closure is data-backed
- No capability expansion chosen while instability persists

### CP7 — Release Gate

Run:

```bash
python scripts/run_cvf_release_gate_bundle.py --json
```

**Acceptance:**

- All 7 checks pass
- No raw key values in logs or committed artifacts
- W133 roadmap status changes to CLOSED only after CP4-CP7 evidence exists

---

## 4. Exit Criteria

W133 can close when:

- SSE/connection lifecycle investigation finding is published
- Fix committed (or classified reason for deferral)
- `user_persona` routing fixed with unit test
- Alibaba re-run: ≥8/12 accepted OR new classified blocker
- DeepSeek re-run: ≥3/6 accepted OR new classified blocker
- Continuation decision published from data
- Release gate PASS

---

## 5. Execution Locks

1. Do not add new user-facing capability.
2. Do not expand routing corpus beyond `user_persona`.
3. Do not count mock fallback as governance proof.
4. Do not count API-only calls as UI proof.
5. Do not print raw provider keys.
6. Do not claim provider parity.
7. Do not close W133 from unit tests alone.
8. Keep W133 claims narrower than the measured evidence.
