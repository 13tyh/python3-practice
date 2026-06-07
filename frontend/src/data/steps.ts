export type { Step, StepStatus } from "./stepTypes";

import { phase1Steps } from "./phase1Steps";
import { phase2Steps } from "./phase2Steps";
import { phase3Steps } from "./phase3Steps";
import { phase4Steps } from "./phase4Steps";
import { phase5Steps } from "./phase5Steps";
import { phase6Steps } from "./phase6Steps";
import { phase7Steps } from "./phase7Steps";
import { learningOrder } from "./stepOrder";

export const stepItems = [
  ...phase1Steps,
  ...phase2Steps,
  ...phase3Steps,
  ...phase4Steps,
  ...phase5Steps,
  ...phase6Steps,
  ...phase7Steps,
];

const orderMap = new Map(learningOrder.map((id, index) => [id, index]));

export const steps = [...stepItems].sort(
  (left, right) => (orderMap.get(left.id) ?? 999) - (orderMap.get(right.id) ?? 999),
);

export const categories = Array.from(new Set(steps.map((step) => step.category)));
