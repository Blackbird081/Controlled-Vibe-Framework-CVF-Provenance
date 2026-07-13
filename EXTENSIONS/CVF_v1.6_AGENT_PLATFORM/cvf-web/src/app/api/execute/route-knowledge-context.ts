/**
 * SOT3-ACT-A1 - Execute route knowledge-context helper
 *
 * Owns tenant-scoped knowledge retrieval, formatting, scope-audit emission,
 * SOT3 knowledge activation evaluation, and knowledge system-prompt
 * construction for `/api/execute`. Extracted from `route.ts` to keep the
 * near-limit route file thin and to give this same-domain block a focused,
 * independently testable owner.
 *
 * Authorization: docs/work_orders/CVF_AGENT_WORK_ORDER_SOT3_ACT_A1_SCOPED_KNOWLEDGE_CONTEXT_PRODUCT_ADAPTER_2026-07-13.md
 */
import { randomUUID } from 'node:crypto';
import { NextResponse } from 'next/server';
import { CVF_SYSTEM_PROMPT } from '@/lib/ai';
import { buildKnowledgeSystemPrompt, hasKnowledgeContext } from '@/lib/knowledge-context-injector';
import { formatKnowledgeChunks, queryKnowledgeChunks, type KnowledgeQueryResult } from '@/lib/knowledge-retrieval';
import { knowledgeStore } from '@/lib/knowledge-store';
import { appendAuditEvent } from '@/lib/control-plane-events';
import { withSessionAuditPayload, type SessionCookie } from '@/lib/middleware-auth';
import {
    evaluateSot3KnowledgeActivation,
    resolveSot3KnowledgeActivationMode,
    type Sot3KnowledgeActivationResult,
    type Sot3KnowledgeChunkInput,
} from '@/lib/sot3-knowledge-adapter';
import { DeterministicClock, SequentialIdFactory } from 'cvf-refinery';

export interface KnowledgeContextParams {
    intent: string;
    orgId: string | undefined;
    teamId: string | undefined;
    requestedCollectionId: string | undefined;
    templateLabel: string;
    session: SessionCookie | null | undefined;
}

export interface KnowledgeContextResult {
    retrievalResult: KnowledgeQueryResult;
    finalKnowledgeContext: string | undefined;
    knowledgeInjected: boolean;
    knowledgeSource: 'retrieval' | 'none';
    knowledgeSystemPrompt: string;
    requestedKnowledgeCollectionId: string | null;
    sot3: Sot3KnowledgeActivationResult | null;
}

function resolveChunkSot3Source(chunk: { id: string; collectionId: string }) {
    const collection = knowledgeStore.getCollection(chunk.collectionId);
    return collection?.chunks.find((stored) => stored.id === chunk.id)?.sot3Source;
}

async function emitScopeFilterAudit(params: {
    retrievalResult: KnowledgeQueryResult;
    session: SessionCookie | null | undefined;
    templateLabel: string;
}): Promise<void> {
    const { retrievalResult, session, templateLabel } = params;
    if (retrievalResult.droppedChunkCount === 0) return;
    await appendAuditEvent({
        eventType: 'KNOWLEDGE_SCOPE_FILTER_APPLIED',
        actorId: session?.userId ?? 'service-account',
        actorRole: session?.role ?? 'service',
        targetResource: templateLabel,
        action: 'FILTER_KNOWLEDGE_SCOPE',
        riskLevel: 'R2',
        phase: 'PHASE D',
        outcome: 'FILTERED',
        payload: withSessionAuditPayload(session, {
            requestedOrgId: session?.orgId ?? null,
            requestedTeamId: session?.teamId ?? null,
            retrievedChunkCount: retrievalResult.matchedChunkCount,
            allowedChunkCount: retrievalResult.allowedChunkCount,
            droppedChunkCount: retrievalResult.droppedChunkCount,
            allowedCollectionIds: retrievalResult.allowedCollectionIds,
            droppedCollectionIds: retrievalResult.droppedCollectionIds,
        }),
    });
}

async function emitSot3ActivationAudit(params: {
    mode: 'SHADOW' | 'ENFORCE';
    result: Sot3KnowledgeActivationResult;
    retrievalResult: KnowledgeQueryResult;
    session: SessionCookie | null | undefined;
    templateLabel: string;
}): Promise<void> {
    const { mode, result, retrievalResult, session, templateLabel } = params;
    await appendAuditEvent({
        eventType: 'SOT3_KNOWLEDGE_ACTIVATION_EVALUATED',
        actorId: session?.userId ?? 'service-account',
        actorRole: session?.role ?? 'service',
        targetResource: templateLabel,
        action: 'EVALUATE_SOT3_KNOWLEDGE_ACTIVATION',
        riskLevel: 'R2',
        phase: 'PHASE D',
        outcome: result.terminalOutcome,
        payload: withSessionAuditPayload(session, {
            mode,
            terminalOutcome: result.terminalOutcome,
            injectionPermitted: result.injectionPermitted,
            failureStage: result.failureStage,
            retrievedChunkCount: retrievalResult.matchedChunkCount,
            allowedChunkCount: retrievalResult.allowedChunkCount,
            droppedChunkCount: retrievalResult.droppedChunkCount,
            refineryPacketId: result.refineryPacketId,
            refineryPacketIds: result.refineryPacketIds,
            refineryStatus: result.refineryStatus,
            kernelDecisionId: result.kernelDecisionId,
            kernelDecisionIds: result.kernelDecisionIds,
            kernelDecision: result.kernelDecision,
            kernelEvidenceCount: result.kernelEvidenceCount,
            truthReferenceId: result.truthReferenceId,
            truthReferenceIds: result.truthReferenceIds,
            flowPackageId: result.flowPackageId,
            flowPackageIds: result.flowPackageIds,
            flowAcknowledgementState: result.flowAcknowledgementState,
        }),
    });
}

/**
 * Blocks inline `knowledgeContext` bypass attempts from unauthenticated
 * service-token callers, auditing the block before rejecting. Returns the
 * rejection response when blocked, or `null` when the request may continue
 * to routing and scoped retrieval.
 */
export async function blockInlineKnowledgeContextBypass(params: {
    session: SessionCookie | null | undefined;
    isServiceAllowed: boolean;
    knowledgeContext: unknown;
    templateLabel: string;
    riskLevel: string | null | undefined;
    phase: string | null | undefined;
}): Promise<NextResponse | null> {
    const { session, isServiceAllowed, knowledgeContext, templateLabel, riskLevel, phase } = params;
    if (session || !isServiceAllowed || typeof knowledgeContext !== 'string' || !knowledgeContext.trim()) {
        return null;
    }

    await appendAuditEvent({
        eventType: 'INLINE_KNOWLEDGE_CONTEXT_BLOCKED',
        actorId: 'service-account',
        actorRole: 'service',
        targetResource: templateLabel,
        action: 'BLOCK_INLINE_KNOWLEDGE_CONTEXT',
        riskLevel: riskLevel ?? 'R2',
        phase: phase ?? 'PHASE D',
        outcome: 'BLOCKED',
        payload: {
            reason: 'service-token-inline-knowledge-disabled',
        },
    });

    return NextResponse.json(
        {
            success: false,
            error: 'Inline knowledgeContext is no longer accepted for service-token execution. Use scoped retrieval instead.',
        },
        { status: 400 },
    );
}

/**
 * Resolves scoped knowledge context for the execute route: retrieval,
 * scope-audit emission, SOT3 activation evaluation (mode-gated), and the
 * final knowledge system prompt. Ordering is fixed: retrieval and scope
 * audit happen first (already-authorized scope remains authoritative), SOT3
 * evaluation happens next, and prompt construction happens last, before
 * provider execution in the caller.
 */
export async function resolveKnowledgeContext(params: KnowledgeContextParams): Promise<KnowledgeContextResult> {
    const { intent, orgId, teamId, requestedCollectionId, templateLabel, session } = params;

    const retrievalResult = await queryKnowledgeChunks({
        intent,
        orgId,
        teamId,
        collectionId: requestedCollectionId,
    });

    await emitScopeFilterAudit({ retrievalResult, session, templateLabel });

    const requestedKnowledgeCollectionId = requestedCollectionId?.trim() ? requestedCollectionId.trim() : null;

    const mode = resolveSot3KnowledgeActivationMode(process.env.CVF_SOT3_KNOWLEDGE_ACTIVATION_MODE);
    const retrievedKnowledgeContext = formatKnowledgeChunks(retrievalResult.chunks);

    let sot3: Sot3KnowledgeActivationResult | null = null;
    let finalKnowledgeContext = retrievedKnowledgeContext ?? undefined;

    if (mode !== 'OFF') {
        const chunkInputs: Sot3KnowledgeChunkInput[] = retrievalResult.chunks.map((chunk) => ({
            id: chunk.id,
            content: chunk.content,
            collectionId: chunk.collectionId,
            sot3Source: resolveChunkSot3Source(chunk),
        }));

        sot3 = evaluateSot3KnowledgeActivation(
            {
                chunks: chunkInputs,
                organization: orgId ?? '',
                team: teamId ?? null,
                actorId: session?.userId ?? 'service-account',
                requestId: randomUUID(),
                policyVersion: 'cvf-web-knowledge-context-v1',
                ruleVersion: 'cvf-web-knowledge-context-v1',
                clock: new DeterministicClock(new Date().toISOString(), 1000),
                ids: new SequentialIdFactory(),
            },
            mode,
        );

        await emitSot3ActivationAudit({ mode, result: sot3, retrievalResult, session, templateLabel });

        if (mode === 'ENFORCE') {
            finalKnowledgeContext = sot3.injectionPermitted && sot3.approvedContext ? sot3.approvedContext : undefined;
        }
    }

    const knowledgeInjected = hasKnowledgeContext(finalKnowledgeContext);
    const knowledgeSource: 'retrieval' | 'none' = knowledgeInjected ? 'retrieval' : 'none';
    const knowledgeSystemPrompt = knowledgeInjected
        ? buildKnowledgeSystemPrompt(CVF_SYSTEM_PROMPT, finalKnowledgeContext as string, { orgId, teamId })
        : CVF_SYSTEM_PROMPT;

    return {
        retrievalResult,
        finalKnowledgeContext,
        knowledgeInjected,
        knowledgeSource,
        knowledgeSystemPrompt,
        requestedKnowledgeCollectionId,
        sot3,
    };
}
