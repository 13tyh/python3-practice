<script setup lang="ts">
import CommandRunCard from "./CommandRunCard.vue";
import type { Step } from "../data/stepTypes";

defineProps<{
  primaryCommand: string;
  runningCommand: string;
  step: Step;
}>();

defineEmits<{
  run: [command: string];
}>();
</script>

<template>
  <section class="mission-board">
    <article class="mission-card">
      <span>今回のゴール</span>
      <h3>{{ step.goals[0] }}</h3>
      <p>{{ step.files[0] }} から読み、TODOを1つずつ動かして直す。</p>
      <div class="learner-focus">
        <div>
          <span>今やる1ファイル</span>
          <code>{{ step.files[0] }}</code>
        </div>
        <div>
          <span>詰まった時ヒント</span>
          <p>テスト名、失敗行、期待値の順に読む。解答例を見る前に1回だけ仮説を書く。</p>
        </div>
        <label>
          <input type="checkbox" />
          解答例を見る前に、自分の修正理由を1文で書いた
        </label>
      </div>
      <div class="learning-route">
        <div>
          <strong>1</strong>
          <span>読む</span>
        </div>
        <div>
          <strong>2</strong>
          <span>書く</span>
        </div>
        <div>
          <strong>3</strong>
          <span>動かす</span>
        </div>
        <div>
          <strong>4</strong>
          <span>判断</span>
        </div>
      </div>
    </article>
    <CommandRunCard :command="primaryCommand" :running-command="runningCommand" @run="$emit('run', $event)" />
  </section>
</template>
