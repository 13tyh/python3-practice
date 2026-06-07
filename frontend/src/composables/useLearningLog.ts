import { onMounted, ref, watch } from "vue";
import type { RunResult } from "../api/learningApi";
import type { Step } from "../data/stepTypes";

const storageKey = "python-master-learning-events";
const maxEvents = 300;

export type LearningEvent = {
  at: string;
  category: string;
  command: string;
  durationMs: number;
  exitCode: number;
  id: string;
  level: string;
  ok: boolean;
  stepId: string;
  stepTitle: string;
};

export function useLearningLog(now = () => new Date()) {
  const learningEvents = ref<LearningEvent[]>([]);

  onMounted(() => {
    const saved = window.localStorage.getItem(storageKey);
    if (saved) learningEvents.value = JSON.parse(saved) as LearningEvent[];
  });

  watch(
    learningEvents,
    (value) => window.localStorage.setItem(storageKey, JSON.stringify(value)),
    { deep: true },
  );

  function recordRun(step: Step, result: RunResult) {
    const at = now().toISOString();
    learningEvents.value = [
      ...learningEvents.value,
      {
        at,
        category: step.category,
        command: result.command,
        durationMs: result.duration_ms,
        exitCode: result.exit_code,
        id: `${at}:${step.id}:${learningEvents.value.length}`,
        level: step.level,
        ok: result.exit_code === 0,
        stepId: step.id,
        stepTitle: step.title,
      },
    ].slice(-maxEvents);
  }

  function exportLearningLog() {
    return learningEvents.value;
  }

  function importLearningLog(events: LearningEvent[] = []) {
    learningEvents.value = events.slice(-maxEvents);
  }

  function resetLearningLog() {
    learningEvents.value = [];
  }

  return {
    exportLearningLog,
    importLearningLog,
    learningEvents,
    recordRun,
    resetLearningLog,
  };
}
