# 117 Fine Tuning Dataset Prep

## 学ぶこと

- fine-tuningはRAGの代替ではなく、応答形式や判断パターンの固定に向く
- 学習データはinput/outputを安定させる
- eval用データを学習に混ぜない

## 書くこと

- chat形式のtraining recordを作る
- 必須roleを検証する
- JSONL行を作る

## 参考URL

- https://platform.openai.com/docs/guides/fine-tuning

```bash
pytest steps/117_finetuning_dataset_prep/tests -q
```

