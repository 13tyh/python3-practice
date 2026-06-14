# 108 Model Fallback Routing

## 学ぶこと

- model fallbackの順番を決める
- retry可能な失敗だけfallbackする
- 安いmodelと強いmodelを使い分ける

## 書くこと

- taskからdeploymentを選ぶ
- 次のfallback候補を返す
- retry不可のエラーを止める

## 参考URL

- https://docs.langchain.com/oss/python/langchain/model_io

```bash
pytest steps/114_model_fallback_routing/tests -q
```

