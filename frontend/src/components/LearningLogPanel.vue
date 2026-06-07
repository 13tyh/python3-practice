<script setup lang="ts">
import { AlertTriangle, BarChart3, History, Target } from "lucide-vue-next";
import { computed } from "vue";
import type { LearningEvent } from "../composables/useLearningLog";
import { analyzeLearningLog } from "../data/learningLogAnalysis";
import type { Step, StepStatus } from "../data/stepTypes";

const props = defineProps<{
  events: LearningEvent[];
  getStatus: (id: string) => StepStatus;
  steps: Step[];
}>();

const analysis = computed(() => analyzeLearningLog(props.steps, props.getStatus, props.events));

function formatDate(value: string) {
  if (!value) return "未実行";
  return new Intl.DateTimeFormat("ja-JP", { day: "2-digit", hour: "2-digit", minute: "2-digit", month: "2-digit" }).format(
    new Date(value),
  );
}
</script>

<template>
  <section class="learning-log-panel" aria-label="学習ログ分析">
    <div class="log-head">
      <div class="work-title">
        <BarChart3 :size="20" />
        <h3>効率ルート</h3>
      </div>
      <div class="log-metrics">
        <span>実行 {{ analysis.totalRuns }}</span>
        <span>成功率 {{ analysis.successRate }}%</span>
      </div>
    </div>

    <ol class="focus-list">
      <li v-for="item in analysis.focusQueue" :key="item.stepId">
        <a class="focus-link" :href="`#${item.stepId}`">
          <strong>{{ item.label }}</strong>
          <span>{{ item.title }}</span>
          <small>{{ item.reason }}</small>
        </a>
      </li>
    </ol>

    <div class="log-details-grid">
      <details class="log-details">
        <summary>
          <AlertTriangle :size="17" />
          苦手カテゴリ
        </summary>
        <code v-for="item in analysis.weakCategories" :key="item.label">
          {{ item.label }}: {{ item.done }}/{{ item.total }} 完了 / 失敗 {{ item.failures }}
        </code>
      </details>

      <details class="log-details">
        <summary>
          <History :size="17" />
          失敗Step
        </summary>
        <code v-if="analysis.failureHotspots.length === 0">まだ失敗ログはありません</code>
        <code v-for="item in analysis.failureHotspots" :key="item.stepId">
          {{ item.title }}: {{ item.failures }}回
        </code>
      </details>

      <details class="log-details">
        <summary>
          <History :size="17" />
          基礎復習
        </summary>
        <code v-for="item in analysis.staleBasics" :key="item.stepId">
          {{ item.title }} / {{ formatDate(item.lastAt) }}
        </code>
      </details>

      <details class="log-details">
        <summary>
          <Target :size="17" />
          ルール
        </summary>
        <code>1回15分で、読む→実行→直す→1行メモ</code>
        <code>10分詰まったら解答例を比較</code>
        <code>新規より、失敗と基礎復習を優先</code>
      </details>
    </div>
  </section>
</template>
