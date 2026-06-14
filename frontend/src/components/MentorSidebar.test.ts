import { mount } from "@vue/test-utils";
import { describe, expect, it, vi } from "vitest";
import MentorSidebar from "./MentorSidebar.vue";
import type { Step } from "../data/stepTypes";

const step: Step = {
  id: "001_syntax",
  title: "基本文法",
  category: "python",
  level: "基礎",
  summary: "summary",
  goals: ["goal"],
  files: ["file.py"],
  commands: ["pytest x -q"],
  reviewPoints: ["review"],
};

function mountSidebar(props = {}) {
  return mount(MentorSidebar, {
    props: {
      categories: ["python"],
      doneCount: 0,
      doingCount: 0,
      getStatus: () => "todo",
      isHomeView: false,
      isOpen: true,
      phaseGroups: [{ id: "phase1", title: "Phase 1 / Python基礎集中", steps: [step] }],
      progressPercent: 0,
      query: "",
      selectedCategory: "all",
      selectedStep: step,
      stepNumber: () => 1,
      stepsLength: 1,
      ...props,
    },
  });
}

describe("MentorSidebar", () => {
  it("Phaseは初期状態で折りたたむ", async () => {
    const wrapper = mountSidebar();

    expect(wrapper.findAll(".phase-step-list button")).toHaveLength(0);
    await wrapper.find(".phase-toggle").trigger("click");

    expect(wrapper.findAll(".phase-step-list button")).toHaveLength(1);
  });

  it("検索入力をdebounceしてemitする", async () => {
    vi.useFakeTimers();
    const wrapper = mountSidebar();

    await wrapper.find('input[type="search"]').setValue("api");
    vi.advanceTimersByTime(181);

    expect(wrapper.emitted("update:query")?.[0]).toEqual(["api"]);
    vi.useRealTimers();
  });

  it("Home表示ではHome行だけをactiveにする", async () => {
    const wrapper = mountSidebar({ isHomeView: true });

    expect(wrapper.find(".sidebar-home-link").classes()).toContain("active");
    expect(wrapper.find(".mentor-step-list button.active").exists()).toBe(false);
    expect(wrapper.findAll(".phase-step-list button")).toHaveLength(0);

    await wrapper.find(".sidebar-home-link").trigger("click");
    expect(wrapper.emitted("openHome")).toHaveLength(1);
  });
});
