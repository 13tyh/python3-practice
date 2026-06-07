import { computed } from "vue";
import { afterEach, describe, expect, it, vi } from "vitest";
import { useStepRunner } from "./useStepRunner";
import type { Step } from "../data/stepTypes";

const step: Step = {
  id: "01_syntax",
  title: "基本文法",
  category: "python",
  level: "基礎",
  summary: "summary",
  goals: ["goal"],
  files: ["file.py"],
  commands: ["pytest x -q"],
  reviewPoints: ["review"],
};

function progressSpies() {
  return {
    markTestFailed: vi.fn(),
    markTestPassed: vi.fn(),
    markTestStarted: vi.fn(),
    setStatus: vi.fn(),
  };
}

afterEach(() => {
  vi.unstubAllGlobals();
});

describe("useStepRunner", () => {
  it("pytest成功時に完了扱いにする", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue({
        ok: true,
        json: async () => ({ command: "pytest x -q", exit_code: 0, duration_ms: 1, stdout: "ok", stderr: "" }),
      }),
    );
    const progress = progressSpies();
    const runner = useStepRunner(computed(() => step), progress);

    await runner.runCommand("pytest x -q");

    expect(progress.markTestStarted).toHaveBeenCalledWith("01_syntax");
    expect(progress.markTestPassed).toHaveBeenCalledWith("01_syntax");
    expect(runner.runResult.value?.exit_code).toBe(0);
  });

  it("pytest失敗時に完了扱いにしない", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue({
        ok: true,
        json: async () => ({ command: "pytest x -q", exit_code: 1, duration_ms: 1, stdout: "", stderr: "fail" }),
      }),
    );
    const progress = progressSpies();
    const runner = useStepRunner(computed(() => step), progress);

    await runner.runCommand("pytest x -q");

    expect(progress.markTestFailed).toHaveBeenCalledWith("01_syntax");
    expect(progress.markTestPassed).not.toHaveBeenCalled();
  });
});
