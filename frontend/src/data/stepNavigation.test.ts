import { describe, expect, it } from "vitest";
import { filterSteps, findStepById, nextStepAfter, stepAtOffset, stepNumberOf } from "./stepNavigation";
import type { Step } from "./steps";

const items: Step[] = [
  {
    id: "01",
    title: "Python Basic",
    category: "python",
    level: "基礎",
    summary: "syntax",
    goals: [],
    files: [],
    commands: [],
    reviewPoints: [],
  },
  {
    id: "02",
    title: "FastAPI",
    category: "api",
    level: "API",
    summary: "router",
    goals: [],
    files: [],
    commands: [],
    reviewPoints: [],
  },
];

describe("stepNavigation", () => {
  it("idからstepと番号を返す", () => {
    expect(findStepById(items, "02")?.title).toBe("FastAPI");
    expect(findStepById(items, "missing")?.id).toBe("01");
    expect(stepNumberOf(items, "02")).toBe(2);
  });

  it("前後のstepを返す", () => {
    expect(stepAtOffset(items, "01", 1)?.id).toBe("02");
    expect(stepAtOffset(items, "01", -1)?.id).toBe("01");
    expect(nextStepAfter(items, "01")?.id).toBe("02");
    expect(nextStepAfter(items, "02")).toBeNull();
  });

  it("カテゴリと文字列で絞り込む", () => {
    expect(filterSteps(items, "", "basic").map((step) => step.id)).toEqual(["01"]);
    expect(filterSteps(items, "router", "all").map((step) => step.id)).toEqual(["02"]);
  });
});
