import { describe, expect, it, vi } from 'vitest';
import { createProviderExecutionFetchGuard } from './provider-execution-guard';

const grant = JSON.stringify({
  authority: 'ORCHESTRATOR_GRANT_REQUIRED',
  grantId: 'grant-001',
  authorizedBy: 'ORCHESTRATOR',
  subjectAgentId: 'worker-001',
  delegationId: 'delegation-001',
  allowedProviders: ['openai'],
  maxCalls: 1,
  expiresAt: '2026-08-26T00:00:00.000Z',
});

const baseEnv = {
  CVF_AGENT_ID: 'worker-001',
  CVF_DELEGATION_ID: 'delegation-001',
  CVF_PROVIDER_EXECUTION_GRANT_ID: 'grant-001',
  CVF_PROVIDER_EXECUTION_GRANT_JSON: grant,
};

describe('provider execution fetch guard', () => {
  it('denies a provider request when no orchestrator grant exists', async () => {
    const underlying = vi.fn();
    const guarded = createProviderExecutionFetchGuard(underlying as typeof fetch, {}, () => new Date('2026-08-25'));
    await expect(guarded('https://api.openai.com/v1/chat/completions')).rejects.toThrow(
      'CVF_PROVIDER_EXECUTION_DENIED',
    );
    expect(underlying).not.toHaveBeenCalled();
  });

  it('allows non-provider network traffic without consuming provider authority', async () => {
    const underlying = vi.fn().mockResolvedValue(new Response('ok'));
    const guarded = createProviderExecutionFetchGuard(underlying as typeof fetch, {}, () => new Date('2026-08-25'));
    await guarded('https://example.com/data');
    expect(underlying).toHaveBeenCalledOnce();
  });

  it('allows only the bounded call granted by the orchestrator', async () => {
    const underlying = vi.fn().mockResolvedValue(new Response('ok'));
    const guarded = createProviderExecutionFetchGuard(underlying as typeof fetch, baseEnv, () => new Date('2026-08-25'));
    await guarded('https://api.openai.com/v1/chat/completions');
    await expect(guarded('https://api.openai.com/v1/chat/completions')).rejects.toThrow('call budget exhausted');
    expect(underlying).toHaveBeenCalledOnce();
  });

  it.each([
    ['wrong subject', { ...baseEnv, CVF_AGENT_ID: 'worker-002' }],
    ['wrong delegation', { ...baseEnv, CVF_DELEGATION_ID: 'delegation-002' }],
    ['wrong grant id', { ...baseEnv, CVF_PROVIDER_EXECUTION_GRANT_ID: 'grant-002' }],
  ])('denies %s', async (_label, env) => {
    const underlying = vi.fn();
    const guarded = createProviderExecutionFetchGuard(underlying as typeof fetch, env, () => new Date('2026-08-25'));
    await expect(guarded('https://api.openai.com/v1/chat/completions')).rejects.toThrow('DENIED');
    expect(underlying).not.toHaveBeenCalled();
  });
});
