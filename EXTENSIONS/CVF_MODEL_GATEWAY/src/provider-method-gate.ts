import type { ProviderCapabilityFile, ProviderMethodName } from "./provider-method-contract";

export class UnsupportedMethodError extends Error {
  constructor(
    public readonly providerId: string,
    public readonly modelId: string,
    public readonly method: ProviderMethodName,
  ) {
    super(`Unsupported provider method: ${providerId}/${modelId} does not support ${method}`);
    this.name = "UnsupportedMethodError";
  }
}

export function assertProviderMethodSupported(
  capability: ProviderCapabilityFile,
  modelId: string,
  method: ProviderMethodName,
): void {
  const model = capability.models.find((entry) => entry.modelId === modelId);
  if (!model || !model.supportedMethods.includes(method)) {
    throw new UnsupportedMethodError(capability.providerId, modelId, method);
  }
}

export function listSupportedMethods(
  capability: ProviderCapabilityFile,
  modelId: string,
): ProviderMethodName[] {
  return capability.models.find((entry) => entry.modelId === modelId)?.supportedMethods ?? [];
}
