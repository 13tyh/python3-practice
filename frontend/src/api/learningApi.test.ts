import { afterEach, describe, expect, it, vi } from "vitest";
import { fetchSolutionCompare, fetchStepReferences, runLearningCommand } from "./learningApi";

afterEach(() => {
  vi.unstubAllGlobals();
});

describe("learningApi", () => {
  it("step referencesを取得する", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue({
        ok: true,
        json: async () => [{ step: "01", comment: "comment", urls: ["https://example.com"] }],
      }),
    );

    await expect(fetchStepReferences("http://api")).resolves.toEqual([
      { step: "01", comment: "comment", urls: ["https://example.com"] },
    ]);
  });

  it("commandを実行する", async () => {
    const fetchMock = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({ command: "pytest x -q", exit_code: 0, duration_ms: 1, stdout: "ok", stderr: "" }),
    });
    vi.stubGlobal("fetch", fetchMock);

    await expect(runLearningCommand("pytest x -q", "http://api")).resolves.toMatchObject({
      command: "pytest x -q",
      exit_code: 0,
    });
    expect(fetchMock).toHaveBeenCalledWith(
      "http://api/api/run",
      expect.objectContaining({ method: "POST" }),
    );
  });

  it("command失敗時はAPIのdetailを投げる", async () => {
    vi.stubGlobal(
      "fetch",
      vi.fn().mockResolvedValue({
        ok: false,
        json: async () => ({ detail: "not allowed" }),
      }),
    );

    await expect(runLearningCommand("rm -rf .", "http://api")).rejects.toThrow("not allowed");
  });

  it("solutions比較を取得する", async () => {
    const fetchMock = vi.fn().mockResolvedValue({
      ok: true,
      json: async () => ({
        exercise_path: "steps/01_syntax/implementation/exercises/basics/01_values.py",
        solution_path: "steps/01_syntax/solutions/basics/01_values.py",
        exercise: "raise NotImplementedError",
        solution: "return value",
        has_solution: true,
      }),
    });
    vi.stubGlobal("fetch", fetchMock);

    await expect(
      fetchSolutionCompare("steps/01_syntax/implementation/exercises/basics/01_values.py", "http://api"),
    ).resolves.toMatchObject({
      has_solution: true,
      solution_path: "steps/01_syntax/solutions/basics/01_values.py",
    });
    expect(fetchMock).toHaveBeenCalledWith(
      "http://api/api/solution-compare?exercise_path=steps%2F01_syntax%2Fimplementation%2Fexercises%2Fbasics%2F01_values.py",
    );
  });
});
