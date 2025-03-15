# docker compose で　Next.js + FastAPI の開発環境を構築

```bash
# docker-compose で起動
docker compose up
```

## その他のコマンド
```bash
# build もする場合
docker compose up --build

# キャッシュを使わずにビルド
docker compose build --no-cache

# コンテナに入る
docker compose exec fast-api bash
docker compose exec nextjs bash

# ログを確認
docker compose logs -f fast-api
docker compose logs -f nextjs
```

http://127.0.0.1:3000 にアクセスすると、Next.jsのページが表示されます。
http://127.0.0.1:8000 にアクセスすると、Swagger UIが表示されます。


# 開発用設定

## commit_template

```bash
git config commit.template .commit_template
```
