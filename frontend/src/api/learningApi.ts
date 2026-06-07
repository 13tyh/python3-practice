export type RunResult = {
  command: string;
  exit_code: number;
  duration_ms: number;
  stdout: string;
  stderr: string;
};

export type StepReference = {
  step: string;
  comment: string;
  urls: string[];
};

export type FileCompare = {
  exercise_path: string;
  solution_path: string;
  exercise: string;
  solution: string;
  has_solution: boolean;
};

export const apiBase = import.meta.env.VITE_API_BASE ?? "http://localhost:8000";

export async function fetchStepReferences(baseUrl = apiBase) {
  const response = await fetch(`${baseUrl}/api/step-references`);
  if (!response.ok) return [];
  return (await response.json()) as StepReference[];
}

export async function runLearningCommand(command: string, baseUrl = apiBase) {
  const response = await fetch(`${baseUrl}/api/run`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ command }),
  });
  if (!response.ok) {
    const body = (await response.json()) as { detail?: string };
    throw new Error(body.detail ?? "コマンド実行に失敗しました");
  }
  return (await response.json()) as RunResult;
}

export async function fetchSolutionCompare(exercisePath: string, baseUrl = apiBase) {
  const params = new URLSearchParams({ exercise_path: exercisePath });
  const response = await fetch(`${baseUrl}/api/solution-compare?${params.toString()}`);
  if (!response.ok) {
    const body = (await response.json()) as { detail?: string };
    throw new Error(body.detail ?? "解答比較の取得に失敗しました");
  }
  return (await response.json()) as FileCompare;
}
