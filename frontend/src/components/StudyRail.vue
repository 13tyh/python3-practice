<script setup lang="ts">
import { Database, ExternalLink, FileCode2, Lightbulb } from "lucide-vue-next";
import { computed } from "vue";
import type { StepReference } from "../api/learningApi";
import { primaryWorkFile } from "../data/learningUi";
import type { Step } from "../data/stepTypes";

const props = defineProps<{
  reference: StepReference | undefined;
  shouldShowMongo: boolean;
  step: Step;
}>();

function fileName(path: string) {
  return path.split("/").pop() ?? path;
}

const workFile = computed(() => primaryWorkFile(props.step));
</script>

<template>
  <aside class="study-rail">
    <article class="rail-card">
      <div class="work-title">
        <Lightbulb :size="20" />
        <h3>学ぶこと</h3>
      </div>
      <ul>
        <li v-for="goal in step.goals" :key="goal">{{ goal }}</li>
      </ul>
    </article>

    <article class="rail-card">
      <div class="work-title">
        <FileCode2 :size="20" />
        <h3>開くファイル</h3>
      </div>
      <div class="directory-row">
        <span>このStepはここだけ触る</span>
        <strong>{{ fileName(workFile) }}</strong>
        <code>{{ workFile }}</code>
      </div>
    </article>

    <article v-if="reference" class="rail-card">
      <h3>参照リソース</h3>
      <p>{{ reference.comment }}</p>
      <div class="reference-links">
        <a v-for="url in reference.urls" :key="url" :href="url" target="_blank" rel="noreferrer">
          <ExternalLink :size="15" />
          {{ url }}
        </a>
      </div>
    </article>

    <article v-if="shouldShowMongo" class="rail-card">
      <div class="work-title">
        <Database :size="20" />
        <h3>Mongo確認</h3>
      </div>
      <code>docker compose exec mongo mongosh</code>
      <code>use python_master</code>
      <code>show collections</code>
      <code>db.subscriptions.find({}, { "_id": 0 })</code>
    </article>
  </aside>
</template>
