import { flushPromises, mount } from "@vue/test-utils";
import { beforeEach, describe, expect, it, vi } from "vitest";
import App from "./App.vue";

function mockFetch(runResult?: { exit_code: number }) {
  const referencesResponse = {
    ok: true,
    json: async () => [
      {
        step: "001_syntax",
        comment: "基本文法の参照",
        urls: ["https://docs.python.org/3/tutorial/"],
      },
    ],
  };
  const runResponse = {
    ok: true,
    json: async () => ({
      command: "pytest steps/001_syntax/tests -q",
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

  it("hashなし起動ではhomeへ正規化し、Step画面へ行かない", async () => {
    mockFetch();
    const wrapper = mount(App);
    await flushPromises();

    expect(window.location.hash).toBe("#home");
    expect(wrapper.find(".home-dashboard").exists()).toBe(true);
    expect(wrapper.text()).toContain("次の1問だけ解く");
    expect(wrapper.text()).not.toContain("この1問");
    expect(wrapper.find(".sidebar-home-link").classes()).toContain("active");
    expect(wrapper.find(".mentor-step-list button.active").exists()).toBe(false);
  });

  it("hashのStepを表示し、主要パネルを出す", async () => {
    window.location.hash = "#025_files";
    mockFetch();

    const wrapper = mount(App);
    await flushPromises();

    expect(wrapper.text()).toContain("ファイル操作");
    expect(wrapper.text()).toContain("この1問");
    expect(wrapper.text()).toContain("最短合格条件");
    expect(wrapper.text()).toContain("読む");
    expect(wrapper.text()).toContain("解く");

    const writeTab = wrapper.findAll(".lesson-tabs button").find((button) => button.text().includes("解く"));
    await writeTab?.trigger("click");

    expect(wrapper.text()).toContain("解く順番");
    expect(wrapper.text()).toContain("注意点");
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
    window.location.hash = "#023_typing_deep";
    mockFetch();
    const wrapper = mount(App);
    await flushPromises();

    window.location.hash = "#135_cli_tools";
    window.dispatchEvent(new Event("hashchange"));
    await flushPromises();

    expect(wrapper.text()).toContain("CLI Tools");
  });

  it("サイドバーを開閉できる", async () => {
    mockFetch();
    const wrapper = mount(App);
    await flushPromises();

    expect(wrapper.find(".mentor-shell").classes()).toContain("sidebar-collapsed");
    await wrapper.find(".sidebar-toggle").trigger("click");
    expect(wrapper.find(".mentor-shell").classes()).not.toContain("sidebar-collapsed");
  });

  it("効率ルートはホーム画面だけに表示する", async () => {
    window.location.hash = "#001_syntax";
    mockFetch();
    const wrapper = mount(App);
    await flushPromises();

    expect(wrapper.text()).toContain("この1問");
    expect(wrapper.find(".mentor-main").text()).not.toContain("効率ルート");

    const homeButton = wrapper.findAll(".learning-toolbar button").find((button) => button.text().includes("ホーム"));
    await homeButton?.trigger("click");

    expect(wrapper.text()).toContain("次の1問だけ解く");
    expect(wrapper.find(".home-dashboard").text()).toContain("効率ルート");
    expect(wrapper.text()).not.toContain("この1問");
    expect(homeButton?.classes()).toContain("active");
    expect(wrapper.find(".sidebar-home-link").classes()).toContain("active");
    expect(wrapper.find(".mentor-shell").classes()).toContain("sidebar-collapsed");
    expect(wrapper.find(".mentor-step-list button.active").exists()).toBe(false);
  });

  it("軽量モードで参照パネルと実務ラボを畳める", async () => {
    window.location.hash = "#001_syntax";
    mockFetch();
    const wrapper = mount(App);
    await flushPromises();

    expect(wrapper.find(".mastery-lab").exists()).toBe(false);
    const labToggle = wrapper.findAll(".collapse-toggle").find((button) => button.text().includes("実務ラボ"));
    expect(labToggle).toBeUndefined();
    const reviewTab = wrapper.findAll(".lesson-tabs button").find((button) => button.text().includes("メモ"));
    await reviewTab?.trigger("click");
    const openedLabToggle = wrapper.findAll(".collapse-toggle").find((button) => button.text().includes("実務ラボ"));
    expect(openedLabToggle).toBeDefined();
    await openedLabToggle?.trigger("click");
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
    window.location.hash = "#001_syntax";
    window.localStorage.setItem("python-master-step-status", JSON.stringify({ "001_syntax": "done" }));
    mockFetch();

    const wrapper = mount(App);
    await flushPromises();

    expect(wrapper.text()).toContain("状態");
    expect(wrapper.text()).toContain("学習中");
  });

  it("pytest失敗では完了にせず、pytest成功時だけ完了にする", async () => {
    window.location.hash = "#001_syntax";
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
      "001_syntax": true,
    });
  });
});
