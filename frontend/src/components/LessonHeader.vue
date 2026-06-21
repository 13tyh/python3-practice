<script setup lang="ts">
import { ChevronLeft, ChevronRight } from "lucide-vue-next";
import type { Step } from "../data/stepTypes";

defineProps<{
  currentPhase: string;
  step: Step;
}>();

defineEmits<{
  move: [offset: number];
}>();
</script>

<template>
  <header class="mentor-header">
    <div>
      <div class="mentor-kicker">{{ currentPhase }} / {{ step.id }}</div>
      <h2>{{ step.title }}</h2>
      <p>{{ step.goals[0] ?? step.summary }}</p>
      <small>説明はこの画面内にまとめています</small>
    </div>
    <div class="mentor-arrows">
      <button type="button" title="前のstep" @click="$emit('move', -1)">
        <ChevronLeft :size="20" />
      </button>
      <button type="button" title="次のstep" @click="$emit('move', 1)">
        <ChevronRight :size="20" />
      </button>
    </div>
  </header>
</template>
