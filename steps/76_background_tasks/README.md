# 76 Background Tasks

## 学ぶこと

- 非同期jobの状態を管理する
- pending/running/succeeded/failedを分ける
- idempotency keyで二重登録を防ぐ

## 書くこと

- jobを作る
- 次に実行するjobを選ぶ
- 完了状態へ更新する

## 参考URL

- https://fastapi.tiangolo.com/tutorial/background-tasks/

```bash
pytest exercise_tests/background_tasks -q
```
