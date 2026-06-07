<script setup lang="ts">
import {
  AlertTriangle,
  BookOpen,
  CheckCircle2,
  ChevronLeft,
  ChevronRight,
  Circle,
  ClipboardCheck,
  Database,
  ExternalLink,
  FileCode2,
  Lightbulb,
  LoaderCircle,
  ListChecks,
  PanelLeftClose,
  PanelLeftOpen,
  PencilLine,
  Play,
  Search,
  Terminal,
} from "lucide-vue-next";
import { computed, onMounted, ref, watch } from "vue";
import { categories, steps, type Step, type StepStatus } from "./data/steps";

const selectedId = ref(window.location.hash.replace("#", "") || steps[0].id);
const query = ref("");
const selectedCategory = ref("all");
const statuses = ref<Record<string, StepStatus>>({});
const passedTests = ref<Record<string, boolean>>({});
const isSidebarOpen = ref(true);
const runningCommand = ref("");
const runResult = ref<RunResult | null>(null);
const runError = ref("");
const stepReferences = ref<StepReference[]>([]);

const storageKey = "python-master-step-status";
const passedTestsStorageKey = "python-master-passed-tests";
const apiBase = import.meta.env.VITE_API_BASE ?? "http://localhost:8000";

type RunResult = {
  command: string;
  exit_code: number;
  duration_ms: number;
  stdout: string;
  stderr: string;
};

type StepReference = {
  step: string;
  comment: string;
  urls: string[];
};

onMounted(async () => {
  const saved = localStorage.getItem(storageKey);
  if (saved) statuses.value = JSON.parse(saved) as Record<string, StepStatus>;
  const savedPassedTests = localStorage.getItem(passedTestsStorageKey);
  if (savedPassedTests) passedTests.value = JSON.parse(savedPassedTests) as Record<string, boolean>;
  try {
    const response = await fetch(`${apiBase}/api/step-references`);
    if (response.ok) {
      stepReferences.value = (await response.json()) as StepReference[];
    }
  } catch {
    stepReferences.value = [];
  }
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

const selectedStep = computed(() => steps.find((step) => step.id === selectedId.value) ?? steps[0]);

const filteredSteps = computed(() => {
  const text = query.value.trim().toLowerCase();
  return steps.filter((step) => {
    const categoryOk =
      selectedCategory.value === "all" ||
      (selectedCategory.value === "basic" && step.level === "基礎") ||
      step.category === selectedCategory.value;
    const textOk =
      text.length === 0 ||
      [step.id, step.title, step.summary, step.category, step.level].some((value) =>
        value.toLowerCase().includes(text),
      );
    return categoryOk && textOk;
  });
});

const doneCount = computed(() => steps.filter((step) => getStatus(step.id) === "done").length);
const doingCount = computed(() => steps.filter((step) => getStatus(step.id) === "doing").length);
const progressPercent = computed(() => Math.round((doneCount.value / steps.length) * 100));
const selectedNumber = computed(() => stepNumber(selectedStep.value.id));
const currentPhase = computed(() => getPhase(selectedNumber.value));
const nextStep = computed(() => steps[selectedNumber.value] ?? null);
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
const resultGuide = computed(() => {
  if (!runResult.value) return "実行ボタンを押すと、ここに終了コード、標準出力、エラーが表示されます。";
  if (runResult.value.exit_code === 0) return "成功です。このStepは完了にして、次のStepへ進めます。";
  return "失敗ログの最初のFAILURESと行番号を読み、対象ファイルのTODOを直します。";
});

const categoryLabels: Record<string, string> = {
  setup: "環境",
  python: "Python",
  test: "テスト",
  design: "設計",
  ops: "運用",
  reading: "読解",
  api: "API",
  security: "認証/安全",
  performance: "性能",
  db: "DB",
  data: "分析/出力",
  ai: "AI",
  review: "レビュー",
  project: "総仕上げ",
};

const writingTipsByCategory: Record<string, string[]> = {
  setup: ["まずREADMEの手順を1つずつ実行する", "失敗したコマンドとエラー行をメモする"],
  python: ["小さい関数に分けて、入力と戻り値を先に決める", "リスト内包表記は1行で読める時だけ使う"],
  test: ["正常系、異常系、境界値を分けて書く", "外部APIやDBはfakeやfixtureに置き換える"],
  design: ["router、service、modelの責務を分ける", "副作用のある処理と純粋な計算を分ける"],
  ops: ["loggerを使い、request_idや処理時間を残す", "secretや個人情報はログに出さない"],
  reading: ["入口、呼び出し先、テストの順に読む", "変更前に影響範囲をメモする"],
  api: ["リクエスト/レスポンスの型を先に作る", "HTTP例外と業務例外を混ぜない"],
  security: ["認証、認可、入力検証を別々に考える", "危険な入力は境界で止める"],
  performance: ["N+1、全件読み込み、重いループを先に疑う", "計測してから改善する"],
  db: ["検索条件、index、projectionを意識して書く", "mongoshで実データを確認してから実装する"],
  data: ["読み込み、変換、出力を段階に分ける", "CSV/PDF/JSONLは文字コードと欠損値を確認する"],
  ai: ["prompt、model、入力、出力をログで追える形にする", "AI出力はschemaとテストで検証する"],
  review: ["何が悪いか、なぜ危険か、どう直すかを書く", "AIの答えを鵜呑みにせず根拠を確認する"],
  project: ["settings、logger、router、service、modelを揃える", "小さく動かしてから結合する"],
};

const cautionTipsByCategory: Record<string, string[]> = {
  python: ["mutable default引数を使わない", "例外を bare except で握りつぶさない"],
  db: ["find()の結果を無制限に全件メモリへ載せない", "本番相当データではindexなし検索に注意する"],
  api: ["routerにDB操作やAI呼び出しを全部書かない", "型ヒントと実際の戻り値をズラさない"],
  ai: ["deployment_nameとmodel_nameを混同しない", "prompt injectionと空回答をテストする"],
  performance: ["推測で最適化しない", "N+1をループ内DB/API呼び出しとして探す"],
};

function getStatus(id: string): StepStatus {
  const status = statuses.value[id] ?? "todo";
  if (status === "done" && !passedTests.value[id]) return "doing";
  return status;
}

function setStatus(id: string, status: StepStatus) {
  statuses.value = { ...statuses.value, [id]: status };
}

function stepNumber(id: string) {
  return steps.findIndex((step) => step.id === id) + 1;
}

function getPhase(number: number) {
  if (number <= 5) return "Phase 1 / Python基礎";
  if (number <= 15) return "Phase 2 / テスト・設計";
  if (number <= 28) return "Phase 3 / FastAPI・外部API";
  if (number <= 43) return "Phase 4 / DB・性能・分析";
  if (number <= 56) return "Phase 5 / AI・RAG";
  return "Phase 6 / 統合・レビュー";
}

function categoryLabel(category: string) {
  return categoryLabels[category] ?? category;
}

function buildStepGuide(step: Step) {
  const categoryTips = writingTipsByCategory[step.category] ?? [
    "目的を1つ決めて、小さい単位で実装する",
    "動かした結果を見ながら修正する",
  ];
  const cautionTips = cautionTipsByCategory[step.category] ?? [];
  return {
    writing: [
      `まず ${step.files[0]} を開いて、TODOかREADMEの指示を読む`,
      ...categoryTips,
      `最後に ${step.commands[0] ?? "pytest"} で確認する`,
    ],
    cautions: [...step.reviewPoints, ...cautionTips].slice(0, 5),
  };
}

function statusLabel(status: StepStatus) {
  if (status === "done") return "完了";
  if (status === "doing") return "学習中";
  return "未着手";
}

function selectStep(step: Step) {
  selectedId.value = step.id;
  window.location.hash = step.id;
}

function move(offset: number) {
  const index = steps.findIndex((step) => step.id === selectedStep.value.id);
  const next = steps[Math.min(Math.max(index + offset, 0), steps.length - 1)];
  selectStep(next);
}

function isRunnable(command: string) {
  return (
    command === "python --version" ||
    command === "ruff check ." ||
    command === "black --check ." ||
    command === "mypy src" ||
    command === "poetry run lint" ||
    command === "poetry run fmt" ||
    command === "poetry run fmt --fix" ||
    command === "poetry run build" ||
    command.startsWith("pytest ") ||
    command.startsWith("poetry run pytest ")
  );
}

function isTestCommand(command: string) {
  return command.startsWith("pytest ") || command.startsWith("poetry run pytest ");
}

async function runCommand(command: string) {
  if (!isRunnable(command) || runningCommand.value) return;
  runningCommand.value = command;
  runError.value = "";
  runResult.value = null;
  setStatus(selectedStep.value.id, "doing");
  if (isTestCommand(command)) {
    passedTests.value = { ...passedTests.value, [selectedStep.value.id]: false };
  }
  try {
    const response = await fetch(`${apiBase}/api/run`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ command }),
    });
    if (!response.ok) {
      const body = (await response.json()) as { detail?: string };
      throw new Error(body.detail ?? "コマンド実行に失敗しました");
    }
    runResult.value = (await response.json()) as RunResult;
    if (isTestCommand(command) && runResult.value.exit_code === 0) {
      passedTests.value = { ...passedTests.value, [selectedStep.value.id]: true };
      setStatus(selectedStep.value.id, "done");
    } else {
      if (isTestCommand(command)) {
        passedTests.value = { ...passedTests.value, [selectedStep.value.id]: false };
      }
      setStatus(selectedStep.value.id, "doing");
    }
  } catch (error) {
    runError.value = error instanceof Error ? error.message : "コマンド実行に失敗しました";
  } finally {
    runningCommand.value = "";
  }
}
</script>

<template>
  <div class="mentor-shell" :class="{ 'sidebar-collapsed': !isSidebarOpen }">
    <aside class="mentor-nav">
      <div class="sidebar-head">
        <div class="mentor-brand">
          <div class="brand-mark">
            <BookOpen :size="21" />
          </div>
          <div>
            <h1>Python Master</h1>
            <p>{{ doneCount }}/{{ steps.length }} 完了</p>
          </div>
        </div>
        <button
          class="sidebar-toggle"
          type="button"
          :title="isSidebarOpen ? 'サイドバーを閉じる' : 'サイドバーを開く'"
          :aria-expanded="isSidebarOpen"
          @click="isSidebarOpen = !isSidebarOpen"
        >
          <PanelLeftClose v-if="isSidebarOpen" :size="20" />
          <PanelLeftOpen v-else :size="20" />
        </button>
      </div>

      <div class="sidebar-metrics">
        <div>
          <span>Progress</span>
          <strong>{{ progressPercent }}%</strong>
        </div>
        <div>
          <span>Active</span>
          <strong>{{ doingCount }}</strong>
        </div>
      </div>

      <div class="progress-track">
        <div class="progress-bar" :style="{ width: `${progressPercent}%` }" />
      </div>

      <div class="current-step-card">
        <span>Current</span>
        <strong>{{ selectedNumber }}. {{ selectedStep.title }}</strong>
        <small>{{ currentPhase }}</small>
      </div>

      <label class="mentor-search">
        <Search :size="17" />
        <input v-model="query" type="search" placeholder="Stepを検索" />
      </label>

      <div class="sidebar-filter">
        <select v-model="selectedCategory" aria-label="category filter">
          <option value="all">全部のカテゴリ</option>
          <option value="basic">基本</option>
          <option v-for="category in categories" :key="category" :value="category">
            {{ categoryLabel(category) }}
          </option>
        </select>
        <span>{{ filteredSteps.length }} steps</span>
      </div>

      <nav class="mentor-step-list" aria-label="steps">
        <button
          v-for="step in filteredSteps"
          :key="step.id"
          :class="{ active: step.id === selectedStep.id }"
          type="button"
          @click="selectStep(step)"
        >
          <span class="step-index">{{ stepNumber(step.id) }}</span>
          <span>
            <strong>{{ step.title }}</strong>
            <small>{{ categoryLabel(step.category) }} / {{ step.level }}</small>
          </span>
          <component :is="getStatus(step.id) === 'done' ? CheckCircle2 : Circle" :size="16" />
        </button>
      </nav>
    </aside>

    <main class="mentor-main">
      <header class="mentor-header">
        <div>
          <div class="mentor-kicker">{{ currentPhase }} / {{ selectedStep.id }}</div>
          <h2>{{ selectedStep.title }}</h2>
          <p>{{ selectedStep.summary }}</p>
        </div>
        <div class="mentor-arrows">
          <button type="button" title="前のstep" @click="move(-1)">
            <ChevronLeft :size="20" />
          </button>
          <button type="button" title="次のstep" @click="move(1)">
            <ChevronRight :size="20" />
          </button>
        </div>
      </header>

      <section class="lesson-strip" aria-label="lesson overview">
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

      <section class="mission-board">
        <article class="mission-card">
          <span>今回のゴール</span>
          <h3>{{ selectedStep.goals[0] }}</h3>
          <p>{{ selectedStep.files[0] }} から読み、TODOを1つずつ動かして直す。</p>
          <div class="learning-route">
            <div>
              <strong>1</strong>
              <span>読む</span>
            </div>
            <div>
              <strong>2</strong>
              <span>書く</span>
            </div>
            <div>
              <strong>3</strong>
              <span>動かす</span>
            </div>
            <div>
              <strong>4</strong>
              <span>判断</span>
            </div>
          </div>
        </article>
        <article class="run-card">
          <span>確認コマンド</span>
          <code>{{ primaryCommand }}</code>
          <button
            type="button"
            :disabled="!isRunnable(primaryCommand) || Boolean(runningCommand)"
            @click="runCommand(primaryCommand)"
          >
            <LoaderCircle v-if="runningCommand === primaryCommand" :size="17" />
            <Play v-else :size="17" />
            テスト実行
          </button>
        </article>
      </section>

      <section class="mentor-workspace">
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

          <article class="result-card">
            <div class="work-title">
              <Terminal :size="20" />
              <h3>実行結果</h3>
            </div>
            <p v-if="!runError">{{ resultGuide }}</p>
            <p v-if="runningCommand">実行中: {{ runningCommand }}</p>
            <p v-if="runError" class="run-error">{{ runError }}</p>
            <div v-if="runResult" class="run-summary" :class="{ success: runResult?.exit_code === 0 }">
              <strong>{{ runResult?.exit_code === 0 ? "成功" : "失敗" }}</strong>
              <span>exit {{ runResult?.exit_code }}</span>
              <span>{{ runResult?.duration_ms }} ms</span>
              <code>{{ runResult?.command }}</code>
            </div>
            <pre v-if="runResult?.stdout"><code>{{ runResult?.stdout }}</code></pre>
            <pre v-if="runResult?.stderr" class="stderr"><code>{{ runResult?.stderr }}</code></pre>
          </article>

          <article v-if="additionalCommands.length > 0" class="work-card">
            <div class="work-title">
              <Terminal :size="20" />
              <h3>追加コマンド</h3>
            </div>
            <div v-for="commandText in additionalCommands" :key="commandText" class="mini-runner">
              <code>{{ commandText }}</code>
              <button
                type="button"
                :disabled="!isRunnable(commandText) || Boolean(runningCommand)"
                @click="runCommand(commandText)"
              >
                実行
              </button>
            </div>
          </article>
        </div>

        <aside class="study-rail">
          <article class="rail-card">
            <div class="work-title">
              <Lightbulb :size="20" />
              <h3>学ぶこと</h3>
            </div>
            <ul>
              <li v-for="goal in selectedStep.goals" :key="goal">{{ goal }}</li>
            </ul>
          </article>

          <article class="rail-card">
            <div class="work-title">
              <FileCode2 :size="20" />
              <h3>対象ファイル</h3>
            </div>
            <code v-for="file in selectedStep.files" :key="file">{{ file }}</code>
          </article>

          <article v-if="selectedReference" class="rail-card">
            <h3>参照リソース</h3>
            <p>{{ selectedReference.comment }}</p>
            <div class="reference-links">
              <a
                v-for="url in selectedReference.urls"
                :key="url"
                :href="url"
                target="_blank"
                rel="noreferrer"
              >
                <ExternalLink :size="15" />
                {{ url }}
              </a>
            </div>
          </article>

          <article v-if="shouldShowMongo" class="rail-card">
            <div class="work-title">
              <Database :size="20" />
              <h3>Mongo確認</h3>
            </div>
            <code>docker compose exec mongo mongosh</code>
            <code>use python_master</code>
            <code>show collections</code>
            <code>db.subscriptions.find({}, { "_id": 0 })</code>
          </article>
        </aside>
      </section>
    </main>
  </div>

  <div v-if="false" class="app-shell">
    <aside class="sidebar">
      <div class="brand-row">
        <div class="brand-mark">
          <BookOpen :size="22" />
        </div>
        <div>
          <h1>Python Master</h1>
          <p>{{ doneCount }}/{{ steps.length }} 完了</p>
        </div>
      </div>

      <div class="progress">
        <div class="progress-meta">
          <span>{{ progressPercent }}%</span>
          <span>学習中 {{ doingCount }}</span>
        </div>
        <div class="progress-track">
          <div class="progress-bar" :style="{ width: `${progressPercent}%` }" />
        </div>
      </div>

      <div class="current-mini">
        <span>現在</span>
        <strong>{{ selectedNumber }}. {{ selectedStep.title }}</strong>
        <small>{{ currentPhase }}</small>
      </div>

      <label class="search-box">
        <Search :size="17" />
        <input v-model="query" type="search" placeholder="RAG、Mongo、FastAPI..." />
      </label>

      <div class="tabs" aria-label="category filter">
        <button
          class="tab"
          :class="{ active: selectedCategory === 'all' }"
          type="button"
          @click="selectedCategory = 'all'"
        >
          全部
        </button>
        <button
          v-for="category in categories"
          :key="category"
          class="tab"
          :class="{ active: selectedCategory === category }"
          type="button"
          @click="selectedCategory = category"
        >
          {{ categoryLabel(category) }}
        </button>
      </div>

      <nav class="step-list" aria-label="steps">
        <button
          v-for="step in filteredSteps"
          :key="step.id"
          class="step-button"
          :class="{ active: step.id === selectedStep.id }"
          type="button"
          @click="selectStep(step)"
        >
          <component :is="getStatus(step.id) === 'done' ? CheckCircle2 : Circle" :size="17" />
          <span>
            <strong>{{ step.id }} {{ step.title }}</strong>
            <small>{{ step.level }} / {{ categoryLabel(step.category) }}</small>
          </span>
        </button>
      </nav>
    </aside>

    <main class="content">
      <section class="step-header">
        <div>
          <div class="step-kicker">
            {{ currentPhase }} / {{ selectedStep.id }} / {{ selectedStep.level }}
          </div>
          <h2>{{ selectedStep.title }}</h2>
          <p>{{ selectedStep.summary }}</p>
        </div>
        <div class="header-actions">
          <button class="icon-button" type="button" title="前のstep" @click="move(-1)">
            <ChevronLeft :size="20" />
          </button>
          <button class="icon-button" type="button" title="次のstep" @click="move(1)">
            <ChevronRight :size="20" />
          </button>
        </div>
      </section>

      <section class="quick-run">
        <div>
          <span>このStepの確認</span>
          <code>{{ primaryCommand }}</code>
        </div>
        <button
          type="button"
          :disabled="!isRunnable(primaryCommand) || Boolean(runningCommand)"
          @click="runCommand(primaryCommand)"
        >
          <LoaderCircle v-if="runningCommand === primaryCommand" :size="17" />
          <Play v-else :size="17" />
          テスト実行
        </button>
      </section>

      <section class="flow-strip" aria-label="learning flow">
        <div class="flow-step active">
          <span>1</span>
          <strong>読む</strong>
          <small>問題と書き方</small>
        </div>
        <div class="flow-step">
          <span>2</span>
          <strong>書く</strong>
          <small>対象ファイル</small>
        </div>
        <div class="flow-step">
          <span>3</span>
          <strong>動かす</strong>
          <small>テスト実行</small>
        </div>
        <div class="flow-step">
          <span>4</span>
          <strong>直す</strong>
          <small>ログ確認</small>
        </div>
      </section>

      <section class="workspace-grid">
        <div class="practice-column">
          <article class="focus-card problem-card">
            <div class="panel-title">
              <ClipboardCheck :size="20" />
              <h3>問題</h3>
            </div>
            <h4>{{ selectedStep.goals[0] }}</h4>
            <p>{{ selectedStep.files[0] }} を開いて、READMEか最初のTODOから進める。</p>
          </article>

          <section class="guide-grid">
            <article class="guide-card">
              <div class="panel-title">
                <PencilLine :size="20" />
                <h3>書き方</h3>
              </div>
              <ol>
                <li v-for="tip in selectedGuide.writing" :key="tip">{{ tip }}</li>
              </ol>
            </article>

            <article class="guide-card caution-card">
              <div class="panel-title">
                <AlertTriangle :size="20" />
                <h3>注意点</h3>
              </div>
              <ul>
                <li v-for="tip in selectedGuide.cautions" :key="tip">{{ tip }}</li>
              </ul>
            </article>
          </section>

          <section class="runner-panel">
            <div class="panel-title">
              <Terminal :size="19" />
              <h3>テスト実行結果</h3>
            </div>
            <p v-if="!runError">{{ resultGuide }}</p>
            <p v-if="runningCommand">実行中: {{ runningCommand }}</p>
            <p v-if="runError" class="run-error">{{ runError }}</p>
            <div v-if="runResult" class="run-summary" :class="{ success: runResult?.exit_code === 0 }">
              <strong>{{ runResult?.exit_code === 0 ? "成功" : "失敗" }}</strong>
              <span>exit {{ runResult?.exit_code }}</span>
              <span>{{ runResult?.duration_ms }} ms</span>
              <code>{{ runResult?.command }}</code>
            </div>
            <pre v-if="runResult?.stdout"><code>{{ runResult?.stdout }}</code></pre>
            <pre v-if="runResult?.stderr" class="stderr"><code>{{ runResult?.stderr }}</code></pre>
          </section>

          <section class="detail-grid compact-details">
            <article class="panel">
              <div class="panel-title">
                <Terminal :size="19" />
                <h3>その他の実行コマンド</h3>
              </div>
              <div v-for="commandText in additionalCommands" :key="commandText" class="command-runner">
                <code>{{ commandText }}</code>
                <button
                  type="button"
                  :disabled="!isRunnable(commandText) || Boolean(runningCommand)"
                  @click="runCommand(commandText)"
                >
                  <LoaderCircle v-if="runningCommand === commandText" :size="17" />
                  <Play v-else :size="17" />
                  実行
                </button>
              </div>
              <p v-if="additionalCommands.length === 0" class="manual-note">
                追加コマンドはありません。まず上の確認コマンドを実行します。
              </p>
            </article>
          </section>

          <section v-if="shouldShowMongo" class="mongo-band">
            <div class="panel-title">
              <Database :size="20" />
              <h3>Mongo seed 確認</h3>
            </div>
            <div class="mongo-grid">
              <code>docker compose exec mongo mongosh</code>
              <code>use python_master</code>
              <code>show collections</code>
              <code>db.subscriptions.find({}, { "_id": 0 })</code>
              <code>db.users.find({ group_ids: "g-reviewer" })</code>
            </div>
          </section>
        </div>

        <aside class="context-rail">
          <article class="side-panel">
            <div class="panel-title">
              <Lightbulb :size="20" />
              <h3>学ぶこと</h3>
            </div>
            <ul>
              <li v-for="goal in selectedStep.goals" :key="goal">{{ goal }}</li>
            </ul>
          </article>

          <article class="side-panel">
            <div class="panel-title">
              <FileCode2 :size="20" />
              <h3>参照</h3>
            </div>
            <p v-if="selectedReference" class="reference-note">{{ selectedReference?.comment }}</p>
            <div v-if="selectedReference" class="reference-links">
              <a
                v-for="url in selectedReference?.urls ?? []"
                :key="url"
                :href="url"
                target="_blank"
                rel="noreferrer"
              >
                <ExternalLink :size="15" />
                {{ url }}
              </a>
            </div>
            <code v-for="file in selectedStep.files" :key="file">{{ file }}</code>
          </article>

          <section class="status-panel">
            <span>進捗</span>
            <div class="status-actions">
              <button
                class="status-button"
                :class="{ active: getStatus(selectedStep.id) === 'todo' }"
                type="button"
                @click="setStatus(selectedStep.id, 'todo')"
              >
                <Circle :size="17" />
                未着手
              </button>
              <button
                class="status-button"
                :class="{ active: getStatus(selectedStep.id) === 'doing' }"
                type="button"
                @click="setStatus(selectedStep.id, 'doing')"
              >
                <ListChecks :size="17" />
                学習中
              </button>
              <button
                class="status-button"
                :class="{ active: getStatus(selectedStep.id) === 'done' }"
                type="button"
                @click="setStatus(selectedStep.id, 'done')"
              >
                <CheckCircle2 :size="17" />
                完了
              </button>
            </div>
            <small>現在: {{ statusLabel(getStatus(selectedStep.id)) }}</small>
          </section>

          <section v-if="nextStep" class="next-step">
            <span>次のStep</span>
            <button type="button" @click="selectStep(nextStep)">
              {{ stepNumber(nextStep.id) }}. {{ nextStep.title }}
            </button>
          </section>
        </aside>
      </section>
    </main>
  </div>
</template>
