# 39 Docs PDF

目的: ドキュメントを分割し、PDF 化する処理を理解する。

## 見るポイント

- 分割単位: 見出し、文字数、ページ数
- ファイル名の安全化
- 出力ディレクトリ
- PDF のページ順
- 文字化け
- 元ファイルを上書きしないこと

## 実行

```bash
pytest exercise_tests/docs_pdf -q
```

## 使うライブラリ

- `reportlab`: テキストから PDF を作る
- `pypdf`: PDF の結合・分割
- `python-docx`: docx を読む時に使う

