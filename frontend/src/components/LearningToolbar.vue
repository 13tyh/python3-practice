<script setup lang="ts">
import { BookOpenCheck, Download, FileDown, Flag, Gauge, HelpCircle, Home, ListFilter, RotateCcw, Search, Upload } from "lucide-vue-next";
import { ref } from "vue";

defineProps<{
  hideDone: boolean;
  isHomeView: boolean;
  isTodayOnly: boolean;
  isLightMode: boolean;
}>();

const emit = defineEmits<{
  downloadBackup: [];
  downloadReport: [];
  importBackup: [text: string];
  finishSession: [];
  startBasicReview: [];
  openHome: [];
  openGuide: [];
  openSearch: [];
  resetProgress: [];
  toggleHideDone: [];
  toggleLightMode: [];
  toggleTodayOnly: [];
}>();

const fileInput = ref<HTMLInputElement | null>(null);

function pickBackup() {
  fileInput.value?.click();
}

function importBackup(event: Event) {
  const file = (event.target as HTMLInputElement).files?.[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = () => emit("importBackup", String(reader.result ?? ""));
  reader.readAsText(file);
  (event.target as HTMLInputElement).value = "";
}
</script>

<template>
  <section class="learning-toolbar" aria-label="学習ツール">
    <button type="button" :class="{ active: isHomeView }" title="ホーム" @click="$emit('openHome')">
      <Home :size="17" />
      ホーム
    </button>
    <button type="button" title="初回ガイド" @click="$emit('openGuide')">
      <HelpCircle :size="17" />
      ガイド
    </button>
    <button type="button" title="Step検索" @click="$emit('openSearch')">
      <Search :size="17" />
      検索
    </button>
    <button
      type="button"
      :class="{ active: isTodayOnly }"
      :title="isTodayOnly ? '全Step表示に戻す' : '今日やるStepだけ表示'"
      @click="$emit('toggleTodayOnly')"
    >
      <Flag :size="17" />
      今日
    </button>
    <button
      type="button"
      :class="{ active: hideDone }"
      :title="hideDone ? '完了済みも表示' : '完了済みを非表示'"
      @click="$emit('toggleHideDone')"
    >
      <ListFilter :size="17" />
      未完了
    </button>
    <button type="button" title="基礎の未完了だけ復習" @click="$emit('startBasicReview')">
      <BookOpenCheck :size="17" />
      基礎
    </button>
    <button
      type="button"
      :class="{ active: isLightMode }"
      :title="isLightMode ? '通常モードに戻す' : '軽量モードにする'"
      @click="$emit('toggleLightMode')"
    >
      <Gauge :size="17" />
      {{ isLightMode ? "通常" : "軽量" }}
    </button>
    <button type="button" title="今日の学習を保存" @click="$emit('finishSession')">
      <Flag :size="17" />
      終了
    </button>
    <button type="button" title="学習レポートをMarkdownで保存" @click="$emit('downloadReport')">
      <FileDown :size="17" />
      レポート
    </button>
    <button type="button" title="進捗をJSONで保存" @click="$emit('downloadBackup')">
      <Download :size="17" />
      保存
    </button>
    <button type="button" title="進捗JSONを読み込む" @click="pickBackup">
      <Upload :size="17" />
      読込
    </button>
    <button type="button" title="進捗をリセット" @click="$emit('resetProgress')">
      <RotateCcw :size="17" />
      リセット
    </button>
    <input ref="fileInput" type="file" accept="application/json,.json" @change="importBackup" />
  </section>
</template>
