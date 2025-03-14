# uv がインストールされたイメージを取得
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# 作業ディレクトリを /app に設定
WORKDIR /app

# pyproject.toml をコピー
COPY pyproject.toml .

# 依存関係をインストール
RUN uv sync

# アプリケーションのソースコードをコピー
COPY src ./src

# FastAPI サーバーを起動
CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
