import type { LearningPhase } from "./phaseConfig";
import type { Step } from "./stepTypes";

export function validateStepCatalog(steps: Step[], learningOrder: string[], phases: LearningPhase[]) {
  const errors: string[] = [];
  const stepIds = steps.map((step) => step.id);
  const duplicatedIds = stepIds.filter((id, index) => stepIds.indexOf(id) !== index);
  const phaseIds = phases.flatMap((phase) => phase.steps.map((step) => step.id));

  if (duplicatedIds.length > 0) {
    errors.push(`duplicated step ids: ${[...new Set(duplicatedIds)].join(", ")}`);
  }
  if (JSON.stringify(stepIds) !== JSON.stringify(learningOrder)) {
    errors.push("steps order does not match learningOrder");
  }
  if (JSON.stringify(phaseIds) !== JSON.stringify(learningOrder)) {
    errors.push("phase steps do not match learningOrder");
  }

  for (const step of steps) {
    if (!step.id.trim()) errors.push("step id is empty");
    if (!step.title.trim()) errors.push(`${step.id}: title is empty`);
    if (!step.summary.trim()) errors.push(`${step.id}: summary is empty`);
    if (step.goals.length === 0) errors.push(`${step.id}: goals is empty`);
    if (step.files.length === 0) errors.push(`${step.id}: files is empty`);
    if (step.commands.length === 0 || !step.commands[0]?.trim()) {
      errors.push(`${step.id}: primary command is empty`);
    }
    if (step.commands.length > 1) {
      errors.push(`${step.id}: only one command is allowed`);
    }
    if (step.reviewPoints.length === 0) errors.push(`${step.id}: reviewPoints is empty`);
  }

  return errors;
}
