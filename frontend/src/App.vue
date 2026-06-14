<script setup lang="ts">
import {
  AlertTriangle,
  PencilLine,
} from "lucide-vue-next";
import { computed, onMounted, onUnmounted, ref, watch } from "vue";
import { fetchStepReferences, type StepReference } from "./api/learningApi";
import CommandList from "./components/CommandList.vue";
import CommandCenter from "./components/CommandCenter.vue";
import FileTestList from "./components/FileTestList.vue";
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
import { useLearningLog } from "./composables/useLearningLog";
import { useStepRunner } from "./composables/useStepRunner";
import { buildStepGuide, fileTestCommandsForStep, getPhase, isRunnable, statusLabel } from "./data/learningUi";
import { learningPhases } from "./data/phaseConfig";
import { analyzeLearningLog } from "./data/learningLogAnalysis";
import { filterSteps, findStepById, stepAtOffset, stepNumberOf } from "./data/stepNavigation";
import { categories, steps, type Step } from "./data/steps";

const initialHash = window.location.hash.replace("#", "");
const selectedId = ref(initialHash && initialHash !== "home" ? initialHash : steps[0].id);
const query = ref("");
const selectedCategory = ref("all");
const hideDone = ref(window.localStorage.getItem("python-master-hide-done") === "true");
const isSidebarOpen = ref(true);
const isLightMode = ref(window.localStorage.getItem("python-master-light-mode") === "true");
const isHomeView = ref(!initialHash || initialHash === "home");
const isOnboardingOpen = ref(false);
const isSearchOpen = ref(false);
const isSessionSummaryOpen = ref(false);
const isTodayOnly = ref(window.localStorage.getItem("python-master-today-only") === "true");
const isReferenceOpen = ref(false);
const isLabOpen = ref(false);
const inspectedFile = ref("");
const latestSession = ref<SessionSummary | null>(null);
const stepReferences = ref<StepReference[]>([]);
type LessonTab = "read" | "write" | "run" | "review";
const activeLessonTab = ref<LessonTab>("read");
const lessonTabs: Array<{ id: LessonTab; label: string }> = [
  { id: "read", label: "読む" },
  { id: "write", label: "書く" },
  { id: "run", label: "実行" },
  { id: "review", label: "振り返り" },
];
const {
  getStatus,
  markTestFailed,
  markTestPassed,
  markTestStarted,
  resetProgress,
  setStatus,
} = useStepProgress();
const { learningEvents, recordRun, resetLearningLog } = useLearningLog();

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
const todayStepIds = computed(() => new Set(learningAnalysis.value.todayTop3.map((item) => item.stepId)));
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
const runCommands = computed(() => [primaryCommand.value, ...additionalCommands.value].filter(Boolean));
const fileTestCommands = computed(() => fileTestCommandsForStep(selectedStep.value));
const acceptanceChecklist = computed(() =>
  [
    `${primaryCommand.value || "pytest"} が成功する`,
    ...selectedStep.value.goals.slice(0, 2).map((goal) => `${goal} を説明できる`),
    "失敗時に原因ファイルと修正理由を1文で残せる",
  ].slice(0, 4),
);
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
watch(
  () => selectedStep.value.id,
  () => {
    activeLessonTab.value = "read";
  },
);

function stepNumber(id: string) {
  return stepNumberOf(steps, id);
}

function syncSelectedFromHash() {
  const hashId = window.location.hash.replace("#", "");
  if (!hashId || hashId === "home") {
    isHomeView.value = true;
    if (!hashId) replaceHashWithHome();
    return;
  }
  if (steps.some((step) => step.id === hashId)) {
    isHomeView.value = false;
    selectedId.value = hashId;
  }
}

function replaceHashWithHome() {
  window.history.replaceState(null, "", `${window.location.pathname}${window.location.search}#home`);
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
  activeLessonTab.value = "review";
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
    runAndShowResult(primaryCommand.value);
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

function startRandomBasicDrill() {
  const unfinishedBasics = steps.filter((step) => step.level === "基礎" && getStatus(step.id) !== "done");
  const basics = unfinishedBasics.length > 0 ? unfinishedBasics : steps.filter((step) => step.level === "基礎");
  const step = basics[Math.floor(Math.random() * basics.length)];
  if (step) {
    selectStep(step);
    window.setTimeout(() => {
      activeLessonTab.value = "write";
    }, 0);
  }
}

function selectFirstFocusStep() {
  const first = steps.find((step) => step.id === learningAnalysis.value.focusQueue[0]?.stepId);
  if (first) selectStep(first);
}

function runAndShowResult(command: string) {
  activeLessonTab.value = "run";
  runCommand(command);
}

function finishSession() {
  const summary: SessionSummary = {
    at: new Date().toISOString(),
    failedRuns: learningEvents.value.filter((event) => !event.ok).length,
    nextItems: learningAnalysis.value.todayTop3.map((item) => `${item.label}: ${item.title}`),
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
        @finish-session="finishSession"
        @open-home="openHome"
        @open-guide="isOnboardingOpen = true"
        @open-search="isSearchOpen = true"
        @reset-progress="resetAllProgress"
        @start-basic-review="startBasicReview"
        @start-random-basic="startRandomBasicDrill"
        @toggle-hide-done="toggleHideDone"
        @toggle-light-mode="toggleLightMode"
        @toggle-today-only="toggleTodayOnly"
      />

      <section v-if="isHomeView" class="home-dashboard">
        <article class="home-hero home-focus">
          <span>Today</span>
          <h2>今日やる3問を上から片づける</h2>
          <p>迷う時間を減らすために、失敗復習、基礎、次のStepだけを先に出します。</p>
          <div class="home-focus-grid">
            <a v-for="item in learningAnalysis.todayTop3" :key="item.stepId" :href="`#${item.stepId}`">
              <strong>{{ item.label }}</strong>
              <span>{{ item.title }}</span>
              <small>{{ item.reason }}</small>
            </a>
          </div>
          <div class="home-actions">
            <button type="button" @click="toggleTodayOnly">今日だけ表示</button>
            <button type="button" @click="startBasicReview">基礎復習</button>
            <button type="button" @click="startRandomBasicDrill">ランダム基礎</button>
            <button type="button" @click="finishSession">学習終了</button>
          </div>
        </article>

        <aside class="home-side-panel" aria-label="学習状況">
          <article class="home-stat-card">
            <span>Progress</span>
            <strong>{{ progressPercent }}%</strong>
            <small>{{ doneCount }} / {{ steps.length }} 完了</small>
          </article>
          <article class="home-stat-card">
            <span>Runs</span>
            <strong>{{ learningAnalysis.totalRuns }}</strong>
            <small>成功率 {{ learningAnalysis.successRate }}%</small>
          </article>
          <article class="home-rule-card">
            <strong>15分ルール</strong>
            <p>読む、書く、実行、1行メモ。詰まったら解答例と差分を見る。</p>
          </article>
        </aside>

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

      <nav v-if="!isHomeView" class="lesson-tabs" aria-label="Step作業タブ">
        <button
          v-for="tab in lessonTabs"
          :key="tab.id"
          type="button"
          :class="{ active: activeLessonTab === tab.id }"
          @click="activeLessonTab = tab.id"
        >
          {{ tab.label }}
        </button>
      </nav>

      <MissionBoard
        v-if="!isHomeView && activeLessonTab === 'read'"
        :primary-command="primaryCommand"
        :running-command="runningCommand"
        :step="selectedStep"
        @run="runAndShowResult"
      />

      <article v-if="!isHomeView && activeLessonTab === 'read'" class="work-card acceptance-card">
        <div class="work-title">
          <PencilLine :size="20" />
          <h3>最短合格条件</h3>
        </div>
        <ul class="step-guide">
          <li v-for="item in acceptanceChecklist" :key="item">{{ item }}</li>
        </ul>
      </article>

      <section v-if="!isHomeView && activeLessonTab !== 'read'" class="mentor-workspace">
        <div class="work-lane">
          <article v-if="activeLessonTab === 'write'" class="work-card">
            <div class="work-title">
              <PencilLine :size="20" />
              <h3>書き方</h3>
            </div>
            <ol class="step-guide">
              <li v-for="tip in selectedGuide.writing" :key="tip">{{ tip }}</li>
            </ol>
          </article>

          <article v-if="activeLessonTab === 'write'" class="work-card warning">
            <div class="work-title">
              <AlertTriangle :size="20" />
              <h3>注意点</h3>
            </div>
            <ul class="step-guide">
              <li v-for="tip in selectedGuide.cautions" :key="tip">{{ tip }}</li>
            </ul>
          </article>

          <RunResultCard
            v-if="activeLessonTab === 'run'"
            :run-error="runError"
            :run-result="runResult"
            :running-command="runningCommand"
            @inspect-file="inspectFile"
          />

          <CommandList
            v-if="activeLessonTab === 'run'"
            :commands="runCommands"
            :running-command="runningCommand"
            @run="runAndShowResult"
          />

          <FileTestList
            v-if="activeLessonTab === 'run'"
            :items="fileTestCommands"
            :running-command="runningCommand"
            @run="runAndShowResult"
          />
        </div>

        <section v-if="activeLessonTab === 'review' && !isLightMode" class="collapse-stack">
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

        <article v-else-if="activeLessonTab === 'review'" class="light-focus-card" aria-label="軽量モード">
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
