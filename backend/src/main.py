"""FastAPI application for file upload handling."""

from fastapi import FastAPI

from src.config.cors import setup_cors

from .routes import setup_routes

# アプリケーションの初期化
app = FastAPI(
    title="File Upload API",
    description="API for handling file uploads with FastAPI",
    version="1.0.0",
)

setup_cors(app)
setup_routes(app)
