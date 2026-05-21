export type ProviderMethodName = "chat" | "stream" | "json_mode" | "vision" | "reasoning";

export interface ProviderMethodContract {
  providerId: string;
  modelId: string;
  supportedMethods: ProviderMethodName[];
  defaultMethod: ProviderMethodName;
  capabilityRef: string;
}

export interface ProviderCapabilityFile {
  providerId: string;
  models: Array<{
    modelId: string;
    supportedMethods: ProviderMethodName[];
    defaultMethod: ProviderMethodName;
  }>;
}
