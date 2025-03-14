# nodejs のイメージをベースにする
FROM node:23-alpine

# 作業ディレクトリを /app に設定
WORKDIR /app

# 全てのファイルをコピー
COPY . .

# 依存関係をインストール
RUN npm install
# ビルド
RUN npm run build

# アプリケーションを起動
CMD ["npm", "start"]
