# docker で FastAPI

```bash
# docker file からイメージを作成
docker build -t mol-infer-learning .
# イメージからコンテナを作成
docker run --rm -p 8000:8000 mol-infer-learning
```

http://127.0.0.1:8000 にアクセスすると、APIドキュメントが表示されます。
また、http://127.0.0.1:8000/docs にアクセスすると、Swagger UIが表示されます。
