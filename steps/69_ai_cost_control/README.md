# 69 AI Cost Control

## 学ぶこと

- token budget、model limit、出力上限を考える
- 高いmodelへ投げる前に入力量を見る
- deployment_nameとmodel_nameの対応を費用面でも判断する

## 書くこと

- おおまかなtoken数を見積もる
- 入力と出力がmodel limitに収まるか判定する
- prompt長から使うmodelを選ぶ

## 注意点

- 文字数とtoken数は完全一致しない
- 長文を全部AIに投げる前にchunk化を考える
- cost情報はログに残すがsecretは残さない

## 参考URL

- https://platform.openai.com/tokenizer

```bash
pytest steps/69_ai_cost_control/tests -q
```

