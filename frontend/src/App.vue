<script setup lang="ts">
import {
  AlertTriangle,
  ArrowRight,
  BookOpenCheck,
  PencilLine,
  Play,
} from "lucide-vue-next";
import { computed, onMounted, onUnmounted, ref, watch } from "vue";
import { fetchStepReferences, type StepReference } from "./api/learningApi";
import CommandCenter from "./components/CommandCenter.vue";
import LearningToolbar from "./components/LearningToolbar.vue";
import LearningLogPanel from "./components/LearningLogPanel.vue";
import LessonHeader from "./components/LessonHeader.vue";
import MentorSidebar from "./components/MentorSidebar.vue";
import MasteryLab from "./components/MasteryLab.vue";
import MissionBoard from "./components/MissionBoard.vue";
import RunResultCard from "./components/RunResultCard.vue";
import SessionSummaryModal from "./components/SessionSummaryModal.vue";
import StudyRail from "./components/StudyRail.vue";
import { useStepProgress } from "./composables/useStepProgress";
import { useLearningLog } from "./composables/useLearningLog";
import { useStepRunner } from "./composables/useStepRunner";
import { buildStepGuide, getPhase, isRunnable, methodPrimerForStep, primaryWorkFile, statusLabel } from "./data/learningUi";
import { learningPhases } from "./data/phaseConfig";
import { analyzeLearningLog } from "./data/learningLogAnalysis";
import { filterSteps, findStepById, stepAtOffset, stepNumberOf } from "./data/stepNavigation";
import { categories, steps, type Step } from "./data/steps";

const initialHash = window.location.hash.replace("#", "");
const selectedId = ref(initialHash && initialHash !== "home" ? initialHash : steps[0].id);
const query = ref("");
const selectedCategory = ref("all");
const isSidebarOpen = ref(window.localStorage.getItem("python-master-sidebar-open") === "true");
const isLightMode = ref(window.localStorage.getItem("python-master-light-mode") === "true");
const isHomeView = ref(!initialHash || initialHash === "home");
const isSearchOpen = ref(false);
const isSessionSummaryOpen = ref(false);
const isReferenceOpen = ref(false);
const isLabOpen = ref(false);
const inspectedFile = ref("");
const latestSession = ref<SessionSummary | null>(null);
const stepReferences = ref<StepReference[]>([]);
type LessonTab = "read" | "write" | "review";
const activeLessonTab = ref<LessonTab>("read");
const lessonTabs: Array<{ id: LessonTab; label: string }> = [
  { id: "read", label: "説明" },
  { id: "write", label: "解く" },
  { id: "review", label: "メモ" },
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
const visibleSteps = computed(() => {
  return steps;
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
const primaryCommand = computed(() => selectedStep.value.commands[0] ?? "");
const runnableCommands = computed(() => (isRunnable(primaryCommand.value) ? [primaryCommand.value] : []));
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
const selectedPrimer = computed(() => methodPrimerForStep(selectedStep.value));
const selectedWorkFile = computed(() => primaryWorkFile(selectedStep.value));
const nextFocusStep = computed(() => steps.find((step) => getStatus(step.id) !== "done") ?? steps[0]);
const nextFocusPrimer = computed(() => methodPrimerForStep(nextFocusStep.value));
const currentRunPassed = computed(
  () => runResult.value?.exit_code === 0 && runResult.value.command === primaryCommand.value,
);
const homeFlowItems = [
  { title: "1. この問題を解く", detail: "未完了の先頭Stepを開く" },
  { title: "2. テスト実行", detail: "結果を見てから直す" },
  { title: "3. 1ファイル修正", detail: "表示されたファイルだけ触る" },
  { title: "4. 次の問題へ", detail: "成功したら止まらず進む" },
];
const lessonAction = computed(() => {
  if (currentRunPassed.value) {
    return {
      title: "次の問題へ進む",
      detail: "このStepは成功しています。流れを切らずに次へ進みます。",
      state: "passed",
    };
  }
  if (runResult.value && runResult.value.exit_code !== 0) {
    return {
      title: "開くファイルを直す",
      detail: `${selectedWorkFile.value} のTODOか失敗行だけ直して、もう一度テスト実行します。`,
      state: "failed",
    };
  }
  return {
    title: "まずテスト実行を押す",
    detail: "最初に失敗内容を見ます。何を直すかはログが教えてくれます。",
    state: "start",
  };
});

type SessionSummary = {
  at: string;
  failedRuns: number;
  nextItems: string[];
  totalRuns: number;
};

watch(isSidebarOpen, (value) => window.localStorage.setItem("python-master-sidebar-open", String(value)));
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
  isSidebarOpen.value = false;
  selectedId.value = step.id;
  window.location.hash = step.id;
}

function move(offset: number) {
  selectStep(stepAtOffset(steps, selectedStep.value.id, offset));
}

function selectNextFocusStep() {
  selectStep(nextFocusStep.value);
}

function selectNextUnfinishedStep() {
  const currentIndex = steps.findIndex((step) => step.id === selectedStep.value.id);
  const afterCurrent = steps.slice(currentIndex + 1).find((step) => getStatus(step.id) !== "done");
  const firstUnfinished = steps.find((step) => getStatus(step.id) !== "done");
  selectStep(afterCurrent ?? firstUnfinished ?? stepAtOffset(steps, selectedStep.value.id, 1));
}

function inspectFile(file: string) {
  inspectedFile.value = file;
  activeLessonTab.value = "review";
  isLabOpen.value = true;
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

function runAndShowResult(command: string) {
  runCommand(command);
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
        :is-home-view="isHomeView"
        :is-light-mode="isLightMode"
        @finish-session="finishSession"
        @open-home="openHome"
        @open-search="isSearchOpen = true"
        @reset-progress="resetAllProgress"
        @toggle-light-mode="toggleLightMode"
      />

      <section v-if="isHomeView" class="home-dashboard">
        <article class="home-hero home-focus">
          <span>Next</span>
          <h2>次の1問だけ解く</h2>
          <p>一覧は気にしなくて大丈夫です。まず1問だけ開いて、テストが通ったら次へ進みます。</p>
          <div class="flow-steps" aria-label="学習の進め方">
            <div v-for="item in homeFlowItems" :key="item.title">
              <strong>{{ item.title }}</strong>
              <small>{{ item.detail }}</small>
            </div>
          </div>
          <div class="next-focus-card">
            <strong>順番に進む</strong>
            <span>{{ nextFocusStep.title }}</span>
            <small>未完了の先頭Step</small>
            <button type="button" @click="selectNextFocusStep">この問題を解く</button>
          </div>
          <div class="primer-card">
            <strong>{{ nextFocusPrimer.title }}</strong>
            <p>{{ nextFocusPrimer.lead }}</p>
            <ul>
              <li v-for="item in nextFocusPrimer.items" :key="item">{{ item }}</li>
            </ul>
          </div>
          <div class="home-actions">
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
            <p>説明、解く、直す、次へ。詰まったら解答例と差分を見る。</p>
          </article>
        </aside>

        <LearningLogPanel :events="learningEvents" :get-status="getStatus" :steps="steps" />
      </section>

      <LessonHeader v-if="!isHomeView" :current-phase="currentPhase" :step="selectedStep" @move="move" />

      <section v-if="!isHomeView" class="lesson-next-action" :class="`state-${lessonAction.state}`">
        <div>
          <span>今やること</span>
          <strong>{{ lessonAction.title }}</strong>
          <p>{{ lessonAction.detail }}</p>
        </div>
        <button
          v-if="!currentRunPassed"
          type="button"
          :disabled="!isRunnable(primaryCommand) || Boolean(runningCommand)"
          @click="runAndShowResult(primaryCommand)"
        >
          <Play :size="17" />
          テスト実行
        </button>
        <button v-else type="button" @click="selectNextUnfinishedStep">
          <ArrowRight :size="17" />
          次の問題へ
        </button>
      </section>

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
          <strong>1 file</strong>
        </div>
        <div class="lesson-chip">
          <span>実行</span>
          <strong>{{ runnableCommands.length > 0 ? "1 test" : "なし" }}</strong>
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

      <article v-if="!isHomeView" class="lesson-map-card">
        <div>
          <BookOpenCheck :size="20" />
          <strong>迷ったらこの順番</strong>
        </div>
        <ol>
          <li>説明タブで目的と開くファイルを見る</li>
          <li>テスト実行を押して失敗内容を見る</li>
          <li>表示された1ファイルだけ直す</li>
          <li>成功したら次の問題へ進む</li>
        </ol>
      </article>

      <MissionBoard
        v-if="!isHomeView && activeLessonTab === 'read'"
        :primary-command="primaryCommand"
        :running-command="runningCommand"
        :step="selectedStep"
        @run="runAndShowResult"
      />

      <RunResultCard
        v-if="!isHomeView && activeLessonTab === 'read' && (runResult || runError || runningCommand)"
        :run-error="runError"
        :run-result="runResult"
        :running-command="runningCommand"
        @inspect-file="inspectFile"
      />

      <article v-if="!isHomeView && activeLessonTab === 'read' && currentRunPassed" class="work-card next-step-card">
        <strong>このStepは完了です</strong>
        <p>止まらず次へ進めます。必要ならあとでメモに戻ればOKです。</p>
        <button type="button" @click="selectNextUnfinishedStep">次の問題へ</button>
      </article>

      <article v-if="!isHomeView && activeLessonTab === 'read'" class="work-card primer-card">
        <div class="work-title">
          <PencilLine :size="20" />
          <h3>{{ selectedPrimer.title }}</h3>
        </div>
        <p>{{ selectedPrimer.lead }}</p>
        <ul>
          <li v-for="item in selectedPrimer.items" :key="item">{{ item }}</li>
        </ul>
      </article>

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
              <h3>解く順番</h3>
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

        </div>

        <section v-if="activeLessonTab === 'review' && !isLightMode" class="collapse-stack">
          <article class="collapsible-panel">
            <button type="button" class="collapse-toggle" @click="isReferenceOpen = !isReferenceOpen">
              参考リンク / 開くファイル
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

    <CommandCenter :open="isSearchOpen" :steps="steps" @close="isSearchOpen = false" @select-step="selectStep" />
    <SessionSummaryModal :open="isSessionSummaryOpen" :summary="latestSession" @close="isSessionSummaryOpen = false" />
  </div>
</template>
