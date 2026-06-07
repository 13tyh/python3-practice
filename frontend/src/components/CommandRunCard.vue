<script setup lang="ts">
import { LoaderCircle, Play } from "lucide-vue-next";
import { isRunnable } from "../data/learningUi";

defineProps<{
  command: string;
  runningCommand: string;
}>();

defineEmits<{
  run: [command: string];
}>();
</script>

<template>
  <article class="run-card">
    <span>確認コマンド</span>
    <code>{{ command }}</code>
    <button
      type="button"
      :aria-label="`${command} を実行`"
      :disabled="!isRunnable(command) || Boolean(runningCommand)"
      @click="$emit('run', command)"
    >
      <LoaderCircle v-if="runningCommand === command" :size="17" />
      <Play v-else :size="17" />
      テスト実行
    </button>
  </article>
</template>
