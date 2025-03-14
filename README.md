# docker で FastAPI

```bash
# docker-compose で起動
docker compose up --build
# コンテナ(web)に入る
docker compose exec web bash
```

http://127.0.0.1:8000 にアクセスすると、APIドキュメントが表示されます。
また、http://127.0.0.1:8000/docs にアクセスすると、Swagger UIが表示されます。


# 開発用設定

## pre-commit

```bash
pre-commit install
pre-commit run --all-files
```

## commit_template

```bash
git config commit.template .commit_template
```
