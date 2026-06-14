# 62 API Pagination Deep

## 学ぶこと

- offset paginationとcursor paginationの違いを理解する
- `limit`、`after_id`、`next_cursor` を設計する
- 大量データでも壊れにくいAPI形を考える

## 書くこと

- cursor指定で次ページを返す
- limitを上限で丸める
- 最終ページでは `next_cursor=None` を返す

## 注意点

- 全件取得してから画面で絞る設計にしない
- cursorが存在しない時の挙動を決める
- sort順が安定していないcursorは危険

## 参考URL

- https://jsonapi.org/profiles/ethanresnick/cursor-pagination/

```bash
pytest steps/051_api_pagination_deep/tests -q
```

