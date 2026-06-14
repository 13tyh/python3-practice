# 61 Domain Modeling

## 学ぶこと

- dataclassで業務データを表す
- 自治体、契約、seat数のようなルールを関数に閉じ込める
- dictのまま処理する危険を理解する

## 書くこと

- 契約モデルを作る
- userを追加できるか判定する
- 自治体ごとのseat数を集計する

## 注意点

- 業務ルールをrouterやDB処理に散らさない
- `active=False` の契約を集計に混ぜない
- 境界値は `current_users == seats` を必ず見る

## 参考URL

- https://docs.python.org/3/library/dataclasses.html

```bash
pytest steps/037_domain_modeling/tests -q
```

