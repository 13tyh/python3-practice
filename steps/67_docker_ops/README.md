# 67 Docker Ops

## 学ぶこと

- healthcheck、env、logs、compose profilesを運用目線で読む
- 起動できるだけでなく調査できるcomposeにする
- migrationやseedの実行タイミングを考える

## 書くこと

- 必須envの不足を検出する
- DB/AI依存を含むhealth状態を返す
- degradedとdownを区別する

## 注意点

- secretをhealth responseへ出さない
- healthcheckが重すぎると障害を増やす
- 本番と開発のprofile差分を明文化する

## 参考URL

- https://docs.docker.com/compose/compose-file/05-services/#healthcheck

```bash
pytest steps/67_docker_ops/tests -q
```

