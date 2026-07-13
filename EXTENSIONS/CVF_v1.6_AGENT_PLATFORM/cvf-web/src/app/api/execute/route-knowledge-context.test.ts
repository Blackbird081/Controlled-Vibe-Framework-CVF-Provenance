import { createHash } from 'node:crypto';
import { mkdtemp, rm } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { knowledgeStore } from '@/lib/knowledge-store';
import { readAuditEvents } from '@/lib/control-plane-events';
import type { Sot3KnowledgeSourceMetadata } from '@/lib/knowledge-store';

vi.mock('next/server', () => ({
  NextResponse: {
    json: (body: unknown, init?: { status?: number }) => ({ status: init?.status ?? 200, json: async () => body }),
  },
}));

vi.mock('@/lib/middleware-auth', () => ({
  withSessionAuditPayload: (
    session: { impersonation?: { realActorId: string; sessionId: string } } | null | undefined,
    payload?: Record<string, unknown>,
  ) => {
    const nextPayload = { ...(payload ?? {}) };
    if (session?.impersonation) {
      nextPayload.impersonatedBy = session.impersonation.realActorId;
      nextPayload.impersonationSessionId = session.impersonation.sessionId;
    }
    return Object.keys(nextPayload).length > 0 ? nextPayload : undefined;
  },
}));

import { blockInlineKnowledgeContextBypass, resolveKnowledgeContext } from './route-knowledge-context';

function computeExpectedContentHash(records: Array<Record<string, unknown>>): string {
  const sorted = records.map((record) => {
    const keys = Object.keys(record).sort();
    return keys.map((key) => [key, record[key]]);
  });
  return `sha256:${createHash('sha256').update(JSON.stringify(sorted)).digest('hex')}`;
}

function buildProvenance(sourceId: string, content: string, overrides: Partial<Sot3KnowledgeSourceMetadata> = {}): Sot3KnowledgeSourceMetadata {
  const rawRecord = { source_id: sourceId, id: sourceId, content };
  return {
    sourceId,
    sourceType: 'INTERNAL',
    owner: 'team-eng',
    capturedAtUtc: '2026-07-13T00:00:00.000Z',
    purpose: ['execute-route-context'],
    confidentiality: 'INTERNAL',
    expectedContentHash: computeExpectedContentHash([rawRecord]),
    rawReference: { type: 'object', location: `knowledge-store://${sourceId}` },
    captureStatus: 'CAPTURED',
    declaredVersion: null,
    validFromUtc: null,
    validUntilUtc: null,
    ...overrides,
  };
}

describe('route-knowledge-context', () => {
  const originalEnv = { ...process.env };
  let tempDir = '';

  beforeEach(async () => {
    tempDir = await mkdtemp(path.join(os.tmpdir(), 'cvf-knowledge-context-'));
    process.env = { ...originalEnv };
    process.env.CVF_CONTROL_PLANE_EVENTS_PATH = path.join(tempDir, 'events.json');

    (knowledgeStore as unknown as { _store: Map<string, unknown> })._store.clear();
    (knowledgeStore as unknown as { _ephemeral: Map<string, unknown> })._ephemeral.clear();
  });

  afterEach(async () => {
    process.env = { ...originalEnv };
    if (tempDir) await rm(tempDir, { recursive: true, force: true });
  });

  describe('blockInlineKnowledgeContextBypass', () => {
    it('returns null when session is present regardless of inline knowledgeContext', async () => {
      const result = await blockInlineKnowledgeContextBypass({
        session: { userId: 'u1', user: 'U', role: 'admin', orgId: 'o', teamId: 't', expiresAt: 0, authMode: 'session' },
        isServiceAllowed: true,
        knowledgeContext: 'INLINE',
        templateLabel: 'tmpl',
        riskLevel: null,
        phase: null,
      });
      expect(result).toBeNull();
    });

    it('blocks and audits inline knowledgeContext for unauthenticated service-token callers', async () => {
      const result = await blockInlineKnowledgeContextBypass({
        session: null,
        isServiceAllowed: true,
        knowledgeContext: 'INLINE-BYPASS',
        templateLabel: 'tmpl',
        riskLevel: null,
        phase: null,
      });
      expect(result).not.toBeNull();
      expect(result?.status).toBe(400);
      const events = await readAuditEvents();
      expect(events.some((event) => event.eventType === 'INLINE_KNOWLEDGE_CONTEXT_BLOCKED')).toBe(true);
    });
  });

  describe('resolveKnowledgeContext - mode resolution', () => {
    it('resolves to OFF behavior when mode env var is missing', async () => {
      delete process.env.CVF_SOT3_KNOWLEDGE_ACTIVATION_MODE;
      knowledgeStore.seed([
        { id: 'col-1', name: 'Col', description: 'd', orgId: null, teamId: null, chunks: [{ id: 'c1', content: 'legacy governance content', keywords: ['governance'] }] },
      ]);

      const result = await resolveKnowledgeContext({
        intent: 'governance content question',
        orgId: undefined,
        teamId: undefined,
        requestedCollectionId: undefined,
        templateLabel: 'tmpl',
        session: null,
      });

      expect(result.sot3).toBeNull();
      expect(result.knowledgeInjected).toBe(true);
      expect(result.knowledgeSource).toBe('retrieval');
      expect(result.finalKnowledgeContext).toContain('legacy governance content');
    });

    it('resolves to OFF behavior when mode env var is invalid', async () => {
      process.env.CVF_SOT3_KNOWLEDGE_ACTIVATION_MODE = 'BOGUS';
      knowledgeStore.seed([
        { id: 'col-1', name: 'Col', description: 'd', orgId: null, teamId: null, chunks: [{ id: 'c1', content: 'legacy governance content', keywords: ['governance'] }] },
      ]);

      const result = await resolveKnowledgeContext({
        intent: 'governance content question',
        orgId: undefined,
        teamId: undefined,
        requestedCollectionId: undefined,
        templateLabel: 'tmpl',
        session: null,
      });

      expect(result.sot3).toBeNull();
      expect(result.knowledgeInjected).toBe(true);
    });
  });

  describe('resolveKnowledgeContext - SHADOW mode', () => {
    it('evaluates SOT3 and audits, but preserves current raw context downstream', async () => {
      process.env.CVF_SOT3_KNOWLEDGE_ACTIVATION_MODE = 'SHADOW';
      const provenance = buildProvenance('src-shadow', 'shadow-mode governed content');
      knowledgeStore.seed([
        { id: 'col-1', name: 'Col', description: 'd', orgId: 'org_a', teamId: 'team_a', chunks: [{ id: 'src-shadow', content: 'shadow-mode governed content', keywords: ['governance'], sot3Source: provenance }] },
      ]);

      const result = await resolveKnowledgeContext({
        intent: 'governance content question',
        orgId: 'org_a',
        teamId: 'team_a',
        requestedCollectionId: undefined,
        templateLabel: 'tmpl',
        session: null,
      });

      expect(result.sot3?.terminalOutcome).toBe('APPROVED');
      expect(result.sot3?.injectionPermitted).toBe(false);
      expect(result.knowledgeInjected).toBe(true);
      expect(result.finalKnowledgeContext).toContain('shadow-mode governed content');

      const events = await readAuditEvents();
      const shadowEvent = events.find((event) => event.eventType === 'SOT3_KNOWLEDGE_ACTIVATION_EVALUATED');
      expect(shadowEvent).toBeDefined();
      expect(shadowEvent?.payload).toMatchObject({
        retrievedChunkCount: 1,
        allowedChunkCount: 1,
        droppedChunkCount: 0,
      });
      expect(JSON.stringify(shadowEvent?.payload ?? {})).not.toContain('shadow-mode governed content');
    });

    it('audits rejection but preserves current context downstream', async () => {
      process.env.CVF_SOT3_KNOWLEDGE_ACTIVATION_MODE = 'SHADOW';
      knowledgeStore.seed([
        { id: 'col-1', name: 'Col', description: 'd', orgId: null, teamId: null, chunks: [{ id: 'no-prov', content: 'no provenance content', keywords: ['governance'] }] },
      ]);

      const result = await resolveKnowledgeContext({
        intent: 'governance content question',
        orgId: undefined,
        teamId: undefined,
        requestedCollectionId: undefined,
        templateLabel: 'tmpl',
        session: null,
      });

      expect(result.sot3?.terminalOutcome).toBe('REJECTED');
      expect(result.sot3?.failureStage).toBe('MISSING_PROVENANCE');
      expect(result.knowledgeInjected).toBe(true);
      expect(result.finalKnowledgeContext).toContain('no provenance content');

      const events = await readAuditEvents();
      const shadowEvent = events.find((event) => event.eventType === 'SOT3_KNOWLEDGE_ACTIVATION_EVALUATED');
      expect(shadowEvent?.payload).toMatchObject({ terminalOutcome: 'REJECTED', failureStage: 'MISSING_PROVENANCE' });
    });
  });

  describe('resolveKnowledgeContext - ENFORCE mode', () => {
    it('injects only approved context after acknowledged Flow package', async () => {
      process.env.CVF_SOT3_KNOWLEDGE_ACTIVATION_MODE = 'ENFORCE';
      const provenance = buildProvenance('src-enforce', 'enforce-mode governed content');
      knowledgeStore.seed([
        { id: 'col-1', name: 'Col', description: 'd', orgId: 'org_a', teamId: 'team_a', chunks: [{ id: 'src-enforce', content: 'enforce-mode governed content', keywords: ['governance'], sot3Source: provenance }] },
      ]);

      const result = await resolveKnowledgeContext({
        intent: 'governance content question',
        orgId: 'org_a',
        teamId: 'team_a',
        requestedCollectionId: undefined,
        templateLabel: 'tmpl',
        session: null,
      });

      expect(result.sot3?.terminalOutcome).toBe('APPROVED');
      expect(result.sot3?.flowAcknowledgementState).toBe('ACKNOWLEDGED');
      expect(result.knowledgeInjected).toBe(true);
      expect(result.finalKnowledgeContext).toContain('enforce-mode governed content');
    });

    it('produces no knowledge block when provenance is missing', async () => {
      process.env.CVF_SOT3_KNOWLEDGE_ACTIVATION_MODE = 'ENFORCE';
      knowledgeStore.seed([
        { id: 'col-1', name: 'Col', description: 'd', orgId: null, teamId: null, chunks: [{ id: 'no-prov', content: 'raw content that must never appear', keywords: ['governance'] }] },
      ]);

      const result = await resolveKnowledgeContext({
        intent: 'governance content question',
        orgId: undefined,
        teamId: undefined,
        requestedCollectionId: undefined,
        templateLabel: 'tmpl',
        session: null,
      });

      expect(result.sot3?.terminalOutcome).toBe('REJECTED');
      expect(result.sot3?.failureStage).toBe('MISSING_PROVENANCE');
      expect(result.knowledgeInjected).toBe(false);
      expect(result.finalKnowledgeContext).toBeUndefined();
      expect(result.knowledgeSystemPrompt).not.toContain('raw content that must never appear');
    });

    it('produces no knowledge block when expected content hash is incorrect (Refinery blocks)', async () => {
      process.env.CVF_SOT3_KNOWLEDGE_ACTIVATION_MODE = 'ENFORCE';
      const provenance = buildProvenance('src-badhash', 'content with bad hash', { expectedContentHash: 'sha256:0000000000000000000000000000000000000000000000000000000000000000' });
      knowledgeStore.seed([
        { id: 'col-1', name: 'Col', description: 'd', orgId: 'org_a', teamId: 'team_a', chunks: [{ id: 'src-badhash', content: 'content with bad hash', keywords: ['governance'], sot3Source: provenance }] },
      ]);

      const result = await resolveKnowledgeContext({
        intent: 'governance content question',
        orgId: 'org_a',
        teamId: 'team_a',
        requestedCollectionId: undefined,
        templateLabel: 'tmpl',
        session: null,
      });

      expect(result.sot3?.terminalOutcome).toBe('REJECTED');
      expect(result.sot3?.failureStage).toBe('REFINERY_NOT_READY');
      expect(result.knowledgeInjected).toBe(false);
      expect(result.finalKnowledgeContext).toBeUndefined();
    });

    it('produces no knowledge block on Kernel non-accepting result', async () => {
      process.env.CVF_SOT3_KNOWLEDGE_ACTIVATION_MODE = 'ENFORCE';
      const provenance = buildProvenance('src-kernelreject', 'kernel-rejected content', { captureStatus: 'REJECTED_AT_INTAKE' });
      knowledgeStore.seed([
        { id: 'col-1', name: 'Col', description: 'd', orgId: 'org_a', teamId: 'team_a', chunks: [{ id: 'src-kernelreject', content: 'kernel-rejected content', keywords: ['governance'], sot3Source: provenance }] },
      ]);

      const result = await resolveKnowledgeContext({
        intent: 'governance content question',
        orgId: 'org_a',
        teamId: 'team_a',
        requestedCollectionId: undefined,
        templateLabel: 'tmpl',
        session: null,
      });

      expect(result.sot3?.terminalOutcome).toBe('REJECTED');
      expect(result.sot3?.failureStage).toBe('KERNEL_NOT_ACCEPTED');
      expect(result.knowledgeInjected).toBe(false);
      expect(result.finalKnowledgeContext).toBeUndefined();
    });

    it('produces no knowledge block and explicit no-context outcome when no chunks are retrieved', async () => {
      process.env.CVF_SOT3_KNOWLEDGE_ACTIVATION_MODE = 'ENFORCE';
      knowledgeStore.seed([
        { id: 'col-1', name: 'Col', description: 'd', orgId: null, teamId: null, chunks: [] },
      ]);

      const result = await resolveKnowledgeContext({
        intent: 'unmatched query with no scoring tokens at all xyz',
        orgId: undefined,
        teamId: undefined,
        requestedCollectionId: undefined,
        templateLabel: 'tmpl',
        session: null,
      });

      expect(result.sot3?.terminalOutcome).toBe('NO_CONTEXT');
      expect(result.knowledgeInjected).toBe(false);
    });
  });

  describe('resolveKnowledgeContext - cross-tenant scope', () => {
    it('keeps existing scope filter and audit intact regardless of mode', async () => {
      process.env.CVF_SOT3_KNOWLEDGE_ACTIVATION_MODE = 'OFF';
      knowledgeStore.seed([
        { id: 'org-a', name: 'Org A', description: 'd', orgId: 'org_a', teamId: 'team_a', chunks: [{ id: 'a1', content: 'tenant-a alpha-scope codename', keywords: ['tenant-a', 'alpha-scope'] }] },
        { id: 'org-b', name: 'Org B', description: 'd', orgId: 'org_b', teamId: 'team_b', chunks: [{ id: 'b1', content: 'tenant-b shadow-beta codename', keywords: ['tenant-b', 'shadow-beta'] }] },
      ]);

      const result = await resolveKnowledgeContext({
        intent: 'compare tenant-a alpha-scope and tenant-b shadow-beta',
        orgId: 'org_a',
        teamId: 'team_a',
        requestedCollectionId: undefined,
        templateLabel: 'tmpl',
        session: null,
      });

      expect(result.finalKnowledgeContext).toContain('tenant-a');
      expect(result.finalKnowledgeContext).not.toContain('shadow-beta');
      expect(result.retrievalResult.droppedChunkCount).toBeGreaterThan(0);

      const events = await readAuditEvents();
      expect(events.some((event) => event.eventType === 'KNOWLEDGE_SCOPE_FILTER_APPLIED')).toBe(true);
    });
  });
});
