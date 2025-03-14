# docker compose で　Next.js + FastAPI の開発環境を構築

```bash
# docker-compose で起動
docker compose up --build
# コンテナ(fastapi)に入る
docker compose exec fastapi bash
```

http://127.0.0.1:8000 にアクセスすると、APIドキュメントが表示されます。
また、http://127.0.0.1:8000/docs にアクセスすると、Swagger UIが表示されます。

# 開発用設定

## commit_template

```bash
git config commit.template .commit_template
```
