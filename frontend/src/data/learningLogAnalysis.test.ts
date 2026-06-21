import { describe, expect, it } from "vitest";
import type { LearningEvent } from "../composables/useLearningLog";
import { analyzeLearningLog } from "./learningLogAnalysis";
import type { Step, StepStatus } from "./stepTypes";

const steps: Step[] = [
  {
    id: "001_syntax",
    title: "基本文法",
    category: "python",
    level: "基礎",
    summary: "",
    goals: [],
    files: [],
    commands: [],
    reviewPoints: [],
  },
  {
    id: "130_fastapi_ai",
    title: "FastAPI AI",
    category: "ai",
    level: "AI",
    summary: "",
    goals: [],
    files: [],
    commands: [],
    reviewPoints: [],
  },
];

const events: LearningEvent[] = [
  {
    at: "2026-01-01T00:00:00.000Z",
    category: "ai",
    command: "pytest",
    durationMs: 10,
    exitCode: 1,
    id: "1",
    level: "AI",
    ok: false,
    stepId: "130_fastapi_ai",
    stepTitle: "FastAPI AI",
  },
];

describe("analyzeLearningLog", () => {
  it("失敗Step、苦手カテゴリ、未復習の基礎を出す", () => {
    const status = (id: string): StepStatus => (id === "130_fastapi_ai" ? "doing" : "todo");

    const result = analyzeLearningLog(steps, status, events, new Date("2026-01-03T00:00:00.000Z"));

    expect(result.totalRuns).toBe(1);
    expect(result.failureHotspots[0].title).toBe("FastAPI AI");
    expect(result.weakCategories[0].label).toBe("AI");
    expect(result.staleBasics[0].title).toBe("基本文法");
    expect(result.focusQueue.map((item) => item.stepId)).toEqual(["001_syntax"]);
    expect(result.focusQueue.map((item) => item.title)).not.toContain("FastAPI AI");
    expect(result.nextActions.join(" ")).toContain("失敗ログ");
    expect(result.dueReviews[0]).toMatchObject({ due: true, stepId: "130_fastapi_ai" });
  });
});
