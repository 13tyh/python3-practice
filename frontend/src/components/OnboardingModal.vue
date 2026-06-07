<script setup lang="ts">
import { X } from "lucide-vue-next";

defineProps<{
  open: boolean;
}>();

defineEmits<{
  close: [];
}>();
</script>

<template>
  <div v-if="open" class="modal-backdrop" role="dialog" aria-modal="true" aria-labelledby="onboarding-title">
    <section class="modal-panel">
      <button class="modal-close" type="button" aria-label="ガイドを閉じる" @click="$emit('close')">
        <X :size="18" />
      </button>
      <span>Start</span>
      <h2 id="onboarding-title">学習の流れ</h2>
      <ol>
        <li>左のStepを選び、対象ファイルとゴールを見る。</li>
        <li>コードを書き、画面の実行ボタンでテストする。</li>
        <li>失敗ログ、解答比較、レビュー採点で判断力を鍛える。</li>
        <li>進捗ツールからレポートやバックアップを出す。</li>
      </ol>
      <button type="button" @click="$emit('close')">始める</button>
    </section>
  </div>
</template>
