import type { Step } from "./steps";

export function findStepById(steps: Step[], id: string) {
  return steps.find((step) => step.id === id) ?? steps[0];
}

export function stepNumberOf(steps: Step[], id: string) {
  return steps.findIndex((step) => step.id === id) + 1;
}

export function stepAtOffset(steps: Step[], currentId: string, offset: number) {
  const index = steps.findIndex((step) => step.id === currentId);
  const nextIndex = Math.min(Math.max(index + offset, 0), steps.length - 1);
  return steps[nextIndex];
}

export function nextStepAfter(steps: Step[], currentId: string) {
  const index = steps.findIndex((step) => step.id === currentId);
  return steps[index + 1] ?? null;
}

export function filterSteps(steps: Step[], query: string, selectedCategory: string) {
  const text = query.trim().toLowerCase();
  return steps.filter((step) => {
    const categoryOk =
      selectedCategory === "all" ||
      (selectedCategory === "basic" && step.level === "基礎") ||
      step.category === selectedCategory;
    const textOk =
      text.length === 0 ||
      [step.id, step.title, step.summary, step.category, step.level].some((value) =>
        value.toLowerCase().includes(text),
      );
    return categoryOk && textOk;
  });
}
