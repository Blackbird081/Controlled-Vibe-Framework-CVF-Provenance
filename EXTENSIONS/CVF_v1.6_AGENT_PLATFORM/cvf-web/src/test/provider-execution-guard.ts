import {
  evaluateProviderExecutionAuthority,
  type ProviderExecutionGrant,
} from 'cvf-control-plane-foundation';

const PROVIDER_HOSTS: Record<string, string> = {
  'api.openai.com': 'openai',
  'api.anthropic.com': 'claude',
  'generativelanguage.googleapis.com': 'gemini',
  'dashscope-intl.aliyuncs.com': 'alibaba',
  'openrouter.ai': 'openrouter',
  'api.deepseek.com': 'deepseek',
};

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

export function createProviderExecutionFetchGuard(
  fetchImpl: typeof fetch,
  env: Readonly<Record<string, string | undefined>> = process.env,
  now: () => Date = () => new Date(),
): typeof fetch {
  let consumedCalls = 0;

  return (async (input: RequestInfo | URL, init?: RequestInit) => {
    const url = requestUrl(input);
    const provider = url ? PROVIDER_HOSTS[url.hostname] : undefined;
    if (!provider) return fetchImpl(input, init);

    const grant = parseGrant(env.CVF_PROVIDER_EXECUTION_GRANT_JSON);
    const result = evaluateProviderExecutionAuthority(grant, {
      workerAgentId: env.CVF_AGENT_ID ?? '',
      delegationId: env.CVF_DELEGATION_ID ?? '',
      grantId: env.CVF_PROVIDER_EXECUTION_GRANT_ID ?? '',
      provider,
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
