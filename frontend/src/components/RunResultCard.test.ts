import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";
import RunResultCard from "./RunResultCard.vue";

describe("RunResultCard", () => {
  it("失敗時に重要ログとファイル候補を表示する", async () => {
    const wrapper = mount(RunResultCard, {
      props: {
        runError: "",
        runningCommand: "",
        runResult: {
          command: "pytest",
          duration_ms: 1,
          exit_code: 1,
          stdout: "FAILED tests/test_sample.py::test_x\nE NotImplementedError",
          stderr: "exercises/sample.py:10: NotImplementedError",
        },
      },
    });

    expect(wrapper.text()).toContain("重要ログ");
    expect(wrapper.text()).toContain("TODO未実装");

    await wrapper.find(".file-candidates-toggle").trigger("click");
    expect(wrapper.text()).toContain("exercises/sample.py");
  });
});
