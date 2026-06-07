import { onMounted, ref, watch } from "vue";
import type { StepStatus } from "../data/steps";

const storageKey = "python-master-step-status";
const passedTestsStorageKey = "python-master-passed-tests";

export function useStepProgress() {
  const statuses = ref<Record<string, StepStatus>>({});
  const passedTests = ref<Record<string, boolean>>({});

  onMounted(() => {
    const saved = localStorage.getItem(storageKey);
    if (saved) statuses.value = JSON.parse(saved) as Record<string, StepStatus>;
    const savedPassedTests = localStorage.getItem(passedTestsStorageKey);
    if (savedPassedTests) passedTests.value = JSON.parse(savedPassedTests) as Record<string, boolean>;
  });

  watch(
    statuses,
    (value) => localStorage.setItem(storageKey, JSON.stringify(value)),
    { deep: true },
  );

  watch(
    passedTests,
    (value) => localStorage.setItem(passedTestsStorageKey, JSON.stringify(value)),
    { deep: true },
  );

  function getStatus(id: string): StepStatus {
    const status = statuses.value[id] ?? "todo";
    if (status === "done" && !passedTests.value[id]) return "doing";
    return status;
  }

  function setStatus(id: string, status: StepStatus) {
    statuses.value = { ...statuses.value, [id]: status };
  }

  function markTestStarted(id: string) {
    passedTests.value = { ...passedTests.value, [id]: false };
  }

  function markTestPassed(id: string) {
    passedTests.value = { ...passedTests.value, [id]: true };
    setStatus(id, "done");
  }

  function markTestFailed(id: string) {
    passedTests.value = { ...passedTests.value, [id]: false };
    setStatus(id, "doing");
  }

  function exportProgress() {
    return {
      passedTests: passedTests.value,
      statuses: statuses.value,
    };
  }

  function importProgress(value: { passedTests?: Record<string, boolean>; statuses?: Record<string, StepStatus> }) {
    statuses.value = value.statuses ?? {};
    passedTests.value = value.passedTests ?? {};
  }

  function resetProgress() {
    statuses.value = {};
    passedTests.value = {};
  }

  return {
    exportProgress,
    getStatus,
    importProgress,
    markTestFailed,
    markTestPassed,
    markTestStarted,
    resetProgress,
    setStatus,
  };
}
