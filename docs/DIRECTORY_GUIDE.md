# Directory Guide

各Stepは `steps/<step_id>/` の中で完結します。

| 場所 | 役割 |
| --- | --- |
| `README.md` | 目的、考え方、進め方 |
| `implementation/` | 自分が実装するファイル |
| `tests/` | そのStepの確認テスト |
| `solutions/` | 解答例。実ファイルがあるStepだけ置く |
| `references/` | Step内専用の補足資料がある時だけ置く。通常の参照URLは `docs/STEP_REFERENCES.md` / `docs/step_references.json` に集約 |

例:

| Step | 実装 | テスト |
| --- | --- | --- |
| `001_syntax` | `steps/001_syntax/implementation/exercises/basics/` | `steps/001_syntax/tests/` |
| `043_fastapi` | `steps/043_fastapi/implementation/exercises/fastapi_app/` | `steps/043_fastapi/tests/` |
| `134_capstone` | `steps/134_capstone/implementation/projects/ai_review_api/` | `steps/134_capstone/implementation/projects/ai_review_api/` |

基本の流れ:

```bash
cd steps/<step_id>
pytest tests -q
```

古い `exercises/` は互換用の入口だけ残しています。実体は `steps/<step_id>/implementation/` にあります。
