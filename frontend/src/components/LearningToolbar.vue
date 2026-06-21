<script setup lang="ts">
import { Flag, Gauge, Home, RotateCcw, Search } from "lucide-vue-next";

defineProps<{
  isHomeView: boolean;
  isLightMode: boolean;
}>();

const emit = defineEmits<{
  finishSession: [];
  openHome: [];
  openSearch: [];
  resetProgress: [];
  toggleLightMode: [];
}>();
</script>

<template>
  <section class="learning-toolbar" aria-label="学習ツール">
    <button type="button" :class="{ active: isHomeView }" title="ホーム" @click="$emit('openHome')">
      <Home :size="17" />
      ホーム
    </button>
    <button type="button" title="Step検索" @click="$emit('openSearch')">
      <Search :size="17" />
      検索
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
    <button type="button" title="学習を保存" @click="$emit('finishSession')">
      <Flag :size="17" />
      終了
    </button>
    <button type="button" title="進捗をリセット" @click="$emit('resetProgress')">
      <RotateCcw :size="17" />
      リセット
    </button>
  </section>
</template>
