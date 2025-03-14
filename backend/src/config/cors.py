"""CORS configuration for FastAPI application."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def setup_cors(app: FastAPI) -> None:
    """Set up CORS middleware for the FastAPI application."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],  # フロントエンド（Next.js）からのリクエストを許可
        allow_credentials=True,
        allow_methods=["*"],  # すべての HTTP メソッド（GET, POST, PUT など）を許可
        allow_headers=["*"],  # すべての HTTP ヘッダーを許可
    )
