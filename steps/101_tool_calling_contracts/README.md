# 101 Tool Calling Contracts

## 学ぶこと

- AIが呼べるtoolをallowlistで制限する
- tool名とargumentsを検証する
- 危険操作を自動実行しない

## 書くこと

- tool callの形を検証する
- allowed toolだけ許可する
- 必須argument不足を返す

## 参考URL

- https://docs.langchain.com/oss/python/langchain/tools

```bash
pytest steps/101_tool_calling_contracts/tests -q
```

