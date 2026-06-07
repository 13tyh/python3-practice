<script setup lang="ts">
import { Search, X } from "lucide-vue-next";
import { computed, ref, watch } from "vue";
import { categoryLabel } from "../data/learningUi";
import type { Step } from "../data/stepTypes";

const props = defineProps<{
  open: boolean;
  steps: Step[];
}>();

const emit = defineEmits<{
  close: [];
  selectStep: [step: Step];
}>();

const query = ref("");
const results = computed(() => {
  const text = query.value.trim().toLowerCase();
  if (!text) return props.steps.slice(0, 12);
  return props.steps
    .filter((step) =>
      [step.id, step.title, step.summary, step.category, step.level, ...step.goals, ...step.files].some((value) =>
        value.toLowerCase().includes(text),
      ),
    )
    .slice(0, 24);
});

watch(
  () => props.open,
  (open) => {
    if (open) query.value = "";
  },
);

function select(step: Step) {
  emit("selectStep", step);
  emit("close");
}
</script>

<template>
  <div v-if="open" class="modal-backdrop" role="dialog" aria-modal="true" aria-labelledby="command-title">
    <section class="modal-panel command-center">
      <button class="modal-close" type="button" aria-label="検索を閉じる" @click="$emit('close')">
        <X :size="18" />
      </button>
      <span>Search</span>
      <h2 id="command-title">Step検索</h2>
      <label class="command-search">
        <Search :size="17" />
        <input v-model="query" type="search" aria-label="Step検索キーワード" placeholder="N+1 / RAG / 型 / Mongo" autofocus />
      </label>
      <div class="command-results">
        <button v-for="step in results" :key="step.id" type="button" @click="select(step)">
          <strong>{{ step.title }}</strong>
          <small>{{ step.id }} / {{ categoryLabel(step.category) }} / {{ step.level }}</small>
        </button>
      </div>
    </section>
  </div>
</template>
