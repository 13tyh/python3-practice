import type { ComputedRef } from "vue";
import { ref } from "vue";
import { runLearningCommand, type RunResult } from "../api/learningApi";
import { isRunnable, isTestCommand } from "../data/learningUi";
import type { Step, StepStatus } from "../data/stepTypes";

type StepProgressApi = {
  markTestFailed: (id: string) => void;
  markTestPassed: (id: string) => void;
  markTestStarted: (id: string) => void;
  setStatus: (id: string, status: StepStatus) => void;
};

type StepRunLogger = {
  recordRun: (step: Step, result: RunResult) => void;
};

export function useStepRunner(selectedStep: ComputedRef<Step>, progress: StepProgressApi, logger?: StepRunLogger) {
  const runningCommand = ref("");
  const runResult = ref<RunResult | null>(null);
  const runError = ref("");

  async function runCommand(command: string) {
    if (!isRunnable(command) || runningCommand.value) return;
    runningCommand.value = command;
    runError.value = "";
    runResult.value = null;
    progress.setStatus(selectedStep.value.id, "doing");
    if (isTestCommand(command)) {
      progress.markTestStarted(selectedStep.value.id);
    }
    try {
      runResult.value = await runLearningCommand(command);
      logger?.recordRun(selectedStep.value, runResult.value);
      if (isTestCommand(command) && runResult.value.exit_code === 0) {
        progress.markTestPassed(selectedStep.value.id);
      } else {
        if (isTestCommand(command)) progress.markTestFailed(selectedStep.value.id);
        else progress.setStatus(selectedStep.value.id, "doing");
      }
    } catch (error) {
      runError.value = error instanceof Error ? error.message : "コマンド実行に失敗しました";
    } finally {
      runningCommand.value = "";
    }
  }

  return {
    runCommand,
    runError,
    runningCommand,
    runResult,
  };
}
