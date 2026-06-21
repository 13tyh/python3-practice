import { describe, expect, it } from "vitest";
import {
  buildStepGuide,
  categoryLabel,
  extractFileCandidates,
  extractRunHighlights,
  getPhase,
  isRunnable,
  isTestCommand,
  methodPrimerForStep,
  primaryWorkFile,
  runFailureHint,
  runResultGuide,
} from "./learningUi";
import type { Step } from "./steps";

const step: Step = {
  id: "001_syntax",
  title: "基本文法",
  category: "python",
  level: "基礎",
  summary: "summary",
  goals: ["goal"],
  files: ["steps/001_syntax/implementation/exercises/basics/01_values.py"],
  commands: ["pytest steps/001_syntax/tests -q"],
  reviewPoints: ["境界値を見る"],
};

describe("learningUi", () => {
  it("step番号からphase名を返す", () => {
    expect(getPhase(1)).toBe("Phase 1 / Python基礎集中");
    expect(getPhase(134)).toBe("Phase 6 / 統合・レビュー");
    expect(getPhase(143)).toBe("Phase 7 / 運用・開発フロー");
  });

  it("カテゴリ表示名を返す", () => {
    expect(categoryLabel("python")).toBe("Python");
    expect(categoryLabel("unknown")).toBe("unknown");
  });

  it("実行可能コマンドとtestコマンドを判定する", () => {
    expect(isRunnable("pytest steps/001_syntax/tests -q")).toBe(true);
    expect(isRunnable("rm -rf .")).toBe(false);
    expect(isTestCommand("pytest steps/001_syntax/tests -q")).toBe(true);
    expect(isTestCommand("uv run build")).toBe(false);
  });

  it("stepの書き方と注意点を作る", () => {
    const guide = buildStepGuide(step);

    expect(guide.writing[0]).toContain(step.files[0]);
    expect(guide.cautions).toContain("境界値を見る");
  });

  it("READMEではなく作業ファイルを返す", () => {
    expect(primaryWorkFile({ ...step, files: ["steps/001_syntax/README.md", step.files[0]] })).toBe(step.files[0]);
  });

  it("stepに合う短い座学を返す", () => {
    const primer = methodPrimerForStep(step);

    expect(primer.title).toBe("最初に使うメソッド");
    expect(primer.items.length).toBeGreaterThan(0);
  });

  it("実行結果に応じた案内を返す", () => {
    expect(runResultGuide(null)).toContain("実行ボタン");
    expect(
      runResultGuide({ command: "pytest", exit_code: 0, duration_ms: 1, stdout: "", stderr: "" }),
    ).toContain("成功");
    expect(
      runResultGuide({ command: "pytest", exit_code: 1, duration_ms: 1, stdout: "", stderr: "" }),
    ).toContain("失敗ログ");
  });

  it("失敗ログから重要行を抽出する", () => {
    expect(
      extractRunHighlights({
        command: "pytest",
        duration_ms: 1,
        exit_code: 1,
        stdout: "FAILED test_sample.py::test_x\nE AssertionError: bad",
        stderr: "tests/test_sample.py:10: AssertionError",
      }),
    ).toEqual([
      "FAILED test_sample.py::test_x",
      "E AssertionError: bad",
      "tests/test_sample.py:10: AssertionError",
    ]);
  });

  it("失敗ログからヒントと対象ファイル候補を返す", () => {
    const result = {
      command: "pytest",
      duration_ms: 1,
      exit_code: 1,
      stdout: "FAILED tests/test_sample.py",
      stderr: "steps/001_syntax/implementation/exercises/sample.py:10: NotImplementedError",
    };

    expect(runFailureHint(result)).toContain("TODO未実装");
    expect(extractFileCandidates(result)).toEqual([
      "tests/test_sample.py",
      "steps/001_syntax/implementation/exercises/sample.py",
    ]);
  });
});
