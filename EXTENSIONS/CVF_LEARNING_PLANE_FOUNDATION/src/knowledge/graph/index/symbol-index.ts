import { readFileSync } from "node:fs";
import { parseFileToAST } from "../ast/ast-parser";
import {
  createDependencyGraph,
  type DependencyGraph,
  type GraphEdge,
  type GraphKnowledgeService,
  type GraphNode,
  type GraphQueryResult,
  type GraphSourceFile,
} from "../schema/graph-schema";

export interface SymbolIndex {
  graph: DependencyGraph;
  byName: ReadonlyMap<string, readonly GraphNode[]>;
  byFile: ReadonlyMap<string, readonly GraphNode[]>;
  getDependencies(nodeId: string): readonly GraphEdge[];
  getDependents(nodeId: string): readonly GraphEdge[];
}

function groupBy<T>(items: readonly T[], selector: (item: T) => string): ReadonlyMap<string, readonly T[]> {
  const grouped = new Map<string, T[]>();
  for (const item of items) {
    const key = selector(item);
    grouped.set(key, [...(grouped.get(key) ?? []), item]);
  }
  return grouped;
}

export function buildSymbolIndexFromSources(
  files: readonly GraphSourceFile[],
): SymbolIndex {
  const parsed = files.map((file) => parseFileToAST(file.filePath, file.source));
  const graph = createDependencyGraph(
    parsed.flatMap((ast) => ast.symbols),
    parsed.flatMap((ast) => ast.dependencies),
  );

  return {
    graph,
    byName: groupBy(graph.nodes, (node) => node.name),
    byFile: groupBy(graph.nodes, (node) => node.filePath),
    getDependencies(nodeId: string): readonly GraphEdge[] {
      return graph.edges.filter((edge) => edge.from === nodeId);
    },
    getDependents(nodeId: string): readonly GraphEdge[] {
      return graph.edges.filter((edge) => edge.to === nodeId);
    },
  };
}

export function buildSymbolIndex(filePaths: readonly string[]): SymbolIndex {
  return buildSymbolIndexFromSources(filePaths.map((filePath) => ({
    filePath,
    source: readFileSync(filePath, "utf8"),
  })));
}

export function lookupSymbol(index: SymbolIndex, name: string): readonly GraphNode[] {
  return index.byName.get(name) ?? [];
}

export function createInMemoryGraphKnowledgeService(
  initialSources: readonly GraphSourceFile[] = [],
): GraphKnowledgeService & { index: SymbolIndex } {
  let currentIndex = buildSymbolIndexFromSources(initialSources);

  return {
    get index(): SymbolIndex {
      return currentIndex;
    },
    async buildIndex(files: readonly string[]): Promise<SymbolIndex> {
      currentIndex = buildSymbolIndex(files);
      return currentIndex;
    },
    queryImpact(input: {
      queryId: string;
      changedFiles?: readonly string[];
      targetSymbols?: readonly string[];
      maxDepth?: number;
    }): GraphQueryResult {
      const changedFiles = new Set(input.changedFiles ?? []);
      const targetSymbols = new Set(input.targetSymbols ?? []);
      const seedNodes = currentIndex.graph.nodes.filter((node) =>
        changedFiles.has(node.filePath) || targetSymbols.has(node.name)
      );
      const nodeIds = new Set(seedNodes.map((node) => node.id));
      const maxDepth = Math.max(1, input.maxDepth ?? 1);

      for (let depth = 0; depth < maxDepth; depth += 1) {
        for (const edge of currentIndex.graph.edges) {
          if (nodeIds.has(edge.from) || nodeIds.has(edge.to)) {
            nodeIds.add(edge.from);
            nodeIds.add(edge.to);
          }
        }
      }

      const resolvedNodes = currentIndex.graph.nodes.filter((node) => nodeIds.has(node.id));
      const resolvedEdges = currentIndex.graph.edges.filter((edge) =>
        nodeIds.has(edge.from) && nodeIds.has(edge.to)
      );
      const affectedFiles = [...new Set(resolvedNodes.map((node) => node.filePath))];

      return {
        queryId: input.queryId,
        queryType: "impact",
        inputScope: [...changedFiles, ...targetSymbols],
        resolvedNodes,
        resolvedEdges,
        affectedFiles,
        confidenceSummary: resolvedNodes.some((node) => node.confidence === "low") ? "low" : "medium",
        tokenBudgetEstimate: resolvedNodes.length * 80 + resolvedEdges.length * 20,
        warnings: ["graph_outputs_are_evidence_not_authority"],
      };
    },
  };
}
