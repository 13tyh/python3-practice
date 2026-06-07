import { phase1Steps } from "./phase1Steps";
import { phase2Steps } from "./phase2Steps";
import { phase3Steps } from "./phase3Steps";
import { phase4Steps } from "./phase4Steps";
import { phase5Steps } from "./phase5Steps";
import { phase6Steps } from "./phase6Steps";
import { phase7Steps } from "./phase7Steps";
import type { Step } from "./stepTypes";

export type LearningPhase = {
  id: string;
  title: string;
  steps: Step[];
};

export const learningPhases: LearningPhase[] = [
  { id: "phase1", title: "Phase 1 / Python基礎集中", steps: phase1Steps },
  { id: "phase2", title: "Phase 2 / テスト・設計", steps: phase2Steps },
  { id: "phase3", title: "Phase 3 / FastAPI・外部API", steps: phase3Steps },
  { id: "phase4", title: "Phase 4 / DB・性能・データ", steps: phase4Steps },
  { id: "phase5", title: "Phase 5 / AI・RAG", steps: phase5Steps },
  { id: "phase6", title: "Phase 6 / 統合・レビュー", steps: phase6Steps },
  { id: "phase7", title: "Phase 7 / 運用・開発フロー", steps: phase7Steps },
];

export function phaseTitleForStepId(stepId: string) {
  return learningPhases.find((phase) => phase.steps.some((step) => step.id === stepId))?.title ?? learningPhases[0].title;
}

export function phaseTitleForPosition(position: number) {
  let end = 0;
  for (const phase of learningPhases) {
    end += phase.steps.length;
    if (position <= end) return phase.title;
  }
  return learningPhases[learningPhases.length - 1]?.title ?? "";
}
