# Directory Guide

各Stepは `steps/<step_id>/` の中で完結します。

| 場所 | 役割 |
| --- | --- |
| `README.md` | 目的、考え方、進め方 |
| `implementation/` | 自分が実装するファイル |
| `tests/` | そのStepの確認テスト |
| `solutions/` | 解答例 |
| `references/` | 参考資料や悪い例 |

例:

| Step | 実装 | テスト |
| --- | --- | --- |
| `01_syntax` | `steps/01_syntax/implementation/exercises/basics/` | `steps/01_syntax/tests/` |
| `16_fastapi` | `steps/16_fastapi/implementation/exercises/fastapi_app/` | `steps/16_fastapi/tests/` |
| `58_capstone` | `steps/58_capstone/implementation/projects/ai_review_api/` | `steps/58_capstone/implementation/projects/ai_review_api/` |

基本の流れ:

```bash
cd steps/<step_id>
pytest tests -q
```

古い `exercises/` は互換用の入口だけ残しています。実体は `steps/<step_id>/implementation/` にあります。
