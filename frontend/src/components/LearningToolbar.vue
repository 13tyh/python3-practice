<script setup lang="ts">
import { BookOpenCheck, Flag, Gauge, HelpCircle, Home, ListFilter, RotateCcw, Search, Shuffle } from "lucide-vue-next";

defineProps<{
  hideDone: boolean;
  isHomeView: boolean;
  isTodayOnly: boolean;
  isLightMode: boolean;
}>();

const emit = defineEmits<{
  finishSession: [];
  startBasicReview: [];
  openHome: [];
  openGuide: [];
  openSearch: [];
  resetProgress: [];
  toggleHideDone: [];
  toggleLightMode: [];
  toggleTodayOnly: [];
  startRandomBasic: [];
}>();
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
    <button type="button" title="基礎Stepをランダムに出す" @click="$emit('startRandomBasic')">
      <Shuffle :size="17" />
      ランダム
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
    <button type="button" title="進捗をリセット" @click="$emit('resetProgress')">
      <RotateCcw :size="17" />
      リセット
    </button>
  </section>
</template>
