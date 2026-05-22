import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";

export const CERTIFIED_SKILL_PACK_REGISTRY_PATH = "governance/registries/cvf-certified-skill-pack-registry.json";

export interface CertifiedSkillPackRegistry {
  registryVersion: string;
  entries: CertifiedSkillPackEntry[];
}

export interface CertifiedSkillPackEntry {
  id: string;
  name: string;
  path: string;
  domain: string;
  riskLevel: string;
  status: string;
  certifiedAt: string;
  tranche: string;
  outcomeKey: string;
}

export interface ProductOutcomeRuntimePlan {
  planVersion: "cvf.productOutcomeRuntime.v1";
  skillPackId: string;
  outcomeKey: string;
  name: string;
  domain: string;
  riskLevel: string;
  status: string;
  templateId: string;
  routeOwner: "cvf-web /api/execute";
  command: string;
  inputContract: string;
  outputContract: string;
  receiptSchemaPath: string;
  failureRecoveryPath: string;
  executionBoundaryPath: string;
  authorityScopePath: string;
  workflowSpecPath: string;
  policyRefs: string[];
}

interface RuntimeBinding {
  templateId: string;
  inputContract: string;
  outputContract: string;
}

const RUNTIME_BINDINGS: Record<string, RuntimeBinding> = {
  strategy_analysis: {
    templateId: "strategy_analysis",
    inputContract: "business_context, options, constraints, success_criteria",
    outputContract: "Strategy analysis with recommendation and risks",
  },
  product_brief: {
    templateId: "app_builder_complete",
    inputContract: "product_goal, target_user, problem, constraints",
    outputContract: "Product requirements document",
  },
  sop_generator: {
    templateId: "documentation",
    inputContract: "process_name, actors, steps, controls",
    outputContract: "Standard operating procedure",
  },
  proposal_writer: {
    templateId: "email_template",
    inputContract: "customer_need, scope, timeline, constraints",
    outputContract: "Proposal document",
  },
  meeting_summarizer: {
    templateId: "meeting_notes",
    inputContract: "meeting_notes, participants, desired_outcome",
    outputContract: "Meeting summary with decisions and actions",
  },
  contract_review: {
    templateId: "tos_review",
    inputContract: "contract_text, review_goal, jurisdiction_context",
    outputContract: "Contract review report",
  },
  landing_page_builder: {
    templateId: "web_build_handoff",
    inputContract: "offer, audience, proof_points, constraints",
    outputContract: "Landing page copy and build handoff",
  },
};

export function loadCertifiedSkillPackRegistry(
  path = CERTIFIED_SKILL_PACK_REGISTRY_PATH,
): CertifiedSkillPackRegistry {
  const resolvedPath = resolveWorkspacePath(path);
  if (!resolvedPath) {
    throw new Error(`Certified skill pack registry not found: ${path}`);
  }
  const payload = JSON.parse(readFileSync(resolvedPath, "utf8")) as CertifiedSkillPackRegistry;
  if (!Array.isArray(payload.entries)) {
    throw new Error(`Certified skill pack registry has no entries: ${path}`);
  }
  return payload;
}

export function listProductOutcomeRuntimePlans(
  registryPath = CERTIFIED_SKILL_PACK_REGISTRY_PATH,
): ProductOutcomeRuntimePlan[] {
  return loadCertifiedSkillPackRegistry(registryPath).entries.map(buildProductOutcomeRuntimePlan);
}

export function resolveProductOutcomeRuntimePlan(
  idOrOutcomeKey: string,
  registryPath = CERTIFIED_SKILL_PACK_REGISTRY_PATH,
): ProductOutcomeRuntimePlan | undefined {
  const normalized = idOrOutcomeKey.trim();
  return listProductOutcomeRuntimePlans(registryPath).find((plan) => {
    return plan.skillPackId === normalized || plan.outcomeKey === normalized;
  });
}

export function buildProductOutcomeRuntimePlan(entry: CertifiedSkillPackEntry): ProductOutcomeRuntimePlan {
  const binding = RUNTIME_BINDINGS[entry.id] ?? RUNTIME_BINDINGS[entry.outcomeKey];
  if (!binding) {
    throw new Error(`No product outcome runtime binding for certified pack: ${entry.id}`);
  }

  return {
    planVersion: "cvf.productOutcomeRuntime.v1",
    skillPackId: entry.id,
    outcomeKey: entry.outcomeKey,
    name: entry.name,
    domain: entry.domain,
    riskLevel: entry.riskLevel,
    status: entry.status,
    templateId: binding.templateId,
    routeOwner: "cvf-web /api/execute",
    command: `cvf run ${entry.id} --role BUILDER --receipt`,
    inputContract: binding.inputContract,
    outputContract: binding.outputContract,
    receiptSchemaPath: `${entry.path}/receipt.schema.json`,
    failureRecoveryPath: `${entry.path}/failure.recovery.md`,
    executionBoundaryPath: `${entry.path}/execution.boundary.json`,
    authorityScopePath: `${entry.path}/authority.scope.json`,
    workflowSpecPath: `${entry.path}/workflow.spec.md`,
    policyRefs: ["CVF_CAPABILITY_INTAKE_PIPELINE_GUARD", "cvf-web /api/execute"],
  };
}

export function assertProductOutcomeRuntimePlanFiles(plan: ProductOutcomeRuntimePlan): void {
  const requiredPaths = [
    plan.receiptSchemaPath,
    plan.failureRecoveryPath,
    plan.executionBoundaryPath,
    plan.authorityScopePath,
    plan.workflowSpecPath,
  ];
  const missing = requiredPaths.filter((path) => !resolveWorkspacePath(path));
  if (missing.length) {
    throw new Error(`Product outcome runtime plan has missing files for ${plan.skillPackId}: ${missing.join(", ")}`);
  }
}

function resolveWorkspacePath(path: string): string | undefined {
  if (existsSync(path)) return path;
  const fromPackage = join(process.cwd(), "..", "..", path);
  if (existsSync(fromPackage)) return fromPackage;
  return undefined;
}
