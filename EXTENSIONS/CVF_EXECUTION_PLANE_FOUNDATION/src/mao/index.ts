// CVF MAO-T1 - Local Module Front Door
//
// Stable local barrel for the src/mao/ task-graph/event-ledger/read-model
// foundation. This file is a LOCAL front door only: it is not imported by
// the root ../index.ts barrel, not consumed by a provider/resolver/adapter,
// and not wired to any queue, scheduler, UI, or runtime caller. A future
// bounded packet may wire root integration; MAO-T1 does not.
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
