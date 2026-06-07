export type StepStatus = "todo" | "doing" | "done";

export type Step = {
  id: string;
  title: string;
  category: string;
  level: "基礎" | "設計" | "API" | "DB" | "AI" | "実務";
  summary: string;
  goals: string[];
  files: string[];
  commands: string[];
  reviewPoints: string[];
};

export const command = (path: string) => `pytest ${path} -q`;
