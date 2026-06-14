<script setup lang="ts">
import {
  Bot,
  Bug,
  CheckSquare,
  ClipboardCheck,
  FileText,
  Database,
  FileSearch,
  GitCompareArrows,
  History,
  ListChecks,
  Search,
  ShieldCheck,
  Sparkles,
} from "lucide-vue-next";
import { computed, ref, watch } from "vue";
import { fetchSolutionCompare, type FileCompare, type RunResult } from "../api/learningApi";
import { categoryLabel } from "../data/learningUi";
import type { Step, StepStatus } from "../data/stepTypes";

type LabState = {
  answer: string;
  aiOutput: string;
  checked: Record<string, boolean>;
  ragDocs: string;
  ragQuestion: string;
  review: string;
};
type LabTab = "compare" | "memo" | "rag" | "mongo" | "review" | "ai";

const props = defineProps<{
  allSteps: Step[];
  doneCount: number;
  doingCount: number;
  getStatus: (id: string) => StepStatus;
  inspectedFile: string;
  runResult: RunResult | null;
  shouldShowMongo: boolean;
  step: Step;
  stepsLength: number;
}>();

defineEmits<{
  run: [command: string];
}>();

const defaultState = (): LabState => ({
  answer: "",
  aiOutput: "",
  checked: {},
  ragDocs: "",
  ragQuestion: "",
  review: "",
});

const labState = ref<LabState>(defaultState());
const memoRefresh = ref(0);
const activeLabTab = ref<LabTab>("compare");
const selectedFile = ref("");
const searchText = ref("");
const compare = ref<FileCompare | null>(null);
const compareError = ref("");
const isLoadingCompare = ref(false);
const labTabs: Array<{ key: LabTab; label: string }> = [
  { key: "compare", label: "比較" },
  { key: "memo", label: "メモ" },
  { key: "rag", label: "RAG" },
  { key: "ai", label: "AI実験" },
  { key: "mongo", label: "Mongo" },
  { key: "review", label: "レビュー" },
];

const stepFiles = computed(() => props.step.files.filter((file) => file.endsWith(".py")));
const selectedCompareFile = computed({
  get: () => selectedFile.value || props.inspectedFile || stepFiles.value[0] || props.step.files[0] || "",
  set: (value: string) => {
    selectedFile.value = value;
  },
});
const compareExerciseLines = computed(() => toNumberedLines(compare.value?.exercise ?? ""));
const compareSolutionLines = computed(() => toNumberedLines(compare.value?.solution ?? ""));
const solutionLineSet = computed(() => new Set(compareSolutionLines.value.map((line) => line.text.trim())));
const exerciseLineSet = computed(() => new Set(compareExerciseLines.value.map((line) => line.text.trim())));

const understandingChecks = computed(() => [
  { key: "read_test", label: "先にテスト名と期待値を読んだ" },
  { key: "explain_type", label: "入力、戻り値、例外を1文で説明できる" },
  { key: "ai_review", label: "AIの出力に型、例外、責務のズレがないか確認した" },
  { key: "edge_case", label: "空、None、0件、重複などの境界値を考えた" },
]);

const debugChecklist = computed(() => [
  "tracebackの一番下から対象行を読む",
  "FAILURESのexpectedとactualを比べる",
  "必要ならbreakpoint()を1箇所だけ置く",
  "ログで入力値、件数、処理時間を残す",
]);

const mongoQueries = [
  "db.users.find({}, { _id: 0, name: 1, group_id: 1 }).limit(5)",
  "db.groups.aggregate([{ $lookup: { from: 'users', localField: '_id', foreignField: 'group_id', as: 'users' } }])",
  "db.subscriptions.find({ status: 'active' }, { _id: 0 }).sort({ city: 1 })",
  "db.subscriptions.createIndex({ municipality_id: 1, status: 1 })",
  "mongoexport --db python_master --collection subscriptions --type=csv --fields municipality_id,city,status --out /tmp/subscriptions.csv",
];

const ragSeedText = computed(() => [
  props.step.summary,
  ...props.step.goals,
  ...props.step.files.map((file) => `対象ファイル: ${file}`),
].join("\n"));
const ragSource = computed(() => labState.value.ragDocs.trim() || ragSeedText.value);
const ragChunks = computed(() =>
  ragSource.value
    .split(/\n|。/)
    .map((line) => line.trim())
    .filter(Boolean)
    .slice(0, 6),
);
const ragMatches = computed(() => {
  const terms = labState.value.ragQuestion.toLowerCase().split(/\s+/).filter(Boolean);
  if (terms.length === 0) return ragChunks.value.slice(0, 2);
  return ragChunks.value.filter((chunk) => terms.some((term) => chunk.toLowerCase().includes(term))).slice(0, 3);
});
const pseudoEmbeddingTerms = computed(() =>
  [...new Set(ragSource.value.toLowerCase().match(/[a-z0-9_]{3,}|[ぁ-んァ-ン一-龥]{2,}/g) ?? [])].slice(0, 12),
);
const promptPreview = computed(
  () => `Context:\n${ragMatches.value.join("\n")}\n\nQuestion:\n${labState.value.ragQuestion || "このStepで重要な判断は？"}`,
);
const chunkSizeExperiments = computed(() =>
  [80, 140, 220].map((size) => ({
    chunks: chunkBySize(ragSource.value, size).slice(0, 4),
    label: `${size} chars`,
    size,
  })),
);
const layerComparison = [
  { layer: "router.py", ok: "HTTP入出力、Depends、status code", ng: "DB検索、prompt生成、重い業務判断" },
  { layer: "service.py", ok: "業務ルール、AI/RAGの組み立て、例外分類", ng: "Request/Response専用schemaへ依存" },
  { layer: "model.py", ok: "Pydantic/dataclass、値の制約", ng: "外部API呼び出し、ログ出力" },
  { layer: "repository.py", ok: "Mongo query、projection、index前提", ng: "HTTPException、画面都合の整形" },
];
const suspiciousAiOutput = computed(
  () =>
    labState.value.aiOutput.trim() ||
    "router.pyにMongo検索、prompt生成、例外握りつぶしを全部書けば早いです。型はdictで十分です。",
);
const aiOutputFindings = computed(() => [
  { label: "router肥大化", ok: /router.*(全部|Mongo|prompt|DB)|全部書/.test(suspiciousAiOutput.value) },
  { label: "型が弱い", ok: /dict|Any|型.*十分/.test(suspiciousAiOutput.value) },
  { label: "例外が危険", ok: /握りつぶ|except|例外/.test(suspiciousAiOutput.value) },
  { label: "テスト不足", ok: !/test|pytest|テスト/.test(suspiciousAiOutput.value) },
]);
const pseudoLlmAnswer = computed(() => {
  const citations = ragMatches.value.map((chunk, index) => `[${index + 1}] ${chunk}`).join(" ");
  return `${props.step.title}では、${props.step.goals[0] ?? "目的"}を先に満たす。根拠: ${citations || props.step.summary}`;
});
const reviewScore = computed(() => {
  const checkScore = Object.values(labState.value.checked).filter(Boolean).length;
  const textScore = labState.value.review.trim().length >= 40 ? 2 : labState.value.review.trim().length >= 10 ? 1 : 0;
  return Math.min(10, checkScore * 2 + textScore);
});
const localReviewFindings = computed(() => [
  { label: "責務分離", ok: /router|service|model|責務|分離/.test(labState.value.review) },
  { label: "型", ok: /型|type|None|Optional|Protocol/.test(labState.value.review) },
  { label: "例外", ok: /例外|error|Exception|HTTPException/.test(labState.value.review) },
  { label: "テスト", ok: /test|pytest|境界|異常系|正常系/.test(labState.value.review) },
  { label: "性能/安全", ok: /N\+1|性能|security|安全|secret|ログ/.test(labState.value.review) },
]);
const localReviewScore = computed(() => localReviewFindings.value.filter((item) => item.ok).length * 2);
const historyText = computed(
  () => `${props.doneCount}完了 / ${props.doingCount}学習中 / ${props.stepsLength} steps`,
);
const lastFailure = computed(() => {
  if (!props.runResult || props.runResult.exit_code === 0) return "まだ失敗ログはありません";
  return `${props.runResult.command} / exit ${props.runResult.exit_code}`;
});
const memoSummaries = computed(() => {
  memoRefresh.value;
  return props.allSteps
    .map((step) => ({ step, state: readLabState(step.id) }))
    .filter(({ state }) => stateHasMemo(state))
    .slice(0, 10);
});
const incompleteByCategory = computed(() => {
  const counts = new Map<string, number>();
  for (const step of props.allSteps) {
    if (props.getStatus(step.id) !== "done") counts.set(step.category, (counts.get(step.category) ?? 0) + 1);
  }
  return [...counts.entries()]
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5)
    .map(([category, count]) => `${categoryLabel(category)}: ${count}`);
});
const nextRecommendedSteps = computed(() =>
  props.allSteps
    .filter((step) => props.getStatus(step.id) !== "done")
    .slice(0, 4)
    .map((step) => `${step.title} (${categoryLabel(step.category)})`),
);
const searchedSteps = computed(() => {
  const text = searchText.value.trim().toLowerCase();
  if (!text) return props.allSteps.slice(0, 6);
  return props.allSteps
    .filter((step) =>
      [step.id, step.title, step.summary, step.category, step.level, ...step.goals, ...step.files].some((value) =>
        value.toLowerCase().includes(text),
      ),
    )
    .slice(0, 8);
});
const issueAcceptance = computed(() => [
  `${props.step.commands[0] ?? "pytest"} が成功する`,
  "router/service/modelの責務が混ざっていない",
  "異常系と境界値のテスト観点を説明できる",
]);
const prReviewChecklist = [
  "1コメント1論点で書く",
  "危険な理由と修正案をセットで書く",
  "好みではなく仕様、型、テスト、性能で判断する",
];
const bugFixMiniTasks = [
  "mutable default引数で前回の結果が混ざる",
  "router内でMongoとAI呼び出しを直書きしている",
  "for文の中で1件ずつDB/APIを呼ぶN+1",
  "AI JSON出力をschema検証せず信じている",
];
const opsChecklist = [
  "healthcheckがある",
  "envとsecretが分離されている",
  "構造化ログとrequest_idがある",
  "migration/rollback手順がある",
  "CIでuv run buildが通る",
];
const cheatSheets = [
  "Python: dict/list/set, 内包表記, 例外, dataclass, pathlib",
  "pytest: fixture, monkeypatch, parametrize, 境界値",
  "FastAPI: router, service, schema, dependency, exception handler",
  "Mongo: find, projection, index, aggregate, lookup, export",
  "Docker/CI: healthcheck, compose profile, env, logs, build",
];

watch(
  () => props.step.id,
  () => {
    labState.value = loadState();
    selectedFile.value = props.inspectedFile || stepFiles.value[0] || "";
    compare.value = null;
    compareError.value = "";
  },
  { immediate: true },
);

watch(
  () => props.inspectedFile,
  (file) => {
    if (file) {
      selectedFile.value = file;
      activeLabTab.value = "compare";
      void loadCompare();
    }
  },
);

watch(
  labState,
  () => {
    window.localStorage.setItem(storageKey(props.step.id), JSON.stringify(labState.value));
    memoRefresh.value += 1;
  },
  { deep: true },
);

async function loadCompare() {
  if (!selectedCompareFile.value) return;
  compareError.value = "";
  isLoadingCompare.value = true;
  try {
    compare.value = await fetchSolutionCompare(selectedCompareFile.value);
  } catch (error) {
    compare.value = null;
    compareError.value = error instanceof Error ? error.message : "解答比較を取得できませんでした";
  } finally {
    isLoadingCompare.value = false;
  }
}

function storageKey(stepId: string) {
  return `python-master-lab:${stepId}`;
}

function loadState() {
  return readLabState(props.step.id);
}

function readLabState(stepId: string) {
  const raw = window.localStorage.getItem(storageKey(stepId));
  if (!raw) return defaultState();
  try {
    return { ...defaultState(), ...JSON.parse(raw) } as LabState;
  } catch {
    return defaultState();
  }
}

function stateHasMemo(state: LabState) {
  return Boolean(state.answer.trim() || state.review.trim() || state.ragQuestion.trim());
}

function toNumberedLines(text: string) {
  return text.split(/\r?\n/).map((line, index) => ({ number: index + 1, text: line }));
}

function chunkBySize(text: string, size: number) {
  const normalized = text.replace(/\s+/g, " ").trim();
  if (!normalized) return [];
  const chunks: string[] = [];
  for (let index = 0; index < normalized.length; index += size) {
    chunks.push(normalized.slice(index, index + size));
  }
  return chunks;
}
</script>

<template>
  <section class="mastery-lab">
    <div class="lab-header">
      <span>実務ラボ</span>
      <h3>動かすだけで終わらせず、読む・判断する・提案するまで練習する</h3>
    </div>

    <nav class="lab-tabs" aria-label="実務ラボタブ">
      <button
        v-for="tab in labTabs"
        :key="tab.key"
        type="button"
        :class="{ active: activeLabTab === tab.key }"
        @click="activeLabTab = tab.key"
      >
        {{ tab.label }}
      </button>
    </nav>

    <article v-if="activeLabTab === 'compare'" class="lab-panel">
      <div class="work-title">
        <FileSearch :size="20" />
        <h3>失敗ログ導線</h3>
      </div>
      <p>{{ lastFailure }}</p>
      <p>実行結果の対象ファイル候補を押すと、このラボの比較対象に入ります。</p>
      <code>{{ selectedCompareFile || "まだ候補ファイルはありません" }}</code>
    </article>

    <article v-if="activeLabTab === 'memo'" class="lab-panel">
      <div class="work-title">
        <CheckSquare :size="20" />
        <h3>理解チェック</h3>
      </div>
      <label v-for="item in understandingChecks" :key="item.key">
        <input v-model="labState.checked[item.key]" type="checkbox" />
        {{ item.label }}
      </label>
      <textarea v-model="labState.answer" aria-label="理解メモ" placeholder="なぜこの実装にしたかを1文で書く"></textarea>
    </article>

    <article v-if="activeLabTab === 'compare'" class="lab-panel lab-wide">
      <div class="work-title">
        <GitCompareArrows :size="20" />
        <h3>解答比較</h3>
      </div>
      <select v-model="selectedCompareFile" aria-label="比較するファイル">
        <option v-for="file in stepFiles" :key="file" :value="file">{{ file }}</option>
      </select>
      <button type="button" @click="loadCompare">
        {{ isLoadingCompare ? "読込中" : "自分の答えとsolutionsを比較" }}
      </button>
      <p v-if="compareError" class="run-error">{{ compareError }}</p>
      <div v-if="compare" class="compare-grid">
        <div>
          <strong>{{ compare.exercise_path }}</strong>
          <pre class="code-preview"><code
            v-for="line in compareExerciseLines"
            :key="line.number"
            :class="{ changed: line.text.trim() && !solutionLineSet.has(line.text.trim()) }"
          ><span>{{ line.number }}</span>{{ line.text }}</code></pre>
        </div>
        <div>
          <strong>{{ compare.solution_path }}</strong>
          <pre v-if="compare.has_solution" class="code-preview"><code
            v-for="line in compareSolutionLines"
            :key="line.number"
            :class="{ changed: line.text.trim() && !exerciseLineSet.has(line.text.trim()) }"
          ><span>{{ line.number }}</span>{{ line.text }}</code></pre>
          <code v-else>解答例はまだありません</code>
        </div>
      </div>
    </article>

    <article v-if="activeLabTab === 'review'" class="lab-panel">
      <div class="work-title">
        <Search :size="20" />
        <h3>Step検索強化</h3>
      </div>
      <input v-model="searchText" aria-label="Step検索強化キーワード" placeholder="N+1 / RAG / 型 / Mongo など" />
      <a v-for="item in searchedSteps" :key="item.id" :href="`#${item.id}`">
        {{ item.title }} / {{ categoryLabel(item.category) }}
      </a>
    </article>

    <article v-if="activeLabTab === 'review'" class="lab-panel">
      <div class="work-title">
        <History :size="20" />
        <h3>弱点分析</h3>
      </div>
      <p>{{ historyText }}</p>
      <code v-for="item in incompleteByCategory" :key="item">{{ item }}</code>
      <strong>次の候補</strong>
      <code v-for="item in nextRecommendedSteps" :key="item">{{ item }}</code>
    </article>

    <article v-if="activeLabTab === 'review'" class="lab-panel lab-wide">
      <div class="work-title">
        <FileText :size="20" />
        <h3>実務Issue形式</h3>
      </div>
      <p>{{ step.summary }}</p>
      <strong>受け入れ条件</strong>
      <ul>
        <li v-for="item in issueAcceptance" :key="item">{{ item }}</li>
      </ul>
    </article>

    <article v-if="activeLabTab === 'review'" class="lab-panel">
      <div class="work-title">
        <Bug :size="20" />
        <h3>デバッグ練習</h3>
      </div>
      <ol>
        <li v-for="item in debugChecklist" :key="item">{{ item }}</li>
      </ol>
    </article>

    <article v-if="activeLabTab === 'review'" class="lab-panel">
      <div class="work-title">
        <Bug :size="20" />
        <h3>バグ修正ミニ課題</h3>
      </div>
      <p>原因、修正案、追加テストを1セットで書く。</p>
      <code v-for="item in bugFixMiniTasks" :key="item">{{ item }}</code>
    </article>

    <article v-if="activeLabTab === 'review'" class="lab-panel">
      <div class="work-title">
        <ClipboardCheck :size="20" />
        <h3>PRレビュー練習</h3>
      </div>
      <p>before/afterを見て、危険な変更・足りないテスト・責務のズレを書く。</p>
      <code v-for="item in prReviewChecklist" :key="item">{{ item }}</code>
    </article>

    <article v-if="activeLabTab === 'mongo'" class="lab-panel">
      <div class="work-title">
        <Database :size="20" />
        <h3>Mongo操作</h3>
      </div>
      <p>{{ shouldShowMongo ? "このStepで重点的に確認" : "DB Stepで使う予習" }}</p>
      <code v-for="query in mongoQueries" :key="query">{{ query }}</code>
    </article>

    <article v-if="activeLabTab === 'rag'" class="lab-panel lab-wide">
      <div class="work-title">
        <Bot :size="20" />
        <h3>RAG可視化</h3>
      </div>
      <p>APIキー不要。chunk、疑似embedding語、retrieval、promptだけを見る。</p>
      <textarea v-model="labState.ragDocs" aria-label="RAG検索対象docs" placeholder="検索対象docsを貼る。空ならこのStep情報を使う"></textarea>
      <input v-model="labState.ragQuestion" aria-label="RAG質問" placeholder="質問を書く" />
      <div class="compare-grid">
        <div>
          <strong>chunks</strong>
          <code v-for="chunk in ragChunks" :key="chunk">{{ chunk }}</code>
        </div>
        <div>
          <strong>pseudo embedding terms</strong>
          <code>{{ pseudoEmbeddingTerms.join(", ") }}</code>
        </div>
        <div>
          <strong>retrieved / citation</strong>
          <code v-for="chunk in ragMatches" :key="chunk">{{ chunk }}</code>
        </div>
        <div>
          <strong>prompt preview</strong>
          <code>{{ promptPreview }}</code>
        </div>
      </div>
    </article>

    <article v-if="activeLabTab === 'ai'" class="lab-panel lab-wide">
      <div class="work-title">
        <Bot :size="20" />
        <h3>APIキー不要AI実験</h3>
      </div>
      <p>外部AIなしで、特化型AIの設計、RAG、採点をローカルで練習します。</p>
      <textarea v-model="labState.aiOutput" aria-label="AI出力採点対象" placeholder="AIが出した回答を貼る"></textarea>
      <div class="compare-grid">
        <div>
          <strong>疑似LLM回答</strong>
          <code>{{ pseudoLlmAnswer }}</code>
        </div>
        <div>
          <strong>AI出力の危険判定</strong>
          <code v-for="item in aiOutputFindings" :key="item.label">{{ item.ok ? "注意" : "OK" }}: {{ item.label }}</code>
        </div>
      </div>
    </article>

    <article v-if="activeLabTab === 'ai'" class="lab-panel lab-wide">
      <div class="work-title">
        <GitCompareArrows :size="20" />
        <h3>FastAPI AI責務分割</h3>
      </div>
      <div class="layer-grid">
        <div v-for="item in layerComparison" :key="item.layer">
          <strong>{{ item.layer }}</strong>
          <code>OK: {{ item.ok }}</code>
          <code>NG: {{ item.ng }}</code>
        </div>
      </div>
    </article>

    <article v-if="activeLabTab === 'ai'" class="lab-panel lab-wide">
      <div class="work-title">
        <FileSearch :size="20" />
        <h3>RAG chunkサイズ比較</h3>
      </div>
      <div class="compare-grid">
        <div v-for="item in chunkSizeExperiments" :key="item.size">
          <strong>{{ item.label }}</strong>
          <code v-for="chunk in item.chunks" :key="chunk">{{ chunk }}</code>
        </div>
      </div>
    </article>

    <article v-if="activeLabTab === 'memo'" class="lab-panel">
      <div class="work-title">
        <History :size="20" />
        <h3>学習履歴</h3>
      </div>
      <p>{{ historyText }}</p>
      <p>このStepの理解メモとチェックはブラウザに保存されます。</p>
    </article>

    <article v-if="activeLabTab === 'memo'" class="lab-panel lab-wide">
      <div class="work-title">
        <FileText :size="20" />
        <h3>学習メモ一覧</h3>
      </div>
      <p v-if="memoSummaries.length === 0">まだメモはありません。</p>
      <div v-for="item in memoSummaries" :key="item.step.id" class="memo-summary">
        <strong>{{ item.step.title }}</strong>
        <p v-if="item.state.answer">{{ item.state.answer }}</p>
        <p v-if="item.state.review">{{ item.state.review }}</p>
        <code v-if="item.state.ragQuestion">Q: {{ item.state.ragQuestion }}</code>
      </div>
    </article>

    <article v-if="activeLabTab === 'review'" class="lab-panel">
      <div class="work-title">
        <Sparkles :size="20" />
        <h3>ルール採点</h3>
      </div>
      <textarea v-model="labState.review" aria-label="レビュー採点メモ" placeholder="問題点 / 修正案 / テスト観点を書く"></textarea>
      <strong>{{ Math.max(reviewScore, localReviewScore) }} / 10</strong>
      <code v-for="item in localReviewFindings" :key="item.label">{{ item.ok ? "OK" : "TODO" }}: {{ item.label }}</code>
      <p>外部AIなし。キーワードと観点でローカル採点します。</p>
    </article>

    <article v-if="activeLabTab === 'review'" class="lab-panel">
      <div class="work-title">
        <ShieldCheck :size="20" />
        <h3>本番運用チェック</h3>
      </div>
      <label v-for="item in opsChecklist" :key="item">
        <input v-model="labState.checked[`ops:${item}`]" type="checkbox" />
        {{ item }}
      </label>
    </article>

    <article v-if="activeLabTab === 'memo'" class="lab-panel lab-wide">
      <div class="work-title">
        <ListChecks :size="20" />
        <h3>チートシート</h3>
      </div>
      <code v-for="item in cheatSheets" :key="item">{{ item }}</code>
    </article>
  </section>
</template>
