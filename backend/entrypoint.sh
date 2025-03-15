#!/bin/sh
if [ "$ENV" = "development" ]; then
  echo "🚀 開発環境モードで起動中..."
else
  echo "🔒 本番環境モードで起動中..."
fi

# FastAPI のサーバーを起動
# exec を使うことで PID 1 が FastAPI のプロセスになる
exec uv run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
