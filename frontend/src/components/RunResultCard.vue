<script setup lang="ts">
import { Terminal } from "lucide-vue-next";
import { computed, ref } from "vue";
import type { RunResult } from "../api/learningApi";
import { extractFileCandidates, extractRunHighlights, runFailureHint, runResultGuide } from "../data/learningUi";

const props = defineProps<{
  runError: string;
  runningCommand: string;
  runResult: RunResult | null;
}>();

defineEmits<{
  inspectFile: [file: string];
}>();

const showFileCandidates = ref(false);
const fileCandidates = computed(() => extractFileCandidates(props.runResult));
const highlights = computed(() => extractRunHighlights(props.runResult));
const failureHint = computed(() => runFailureHint(props.runResult));
</script>

<template>
  <article class="result-card">
    <div class="work-title">
      <Terminal :size="20" />
      <h3>実行結果</h3>
    </div>
    <p v-if="!runError">{{ runResultGuide(runResult) }}</p>
    <p v-if="runningCommand">実行中: {{ runningCommand }}</p>
    <p v-if="runError" class="run-error">{{ runError }}</p>
    <div v-if="runResult" class="run-summary" :class="{ success: runResult?.exit_code === 0 }">
      <strong>{{ runResult?.exit_code === 0 ? "成功" : "失敗" }}</strong>
      <span>exit {{ runResult?.exit_code }}</span>
      <span>{{ runResult?.duration_ms }} ms</span>
      <code>{{ runResult?.command }}</code>
    </div>
    <p v-if="failureHint" class="run-hint">{{ failureHint }}</p>
    <div v-if="highlights.length > 0" class="run-highlights">
      <strong>重要ログ</strong>
      <code v-for="line in highlights" :key="line">{{ line }}</code>
    </div>
    <div v-if="fileCandidates.length > 0" class="file-candidates">
      <button class="file-candidates-toggle" type="button" @click="showFileCandidates = !showFileCandidates">
        {{ showFileCandidates ? "対象ファイル候補を隠す" : "対象ファイル候補を表示" }}
      </button>
      <div v-if="showFileCandidates">
        <button
          v-for="file in fileCandidates"
          :key="file"
          class="file-candidate-button"
          type="button"
          @click="$emit('inspectFile', file)"
        >
          {{ file }}
        </button>
      </div>
    </div>
    <pre v-if="runResult?.stdout"><code>{{ runResult?.stdout }}</code></pre>
    <pre v-if="runResult?.stderr" class="stderr"><code>{{ runResult?.stderr }}</code></pre>
  </article>
</template>
