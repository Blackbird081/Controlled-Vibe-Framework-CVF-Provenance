import { describe, expect, it } from 'vitest';
import { buildAuditMemoryReceipt } from './audit-memory-receipt';

describe('audit-memory-receipt', () => {
    it('captures a governance audit event as session memory after receipt emission', () => {
        const auditMemoryReceipt = buildAuditMemoryReceipt({
            governanceReceiptId: 'receipt-123',
            actorId: 'user-1',
            actorRole: 'BUILDER',
            sessionId: 'session-1',
            templateId: 'app_builder_complete',
            workflowId: 'workflow.product.create_product_brief.v1',
            provider: 'openai',
            model: 'gpt-4o',
            decision: 'ALLOW',
            stepTraceIds: [
                'step-1-intake-validation',
                'step-3-provider-call',
                'step-5-receipt-emit',
            ],
            rolePermission: {
                role: 'BUILDER',
                permissionRole: 'BUILDER',
                outputClass: 'artifact',
                allowed: true,
            },
        });

        expect(auditMemoryReceipt).toMatchObject({
            tier: 'session',
            contractVersion: 'phaseD.memoryContinuity.v1',
            ownerRole: 'OPERATOR',
            writesRequireReceipt: true,
            privacyFilters: ['scope_minimization', 'pii_redaction'],
            reinjectionPolicy: {
                tier: 'session',
                privacyFilter: 'pii_redaction',
                receiptRequired: true,
            },
            receipt: {
                traceId: 'receipt-123',
                decision: 'captured',
                reason: 'memory_captured_after_policy_and_privacy',
                actorId: 'user-1',
                provenanceRequired: true,
            },
        });
        expect(auditMemoryReceipt.receipt.memoryIds).toHaveLength(1);
    });

    it('session ownerRole is OPERATOR', () => {
        const result = buildAuditMemoryReceipt({
            governanceReceiptId: 'gr-001',
            actorId: 'actor-001',
            actorRole: 'OPERATOR',
        });

        expect(result.ownerRole).toBe('OPERATOR');
    });

    it('writesRequireReceipt is true for session tier', () => {
        const result = buildAuditMemoryReceipt({
            governanceReceiptId: 'gr-002',
            actorId: 'actor-002',
            actorRole: 'SERVICE_AGENT',
        });

        // canReinject remains hardcoded false in the capture call; policy
        // reinjectionAllowed stays metadata and is not used as a write gate.
        expect(result.writesRequireReceipt).toBe(true);
        expect(Array.isArray(result.privacyFilters)).toBe(true);
        expect(result.privacyFilters).toContain('pii_redaction');
    });
});
