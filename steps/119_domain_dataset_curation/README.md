# 113 Domain Dataset Curation

## 学ぶこと

- 特化型AIはデータ品質が性能を決める
- 重複、空回答、偏りを取り除く
- train/eval/testを混ぜない

## 書くこと

- 重複例を除外する
- 空のquestion/answerを除外する
- deterministicにsplitする

## 参考URL

- https://developers.google.com/machine-learning/data-prep

```bash
pytest steps/119_domain_dataset_curation/tests -q
```

