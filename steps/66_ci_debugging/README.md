# 66 CI Debugging

## 学ぶこと

- GitHub Actionsの失敗ログを読む
- pytestのFAILED行を拾う
- PRで落ちた時に最初に見る場所を決める

## 書くこと

- logから失敗stepを抽出する
- pytestのFAILED行を抽出する
- 失敗原因の候補を短くまとめる

## 注意点

- 最後のエラーだけ見て原因と決めつけない
- lint、format、testのどこで落ちたか分ける
- ローカルとCIのenv差分を疑う

## 参考URL

- https://docs.github.com/actions/monitoring-and-troubleshooting-workflows/using-workflow-run-logs

```bash
pytest steps/66_ci_debugging/tests -q
```

