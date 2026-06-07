import type { LearningEvent } from "../composables/useLearningLog";
import { categoryLabel } from "./learningUi";
import type { Step, StepStatus } from "./stepTypes";

export type LearningLogAnalysis = {
  basicDrill: Array<{ reason: string; stepId: string; title: string }>;
  dueReviews: Array<{ due: boolean; nextReviewAt: string; stepId: string; title: string }>;
  failureHotspots: Array<{ failures: number; stepId: string; title: string }>;
  focusQueue: Array<{ label: string; reason: string; stepId: string; title: string }>;
  latestEvents: LearningEvent[];
  nextActions: string[];
  staleBasics: Array<{ lastAt: string; stepId: string; title: string }>;
  successRate: number;
  todayTop3: Array<{ label: string; reason: string; stepId: string; title: string }>;
  totalRuns: number;
  weakCategories: Array<{ category: string; done: number; failures: number; label: string; total: number }>;
};

export function analyzeLearningLog(
  steps: Step[],
  getStatus: (id: string) => StepStatus,
  events: LearningEvent[],
  now = new Date(),
): LearningLogAnalysis {
  const latestByStep = new Map<string, LearningEvent>();
  const failuresByStep = new Map<string, number>();
  const categories = new Map<string, { category: string; done: number; failures: number; label: string; total: number }>();

  for (const step of steps) {
    const entry = categories.get(step.category) ?? {
      done: 0,
      failures: 0,
      category: step.category,
      label: categoryLabel(step.category),
      total: 0,
    };
    entry.total += 1;
    if (getStatus(step.id) === "done") entry.done += 1;
    categories.set(step.category, entry);
  }

  for (const event of events) {
    const previous = latestByStep.get(event.stepId);
    if (!previous || previous.at < event.at) latestByStep.set(event.stepId, event);
    if (!event.ok) {
      failuresByStep.set(event.stepId, (failuresByStep.get(event.stepId) ?? 0) + 1);
      const entry = categories.get(event.category);
      if (entry) entry.failures += 1;
    }
  }

  const failureHotspots = [...failuresByStep.entries()]
    .map(([stepId, failures]) => ({
      failures,
      stepId,
      title: steps.find((step) => step.id === stepId)?.title ?? stepId,
    }))
    .sort((a, b) => b.failures - a.failures)
    .slice(0, 4);

  const weakCategories = [...categories.values()]
    .sort((a, b) => b.failures * 2 + (b.total - b.done) - (a.failures * 2 + (a.total - a.done)))
    .slice(0, 4);

  const staleBasics = steps
    .filter((step) => step.level === "基礎" && getStatus(step.id) !== "done")
    .map((step) => ({ lastAt: latestByStep.get(step.id)?.at ?? "", stepId: step.id, title: step.title }))
    .sort((a, b) => Date.parse(a.lastAt || "1970-01-01") - Date.parse(b.lastAt || "1970-01-01"))
    .slice(0, 4);

  const nextActions = [
    failureHotspots[0] ? `${failureHotspots[0].title} の失敗ログを読み直す` : "",
    staleBasics[0] ? `${staleBasics[0].title} を復習する` : "",
    weakCategories[0] ? `${weakCategories[0].label} を1Step進める` : "",
  ].filter(Boolean);
  const focusQueue = buildFocusQueue(steps, getStatus, failureHotspots, staleBasics, weakCategories);
  const dueReviews = buildDueReviews(steps, getStatus, latestByStep, now);
  const basicDrill = buildBasicDrill(steps, getStatus, now);
  const todayTop3 = buildTodayTop3(focusQueue, dueReviews, staleBasics, basicDrill);

  return {
    basicDrill,
    dueReviews,
    failureHotspots,
    focusQueue,
    latestEvents: [...events].sort((a, b) => b.at.localeCompare(a.at)).slice(0, 6),
    nextActions: nextActions.length > 0 ? nextActions : ["テストを1回実行して学習ログを作る"],
    staleBasics,
    successRate: events.length === 0 ? 0 : Math.round((events.filter((event) => event.ok).length / events.length) * 100),
    todayTop3,
    totalRuns: events.length,
    weakCategories,
  };
}

function buildFocusQueue(
  steps: Step[],
  getStatus: (id: string) => StepStatus,
  failureHotspots: Array<{ failures: number; stepId: string; title: string }>,
  staleBasics: Array<{ lastAt: string; stepId: string; title: string }>,
  weakCategories: Array<{ category: string; done: number; failures: number; label: string; total: number }>,
) {
  const queue: Array<{ label: string; reason: string; stepId: string; title: string }> = [];
  const used = new Set<string>();
  const unfinished = steps.filter((step) => getStatus(step.id) !== "done");
  const earliestLevel = unfinished[0]?.level;
  const earlyPool = earliestLevel ? unfinished.filter((step) => step.level === earliestLevel) : unfinished;
  const push = (label: string, step: Step | undefined, reason: string) => {
    if (!step || used.has(step.id)) return;
    used.add(step.id);
    queue.push({ label, reason, stepId: step.id, title: step.title });
  };

  push(
    "失敗を潰す",
    failureHotspots
      .map((item) => earlyPool.find((step) => step.id === item.stepId))
      .find((step) => step && getStatus(step.id) !== "done"),
    "今のPhase内の失敗を減らす",
  );
  push(
    "基礎を復習",
    staleBasics.map((item) => earlyPool.find((step) => step.id === item.stepId)).find(Boolean),
    "忘れる前に戻す",
  );
  push(
    "弱点を補強",
    earlyPool.find((step) => weakCategories.some((category) => category.category === step.category)),
    earliestLevel ? `${earliestLevel}Phaseを優先` : "",
  );
  push("新規を1つ", earlyPool[0], "順番に前へ進める");
  for (const step of earlyPool) {
    push("順番に進む", step, "早いPhaseから片づける");
  }

  return queue.slice(0, 4);
}

function buildDueReviews(
  steps: Step[],
  getStatus: (id: string) => StepStatus,
  latestByStep: Map<string, LearningEvent>,
  now: Date,
) {
  return steps
    .map((step) => {
      const latest = latestByStep.get(step.id);
      if (!latest || latest.ok || getStatus(step.id) === "done") return null;
      const nextReviewAt = new Date(latest.at);
      nextReviewAt.setDate(nextReviewAt.getDate() + 1);
      return {
        due: nextReviewAt.getTime() <= now.getTime(),
        nextReviewAt: nextReviewAt.toISOString(),
        stepId: step.id,
        title: step.title,
      };
    })
    .filter((item): item is { due: boolean; nextReviewAt: string; stepId: string; title: string } => Boolean(item))
    .sort((a, b) => Number(b.due) - Number(a.due) || a.nextReviewAt.localeCompare(b.nextReviewAt))
    .slice(0, 4);
}

function buildBasicDrill(steps: Step[], getStatus: (id: string) => StepStatus, now: Date) {
  const basics = steps.filter((step) => step.level === "基礎" && getStatus(step.id) !== "done");
  if (basics.length === 0) return [];
  const seed = Math.floor(now.getTime() / 86_400_000) % basics.length;
  return [...basics.slice(seed), ...basics.slice(0, seed)]
    .slice(0, 3)
    .map((step) => ({ reason: "基礎ランダム出題", stepId: step.id, title: step.title }));
}

function buildTodayTop3(
  focusQueue: Array<{ label: string; reason: string; stepId: string; title: string }>,
  dueReviews: Array<{ due: boolean; nextReviewAt: string; stepId: string; title: string }>,
  staleBasics: Array<{ lastAt: string; stepId: string; title: string }>,
  basicDrill: Array<{ reason: string; stepId: string; title: string }>,
) {
  const queue: Array<{ label: string; reason: string; stepId: string; title: string }> = [];
  const used = new Set<string>();
  const push = (item: { label: string; reason: string; stepId: string; title: string } | undefined) => {
    if (!item || used.has(item.stepId)) return;
    used.add(item.stepId);
    queue.push(item);
  };

  for (const item of dueReviews.filter((review) => review.due)) {
    push({ label: "昨日の失敗を復習", reason: "1日後にもう一度解く", stepId: item.stepId, title: item.title });
  }
  for (const item of staleBasics) {
    push({ label: "基礎を戻す", reason: "序盤の穴を残さない", stepId: item.stepId, title: item.title });
  }
  for (const item of basicDrill) {
    push({ label: "ランダム基礎", reason: item.reason, stepId: item.stepId, title: item.title });
  }
  for (const item of focusQueue) push(item);

  return queue.slice(0, 3);
}
