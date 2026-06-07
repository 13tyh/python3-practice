import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";
import CommandRunCard from "./CommandRunCard.vue";

describe("CommandRunCard", () => {
  it("実行可能コマンドならrunをemitする", async () => {
    const wrapper = mount(CommandRunCard, {
      props: { command: "pytest exercise_tests -q", runningCommand: "" },
    });

    await wrapper.find("button").trigger("click");

    expect(wrapper.emitted("run")?.[0]).toEqual(["pytest exercise_tests -q"]);
  });

  it("危険なコマンドはdisabledにする", () => {
    const wrapper = mount(CommandRunCard, {
      props: { command: "rm -rf .", runningCommand: "" },
    });

    expect(wrapper.find("button").attributes("disabled")).toBeDefined();
  });
});
