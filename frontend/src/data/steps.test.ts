import { describe, expect, it } from "vitest";
import { learningPhases } from "./phaseConfig";
import { learningOrder } from "./stepOrder";
import { validateStepCatalog } from "./stepValidation";
import { categories, steps } from "./steps";

describe("steps data", () => {
  it("learningOrderとstepsのIDが一致する", () => {
    expect(steps.map((step) => step.id)).toEqual(learningOrder);
  });

  it("step idが重複していない", () => {
    expect(new Set(steps.map((step) => step.id)).size).toBe(steps.length);
  });

  it("各stepに確認コマンドがある", () => {
    for (const step of steps) {
      expect(step.commands[0], `${step.id} has no primary command`).toBeTruthy();
    }
  });

  it("各stepに参照ファイルがある", () => {
    for (const step of steps) {
      expect(step.files.length, `${step.id} has no files`).toBeGreaterThan(0);
    }
  });

  it("カテゴリ一覧がstepsから生成されている", () => {
    expect(categories).toEqual(Array.from(new Set(steps.map((step) => step.category))));
  });

  it("step catalog schemaが有効", () => {
    expect(validateStepCatalog(steps, learningOrder, learningPhases)).toEqual([]);
  });
});
