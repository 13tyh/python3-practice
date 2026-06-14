# 81 Property Based Thinking

## 学ぶこと

- 具体例だけでなく性質でテストを考える
- 正規化、冪等性、順序安定を確認する
- AIのコードに抜けた不変条件を見つける

## 書くこと

- tagを正規化する
- 同じ処理を2回しても変わらないことを確認する
- 不変条件を関数で表す

## 参考URL

- https://hypothesis.readthedocs.io/en/latest/

```bash
pytest steps/029_property_based_thinking/tests -q
```

