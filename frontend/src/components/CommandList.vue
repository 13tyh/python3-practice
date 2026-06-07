<script setup lang="ts">
import { Terminal } from "lucide-vue-next";
import { isRunnable } from "../data/learningUi";

defineProps<{
  commands: string[];
  runningCommand: string;
}>();

defineEmits<{
  run: [command: string];
}>();
</script>

<template>
  <article v-if="commands.length > 0" class="work-card">
    <div class="work-title">
      <Terminal :size="20" />
      <h3>追加コマンド</h3>
    </div>
    <div v-for="commandText in commands" :key="commandText" class="mini-runner">
      <code>{{ commandText }}</code>
      <button
        type="button"
        :disabled="!isRunnable(commandText) || Boolean(runningCommand)"
        @click="$emit('run', commandText)"
      >
        実行
      </button>
    </div>
  </article>
</template>
