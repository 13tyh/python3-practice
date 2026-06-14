# 99 Prompt Injection Defense

## 学ぶこと

- prompt injectionの典型文を疑う
- user入力とtrusted contextを分ける
- RAG contextを命令ではなく資料として扱う

## 書くこと

- 危険な命令文を検出する
- contextを引用ブロックとして包む
- injection疑いの理由を返す

## 参考URL

- https://owasp.org/www-project-top-10-for-large-language-model-applications/

```bash
pytest steps/105_prompt_injection_defense/tests -q
```

