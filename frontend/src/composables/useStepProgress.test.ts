import { defineComponent, nextTick } from "vue";
import { mount } from "@vue/test-utils";
import { describe, expect, it } from "vitest";
import { useStepProgress } from "./useStepProgress";

const Harness = defineComponent({
  setup() {
    return useStepProgress();
  },
  template: `
    <div>
      <span class="status">{{ getStatus("001_syntax") }}</span>
      <button class="pass" @click="markTestPassed('001_syntax')">pass</button>
      <button class="fail" @click="markTestFailed('001_syntax')">fail</button>
      <button class="done" @click="setStatus('001_syntax', 'done')">done</button>
    </div>
  `,
});

describe("useStepProgress", () => {
  it("localStorageから進捗を復元する", async () => {
    localStorage.setItem("python-master-step-status", JSON.stringify({ "001_syntax": "done" }));
    localStorage.setItem("python-master-passed-tests", JSON.stringify({ "001_syntax": true }));

    const wrapper = mount(Harness);
    await nextTick();

    expect(wrapper.find(".status").text()).toBe("done");
  });

  it("doneでもテスト成功記録がなければdoing扱いにする", async () => {
    localStorage.setItem("python-master-step-status", JSON.stringify({ "001_syntax": "done" }));

    const wrapper = mount(Harness);
    await nextTick();

    expect(wrapper.find(".status").text()).toBe("doing");
  });

  it("テスト成功時だけ完了にする", async () => {
    const wrapper = mount(Harness);

    await wrapper.find(".pass").trigger("click");
    await nextTick();
    expect(wrapper.find(".status").text()).toBe("done");

    await wrapper.find(".fail").trigger("click");
    await nextTick();
    expect(wrapper.find(".status").text()).toBe("doing");
  });
});
