// CVF MAO-T1 - Local Module Front Door
//
// Stable local barrel for the src/mao/ task-graph/event-ledger/read-model
// foundation. This file is a LOCAL front door only: it is not imported by
// the root ../index.ts barrel and not wired to any queue, scheduler, UI, or
// runtime caller. A future bounded packet may wire root integration; MAO-T1
// does not.
//
// MAO-T2 consumer note: the control-plane role resolver
// (EXTENSIONS/CVF_CONTROL_PLANE_FOUNDATION/src/mao/role.resolver.contract.ts)
// imports MaoTaskGraph, MaoAuthorityEnvelope, MaoTaskDefinition,
// MaoRiskLevel, and MaoTaskRole directly from ./task.graph.contract (not
// through this barrel, to avoid adding a barrel-level dependency edge). The
// dependency direction is control-plane -> execution-plane only, per the
// MAO contract's Role Resolver Ownership decision: execution-plane owns
// task-graph/state mechanics; the control-plane resolver owns admission
// policy and must never be imported back into this module.
//
// See docs/reference/multi_agent_orchestration/README.md and
// docs/reference/multi_agent_orchestration/CVF_MAO_RUNTIME_FOUNDATION_CONTRACT.md
// for the design authority this module implements.

export type {
  MaoRoute,
  MaoRiskLevel,
  MaoTaskRole,
  MaoApprovalCheckpoint,
  MaoBudgetAllocation,
  MaoAuthorityEnvelopeInput,
  MaoAuthorityEnvelope,
  MaoTaskDefinition,
  MaoTaskDefinitionInput,
  MaoDependencyEdge,
  MaoTaskGraphInput,
  MaoTaskGraph,
  MaoGraphCompileFailureReason,
  MaoGraphCompileSuccess,
  MaoGraphCompileFailure,
  MaoGraphCompileResult,
} from "./task.graph.contract";

export {
  computeAuthorityHash,
  buildAuthorityEnvelope,
  verifyAuthorityEnvelope,
  detectDependencyCycle,
  compileTaskGraph,
  directDependents,
  directDependencies,
} from "./task.graph.contract";

export type {
  MaoTaskState,
  MaoEventType,
  MaoEventLedgerEntry,
  MaoAppendEventInput,
  MaoLedgerAppendFailureReason,
  MaoLedgerAppendSuccess,
  MaoLedgerAppendFailure,
  MaoLedgerAppendResult,
} from "./event.ledger.contract";

export {
  MAO_TERMINAL_STATES,
  isTerminalState,
  descendantPropagationFor,
  MaoEventLedger,
} from "./event.ledger.contract";

export type {
  MaoTerminalOutcome,
  MaoReadModelTaskState,
  MaoGeneratedReadModel,
  MaoReadModelBuildInput,
} from "./read.model.contract";

export { buildReadModel, readModelsAreEqual } from "./read.model.contract";

export type {
  MaoAdmissionReceiptLike,
  MaoDiagnosticClass,
  MaoCapabilityDeclaration,
  MaoUsageEnvelope,
  MaoInvocationReceipt,
  MaoInvocationRejectionReason,
  MaoInvocationRequest,
  MaoInvocationSuccess,
  MaoInvocationFailure,
  MaoInvocationResult,
} from "./delegation.adapter.contract";

export { MaoDelegationAdapter, createMaoDelegationAdapter } from "./delegation.adapter.contract";

// --- MAO-T4 reviewer isolation, dissent, and revision loop ---

export type {
  MaoIsolatedSourcePacket,
  MaoExcludedContextEntry,
  MaoReviewerSourceContract,
  MaoSelfApprovalCheck,
  MaoRecomputedEvidence,
} from "./reviewer.isolation.contract";

export {
  buildIsolatedSourcePacket,
  verifyIsolatedSourcePacket,
  checkSelfApproval,
  checkEvidenceIndependence,
  buildRecomputedEvidence,
} from "./reviewer.isolation.contract";

export type {
  MaoDefectClass,
  MaoReviewDecision,
  MaoDissentRecord,
  MaoDefectEntry,
  MaoReviewReceipt,
  MaoRevisionLedger,
  MaoReviewReceiptInput,
  MaoRevisionCeilingCheck,
  MaoRecordReviewResult,
  MaoReviewTerminalDecision,
} from "./dissent.revision.contract";

export {
  buildReviewReceipt,
  buildDefectEntry,
  buildDissentRecord,
  checkRevisionCeiling,
  createRevisionLedger,
  recordReviewInLedger,
  terminalReviewDecision,
  verifyDissentDeterminism,
  verifyReviewReceiptConsistency,
} from "./dissent.revision.contract";
