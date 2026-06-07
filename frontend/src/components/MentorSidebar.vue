<script setup lang="ts">
import { BookOpen, CheckCircle2, Circle, Home, PanelLeftClose, PanelLeftOpen, Search } from "lucide-vue-next";
import { computed, ref, watch } from "vue";
import { categoryLabel } from "../data/learningUi";
import type { Step, StepStatus } from "../data/steps";

type PhaseGroup = {
  id: string;
  title: string;
  steps: Step[];
};

const props = defineProps<{
  categories: string[];
  doneCount: number;
  doingCount: number;
  getStatus: (id: string) => StepStatus;
  isHomeView: boolean;
  isOpen: boolean;
  phaseGroups: PhaseGroup[];
  progressPercent: number;
  query: string;
  selectedCategory: string;
  selectedStep: Step;
  stepNumber: (id: string) => number;
  stepsLength: number;
}>();

const emit = defineEmits<{
  openHome: [];
  selectStep: [step: Step];
  "update:isOpen": [value: boolean];
  "update:query": [value: string];
  "update:selectedCategory": [value: string];
}>();

const localQuery = ref(props.query);
const collapsedPhases = ref<Set<string>>(new Set());
let queryTimer: ReturnType<typeof setTimeout> | undefined;

const visibleStepCount = computed(() =>
  props.phaseGroups.reduce((count, phase) => count + phase.steps.length, 0),
);

watch(
  () => props.query,
  (value) => {
    if (value !== localQuery.value) localQuery.value = value;
  },
);

watch(localQuery, (value) => {
  if (queryTimer) clearTimeout(queryTimer);
  queryTimer = setTimeout(() => emit("update:query", value), 180);
});
watch(
  () => [props.phaseGroups.map((phase) => phase.id).join(","), props.isHomeView],
  () => {
    collapsedPhases.value = new Set(props.phaseGroups.map((phase) => phase.id));
  },
  { immediate: true },
);

function togglePhase(id: string) {
  const next = new Set(collapsedPhases.value);
  if (next.has(id)) next.delete(id);
  else next.add(id);
  collapsedPhases.value = next;
}

function isPhaseCollapsed(id: string) {
  return collapsedPhases.value.has(id);
}

function updateCategory(event: Event) {
  emit("update:selectedCategory", (event.target as HTMLSelectElement).value);
}
</script>

<template>
  <aside class="mentor-nav">
    <div class="sidebar-head">
      <div class="mentor-brand">
        <div class="brand-mark">
          <BookOpen :size="21" />
        </div>
        <div>
          <h1>Python Master</h1>
          <p>{{ doneCount }}/{{ stepsLength }} 完了</p>
        </div>
      </div>
      <button
        class="sidebar-toggle"
        type="button"
        :title="isOpen ? 'サイドバーを閉じる' : 'サイドバーを開く'"
        :aria-expanded="isOpen"
        @click="emit('update:isOpen', !isOpen)"
      >
        <PanelLeftClose v-if="isOpen" :size="20" />
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

    <button class="sidebar-home-link" :class="{ active: isHomeView }" type="button" @click="emit('openHome')">
      <Home :size="17" />
      <span>
        <strong>Home</strong>
        <small>学習ダッシュボード</small>
      </span>
    </button>

    <label class="mentor-search">
      <Search :size="17" />
      <input v-model="localQuery" type="search" aria-label="Stepを検索" placeholder="Stepを検索" />
    </label>

    <div class="sidebar-filter">
      <select :value="selectedCategory" aria-label="category filter" @change="updateCategory">
        <option value="all">全部のカテゴリ</option>
        <option value="basic">基本</option>
        <option v-for="category in categories" :key="category" :value="category">
          {{ categoryLabel(category) }}
        </option>
      </select>
      <span>{{ visibleStepCount }} steps</span>
    </div>

    <nav class="mentor-step-list" aria-label="steps">
      <section v-for="phase in phaseGroups" :key="phase.id" class="phase-nav-group">
        <button
          class="phase-toggle"
          type="button"
          :aria-expanded="!isPhaseCollapsed(phase.id)"
          @click="togglePhase(phase.id)"
        >
          <span>{{ isPhaseCollapsed(phase.id) ? "+" : "-" }}</span>
          <strong>{{ phase.title }}</strong>
          <small>{{ phase.steps.length }}</small>
        </button>
        <div v-if="!isPhaseCollapsed(phase.id)" class="phase-step-list">
          <button
            v-for="step in phase.steps"
            :key="step.id"
            v-memo="[!isHomeView && step.id === selectedStep.id, getStatus(step.id)]"
            :class="{ active: !isHomeView && step.id === selectedStep.id }"
            type="button"
            @click="emit('selectStep', step)"
          >
            <span class="step-index">{{ stepNumber(step.id) }}</span>
            <span>
              <strong>{{ step.title }}</strong>
              <small>{{ categoryLabel(step.category) }} / {{ step.level }}</small>
            </span>
            <component :is="getStatus(step.id) === 'done' ? CheckCircle2 : Circle" :size="16" />
          </button>
        </div>
      </section>
    </nav>
  </aside>
</template>
