<script setup lang="ts">
import { computed } from "vue";
import CommandRunCard from "./CommandRunCard.vue";
import { primaryWorkFile } from "../data/learningUi";
import type { Step } from "../data/stepTypes";

const props = defineProps<{
  primaryCommand: string;
  runningCommand: string;
  step: Step;
}>();

defineEmits<{
  run: [command: string];
}>();

function fileName(path: string) {
  return path.split("/").pop() ?? path;
}

const workFile = computed(() => primaryWorkFile(props.step));
</script>

<template>
  <section class="mission-board">
    <article class="mission-card">
      <span>この1問</span>
      <h3>{{ step.goals[0] }}</h3>
      <p>まず下の確認コマンドを押します。失敗したら、この1ファイルのTODOだけ直します。</p>
      <div class="learner-focus">
        <div>
          <span>開くファイル</span>
          <strong>{{ fileName(workFile) }}</strong>
          <code>{{ workFile }}</code>
        </div>
        <div>
          <span>やること</span>
          <p>TODOを1つ直して、もう一度テスト実行。</p>
        </div>
        <div>
          <span>詰まった時</span>
          <p>最初の失敗ログだけ読む。10分止まったら解答例との差分を見て次へ進む。</p>
        </div>
        <label>
          <input type="checkbox" />
          直した理由を1文で言える
        </label>
      </div>
      <div class="learning-route">
        <div>
          <strong>1</strong>
          <span>説明</span>
        </div>
        <div>
          <strong>2</strong>
          <span>実行</span>
        </div>
        <div>
          <strong>3</strong>
          <span>修正</span>
        </div>
        <div>
          <strong>4</strong>
          <span>次へ</span>
        </div>
      </div>
    </article>
    <CommandRunCard :command="primaryCommand" :running-command="runningCommand" @run="$emit('run', $event)" />
  </section>
</template>
