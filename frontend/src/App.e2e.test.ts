import { flushPromises, mount } from "@vue/test-utils";
import { beforeEach, describe, expect, it, vi } from "vitest";
import App from "./App.vue";

function mockFetch() {
  return vi
    .spyOn(globalThis, "fetch")
    .mockResolvedValueOnce({
      ok: true,
      json: async () => [{ step: "001_syntax", comment: "syntax", urls: ["https://example.com"] }],
    } as Response)
    .mockResolvedValue({
      ok: true,
      json: async () => ({
        command: "pytest steps/133_api_compatibility_design/tests -q",
        duration_ms: 10,
        exit_code: 0,
        stdout: "passed",
        stderr: "",
      }),
    } as Response);
}

describe("app e2e flow", () => {
  beforeEach(() => {
    window.localStorage.clear();
    window.location.hash = "#001_syntax";
    vi.restoreAllMocks();
  });

  it("起動、検索、Step選択、テスト成功、ホーム復帰まで進める", async () => {
    mockFetch();
    const wrapper = mount(App);
    await flushPromises();

    expect(wrapper.text()).toContain("基本文法");

    const searchButton = wrapper.findAll(".learning-toolbar button").find((button) => button.text().includes("検索"));
    expect(searchButton).toBeTruthy();
    await searchButton?.trigger("click");
    await wrapper.find(".command-search input").setValue("API Compatibility");
    await flushPromises();

    const target = wrapper.findAll(".command-results button").find((button) => button.text().includes("API Compatibility"));
    expect(target).toBeTruthy();
    await target?.trigger("click");
    await flushPromises();
    expect(wrapper.text()).toContain("API Compatibility Design");

    await wrapper.find(".run-card button").trigger("click");
    await flushPromises();
    expect(wrapper.find(".run-summary").text()).toContain("成功");
    expect(wrapper.text()).not.toContain("効率ルート");
    expect(window.localStorage.getItem("python-master-learning-events")).toContain("API Compatibility Design");

    const homeButton = wrapper.findAll(".learning-toolbar button").find((button) => button.text().includes("ホーム"));
    await homeButton?.trigger("click");
    expect(wrapper.text()).toContain("効率ルート");
    expect(wrapper.findAll(".learning-toolbar button").some((button) => button.text().includes("レポート"))).toBe(false);
    expect(wrapper.findAll(".learning-toolbar button").some((button) => button.text().includes("保存"))).toBe(false);
    expect(wrapper.findAll(".learning-toolbar button").some((button) => button.text().includes("読込"))).toBe(false);
  });

  it("学習メモ一覧を表示する", async () => {
    window.localStorage.setItem(
      "python-master-lab:001_syntax",
      JSON.stringify({ answer: "基本文法を説明した", ragQuestion: "なぜ小さい関数にする？", review: "tracebackを確認" }),
    );
    mockFetch();
    const wrapper = mount(App);
    await flushPromises();

    const reviewTab = wrapper.findAll(".lesson-tabs button").find((button) => button.text().includes("メモ"));
    await reviewTab?.trigger("click");
    const labToggle = wrapper.findAll(".collapse-toggle").find((button) => button.text().includes("実務ラボ"));
    await labToggle?.trigger("click");
    const memoTab = wrapper.findAll(".lab-tabs button").find((button) => button.text().includes("メモ"));
    await memoTab?.trigger("click");

    expect(wrapper.text()).toContain("学習メモ一覧");
    expect(wrapper.text()).toContain("基本文法を説明した");
  });
});
