# 22 Network API

目的: API を呼ぶコードを読める・書ける・危険な点を判断できるようにする。

## 見るポイント

- URL、method、headers、params、json body
- status code
- timeout
- retry してよい処理か
- API key をログに出していないか
- レスポンス JSON の形を信用しすぎていないか

## 課題

```bash
pytest steps/22_network_api/tests -q
```

`steps/22_network_api/implementation/exercises/network_api/01_http_basics.py` の TODO を埋める。


