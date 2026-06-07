<script setup lang="ts">
import {
  AlertTriangle,
  PencilLine,
} from "lucide-vue-next";
import { computed, onMounted, onUnmounted, ref, watch } from "vue";
import { fetchStepReferences, type StepReference } from "./api/learningApi";
import CommandList from "./components/CommandList.vue";
import CommandCenter from "./components/CommandCenter.vue";
import LearningToolbar from "./components/LearningToolbar.vue";
import LearningLogPanel from "./components/LearningLogPanel.vue";
import LessonHeader from "./components/LessonHeader.vue";
import MentorSidebar from "./components/MentorSidebar.vue";
import MasteryLab from "./components/MasteryLab.vue";
import MissionBoard from "./components/MissionBoard.vue";
import OnboardingModal from "./components/OnboardingModal.vue";
import RunResultCard from "./components/RunResultCard.vue";
import SessionSummaryModal from "./components/SessionSummaryModal.vue";
import StudyRail from "./components/StudyRail.vue";
import { useStepProgress } from "./composables/useStepProgress";
import { useLearningLog, type LearningEvent } from "./composables/useLearningLog";
import { useStepRunner } from "./composables/useStepRunner";
import { buildStepGuide, getPhase, isRunnable, statusLabel } from "./data/learningUi";
import { learningPhases } from "./data/phaseConfig";
import { analyzeLearningLog } from "./data/learningLogAnalysis";
import { filterSteps, findStepById, stepAtOffset, stepNumberOf } from "./data/stepNavigation";
import { categories, steps, type Step, type StepStatus } from "./data/steps";

const initialHash = window.location.hash.replace("#", "");
const selectedId = ref(initialHash && initialHash !== "home" ? initialHash : steps[0].id);
const query = ref("");
const selectedCategory = ref("all");
const hideDone = ref(window.localStorage.getItem("python-master-hide-done") === "true");
const isSidebarOpen = ref(true);
const isLightMode = ref(window.localStorage.getItem("python-master-light-mode") === "true");
const isHomeView = ref(initialHash === "home");
const isOnboardingOpen = ref(false);
const isSearchOpen = ref(false);
const isSessionSummaryOpen = ref(false);
const isTodayOnly = ref(window.localStorage.getItem("python-master-today-only") === "true");
const isReferenceOpen = ref(false);
const isLabOpen = ref(false);
const inspectedFile = ref("");
const latestSession = ref<SessionSummary | null>(null);
const stepReferences = ref<StepReference[]>([]);
const {
  exportProgress,
  getStatus,
  importProgress,
  markTestFailed,
  markTestPassed,
  markTestStarted,
  resetProgress,
  setStatus,
} = useStepProgress();
const { exportLearningLog, importLearningLog, learningEvents, recordRun, resetLearningLog } = useLearningLog();

onMounted(async () => {
  window.addEventListener("hashchange", syncSelectedFromHash);
  window.addEventListener("keydown", handleShortcut);
  syncSelectedFromHash();
  if (window.localStorage.getItem("python-master-onboarding-seen") !== "true") {
    isOnboardingOpen.value = true;
  }
  try {
    stepReferences.value = await fetchStepReferences();
  } catch {
    stepReferences.value = [];
  }
});

onUnmounted(() => {
  window.removeEventListener("hashchange", syncSelectedFromHash);
  window.removeEventListener("keydown", handleShortcut);
});

const selectedStep = computed(() => findStepById(steps, selectedId.value));
const { runCommand, runError, runningCommand, runResult } = useStepRunner(selectedStep, {
  markTestFailed,
  markTestPassed,
  markTestStarted,
  setStatus,
}, { recordRun });
const learningAnalysis = computed(() => analyzeLearningLog(steps, getStatus, learningEvents.value));
const todayStepIds = computed(() => new Set(learningAnalysis.value.focusQueue.map((item) => item.stepId)));
const visibleSteps = computed(() => {
  let result = isTodayOnly.value ? steps.filter((step) => todayStepIds.value.has(step.id)) : steps;
  if (hideDone.value) result = result.filter((step) => getStatus(step.id) !== "done");
  return result.length > 0 ? result : steps;
});
const filteredSteps = computed(() => filterSteps(visibleSteps.value, query.value, selectedCategory.value));
const phaseGroups = computed(() => {
  const visibleIds = new Set(filteredSteps.value.map((step) => step.id));
  return learningPhases
    .map((phase) => ({
      id: phase.id,
      title: phase.title,
      steps: phase.steps.filter((step) => visibleIds.has(step.id)),
    }))
    .filter((phase) => phase.steps.length > 0);
});

const doneCount = computed(() => steps.filter((step) => getStatus(step.id) === "done").length);
const doingCount = computed(() => steps.filter((step) => getStatus(step.id) === "doing").length);
const progressPercent = computed(() => Math.round((doneCount.value / steps.length) * 100));
const selectedNumber = computed(() => stepNumberOf(steps, selectedStep.value.id));
const currentPhase = computed(() => getPhase(selectedNumber.value));
const runnableCommands = computed(() => selectedStep.value.commands.filter((command) => isRunnable(command)));
const additionalCommands = computed(() => selectedStep.value.commands.slice(1));
const primaryCommand = computed(() => selectedStep.value.commands[0] ?? "");
const shouldShowMongo = computed(
  () => selectedStep.value.category === "db" || selectedStep.value.id.includes("mongo"),
);
const selectedReference = computed(() =>
  stepReferences.value.find((reference) => reference.step === selectedStep.value.id),
);
const selectedGuide = computed(() => buildStepGuide(selectedStep.value));

type SessionSummary = {
  at: string;
  failedRuns: number;
  nextItems: string[];
  totalRuns: number;
};

watch(hideDone, (value) => window.localStorage.setItem("python-master-hide-done", String(value)));
watch(isTodayOnly, (value) => window.localStorage.setItem("python-master-today-only", String(value)));

function stepNumber(id: string) {
  return stepNumberOf(steps, id);
}

function syncSelectedFromHash() {
  const hashId = window.location.hash.replace("#", "");
  if (hashId === "home") {
    isHomeView.value = true;
    return;
  }
  if (!hashId) {
    isHomeView.value = false;
    selectedId.value = steps[0].id;
    return;
  }
  if (steps.some((step) => step.id === hashId)) {
    isHomeView.value = false;
    selectedId.value = hashId;
  }
}

function selectStep(step: Step) {
  isHomeView.value = false;
  selectedId.value = step.id;
  window.location.hash = step.id;
}

function move(offset: number) {
  selectStep(stepAtOffset(steps, selectedStep.value.id, offset));
}

function inspectFile(file: string) {
  inspectedFile.value = file;
  isLabOpen.value = true;
}

function closeOnboarding() {
  window.localStorage.setItem("python-master-onboarding-seen", "true");
  isOnboardingOpen.value = false;
}

function handleShortcut(event: KeyboardEvent) {
  if (isTypingTarget(event.target)) return;
  if (event.key === "j") {
    event.preventDefault();
    move(1);
  }
  if (event.key === "k") {
    event.preventDefault();
    move(-1);
  }
  if (event.key === "r") {
    event.preventDefault();
    runCommand(primaryCommand.value);
  }
  if (event.key === "/") {
    event.preventDefault();
    isSearchOpen.value = true;
  }
  if (event.key === "s") {
    event.preventDefault();
    isSidebarOpen.value = !isSidebarOpen.value;
  }
  if (event.key === "l") {
    event.preventDefault();
    toggleLightMode();
  }
  if (event.key === "h") {
    event.preventDefault();
    openHome();
  }
  if (event.key === "Escape") {
    isSearchOpen.value = false;
    isOnboardingOpen.value = false;
  }
}

function isTypingTarget(target: EventTarget | null) {
  const element = target as HTMLElement | null;
  return Boolean(element && "closest" in element && element.closest("input, textarea, select, [contenteditable='true']"));
}

function downloadReport() {
  const byCategory = new Map<string, { done: number; total: number }>();
  for (const step of steps) {
    const entry = byCategory.get(step.category) ?? { done: 0, total: 0 };
    entry.total += 1;
    if (getStatus(step.id) === "done") entry.done += 1;
    byCategory.set(step.category, entry);
  }
  const memoLines = collectLabMemos()
    .flatMap(({ step, state }) => [
      `### ${step.title} (${step.id})`,
      state.answer ? `- 理解メモ: ${state.answer}` : "",
      state.review ? `- レビュー: ${state.review}` : "",
      state.ragQuestion ? `- RAG質問: ${state.ragQuestion}` : "",
      "",
    ])
    .filter(Boolean);
  const lines = [
    "# Python Master 学習レポート",
    "",
    `- 出力日時: ${new Date().toISOString()}`,
    `- 完了: ${doneCount.value} / ${steps.length}`,
    `- 学習中: ${doingCount.value}`,
    "",
    "## カテゴリ別",
    ...[...byCategory.entries()].map(([category, value]) => `- ${category}: ${value.done} / ${value.total}`),
    "",
    "## 未完了の次候補",
    ...steps.filter((step) => getStatus(step.id) !== "done").slice(0, 10).map((step) => `- ${step.title} (${step.id})`),
    "",
    "## 学習メモ",
    ...(memoLines.length > 0 ? memoLines : ["- まだメモはありません"]),
    "",
    "## 学習ログ",
    `- 実行回数: ${learningEvents.value.length}`,
    `- 失敗回数: ${learningEvents.value.filter((event) => !event.ok).length}`,
    ...learningEvents.value.slice(-10).map((event) => `- ${event.at} ${event.ok ? "OK" : "NG"} ${event.stepTitle}`),
  ];
  downloadText("python-master-report.md", lines.join("\n"), "text/markdown");
}

function downloadBackup() {
  const labEntries: Record<string, string> = {};
  for (let index = 0; index < window.localStorage.length; index += 1) {
    const key = window.localStorage.key(index) ?? "";
    if (key.startsWith("python-master-lab:")) labEntries[key] = window.localStorage.getItem(key) ?? "";
  }
  downloadText(
    "python-master-backup.json",
    JSON.stringify(
      {
        exportedAt: new Date().toISOString(),
        labEntries,
        learningEvents: exportLearningLog(),
        progress: exportProgress(),
        version: 1,
      },
      null,
      2,
    ),
    "application/json",
  );
}

function importBackup(text: string) {
  const data = JSON.parse(text) as {
    labEntries?: Record<string, string>;
    learningEvents?: LearningEvent[];
    progress?: { passedTests?: Record<string, boolean>; statuses?: Record<string, StepStatus> };
  };
  if (data.progress) importProgress(data.progress);
  importLearningLog(data.learningEvents);
  for (const [key, value] of Object.entries(data.labEntries ?? {})) {
    if (key.startsWith("python-master-lab:")) window.localStorage.setItem(key, value);
  }
}

function resetAllProgress() {
  resetProgress();
  resetLearningLog();
  for (const key of Object.keys(window.localStorage)) {
    if (key.startsWith("python-master-lab:")) window.localStorage.removeItem(key);
  }
}

function openHome() {
  isHomeView.value = true;
  window.location.hash = "home";
}

function toggleTodayOnly() {
  isTodayOnly.value = !isTodayOnly.value;
  if (isTodayOnly.value) selectFirstFocusStep();
}

function toggleHideDone() {
  hideDone.value = !hideDone.value;
}

function startBasicReview() {
  selectedCategory.value = "basic";
  hideDone.value = true;
  isTodayOnly.value = false;
  const firstBasic = steps.find((step) => step.level === "基礎" && getStatus(step.id) !== "done");
  if (firstBasic) selectStep(firstBasic);
}

function selectFirstFocusStep() {
  const first = steps.find((step) => step.id === learningAnalysis.value.focusQueue[0]?.stepId);
  if (first) selectStep(first);
}

function finishSession() {
  const summary: SessionSummary = {
    at: new Date().toISOString(),
    failedRuns: learningEvents.value.filter((event) => !event.ok).length,
    nextItems: learningAnalysis.value.focusQueue.map((item) => `${item.label}: ${item.title}`),
    totalRuns: learningEvents.value.length,
  };
  latestSession.value = summary;
  saveSessionSummary(summary);
  isSessionSummaryOpen.value = true;
}

function saveSessionSummary(summary: SessionSummary) {
  const key = "python-master-session-summaries";
  const saved = window.localStorage.getItem(key);
  const summaries = saved ? (JSON.parse(saved) as SessionSummary[]) : [];
  window.localStorage.setItem(key, JSON.stringify([...summaries, summary].slice(-30)));
}

function toggleLightMode() {
  isLightMode.value = !isLightMode.value;
  window.localStorage.setItem("python-master-light-mode", String(isLightMode.value));
}

function downloadText(filename: string, body: string, type: string) {
  const url = URL.createObjectURL(new Blob([body], { type }));
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = filename;
  anchor.click();
  URL.revokeObjectURL(url);
}

function collectLabMemos() {
  return steps
    .map((step) => ({ step, state: readLabState(step.id) }))
    .filter(({ state }) => state.answer || state.review || state.ragQuestion);
}

function readLabState(stepId: string) {
  const raw = window.localStorage.getItem(`python-master-lab:${stepId}`);
  if (!raw) return { answer: "", ragQuestion: "", review: "" };
  try {
    const value = JSON.parse(raw) as { answer?: string; ragQuestion?: string; review?: string };
    return {
      answer: value.answer?.trim() ?? "",
      ragQuestion: value.ragQuestion?.trim() ?? "",
      review: value.review?.trim() ?? "",
    };
  } catch {
    return { answer: "", ragQuestion: "", review: "" };
  }
}
</script>

<template>
  <div class="mentor-shell" :class="{ 'sidebar-collapsed': !isSidebarOpen, 'home-view': isHomeView, 'light-mode': isLightMode }">
    <MentorSidebar
      :categories="categories"
      :done-count="doneCount"
      :doing-count="doingCount"
      :get-status="getStatus"
      :is-home-view="isHomeView"
      :is-open="isSidebarOpen"
      :phase-groups="phaseGroups"
      :progress-percent="progressPercent"
      :query="query"
      :selected-category="selectedCategory"
      :selected-step="selectedStep"
      :step-number="stepNumber"
      :steps-length="steps.length"
      @open-home="openHome"
      @select-step="selectStep"
      @update:is-open="isSidebarOpen = $event"
      @update:query="query = $event"
      @update:selected-category="selectedCategory = $event"
    />

    <main class="mentor-main">
      <LearningToolbar
        :hide-done="hideDone"
        :is-home-view="isHomeView"
        :is-light-mode="isLightMode"
        :is-today-only="isTodayOnly"
        @download-backup="downloadBackup"
        @download-report="downloadReport"
        @finish-session="finishSession"
        @import-backup="importBackup"
        @open-home="openHome"
        @open-guide="isOnboardingOpen = true"
        @open-search="isSearchOpen = true"
        @reset-progress="resetAllProgress"
        @start-basic-review="startBasicReview"
        @toggle-hide-done="toggleHideDone"
        @toggle-light-mode="toggleLightMode"
        @toggle-today-only="toggleTodayOnly"
      />

      <section v-if="isHomeView" class="home-dashboard">
        <article class="home-hero">
          <span>home</span>
          <h2>次の1手だけ決める</h2>
          <p>上から順番に進めます。後半Phaseは、前半が終わるまで出しすぎません。</p>
          <div class="home-actions">
            <button type="button" @click="toggleTodayOnly">今日だけ表示</button>
            <button type="button" @click="startBasicReview">基礎復習</button>
            <button type="button" @click="finishSession">学習終了</button>
          </div>
        </article>
        <LearningLogPanel :events="learningEvents" :get-status="getStatus" :steps="steps" />
      </section>

      <LessonHeader v-if="!isHomeView" :current-phase="currentPhase" :step="selectedStep" @move="move" />

      <section v-if="!isHomeView" class="lesson-strip" aria-label="lesson overview">
        <div class="lesson-chip">
          <span>Step</span>
          <strong>{{ selectedNumber }} / {{ steps.length }}</strong>
        </div>
        <div class="lesson-chip">
          <span>状態</span>
          <strong>{{ statusLabel(getStatus(selectedStep.id)) }}</strong>
        </div>
        <div class="lesson-chip">
          <span>対象</span>
          <strong>{{ selectedStep.files.length }} files</strong>
        </div>
        <div class="lesson-chip">
          <span>実行</span>
          <strong>{{ runnableCommands.length }} commands</strong>
        </div>
      </section>

      <MissionBoard
        v-if="!isHomeView"
        :primary-command="primaryCommand"
        :running-command="runningCommand"
        :step="selectedStep"
        @run="runCommand"
      />

      <section v-if="!isHomeView" class="mentor-workspace">
        <div class="work-lane">
          <article class="work-card">
            <div class="work-title">
              <PencilLine :size="20" />
              <h3>書き方</h3>
            </div>
            <ol class="step-guide">
              <li v-for="tip in selectedGuide.writing" :key="tip">{{ tip }}</li>
            </ol>
          </article>

          <article class="work-card warning">
            <div class="work-title">
              <AlertTriangle :size="20" />
              <h3>注意点</h3>
            </div>
            <ul class="step-guide">
              <li v-for="tip in selectedGuide.cautions" :key="tip">{{ tip }}</li>
            </ul>
          </article>

          <RunResultCard
            :run-error="runError"
            :run-result="runResult"
            :running-command="runningCommand"
            @inspect-file="inspectFile"
          />

          <CommandList :commands="additionalCommands" :running-command="runningCommand" @run="runCommand" />
        </div>

        <section v-if="!isLightMode" class="collapse-stack">
          <article class="collapsible-panel">
            <button type="button" class="collapse-toggle" @click="isReferenceOpen = !isReferenceOpen">
              参照リソース / 対象ファイル
              <span>{{ isReferenceOpen ? "閉じる" : "開く" }}</span>
            </button>
            <StudyRail
              v-if="isReferenceOpen"
              :reference="selectedReference"
              :should-show-mongo="shouldShowMongo"
              :step="selectedStep"
            />
          </article>

          <article class="collapsible-panel">
            <button type="button" class="collapse-toggle" @click="isLabOpen = !isLabOpen">
              実務ラボ / 比較 / メモ / RAG
              <span>{{ isLabOpen ? "閉じる" : "開く" }}</span>
            </button>
            <MasteryLab
              v-if="isLabOpen"
              :all-steps="steps"
              :done-count="doneCount"
              :doing-count="doingCount"
              :get-status="getStatus"
              :inspected-file="inspectedFile"
              :run-result="runResult"
              :should-show-mongo="shouldShowMongo"
              :step="selectedStep"
              :steps-length="steps.length"
            />
          </article>
        </section>

        <article v-else class="light-focus-card" aria-label="軽量モード">
          <strong>軽量モード</strong>
          <p>今は問題、書き方、注意点、実行結果だけに絞っています。</p>
          <button type="button" @click="toggleLightMode">通常表示に戻す</button>
        </article>
      </section>
    </main>

    <OnboardingModal :open="isOnboardingOpen" @close="closeOnboarding" />
    <CommandCenter :open="isSearchOpen" :steps="steps" @close="isSearchOpen = false" @select-step="selectStep" />
    <SessionSummaryModal :open="isSessionSummaryOpen" :summary="latestSession" @close="isSessionSummaryOpen = false" />
  </div>
</template>
