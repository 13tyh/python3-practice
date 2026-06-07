import { flushPromises, mount } from "@vue/test-utils";
import { beforeEach, describe, expect, it, vi } from "vitest";
import App from "./App.vue";

function mockFetch() {
  return vi
    .spyOn(globalThis, "fetch")
    .mockResolvedValueOnce({
      ok: true,
      json: async () => [{ step: "00_environment", comment: "env", urls: ["https://example.com"] }],
    } as Response)
    .mockResolvedValue({
      ok: true,
      json: async () => ({
        command: "pytest exercise_tests/api_compatibility_design/test_api_compatibility.py -q",
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
    window.localStorage.setItem("python-master-onboarding-seen", "true");
    window.location.hash = "#00_environment";
    vi.restoreAllMocks();
    vi.stubGlobal("URL", {
      createObjectURL: vi.fn(() => "blob:report"),
      revokeObjectURL: vi.fn(),
    });
    vi.spyOn(HTMLAnchorElement.prototype, "click").mockImplementation(() => undefined);
  });

  it("起動、検索、Step選択、テスト成功、バックアップ出力まで進める", async () => {
    mockFetch();
    const wrapper = mount(App);
    await flushPromises();

    expect(wrapper.text()).toContain("環境構築");

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

    const backupButton = wrapper.findAll(".learning-toolbar button").find((button) => button.text().includes("保存"));
    await backupButton?.trigger("click");
    expect(URL.createObjectURL).toHaveBeenCalled();
  });

  it("学習メモ一覧を表示し、Markdownレポートへ含める", async () => {
    const reportBlob: { value: Blob | null } = { value: null };
    vi.stubGlobal("URL", {
      createObjectURL: vi.fn((blob: Blob) => {
        reportBlob.value = blob;
        return "blob:report";
      }),
      revokeObjectURL: vi.fn(),
    });
    window.localStorage.setItem(
      "python-master-lab:00_environment",
      JSON.stringify({ answer: "Dockerの役割を説明した", ragQuestion: "なぜDockerで統一する？", review: "envとログを確認" }),
    );
    mockFetch();
    const wrapper = mount(App);
    await flushPromises();

    const labToggle = wrapper.findAll(".collapse-toggle").find((button) => button.text().includes("実務ラボ"));
    await labToggle?.trigger("click");
    const memoTab = wrapper.findAll(".lab-tabs button").find((button) => button.text().includes("メモ"));
    await memoTab?.trigger("click");

    expect(wrapper.text()).toContain("学習メモ一覧");
    expect(wrapper.text()).toContain("Dockerの役割を説明した");

    const reportButton = wrapper.findAll(".learning-toolbar button").find((button) => button.text().includes("レポート"));
    await reportButton?.trigger("click");

    expect(reportBlob.value).not.toBeNull();
    await expect(reportBlob.value?.text()).resolves.toContain("Dockerの役割を説明した");
  });
});
