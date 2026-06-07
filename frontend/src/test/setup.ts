import { afterEach, beforeEach, vi } from "vitest";

beforeEach(() => {
  window.localStorage.clear();
  window.location.hash = "";
});

afterEach(() => {
  vi.restoreAllMocks();
});
