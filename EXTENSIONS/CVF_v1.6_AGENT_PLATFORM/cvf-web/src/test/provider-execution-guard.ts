import {
  evaluateProviderExecutionAuthority,
  type ProviderExecutionGrant,
} from 'cvf-control-plane-foundation';
import {
  ALIBABA_DASHSCOPE_INTL_ENDPOINT,
  ALIBABA_DASHSCOPE_MAINLAND_ENDPOINT,
} from 'cvf-model-gateway';

// EAFR-R7. Egress authority is decided by destination, never by provider
// identity. The previous control mapped six hardcoded hostnames to providers
// and returned the unwrapped fetch on a lookup miss, so every destination it
// had not been told about was permitted. That default is inverted here: a
// request either resolves to a permitted destination class, or it is denied
// before any network I/O.

/**
 * Destinations that carry no provider authority and are therefore permitted
 * without a grant. This list is deliberately small and explicit: each entry is
 * a destination class the non-live suite legitimately talks to, not a
 * destination that merely happens to be unenumerated.
 */
const NON_EGRESS_PROTOCOLS = new Set(['data:', 'blob:', 'file:']);

const LOOPBACK_HOSTNAMES = new Set([
  'localhost',
  '127.0.0.1',
  '[::1]',
  '::1',
  '0.0.0.0',
]);

/**
 * Provider endpoints derived from the gateway package, which is the
 * authoritative surface for destinations. `provider-registry.ts` and
 * PROVIDER_CAPABILITY_REGISTRY are keyed by provider identity and declare no
 * hostname, so they cannot decide endpoint coverage and are deliberately not
 * used here.
 *
 * Adding an endpoint constant to the gateway brings it into coverage without
 * editing this file.
 */
const GATEWAY_DERIVED_ENDPOINTS: ReadonlyArray<readonly [string, string]> = [
  [ALIBABA_DASHSCOPE_INTL_ENDPOINT, 'alibaba'],
  [ALIBABA_DASHSCOPE_MAINLAND_ENDPOINT, 'alibaba'],
];

/**
 * Provider hostnames with no gateway endpoint constant to derive from. These
 * are still destination-keyed, never identity-keyed.
 */
const ADDITIONAL_PROVIDER_HOSTS: ReadonlyArray<readonly [string, string]> = [
  ['api.openai.com', 'openai'],
  ['api.anthropic.com', 'claude'],
  ['generativelanguage.googleapis.com', 'gemini'],
  ['openrouter.ai', 'openrouter'],
  ['api.deepseek.com', 'deepseek'],
];

function hostnameOf(endpoint: string): string | null {
  try {
    return new URL(endpoint).hostname.toLowerCase();
  } catch {
    return null;
  }
}

function buildProviderHosts(): ReadonlyMap<string, string> {
  const hosts = new Map<string, string>();
  for (const [endpoint, provider] of GATEWAY_DERIVED_ENDPOINTS) {
    const hostname = hostnameOf(endpoint);
    if (hostname) hosts.set(hostname, provider);
  }
  for (const [hostname, provider] of ADDITIONAL_PROVIDER_HOSTS) {
    hosts.set(hostname.toLowerCase(), provider);
  }
  return hosts;
}

const PROVIDER_HOSTS = buildProviderHosts();

export function providerForHostname(hostname: string): string | undefined {
  return PROVIDER_HOSTS.get(hostname.toLowerCase());
}

export function knownProviderHostnames(): readonly string[] {
  return [...PROVIDER_HOSTS.keys()].sort();
}

function parseGrant(raw: string | undefined): ProviderExecutionGrant | undefined {
  if (!raw) return undefined;
  try {
    return JSON.parse(raw) as ProviderExecutionGrant;
  } catch {
    return undefined;
  }
}

function requestUrl(input: RequestInfo | URL): URL | null {
  try {
    if (input instanceof Request) return new URL(input.url);
    return new URL(String(input));
  } catch {
    return null;
  }
}

type Decision =
  | { kind: 'permit-non-provider' }
  | { kind: 'provider'; provider: string }
  | { kind: 'deny'; reason: string };

/**
 * Classify a request destination. Anything that is not positively recognised
 * as a permitted non-provider destination or a known provider endpoint is
 * denied, so an unrecognised hostname can never reach the network.
 */
export function classifyDestination(input: RequestInfo | URL): Decision {
  const raw = input instanceof Request ? input.url : String(input);
  const url = requestUrl(input);

  if (!url) {
    // A relative URL cannot address an external host under jsdom, and an
    // unparseable one cannot be shown to be safe. Relative paths are permitted;
    // anything else unparseable is denied.
    if (
      (raw.startsWith('/') && !raw.startsWith('//'))
      || raw.startsWith('./')
      || raw.startsWith('../')
    ) {
      return { kind: 'permit-non-provider' };
    }
    return { kind: 'deny', reason: `unparseable request destination: ${raw}` };
  }

  if (NON_EGRESS_PROTOCOLS.has(url.protocol)) {
    return { kind: 'permit-non-provider' };
  }

  if (url.protocol !== 'http:' && url.protocol !== 'https:') {
    return { kind: 'deny', reason: `unsupported protocol ${url.protocol}` };
  }

  const hostname = url.hostname.toLowerCase();

  const provider = PROVIDER_HOSTS.get(hostname);
  if (provider) {
    return { kind: 'provider', provider };
  }

  if (LOOPBACK_HOSTNAMES.has(hostname) || hostname.endsWith('.localhost')) {
    return { kind: 'permit-non-provider' };
  }

  // Default deny. An unrecognised hostname is not evidence that the request is
  // not provider traffic: it may be a mainland endpoint, an environment
  // override, or a caller-supplied endpoint paired with a covered providerId.
  return {
    kind: 'deny',
    reason:
      `unrecognised egress destination ${hostname}; provider egress requires a ` +
      'known provider endpoint and an orchestrator grant',
  };
}

export function createProviderExecutionFetchGuard(
  fetchImpl: typeof fetch,
  env: Readonly<Record<string, string | undefined>> = process.env,
  now: () => Date = () => new Date(),
): typeof fetch {
  let consumedCalls = 0;

  return (async (input: RequestInfo | URL, init?: RequestInit) => {
    const decision = classifyDestination(input);

    if (decision.kind === 'deny') {
      throw new Error(`CVF_PROVIDER_EXECUTION_DENIED: ${decision.reason}`);
    }

    if (decision.kind === 'permit-non-provider') {
      return fetchImpl(input, init);
    }

    const grant = parseGrant(env.CVF_PROVIDER_EXECUTION_GRANT_JSON);
    const result = evaluateProviderExecutionAuthority(grant, {
      workerAgentId: env.CVF_AGENT_ID ?? '',
      delegationId: env.CVF_DELEGATION_ID ?? '',
      grantId: env.CVF_PROVIDER_EXECUTION_GRANT_ID ?? '',
      provider: decision.provider,
      consumedCalls,
      nowIso: now().toISOString(),
    });
    if (!result.allowed) {
      throw new Error(`CVF_PROVIDER_EXECUTION_DENIED: ${result.reason}`);
    }
    consumedCalls += 1;
    return fetchImpl(input, init);
  }) as typeof fetch;
}
