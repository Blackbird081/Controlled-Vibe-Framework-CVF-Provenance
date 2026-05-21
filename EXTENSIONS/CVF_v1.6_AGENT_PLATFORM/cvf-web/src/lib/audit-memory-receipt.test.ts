import { afterEach, describe, expect, it, vi } from 'vitest';
import { buildAuditMemoryReceipt, buildRouteAuditMemoryCapture } from './audit-memory-receipt';

afterEach(() => {
    vi.doUnmock('cvf-learning-plane-foundation');
    vi.doUnmock('../../../../CVF_GUARD_CONTRACT/src/contracts/memory-continuity.contract');
    vi.resetModules();
});

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

    it('surfaces policy fields and capture state in route audit readout', () => {
        const result = buildRouteAuditMemoryCapture({
            governanceReceiptId: 'gr-003',
            actorId: 'actor-003',
            actorRole: 'BUILDER',
            templateId: 'documentation',
            templateName: 'Documentation',
            decision: 'ALLOW',
        });

        expect(result.auditEventPayload.payload).toMatchObject({
            governanceReceiptId: 'gr-003',
            memoryTier: 'session',
            memoryContractVersion: 'phaseD.memoryContinuity.v1',
            writesRequireReceipt: true,
            privacyFilters: ['scope_minimization', 'pii_redaction'],
            memoryReceiptDecision: 'captured',
            memoryCaptureMode: 'captured',
            memoryCaptureReason: 'memory_captured_after_policy_and_privacy',
        });
        expect(JSON.stringify(result.auditEventPayload.payload)).not.toContain('reinjectionAllowed');
    });

    it('preserves canReinject=false as the capture policy binding', async () => {
        const capture = vi.fn().mockReturnValue({
            receipt: {
                receiptId: 'mem-001',
                traceId: 'gr-004',
                decision: 'captured',
                reason: 'memory_captured_after_policy_and_privacy',
                createdAt: '2026-05-21T00:00:00.000Z',
                actorId: 'actor-004',
                memoryIds: ['memory-1'],
                maskedTokenCount: 0,
                estimatedTokens: 0,
                provenanceRequired: true,
            },
        });

        vi.resetModules();
        vi.doMock('cvf-learning-plane-foundation', () => ({
            createControlledMemoryGatewayContract: () => ({ capture }),
        }));

        const module = await import('./audit-memory-receipt');
        module.buildAuditMemoryReceipt({
            governanceReceiptId: 'gr-004',
            actorId: 'actor-004',
            actorRole: 'BUILDER',
        });

        expect(capture).toHaveBeenCalledWith(expect.objectContaining({
            policy: expect.objectContaining({
                canReinject: false,
            }),
        }));
        expect(JSON.stringify(capture.mock.calls[0][0])).not.toContain('reinjectionAllowed');
    });

    it('surfaces degraded-capture reason without triggering reinjection', async () => {
        const capture = vi.fn();

        vi.resetModules();
        vi.doMock('cvf-learning-plane-foundation', () => ({
            createControlledMemoryGatewayContract: () => ({ capture }),
        }));
        vi.doMock('../../../../CVF_GUARD_CONTRACT/src/contracts/memory-continuity.contract', () => ({
            MEMORY_CONTINUITY_CONTRACT_VERSION: 'phaseD.memoryContinuity.v1',
            MEMORY_TIER_OWNER_POLICIES: {
                session: {
                    ownerRole: 'OPERATOR',
                    writesRequireReceipt: false,
                    privacyFilters: ['scope_minimization', 'pii_redaction'],
                },
            },
            MEMORY_REINJECTION_POLICIES: {
                session: {
                    privacyFilter: 'pii_redaction',
                    provenanceScoreThreshold: 0.7,
                    maxAgeSeconds: 86400,
                    receiptRequired: true,
                },
            },
        }));

        const module = await import('./audit-memory-receipt');
        const result = module.buildRouteAuditMemoryCapture({
            governanceReceiptId: 'gr-005',
            actorId: 'actor-005',
            actorRole: 'SERVICE_AGENT',
        });

        expect(result.auditEventPayload.outcome).toBe('DEGRADED');
        expect(result.auditEventPayload.payload).toMatchObject({
            writesRequireReceipt: false,
            privacyFilters: ['scope_minimization', 'pii_redaction'],
            memoryReceiptDecision: 'policy_skipped',
            memoryCaptureMode: 'degraded',
            memoryCaptureReason: 'memory_tier_does_not_require_receipt_write',
        });
        expect(capture).not.toHaveBeenCalled();
        expect(JSON.stringify(result.auditEventPayload.payload)).not.toContain('reinjectionAllowed');
    });
});
