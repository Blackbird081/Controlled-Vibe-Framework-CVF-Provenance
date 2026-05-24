import type {
  CVFCanonicalDecision,
  CVFCanonicalRisk,
} from './cross-channel-guard-contract.ts';

export const TOOL_ACTION_TAXONOMY_VERSION = 'cvf.toolActionTaxonomy.w3.v1' as const;

export type ToolActionSurface =
  | 'local_tool'
  | 'command_runtime'
  | 'mcp_tool'
  | 'database'
  | 'capability_provider';

export type ToolActionSideEffect =
  | 'read_only'
  | 'local_write'
  | 'workspace_mutation'
  | 'external_mutation'
  | 'install'
  | 'network_egress'
  | 'database_read'
  | 'database_write'
  | 'database_export'
  | 'database_schema_mutation'
  | 'database_recovery'
  | 'database_admin'
  | 'destructive'
  | 'privileged'
  | 'unknown';

export type DatabaseActionFamily =
  | 'schema_inspection'
  | 'query_drafting'
  | 'read_execution'
  | 'write_execution'
  | 'schema_mutation'
  | 'export_movement'
  | 'backup_recovery'
  | 'administrative';

export type ToolTransport = 'local' | 'stdio_mcp' | 'remote_mcp' | 'http' | 'browser' | 'database_connection';

export type ToolActionApprovalLevel = 'none' | 'review' | 'explicit' | 'privileged' | 'admin';

export type ToolActionDiagnosticClass =
  | 'none'
  | 'invalid_input'
  | 'approval_required'
  | 'policy_blocked'
  | 'routing_unresolved'
  | 'receipt_missing'
  | 'network_error';

export type ToolActionUserAction =
  | 'none'
  | 'revise_request'
  | 'request_approval'
  | 'inspect_receipt'
  | 'contact_admin'
  | 'do_not_retry_without_new_evidence';

export interface ToolActionTaxonomyRequest {
  actionId: string;
  surface: ToolActionSurface;
  sideEffect: ToolActionSideEffect;
  databaseFamily?: DatabaseActionFamily;
  transport?: ToolTransport;
  scopeDeclared?: boolean;
  targetDeclared?: boolean;
  traceBindingId?: string;
  approvalSatisfied?: boolean;
  sandboxDeclared?: boolean;
  rollbackDeclared?: boolean;
  hasExternalDataTransfer?: boolean;
  sourceFamily?: string;
}

export interface ToolActionDiagnostic {
  stage: 'request_validation' | 'governance' | 'routing' | 'network';
  class: ToolActionDiagnosticClass;
  retryable: boolean;
  userAction: ToolActionUserAction;
  safeMessage: string;
}

export interface ToolActionTaxonomyEvaluation {
  taxonomyVersion: typeof TOOL_ACTION_TAXONOMY_VERSION;
  actionId: string;
  surface: ToolActionSurface;
  sideEffect: ToolActionSideEffect;
  riskLevel: CVFCanonicalRisk;
  decision: CVFCanonicalDecision;
  approvalLevel: ToolActionApprovalLevel;
  traceRequired: boolean;
  auditReceiptRequired: boolean;
  sandboxRequired: boolean;
  mutationCaptureRequired: boolean;
  rollbackRequired: boolean;
  runtimeExecutionAuthorized: false;
  diagnostic: ToolActionDiagnostic;
  reasons: string[];
}

const READ_ONLY_EFFECTS = new Set<ToolActionSideEffect>([
  'read_only',
  'database_read',
]);

const MUTATION_EFFECTS = new Set<ToolActionSideEffect>([
  'local_write',
  'workspace_mutation',
  'external_mutation',
  'install',
  'database_write',
  'database_export',
  'database_schema_mutation',
  'database_recovery',
  'database_admin',
  'destructive',
  'privileged',
]);

export function evaluateToolActionTaxonomy(
  request: ToolActionTaxonomyRequest,
): ToolActionTaxonomyEvaluation {
  const reasons: string[] = [];
  const actionId = String(request.actionId || '').trim();

  if (!actionId) {
    return buildEvaluation(request, {
      actionId: 'unknown',
      riskLevel: 'R3',
      decision: 'BLOCK',
      approvalLevel: 'explicit',
      traceRequired: true,
      auditReceiptRequired: true,
      sandboxRequired: true,
      mutationCaptureRequired: false,
      rollbackRequired: false,
      diagnostic: {
        stage: 'request_validation',
        class: 'invalid_input',
        retryable: false,
        userAction: 'revise_request',
        safeMessage: 'Tool action request is missing actionId.',
      },
      reasons: ['missing_action_id'],
    });
  }

  if (request.sideEffect === 'unknown') {
    return blockUnknown(request, actionId, 'unknown_side_effect');
  }

  if (request.sideEffect === 'destructive' || request.sideEffect === 'privileged') {
    return buildEvaluation(request, {
      actionId,
      riskLevel: 'R4',
      decision: 'BLOCK',
      approvalLevel: 'privileged',
      traceRequired: true,
      auditReceiptRequired: true,
      sandboxRequired: true,
      mutationCaptureRequired: true,
      rollbackRequired: true,
      diagnostic: {
        stage: 'governance',
        class: 'policy_blocked',
        retryable: false,
        userAction: 'request_approval',
        safeMessage: 'Privileged or destructive actions require a fresh runtime work order and cannot be authorized by W3 taxonomy.',
      },
      reasons: [`blocked_${request.sideEffect}`],
    });
  }

  const riskLevel = resolveRiskLevel(request);
  const approvalLevel = resolveApprovalLevel(request);
  const sandboxRequired = resolveSandboxRequired(request);
  const mutationCaptureRequired = MUTATION_EFFECTS.has(request.sideEffect);
  const rollbackRequired = mutationCaptureRequired && request.sideEffect !== 'local_write';
  const traceRequired = true;
  const auditReceiptRequired = true;

  if (requiresScope(request) && !request.scopeDeclared) {
    reasons.push('scope_required');
  }

  if (requiresTarget(request) && !request.targetDeclared) {
    reasons.push('target_required');
  }

  if (traceRequired && !request.traceBindingId) {
    reasons.push('trace_binding_missing');
  }

  if (sandboxRequired && !request.sandboxDeclared) {
    reasons.push('sandbox_required');
  }

  if (rollbackRequired && !request.rollbackDeclared) {
    reasons.push('rollback_required');
  }

  const hardBlock = reasons.some(reason =>
    reason === 'scope_required' ||
    reason === 'target_required' ||
    reason === 'trace_binding_missing'
  );

  const approvalMissing = approvalLevel !== 'none' && !request.approvalSatisfied;
  const decision: CVFCanonicalDecision = hardBlock
    ? 'BLOCK'
    : approvalMissing || (sandboxRequired && !request.sandboxDeclared) || (rollbackRequired && !request.rollbackDeclared)
      ? 'ESCALATE'
      : READ_ONLY_EFFECTS.has(request.sideEffect)
        ? 'ALLOW'
        : 'ALLOW';

  const diagnostic = resolveDiagnostic({
    decision,
    approvalMissing,
    hardBlock,
    reasons,
  });

  return buildEvaluation(request, {
    actionId,
    riskLevel,
    decision,
    approvalLevel,
    traceRequired,
    auditReceiptRequired,
    sandboxRequired,
    mutationCaptureRequired,
    rollbackRequired,
    diagnostic,
    reasons: reasons.length > 0 ? reasons : ['taxonomy_classified'],
  });
}

export function isRuntimeExecutionAuthorized(
  evaluation: ToolActionTaxonomyEvaluation,
): false {
  void evaluation;
  return false;
}

function resolveRiskLevel(request: ToolActionTaxonomyRequest): CVFCanonicalRisk {
  if (request.hasExternalDataTransfer) return 'R3';

  switch (request.sideEffect) {
    case 'read_only':
    case 'database_read':
      return request.surface === 'mcp_tool' || request.surface === 'capability_provider' ? 'R2' : 'R1';
    case 'local_write':
      return 'R2';
    case 'workspace_mutation':
    case 'external_mutation':
    case 'install':
    case 'network_egress':
    case 'database_write':
    case 'database_export':
      return 'R3';
    case 'database_schema_mutation':
    case 'database_recovery':
    case 'database_admin':
    case 'destructive':
    case 'privileged':
      return 'R4';
    case 'unknown':
      return 'R3';
  }
}

function resolveApprovalLevel(request: ToolActionTaxonomyRequest): ToolActionApprovalLevel {
  switch (request.sideEffect) {
    case 'read_only':
    case 'database_read':
      return request.hasExternalDataTransfer ? 'review' : 'none';
    case 'local_write':
      return 'review';
    case 'workspace_mutation':
    case 'external_mutation':
    case 'install':
    case 'network_egress':
    case 'database_write':
    case 'database_export':
      return 'explicit';
    case 'database_schema_mutation':
    case 'database_recovery':
      return 'privileged';
    case 'database_admin':
    case 'destructive':
    case 'privileged':
      return 'admin';
    case 'unknown':
      return 'explicit';
  }
}

function resolveSandboxRequired(request: ToolActionTaxonomyRequest): boolean {
  if (request.surface === 'mcp_tool' || request.surface === 'command_runtime') return true;
  if (request.surface === 'database') {
    return request.sideEffect !== 'read_only' && request.sideEffect !== 'database_read';
  }
  return MUTATION_EFFECTS.has(request.sideEffect) || request.sideEffect === 'network_egress';
}

function requiresScope(request: ToolActionTaxonomyRequest): boolean {
  return request.surface === 'database' ||
    request.surface === 'mcp_tool' ||
    MUTATION_EFFECTS.has(request.sideEffect) ||
    request.sideEffect === 'network_egress';
}

function requiresTarget(request: ToolActionTaxonomyRequest): boolean {
  return request.surface === 'database' ||
    request.sideEffect === 'external_mutation' ||
    request.sideEffect === 'database_export' ||
    request.sideEffect === 'network_egress';
}

function blockUnknown(
  request: ToolActionTaxonomyRequest,
  actionId: string,
  reason: string,
): ToolActionTaxonomyEvaluation {
  return buildEvaluation(request, {
    actionId,
    riskLevel: 'R3',
    decision: 'BLOCK',
    approvalLevel: 'explicit',
    traceRequired: true,
    auditReceiptRequired: true,
    sandboxRequired: true,
    mutationCaptureRequired: false,
    rollbackRequired: false,
    diagnostic: {
      stage: 'routing',
      class: 'routing_unresolved',
      retryable: false,
      userAction: 'revise_request',
      safeMessage: 'Tool action side effect is unknown and cannot be governed safely.',
    },
    reasons: [reason],
  });
}

function resolveDiagnostic(params: {
  decision: CVFCanonicalDecision;
  approvalMissing: boolean;
  hardBlock: boolean;
  reasons: string[];
}): ToolActionDiagnostic {
  if (params.decision === 'ALLOW') {
    return {
      stage: 'governance',
      class: 'none',
      retryable: false,
      userAction: 'none',
      safeMessage: 'Tool action taxonomy classified the planned action without granting runtime execution.',
    };
  }

  if (params.hardBlock) {
    return {
      stage: 'governance',
      class: params.reasons.includes('trace_binding_missing') ? 'receipt_missing' : 'invalid_input',
      retryable: false,
      userAction: params.reasons.includes('trace_binding_missing') ? 'inspect_receipt' : 'revise_request',
      safeMessage: 'Tool action is missing required scope, target, or trace binding.',
    };
  }

  if (params.approvalMissing) {
    return {
      stage: 'governance',
      class: 'approval_required',
      retryable: false,
      userAction: 'request_approval',
      safeMessage: 'Tool action requires approval before any future runtime may execute it.',
    };
  }

  return {
    stage: 'governance',
    class: 'policy_blocked',
    retryable: false,
    userAction: 'do_not_retry_without_new_evidence',
    safeMessage: 'Tool action did not satisfy W3 taxonomy requirements.',
  };
}

function buildEvaluation(
  request: ToolActionTaxonomyRequest,
  result: Omit<ToolActionTaxonomyEvaluation, 'taxonomyVersion' | 'surface' | 'sideEffect' | 'runtimeExecutionAuthorized'>,
): ToolActionTaxonomyEvaluation {
  return {
    taxonomyVersion: TOOL_ACTION_TAXONOMY_VERSION,
    actionId: result.actionId,
    surface: request.surface,
    sideEffect: request.sideEffect,
    riskLevel: result.riskLevel,
    decision: result.decision,
    approvalLevel: result.approvalLevel,
    traceRequired: result.traceRequired,
    auditReceiptRequired: result.auditReceiptRequired,
    sandboxRequired: result.sandboxRequired,
    mutationCaptureRequired: result.mutationCaptureRequired,
    rollbackRequired: result.rollbackRequired,
    runtimeExecutionAuthorized: false,
    diagnostic: result.diagnostic,
    reasons: result.reasons,
  };
}
