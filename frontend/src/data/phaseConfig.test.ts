import { describe, expect, it } from "vitest";
import { learningPhases, phaseTitleForPosition, phaseTitleForStepId } from "./phaseConfig";

describe("phaseConfig", () => {
  it("phaseごとのstep数を固定する", () => {
    expect(learningPhases.map((phase) => phase.steps.length)).toEqual([26, 15, 22, 25, 41, 5, 8]);
  });

  it("positionからphase名を返す", () => {
    expect(phaseTitleForPosition(1)).toBe("Phase 1 / Python基礎集中");
    expect(phaseTitleForPosition(134)).toBe("Phase 6 / 統合・レビュー");
    expect(phaseTitleForPosition(143)).toBe("Phase 7 / 運用・開発フロー");
  });

  it("step idからphase名を返す", () => {
    expect(phaseTitleForStepId("133_api_compatibility_design")).toBe("Phase 6 / 統合・レビュー");
  });
});
