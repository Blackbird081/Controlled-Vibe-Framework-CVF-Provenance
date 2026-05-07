<!-- Memory class: FULL_RECORD -->

# CVF W133 CP1 — SSE/Connection Lifecycle Investigation

Date: 2026-05-07
Status: COMPLETE — root causes identified

---

## Finding 1: Route Does Not Use SSE

**The `/api/execute` route does NOT use SSE or streaming at the route level.**

All responses are plain JSON via `NextResponse.json()`. The word "SSE" in the W132
root cause classification was imprecise — the actual failure is at the HTTP
connection pool level, not a streaming/event-source channel.

File: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/app/api/execute/route.ts`

All return paths use `NextResponse.json(...)`. There are no `ReadableStream`,
`TransformStream`, `EventSource`, or `text/event-stream` patterns in the route.

---

## Finding 2: TCP Keep-Alive Connection Pool (Primary Root Cause)

**Root cause: stale HTTP keep-alive connection after J1's long provider request.**

The Alibaba provider uses Node.js `fetch` with `AbortSignal.timeout(85_000)`:

```typescript
// providers.ts:238-260
const response = await fetch(
  'https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions',
  {
    headers: { 'Content-Type': '...', 'Authorization': '...' },
    body: JSON.stringify({...}),
    signal: AbortSignal.timeout(85_000),
  }
);
```

J1 takes ~33s (qwen-plus) or ~15s (qwen-turbo). Node.js's undici HTTP pool retains
the keep-alive connection to `dashscope-intl.aliyuncs.com` after J1 completes. The
DashScope server may have closed or invalidated that connection on their side (common
after a ~30s long request). When J2 starts ~1s later, undici attempts to reuse the
stale pooled connection. The OS-level TCP stack must detect the dead connection
(RST/FIN from the server, or a TCP keepalive probe timeout), which can take up to
the full OS TCP timeout before failing.

This explains:
- `provider_timeout` (HTTP 400): the 85s AbortSignal fires and returns a classified error
- `execute_route_timeout` (HTTP —): the TCP detection stalls; the response arrives
  after the Playwright 90s timeout has already fired

**Evidence ruling out alternative hypotheses:**

| Hypothesis | Evidence against |
|---|---|
| Provider RPM limit | qwen-plus (higher RPM) shows identical failure pattern — rules out RPM |
| Alibaba-specific | DeepSeek shows identical pattern — rules out single-provider issue |
| Form type | J9 (`documentation`) fails even though J1 (`documentation`) passes — rules out form type |
| Browser session cascade | CP1 isolated BrowserContext confirmed 0 cascade failures — rules out browser |

**The consistent 93s elapsed time for execute_route_timeout cases is consistent with
the Playwright 90s page timeout firing just before Node.js detects the TCP failure.**

---

## Finding 3: user_persona Route Miss (Secondary — Independent of Connection Issue)

**Root cause: wizard detection takes precedence over trusted form routing.**

File: `EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/intent-router.ts:121-142`

The intent router checks wizard detection first:
```typescript
const detected = detectIntent(userInput);
const isWeak = detected.suggestedTemplates.length === 0;

// Precedence 1: wizard route (runs BEFORE form route check)
if (!isWeak) {
  return { ..., routeType: 'wizard', ... };
}

// Precedence 2: trusted form (only when NO wizard matched)
const formMatch = routeToTrustedForm(userInput);
```

The `user_persona` form IS registered in:
`EXTENSIONS/CVF_v1.6_AGENT_PLATFORM/cvf-web/src/lib/form-routing.ts:85-97`

with patterns: `user persona`, `buyer persona`, `target audience`, `customer profile`,
`ideal customer`, `người dùng mục tiêu`.

But if `detectIntent()` returns ANY wizard suggestion (e.g., product-design wizard
matching "product design" in the same prompt), Precedence 1 fires and the form
route check never runs. The CTA button is disabled (`routeType: null`).

This is a **pure routing precedence bug** — `user_persona` routes correctly when
no wizard matches, but wizard detection short-circuits the check.

---

## Recommended Fixes

### Fix A — TCP connection: add `Connection: close` to provider fetch (CP2)

Add `'Connection': 'close'` to the headers of Alibaba and DeepSeek provider fetch
calls. This tells both the client and server not to reuse the connection, ensuring
J2 always gets a fresh TCP connection.

Also reduce `AbortSignal.timeout` from 85s to 60s to provide more headroom before
the 90s Playwright limit.

### Fix B — Routing: check form routes BEFORE wizard detection (CP3)

Swap the routing precedence in `intent-router.ts`:
1. Run `routeToTrustedForm(userInput)` first
2. If a form matches, return the form route
3. Only fall through to wizard detection if no form matched

This is safe: trusted forms use specific multi-word patterns that rarely conflict
with wizard intents. The `wizardWinsWhen` field in form-routing.ts documents edge
cases but those are documented advisor notes, not enforced by code.

### Fix C — E2E inter-journey delay (CP2 fallback)

Add a 1–2s `waitForTimeout` between journeys in the E2E spec as a defensive
measure to allow the OS TCP stack to flush connections between journeys.

---

## Files Changed By Fixes

- `src/lib/ai/providers.ts` — Fix A (Connection: close + reduced timeout)
- `src/lib/intent-router.ts` — Fix B (precedence swap)
- `tests/e2e/w133-runtime-stability.live.spec.ts` — new spec + inter-journey delay
