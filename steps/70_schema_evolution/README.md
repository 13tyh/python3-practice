# 70 Schema Evolution

## 学ぶこと

- 既存データへ新しいfieldを足すmigrationを考える
- 再実行可能なbackfillを作る
- deploy順と互換性を判断する

## 書くこと

- fieldが欠けているdocを検出する
- update payloadを作る
- migration対象件数をsummaryにする

## 注意点

- 一度実行したmigrationが再実行で壊れないようにする
- APIが新旧schemaを一時的に読めるようにする
- 本番ではdry-runと件数確認を先に行う

## 参考URL

- https://www.mongodb.com/docs/manual/core/schema-validation/

```bash
pytest exercise_tests/schema_evolution -q
```
