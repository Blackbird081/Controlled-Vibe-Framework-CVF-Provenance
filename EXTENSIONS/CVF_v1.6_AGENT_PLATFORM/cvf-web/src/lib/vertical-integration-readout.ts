import {
    evaluateMemoryEventHook,
    MEMORY_EVENT_HOOKS_VERSION,
    type MemoryEventHookEvaluation,
} from 'cvf-learning-plane-foundation';
import type { ExecutionRequest, GovernanceEvidenceReceipt } from '@/lib/ai';
import type { AuditMemoryReceipt } from '@/lib/audit-memory-receipt';
import type { Phase2CProductBriefSlice } from '@/lib/phase2c-product-brief-slice';
import type { Phase3EEmissionPilot } from '@/lib/phase3e-operational-emission';
import type { RouteRequestContextReadout } from '@/lib/route-request-context-readout';
import type { WorkflowExecutionProjection } from '@/lib/workflows/workflow-resolver';

export const VERTICAL_INTEGRATION_READOUT_VERSION = 'cvf.verticalWorkflowIntegration.vi1.v1';

export type VerticalIntegrationStatus = 'integrated' | 'partial' | 'not_applicable';

export type VerticalIntegrationSurfaceId =
    | 'governance_receipt'
    | 'workflow_state_machine'
    | 'workflow_recovery'
    | 'request_context_profile'
    | 'memory_event_hook'
    | 'artifact_verification'
    | 'operational_metrics';

export interface VerticalIntegrationSurfaceReadout {
    surfaceId: VerticalIntegrationSurfaceId;
    contractVersion: string;
    present: boolean;
    status: 'present' | 'missing';
    summary: string;
    evidenceRefs: readonly string[];
}

export interface VerticalIntegrationChainReadout {
    turnIndex: number;
    threadId: string | null;
    rootReceiptId: string | null;
    parentReceiptId: string | null;
    currentReceiptId: string;
    continuityProven: boolean;
    reason: string;
}

export interface VerticalIntegrationReadout {
    contractVersion: typeof VERTICAL_INTEGRATION_READOUT_VERSION;
    status: VerticalIntegrationStatus;
    requiredSurfaceCount: number;
    integratedSurfaceCount: number;
    liveReceipt: {
        present: boolean;
        receiptId: string;
        envelopeId?: string;
        provider?: string;
        model?: string;
        evidenceMode: GovernanceEvidenceReceipt['evidenceMode'];
    };
    surfaces: readonly VerticalIntegrationSurfaceReadout[];
    memoryEventHook: MemoryEventHookEvaluation;
    chain: VerticalIntegrationChainReadout;
    boundaries: readonly string[];
}

export interface BuildVerticalIntegrationReadoutInput {
    evidenceReceipt: GovernanceEvidenceReceipt;
    workflowExecution?: WorkflowExecutionProjection;
    auditMemoryReceipt?: AuditMemoryReceipt;
    requestContextReadout?: RouteRequestContextReadout;
    phase2cProductBrief?: Phase2CProductBriefSlice;
    phase3eOperationalMetrics?: Phase3EEmissionPilot;
    chainRequest?: ExecutionRequest['verticalIntegrationChain'];
    actorId: string;
    templateId?: string;
}

const REQUIRED_SURFACE_COUNT = 5;

function normalizeRiskLevel(riskLevel?: string): 'R0' | 'R1' | 'R2' | 'R3' {
    if (riskLevel === 'R0' || riskLevel === 'R1' || riskLevel === 'R2' || riskLevel === 'R3') {
        return riskLevel;
    }
    return 'R1';
}

function mapPolicyDecision(decision?: string): 'allow' | 'allow_limited' | 'deny' | 'require_human_approval' {
    const normalized = String(decision ?? '').toUpperCase();
    if (normalized === 'BLOCK' || normalized === 'DENY') {
        return 'deny';
    }
    if (normalized === 'NEEDS_APPROVAL') {
        return 'require_human_approval';
    }
    return 'allow_limited';
}

function buildSurface(
    surfaceId: VerticalIntegrationSurfaceId,
    contractVersion: string,
    present: boolean,
    summary: string,
    evidenceRefs: readonly string[],
): VerticalIntegrationSurfaceReadout {
    return {
        surfaceId,
        contractVersion,
        present,
        status: present ? 'present' : 'missing',
        summary,
        evidenceRefs,
    };
}

function buildChainReadout(
    receipt: GovernanceEvidenceReceipt,
    chain?: ExecutionRequest['verticalIntegrationChain'],
): VerticalIntegrationChainReadout {
    const turnIndex = Number.isFinite(chain?.turnIndex) && Number(chain?.turnIndex) > 0
        ? Number(chain?.turnIndex)
        : 1;
    const parentReceiptId = chain?.parentReceiptId?.trim() || null;
    const rootReceiptId = chain?.rootReceiptId?.trim() || parentReceiptId;
    const threadId = chain?.threadId?.trim() || null;
    const continuityProven = turnIndex >= 2 && Boolean(threadId && parentReceiptId && rootReceiptId);

    return {
        turnIndex,
        threadId,
        rootReceiptId,
        parentReceiptId,
        currentReceiptId: receipt.receiptId,
        continuityProven,
        reason: continuityProven
            ? 'second_or_later_turn_links_to_prior_receipt'
            : turnIndex >= 2
                ? 'continuity_metadata_incomplete'
                : 'root_turn_or_single_turn',
    };
}

export function buildVerticalIntegrationReadout(
    input: BuildVerticalIntegrationReadoutInput,
): VerticalIntegrationReadout {
    const receipt = input.evidenceReceipt;
    const memoryIds = input.auditMemoryReceipt?.receipt.memoryIds ?? [];
    const captureRecord = input.auditMemoryReceipt?.captureRecord;
    const chain = buildChainReadout(receipt, input.chainRequest);
    const memoryEventHook = evaluateMemoryEventHook({
        eventId: `vi1-${receipt.receiptId}`,
        sessionId: chain.threadId ?? receipt.envelopeId ?? receipt.receiptId,
        actorId: input.actorId,
        projectId: input.templateId ?? receipt.routeId,
        eventType: 'execution_result',
        riskLevel: normalizeRiskLevel(receipt.riskLevel),
        policyDecision: mapPolicyDecision(receipt.decision),
        memoryIds,
        containsSensitiveData: false,
    });

    const artifactVerification = input.phase2cProductBrief?.deliverablePack.artifactVerification;
    const surfaces = [
        buildSurface(
            'governance_receipt',
            'web_governance_evidence_receipt',
            Boolean(receipt.receiptId && receipt.envelopeId),
            receipt.evidenceMode === 'live'
                ? 'live governance receipt is attached to the route response'
                : `${receipt.evidenceMode} governance receipt is attached to the route response`,
            [receipt.receiptId, receipt.envelopeId].filter(Boolean) as string[],
        ),
        buildSurface(
            'workflow_state_machine',
            'cvf.workflowStateMachineProjection.v1',
            input.workflowExecution?.stateMachine.contractVersion === 'cvf.workflowStateMachineProjection.v1',
            input.workflowExecution
                ? `workflow final state ${input.workflowExecution.stateMachine.finalState}`
                : 'workflow state-machine projection is not present',
            input.workflowExecution?.stateMachine.completedStepIds ?? [],
        ),
        buildSurface(
            'workflow_recovery',
            'cvf.workflowRecoveryReadout.wr1.v1',
            input.workflowExecution?.recovery.contractVersion === 'cvf.workflowRecoveryReadout.wr1.v1',
            input.workflowExecution
                ? `workflow recovery action ${input.workflowExecution.recovery.recoveryAction}`
                : 'workflow recovery readout is not present',
            input.workflowExecution?.recovery.lastRestorableCheckpoint?.receiptId
                ? [input.workflowExecution.recovery.lastRestorableCheckpoint.receiptId]
                : [],
        ),
        buildSurface(
            'request_context_profile',
            'cvf.routeRequestContextProfile.vi2.v1',
            input.requestContextReadout?.readoutVersion === 'cvf.routeRequestContextProfile.vi2.v1',
            input.requestContextReadout
                ? `request context ${input.requestContextReadout.readiness}; profile ${input.requestContextReadout.profile}`
                : 'request context profile readout is not present',
            input.requestContextReadout?.detectedSignals ?? [],
        ),
        buildSurface(
            'memory_event_hook',
            MEMORY_EVENT_HOOKS_VERSION,
            memoryEventHook.allowed,
            `${memoryEventHook.decision}; capture=${captureRecord?.captureDecision ?? 'missing'}; rawMemoryReleased=${memoryEventHook.receipt.rawMemoryReleased}; canReinject=${memoryEventHook.receipt.canReinject}`,
            [...memoryIds, captureRecord?.eventId, captureRecord?.auditReceiptId].filter(Boolean) as string[],
        ),
        buildSurface(
            'artifact_verification',
            'cvf.packArtifactVerification.w6.v1',
            artifactVerification?.provenance.rendererPolicy === 'cvf.packArtifactVerification.w6.v1',
            artifactVerification
                ? `artifact verification ${artifactVerification.status}`
                : 'artifact verification is not present',
            artifactVerification?.provenance.receiptId ? [artifactVerification.provenance.receiptId] : [],
        ),
        buildSurface(
            'operational_metrics',
            'CVF_17_05_PHASE_3E_EMISSION_PILOT',
            input.phase3eOperationalMetrics?.status === 'emitted',
            input.phase3eOperationalMetrics
                ? `operational metrics emitted: ${input.phase3eOperationalMetrics.metrics.map(metric => metric.metricId).join(', ')}`
                : 'operational metric emission is not present',
            input.phase3eOperationalMetrics?.metrics.map(metric => metric.metricId) ?? [],
        ),
    ] as const;
    const integratedSurfaceCount = surfaces.filter(surface => surface.present).length;
    const status: VerticalIntegrationStatus = integratedSurfaceCount >= REQUIRED_SURFACE_COUNT
        ? 'integrated'
        : integratedSurfaceCount > 0
            ? 'partial'
            : 'not_applicable';

    return {
        contractVersion: VERTICAL_INTEGRATION_READOUT_VERSION,
        status,
        requiredSurfaceCount: REQUIRED_SURFACE_COUNT,
        integratedSurfaceCount,
        liveReceipt: {
            present: receipt.evidenceMode === 'live' && Boolean(receipt.receiptId),
            receiptId: receipt.receiptId,
            envelopeId: receipt.envelopeId,
            provider: receipt.provider,
            model: receipt.model,
            evidenceMode: receipt.evidenceMode,
        },
        surfaces,
        memoryEventHook,
        chain,
        boundaries: [
            'response_level_readout_only',
            'no_new_receipt_envelope_schema',
            'no_workflow_engine_or_route_transition_blocking',
            'no_memory_reinjection_or_raw_memory_release',
            'no_provider_adapter_semantic_change',
        ],
    };
}
