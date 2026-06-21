import type { Step, StepStatus } from "./steps";
import type { RunResult } from "../api/learningApi";
import { phaseTitleForPosition } from "./phaseConfig";

export type MethodPrimer = {
  title: string;
  lead: string;
  items: string[];
};

export const categoryLabels: Record<string, string> = {
  setup: "環境",
  python: "Python",
  test: "テスト",
  design: "設計",
  ops: "運用",
  reading: "読解",
  api: "API",
  security: "認証/安全",
  performance: "性能",
  db: "DB",
  data: "分析/出力",
  ai: "AI",
  review: "レビュー",
  project: "総仕上げ",
};

const writingTipsByCategory: Record<string, string[]> = {
  setup: ["画面の説明に沿ってコマンドを1つずつ実行する", "失敗したコマンドとエラー行をメモする"],
  python: ["小さい関数に分けて、入力と戻り値を先に決める", "リスト内包表記は1行で読める時だけ使う"],
  test: ["正常系、異常系、境界値を分けて書く", "外部APIやDBはfakeやfixtureに置き換える"],
  design: ["router、service、modelの責務を分ける", "副作用のある処理と純粋な計算を分ける"],
  ops: ["loggerを使い、request_idや処理時間を残す", "secretや個人情報はログに出さない"],
  reading: ["入口、呼び出し先、テストの順に読む", "変更前に影響範囲をメモする"],
  api: ["リクエスト/レスポンスの型を先に作る", "HTTP例外と業務例外を混ぜない"],
  security: ["認証、認可、入力検証を別々に考える", "危険な入力は境界で止める"],
  performance: ["N+1、全件読み込み、重いループを先に疑う", "計測してから改善する"],
  db: ["検索条件、index、projectionを意識して書く", "mongoshで実データを確認してから実装する"],
  data: ["読み込み、変換、出力を段階に分ける", "CSV/PDF/JSONLは文字コードと欠損値を確認する"],
  ai: ["prompt、model、入力、出力をログで追える形にする", "AI出力はschemaとテストで検証する"],
  review: ["何が悪いか、なぜ危険か、どう直すかを書く", "AIの答えを鵜呑みにせず根拠を確認する"],
  project: ["settings、logger、router、service、modelを揃える", "小さく動かしてから結合する"],
};

const cautionTipsByCategory: Record<string, string[]> = {
  python: ["mutable default引数を使わない", "例外を bare except で握りつぶさない"],
  db: ["find()の結果を無制限に全件メモリへ載せない", "本番相当データではindexなし検索に注意する"],
  api: ["routerにDB操作やAI呼び出しを全部書かない", "型ヒントと実際の戻り値をズラさない"],
  ai: ["deployment_nameとmodel_nameを混同しない", "prompt injectionと空回答をテストする"],
  performance: ["推測で最適化しない", "N+1をループ内DB/API呼び出しとして探す"],
};

const methodPrimersByCategory: Record<string, MethodPrimer> = {
  python: {
    title: "最初に使うメソッド",
    lead: "このStepは全部覚えなくてOK。まず1つ動かして、失敗ログで必要なものだけ確認します。",
    items: ["len / range: 個数と繰り返し", "str.strip / split / join: 文字列を整える", "list.append / dict.get: 値を追加・安全に読む"],
  },
  test: {
    title: "テストで見るところ",
    lead: "pytestは答え合わせです。失敗したら、最初のFAILEDとAssertionErrorだけ見ます。",
    items: ["assert: 期待値と実際の値を比べる", "fixture: テスト前の準備", "monkeypatch: 外部依存を一時的に差し替える"],
  },
  api: {
    title: "APIで見るところ",
    lead: "入口、型、返す値の順で見ます。routerに全部書かないのがコツです。",
    items: ["GET / POST: 取得と作成", "status_code: 成功・失敗の種類", "json / schema: 入出力の形"],
  },
  db: {
    title: "DBで見るところ",
    lead: "全件取得より、条件・件数・並び順を先に決めます。",
    items: ["find / filter: 必要な行だけ取る", "limit / sort: 件数と順序を絞る", "index: よく検索する列を速くする"],
  },
  ai: {
    title: "AIで見るところ",
    lead: "prompt、入力、出力schema、失敗時の扱いを分けて確認します。",
    items: ["prompt: 指示文", "schema: AI出力の形", "fallback: 失敗した時の逃げ道"],
  },
};

export function getPhase(number: number) {
  return phaseTitleForPosition(number);
}

export function categoryLabel(category: string) {
  return categoryLabels[category] ?? category;
}

export function statusLabel(status: StepStatus) {
  if (status === "done") return "完了";
  if (status === "doing") return "学習中";
  return "未着手";
}

export function runResultGuide(result: RunResult | null) {
  if (!result) return "実行ボタンを押すと、ここに終了コード、標準出力、エラーが表示されます。";
  if (result.exit_code === 0) return "成功です。このStepは完了にして、次のStepへ進めます。";
  return "失敗ログの最初のFAILURESと行番号を読み、対象ファイルのTODOを直します。";
}

export function extractRunHighlights(result: RunResult | null) {
  if (!result || result.exit_code === 0) return [];
  const lines = `${result.stdout}\n${result.stderr}`
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);
  const importantPatterns = [
    /^FAILED /,
    /^E\s+/,
    /AssertionError/,
    /Error:/,
    /Exception/,
    /NotImplementedError/,
    /\.py:\d+/,
  ];
  return lines.filter((line) => importantPatterns.some((pattern) => pattern.test(line))).slice(0, 8);
}

export function runFailureHint(result: RunResult | null) {
  if (!result || result.exit_code === 0) return "";
  const output = `${result.stdout}\n${result.stderr}`;
  if (output.includes("NotImplementedError")) {
    return "TODO未実装です。対象ファイルの raise NotImplementedError を実装に置き換えます。";
  }
  if (output.includes("AssertionError")) {
    return "期待値との差分があります。テストのexpectedとactualを比べます。";
  }
  if (output.includes("ModuleNotFoundError")) {
    return "import先が見つかっていません。ファイル名、module名、__init__.pyを確認します。";
  }
  return "最初に失敗したテスト名と行番号から読みます。";
}

export function extractFileCandidates(result: RunResult | null) {
  if (!result || result.exit_code === 0) return [];
  const output = `${result.stdout}\n${result.stderr}`;
  const candidates = output.match(/(?:steps|tests|src)\/[A-Za-z0-9_./-]+\.py/g) ?? [];
  return [...new Set(candidates)].slice(0, 8);
}

export function buildStepGuide(step: Step) {
  const workFile = primaryWorkFile(step);
  const categoryTips = writingTipsByCategory[step.category] ?? [
    "目的を1つ決めて、小さい単位で実装する",
    "動かした結果を見ながら修正する",
  ];
  const cautionTips = cautionTipsByCategory[step.category] ?? [];
  return {
    writing: [
      `開くファイルは ${workFile} だけ`,
      ...categoryTips,
      `最後に ${step.commands[0] ?? "pytest"} で確認する`,
    ],
    cautions: [...step.reviewPoints, ...cautionTips].slice(0, 5),
  };
}

export function primaryWorkFile(step: Step) {
  return step.files.find((file) => !file.toLowerCase().endsWith("readme.md")) ?? step.files[0] ?? "";
}

export function methodPrimerForStep(step: Step): MethodPrimer {
  return (
    methodPrimersByCategory[step.category] ?? {
      title: "最初に見ること",
      lead: "細かい説明より、入口ファイル、TODO、テスト結果の3つを順番に見ます。",
      items: ["画面上部: 目的を読む", "TODO: 1つだけ直す", "pytest: 結果で次を判断する"],
    }
  );
}

export function isRunnable(command: string) {
  return (
    command === "python --version" ||
    command === "ruff check ." ||
    command === "black --check ." ||
    command === "mypy src" ||
    command === "uv run lint" ||
    command === "uv run fmt" ||
    command === "uv run fmt --fix" ||
    command === "uv run build" ||
    command.startsWith("pytest ") ||
    command.startsWith("uv run pytest ")
  );
}

export function isTestCommand(command: string) {
  return command.startsWith("pytest ") || command.startsWith("uv run pytest ");
}
