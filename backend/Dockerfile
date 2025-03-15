# uv がインストールされたイメージを取得
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# 作業ディレクトリを /app に設定
WORKDIR /app

# pyproject.toml をコピー
COPY pyproject.toml .

# entrypoint.sh をコピー
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh


# 依存関係をインストール
RUN uv sync

# アプリケーションのソースコードをコピー
COPY src ./src

# entrypoint.sh を実行
ENTRYPOINT ["/entrypoint.sh"]
