<script setup lang="ts">
defineProps<{
  open: boolean;
  summary: {
    at: string;
    failedRuns: number;
    nextItems: string[];
    totalRuns: number;
  } | null;
}>();

defineEmits<{
  close: [];
}>();

function formatDate(value: string) {
  return new Intl.DateTimeFormat("ja-JP", {
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    month: "2-digit",
  }).format(new Date(value));
}
</script>

<template>
  <div v-if="open && summary" class="modal-backdrop">
    <section class="modal-panel session-summary" aria-label="学習終了サマリー">
      <button type="button" class="modal-close" title="閉じる" @click="$emit('close')">x</button>
      <span>session saved</span>
      <h2>学習を保存しました</h2>
      <code>{{ formatDate(summary.at) }}</code>
      <code>実行 {{ summary.totalRuns }} / 失敗 {{ summary.failedRuns }}</code>
      <strong>次回はここから</strong>
      <code v-for="item in summary.nextItems" :key="item">{{ item }}</code>
    </section>
  </div>
</template>
