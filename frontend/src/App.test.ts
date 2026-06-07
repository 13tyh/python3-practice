import { flushPromises, mount } from "@vue/test-utils";
import { beforeEach, describe, expect, it, vi } from "vitest";
import App from "./App.vue";

function mockFetch(runResult?: { exit_code: number }) {
  const referencesResponse = {
    ok: true,
    json: async () => [
      {
        step: "01_syntax",
        comment: "基本文法の参照",
        urls: ["https://docs.python.org/3/tutorial/"],
      },
    ],
  };
  const runResponse = {
    ok: true,
    json: async () => ({
      command: "pytest exercise_tests/basics/test_01_values.py -q",
      exit_code: runResult?.exit_code ?? 0,
      duration_ms: 12,
      stdout: runResult?.exit_code === 0 ? "passed" : "",
      stderr: runResult?.exit_code === 0 ? "" : "failed",
    }),
  };

  return vi
    .spyOn(globalThis, "fetch")
    .mockResolvedValueOnce(referencesResponse as Response)
    .mockResolvedValue(runResponse as Response);
}

describe("Python Master app", () => {
  beforeEach(() => {
    window.localStorage.clear();
    window.location.hash = "";
    vi.restoreAllMocks();
  });

  it("hashのStepを表示し、主要パネルを出す", async () => {
    window.location.hash = "#03_files";
    mockFetch();

    const wrapper = mount(App);
    await flushPromises();

    expect(wrapper.text()).toContain("ファイル操作");
    expect(wrapper.text()).toContain("今回のゴール");
    expect(wrapper.text()).toContain("書き方");
    expect(wrapper.text()).toContain("注意点");
    expect(wrapper.text()).toContain("対象ファイル");
  });

  it("基本カテゴリで基礎レベルのStepへ絞り込める", async () => {
    mockFetch();
    const wrapper = mount(App);
    await flushPromises();

    await wrapper.find(".sidebar-filter select").setValue("basic");

    await wrapper.find(".phase-toggle").trigger("click");

    expect(wrapper.text()).toContain("基本文法");
    expect(wrapper.text()).toContain("型ヒント");
    expect(wrapper.text()).not.toContain("logger");
  });

  it("URL hashの変更に追従してStepを切り替える", async () => {
    window.location.hash = "#02_typing_deep";
    mockFetch();
    const wrapper = mount(App);
    await flushPromises();

    window.location.hash = "#59_cli_tools";
    window.dispatchEvent(new Event("hashchange"));
    await flushPromises();

    expect(wrapper.text()).toContain("CLI Tools");
  });

  it("サイドバーを開閉できる", async () => {
    mockFetch();
    const wrapper = mount(App);
    await flushPromises();

    expect(wrapper.find(".mentor-shell").classes()).not.toContain("sidebar-collapsed");
    await wrapper.find(".sidebar-toggle").trigger("click");
    expect(wrapper.find(".mentor-shell").classes()).toContain("sidebar-collapsed");
  });

  it("効率ルートはホーム画面だけに表示する", async () => {
    window.location.hash = "#00_environment";
    mockFetch();
    const wrapper = mount(App);
    await flushPromises();

    expect(wrapper.text()).toContain("今回のゴール");
    expect(wrapper.find(".mentor-main").text()).not.toContain("効率ルート");

    const homeButton = wrapper.findAll(".learning-toolbar button").find((button) => button.text().includes("ホーム"));
    await homeButton?.trigger("click");

    expect(wrapper.text()).toContain("次の1手だけ決める");
    expect(wrapper.find(".home-dashboard").text()).toContain("効率ルート");
    expect(wrapper.text()).not.toContain("今回のゴール");
    expect(homeButton?.classes()).toContain("active");
    expect(wrapper.find(".sidebar-home-link").classes()).toContain("active");
    expect(wrapper.find(".mentor-shell").classes()).not.toContain("sidebar-collapsed");
    expect(wrapper.find(".mentor-step-list button.active").exists()).toBe(false);
  });

  it("軽量モードで参照パネルと実務ラボを畳める", async () => {
    mockFetch();
    const wrapper = mount(App);
    await flushPromises();

    expect(wrapper.find(".mastery-lab").exists()).toBe(false);
    const labToggle = wrapper.findAll(".collapse-toggle").find((button) => button.text().includes("実務ラボ"));
    await labToggle?.trigger("click");
    expect(wrapper.find(".mastery-lab").exists()).toBe(true);

    const lightButton = wrapper.findAll(".learning-toolbar button").find((button) => button.text().includes("軽量"));
    expect(lightButton).toBeDefined();
    await lightButton?.trigger("click");

    expect(wrapper.find(".mentor-shell").classes()).toContain("light-mode");
    expect(wrapper.text()).toContain("軽量モード");
    expect(wrapper.find(".mastery-lab").exists()).toBe(false);
    expect(window.localStorage.getItem("python-master-light-mode")).toBe("true");
  });

  it("保存済みdoneでもテスト成功記録がなければ完了扱いにしない", async () => {
    window.location.hash = "#01_syntax";
    window.localStorage.setItem("python-master-step-status", JSON.stringify({ "01_syntax": "done" }));
    mockFetch();

    const wrapper = mount(App);
    await flushPromises();

    expect(wrapper.text()).toContain("状態");
    expect(wrapper.text()).toContain("学習中");
  });

  it("pytest失敗では完了にせず、pytest成功時だけ完了にする", async () => {
    window.location.hash = "#01_syntax";
    mockFetch({ exit_code: 1 });
    const failedWrapper = mount(App);
    await flushPromises();

    await failedWrapper.find(".run-card button").trigger("click");
    await flushPromises();

    expect(failedWrapper.find(".run-summary").text()).toContain("失敗");
    expect(failedWrapper.find(".run-summary").text()).not.toContain("成功");

    window.localStorage.clear();
    mockFetch({ exit_code: 0 });
    const passedWrapper = mount(App);
    await flushPromises();

    await passedWrapper.find(".run-card button").trigger("click");
    await flushPromises();

    expect(passedWrapper.text()).toContain("成功");
    expect(JSON.parse(window.localStorage.getItem("python-master-passed-tests") ?? "{}")).toEqual({
      "01_syntax": true,
    });
  });
});
