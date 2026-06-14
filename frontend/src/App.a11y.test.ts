import { flushPromises, mount } from "@vue/test-utils";
import { beforeEach, describe, expect, it, vi } from "vitest";
import App from "./App.vue";

function mockFetch() {
  return vi.spyOn(globalThis, "fetch").mockResolvedValue({
    ok: true,
    json: async () => [],
  } as Response);
}

describe("app accessibility", () => {
  beforeEach(() => {
    window.localStorage.clear();
    window.localStorage.setItem("python-master-onboarding-seen", "true");
    window.location.hash = "#000_environment";
    vi.restoreAllMocks();
  });

  it("主要操作に名前と状態がある", async () => {
    mockFetch();
    const wrapper = mount(App);
    await flushPromises();

    expect(wrapper.find(".run-card button").attributes("aria-label")).toContain("実行");
    expect(wrapper.find(".mentor-search input").attributes("aria-label")).toBe("Stepを検索");
    expect(wrapper.find(".sidebar-filter select").attributes("aria-label")).toBe("category filter");
    expect(wrapper.find(".phase-toggle").attributes("aria-expanded")).toBe("false");
    expect(wrapper.findAll(".learning-toolbar button").every((button) => Boolean(button.attributes("title")))).toBe(true);
  });

  it("キーボードで検索を開閉し、Step移動できる", async () => {
    mockFetch();
    const wrapper = mount(App);
    await flushPromises();

    window.dispatchEvent(new KeyboardEvent("keydown", { key: "/" }));
    await flushPromises();
    expect(wrapper.text()).toContain("Step検索");

    window.dispatchEvent(new KeyboardEvent("keydown", { key: "Escape" }));
    await flushPromises();
    expect(wrapper.find(".command-center").exists()).toBe(false);

    window.dispatchEvent(new KeyboardEvent("keydown", { key: "j" }));
    await flushPromises();
    expect(wrapper.text()).toContain("基本文法");

    window.dispatchEvent(new KeyboardEvent("keydown", { key: "l" }));
    await flushPromises();
    expect(wrapper.find(".mentor-shell").classes()).toContain("light-mode");
  });
});
