<script setup lang="ts">
import { FileCheck2 } from "lucide-vue-next";
import type { FileTestCommand } from "../data/fileTestCommands";
import { isRunnable } from "../data/learningUi";

defineProps<{
  items: FileTestCommand[];
  runningCommand: string;
}>();

defineEmits<{
  run: [command: string];
}>();
</script>

<template>
  <article v-if="items.length > 0" class="work-card file-test-card">
    <div class="work-title">
      <FileCheck2 :size="20" />
      <h3>ファイル別テスト</h3>
    </div>
    <div v-for="item in items" :key="item.file" class="mini-runner file-test-runner">
      <div>
        <strong>{{ item.label }}</strong>
        <code>{{ item.file }}</code>
        <code>{{ item.command }}</code>
      </div>
      <button
        type="button"
        :disabled="!isRunnable(item.command) || Boolean(runningCommand)"
        @click="$emit('run', item.command)"
      >
        実行
      </button>
    </div>
  </article>
</template>
